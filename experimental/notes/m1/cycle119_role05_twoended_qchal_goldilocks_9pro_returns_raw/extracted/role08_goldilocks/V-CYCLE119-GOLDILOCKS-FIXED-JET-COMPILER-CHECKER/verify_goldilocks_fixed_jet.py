#!/usr/bin/env python3
"""Deterministic arithmetic/structural checker for the Cycle119 Goldilocks theorem.

The main L(q) theorem uses a proved collision-averaging lemma and is existential
in beta.  This checker verifies every finite arithmetic antecedent of that lemma
and the fixed-jet parameter ledger.  It also directly constructs and checks a
fully explicit beta=0 packet of 64 distinct slopes and their degree-<256
explaining polynomials on 264-point supports.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable, List

Q = 2**64 - 2**32 + 1
PROTH_A = 7
EXPECTED_THETA = 1_803_076_106_186_727_246
EXPECTED_M = 1_777_090_076_065_542_336
EXPECTED_COLLISION_CAP = 20_543_782_425_128_147_188
EXPECTED_L = 73_674_899_375_228_060
CYCLE116_N = 52_747_567_092


class CheckFailure(RuntimeError):
    pass


def require(condition: bool, code: str, detail: str = "") -> None:
    if not condition:
        raise CheckFailure(f"{code}: {detail}" if detail else code)


def ceil_div(a: int, b: int) -> int:
    require(b > 0, "NONPOSITIVE_DIVISOR")
    return -(-a // b)


def poly_mul(a: List[int], b: List[int], mod: int) -> List[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % mod
    return out


def poly_eval(coeffs: Iterable[int], x: int, mod: int) -> int:
    acc = 0
    for c in reversed(list(coeffs)):
        acc = (acc * x + c) % mod
    return acc


def verify_proth_primality() -> dict:
    n = 32
    k = 2**32 - 1
    require(Q == k * 2**n + 1, "PROTH_FORM_MISMATCH")
    require(k % 2 == 1, "PROTH_K_NOT_ODD")
    require(0 < k < 2**n, "PROTH_SIZE_CONDITION_FAILED")
    residue = pow(PROTH_A, (Q - 1) // 2, Q)
    require(residue == Q - 1, "PROTH_RESIDUE_FAILED", str(residue))
    # Proth criterion proof is recorded in STANDALONE_CERTIFICATE.md.
    return {"k": k, "n": n, "witness": PROTH_A, "residue": residue}


def verify_domain() -> dict:
    theta = pow(PROTH_A, (Q - 1) // 512, Q)
    require(theta == EXPECTED_THETA, "THETA_CONSTANT_MISMATCH", str(theta))
    require(pow(theta, 256, Q) == Q - 1, "THETA_256_NOT_MINUS_ONE")
    require(pow(theta, 512, Q) == 1, "THETA_512_NOT_ONE")
    H = [pow(theta, i, Q) for i in range(512)]
    require(len(set(H)) == 512, "H_NOT_ORDER_512")
    G_values = [pow(x, 8, Q) for x in H]
    counts = Counter(G_values)
    require(len(counts) == 64, "H8_IMAGE_NOT_64")
    require(set(counts.values()) == {8}, "H8_FIBERS_NOT_ALL_8")
    gamma = pow(theta, 8, Q)
    G = [pow(gamma, i, Q) for i in range(64)]
    require(set(G) == set(counts), "G_GENERATOR_IMAGE_MISMATCH")
    require(pow(gamma, 32, Q) == Q - 1, "GAMMA_32_NOT_MINUS_ONE")
    require(pow(gamma, 64, Q) == 1, "GAMMA_64_NOT_ONE")
    return {"theta": theta, "gamma": gamma, "H": H, "G": G}


def verify_averaging_ledger() -> dict:
    n = 512
    k = 256
    fiber = 8
    subset_size = 31
    j = fiber * subset_size
    sigma = 8
    r = j + sigma
    agreement = n - j
    difference_degree = fiber * (subset_size - 1)
    require(j == 248, "J_LEDGER_FAILED")
    require(sigma == 8, "SIGMA_LEDGER_FAILED")
    require(r == 256 and k == n - r, "DIMENSION_LEDGER_FAILED")
    require(agreement == 264, "AGREEMENT_LEDGER_FAILED")
    require(difference_degree == j - sigma == 240, "FIXED_JET_DEGREE_FAILED")
    require(j + 1 <= r, "NONCONTAINMENT_VANDERMONDE_FAILED")

    M = math.comb(64, 31)
    require(M == EXPECTED_M, "M_MISMATCH", str(M))
    pair_count = math.comb(M, 2)
    beta_count = Q - n
    collision_cap = (difference_degree * pair_count) // beta_count
    require(collision_cap == EXPECTED_COLLISION_CAP,
            "COLLISION_CAP_MISMATCH", str(collision_cap))
    L = ceil_div(M * M, M + 2 * collision_cap)
    require(L == EXPECTED_L, "L_MISMATCH", str(L))
    require(L > CYCLE116_N, "CYCLE116_NUMERATOR_NOT_PRESERVED")
    require(251 * L > Q, "ONE_OVER_251_COMPARISON_FAILED")
    require((2**128) * L > Q, "TWO_TO_MINUS_128_COMPARISON_FAILED")
    require(agreement >= 263, "STRICT_BALL_AGREEMENT_FAILED")
    require(n - agreement == 248 and 248 < 250, "STRICT_DISTANCE_FAILED")
    return {
        "n": n,
        "k": k,
        "j": j,
        "sigma": sigma,
        "r": r,
        "agreement": agreement,
        "difference_degree": difference_degree,
        "M": M,
        "pair_count": pair_count,
        "beta_candidates": beta_count,
        "collision_cap": collision_cap,
        "L": L,
    }


def verify_explicit_beta_zero_packet(domain: dict) -> dict:
    """Check a concrete 64-slope subpacket at beta=0.

    A_s={s,s+1,...,s+30} in Z/64.  Translation changes the exponent sum by
    31s, hence all 64 locator values/slopes are distinct.  For each s, construct
    the exact degree-<256 polynomial
        c_s(X)=(X^264+z_s-P_{S_s}(X))/X,
    P_{S_s}(X)=prod_{b notin A_s}(X^8-gamma^b),
    and check agreement with u_z(X)=X^263+z X^{-1} on all 264 support points.
    """
    theta = domain["theta"]
    gamma = domain["gamma"]
    H = domain["H"]
    G = domain["G"]
    G_index = {v: i for i, v in enumerate(G)}
    require(len(G_index) == 64, "G_INDEX_COLLISION")

    base = set(range(31))
    base_sum = sum(base) % 64
    slopes = []
    support_receipts = []

    for s in range(64):
        A_exp = {(i + s) % 64 for i in base}
        require(len(A_exp) == 31, "TRANSLATED_A_SIZE_FAILED")
        sum_exp = sum(A_exp) % 64
        require(sum_exp == (base_sum + 31 * s) % 64,
                "TRANSLATION_SUM_IDENTITY_FAILED")
        # P_A(0)=(-1)^31 prod_{a in A} gamma^a = -gamma^sum.
        P_A_zero = (-pow(gamma, sum_exp, Q)) % Q
        z = (-pow(P_A_zero, -1, Q)) % Q
        require(z == pow(gamma, (-sum_exp) % 64, Q),
                "BETA_ZERO_SLOPE_FORMULA_FAILED")
        slopes.append(z)

        J = [x for x in H if G_index[pow(x, 8, Q)] in A_exp]
        S = [x for x in H if G_index[pow(x, 8, Q)] not in A_exp]
        require(len(J) == 248 and len(S) == 264, "EXPLICIT_SUPPORT_SIZE_FAILED")

        # Q_S(Y)=prod_{b notin A}(Y-gamma^b), degree 33.
        qS = [1]
        for e in sorted(set(range(64)) - A_exp):
            qS = poly_mul(qS, [(-pow(gamma, e, Q)) % Q, 1], Q)
        require(len(qS) == 34 and qS[-1] == 1, "QS_MONIC_DEGREE_33_FAILED")
        require(qS[0] == z, "QS_CONSTANT_NOT_SLOPE")

        # c(X) has coefficient -qS[d] at X^(8d-1), d=1..32.
        c = [0] * 256
        for d in range(1, 33):
            c[8 * d - 1] = (-qS[d]) % Q
        require(len(c) == 256 and c[-1] == (-qS[32]) % Q,
                "CODEWORD_DEGREE_BOUND_FAILED")

        for x in S:
            u = (pow(x, 263, Q) + z * pow(x, -1, Q)) % Q
            cv = poly_eval(c, x, Q)
            require(cv == u, "EXPLICIT_AGREEMENT_FAILED", f"s={s}")

        # Noncontainment is the root-count certificate:
        # if h deg<256 agreed with x^-1 on 264 points, Xh-1 (deg<=256)
        # would have 264 roots but nonzero constant -1.
        require(len(S) > 256, "EXPLICIT_NONCONTAINMENT_MARGIN_FAILED")
        support_receipts.append({"s": s, "z": z, "J_size": len(J), "S_size": len(S)})

    require(len(set(slopes)) == 64, "EXPLICIT_SLOPES_NOT_DISTINCT")
    return {
        "beta": 0,
        "line": "u_z(x)=x^263+z*x^(-1)",
        "distinct_slopes": len(set(slopes)),
        "slopes": slopes,
        "supports": support_receipts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--self-test-tamper", action="store_true")
    args = parser.parse_args()

    try:
        proth = verify_proth_primality()
        domain = verify_domain()
        averaging = verify_averaging_ledger()
        explicit = verify_explicit_beta_zero_packet(domain)
        if args.self_test_tamper:
            require(averaging["L"] == EXPECTED_L + 1, "SELF_TEST_TAMPER_REJECTED")

        receipt = {
            "schema": "cycle119.goldilocks_fixed_jet_compiler.v1",
            "status": "VERIFIED",
            "scope": "FINITE_SOURCE_SCOPED_LD_SW_AND_MCA_ONLY",
            "field": {
                "q": Q,
                "prime_proof": "PROTH_WITNESS_7",
                "proth": proth,
            },
            "domain": {
                "theta": domain["theta"],
                "theta_256": pow(domain["theta"], 256, Q),
                "theta_512": pow(domain["theta"], 512, Q),
                "order": 512,
                "H8_image_size": 64,
                "H8_fiber_size": 8,
            },
            "row": {
                "n": averaging["n"],
                "k": averaging["k"],
                "agreement": averaging["agreement"],
                "distance_upper_bound": 248,
                "strict_target_distance": 250,
            },
            "fixed_jet": {
                "j": averaging["j"],
                "sigma": averaging["sigma"],
                "difference_degree": averaging["difference_degree"],
                "family_size": averaging["M"],
            },
            "main_numerator": {
                "mode": "EXISTENTIAL_BETA_BY_COLLISION_AVERAGING",
                "beta_is_explicit": False,
                "collision_cap": averaging["collision_cap"],
                "distinct_slopes_lower_bound": averaging["L"],
                "cycle116_numerator_preserved": averaging["L"] > CYCLE116_N,
            },
            "explicit_subpacket": {
                "mode": "BETA_ZERO_CONSTRUCTIVE",
                "beta": 0,
                "line": explicit["line"],
                "distinct_slopes": explicit["distinct_slopes"],
                "agreement": 264,
            },
            "field_ledger": {
                "q_gen": Q,
                "q_code": Q,
                "q_line": Q,
                "q_chal": None,
                "denominator": "q_line",
            },
            "threshold": {
                "L": averaging["L"],
                "251L_minus_q": 251 * averaging["L"] - Q,
                "two128L_minus_q": (2**128) * averaging["L"] - Q,
                "greater_than_2^-128": True,
            },
            "official_status": "OFFICIAL_ROW_EVENT_CHALLENGE_CONTRACT_PENDING",
            "terminal": "CYCLE119_GOLDILOCKS_FIXED_JET_COMPILER_VERIFIED_EXISTENTIAL_BETA",
        }
        if args.receipt:
            args.receipt.parent.mkdir(parents=True, exist_ok=True)
            args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        print("GOLDILOCKS_PRIME_PROTH_VERIFIED")
        print("ORDER_512_DOMAIN_VERIFIED")
        print("MU8_FIBER_FIXED_JET_FAMILY_VERIFIED")
        print(f"AVERAGE_SPECIALIZATION_NUMERATOR={averaging['L']}")
        print("AGREEMENT_264_VERIFIED")
        print("STRICT_BALL_263_SURVIVES")
        print("EXPLICIT_BETA_ZERO_64_SLOPE_PACKET_VERIFIED")
        print("q_gen=q_code=q_line=18446744069414584321")
        print("q_chal=null")
        print("OFFICIAL_CONTRACT_PENDING")
        print("CYCLE119_GOLDILOCKS_FIXED_JET_COMPILER_VERIFIED_EXISTENTIAL_BETA")
        return 0
    except CheckFailure as exc:
        print(f"CHECK_FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
