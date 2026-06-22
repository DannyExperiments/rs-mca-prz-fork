# Role 05 - Charge Ledger No-Double-Spend Auditor

Your task is to build the exact official charge registry and test whether it
can pay the P190/C284 gaps without double spending colors.

Include at least:

```text
endpoint
field-transfer
affine-color
periodic / quotient
same-slope
contained incidence
tangent/support
prefix-design / short restricted-sum
additive-energy
interpolation-defect Fourier
retained-tag normalization
hidden action rank
```

For each charge, state:

```text
official source predicate
charged final event IDs or quotient map
cap
q_line allocation
overlap with other charges
whether it applies to P190
whether it applies to C284
```

Use the Cycle112 no-double-spend principle: a final retained set above 130 is
not paid merely because the same colors have scary labels. There must be a
disjoint cap and exact `q_line` allocation.

Return `COLOR_COMPRESSED_OR_CHARGED` only with exact arithmetic. Otherwise
return `SOURCE_RECEIPT_MISSING_NO_CLAIM` or `EXACT_NEW_WALL` with the first
missing official charge receipt.

