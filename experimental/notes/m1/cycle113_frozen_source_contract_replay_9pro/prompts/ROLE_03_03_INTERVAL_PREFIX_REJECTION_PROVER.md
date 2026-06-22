# Role 03 - Interval Prefix Rejection Prover

Your task is to prove that the interval / overlapping-prefix stress family is
rejected by official source/APcorr conditions, or else identify why that
rejection is not source-valid.

Do not merely say "intervals have additive structure." You must connect the
structure to an official predicate or derive a theorem of the form:

```text
official AP_corr + no frozen charge
  => interval/overlapping-prefix retained colors <= floor(q_line / 2^128)
```

Search the packet for the exact source-visible invariants available:

```text
restricted sums
interpolation defect
high coefficient Fourier mass
short prefix concentration
same-slope collisions
endpoint collapse
affine color normalization
periodic or quotient stabilizers
```

Try to return `PROOF` as either:

```text
SOURCE_REJECTED
```

or

```text
T1_APCORR_LOCAL_LIMIT
```

If the interval family survives all source-visible predicates in the packet,
return `EXACT_NEW_WALL` and specify the smallest missing APcorr/local-limit
lemma. If you find a source-valid survival mechanism, outline a
`COUNTERPACKET` route with exact data needed.

