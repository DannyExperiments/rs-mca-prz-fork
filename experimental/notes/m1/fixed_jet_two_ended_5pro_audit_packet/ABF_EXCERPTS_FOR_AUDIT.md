# ABF Excerpts For Definition Audit

Source under discussion:

```text
Open Problems in List Decoding and Correlated Agreement
Gal Arnon, Dan Boneh, Giacomo Fenzi
IACR ePrint 2026/680
```

This file records the relevant interpretation being audited. The ABF-definition
auditor should verify these against the supplied PDF or reject the consequence
at the first mismatch.

## Grand MCA Challenge As Currently Read

The grand MCA challenge gives a Reed-Solomon code

```text
C = RS[F,L,k]
```

over a smooth evaluation domain `L subset F`, with constant rate in

```text
{1/2, 1/4, 1/8, 1/16}.
```

For the target

```text
epsilon* = 2^-128,
```

it asks for the largest `delta*_C` such that

```text
epsilon_mca(C, delta*_C) <= epsilon*.
```

## Smooth Domain Interpretation Being Audited

The current reading is that a smooth evaluation domain is a multiplicative
coset of a subgroup of `F^*` whose order is a power of two.

The row under audit uses:

```text
K = F_17^32,
H = <theta> subset K^*,
|H| = 512 = 2^9.
```

## MCA Definition Being Audited

The current reading of ABF Definition 4.3 is:

```text
epsilon_mca(C,delta)
 =
 max_{f1,f2}
 Pr_{gamma <- F}[there exists S subset [n] such that
   |S| >= (1-delta)n,
   f1 + gamma f2 is code-explained on S,
   (f1,f2) is not simultaneously code-explained on S].
```

The sampling notation `gamma <- F` is read as uniform sampling from `F`.

The support threshold is read as closed:

```text
|S| >= (1-delta)n.
```

No separate `q_chal`, endpoint deletion, quotienting, charge registry, or
event filter has been found in the printed grand MCA definition.

## Arithmetic Being Audited

For the row:

```text
n = 512,
k = 256,
delta = 125/256,
```

the closed support threshold is:

```text
(1-delta)n = (131/256)512 = 262.
```

The field-size comparison is:

```text
17^32 = 2367911594760467245844106297320951247361,
floor(17^32 / 2^128) = 6,
52,747,567,092 > 6.
```

Therefore the claimed ABF consequence is:

```text
epsilon_mca(RS[F_17^32,H,256],125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```
