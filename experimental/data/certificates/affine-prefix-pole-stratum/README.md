# Affine-prefix pole-stratum certificate

This directory binds the zero-ledger structural theorem in
`experimental/notes/thresholds/affine_prefix_pole_stratum.md` to its current
source dependencies and deterministic replay.

Run from the repository root:

```bash
python3 experimental/scripts/verify_affine_prefix_pole_stratum.py
python3 -O experimental/scripts/verify_affine_prefix_pole_stratum.py
```

Both outputs must match
`verify_affine_prefix_pole_stratum.expected.txt`.  `source_pins.json` records
the exact base and ten load-bearing source files.  The verifier uses only the
Python standard library and includes eleven semantic mutation tests.

This certificate proves no semantic C1--C9 survival, ledger payment, parent
theorem, or official-score movement.
