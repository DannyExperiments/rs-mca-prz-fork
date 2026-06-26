#!/usr/bin/env python3
"""Compute generated-field/list and deep-point MCA entropy floors.

This is a lightweight planning calculator for the theorem package in
`experimental/experiments.tex`, Section "Generated-Field Entropy Floors and
Deep-Point MCA Conversion".

It uses log2 quantities, so it works for very large n without constructing
huge binomial coefficients.
"""
from __future__ import annotations

import argparse
import math


def log2_binom(n: int, a: int) -> float:
    if a < 0 or a > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(a + 1) - math.lgamma(n - a + 1)) / math.log(2)


def log2_add(x: float, y: float) -> float:
    if x == float("-inf"):
        return y
    if y == float("-inf"):
        return x
    m = max(x, y)
    return m + math.log2(2 ** (x - m) + 2 ** (y - m))


def log2_sub_one_from_power(log_x: float) -> float:
    """Return log2(2^log_x - 1), assuming log_x >= 0."""
    if log_x <= 0:
        return float("-inf")
    if log_x > 60:
        return log_x + math.log2(1 - 2 ** (-log_x))
    return math.log2(2 ** log_x - 1)


def mca_floor_log2(logL: float, log_q: float, log_q_minus_n: float, log_k: float) -> float:
    """log2( L(q-n) / ( q(q-n + k(L-1)) ) )."""
    if logL == float("-inf"):
        return float("-inf")
    log_L_minus_1 = log2_sub_one_from_power(max(0.0, logL)) if logL > 0 else float("-inf")
    log_k_L_minus_1 = log_k + log_L_minus_1 if log_L_minus_1 != float("-inf") else float("-inf")
    log_denom_inner = log2_add(log_q_minus_n, log_k_L_minus_1)
    return logL + log_q_minus_n - log_q - log_denom_inner


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--a", type=int, required=True, help="agreement level")
    ap.add_argument("--log2-qgen", type=float, required=True, help="log2 of generated/base field size")
    ap.add_argument("--log2-qline", type=float, required=True, help="log2 of line/slope field size")
    ap.add_argument("--log2-qminusn", type=float, default=None, help="log2(|F|-n); defaults to log2(|F|) when n is negligible")
    ap.add_argument("--quotient-c", type=int, default=None, help="optional quotient fiber size c with a divisible by c")
    args = ap.parse_args()

    n, k, a = args.n, args.k, args.a
    log_qgen = args.log2_qgen
    log_q = args.log2_qline
    log_q_minus_n = args.log2_qminusn if args.log2_qminusn is not None else log_q
    log_k = math.log2(k)

    sigma_base = a - k
    sigma_plus = a - k - 1
    log_bin = log2_binom(n, a)
    log_L_base = log_bin - sigma_base * log_qgen
    log_L_plus = log_bin - sigma_plus * log_qgen
    log_eps = mca_floor_log2(log_L_plus, log_q, log_q_minus_n, log_k)

    print(f"n={n} k={k} a={a}")
    print(f"log2 binom(n,a)              = {log_bin:.6f}")
    print(f"log2 L_ent base              = {log_L_base:.6f}")
    print(f"log2 L_ent plus              = {log_L_plus:.6f}")
    print(f"log2 MCA entropy floor       = {log_eps:.6f}")
    print(f"above 2^-128?                = {log_eps > -128}")

    if args.quotient_c is not None:
        c = args.quotient_c
        if n % c != 0 or a % c != 0:
            print("quotient floor unavailable: c does not divide n and a")
        else:
            N, m = n // c, a // c
            exp_base = m - math.ceil(k / c)
            exp_plus = m - math.ceil((k + 1) / c)
            log_bin_q = log2_binom(N, m)
            log_Lq_base = log_bin_q - exp_base * log_qgen if exp_base >= 0 else float("-inf")
            log_Lq_plus = log_bin_q - exp_plus * log_qgen if exp_plus >= 0 else float("-inf")
            log_eps_q = mca_floor_log2(log_Lq_plus, log_q, log_q_minus_n, log_k)
            print("\nquotient floor")
            print(f"c={c} N={N} m={m}")
            print(f"log2 binom(N,m)              = {log_bin_q:.6f}")
            print(f"exp_base=m-ceil(k/c)         = {exp_base}")
            print(f"exp_plus=m-ceil((k+1)/c)     = {exp_plus}")
            print(f"log2 L_quot base             = {log_Lq_base:.6f}")
            print(f"log2 L_quot plus             = {log_Lq_plus:.6f}")
            print(f"log2 MCA quotient floor      = {log_eps_q:.6f}")
            print(f"above 2^-128?                = {log_eps_q > -128}")


if __name__ == "__main__":
    main()
