# Role 07: q-Ledger LOW Budget

No Internet. Use only the attached packet and your own reasoning.

Build the exact q-ledger for the LOW branch.

You must distinguish:

- `q_gen`: corrected-reserve / entropy source field;
- `q_code`: code alphabet;
- `q_line`: actual distinct-slope field and security denominator;
- `q_chal`: protocol challenge field, unusable without transfer theorem.

Derive the exact inequality a LOW theorem must satisfy to fit the final target:

```text
N_off <= floor(q_line / 2^128)
```

If LOW contributes a calibrated main term, state the exact allowed budget and
what field-size lower bound or charge cap is required. If the LOW budget cannot
fit, state the exact counterpacket mechanism or parameter obstruction.

