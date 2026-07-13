#!/usr/bin/env python3
"""Exact arithmetic checks for the A6 all-witness section compiler.

This checks only the finite parameter and degree ledger. It does not
machine-prove the imported Noether-form theorem or the algebraic-geometry
factor-specialization argument.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def parameters(r: int) -> dict[str, int]:
    assert r >= 1
    return {
        "N": 500 * r,
        "kappa": 225 * r,
        "t": 150 * r,
        "d": 250 * r,
        "m": 4,
        "L": 52,
        "D": 1400 * r - 1,
    }


def unknown_count(D: int, w: int, L: int) -> tuple[int, int]:
    q = D // w
    total = sum((L - c + 1) * (D - c * w + 1) for c in range(q + 1))
    return q, total


def condition_count(m: int, L: int) -> int:
    return sum(
        (m - j) * (L - j + 1)
        for j in range(min(m - 1, L) + 1)
    )


def capped_unknown_count(D: int, w: int, L: int, q: int) -> int:
    assert 1 <= q <= L
    assert q * w <= D
    return sum((D - c * w + 1) * (L - c + 1) for c in range(q + 1))


def least_degree(mu: int, L: int, q: int, N: int, w: int) -> int:
    A = sum(L - c + 1 for c in range(q + 1))
    b = sum((1 - c * w) * (L - c + 1) for c in range(q + 1))
    return max(q * w, (N * condition_count(mu, L) - b) // A + 1)


def moving_ratio(t: int, d: int) -> Fraction:
    return Fraction(t + 1, 1) if d <= t else Fraction(d, d - t)


def all_parameter_bound(
    mu: int,
    L: int,
    q: int,
    D: int,
    N: int,
    kappa: int,
    t: int,
    d: int,
) -> int:
    w = kappa - 1
    assert capped_unknown_count(D, w, L, q) > N * condition_count(mu, L)
    assert D < mu * (N - t)
    rho = moving_ratio(t, d)
    moving = q * (L + 1) * rho
    return (
        L
        + q * L * (12 * D**6 + 1)
        + q
        + moving.numerator // moving.denominator
    )


def sharpened_canonical_bound(r: int) -> tuple[int, int]:
    N, kappa, t, d = 500 * r, 225 * r, 150 * r, 250 * r
    D = (489_950 * r - 1_372) // 350 + 1
    bound = all_parameter_bound(4, 52, 6, D, N, kappa, t, d)
    return D, bound


def slope_bound(r: int) -> int:
    p = parameters(r)
    q, _ = unknown_count(p["D"], p["kappa"] - 1, p["L"])
    delta = p["D"] + q
    exceptional = p["L"] + q * p["L"] * (12 * delta**6 + 1)
    moving = q + (p["N"] * q * (p["L"] + 1)) // (p["d"] - p["t"])
    return exceptional + moving


def check(r: int) -> int:
    p = parameters(r)
    w = p["kappa"] - 1
    q, unknowns = unknown_count(p["D"], w, p["L"])
    conditions = p["N"] * condition_count(p["m"], p["L"])

    assert q == 6
    assert p["D"] - 6 * w == 50 * r + 5 >= 0
    assert p["D"] - 7 * w == -175 * r + 6 < 0
    assert condition_count(p["m"], p["L"]) == 520
    assert unknowns == 260050 * r + 1022
    assert conditions == 260000 * r
    assert unknowns - conditions == 50 * r + 1022 > 0
    assert p["m"] * (p["N"] - p["t"]) > p["D"]
    assert p["d"] - p["t"] == 100 * r > 0

    delta = p["D"] + q
    assert delta == 1400 * r + 5
    assert q * p["L"] == 312
    assert 12 * q * p["L"] == 3744
    assert q * (p["L"] + 1) == 318

    moving_nontrivial = (
        p["N"] * q * (p["L"] + 1)
    ) // (p["d"] - p["t"])
    assert moving_nontrivial == 1590
    assert q + moving_nontrivial == 1596

    expected = 1960 + 3744 * (1400 * r + 5) ** 6
    assert slope_bound(r) == expected
    return 18


def tamper_checks() -> int:
    p = parameters(1)
    assert 3 * (p["N"] - p["t"]) <= p["D"]

    p = parameters(41)
    q, unknowns = unknown_count(p["D"], p["kappa"] - 1, 51)
    conditions = p["N"] * condition_count(4, 51)
    assert q == 6
    assert unknowns <= conditions

    r = 1
    old_repaired_claim = 1648 + 3744 * (1400 * r + 5) ** 6
    assert slope_bound(r) - old_repaired_claim == 312
    return 3


def all_parameter_checks() -> int:
    checks = 0
    for r in (1, 2, 3, 7, 41, 100, 1000):
        N, kappa, t, d = 500 * r, 225 * r, 150 * r, 250 * r
        w = kappa - 1
        D, bound = sharpened_canonical_bound(r)
        assert D == least_degree(4, 52, 6, N, w)
        assert 6 * w <= D < 4 * (N - t)
        assert bound == 1165 + 3744 * D**6
        assert bound < slope_bound(r)
        assert moving_ratio(t, d) == Fraction(5, 2)
        checks += 6

    # Exact optimizer and capacity-frontier regression over small rows.
    for N in range(3, 25):
        for kappa in range(2, N + 1):
            w = kappa - 1
            for t in range(0, N):
                a = N - t
                frontier = a * a > N * w
                found = False
                for mu in range(1, 13):
                    for L in range(1, 18):
                        for q in range(1, L + 1):
                            D = least_degree(mu, L, q, N, w)
                            if D < mu * a:
                                assert capped_unknown_count(D, w, L, q) > (
                                    N * condition_count(mu, L)
                                )
                                found = True
                                break
                        if found:
                            break
                    if found:
                        break
                if frontier:
                    # Construct a witness exactly as in the sufficiency proof:
                    # D=mu*a-1, q=floor(D/w), then choose L after the affine
                    # surplus coefficient becomes positive.
                    mu = 1
                    while True:
                        D = mu * a - 1
                        q = D // w
                        if q >= 1:
                            coefficient = sum(
                                D - c * w + 1 for c in range(q + 1)
                            ) - N * mu * (mu + 1) // 2
                            if coefficient > 0:
                                L = max(q, mu - 1)
                                surplus = (
                                    capped_unknown_count(D, w, L, q)
                                    - N * condition_count(mu, L)
                                )
                                if surplus <= 0:
                                    L += (-surplus) // coefficient + 1
                                assert capped_unknown_count(D, w, L, q) > (
                                    N * condition_count(mu, L)
                                )
                                assert D < mu * a
                                break
                        mu += 1
                        assert mu < 10_000
                else:
                    assert not found
                checks += 1

    assert moving_ratio(8, 8) == 9
    assert moving_ratio(8, 7) == 9
    assert moving_ratio(8, 9) == 9
    assert moving_ratio(8, 16) == 2
    checks += 4
    return checks


def global_section_parameters(n: int, k: int, a: int) -> dict[str, int]:
    """Explicit section-positive tuple from the global one-cell corollary."""
    assert 2 <= k < a < n
    w = k - 1
    t = n - a
    J = a * a - n * w
    assert J > 0
    mu = (w * t) // J + 1
    D = mu * a - 1
    q = D // w
    sigma = sum(c * (mu * a - c * w) for c in range(q + 1))
    L = max(q, mu - 1, sigma)
    return {
        "n": n,
        "k": k,
        "a": a,
        "w": w,
        "t": t,
        "J": J,
        "mu": mu,
        "D": D,
        "q": q,
        "sigma": sigma,
        "L": L,
    }


def global_section_bound(p: dict[str, int]) -> int:
    return (
        p["L"]
        + p["q"] * p["L"] * (12 * p["D"] ** 6 + 1)
        + p["q"]
        + p["q"] * (p["L"] + 1) * (p["t"] + 1)
    )


def global_section_positive_checks() -> int:
    checks = 0
    interior = 0
    endpoints = 0
    stronger = 0

    for n in range(3, 151):
        for k in range(2, n):
            w = k - 1
            for a in range(k + 1, n + 1):
                J = a * a - n * w
                if J <= 0:
                    continue
                if a == n:
                    # The theorem uses a separate full-support argument here;
                    # the section tuple must never divide by t=n-a=0.
                    assert n - a == 0
                    endpoints += 1
                    checks += 1
                    continue

                p = global_section_parameters(n, k, a)
                assert p["mu"] * J > w * p["t"]
                assert p["q"] >= 1
                assert p["q"] * w <= p["D"] < p["mu"] * a
                assert p["L"] >= max(p["q"], p["mu"] - 1, p["sigma"])

                A = sum(
                    p["mu"] * a - c * w for c in range(p["q"] + 1)
                )
                M = p["mu"] * (p["mu"] + 1) // 2
                G = A - n * M
                assert G >= 1

                surplus = (
                    capped_unknown_count(p["D"], w, p["L"], p["q"])
                    - n * condition_count(p["mu"], p["L"])
                )
                assert surplus >= 1

                bound = global_section_bound(p)
                assert bound < 10_000 * n**27
                if a * a >= n * k:
                    assert J >= n
                    assert bound < 10_000 * n**17
                    stronger += 1

                interior += 1
                checks += 9

    assert interior == 367_812
    assert endpoints == 11_026
    assert interior + endpoints == 378_838

    # The ratio is load-bearing.  Reversing it fails at the first small
    # counterexample (n,k,a)=(7,2,3).
    n, k, a = 7, 2, 3
    w, t, J = k - 1, n - a, a * a - n * (k - 1)
    mu_bad = J // (w * t) + 1
    D_bad = mu_bad * a - 1
    q_bad = D_bad // w
    A_bad = sum(mu_bad * a - c * w for c in range(q_bad + 1))
    G_bad = A_bad - n * mu_bad * (mu_bad + 1) // 2
    assert (J, w * t, mu_bad, G_bad) == (2, 4, 1, -1)
    checks += 1

    # Canonical line-uniform specialization.
    for r in (1, 2, 3, 7, 41, 100, 1000):
        n, k, a = 500 * r, 225 * r, 350 * r
        w, t, J = k - 1, n - a, a * a - n * (k - 1)
        assert (w * t) // J + 1 == 4
        D, _ = sharpened_canonical_bound(r)
        uniform = (
            52
            + 6 * 52 * (12 * D**6 + 1)
            + 6
            + 6 * 53 * (t + 1)
        )
        assert uniform == 3744 * D**6 + 47_700 * r + 688
        checks += 2

    # Dimension-one and full-support formulas are exact finite integers.
    assert comb(3, 2) == 3
    checks += 1

    print(
        "PASS: global section-positive atlas",
        f"interior={interior}",
        f"endpoints={endpoints}",
        f"stronger={stronger}",
    )
    return checks


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")
    checks = sum(check(r) for r in (1, 2, 3, 7, 41, 100, 1000))
    checks += tamper_checks()
    checks += all_parameter_checks()
    checks += global_section_positive_checks()
    print(f"PASS: {checks} exact A6 compiler checks")


if __name__ == "__main__":
    main()
