# Cycle 87 Current State

## Executive State

The active wall is no longer the Cycle84 product multiplicity computation. That
finite wall is banked as:

```text
m_max(beta) = 2
Occ(beta) = 52,747,567,092
D = 24
```

Cycle85 transferred that finite model honestly into one-copy shifted `t=1`
RS/MCA coordinates:

```text
L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY
M_C0(6) >= 52,747,567,092
```

The one-copy slope is reciprocal/affine-normalized. It is not the raw product
coordinate.

Cycle86 found a plausible official-scale amplification route: two independent
Role05 color coordinates fused into one RS/GRS MCA line over `F_17^48`.

This is not yet a public proof. The missing object is an explicit separator
certificate.

## Banked Route Cuts

Do not use the naive additive formula as a banked theorem. The surviving
composition is product/reciprocal product:

```text
slope approximately 1 / (rho_beta(T1) * P_T2(y))
```

up to common affine normalization.

Do not use direct tensor/direct-sum amplification as a `t=1` one-line theorem.
That produces multiple color coordinates or a higher-dimensional object unless
the two copies are fused through a genuine one-line RS/GRS construction.

Role 09 in Cycle86 was stale Cycle85 context. It is useful only for one-copy
status and should not be counted as a Cycle86 two-copy worker.

## Candidate Packages

### Padded package

Cycle86 Role 01 proposed:

```text
(n,k,sigma,j) = (560,280,6,274)
```

over `F_17^48`, using two translated blocks plus 48 fixed padding points.

### Shortened package

Cycle86 Role 08 proposed the cleaner package:

```text
(n,k,sigma,j) = (464,232,6,226)
```

obtained by deleting 24 universally unused coordinates from each block.

This should be preferred if the shortening algebra is valid.

## Numerical Frontier

Let

```text
P = 52,747,567,104
N = Occ(beta) = 52,747,567,092
q_line = 17^48
T_line = floor(q_line / 2^128)
       = 338,617,018,271,848,945,628
```

Then

```text
P*N = 2,782,305,834,758,012,141,568 > T_line
N^2 = 2,782,305,834,125,041,336,464 > T_line
```

The margin is about a factor of 8.2.

## Active Exact Wall

```text
L-CYCLE86-EXPLICIT-TWO-COPY-SEPARATOR-CERTIFICATE
```

Prove, with a replayable certificate, that a concrete separator `y` for the
two-copy construction has projective multiplicity at most 8 and that the
resulting supports form one transverse affine syndrome line of a single
official-rate GRS code.

Equivalent checker wall:

```text
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

For `y` in an extension over the Cycle84 base field, define

```text
mu_proj(y) =
  max_kappa #{ T in P0 : [P_T(y)] = kappa in L^x / F0^x }.
```

If

```text
mu_proj(y) <= 8,
```

then the two-copy construction has enough distinct slopes to clear the
official `2^-128` finite target.

## What Counts As Success

A success must give one of:

```text
PROOF:
  explicit field/domain/separator certificate proving the official two-copy
  fail row.

COUNTERPACKET:
  exact flaw in the two-copy route, with the first false implication and,
  where possible, a small model or algebraic counterexample.

BANKABLE_LEMMA:
  a verified component theorem that materially narrows the remaining wall.

ROUTE_CUT:
  a precise reason a tempting subroute cannot prove the result.
```

Broad plans, rate-only claims, or "probably generic" statements are not enough.

