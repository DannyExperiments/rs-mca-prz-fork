# Official Admissibility Checklist

This checklist is for deciding whether the Cycle119 strict-263 finite/source theorem is also an official Proximity Prize counterexample.

## Already Proved In The Packet

### Finite Row

```text
K = F_17^32
H = <theta>
|H| = 512
C = RS[K,H,256]
```

### Support-Wise Lower Bound

```text
LD_sw(C,263) >= 52,747,567,092
```

### Strict Radius

```text
distance <= 512 - 263 = 249
249 < 250 = (125/256)*512
```

### Source Density

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128
```

provided the source denominator is the line field:

```text
q_line = |K| = 17^32.
```

### Theoretical Repair

The proof uses the two-ended locator theorem:

```text
common top six coefficients + common nonzero constant coefficient
```

for the augmented degree-249 locators. It does not multiply native explainers by a degree-120 padding locator.

## Needs Official Confirmation

### Gate 1: Row Admission

Question:

```text
Does the grand MCA challenge admit C = RS[F_17^32,H,256]?
```

Positive consequence:

```text
Proceed to predicate/sampler matching.
```

Negative consequence:

```text
Ask for the first rejected feature:
extension field, n=512, smooth subgroup, rate, or another row condition.
```

If extension fields are rejected, activate the Goldilocks fallback route.

### Gate 2: Smooth Domain Admission

Question:

```text
Is H=<theta>, |H|=512, a permitted smooth multiplicative evaluation domain?
```

Positive consequence:

```text
The row is a valid rate-1/2 smooth RS row.
```

Negative consequence:

```text
Need an accepted-domain compiler.
```

### Gate 3: Predicate Matching

Question:

```text
Is official epsilon_mca the support-wise same-support noncontainment predicate?
```

Our predicate:

```text
There exists a large support S where f+gamma g is code-explained,
but f and g are not simultaneously code-explained on that same S.
```

Positive consequence:

```text
The LD_sw theorem feeds epsilon_mca directly.
```

Negative consequence:

```text
Need a predicate adapter or identify the first missing condition.
```

### Gate 4: Sampler / Denominator Matching

Question:

```text
Is gamma sampled uniformly from F_17^32?
```

Positive consequence:

```text
Denominator = 17^32 and the displayed density is official.
```

Negative consequences:

```text
If a larger field E is used by identity scalar extension, density may be killed.
If a separate challenge space maps to K, need a balanced projection or exact
pushforward mass certificate.
```

### Gate 5: Event Retention

Question:

```text
Are there endpoint, quotient, periodic, charge, duplicate, or event-retention filters?
```

Positive consequence:

```text
No finite numerator loss beyond the already counted slope collisions.
```

Negative consequence:

```text
Need the exact retained numerator T and denominator M, then check:
2^128 * T > M.
```

## Decision Table

| Official answers | Status |
|---|---|
| Gates 1-5 all yes | Prize-level counterexample candidate. Prepare submission-grade proof. |
| Row yes, predicate yes, sampler balanced/direct, event mass above threshold | Prize-level counterexample candidate. |
| Extension field rejected | Pivot to Goldilocks prime-field fallback or accepted-field compiler. |
| Predicate differs | Build predicate adapter or stop at finite/source theorem. |
| Sampler maps from larger field by identity | Current K-valued line density is likely killed. Need different line or balanced projection. |
| Event filter reduces retained mass to at most threshold | Not an official counterexample under that event contract. |
| Any gate unknown | Status remains finite/source theorem plus official route cut. |

## One-Sentence Ask

```text
Does the official grand MCA challenge accept the row/predicate/sampler exactly
enough that LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092 implies
epsilon_mca(C,125/256) > 2^-128?
```

