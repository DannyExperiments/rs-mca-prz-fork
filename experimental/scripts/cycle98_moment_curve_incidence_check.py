#!/usr/bin/env python3
"""Toy verifier for Cycle98's B1 moment-curve incidence reduction.

For small prime fields with a multiplicative subgroup H, this checks that
external bandwidth-1 roots theta are exactly the intersection

    v(F_p \\ H) cap (P - M_s),

where v(theta)=(theta,...,theta^m), P is the power-sum prefix of U, and M_s is
the power-sum image of s-subsets of H. This is a finite sanity check only.
"""

from __future__ import annotations

from itertools import combinations
from random import Random


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] = (out[i + j] + av * bv) % p
    return trim(out)


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return trim(out)


def prefix_from_monic(poly: list[int], count: int, p: int) -> tuple[int, ...]:
    degree = len(poly) - 1
    assert poly[-1] == 1
    vals: list[int] = []
    for j in range(1, count + 1):
        coeff = poly[degree - j] if degree - j >= 0 else 0
        vals.append(((-1) ** j * coeff) % p)
    return tuple(vals)


def power_sums_from_elementaries(elems: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Newton identities for p_j from elementary e_1,...,e_m."""
    powers: list[int] = []
    for m in range(1, len(elems) + 1):
        total = 0
        for i in range(1, m):
            total = (total + ((-1) ** (i - 1)) * elems[i - 1] * powers[m - i - 1]) % p
        total = (total + ((-1) ** (m - 1)) * m * elems[m - 1]) % p
        powers.append(total % p)
    return tuple(powers)


def subset_power_sums(points: tuple[int, ...], count: int, p: int) -> tuple[int, ...]:
    return tuple(sum(pow(x, j, p) for x in points) % p for j in range(1, count + 1))


def theta_prefix(c: tuple[int, ...], theta: int, p: int) -> tuple[int, ...]:
    c0 = (1,) + c
    out: list[int] = []
    for j in range(1, len(c) + 1):
        total = 0
        for i in range(j + 1):
            total = (total + pow((-theta) % p, j - i, p) * c0[i]) % p
        out.append(total)
    return tuple(out)


def primitive_root(p: int) -> int:
    factors: set[int] = set()
    x = p - 1
    d = 2
    while d * d <= x:
        if x % d == 0:
            factors.add(d)
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        factors.add(x)
    for g in range(2, p):
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise ValueError(f"no primitive root found for {p}")


def subgroup(p: int, n: int) -> tuple[int, ...]:
    assert (p - 1) % n == 0
    g = primitive_root(p)
    h = pow(g, (p - 1) // n, p)
    return tuple(sorted({pow(h, i, p) for i in range(n)}))


def monic_degree_poly(degree: int, p: int, rng: Random) -> list[int]:
    return [rng.randrange(p) for _ in range(degree)] + [1]


def scan_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | bool]:
    rng = Random(seed)
    H = subgroup(p, n)
    s = k + sigma
    degree = s + 1
    count = sigma + 1
    U = monic_degree_poly(degree, p, rng)
    c = prefix_from_monic(U, count, p)
    P = power_sums_from_elementaries(c, p)

    direct_pairs: set[tuple[int, tuple[int, ...]]] = set()
    incidence_pairs: set[tuple[int, tuple[int, ...]]] = set()
    prefix_theta: set[int] = set()
    incidence_theta: set[int] = set()

    for theta in range(p):
        if theta in H:
            continue
        target_prefix = theta_prefix(c, theta, p)
        target_powers = tuple((P[j - 1] - pow(theta, j, p)) % p for j in range(1, count + 1))
        for S in combinations(H, s):
            Ls = locator(S, p)
            pair = (theta, tuple(S))
            if prefix_from_monic(Ls, count, p) == target_prefix:
                direct_pairs.add(pair)
                prefix_theta.add(theta)
                assert theta == (c[0] - prefix_from_monic(Ls, 1, p)[0]) % p
            if subset_power_sums(tuple(S), count, p) == target_powers:
                incidence_pairs.add(pair)
                incidence_theta.add(theta)

    assert direct_pairs == incidence_pairs, (direct_pairs - incidence_pairs, incidence_pairs - direct_pairs)
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": s,
        "seed": seed,
        "external_theta": len(prefix_theta),
        "external_pairs": len(direct_pairs),
        "passed": True,
    }


def main() -> None:
    cases = [
        (17, 8, 2, 2, range(20)),
        (41, 8, 2, 3, range(12)),
        (37, 12, 3, 2, range(8)),
    ]
    reports = []
    for p, n, k, sigma, seeds in cases:
        for seed in seeds:
            reports.append(scan_case(p, n, k, sigma, seed))
    print("cycle98 moment-curve incidence check")
    print(f"cases_checked: {len(reports)}")
    print(f"total_external_theta: {sum(int(r['external_theta']) for r in reports)}")
    print(f"total_external_pairs: {sum(int(r['external_pairs']) for r in reports)}")
    for item in reports[:8]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
