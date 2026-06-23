#!/usr/bin/env python3
"""Nonmutating self-tests for the Cycle117 checker.

The full Cycle116 replay runs once. Destructive tests run only in temporary
copies; official-contract state-machine tests use temporary synthetic documents.
No package receipt is overwritten and the legacy mutating Cycle116 self-test is
never invoked.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / "verify_source_contract.py"
N = 52_747_567_092
Q = 17 ** 32
EVENT_NAMES = [
    "endpoint",
    "periodic",
    "quotient",
    "tangent",
    "contained_line",
    "affine_color",
    "retained_event",
    "charge_registry",
    "challenge_filter",
]


def tree_digest(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        rel = path.relative_to(root).as_posix().encode("utf-8")
        raw = path.read_bytes()
        h.update(len(rel).to_bytes(8, "big")); h.update(rel)
        h.update(len(raw).to_bytes(8, "big")); h.update(raw)
    return h.hexdigest()


def run(args: list[str], timeout: int = 240) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.run(args, cwd=ROOT, env=env, capture_output=True, text=True, timeout=timeout, check=False)


def parse(proc: subprocess.CompletedProcess[str]) -> dict[str, Any]:
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(
            f"not JSON: rc={proc.returncode}, stdout={proc.stdout!r}, stderr={proc.stderr!r}"
        ) from exc


def baseline_test() -> None:
    proc = run([sys.executable, "-B", str(CHECKER)])
    assert proc.returncode == 0, (proc.returncode, proc.stdout, proc.stderr)
    got = parse(proc)
    expected = json.loads((ROOT / "EXPECTED_RECEIPT.json").read_text(encoding="utf-8"))
    assert got == expected
    assert got["label"] == "BANKABLE_LEMMA"
    assert got["primary_terminal"] == "SOURCE_CONTRACT_MISSING_NO_CLAIM"
    assert got["attached_manuscript_source"] == {
        "basis": "PINNED_SOURCE_TEXT_PLUS_SYMBOLIC_LEMMAS_L1_L4",
        "event": "EVENT_RETAINED",
        "q_chal": "QCHAL_UNDEFINED_FINITE_MCA_ONLY",
        "row": "SOURCE_ACCEPTED_CYCLE116_ROW",
    }


def copied_package() -> tuple[tempfile.TemporaryDirectory[str], Path]:
    td: tempfile.TemporaryDirectory[str] = tempfile.TemporaryDirectory(prefix="cycle117-selftest-")
    dst = Path(td.name) / "pkg"
    shutil.copytree(ROOT, dst)
    return td, dst


def hash_tamper_test() -> None:
    td, dst = copied_package()
    try:
        p = dst / "inputs/source/RS_disproof_v3.tex"
        p.write_text(p.read_text(encoding="utf-8") + "\n% tamper\n", encoding="utf-8")
        proc = run([sys.executable, "-B", str(CHECKER), "--root", str(dst)], timeout=30)
        out = parse(proc)
        assert proc.returncode == 1
        assert out["failure_clause"] == "INPUT_HASH_MISMATCH"
    finally:
        td.cleanup()


ROW_VALIDATOR_BOOTSTRAP = r'''
import importlib.util, json, pathlib, sys
sys.dont_write_bytecode = True
checker = pathlib.Path(sys.argv[1])
root = pathlib.Path(sys.argv[2])
spec = importlib.util.spec_from_file_location("cycle117_checker_test", checker)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
c116 = json.loads((root / "inputs/cycle116/verifier/receipts/success.json").read_text())
try:
    mod.verify_row_contract(root, c116)
except mod.CheckFailure as exc:
    print(json.dumps({"failure_clause": exc.clause, "detail": exc.detail}))
    raise SystemExit(1)
print(json.dumps({"decision": "UNEXPECTED_ACCEPT"}))
raise SystemExit(0)
'''


def semantic_tamper_test(mutator: Callable[[dict[str, Any]], None], expected_clause: str) -> None:
    td, dst = copied_package()
    try:
        row_path = dst / "ROW_CONTRACT.json"
        row = json.loads(row_path.read_text(encoding="utf-8"))
        mutator(row)
        row_path.write_text(json.dumps(row, indent=2) + "\n", encoding="utf-8")
        proc = run(
            [sys.executable, "-B", "-c", ROW_VALIDATOR_BOOTSTRAP, str(CHECKER), str(dst)],
            timeout=30,
        )
        out = parse(proc)
        assert proc.returncode == 1, (proc.returncode, out)
        assert out["failure_clause"] == expected_clause, out
    finally:
        td.cleanup()


OFFICIAL_VALIDATOR_BOOTSTRAP = r'''
import importlib.util, json, pathlib, sys
sys.dont_write_bytecode = True
checker = pathlib.Path(sys.argv[1])
contract = pathlib.Path(sys.argv[2])
document = pathlib.Path(sys.argv[3])
trusted = None if sys.argv[4] == "-" else sys.argv[4]
spec = importlib.util.spec_from_file_location("cycle117_checker_test", checker)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
try:
    result = mod.validate_official_contract(contract, document, trusted)
except mod.CheckFailure as exc:
    print(json.dumps({"failure_clause": exc.clause, "detail": exc.detail}))
    raise SystemExit(1)
print(json.dumps(result, sort_keys=True))
raise SystemExit(0)
'''


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def clause(line_no: int, line: str, cid: str) -> dict[str, Any]:
    return {
        "id": cid,
        "line_start": line_no,
        "line_end": line_no,
        "text_sha256": sha256_bytes((line + "\n").encode("utf-8")),
    }


def make_official_fixture(
    td: Path,
    *,
    row_decision: str = "ACCEPT",
    qchal_defined: bool = False,
    changed_rule: tuple[str, str, int] | None = None,
) -> tuple[Path, Path, str]:
    lines = [
        "Authority-pinned Cycle117 source contract.",
        f"The exact Cycle116 extension-field row decision is {row_decision}.",
        f"The line parameter is sampled over a field of size {Q}.",
        "The protocol challenge field is separately defined." if qchal_defined else "No protocol challenge field is defined for this theorem.",
    ]
    event_line: dict[str, int] = {}
    for name in EVENT_NAMES:
        event_line[name] = len(lines) + 1
        action = changed_rule[1] if changed_rule and changed_rule[0] == name else "RETAIN"
        lines.append(f"Event family {name} has action {action}.")
    document = td / "official_source.txt"
    document.write_text("\n".join(lines) + "\n", encoding="utf-8")

    rules = []
    for name in EVENT_NAMES:
        action = changed_rule[1] if changed_rule and changed_rule[0] == name else "RETAIN"
        rule: dict[str, Any] = {
            "name": name,
            "action": action,
            "clause": clause(event_line[name], lines[event_line[name] - 1], f"event-{name}"),
        }
        if action != "RETAIN":
            assert changed_rule is not None
            rule["surviving_numerator"] = changed_rule[2]
        rules.append(rule)

    qchal = (
        {"status": "DEFINED", "field_size": 65537, "clause": clause(4, lines[3], "q-chal")}
        if qchal_defined
        else {"status": "UNDEFINED", "field_size": None, "clause": None}
    )
    contract_obj = {
        "schema": "cycle117.official_source_contract.v1",
        "authority": {"name": "Synthetic Test Authority", "version": "test-v1", "effective_date": "2026-06-22"},
        "source_document": {"path": document.name, "sha256": hashlib.sha256(document.read_bytes()).hexdigest()},
        "row": {
            "decision": row_decision,
            "clause": clause(2, lines[1], "row"),
            "field": "F_17^32",
            "domain_order": 512,
            "dimension": 256,
        },
        "line_parameter": {"field_size": Q, "clause": clause(3, lines[2], "line-parameter")},
        "q_chal": qchal,
        "event_rules": rules,
        "exhaustive_event_registry": True,
    }
    contract = td / "official_contract.json"
    contract.write_text(json.dumps(contract_obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return contract, document, hashlib.sha256(contract.read_bytes()).hexdigest()


def official_call(contract: Path, document: Path, trusted: str | None) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    proc = run(
        [sys.executable, "-B", "-c", OFFICIAL_VALIDATOR_BOOTSTRAP, str(CHECKER), str(contract), str(document), trusted or "-"],
        timeout=30,
    )
    return proc, parse(proc)


def official_trust_pin_test() -> None:
    with tempfile.TemporaryDirectory(prefix="cycle117-official-") as td_text:
        td = Path(td_text)
        contract, document, _ = make_official_fixture(td)
        proc, out = official_call(contract, document, None)
        assert proc.returncode == 1
        assert out["failure_clause"] == "OFFICIAL_TRUST_PIN_MISSING"


def official_terminal_tests() -> None:
    with tempfile.TemporaryDirectory(prefix="cycle117-official-terminals-") as td_text:
        td = Path(td_text)

        # Use separate directories so every document/contract pair is immutable.
        cases = []
        for dirname, kwargs in [
            ("accept", {}),
            ("reject", {"row_decision": "REJECT"}),
            ("charged", {"changed_rule": ("charge_registry", "CHARGE", N)}),
            ("defined_qchal", {"qchal_defined": True}),
        ]:
            case_dir = td / dirname
            case_dir.mkdir()
            c, d, h = make_official_fixture(case_dir, **kwargs)
            proc, out = official_call(c, d, h)
            assert proc.returncode == 0, (proc.returncode, out)
            cases.append((dirname, out))

        by_name = dict(cases)
        assert by_name["accept"]["row"] == "SOURCE_ACCEPTED_CYCLE116_ROW"
        assert by_name["accept"]["event"] == "EVENT_RETAINED"
        assert by_name["accept"]["q_chal"] == "QCHAL_UNDEFINED_FINITE_MCA_ONLY"

        assert by_name["reject"]["row"] == "SOURCE_REJECTED_CYCLE116_ROW"
        assert by_name["charged"]["event"] == "EVENT_CHARGED_OR_EXCLUDED"

        assert by_name["defined_qchal"]["q_chal"] is None
        assert by_name["defined_qchal"]["q_chal_definition"] == {
            "status": "DEFINED_BY_AUTHORITY",
            "field_size": 65537,
        }


def qchal_filter_contradiction_test() -> None:
    with tempfile.TemporaryDirectory(prefix="cycle117-qchal-contradiction-") as td_text:
        td = Path(td_text)
        contract, document, pin = make_official_fixture(
            td,
            qchal_defined=False,
            changed_rule=("challenge_filter", "EXCLUDE", N - 1),
        )
        proc, out = official_call(contract, document, pin)
        assert proc.returncode == 1
        assert out["failure_clause"] == "OFFICIAL_QCHAL_EVENT_CONTRADICTION"


def main() -> int:
    before = tree_digest(ROOT)
    baseline_test()
    hash_tamper_test()
    semantic_tamper_test(
        lambda row: row["canonical_odd_coset_partition"].update(
            {
                "A_padding_support_zero": {"exponent_start": 119, "exponent_end": 255, "size": 137},
                "R_unused_fixed_cosupport": {"exponent_start": 0, "exponent_end": 118, "size": 119},
            }
        ),
        "CANONICAL_AR_REJECTED",
    )
    semantic_tamper_test(
        lambda row: row["field_ledger"].update({"q_chal": row["field_ledger"]["q_line"]}),
        "FIELD_LEDGER",
    )
    semantic_tamper_test(
        lambda row: row["primitive_log_gauge"].update(
            {"canonical_generator": "X+1", "canonical_coefficients_low_to_high": [1, 1]}
        ),
        "GAUGE_MISMATCH",
    )
    official_trust_pin_test()
    official_terminal_tests()
    qchal_filter_contradiction_test()
    after = tree_digest(ROOT)
    assert before == after, (before, after)
    assert not any(ROOT.rglob("__pycache__"))
    print(
        json.dumps(
            {
                "decision": "NONMUTATING_SELF_TESTS_PASS",
                "package_tree_sha256": after,
                "tests": [
                    "baseline_expected_receipt",
                    "source_hash_tamper_rejected",
                    "canonical_A_R_swap_rejected",
                    "invented_q_chal_rejected",
                    "X_plus_1_canonical_gauge_rejected",
                    "untrusted_official_contract_rejected",
                    "official_accept_terminal_verified",
                    "official_reject_terminal_verified",
                    "official_charged_or_excluded_terminal_verified",
                    "defined_qchal_recorded_without_invented_terminal",
                    "undefined_qchal_challenge_filter_contradiction_rejected",
                    "package_tree_unchanged",
                ],
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
