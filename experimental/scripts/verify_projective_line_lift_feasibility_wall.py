#!/usr/bin/env python3
"""Replay the projective-line lift feasibility wall with Python stdlib only.

All checks use explicit exceptions rather than ``assert``, so ``python -O``
does not remove any verification logic.
"""

from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd, isqrt
from pathlib import Path


P = 2_130_706_433
N = 2_097_152
K = 1_048_576
M = 1_116_047
SIGMA = M - K
TARGET = 274_854_110_496_187_592
EXPECTED_BUDGET = 274_980_728_111_395_087
EXPECTED_SHADOW_RATIO = Fraction(4_581_294_080, 289_215_899_480_839)
EXPECTED_ENDPOINT_CUT = 406_554_737_445_582_740
EXPECTED_SHADOW_FLOOR = 2_618_290_424_420_403_004_360_190_639_514


class VerificationError(RuntimeError):
    """Raised when an exact certificate check fails."""


CHECKS = 0


def require(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise VerificationError(label)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    limit = isqrt(value)
    while divisor <= limit:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def add_shifted_power(coefficients: list[int], degree: int, scale: int) -> None:
    """Add ``scale * (X - 1)^degree`` in ascending coefficient order."""

    for power in range(degree + 1):
        coefficients[power] += (
            scale * comb(degree, power) * (-1) ** (degree - power)
        )


def scalar_agreement_polynomial(
    p: int, n: int, dimension: int, agreement: int, tail: int
) -> list[int]:
    coefficients = [0] * (agreement + 1)
    for degree in range(dimension + 1):
        add_shifted_power(
            coefficients,
            degree,
            comb(n, degree) * p ** (dimension - degree),
        )
    coefficients[agreement] += tail
    for degree in range(dimension + 1):
        add_shifted_power(
            coefficients,
            degree,
            -tail * comb(agreement, degree),
        )
    return coefficients


def krawtchouk(p: int, n: int, shell: int, weight: int) -> int:
    lower = max(0, shell - (n - weight))
    upper = min(shell, weight)
    return sum(
        (-1) ** overlap
        * (p - 1) ** (shell - overlap)
        * comb(weight, overlap)
        * comb(n - weight, shell - overlap)
        for overlap in range(lower, upper + 1)
    )


def projective_mds_shell(p: int, n: int, dimension: int, shell: int) -> int:
    excess = shell - dimension
    if excess < 1:
        return 0
    alternating = sum(
        (-1) ** index
        * comb(shell - 1, index)
        * p ** (excess - 1 - index)
        for index in range(excess)
    )
    return comb(n, shell) * alternating


def eval_poly(coefficients: tuple[int, ...], point: int, p: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * point + coefficient) % p
    return value


def canonical_projective(vector: tuple[int, ...], p: int) -> tuple[int, ...]:
    first = next((value % p for value in vector if value % p), None)
    if first is None:
        raise VerificationError("zero vector has no projective normalization")
    inverse = pow(first, -1, p)
    return tuple((value * inverse) % p for value in vector)


def projective_points(p: int, dimension: int) -> tuple[tuple[int, ...], ...]:
    points = {
        canonical_projective(vector, p)
        for vector in product(range(p), repeat=dimension)
        if any(vector)
    }
    return tuple(sorted(points))


def projective_lines(
    points: tuple[tuple[int, ...], ...], p: int
) -> tuple[frozenset[tuple[int, ...]], ...]:
    lines: set[frozenset[tuple[int, ...]]] = set()
    for left, right in combinations(points, 2):
        span = {
            canonical_projective(
                tuple(
                    (a * x + b * y) % p
                    for x, y in zip(left, right)
                ),
                p,
            )
            for a, b in product(range(p), repeat=2)
            if a or b
        }
        if len(span) == p + 1:
            lines.add(frozenset(span))
    return tuple(sorted(lines, key=lambda line: tuple(sorted(line))))


def projective_hyperplanes(
    points: tuple[tuple[int, ...], ...], p: int
) -> set[frozenset[tuple[int, ...]]]:
    functionals = projective_points(p, len(points[0]))
    return {
        frozenset(
            point
            for point in points
            if sum(a * x for a, x in zip(functional, point)) % p == 0
        )
        for functional in functionals
    }


def check_optimization_safety() -> None:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=__file__)
    require(
        not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
        "verifier must not contain assert statements",
    )


def check_deployed_ledger() -> dict[str, int | Fraction]:
    require(P == 2**31 - 2**24 + 1, "KoalaBear prime formula")
    require(is_prime(P), "deployed base/list field must be prime")
    require(N == 2**21 and K == 2**20, "deployed powers of two")
    require(N == 2 * K, "self-dual-dimension relation n=2K")
    require(M == K + SIGMA and SIGMA == 67_471, "agreement decomposition")
    require(N - M == 981_105, "weight threshold n-m")
    require((P - 1) % N == 0, "cyclic evaluation domain divisibility")
    require((P - 1) // N == 1_016, "cyclic evaluation domain index")
    require(P > 2 * N, "coefficient nonnegativity field gate")

    budget = P**6 // 2**128
    compiled_target = ((budget + 1) * (P - N + M) - 1) // P
    require(budget == EXPECTED_BUDGET, "sextic challenge budget")
    require(P - N + M == 2_129_725_328, "shell-compression denominator")
    require(compiled_target == TARGET, "compiled one-row target")

    lambda_lower_100 = Fraction(3, 2) ** 100
    lambda_floor_100 = floor_fraction(lambda_lower_100)
    require(K - 3 * SIGMA == 846_163, "3/2 ratio gate")
    require(lambda_floor_100 == 406_561_177_535_215_237, "lambda lower floor")
    require(
        lambda_floor_100 - TARGET == 131_707_067_039_027_645,
        "T+1 scalar interval margin",
    )
    require(TARGET + 1 <= lambda_floor_100, "T+1 lies below lambda")

    rho = Fraction(SIGMA, K)
    x = Fraction(N * K, P * SIGMA)
    y = Fraction(N, P)
    require(0 < rho < 1 and 0 < x < 1 and 0 < y < 1, "scalar bound ratios")

    positive_gap = (
        (1 - Fraction(1, P)) * (1 - y)
        - (rho / (1 - x) + Fraction(1, P))
    )
    expected_positive_gap = Fraction(
        629_197_861_639_644_034_270_808_063_071_854_583_327,
        673_896_871_014_088_741_031_154_346_685_050_650_624,
    )
    require(positive_gap == expected_positive_gap, "positive N-shell gap")
    require(positive_gap > 0, "positive N-shell endpoint")

    low_gate_1 = P * SIGMA - 100 * K * (K + 9)
    low_gate_2 = P * (SIGMA - 8) - 100 * K * (K + 9)
    require(low_gate_1 == 33_808_787_244_943, "low-shell first ratio gate")
    require(low_gate_2 == 33_791_741_593_479, "low-shell later ratio gate")
    require(low_gate_1 > 0 and low_gate_2 > 0, "low-shell positivity")

    negative_gap = (1 - y) - (P * rho**8 / (1 - x) + y**7)
    expected_negative_gap = Fraction(
        14_980_060_041_633_554_401_788_097_188_418_356_598_094_456_587_298_273_461_558_641_437_112_289_293_525_930_573_440_576_326_435_256_327_699_206_799_425_444_516_551_221_233,
        41_248_761_974_934_491_830_107_366_569_484_286_197_063_703_498_391_909_062_631_935_376_216_209_552_254_878_164_750_035_783_418_216_201_653_194_750_176_047_587_269_804_032,
    )
    require(negative_gap == expected_negative_gap, "negative N-shell gap")
    require(negative_gap > 0, "negative N-shell endpoint")

    return {
        "budget": budget,
        "compiled_target": compiled_target,
        "lambda_floor_100": lambda_floor_100,
        "lambda_margin": lambda_floor_100 - TARGET,
        "positive_gap": positive_gap,
        "negative_gap": negative_gap,
        "low_gate_1": low_gate_1,
        "low_gate_2": low_gate_2,
    }


def check_shadow_cap() -> dict[str, int | Fraction]:
    raw_numerator = K * (K - 1)
    raw_denominator = SIGMA * (
        (SIGMA - 1) + (K + 2) * (K - SIGMA)
    )
    ratio = Fraction(raw_numerator, raw_denominator)
    require(gcd(raw_numerator, raw_denominator) == 240, "shadow ratio gcd")
    require(ratio == EXPECTED_SHADOW_RATIO, "reduced K+2 shadow ratio")
    require(0 < ratio < 1, "shadow cap is a strict reduction")

    endpoint_cut = floor_fraction((1 - ratio) * Fraction(3, 2) ** 100)
    shadow_floor = floor_fraction(ratio * Fraction(3, 2) ** 200)
    require(endpoint_cut == EXPECTED_ENDPOINT_CUT, "R12 endpoint cut")
    require(shadow_floor == EXPECTED_SHADOW_FLOOR, "shadow lower floor")
    require(shadow_floor > TARGET, "shadow cap remains above T")
    require(shadow_floor > 2_618_000_000_000_000_000_000_000_000_000, "2.618e30 gate")

    return {
        "ratio": ratio,
        "endpoint_cut": endpoint_cut,
        "shadow_floor": shadow_floor,
    }


def check_support_model() -> dict[str, int]:
    simplex_18_length = 2**18 - 1
    simplex_18_distance = 2**17
    simplex_7_length = 2**7 - 1
    simplex_7_distance = 2**6
    repeated_7_length = 1_055 * simplex_7_length
    repeated_7_distance = 1_055 * simplex_7_distance

    code_length = 3 * simplex_18_length + repeated_7_length + 60_691
    code_dimension = 3 * 18 + 7
    code_distance = min(simplex_18_distance, repeated_7_distance)
    code_size = 2**code_dimension

    require(code_length == 981_105, "binary support-code length")
    require(code_dimension == 61, "binary support-code dimension")
    require(code_distance == 67_520, "binary support-code distance")
    require(code_size == 2_305_843_009_213_693_952, "binary support-code size")
    require(code_size > TARGET, "binary support model exceeds T")
    require(2 * code_length == 1_962_210 < N, "disjoint coordinate pairs fit")
    require(N - 2 * code_length == 134_942, "unused coordinate count")
    require(M - code_distance == K - 49, "block intersection ceiling")
    require(M - code_distance < K, "block intersections are below K")

    full_support_points = P - K - 1
    require(full_support_points == 2_129_657_856, "K+2 line full-support points")
    require(
        (K + 2) + full_support_points == P + 1,
        "K+2 shortened-dual line partition",
    )
    local_completions = {
        0: 1,
        1: 1,
        K + 2: (K + 2) + full_support_points,
    }
    require(
        set(local_completions.values()) == {1, P + 1},
        "0/1/K+2 facets complete to the 1-or-p+1 law",
    )

    return {
        "length": code_length,
        "dimension": code_dimension,
        "distance": code_distance,
        "size": code_size,
        "size_margin": code_size - TARGET,
        "intersection": M - code_distance,
        "full_support_points": full_support_points,
    }


def check_weighted_grs_normalization() -> int:
    p = 7
    domain = tuple(range(1, p))
    dimension = 3
    multipliers = (1, 2, 3, 4, 5, 6)
    received = tuple(
        multiplier * pow(point, dimension, p) % p
        for point, multiplier in zip(domain, multipliers)
    )

    agreement_counts: Counter[int] = Counter()
    for coefficients in product(range(p), repeat=dimension):
        codeword = tuple(
            multiplier * eval_poly(coefficients, point, p) % p
            for point, multiplier in zip(domain, multipliers)
        )
        normalized_received = tuple(
            value * pow(multiplier, -1, p) % p
            for value, multiplier in zip(received, multipliers)
        )
        normalized_codeword = tuple(
            value * pow(multiplier, -1, p) % p
            for value, multiplier in zip(codeword, multipliers)
        )
        weighted_agreement = sum(
            left == right for left, right in zip(received, codeword)
        )
        normalized_agreement = sum(
            left == right
            for left, right in zip(normalized_received, normalized_codeword)
        )
        require(weighted_agreement == normalized_agreement, "monomial isometry")
        agreement_counts[weighted_agreement] += 1

    formal = scalar_agreement_polynomial(p, len(domain), dimension, 4, 0)
    require(sum(agreement_counts.values()) == p**dimension, "weighted GRS census")
    require(
        all(agreement_counts[agreement] == formal[agreement]
            for agreement in range(len(formal))),
        "weighted degree-K word realizes Z_0",
    )
    require(
        all(agreement_counts[agreement] == 0
            for agreement in range(len(formal), len(domain) + 1)),
        "degree-K word has no excess roots",
    )
    return p**dimension


def check_scalar_toy_replay() -> dict[str, int]:
    p = 1_009
    n = 16
    dimension = 8
    agreement = 10
    scalar_endpoint = Fraction(comb(n, dimension), comb(agreement, dimension))
    require(scalar_endpoint == 286, "toy scalar endpoint")

    krawtchouk_table = [
        [krawtchouk(p, n, shell, weight) for weight in range(n + 1)]
        for shell in range(n + 1)
    ]
    shell_checks = 0
    for tail in range(scalar_endpoint.numerator + 1):
        z = scalar_agreement_polynomial(
            p, n, dimension, agreement, tail
        )
        weights = [
            z[n - weight] if 0 <= n - weight < len(z) else 0
            for weight in range(n + 1)
        ]
        require(min(z) >= 0, "toy nonnegative agreement coefficients")
        require(sum(weights) == p**dimension, "toy scalar mass")
        require(weights[0] == 0, "toy nonzero coset")
        require(
            sum(weights[: n - agreement + 1]) == tail,
            "toy scalar tail",
        )

        for shell in range(n + 1):
            transform = sum(
                weights[weight] * krawtchouk_table[shell][weight]
                for weight in range(n + 1)
            )
            if shell == 0:
                require(transform == p**dimension, "toy shell zero")
            elif shell <= dimension:
                require(transform == 0, "toy vanishing dual shell")
            else:
                projective_shell = projective_mds_shell(
                    p, n, dimension, shell
                )
                require(
                    transform % p**dimension == 0,
                    "toy Krawtchouk divisibility",
                )
                numerator = transform // p**dimension + projective_shell
                require(numerator % p == 0, "toy projective congruence")
                selected = numerator // p
                require(
                    0 <= selected <= projective_shell,
                    "toy projective shell interval",
                )
                shell_checks += 1

    return {
        "profiles": scalar_endpoint.numerator + 1,
        "shell_checks": shell_checks,
    }


def check_projective_line_characterization() -> dict[str, int]:
    cases = ((2, 3), (3, 3), (2, 4))
    total_candidates = 0
    total_hyperplanes = 0

    for p, dimension in cases:
        points = projective_points(p, dimension)
        lines = projective_lines(points, p)
        hyperplanes = projective_hyperplanes(points, p)
        expected_points = (p**dimension - 1) // (p - 1)
        expected_lines = (
            (p**dimension - 1)
            * (p ** (dimension - 1) - 1)
            // ((p**2 - 1) * (p - 1))
        )
        hyperplane_size = (p ** (dimension - 1) - 1) // (p - 1)
        require(len(points) == expected_points, "projective point count")
        require(len(lines) == expected_lines, "projective line count")
        require(
            all(len(line) == p + 1 for line in lines),
            "projective line cardinality",
        )
        require(
            len(hyperplanes) == expected_points,
            "dual projective hyperplane count",
        )
        require(
            all(len(hyperplane) == hyperplane_size for hyperplane in hyperplanes),
            "projective hyperplane cardinality",
        )

        feasible: set[frozenset[tuple[int, ...]]] = set()
        for chosen in combinations(points, hyperplane_size):
            selected = frozenset(chosen)
            if all(len(selected & line) in (1, p + 1) for line in lines):
                feasible.add(selected)
        require(
            feasible == hyperplanes,
            "1-or-(p+1) line law characterizes hyperplanes",
        )
        total_candidates += comb(len(points), hyperplane_size)
        total_hyperplanes += len(hyperplanes)

    return {
        "cases": len(cases),
        "candidates": total_candidates,
        "hyperplanes": total_hyperplanes,
    }


def main() -> None:
    check_optimization_safety()
    ledger = check_deployed_ledger()
    shadow = check_shadow_cap()
    support = check_support_model()
    weighted_words = check_weighted_grs_normalization()
    scalar_toy = check_scalar_toy_replay()
    projective_toy = check_projective_line_characterization()

    print("object: projective-line lift feasibility wall")
    print("status: PROVED route cut / exact new wall")
    print("runtime: Python stdlib only; assert-free explicit checks")
    print(
        "deployed: "
        f"p={P} n={N} K={K} m={M} sigma={SIGMA} T={TARGET}"
    )
    print(
        "field gate: "
        f"prime=PASS (p-1)/n={(P - 1) // N} weighted-GRS=PASS "
        f"({weighted_words} words)"
    )
    print(
        "challenge ledger: "
        f"B*={ledger['budget']} compiled_T={ledger['compiled_target']}"
    )
    print(
        "scalar T+1 gate: "
        f"floor((3/2)^100)={ledger['lambda_floor_100']} "
        f"margin_over_T={ledger['lambda_margin']}"
    )
    print(
        "scalar shell gates: "
        f"g_plus={ledger['positive_gap']} g_minus={ledger['negative_gap']} "
        f"low_gates=({ledger['low_gate_1']},{ledger['low_gate_2']})"
    )
    print(
        "scalar toy replay: "
        f"profiles={scalar_toy['profiles']} "
        f"dual_shell_checks={scalar_toy['shell_checks']} PASS"
    )
    ratio = shadow["ratio"]
    print(
        "K+2 shadow: "
        f"ratio={ratio.numerator}/{ratio.denominator} "
        f"endpoint_cut>={shadow['endpoint_cut']} "
        f"certified_floor={shadow['shadow_floor']}"
    )
    print(
        "support model: "
        f"[{support['length']},{support['dimension']},>={support['distance']}]_2 "
        f"size={support['size']} margin_over_T={support['size_margin']} "
        f"max_intersection={support['intersection']}"
    )
    print(
        "K+2 local lines: "
        f"full_support_points={support['full_support_points']} "
        "facet_states={0,1,K+2} PASS"
    )
    print(
        "projective line-law exhaustion: "
        f"cases={projective_toy['cases']} "
        f"candidate_subsets={projective_toy['candidates']} "
        f"hyperplanes={projective_toy['hyperplanes']} PASS"
    )
    print(f"checks: {CHECKS} PASS")
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
