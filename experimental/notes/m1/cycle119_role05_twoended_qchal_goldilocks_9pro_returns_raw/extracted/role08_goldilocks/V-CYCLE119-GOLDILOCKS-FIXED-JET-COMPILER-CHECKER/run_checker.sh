#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 verify_goldilocks_fixed_jet.py --receipt receipts/success.json
