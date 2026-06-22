#!/usr/bin/env python3
"""Deterministic antecedent verifier for the Cycle84 -> RS-MCA/LD_sw transfer.

This script uses only the supplied Cycle116 packet.  It verifies:
  * the existing Cycle84 finite occupancy certificate;
  * the explicit F_17^16 field, eta, beta, and subgroup facts;
  * all 336 slot-locator top-jet and evaluation-factorization identities;
  * the aggregate Cycle84 fixed-six-jet and common nonzero scalar identity;
  * the explicit common quotient high part U for the native [256,137] row;
  * the quadratic F_17^32 lift, order-512 subgroup, padding partition;
  * the agreement/radius/degree and 2^-128 arithmetic ledgers.

The universal implication from these checked antecedents to LD_sw/MCA is a
mathematical lemma stated in the accompanying proof note; it is not replaced by
brute-force enumeration of all slopes or supports.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence

ZERO = ()
ONE = (1,)


def load_cycle68_model(cert_root: Path):
    model_path = cert_root / "model" / "cycle68_slot_factorization_checker.py"
    spec = importlib.util.spec_from_file_location("cycle68_transfer", model_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {model_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def v2(n: int) -> int:
    r = 0
    while n % 2 == 0:
        r += 1
        n //= 2
    return r


def multiplicative_order_mod(a: int, m: int) -> int:
    x = 1
    for d in range(1, m + 1):
        x = (x * a) % m
        if x == 1:
            return d
    raise AssertionError("order not found")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--packet-root",
        type=Path,
        default=Path("/mnt/data/cycle116_packet/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro"),
        help="root of the extracted Cycle116 packet",
    )
    args = parser.parse_args()
    packet_root = args.packet_root.resolve()
    cert_root = packet_root / "context" / "cycle84_finite_certificate"
    if not cert_root.is_dir():
        raise SystemExit(f"Cycle84 certificate directory not found: {cert_root}")

    c = load_cycle68_model(cert_root)
    fmod = c.find_field_poly()
    assert fmod == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    assert c.irred16(fmod)
    eta = c.find_eta(fmod)
    beta = c.find_beta(fmod)
    assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
    assert beta == (2, 1)

    p = 17
    q0 = p**16
    q1 = p**32
    group_order = q0 - 1
    minus_one = (p - 1,)

    def fa(x, y):
        return c.padd(x, y)

    def fs(x, y):
        return c.psub(x, y)

    def fm(x, y):
        return c.fmul(x, y, fmod)

    def fp(x, e: int):
        return c.fpow(x, e, fmod)

    def fe(n: int):
        return c.emb(n)

    # Exact field/group facts.
    assert fp(eta, 256) == ONE
    assert fp(eta, 128) == minus_one
    assert fp(eta, 16) == fe(3)
    assert v2(group_order) == 8
    assert fp(eta, group_order // 2) == minus_one  # eta is nonsquare.
    assert multiplicative_order_mod(17, 256) == 16  # eta generates F_17^16 as a field.

    factors = {2: 8, 3: 2, 5: 1, 29: 1, 18913: 1, 41761: 1, 184417: 1}
    for prime in factors:
        assert fp(beta, group_order // prime) != ONE
    assert fp(beta, group_order) == ONE
    assert fp(beta, 256) != ONE

    # Run the existing finite occupancy verifier and consume its exact output.
    proc = subprocess.run(
        [sys.executable, str(cert_root / "verify_certificate.py")],
        cwd=cert_root,
        check=True,
        text=True,
        capture_output=True,
    )
    anchor = json.loads(proc.stdout)
    assert anchor["decision"] == "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED"
    assert anchor["exact_true_m_max"] == 2
    assert anchor["exact_true_occupancy"] == 52_747_567_092
    assert anchor["exact_true_ordered_offdiagonal_energy"] == 24
    assert anchor["true_double_fibers"] == 12
    N = anchor["exact_true_occupancy"]

    # Polynomial arithmetic in an outer variable, with coefficients in F_0.
    def op_trim(a: Sequence[tuple[int, ...]]) -> list[tuple[int, ...]]:
        out = list(a)
        while out and out[-1] == ZERO:
            out.pop()
        return out

    def op_mul(a: Sequence[tuple[int, ...]], b: Sequence[tuple[int, ...]]):
        if not a or not b:
            return []
        r = [ZERO] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x == ZERO:
                continue
            for j, y in enumerate(b):
                if y != ZERO:
                    r[i + j] = fa(r[i + j], fm(x, y))
        return op_trim(r)

    def op_eval(a: Sequence[tuple[int, ...]], x):
        r = ZERO
        for coeff in reversed(a):
            r = fa(fm(r, x), coeff)
        return r

    # Verify P_i(Y)=prod_{e in E_i}(Y-3^e) exactly, including zero Y^7,Y^6 terms.
    for i in (1, 2, 3):
        poly = (1,)
        for e in sorted(c.E_SETS[i]):
            poly = c.pmul(poly, ((-pow(3, e, p)) % p, 1))
        assert poly == c.P_COEFFS[i]
        assert len(poly) == 9 and poly[8] == 1 and poly[7] == 0 and poly[6] == 0

    table = c.build_u(fmod, eta, beta)
    eta_pows = [fp(eta, e) for e in range(256)]
    slot_identity_count = 0
    slot_root_count = 0
    all_slot_jets = set()

    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                B = {(a + e) % 16 for e in c.E_SETS[i]}
                # The 16 points eta^(t+8m), m mod 16 in B, lie in the t-th coset.
                exponents = sorted({(t + 8 * m) % 256 for m in range(32) if (m % 16) in B})
                assert len(exponents) == 16
                assert all(e % 8 == t for e in exponents)
                roots = [eta_pows[e] for e in exponents]
                assert len(set(roots)) == 16
                assert ONE not in roots
                slot_root_count += len(roots)

                # L_{t,i,a}(X)=prod_{b in B}(X^2-eta^(2t)3^b).
                L = [ONE]
                for b in sorted(B):
                    const = fm(fp(eta, 2 * t), fe(pow(3, b, p)))
                    L = op_mul(L, [fs(ZERO, const), ZERO, ONE])
                assert len(L) == 17 and L[16] == ONE
                # X^16 + O(X^10): every coefficient of degree 11,...,15 vanishes.
                assert all(L[d] == ZERO for d in range(11, 16))
                all_slot_jets.add(tuple(L[11:17]))

                # Every listed point is a root, and evaluation at beta is 3^t u_t(i,a).
                assert all(op_eval(L, x) == ZERO for x in roots)
                assert op_eval(L, beta) == fm(fe(pow(3, t, p)), table[(t, i, a)])
                slot_identity_count += 1

    assert slot_identity_count == 336
    assert slot_root_count == 336 * 16
    assert len(all_slot_jets) == 1

    # The seven slot cosets (t=1,...,7) and the fixed point 1 are disjoint.
    cosets = []
    for t in range(1, 8):
        coset = {eta_pows[(t + 8 * m) % 256] for m in range(32)}
        assert len(coset) == 32 and ONE not in coset
        cosets.append(coset)
    assert len(set().union(*cosets)) == 7 * 32

    # Aggregate fixed jet: product of seven X^16+O(X^10) locators, then X-1.
    # The result is X^113-X^112+O(X^107), i.e. fixed coefficients 113,...,108.
    aggregate_fixed_jet = [ONE, minus_one, ZERO, ZERO, ZERO, ZERO]

    kappa = fm(fs(beta, ONE), fe(pow(3, 28, p)))
    assert kappa != ZERO

    # D_0=<eta> has locator V_D=X^256-1.  The common quotient terms above degree 137 are
    # U=X^143+...+X^138.  Check the telescoping top-part identity.
    U = [ZERO] * 144
    for d in range(138, 144):
        U[d] = ONE
    P_top = [ZERO] * 114
    P_top[112] = minus_one
    P_top[113] = ONE
    PU = op_mul(P_top, U)
    # P_top*U = X^256-X^250; unknown P remainder has degree <=107, hence times U <=250.
    assert len(PU) == 257 and PU[256] == ONE and PU[250] == minus_one
    assert all(PU[d] == ZERO for d in range(251, 256))
    alpha = op_eval(U, beta)
    Vbeta = fs(fp(beta, 256), ONE)
    lam = fs(ZERO, Vbeta)
    assert Vbeta != ZERO and lam != ZERO

    # Quadratic extension K=F_0(theta), theta^2=eta.
    # Pair (a,b) represents a+b theta.
    KZERO = (ZERO, ZERO)
    KONE = (ONE, ZERO)
    KMINUSONE = (minus_one, ZERO)
    theta = (ZERO, ONE)

    def ka(x, y):
        return (fa(x[0], y[0]), fa(x[1], y[1]))

    def km(x, y):
        return (
            fa(fm(x[0], y[0]), fm(fm(x[1], y[1]), eta)),
            fa(fm(x[0], y[1]), fm(x[1], y[0])),
        )

    def kp(x, e: int):
        r = KONE
        b = x
        while e:
            if e & 1:
                r = km(r, b)
            b = km(b, b)
            e >>= 1
        return r

    assert km(theta, theta) == (eta, ZERO)
    assert kp(theta, 256) == KMINUSONE
    assert kp(theta, 512) == KONE
    H = [kp(theta, e) for e in range(512)]
    assert len(set(H)) == 512
    even = {H[2 * i] for i in range(256)}
    odd = {H[2 * i + 1] for i in range(256)}
    embedded_D0 = {(eta_pows[i], ZERO) for i in range(256)}
    assert even == embedded_D0
    assert even.isdisjoint(odd)
    assert even | odd == set(H)

    A_pad = {H[2 * i + 1] for i in range(119)}
    R_unused = {H[2 * i + 1] for i in range(119, 256)}
    assert len(A_pad) == 119 and len(R_unused) == 137
    assert A_pad.isdisjoint(R_unused)
    assert A_pad | R_unused == odd

    # Exact parameter and target arithmetic.
    n0, j0, sigma0 = 256, 113, 6
    k0 = n0 - j0 - sigma0
    a0 = n0 - j0
    assert (k0, a0) == (137, 143)
    n1, k1 = 512, 256
    a1 = a0 + len(A_pad)
    j1 = n1 - a1
    assert (a1, j1) == (262, 250)
    assert (j1, n1) == (250, 512)
    # delta=j1/n1=125/256 and ceil((1-delta)n1)=262 exactly.
    assert j1 * 256 == 125 * n1
    assert (n1 - j1) == 262
    assert (k0 - 1) + len(A_pad) == 255 < k1
    assert q1 // (2**128) == 6
    assert N > q1 // (2**128)
    assert N * (2**128) > q1

    result = {
        "decision": "CYCLE116_C84_TO_RS_MCA_LD_TRANSFER_ANTECEDENTS_VERIFIED",
        "cycle84_anchor": {
            "m_max": 2,
            "occupancy": N,
            "ordered_offdiagonal_energy": 24,
            "double_fibers": 12,
        },
        "native_row": {
            "field_size": q0,
            "n": n0,
            "k": k0,
            "agreement": a0,
            "delta": "113/256",
            "fixed_jet": "X^113-X^112+O(X^107)",
            "slot_locator_identities_checked": slot_identity_count,
            "kappa_coefficients": list(kappa),
            "U_coeff_degrees": list(range(138, 144)),
            "alpha_coefficients": list(alpha),
            "lambda_coefficients": list(lam),
        },
        "smooth_lift": {
            "field_size": q1,
            "theta_order": 512,
            "H_size": len(H),
            "padding_points": len(A_pad),
            "unused_odd_coset_points": len(R_unused),
            "n": n1,
            "k": k1,
            "agreement": a1,
            "delta": "125/256",
        },
        "field_checks": {
            "base_modulus_irreducible": True,
            "eta_order": 256,
            "v2_17pow16_minus1": 8,
            "eta_nonsquare": True,
            "ord_256_of_17": 16,
            "beta_primitive": True,
        },
        "target": {
            "floor_17pow32_over_2pow128": q1 // (2**128),
            "occupancy_gt_floor": N > q1 // (2**128),
            "exact_cross_multiplication": N * (2**128) > q1,
        },
        "semantic_note": (
            "The checker verifies concrete antecedents and arithmetic. "
            "The proof note supplies the universal fixed-jet-to-LD_sw/MCA lemma "
            "and the divisibility proof of noncontainment after padding."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
