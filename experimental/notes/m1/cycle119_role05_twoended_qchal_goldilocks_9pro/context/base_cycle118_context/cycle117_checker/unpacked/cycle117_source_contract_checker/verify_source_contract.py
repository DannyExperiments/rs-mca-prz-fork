#!/usr/bin/env python3
"""Fail-closed Cycle117 source/admissibility checker.

No third-party packages. The checker writes nothing: its only output is JSON on
stdout. It verifies the attached manuscript source profile, replays the finite
Cycle116 verifier without running its mutating self-test, and fails closed on
missing authority-pinned official contract data.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any, Iterable

Q = 17 ** 32
N = 52_747_567_092
PACKET_SUPPORTS = 52_747_567_104
TWO128 = 1 << 128

TERMINALS = {
    "SOURCE_ACCEPTED_CYCLE116_ROW",
    "SOURCE_REJECTED_CYCLE116_ROW",
    "SOURCE_CONTRACT_MISSING_NO_CLAIM",
    "QCHAL_UNDEFINED_FINITE_MCA_ONLY",
    "EVENT_RETAINED",
    "EVENT_CHARGED_OR_EXCLUDED",
}

CRITICAL_HASHES = {
    "ROW_CONTRACT.json": "c096e7e54ad702e804ac1a102b12118aa470065a9062a10fa2ac3b51e8329f31",
    "EVENT_AUDIT.json": "8cfeb852497803d37734c7525f804bea85b35782cc84e04afd3cc75e09112472",
    "SYMBOLIC_LEMMAS.md": "c2b6d93898075997c6e150fb97d208dd8d0f1e330fbb226df1721f0c388efc88",
    "SOURCE_CLAUSES.json": "a0f96bed2d7c2fba62b983661daa7431519a7a1332e842d19bd68fae6d668ed7",
    "SOURCE_CLAUSE_LEDGER.md": "030e22829f8db2ef78e16ee57a40f2c5b862465651c753fb5f6c4dcafb9211a6",
    "OFFICIAL_CONTRACT_SCHEMA.json": "edb77371444d9228529bd8be530f00b4377cd6fc80e516a795ade931036b11e4",
    "PACKAGE_PROVENANCE.json": "af22281a26da642a44e7ed7eda1fd56f416d54367314c6843a84299885514701",
    "inputs/source/RS_disproof_v3.tex": "681905d6de89697dafb8dccfc64d23cd6895050427d19f01ce504e13e0e799bd",
    "inputs/source/slackMCA_v3.tex": "99e2b292e88526a9ba8cf289bf8255c91d4bd49dde799cf1be10d98e18d63bbc",
    "inputs/source/m2_line_decoding_mca_bridge.md": "e3fe7497eecd82a3f7db102b01586895cc90e366f190e9513a4c29ebff76f1cd",
    "inputs/cycle116/CYCLE116_CERTIFICATE.md": "3072bf3e63ca07038c6d12cdde80c5fe411764810e180eb5df91ca652a1ce3d9",
    "inputs/cycle116/verifier/MANIFEST.sha256": "f1d95792e563aed890070f234f8d9361c7df1afd319bb41ea562f184b81dc5c4",
}

REQUIRED_CLAUSE_IDS = {
    "RS_GENERAL_SMOOTH_ROW",
    "RS_CAPACITY_TRANSCRIPTION_SCOPE",
    "RS_SUPPORTWISE_MCA_DEFINITION",
    "RS_EXTENSION_FIELD_CONSTRUCTION",
    "RS_EXTENSION_FIELD_THEOREM",
    "RS_PROTOCOL_SCOPE_CUT",
    "SLACK_GENERAL_PRIME_POWER_NOTATION",
    "SLACK_SUBFIELD_CORRECTION",
    "SLACK_SUPPORTWISE_MCA_DEFINITION",
    "SLACK_TANGENT_FLOOR",
    "SLACK_SUBFIELD_CONFINEMENT",
    "SLACK_QUOTIENT_PERIODIC_ANALYTIC_ROLE",
    "SLACK_QUOTIENT_PERIODIC_FLOOR_SEPARATION",
    "M2_LDSW_EXACT_BRIDGE",
    "M2_CLOSE_POINT_LINE_DECODING_SUFFICIENT_ONLY",
    "M2_EXTERNAL_DEFINITION_STILL_TO_MATCH",
    "C116_SMOOTH_ROW_AND_CANONICAL_AR",
    "C116_PADDING_RETENTION_AND_THRESHOLD",
    "C116_NONCONTAINMENT_PROOF",
    "C116_Q_LEDGER_AND_SCOPE",
    "C116_OFFICIAL_CONTRACT_WALL",
}

EVENT_RULE_NAMES = {
    "endpoint",
    "periodic",
    "quotient",
    "tangent",
    "contained_line",
    "affine_color",
    "retained_event",
    "charge_registry",
    "challenge_filter",
}


class CheckFailure(Exception):
    def __init__(self, clause: str, detail: str):
        super().__init__(f"{clause}: {detail}")
        self.clause = clause
        self.detail = detail


def require(condition: bool, clause: str, detail: str) -> None:
    if not condition:
        raise CheckFailure(clause, detail)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CheckFailure("MALFORMED_JSON", f"{path}: {exc}") from exc


def exact_keys(obj: dict[str, Any], keys: Iterable[str], clause: str) -> None:
    expected = set(keys)
    actual = set(obj)
    require(actual == expected, clause, f"keys={sorted(actual)!r}, expected={sorted(expected)!r}")


def line_slice(path: Path, start: int, end: int) -> bytes:
    require(start >= 1 and end >= start, "CLAUSE_RANGE", f"invalid line range {start}-{end}")
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    require(end <= len(lines), "CLAUSE_RANGE", f"{path} has only {len(lines)} lines; requested {start}-{end}")
    return "".join(lines[start - 1 : end]).encode("utf-8")


def tree_digest(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        rel = path.relative_to(root).as_posix().encode("utf-8")
        h.update(len(rel).to_bytes(8, "big"))
        h.update(rel)
        raw = path.read_bytes()
        h.update(len(raw).to_bytes(8, "big"))
        h.update(raw)
    return h.hexdigest()


def verify_critical_hashes(root: Path) -> dict[str, str]:
    observed: dict[str, str] = {}
    for rel, expected in CRITICAL_HASHES.items():
        path = root / rel
        require(path.is_file(), "MISSING_CRITICAL_INPUT", rel)
        got = sha256_file(path)
        require(got == expected, "INPUT_HASH_MISMATCH", f"{rel}: {got} != {expected}")
        observed[rel] = got
    return observed


def verify_clause_ledger(root: Path) -> list[dict[str, Any]]:
    ledger = load_json(root / "SOURCE_CLAUSES.json")
    require(isinstance(ledger, dict), "CLAUSE_LEDGER_SCHEMA", "top level is not an object")
    exact_keys(ledger, {"schema", "clauses"}, "CLAUSE_LEDGER_SCHEMA")
    require(ledger["schema"] == "cycle117.source_clauses.v1", "CLAUSE_LEDGER_SCHEMA", "wrong schema")
    require(isinstance(ledger["clauses"], list), "CLAUSE_LEDGER_SCHEMA", "clauses is not a list")
    seen: set[str] = set()
    checked: list[dict[str, Any]] = []
    for item in ledger["clauses"]:
        require(isinstance(item, dict), "CLAUSE_LEDGER_SCHEMA", "clause is not an object")
        exact_keys(
            item,
            {"id", "file", "line_start", "line_end", "slice_sha256", "description", "text"},
            "CLAUSE_LEDGER_SCHEMA",
        )
        cid = item["id"]
        require(isinstance(cid, str) and cid not in seen, "CLAUSE_LEDGER_DUPLICATE", repr(cid))
        seen.add(cid)
        rel = item["file"]
        require(isinstance(rel, str), "CLAUSE_LEDGER_SCHEMA", f"{cid}: file is not string")
        p = Path(rel)
        require(not p.is_absolute() and ".." not in p.parts, "CLAUSE_PATH", rel)
        path = root / p
        require(path.is_file(), "CLAUSE_PATH", f"missing {rel}")
        start, end = item["line_start"], item["line_end"]
        require(isinstance(start, int) and isinstance(end, int), "CLAUSE_RANGE", cid)
        raw = line_slice(path, start, end)
        got = sha256_bytes(raw)
        require(got == item["slice_sha256"], "CLAUSE_SLICE_HASH", f"{cid}: {got}")
        require(raw.decode("utf-8").rstrip("\n") == item["text"], "CLAUSE_TEXT", cid)
        checked.append({"id": cid, "file": rel, "lines": [start, end], "slice_sha256": got})
    require(seen == REQUIRED_CLAUSE_IDS, "CLAUSE_LEDGER_COMPLETENESS", f"seen={sorted(seen)!r}")
    return checked


def verify_embedded_manifest(verifier_root: Path) -> dict[str, str]:
    manifest = verifier_root / "MANIFEST.sha256"
    lines = manifest.read_text(encoding="utf-8").splitlines()
    observed: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-f]{64})  (\./.+)$")
    for line in lines:
        m = pattern.fullmatch(line)
        require(m is not None, "C116_MANIFEST_FORMAT", line)
        expected, rel_text = m.groups()
        rel = Path(rel_text[2:])
        require(not rel.is_absolute() and ".." not in rel.parts, "C116_MANIFEST_PATH", rel_text)
        require(rel.as_posix() not in observed, "C116_MANIFEST_DUPLICATE", rel.as_posix())
        path = verifier_root / rel
        require(path.is_file(), "C116_MANIFEST_MISSING", rel.as_posix())
        got = sha256_file(path)
        require(got == expected, "C116_MANIFEST_HASH", f"{rel}: {got} != {expected}")
        observed[rel.as_posix()] = got
    require(len(observed) == 18, "C116_MANIFEST_CARDINALITY", str(len(observed)))
    return observed


def run_cycle116_verifier_nonmutating(verifier_root: Path) -> dict[str, Any]:
    before = tree_digest(verifier_root)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(
        [
            sys.executable,
            "-B",
            str(verifier_root / "verify_transfer.py"),
            "--anchor",
            str(verifier_root / "inputs/cycle84_anchor.json"),
            "--fixed-jet",
            str(verifier_root / "inputs/fixed_jet_certificate.json"),
        ],
        cwd=verifier_root,
        env=env,
        capture_output=True,
        text=True,
        timeout=180,
        check=False,
    )
    after = tree_digest(verifier_root)
    require(before == after, "C116_VERIFIER_MUTATED_INPUT_TREE", f"{before} != {after}")
    require(not any(verifier_root.rglob("__pycache__")), "C116_BYTECODE_MUTATION", "__pycache__ created")
    require(proc.returncode == 0, "C116_VERIFIER_EXIT", f"rc={proc.returncode}; stderr={proc.stderr[-2000:]}")
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise CheckFailure("C116_VERIFIER_OUTPUT", str(exc)) from exc
    require(result.get("decision") == "CYCLE116_TRANSFER_CERTIFICATE_VERIFIED", "C116_DECISION", repr(result.get("decision")))
    return result


def verify_row_contract(root: Path, c116: dict[str, Any]) -> dict[str, Any]:
    row = load_json(root / "ROW_CONTRACT.json")
    require(row.get("schema") == "cycle117.cycle116_row_contract.v1", "ROW_SCHEMA", repr(row.get("schema")))
    require(row.get("claim_scope") == "FINITE_RAW_SUPPORTWISE_MCA_AND_LD_SW_ONLY", "CLAIM_SCOPE", repr(row.get("claim_scope")))

    r = row["row"]
    expected_row = {
        "field": "F_17^32",
        "characteristic": 17,
        "extension_degree": 32,
        "domain": "H=<theta>",
        "domain_order": 512,
        "domain_generates_code_field": True,
        "dimension": 256,
        "rate": "1/2",
        "agreement": 262,
        "delta": "125/256",
    }
    require(r == expected_row, "ROW_PARAMETERS", repr(r))

    ledger = row["field_ledger"]
    require(ledger == {"q_gen": Q, "q_code": Q, "q_line": Q, "q_chal": None, "mca_denominator": "q_line"}, "FIELD_LEDGER", repr(ledger))

    num = row["numerator"]
    require(num["distinct_bad_slopes"] == N, "NUMERATOR", repr(num))
    require(num["packet_supports_before_same_slope_deduplication"] == PACKET_SUPPORTS, "PACKET_SUPPORTS", repr(num))
    require(num["double_fibers"] == 12 and num["maximum_packet_fiber_size"] == 2, "FIBER_LEDGER", repr(num))
    require(PACKET_SUPPORTS - num["double_fibers"] == N, "DISTINCT_OCCUPANCY", repr(num))

    part = row["canonical_odd_coset_partition"]
    require(
        part
        == {
            "A_padding_support_zero": {"exponent_start": 0, "exponent_end": 118, "size": 119},
            "R_unused_fixed_cosupport": {"exponent_start": 119, "exponent_end": 255, "size": 137},
        },
        "CANONICAL_AR_REJECTED",
        repr(part),
    )

    gauge = row["primitive_log_gauge"]
    require(gauge["canonical_generator"] == "beta=X+2", "GAUGE_MISMATCH", repr(gauge))
    require(gauge["canonical_coefficients_low_to_high"] == [2, 1], "GAUGE_MISMATCH", repr(gauge))
    require(gauge["legacy_display_generator"] == "X+1", "GAUGE_METADATA", repr(gauge))
    require(gauge["legacy_status"] == "QUARANTINED_NOT_CONSUMED", "GAUGE_LEGACY_CONSUMED", repr(gauge))
    require(gauge["numeric_logs_accepted_only_in_canonical_gauge"] is True, "GAUGE_POLICY", repr(gauge))

    exclusions = row["scope_exclusions"]
    require(all(exclusions.get(k) is True for k in ("ordinary_list_decoding", "protocol_soundness_failure", "asymptotic_theorem", "official_prize_counterpacket", "accepted_deployed_prime_field_theorem")), "SCOPE_EXCLUSIONS", repr(exclusions))

    cledger = c116["field_parameter_ledger"]
    require(cledger["q_gen"] == Q and cledger["q_code"] == Q and cledger["q_line"] == Q, "C116_Q_LEDGER", repr(cledger))
    require(cledger["q_chal"] is None and cledger["mca_denominator"] == "q_line", "C116_QCHAL", repr(cledger))
    require(cledger["bad_slope_numerator"] == N, "C116_NUMERATOR", repr(cledger))
    require(cledger["floor_q_line_over_2^128"] == 6, "C116_THRESHOLD", repr(cledger))

    lift = c116["smooth_lift"]
    require(lift["code"] == "RS[F_17^32,H,256]", "C116_ROW", repr(lift))
    require(lift["H_order"] == 512 and lift["H_generates_K"] is True, "C116_GENERATED_DOMAIN", repr(lift))
    require(lift["A_size"] == 119 and lift["R_size"] == 137, "C116_AR", repr(lift))
    require(lift["agreement"] == 262 and lift["delta"] == "125/256", "C116_AGREEMENT", repr(lift))
    require(lift["LD_sw_lower_bound"] == N, "C116_LDSW", repr(lift))

    field = c116["field"]
    require(field["slot_log_generator_is_beta_and_primitive"] is True, "C116_GAUGE_PRIMITIVE", repr(field))
    notice = c116["imports"]["metadata_notice"]
    require(notice["executable_slot_log_generator"] == [2, 1], "C116_GAUGE_EXECUTABLE", repr(notice))
    require(notice["master_display_generator"] == [1, 1], "C116_GAUGE_LEGACY", repr(notice))
    require(notice["status"] == "NONFATAL_METADATA_MISMATCH", "C116_GAUGE_NOTICE", repr(notice))

    scope = c116["scope"]
    require(all(scope.get(k) is False for k in ("ordinary_list_decoding_lower_bound", "protocol_soundness_failure", "asymptotic_theorem", "official_proximity_prize_counterpacket", "accepted_deployed_prime_field_theorem")), "C116_SCOPE", repr(scope))
    return row


def verify_source_arithmetic() -> dict[str, Any]:
    p, m, d, n, k = 17, 16, 32, 512, 256
    require(p % 4 == 1, "EXTENSION_ROW_P_MOD_4", str(p))
    require(m == 1 << 4, "EXTENSION_ROW_M", str(m))
    require(d > 0 and d & (d - 1) == 0, "EXTENSION_ROW_D_POWER_OF_TWO", str(d))
    require(n == m * d and n & (n - 1) == 0, "EXTENSION_ROW_N", str(n))
    require(k * 2 == n, "EXTENSION_ROW_RATE", f"{k}/{n}")
    require(pow(p, d, n) == 1, "EXTENSION_ROW_ORDER", "17^32 != 1 mod 512")
    for e in (1, 2, 4, 8, 16):
        require(pow(p, e, n) != 1, "EXTENSION_ROW_ORDER", f"17^{e} == 1 mod 512")
    require((1 * 1 * m * m) // 4 >= p, "EXTENSION_ROW_COVERAGE", "rho(1-rho)m^2 < p")
    agreement = ((256 - 125) * n + 256 - 1) // 256
    require(agreement == 262, "AGREEMENT_CEILING", str(agreement))
    require(Q // TWO128 == 6, "THRESHOLD_FLOOR", str(Q // TWO128))
    require(TWO128 * N > Q, "THRESHOLD_STRICT", "2^128*N <= 17^32")
    return {
        "p": p,
        "m": m,
        "d": d,
        "n": n,
        "k": k,
        "ord_512_17": 32,
        "coverage_value": 64,
        "agreement": agreement,
        "floor_q_line_over_2^128": 6,
        "threshold_crossing": True,
        "threshold_note": "true but not the main mathematical content; seven slopes already cross",
    }


def verify_event_audit(root: Path) -> dict[str, Any]:
    audit = load_json(root / "EVENT_AUDIT.json")
    require(audit.get("schema") == "cycle117.event_audit.v1", "EVENT_AUDIT_SCHEMA", repr(audit.get("schema")))
    require(audit.get("scope") == "ATTACHED_MANUSCRIPT_SUPPORTWISE_MCA_DEFINITION", "EVENT_AUDIT_SCOPE", repr(audit.get("scope")))
    require(audit.get("attached_source_terminal") == "EVENT_RETAINED", "EVENT_AUDIT_TERMINAL", repr(audit.get("attached_source_terminal")))
    require(audit.get("official_terminal") == "SOURCE_CONTRACT_MISSING_NO_CLAIM", "EVENT_AUDIT_OFFICIAL", repr(audit.get("official_terminal")))
    items = audit.get("items")
    require(isinstance(items, list) and len(items) == 10, "EVENT_AUDIT_CARDINALITY", repr(items))
    statuses = {i["name"]: i["status"] for i in items}
    required = {
        "endpoint deletion": "ABSENT_FROM_SOURCE",
        "periodic quotienting": "PRESENT_BUT_IRRELEVANT",
        "quotient profile or quotient-core charge": "PRESENT_BUT_IRRELEVANT",
        "tangent floor": "PRESENT_BUT_IRRELEVANT",
        "contained-line or contained-incidence exclusion": "PRESENT_AND_PAID",
        "same-slope collision": "PRESENT_AND_PAID",
        "affine-color normalization": "ABSENT_FROM_SOURCE",
        "retained-event map": "ABSENT_FROM_SOURCE",
        "AP_corr or exhaustive charge registry": "ABSENT_FROM_SOURCE",
        "protocol challenge-field filtering": "UNKNOWN_MISSING_CONTRACT",
    }
    require(statuses == required, "EVENT_AUDIT_CONTENT", repr(statuses))

    source_text = "\n".join(
        (root / rel).read_text(encoding="utf-8")
        for rel in (
            "inputs/source/RS_disproof_v3.tex",
            "inputs/source/slackMCA_v3.tex",
            "inputs/source/m2_line_decoding_mca_bridge.md",
        )
    )
    literal_audit = {
        "q_chal_literal_occurrences": source_text.count("q_chal"),
        "AP_corr_literal_occurrences": source_text.count("AP_corr"),
        "affine_color_literal_occurrences": source_text.count("affine-color") + source_text.count("affine_color"),
        "charge_registry_literal_occurrences": source_text.lower().count("charge registry"),
    }
    require(all(v == 0 for v in literal_audit.values()), "UNEXPECTED_CONTRACT_LITERAL", repr(literal_audit))
    return {"items": items, "literal_audit": literal_audit}


def validate_official_clause(document: Path, clause: Any, name: str) -> dict[str, Any]:
    require(isinstance(clause, dict), "OFFICIAL_CLAUSE", f"{name}: not an object")
    exact_keys(clause, {"id", "line_start", "line_end", "text_sha256"}, "OFFICIAL_CLAUSE")
    require(isinstance(clause["id"], str) and clause["id"], "OFFICIAL_CLAUSE", f"{name}: empty id")
    require(isinstance(clause["line_start"], int) and isinstance(clause["line_end"], int), "OFFICIAL_CLAUSE", name)
    raw = line_slice(document, clause["line_start"], clause["line_end"])
    got = sha256_bytes(raw)
    require(got == clause["text_sha256"], "OFFICIAL_CLAUSE_HASH", f"{name}: {got}")
    return {"id": clause["id"], "lines": [clause["line_start"], clause["line_end"]], "text_sha256": got}


def validate_official_contract(contract_path: Path | None, document_path: Path | None, trusted_hash: str | None) -> dict[str, Any]:
    if contract_path is None:
        require(document_path is None and trusted_hash is None, "OFFICIAL_ARGUMENTS", "document/hash supplied without contract")
        return {
            "row": "SOURCE_CONTRACT_MISSING_NO_CLAIM",
            "event": "SOURCE_CONTRACT_MISSING_NO_CLAIM",
            "q_chal": "QCHAL_UNDEFINED_FINITE_MCA_ONLY",
            "q_chal_definition": None,
            "reason": "No authority-pinned official contract was supplied.",
        }

    require(contract_path.is_file(), "OFFICIAL_CONTRACT_MISSING", str(contract_path))
    require(document_path is not None and document_path.is_file(), "OFFICIAL_DOCUMENT_MISSING", repr(document_path))
    require(isinstance(trusted_hash, str) and re.fullmatch(r"[0-9a-f]{64}", trusted_hash) is not None, "OFFICIAL_TRUST_PIN_MISSING", repr(trusted_hash))
    got_contract_hash = sha256_file(contract_path)
    require(got_contract_hash == trusted_hash, "OFFICIAL_CONTRACT_UNTRUSTED", f"{got_contract_hash} != {trusted_hash}")

    contract = load_json(contract_path)
    require(isinstance(contract, dict), "OFFICIAL_SCHEMA", "top level not object")
    exact_keys(
        contract,
        {"schema", "authority", "source_document", "row", "line_parameter", "q_chal", "event_rules", "exhaustive_event_registry"},
        "OFFICIAL_SCHEMA",
    )
    require(contract["schema"] == "cycle117.official_source_contract.v1", "OFFICIAL_SCHEMA", repr(contract["schema"]))
    require(contract["exhaustive_event_registry"] is True, "OFFICIAL_EVENT_REGISTRY", "not exhaustive")

    authority = contract["authority"]
    require(isinstance(authority, dict), "OFFICIAL_AUTHORITY", repr(authority))
    exact_keys(authority, {"name", "version", "effective_date"}, "OFFICIAL_AUTHORITY")
    require(all(isinstance(authority[k], str) and authority[k] for k in authority), "OFFICIAL_AUTHORITY", repr(authority))
    try:
        date.fromisoformat(authority["effective_date"])
    except ValueError as exc:
        raise CheckFailure("OFFICIAL_AUTHORITY_DATE", authority["effective_date"]) from exc

    source_doc = contract["source_document"]
    require(isinstance(source_doc, dict), "OFFICIAL_DOCUMENT", repr(source_doc))
    exact_keys(source_doc, {"path", "sha256"}, "OFFICIAL_DOCUMENT")
    require(isinstance(source_doc["path"], str) and source_doc["path"], "OFFICIAL_DOCUMENT_PATH", repr(source_doc["path"]))
    require(Path(source_doc["path"]).name == document_path.name, "OFFICIAL_DOCUMENT_PATH", f"{source_doc['path']!r} != {document_path.name!r}")
    require(isinstance(source_doc["sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", source_doc["sha256"]) is not None, "OFFICIAL_DOCUMENT_HASH", repr(source_doc["sha256"]))
    got_doc_hash = sha256_file(document_path)
    require(got_doc_hash == source_doc["sha256"], "OFFICIAL_DOCUMENT_HASH", f"{got_doc_hash} != {source_doc['sha256']}")

    row = contract["row"]
    require(isinstance(row, dict), "OFFICIAL_ROW", repr(row))
    exact_keys(row, {"decision", "clause", "field", "domain_order", "dimension"}, "OFFICIAL_ROW")
    require(row["decision"] in {"ACCEPT", "REJECT"}, "OFFICIAL_ROW", repr(row["decision"]))
    require(row["field"] == "F_17^32" and row["domain_order"] == 512 and row["dimension"] == 256, "OFFICIAL_ROW_PARAMETERS", repr(row))
    row_clause = validate_official_clause(document_path, row["clause"], "row")

    line = contract["line_parameter"]
    require(isinstance(line, dict), "OFFICIAL_LINE_PARAMETER", repr(line))
    exact_keys(line, {"field_size", "clause"}, "OFFICIAL_LINE_PARAMETER")
    require(line["field_size"] == Q, "OFFICIAL_LINE_FIELD", repr(line["field_size"]))
    line_clause = validate_official_clause(document_path, line["clause"], "line_parameter")

    qchal = contract["q_chal"]
    require(isinstance(qchal, dict), "OFFICIAL_QCHAL", repr(qchal))
    exact_keys(qchal, {"status", "field_size", "clause"}, "OFFICIAL_QCHAL")
    require(qchal["status"] in {"UNDEFINED", "DEFINED"}, "OFFICIAL_QCHAL", repr(qchal["status"]))
    if qchal["status"] == "UNDEFINED":
        require(qchal["field_size"] is None and qchal["clause"] is None, "OFFICIAL_QCHAL", repr(qchal))
        qchal_terminal: str | None = "QCHAL_UNDEFINED_FINITE_MCA_ONLY"
        qchal_clause = None
        qchal_definition = None
    else:
        require(isinstance(qchal["field_size"], int) and not isinstance(qchal["field_size"], bool) and qchal["field_size"] > 1, "OFFICIAL_QCHAL", repr(qchal))
        qchal_clause = validate_official_clause(document_path, qchal["clause"], "q_chal")
        qchal_terminal = None
        qchal_definition = {"status": "DEFINED_BY_AUTHORITY", "field_size": qchal["field_size"]}

    rules = contract["event_rules"]
    require(isinstance(rules, list) and len(rules) == len(EVENT_RULE_NAMES), "OFFICIAL_EVENT_RULES", repr(rules))
    seen: set[str] = set()
    rule_receipts = []
    actions: dict[str, str] = {}
    any_loss = False
    for rule in rules:
        require(isinstance(rule, dict), "OFFICIAL_EVENT_RULE", repr(rule))
        require(set(rule) in ({"name", "action", "clause"}, {"name", "action", "clause", "surviving_numerator"}), "OFFICIAL_EVENT_RULE", repr(rule))
        name = rule["name"]
        require(name in EVENT_RULE_NAMES and name not in seen, "OFFICIAL_EVENT_RULE_NAME", repr(name))
        seen.add(name)
        action = rule["action"]
        require(action in {"RETAIN", "EXCLUDE", "IDENTIFY", "CHARGE"}, "OFFICIAL_EVENT_ACTION", repr(action))
        surviving = rule.get("surviving_numerator")
        if action == "RETAIN":
            require(surviving in (None, N), "OFFICIAL_EVENT_NUMERATOR", repr(rule))
        elif action in {"EXCLUDE", "IDENTIFY"}:
            any_loss = True
            require(isinstance(surviving, int) and not isinstance(surviving, bool) and 0 <= surviving < N, "OFFICIAL_EVENT_NUMERATOR", repr(rule))
        else:  # CHARGE can leave the raw numerator unchanged but makes it non-free.
            any_loss = True
            require(isinstance(surviving, int) and not isinstance(surviving, bool) and 0 <= surviving <= N, "OFFICIAL_EVENT_NUMERATOR", repr(rule))
        actions[name] = action
        rule_receipts.append(
            {
                "name": name,
                "action": action,
                "clause": validate_official_clause(document_path, rule["clause"], f"event:{name}"),
                "surviving_numerator": surviving,
            }
        )
    require(seen == EVENT_RULE_NAMES, "OFFICIAL_EVENT_RULE_COMPLETENESS", repr(seen))
    if qchal["status"] == "UNDEFINED":
        require(actions["challenge_filter"] == "RETAIN", "OFFICIAL_QCHAL_EVENT_CONTRADICTION", repr(actions["challenge_filter"]))

    row_terminal = "SOURCE_ACCEPTED_CYCLE116_ROW" if row["decision"] == "ACCEPT" else "SOURCE_REJECTED_CYCLE116_ROW"
    event_terminal = "EVENT_CHARGED_OR_EXCLUDED" if any_loss else "EVENT_RETAINED"
    require(row_terminal in TERMINALS and event_terminal in TERMINALS, "OFFICIAL_TERMINAL_SET", f"{row_terminal}, {event_terminal}")
    require(qchal_terminal is None or qchal_terminal in TERMINALS, "OFFICIAL_TERMINAL_SET", repr(qchal_terminal))

    return {
        "row": row_terminal,
        "event": event_terminal,
        "q_chal": qchal_terminal,
        "q_chal_definition": qchal_definition,
        "contract_sha256": got_contract_hash,
        "source_document_sha256": got_doc_hash,
        "authority": authority,
        "clauses": {"row": row_clause, "line_parameter": line_clause, "q_chal": qchal_clause, "event_rules": rule_receipts},
    }
def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="checker package root")
    ap.add_argument("--official-contract", type=Path)
    ap.add_argument("--official-document", type=Path)
    ap.add_argument("--trusted-official-contract-sha256")
    return ap.parse_args()


def main() -> dict[str, Any]:
    args = parse_args()
    root = args.root.resolve()
    require(root.is_dir(), "ROOT_MISSING", str(root))

    critical = verify_critical_hashes(root)
    clauses = verify_clause_ledger(root)
    verifier_root = root / "inputs/cycle116/verifier"
    manifest = verify_embedded_manifest(verifier_root)
    c116 = run_cycle116_verifier_nonmutating(verifier_root)
    row = verify_row_contract(root, c116)
    arithmetic = verify_source_arithmetic()
    event = verify_event_audit(root)
    official = validate_official_contract(args.official_contract, args.official_document, args.trusted_official_contract_sha256)

    attached = {
        "row": "SOURCE_ACCEPTED_CYCLE116_ROW",
        "q_chal": "QCHAL_UNDEFINED_FINITE_MCA_ONLY",
        "event": "EVENT_RETAINED",
        "basis": "PINNED_SOURCE_TEXT_PLUS_SYMBOLIC_LEMMAS_L1_L4",
    }
    require(set(attached.values()) & TERMINALS == {"SOURCE_ACCEPTED_CYCLE116_ROW", "QCHAL_UNDEFINED_FINITE_MCA_ONLY", "EVENT_RETAINED"}, "TERMINAL_SET", repr(attached))

    if official["row"] == "SOURCE_CONTRACT_MISSING_NO_CLAIM":
        label = "BANKABLE_LEMMA"
        primary = "SOURCE_CONTRACT_MISSING_NO_CLAIM"
    elif official["row"] == "SOURCE_REJECTED_CYCLE116_ROW":
        label = "ROUTE_CUT"
        primary = "SOURCE_REJECTED_CYCLE116_ROW"
    elif official["row"] == "SOURCE_ACCEPTED_CYCLE116_ROW" and official["event"] == "EVENT_RETAINED":
        label = "PROOF"
        primary = "SOURCE_ACCEPTED_CYCLE116_ROW"
    else:
        label = "ROUTE_CUT"
        primary = official["event"]

    return {
        "checker": "cycle117_source_contract_checker.v1.1",
        "label": label,
        "primary_terminal": primary,
        "attached_manuscript_source": attached,
        "official_contract": official,
        "field_ledger": row["field_ledger"],
        "finite_theorem": {
            "code": "RS[F_17^32,H,256]",
            "n": 512,
            "k": 256,
            "agreement": 262,
            "delta": "125/256",
            "LD_sw_lower_bound": N,
            "epsilon_mca_lower_bound": f"{N}/17^32",
            "ordinary_list_decoding_claim": False,
        },
        "canonicalization": {
            "A": "119 padding/support-zero points, exponents 0..118",
            "R": "137 unused/fixed co-support points, exponents 119..255",
            "primitive_log_gauge": "beta=X+2 only",
            "legacy_X_plus_1": "QUARANTINED_NOT_CONSUMED",
        },
        "source_arithmetic": arithmetic,
        "event_audit": event,
        "line_decoding_adapter": {
            "identity": "epsilon_mca(C,delta)=LD_sw(C,ceil((1-delta)n))/|F|",
            "cycle116_agreement": 262,
            "external_(delta,a_LD,n+1)_definition": "ABSENT_NOT_PROMOTED",
        },
        "machine_verification": {
            "critical_file_hashes": critical,
            "source_clauses_checked": clauses,
            "cycle116_manifest_files_checked": len(manifest),
            "cycle116_decision": c116["decision"],
            "cycle116_verifier_nonmutating": True,
        },
        "symbolic_lemmas": ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"],
        "scope": {
            "finite_supportwise_MCA_and_LD_sw": True,
            "ordinary_list_decoding": False,
            "protocol_soundness_failure": False,
            "asymptotic_theorem": False,
            "official_prize_counterpacket": label == "PROOF" and primary == "SOURCE_ACCEPTED_CYCLE116_ROW",
        },
    }


def entrypoint() -> int:
    try:
        result = main()
    except CheckFailure as exc:
        print(json.dumps({"checker": "cycle117_source_contract_checker.v1.1", "decision": "CHECKER_REJECTED", "failure_clause": exc.clause, "detail": exc.detail}, indent=2, sort_keys=True))
        return 1
    except (KeyError, TypeError, ValueError, OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"checker": "cycle117_source_contract_checker.v1.1", "decision": "CHECKER_MALFORMED", "detail": str(exc)}, indent=2, sort_keys=True))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(entrypoint())
