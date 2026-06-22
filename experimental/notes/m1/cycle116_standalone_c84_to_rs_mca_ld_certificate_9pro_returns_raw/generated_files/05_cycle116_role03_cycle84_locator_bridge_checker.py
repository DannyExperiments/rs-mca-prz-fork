#!/usr/bin/env python3
"""Deterministic Cycle84-to-locator bridge verifier.

Usage:
  python3 cycle116_role03_cycle84_locator_bridge_checker.py \
      /path/to/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro

This checker does not rerun the 52.7-billion-entry census. It imports the
already-emitted finite occupancy result and checks the exact algebraic clauses
needed to identify that census with evaluations of the 113-point Cycle84
co-support locators. It also checks one explicit smooth [512,256] fixed-root
lift.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Iterable, Sequence

P = 17
Q0 = P**16
N0 = Q0 - 1
PRIME_FACTORS_N0 = (2, 3, 5, 29, 18913, 41761, 184417)
ZERO = ()
ONE = (1,)


def load_model(cert_root: Path):
    model_path = cert_root / "model" / "cycle68_slot_factorization_checker.py"
    spec = importlib.util.spec_from_file_location("cycle68_model", model_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {model_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def int_poly_mul(a: Sequence[int], b: Sequence[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    while out and out[-1] == 0:
        out.pop()
    return out


def poly_trim(a: Sequence[tuple[int, ...]]) -> list[tuple[int, ...]]:
    out = list(a)
    while out and out[-1] == ZERO:
        out.pop()
    return out


def poly_mul(c, f, a, b):
    if not a or not b:
        return []
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == ZERO:
            continue
        for j, y in enumerate(b):
            if y != ZERO:
                out[i + j] = c.padd(out[i + j], c.fmul(x, y, f))
    return poly_trim(out)


def poly_mul_linear(c, f, a, root):
    return poly_mul(c, f, a, [c.psub(ZERO, root), ONE])


def poly_eval(c, f, a, x):
    out = ZERO
    for coeff in reversed(a):
        out = c.padd(c.fmul(out, x, f), coeff)
    return out


def poly_divmod_monic(c, f, a, b):
    aa = list(a)
    bb = poly_trim(b)
    assert bb and bb[-1] == ONE
    q = [ZERO] * max(1, len(aa) - len(bb) + 1)
    while aa and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        lead = aa[-1]
        q[d] = lead
        for i, coeff in enumerate(bb):
            aa[d + i] = c.psub(aa[d + i], c.fmul(lead, coeff, f))
        aa = poly_trim(aa)
    return poly_trim(q), poly_trim(aa)


def fcoeff(x: tuple[int, ...], degree: int = 16) -> list[int]:
    return list(x) + [0] * (degree - len(x))


# K = F0(theta), theta^2 = eta. K-elements are pairs (a,b), meaning a+b theta.
def k_add(c, x, y):
    return (c.padd(x[0], y[0]), c.padd(x[1], y[1]))


def k_sub(c, x, y):
    return (c.psub(x[0], y[0]), c.psub(x[1], y[1]))


def k_mul(c, f, eta, x, y):
    ac = c.fmul(x[0], y[0], f)
    bdeta = c.fmul(c.fmul(x[1], y[1], f), eta, f)
    adbc = c.padd(c.fmul(x[0], y[1], f), c.fmul(x[1], y[0], f))
    return (c.padd(ac, bdeta), adbc)


def k_pow(c, f, eta, x, e: int):
    out = (ONE, ZERO)
    base = x
    while e:
        if e & 1:
            out = k_mul(c, f, eta, out, base)
        base = k_mul(c, f, eta, base, base)
        e >>= 1
    return out


def k_poly_trim(a):
    z = (ZERO, ZERO)
    out = list(a)
    while out and out[-1] == z:
        out.pop()
    return out


def k_poly_mul_linear(c, f, eta, a, root):
    z = (ZERO, ZERO)
    o = (ONE, ZERO)
    out = [z] * (len(a) + 1)
    negroot = k_sub(c, z, root)
    for i, coeff in enumerate(a):
        out[i] = k_add(c, out[i], k_mul(c, f, eta, coeff, negroot))
        out[i + 1] = k_add(c, out[i + 1], coeff)
    return k_poly_trim(out)


def k_poly_mul(c, f, eta, a, b):
    z = (ZERO, ZERO)
    if not a or not b:
        return []
    out = [z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == z:
            continue
        for j, y in enumerate(b):
            if y != z:
                out[i + j] = k_add(c, out[i + j], k_mul(c, f, eta, x, y))
    return k_poly_trim(out)


def k_poly_divmod_monic(c, f, eta, a, b):
    z = (ZERO, ZERO)
    o = (ONE, ZERO)
    aa = list(a)
    bb = k_poly_trim(b)
    assert bb and bb[-1] == o
    q = [z] * max(1, len(aa) - len(bb) + 1)
    while aa and len(aa) >= len(bb):
        d = len(aa) - len(bb)
        lead = aa[-1]
        q[d] = lead
        for i, coeff in enumerate(bb):
            aa[d + i] = k_sub(c, aa[d + i], k_mul(c, f, eta, lead, coeff))
        aa = k_poly_trim(aa)
    return k_poly_trim(q), k_poly_trim(aa)


def k_poly_eval(c, f, eta, a, x):
    z = (ZERO, ZERO)
    out = z
    for coeff in reversed(a):
        out = k_add(c, k_mul(c, f, eta, out, x), coeff)
    return out


def encode_k(x):
    return {"a": fcoeff(x[0]), "b": fcoeff(x[1])}


def multiplicative_order_mod(a: int, m: int) -> int:
    x = 1
    for d in range(1, 10_000):
        x = (x * a) % m
        if x == 1:
            return d
    raise RuntimeError("order search failed")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if not __debug__:
        raise SystemExit("run this verifier without Python -O; its checks use assert")
    ap = argparse.ArgumentParser()
    ap.add_argument("packet_root", type=Path)
    args = ap.parse_args()
    root = args.packet_root.resolve()
    cert_root = root / "context" / "cycle84_finite_certificate"
    if not cert_root.is_dir():
        raise SystemExit(f"not a packet root: {root}")

    c = load_model(cert_root)
    f = (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    eta = (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
    beta = (2, 1)
    three = (3,)
    minus_one = (16,)

    # Field and distinguished elements.
    assert c.irred16(f)
    assert c.find_field_poly() == f
    assert c.find_eta(f) == eta
    assert c.find_beta(f) == beta
    assert c.fpow(eta, 256, f) == ONE
    assert c.fpow(eta, 128, f) != ONE
    assert c.fpow(eta, 16, f) == three
    assert c.fpow(beta, 256, f) != ONE
    assert all(c.fpow(beta, N0 // p, f) != ONE for p in PRIME_FACTORS_N0)

    D0 = [c.fpow(eta, m, f) for m in range(256)]
    H32 = [c.fpow(eta, 8 * m, f) for m in range(32)]
    assert len(set(D0)) == 256
    assert len(set(H32)) == 32
    assert set(H32).issubset(set(D0))

    # Base degree-eight templates and shifted 8-sets.
    for i, E in c.E_SETS.items():
        formal = [1]
        for e in sorted(E):
            formal = int_poly_mul(formal, [(-pow(3, e, P)) % P, 1])
        assert tuple(formal) == c.P_COEFFS[i]
        assert formal[7] == 0 and formal[6] == 0

    slot_log_path = cert_root / "data" / "slot_logs.json"
    slot_data = json.loads(slot_log_path.read_text())
    records = {(r["t"], r["i"], r["a"]): r for r in slot_data["records"]}
    assert len(records) == 336
    assert slot_data["generator"] == [2, 1]
    assert slot_data["N"] == N0

    def bset(i: int, a: int):
        return frozenset((a + e) % 16 for e in c.E_SETS[i])

    all_bsets = {}
    for i in (1, 2, 3):
        for a in range(16):
            B = bset(i, a)
            assert len(B) == 8
            assert sum(B) % 16 == (c.S_COLOR[i] + 8 * (a & 1)) % 16
            assert B not in all_bsets
            all_bsets[B] = (i, a)
    assert len(all_bsets) == 48

    def lift(i: int, a: int):
        targets = {(pow(3, b, P),) for b in bset(i, a)}
        ys = tuple(y for y in H32 if c.fpow(y, 2, f) in targets)
        assert len(ys) == 16
        counts = {target: 0 for target in targets}
        for y in ys:
            counts[c.fpow(y, 2, f)] += 1
        assert set(counts.values()) == {2}
        return ys

    lifts = {(i, a): lift(i, a) for i in (1, 2, 3) for a in range(16)}
    assert len(set(lifts.values())) == 48

    block_roots = {}
    block_polys = {}
    slot_values = {}
    for t in range(1, 8):
        et = c.fpow(eta, t, f)
        coset = {c.fmul(et, y, f) for y in H32}
        assert len(coset) == 32
        assert coset.isdisjoint(set(H32))
        per_t_sets = set()
        for i in (1, 2, 3):
            for a in range(16):
                roots = tuple(c.fmul(et, y, f) for y in lifts[(i, a)])
                assert len(set(roots)) == 16
                assert set(roots).issubset(coset)
                assert frozenset(roots) not in per_t_sets
                per_t_sets.add(frozenset(roots))

                poly = [ONE]
                for root_elem in roots:
                    poly = poly_mul_linear(c, f, poly, root_elem)
                assert len(poly) == 17 and poly[16] == ONE
                # X^15,...,X^11 vanish: evenness kills odd terms; the two
                # zero template coefficients kill X^14 and X^12.
                assert all(poly[d] == ZERO for d in range(11, 16))

                value = poly_eval(c, f, poly, beta)
                rec = records[(t, i, a)]
                assert rec["color"] == (c.S_COLOR[i] + 8 * (a & 1)) % 16
                u_cert = c.fpow(beta, int(rec["log"]), f)
                assert value == c.fmul(c.fpow(three, t, f), u_cert, f)

                block_roots[(t, i, a)] = roots
                block_polys[(t, i, a)] = poly
                slot_values[(t, i, a)] = u_cert
        assert len(per_t_sets) == 48

    # Distinct t=0,...,7 cosets partition D0.
    cosets = []
    for t in range(8):
        et = c.fpow(eta, t, f)
        cosets.append({c.fmul(et, y, f) for y in H32})
    assert all(cosets[i].isdisjoint(cosets[j]) for i in range(8) for j in range(i))
    assert set().union(*cosets) == set(D0)

    def tuple_support(choices):
        roots = [ONE]
        for t, (i, a) in enumerate(choices, 1):
            roots.extend(block_roots[(t, i, a)])
        assert len(roots) == len(set(roots)) == 113
        return tuple(roots)

    def tuple_phi(choices):
        out = ONE
        for t, (i, a) in enumerate(choices, 1):
            out = c.fmul(out, slot_values[(t, i, a)], f)
        return out

    def locator(roots):
        out = [ONE]
        for x in roots:
            out = poly_mul_linear(c, f, out, x)
        return out

    # Representative verifies the common six-jet and the native complement jet.
    choices0 = [(1, 0)] * 7
    roots0 = tuple_support(choices0)
    P0_poly = locator(roots0)
    assert len(P0_poly) == 114
    assert P0_poly[113] == ONE
    assert P0_poly[112] == minus_one
    assert all(P0_poly[d] == ZERO for d in range(108, 112))
    assert max((d for d, coeff in enumerate(P0_poly) if coeff != ZERO and d < 112), default=-1) <= 107

    x256_minus_1 = [ZERO] * 257
    x256_minus_1[0] = minus_one
    x256_minus_1[256] = ONE
    Ls0, rem = poly_divmod_monic(c, f, x256_minus_1, P0_poly)
    assert rem == [] and len(Ls0) == 144
    native_U = [ZERO] * 144
    for d in range(138, 144):
        native_U[d] = ONE
    assert all(Ls0[d] == native_U[d] for d in range(138, 144))
    # The variable part starts at degree <= k=137.

    # Exact common scalar linking locator evaluations to the certified Phi table.
    kappa = c.fmul(c.psub(beta, ONE), c.fpow(three, 28, f), f)
    assert c.fpow(three, 28, f) == (4,)
    assert kappa == (4, 4) and kappa != ZERO

    def check_tuple(choices):
        roots = tuple_support(choices)
        Ppoly = locator(roots)
        p_beta = poly_eval(c, f, Ppoly, beta)
        phi = tuple_phi(choices)
        assert p_beta == c.fmul(kappa, phi, f)
        return roots, phi, p_beta

    # Check the explicit certified double fiber end-to-end.
    witness_a = [(1, 4), (2, 10), (3, 14), (1, 12), (3, 0), (2, 6), (3, 8)]
    witness_b = [(2, 0), (2, 11), (1, 7), (1, 1), (3, 9), (2, 8), (1, 14)]
    roots_a, phi_a, p_beta_a = check_tuple(witness_a)
    roots_b, phi_b, p_beta_b = check_tuple(witness_b)
    assert roots_a != roots_b
    assert phi_a == phi_b and p_beta_a == p_beta_b

    master = json.loads((cert_root / "cycle84_master_proof_certificate.json").read_text())
    light = json.loads((cert_root / "output" / "light_verification.out").read_text())
    fresh = json.loads((cert_root / "output" / "fresh_full_certificate.json").read_text())
    OCC = 52_747_567_092
    assert master["distinct_products"] == OCC
    assert master["m_max"] == 2
    assert master["D_offdiagonal_ordered"] == 24
    assert master["fiber_histogram"] == {
        "multiplicity_1": 52_747_567_080,
        "multiplicity_2": 12,
        "multiplicity_ge_3": 0,
    }
    assert light["exact_true_occupancy"] == OCC
    assert fresh["distinct_products"] == OCC

    # Smooth fixed-root lift K/F0 with theta^2=eta.
    assert c.fpow(eta, (Q0 - 1) // 2, f) == minus_one
    kz = (ZERO, ZERO)
    ko = (ONE, ZERO)
    theta = (ZERO, ONE)
    eta_k = (eta, ZERO)
    beta_k = (beta, ZERO)
    assert k_mul(c, f, eta, theta, theta) == eta_k
    assert k_pow(c, f, eta, theta, 512) == ko
    assert k_pow(c, f, eta, theta, 256) != ko
    H512 = [k_pow(c, f, eta, theta, m) for m in range(512)]
    assert len(set(H512)) == 512
    D0_k = {(x, ZERO) for x in D0}
    assert {H512[2 * m] for m in range(256)} == D0_k
    assert beta_k not in set(H512)

    # Canonical 137-point fixed set in the odd half: R={theta^(2m+1):0<=m<137}.
    R = tuple(H512[2 * m + 1] for m in range(137))
    assert len(set(R)) == 137
    assert set(R).isdisjoint(D0_k)

    P_R = [ko]
    for r in R:
        P_R = k_poly_mul_linear(c, f, eta, P_R, r)
    assert len(P_R) == 138 and P_R[-1] == ko
    PR_beta = k_poly_eval(c, f, eta, P_R, beta_k)
    assert PR_beta != kz

    P0_k = [(coeff, ZERO) for coeff in P0_poly]
    Pplus0 = k_poly_mul(c, f, eta, P_R, P0_k)
    assert len(Pplus0) == 251 and Pplus0[-1] == ko
    # Fixed-jet preservation: deg P_R + 107 = 244 = 250-6.
    assert 137 + 107 == 250 - 6

    x512_minus_1 = [kz] * 513
    x512_minus_1[0] = (minus_one, ZERO)
    x512_minus_1[512] = ko
    Lplus0, krem = k_poly_divmod_monic(c, f, eta, x512_minus_1, Pplus0)
    assert krem == [] and len(Lplus0) == 263
    lifted_U_top = Lplus0[257:263]
    assert len(lifted_U_top) == 6 and lifted_U_top[-1] == ko

    # Evaluation-spectrum preservation and nonzero reciprocal coefficient.
    lifted_kappa = k_mul(c, f, eta, PR_beta, (kappa, ZERO))
    assert lifted_kappa != kz
    assert k_pow(c, f, eta, beta_k, 512) != ko

    # q-ledger checks.
    assert multiplicative_order_mod(17, 256) == 16
    assert multiplicative_order_mod(17, 512) == 32
    q1 = 17**32
    target = q1 // 2**128
    assert target == 6
    assert OCC > target
    assert OCC * 2**128 > q1

    result = {
        "decision": "CYCLE116_ROLE03_C84_LOCATOR_BRIDGE_VERIFIED",
        "packet_root": str(root),
        "imported_finite_certificate": {
            "m_max": 2,
            "occupancy": OCC,
            "ordered_offdiagonal_energy": 24,
            "double_fibers": 12,
            "fibers_ge_3": 0,
            "slot_logs_sha256": sha256(slot_log_path),
        },
        "native_cycle84": {
            "field_size": Q0,
            "eta_order": 256,
            "eta_power_16": fcoeff(c.fpow(eta, 16, f)),
            "beta_power_256_is_one": False,
            "domain_size": 256,
            "cosupport_size": 113,
            "common_top_coefficients_degrees_113_to_108": [
                fcoeff(P0_poly[d]) for d in range(113, 107, -1)
            ],
            "remainder_degree_bound": 107,
            "sigma": 6,
            "k": 137,
            "agreement": 143,
            "kappa_coefficients": fcoeff(kappa),
            "product_to_locator_all_336_local_checks": True,
            "tuple_to_cosupport_injective": True,
            "distinct_locator_values": OCC,
            "native_common_support_locator_high_part": {
                "degrees": [143, 142, 141, 140, 139, 138],
                "coefficients": [fcoeff(ONE)] * 6,
            },
        },
        "smooth_lift": {
            "field_size": q1,
            "eta_nonsquare": True,
            "theta_order": 512,
            "domain_size": 512,
            "fixed_root_set": "R={theta^(2m+1): 0<=m<137}",
            "fixed_root_count": 137,
            "cosupport_size": 250,
            "sigma": 6,
            "k": 256,
            "agreement": 262,
            "delta": "125/256",
            "lifted_kappa": encode_k(lifted_kappa),
            "lifted_common_support_locator_top_six": [encode_k(x) for x in reversed(lifted_U_top)],
            "distinct_locator_values": OCC,
        },
        "field_ledger": {
            "q_gen": q1,
            "q_code": q1,
            "q_line": q1,
            "q_chal": None,
            "floor_q_line_over_2_pow_128": target,
            "occupancy_gt_target": True,
            "epsilon_lower_bound_gt_2_pow_minus_128": True,
        },
        "scope": (
            "Checks the Cycle84 locator bridge and one smooth finite RS-MCA/LD_sw lift; "
            "does not prove ordinary list decoding, protocol soundness failure, asymptotics, "
            "or official prize admissibility."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
