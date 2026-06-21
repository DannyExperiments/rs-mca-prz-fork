#!/usr/bin/env python3
"""Exact arithmetic check for the Cycle91 extension-field power-of-two row.

This verifies only the finite integer/2-adic claims used in the audit. It does
not construct the finite field or enumerate subset sums.
"""

from math import comb, log2


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out


def multiplicative_order(a: int, mod: int) -> int:
    if a % mod == 0:
        raise ValueError("a must be a unit modulo mod")
    x = a % mod
    k = 1
    while x != 1:
        x = (x * a) % mod
        k += 1
        if k > mod:
            raise RuntimeError("order search failed")
    return k


def h2_num_den(num: int, den: int) -> float:
    rho = num / den
    return -(rho * log2(rho) + (1 - rho) * log2(1 - rho))


def main() -> None:
    p = 5
    d = 64
    q = p**d
    n = 256
    rho_num, rho_den = 1, 16
    k = n * rho_num // rho_den
    ell = k + 1
    support_count = comb(n, ell)
    threshold = q // 2**128
    single_weight_count = comb(d, ell) * 2**ell
    parity_sum_count = sum(
        comb(d, w) * 2**w
        for w in range(ell + 1)
        if (w - ell) % 2 == 0
    )
    quotient_profile_bits = log2(comb(127, 8))
    entropy = h2_num_den(rho_num, rho_den)
    tau_star_leading = entropy / log2(q)
    gap = 1 / n

    checks = {
        "p": p,
        "d": d,
        "q": q,
        "n": n,
        "k": k,
        "ell": ell,
        "v2_q_minus_1": v2(q - 1),
        "ord_256_5": multiplicative_order(5, 256),
        "floor_q_over_2_128": threshold,
        "binom_256_17": support_count,
        "single_weight_count": single_weight_count,
        "parity_sum_count": parity_sum_count,
        "single_weight_margin": single_weight_count - threshold,
        "parity_sum_margin": parity_sum_count - threshold,
        "log2_q": log2(q),
        "log2_threshold": log2(threshold),
        "log2_binom_256_17": log2(support_count),
        "exact_binomial_reserve_margin_bits": log2(q) - log2(support_count),
        "log2_single_weight_count": log2(single_weight_count),
        "log2_parity_sum_count": log2(parity_sum_count),
        "mca_margin_bits_single_weight": log2(q) - log2(single_weight_count),
        "mca_margin_bits_parity_sum": log2(q) - log2(parity_sum_count),
        "quotient_profile_bits_M2": quotient_profile_bits,
        "h2_1_16": entropy,
        "tau_star_leading": tau_star_leading,
        "gap": gap,
        "gap_over_tau_star_leading": gap / tau_star_leading,
    }

    assert checks["v2_q_minus_1"] == 8
    assert checks["ord_256_5"] == 64
    assert single_weight_count > threshold
    assert parity_sum_count > threshold
    assert q > support_count
    assert gap > tau_star_leading

    for key, value in checks.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
