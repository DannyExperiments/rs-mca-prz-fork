#!/usr/bin/env python3
"""Fail-closed Cycle119 q_chal sampler-map checker.

Stdout is exactly one required semantic terminal. Diagnostics, when requested,
go to stderr. Any malformed, unauthenticated, unsupported, or inconsistent input
fails closed to UNDEFINED_MAP_NO_OFFICIAL_CLAIM.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

TERMINALS = {
    "DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED",
    "BALANCED_CHALLENGE_PROJECTION_NO_LOSS",
    "IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED",
    "OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD",
    "UNDEFINED_MAP_NO_OFFICIAL_CLAIM",
}
UNDEFINED = "UNDEFINED_MAP_NO_OFFICIAL_CLAIM"

P = 17
K_DEGREE = 32
Q = P ** K_DEGREE
N = 52_747_567_092
THRESHOLD_DEN = 2 ** 128
AGREEMENT = 262
RADIUS = "125/256"
SOURCE_DEFINITION_HASH = "89ebe887c02064a52b840c5e96992ff4f328575280a8f6dbed86e2b7dd7e7327"

INPUT_HASHES = {
    "RS_disproof_v3.tex": "681905d6de89697dafb8dccfc64d23cd6895050427d19f01ce504e13e0e799bd",
    "slackMCA_v3.tex": "99e2b292e88526a9ba8cf289bf8255c91d4bd49dde799cf1be10d98e18d63bbc",
    "cycle117_EXPECTED_RECEIPT.json": "89592ac16beb2861f3428403118f9318dd781ad222c1ea7afb55d9ba6dc5d436",
    "cycle117_observed_checker_receipt.json": "89592ac16beb2861f3428403118f9318dd781ad222c1ea7afb55d9ba6dc5d436",
    "cycle118_role07_response.md": "f26ef4934a67483bc906d030cf816247c770346c610d2c30d5ba5bb909b2799a",
}

TOP_LEVEL_KEYS = {
    "authority_root",
    "source_definition_hash",
    "challenge_space",
    "challenge_distribution",
    "q_chal",
    "line_field",
    "challenge_to_line_parameter_map",
    "bad_event_pullback_or_filter",
    "duplicate_policy",
    "quotient_or_charge_policy",
    "final_retained_numerator",
}

class Reject(Exception):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_payload(receipt: dict[str, Any]) -> bytes:
    payload = dict(receipt)
    payload.pop("authority_root", None)
    return json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def compute_authority_root(receipt: dict[str, Any]) -> str:
    return sha256(b"CYCLE119_QCHAL_AUTHORITY_PAYLOAD_V1\0" + canonical_payload(receipt))


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes())


def definition_hash(inputs: Path) -> str:
    components = [
        ("RS_disproof_v3.tex", 110, 115),
        ("slackMCA_v3.tex", 639, 653),
    ]
    h = hashlib.sha256()
    h.update(b"CYCLE119_QCHAL_SOURCE_DEFINITION_V1\0")
    for name, start, end in components:
        lines = (inputs / name).read_bytes().splitlines(keepends=True)
        if len(lines) < end:
            raise Reject(f"source too short: {name}")
        slice_bytes = b"".join(lines[start - 1 : end])
        h.update(f"context/base_cycle118_context/source/{name}".encode("utf-8"))
        h.update(b"\0")
        h.update(f"{start}:{end}".encode("ascii"))
        h.update(b"\0")
        h.update(slice_bytes)
        h.update(b"\0")
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Reject(message)


def require_int(value: Any, name: str, minimum: int = 0) -> int:
    require(isinstance(value, int) and not isinstance(value, bool), f"{name} not integer")
    require(value >= minimum, f"{name} below minimum")
    return value


def verify_inputs(root: Path) -> None:
    inputs = root / "inputs"
    for name, expected in INPUT_HASHES.items():
        p = inputs / name
        require(p.is_file(), f"missing pinned input {name}")
        require(file_hash(p) == expected, f"hash mismatch {name}")
    require(definition_hash(inputs) == SOURCE_DEFINITION_HASH, "source definition composite hash mismatch")

    expected = json.loads((inputs / "cycle117_EXPECTED_RECEIPT.json").read_text())
    observed = json.loads((inputs / "cycle117_observed_checker_receipt.json").read_text())
    require(expected == observed, "Cycle117 expected/observed receipts differ")
    require(observed.get("primary_terminal") == "SOURCE_CONTRACT_MISSING_NO_CLAIM", "packet authority status changed")
    fld = observed.get("field_ledger", {})
    require(fld.get("q_gen") == Q and fld.get("q_code") == Q and fld.get("q_line") == Q, "Cycle117 field ledger mismatch")
    require(fld.get("q_chal") is None, "Cycle117 source unexpectedly defines q_chal")
    ft = observed.get("finite_theorem", {})
    require(ft.get("LD_sw_lower_bound") == N, "Cycle116 numerator mismatch")
    require(ft.get("agreement") == AGREEMENT, "Cycle116 agreement mismatch")
    require(ft.get("delta") == RADIUS, "Cycle116 radius mismatch")


def defined(obj: Any) -> bool:
    return isinstance(obj, dict) and obj.get("status") == "DEFINED"


def verify_field(obj: dict[str, Any], name: str) -> tuple[int, int, int]:
    require(defined(obj), f"{name} undefined")
    require(obj.get("kind") == "FINITE_FIELD", f"{name} not a finite field")
    characteristic = require_int(obj.get("characteristic"), f"{name}.characteristic", 2)
    degree = require_int(obj.get("degree"), f"{name}.degree", 1)
    cardinality = require_int(obj.get("cardinality"), f"{name}.cardinality", 2)
    require(characteristic == P, f"{name} characteristic mismatch")
    require(cardinality == characteristic ** degree, f"{name} cardinality mismatch")
    require(degree % K_DEGREE == 0, f"{name} is not an extension of K")
    ext_degree = require_int(obj.get("extension_over_K_degree"), f"{name}.extension_over_K_degree", 1)
    require(ext_degree == degree // K_DEGREE, f"{name} extension degree mismatch")
    return degree, cardinality, ext_degree


def verify_pipeline(receipt: dict[str, Any], expected_prefilter: int) -> tuple[int, bool]:
    event = receipt["bad_event_pullback_or_filter"]
    require(defined(event), "bad event pullback/filter undefined")
    require(event.get("base_event") == "CYCLE116_CERTIFIED_BAD_SLOPES_AGREEMENT_262", "wrong base event")
    require(event.get("event_scope") == "CYCLE116_CERTIFIED_EVENT_PACKET", "wrong event scope")
    require(event.get("base_slope_numerator") == N, "wrong base slope numerator")
    require(event.get("pullback") == "EXACT_PREIMAGE", "pullback is not exact preimage")
    pre = require_int(event.get("prefilter_numerator"), "prefilter_numerator")
    require(pre == expected_prefilter, "prefilter numerator does not match map")
    action = event.get("filter_action")
    require(action in {"RETAIN", "FILTER"}, "unsupported filter action")
    post = require_int(event.get("postfilter_numerator"), "postfilter_numerator")
    require(post <= pre, "filter increases numerator")
    if action == "RETAIN":
        require(post == pre, "RETAIN changed numerator")
    else:
        require(post < pre, "FILTER did not strictly reduce numerator")

    dup = receipt["duplicate_policy"]
    require(defined(dup), "duplicate policy undefined")
    dup_action = dup.get("action")
    require(dup_action in {"COUNT_CHALLENGE_OCCURRENCES", "DEDUPLICATE_OR_IDENTIFY"}, "unsupported duplicate action")
    dup_in = require_int(dup.get("input_numerator"), "duplicate input")
    dup_out = require_int(dup.get("output_numerator"), "duplicate output")
    require(dup_in == post, "duplicate pipeline input mismatch")
    require(dup_out <= dup_in, "duplicate policy increases numerator")
    if dup_action == "COUNT_CHALLENGE_OCCURRENCES":
        require(dup_out == dup_in, "challenge-mass counting changed numerator")
    else:
        require(dup_out < dup_in, "deduplication did not strictly reduce numerator")

    qc = receipt["quotient_or_charge_policy"]
    require(defined(qc), "quotient/charge policy undefined")
    qc_action = qc.get("action")
    require(qc_action in {"NONE", "QUOTIENT_OR_CHARGE"}, "unsupported quotient/charge action")
    qc_in = require_int(qc.get("input_numerator"), "quotient/charge input")
    qc_out = require_int(qc.get("output_numerator"), "quotient/charge output")
    require(qc_in == dup_out, "quotient/charge pipeline input mismatch")
    require(qc_out <= qc_in, "quotient/charge increases numerator")
    if qc_action == "NONE":
        require(qc_out == qc_in, "NONE changed numerator")
    else:
        require(qc_out < qc_in, "quotient/charge did not strictly reduce numerator")

    final = receipt["final_retained_numerator"]
    require(defined(final), "final retained numerator undefined")
    require(final.get("numerator_scope") == "CYCLE116_CERTIFIED_EVENT_PACKET", "wrong final numerator scope")
    final_cert = require_int(final.get("certified_event_numerator"), "final certified numerator")
    require(final_cert == qc_out, "final numerator pipeline mismatch")
    all_bad_upper = final.get("all_bad_event_upper_bound")
    if all_bad_upper is not None:
        all_bad_upper = require_int(all_bad_upper, "all-bad upper bound")
        require(final_cert <= all_bad_upper, "certified event exceeds all-bad upper bound")

    no_loss = (
        action == "RETAIN"
        and dup_action == "COUNT_CHALLENGE_OCCURRENCES"
        and qc_action == "NONE"
        and final_cert == expected_prefilter
    )
    return final_cert, no_loss


def classify(receipt: dict[str, Any], trusted_root: str | None) -> str:
    require(set(receipt.keys()) == TOP_LEVEL_KEYS, "top-level schema mismatch")
    require(receipt.get("source_definition_hash") == SOURCE_DEFINITION_HASH, "receipt source definition hash mismatch")

    # No embedded root self-authenticates. A separate pin is mandatory.
    embedded_root = receipt.get("authority_root")
    require(isinstance(embedded_root, str) and len(embedded_root) == 64, "authority root absent")
    require(trusted_root is not None, "external authority trust pin absent")
    trusted_root = trusted_root.lower()
    require(all(c in "0123456789abcdef" for c in trusted_root) and len(trusted_root) == 64, "invalid external trust pin")
    computed_root = compute_authority_root(receipt)
    require(embedded_root == computed_root, "embedded authority root mismatch")
    require(trusted_root == computed_root, "external authority trust pin mismatch")

    cs_degree, cs_q, cs_r = verify_field(receipt["challenge_space"], "challenge_space")
    dist = receipt["challenge_distribution"]
    require(defined(dist), "challenge distribution undefined")
    require(dist.get("kind") == "UNIFORM", "only uniform challenge distributions are checker-supported")
    q_chal = require_int(receipt.get("q_chal"), "q_chal", 2)
    require(q_chal == cs_q, "q_chal is not challenge-space cardinality")
    lf_degree, lf_q, lf_r = verify_field(receipt["line_field"], "line_field")

    mp = receipt["challenge_to_line_parameter_map"]
    require(defined(mp), "challenge-to-line map undefined")
    kind = mp.get("kind")

    if kind == "IDENTITY":
        require(cs_q == lf_q and cs_degree == lf_degree, "identity map field mismatch")
        require(mp.get("domain_cardinality") == cs_q, "identity domain mismatch")
        require(mp.get("codomain_cardinality") == lf_q, "identity codomain mismatch")
        if cs_r == 1:
            branch = "DIRECT_K"
            expected_prefilter = N
        else:
            branch = "IDENTITY_E"
            expected_prefilter = N
    elif kind == "K_COORDINATE_PROJECTION":
        require(lf_r == 1 and lf_q == Q, "projection codomain is not K")
        require(cs_r >= 2, "projection challenge extension is not proper")
        require(mp.get("K_dimension") == cs_r, "projection dimension mismatch")
        require(mp.get("coordinate_index") == 0, "only canonical coordinate-zero projection supported")
        require(mp.get("coordinate_encoding") == "ORDERED_K_TUPLE", "projection coordinate encoding missing")
        basis_id = mp.get("basis_id")
        require(isinstance(basis_id, str) and len(basis_id) >= 1, "projection basis_id missing")
        coordinate_model = receipt["challenge_space"].get("K_coordinate_model")
        require(isinstance(coordinate_model, dict), "challenge coordinate model missing")
        require(coordinate_model.get("kind") == "ORDERED_K_BASIS_COORDINATES", "wrong coordinate model")
        require(coordinate_model.get("dimension") == cs_r, "coordinate model dimension mismatch")
        require(coordinate_model.get("basis_id") == basis_id, "map/challenge basis binding mismatch")
        fiber_size = require_int(mp.get("fiber_size"), "projection fiber_size", 1)
        require(fiber_size == Q ** (cs_r - 1), "projection fiber size mismatch")
        require(cs_q == Q * fiber_size, "projection balance arithmetic mismatch")
        branch = "BALANCED"
        expected_prefilter = N * fiber_size
    else:
        raise Reject("unsupported or undefined map kind")

    final_cert, no_loss = verify_pipeline(receipt, expected_prefilter)
    final_obj = receipt["final_retained_numerator"]

    if branch == "IDENTITY_E":
        # Exact scalar-extension confinement: the full bad set is contained in K.
        upper = final_obj.get("all_bad_event_upper_bound")
        require(upper == Q, "identity scalar-extension branch lacks exact K upper bound")
        require(final_obj.get("all_bad_event_upper_bound_scope") == "FULL_SCALAR_EXTENDED_CYCLE116_LINE", "wrong all-bad upper-bound scope")
        require(THRESHOLD_DEN * Q < q_chal, "proper scalar extension not below threshold")
        return "IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED"

    # Filter terminal is reserved for a genuine threshold crossing caused by
    # official processing: pre-filter above threshold, post-filter at/below it.
    prefilter_above = THRESHOLD_DEN * expected_prefilter > q_chal
    final_below = THRESHOLD_DEN * final_cert <= q_chal
    if not no_loss and prefilter_above and final_below:
        return "OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD"

    if branch == "DIRECT_K" and no_loss:
        require(lf_q == Q and q_chal == Q, "direct K branch ledger mismatch")
        require(THRESHOLD_DEN * final_cert > q_chal, "direct K density not above threshold")
        return "DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED"

    if branch == "BALANCED" and no_loss:
        require(THRESHOLD_DEN * final_cert > q_chal, "balanced density not above threshold")
        require(final_cert * Q == N * q_chal, "balanced no-loss identity failed")
        return "BALANCED_CHALLENGE_PROJECTION_NO_LOSS"

    # Required vocabulary has no positive terminal for lossy-but-still-above.
    raise Reject("defined but unsupported/lossy sampler state")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("receipt", type=Path)
    parser.add_argument("--trusted-authority-root", default=None)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    terminal = UNDEFINED
    diagnostic = ""
    try:
        root = Path(__file__).resolve().parent
        verify_inputs(root)
        receipt = json.loads(args.receipt.read_text(encoding="utf-8"))
        require(isinstance(receipt, dict), "receipt is not an object")
        terminal = classify(receipt, args.trusted_authority_root)
        require(terminal in TERMINALS, "internal terminal error")
    except Exception as exc:  # fail closed by design
        terminal = UNDEFINED
        diagnostic = f"{type(exc).__name__}: {exc}"
    if args.verbose and diagnostic:
        print(diagnostic, file=sys.stderr)
    print(terminal)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
