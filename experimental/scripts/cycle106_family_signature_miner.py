#!/usr/bin/env python3
"""Aggregate finite signatures for Cycle106 stress families.

This is a reproducibility companion for cycle106_kfree_incidence_stress.py.
It recomputes the same finite toy grid and records compact signature histograms
for selected stress-survivor families. The output is experimental evidence only;
it is not a Cycle106 theorem or a source-valid counterpacket.
"""

import argparse
import json
from collections import Counter
from itertools import combinations, product

from cycle105_kfree_collapse_check import g_tuple, prefix_tuple, roots_of_unity
from cycle106_kfree_incidence_stress import (
    active_profile,
    candidate_tags,
    coefficient_profile,
    cosets,
    family_tags,
    rough_aperiodic_candidate,
)


DEFAULT_CASES = [
    (23, 11, 2),
    (31, 10, 2),
    (37, 12, 2),
    (41, 10, 2),
    (43, 14, 2),
]

DEFAULT_FAMILIES = ["dominant_cluster", "distributed_dense_tail"]


def iter_normalized_uhats(p, sigma):
    for tail in product(range(p), repeat=sigma + 1):
        yield (1,) + tail


def parse_case(text):
    parts = text.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("case must have form p,n,sigma")
    try:
        p, n, sigma = (int(part) for part in parts)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("case entries must be integers") from exc
    if p <= 2 or n <= 1 or sigma <= 0:
        raise argparse.ArgumentTypeError("case requires p>2, n>1, sigma>0")
    return p, n, sigma


def inv_mod(a, p):
    return pow(a, p - 2, p)


def case_key(p, n, sigma):
    return f"p={p},n={n},sigma={sigma}"


def counter_rows(counter, top=None):
    rows = [
        {"signature": key, "count": count}
        for key, count in counter.most_common(top)
    ]
    return rows


def inc(counter, key):
    encoded = key if isinstance(key, str) else json.dumps(key, sort_keys=True)
    counter[encoded] += 1


def coset_membership(coset_list):
    return {x: index for index, coset in enumerate(coset_list) for x in coset}


def tail_ratio(tail, p):
    first = next((u % p for u in tail if u % p), None)
    if first is None:
        return None
    first_inv = inv_mod(first, p)
    return [(u * first_inv) % p for u in tail]


def tail_relations(tail, p):
    if len(tail) != 3 or any((u % p) == 0 for u in tail):
        return None
    u1, u2, u3 = [u % p for u in tail]
    discriminant = (u2 * u2 - 4 * u1 * u3) % p
    disc_square = discriminant == 0 or pow(discriminant, (p - 1) // 2, p) == 1
    geometric_tail = (u2 * u2 - u1 * u3) % p == 0
    return {
        "disc_square": disc_square,
        "geometric_tail": geometric_tail,
        "u1u3_over_u2sq": (u1 * u3 * inv_mod((u2 * u2) % p, p)) % p,
    }


def empty_family_state():
    return {
        "case_totals": Counter(),
        "active_count_by_case": Counter(),
        "occupancy_by_case": Counter(),
        "s_by_case": Counter(),
        "tail_weight_by_case": Counter(),
        "tag_intersections": Counter(),
        "family_intersections": Counter(),
        "coarse_signatures": Counter(),
        "active_set_reuse": Counter(),
        "tail_ratio": Counter(),
        "tail_relations": Counter(),
        "top_examples": {},
    }


def note_example(state, coarse_key, row):
    encoded = json.dumps(coarse_key, sort_keys=True)
    if encoded not in state["top_examples"]:
        state["top_examples"][encoded] = row


def summarize_state(state, top):
    total = sum(state["case_totals"].values())
    return {
        "total": total,
        "case_totals": counter_rows(state["case_totals"]),
        "active_count_by_case": counter_rows(state["active_count_by_case"]),
        "occupancy_by_case": counter_rows(state["occupancy_by_case"]),
        "s_by_case": counter_rows(state["s_by_case"]),
        "tail_weight_by_case": counter_rows(state["tail_weight_by_case"]),
        "tag_intersections": counter_rows(state["tag_intersections"]),
        "family_intersections": counter_rows(state["family_intersections"]),
        "top_coarse_signatures": counter_rows(state["coarse_signatures"], top),
        "top_active_set_reuse": counter_rows(state["active_set_reuse"], top),
        "top_tail_ratio": counter_rows(state["tail_ratio"], top),
        "top_tail_relations": counter_rows(state["tail_relations"], top),
        "top_examples": {
            row["signature"]: state["top_examples"][row["signature"]]
            for row in counter_rows(state["coarse_signatures"], top)
            if row["signature"] in state["top_examples"]
        },
    }


def read_summary_family_counts(path):
    if not path:
        return {}
    counts = {}
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row.get("row_type") != "summary":
                continue
            key = case_key(row["p"], row["n"], row["sigma"])
            counts[key] = {
                family: int(count)
                for family, count in row.get("candidate_family_histogram", {}).items()
            }
    return counts


def mine_case(
    p,
    n,
    sigma,
    families,
    states,
    density_num,
    density_den,
    candidate_min_active,
    stress_survivor_min_active,
):
    assert (p - 1) % n == 0
    H = roots_of_unity(n, p)
    coset_list = cosets(H, p)
    coset_index = coset_membership(coset_list)
    layers = {
        s: {prefix_tuple(subset, sigma, p) for subset in combinations(H, s)}
        for s in range(sigma + 1, n)
    }
    layer_sizes = {s: len(layer) for s, layer in layers.items()}
    ambient_size = p ** (sigma + 1)
    key = case_key(p, n, sigma)

    for uhat in iter_normalized_uhats(p, sigma):
        theta_values = [
            (theta, g_tuple(theta, uhat, sigma, p))
            for theta in range(p)
        ]
        for s, layer in layers.items():
            hits = [theta for theta, value in theta_values if value in layer]
            active_count = len(hits)
            if not rough_aperiodic_candidate(uhat, hits, coset_list, p):
                continue
            if layer_sizes[s] * density_den > density_num * ambient_size:
                continue
            if active_count < candidate_min_active:
                continue

            tags = candidate_tags(
                uhat,
                hits,
                H,
                coset_list,
                p,
                stress_survivor_min_active,
            )
            row_families = family_tags(tags)
            targets = [family for family in families if family in row_families]
            if not targets:
                continue

            profile = active_profile(hits, H, coset_list, p)
            coeff_profile = coefficient_profile(uhat, p)
            occupancies = profile["H_coset_occupancies"]
            coset_ids = [
                coset_index[theta]
                for theta in hits
                if theta != 0
            ]
            rel = tail_relations(coeff_profile["tail"], p)
            ratio = tail_ratio(coeff_profile["tail"], p)

            for family in targets:
                state = states[family]
                state["case_totals"][key] += 1
                inc(state["active_count_by_case"], [key, active_count])
                inc(state["occupancy_by_case"], [key, occupancies])
                inc(state["s_by_case"], [key, s])
                inc(state["tail_weight_by_case"], [key, coeff_profile["tail_weight"]])
                for tag in tags:
                    inc(state["tag_intersections"], tag)
                for row_family in row_families:
                    inc(state["family_intersections"], row_family)
                coarse_key = {
                    "case": key,
                    "s": s,
                    "active_count": active_count,
                    "occupancies": occupancies,
                    "negation_pairs": profile["negation_pair_count"],
                    "inverse_pairs": profile["inverse_pair_count"],
                }
                inc(state["coarse_signatures"], coarse_key)
                inc(state["active_set_reuse"], [key, hits])
                inc(state["tail_ratio"], [key, ratio])
                if rel is not None:
                    inc(state["tail_relations"], [key, rel])
                note_example(
                    state,
                    coarse_key,
                    {
                        "case": key,
                        "s": s,
                        "uhat": list(uhat),
                        "active_thetas": hits,
                        "active_profile": profile,
                        "coefficient_profile": coeff_profile,
                        "coset_ids": sorted(coset_ids),
                        "tags": tags,
                        "family_tags": row_families,
                        "tail_relations": rel,
                    },
                )


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        type=parse_case,
        action="append",
        dest="cases",
        help="Run one case p,n,sigma. May be repeated.",
    )
    parser.add_argument(
        "--family",
        action="append",
        dest="families",
        help="Family to aggregate. May be repeated.",
    )
    parser.add_argument("--json", help="Write compact JSON summary to this path.")
    parser.add_argument(
        "--summary-jsonl",
        help="Optional stress-checker JSONL whose summary family counts are compared.",
    )
    parser.add_argument("--top", type=int, default=20, help="Top signatures to keep.")
    parser.add_argument("--max-layer-density-num", type=int, default=1)
    parser.add_argument("--max-layer-density-den", type=int, default=20)
    parser.add_argument("--candidate-min-active", type=int, default=3)
    parser.add_argument("--stress-survivor-min-active", type=int, default=3)
    return parser.parse_args()


def main():
    args = parse_args()
    if args.top <= 0:
        raise SystemExit("top must be positive")
    cases = args.cases if args.cases else DEFAULT_CASES
    families = args.families if args.families else DEFAULT_FAMILIES
    states = {family: empty_family_state() for family in families}

    for case in cases:
        mine_case(
            *case,
            families,
            states,
            args.max_layer_density_num,
            args.max_layer_density_den,
            args.candidate_min_active,
            args.stress_survivor_min_active,
        )

    summary_counts = read_summary_family_counts(args.summary_jsonl)
    output = {
        "status": "EXPERIMENTAL_SIGNATURE_SUMMARY",
        "claim_boundary": (
            "Finite toy stress signatures only; not a theorem, not a "
            "source-valid counterpacket, and not prize-level evidence."
        ),
        "settings": {
            "cases": [list(case) for case in cases],
            "families": families,
            "max_layer_density_num": args.max_layer_density_num,
            "max_layer_density_den": args.max_layer_density_den,
            "candidate_min_active": args.candidate_min_active,
            "stress_survivor_min_active": args.stress_survivor_min_active,
            "top": args.top,
        },
        "families": {
            family: summarize_state(state, args.top)
            for family, state in states.items()
        },
        "summary_family_count_comparison": {},
    }

    for family, state in states.items():
        comparisons = []
        for case, count in sorted(state["case_totals"].items()):
            expected = summary_counts.get(case, {}).get(family)
            comparisons.append(
                {
                    "case": case,
                    "computed": count,
                    "summary_jsonl": expected,
                    "matches": expected is None or expected == count,
                }
            )
        output["summary_family_count_comparison"][family] = comparisons

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(output, fh, indent=2, sort_keys=True)
            fh.write("\n")
        print(f"JSON_WRITTEN {args.json}")
    else:
        print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
