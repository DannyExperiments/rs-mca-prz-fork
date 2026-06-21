# COMMON PROMPT FOR CYCLE 86

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

You are working on the RS-MCA / proximity-prize finite obstruction route. Do
not brainstorm from scratch. Use the attached Cycle84/Cycle85 context and the
Cycle85 synthesis.

## Banked Context

Cycle84 public replay closed the finite seven-slot model:

```text
m_max(beta) = 2
Occ(beta) = 52,747,567,092
D = 24
```

Cycle85 established the honest one-copy transfer:

```text
L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY
```

For the explicit Role05 packet over

```text
F0 = F_17[X] / (X^16 + X^8 + 3)
```

with

```text
n = 256
k = 137
sigma = 6
j = 113
```

there is a shifted `t=1` RS/GRS MCA syndrome line with at least

```text
M_C(6) >= 52,747,567,092
```

distinct transverse bad slopes.

The slope coordinate is reciprocal/affine normalized:

```text
chi_T = a + b / rho_beta(T),  b != 0
```

or in one gauge:

```text
chi_T = -rho_beta(T)^(-1).
```

There is no extra multiplicity loss because the packet has fixed exact
`Delta = 6[infinity]` jet, equivalently `gamma_T = 1`.

## What Cycle85 Cut

The one-copy packet is not an official prize-frontier counterpacket.

Native field:

```text
q_line = 17^16
floor(q_line / 2^128) = 0
```

Allowed compatible line-field extensions under `q_line < 2^256`:

```text
17^16 -> target 0
17^32 -> target 6
17^48 -> target 338,617,018,271,848,945,628
```

The single-copy packet is redundant at `17^16`/`17^32` and too small at
`17^48`. Naive Cartesian tensoring is also cut: it creates separate colors or
a non-RS object unless one proves a single RS-compatible affine syndrome line.

## Active Cycle86 Wall

The active wall is:

```text
W-CYCLE86-TWO-COPY-F17^48-AFFINE-COLOR-SEPARATION
```

Let

```text
Omega = {rho_beta(T) : T in P0} subset F0
|Omega| = N = 52,747,567,092.
```

Arithmetic:

```text
N^2 = 2,782,305,834,125,041,336,464
floor(N^2 / 8) = 347,788,229,265,630,167,058
floor(17^48 / 2^128) = 338,617,018,271,848,945,628
```

So if a two-copy RS-compatible construction gives even `N^2/8` distinct slopes
over `F_17^48`, it clears the native `2^-128` target.

## Desired Theorem Shape

Prove, materialize, or kill a theorem of the following kind:

```text
L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION
```

Over

```text
L = F_17^48,
```

choose `alpha in L \ F0` and construct one official-rate `t=1` RS/GRS MCA
instance and one support map

```text
Psi: P0 x P0 -> binom(D^(2), j^(2))
```

such that, after one common affine normalization,

```text
z_{Psi(T1,T2)} = rho_beta(T1) + alpha rho_beta(T2).
```

Then `1, alpha` being `F0`-linearly independent makes the slope map injective
on `Omega^2`.

You may also prove a multiplicative/product variant if it is genuinely one
RS-compatible `t=1` line and has max pair-product multiplicity at most 8.

## Non-Negotiable Checks

You must distinguish:

```text
finite/model certificate
official prize counterpacket
MCA numerator lower certificate
scalar-list numerator
q_gen / q_line / q_code / q_chal
T_line = floor(q_line / 2^128)
```

Do not claim a prize-level result unless all profile, field, reserve, domain,
code, transversality, and one-line hypotheses are explicit.

The construction must be one MCA affine syndrome line for one RS/GRS code. A
direct product of two unrelated lines is not enough.

## Output Rules

Start with one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. executive verdict and confidence;
2. exact theorem/counterpacket/checker statement;
3. proof or construction;
4. verification requirements;
5. next exact lemma or construction.

Before finalizing, do a self-audit:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
