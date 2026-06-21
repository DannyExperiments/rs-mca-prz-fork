#!/usr/bin/env python3
"""Toy verifier for the Cycle94 anchored secant-intersection lemma.

This is a finite-field sanity check, not a proof. It enumerates exact support
locators for small arbitrary-anchor residue data and verifies that distinct
bad slopes have witnesses whose pairwise support intersection is at most
``k + t - 1``.
"""

from __future__ import annotations

from itertools import combinations
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


def divmod_poly(a: list[int], b: list[int], p: int) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, (len(a) - len(b) + 1))
    inv_lc = pow(b[-1], -1, p)
    while len(a) >= len(b) and a != [0]:
        coeff = a[-1] * inv_lc % p
        shift = len(a) - len(b)
        q[shift] = coeff
        for i, bv in enumerate(b):
            a[shift + i] = (a[shift + i] - coeff * bv) % p
        trim(a)
    return trim(q), trim(a)


def mod_poly(a: list[int], modulus: list[int], p: int) -> list[int]:
    return divmod_poly(a, modulus, p)[1]


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


def scalar_multiple(qmod: list[int], bmod: list[int], p: int) -> int | None:
    qmod = qmod + [0] * (len(bmod) - len(qmod))
    bmod = bmod + [0] * (len(qmod) - len(bmod))
    z = None
    for q, b in zip(qmod, bmod):
        if b == 0:
            if q != 0:
                return None
            continue
        candidate = q * pow(b, -1, p) % p
        if z is None:
            z = candidate
        elif z != candidate:
            return None
    return z


def scan_case(p: int, n: int, k: int, sigma: int, e_poly: list[int], b_poly: list[int], seed: int) -> dict:
    rng = Random(seed)
    domain = list(range(n))
    t = len(trim(e_poly[:])) - 1
    assert all(eval_poly(e_poly, x, p) != 0 for x in domain)
    assert 0 < len(trim(b_poly[:])) <= t
    a = k + sigma
    bmod = mod_poly(b_poly, e_poly, p)
    witness_by_slope: dict[int, list[tuple[int, ...]]] = {}
    w = [rng.randrange(p) for _ in domain]
    for support in combinations(domain, a):
        q_poly = interpolate([(x, w[x]) for x in support], p)
        if len(q_poly) - 1 >= k + t:
            continue
        z = scalar_multiple(mod_poly(q_poly, e_poly, p), bmod, p)
        if z is not None:
            witness_by_slope.setdefault(z, []).append(tuple(support))

    max_intersection = 0
    worst = None
    slopes = sorted(witness_by_slope)
    for i, z in enumerate(slopes):
        for zp in slopes[i + 1 :]:
            for s in witness_by_slope[z]:
                for sp in witness_by_slope[zp]:
                    inter = len(set(s) & set(sp))
                    if inter > max_intersection:
                        max_intersection = inter
                        worst = (z, zp, s, sp)
    bound = k + t - 1
    assert max_intersection <= bound, (max_intersection, bound, worst)
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "t": t,
        "seed": seed,
        "bad_slope_count": len(slopes),
        "witness_count": sum(len(v) for v in witness_by_slope.values()),
        "max_intersection_distinct_slopes": max_intersection,
        "bound": bound,
        "passed": True,
    }


def main() -> None:
    cases = [
        # E = X - alpha, alpha outside the domain.
        (17, 9, 3, 2, [5, 1], [1], range(20)),
        # E = (X-10)(X-11) over F_19, no roots on domain 0..8.
        (19, 9, 3, 2, [110 % 19, (-21) % 19, 1], [3, 1], range(20)),
    ]
    reports = []
    for p, n, k, sigma, e_poly, b_poly, seeds in cases:
        for seed in seeds:
            reports.append(scan_case(p, n, k, sigma, e_poly, b_poly, seed))
    total_slopes = sum(item["bad_slope_count"] for item in reports)
    print("cycle94 anchored secant toy check")
    print(f"cases_checked: {len(reports)}")
    print(f"total_bad_slopes_seen: {total_slopes}")
    for item in reports[:6]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
