#!/usr/bin/env python3
"""Exact verifier for Cycle102's short-window Padé route cut.

The checker verifies the returned finite falsifier over F_29:

  p = 29, n = 7, H = mu_7, sigma = 3, m = 3, S' = {1,16,24}, theta = 2.

It checks:

  * H is exactly the order-7 subgroup in F_29^*.
  * p_j(S') = theta^j - P_j for j = 1..4, so theta is active in the
    banked complement-window sense.
  * A monic degree-5 U with the stated prefix P_1..P_4 exists.
  * The length-4 Berlekamp-Massey denominator is T^2 - 24T + 1.
  * That quadratic is irreducible over F_29 and does not divide X^7 - 1.

This verifies the Padé-divisor implication is false in a finite source-valid
toy instance. It is not a counterpacket to the prize theorem.
"""

from __future__ import annotations


P = 29


def inv(a: int) -> int:
    return pow(a % P, P - 2, P)


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P
    return trim(out)


def sub(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % P
    return trim(out)


def mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            out[i + j] = (out[i + j] + av * bv) % P
    return trim(out)


def divmod_poly(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [0], a
    q = [0] * (len(a) - len(b) + 1)
    b_lc_inv = inv(b[-1])
    while len(a) >= len(b) and a != [0]:
        shift = len(a) - len(b)
        coeff = a[-1] * b_lc_inv % P
        q[shift] = coeff
        subtractor = [0] * shift + [(coeff * x) % P for x in b]
        a = sub(a, subtractor)
    return trim(q), trim(a)


def power_sums_to_monic_coeffs(power_sums: list[int], degree: int) -> list[int]:
    """Build a monic degree-d polynomial with given first power sums."""
    # Polynomial is X^d + a1 X^(d-1) + ... + ad.
    a = [0] * (degree + 1)
    for m, sm in enumerate(power_sums, start=1):
        total = sm
        for i in range(1, m):
            total = (total + a[i] * power_sums[m - i - 1]) % P
        a[m] = (-total * inv(m)) % P
    coeffs_low_to_high = [0] * degree + [1]
    for i in range(1, min(len(power_sums), degree) + 1):
        coeffs_low_to_high[degree - i] = a[i]
    return trim(coeffs_low_to_high)


def power_sum(points: set[int], j: int) -> int:
    return sum(pow(x, j, P) for x in points) % P


def bm_degree_two(window: list[int]) -> tuple[int, int]:
    a1, a2, a3, a4 = window
    # Solve a3 = c1 a2 + c2 a1 and a4 = c1 a3 + c2 a2.
    det = (a2 * a2 - a1 * a3) % P
    assert det != 0
    c1 = (a3 * a2 - a1 * a4) * inv(det) % P
    c2 = (a2 * a4 - a3 * a3) * inv(det) % P
    assert (c1 * a2 + c2 * a1) % P == a3
    assert (c1 * a3 + c2 * a2) % P == a4
    # Verify no degree-one recurrence fits.
    assert a2 * inv(a1) % P * a2 % P != a3
    return c1, c2


def main() -> None:
    H = {1, 7, 16, 20, 23, 24, 25}
    assert len(H) == 7
    assert all(pow(x, 7, P) == 1 for x in H)
    assert H == {x for x in range(1, P) if pow(x, 7, P) == 1}

    sprime = {1, 16, 24}
    theta = 2
    sigma = 3
    window = [power_sum(sprime, j) for j in range(1, sigma + 2)]
    assert window == [12, 21, 28, 13]

    prefix = [(pow(theta, j, P) - window[j - 1]) % P for j in range(1, sigma + 2)]
    assert prefix == [19, 12, 9, 3]
    U = power_sums_to_monic_coeffs(prefix, degree=5)
    assert U[-1] == 1 and len(U) == 6

    c1, c2 = bm_degree_two(window)
    assert (c1, c2) == (24, 28)  # c2 = -1.
    # Connection polynomial in T: T^2 - 24T + 1.
    char_poly = [1, (-24) % P, 1]
    assert char_poly == [1, 5, 1]

    discr = ((-24) ** 2 - 4) % P
    residues = {x * x % P for x in range(P)}
    assert discr == 21
    assert discr not in residues

    x7_minus_1 = [(-1) % P] + [0] * 6 + [1]
    _q, rem = divmod_poly(x7_minus_1, char_poly)
    assert rem != [0]

    print("cycle102 pade falsifier check")
    print(f"H={sorted(H)}")
    print(f"Sprime={sorted(sprime)} theta={theta}")
    print(f"window={window}")
    print(f"P_prefix={prefix}")
    print(f"monic_U_low_to_high={U}")
    print("BM_connection: a_j = 24*a_{j-1} - a_{j-2}")
    print("char_poly=T^2-24T+1 irreducible over F_29 and not a divisor of X^7-1")
    print("PASS")


if __name__ == "__main__":
    main()
