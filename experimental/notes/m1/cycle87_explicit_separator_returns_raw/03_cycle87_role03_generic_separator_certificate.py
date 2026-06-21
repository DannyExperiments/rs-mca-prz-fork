#!/usr/bin/env python3
"""Replay the Cycle87 Role03 generic projective-separator root count.

This certifies existence of some y in L\\F0 with mu_proj(y)=1, assuming the
banked Cycle84 packet consists of P distinct 113-element supports in F0.
It deliberately does not claim that the fixed candidate y=U is good.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path
from typing import Iterable

P_CHAR = 17
DEG_F0 = 16
SUPPORT_SIZE = 113
PACKET_SUPPORTS = 52_747_567_104
OCCUPANCY = 52_747_567_092
TARGET_BITS = 128

# f(X) = X^16 + X^8 + 3 over F_17, low coefficient first.
F_MOD = [3] + [0] * 7 + [1] + [0] * 7 + [1]


def trim(a: list[int]) -> list[int]:
    while len(a) > 1 and a[-1] % P_CHAR == 0:
        a.pop()
    return [x % P_CHAR for x in a]


def poly_add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % P_CHAR
    return trim(out)


def poly_sub(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % P_CHAR
    return trim(out)


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] = (out[i + j] + ai * bj) % P_CHAR
    return trim(out)


def inv_mod_p(a: int) -> int:
    a %= P_CHAR
    if a == 0:
        raise ZeroDivisionError
    return pow(a, P_CHAR - 2, P_CHAR)


def poly_divmod(a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [0], a
    q = [0] * (len(a) - len(b) + 1)
    inv_lc = inv_mod_p(b[-1])
    while a != [0] and len(a) >= len(b):
        d = len(a) - len(b)
        c = a[-1] * inv_lc % P_CHAR
        q[d] = c
        for i, bi in enumerate(b):
            a[i + d] = (a[i + d] - c * bi) % P_CHAR
        a = trim(a)
    return trim(q), a


def poly_mod(a: list[int], m: list[int]) -> list[int]:
    return poly_divmod(a, m)[1]


def poly_gcd(a: list[int], b: list[int]) -> list[int]:
    a, b = trim(a[:]), trim(b[:])
    while b != [0]:
        a, b = b, poly_mod(a, b)
    if a == [0]:
        return [0]
    inv = inv_mod_p(a[-1])
    return trim([(inv * x) % P_CHAR for x in a])


def poly_pow_mod(base: list[int], exponent: int, modulus: list[int]) -> list[int]:
    result = [1]
    base = poly_mod(base, modulus)
    while exponent:
        if exponent & 1:
            result = poly_mod(poly_mul(result, base), modulus)
        base = poly_mod(poly_mul(base, base), modulus)
        exponent >>= 1
    return result


def verify_f0_modulus_irreducible() -> None:
    """Rabin irreducibility test for degree 16 over F_17."""
    x = [0, 1]
    # n=16 has the single prime divisor 2.
    x_p8 = poly_pow_mod(x, P_CHAR ** 8, F_MOD)
    g = poly_gcd(poly_sub(x_p8, x), F_MOD)
    assert g == [1], f"gcd test failed: {g}"
    x_p16 = poly_pow_mod(x, P_CHAR ** 16, F_MOD)
    assert poly_sub(x_p16, x) == [0], "Frobenius closure test failed"


# F0 elements are represented as 16 coefficients in the X-power basis.
def f0_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((a[i] + b[i]) % P_CHAR for i in range(DEG_F0))


def f0_mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    product = [0] * (2 * DEG_F0 - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            product[i + j] = (product[i + j] + ai * bj) % P_CHAR
    # X^16 = -X^8 - 3.
    for d in range(2 * DEG_F0 - 2, DEG_F0 - 1, -1):
        c = product[d] % P_CHAR
        if c:
            product[d - 8] = (product[d - 8] - c) % P_CHAR
            product[d - 16] = (product[d - 16] - 3 * c) % P_CHAR
            product[d] = 0
    return tuple(product[:DEG_F0])


def f0_pow(a: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    one = (1,) + (0,) * (DEG_F0 - 1)
    result = one
    base = a
    while exponent:
        if exponent & 1:
            result = f0_mul(result, base)
        base = f0_mul(base, base)
        exponent >>= 1
    return result


def main() -> None:
    verify_f0_modulus_irreducible()

    q0 = P_CHAR ** DEG_F0
    q_line = q0 ** 3
    outside_base = q_line - q0

    one = (1,) + (0,) * (DEG_F0 - 1)
    x = (0, 1) + (0,) * (DEG_F0 - 2)
    two = (2,) + (0,) * (DEG_F0 - 1)
    beta = f0_add(x, two)
    eta = tuple(6 if i == 9 else 0 for i in range(DEG_F0))
    assert f0_pow(eta, 256) == one
    assert f0_pow(eta, 128) != one
    assert f0_pow(beta, 256) != one  # beta is not in D=<eta>
    assert pow(P_CHAR, 16, 256) == 1 and pow(P_CHAR, 8, 256) != 1
    beta_cubic_character = f0_pow(beta, (q0 - 1) // 3)
    expected_character = tuple(2 if i == 0 else 5 if i == 8 else 0 for i in range(DEG_F0))
    assert beta_cubic_character == expected_character
    assert beta_cubic_character != one
    # Since q0 == 1 mod 3, beta is a noncube. A reducible cubic has a root,
    # so U^3-beta is irreducible and defines the degree-3 field L/F0.
    assert q0 % 3 == 1

    pair_count = PACKET_SUPPORTS * (PACKET_SUPPORTS - 1) // 2
    # Simple uniform bound: 113 roots for every lambda in F0^x.
    projective_bad_bound = SUPPORT_SIZE * (q0 - 1) * pair_count
    # Slightly sharper: lambda=1 cancels the leading term, so degree <=112.
    projective_bad_bound_sharp = (
        (SUPPORT_SIZE - 1) + SUPPORT_SIZE * (q0 - 2)
    ) * pair_count

    assert projective_bad_bound_sharp <= projective_bad_bound
    assert projective_bad_bound < outside_base

    pair_packet = PACKET_SUPPORTS * OCCUPANCY
    direct_product_bad_bound = SUPPORT_SIZE * pair_packet * (pair_packet - 1) // 2
    assert direct_product_bad_bound < outside_base
    native_target = q_line // (1 << TARGET_BITS)
    assert pair_packet // 8 > native_target

    result = {
        "certificate": "cycle87.role03.generic-projective-separator.v1",
        "decision": "GENERIC_PROJECTIVE_SEPARATOR_EXISTS",
        "scope": "existence_only_not_fixed_U",
        "assumptions": {
            "packet_supports_are_distinct": True,
            "support_size": SUPPORT_SIZE,
            "all_support_points_lie_in_F0": True,
        },
        "field": {
            "characteristic": P_CHAR,
            "F0_degree": DEG_F0,
            "F0_size": q0,
            "F0_modulus_low_first": F_MOD,
            "beta_power_basis": list(beta),
            "eta_power_basis": list(eta),
            "eta_exact_order": 256,
            "ord_256_of_17": 16,
            "beta_cubic_character": list(beta_cubic_character),
            "extension_polynomial": "U^3-beta",
            "extension_degree_over_F0": 3,
            "L_size": q_line,
        },
        "root_count": {
            "packet_supports": PACKET_SUPPORTS,
            "unordered_support_pairs": pair_count,
            "simple_bad_y_upper_bound": projective_bad_bound,
            "sharp_bad_y_upper_bound": projective_bad_bound_sharp,
            "available_y_outside_F0": outside_base,
            "simple_bound_margin": outside_base - projective_bad_bound,
            "conclusion": "there exists y in L\\F0 with mu_proj(y)=1",
            "direct_N_times_P_product_bad_y_upper_bound": direct_product_bad_bound,
            "direct_product_conclusion": "there also exists y making (a,T)->a*P_T(y) injective on Omega x P0",
        },
        "official_threshold_check_if_mu_proj_le_8": {
            "occupancy": OCCUPANCY,
            "P_times_N": pair_packet,
            "floor_P_times_N_over_8": pair_packet // 8,
            "q_line": q_line,
            "floor_q_line_over_2^128": native_target,
            "margin": pair_packet // 8 - native_target,
        },
        "not_certified": [
            "mu_proj(U)<=8 for the fixed U satisfying U^3=beta",
            "coordinates of a good separator y",
            "ordered 464-point domain digest",
            "public projective census artifact",
        ],
    }

    out_path = Path("/mnt/data/cycle87_role03_generic_separator_result.json")
    out_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    print(f"WROTE {out_path}")


if __name__ == "__main__":
    main()
