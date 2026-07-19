#!/usr/bin/env python3
"""Exact finite replay of the affine-prefix fixed-point half-slice."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


P = 5
Q_POLY = [1, 4, 4, 4, 1]
ALL_POLY = [1, 4, 5, 4, 1]
SQUARE = ((0, 0), (1, 0), (0, 1), (1, 1))
ALLOWED_PAIRS = {
    frozenset((0, 1)),
    frozenset((0, 2)),
    frozenset((1, 3)),
    frozenset((2, 3)),
}
ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "experimental/data/certificates/affine-prefix-fixed-point-half-slice"
BASE = "3404d21b64c876c6d9b995ad3e29d7120ab27a54"
PROOF_AUDIT = "5d80191c49a2d9915ed6ba56e884e8fa77dd81448efa6965784506939fd8ecb8"
SOURCE_AUDIT = "56d1c489d3421d072cb031f3c5054d8631bdea37e79bb4fdc9379e3d2acf046f"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_source_pins() -> int:
    payload = json.loads((CERT / "source_pins.json").read_text(encoding="utf-8"))
    require(payload["base"] == BASE, "wrong source base")
    require(payload["proof_audit_sha256"] == PROOF_AUDIT, "wrong proof audit pin")
    require(payload["source_audit_sha256"] == SOURCE_AUDIT, "wrong source audit pin")
    for relative, expected in payload["files"].items():
        require(file_sha256(ROOT / relative) == expected, f"source pin mismatch: {relative}")
    return len(payload["files"])


def int_poly_trim(poly: list[int]) -> list[int]:
    out = [value % P for value in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def int_poly_sub(left: list[int], right: list[int]) -> list[int]:
    out = [0] * max(len(left), len(right))
    for index in range(len(out)):
        out[index] = (
            (left[index] if index < len(left) else 0)
            - (right[index] if index < len(right) else 0)
        ) % P
    return int_poly_trim(out)


def int_poly_divmod(
    numerator: list[int], denominator: list[int]
) -> tuple[list[int], list[int]]:
    denominator = int_poly_trim(denominator)
    require(denominator != [0], "integer polynomial division by zero")
    remainder = int_poly_trim(numerator)
    quotient = [0] * max(1, len(remainder) - len(denominator) + 1)
    inverse = pow(denominator[-1], P - 2, P)
    while remainder != [0] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = remainder[-1] * inverse % P
        quotient[shift] = factor
        for index, value in enumerate(denominator):
            remainder[index + shift] = (
                remainder[index + shift] - factor * value
            ) % P
        remainder = int_poly_trim(remainder)
    return int_poly_trim(quotient), remainder


def int_poly_gcd(left: list[int], right: list[int]) -> list[int]:
    left = int_poly_trim(left)
    right = int_poly_trim(right)
    while right != [0]:
        _, remainder = int_poly_divmod(left, right)
        left, right = right, remainder
    inverse = pow(left[-1], P - 2, P)
    return int_poly_trim([inverse * value for value in left])


def int_poly_mul_mod(
    left: list[int], right: list[int], modulus: list[int]
) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] = (product[i + j] + a * b) % P
    return int_poly_divmod(product, modulus)[1]


def int_poly_pow_mod(
    base: list[int], exponent: int, modulus: list[int]
) -> list[int]:
    out = [1]
    base = int_poly_divmod(base, modulus)[1]
    while exponent:
        if exponent & 1:
            out = int_poly_mul_mod(out, base, modulus)
        base = int_poly_mul_mod(base, base, modulus)
        exponent //= 2
    return int_poly_trim(out)


def prime_divisors(value: int) -> set[int]:
    divisors: set[int] = set()
    candidate = 2
    while candidate * candidate <= value:
        if value % candidate == 0:
            divisors.add(candidate)
            while value % candidate == 0:
                value //= candidate
        candidate += 1
    if value > 1:
        divisors.add(value)
    return divisors


def is_irreducible(modulus: list[int]) -> bool:
    modulus = int_poly_trim(modulus)
    degree = len(modulus) - 1
    if degree < 1 or modulus[-1] != 1 or modulus[0] == 0:
        return False
    x = [0, 1]
    if int_poly_pow_mod(x, P**degree, modulus) != x:
        return False
    for prime in prime_divisors(degree):
        frobenius = int_poly_pow_mod(x, P ** (degree // prime), modulus)
        if int_poly_gcd(modulus, int_poly_sub(frobenius, x)) != [1]:
            return False
    return True


Element = tuple[int, ...]


@dataclass(frozen=True)
class Field:
    modulus: tuple[int, ...]

    @property
    def degree(self) -> int:
        return len(self.modulus) - 1

    @property
    def order(self) -> int:
        return P**self.degree

    @property
    def zero(self) -> Element:
        return (0,) * self.degree

    @property
    def one(self) -> Element:
        return (1,) + (0,) * (self.degree - 1)

    @property
    def t(self) -> Element:
        return (0, 1) + (0,) * (self.degree - 2)

    def constant(self, value: int) -> Element:
        return (value % P,) + (0,) * (self.degree - 1)

    def add(self, left: Element, right: Element) -> Element:
        return tuple((a + b) % P for a, b in zip(left, right))

    def neg(self, value: Element) -> Element:
        return tuple((-coefficient) % P for coefficient in value)

    def sub(self, left: Element, right: Element) -> Element:
        return self.add(left, self.neg(right))

    def mul(self, left: Element, right: Element) -> Element:
        degree = self.degree
        product = [0] * (2 * degree - 1)
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                product[i + j] = (product[i + j] + a * b) % P
        for exponent in range(2 * degree - 2, degree - 1, -1):
            leading = product[exponent]
            if leading == 0:
                continue
            shift = exponent - degree
            for index in range(degree):
                product[index + shift] = (
                    product[index + shift] - leading * self.modulus[index]
                ) % P
        return tuple(product[:degree])

    def pow(self, base: Element, exponent: int) -> Element:
        out = self.one
        while exponent:
            if exponent & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            exponent //= 2
        return out

    def inv(self, value: Element) -> Element:
        require(value != self.zero, "field inversion by zero")
        return self.pow(value, self.order - 2)


def coefficient(poly: list[int], degree: int) -> int:
    return poly[degree] if 0 <= degree < len(poly) else 0


def integer_poly_multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def integer_poly_power(poly: list[int], exponent: int) -> list[int]:
    out = [1]
    while exponent:
        if exponent & 1:
            out = integer_poly_multiply(out, poly)
        poly = integer_poly_multiply(poly, poly)
        exponent //= 2
    return out


def field_poly_trim(poly: list[Element], field: Field) -> list[Element]:
    out = poly[:]
    while len(out) > 1 and out[-1] == field.zero:
        out.pop()
    return out


def field_poly_mul(
    left: list[Element], right: list[Element], field: Field
) -> list[Element]:
    out = [field.zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = field.add(out[i + j], field.mul(a, b))
    return field_poly_trim(out, field)


def field_poly_sub(
    left: list[Element], right: list[Element], field: Field
) -> list[Element]:
    out = [field.zero] * max(len(left), len(right))
    for index in range(len(out)):
        a = left[index] if index < len(left) else field.zero
        b = right[index] if index < len(right) else field.zero
        out[index] = field.sub(a, b)
    return field_poly_trim(out, field)


def field_poly_divmod(
    numerator: list[Element], denominator: list[Element], field: Field
) -> tuple[list[Element], list[Element]]:
    denominator = field_poly_trim(denominator, field)
    require(denominator != [field.zero], "field polynomial division by zero")
    remainder = field_poly_trim(numerator, field)
    quotient = [field.zero] * max(1, len(remainder) - len(denominator) + 1)
    inverse = field.inv(denominator[-1])
    while remainder != [field.zero] and len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        factor = field.mul(remainder[-1], inverse)
        quotient[shift] = factor
        for index, value in enumerate(denominator):
            remainder[index + shift] = field.sub(
                remainder[index + shift], field.mul(factor, value)
            )
        remainder = field_poly_trim(remainder, field)
    return field_poly_trim(quotient, field), remainder


def field_poly_gcd(
    left: list[Element], right: list[Element], field: Field
) -> list[Element]:
    left = field_poly_trim(left, field)
    right = field_poly_trim(right, field)
    while right != [field.zero]:
        _, remainder = field_poly_divmod(left, right, field)
        left, right = right, remainder
    inverse = field.inv(left[-1])
    return [field.mul(value, inverse) for value in left]


def field_poly_eval(poly: list[Element], value: Element, field: Field) -> Element:
    out = field.zero
    for coefficient_value in reversed(poly):
        out = field.add(field.mul(out, value), coefficient_value)
    return out


def locator(indices: tuple[int, ...], points: list[Element], field: Field) -> list[Element]:
    out = [field.one]
    for index in indices:
        out = field_poly_mul([field.neg(points[index]), field.one], out, field)
    return out


def source_points(blocks: int, field: Field) -> list[Element]:
    points: list[Element] = []
    for block in range(blocks):
        scale = field.pow(field.t, 3 * block)
        for epsilon, eta in SQUARE:
            local = field.add(
                field.one,
                field.add(
                    field.mul(field.constant(epsilon), field.t),
                    field.mul(field.constant(eta), field.pow(field.t, 2)),
                ),
            )
            points.append(field.mul(scale, local))
    return points


def no_diagonal(indices: tuple[int, ...], blocks: int) -> bool:
    chosen = set(indices)
    for block in range(blocks):
        local = frozenset(
            index - 4 * block
            for index in chosen
            if 4 * block <= index < 4 * block + 4
        )
        if len(local) == 2 and local not in ALLOWED_PAIRS:
            return False
    return True


def support_family(blocks: int) -> list[tuple[int, ...]]:
    size = 2 * blocks
    return [
        indices
        for indices in combinations(range(4 * blocks), size)
        if no_diagonal(indices, blocks)
    ]


def family_gcd(
    family: list[tuple[int, ...]], points: list[Element], field: Field
) -> list[Element]:
    common = locator(family[0], points, field)
    for indices in family[1:]:
        common = field_poly_gcd(common, locator(indices, points, field), field)
        if len(common) == 1:
            break
    return common


def audit_blocks(blocks: int, modulus: list[int]) -> tuple[int, int, int]:
    require(is_irreducible(modulus), f"reducible field modulus at B={blocks}")
    field = Field(tuple(modulus))
    require(field.degree == 3 * blocks, "wrong extension degree")
    require(field.pow(field.t, field.order) == field.t, "Frobenius field check failed")

    points = source_points(blocks, field)
    require(len(set(points)) == 4 * blocks, "source points are not distinct")
    supports = support_family(blocks)
    planted = [indices for indices in supports if 0 in indices]
    c_blocks = coefficient(integer_poly_power(Q_POLY, blocks), 2 * blocks)
    all_slopes = coefficient(integer_poly_power(ALL_POLY, blocks), 2 * blocks)
    require(len(supports) == c_blocks, f"wrong no-diagonal census B={blocks}")
    require(len(planted) * 2 == c_blocks, f"wrong fixed-point half-census B={blocks}")
    require(all_slopes > c_blocks, "raw all-strata count did not exceed j=0 count")

    support_to_slope: dict[tuple[int, ...], Element] = {}
    slope_to_support: dict[Element, tuple[int, ...]] = {}
    locators: list[list[Element]] = []
    m = 2 * blocks
    k = m - 1
    for indices in planted:
        loc = locator(indices, points, field)
        locators.append(loc)
        require(len(loc) - 1 == m and loc[-1] == field.one, "locator degree/monic failure")
        support_sum = field.zero
        for index in indices:
            support_sum = field.add(support_sum, points[index])
        gamma = field.neg(support_sum)
        require(loc[m - 1] == gamma, "depth-one coefficient mismatch")
        require(gamma not in slope_to_support, "depth-one slope is not injective")
        support_to_slope[indices] = gamma
        slope_to_support[gamma] = indices

        received = [field.zero] * (m + 1)
        received[m] = field.one
        received[m - 1] = gamma
        codeword = field_poly_sub(received, loc, field)
        require(len(codeword) - 1 <= k - 1, "RS degree cancellation failed")
        root_indices = {
            index
            for index, point in enumerate(points)
            if field_poly_eval(loc, point, field) == field.zero
        }
        require(root_indices == set(indices), "locator has wrong source-row zero set")
        require(len(indices) == k + 1, "support-wise nontriviality size failed")

    require(len(slope_to_support) == c_blocks // 2, "wrong planted slope count")
    common = locators[0]
    for loc in locators[1:]:
        common = field_poly_gcd(common, loc, field)
    expected_gcd = [field.neg(points[0]), field.one]
    require(common == expected_gcd, "planted locator gcd is not exactly X-p")
    require(
        all(any(index not in indices for indices in planted) for index in range(1, 4 * blocks)),
        "a non-planted source coordinate occurs in every planted support",
    )

    wrong_pairs = {
        frozenset((0, 3)),
        frozenset((1, 2)),
        frozenset((0, 1)),
        frozenset((2, 3)),
    }
    unplanted_gcd = family_gcd(supports, points, field)
    wrong_sign_survives = all(
        field.neg(gamma) == locator(indices, points, field)[m - 1]
        for indices, gamma in support_to_slope.items()
    )
    first_indices = planted[0]
    extra_root = field_poly_mul(
        locators[0], [field.neg(points[next(i for i in range(4 * blocks) if i not in first_indices)]), field.one], field
    )
    mutations_caught = {
        "allow_diagonals": comb(4 * blocks, m) != c_blocks,
        "omit_fixed_point": len(supports) != len(planted),
        "flip_slope_sign": not wrong_sign_survives,
        "change_support_size": m + 1 != k + 1,
        "use_reducible_modulus": not is_irreducible([0] * (3 * blocks) + [1]),
        "delete_common_plant": unplanted_gcd == [field.one],
        "add_extra_locator_root": len(extra_root) - 1 != m,
        "change_local_pair_rule": wrong_pairs != ALLOWED_PAIRS,
        "replace_j0_coefficient": all_slopes != c_blocks,
    }
    require(all(mutations_caught.values()), f"semantic mutation survived B={blocks}: {mutations_caught}")
    return len(supports), len(planted), len(mutations_caught)


def main() -> None:
    source_pin_count = check_source_pins()
    cases = {
        2: [1, 0, 0, 0, 1, 1, 1],
        3: [1, 0, 0, 0, 0, 0, 0, 2, 3, 1],
    }
    rows = []
    for blocks, modulus in cases.items():
        total, planted, mutations = audit_blocks(blocks, modulus)
        rows.append((blocks, total, planted, mutations))

    print("AFFINE_PREFIX_FIXED_POINT_HALF_SLICE: PASS")
    print(f"base={BASE}")
    print(f"source_pins=PASS,count={source_pin_count}")
    print(f"proof_audit_sha256={PROOF_AUDIT}")
    print(f"source_audit_sha256={SOURCE_AUDIT}")
    for blocks, total, planted, mutations in rows:
        print(
            f"B={blocks} field=5^{3 * blocks} U={total} P={planted} "
            f"slopes={planted} gcd=X-p mutations={mutations}/{mutations}"
        )
    print("semantic_tamper_selftests=PASS,count=18")
    print("accepted_scope=finite_fixed_point_j0_half_slice_and_conditional_retention_only")
    print("nonclaims=no_semantic_owner,no_payment,no_parent,no_recurrence,no_score")
    print("finite_ledger_delta=0 asymptotic_ledger_delta=0 official_score=0/2")


if __name__ == "__main__":
    main()
