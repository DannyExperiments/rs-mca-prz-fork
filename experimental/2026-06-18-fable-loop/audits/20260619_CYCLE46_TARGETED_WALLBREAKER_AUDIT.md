# Cycle 46 Targeted Wallbreaker Audit

Status: PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT

Raw provenance:

- `raw/cycle46_targeted_wallbreaker_5p5/01_OFFICIAL_DOMAIN_ADMISSIBILITY_AUDITOR.txt`
- `raw/cycle46_targeted_wallbreaker_5p5/02_SMOOTH_DOMAIN_TRANSFER_PROOF_BUILDER.txt`
- `raw/cycle46_targeted_wallbreaker_5p5/03_FROBENIUS_COMPRESSED_LANDING_PROOF_BUILDER_DUPLICATE.txt`
- `raw/cycle46_targeted_wallbreaker_5p5/04_OBSTRUCTION_COUNTERPACKET_HUNTER.txt`
- `raw/cycle46_targeted_wallbreaker_5p5/05_INTERLEAVED_LIST_BRIDGE_AUDITOR.txt`
- `raw/cycle46_targeted_wallbreaker_5p5/06_RESTRICTED_BRANCH_THEOREM_FORMALIZER.txt`

Note: raw outputs 02 and 03 are byte-identical duplicates. They are preserved
separately because they came from two user-provided attachment slots.

## Conservative Verdict

This round is significant and positive. It changes the post-lit route board.

The Cycle 45 audit treated the main post-lit wall as Frobenius compression
from the additive `D=F_p subset F_{p^2}` branch. Cycle 46 points out a simpler
and likely stronger route:

> The pair-rank theorem is domain-free. It can be rerun directly on arbitrary
> smooth multiplicative domains, paying only a subexponential Johnson-shell
> factor.

If source-checked, this gives a scalar smooth-domain MCA counterpacket in the
strict range

```text
c < H_2(rho)
```

for prime-field smooth multiplicative subgroups with `log q=o(n)`.

This is not yet a final Proximity Prize solve. It still needs exact comparison
against the official challenge quantifiers, especially field-size/asymptotic
regime and whether an upper/lower threshold determination is required rather
than a counterexample branch.

## Bankable Lemma Candidate: Domain-Free Pair-Rank

Let `F=F_Q`, let `D subset F` be any set of `n` distinct points, and let
`E in F[X]` have degree `t` and no roots on `D`. For `S=D\T`, define

```text
R_T(w) = [interp_S(w)]_E.
```

For supports `S,S'` of size `a`, let

```text
r = |S\S'| = |T\T'|,
C = S cap S'.
```

Then

```text
Im(R_T,R_T') = { (u,v) in A^2 :
                 u-v in [L_C F[X]_<r]_E },
```

and therefore

```text
rank_F(R_T,R_T') = t + min(t,r).
```

This proof does not use `D=F_p`, additive closure, `X^p-X`, subfield
structure, or symmetric functions. It uses only interpolation on distinct
points and the fact that `[L_C]_E` is a unit because `E` has no roots on `D`.

Classification: `BANKABLE_LEMMA`, pending source-audited writeup.

## Bankable Lemma Candidate: Domain-Uniform Bessel/Shell Moment Bound

For arbitrary `D subset F_Q`, define

```text
N = binom(n,j),
lambda = N / Q^t,
K_r = binom(j,r) binom(a,r),
J = sum_{0 <= r < t} K_r Q^{-r}.
```

For each fixed slope `z`,

```text
Var(nu_w(z)) <= lambda J.
```

Consequently,

```text
E_w sum_z (nu_w(z)-lambda)^2 <= Q lambda J.
```

A deterministic anchor exists with this discrepancy. Missing slopes are
bounded by

```text
Q - N_split <= Q J / lambda.
```

The shell factor satisfies

```text
J <= sum_r (aj/Q)^r/(r!)^2
  <= I_0(2 sqrt(aj/Q))
  <= exp(2 sqrt(aj/Q))
  <= exp(n/sqrt(Q)).
```

In particular, if `Q >= n`, then `J <= exp(sqrt(n)) = 2^{o(n)}`.

Classification: `BANKABLE_LEMMA`, pending source-audited writeup.

## Proof Candidate: Smooth Prime-Field Scalar MCA Counterpacket

Take a smooth multiplicative subgroup

```text
D <= F_p^*
|D| = n = 2^s
```

with `p = poly(n)`, for example by choosing primes `p == 1 mod 2n` along a
Linnik-type arithmetic progression. Then `log p=o(n)`.

Set

```text
k = floor(rho n),
t = floor(c n / log_2 p),
a = k+t,
j = n-a,
Q=p.
```

For `c < H_2(rho)`,

```text
lambda = binom(n,j)/p^t = 2^{(H_2(rho)-c+o(1))n},
```

while

```text
p J = 2^{o(n)}.
```

Thus the all-slope criterion `lambda > pJ` holds for sufficiently large `n`.

Choose a source-valid denominator nonzero on `D`, e.g. `E=X^t` when
`0 notin D`, and `B=1`. For every realized slope the same root-count argument
gives noncontainment. Since `D subset F_p^*` is multiplicative, the exact
normal-form hypothesis is automatic via `X^{n-k}`.

Candidate conclusion:

```text
emca(RS[F_p,D,k], 1-(k+t)/n) = 1
```

for every strict `c < H_2(rho)` along such smooth multiplicative subgroups.

Classification: `PROOF_CANDIDATE`, not yet final. Needs official challenge
quantifier/admissibility alignment and a polished source-audited proof.

## Route Cut

The Cycle 45 wall

```text
W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING
```

is no longer the preferred next scalar-MCA target. It is only needed if the
official challenge forces the quadratic extension ledger

```text
F_p subset F_{p^2}
```

or otherwise disallows prime-field smooth multiplicative subgroups.

The preferred scalar wall is now:

```text
W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT
```

## Interleaved List Side

Cycle 46 contains two list observations:

1. Cycle 45 MCA support counts do not automatically imply large same-radius
   interleaved lists. Noncontainment and the one-bad-parameter-per-support
   theorem block the naive bridge from many MCA slopes to a common-support
   list for `(f,g)`.

2. A direct `m`-anchor zero-residue construction gives a column-distance
   interleaved list lower bound

   ```text
   |Lambda(C^{equiv m}, j/n)|
   >= binom(n,j) Q^{-mt} / shell_m
   ```

   with

   ```text
   shell_m <= exp(2 sqrt(aj/Q^m)).
   ```

   Hence, when `log Q=o(n)` and
   `t=(c+o(1))n/log_2 Q`,

   ```text
   log_2 |Lambda| >= (H_2(rho)-m c+o(1)) n.
   ```

This is a genuine column-distance statement about `C^{equiv m}`, but it may be
the ordinary volume lower bound transported through an explicit construction.
It does not by itself determine the grand list-decoding threshold.

Classification: `BANKABLE_LEMMA / EXACT_NEW_WALL`, pending review.

New list wall:

```text
W-F1-LIST-M-ANCHOR-ZERO-RESIDUE-DISTINCTNESS
```

and, if the goal is a stronger genuinely `m`-dimensional list obstruction:

```text
W-F1-LIST-CORRELATED-COMMON-SUPPORT-RANK-COMPRESSION
```

## What Is Newly Significant

- The restricted additive branch remains solved.
- The scalar smooth-domain MCA branch may be much closer than previously
  thought: the same rank mechanism appears to transfer directly to smooth
  multiplicative subgroups.
- The apparent `H_2(rho)/2` barrier is ledger-dependent, not intrinsic to
  scalar MCA. In the single-field prime-domain ledger, the random-anchor
  threshold is `H_2(rho)`.
- The interleaved list branch now has a concrete direct lower-bound
  construction, though not yet a full challenge solution.

## Remaining Source Checks Before Prize-Level Promotion

1. Does the official grand MCA challenge allow the smooth prime-field subgroup
   family used above?
2. Is the challenge asking only for a counterpacket/failure radius, or for an
   exact determination of `delta_C^*(epsilon*)` requiring matching upper
   bounds?
3. Are the allowed field-size quantifiers compatible with `log q=o(n)` and
   Linnik-produced primes `p=poly(n)`?
4. Does the grand list challenge threshold match the `m`-anchor exponent
   `H_2(rho)-mc`, or is a stronger genuinely interleaved construction needed?
5. Can the domain-uniform moment theorem and smooth-subgroup instantiation be
   written without hidden dependence on excluded monomial/periodic
   denominators?

## Director Recommendation

Do not launch another broad homerun immediately. The next best step is to
formalize and source-audit two theorems:

1. `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT`
2. `W-F1-AA-SMOOTH-PRIME-SUBGROUP-MCA-COUNTERPACKET`

Then compare those two statements literally against the official grand MCA
challenge text. In parallel, ask for/download the two missing instance-4 files
if they contain a formal proof or checker for the domain-uniform transfer or
the `m`-anchor list construction.
