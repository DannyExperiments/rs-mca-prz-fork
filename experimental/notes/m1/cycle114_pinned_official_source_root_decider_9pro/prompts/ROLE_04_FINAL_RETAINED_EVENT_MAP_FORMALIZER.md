# Role 04 - Final Retained Event Map Formalizer

Your task is to define the final `q_line` event/color map from official source
files. Cycle113 showed that preliminary color counts are meaningless unless we
know what survives to the final ledger.

Build the strongest formal map supported by the packet:

```text
raw model color/support data
  -> source adapter object
  -> endpoint-normalized object
  -> affine/retained-tag-normalized object
  -> quotient/periodic/same-slope/contained-filtered object
  -> final q_line free event ID
```

Apply it to P190 and C284 if possible. You must output one of:

```text
final retained free events <= 130, with exact map and losses
final retained free events > 130, with exact official assumptions
SOURCE_RECEIPT_MISSING_NO_CLAIM
```

If the official final map is absent, do not make one up. Give the minimal
schema/receipt required for a replay checker to decide it.

