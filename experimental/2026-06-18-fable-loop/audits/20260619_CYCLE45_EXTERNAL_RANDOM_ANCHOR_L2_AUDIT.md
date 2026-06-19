# Cycle 45 External Random-Anchor L2 Audit

Status: PROOF / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL

Target:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

External provenance:

- `raw/cycle45_external_random_anchor_l2/20260619_CYCLE45_RANDOM_ANCHOR_L2_CERTIFICATE.md`
- `raw/cycle45_external_random_anchor_l2/cycle45_random_anchor_reserve_lift_certificate.md`
- `raw/cycle45_external_random_anchor_l2/20260619_cycle45_moment_formula_checker.py`
- `raw/cycle45_external_random_anchor_l2/20260619_cycle45_moment_formula_checker_sample.txt`
- The user also pasted additional external answers in chat. Those are used
  only as corroborating audit evidence here; the four files above are the
  local raw artifacts preserved and hashed.

Local check:

- The checker is pure standard-library Python and implements the exact
  Johnson-distance second-moment formula; it does not enumerate anchors.
- `python3 -m py_compile` passed.
- Running the sample command
  `python3 .../20260619_cycle45_moment_formula_checker.py 31 2 4`
  reproduced the provided sample values, including
  `lambda_float=0.03407069249102078`,
  `Var_nu_float=0.0378956356452929`, and
  `variance_bound_pass_using_Cstar_lt_2=True`.

## Verdict

The Cycle 45 external round appears mathematically significant. It cuts the
literal uniform-in-anchor L2 wall, but it also closes the existential
random-anchor version of the reserve lift in the restricted additive
`D=F_p`, `F=F_{p^2}` residue-line branch.

This is not a full Proximity Prize solve. The result remains below the final
generated-field / smooth-domain target, and the proof uses the load-bearing
separation

```text
q_gen = p,      q_line = p^2.
```

The conservative bankable statement is:

> In the restricted full-base-domain residue-line branch with
> `B=F_p`, `F=F_{p^2}`, `D=F_p`, `q_line=p^2`, and balanced support
> `a=k+t`, there exist source-valid anchors satisfying the Cycle 44
> landing main term and L2 anticollision estimate whenever
> `binom(p,j)/p^(2t) -> infinity`. In the strict entropy range
> `t=(C+o(1))p/log_2 p`, `C < H_2(rho)/2`, this gives
> `(1-o(1))p^2` slopes, and under the stronger finite gap
> `binom(p,j)/p^(2t) >> p^2` it gives all `p^2` slopes for large `p`.

## Audit Corrections

1. The Cycle 44 falsifier threshold was misstated.

   A single fiber of size `#Land/p^(1+eps)` is smaller than the allowed RMS
   scale `#Land/p`, since `q_line=p^2`. A one-fiber L2 falsifier needs
   `max_z nu(z) >> #Land/p`, for example
   `max_z nu(z) >= #Land/p^(1-eps)`, or else a direct second-moment or
   small-image collapse.

2. The correct quantifier for the packing maximum is existential in the
   source datum, especially the anchor `w`.

   A bad source-valid anchor disproves only a theorem uniform in `w`; it does
   not disprove the reserve lift.

3. Slope uniqueness requires `b=[B_num]_E != 0`.

   The old condition `[W]_E notin F b` is not the slope-uniqueness condition.
   It may be useful for excluding one resonance locus, but sparse-anchor
   concentration persists off that locus.

4. If a character-sum formulation is used with non-squarefree `E`, the
   algebra trace pairing may be degenerate.

   Use either a squarefree denominator family or a fixed nondegenerate
   additive `F_p`-bilinear pairing on the vector space `A`.

## Route Cut

The universal fixed-anchor route is false:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

if interpreted as "all source-valid anchors satisfy L2 anticollision."

The zero anchor gives `I_S=0` for every support, so all cosupports land at one
slope:

```text
N_split = 1,
M_2 = binom(p,j)^2.
```

One-spike and sparse-anchor variants give the same obstruction even off the
old `[W]_E in F b` resonance locus. The mechanism is duplicate-support
clustering: many different `a`-subsets can encode the same witness polynomial.

This route cut does not harm the packing problem, because the packing maximum
only needs one good source-valid datum.

## Bankable Lemma

Let `Q=p^2`, `A=F[X]/E`, `dim_F A=t`, `D=F_p`, and let
`S=D\T`, `S'=D\T'` have size `a`. Put

```text
r = |S \ S'| = |T \ T'|,
C = S cap S'.
```

For

```text
R_T(w) = [interp_S(w)]_E,
```

the joint image of

```text
w |-> (R_T(w), R_T'(w))
```

is exactly

```text
{ (u,v) in A^2 : u-v in [L_C F[X]_<r]_E }.
```

Since `E` has no roots in `D`, `[L_C]_E` is a unit, so

```text
dim_F [L_C F[X]_<r]_E = min(t,r)
```

and therefore

```text
rank_F(R_T, R_T') = t + min(t,r).
```

Equivalently, residues attached to supports separated by at least `t`
exchanges are exactly independent for a uniformly random anchor.

This rank identity is the missing incidence lemma below the Cycle 44
symmetric-function formulation.

## Proof Skeleton

Choose `w` uniformly from `F^D`. Fix `0 != b=[B_num]_E` and define

```text
nu_w(z) = #{T : R_T(w) = z b},
N = binom(p,j),
lambda = N / Q^t.
```

For each fixed slope `z`,

```text
E nu_w(z) = lambda.
```

For fixed `T`, the number of `T'` at exchange distance `r` is

```text
K_r = binom(j,r) binom(a,r).
```

The pair-rank lemma gives

```text
Pr(R_T(w)=z b, R_T'(w)=z b) = Q^(-t-min(t,r)).
```

Since `a+j=p`, one has

```text
ja <= p^2/4 = Q/4,
K_r Q^(-r) <= 4^(-r)/(r!)^2.
```

Thus

```text
Var(nu_w(z)) <= C_* lambda
```

for an absolute `C_* < e^(1/4)` up to the harmless convention about whether
the `r=0` term is included.

Summing over all `Q` slopes gives a total discrepancy

```text
Phi(w) = sum_z (nu_w(z)-lambda)^2
```

with

```text
E Phi(w) <= C_* Q lambda.
```

Therefore some deterministic anchor satisfies this bound. For that anchor,
if `L=sum_z nu(z)` and `M_2=sum_z nu(z)^2`, then Cauchy-Schwarz gives

```text
L = Q lambda (1 + O(lambda^(-1/2))),
M_2 <= (1+o(1)) L^2/Q
```

whenever `lambda -> infinity`.

This is stronger than the Cycle 44 target

```text
M_2 <= L + (1+o(1)) L^2/q_line.
```

It also gives

```text
N_split >= L^2/M_2 = (1-o(1))Q.
```

If `lambda > C_* Q`, every slope occurs, because a missing slope contributes
`lambda^2` to `Phi(w)`.

## Source-Valid Reserve Family

Take a rate `0<rho<1`, and set

```text
k = floor(rho p),
t = floor(C p/log_2 p),
a = k+t,
j = p-a.
```

Then

```text
log_2 lambda = (H_2(rho)-2C+o(1))p.
```

If `C < H_2(rho)/2`, then `lambda` grows exponentially, and in fact
`lambda/Q -> infinity`; hence all `p^2` slopes occur for sufficiently large
`p` under the deterministic-good-anchor selection.

For final source hygiene, prefer an aperiodic separated denominator such as

```text
E_p(X) = X^t + alpha X + 1
```

with `alpha in F_{p^2}\F_p`, or a squarefree variant with finitely many bad
`alpha` excluded, rather than relying only on the pure monomial
`X^t-alpha`. The monomial family is useful for the rank proof but may be too
special if quotient-periodic exclusions are in force.

For every landing support `S`, the interpolant `Q_z=I_S` satisfies

```text
deg Q_z < a = k+t,
Q_z == z B_num mod E,
Q_z = w on S.
```

Noncontainment is automatic when `B_num != 0`: if a degree `<k` polynomial
`G` agreed with `-B_num/E` on `|S|=k+t` points, then `E G+B_num` would have
`k+t` roots and degree `<k+t`, forcing `E | B_num`, impossible because
`deg B_num < deg E` and `B_num != 0`.

## What This Does Not Prove

This audit does not promote a generated-field theorem, smooth multiplicative
domain theorem, corrected-reserve sufficiency theorem, list-decoding theorem,
protocol/SNARK statement, or Proximity Prize solve.

The load-bearing limitation is:

```text
D = F_p generates B = F_p, not F = F_{p^2}.
```

The proof also uses `q_line=p^2` in the local-pair estimate
`ja/q_line <= 1/4`. Replacing `q_line` by `q_gen=p` destroys the constant
series bound.

## Exact New Wall

For the restricted additive residue-line branch, no further L2 cancellation
lemma is missing. The next full-problem wall is a transfer/compression wall:

```text
W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING
```

Target form:

Construct source-valid `E,b,w` and a `B`-linear subspace

```text
U subset A,
dim_B U = t+1,
F b subset U,
```

such that almost all cosupport residues land in `U` and are balanced inside
`U`. This would reduce the codimension from `2(t-1)` `B`-dimensions to
`t-1`, moving the entropy threshold from

```text
C < H_2(rho)/2
```

to the generated-field scale

```text
C < H_2(rho).
```

This new wall is not yet solved. It is the cleanest next theorem-sized target
if the aim is the full prize statement rather than the restricted branch.

## Confidence

- Cycle 44 identity and sign: high.
- Pair-rank lemma: high.
- Existential random-anchor L2 theorem in the restricted additive branch:
  high, pending independent human review of the source definitions.
- All-slope conclusion in the strict entropy interior: moderate-high to high;
  the asymptotic gap gives the needed `lambda/Q -> infinity`.
- Promotion to the full Proximity Prize problem: not justified.
