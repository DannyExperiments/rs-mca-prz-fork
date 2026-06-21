#!/usr/bin/env python3
r"""Toy verifier for Cycle101's DFT/line-incidence reformulation.

For small prime fields this constructs words with at least one active external
root and checks the exact finite identities used in Cycle101:

  theta active
    <=> exists S subset H with p_j(S) = P_j - theta^j for j <= sigma+1
    <=> for S' = H \ S, p_j(S') = theta^j - P_j for j <= sigma+1

The last equation is precisely the DFT/indicator spectral-window form because
p_j(S') = sum_{x in H} 1_{S'}(x) x^j.

The script also checks theta = p_1(S') + P_1 and the Cycle100/101 pairwise
distance lower bound on complement witnesses whenever a case has multiple
active roots. This is a finite algebra sanity check, not a proof of L2.
"""

from __future__ import annotations

from itertools import combinations
from math import log2
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


def sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return trim(out)


def mul(a: list[int], b: list[int], p: int) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] = (out[i + j] + av * bv) % p
    return trim(out)


def degree(poly: list[int]) -> int:
    return len(trim(poly[:])) - 1


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return trim(out)


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
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def subgroup(p: int, n: int) -> tuple[int, ...]:
    assert (p - 1) % n == 0
    g = primitive_root(p)
    h = pow(g, (p - 1) // n, p)
    return tuple(sorted({pow(h, i, p) for i in range(n)}))


def power_sums_from_monic(poly: list[int], length: int, p: int) -> list[int]:
    """Return root power sums p_1..p_length for a monic polynomial."""
    poly = trim(poly[:])
    d = degree(poly)
    assert poly[-1] == 1
    # a[i] is the coefficient of X^(d-i) in X^d+a1 X^(d-1)+...
    a = [0] + [poly[d - i] % p if d - i >= 0 else 0 for i in range(1, d + 1)]
    sums = [0] * (length + 1)
    for m in range(1, length + 1):
        total = 0
        for i in range(1, min(m, d) + 1):
            if i < m:
                total = (total + a[i] * sums[m - i]) % p
            else:
                total = (total + m * a[i]) % p
        sums[m] = (-total) % p
    return sums[1:]


def support_power_sum(points: tuple[int, ...], j: int, p: int) -> int:
    return sum(pow(x, j, p) for x in points) % p


def constructed_word(p: int, n: int, k: int, sigma: int, seed: int) -> tuple[tuple[int, ...], list[int]]:
    rng = Random(seed)
    H = subgroup(p, n)
    s = k + sigma
    S = tuple(sorted(rng.sample(list(H), s)))
    theta = rng.choice([x for x in range(p) if x not in set(H)])
    remainder = [rng.randrange(p) for _ in range(k)]
    U = add(mul([(-theta) % p, 1], locator(S, p), p), remainder, p)
    return H, U


def active_data(
    p: int, H: tuple[int, ...], U: list[int], k: int, sigma: int
) -> list[tuple[int, tuple[int, ...], tuple[int, ...]]]:
    H_set = set(H)
    s = k + sigma
    P = power_sums_from_monic(U, sigma + 1, p)
    hits: list[tuple[int, tuple[int, ...], tuple[int, ...]]] = []
    for theta in range(p):
        if theta in H_set:
            continue
        for S in combinations(H, s):
            ok = True
            for j in range(1, sigma + 2):
                if support_power_sum(S, j, p) != (P[j - 1] - pow(theta, j, p)) % p:
                    ok = False
                    break
            if ok:
                Sprime = tuple(x for x in H if x not in set(S))
                hits.append((theta, tuple(S), Sprime))
    return hits


def check_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | float | bool]:
    H, U = constructed_word(p, n, k, sigma, seed)
    H_set = set(H)
    P = power_sums_from_monic(U, sigma + 1, p)
    hits = active_data(p, H, U, k, sigma)
    assert hits
    for theta, S, Sprime in hits:
        assert theta not in H_set
        assert len(S) == k + sigma
        assert len(Sprime) == n - k - sigma
        assert (support_power_sum(Sprime, 1, p) + P[0]) % p == theta
        for j in range(1, sigma + 2):
            lhs = support_power_sum(Sprime, j, p)
            rhs = (pow(theta, j, p) - P[j - 1]) % p
            assert lhs == rhs

    min_dist = 10**9
    for i, (theta1, _S1, Sprime1) in enumerate(hits):
        A = set(Sprime1)
        for theta2, _S2, Sprime2 in hits[i + 1 :]:
            if theta1 == theta2:
                continue
            min_dist = min(min_dist, len(A.symmetric_difference(set(Sprime2))))
    if min_dist != 10**9:
        assert min_dist >= 2 * sigma + 2
    else:
        min_dist = -1

    main_exponent = n - sigma * log2(p)
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "seed": seed,
        "active_hits": len(hits),
        "distinct_theta": len({theta for theta, _S, _Sprime in hits}),
        "min_dist": min_dist,
        "main_exponent_n_minus_sigma_log2p": round(main_exponent, 6),
        "passed": True,
    }


def main() -> None:
    cases = []
    for seed in range(12):
        cases.append(check_case(17, 8, 2, 2, seed))
    for seed in range(8):
        cases.append(check_case(41, 8, 2, 3, seed))
    print("cycle101 dft-line incidence check")
    print(f"cases_checked: {len(cases)}")
    print(f"total_active_hits: {sum(int(c['active_hits']) for c in cases)}")
    print(f"max_distinct_theta: {max(int(c['distinct_theta']) for c in cases)}")
    print(f"cases_with_multiple_theta: {sum(1 for c in cases if int(c['distinct_theta']) > 1)}")
    for case in cases[:10]:
        print(case)
    print("PASS")


if __name__ == "__main__":
    main()
