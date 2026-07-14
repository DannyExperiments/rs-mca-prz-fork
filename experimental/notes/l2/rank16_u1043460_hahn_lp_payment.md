# Exact constant-weight Hahn LP payment at `u=1,043,460`

## Verdict

`PROVED EXACT-STATE ELIMINATION, UNIFORM IN AFFINE RANK.`

The new first unpaid high-rank state is actually target-safe.  The ordinary
spherical seventh Levenshtein bound supplied for this state is

```text
2,128,724,737,686,483,246 > T,
```

but it loses the integrality and constant-weight geometry of the selected
agreement supports.  In the exact Johnson association scheme, a degree-five
normalized Hahn Delsarte polynomial gives

```text
L_Hahn(1,043,460)
 <=41,358,983,685,320,209
 <274,854,110,496,187,592=T.                             (1)
```

The improvement is by more than a factor of six relative to the target and
more than a factor of fifty relative to the spherical `L7` calibration.  No
line cap, two-flat cap, affine-rank assumption, locator classification, or
recurrence input is used.

This note proves only the exact state `u=1,043,460`.  Existing higher-state
payments are separate imported results and are not reproved here.  With those
board entries retained, the next unresolved all-rank state is `u=1,043,459`.

## Source and ownership

The source reduction is the selected-support argument in
`experimental/notes/l2/affine_section_one_row_rank_reduction.md`, evaluated at
the deployed one-row parameters.  This packet is based on `origin/main` commit
`9262f63cf093a7510a2df435f220390f59e2bcd5`; it does not consume a pending PR.
The challenge-field denominator remains `p^6`, while this one-row support
calculation is over the base-field row exactly as in the source reduction.

## 1. Exact constant-weight code

Remove the actual universal agreement set `Z`, `|Z|=u`, and choose exactly
`m` agreements containing `Z` for every listed polynomial.  At `u=1,043,460`
the selected residual supports form an injective constant-weight code with

```text
N=n-u       =1,053,692,
a=m-u       =72,587,
h=K-u-1     =5,115,
d=a-h       =67,472.                                    (3)
```

Here Johnson distance is `i=a-|A intersection B|`, so every distinct pair has

```text
d<=i<=a.                                                 (4)
```

Injectivity is exact: two candidates with the same selected `m`-support would
have a nonzero degree-`<K` difference with at least `m>K-1` roots.

## 2. Exact Hahn normalization

For `0<=j<=a`, define the normalized Johnson-scheme zonal function

```text
H_j(i)=sum_(t=0)^j (-1)^t
       binom(j,t) binom(N+1-j,t) binom(i,t)
       /[binom(a,t) binom(N-a,t)].                       (5)
```

This is the normalized dual Hahn/Eberlein function with

```text
H_j(0)=1.                                                (6)
```

For every family of `a`-subsets, the matrix
`[H_j(dist(A,B))]_(A,B)` is positive semidefinite: it is the primitive
Johnson idempotent of degree `j`, divided by its diagonal value.  Consequently
the standard Delsarte dual statement applies:

> If `F(i)=f_0+sum_(j>=1) f_j H_j(i)`, with `f_0>0`, every `f_j>=0`, and
> `F(i)<=0` for every allowed nonzero code distance, then
> `|C|<=F(0)/f_0`.

## 3. Literal degree-five certificate

Put `f_0=1`.  The five positive coefficients `f_1,...,f_5` are the unique
exact rational solution of

```text
1+sum_(j=1)^5 f_j H_j(i)=0                               (7)
```

at

```text
i=67,472,
  67,586, 67,587,
  67,700, 67,701.                                        (8)
```

For scale, their decimal values are

```text
f_1 =2.249209138766... *10^5,
f_2 =2.078717027087... *10^8,
f_3 =2.775619448268... *10^11,
f_4 =7.354480610853... *10^13,
f_5 =4.128516110917... *10^16.                            (9)
```

The verifier solves (7) in exact `Rational` arithmetic; no decimal value in
(9) is used.

The resulting `F` has degree five in `i` and exactly the roots (8).  Its
leading coefficient is negative.  The last four roots occur as adjacent
integer pairs.  Hence every allowed integer distance in (4) lies in a
nonpositive sign interval: the positive real intervals between `67,586` and
`67,587`, and between `67,700` and `67,701`, contain no integer.  The verifier
also evaluates `F(i)` exactly at all

```text
a-d+1=5,116
```

allowed integer distances and finds no positive value.

All nonconstant Hahn coefficients are positive, so Delsarte gives

```text
|C|<=F(0)=1+sum_(j=1)^5 f_j,
floor F(0)=41,358,983,685,320,209,                       (10)
```

proving (1).

## 4. Line/two-flat composition

The line ceiling `15` and two-flat ceiling `213` are not needed.  Equation
(10) bounds the **entire selected-support family** before any decomposition
into affine lines or planes.  Composing those local caps with (10) would only
weaken the proof interface by introducing owner multiplicities; it cannot be
needed to reach the target at this state.

This also means the theorem is uniform in affine rank.  It pays rank 16,
every rank at least 17, and all lower ranks at `u=1,043,460` in one step.

## Nonclaims

- No state below `u=1,043,460` is paid here.
- The supplied spherical `L7` number is used only for comparison; the exact
  Hahn certificate is independently reconstructed.
- No claim is made that degree five is the globally optimal full Hahn LP.
- This exact-state payment does not prove the base one-row target uniformly in
  `u`, the official Grand List theorem, or either official prize question.

## Replay

```text
ruby --disable-gems -w experimental/scripts/verify_rank16_u1043460_hahn_lp_payment.rb
```

The canonical output is frozen at
`experimental/data/certificates/rank16-u1043460-hahn-lp-payment/verifier_output.txt`.
