# Official Admissibility Gates

Cycle120 update:

```text
The ABF PDF was checked directly. Under the printed ABF grand MCA definition,
the row/domain/predicate/sampler/filter gates below pass for
RS[F_17^32,H,256]. See:

experimental/notes/m1/cycle120_abf_negative_result_packet/
experimental/notes/m1/cycle119_official_source_audit/V_CYCLE120_ABF_DIRECT_ADMISSIBILITY_AUDIT.md
```

The theorem is not the same object as an official Proximity Prize claim until all gates below are accepted.

## Gate 1: Row

```text
C = RS[F_17^32,H,256], |H|=512
```

Question:

```text
Is this row admitted by the grand MCA challenge?
```

If rejected, ask whether the rejected feature is:

```text
extension field;
field size;
n=512;
rate 1/2;
smooth subgroup domain;
another row condition.
```

## Gate 2: Smooth Domain

Question:

```text
Is H=<theta> a permitted smooth multiplicative evaluation domain?
```

This should be accepted if the challenge admits power-of-two multiplicative subgroups.

## Gate 3: Predicate

Our predicate:

```text
There exists a support S of size at least (1-delta)n where f+gamma g is
explained by a codeword, but f and g are not simultaneously explained on
that same support S.
```

Question:

```text
Is this the official epsilon_mca predicate?
```

## Gate 4: Sampler

Source theorem denominator:

```text
q_line = |F_17^32|.
```

Question:

```text
Is gamma sampled uniformly from F_17^32?
```

If not, require:

```text
challenge space Omega;
distribution on Omega;
map Omega -> F_17^32 or to another line field;
exact pushforward mass of the certified bad slope set.
```

## Gate 5: Event Retention

Question:

```text
Are the certified support-wise events retained without endpoint, quotient,
periodic, duplicate, charge, or protocol filters?
```

If filters exist, require the final official mass:

```text
T / M
```

and check:

```text
2^128 * T > M.
```

## Gate Outcomes

```text
All gates accepted:
  Prepare official negative-result submission.

Extension field rejected:
  Activate Goldilocks prime-field fallback.

Predicate mismatch:
  Build a predicate adapter or stop at the theorem.

Sampler mismatch:
  Prove balanced projection or exact pushforward mass.

Event filter reduces mass:
  Need exact retained-mass theorem.
```
