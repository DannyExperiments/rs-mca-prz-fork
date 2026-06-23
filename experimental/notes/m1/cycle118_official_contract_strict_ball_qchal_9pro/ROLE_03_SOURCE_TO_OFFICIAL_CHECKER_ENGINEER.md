# Role 03 - Source-to-Official Checker Engineer

You are the reviewer/checker engineer for the official-contract layer.

Design the deterministic checker or schema that would turn Cycle117 from
`SOURCE_CONTRACT_MISSING_NO_CLAIM` into a terminal official result. If the
attached files already contain enough data, specify the checker and terminal
receipt. If not, specify the minimal missing input object and fail-closed
terminal.

Required terminal statuses:

```text
OFFICIAL_ROW_EVENT_CONTRACT_ACCEPTED
OFFICIAL_ROW_REJECTED
OFFICIAL_EVENT_CHARGED_OR_EXCLUDED
OFFICIAL_QCHAL_DENSITY_LOSS
SOURCE_CONTRACT_MISSING_NO_CLAIM
MALFORMED_INPUT
```

The checker must separately record:

```text
row field
domain H
code dimension
line parameter field
q_gen
q_code
q_line
q_chal
agreement convention
retained-event rules
charge/exclusion rules
final numerator
official_prize_status
```

If you can, provide a proof-level schema and a sample JSON receipt for the
Cycle116 row.

