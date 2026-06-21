#!/usr/bin/env python3
"""Toy verifier for Cycle99's divisor and line-incidence reductions.

For small prime fields, this checks that the Cycle98 external-root incidence
condition is equivalent to:

  1. a degree-s divisor f of X^n-1 with deg(U - (X-theta)f) < k;
  2. a deg-<k RS codeword r=U-(X-theta)f;
  3. the reciprocal affine-line condition on elementary symmetric functions of
     H \\ S.

For very small cases it also verifies the additive-character counting identity
numerically. This is a finite sanity check only.
"""

from __future__ import annotations

import cmath
from itertools import combinations, product
from math import comb
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


def truncate(poly: list[int], length: int) -> list[int]:
    return (poly + [0] * length)[:length]


def degree(poly: list[int]) -> int:
    return len(trim(poly[:])) - 1


def locator(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [(-x) % p, 1], p)
    return trim(out)


def one_minus_product(points: tuple[int, ...], p: int) -> list[int]:
    out = [1]
    for x in points:
        out = mul(out, [1, (-x) % p], p)
    return trim(out)


def monic_degree_poly(degree_: int, p: int, rng: Random) -> list[int]:
    return [rng.randrange(p) for _ in range(degree_)] + [1]


def prefix_from_monic(poly: list[int], count: int, p: int) -> tuple[int, ...]:
    deg = len(poly) - 1
    assert poly[-1] == 1
    vals: list[int] = []
    for j in range(1, count + 1):
        coeff = poly[deg - j] if deg - j >= 0 else 0
        vals.append(((-1) ** j * coeff) % p)
    return tuple(vals)


def elementary_from_points(points: tuple[int, ...], count: int, p: int) -> tuple[int, ...]:
    loc = locator(points, p)
    return prefix_from_monic(loc, count, p)


def power_sums_from_elementaries(elems: tuple[int, ...], p: int) -> tuple[int, ...]:
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


def reverse_monic(poly: list[int], degree_: int, p: int) -> list[int]:
    return [poly[degree_ - i] if degree_ - i >= 0 else 0 for i in range(degree_ + 1)]


def series_inverse(poly: list[int], length: int, p: int) -> list[int]:
    assert poly[0] % p == 1
    inv = [1]
    for m in range(1, length):
        total = 0
        for i in range(1, m + 1):
            total = (total + (poly[i] if i < len(poly) else 0) * inv[m - i]) % p
        inv.append((-total) % p)
    return inv


def character_identity_count(
    p: int,
    H: tuple[int, ...],
    s: int,
    count: int,
    P: tuple[int, ...],
) -> complex:
    """Numerically evaluate the exact additive-character expansion."""
    zeta = cmath.exp(2j * cmath.pi / p)
    total = 0j
    external = [x for x in range(p) if x not in H]
    H_list = list(H)
    for t in product(range(p), repeat=count):
        phase_p = sum(t[j - 1] * P[j - 1] for j in range(1, count + 1)) % p
        es = 0j
        for S in combinations(H_list, s):
            val = 0
            for x in S:
                val = (val + sum(t[j - 1] * pow(x, j, p) for j in range(1, count + 1))) % p
            es += zeta ** val
        theta_sum = 0j
        for theta in external:
            val = sum(t[j - 1] * pow(theta, j, p) for j in range(1, count + 1)) % p
            theta_sum += zeta ** val
        total += (zeta ** (-phase_p % p)) * es * theta_sum
    return total / (p**count)


def scan_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | float | bool]:
    rng = Random(seed)
    H = subgroup(p, n)
    H_set = set(H)
    s = k + sigma
    m = n - s
    deg_u = s + 1
    count = sigma + 1
    U = monic_degree_poly(deg_u, p, rng)
    c = prefix_from_monic(U, count, p)
    P = power_sums_from_elementaries(c, p)
    U_rev = reverse_monic(U, deg_u, p)
    W = series_inverse(U_rev, count + 1, p)

    incidence_pairs: set[tuple[int, tuple[int, ...]]] = set()
    divisor_pairs: set[tuple[int, tuple[int, ...]]] = set()
    line_theta: set[int] = set()
    codeword_to_theta: dict[tuple[int, ...], int] = {}

    for theta in range(p):
        if theta in H_set:
            continue
        target_powers = tuple((P[j - 1] - pow(theta, j, p)) % p for j in range(1, count + 1))
        for S in combinations(H, s):
            S_t = tuple(S)
            Ls = locator(S_t, p)
            if subset_power_sums(S_t, count, p) == target_powers:
                incidence_pairs.add((theta, S_t))
            V = mul([(-theta) % p, 1], Ls, p)
            if degree(sub(U, V, p)) < k:
                pair = (theta, S_t)
                divisor_pairs.add(pair)
                r = tuple(truncate(sub(U, V, p), k))
                if r in codeword_to_theta:
                    assert codeword_to_theta[r] == theta
                codeword_to_theta[r] = theta

                comp = tuple(x for x in H if x not in set(S_t))
                g = one_minus_product(comp, p)
                rhs = mul([1, (-theta) % p], W, p)
                assert truncate(g, count + 1) == truncate(rhs, count + 1)
                line_e = tuple(((-1) ** i * (W[i] - theta * W[i - 1])) % p for i in range(1, count + 1))
                assert elementary_from_points(comp, count, p) == line_e

    assert incidence_pairs == divisor_pairs, (incidence_pairs - divisor_pairs, divisor_pairs - incidence_pairs)

    E_m = {elementary_from_points(tuple(comp), count, p) for comp in combinations(H, m)}
    for theta in range(p):
        if theta in H_set:
            continue
        line_e = tuple(((-1) ** i * (W[i] - theta * W[i - 1])) % p for i in range(1, count + 1))
        if line_e in E_m:
            line_theta.add(theta)
    assert line_theta == {theta for theta, _ in divisor_pairs}

    char_error_abs = -1.0
    if p**count <= 6000:
        approx = character_identity_count(p, H, s, count, P)
        assert abs(approx.real - len(divisor_pairs)) < 1e-6 and abs(approx.imag) < 1e-6, approx
        main = comb(n, s) * (p - n) / (p**count)
        char_error_abs = abs(len(divisor_pairs) - main)

    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": s,
        "m": m,
        "seed": seed,
        "external_theta": len(line_theta),
        "external_pairs": len(divisor_pairs),
        "codewords": len(codeword_to_theta),
        "char_error_abs": char_error_abs,
        "johnson_gap": s * s - k * n,
        "passed": True,
    }


def scan_constructed_case(p: int, n: int, k: int, sigma: int, seed: int) -> dict[str, int | float | bool]:
    """Build U=(X-theta)L_S+r so at least one external witness exists."""
    rng = Random(seed)
    H = subgroup(p, n)
    H_set = set(H)
    s = k + sigma
    S = tuple(sorted(rng.sample(list(H), s)))
    external = [x for x in range(p) if x not in H_set]
    theta = external[rng.randrange(len(external))]
    r = [rng.randrange(p) for _ in range(k)]
    V = mul([(-theta) % p, 1], locator(S, p), p)
    U = add(V, r, p)
    assert len(U) == s + 2 and U[-1] == 1

    count = sigma + 1
    c = prefix_from_monic(U, count, p)
    P = power_sums_from_elementaries(c, p)
    U_rev = reverse_monic(U, s + 1, p)
    W = series_inverse(U_rev, count + 1, p)

    divisor_pairs: set[tuple[int, tuple[int, ...]]] = set()
    incidence_pairs: set[tuple[int, tuple[int, ...]]] = set()
    for th in range(p):
        if th in H_set:
            continue
        target_powers = tuple((P[j - 1] - pow(th, j, p)) % p for j in range(1, count + 1))
        for S2 in combinations(H, s):
            Ls = locator(tuple(S2), p)
            if subset_power_sums(tuple(S2), count, p) == target_powers:
                incidence_pairs.add((th, tuple(S2)))
            V2 = mul([(-th) % p, 1], Ls, p)
            if degree(sub(U, V2, p)) < k:
                divisor_pairs.add((th, tuple(S2)))
                comp = tuple(x for x in H if x not in set(S2))
                g = one_minus_product(comp, p)
                rhs = mul([1, (-th) % p], W, p)
                assert truncate(g, count + 1) == truncate(rhs, count + 1)

    assert (theta, S) in divisor_pairs
    assert divisor_pairs == incidence_pairs
    return {
        "p": p,
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": s,
        "m": n - s,
        "seed": seed,
        "constructed_theta": theta,
        "external_theta": len({th for th, _ in divisor_pairs}),
        "external_pairs": len(divisor_pairs),
        "johnson_gap": s * s - k * n,
        "passed": True,
    }


def main() -> None:
    cases = [
        (17, 8, 2, 2, range(8)),
        (41, 8, 2, 3, range(6)),
        (37, 12, 3, 2, range(6)),
    ]
    reports = []
    for p, n, k, sigma, seeds in cases:
        for seed in seeds:
            reports.append(scan_case(p, n, k, sigma, seed))
    constructed = [
        scan_constructed_case(17, 8, 2, 2, seed) for seed in range(6)
    ] + [
        scan_constructed_case(41, 8, 2, 3, seed) for seed in range(4)
    ]
    print("cycle99 divisor-line incidence check")
    print(f"cases_checked: {len(reports)}")
    print(f"constructed_cases_checked: {len(constructed)}")
    print(f"total_external_theta: {sum(int(r['external_theta']) for r in reports)}")
    print(f"total_external_pairs: {sum(int(r['external_pairs']) for r in reports)}")
    print(f"constructed_external_pairs: {sum(int(r['external_pairs']) for r in constructed)}")
    print(f"total_codewords: {sum(int(r['codewords']) for r in reports)}")
    for item in reports[:8]:
        print(item)
    for item in constructed[:4]:
        print(item)
    print("PASS")


if __name__ == "__main__":
    main()
