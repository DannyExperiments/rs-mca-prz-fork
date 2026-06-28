# Low-Tail Arbitrary-Anchor Skeleton Payment

Status: PROVED local lemma / AUDIT.

This note records a narrow residue-line packing lemma for balanced low-tail
arbitrary-anchor witnesses.  It is not an official prize solve, not a protocol
soundness claim, not an ordinary list-decoding theorem, not a Paper-A
no-slack example, not a proof of full arbitrary-anchor M1, not a proof of
`conj:B`, and not a proof of `conj:final-mca`.  It also does not show that
the quotient reserve or quotient-periodic separation can be ignored.

## 1. Statement

Let `F` be a field, let `H subset F` have `n` distinct points, and let
`E in F[X]` be nonzero on `H` with `deg E = a`.  Let `B in F[X]` have
`deg B < a` and `B != 0`.  Fix `h >= 0` and put `d=a+h`.

Let `w:H -> F` be arbitrary.  Suppose `Gamma` is a set of distinct parameters
`z in F` such that for each `z in Gamma` there are a support
`S_z subset H`, `|S_z|=d`, and a polynomial `R_z in F[X]_<h` satisfying

```text
Q_z = zB + E R_z,
Q_z = w  on S_z.
```

Then

```text
|Gamma| <= binom(n,h+1) / binom(a+h-1,h).
```

Consequently,

```text
|Gamma| <= n/(h+1) * (n/a)^h.
```

If `a >= c n/log n` for fixed `c>0` and
`h=o(log n/log log n)`, then `|Gamma| <= n^{1+o(1)}`.

## 2. Determining Skeletons

Set

```text
V = F B + E F[X]_<h.
```

For `T subset H`, `|T|=h+1`, say that `T` is determining if restriction
`V -> F^T` is injective.

Because `E` is nonzero on `H`, this is equivalent to saying that no
`G in F[X]_<h` satisfies

```text
G(x) = -B(x)/E(x)  for all x in T.
```

Indeed, if `cB+ER` vanishes on `T`, then either `c=0`, in which case
`R` has `h+1` roots and is zero, or `c != 0`, in which case after dividing
by `c` the polynomial `-R/c` agrees with `-B/E` on `T`.

The following elementary lemma is the only combinatorial input.

**Lemma.** Let `S` be a set of `d` distinct field points and let
`phi:S -> F` not be the restriction to `S` of a polynomial of degree `< h`.
Then at least

```text
binom(d-1,h)
```

subsets `T subset S`, `|T|=h+1`, fail to lie on a degree-`<h` graph.

For `h=0`, this says a nonzero function has at least one nonzero point.  For
`h>=1`, one proves the lemma by induction on `(d,h)`.  Fix `p in S`.  If
`phi` restricted to `S\{p}` has degree `<h`, then every `h`-subset
`U subset S\{p}` gives a rejecting set `U union {p}`; otherwise the degree
`<h` interpolant on `U union {p}` would agree with the degree `<h`
interpolant on `S\{p}` at the `h` points of `U` and hence would be the same
polynomial, forcing `phi` to have degree `<h` on all of `S`.

If `phi` restricted to `S\{p}` is still not degree `<h`, induction gives at
least `binom(d-2,h)` rejecting `(h+1)`-subsets not containing `p`.  Also the
divided difference

```text
psi(x) = (phi(x)-phi(p))/(x-p),  x in S\{p},
```

is not degree `<h-1`.  Induction gives at least `binom(d-2,h-1)` rejecting
`h`-subsets `U subset S\{p}` for `psi`, and these are exactly the sets
`U union {p}` rejecting degree `<h` for `phi`.  Pascal's identity gives
`binom(d-1,h)`.

Apply the lemma to

```text
phi(x) = -B(x)/E(x)
```

on each selected support `S_z`.  This function is not degree `<h` on `S_z`:
otherwise `B+EG` would be a nonzero polynomial of degree `<a+h=d` vanishing on
the `d` distinct points of `S_z`, impossible because `deg B<a` and `B != 0`.
Therefore each `S_z` contains at least

```text
binom(d-1,h) = binom(a+h-1,h)
```

determining `(h+1)`-subsets.

## 3. Incidence Count

Count pairs `(z,T)` where `z in Gamma`, `T subset S_z`, `|T|=h+1`, and `T` is
determining.  The lower bound is

```text
|Gamma| binom(a+h-1,h).
```

The upper bound is `binom(n,h+1)`, because a determining `T` can occur for at
most one slope.  If `T subset S_z cap S_z'`, then both `Q_z` and `Q_z'` equal
`w` on `T`, so `Q_z-Q_z' in V` vanishes on `T`.  Since `T` is determining,
`Q_z=Q_z'`.  Reducing modulo `E` gives

```text
(z-z')B = 0 mod E.
```

Since `deg B<a` and `B != 0`, this forces `z=z'`.

Thus

```text
|Gamma| binom(a+h-1,h) <= binom(n,h+1),
```

which proves the claim.

## 4. Corrected-Reserve Consequence

The exact bound gives

```text
|Gamma|
  <= binom(n,h+1) / binom(a+h-1,h)
  <= n/(h+1) * (n/a)^h.
```

If `a >= c n/log n`, this is at most

```text
n/(h+1) * (O_c(log n))^h.
```

For `h=o(log n/log log n)`, the factor `(log n)^h` is `n^{o(1)}`, so

```text
|Gamma| <= n^{1+o(1)}.
```

## 5. Relation To Paper B

The labels `def:residue` and `lem:denom` provide the residue-line witness
language, while `thm:normalform` explains why noncontained residue-line slope
packing is the relevant Paper-B all-line MCA problem.  The proposition
`thm:closure` is only a coordinate normal form and is not used as a packing
estimate.

The result is a skeleton-level strengthening of the `thm:onez` philosophy in
this balanced low-tail stratum: not only can one full support not witness two
noncontained slopes, but one determining `(h+1)`-skeleton cannot be reused by
two distinct parameters.

The warning from `prop:noanchor` remains important.  This lemma does not say
that arbitrary anchors are generally controlled by locator bottom
coefficients.  It pays only the special low-tail cloud in which every selected
witness polynomial belongs to the affine space

```text
F B + E F[X]_<h.
```

The quotient-periodic separation in `rem:aper` is not used.  The conjectural
global packing statements `conj:B` and `conj:final-mca` remain open.

## 6. Remaining Obstruction

This lemma does not cover general Paper-B witnesses of the form
`Q_z=zB+EA_z` with `deg A_z<k`, nor packets where low-tail structure appears
only after comparing pairs of supports.  It also does not address the
medium/wide tail range, where the binomial estimate is no longer enough.

The next bridge target is:

```text
M1-PRIMITIVE-PACKET-TO-LOW-TAIL-CLOUD-OR-WIDE-GRAVER.
```

It should prove that every primitive superlinear residue-line packet either
contains a balanced low-tail cloud paid by this note, enters a charged branch,
or produces a medium/wide signed Cauchy-Pade Graver atom.
