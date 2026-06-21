#!/usr/bin/env python3
"""Finite checks for the Cycle105 k-free collapse and complement duality.

The script verifies, on small split multiplicative subgroups, that the
Cycle104 active-theta divisor predicate is exactly the Cycle105 incidence
predicate

    (g_1(theta), ..., g_{sigma+1}(theta)) in M_s,

where M_s is the prefix elementary-symmetric image of s-subsets of mu_n.

It also verifies the fixed triangular complement map iota: M_s -> M_{n-s}.
"""

from itertools import combinations


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


def prefix_tuple(subset, sigma, p):
    poly = [1]
    for x in subset:
        poly = mul(poly, [1, (-x) % p], p)  # product (1 - xX)
    return tuple((poly[i] if i < len(poly) else 0) % p for i in range(1, sigma + 2))


def reverse_locator_coeffs(subset, degree, p):
    poly = [1]
    for x in subset:
        poly = mul(poly, [1, (-x) % p], p)
    out = [0] * (degree + 1)
    for i, coeff in enumerate(poly):
        out[degree - i] = coeff % p
    return out


def g_tuple(theta, uhat, sigma, p):
    vals = []
    for ell in range(1, sigma + 2):
        val = 0
        for j in range(ell + 1):
            u = uhat[ell - j] if ell - j < len(uhat) else 0
            val = (val + u * pow(theta, j, p)) % p
        vals.append(val)
    return tuple(vals)


def B_coeffs(theta, uhat, sigma, k, p):
    s = sigma + k
    coeffs = [0] * (s + 1)
    coeffs[s] = 1
    gt = g_tuple(theta, uhat, sigma, p)
    for ell, val in enumerate(gt, start=1):
        coeffs[s - ell] = val
    return coeffs


def active_by_cycle104(p, n, sigma, k, uhat):
    s = sigma + k
    H = roots_of_unity(n, p)
    active = set()
    divisor_coeffs = [reverse_locator_coeffs(subset, s, p) for subset in combinations(H, s)]
    for theta in range(p):
        b = B_coeffs(theta, uhat, sigma, k, p)
        for div in divisor_coeffs:
            if all(b[j] == div[j] for j in range(k - 1, s + 1)):
                active.add(theta)
                break
    return H, active


def active_by_kfree_incidence(p, n, sigma, k, uhat):
    s = sigma + k
    H = roots_of_unity(n, p)
    M_s = {prefix_tuple(subset, sigma, p) for subset in combinations(H, s)}
    return H, {theta for theta in range(p) if g_tuple(theta, uhat, sigma, p) in M_s}


def iota(prefix, p):
    # If A(X)B(X)=1 mod X^{sigma+2}, this recursively recovers B from A.
    b = []
    for t in range(1, len(prefix) + 1):
        total = prefix[t - 1]
        for i in range(1, t):
            total = (total + prefix[i - 1] * b[t - i - 1]) % p
        b.append((-total) % p)
    return tuple(b)


def check_case(p, n, sigma, k, uhat):
    s = sigma + k
    m = n - s
    assert s >= 0 and m >= 0
    H, active_cycle104 = active_by_cycle104(p, n, sigma, k, uhat)
    _, active_kfree = active_by_kfree_incidence(p, n, sigma, k, uhat)
    assert active_cycle104 == active_kfree, (p, n, sigma, k, active_cycle104, active_kfree)

    M_s = {prefix_tuple(subset, sigma, p) for subset in combinations(H, s)}
    M_m = {prefix_tuple(subset, sigma, p) for subset in combinations(H, m)}
    assert {iota(a, p) for a in M_s} == M_m, (p, n, sigma, k, len(M_s), len(M_m))

    return {
        "p": p,
        "n": n,
        "sigma": sigma,
        "k": k,
        "s": s,
        "m": m,
        "active": len(active_cycle104),
        "M_s": len(M_s),
        "M_m": len(M_m),
        "active_thetas": sorted(active_cycle104),
    }


def main():
    cases = [
        (11, 5, 1, 1, [1, 2, 3, 4]),
        (11, 5, 1, 2, [1, 2, 3, 4]),
        (17, 8, 2, 2, [1, 5, 0, 3, 6, 2]),
        (17, 8, 2, 3, [1, 1, 4, 2, 8, 16]),
        (29, 7, 2, 3, [1, 3, 5, 7, 11, 13]),
        (31, 10, 3, 2, [1, 4, 1, 9, 16, 25]),
    ]
    print("cycle105 k-free collapse and complement-duality check")
    for case in cases:
        result = check_case(*case)
        print(
            f"p={result['p']} n={result['n']} sigma={result['sigma']} "
            f"k={result['k']} s={result['s']} m={result['m']} "
            f"active={result['active']} M_s={result['M_s']} M_m={result['M_m']} "
            f"theta={result['active_thetas']}"
        )
    print("PASS")


if __name__ == "__main__":
    main()
