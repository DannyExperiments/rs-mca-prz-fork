#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
exec python3 verify_transfer.py \
  --anchor inputs/cycle84_anchor.json \
  --fixed-jet inputs/fixed_jet_certificate.json
