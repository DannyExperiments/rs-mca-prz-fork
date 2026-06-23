#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
./run_checker.sh > receipts/success.out
if python3 verify_goldilocks_fixed_jet.py --self-test-tamper > receipts/tamper.out 2> receipts/tamper.err; then
  echo "TAMPER_SELF_TEST_UNEXPECTEDLY_PASSED" >&2
  exit 1
fi
grep -q 'SELF_TEST_TAMPER_REJECTED' receipts/tamper.err
echo 'SELF_TESTS_PASS'
