#!/usr/bin/env python3
"""Exact replay for the canonical reduced rational-host compiler.

The compiler construction is checked against an independent brute-force scan
of every slope and every degree-<k explaining polynomial in two F_17 cases:
the collision-literal d=1 example in the note and a nontrivial d=2 case.  The
script also exhausts every reduced direction presentation with denominator
degree at most a-k and every canonical host polynomial for the fixed direction.

The verifier is stdlib-only, deterministic, and optimization-safe.  It uses no
Python ``assert`` statements; failures raise VerificationFailure explicitly.
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path


class VerificationFailure(RuntimeError):
    """Raised when a replay gate fails."""


CHECKS = 0


def require(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise VerificationFailure(label)


def trim(poly: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    out = list(poly)
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def coefficient(poly: tuple[int, ...], degree: int) -> int:
    return poly[degree] if degree < len(poly) else 0


def pad(poly: tuple[int, ...], length: int) -> tuple[int, ...]:
    return tuple(coefficient(poly, index) for index in range(length))


def poly_add(
    left: tuple[int, ...], right: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    length = max(len(left), len(right))
    return trim(
        tuple(
            (coefficient(left, index) + coefficient(right, index)) % modulus
            for index in range(length)
        )
    )


def poly_sub(
    left: tuple[int, ...], right: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    length = max(len(left), len(right))
    return trim(
        tuple(
            (coefficient(left, index) - coefficient(right, index)) % modulus
            for index in range(length)
        )
    )


def poly_scale(
    poly: tuple[int, ...], scalar: int, modulus: int
) -> tuple[int, ...]:
    return trim(tuple((scalar * value) % modulus for value in poly))


def poly_mul(
    left: tuple[int, ...], right: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    if not left or not right:
        return ()
    out = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            out[i + j] = (out[i + j] + left_value * right_value) % modulus
    return trim(out)


def poly_divmod(
    numerator: tuple[int, ...], denominator: tuple[int, ...], modulus: int
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if not denominator:
        raise VerificationFailure("polynomial division by zero")
    remainder = list(trim(numerator))
    quotient = [0] * max(0, len(remainder) - len(denominator) + 1)
    leading_inverse = pow(denominator[-1], modulus - 2, modulus)
    while remainder and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        scalar = remainder[-1] * leading_inverse % modulus
        quotient[shift] = scalar
        for index, value in enumerate(denominator):
            remainder[shift + index] = (
                remainder[shift + index] - scalar * value
            ) % modulus
        remainder = list(trim(remainder))
    return trim(quotient), trim(remainder)


def poly_gcd(
    left: tuple[int, ...], right: tuple[int, ...], modulus: int
) -> tuple[int, ...]:
    while right:
        left, right = right, poly_divmod(left, right, modulus)[1]
    if not left:
        return ()
    return poly_scale(left, pow(left[-1], modulus - 2, modulus), modulus)


def poly_eval(poly: tuple[int, ...], value: int, modulus: int) -> int:
    result = 0
    for item in reversed(poly):
        result = (result * value + item) % modulus
    return result


def locator(support: tuple[int, ...], modulus: int) -> tuple[int, ...]:
    result = (1,)
    for point in support:
        result = poly_mul(result, ((-point) % modulus, 1), modulus)
    return result


def interpolation_basis(
    points: tuple[int, ...], modulus: int
) -> tuple[tuple[int, ...], ...]:
    basis = []
    for index, point in enumerate(points):
        numerator = (1,)
        denominator = 1
        for other_index, other_point in enumerate(points):
            if index == other_index:
                continue
            numerator = poly_mul(
                numerator, ((-other_point) % modulus, 1), modulus
            )
            denominator = denominator * (point - other_point) % modulus
        basis.append(
            poly_scale(
                numerator, pow(denominator, modulus - 2, modulus), modulus
            )
        )
    return tuple(basis)


def interpolate(
    values: tuple[int, ...],
    basis: tuple[tuple[int, ...], ...],
    modulus: int,
) -> tuple[int, ...]:
    result: tuple[int, ...] = ()
    for value, basis_poly in zip(values, basis):
        result = poly_add(result, poly_scale(basis_poly, value, modulus), modulus)
    return result


def explained_on_support(
    word: tuple[int, ...],
    support: tuple[int, ...],
    domain: tuple[int, ...],
    dimension: int,
    modulus: int,
) -> bool:
    selected_points = support[:dimension]
    selected_values = tuple(word[domain.index(point)] for point in selected_points)
    basis = interpolation_basis(selected_points, modulus)
    candidate = interpolate(selected_values, basis, modulus)
    return len(candidate) <= dimension and all(
        poly_eval(candidate, point, modulus) == word[domain.index(point)]
        for point in support
    )


def span_scalar(
    remainder: tuple[int, ...],
    direction: tuple[int, ...],
    degree: int,
    modulus: int,
) -> tuple[bool, int]:
    padded_direction = pad(direction, degree)
    padded_remainder = pad(remainder, degree)
    pivot = next(
        (index for index, value in enumerate(padded_direction) if value), None
    )
    if pivot is None:
        raise VerificationFailure("zero rational direction")
    scalar = (
        padded_remainder[pivot]
        * pow(padded_direction[pivot], modulus - 2, modulus)
        % modulus
    )
    return (
        all(
            padded_remainder[index]
            == scalar * padded_direction[index] % modulus
            for index in range(degree)
        ),
        scalar,
    )


@dataclass(frozen=True)
class RationalHostCase:
    name: str
    modulus: int
    domain: tuple[int, ...]
    dimension: int
    agreement: int
    denominator: tuple[int, ...]
    direction: tuple[int, ...]
    host_0: tuple[int, ...]
    host_1: tuple[int, ...]
    numerator: tuple[int, ...]

    @property
    def denominator_degree(self) -> int:
        return len(self.denominator) - 1

    @property
    def prefix_depth(self) -> int:
        return self.agreement - self.dimension - self.denominator_degree


def received_words(case: RationalHostCase) -> tuple[tuple[int, ...], tuple[int, ...]]:
    first = []
    second = []
    for point in case.domain:
        denominator_value = poly_eval(case.denominator, point, case.modulus)
        if denominator_value == 0:
            raise VerificationFailure(f"{case.name}: denominator root in domain")
        denominator_inverse = pow(denominator_value, case.modulus - 2, case.modulus)
        first.append(
            (
                poly_eval(case.host_0, point, case.modulus)
                + poly_eval(case.numerator, point, case.modulus)
                * denominator_inverse
            )
            % case.modulus
        )
        second.append(
            (
                poly_eval(case.host_1, point, case.modulus)
                - poly_eval(case.direction, point, case.modulus)
                * denominator_inverse
            )
            % case.modulus
        )
    return tuple(first), tuple(second)


def compiler_witnesses(
    case: RationalHostCase,
) -> tuple[set[tuple[int, tuple[int, ...], tuple[int, ...]]], Counter[int]]:
    modulus = case.modulus
    degree = case.denominator_degree
    leading = case.numerator[-1]
    leading_inverse = pow(leading, modulus - 2, modulus)
    prefix = tuple(
        coefficient(case.numerator, case.agreement - index)
        * leading_inverse
        % modulus
        for index in range(1, case.prefix_depth + 1)
    )
    first_word, second_word = received_words(case)
    witnesses: set[tuple[int, tuple[int, ...], tuple[int, ...]]] = set()
    multiplicities: Counter[int] = Counter()

    for support in combinations(case.domain, case.agreement):
        support_locator = locator(support, modulus)
        support_prefix = tuple(
            coefficient(support_locator, case.agreement - index)
            for index in range(1, case.prefix_depth + 1)
        )
        if support_prefix != prefix:
            continue
        difference = poly_sub(
            case.numerator, poly_scale(support_locator, leading, modulus), modulus
        )
        _, remainder = poly_divmod(difference, case.denominator, modulus)
        lies_in_span, slope = span_scalar(
            remainder, case.direction, degree, modulus
        )
        if not lies_in_span:
            continue

        adjusted = poly_sub(
            difference, poly_scale(case.direction, slope, modulus), modulus
        )
        quotient, division_remainder = poly_divmod(
            adjusted, case.denominator, modulus
        )
        require(not division_remainder, f"{case.name}: nonexact host division")
        explaining = poly_add(
            poly_add(
                case.host_0,
                poly_scale(case.host_1, slope, modulus),
                modulus,
            ),
            quotient,
            modulus,
        )
        require(
            len(explaining) <= case.dimension,
            f"{case.name}: explaining polynomial exceeds dimension",
        )

        agreement_set = tuple(
            point
            for point, first_value, second_value in zip(
                case.domain, first_word, second_word
            )
            if (first_value + slope * second_value) % modulus
            == poly_eval(explaining, point, modulus)
        )
        require(
            agreement_set == support,
            f"{case.name}: full agreement set is not the support",
        )
        require(
            not explained_on_support(
                second_word,
                support,
                case.domain,
                case.dimension,
                modulus,
            ),
            f"{case.name}: rational direction became support-wise common",
        )
        witness = (slope, support, pad(explaining, case.dimension))
        require(witness not in witnesses, f"{case.name}: duplicate compiler witness")
        witnesses.add(witness)
        multiplicities[slope] += 1

    return witnesses, multiplicities


def brute_force_witnesses(
    case: RationalHostCase,
) -> set[tuple[int, tuple[int, ...], tuple[int, ...]]]:
    modulus = case.modulus
    first_word, second_word = received_words(case)
    codewords = []
    for coefficients in product(range(modulus), repeat=case.dimension):
        polynomial = trim(coefficients)
        values = tuple(
            poly_eval(polynomial, point, modulus) for point in case.domain
        )
        codewords.append((coefficients, values))

    witnesses: set[tuple[int, tuple[int, ...], tuple[int, ...]]] = set()
    for slope in range(modulus):
        line_word = tuple(
            (first_value + slope * second_value) % modulus
            for first_value, second_value in zip(first_word, second_word)
        )
        for coefficients, codeword in codewords:
            agreement_set = tuple(
                point
                for point, line_value, code_value in zip(
                    case.domain, line_word, codeword
                )
                if line_value == code_value
            )
            if len(agreement_set) < case.agreement:
                continue
            for support in combinations(agreement_set, case.agreement):
                common = explained_on_support(
                    first_word,
                    support,
                    case.domain,
                    case.dimension,
                    modulus,
                ) and explained_on_support(
                    second_word,
                    support,
                    case.domain,
                    case.dimension,
                    modulus,
                )
                if not common:
                    witnesses.add((slope, support, coefficients))
    return witnesses


def reduced_direction_matches(case: RationalHostCase) -> list[tuple[object, ...]]:
    modulus = case.modulus
    _, second_word = received_words(case)
    interpolation_points = case.domain[: case.dimension]
    basis = interpolation_basis(interpolation_points, modulus)
    matches = []

    for degree in range(1, case.agreement - case.dimension + 1):
        for lower_coefficients in product(range(modulus), repeat=degree):
            denominator = trim(lower_coefficients + (1,))
            denominator_values = tuple(
                poly_eval(denominator, point, modulus) for point in case.domain
            )
            if any(value == 0 for value in denominator_values):
                continue
            for direction_coefficients in product(range(modulus), repeat=degree):
                direction = trim(direction_coefficients)
                if not direction or len(poly_gcd(denominator, direction, modulus)) > 1:
                    continue
                host_values = tuple(
                    (
                        received
                        + poly_eval(direction, point, modulus)
                        * pow(denominator_value, modulus - 2, modulus)
                    )
                    % modulus
                    for point, received, denominator_value in zip(
                        case.domain, second_word, denominator_values
                    )
                )
                host = interpolate(host_values[: case.dimension], basis, modulus)
                if len(host) > case.dimension:
                    continue
                if all(
                    poly_eval(host, point, modulus) == value
                    for point, value in zip(case.domain, host_values)
                ):
                    matches.append((degree, denominator, direction, host))
    return matches


def canonical_host_matches(case: RationalHostCase) -> list[tuple[object, ...]]:
    modulus = case.modulus
    first_word, _ = received_words(case)
    full_basis = interpolation_basis(case.domain, modulus)
    degree = case.denominator_degree
    matches = []

    for host_coefficients in product(range(modulus), repeat=case.dimension):
        host = trim(host_coefficients)
        numerator_values = tuple(
            poly_eval(case.denominator, point, modulus)
            * (received - poly_eval(host, point, modulus))
            % modulus
            for point, received in zip(case.domain, first_word)
        )
        numerator = interpolate(numerator_values, full_basis, modulus)
        if len(numerator) != case.agreement + 1 or numerator[-1] == 0:
            continue
        if any(
            coefficient(numerator, index) != 0
            for index in range(degree, degree + case.dimension)
        ):
            continue
        matches.append((host, numerator))
    return matches


def verify_case(
    case: RationalHostCase,
) -> tuple[set[tuple[int, tuple[int, ...], tuple[int, ...]]], Counter[int]]:
    modulus = case.modulus
    n = len(case.domain)
    degree = case.denominator_degree
    require(case.denominator[-1] == 1, f"{case.name}: denominator is not monic")
    require(
        len(poly_gcd(case.denominator, case.direction, modulus)) == 1,
        f"{case.name}: direction is not reduced",
    )
    require(case.direction, f"{case.name}: zero direction")
    require(
        all(poly_eval(case.denominator, point, modulus) for point in case.domain),
        f"{case.name}: denominator meets domain",
    )
    require(
        len(case.numerator) == case.agreement + 1,
        f"{case.name}: wrong numerator degree",
    )
    require(
        all(
            coefficient(case.numerator, index) == 0
            for index in range(degree, degree + case.dimension)
        ),
        f"{case.name}: canonical host gauge fails",
    )
    require(
        case.agreement * case.agreement - n * (case.dimension - 1) <= 0,
        f"{case.name}: case is not section-nonpositive",
    )
    require(
        case.dimension + 2 * degree < n,
        f"{case.name}: direction uniqueness degree gate fails",
    )

    compiled, multiplicities = compiler_witnesses(case)
    brute = brute_force_witnesses(case)
    require(compiled == brute, f"{case.name}: compiler is not witness-exhaustive")

    explanation_occupancy: dict[tuple[int, tuple[int, ...]], set[tuple[int, ...]]] = (
        defaultdict(set)
    )
    support_slopes: dict[tuple[int, ...], set[int]] = defaultdict(set)
    for slope, support, explaining in compiled:
        explanation_occupancy[(slope, explaining)].add(support)
        support_slopes[support].add(slope)
    require(
        all(len(supports) == 1 for supports in explanation_occupancy.values()),
        f"{case.name}: explanation occupancy is not one",
    )
    require(
        all(len(slopes) == 1 for slopes in support_slopes.values()),
        f"{case.name}: one support carries multiple slopes",
    )
    require(
        len(explanation_occupancy) == len(compiled),
        f"{case.name}: LineRay pair count mismatch",
    )
    require(
        sum(multiplicities.values()) == len(compiled),
        f"{case.name}: slope fibers do not add back",
    )

    cells: dict[int, list[tuple[int, tuple[int, ...], tuple[int, ...]]]] = (
        defaultdict(list)
    )
    for witness in compiled:
        cells[min(witness[1])].append(witness)
    seen_slopes: set[int] = set()
    for cell_index in sorted(cells):
        cell_slopes = {witness[0] for witness in cells[cell_index]}
        fresh_slopes = cell_slopes - seen_slopes
        require(
            len(fresh_slopes) <= len(cells[cell_index]),
            f"{case.name}: first-match cell exceeds support count",
        )
        seen_slopes.update(cell_slopes)
    require(
        seen_slopes == set(multiplicities),
        f"{case.name}: first-match union misses a slope",
    )

    direction_matches = reduced_direction_matches(case)
    expected_direction = (
        degree,
        case.denominator,
        case.direction,
        case.host_1,
    )
    require(
        direction_matches == [expected_direction],
        f"{case.name}: reduced direction normal form is not unique",
    )

    host_matches = canonical_host_matches(case)
    require(
        host_matches == [(case.host_0, case.numerator)],
        f"{case.name}: canonical host is not unique",
    )
    return compiled, multiplicities


def verify_integer_gate() -> int:
    parameter_tuples = 0
    for n in range(2, 65):
        for dimension in range(1, n):
            for agreement in range(dimension + 1, n + 1):
                if agreement * agreement - n * (dimension - 1) > 0:
                    continue
                require(agreement < n, "J<=0 failed to force a<n")
                for degree in range(1, agreement - dimension + 1):
                    require(
                        dimension + 2 * degree < n,
                        "J<=0 failed the rational-direction degree gate",
                    )
                    parameter_tuples += 1
    return parameter_tuples


def verify_optimization_safety() -> None:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    require(
        not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
        "verifier contains optimization-sensitive assert statements",
    )


def format_multiplicities(multiplicities: Counter[int]) -> str:
    return ",".join(
        f"{slope}:{multiplicities[slope]}" for slope in sorted(multiplicities)
    )


def main() -> None:
    verify_optimization_safety()
    parameter_tuples = verify_integer_gate()

    common = {
        "modulus": 17,
        "domain": tuple(range(13)),
        "dimension": 3,
        "agreement": 5,
        "numerator": (0, 0, 0, 0, 0, 1),
    }
    simple_pole = RationalHostCase(
        name="d1_nonseparating",
        denominator=(4, 1),
        direction=(1,),
        host_0=(),
        host_1=(),
        **common,
    )
    quadratic_host = RationalHostCase(
        name="d2_reduced_host",
        denominator=(12, 7, 1),
        direction=(1, 1),
        host_0=(2, 3, 4),
        host_1=(5, 6, 7),
        **common,
    )

    simple_witnesses, simple_multiplicities = verify_case(simple_pole)
    quadratic_witnesses, quadratic_multiplicities = verify_case(quadratic_host)

    expected_simple = Counter(
        {
            0: 4,
            1: 4,
            2: 5,
            3: 7,
            4: 5,
            5: 6,
            6: 4,
            7: 4,
            8: 6,
            9: 5,
            10: 5,
            11: 7,
            12: 3,
            14: 5,
            15: 3,
            16: 3,
        }
    )
    require(
        simple_multiplicities == expected_simple,
        "F_17 simple-pole slope table changed",
    )
    require(len(simple_witnesses) == 76, "F_17 support count is not 76")
    require(len(simple_multiplicities) == 16, "F_17 slope count is not 16")
    require(max(simple_multiplicities.values()) == 7, "F_17 max fiber is not 7")
    require(13 not in simple_multiplicities, "F_17 absent slope 13 appeared")

    earlier = {3, 11}
    deleted = sum(simple_multiplicities[slope] for slope in earlier)
    residual_witnesses = {
        witness for witness in simple_witnesses if witness[0] not in earlier
    }
    residual_slopes = set(simple_multiplicities) - earlier
    require(deleted == 14, "earlier-owner deletion did not remove 14 witnesses")
    require(
        len(residual_witnesses) == 62,
        "earlier-owner deletion did not leave 62 witnesses",
    )
    require(
        len(residual_slopes) == 14,
        "earlier-owner deletion did not leave 14 slopes",
    )

    require(len(quadratic_witnesses) == 77, "d=2 support count is not 77")
    require(len(quadratic_multiplicities) == 15, "d=2 slope count is not 15")
    require(
        max(quadratic_multiplicities.values()) == 8,
        "d=2 maximum slope fiber is not 8",
    )

    print("canonical_reduced_rational_host_compiler")
    print("field=F_17 domain=0..12 n=13 k=3 a=5 J=-1")
    print(f"integer_degree_gate_tuples={parameter_tuples}")
    print("optimization_safe=no_assert_statements")
    print(
        "d=1 supports=76 line_rays=76 slopes=16 max_slope_fiber=7 "
        "absent_slopes=13"
    )
    print(f"d=1 slope_multiplicities={format_multiplicities(simple_multiplicities)}")
    print("d=1 earlier_E=3,11 deleted=14 residual_supports=62 residual_slopes=14")
    print("d=1 direction_normal_forms=1 canonical_hosts=1 brute_force_match=PASS")
    print(
        "d=2 supports=77 line_rays=77 slopes=15 max_slope_fiber=8 "
        "direction_normal_forms=1 canonical_hosts=1 brute_force_match=PASS"
    )
    print(f"checks={CHECKS}")
    print("RESULT: PASS")


if __name__ == "__main__":
    main()
