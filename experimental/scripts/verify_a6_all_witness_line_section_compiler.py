#!/usr/bin/env python3
"""Exact arithmetic checks for the A6 all-witness section compiler.

This checks only the finite parameter and degree ledger. It does not
machine-prove the imported Noether-form theorem or the algebraic-geometry
factor-specialization argument.
"""

from __future__ import annotations

from fractions import Fraction


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


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")
    checks = sum(check(r) for r in (1, 2, 3, 7, 41, 100, 1000))
    checks += tamper_checks()
    checks += all_parameter_checks()
    print(f"PASS: {checks} exact A6 compiler checks")


if __name__ == "__main__":
    main()
