#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHECKER = ROOT / "cycle109_checker.py"

CASES = [
    ("enumerate", "example_enumerate.json", "example_truth.test.json", None),
    ("audit", "example_certified_empty.json", "example_certified_empty.test.json", "STRATIFIED_COVER_CERTIFIED"),
    ("audit", "example_unpaid_balanced.json", "example_unpaid_balanced.test.json", "UNPAID_BALANCED_COVER"),
    ("audit", "example_unpaid_high.json", "example_unpaid_high.test.json", "UNPAID_HIGH_PLANE"),
]

for command, src, dst, expected in CASES:
    out = ROOT / dst
    subprocess.run([sys.executable, str(CHECKER), command, str(ROOT / src), "--output", str(out)], check=True)
    data = json.loads(out.read_text())
    if expected is not None and data.get("terminal_label") != expected:
        raise SystemExit(f"{src}: expected {expected}, got {data.get('terminal_label')}")
    print(f"OK {src}: {data.get('terminal_label', 'ENUMERATED')} ")
print("ALL TESTS PASSED")
