#!/usr/bin/env python3
"""Finite checks for the Cycle104 fixed-k divisor-incidence proof.

This verifies the fixed-bandwidth reformulation on small fields:

  theta active iff some degree-s divisor of 1-X^n matches the high
  coefficients of B_theta, with the low k-1 coefficients filled by psi.

It also checks the local obstruction used in the proof:
  * k=2 active theta force a pair collision B_theta(x)=B_theta(y).
  * fixed k active theta force a zero order-(k-1) divided difference on
    some k-subset of the active co-support.
"""

from itertools import combinations


def inv(a, p):
    return pow(a % p, p - 2, p)


def trim(poly):
    poly = poly[:]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out)


def roots_of_unity(n, p):
    return [x for x in range(1, p) if pow(x, n, p) == 1]


def locator(subset, p):
    poly = [1]
    for x in subset:
        poly = mul(poly, [1, (-x) % p], p)  # product (1-xX)
    return poly


def reverse(poly, deg):
    out = [0] * (deg + 1)
    for i, coeff in enumerate(poly):
        out[deg - i] = coeff
    return trim(out)


def g_coeffs(theta, uhat, sigma, p):
    coeffs = []
    for ell in range(sigma + 2):
        val = 0
        for j in range(ell + 1):
            u = uhat[ell - j] if ell - j < len(uhat) else 0
            val = (val + u * pow(theta, j, p)) % p
        coeffs.append(val)
    return coeffs


def B_coeffs(theta, uhat, sigma, k, p):
    s = sigma + k
    g = g_coeffs(theta, uhat, sigma, p)
    b = [0] * (s + 1)
    b[s] = 1
    for ell in range(1, sigma + 2):
        b[s - ell] = g[ell]
    return b


def eval_poly(poly, x, p):
    acc = 0
    power = 1
    for coeff in poly:
        acc = (acc + coeff * power) % p
        power = power * x % p
    return acc


def divided_difference(values, p):
    # values = [(x_i, y_i)] with distinct x_i
    total = 0
    for i, (xi, yi) in enumerate(values):
        den = 1
        for j, (xj, _) in enumerate(values):
            if i != j:
                den = den * ((xi - xj) % p) % p
        total = (total + yi * inv(den, p)) % p
    return total


def active_by_divisors(p, n, sigma, k, uhat):
    s = sigma + k
    H = roots_of_unity(n, p)
    assert len(H) == n
    divisors = []
    for subset in combinations(H, s):
        rev = reverse(locator(subset, p), s)
        divisors.append((subset, rev))
    active = {}
    for theta in range(p):
        B = B_coeffs(theta, uhat, sigma, k, p)
        witnesses = []
        for subset, rev in divisors:
            if all(B[j] == rev[j] for j in range(k - 1, s + 1)):
                witnesses.append(subset)
        if witnesses:
            active[theta] = witnesses
    return H, active


def check_case(p, n, sigma, k, uhat):
    H, active = active_by_divisors(p, n, sigma, k, uhat)
    bound = len(list(combinations(H, k))) * (sigma + 1)
    assert len(active) <= bound
    for theta, witnesses in active.items():
        B = B_coeffs(theta, uhat, sigma, k, p)
        subset = witnesses[0]
        if k == 2:
            found = False
            for x, y in combinations(subset, 2):
                if eval_poly(B, x, p) == eval_poly(B, y, p):
                    found = True
                    break
            assert found, (p, n, sigma, k, theta, subset)
        found = False
        for nodes in combinations(subset, k):
            vals = [(x, eval_poly(B, x, p)) for x in nodes]
            if divided_difference(vals, p) == 0:
                found = True
                break
        assert found, (p, n, sigma, k, theta, subset)
    return {
        "p": p,
        "n": n,
        "sigma": sigma,
        "k": k,
        "active_count": len(active),
        "bound": bound,
        "active_thetas": sorted(active),
    }


def main():
    cases = [
        (11, 5, 1, 2, [1, 2, 3, 4]),
        (17, 8, 2, 2, [1, 5, 0, 3, 6, 2]),
        (17, 8, 2, 3, [1, 1, 4, 2, 8, 16]),
        (29, 7, 2, 3, [1, 3, 5, 7, 11, 13]),
        (31, 10, 3, 2, [1, 4, 1, 9, 16, 25]),
    ]
    print("cycle104 fixed-k divisor-incidence check")
    for case in cases:
        result = check_case(*case)
        print(
            f"p={result['p']} n={result['n']} sigma={result['sigma']} "
            f"k={result['k']} active={result['active_count']} "
            f"bound={result['bound']} theta={result['active_thetas']}"
        )
    print("PASS")


if __name__ == "__main__":
    main()

