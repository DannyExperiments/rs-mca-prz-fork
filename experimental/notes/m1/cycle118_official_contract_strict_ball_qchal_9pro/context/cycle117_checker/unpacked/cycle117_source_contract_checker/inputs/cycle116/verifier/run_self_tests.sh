#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

./run_verifier.sh > receipts/success.json
python3 - <<'PY'
import json
r=json.load(open('receipts/success.json'))
assert r['decision']=='CYCLE116_TRANSFER_CERTIFICATE_VERIFIED'
PY

set +e
python3 verify_transfer.py --anchor inputs/cycle84_anchor.json --fixed-jet inputs/DOES_NOT_EXIST.json > receipts/missing_fixed_jet.json
rc_missing=$?
set -e
[[ "$rc_missing" -eq 3 ]]

bad="$(mktemp)"
python3 - "$bad" <<'PY'
import json, sys
src='inputs/fixed_jet_certificate.json'
d=json.load(open(src))
d['schema']='cycle116.invalid_schema.v0'
open(sys.argv[1],'w').write(json.dumps(d))
PY
set +e
python3 verify_transfer.py --anchor inputs/cycle84_anchor.json --fixed-jet "$bad" > receipts/tamper_rejected.json
rc_bad=$?
set -e
rm -f "$bad"
[[ "$rc_bad" -eq 1 ]]

grep -q 'MISSING_FIXED_JET_CERTIFICATE' receipts/missing_fixed_jet.json
grep -q 'CERTIFICATE_REJECTED' receipts/tamper_rejected.json
printf '%s\n' 'SELF_TESTS_PASS'
