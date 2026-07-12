#!/usr/bin/env python3
"""Exact recurrence checks for the deployed affine-section rank reduction."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    n: int
    k: int
    s: int


def recurrence_rows(params: Parameters, max_dimension: int) -> list[int]:
    """Return F_{s,d}(0) for d=0,...,max_dimension."""
    n, k, s = params.n, params.k, params.s
    assert s >= k
    previous = [1] * (k + 2)
    values = [1]

    for dimension in range(1, max_dimension + 1):
        upper = k - dimension
        current = [0] * (k + 2)
        suffix_max = 0
        for u in range(upper, -1, -1):
            incidence = (n - u) * previous[u + 1] // (s - u)
            determinant = (s - u) ** 2 - (n - u) * (k - 1 - u)
            if determinant > 0:
                johnson = (n - u) * (s - k + 1) // determinant
                candidate = min(incidence, johnson)
            else:
                candidate = incidence
            suffix_max = max(suffix_max, candidate)
            current[u] = suffix_max
        previous = current
        values.append(current[0])
    return values


def slow_reference(params: Parameters, max_dimension: int) -> list[list[int]]:
    """Literal small-parameter recurrence used to check the suffix optimizer."""
    n, k, s = params.n, params.k, params.s
    rows = [[1] * (k + 2)]
    for dimension in range(1, max_dimension + 1):
        row = [0] * (k + 2)
        for z in range(k - dimension, -1, -1):
            candidates: list[int] = []
            for u in range(z, k - dimension + 1):
                incidence = (n - u) * rows[-1][u + 1] // (s - u)
                determinant = (s - u) ** 2 - (n - u) * (k - 1 - u)
                if determinant > 0:
                    johnson = (n - u) * (s - k + 1) // determinant
                    incidence = min(incidence, johnson)
                candidates.append(incidence)
            row[z] = max(candidates)
        rows.append(row)
    return rows


def small_checks() -> int:
    checks = 0
    for n in range(3, 18):
        for k in range(1, n + 1):
            for s in range(k, n + 1):
                max_dimension = min(5, k)
                fast = recurrence_rows(Parameters(n, k, s), max_dimension)
                slow = slow_reference(Parameters(n, k, s), max_dimension)
                assert fast == [row[0] for row in slow]
                checks += max_dimension + 1
    return checks


def deployed_checks() -> dict[str, int]:
    params = Parameters(n=2**21, k=2**20, s=1_116_047)
    values = recurrence_rows(params, 15)
    target = 274_854_110_496_187_592
    assert values[14] == 19_559_637_074_221_362
    assert values[15] == 284_377_931_860_724_492
    assert target - values[14] == 255_294_473_421_966_230
    assert values[15] - target == 9_523_821_364_536_900

    rows = 16 * params.s - params.n
    columns = 15 * params.k
    left_kernel = rows - (columns - 1)
    assert rows == 15_759_600
    assert columns == 15_728_640
    assert left_kernel == 30_961

    # Negative control: deleting the Johnson term changes the dimension-14 row.
    no_johnson = [1] * (params.k + 2)
    for dimension in range(1, 15):
        current = [0] * (params.k + 2)
        suffix_max = 0
        for u in range(params.k - dimension, -1, -1):
            candidate = (params.n - u) * no_johnson[u + 1] // (params.s - u)
            suffix_max = max(suffix_max, candidate)
            current[u] = suffix_max
        no_johnson = current
    assert no_johnson[0] != values[14]

    return {
        "F_m_14_0": values[14],
        "F_m_15_0": values[15],
        "target": target,
        "dimension_14_slack": target - values[14],
        "dimension_15_gap": values[15] - target,
        "matrix_rows": rows,
        "matrix_columns": columns,
        "left_kernel_floor": left_kernel,
    }


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")
    small = small_checks()
    deployed = deployed_checks()
    print("AFFINE_SECTION_ONE_ROW_RANK: PASS")
    print("small_recurrence_checks:", small)
    print("deployed:", deployed)
    print("tamper: omitted Johnson term rejected")


if __name__ == "__main__":
    main()
