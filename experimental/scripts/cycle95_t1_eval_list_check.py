#!/usr/bin/env python3
"""Finite sanity check for Cycle95's t=1 eval-list reduction.

This script is not a proof. It verifies on small fields that for
E = X - alpha, B = 1, and arbitrary anchor w, the bad slopes are exactly
{P(alpha) : deg P <= k and P agrees with w on at least k+sigma points}.
It also checks that the t=1 direction is noncontained on every witness support.
"""

from __future__ import annotations

from itertools import combinations, product
from random import Random


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] = (out[i + j] + av * bv) % p
    return trim(out)


def scale(a: list[int], c: int, p: int) -> list[int]:
    return trim([(c * x) % p for x in a])


def eval_poly(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def interpolate(points: list[tuple[int, int]], p: int) -> list[int]:
    out = [0]
    for i, (xi, yi) in enumerate(points):
        num = [1]
        den = 1
        for j, (xj, _) in enumerate(points):
            if i == j:
                continue
            num = mul(num, [(-xj) % p, 1], p)
            den = den * ((xi - xj) % p) % p
        out = add(out, scale(num, yi * pow(den, -1, p), p), p)
    return trim(out)


def all_polys_deg_le(k: int, p: int):
    for coeffs in product(range(p), repeat=k + 1):
        yield trim(list(coeffs))


def noncontained_t1(support: tuple[int, ...], alpha: int, k: int, p: int) -> bool:
    target = [(-pow((x - alpha) % p, -1, p)) % p for x in support]
    for coeffs in product(range(p), repeat=k):
        g = trim(list(coeffs))
        if all(eval_poly(g, x, p) == y for x, y in zip(support, target)):
            return False
    return True


def scan_case(p: int, n: int, k: int, sigma: int, alpha: int, seed: int) -> dict:
    domain = list(range(n))
    assert alpha not in domain
    rng = Random(seed)
    w = [rng.randrange(p) for _ in domain]
    s = k + sigma

    bad_slopes = set()
    supports_checked = 0
    for support in combinations(domain, s):
        q_poly = interpolate([(x, w[x]) for x in support], p)
        if len(q_poly) - 1 <= k:
            supports_checked += 1
            assert noncontained_t1(support, alpha, k, p)
            bad_slopes.add(eval_poly(q_poly, alpha, p))

    list_polys = []
    eval_slopes = set()
    for poly in all_polys_deg_le(k, p):
        agreement = sum(1 for x in domain if eval_poly(poly, x, p) == w[x])
        if agreement >= s:
            list_polys.append(tuple(poly))
            eval_slopes.add(eval_poly(poly, alpha, p))

    assert bad_slopes == eval_slopes, (bad_slopes, eval_slopes)
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "alpha": alpha,
        "seed": seed,
        "bad_slope_count": len(bad_slopes),
        "list_size": len(list_polys),
        "supports_checked": supports_checked,
        "eval_collisions": len(list_polys) - len(eval_slopes),
        "passed": True,
    }


def main() -> None:
    cases = [
        (11, 7, 2, 2, 9, range(30)),
        (13, 8, 2, 2, 11, range(30)),
        (17, 8, 3, 2, 13, range(10)),
    ]
    reports = []
    for p, n, k, sigma, alpha, seeds in cases:
        for seed in seeds:
            reports.append(scan_case(p, n, k, sigma, alpha, seed))
    print("cycle95 t=1 eval-list sanity check")
    print(f"cases_checked: {len(reports)}")
    print(f"total_bad_slopes_seen: {sum(r['bad_slope_count'] for r in reports)}")
    print(f"total_list_polys_seen: {sum(r['list_size'] for r in reports)}")
    for item in reports[:6]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
