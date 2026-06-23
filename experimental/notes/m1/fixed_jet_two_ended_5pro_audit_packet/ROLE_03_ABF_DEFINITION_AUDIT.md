# Role 03 - ABF Definition Audit

Audit the ABF consequence only.

Use:

```text
ABF_EXCERPTS_FOR_AUDIT.md
cycle120_THEOREM_NOTE.md
fixed_jet_and_two_ended_transfer_note.md
```

You may use the supplied ABF source text/PDF if available in the context. Do
not use the open internet.

## Question

Assuming the row theorem is correct:

```text
LD_sw(RS[F_17^32,H,256],262) >= 52,747,567,092,
```

does it actually imply, under ABF Definition 4.3 as printed,

```text
epsilon_mca(RS[F_17^32,H,256],125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128?
```

## Required Checks

- Does ABF allow `F = F_17^32`?
- Does ABF allow `H=<theta>`, `|H|=512`, as a smooth evaluation domain?
- Does ABF require rate in `{1/2,1/4,1/8,1/16}`, and does the row have rate
  `1/2`?
- Does ABF Definition 4.3 use support-wise same-support noncontainment?
- Does ABF sample `gamma <- F` uniformly?
- Does ABF use the closed threshold `|S| >= (1-delta)n`?
- At `delta=125/256`, `n=512`, is the threshold exactly `262`?
- Is there any printed extra endpoint, quotient, periodic, charge, duplicate,
  or event-retention filter in the grand MCA definition?

Find the first mismatch if one exists.
