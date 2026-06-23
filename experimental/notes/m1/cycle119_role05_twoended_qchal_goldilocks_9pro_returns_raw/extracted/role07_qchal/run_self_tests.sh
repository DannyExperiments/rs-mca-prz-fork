#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
CHECK="$ROOT/verify_qchal_sampler_map.py"
R="$ROOT/receipts"

root_of() {
  python - "$1" <<'PY'
import json,sys
print(json.load(open(sys.argv[1]))['authority_root'])
PY
}

check() {
  local file="$1" expected="$2" mode="${3:-pinned}"
  local got
  if [[ "$mode" == "unpinned" ]]; then
    got="$(python "$CHECK" "$file")"
  else
    got="$(python "$CHECK" "$file" --trusted-authority-root "$(root_of "$file")")"
  fi
  [[ "$got" == "$expected" ]] || { echo "FAIL $file: $got != $expected"; exit 1; }
  echo "PASS $(basename "$file") -> $got"
}

check "$R/current_packet_missing_authority.json" UNDEFINED_MAP_NO_OFFICIAL_CLAIM unpinned
check "$R/direct_k_valid.json" DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
check "$R/balanced_projection_valid.json" BALANCED_CHALLENGE_PROJECTION_NO_LOSS
check "$R/identity_E_scalar_extension_valid.json" IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
check "$R/official_filter_drops_below.json" OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD
check "$R/balanced_dedup_drops_below.json" OFFICIAL_EVENT_FILTER_DROPS_BELOW_THRESHOLD
check "$R/undefined_map_valid_root.json" UNDEFINED_MAP_NO_OFFICIAL_CLAIM
check "$R/lossy_but_still_above.json" UNDEFINED_MAP_NO_OFFICIAL_CLAIM
check "$R/tampered_source_hash.json" UNDEFINED_MAP_NO_OFFICIAL_CLAIM

# A valid receipt without an independently supplied root must fail closed.
check "$R/direct_k_valid.json" UNDEFINED_MAP_NO_OFFICIAL_CLAIM unpinned

# A wrong external trust pin must fail closed.
got="$(python "$CHECK" "$R/direct_k_valid.json" --trusted-authority-root "$(printf '0%.0s' {1..64})")"
[[ "$got" == UNDEFINED_MAP_NO_OFFICIAL_CLAIM ]] || { echo "FAIL wrong trust pin"; exit 1; }
echo "PASS wrong external trust pin -> $got"

echo ALL_QCHAL_SAMPLER_MAP_SELF_TESTS_PASSED
