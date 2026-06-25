#!/usr/bin/env python3
"""Deterministic checks for the M1 primitive critical residue-syndrome note.

This script is intentionally small and dependency-free.  It verifies two finite
packets over F_97 for the Paper-B residue-line toy row

    H=<8>, n=16, k=8, sigma=2, |S|=10.

The checks are finite computations, not an asymptotic theorem.
"""

from collections import Counter
from itertools import combinations, product

P = 97
H = [pow(8, i, P) for i in range(16)]
K = 8
SIGMA = 2
SUPPORT_SIZE = K + SIGMA


def trim(poly):
    poly = [c % P for c in poly]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a, b):
    n = max(len(a), len(b))
    return trim([
        ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P
        for i in range(n)
    ])


def sub(a, b):
    n = max(len(a), len(b))
    return trim([
        ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % P
        for i in range(n)
    ])


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % P
    return trim(out)


def scale(a, c):
    return trim([(c * x) % P for x in a])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], P - 2, P)
    while len(a) >= len(b) and a != [0]:
        d = len(a) - len(b)
        coeff = a[-1] * inv % P
        q[d] = coeff
        for i in range(len(b)):
            a[d + i] = (a[d + i] - coeff * b[i]) % P
        a = trim(a)
    return trim(q), trim(a)


def mod_poly(a, b):
    return divmod_poly(a, b)[1]


def eval_poly(poly, x):
    total = 0
    xp = 1
    for coeff in poly:
        total = (total + coeff * xp) % P
        xp = xp * x % P
    return total


def degree(poly):
    poly = trim(poly)
    if poly == [0]:
        return -1
    return len(poly) - 1


def interpolate(xs, ys):
    coeff = [0]
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        basis = [1]
        denom = 1
        for j, xj in enumerate(xs):
            if i == j:
                continue
            basis = mul(basis, [(-xj) % P, 1])
            denom = denom * (xi - xj) % P
        basis = scale(basis, yi * pow(denom, P - 2, P))
        coeff = add(coeff, basis)
    return trim(coeff)


def poly_from_y(coeff_y, alpha):
    """Return coeff_y(Y) in X-coordinates, where Y=X-alpha."""
    out = [0]
    y_poly = [(-alpha) % P, 1]
    power = [1]
    for coeff in coeff_y:
        out = add(out, scale(power, coeff))
        power = mul(power, y_poly)
    return trim(out)


def values_from_x_poly(poly):
    return [eval_poly(poly, x) for x in H]


def no_smaller_denominator(g_values, tau):
    """Brute force monic denominators D of degree < tau in X-coordinates.

    A representation with denominator degree u exists iff some monic D of
    degree u, nonzero on H, makes the interpolation of D*g have degree < K+u.
    Degree zero is represented by D=1.
    """
    for u in range(tau):
        denominators = [[1]] if u == 0 else (
            list(coeffs) + [1] for coeffs in product(range(P), repeat=u)
        )
        for denominator in denominators:
            if any(eval_poly(denominator, x) == 0 for x in H):
                continue
            vals = [
                eval_poly(denominator, x) * gx % P
                for x, gx in zip(H, g_values)
            ]
            interp = interpolate(H, vals)
            if degree(interp) < K + u:
                return False, (u, denominator, interp)
    return True, None


def verify_quadratic_85():
    e_poly = [64, 45, 1]  # X^2 + 45X + 64
    b_poly = [1, (-1) % P]  # 1 - X
    w_poly = [0] * 16
    for deg, coeff in [
        (1, 27),
        (10, 73),
        (11, 6),
        (12, 49),
        (13, 21),
        (14, 77),
        (15, 36),
    ]:
        w_poly[deg] = coeff % P

    w_values = values_from_x_poly(w_poly)
    assert w_values == [95, 3, 8, 94, 31, 18, 68, 18, 12, 3, 9, 38, 58, 29, 10, 88]
    assert all(eval_poly(e_poly, x) != 0 for x in H)
    assert eval_poly(e_poly, 1) == 13  # gcd(E,1-X)=1.

    hits = [0] * P
    witness_polys = {}
    success = 0
    antipodal_success = 0

    for support in combinations(range(len(H)), SUPPORT_SIZE):
        locator = [1]
        for i in support:
            locator = mul(locator, [(-H[i]) % P, 1])
        q_poly = mod_poly(w_poly, locator)
        remainder = mod_poly(q_poly, e_poly)
        a = remainder[0] if len(remainder) > 0 else 0
        b = remainder[1] if len(remainder) > 1 else 0
        if (a + b) % P != 0:
            continue

        z = a
        success += 1
        hits[z] += 1
        witness_polys[tuple(q_poly + [0] * (SUPPORT_SIZE - len(q_poly)))] = z

        support_set = set(support)
        if all((i + 8) % 16 in support_set for i in support):
            antipodal_success += 1

        q_minus_zb = sub(q_poly, scale(b_poly, z))
        a_poly, rem = divmod_poly(q_minus_zb, e_poly)
        assert rem == [0]
        assert degree(a_poly) < K
        for i in support:
            lhs = (
                eval_poly(e_poly, H[i]) * eval_poly(a_poly, H[i])
                + z * eval_poly(b_poly, H[i])
            ) % P
            assert lhs == w_values[i]

    agreement_distribution = Counter()
    for q_key in witness_polys:
        q_poly = list(q_key)
        agree = sum(1 for x, w in zip(H, w_values) if eval_poly(q_poly, x) == w)
        agreement_distribution[agree] += 1

    g_values = [
        (-eval_poly(b_poly, x) * pow(eval_poly(e_poly, x), P - 2, P)) % P
        for x in H
    ]
    minimal, witness = no_smaller_denominator(g_values, tau=2)
    assert minimal, witness

    missing = [z for z, count in enumerate(hits) if count == 0]
    assert success == 145
    assert antipodal_success == 0
    assert len(witness_polys) == 125
    assert dict(sorted(agreement_distribution.items())) == {10: 123, 11: 2}
    assert sum(count > 0 for count in hits) == 85
    assert missing == [0, 24, 37, 42, 49, 52, 54, 57, 60, 63, 67, 71]
    assert min(count for count in hits if count) == 1
    assert max(hits) == 12
    assert 2 * 2 <= len(H) - K
    assert e_poly[1] != 0  # The unique minimal quadratic is not a polynomial in X^2.

    return {
        "success": success,
        "distinct_slopes": sum(count > 0 for count in hits),
        "missing": missing,
        "agreement_distribution": dict(sorted(agreement_distribution.items())),
    }


def verify_shifted_cubic_83():
    # Y = X - 2.
    e_y = [0, 0, 0, 1]  # Y^3
    b_y = [1, 46, 53]
    w_y = [0] * 12
    w_y[1] = 15
    w_y[2] = 13
    w_y[11] = 1

    e_poly = poly_from_y(e_y, alpha=2)
    b_poly = poly_from_y(b_y, alpha=2)
    w_poly = poly_from_y(w_y, alpha=2)
    y_points = [(x - 2) % P for x in H]
    w_values = values_from_x_poly(w_poly)

    assert 2 not in H
    assert all(eval_poly(e_poly, x) != 0 for x in H)
    assert eval_poly(b_poly, 2) == 1  # gcd(Y^3,B)=1.
    assert w_values == [94, 57, 13, 58, 26, 92, 64, 0, 47, 78, 25, 61, 43, 70, 80, 47]

    hits = [0] * P
    multiplicities = Counter()
    success = 0
    tangent_success = 0

    y_poly = [0, 1]

    for support in combinations(range(len(H)), SUPPORT_SIZE):
        locator_y = [1]
        for i in support:
            locator_y = mul(locator_y, [(-y_points[i]) % P, 1])
        support_hits = 0
        for r in range(P):
            q_y = sub(w_y, mul(add(y_poly, [r]), locator_y))
            assert degree(q_y) < K + 3
            remainder = mod_poly(q_y, e_y)
            coeff = remainder + [0] * (3 - len(remainder))
            z = coeff[0]
            if coeff[1] != 46 * z % P:
                continue
            if coeff[2] != 53 * z % P:
                continue

            support_hits += 1
            success += 1
            hits[z] += 1

            ell0, ell1, ell2 = locator_y[0], locator_y[1], locator_y[2]
            tangent = (ell1 - 46 * ell0) % P == 0 and (ell2 - 53 * ell0) % P == 0
            if tangent:
                tangent_success += 1

            q_x = poly_from_y(q_y, alpha=2)
            q_minus_zb = sub(q_x, scale(b_poly, z))
            a_poly, rem = divmod_poly(q_minus_zb, e_poly)
            assert rem == [0]
            assert degree(a_poly) < K
            for i in support:
                lhs = (
                    eval_poly(e_poly, H[i]) * eval_poly(a_poly, H[i])
                    + z * eval_poly(b_poly, H[i])
                ) % P
                assert lhs == w_values[i]

        assert support_hits <= 1

    for count in hits:
        if count:
            multiplicities[count] += 1

    g_values = [
        (-eval_poly(b_poly, x) * pow(eval_poly(e_poly, x), P - 2, P)) % P
        for x in H
    ]
    minimal, witness = no_smaller_denominator(g_values, tau=3)
    assert minimal, witness

    missing = [z for z, count in enumerate(hits) if count == 0]
    assert success == 133
    assert tangent_success == 0
    assert sum(count > 0 for count in hits) == 83
    assert missing == [3, 6, 13, 16, 19, 32, 38, 46, 49, 56, 59, 76, 84, 89]
    assert dict(sorted(multiplicities.items())) == {1: 52, 2: 21, 3: 8, 4: 1, 11: 1}
    assert 2 * 3 <= len(H) - K
    assert 3 % 2 == 1 and 3 % 4 == 3 and 3 % 8 == 3

    return {
        "success": success,
        "distinct_slopes": sum(count > 0 for count in hits),
        "missing": missing,
        "multiplicities": dict(sorted(multiplicities.items())),
    }


def main():
    quadratic = verify_quadratic_85()
    shifted_cubic = verify_shifted_cubic_83()
    print("H =", H)
    print("quadratic_85: PASS", quadratic)
    print("shifted_cubic_83: PASS", shifted_cubic)


if __name__ == "__main__":
    main()
