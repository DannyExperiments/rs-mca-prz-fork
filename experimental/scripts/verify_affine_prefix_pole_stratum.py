#!/usr/bin/env python3
"""Director replay for the R32 Role-11 pole-separated source stratum."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import combinations
import json
from math import comb, log
from pathlib import Path


Q = (1, 4, 4, 4, 1)
ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "experimental/data/certificates/affine-prefix-pole-stratum"
BASE = "999b8f3a1da959b8002ecf1819d37725af56d383"
MUTATIONS = (
    "wrong_characteristic",
    "all_signatures_unique",
    "wrong_source_polynomial",
    "wrong_ambiguous_blocks",
    "drop_fibre_factor",
    "field_too_small",
    "unsafe_degree",
    "omit_pairwise_separator",
    "ordinary_limit",
    "drop_scale_hypothesis",
    "semantic_promotion",
)


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
    for relative, expected in payload["files"].items():
        require(file_sha256(ROOT / relative) == expected, f"source pin mismatch: {relative}")
    return len(payload["files"])


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def power(poly: tuple[int, ...], exponent: int) -> list[int]:
    out = [1]
    base = list(poly)
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def local_census(modulus: int) -> Counter[tuple[int, int, int]]:
    points = ((0, 0), (1, 0), (0, 1), (1, 1))
    census: Counter[tuple[int, int, int]] = Counter()
    for mask in range(16):
        chosen = [points[i] for i in range(4) if mask & (1 << i)]
        census[(
            len(chosen) % modulus,
            sum(x for x, _ in chosen) % modulus,
            sum(y for _, y in chosen) % modulus,
        )] += 1
    return census


def source_polynomial(census: Counter[tuple[int, int, int]]) -> tuple[int, ...]:
    counts = [0] * 5
    for (size, _, _), multiplicity in census.items():
        if multiplicity == 1:
            counts[size] += 1
    return tuple(counts)


@dataclass(frozen=True)
class Config:
    modulus: int = 5
    expected_ambiguity: tuple[tuple[int, int], ...] = ((1, 14), (2, 1))
    source_q: tuple[int, ...] = Q
    t: int = 1
    ambiguous_blocks: int = 9
    fibre_factor: int = 1 << 9
    field_degree: int = 30
    locator_difference_degree: int = 19
    separator_pairs: bool = True
    limit_mode: str = "liminf"
    retain_scale_hypothesis: bool = True
    scope: str = "structural"


def verify(config: Config) -> dict[str, int | float]:
    t = config.t
    blocks = 10 * t
    ambiguous = config.ambiguous_blocks * t
    remaining = blocks - ambiguous
    require(config.modulus == 5, "source characteristic must be five")
    census = local_census(config.modulus)
    require(len(census) == 15, "wrong local signature count")
    ambiguity = tuple(sorted(Counter(census.values()).items()))
    require(ambiguity == config.expected_ambiguity, "wrong ambiguity pattern")
    derived_q = source_polynomial(census)
    require(derived_q == config.source_q == Q, "wrong literal source polynomial")
    require(ambiguous == 9 * t and remaining == t, "wrong whole-stratum block split")
    coefficient = power(config.source_q, remaining)[2 * t]
    l_value = comb(blocks, ambiguous) * coefficient
    expected_fibre = 1 << (9 * t)
    require(config.fibre_factor == expected_fibre, "wrong uniform source fibre")
    m_value = config.fibre_factor * l_value

    n = 40 * t
    m = 20 * t
    k = m - 1
    require(config.locator_difference_degree == k, "unsafe separator degree")
    require(m == k + 1 and m == n // 2, "wrong exact-agreement endpoint")
    require(config.field_degree == 30 * t, "wrong coefficient field degree")
    q_field = 5 ** config.field_degree
    pair_count = comb(m_value, 2) if config.separator_pairs else 0
    forbidden = n + k * pair_count
    require(config.separator_pairs, "pairwise locator separation omitted")
    require(q_field > forbidden, "separator field guard failed")

    require(config.limit_mode == "liminf", "ordinary limit is not source-certified")
    require(config.retain_scale_hypothesis, "inherited scale/K_t hypotheses dropped")
    require(config.scope == "structural", "semantic primitive-cell promotion")

    for small_t in range(1, 9):
        b = 10 * small_t
        l_small = comb(b, small_t) * power(Q, small_t)[2 * small_t]
        m_small = (1 << (9 * small_t)) * l_small
        q_small = 5 ** (30 * small_t)
        forbidden_small = 40 * small_t + (20 * small_t - 1) * comb(m_small, 2)
        require(q_small > forbidden_small, f"exact separator failed at t={small_t}")

    a_bound = (1 << 19) * 14
    require(5 ** 30 > 20 * a_bound**2, "all-t separator seed failed")
    for small_t in range(1, 21):
        q_small = 5 ** (30 * small_t)
        crude_m = a_bound ** small_t
        crude_forbidden = 40 * small_t + (20 * small_t - 1) * comb(crude_m, 2)
        require(q_small > crude_forbidden, f"crude all-t guard failed at t={small_t}")

    entropy = -(0.9 * log(0.9) + 0.1 * log(0.1))
    lam = entropy + 0.1 * log(14)
    require(abs(lam - 0.5889887063529741) < 1e-15, "wrong lambda")
    return {
        "L1": l_value,
        "M1": m_value,
        "forbidden1": forbidden,
        "field1": q_field,
        "margin1": q_field - forbidden,
        "lambda_over_4": lam / 4,
    }


def mutate(config: Config, name: str) -> Config:
    if name == "wrong_characteristic":
        return replace(config, modulus=7)
    if name == "all_signatures_unique":
        return replace(config, expected_ambiguity=((1, 16),))
    if name == "wrong_source_polynomial":
        return replace(config, source_q=(1, 4, 5, 4, 1))
    if name == "wrong_ambiguous_blocks":
        return replace(config, ambiguous_blocks=8)
    if name == "drop_fibre_factor":
        return replace(config, fibre_factor=1)
    if name == "field_too_small":
        return replace(config, field_degree=9)
    if name == "unsafe_degree":
        return replace(config, locator_difference_degree=18)
    if name == "omit_pairwise_separator":
        return replace(config, separator_pairs=False)
    if name == "ordinary_limit":
        return replace(config, limit_mode="limit")
    if name == "drop_scale_hypothesis":
        return replace(config, retain_scale_hypothesis=False)
    if name == "semantic_promotion":
        return replace(config, scope="semantic")
    raise ValueError(name)


def main() -> None:
    source_pin_count = check_source_pins()
    baseline = Config()
    values = verify(baseline)
    caught = 0
    for name in MUTATIONS:
        try:
            verify(mutate(baseline, name))
        except RuntimeError:
            caught += 1
    require(caught == len(MUTATIONS), "semantic mutation survived")
    print("R32_ROLE11_POLE_STRATUM: PASS")
    print(f"base={BASE} source_pins=PASS,count={source_pin_count}")
    print("local_signatures=15 ambiguity_pattern=14x1+1x2 Q=1,4,4,4,1")
    print(f"t1_L={values['L1']} t1_fibre=512 t1_M={values['M1']}")
    print(f"t1_forbidden={values['forbidden1']} field=5^30 margin={values['margin1']}")
    print("separator_checks=exact_t1..t8,crude_t1..t20,all_t_seed")
    print(f"lambda_over_4={values['lambda_over_4']:.18f}")
    print("scope=structural_line_local lower_bound_only liminf_only")
    print(f"semantic_mutations={caught}/{len(MUTATIONS)}")
    print("finite_ledger_delta=0 asymptotic_ledger_delta=0 official_score=0/2")


if __name__ == "__main__":
    main()
