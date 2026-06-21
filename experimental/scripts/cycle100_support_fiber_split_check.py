#!/usr/bin/env python3
"""Toy verifier for Cycle100's support-vs-fiber split.

For small prime fields this computes the active external-root fibers F(theta)
directly and checks:

  N = sum_theta F(theta)
  support = #{theta : F(theta)>0}
  F_max = max_theta F(theta)
  max(support, F_max) <= N <= support * F_max

It also verifies the PTE min-distance lemma for every nontrivial fiber:
distinct supports in one fiber differ in at least 2(sigma+2) elements.
This is a finite sanity check only.
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
        if all(pow(g, (p - 1) // r, p) != 1 for r in factors):
            return g
    raise ValueError(f"no primitive root for {p}")


def subgroup(p: int, n: int) -> tuple[int, ...]:
    assert (p - 1) % n == 0
    g = primitive_root(p)
    h = pow(g, (p - 1) // n, p)
    return tuple(sorted({pow(h, i, p) for i in range(n)}))


def monic_degree_poly(degree_: int, p: int, rng: Random) -> list[int]:
    return [rng.randrange(p) for _ in range(degree_)] + [1]


def active_fibers(p: int, H: tuple[int, ...], U: list[int], k: int, sigma: int) -> dict[int, list[tuple[int, ...]]]:
    H_set = set(H)
    s = k + sigma
    fibers: dict[int, list[tuple[int, ...]]] = {}
    for theta in range(p):
        if theta in H_set:
            continue
        hits: list[tuple[int, ...]] = []
        for S in combinations(H, s):
            V = mul([(-theta) % p, 1], locator(tuple(S), p), p)
            if degree(sub(U, V, p)) < k:
                hits.append(tuple(S))
        if hits:
            fibers[theta] = hits
    return fibers


def min_symdiff(fibers: dict[int, list[tuple[int, ...]]]) -> int | None:
    best: int | None = None
    for hits in fibers.values():
        for i, S1 in enumerate(hits):
            A = set(S1)
            for S2 in hits[i + 1 :]:
                diff = len(A.symmetric_difference(set(S2)))
                best = diff if best is None else min(best, diff)
    return best


def scan_random_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | bool | None]:
    rng = Random(seed)
    H = subgroup(p, n)
    s = k + sigma
    U = monic_degree_poly(s + 1, p, rng)
    fibers = active_fibers(p, H, U, k, sigma)
    return summarize(p, n, k, sigma, seed, fibers, constructed=False)


def scan_constructed_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | bool | None]:
    rng = Random(seed)
    H = subgroup(p, n)
    H_set = set(H)
    s = k + sigma
    S = tuple(sorted(rng.sample(list(H), s)))
    theta = rng.choice([x for x in range(p) if x not in H_set])
    r = [rng.randrange(p) for _ in range(k)]
    U = add(mul([(-theta) % p, 1], locator(S, p), p), r, p)
    fibers = active_fibers(p, H, U, k, sigma)
    assert theta in fibers and S in fibers[theta]
    return summarize(p, n, k, sigma, seed, fibers, constructed=True)


def summarize(
    p: int,
    n: int,
    k: int,
    sigma: int,
    seed: int,
    fibers: dict[int, list[tuple[int, ...]]],
    constructed: bool,
) -> dict[str, int | bool | None]:
    support = len(fibers)
    counts = [len(v) for v in fibers.values()]
    fmax = max(counts, default=0)
    N = sum(counts)
    if N:
        assert max(support, fmax) <= N <= support * fmax
    else:
        assert support == 0 and fmax == 0
    msd = min_symdiff(fibers)
    if msd is not None:
        assert msd >= 2 * (sigma + 2)
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": k + sigma,
        "seed": seed,
        "constructed": constructed,
        "support": support,
        "N": N,
        "F_max": fmax,
        "min_symdiff": msd,
        "johnson_gap": (k + sigma) * (k + sigma) - k * n,
        "passed": True,
    }


def main() -> None:
    reports = []
    for seed in range(12):
        reports.append(scan_random_case(17, 8, 2, 2, seed))
    for seed in range(8):
        reports.append(scan_constructed_case(17, 8, 2, 2, seed))
    for seed in range(6):
        reports.append(scan_constructed_case(41, 8, 2, 3, seed))
    print("cycle100 support-fiber split check")
    print(f"cases_checked: {len(reports)}")
    print(f"total_support: {sum(int(r['support']) for r in reports)}")
    print(f"total_N: {sum(int(r['N']) for r in reports)}")
    print(f"max_F_max: {max(int(r['F_max']) for r in reports)}")
    for item in reports[:10]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
