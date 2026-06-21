#!/usr/bin/env python3
"""Exact finite checker for the Cycle106 complement-line eliminant.

Let d=sigma+1, H=mu_n in F_p, s be the Cycle105 subset size, and m=n-s.
For U(X)=1+u_1 X+... define V(X)=U(X)^(-1) mod X^(d+1):

    V(X)=sum_{j=0}^d v_j X^j,  v_0=1.

Cycle105 complement duality gives the exact affine-line form

    theta active  <=>  (v_j-theta*v_{j-1})_{j=1}^d in M_m.

For total-degree <=D polynomials F(Y_1,...,Y_d), this script forms

    A(F) = evaluation of F on the distinct points M_m,
    B(F) = coefficients of F(v_1-T, v_2-v_1*T, ..., v_d-v_{d-1}*T).

Then a degree-D separator exists iff

    ker(A) is not contained in ker(B)
    iff rank(A) < rank([A;B]).

A separator certifies the distinct-support bound

    |{theta in F_p : line(theta) in M_m}| <= D.

This is an exact finite/model certificate.  It enumerates C(n,m) subsets and
all total-degree <=D monomials, so it is not an asymptotic checker and it does
not implement the project's omitted 'above-reserve aperiodicity' predicate.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from math import comb
from typing import List, Sequence, Tuple


def trim(poly: List[int]) -> List[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def poly_mul(a: Sequence[int], b: Sequence[int], p: int, cap: int) -> List[int]:
    out = [0] * min(cap + 1, len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j > cap:
                break
            out[i + j] = (out[i + j] + ai * bj) % p
    return trim(out)


def poly_pow(a: Sequence[int], exponent: int, p: int, cap: int) -> List[int]:
    out = [1]
    base = list(a)
    e = exponent
    while e:
        if e & 1:
            out = poly_mul(out, base, p, cap)
        e >>= 1
        if e:
            base = poly_mul(base, base, p, cap)
    return out


def ceil_nth_root(value: int, exponent: int) -> int:
    """Least integer q with q**exponent >= value."""
    lo, hi = 1, 2
    while hi**exponent < value:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**exponent >= value:
            hi = mid
        else:
            lo = mid + 1
    return lo


def roots_of_unity(n: int, p: int) -> List[int]:
    return [x for x in range(1, p) if pow(x, n, p) == 1]


def subset_prefix(subset: Sequence[int], d: int, p: int) -> Tuple[int, ...]:
    poly = [1]
    for x in subset:
        poly = poly_mul(poly, [1, (-x) % p], p, d)
    return tuple(poly[i] if i < len(poly) else 0 for i in range(1, d + 1))


def inverse_prefix(uhat: Sequence[int], d: int, p: int) -> List[int]:
    if not uhat or uhat[0] % p != 1:
        raise ValueError("require u_0=1")
    u = [(uhat[i] if i < len(uhat) else 0) % p for i in range(d + 1)]
    v = [0] * (d + 1)
    v[0] = 1
    for j in range(1, d + 1):
        v[j] = (-sum(u[i] * v[j - i] for i in range(1, j + 1))) % p
    return v


def total_degree_exponents(d: int, D: int) -> List[Tuple[int, ...]]:
    out: List[Tuple[int, ...]] = []

    def rec(i: int, remaining: int, current: List[int]) -> None:
        if i == d:
            current.append(remaining)
            out.append(tuple(current))
            current.pop()
            return
        for exponent in range(remaining + 1):
            current.append(exponent)
            rec(i + 1, remaining - exponent, current)
            current.pop()

    # Include every exact total degree from 0 through D.
    for degree in range(D + 1):
        rec(1, degree, [])
    return out


def eval_monomial(point: Sequence[int], exponent: Sequence[int], p: int) -> int:
    value = 1
    for coordinate, power in zip(point, exponent):
        value = value * pow(coordinate, power, p) % p
    return value


def restrict_monomial(
    exponent: Sequence[int], v: Sequence[int], p: int, D: int
) -> List[int]:
    out = [1]
    for j, power in enumerate(exponent, start=1):
        # Y_j -> v_j - v_{j-1} T.
        line_coordinate = [v[j] % p, (-v[j - 1]) % p]
        out = poly_mul(out, poly_pow(line_coordinate, power, p, D), p, D)
    return out + [0] * (D + 1 - len(out))


def rref_mod(matrix: Sequence[Sequence[int]], p: int) -> Tuple[List[List[int]], List[int]]:
    if not matrix:
        return [], []
    a = [[entry % p for entry in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    pivots: List[int] = []
    pivot_row = 0
    for col in range(cols):
        found = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if found is None:
            continue
        a[pivot_row], a[found] = a[found], a[pivot_row]
        inv = pow(a[pivot_row][col], p - 2, p)
        a[pivot_row] = [(entry * inv) % p for entry in a[pivot_row]]
        for r in range(rows):
            if r == pivot_row or a[r][col] == 0:
                continue
            factor = a[r][col]
            a[r] = [(x - factor * y) % p for x, y in zip(a[r], a[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return a, pivots


def rank_mod(matrix: Sequence[Sequence[int]], p: int) -> int:
    return len(rref_mod(matrix, p)[1]) if matrix else 0


def nullspace_mod(matrix: Sequence[Sequence[int]], p: int) -> List[List[int]]:
    if not matrix:
        return []
    reduced, pivots = rref_mod(matrix, p)
    cols = len(matrix[0])
    free = [col for col in range(cols) if col not in pivots]
    basis: List[List[int]] = []
    for free_col in free:
        vector = [0] * cols
        vector[free_col] = 1
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = (-reduced[row][free_col]) % p
        basis.append(vector)
    return basis


def combine_restrictions(
    coefficients: Sequence[int], restrictions: Sequence[Sequence[int]], p: int
) -> List[int]:
    out = [0] * len(restrictions[0])
    for scalar, polynomial in zip(coefficients, restrictions):
        if scalar:
            for degree, value in enumerate(polynomial):
                out[degree] = (out[degree] + scalar * value) % p
    return trim(out)


def parse_uhat(text: str) -> List[int]:
    values = [int(piece.strip()) for piece in text.split(",") if piece.strip()]
    if not values:
        raise ValueError("uhat must contain u_0")
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--sigma", type=int, required=True)
    parser.add_argument("--s", type=int, required=True)
    parser.add_argument("--uhat", required=True, help="comma-separated u_0,u_1,...")
    parser.add_argument("--D", type=int, default=None)
    parser.add_argument("--max-subsets", type=int, default=2_000_000)
    parser.add_argument("--max-monomials", type=int, default=200_000)
    args = parser.parse_args()

    p, n, sigma, s = args.p, args.n, args.sigma, args.s
    d = sigma + 1
    m = n - s
    if (p - 1) % n != 0:
        raise SystemExit("require n | (p-1)")
    if not (0 <= s <= n):
        raise SystemExit("require 0 <= s <= n")
    if not (1 <= d < n):
        raise SystemExit("require 1 <= sigma+1 < n")

    # Uniform point-count threshold: dim P_{<=D0}(F_p^d) > 2^n > |M_m|.
    q = ceil_nth_root(2**n, d)
    D0 = d * (q - 1)
    D = D0 if args.D is None else args.D
    if D < 0:
        raise SystemExit("require D >= 0")

    subset_count = comb(n, m)
    monomial_count = comb(D + d, d)
    if subset_count > args.max_subsets:
        raise SystemExit(
            f"refusing to enumerate C({n},{m})={subset_count}; raise --max-subsets"
        )
    if monomial_count > args.max_monomials:
        raise SystemExit(
            f"refusing to build C({D+d},{d})={monomial_count} monomials; "
            "raise --max-monomials or lower --D"
        )

    H = roots_of_unity(n, p)
    if len(H) != n:
        raise SystemExit(f"expected {n} roots of unity, found {len(H)}")

    uhat = [value % p for value in parse_uhat(args.uhat)]
    v = inverse_prefix(uhat, d, p)
    points = sorted({subset_prefix(T, d, p) for T in combinations(H, m)})
    point_set = set(points)
    exponents = total_degree_exponents(d, D)

    A = [[eval_monomial(point, exponent, p) for exponent in exponents] for point in points]
    restrictions = [restrict_monomial(exponent, v, p, D) for exponent in exponents]
    B = [[restrictions[col][degree] for col in range(len(exponents))] for degree in range(D + 1)]

    rank_A = rank_mod(A, p)
    rank_stacked = rank_mod(A + B, p)
    kernel = nullspace_mod(A, p)

    separator = None
    nonzero_restrictions: List[List[int]] = []
    for vector in kernel:
        restricted = combine_restrictions(vector, restrictions, p)
        if any(restricted):
            nonzero_restrictions.append(restricted)
            if separator is None:
                separator = {
                    "terms": [
                        {"coefficient": coefficient, "exponents": list(exponent)}
                        for coefficient, exponent in zip(vector, exponents)
                        if coefficient
                    ],
                    "restriction_coefficients_low_to_high": restricted,
                    "restriction_degree": len(restricted) - 1,
                }

    active = []
    for theta in range(p):
        point = tuple((v[j] - theta * v[j - 1]) % p for j in range(1, d + 1))
        if point in point_set:
            active.append(theta)

    decision = "LINE_ESCAPES_DEGREE_D_CLOSURE" if rank_stacked > rank_A else "LINE_CONTAINED_IN_DEGREE_D_CLOSURE"
    result = {
        "decision": decision,
        "parameters": {"p": p, "n": n, "sigma": sigma, "d": d, "s": s, "m": m, "D": D},
        "uniform_dimension_threshold_D0": D0,
        "dimension_threshold_inequality": {
            "current_D_monomials": monomial_count,
            "D0_monomials": comb(D0 + d, d),
            "distinct_M_m_points": len(points),
            "all_subsets": subset_count,
            "two_to_n": 2**n,
        },
        "inverse_prefix_v_0_to_d": v,
        "ranks": {"A": rank_A, "stacked_A_B": rank_stacked},
        "relation_space_dimension": len(kernel),
        "active_theta_count": len(active),
        "active_thetas": active,
        "separator": separator,
        "scope": (
            "exact finite/model certificate; exhaustive enumeration; "
            "does not certify asymptotic aperiodicity or the official prize chain"
        ),
    }

    assert (rank_stacked > rank_A) == (separator is not None)
    if separator is not None:
        assert len(active) <= separator["restriction_degree"] <= D
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
