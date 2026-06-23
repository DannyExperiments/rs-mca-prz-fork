#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
TMPDIR_LOCAL="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_LOCAL"; rm -f "$ROOT"/inputs/tamper.*.json' EXIT

python3 "$ROOT/verify_two_ended.py" > "$TMPDIR_LOCAL/success.json"
python3 - "$TMPDIR_LOCAL/success.json" <<'PY'
import json, sys
x=json.load(open(sys.argv[1]))
assert x['decision']=='CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED'
assert x['finite_checks']['cycle84_distinct_occupancy']==52_747_567_092
assert x['row']['agreement']==263
print('SUCCESS_TERMINAL_OK')
PY

set +e
python3 "$ROOT/verify_two_ended.py" --two-ended "$TMPDIR_LOCAL/missing.json" > "$TMPDIR_LOCAL/missing.json.out"
status=$?
set -e
[[ $status -eq 3 ]]
python3 - "$TMPDIR_LOCAL/missing.json.out" <<'PY'
import json, sys
x=json.load(open(sys.argv[1]))
assert x['decision']=='MISSING_TWO_ENDED_CERTIFICATE'
print('MISSING_INPUT_FAIL_CLOSED_OK')
PY

TAMPER="$(mktemp "$ROOT/inputs/tamper.XXXXXX.json")"
python3 - "$ROOT/inputs/two_ended_certificate.json" "$TAMPER" <<'PY'
import json, sys
x=json.load(open(sys.argv[1]))
x['partition']['A_odd_coset_exponent_range_inclusive']=[0,118]
open(sys.argv[2],'w').write(json.dumps(x,indent=2,sort_keys=True)+'\n')
PY
set +e
python3 "$ROOT/verify_two_ended.py" --two-ended "$TAMPER" > "$TMPDIR_LOCAL/tamper.json.out"
status=$?
set -e
[[ $status -eq 1 ]]
python3 - "$TMPDIR_LOCAL/tamper.json.out" <<'PY'
import json, sys
x=json.load(open(sys.argv[1]))
assert x['decision']=='CERTIFICATE_REJECTED'
assert x['failure_clause']=='TWO_ENDED_PARTITION_RANGES'
print('PARTITION_TAMPER_REJECTED_OK')
PY

printf '%s\n' CYCLE118_TWO_ENDED_SELF_TESTS_PASSED
