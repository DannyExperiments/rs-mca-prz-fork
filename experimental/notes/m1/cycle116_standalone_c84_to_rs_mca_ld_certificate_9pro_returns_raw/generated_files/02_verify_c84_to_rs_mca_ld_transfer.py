#!/usr/bin/env python3
"""Deterministic finite-hypothesis verifier for the Cycle84 -> RS MCA/LD transfer.

This script uses only the supplied Cycle116 packet.  It verifies:
  * the existing Cycle84 occupancy certificate;
  * the explicit Cycle84 root/template data and all 336 slot locators;
  * the slot-to-product scalar identity and the common six-jet hypothesis;
  * the field/order facts for the smooth F_{17^32}, order-512 lift;
  * the exact parameter and 2^-128 arithmetic ledger.

The general fixed-jet locator-to-MCA lemma and the agreement-padding lemma are
mathematical lemmas, not finite computations; this script verifies every finite
hypothesis used when instantiating those lemmas.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

P = 17
N_BAD = 52_747_567_092
P_PACKET = 52_747_567_104


def order_mod(a: int, m: int) -> int:
    x = 1
    for d in range(1, m + 1):
        x = (x * a) % m
        if x == 1:
            return d
    raise AssertionError("order not found")


def v2(n: int) -> int:
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "packet_root",
        nargs="?",
        default="/mnt/data/cycle116_packet/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro",
    )
    args = parser.parse_args()
    root = Path(args.packet_root).resolve()
    finite = root / "context" / "cycle84_finite_certificate"
    model_path = finite / "model" / "cycle68_slot_factorization_checker.py"
    verifier_path = finite / "verify_certificate.py"
    assert model_path.is_file() and verifier_path.is_file(), root

    # Existing exact occupancy certificate.
    cp = subprocess.run(
        [sys.executable, str(verifier_path)],
        cwd=finite,
        check=True,
        text=True,
        capture_output=True,
    )
    occ = json.loads(cp.stdout)
    assert occ["decision"] == "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED"
    assert occ["exact_true_m_max"] == 2
    assert occ["exact_true_occupancy"] == N_BAD
    assert occ["exact_true_ordered_offdiagonal_energy"] == 24
    assert occ["true_double_fibers"] == 12

    spec = importlib.util.spec_from_file_location("cycle84_model", model_path)
    assert spec and spec.loader
    c = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(c)

    fmod = c.find_field_poly()
    eta = c.find_eta(fmod)
    beta = c.find_beta(fmod)
    assert fmod == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    assert c.irred16(fmod)
    assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
    assert beta == (2, 1)
    assert c.fpow(eta, 16, fmod) == c.emb(3)
    assert c.fpow(eta, 128, fmod) == c.emb(-1)
    assert c.fpow(eta, 256, fmod) == c.ONE
    assert c.fpow(beta, 256, fmod) != c.ONE  # beta not in D_0
    assert beta != c.ONE

    q0 = P**16
    q1 = P**32
    assert v2(q0 - 1) == 8
    assert order_mod(P, 256) == 16
    assert order_mod(P, 512) == 32
    assert c.fpow(eta, (q0 - 1) // 2, fmod) == c.emb(-1)  # eta nonsquare

    # Verify the three template factorizations h_i(Z)=prod_{e in E_i}(Z-3^e),
    # including the vanishing Z^7 and Z^6 coefficients responsible for the jet.
    for i, eset in c.E_SETS.items():
        h = c.ONE
        for e in sorted(eset):
            h = c.pmul(h, ((-pow(3, e, P)) % P, 1))
        assert h == c.P_COEFFS[i]
        assert len(h) == 9 and h[8] == 1 and h[7] == 0 and h[6] == 0

    def fadd(a, b):
        return c.padd(a, b)

    def fneg(a):
        return c.psub((), a)

    def fpoly_mul(A, B):
        out = [()] * (len(A) + len(B) - 1)
        for i, x in enumerate(A):
            for j, y in enumerate(B):
                out[i + j] = fadd(out[i + j], c.fmul(x, y, fmod))
        while len(out) > 1 and out[-1] == ():
            out.pop()
        return out

    def fpoly_eval(A, x):
        y = ()
        for coeff in reversed(A):
            y = fadd(c.fmul(y, x, fmod), coeff)
        return y

    u_table = c.build_u(fmod, eta, beta)
    eta_pows = [c.fpow(eta, e, fmod) for e in range(256)]

    # The 48 state sets are distinct; every slot block has 16 roots and locator
    # Y^16 + O(Y^10), hence no coefficients in degrees 15,...,11.
    bsets = {}
    for i in (1, 2, 3):
        for a in range(16):
            B = frozenset((a + e) % 16 for e in c.E_SETS[i])
            assert len(B) == 8
            assert B not in bsets
            bsets[B] = (i, a)
            assert sum(B) % 16 == (c.S_COLOR[i] + 8 * (a & 1)) % 16
    assert len(bsets) == 48

    slot_checks = 0
    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                B = frozenset((a + e) % 16 for e in c.E_SETS[i])
                exponents = sorted({(t + 8 * m) % 256 for b in B for m in (b, b + 16)})
                assert len(exponents) == 16
                assert all(e % 8 == t for e in exponents)

                locator = [c.ONE]
                for e in exponents:
                    locator = fpoly_mul(locator, [fneg(eta_pows[e]), c.ONE])
                assert len(locator) == 17 and locator[16] == c.ONE
                assert all(locator[d] == () for d in range(11, 16))

                slot_value = fpoly_eval(locator, beta)
                expected = c.fmul(c.emb(pow(3, t, P)), u_table[(t, i, a)], fmod)
                assert slot_value == expected
                assert u_table[(t, i, a)] != ()
                slot_checks += 1
    assert slot_checks == 336

    # Consequences checked symbolically from the preceding all-slot clauses:
    # seven slot locators give Y^112+O(Y^106); multiplying by (Y-1) gives
    # P_T(Y)=Y^113-Y^112+O(Y^107).  At beta the scalar is kappa=(beta-1)3^28.
    kappa = c.fmul(c.psub(beta, c.ONE), c.emb(pow(3, 28, P)), fmod)
    assert kappa != ()

    # Quadratic extension K=F0(theta), theta^2=eta.
    ZERO2 = ((), ())
    ONE2 = (c.ONE, ())
    THETA = ((), c.ONE)

    def qadd(x, y):
        return (fadd(x[0], y[0]), fadd(x[1], y[1]))

    def qmul(x, y):
        ac = c.fmul(x[0], y[0], fmod)
        bdeta = c.fmul(c.fmul(x[1], y[1], fmod), eta, fmod)
        adbc = fadd(c.fmul(x[0], y[1], fmod), c.fmul(x[1], y[0], fmod))
        return (fadd(ac, bdeta), adbc)

    def qpow(x, e):
        r, b = ONE2, x
        while e:
            if e & 1:
                r = qmul(r, b)
            b = qmul(b, b)
            e >>= 1
        return r

    assert qmul(THETA, THETA) == (eta, ())
    assert qpow(THETA, 256) == (c.emb(-1), ())
    assert qpow(THETA, 512) == ONE2
    H = [qpow(THETA, e) for e in range(512)]
    assert len(set(H)) == 512
    D0 = set(H[0::2])
    odd = H[1::2]
    assert len(D0) == 256 and len(set(odd)) == 256 and D0.isdisjoint(odd)
    A = set(odd[:119])
    R = set(odd[119:])
    assert len(A) == 119 and len(R) == 137 and A.isdisjoint(R)
    assert D0.isdisjoint(A) and D0.isdisjoint(R)
    assert len(D0 | A | R) == 512

    # Exact parameter and field ledger.
    n0, j0, sigma0, k0, a0 = 256, 113, 6, 137, 143
    assert k0 == n0 - j0 - sigma0 and a0 == k0 + sigma0 == n0 - j0
    h = 119
    n1, k1, a1 = 512, k0 + h, a0 + h
    assert (n1, k1, a1) == (512, 256, 262)
    assert 1 - a1 / n1 == 125 / 256
    assert q1 // 2**128 == 6
    assert N_BAD > q1 // 2**128
    assert N_BAD * 2**128 > q1

    result = {
        "decision": "C84_TO_RS_MCA_LD_TRANSFER_FINITE_HYPOTHESES_VERIFIED",
        "cycle84": {
            "m_max": 2,
            "occupancy": N_BAD,
            "packet_size": P_PACKET,
            "ordered_offdiagonal_energy": 24,
            "double_fibers": 12,
        },
        "bridge": {
            "slot_locator_checks": slot_checks,
            "fixed_jet": "P_T(Y)=Y^113-Y^112+O(Y^107)",
            "product_scalar": "P_T(beta)=(beta-1)*3^28*Phi(T)",
            "kappa_nonzero": True,
        },
        "native_row": {
            "field_size": q0,
            "n": n0,
            "k": k0,
            "agreement": a0,
            "delta": "113/256",
            "bad_slope_lower_bound": N_BAD,
        },
        "smooth_row": {
            "field_size": q1,
            "domain_order": 512,
            "n": n1,
            "k": k1,
            "agreement": a1,
            "delta": "125/256",
            "bad_slope_lower_bound": N_BAD,
            "floor_q_over_2^128": q1 // 2**128,
            "ratio_exceeds_2^-128": True,
        },
        "scope": "finite hypotheses only; general transfer lemmas are proved in the accompanying theorem note",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
