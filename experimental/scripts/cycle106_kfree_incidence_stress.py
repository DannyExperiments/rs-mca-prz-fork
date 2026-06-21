#!/usr/bin/env python3
"""Tiny finite stress checks for the Cycle106 k-free incidence wall.

This script does not prove the Cycle106 theorem. It enumerates small split
subgroup cases for the Cycle105 incidence object

    Gamma(Uhat) cap M_s,

where Gamma(Uhat) = {(g_1(theta), ..., g_{sigma+1}(theta)) : theta in F_p}
and M_s is the prefix elementary-symmetric image of s-subsets of H=mu_n.

The goal is to catch obvious small stress candidates and provide a deterministic
baseline for future Cycle106 work. The finite density gate and survivor threshold
are only toy reserve proxies for this stress layer, not theorem hypotheses.
"""

import argparse
import json
from itertools import combinations, product

from cycle105_kfree_collapse_check import g_tuple, prefix_tuple, roots_of_unity


DEFAULT_CASES = [
    (11, 5, 1),
    (17, 8, 1),
    (17, 8, 2),
    (29, 7, 2),
    (31, 5, 2),
]


def iter_normalized_uhats(p, sigma):
    """Enumerate normalized Uhat prefixes with u_0=1."""
    for tail in product(range(p), repeat=sigma + 1):
        yield (1,) + tail


def active_thetas(p, sigma, uhat, layer):
    return [theta for theta in range(p) if g_tuple(theta, uhat, sigma, p) in layer]


def cosets(H, p):
    Hset = set(H)
    seen = set()
    out = []
    for a in range(1, p):
        if a in seen:
            continue
        coset = frozenset((a * h) % p for h in Hset)
        out.append(coset)
        seen.update(coset)
    return out


def is_zero_tail(uhat, p):
    return all((u % p) == 0 for u in uhat[1:])


def is_geometric_prefix(uhat, p):
    r = uhat[1] % p if len(uhat) > 1 else 0
    return all((uhat[i] % p) == pow(r, i, p) for i in range(1, len(uhat)))


def hit_tags(hits, coset_list):
    hit_set = set(hits)
    nonzero = {x for x in hit_set if x != 0}
    zero_in_hits = 0 in hit_set
    coset_subset = any(nonzero <= coset for coset in coset_list)
    coset_equal = any(nonzero == coset for coset in coset_list)
    return {
        "zero_in_hits": zero_in_hits,
        "coset_subset": coset_subset,
        "coset_equal": coset_equal,
    }


def rough_aperiodic_candidate(uhat, hits, coset_list, p):
    """Toy filter only: excludes obvious geometric/coset-supported artifacts."""
    if is_zero_tail(uhat, p) or is_geometric_prefix(uhat, p):
        return False
    return not hit_tags(hits, coset_list)["coset_subset"]


def inc_hist(histogram, count):
    histogram[count] = histogram.get(count, 0) + 1


def format_hist(histogram):
    return ",".join(f"{k}:{histogram[k]}" for k in sorted(histogram)) or "empty"


def format_hits(uhat, hits, coset_list, p):
    tags = []
    if is_zero_tail(uhat, p):
        tags.append("zero_tail")
    if is_geometric_prefix(uhat, p):
        tags.append("geometric_prefix")
    htags = hit_tags(hits, coset_list)
    if htags["zero_in_hits"]:
        tags.append("zero_hit")
    if htags["coset_equal"]:
        tags.append("coset_equal")
    elif htags["coset_subset"]:
        tags.append("coset_subset")
    return ",".join(tags) or "unclassified"


def active_profile(hits, H, coset_list, p):
    hit_set = set(hits)
    nonzero_hits = [x for x in hits if x != 0]
    coset_occupancies = [
        sum(1 for x in hit_set if x != 0 and x in coset)
        for coset in coset_list
    ]
    coset_occupancies = [count for count in coset_occupancies if count]
    negation_pairs = {
        tuple(sorted((x, (-x) % p)))
        for x in nonzero_hits
        if (-x) % p in hit_set and x != (-x) % p
    }
    inverse_pairs = {
        tuple(sorted((x, pow(x, p - 2, p))))
        for x in nonzero_hits
        if pow(x, p - 2, p) in hit_set and x != pow(x, p - 2, p)
    }
    profile = {
        "active_count": len(hits),
        "zero_count": sum(1 for x in hits if x == 0),
        "nonzero_count": len(nonzero_hits),
        "H_coset_cover_count": len(coset_occupancies),
        "H_coset_occupancies": sorted(coset_occupancies, reverse=True),
        "max_H_coset_occupancy": max(coset_occupancies) if coset_occupancies else 0,
        "contained_in_single_H_coset": bool(nonzero_hits) and len(coset_occupancies) <= 1,
        "negation_pair_count": len(negation_pairs),
        "negation_symmetric": bool(hits) and hit_set == {(-x) % p for x in hit_set},
        "inverse_pair_count": len(inverse_pairs),
        "inverse_symmetric": bool(nonzero_hits)
        and hit_set == {pow(x, p - 2, p) for x in nonzero_hits},
    }
    if len(hits) != 2:
        return profile

    a, b = hits
    ratio = (b * pow(a, p - 2, p)) % p if a != 0 else None
    profile.update(
        {
            "pair": [a, b],
            "sum_mod_p": (a + b) % p,
            "product_mod_p": (a * b) % p,
            "ratio_b_over_a": ratio,
            "ratio_in_H": ratio in set(H) if ratio is not None else False,
            "additive_inverse_pair": (a + b) % p == 0,
            "multiplicative_inverse_pair": a != 0 and b != 0 and (a * b) % p == 1,
        }
    )
    profile["same_H_coset"] = profile["ratio_in_H"]
    return profile


def coefficient_profile(uhat, p):
    tail = [u % p for u in uhat[1:]]
    nonzero_positions = [i + 1 for i, u in enumerate(tail) if u != 0]
    zero_positions = [i + 1 for i, u in enumerate(tail) if u == 0]
    profile = {
        "tail": tail,
        "tail_weight": len(nonzero_positions),
        "zero_positions": zero_positions,
        "nonzero_positions": nonzero_positions,
    }
    if len(tail) == 3:
        u1, u2, u3 = tail
        profile.update(
            {
                "sigma2_u1_zero": u1 == 0,
                "sigma2_u2_zero": u2 == 0,
                "sigma2_u3_zero": u3 == 0,
                "sigma2_even_tail": u1 == 0 and u3 == 0 and u2 != 0,
                "sigma2_odd_tail": u2 == 0 and (u1 != 0 or u3 != 0),
                "sigma2_endpoint_sparse": u1 == 0 or u3 == 0,
                "sigma2_tail_palindrome": u1 == u3,
            }
        )
    return profile


def coefficient_tags(uhat, p):
    profile = coefficient_profile(uhat, p)
    tags = [f"tail_weight_{profile['tail_weight']}"]
    if profile["tail_weight"] <= 1:
        tags.append("coefficient_monomial_tail")
    if profile["tail_weight"] <= 2:
        tags.append("coefficient_sparse_tail")
    for position in profile["zero_positions"]:
        tags.append(f"u{position}_zero")
    if len(profile["tail"]) == 3:
        for key in (
            "sigma2_even_tail",
            "sigma2_odd_tail",
            "sigma2_endpoint_sparse",
            "sigma2_tail_palindrome",
        ):
            if profile[key]:
                tags.append(key)
    return tags


def active_geometry_tags(profile):
    tags = []
    cover = profile["H_coset_cover_count"]
    active_count = profile["active_count"]
    max_occupancy = profile["max_H_coset_occupancy"]
    if cover:
        tags.append(f"H_coset_cover_{cover}")
    if cover == 2:
        tags.append("two_H_coset_cover")
    elif cover == 3:
        tags.append("three_H_coset_cover")
    elif cover > 3:
        tags.append("many_H_coset_cover")

    if active_count and max_occupancy == active_count:
        tags.append("single_H_coset_cover")
    elif active_count and max_occupancy >= active_count - 1:
        tags.append("single_H_coset_plus_one_outlier")
        tags.append("dominant_H_coset_cluster")
    elif active_count >= 4 and max_occupancy >= active_count - 2 and 2 * max_occupancy > active_count:
        tags.append("single_H_coset_plus_two_outliers")
        tags.append("dominant_H_coset_cluster")
    elif cover == 2 and active_count and 2 * max_occupancy == active_count:
        tags.append("balanced_two_H_coset_split")
    elif cover >= 3:
        tags.append("distributed_H_coset_cover")

    if profile["negation_pair_count"]:
        tags.append("negation_pair_present")
    if profile["negation_symmetric"]:
        tags.append("negation_symmetric_active_set")
    if profile["inverse_pair_count"]:
        tags.append("inverse_pair_present")
    if profile["inverse_symmetric"]:
        tags.append("inverse_symmetric_active_set")
    return tags


def candidate_tags(uhat, hits, H, coset_list, p, stress_survivor_min_active):
    raw_tags = format_hits(uhat, hits, coset_list, p).split(",")
    tags = [] if raw_tags == ["unclassified"] else raw_tags
    profile = active_profile(hits, H, coset_list, p)
    tags.extend(coefficient_tags(uhat, p))
    tags.extend(active_geometry_tags(profile))

    if len(hits) == 2:
        tags.append("two_hit_only")
        if profile["zero_count"] == 0:
            tags.append("nonzero_pair")
            if profile["same_H_coset"]:
                tags.append("same_H_coset_pair")
            else:
                tags.append("off_H_coset_pair")
        if profile.get("additive_inverse_pair"):
            tags.append("additive_inverse_pair")
        if profile.get("multiplicative_inverse_pair"):
            tags.append("multiplicative_inverse_pair")
    elif len(hits) > 2:
        tags.append("multi_hit")
        if profile["zero_count"] == 0:
            tags.append("nonzero_active_set")
        if profile["contained_in_single_H_coset"]:
            tags.append("same_H_coset_set")
        else:
            tags.append("off_H_coset_set")

    if len(hits) < stress_survivor_min_active:
        tags.append("below_stress_survivor_min_active")
    else:
        tags.append("stress_survivor_min_active_pass")

    return sorted(dict.fromkeys(tags)) or ["unclassified"]


def family_tags(tags):
    tag_set = set(tags)
    families = ["all"]
    if "stress_survivor_min_active_pass" in tag_set:
        families.append("stress_survivor")
    if "dominant_H_coset_cluster" in tag_set:
        families.append("dominant_cluster")
    if "single_H_coset_plus_one_outlier" in tag_set:
        families.append("cluster_plus_one")
    if "single_H_coset_plus_two_outliers" in tag_set:
        families.append("cluster_plus_two")
    if "distributed_H_coset_cover" in tag_set:
        families.append("distributed_cover")
    if "balanced_two_H_coset_split" in tag_set:
        families.append("balanced_two_coset")
    if "coefficient_sparse_tail" in tag_set:
        families.append("coefficient_sparse")
    if "tail_weight_3" in tag_set:
        families.append("dense_tail")
    if "distributed_H_coset_cover" in tag_set and "tail_weight_3" in tag_set:
        families.append("distributed_dense_tail")
    if "zero_hit" in tag_set:
        families.append("zero_hit")
    return families


def should_emit_candidate(tags, emit_family):
    return emit_family == "all" or emit_family in family_tags(tags)


def stress_case(
    p,
    n,
    sigma,
    density_num,
    density_den,
    candidate_min_active,
    stress_survivor_min_active,
    max_candidate_rows_per_case,
    emit_family,
):
    assert (p - 1) % n == 0
    H = roots_of_unity(n, p)
    assert len(H) == n
    coset_list = cosets(H, p)

    layers = {
        s: {prefix_tuple(subset, sigma, p) for subset in combinations(H, s)}
        for s in range(sigma + 1, n)
    }
    layer_sizes = {s: len(layer) for s, layer in layers.items()}
    ambient_size = p ** (sigma + 1)
    max_active = 0
    examples = []
    max_nonconstant_active = 0
    nonconstant_examples = []
    max_nongeometric_active = 0
    nongeometric_examples = []
    max_rough_active = 0
    rough_examples = []
    vectors_checked = 0
    histogram = {}
    nonconstant_histogram = {}
    nongeometric_histogram = {}
    rough_histogram = {}
    candidate_active_histogram = {}
    candidate_tag_histogram = {}
    candidate_coset_cover_histogram = {}
    candidate_tail_weight_histogram = {}
    candidate_family_histogram = {}
    candidate_count = 0
    stress_survivor_count = 0
    candidate_rows = []

    for uhat in iter_normalized_uhats(p, sigma):
        vectors_checked += 1
        nonconstant = any(uhat[i] % p for i in range(1, len(uhat)))
        nongeometric = not is_geometric_prefix(uhat, p)
        case_max = 0
        case_hits = []
        case_nongeometric_max = 0
        case_nongeometric_hits = []
        case_rough_max = 0
        case_rough_hits = []
        theta_values = [
            (theta, g_tuple(theta, uhat, sigma, p))
            for theta in range(p)
        ]
        for s, layer in layers.items():
            hits = [theta for theta, value in theta_values if value in layer]
            count = len(hits)
            inc_hist(histogram, count)
            if nonconstant:
                inc_hist(nonconstant_histogram, count)
            if nongeometric:
                inc_hist(nongeometric_histogram, count)
                if count > case_nongeometric_max:
                    case_nongeometric_max = count
                    case_nongeometric_hits = [(s, hits)]
                elif count == case_nongeometric_max and count:
                    case_nongeometric_hits.append((s, hits))
            if rough_aperiodic_candidate(uhat, hits, coset_list, p):
                inc_hist(rough_histogram, count)
                layer_size = layer_sizes[s]
                density_gate_pass = layer_size * density_den <= density_num * ambient_size
                if density_gate_pass and count >= candidate_min_active:
                    tags = candidate_tags(
                        uhat,
                        hits,
                        H,
                        coset_list,
                        p,
                        stress_survivor_min_active,
                    )
                    profile = active_profile(hits, H, coset_list, p)
                    coeff_profile = coefficient_profile(uhat, p)
                    candidate_count += 1
                    stress_survivor_passed = count >= stress_survivor_min_active
                    if stress_survivor_passed:
                        stress_survivor_count += 1
                    inc_hist(candidate_active_histogram, count)
                    for tag in tags:
                        inc_hist(candidate_tag_histogram, tag)
                    inc_hist(
                        candidate_coset_cover_histogram,
                        profile["H_coset_cover_count"],
                    )
                    inc_hist(candidate_tail_weight_histogram, coeff_profile["tail_weight"])
                    families = family_tags(tags)
                    for family in families:
                        inc_hist(candidate_family_histogram, family)
                    emit_row = (
                        should_emit_candidate(tags, emit_family)
                        and (
                            max_candidate_rows_per_case is None
                            or len(candidate_rows) < max_candidate_rows_per_case
                        )
                    )
                    if emit_row:
                        candidate_rows.append(
                            {
                                "row_type": "candidate",
                                "status": "EXPERIMENTAL_STRESS_CANDIDATE",
                                "p": p,
                                "n": n,
                                "sigma": sigma,
                                "s": s,
                                "uhat": list(uhat),
                                "active_count": count,
                                "active_thetas": hits,
                                "tags": tags,
                                "family_tags": families,
                                "active_profile": profile,
                                "coefficient_profile": coeff_profile,
                                "layer_size": layer_size,
                                "ambient_size": ambient_size,
                                "density_gate": {
                                    "max_layer_density_num": density_num,
                                    "max_layer_density_den": density_den,
                                    "passed": True,
                                },
                                "stress_survivor_gate": {
                                    "min_active": stress_survivor_min_active,
                                    "passed": stress_survivor_passed,
                                },
                            }
                        )
                if count > case_rough_max:
                    case_rough_max = count
                    case_rough_hits = [(s, hits)]
                elif count == case_rough_max and count:
                    case_rough_hits.append((s, hits))
            if count > case_max:
                case_max = count
                case_hits = [(s, hits)]
            elif count == case_max and count:
                case_hits.append((s, hits))
        if case_max > max_active:
            max_active = case_max
            examples = [(uhat, case_hits[:3])]
        elif case_max == max_active and len(examples) < 3:
            examples.append((uhat, case_hits[:3]))
        if nonconstant:
            if case_max > max_nonconstant_active:
                max_nonconstant_active = case_max
                nonconstant_examples = [(uhat, case_hits[:3])]
            elif case_max == max_nonconstant_active and len(nonconstant_examples) < 3:
                nonconstant_examples.append((uhat, case_hits[:3]))
        if nongeometric:
            if case_nongeometric_max > max_nongeometric_active:
                max_nongeometric_active = case_nongeometric_max
                nongeometric_examples = [(uhat, case_nongeometric_hits[:3])]
            elif case_nongeometric_max == max_nongeometric_active and len(nongeometric_examples) < 3:
                nongeometric_examples.append((uhat, case_nongeometric_hits[:3]))
        if case_rough_max > max_rough_active:
            max_rough_active = case_rough_max
            rough_examples = [(uhat, case_rough_hits[:3])]
        elif case_rough_max > 0 and case_rough_max == max_rough_active and len(rough_examples) < 3:
            rough_examples.append((uhat, case_rough_hits[:3]))

    return {
        "p": p,
        "n": n,
        "sigma": sigma,
        "vectors_checked": vectors_checked,
        "s_values": sorted(layers),
        "ambient_size": ambient_size,
        "layer_sizes": layer_sizes,
        "max_layer_size": max(layer_sizes.values()) if layer_sizes else 0,
        "max_active": max_active,
        "max_nonconstant_active": max_nonconstant_active,
        "max_nongeometric_active": max_nongeometric_active,
        "max_rough_active": max_rough_active,
        "histogram": histogram,
        "nonconstant_histogram": nonconstant_histogram,
        "nongeometric_histogram": nongeometric_histogram,
        "rough_histogram": rough_histogram,
        "candidate_active_histogram": candidate_active_histogram,
        "candidate_tag_histogram": candidate_tag_histogram,
        "candidate_coset_cover_histogram": candidate_coset_cover_histogram,
        "candidate_tail_weight_histogram": candidate_tail_weight_histogram,
        "candidate_family_histogram": candidate_family_histogram,
        "emit_family": emit_family,
        "examples": examples,
        "nonconstant_examples": nonconstant_examples,
        "nongeometric_examples": nongeometric_examples,
        "rough_examples": rough_examples,
        "candidate_count": candidate_count,
        "stress_survivor_count": stress_survivor_count,
        "candidate_rows": candidate_rows,
        "coset_list": coset_list,
    }


def summary_row(
    result,
    density_num,
    density_den,
    candidate_min_active,
    stress_survivor_min_active,
):
    return {
        "row_type": "summary",
        "status": "EXPERIMENTAL_STRESS_SUMMARY",
        "p": result["p"],
        "n": result["n"],
        "sigma": result["sigma"],
        "vectors_checked": result["vectors_checked"],
        "s_values": result["s_values"],
        "ambient_size": result["ambient_size"],
        "layer_sizes": result["layer_sizes"],
        "max_layer_size": result["max_layer_size"],
        "max_active": result["max_active"],
        "max_nonconstant_active": result["max_nonconstant_active"],
        "max_nongeometric_active": result["max_nongeometric_active"],
        "max_rough_active": result["max_rough_active"],
        "histogram": result["histogram"],
        "nonconstant_histogram": result["nonconstant_histogram"],
        "nongeometric_histogram": result["nongeometric_histogram"],
        "rough_histogram": result["rough_histogram"],
        "candidate_active_histogram": result["candidate_active_histogram"],
        "candidate_tag_histogram": result["candidate_tag_histogram"],
        "candidate_coset_cover_histogram": result["candidate_coset_cover_histogram"],
        "candidate_tail_weight_histogram": result["candidate_tail_weight_histogram"],
        "candidate_family_histogram": result["candidate_family_histogram"],
        "candidate_count": result["candidate_count"],
        "candidate_rows_emitted": len(result["candidate_rows"]),
        "emit_family": result["emit_family"],
        "stress_survivor_count": result["stress_survivor_count"],
        "density_gate": {
            "max_layer_density_num": density_num,
            "max_layer_density_den": density_den,
        },
        "candidate_min_active": candidate_min_active,
        "stress_survivor_min_active": stress_survivor_min_active,
    }


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, sort_keys=True) + "\n")


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


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--case",
        type=parse_case,
        action="append",
        dest="cases",
        help=(
            "Run one case p,n,sigma. May be repeated. "
            "If omitted, the built-in tiny baseline cases are used."
        ),
    )
    parser.add_argument(
        "--jsonl",
        help="Write summary and gated candidate rows to this JSONL path.",
    )
    parser.add_argument(
        "--max-layer-density-num",
        type=int,
        default=1,
        help="Numerator for the toy per-layer density gate.",
    )
    parser.add_argument(
        "--max-layer-density-den",
        type=int,
        default=20,
        help="Denominator for the toy per-layer density gate.",
    )
    parser.add_argument(
        "--candidate-min-active",
        type=int,
        default=2,
        help="Minimum active theta count for gated candidate rows.",
    )
    parser.add_argument(
        "--stress-survivor-min-active",
        type=int,
        default=3,
        help=(
            "Minimum active theta count for a gated row to remain a stress "
            "survivor candidate. Rows below this threshold are still "
            "emitted for classification."
        ),
    )
    parser.add_argument(
        "--counterpacket-min-active",
        type=int,
        dest="deprecated_counterpacket_min_active",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--max-candidate-rows-per-case",
        type=int,
        help=(
            "Emit at most this many candidate rows per case while preserving "
            "total candidate counts in summary rows."
        ),
    )
    parser.add_argument(
        "--emit-family",
        choices=[
            "all",
            "stress_survivor",
            "dominant_cluster",
            "cluster_plus_one",
            "cluster_plus_two",
            "distributed_cover",
            "distributed_dense_tail",
            "balanced_two_coset",
            "coefficient_sparse",
            "dense_tail",
            "zero_hit",
        ],
        default="all",
        help="Restrict emitted candidate rows to this family; summaries still count all families.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.max_layer_density_num <= 0 or args.max_layer_density_den <= 0:
        raise SystemExit("density gate numerator and denominator must be positive")
    if args.candidate_min_active <= 0:
        raise SystemExit("candidate minimum active count must be positive")
    if args.deprecated_counterpacket_min_active is not None:
        args.stress_survivor_min_active = args.deprecated_counterpacket_min_active
    if args.stress_survivor_min_active <= 0:
        raise SystemExit("stress survivor minimum active count must be positive")
    if (
        args.max_candidate_rows_per_case is not None
        and args.max_candidate_rows_per_case < 0
    ):
        raise SystemExit("max candidate rows per case must be nonnegative")

    cases = args.cases if args.cases else DEFAULT_CASES

    jsonl_rows = []
    print("cycle106 k-free incidence stress check")
    print(
        "candidate_gate="
        f"layer_density<={args.max_layer_density_num}/{args.max_layer_density_den},"
        f" active_count>={args.candidate_min_active}; "
        f"stress_survivor_min_active={args.stress_survivor_min_active}; "
        f"emit_family={args.emit_family}"
    )
    for case in cases:
        result = stress_case(
            *case,
            args.max_layer_density_num,
            args.max_layer_density_den,
            args.candidate_min_active,
            args.stress_survivor_min_active,
            args.max_candidate_rows_per_case,
            args.emit_family,
        )
        jsonl_rows.append(
            summary_row(
                result,
                args.max_layer_density_num,
                args.max_layer_density_den,
                args.candidate_min_active,
                args.stress_survivor_min_active,
            )
        )
        jsonl_rows.extend(result["candidate_rows"])
        print(
            f"p={result['p']} n={result['n']} sigma={result['sigma']} "
            f"vectors={result['vectors_checked']} s={result['s_values']} "
            f"ambient={result['ambient_size']} layer_sizes={result['layer_sizes']} "
            f"max_layer={result['max_layer_size']}/{result['ambient_size']} "
            f"max_active={result['max_active']} "
            f"max_nonconstant_active={result['max_nonconstant_active']} "
            f"max_nongeometric_active={result['max_nongeometric_active']} "
            f"max_rough_active={result['max_rough_active']} "
            f"hist={format_hist(result['histogram'])} "
            f"nonconstant_hist={format_hist(result['nonconstant_histogram'])} "
            f"nongeometric_hist={format_hist(result['nongeometric_histogram'])} "
            f"rough_hist={format_hist(result['rough_histogram'])} "
            f"gated_candidates={result['candidate_count']} "
            f"emitted_candidates={len(result['candidate_rows'])} "
            f"stress_survivors={result['stress_survivor_count']}"
        )
        coset_list = result["coset_list"]
        p = result["p"]
        for uhat, hits in result["examples"]:
            tagged = [(s, hs, format_hits(uhat, hs, coset_list, p)) for s, hs in hits]
            print(f"  example_uhat={uhat} hits={tagged}")
        for uhat, hits in result["nonconstant_examples"]:
            tagged = [(s, hs, format_hits(uhat, hs, coset_list, p)) for s, hs in hits]
            print(f"  nonconstant_example_uhat={uhat} hits={tagged}")
        for uhat, hits in result["nongeometric_examples"]:
            tagged = [(s, hs, format_hits(uhat, hs, coset_list, p)) for s, hs in hits]
            print(f"  nongeometric_example_uhat={uhat} hits={tagged}")
        for uhat, hits in result["rough_examples"]:
            tagged = [(s, hs, format_hits(uhat, hs, coset_list, p)) for s, hs in hits]
            print(f"  rough_example_uhat={uhat} hits={tagged}")
    if args.jsonl:
        write_jsonl(args.jsonl, jsonl_rows)
        print(f"JSONL_WRITTEN {args.jsonl} rows={len(jsonl_rows)}")
    print("DONE")


if __name__ == "__main__":
    main()
