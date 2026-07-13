#!/usr/bin/env python3
"""Exact F_169 replay for the deep partial-occupancy counterexample.

This is a stdlib-only verifier.  It enumerates the complete canonical cell,
checks the analytic fixed-remainder image bound label by label, and records
the realized locator-prefix census.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
import sys


P = 13
ONE = 1


def enc(a: int, b: int) -> int:
    return (a % P) + P * (b % P)


def add(x: int, y: int) -> int:
    return enc(x % P + y % P, x // P + y // P)


def neg(x: int) -> int:
    return enc(-(x % P), -(x // P))


def mul(x: int, y: int) -> int:
    a, b = x % P, x // P
    c, d = y % P, y // P
    return enc(a * c + 2 * b * d, a * d + b * c)


def fpow(x: int, exponent: int) -> int:
    out = ONE
    while exponent:
        if exponent & 1:
            out = mul(out, x)
        x = mul(x, x)
        exponent >>= 1
    return out


def inv(x: int) -> int:
    assert x != 0
    return fpow(x, 167)


def div(x: int, y: int) -> int:
    return mul(x, inv(y))


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


def locator_prefix(support: list[int], depth: int) -> tuple[int, ...]:
    """Return the first `depth` coefficients after the monic leading term."""
    coeff = [ONE]
    for root in support:
        new = [0] * (len(coeff) + 1)
        for index, value in enumerate(coeff):
            new[index] = add(new[index], value)
            new[index + 1] = add(new[index + 1], neg(mul(value, root)))
        coeff = new
    assert len(coeff) == len(support) + 1
    return tuple(coeff[1 : depth + 1])


def field_and_fibers() -> tuple[list[tuple[int, int]], int]:
    assert pow(2, 6, 13) == 12  # T^2-2 is irreducible over F_13.

    theta = enc(2, 1)
    assert fpow(theta, 168) == ONE
    assert all(fpow(theta, 168 // prime) != ONE for prime in (2, 3, 7))
    assert fpow(theta, 7) == enc(0, 1)
    assert fpow(theta, 24) == enc(4, 1)
    assert fpow(theta, 56) == enc(3, 0)
    assert fpow(theta, 84) == enc(-1, 0)

    hgen = fpow(theta, 7)
    subgroup = [fpow(hgen, index) for index in range(24)]
    domain = [mul(theta, value) for value in subgroup]
    assert len(set(subgroup)) == len(set(domain)) == 24

    by_square: dict[int, list[int]] = {}
    for point in domain:
        by_square.setdefault(fpow(point, 2), []).append(point)
    assert len(by_square) == 12
    assert all(len(points) == 2 for points in by_square.values())

    eta = fpow(theta, 2)
    descended = {div(value, eta) for value in by_square}
    assert descended == set(range(1, 13))

    fibers = [tuple(sorted(by_square[value])) for value in sorted(by_square)]
    return fibers, theta


def enumerate_cell() -> Counter[tuple[int, ...]]:
    fibers, _ = field_and_fibers()
    counts: Counter[tuple[int, ...]] = Counter()
    indices = tuple(range(12))
    labels = 0

    for partial in combinations(indices, 4):
        partial_set = set(partial)
        remaining = tuple(index for index in indices if index not in partial_set)
        for mask in range(16):
            partial_points = [
                fibers[fiber_index][(mask >> bit) & 1]
                for bit, fiber_index in enumerate(partial)
            ]
            fixed_label_image: set[tuple[int, ...]] = set()
            for complete in combinations(remaining, 4):
                support = partial_points + [
                    point for fiber_index in complete for point in fibers[fiber_index]
                ]
                assert len(support) == 12
                prefix = locator_prefix(support, 3)
                counts[prefix] += 1
                fixed_label_image.add(prefix)

            # The theorem's fixed-label bound is |B_phi|^d=13^1.
            assert len(fixed_label_image) <= 13
            labels += 1

    assert labels == comb(12, 4) * 2**4 == 7_920
    return counts


def collision_floor(list_size: int) -> tuple[int, int]:
    q, n, k, challenge = 169, 24, 8, 168
    multiplicity = ceil_div(list_size * (q - n), q - n + k * (list_size - 1))
    return multiplicity, ceil_div(challenge * multiplicity, q)


def verify() -> None:
    counts = enumerate_cell()

    labels = comb(12, 4) * 2**4
    omega = labels * comb(8, 4)
    depth = min(4, 3 // 2)
    image_bound = labels * 13**depth
    guaranteed_list = ceil_div(comb(8, 4), 13**depth)
    identity_list = ceil_div(comb(24, 12), 169**3)

    assert labels == 7_920
    assert omega == 554_400
    assert image_bound == 102_960
    assert guaranteed_list == 6
    assert identity_list == 1

    assert sum(counts.values()) == omega
    assert len(counts) == 86_320
    assert max(counts.values()) == 20
    assert Fraction(omega, len(counts)) == Fraction(6_930, 1_079)
    assert len(counts) <= image_bound
    assert Fraction(omega, len(counts)) >= Fraction(comb(8, 4), 13)
    assert max(counts.values()) >= guaranteed_list

    assert collision_floor(6) == (5, 5)
    assert collision_floor(20) == (10, 10)
    assert min(168, 24 - 12 + 1) == 13

    print("field=F_13[T]/(T^2-2) theta=2+T domain=theta<theta^7>")
    print(f"labels={labels} supports={omega} analytic_image_bound={image_bound}")
    print(
        f"realized_image={len(counts)} max_fiber={max(counts.values())} "
        f"average={Fraction(omega, len(counts))}"
    )
    print(
        f"guaranteed_list={guaranteed_list} identity_floor={identity_list} "
        "pole_floor_L6=5 pole_floor_L20=10 tangent_floor=13"
    )
    print("RESULT: PASS")


def tamper_selftest() -> None:
    theta_bad = enc(1, 1)
    assert fpow(theta_bad, 28) == ONE
    assert fpow(theta_bad, 168 // 2) == ONE

    assert comb(12, 4) * 15 * comb(8, 4) == 519_750
    assert comb(12, 4) * 16 * comb(8, 4) == 554_400

    assert 7_920 * 169 == 1_338_480
    assert ceil_div(comb(8, 4), 169) == 1
    assert ceil_div(comb(8, 4), 13) == 6
    print("RESULT: PASS tamper-selftest 3/3")


def main() -> int:
    if not __debug__:
        raise RuntimeError("run without -O; this verifier uses assertions")
    if len(sys.argv) == 1 or sys.argv[1] == "--check":
        verify()
        return 0
    if sys.argv[1] == "--tamper-selftest":
        tamper_selftest()
        return 0
    print("usage: verify_deep_remainder_partial_occupancy_counterexample.py "
          "[--check | --tamper-selftest]")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
