# Role 08: Certificate Engineer / LOW Stress Harness

No Internet. Use only the attached packet and your own reasoning.

Design a proof-carrying checker or finite stress harness for Cycle110 LOW. You
may build on the Cycle109 Role 08 checker, but do not treat finite data as a
universal proof.

The checker should certify, for finite official instances:

- exact `Z_t(E,B,w)` extraction;
- same-slope deduplication in `K_line`;
- charge classification where mechanically checkable;
- retained chart tags;
- same-field injective normalization;
- exact `q_line` numerator accounting;
- terminal labels that cannot overclaim.

Accepted terminal labels should separate:

```text
LOW_CERTIFIED_FOR_INSTANCE
UNPAID_LOW_RESIDUAL
FIELD_LEDGER_MISMATCH
MODEL_ONLY_STRESS_FAMILY
SOURCE_VALID_LOW_COUNTERPACKET
```

State exactly what external proof receipts would be needed to promote a family
from finite stress to theorem/counterpacket.

