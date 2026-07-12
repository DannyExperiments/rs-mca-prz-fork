#!/usr/bin/env python3
"""Exact checks for affine/projective interleaved shell compression."""

from __future__ import annotations

import itertools
import random
from typing import Iterable, Sequence

Vec = tuple[int, ...]
TupleCodeword = tuple[Vec, ...]


def eval_poly(coeffs: Sequence[int], x: int, p: int) -> int:
    out = 0
    for coeff in reversed(coeffs):
        out = (out * x + coeff) % p
    return out


def rs_code(p: int, domain: Sequence[int], k: int) -> list[Vec]:
    return [
        tuple(eval_poly(coeffs, x, p) for x in domain)
        for coeffs in itertools.product(range(p), repeat=k)
    ]


def add_scaled(rows: Sequence[Vec], coeffs: Sequence[int], p: int) -> Vec:
    return tuple(
        sum(coeff * row[x] for coeff, row in zip(coeffs, rows)) % p
        for x in range(len(rows[0]))
    )


def agreement_mask(row: Vec, codeword: Vec) -> int:
    mask = 0
    for i, (left, right) in enumerate(zip(row, codeword)):
        if left == right:
            mask |= 1 << i
    return mask


def one_row_list_size(row: Vec, code: Sequence[Vec], s: int) -> int:
    return sum(agreement_mask(row, word).bit_count() >= s for word in code)


def common_list(rows: Sequence[Vec], code: Sequence[Vec], s: int) -> list[TupleCodeword]:
    masks = [[agreement_mask(row, word) for word in code] for row in rows]
    full = (1 << len(rows[0])) - 1
    listed: list[TupleCodeword] = []
    for indices in itertools.product(range(len(code)), repeat=len(rows)):
        common = full
        for i, index in enumerate(indices):
            common &= masks[i][index]
        if common.bit_count() >= s:
            listed.append(tuple(code[index] for index in indices))
    return listed


def projective_directions(p: int, r: int) -> list[tuple[int, ...]]:
    directions: list[tuple[int, ...]] = []
    for vector in itertools.product(range(p), repeat=r):
        if not any(vector):
            continue
        first = next(value for value in vector if value)
        inverse = pow(first, -1, p)
        normalized = tuple(value * inverse % p for value in vector)
        if normalized not in directions:
            directions.append(normalized)
    return directions


def pi(p: int, j: int) -> int:
    return sum(p**i for i in range(j + 1))


def verify_instance(
    p: int,
    domain: Sequence[int],
    k: int,
    rows: Sequence[Vec],
    s: int,
) -> tuple[int, int, int]:
    n = len(domain)
    r = len(rows)
    code = rs_code(p, domain, k)
    listed = common_list(rows, code, s)

    affine_lhs = 0
    for words in listed:
        tail = (1 << n) - 1
        for row, word in zip(rows[1:], words[1:]):
            tail &= agreement_mask(row, word)
        affine_lhs += p ** (r - 2) * (p - n + tail.bit_count())

    affine_rhs = 0
    for tail_coeffs in itertools.product(range(p), repeat=r - 1):
        coeffs = (1,) + tail_coeffs
        affine_rhs += one_row_list_size(add_scaled(rows, coeffs, p), code, s)
    assert affine_lhs <= affine_rhs

    directions = projective_directions(p, r)
    projective_rhs = sum(
        one_row_list_size(add_scaled(rows, direction, p), code, s)
        for direction in directions
    )
    denominator = pi(p, r - 1) - (n - s) * pi(p, r - 2)
    assert denominator > 0
    assert denominator * len(listed) <= projective_rhs

    subset = listed[::2]
    if r == 2:
        subset_lhs = 0
        for first, second in subset:
            support = agreement_mask(rows[1], second).bit_count()
            subset_lhs += p - n + support
        assert subset_lhs <= affine_rhs

    return 1, len(listed), affine_rhs


def exhaustive_checks() -> tuple[int, int]:
    theorem_checks = listed_tuples = 0
    configurations = [
        (2, (0, 1), 1, 2),
        (2, (0, 1), 1, 3),
        (3, (0, 1, 2), 1, 2),
        (3, (0, 1, 2), 2, 2),
    ]
    for p, domain, k, r in configurations:
        rows = list(itertools.product(range(p), repeat=len(domain)))
        for received in itertools.product(rows, repeat=r):
            for s in range(k, len(domain) + 1):
                checks, count, _ = verify_instance(p, domain, k, received, s)
                theorem_checks += checks
                listed_tuples += count
    return theorem_checks, listed_tuples


def sampled_checks() -> tuple[int, int]:
    rng = random.Random(20260712)
    theorem_checks = listed_tuples = 0
    for p, domain, k, r, samples in [
        (5, (0, 1, 2, 3), 2, 2, 120),
        (5, (0, 1, 2, 3), 2, 3, 80),
    ]:
        for _ in range(samples):
            received = tuple(
                tuple(rng.randrange(p) for _ in domain) for _ in range(r)
            )
            s = rng.randrange(k, len(domain) + 1)
            checks, count, _ = verify_instance(p, domain, k, received, s)
            theorem_checks += checks
            listed_tuples += count
    return theorem_checks, listed_tuples


def deployed_arithmetic() -> dict[str, int]:
    p = 2**31 - 2**24 + 1
    q = p**6
    n = 2**21
    k = 2**20
    m = 1_116_047
    budget = q // 2**128
    denominator = p - n + m
    threshold = ((budget + 1) * denominator - 1) // p
    assert p == 2_130_706_433
    assert budget == 274_980_728_111_395_087
    assert denominator == 2_129_725_328
    assert threshold == 274_854_110_496_187_592
    assert budget - threshold == 126_617_615_207_495

    projective: dict[int, int] = {}
    for rank in (1, 2, 3, 6, 12):
        if rank == 1:
            projective[rank] = budget
            continue
        numerator = pi(p, rank - 1)
        den = numerator - (n - m) * pi(p, rank - 2)
        projective[rank] = ((budget + 1) * den - 1) // numerator
    assert projective == {
        1: 274_980_728_111_395_087,
        2: 274_854_110_496_247_017,
        3: 274_854_110_496_187_592,
        6: 274_854_110_496_187_592,
        12: 274_854_110_496_187_592,
    }
    return {
        "p": p,
        "q": q,
        "n": n,
        "k": k,
        "m": m,
        "budget": budget,
        "denominator": denominator,
        "threshold": threshold,
        **{f"projective_rank_{rank}": value for rank, value in projective.items()},
    }


def denominator_tamper() -> None:
    p = 3
    domain = (0, 1, 2)
    k = 1
    s = len(domain)
    rows = ((0, 0, 0), (0, 0, 0))
    code = rs_code(p, domain, k)
    listed = common_list(rows, code, s)
    rhs = sum(
        one_row_list_size(add_scaled(rows, (1, lam), p), code, s)
        for lam in range(p)
    )
    exact_denominator = p - len(domain) + s
    assert exact_denominator * len(listed) == rhs
    assert (exact_denominator + 1) * len(listed) > rhs


def main() -> None:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")
    exhaustive, exhaustive_lists = exhaustive_checks()
    sampled, sampled_lists = sampled_checks()
    arithmetic = deployed_arithmetic()
    denominator_tamper()
    print("AFFINE_INTERLEAVED_SHELL_COMPRESSION: PASS")
    print("exhaustive:", {
        "theorem_checks": exhaustive,
        "listed_tuples": exhaustive_lists,
    })
    print("sampled:", {
        "theorem_checks": sampled,
        "listed_tuples": sampled_lists,
    })
    print("deployed:", arithmetic)
    print("tamper: denominator +1 rejected")


if __name__ == "__main__":
    main()
