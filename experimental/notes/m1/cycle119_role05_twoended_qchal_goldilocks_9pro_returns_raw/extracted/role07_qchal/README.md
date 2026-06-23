# Cycle119 qchal Sampler-Map Checker

Run the packet-only receipt:

```bash
python verify_qchal_sampler_map.py receipts/current_packet_missing_authority.json
```

Expected stdout:

```text
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

Run all synthetic branch tests:

```bash
./run_self_tests.sh
```

Positive synthetic receipts require their independently supplied trust pin:

```bash
ROOT=$(python -c 'import json; print(json.load(open("receipts/direct_k_valid.json"))["authority_root"])')
python verify_qchal_sampler_map.py receipts/direct_k_valid.json --trusted-authority-root "$ROOT"
```

The synthetic roots exercise the state machine only. They are not official authority roots.
