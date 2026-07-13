#!/usr/bin/env python3
"""Exact checks for the rank-15 hybrid recurrence and Pade wall.

The verifier uses only the Python standard library and integer arithmetic.
It rebuilds the pre-existing affine-section recurrence, composes the
directional two-flat and collision-class refinements, and then checks the
primitive-degree, second-pivot, field, denominator, and Pade ledgers.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from random import Random


P = 2_130_706_433
N = 2_097_152
K = 1_048_576
M = 1_116_047
TARGET = 274_854_110_496_187_592

EXPECTED_C153_MAX = 274_820_133_549_158_646


@dataclass(frozen=True)
class Row:
    n: int
    k: int
    s: int


@dataclass(frozen=True)
class RawScan:
    f14_at_zero: int
    states: tuple[int, ...]


@dataclass(frozen=True)
class HybridScan:
    lower_state: int
    values: tuple[int, ...]
    exact_p_evaluations: int
    skipped_p_evaluations: int

    def value(self, u: int) -> int:
        return self.values[u - self.lower_state]


def johnson_bound(row: Row, u: int) -> int | None:
    """Return the selected-support Johnson bound, when its determinant is positive."""
    n_u = row.n - u
    s_u = row.s - u
    determinant = s_u * s_u - n_u * (row.k - 1 - u)
    if determinant <= 0:
        return None
    return n_u * (row.s - row.k + 1) // determinant


def exact_one_flat(row: Row, u: int) -> int:
    incidence = (row.n - u) // (row.s - u)
    johnson = johnson_bound(row, u)
    return incidence if johnson is None else min(incidence, johnson)


def raw_rank15_scan(
    row: Row,
    threshold: int,
    *,
    inclusive: bool = False,
) -> RawScan:
    """Rebuild #703 through dimension 14 and select exact dimension-15 states."""
    previous = [1] * (row.k + 2)
    for dimension in range(1, 15):
        current = [0] * (row.k + 2)
        suffix_max = 0
        for u in range(row.k - dimension, -1, -1):
            candidate = (row.n - u) * previous[u + 1] // (row.s - u)
            johnson = johnson_bound(row, u)
            if johnson is not None:
                candidate = min(candidate, johnson)
            suffix_max = max(suffix_max, candidate)
            current[u] = suffix_max
        previous = current

    states: list[int] = []
    for u in range(row.k - 15 + 1):
        candidate = (row.n - u) * previous[u + 1] // (row.s - u)
        johnson = johnson_bound(row, u)
        if johnson is not None:
            candidate = min(candidate, johnson)
        passes_threshold = candidate >= threshold if inclusive else candidate > threshold
        if passes_threshold:
            states.append(u)
    return RawScan(f14_at_zero=previous[0], states=tuple(states))


def rich_direction_bound(list_size: int, richness: int) -> int:
    return list_size * ((list_size - 1) // (richness - 1)) // richness


def directional_capacity(row: Row, f1: list[int], u: int, list_size: int) -> int:
    n_u = row.n - u
    multiplicity = row.k - u - 1
    q_u = f1[u + 1]
    return n_u + sum(
        min(n_u, multiplicity * rich_direction_bound(list_size, richness))
        for richness in range(2, q_u + 1)
    )


def orientation(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    """Orientation for points (1/index, value), with denominators cleared."""
    ca, ya = a
    cb, yb = b
    cc, yc = c
    return (ca - cb) * cc * (yc - ya) - (yb - ya) * (ca - cc) * cb


def append_upper_hull(hull: list[tuple[int, int]], point: tuple[int, int]) -> None:
    while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) >= 0:
        hull.pop()
    hull.append(point)


def hull_lambda(
    hull: list[tuple[int, int]],
    t: int,
    prefix_max: int,
) -> tuple[int, int]:
    """Return max_c c(g(c)-R_t)_+/(c-t) as an unreduced fraction."""
    if not hull:
        return 0, 1

    low = 0
    high = len(hull) - 1
    while low < high:
        middle = (low + high) // 2
        c0, g0 = hull[middle]
        c1, g1 = hull[middle + 1]
        left = c0 * (g0 - prefix_max) * (c1 - t)
        right = c1 * (g1 - prefix_max) * (c0 - t)
        if left <= right:
            low = middle + 1
        else:
            high = middle

    c, value = hull[low]
    numerator = c * (value - prefix_max)
    if numerator <= 0:
        return 0, 1
    return numerator, c - t


def collision_p_bound(g: list[int], n_u: int, s_u: int, h: int, rank: int) -> int:
    """Evaluate the exact P_d collision-class upper hull."""
    c_max = len(g) - 1
    t_max = min(c_max, h // rank)
    assert t_max >= 1

    prefix = [0] * (t_max + 1)
    running = 0
    for c in range(1, t_max + 1):
        running = max(running, g[c])
        prefix[c] = running

    hull: list[tuple[int, int]] = []
    for c in range(c_max, t_max, -1):
        append_upper_hull(hull, (c, g[c]))

    best_numerator = 0
    best_denominator = 1
    for t in range(t_max, 0, -1):
        lambda_numerator, lambda_denominator = hull_lambda(hull, t, prefix[t])
        objective_numerator = (
            n_u * prefix[t] * lambda_denominator
            + (h - rank * t) * lambda_numerator
        )
        if objective_numerator * best_denominator > best_numerator * lambda_denominator:
            best_numerator = objective_numerator
            best_denominator = lambda_denominator
        append_upper_hull(hull, (t, g[t]))

    return best_numerator // (best_denominator * s_u)


def literal_collision_p_bound(
    g: list[int],
    n_u: int,
    s_u: int,
    h: int,
    rank: int,
) -> int:
    """Slow definition used only to audit the upper-hull implementation."""
    c_max = len(g) - 1
    t_max = min(c_max, h // rank)
    best_numerator = 0
    best_denominator = 1
    for t in range(1, t_max + 1):
        prefix_max = max(g[1 : t + 1])
        lambda_numerator = 0
        lambda_denominator = 1
        for c in range(t + 1, c_max + 1):
            numerator = c * max(g[c] - prefix_max, 0)
            denominator = c - t
            if numerator * lambda_denominator > lambda_numerator * denominator:
                lambda_numerator = numerator
                lambda_denominator = denominator
        objective_numerator = (
            n_u * prefix_max * lambda_denominator
            + (h - rank * t) * lambda_numerator
        )
        if objective_numerator * best_denominator > best_numerator * lambda_denominator:
            best_numerator = objective_numerator
            best_denominator = lambda_denominator
    return best_numerator // (best_denominator * s_u)


def small_collision_checks() -> int:
    rng = Random(20260713)
    checks = 0
    for c_max in range(2, 18):
        for _ in range(20):
            rank = rng.randint(1, min(7, c_max))
            h = c_max + rank - 1
            n_u = h + rng.randint(1, 30)
            s_u = rng.randint(1, n_u)
            g = [0] + [rng.randint(0, 40) for _ in range(c_max)]
            fast = collision_p_bound(g, n_u, s_u, h, rank)
            slow = literal_collision_p_bound(g, n_u, s_u, h, rank)
            assert fast == slow
            checks += 1
    return checks


def range_maxima(
    previous: list[int],
    row: Row,
    lower_state: int,
    dimension: int,
) -> tuple[list[int], list[int], list[int]]:
    """Build R*, its first maximizing index, and R0 for every parent state."""
    size = row.k - lower_state + 2
    child_upper = row.k - (dimension - 1)
    parent_upper = row.k - dimension

    suffix_value = [0] * size
    suffix_index = [0] * size
    maximum = -1
    maximizing_index = child_upper
    for v in range(child_upper, lower_state, -1):
        value = previous[v - lower_state]
        if value >= maximum:
            maximum = value
            maximizing_index = v
        suffix_value[v - lower_state] = maximum
        suffix_index[v - lower_state] = maximizing_index

    rank = dimension - 1
    short_max = [0] * size
    active: deque[int] = deque()
    right = lower_state
    for u in range(lower_state, parent_upper + 1):
        end = u + (row.k - u - 1) // rank
        while right < end:
            right += 1
            value = previous[right - lower_state]
            while active and previous[active[-1] - lower_state] <= value:
                active.pop()
            active.append(right)
        while active and active[0] < u + 1:
            active.popleft()
        short_max[u - lower_state] = previous[active[0] - lower_state]

    return suffix_value, suffix_index, short_max


def hybrid_tail(row: Row, lower_state: int) -> HybridScan:
    """Compute D_d(u), d<=15, on the dependency cone above lower_state."""
    assert 0 <= lower_state <= row.k - 15
    size = row.k - lower_state + 2

    d1 = [0] * size
    for u in range(lower_state, row.k):
        d1[u - lower_state] = exact_one_flat(row, u)

    f1 = [0] * (row.k + 2)
    maximum = 0
    for u in range(row.k - 1, lower_state - 1, -1):
        maximum = max(maximum, d1[u - lower_state])
        f1[u] = maximum

    previous = [0] * size
    for u in range(lower_state, row.k - 1):
        n_u = row.n - u
        s_u = row.s - u
        raw = n_u * f1[u + 1] // s_u
        johnson = johnson_bound(row, u)
        if johnson is not None:
            raw = min(raw, johnson)
        directional = raw
        while directional * s_u > directional_capacity(row, f1, u, directional):
            directional -= 1
        # At d=2, t=h makes P_2 at least the raw incidence bound, and Q_2
        # equals it. H_2 already includes Johnson, so D_2=H_2.
        previous[u - lower_state] = directional

    exact_p_evaluations = 0
    skipped_p_evaluations = 0
    for dimension in range(3, 16):
        rank = dimension - 1
        parent_upper = row.k - dimension
        suffix_value, suffix_index, short_max = range_maxima(
            previous, row, lower_state, dimension
        )
        current = [0] * size

        for u in range(lower_state, parent_upper + 1):
            offset = u - lower_state
            n_u = row.n - u
            s_u = row.s - u
            h = row.k - u - 1
            c_max = row.k - u - dimension + 1
            t_max = h // rank
            r_star = suffix_value[u + 1 - lower_state]
            r_zero = short_max[offset]

            q_bound = (h * r_star + (n_u - h) * r_zero) // s_u
            johnson = johnson_bound(row, u)
            candidate = q_bound if johnson is None else min(q_bound, johnson)

            # A single admissible t=t_max and the global maximizing child give
            # a certified lower bound on P_d. If it already reaches the other
            # bounds, constructing the exact upper hull cannot change D_d.
            if r_star == r_zero:
                p_lower = n_u * r_star // s_u
            else:
                c_star = suffix_index[u + 1 - lower_state] - u
                assert t_max < c_star <= c_max
                numerator = (
                    n_u * r_zero * (c_star - t_max)
                    + (h - rank * t_max) * c_star * (r_star - r_zero)
                )
                p_lower = numerator // ((c_star - t_max) * s_u)

            if p_lower >= candidate:
                current[offset] = candidate
                skipped_p_evaluations += 1
                continue

            g = [0] + [
                previous[u + c - lower_state] for c in range(1, c_max + 1)
            ]
            p_bound = collision_p_bound(g, n_u, s_u, h, rank)
            assert p_bound >= p_lower
            current[offset] = min(candidate, p_bound)
            exact_p_evaluations += 1

        previous = current

    return HybridScan(
        lower_state=lower_state,
        values=tuple(previous),
        exact_p_evaluations=exact_p_evaluations,
        skipped_p_evaluations=skipped_p_evaluations,
    )


def recurrence_value(row: Row, dimension: int) -> int:
    """Compute F_{s,dimension}(0) for a moderate-size row."""
    previous = [1] * (row.k + 2)
    for d in range(1, dimension + 1):
        current = [0] * (row.k + 2)
        suffix_max = 0
        for u in range(row.k - d, -1, -1):
            candidate = (row.n - u) * previous[u + 1] // (row.s - u)
            johnson = johnson_bound(row, u)
            if johnson is not None:
                candidate = min(candidate, johnson)
            suffix_max = max(suffix_max, candidate)
            current[u] = suffix_max
        previous = current
    return previous[0]


def second_pivot_checks(rank15_states: tuple[int, ...]) -> dict[str, int]:
    first_ceiling = 4_986
    first_values = [
        recurrence_value(Row(N - u, first_ceiling, M - u), 14)
        for u in rank15_states
    ]
    first_bound = max(first_values)
    first_argmax = rank15_states[first_values.index(first_bound)]

    c152_states = (1_043_403, 1_043_404, 1_043_405, 1_043_406)
    second_ceiling = 5_010
    second_values = [
        recurrence_value(Row(N - u, second_ceiling, M - u), 14)
        for u in c152_states
    ]
    second_bound = max(second_values)
    second_argmax = c152_states[second_values.index(second_bound)]

    return {
        "first_bound": first_bound,
        "first_argmax": first_argmax,
        "first_product": P * first_bound,
        "second_bound": second_bound,
        "second_argmax": second_argmax,
        "second_product": P * second_bound,
    }


def is_prime_by_trial_division(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def field_and_denominator_checks() -> dict[str, int]:
    assert P == 2**31 - 2**24 + 1
    assert is_prime_by_trial_division(P)
    assert (P - 1) % N == 0

    sextic_order = P**6
    budget = sextic_order // 2**128
    shell_denominator = P - N + M
    target = ((budget + 1) * shell_denominator - 1) // P
    assert sextic_order == 93_571_093_019_388_561_295_270_373_781_649_880_353_786_165_192_103_559_169
    assert budget == 274_980_728_111_395_087
    assert shell_denominator == 2_129_725_328
    assert target == TARGET
    return {
        "p": P,
        "subgroup_index": (P - 1) // N,
        "q_list": sextic_order,
        "budget": budget,
        "shell_denominator": shell_denominator,
        "target": target,
    }


def pade_checks() -> dict[str, int]:
    sigma = M - K
    error_count = N - M
    dual_dimension = N - K
    minor_ceiling = N + K - 2 * M - 1
    base_kernel = 14 * sigma - minor_ceiling
    generic_rectangular_kernel = 16 * sigma - dual_dimension

    assert sigma == 67_471
    assert error_count == 981_105
    assert dual_dimension == 1_048_576
    assert minor_ceiling == 913_633
    assert base_kernel == 30_961
    assert generic_rectangular_kernel == 30_960

    rng = Random(913633)
    algebra_checks = 0
    for _ in range(256):
        common_errors = rng.randint(0, min(error_count, minor_ceiling))
        primitive_degree = rng.randint(0, minor_ceiling - common_errors)
        cuts = sorted(rng.randint(0, primitive_degree) for _ in range(13))
        minimal_indices = [
            right - left
            for left, right in zip([0] + cuts, cuts + [primitive_degree])
        ]
        eta = (
            minor_ceiling - common_errors - primitive_degree
            + sum(max(index - sigma, 0) for index in minimal_indices)
        )
        bounded_kernel = sum(max(sigma - index, 0) for index in minimal_indices)
        assert bounded_kernel == base_kernel + common_errors + eta
        intersection = dual_dimension - 16 * sigma + bounded_kernel
        assert intersection == common_errors + 1 + eta
        assert intersection - common_errors == 1 + eta
        algebra_checks += 1

    return {
        "sigma": sigma,
        "error_count": error_count,
        "dual_dimension": dual_dimension,
        "minor_ceiling": minor_ceiling,
        "base_kernel": base_kernel,
        "generic_rectangular_kernel": generic_rectangular_kernel,
        "algebra_checks": algebra_checks,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")

    small_checks = small_collision_checks()
    field = field_and_denominator_checks()
    pade = pade_checks()

    deployed = Row(N, K, M)
    raw = raw_rank15_scan(deployed, TARGET)
    assert raw.f14_at_zero == 19_559_637_074_221_362
    assert raw.states == tuple(range(1_040_879, 1_043_583))

    hybrid = hybrid_tail(deployed, raw.states[0])
    unsafe = tuple(u for u in raw.states if hybrid.value(u) > TARGET)
    assert unsafe == tuple(range(1_042_375, 1_043_583))
    expected_deployed = {
        1_042_373: 274_848_095_090_415_020,
        1_042_374: 274_851_640_267_880_631,
        1_042_375: 274_858_628_070_449_169,
        1_042_376: 274_869_098_154_375_130,
        1_043_582: 283_039_300_733_528_044,
    }
    for u, expected in expected_deployed.items():
        assert hybrid.value(u) == expected

    c152_row = Row(N, K - 152, M)
    raw_c152 = raw_rank15_scan(c152_row, TARGET)
    hybrid_c152 = hybrid_tail(c152_row, raw_c152.states[0])
    unsafe_c152 = tuple(u for u in raw_c152.states if hybrid_c152.value(u) > TARGET)
    assert unsafe_c152 == (1_043_403, 1_043_404, 1_043_405, 1_043_406)
    expected_c152 = {
        1_043_403: 274_854_274_902_114_747,
        1_043_404: 274_857_797_694_413_816,
        1_043_405: 274_861_320_583_703_395,
        1_043_406: 274_864_843_569_987_490,
    }
    for u, expected in expected_c152.items():
        assert hybrid_c152.value(u) == expected

    c153_row = Row(N, K - 153, M)
    raw_c153 = raw_rank15_scan(c153_row, EXPECTED_C153_MAX, inclusive=True)
    hybrid_c153 = hybrid_tail(c153_row, raw_c153.states[0])
    c153_pairs = tuple((u, hybrid_c153.value(u)) for u in raw_c153.states)
    c153_max_u, c153_max = max(c153_pairs, key=lambda pair: pair[1])
    assert c153_max == EXPECTED_C153_MAX
    # Outside raw_c153.states, the old recurrence is smaller than this value;
    # the hybrid recurrence is pointwise no larger than the old recurrence.

    pivot = second_pivot_checks(unsafe)
    assert pivot["first_bound"] == 15_703_201
    assert pivot["first_product"] == 33_458_911_389_392_033 < TARGET
    assert pivot["second_bound"] == 45_706_459
    assert pivot["second_product"] == 97_387_046_220_950_747 < TARGET

    defect_floor = sum(range(13)) + 4_986 + 4_987 - 105
    c152_defect_floor = sum(range(13)) + 5_010 + 5_017 - 105
    endpoint_defect_floor = sum(range(13)) + 4_986 + 4_993 - 105
    assert defect_floor == 9_946
    assert c152_defect_floor == 10_000
    assert endpoint_defect_floor == 9_952

    print("RANK15_HYBRID_RECURRENCE_AND_PADE_WALL: PASS")
    print("small_collision_upper_hull_checks:", small_checks)
    print("field_ledger:", field)
    print(
        "raw_rank15_window:",
        f"{raw.states[0]}..{raw.states[-1]}",
        f"({len(raw.states)} states)",
    )
    print(
        "hybrid_rank15_unsafe:",
        f"{unsafe[0]}..{unsafe[-1]}",
        f"({len(unsafe)} states)",
    )
    print("hybrid_boundary_values:", expected_deployed)
    print(
        "hybrid_evaluator_work:",
        {
            "exact_P": hybrid.exact_p_evaluations,
            "certified_P_skips": hybrid.skipped_p_evaluations,
        },
    )
    print(
        "primitive_deficit_c153:",
        {"argmax_u": c153_max_u, "global_max": c153_max, "slack": TARGET - c153_max},
    )
    print(
        "primitive_deficit_c152:",
        {
            "unsafe_states": unsafe_c152,
            "values": expected_c152,
            "first_gap": expected_c152[unsafe_c152[0]] - TARGET,
        },
    )
    print("second_pivot:", pivot)
    print(
        "alternant_defect_floors:",
        {
            "all_survivors": defect_floor,
            "c152": c152_defect_floor,
            "u_1043582": endpoint_defect_floor,
        },
    )
    print("pade_ledger:", pade)
    print("nonclaim: recurrence values above T are failed upper bounds, not realized lists")
    print("nonclaim: affine dimension >=16 and the official endpoint remain unpaid")


if __name__ == "__main__":
    main()
