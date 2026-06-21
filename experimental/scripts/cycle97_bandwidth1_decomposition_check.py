#!/usr/bin/env python3
"""Toy verifier for Cycle97's bandwidth-1 decomposition.

For small prime fields it checks that degree-(s+1) arbitrary-word lists split
into:
  Type A: all s+1 roots in H, a bandwidth-0 prefix fiber on (s+1)-sets.
  Type B: s roots in H plus one extra root theta, with theta forcing a
          bandwidth-0 prefix target on s-sets.

This is a finite sanity check, not a proof.
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


def eval_poly(poly: list[int], x: int, p: int) -> int:
    acc = 0
    for coeff in reversed(poly):
        acc = (acc * x + coeff) % p
    return acc


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return trim(out)


def monic_degree_poly(degree: int, p: int, rng: Random) -> list[int]:
    return [rng.randrange(p) for _ in range(degree)] + [1]


def all_polys_deg_lt(k: int, p: int):
    for coeffs in product(range(p), repeat=k):
        yield trim(list(coeffs))


def prefix_from_monic(poly: list[int], count: int, p: int) -> tuple[int, ...]:
    degree = len(poly) - 1
    assert poly[-1] == 1
    vals = []
    for j in range(1, count + 1):
        coeff = poly[degree - j] if degree - j >= 0 else 0
        vals.append(((-1) ** j * coeff) % p)
    return tuple(vals)


def theta_prefix(c: tuple[int, ...], theta: int, p: int) -> tuple[int, ...]:
    c0 = (1,) + c
    out = []
    for j in range(1, len(c) + 1):
        total = 0
        for i in range(j + 1):
            total = (total + pow((-theta) % p, j - i, p) * c0[i]) % p
        out.append(total)
    return tuple(out)


def scan_case(p: int, H: tuple[int, ...], k: int, sigma: int, seed: int) -> dict:
    rng = Random(seed)
    s = k + sigma
    degree = s + 1
    U = monic_degree_poly(degree, p, rng)
    c = prefix_from_monic(U, sigma + 1, p)

    direct = []
    for P in all_polys_deg_lt(k, p):
        V = sub(U, P, p)
        roots = tuple(x for x in H if eval_poly(V, x, p) == 0)
        if len(roots) >= s:
            direct.append((tuple(V), roots))

    type_a = set()
    for R in combinations(H, s + 1):
        L = locator(R, p)
        if prefix_from_monic(L, sigma + 1, p) == c:
            type_a.add(tuple(L))

    type_b = set()
    active_theta: set[int] = set()
    external_theta: set[int] = set()
    h_theta: set[int] = set()
    for theta in range(p):
        target = theta_prefix(c, theta, p)
        for S in combinations(H, s):
            Ls = locator(S, p)
            if prefix_from_monic(Ls, sigma + 1, p) == target:
                V = mul([(-theta) % p, 1], Ls, p)
                assert prefix_from_monic(V, sigma + 1, p) == c
                assert theta == (c[0] - prefix_from_monic(Ls, 1, p)[0]) % p
                type_b.add(tuple(V))
                active_theta.add(theta)
                if theta in H:
                    h_theta.add(theta)
                else:
                    external_theta.add(theta)

    decomp = type_a | type_b
    direct_set = {V for V, _ in direct}
    assert direct_set == decomp, (direct_set - decomp, decomp - direct_set)
    return {
        "p": p,
        "H_size": len(H),
        "k": k,
        "sigma": sigma,
        "s": s,
        "seed": seed,
        "direct_list": len(direct_set),
        "type_a": len(type_a),
        "type_b": len(type_b),
        "active_theta": len(active_theta),
        "external_theta": len(external_theta),
        "h_theta": len(h_theta),
        "passed": True,
    }


def main() -> None:
    cases = [
        (17, tuple(range(8)), 2, 2, range(20)),
        (19, tuple(range(9)), 3, 2, range(20)),
    ]
    reports = []
    for p, H, k, sigma, seeds in cases:
        for seed in seeds:
            reports.append(scan_case(p, H, k, sigma, seed))
    print("cycle97 bandwidth-1 decomposition check")
    print(f"cases_checked: {len(reports)}")
    print(f"total_direct_list: {sum(r['direct_list'] for r in reports)}")
    print(f"total_active_theta: {sum(r['active_theta'] for r in reports)}")
    print(f"total_external_theta: {sum(r['external_theta'] for r in reports)}")
    for item in reports[:6]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
