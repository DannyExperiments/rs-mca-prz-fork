#!/usr/bin/env python3
"""Verify the signed local-minority fixed-composition theorem.

The checker is stdlib-only.  It derives all caps from the theorem's formulas,
checks the deployed integers exactly, exhausts small prime-field profiles, and
contains negative fixtures for the sign, shadow, Plotkin, and zero hypotheses.
It does not verify an all-profile compiler, a ray theorem, or a prize bound.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import comb, factorial, gcd, isqrt, prod
import sys
from typing import Iterable


class VerificationError(RuntimeError):
    """Raised when an exact check fails."""


def require(condition: bool, message: str) -> None:
    """Always-active replacement for assertion-based certificate checks."""
    if not condition:
        raise VerificationError(message)


def ceil_div(numerator: int, denominator: int) -> int:
    require(denominator > 0, "ceil_div denominator must be positive")
    return (numerator + denominator - 1) // denominator


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    for divisor in range(3, isqrt(value) + 1, 2):
        if value % divisor == 0:
            return False
    return True


def prime_factors(value: int) -> tuple[int, ...]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return tuple(factors)


def primitive_root(prime: int) -> int:
    require(is_prime(prime), "primitive_root requires a prime")
    factors = prime_factors(prime - 1)
    for candidate in range(2, prime):
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return candidate
    raise VerificationError("primitive root not found")


def vector_sum(
    vectors: Iterable[tuple[int, ...]], prime: int, width: int
) -> tuple[int, ...]:
    result = [0] * width
    for vector in vectors:
        require(len(vector) == width, "vector width mismatch")
        for index, value in enumerate(vector):
            result[index] = (result[index] + value) % prime
    return tuple(result)


def signed_vector_sum(
    offset: tuple[int, ...],
    terms: Iterable[tuple[int, tuple[int, ...]]],
    prime: int,
) -> tuple[int, ...]:
    result = list(offset)
    for sign, vector in terms:
        require(sign in (-1, 1), "invalid sign")
        require(len(vector) == len(result), "signed vector width mismatch")
        for index, value in enumerate(vector):
            result[index] = (result[index] + sign * value) % prime
    return tuple(result)


def power_sums(
    support: Iterable[int], prime: int, width: int
) -> tuple[int, ...]:
    points = tuple(support)
    return tuple(
        sum(pow(point, exponent, prime) for point in points) % prime
        for exponent in range(1, width + 1)
    )


@dataclass(frozen=True)
class Profile:
    q: int
    occupancies: tuple[int, ...]
    partial_indices: tuple[int, ...]
    minority_sizes: tuple[int, ...]
    signs: tuple[int, ...]
    total_minority: int
    positive_mass: int
    negative_mass: int
    block_variance: int
    support_size: int
    profile_size: int


def make_profile(q: int, occupancies: tuple[int, ...]) -> Profile:
    require(q > 0, "block size must be positive")
    require(all(0 <= value <= q for value in occupancies), "bad occupancy")
    partial_indices = tuple(
        index for index, value in enumerate(occupancies) if 0 < value < q
    )
    minority_sizes = tuple(
        min(occupancies[index], q - occupancies[index])
        for index in partial_indices
    )
    signs = tuple(
        1 if 2 * occupancies[index] <= q else -1
        for index in partial_indices
    )
    positive_mass = sum(
        size for size, sign in zip(minority_sizes, signs) if sign == 1
    )
    negative_mass = sum(
        size for size, sign in zip(minority_sizes, signs) if sign == -1
    )
    return Profile(
        q=q,
        occupancies=occupancies,
        partial_indices=partial_indices,
        minority_sizes=minority_sizes,
        signs=signs,
        total_minority=sum(minority_sizes),
        positive_mass=positive_mass,
        negative_mass=negative_mass,
        block_variance=sum(value * (q - value) for value in occupancies),
        support_size=sum(occupancies),
        profile_size=prod(comb(q, value) for value in occupancies),
    )


def exact_profile_supports(
    blocks: tuple[tuple[int, ...], ...], profile: Profile
) -> list[frozenset[int]]:
    require(len(blocks) == len(profile.occupancies), "profile block count")
    require(all(len(block) == profile.q for block in blocks), "unequal blocks")
    local_choices = [
        tuple(frozenset(choice) for choice in combinations(block, occupancy))
        for block, occupancy in zip(blocks, profile.occupancies)
    ]
    supports = [
        frozenset().union(*choices) for choices in product(*local_choices)
    ]
    require(len(supports) == profile.profile_size, "profile support census")
    return supports


def minority_sets(
    support: frozenset[int],
    blocks: tuple[tuple[int, ...], ...],
    profile: Profile,
) -> tuple[frozenset[int], ...]:
    result: list[frozenset[int]] = []
    for index, sign in zip(profile.partial_indices, profile.signs):
        block = frozenset(blocks[index])
        local = support & block
        minority = local if sign == 1 else block - local
        result.append(minority)
    require(
        tuple(map(len, result)) == profile.minority_sizes,
        "minority size mismatch",
    )
    return tuple(result)


def fixed_offset(
    blocks: tuple[tuple[int, ...], ...],
    profile: Profile,
    prime: int,
    width: int,
) -> tuple[int, ...]:
    dense_block_moments = (
        power_sums(block, prime, width)
        for block, occupancy in zip(blocks, profile.occupancies)
        if 2 * occupancy > profile.q
    )
    return vector_sum(dense_block_moments, prime, width)


def signed_normal_form(
    support: frozenset[int],
    blocks: tuple[tuple[int, ...], ...],
    profile: Profile,
    prime: int,
    width: int,
) -> tuple[int, ...]:
    offset = fixed_offset(blocks, profile, prime, width)
    minorities = minority_sets(support, blocks, profile)
    return signed_vector_sum(
        offset,
        (
            (sign, power_sums(minority, prime, width))
            for sign, minority in zip(profile.signs, minorities)
        ),
        prime,
    )


def swapped_collision_sets(
    left: tuple[frozenset[int], ...],
    right: tuple[frozenset[int], ...],
    signs: tuple[int, ...],
) -> tuple[frozenset[int], frozenset[int]]:
    a_parts: list[frozenset[int]] = []
    b_parts: list[frozenset[int]] = []
    for left_local, right_local, sign in zip(left, right, signs):
        if sign == 1:
            a_parts.append(left_local)
            b_parts.append(right_local)
        else:
            a_parts.append(right_local)
            b_parts.append(left_local)
    return frozenset().union(*a_parts), frozenset().union(*b_parts)


def johnson_distance(left: frozenset[int], right: frozenset[int]) -> int:
    require(len(left) == len(right), "Johnson distance requires equal sizes")
    return len(left - right)


def shadow_cap(q: int, minority_sizes: tuple[int, ...], width: int) -> int:
    best: int | None = None
    for retained in product(*(range(size + 1) for size in minority_sizes)):
        if sum(size - value for size, value in zip(minority_sizes, retained)) > width:
            continue
        numerator = prod(comb(q, value) for value in retained)
        denominator = prod(
            comb(size, value)
            for size, value in zip(minority_sizes, retained)
        )
        candidate = numerator // denominator
        best = candidate if best is None else min(best, candidate)
    require(best is not None, "shadow admissible set is empty")
    require(best >= 1, "shadow cap must be positive")
    return best


def plotkin_cap(profile: Profile, width: int) -> int | None:
    delta_q = (width + 1) * profile.q
    if profile.block_variance < delta_q:
        return delta_q // (delta_q - profile.block_variance)
    if profile.block_variance == delta_q:
        return 2 * len(profile.partial_indices) * (profile.q - 1)
    return None


def theorem_cap(profile: Profile, width: int) -> tuple[int, int, int | None]:
    shadow = shadow_cap(profile.q, profile.minority_sizes, width)
    plotkin = plotkin_cap(profile, width)
    cap = shadow if plotkin is None else min(shadow, plotkin)
    require(cap >= 1, "theorem cap must be positive")
    return cap, shadow, plotkin


def fiber_map(
    supports: Iterable[frozenset[int]], prime: int, width: int
) -> dict[tuple[int, ...], list[frozenset[int]]]:
    fibers: dict[tuple[int, ...], list[frozenset[int]]] = defaultdict(list)
    for support in supports:
        fibers[power_sums(support, prime, width)].append(support)
    return dict(fibers)


def verify_exact_profile(
    blocks: tuple[tuple[int, ...], ...],
    occupancies: tuple[int, ...],
    prime: int,
    width: int,
) -> Counter[str]:
    profile = make_profile(len(blocks[0]), occupancies)
    supports = exact_profile_supports(blocks, profile)
    offset = fixed_offset(blocks, profile, prime, width)
    counts: Counter[str] = Counter()

    for support in supports:
        require(
            power_sums(support, prime, width)
            == signed_normal_form(support, blocks, profile, prime, width),
            "signed affine normal form",
        )
        counts["affine_checks"] += 1

    fibers = fiber_map(supports, prime, width)
    cap, shadow, plotkin = theorem_cap(profile, width)
    maximum = max(map(len, fibers.values()))
    require(maximum <= cap, "exact profile fiber cap")
    require(
        len(fibers) >= ceil_div(profile.profile_size, cap),
        "realized image lower bound",
    )
    counts["cap_checks"] += 2

    for family in fibers.values():
        for left_support, right_support in combinations(family, 2):
            left = minority_sets(left_support, blocks, profile)
            right = minority_sets(right_support, blocks, profile)
            a_set, b_set = swapped_collision_sets(left, right, profile.signs)
            require(
                len(a_set) == len(b_set) == profile.total_minority,
                "swapped collision cardinality",
            )
            require(
                power_sums(a_set, prime, width)
                == power_sums(b_set, prime, width),
                "swapped collision power sums",
            )
            product_distance = sum(
                len(left_local - right_local)
                for left_local, right_local in zip(left, right)
            )
            require(
                product_distance == johnson_distance(a_set, b_set),
                "product-Johnson identity",
            )
            require(
                product_distance >= width + 1,
                "same-fiber product-Johnson distance",
            )
            counts["collision_pair_checks"] += 4

    residual = [
        support for index, support in enumerate(supports) if index % 3 != 1
    ]
    require(residual, "deterministic residual must be nonempty")
    residual_fibers = fiber_map(residual, prime, width)
    residual_maximum = max(map(len, residual_fibers.values()))
    require(residual_maximum <= cap, "hereditary absolute cap")
    require(
        residual_maximum * len(residual_fibers) <= cap * len(residual),
        "residual-own-image Q normalization",
    )
    for moment in (2, 3):
        require(
            sum(len(family) ** moment for family in residual_fibers.values())
            <= cap ** (moment - 1) * len(residual),
            "hereditary fiber moment",
        )
    counts["hereditary_checks"] += 4

    zero = (0,) * width
    if (
        offset == zero
        and profile.partial_indices
        and profile.positive_mass <= width
        and profile.negative_mass <= width
    ):
        require(zero not in fibers, "split-sign zero exclusion")
        counts["split_zero_checks"] += 1

    delta_q = (width + 1) * profile.q
    if profile.block_variance < delta_q:
        counts["strict_profiles"] += 1
    elif profile.block_variance == delta_q:
        counts["equality_profiles"] += 1
    else:
        counts["beyond_plotkin_profiles"] += 1
    if offset != zero:
        counts["nonzero_offset_profiles"] += 1
    if any(sign == -1 for sign in profile.signs):
        counts["dense_profiles"] += 1
    if shadow > 1:
        counts["nontrivial_shadow_profiles"] += 1
    if plotkin is not None:
        counts["finite_plotkin_profiles"] += 1
    counts["profiles"] += 1
    counts["supports"] += len(supports)
    return counts


def verify_general_exhaustive() -> Counter[str]:
    prime = 13
    q = 3
    blocks = tuple(
        tuple(range(1 + q * index, 1 + q * (index + 1)))
        for index in range(4)
    )
    require(
        frozenset().union(*(frozenset(block) for block in blocks))
        == frozenset(range(1, prime)),
        "general fixture partition",
    )
    totals: Counter[str] = Counter()
    for width in (1, 2, 3):
        for occupancies in product(range(q + 1), repeat=len(blocks)):
            totals.update(
                verify_exact_profile(blocks, occupancies, prime, width)
            )
    require(totals["profiles"] == 3 * 4**4, "general profile count")
    require(totals["strict_profiles"] > 0, "strict branch not exercised")
    require(totals["equality_profiles"] > 0, "equality branch not exercised")
    require(
        totals["beyond_plotkin_profiles"] > 0,
        "beyond-Plotkin branch not exercised",
    )
    require(
        totals["nonzero_offset_profiles"] > 0,
        "affine offset branch not exercised",
    )
    require(totals["dense_profiles"] > 0, "dense sign branch not exercised")
    require(
        totals["nontrivial_shadow_profiles"] > 0,
        "nontrivial shadow branch not exercised",
    )
    require(
        totals["split_zero_checks"] > 0,
        "split zero branch not exercised",
    )
    return totals


def multiplicative_cosets(
    prime: int, q: int
) -> tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    require((prime - 1) % q == 0, "subgroup order must divide p-1")
    generator = primitive_root(prime)
    h_generator = pow(generator, (prime - 1) // q, prime)
    subgroup = tuple(sorted(pow(h_generator, index, prime) for index in range(q)))
    require(len(set(subgroup)) == q, "subgroup order")
    unseen = set(range(1, prime))
    blocks: list[tuple[int, ...]] = []
    while unseen:
        representative = min(unseen)
        block = tuple(
            sorted((representative * value) % prime for value in subgroup)
        )
        require(len(set(block)) == q, "coset size")
        blocks.append(block)
        unseen.difference_update(block)
    return subgroup, tuple(blocks)


def occupancy_of(
    support: frozenset[int], blocks: tuple[tuple[int, ...], ...]
) -> tuple[int, ...]:
    return tuple(len(support & frozenset(block)) for block in blocks)


def verify_cyclic_exhaustive() -> Counter[str]:
    prime = 13
    q = 4
    subgroup, blocks = multiplicative_cosets(prime, q)
    require(len(blocks) == 3, "cyclic fixture block count")
    totals: Counter[str] = Counter()

    for width in (1, 2, 3):
        require(q > width, "cyclic fixture requires q>w")
        zero = (0,) * width
        for block in blocks:
            require(
                power_sums(block, prime, width) == zero,
                "complete coset moments",
            )
            totals["complete_coset_checks"] += 1

        for occupancies in product(range(q + 1), repeat=len(blocks)):
            profile = make_profile(q, occupancies)
            supports = exact_profile_supports(blocks, profile)
            cap, _, _ = theorem_cap(profile, width)
            offset = fixed_offset(blocks, profile, prime, width)
            require(offset == zero, "cyclic complete-block offset")
            zero_supports = [
                support
                for support in supports
                if power_sums(support, prime, width) == zero
            ]
            local_gcd = reduce(gcd, (q, *occupancies))
            exclusion_fires = (
                profile.block_variance < (q - local_gcd) * (width + 1)
                or cap * local_gcd < q
            )
            if exclusion_fires:
                require(not zero_supports, "cyclic zero exclusion")
                totals["cyclic_exclusion_profiles"] += 1
            if (
                profile.partial_indices
                and profile.positive_mass <= width
                and profile.negative_mass <= width
            ):
                require(not zero_supports, "cyclic split-sign exclusion")
                totals["cyclic_split_profiles"] += 1

            for support in zero_supports:
                stabilizer = tuple(
                    value
                    for value in subgroup
                    if frozenset(
                        (value * point) % prime for point in support
                    )
                    == support
                )
                k = len(stabilizer)
                require(k > 0 and q % k == 0, "stabilizer order")
                require(
                    all(value % k == 0 for value in occupancies),
                    "stabilizer divides occupancies",
                )
                require(local_gcd % k == 0, "stabilizer divides profile gcd")

                rotations = tuple(
                    frozenset((value * point) % prime for point in support)
                    for value in subgroup
                )
                require(
                    sum(johnson_distance(support, rotated) for rotated in rotations)
                    == profile.block_variance,
                    "cyclic distance budget identity",
                )
                orbit = frozenset(rotations)
                require(len(orbit) == q // k, "orbit-stabilizer")
                require(len(orbit) <= cap, "orbit fiber bounded by theorem cap")
                for rotated in orbit:
                    require(
                        occupancy_of(rotated, blocks) == occupancies,
                        "rotation preserves labeled profile",
                    )
                    require(
                        power_sums(rotated, prime, width) == zero,
                        "rotation preserves zero target",
                    )
                    if rotated != support:
                        require(
                            johnson_distance(support, rotated) >= width + 1,
                            "nontrivial zero rotation distance",
                        )
                require(
                    profile.block_variance >= (q - k) * (width + 1),
                    "cyclic zero variance lower bound",
                )
                totals["zero_supports"] += 1
                totals["cyclic_zero_checks"] += 8 + 3 * len(orbit)
                if profile.partial_indices:
                    totals["nontrivial_zero_supports"] += 1

            totals["profiles"] += 1
            totals["supports"] += len(supports)

    require(totals["profiles"] == 3 * 5**3, "cyclic profile count")
    require(
        totals["cyclic_exclusion_profiles"] > 0,
        "cyclic exclusion not exercised",
    )
    require(
        totals["nontrivial_zero_supports"] > 0,
        "cyclic nontrivial zeros not exercised",
    )
    return totals


def ratio_power_exceeds_two_power(
    numerator: int, denominator: int, exponent: int, bits: int
) -> bool:
    require(
        numerator > denominator > 0 and exponent > 0 and bits >= 0,
        "ratio comparison preconditions",
    )
    return pow(numerator, exponent) > (1 << bits) * pow(denominator, exponent)


def verify_deployed() -> dict[str, int]:
    prime = 2_130_706_433
    n = 2_097_152
    m = 981_104
    width = 67_471
    delta = width + 1
    q = 1 << 17
    block_count = n // q

    require(is_prime(prime), "deployed modulus is not prime")
    require(prime - 1 == 1016 * n, "deployed multiplicative-domain divisor")
    require(block_count == 16 and q * block_count == n, "deployed block scale")
    require(prime > width and q > width, "deployed characteristic/block gate")

    nine = (
        129_214,
        *(129_215 for _ in range(6)),
        38_300,
        38_300,
        *(0 for _ in range(7)),
    )
    nine_profile = make_profile(q, nine)
    require(len(nine) == block_count, "nine-partial vector length")
    require(nine_profile.support_size == m, "nine-partial support size")
    require(len(nine_profile.partial_indices) == 9, "nine partial blocks")
    require(
        nine_profile.minority_sizes
        == (1_858, *(1_857 for _ in range(6)), 38_300, 38_300),
        "nine-partial minority vector",
    )
    require(nine_profile.negative_mass == 13_000, "nine negative mass")
    require(nine_profile.positive_mass == 76_600, "nine positive mass")
    require(nine_profile.total_minority == 89_600, "nine total minority")
    require(nine_profile.total_minority > width, "nine profile is noninjective")
    require(nine_profile.block_variance == 8_786_128_342, "nine B_r")

    delta_q = delta * q
    gap = delta_q - nine_profile.block_variance
    require(delta_q == 8_843_689_984, "deployed delta*q")
    require(gap == 57_561_642 and gap > 0, "deployed strict Plotkin gap")
    strict_cap = plotkin_cap(nine_profile, width)
    require(strict_cap == 153, "deployed strict Plotkin cap")
    require(153 * gap <= delta_q < 154 * gap, "strict cap floor witnesses")

    profile_size = (
        comb(q, 1_858)
        * comb(q, 1_857) ** 6
        * comb(q, 38_300) ** 2
    )
    require(profile_size == nine_profile.profile_size, "nine profile size")
    image_lower = ceil_div(profile_size, strict_cap)
    require(
        (image_lower - 1) * strict_cap < profile_size
        <= image_lower * strict_cap,
        "nine realized-image lower ceiling",
    )

    local_gcd = reduce(gcd, (q, *nine))
    variance_margin = (q - local_gcd) * delta - nine_profile.block_variance
    require(local_gcd == 1, "nine local rotation gcd")
    require(variance_margin == 57_494_170, "nine zero variance margin")
    require(variance_margin > 0, "nine cyclic variance exclusion")
    require(strict_cap * local_gcd < q, "nine cyclic orbit-cap exclusion")

    minority_length = 9 * q
    require(minority_length == 1_179_648, "minority ambient length")
    require(
        nine_profile.total_minority
        * (minority_length - nine_profile.total_minority)
        == 97_668_300_800,
        "minority ambient variance",
    )
    require(
        delta * minority_length == 79_593_209_856,
        "minority ambient Plotkin threshold",
    )
    require(
        nine_profile.total_minority
        * (minority_length - nine_profile.total_minority)
        > delta * minority_length,
        "minority ambient Plotkin must fail",
    )
    require(m * (n - m) == 1_094_959_156_992, "global variance numerator")
    require(delta * n == 141_499_039_744, "global Plotkin threshold")
    require(m * (n - m) > delta * n, "global Plotkin must fail")

    shadow_retention = m - width
    require(shadow_retention == 913_633, "global shadow retention")
    require(Fraction(m, n) == Fraction(61_319, 131_072), "deployed density")
    require(
        ratio_power_exceeds_two_power(
            131_072, 61_319, shadow_retention, 1_000_000
        ),
        "global shadow lower bound",
    )

    orbit_profiles = factorial(16) // (
        factorial(1) * factorial(6) * factorial(2) * factorial(7)
    )
    orbit_upper = orbit_profiles * strict_cap
    require(orbit_profiles == 2_882_880, "permutation profile count")
    require(orbit_upper == 441_080_640, "permutation union upper bound")

    neighbor = (
        *(130_800 for _ in range(3)),
        *(130_801 for _ in range(4)),
        32_750,
        32_750,
        *(0 for _ in range(7)),
    )
    neighbor_profile = make_profile(q, neighbor)
    require(len(neighbor) == block_count, "neighbor vector length")
    require(neighbor_profile.support_size == m, "neighbor support size")
    require(
        neighbor_profile.minority_sizes
        == (
            *(272 for _ in range(3)),
            *(271 for _ in range(4)),
            32_750,
            32_750,
        ),
        "neighbor minority vector",
    )
    require(neighbor_profile.negative_mass == 1_900, "neighbor negative mass")
    require(neighbor_profile.positive_mass == 65_500, "neighbor positive mass")
    require(neighbor_profile.total_minority == 67_400, "neighbor T")
    require(
        neighbor_profile.total_minority <= width,
        "neighbor injectivity hypothesis",
    )
    require(
        neighbor_profile.positive_mass <= width
        and neighbor_profile.negative_mass <= width,
        "neighbor split-sign zero hypotheses",
    )

    partial = make_profile(q, (129_172, 32_750, 32_750))
    full_choices = comb(13, 6)
    require(partial.support_size == 194_672, "coarse partial support size")
    require(partial.negative_mass == 1_900, "coarse negative mass")
    require(partial.positive_mass == 65_500, "coarse positive mass")
    require(partial.total_minority == 67_400 <= width, "coarse injectivity")
    require(
        partial.support_size + 6 * q == m,
        "coarse full-coset support size",
    )
    require(full_choices == 1_716, "coarse full-coset multiplicity")

    wall = tuple(
        value
        for pair in ((71_072, 51_566) for _ in range(8))
        for value in pair
    )
    wall_profile = make_profile(q, wall)
    require(wall_profile.support_size == m, "remaining-wall support size")
    require(wall_profile.negative_mass == 480_000, "wall negative mass")
    require(wall_profile.positive_mass == 412_528, "wall positive mass")
    require(wall_profile.total_minority == 892_528, "wall total minority")
    require(
        wall_profile.negative_mass > width
        and wall_profile.positive_mass > width,
        "wall split-sign tests must fail",
    )
    require(
        wall_profile.block_variance == 66_913_011_168,
        "remaining-wall B_r",
    )
    require(
        wall_profile.block_variance > delta_q,
        "remaining wall must be beyond block Plotkin",
    )
    retained = wall_profile.total_minority - width
    require(retained == 825_057, "remaining-wall shadow retention")
    require(
        ratio_power_exceeds_two_power(4_096, 1_875, retained, 930_000),
        "remaining-wall product-shadow lower bound",
    )

    coarser = (
        (262_144, 8, 122_638),
        (524_288, 4, 245_276),
        (1_048_576, 2, 490_552),
        (2_097_152, 1, 981_104),
    )
    global_threshold = Fraction(m * (n - m), n)
    require(
        global_threshold == Fraction(4_277_184_207, 8_192),
        "global local-variance threshold",
    )
    require(global_threshold > delta, "global local variance exceeds delta")
    for coarse_q, coarse_n, coarse_r in coarser:
        require(coarse_q * coarse_n == n, "coarse partition length")
        require(coarse_r * coarse_n == m, "coarse partition mass")
        local_threshold = Fraction(
            coarse_n * coarse_r * (coarse_q - coarse_r), coarse_q
        )
        require(local_threshold == global_threshold, "coarse uniform variance")
        require(
            coarse_n * coarse_r * (coarse_q - coarse_r) > delta * coarse_q,
            "coarse block Plotkin must fail",
        )

    return {
        "prime": prime,
        "delta_q": delta_q,
        "strict_gap": gap,
        "strict_cap": strict_cap,
        "zero_variance_margin": variance_margin,
        "profile_size_bits": profile_size.bit_length(),
        "image_lower_bits": image_lower.bit_length(),
        "orbit_profiles": orbit_profiles,
        "orbit_union_upper": orbit_upper,
        "neighbor_total_minority": neighbor_profile.total_minority,
        "coarse_multiplicity": full_choices,
        "wall_variance": wall_profile.block_variance,
        "wall_shadow_retained": retained,
        "coarse_scales": len(coarser),
    }


def verify_tamper_cases() -> dict[str, int]:
    results: dict[str, int] = {}

    prime = 13
    q = 3
    blocks = tuple(
        tuple(range(1 + q * index, 1 + q * (index + 1)))
        for index in range(4)
    )

    signed_profile = make_profile(q, (2, 1, 0, 0))
    signed_supports = exact_profile_supports(blocks, signed_profile)
    offset = fixed_offset(blocks, signed_profile, prime, 3)
    require(offset != (0, 0, 0), "sign tamper requires nonzero offset")
    wrong_sign_mismatches = 0
    missing_offset_mismatches = 0
    for support in signed_supports:
        actual = power_sums(support, prime, 3)
        minorities = minority_sets(support, blocks, signed_profile)
        unsigned = signed_vector_sum(
            offset,
            (
                (1, power_sums(minority, prime, 3))
                for minority in minorities
            ),
            prime,
        )
        no_offset = signed_vector_sum(
            (0, 0, 0),
            (
                (sign, power_sums(minority, prime, 3))
                for sign, minority in zip(signed_profile.signs, minorities)
            ),
            prime,
        )
        wrong_sign_mismatches += unsigned != actual
        missing_offset_mismatches += no_offset != actual
    require(wrong_sign_mismatches > 0, "unsigned dense mutation survived")
    require(missing_offset_mismatches > 0, "missing offset mutation survived")
    results["sign_mutation_rejections"] = (
        wrong_sign_mismatches + missing_offset_mismatches
    )

    shadow_profile = make_profile(q, (1, 1, 1, 0))
    shadow_supports = exact_profile_supports(blocks, shadow_profile)
    shadow_fibers = fiber_map(shadow_supports, prime, 1)
    shadow_maximum = max(map(len, shadow_fibers.values()))
    cap, correct_shadow, endpoint = theorem_cap(shadow_profile, 1)
    require(shadow_profile.total_minority == 3, "shadow fixture T")
    require(correct_shadow == 9 and endpoint == 12 and cap == 9, "shadow fixture caps")
    invalid_retained = (0, 0, 0)
    invalid_deficit = sum(
        size - value
        for size, value in zip(
            shadow_profile.minority_sizes, invalid_retained
        )
    )
    invalid_cap = prod(comb(q, value) for value in invalid_retained) // prod(
        comb(size, value)
        for size, value in zip(
            shadow_profile.minority_sizes, invalid_retained
        )
    )
    require(invalid_deficit == 3 > 1, "invalid shadow deficit")
    require(invalid_cap == 1 < shadow_maximum == 7, "shadow gate mutation")
    results["shadow_gate_rejections"] = 1

    strict_profile = make_profile(q, (1, 1, 0, 0))
    strict_supports = exact_profile_supports(blocks, strict_profile)
    strict_maximum = max(map(len, fiber_map(strict_supports, prime, 1).values()))
    correct_plotkin = plotkin_cap(strict_profile, 1)
    delta_q = 2 * q
    reversed_fraction = (
        delta_q - strict_profile.block_variance
    ) // delta_q
    missing_q_fraction = 2 // (delta_q - strict_profile.block_variance)
    require(strict_profile.block_variance == 4 < delta_q == 6, "strict fixture")
    require(correct_plotkin == 3 == strict_maximum, "sharp strict Plotkin fixture")
    require(reversed_fraction == 0 < strict_maximum, "reversed Plotkin mutation")
    require(missing_q_fraction == 1 < strict_maximum, "missing-q Plotkin mutation")
    results["plotkin_formula_rejections"] = 2

    affine_blocks = ((1, 2), (3, 4), (5, 6))
    affine_profile = make_profile(2, (0, 1, 2))
    affine_supports = exact_profile_supports(affine_blocks, affine_profile)
    affine_offset = fixed_offset(affine_blocks, affine_profile, 7, 2)
    affine_zero_count = sum(
        power_sums(support, 7, 2) == (0, 0)
        for support in affine_supports
    )
    require(affine_offset == (4, 5), "affine zero fixture offset")
    require(affine_profile.partial_indices, "affine zero fixture partial block")
    require(
        affine_profile.positive_mass <= 2
        and affine_profile.negative_mass <= 2,
        "affine zero fixture side masses",
    )
    require(affine_zero_count == 1, "offset-zero hypothesis counterfixture")
    results["zero_offset_hypothesis_rejections"] = 1

    subgroup, cyclic_blocks = multiplicative_cosets(13, 4)
    require(len(subgroup) == 4, "mixed-sign zero subgroup")
    mixed_profile = make_profile(4, (0, 3, 2))
    mixed_supports = exact_profile_supports(cyclic_blocks, mixed_profile)
    mixed_zero_count = sum(
        power_sums(support, 13, 1) == (0,)
        for support in mixed_supports
    )
    mixed_cap, mixed_shadow, mixed_plotkin = theorem_cap(mixed_profile, 1)
    mixed_gcd = reduce(gcd, (4, *mixed_profile.occupancies))
    require(
        fixed_offset(cyclic_blocks, mixed_profile, 13, 1) == (0,),
        "mixed zero fixture offset",
    )
    require(
        mixed_profile.positive_mass == 2 > 1
        and mixed_profile.negative_mass == 1,
        "mixed zero side-mass fixture",
    )
    require(mixed_profile.block_variance == 7, "mixed zero B_r")
    require(
        mixed_shadow == 6 and mixed_plotkin == 8 and mixed_cap == 6,
        "mixed zero caps",
    )
    require(mixed_gcd == 1, "mixed zero gcd")
    require(
        not (
            mixed_profile.block_variance < (4 - mixed_gcd) * 2
            or mixed_cap * mixed_gcd < 4
        ),
        "mixed zero cyclic guardrail should not fire",
    )
    require(mixed_zero_count == 4, "side-mass zero counterfixture")
    results["zero_side_hypothesis_rejections"] = 1
    results["mixed_sign_zero_fiber"] = mixed_zero_count

    return results


def guard_selftest() -> None:
    rejected = False
    try:
        require(False, "guard self-test")
    except VerificationError:
        rejected = True
    require(rejected, "always-active guard failed")


def run_full_check() -> None:
    guard_selftest()
    deployed = verify_deployed()
    general = verify_general_exhaustive()
    cyclic = verify_cyclic_exhaustive()
    tamper = verify_tamper_cases()

    print("always_active_guard=PASS")
    print(
        "deployed_profile: "
        f"p={deployed['prime']} delta_q={deployed['delta_q']} "
        f"B_r={deployed['delta_q'] - deployed['strict_gap']} "
        f"gap={deployed['strict_gap']}"
    )
    print(
        "strict_plotkin_cap: "
        f"floor(delta*q/(delta*q-B_r))={deployed['strict_cap']} "
        "(nine-partial profile fibers are at most 153)"
    )
    print(
        "zero_empty: "
        f"variance_margin={deployed['zero_variance_margin']} "
        "and 153<131072"
    )
    print(
        "realized_image_arithmetic: "
        f"profile_size_bits={deployed['profile_size_bits']} "
        f"lower_bound_bits={deployed['image_lower_bits']}"
    )
    print(
        "permutation_orbit: "
        f"profiles={deployed['orbit_profiles']} "
        f"fiber_upper_bound={deployed['orbit_union_upper']} "
        "(upper bound only; no attainment claim)"
    )
    print(
        "neighbor_and_coarse: "
        f"injective_T={deployed['neighbor_total_minority']} "
        f"coarse_exact_multiplicity={deployed['coarse_multiplicity']}"
    )
    print(
        "remaining_mixed_sign_wall: "
        f"B_r={deployed['wall_variance']} "
        f"shadow_retained={deployed['wall_shadow_retained']} "
        f"nested_scales={deployed['coarse_scales']}"
    )
    print(
        "general_exhaustive: "
        f"profiles={general['profiles']} supports={general['supports']} "
        f"collision_pair_checks={general['collision_pair_checks']} "
        f"strict={general['strict_profiles']} "
        f"equality={general['equality_profiles']} "
        f"beyond={general['beyond_plotkin_profiles']}"
    )
    print(
        "cyclic_exhaustive: "
        f"profiles={cyclic['profiles']} supports={cyclic['supports']} "
        f"zero_supports={cyclic['zero_supports']} "
        f"zero_checks={cyclic['cyclic_zero_checks']} "
        f"exclusion_profiles={cyclic['cyclic_exclusion_profiles']}"
    )
    print(
        "tamper_regressions: "
        f"sign={tamper['sign_mutation_rejections']} "
        f"shadow={tamper['shadow_gate_rejections']} "
        f"plotkin={tamper['plotkin_formula_rejections']} "
        f"zero_offset={tamper['zero_offset_hypothesis_rejections']} "
        f"zero_side={tamper['zero_side_hypothesis_rejections']} "
        f"mixed_zero_fiber={tamper['mixed_sign_zero_fiber']}"
    )
    print("NONCLAIMS: no all-profile Q; no global nu(0)<=n^3; no RC/ray/CAT/UNIF")
    print("NONCLAIMS: no finite threshold, Grand MCA, or Grand List solve")
    print("RESULT: PASS")


def run_tamper_selftest() -> None:
    guard_selftest()
    tamper = verify_tamper_cases()
    print(
        "tamper_selftest: "
        f"sign={tamper['sign_mutation_rejections']} "
        f"shadow={tamper['shadow_gate_rejections']} "
        f"plotkin={tamper['plotkin_formula_rejections']} "
        f"zero_offset={tamper['zero_offset_hypothesis_rejections']} "
        f"zero_side={tamper['zero_side_hypothesis_rejections']} "
        f"mixed_zero_fiber={tamper['mixed_sign_zero_fiber']}"
    )
    print("RESULT: PASS tamper-selftest")


def main() -> int:
    if sys.flags.optimize:
        print(
            "ERROR: optimized mode is refused; run without -O",
            file=sys.stderr,
        )
        return 2

    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true", help="run all checks")
    modes.add_argument(
        "--tamper-selftest",
        action="store_true",
        help="run only negative regression fixtures",
    )
    args = parser.parse_args()

    if args.check:
        run_full_check()
    else:
        run_tamper_selftest()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
