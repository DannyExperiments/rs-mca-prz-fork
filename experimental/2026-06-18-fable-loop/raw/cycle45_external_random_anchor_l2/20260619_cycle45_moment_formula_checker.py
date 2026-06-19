#!/usr/bin/env python3
"""Exact combinatorial checker for the Cycle 45 random-anchor moment bounds.

This does not enumerate field anchors. It evaluates the exact Johnson-distance
second-moment formula implied by the proved pair-rank law.
"""
from __future__ import annotations

import argparse
import math
from fractions import Fraction


def exact_moments(p: int, t: int, j: int) -> dict[str, object]:
    if not (0 <= j <= p):
        raise ValueError("need 0 <= j <= p")
    a = p - j
    if not (1 <= t <= a):
        raise ValueError("need 1 <= t <= p-j")
    q = p * p
    N = math.comb(p, j)
    lam = Fraction(N, q**t)
    second = Fraction(0, 1)
    near_weight = Fraction(0, 1)
    for r in range(min(j, a) + 1):
        K = math.comb(j, r) * math.comb(a, r)
        second += Fraction(N * K, q ** (t + min(t, r)))
        near_weight += Fraction(K, q**r)
    variance = second - lam * lam
    term = 1.0
    cstar = term
    for r in range(1, 100):
        term *= 0.25 / (r * r)
        cstar += term
    return {
        "p": p,
        "q_line": q,
        "t": t,
        "j": j,
        "a": a,
        "N_subsets": N,
        "lambda_float": float(lam),
        "lambda_over_q_line": float(lam / q),
        "E_nu2_float": float(second),
        "Var_nu_float": float(variance),
        "Cstar": cstar,
        "variance_bound_float": cstar * float(lam),
        "near_weight_float": float(near_weight),
        "variance_bound_pass_using_Cstar_lt_2": variance <= 2 * lam,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("p", type=int)
    parser.add_argument("t", type=int)
    parser.add_argument("j", type=int)
    args = parser.parse_args()
    out = exact_moments(args.p, args.t, args.j)
    for key, value in out.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
