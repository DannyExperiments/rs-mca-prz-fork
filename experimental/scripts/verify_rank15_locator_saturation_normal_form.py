#!/usr/bin/env python3
"""Replay the rank-15 two-flat locator-saturation arithmetic certificate.

Standard library only.  All verification gates use explicit exceptions, not
assert statements, so running with ``python -O`` cannot disable any check.
"""

from __future__ import annotations

import hashlib
import json
from math import comb


class VerificationError(RuntimeError):
    """Raised when a certificate or independent cross-check fails."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, "ceil_div requires a positive denominator")
    return -(-numerator // denominator)


P = 2**31 - 2**24 + 1
N_CODE = 2**21
K = 2**20
M_AGREEMENT = 1_116_047
U_UNIVERSAL = 1_043_596
Q = 15
N = N_CODE - U_UNIVERSAL
A = M_AGREEMENT - U_UNIVERSAL
LAMBDA = K - 1 - U_UNIVERSAL

EXPECTED_DEGREE_ROWS = (
    (212, 443_728, 609_828, 123, 3_717, 4_674, 4_674, 304),
    (213, 371_277, 682_279, 138, 3_807, 4_675, 4_675, 303),
    (214, 298_826, 754_730, 152, 3_949, 4_676, 4_676, 303),
    (215, 226_375, 827_181, 167, 4_089, 4_676, 4_676, 302),
    (216, 153_924, 899_632, 181, 4_228, 4_676, 4_676, 302),
    (217, 81_473, 972_083, 196, 4_480, 4_677, 4_677, 302),
    (218, 9_022, 1_044_534, 210, 4_792, 4_677, 4_792, 176),
)

EXPECTED_M218_LOCATOR_ROWS = (
    (210, 1_056, 4),
    (211, 6_035, 26),
    (212, 11_014, 48),
    (213, 15_993, 70),
    (214, 20_972, 91),
    (215, 25_951, 113),
    (216, 30_930, 134),
    (217, 35_909, 155),
    (218, 40_888, 176),
)

# Canonical payload hash.  This freezes every printed certificate field.
EXPECTED_CERTIFICATE_SHA256 = (
    "905e88942c3d8b8afc0fa47a346900d2e4da61dae82e96b98152660ce9127e2e"
)


def rich_direction_ceiling(list_size: int, occupancy: int) -> int:
    """B_j(M), including the essential nested floor."""
    require(2 <= occupancy <= list_size, "invalid rich-line occupancy")
    per_point = (list_size - 1) // (occupancy - 1)
    return list_size * per_point // occupancy


def direction_capacity(list_size: int, degree: int, coordinate_count: int) -> int:
    """The layer-cake direction capacity D_M(d,N_0)."""
    require(degree >= 0 and coordinate_count >= 0, "negative capacity input")
    return coordinate_count + sum(
        min(coordinate_count, degree * rich_direction_ceiling(list_size, j))
        for j in range(2, Q + 1)
    )


def full_chunk_upgrades(full_chunks: int, pair_budget: int, q: int = Q) -> int:
    """Closed formula U_q(f,B) for equal full-weight directions."""
    require(full_chunks >= 0 and pair_budget >= 0, "negative upgrade input")
    require(q >= 1, "q must be positive")
    if full_chunks == 0 or q == 1:
        return 0

    layer = max(
        level
        for level in range(q)
        if full_chunks * level * (level + 1) // 2 <= pair_budget
    )
    if layer == q - 1:
        return full_chunks * (q - 1)

    spent = full_chunks * layer * (layer + 1) // 2
    partial = min(full_chunks, (pair_budget - spent) // (layer + 1))
    return full_chunks * layer + partial


def pair_capacity(
    list_size: int,
    degree: int,
    coordinate_count: int,
    q: int = Q,
) -> int:
    """Exact optimum P_M(d,N_0) of the global pair-budget relaxation."""
    require(degree > 0, "pair capacity requires positive degree")
    require(coordinate_count >= 0, "negative coordinate count")
    require(1 <= q <= list_size, "invalid maximum occupancy")

    full_chunks, remainder = divmod(coordinate_count, degree)
    budget = comb(list_size, 2)
    if remainder == 0:
        return coordinate_count + degree * full_chunk_upgrades(
            full_chunks, budget, q
        )

    upgraded = max(
        remainder * (h - 1)
        + degree
        * full_chunk_upgrades(full_chunks, budget - comb(h, 2), q)
        for h in range(1, q + 1)
        if comb(h, 2) <= budget
    )
    return coordinate_count + upgraded


def pair_capacity_literal_dp(
    list_size: int,
    degree: int,
    coordinate_count: int,
    q: int,
) -> int:
    """Independent unbounded-direction DP for small pair relaxations.

    A DP item is one direction with coordinate weight c, line occupancy h,
    pair cost C(h,2), and objective contribution c*h.  Unlike pair_capacity,
    this code does not use the exchange reduction or upgrade layers.
    """
    require(degree > 0 and coordinate_count >= 0, "invalid DP dimensions")
    require(1 <= q <= list_size, "invalid DP occupancy")

    budget = comb(list_size, 2)
    unreachable = -1
    dp = [[unreachable] * (budget + 1) for _ in range(coordinate_count + 1)]
    dp[0][0] = 0

    for used in range(coordinate_count + 1):
        for spent, value in enumerate(dp[used]):
            if value == unreachable:
                continue
            max_weight = min(degree, coordinate_count - used)
            for weight in range(1, max_weight + 1):
                for occupancy in range(1, q + 1):
                    next_spent = spent + comb(occupancy, 2)
                    if next_spent > budget:
                        continue
                    candidate = value + weight * occupancy
                    if candidate > dp[used + weight][next_spent]:
                        dp[used + weight][next_spent] = candidate

    optimum = max(dp[coordinate_count])
    require(optimum >= 0, "literal DP found no feasible direction packing")
    return optimum


def minimum_passing_degree(capacity, list_size: int) -> int:
    required = list_size * A
    for degree in range(1, LAMBDA + 1):
        if capacity(list_size, degree, N) >= required:
            return degree
    raise VerificationError(f"no passing degree for M={list_size}")


def largest_capacity_compatible_r(list_size: int) -> int:
    """Exhaust all r after imposing d<=lambda-r and N_0=N-r."""
    required = list_size * A
    compatible: list[int] = []
    for inactive_roots in range(LAMBDA):
        degree = LAMBDA - inactive_roots
        coordinates = N - inactive_roots
        if (
            direction_capacity(list_size, degree, coordinates) >= required
            and pair_capacity(list_size, degree, coordinates) >= required
        ):
            compatible.append(inactive_roots)
    require(compatible, f"no capacity-compatible r for M={list_size}")
    return max(compatible)


def deployed_degree_rows() -> tuple[tuple[int, ...], ...]:
    rows = []
    for list_size in range(212, 219):
        delta = Q * N - list_size * A
        rich_coordinates = N - delta
        t_zero = ceil_div(rich_coordinates, LAMBDA)
        direction_floor = minimum_passing_degree(direction_capacity, list_size)
        pair_floor = minimum_passing_degree(pair_capacity, list_size)
        degree_floor = max(direction_floor, pair_floor)
        r_max = largest_capacity_compatible_r(list_size)
        rows.append(
            (
                list_size,
                delta,
                rich_coordinates,
                t_zero,
                direction_floor,
                pair_floor,
                degree_floor,
                r_max,
            )
        )
    result = tuple(rows)
    require(result == EXPECTED_DEGREE_ROWS, "deployed degree table mismatch")
    return result


def m218_locator_rows() -> tuple[tuple[int, ...], ...]:
    list_size = 218
    delta = Q * N - list_size * A
    rich_coordinates = N - delta
    rows = []
    for directions in range(210, 219):
        correction = LAMBDA * directions - rich_coordinates
        r_bound = correction // (directions + Q - 1)
        rows.append((directions, correction, r_bound))
    result = tuple(rows)
    require(result == EXPECTED_M218_LOCATOR_ROWS, "M=218 locator table mismatch")
    return result


def independent_pair_checks() -> int:
    all_cases = [
        (list_size, q, degree, coordinates)
        for list_size in range(3, 11)
        for q in range(2, min(5, list_size) + 1)
        for degree in range(1, 6)
        for coordinates in range(1, 16)
    ]
    require(len(all_cases) >= 1_200, "insufficient DP cases")
    cases = [all_cases[index * len(all_cases) // 1_200] for index in range(1_200)]
    require(len(set(cases)) == 1_200, "DP case selection contains duplicates")

    for case in cases:
        list_size, q, degree, coordinates = case
        formula = pair_capacity(list_size, degree, coordinates, q)
        literal = pair_capacity_literal_dp(list_size, degree, coordinates, q)
        require(formula == literal, f"pair-capacity mismatch at {case}")
    return len(cases)


def sharp_m218_certificate() -> dict[str, int]:
    list_size = 218
    degree = 4_792
    delta = Q * N - list_size * A
    rich_coordinates = N - delta

    require(217 * degree < rich_coordinates, "t=217 was not excluded")
    correction_budget = list_size * degree - rich_coordinates
    require(correction_budget == 122, "sharp correction budget mismatch")
    r_max = correction_budget // (Q - 1)
    require(r_max == 8, "sharp inactive-root bound mismatch")

    lines = list_size
    lines_per_point = (list_size - 1) // (Q - 1)
    require(lines_per_point == 15, "rich lines per point mismatch")
    uncovered_degree = list_size - 1 - lines_per_point * (Q - 1)
    uncovered_edges = comb(list_size, 2) - lines * comb(Q, 2)
    require(uncovered_degree == 7, "uncovered graph degree mismatch")
    require(
        uncovered_edges == list_size * uncovered_degree // 2 == 763,
        "uncovered graph edge count mismatch",
    )

    return {
        "M": list_size,
        "d": degree,
        "t": list_size,
        "b": lines,
        "r_max": r_max,
        "correction_at_r0": correction_budget,
        "correction_at_r8": correction_budget - (Q - 1) * r_max,
        "uncovered_degree": uncovered_degree,
        "uncovered_edges": uncovered_edges,
        "rich_pair_factors": lines * comb(Q, 2),
        "total_pair_factors": comb(list_size, 2),
    }


def tamper_controls() -> dict[str, bool]:
    controls = {
        "rich_line_2372_rejected": N + (Q - 1) * 2_372 < Q * A,
        "M212_d4673_rejected": pair_capacity(212, 4_673, N) < 212 * A,
        "M218_d4791_rejected": direction_capacity(218, 4_791, N) < 218 * A,
        "degree_4096_routes_rejected": all(
            pair_capacity(list_size, 4_096, N) < list_size * A
            for list_size in range(212, 219)
        ),
        "M218_d4792_r9_rejected": 218 * 4_792 < 1_044_534 + 14 * 9,
        "uncovered_edge_762_rejected": (
            comb(218, 2) - 218 * comb(15, 2) != 762
        ),
    }
    require(all(controls.values()), "one or more tamper controls failed")
    return controls


def build_certificate() -> dict[str, object]:
    require(P == 2_130_706_433, "deployed prime expression mismatch")
    require(N == 1_053_556, "residual coordinate count mismatch")
    require(A == 72_451, "outside-core agreement mismatch")
    require(LAMBDA == 4_979, "residual degree cap mismatch")
    require(comb(Q, 2) == 105, "rich-line pair count mismatch")
    require(LAMBDA // 2_373 == 2, "parallel rich-line cap mismatch")
    require(
        all(rich_direction_ceiling(list_size, Q) == list_size
            for list_size in range(212, 219)),
        "deployed rich-line packing cap mismatch",
    )

    threshold_numerator = Q * A - N
    rich_line_threshold = ceil_div(threshold_numerator, Q - 1)
    require(threshold_numerator == 33_209, "rich-line numerator mismatch")
    require(rich_line_threshold == 2_373, "rich-line threshold mismatch")
    require(
        N + (Q - 1) * (rich_line_threshold - 1) == Q * A - 1 == 1_086_764,
        "rich-line sharpness identity mismatch",
    )

    pair_checks = independent_pair_checks()
    certificate = {
        "status": "PROVED necessary normal form / AUDIT",
        "optimization_safe": True,
        "parameters": {
            "p": P,
            "n": N_CODE,
            "K": K,
            "m": M_AGREEMENT,
            "u": U_UNIVERSAL,
            "q": Q,
            "N": N,
            "a": A,
            "lambda": LAMBDA,
        },
        "rich_line": {
            "numerator": threshold_numerator,
            "threshold": rich_line_threshold,
            "sharp_previous_rhs": 1_086_764,
        },
        "degree_rows": deployed_degree_rows(),
        "m218_locator_rows": m218_locator_rows(),
        "sharp_m218_d4792": sharp_m218_certificate(),
        "pair_capacity_dp_checks": pair_checks,
        "tamper_controls": tamper_controls(),
    }
    return certificate


def canonical_hash(payload: dict[str, object]) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    certificate = build_certificate()
    digest = canonical_hash(certificate)
    if EXPECTED_CERTIFICATE_SHA256 != "TO_BE_FILLED":
        require(digest == EXPECTED_CERTIFICATE_SHA256, "certificate digest mismatch")

    print("RANK15_LOCATOR_SATURATION_NORMAL_FORM: PASS")
    print("status: PROVED necessary normal form / AUDIT")
    print("optimization_safe: yes (no assert-dependent logic)")
    params = certificate["parameters"]
    print("parameters:", json.dumps(params, sort_keys=True, separators=(",", ":")))
    print("rich_line:", json.dumps(certificate["rich_line"], sort_keys=True))
    print("degree_table:")
    print("M Delta W t0 d_dir d_pair d_min r_max")
    for row in certificate["degree_rows"]:
        print(" ".join(str(value) for value in row))
    print("m218_locator_table:")
    print("t correction r_max")
    for row in certificate["m218_locator_rows"]:
        print(" ".join(str(value) for value in row))
    print(
        "sharp_m218_d4792:",
        json.dumps(certificate["sharp_m218_d4792"], sort_keys=True),
    )
    print("pair_capacity_dp_checks:", certificate["pair_capacity_dp_checks"])
    print("tamper_controls:", sum(certificate["tamper_controls"].values()), "PASS")
    print("certificate_sha256:", digest)


if __name__ == "__main__":
    main()
