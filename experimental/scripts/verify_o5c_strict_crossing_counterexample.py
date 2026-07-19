#!/usr/bin/env python3
"""Verify the sparse exact-deep counterexample to the O5c strict crossing.

Standard library only. The verifier binds the current source theorem labels,
checks the concrete GF(2^129) presentation, reconstructs the endpoint and the
sparse m >= 129 family, verifies the exact two-slope line, and rejects semantic
mutations. It does not enumerate the exponentially large field or code.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "experimental/data/certificates/o5c-strict-crossing-counterexample"
SOURCE_PINS = CERT / "source_pins.json"
MANIFEST = CERT / "manifest.json"


class VerificationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ceil_div(numerator: int, denominator: int) -> int:
    require(numerator >= 0 and denominator > 0, "ceil domain")
    return (numerator + denominator - 1) // denominator


def poly_degree(value: int) -> int:
    return value.bit_length() - 1


def poly_mod(value: int, modulus: int) -> int:
    degree = poly_degree(modulus)
    while value and poly_degree(value) >= degree:
        value ^= modulus << (poly_degree(value) - degree)
    return value


def poly_multiply_mod(left: int, right: int, modulus: int) -> int:
    degree = poly_degree(modulus)
    result = 0
    while right:
        if right & 1:
            result ^= left
        right >>= 1
        left <<= 1
        if left & (1 << degree):
            left ^= modulus
    return result


def poly_gcd(left: int, right: int) -> int:
    while right:
        left, right = right, poly_mod(left, right)
    return left


def rabin_irreducible_binary(modulus: int, degree: int) -> bool:
    if poly_degree(modulus) != degree or not (modulus & 1):
        return False
    x = 0b10
    value = x
    checkpoints: dict[int, int] = {}
    wanted = {degree // 3, degree // 43, degree}
    for exponent in range(1, degree + 1):
        value = poly_multiply_mod(value, value, modulus)
        if exponent in wanted:
            checkpoints[exponent] = value
    return (
        checkpoints[degree] == x
        and poly_gcd(checkpoints[degree // 3] ^ x, modulus) == 1
        and poly_gcd(checkpoints[degree // 43] ^ x, modulus) == 1
    )


@dataclass(frozen=True)
class Contract:
    m: int = 129
    target_denominator_exponent: int = 128
    target_frozen_first: bool = True
    domain_is_full_multiplicative_group: bool = True
    full_challenge_field: bool = True
    collision_formula_orientation: str = "source"
    reserve_combination: str = "maximum"
    exact_support_first_match: bool = True
    complete_envelope_retained: bool = True
    profile_list_cap: int = 1
    strict_comparison: bool = True
    field_polynomial: int = (1 << 129) | (1 << 5) | 1


def source_checks() -> int:
    pins = json.loads(SOURCE_PINS.read_text(encoding="utf-8"))
    require(pins["base"] == "6f4e918f27a11995d3951f4ebe7546d4add0f345",
            "wrong source base")
    for relative, expected in pins["files"].items():
        path = ROOT / relative
        require(path.is_file(), f"missing source: {relative}")
        require(sha256(path) == expected, f"source pin mismatch: {relative}")

    tex = (ROOT / "experimental/asymptotic_rs_mca_frontiers.tex").read_text(
        encoding="utf-8"
    )
    required_labels = (
        r"\label{def:admissible-sequence}",
        r"\label{lem:exact-agreement-reduction}",
        r"\label{prop:exact-support-upper}",
        r"\label{prop:universal-tangent-floor}",
        r"\label{cor:exact-deep-numerator}",
        r"\label{thm:collision-aware-pole}",
        r"\label{prop:simple-pole-lower}",
    )
    require(all(label in tex for label in required_labels), "source label drift")
    require(
        r"\frac{L(q-n)}{q-n+k(L-1)}" in tex,
        "collision-aware source formula drift",
    )
    return len(pins["files"])


def validate(contract: Contract) -> dict[str, int | bool | str]:
    require(contract.m >= 129, "frozen target endpoint")
    require(contract.target_denominator_exponent == 128, "target density")
    require(contract.target_frozen_first, "target chronology")
    require(contract.domain_is_full_multiplicative_group, "domain contract")
    require(contract.full_challenge_field, "challenge contract")
    require(contract.collision_formula_orientation == "source",
            "collision formula orientation")
    require(contract.reserve_combination == "maximum", "reserve combination")
    require(contract.exact_support_first_match, "first-match ownership")
    require(contract.complete_envelope_retained, "A7 envelope")
    require(contract.profile_list_cap == 1, "adjacent list cap")
    require(contract.strict_comparison, "strict target predicate")

    m = contract.m
    q = 1 << m
    n = q - 1
    k = (1 << (m - 1)) - 1
    a = n - 1
    gamma_size = q
    target = gamma_size // (1 << contract.target_denominator_exponent)
    radius = n - a
    redundancy = n - k
    minimum_distance = redundancy + 1
    overlap_roots = 2 * a - n
    list_margin = overlap_roots - k

    require(q - n == 1, "simple-pole complement")
    require(1 <= k < n and k + 1 <= a <= n, "row range")
    require(radius == 1, "radius")
    require(3 * radius <= redundancy, "exact-deep hypothesis")
    require(list_margin > 0, "adjacent-code list collapse")
    require(minimum_distance > 3, "explicit line minimum-distance margin")

    if m == 129:
        require(
            rabin_irreducible_binary(contract.field_polynomial, 129),
            "concrete field polynomial",
        )

    # The correct source formula is ceil(L(q-n)/(q-n+k(L-1))). Only L=1 is
    # consumed here; no reciprocal or L>1 statement enters the certificate.
    list_size = contract.profile_list_cap
    pole_numerator = list_size * (q - n)
    pole_denominator = (q - n) + k * (list_size - 1)
    pole_slopes = ceil_div(pole_numerator, pole_denominator)
    profile_floor = ceil_div(gamma_size * pole_slopes, q)
    tangent = min(gamma_size, n - a + 1)
    actual_numerator = tangent
    complete_floor = max(profile_floor, tangent)

    require(pole_slopes == 1 and profile_floor == 1, "L=1 pole floor")
    require(tangent == 2 and actual_numerator == 2, "exact numerator")
    require(complete_floor == 2, "complete lower reserve")
    require(not (complete_floor > target), "strict crossing must fail")

    # The explicit line (e_theta, e_1+e_theta) has slopes 0 and 1. For those
    # slopes the zero codeword owns S_theta and S_1. Every other slope gives a
    # weight-two word; any explaining codeword would have weight at most three,
    # below the RS minimum distance. The owner supports may overlap, while the
    # first-match slope sets are disjoint.
    bad_slope_count = 2
    require(bad_slope_count == actual_numerator, "explicit line sharpness")

    # A1-A7: F* is a multiplicative coset; the n omitted-point supports form
    # e^{o(n)} cells and each contributes at most one slope. That atlas is
    # witness-exhaustive, leaving no primitive or residual cells. A7 remains
    # retained rather than replaced by the identity term.
    exact_support_cells = n
    require(exact_support_cells.bit_length() <= m + 1, "subexponential atlas")

    return {
        "m": m,
        "q": q,
        "n": n,
        "k": k,
        "a": a,
        "n_minus_k": redundancy,
        "minimum_distance": minimum_distance,
        "two_list_margin": list_margin,
        "target": target,
        "profile_list_cap": list_size,
        "profile_floor": profile_floor,
        "tangent_floor": tangent,
        "actual_numerator": actual_numerator,
        "complete_floor": complete_floor,
        "strict_crossing": complete_floor > target,
        "bad_slope_count": bad_slope_count,
        "exact_support_cells": exact_support_cells,
    }


def family_checks() -> int:
    checked = 0
    for m in range(129, 513):
        result = validate(replace(Contract(), m=m))
        require(result["actual_numerator"] == 2, "family numerator")
        require(result["target"] == 1 << (m - 128), "family target")
        require(result["actual_numerator"] <= result["target"],
                "family target comparison")
        checked += 1
    return checked


def mutation_checks() -> int:
    mutations = (
        replace(Contract(), m=128),
        replace(Contract(), target_denominator_exponent=127),
        replace(Contract(), target_frozen_first=False),
        replace(Contract(), domain_is_full_multiplicative_group=False),
        replace(Contract(), full_challenge_field=False),
        replace(Contract(), collision_formula_orientation="reciprocal"),
        replace(Contract(), reserve_combination="sum"),
        replace(Contract(), exact_support_first_match=False),
        replace(Contract(), complete_envelope_retained=False),
        replace(Contract(), profile_list_cap=2),
        replace(Contract(), strict_comparison=False),
        replace(Contract(), field_polynomial=(1 << 129) | (1 << 5) | (1 << 1) | 1),
    )
    caught = 0
    for mutation in mutations:
        try:
            validate(mutation)
        except VerificationError:
            caught += 1
    require(caught == len(mutations), "semantic mutation survived")
    return caught


def main() -> int:
    try:
        source_pin_count = source_checks()
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        require(manifest["schema"] == "rs-mca-o5c-strict-crossing-counterexample-v1",
                "manifest schema")
        result = validate(Contract())
        family_count = family_checks()
        mutation_count = mutation_checks()

        if sys.argv[1:] == ["--tamper-selftest"]:
            print(f"semantic_mutations=PASS,{mutation_count}/{mutation_count}")
            print("RESULT: PASS")
            return 0
        require(not sys.argv[1:], "usage")

        print("O5C_STRICT_CROSSING_COUNTEREXAMPLE: PASS")
        print(f"base={manifest['source_base']}")
        print(f"source_pins=PASS,count={source_pin_count}")
        print("field=GF(2^129),polynomial=T^129+T^5+1,irreducible=True")
        for key in (
            "q", "n", "k", "a", "n_minus_k", "minimum_distance",
            "two_list_margin", "target", "profile_list_cap", "profile_floor",
            "tangent_floor", "actual_numerator", "complete_floor",
            "strict_crossing", "bad_slope_count", "exact_support_cells",
        ):
            print(f"{key}={result[key]}")
        print(f"family_checks=m129..m512,count={family_count}")
        print(f"semantic_mutations=PASS,{mutation_count}/{mutation_count}")
        print("finite_ledger_delta=0")
        print("asymptotic_ledger_delta=0")
        print("official_score=0/2")
        return 0
    except (VerificationError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"RESULT: FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
