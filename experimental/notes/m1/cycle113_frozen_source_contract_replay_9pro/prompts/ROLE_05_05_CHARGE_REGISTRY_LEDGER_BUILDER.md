# Role 05 - Charge Registry Ledger Builder

Your task is to build the most complete exact charge registry and integer
`q_line` ledger the packet supports.

Include at least these possible charge families:

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
official predicate
charged final color set
cap
q_line allocation
whether it overlaps another charge
whether it applies to interval/P190
```

Use Cycle112's no-double-spend theorem: an above-threshold final retained color
set cannot be saved by partitioning the same colors into charged/free bins
unless the charge has an exact disjoint cap and allocation.

Try to prove:

```text
COLOR_COMPRESSED_OR_CHARGED
```

or explain exactly why no official charge ledger is present. If you prove a
charge, show how many final colors remain and verify:

```text
2^128 * N_free <= q_line
```

If no complete ledger can be built, return `EXACT_NEW_WALL` with the first
missing charge receipt.

