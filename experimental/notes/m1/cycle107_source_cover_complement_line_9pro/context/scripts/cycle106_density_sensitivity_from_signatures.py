#!/usr/bin/env python3
"""Derive Cycle106 family density sensitivity from signature summaries.

This post-processor does not enumerate new candidates. It takes a signature
summary produced by cycle106_family_signature_miner.py and filters each
family's `s_by_case` counts by stricter toy layer-density gates. The result is
only finite stress bookkeeping, not theorem evidence.
"""

import argparse
import json


DEFAULT_DENSITY_DENS = [20, 50, 100, 200, 500]


def parse_density_den(text):
    try:
        value = int(text)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("density denominator must be an integer") from exc
    if value <= 0:
        raise argparse.ArgumentTypeError("density denominator must be positive")
    return value


def parse_case_signature(text):
    out = {}
    for part in text.split(","):
        key, value = part.split("=", 1)
        out[key] = int(value)
    return out["p"], out["n"], out["sigma"]


def load_stress_summaries(path):
    summaries = {}
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            row = json.loads(line)
            if row.get("row_type") != "summary":
                continue
            key = f"p={row['p']},n={row['n']},sigma={row['sigma']}"
            summaries[key] = {
                "ambient_size": row["ambient_size"],
                "layer_sizes": {int(s): int(size) for s, size in row["layer_sizes"].items()},
                "candidate_count": row["candidate_count"],
                "stress_survivor_count": row["stress_survivor_count"],
                "candidate_family_histogram": row.get("candidate_family_histogram", {}),
            }
    return summaries


def load_family_s_by_case(signature_summary):
    family_s_counts = {}
    for family, family_data in signature_summary["families"].items():
        counts = {}
        for row in family_data["s_by_case"]:
            case_key, s_value = json.loads(row["signature"])
            counts[(case_key, int(s_value))] = int(row["count"])
        family_s_counts[family] = counts
    return family_s_counts


def passed_layers(summary, density_num, density_den):
    return [
        s
        for s, size in sorted(summary["layer_sizes"].items())
        if size * density_den <= density_num * summary["ambient_size"]
    ]


def summarize(signature_summary, stress_summaries, density_num, density_dens):
    family_s_counts = load_family_s_by_case(signature_summary)
    result = {
        "status": "EXPERIMENTAL_DENSITY_SENSITIVITY_SUMMARY",
        "claim_boundary": (
            "Derived finite toy stress bookkeeping only; not a theorem, not a "
            "source-valid counterpacket, and not prize-level evidence."
        ),
        "source_signature_status": signature_summary.get("status"),
        "density_num": density_num,
        "density_dens": density_dens,
        "cases": {},
        "families": {},
    }

    for case_key, summary in sorted(stress_summaries.items()):
        p, n, sigma = parse_case_signature(case_key)
        result["cases"][case_key] = {
            "p": p,
            "n": n,
            "sigma": sigma,
            "quotient_index": (p - 1) // n,
            "ambient_size": summary["ambient_size"],
            "stress_survivor_count_source": summary["stress_survivor_count"],
            "candidate_count_source": summary["candidate_count"],
            "passed_s_by_density_den": {
                str(den): passed_layers(summary, density_num, den)
                for den in density_dens
            },
        }

    for family, counts in family_s_counts.items():
        family_total = signature_summary["families"][family]["total"]
        family_out = {
            "source_total": family_total,
            "by_density_den": [],
        }
        for den in density_dens:
            total = 0
            by_case = {}
            for case_key, summary in sorted(stress_summaries.items()):
                allowed = set(passed_layers(summary, density_num, den))
                case_total = sum(
                    count
                    for (row_case, s_value), count in counts.items()
                    if row_case == case_key and s_value in allowed
                )
                if case_total:
                    by_case[case_key] = case_total
                total += case_total
            family_out["by_density_den"].append(
                {
                    "density_gate": f"{density_num}/{den}",
                    "total": total,
                    "fraction_of_source_total": (
                        total / family_total if family_total else None
                    ),
                    "by_case": by_case,
                }
            )
        result["families"][family] = family_out

    return result


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--signature-json", required=True)
    parser.add_argument("--stress-jsonl", required=True)
    parser.add_argument("--json", required=True, help="Write summary JSON here.")
    parser.add_argument("--density-num", type=int, default=1)
    parser.add_argument(
        "--density-den",
        type=parse_density_den,
        action="append",
        dest="density_dens",
        help="Density denominator D for layer_size/ambient <= density_num/D.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.density_num <= 0:
        raise SystemExit("density numerator must be positive")
    density_dens = args.density_dens if args.density_dens else DEFAULT_DENSITY_DENS
    with open(args.signature_json, "r", encoding="utf-8") as fh:
        signature_summary = json.load(fh)
    stress_summaries = load_stress_summaries(args.stress_jsonl)
    result = summarize(signature_summary, stress_summaries, args.density_num, density_dens)
    with open(args.json, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"JSON_WRITTEN {args.json}")


if __name__ == "__main__":
    main()
