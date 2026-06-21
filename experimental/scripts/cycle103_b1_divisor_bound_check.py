#!/usr/bin/env python3
"""Finite checks for the Cycle103 B1 divisor-incidence proof.

This is not a proof of the theorem. It verifies, on small finite fields, the
key B1 equivalence used in the audit:

  theta active <=> G(theta, X) is a degree-(sigma+1) divisor of 1-X^n.

For k=1, s=sigma+1 and the congruence modulo X^(sigma+2) fixes the complete
co-locator. Thus the active theta set can be computed either by subset
enumeration of H=mu_n or by direct divisibility against X^n-1.
"""

from itertools import combinations


def inv(a, p):
    return pow(a % p, p - 2, p)


def trim(poly):
    poly = poly[:]
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a, b, p):
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return trim(out)


def mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out)


def div_rem(num, den, p):
    num = trim(num)
    den = trim(den)
    if den == [0]:
        raise ZeroDivisionError
    if len(num) < len(den):
        return [0], num
    out = [0] * (len(num) - len(den) + 1)
    rem = num[:]
    lead_inv = inv(den[-1], p)
    while len(rem) >= len(den) and rem != [0]:
        shift = len(rem) - len(den)
        coef = rem[-1] * lead_inv % p
        out[shift] = coef
        for i in range(len(den)):
            rem[shift + i] = (rem[shift + i] - coef * den[i]) % p
        rem = trim(rem)
    return trim(out), rem


def divisors_by_subset(H, d, p):
    divs = {}
    for subset in combinations(H, d):
        poly = [1]
        for x in subset:
            poly = mul(poly, [1, (-x) % p], p)
        divs[tuple(poly)] = subset
    return divs


def G_poly(theta, uhat, sigma, p):
    coeffs = []
    for ell in range(sigma + 2):
        val = 0
        for j in range(ell + 1):
            u = uhat[ell - j] if ell - j < len(uhat) else 0
            val = (val + u * pow(theta, j, p)) % p
        coeffs.append(val)
    return trim(coeffs)


def roots_of_unity(n, p):
    return [x for x in range(1, p) if pow(x, n, p) == 1]


def check_case(p, n, sigma, uhat):
    d = sigma + 1
    assert (p - 1) % n == 0
    H = roots_of_unity(n, p)
    assert len(H) == n
    divisors = divisors_by_subset(H, d, p)
    target = [1] + [0] * (n - 1) + [p - 1]  # 1 - X^n
    by_subset = set()
    by_remainder = set()
    for theta in range(p):
        G = G_poly(theta, uhat, sigma, p)
        if len(G) == d + 1 and tuple(G) in divisors:
            by_subset.add(theta)
        if len(G) == d + 1:
            _, rem = div_rem(target, G, p)
            if rem == [0]:
                by_remainder.add(theta)
    assert by_subset == by_remainder, (p, n, sigma, uhat, by_subset, by_remainder)
    bound = (n - sigma + 1) * (sigma + 1)
    assert len(by_subset) <= bound
    return {
        "p": p,
        "n": n,
        "sigma": sigma,
        "uhat": uhat,
        "active_count": len(by_subset),
        "bound": bound,
        "active_thetas": sorted(by_subset),
    }


def main():
    cases = [
        (11, 5, 1, [1, 2, 3, 4]),
        (11, 5, 2, [1, 0, 4, 7, 9]),
        (17, 8, 2, [1, 5, 0, 3, 6, 2]),
        (29, 7, 3, [1, 10, 15, 7, 0, 0]),
        (31, 10, 3, [1, 4, 1, 9, 16, 25]),
    ]
    results = [check_case(*case) for case in cases]
    print("cycle103 B1 divisor-bound check")
    for result in results:
        print(
            f"p={result['p']} n={result['n']} sigma={result['sigma']} "
            f"active={result['active_count']} bound={result['bound']} "
            f"theta={result['active_thetas']}"
        )
    print("PASS")


if __name__ == "__main__":
    main()

