# Checked-Edge Trichotomy For Low-Tail Residue Transitions

Status: PROVED local lemma / AUDIT.

This note records a local Paper-B M1 residue-line lemma.  It is not a prize
solve, does not move or optimize any finite leaderboard row, is not a
Paper-A no-slack example, is not a protocol soundness claim, does not prove
`conj:B`, and does not pay nonzero Cech holonomy in general.  Its purpose is
to separate three elementary outcomes for selected low-tail transition
equations: fiberwise zero holonomy, a single-edge local obstruction, or
private denominator-skeleton payment.

## 1. Statement

Let `F` be a field and let `X subset F` be a finite set of distinct points.
Let `E in F[X]` be nonzero on `X`, with `deg E=a`, and let `B in F[X]`
satisfy

```text
B != 0,        deg B < a.
```

Put

```text
f = B/E on X,        P_h = F[X]_<h,
```

with the convention `P_0={0}`.  Let `Gamma` be a finite set of retained
indices with pairwise distinct slope parameters `z_i`, and let
`S_i subset X` be post-puncture supports.

For `U subset X`, `|U|=h+1`, set

```text
L_U(T) = prod_{u in U} (T-u),
partial_U(f) = sum_{u in U} f(u)/L_U'(u).
```

Call `U` denominator-determining if `partial_U(f) != 0`, equivalently if
`f|_U` does not agree with any polynomial in `P_h`.  Define

```text
D_h(S) = #{ U subset S : |U|=h+1 and partial_U(f) != 0 }.
```

Let `G` be a checked-edge graph on `Gamma`.  Suppose there exist
`R_i in P_h` such that, for every checked edge `ij in G`,

```text
R_i - R_j = (z_j-z_i) f on all of S_i cap S_j.
```

Then the following three alternatives give the local decision tree.

### A. Fiberwise Saturation

For `x in X`, let

```text
Gamma_x = { i in Gamma : x in S_i }.
```

Let `G_x` be the graph on `Gamma_x` induced by checked edges whose overlap
contains `x`.  If every `G_x` is connected, then complete pairwise punctured
zero holonomy holds:

```text
R_i - R_j = (z_j-z_i) f on S_i cap S_j
```

for every retained pair `i,j`.

Consequently, the zero-holonomy reanchoring payment applies to any retained
subpacket satisfying the required post-puncture reserve or skeleton condition.

### B. Shared Determining Missing-Edge Atom

If a missing retained pair `ij notin G` contains a denominator-determining
set

```text
U subset S_i cap S_j,       |U|=h+1,
```

then

```text
partial_U((z_j-z_i)f) = (z_j-z_i) partial_U(f) != 0.
```

Thus no polynomial in `P_h` can equal `(z_j-z_i)f` on `U`.  The missing
edge carries a genuine single-edge Cech-Pade/local-unit obstruction.  This is
an atomization statement, not a many-slope payment.

### C. Private Denominator-Skeleton Payment

If no missing retained pair contains a denominator-determining `(h+1)`-set in
its overlap, then every denominator-determining `(h+1)`-set is contained in
at most one retained support.  Hence

```text
sum_i D_h(S_i) <= binom(|X|,h+1).
```

In particular, if

```text
D_h(S_i) >= b_h
```

for every retained `i`, then

```text
|Gamma| b_h <= binom(|X|,h+1).
```

The crude post-puncture reserve condition

```text
|S_i| >= a+h
```

implies the intrinsic lower bound

```text
D_h(S_i) >= binom(|S_i|-1,h) >= binom(a+h-1,h),
```

and therefore gives

```text
|Gamma| <= binom(|X|,h+1) / binom(a+h-1,h).
```

All support and reserve hypotheses in this statement are post-puncture:
typically `X=H\W` and `S_i=T_i\W`.

## 2. Proof

For `|U|=h+1`, the Lagrange interpolation polynomial of a word
`phi:U -> F` has `T^h` coefficient

```text
partial_U(phi) = sum_{u in U} phi(u)/L_U'(u).
```

Thus `partial_U(P)=0` for every `P in P_h`, and
`partial_U(f) != 0` is exactly the assertion that `f|_U` is not degree
`<h`.  For `h=0`, this says that a singleton `{u}` is determining exactly
when `f(u) != 0`.

For the fiberwise branch, fix `x in S_i cap S_j`.  Since `i,j in Gamma_x`,
a path

```text
i=v_0, v_1, ..., v_m=j
```

inside `G_x` gives

```text
R_{v_l}(x)-R_{v_{l+1}}(x)
  = (z_{v_{l+1}}-z_{v_l}) f(x)
```

on every edge of the path.  Telescoping gives

```text
R_i(x)-R_j(x) = (z_j-z_i)f(x).
```

Since this holds for every shared point `x`, complete pairwise zero holonomy
follows.

For the single-edge atom branch, if `U subset S_i cap S_j` is
denominator-determining and `ij` is missing, then

```text
partial_U((z_j-z_i)f)=(z_j-z_i)partial_U(f).
```

The slopes are distinct, so the right side is nonzero.  Hence no element of
`P_h` can fill the transition on `U`.

For the private skeleton branch, suppose a denominator-determining `U` lies in
`S_i cap S_j` for `i != j`.  If `ij` is a missing pair, this contradicts the
branch hypothesis.  If `ij` is checked, then on `U`

```text
R_i - R_j = (z_j-z_i)f.
```

As `R_i-R_j in P_h` and `z_j-z_i != 0`, this makes `f|_U` degree `<h`,
contradicting that `U` is denominator-determining.  Therefore each
determining skeleton is counted by at most one support, proving

```text
sum_i D_h(S_i) <= binom(|X|,h+1).
```

It remains to justify the crude reserve corollary.  Let `Y subset X` with
`|Y|>=a+h`.  If `f` agreed on `Y` with some `G in P_h`, then

```text
B - E G
```

would vanish on at least `a+h` distinct points while having degree `<a+h`.
Thus `B-EG` would be identically zero.  This is impossible: if `G=0`, then
`B=0`; if `G != 0`, then `deg(EG)>=a>deg B`.  Hence `f|_Y` is not degree
`<h`.

The elementary determining-skeleton lemma says that if a word on `Y` is not
degree `<h`, then at least

```text
binom(|Y|-1,h)
```

of its `(h+1)`-subsets reject degree `<h`.  This gives the displayed lower
bound for `D_h(S_i)`.

## 3. Contact-Shadow Complement

For later use, record the exact complement of denominator-determining
overlaps.  If `I subset X`, then `I` contains no denominator-determining
`(h+1)`-subset if and only if there exists `G in P_h` with

```text
I subset Z_G,       Z_G = { x in X : E(x)G(x)=B(x) }.
```

Indeed, if such `G` exists, then `f` is degree `<h` on every
`(h+1)`-subset of `I`.  Conversely, if every `(h+1)`-subset of `I` has zero
`h`-th divided difference, then `f|_I` is represented by a polynomial in
`P_h` by interpolation, trivially when `|I|<=h` and by the vanishing of all
`h`-th divided differences otherwise.

Each fixed shadow has size at most `a+h-1`.  Otherwise `EG-B`, a nonzero
polynomial of degree `<a+h`, would have at least `a+h` roots.  It cannot be
identically zero because `B != 0` and `deg B<a=deg E`.

This localization is structural, not a payment theorem when the labels `G`
move from edge to edge.

## 4. Relation To Paper B

The labels `def:residue` and `lem:denom` provide the residue-line datum and
legitimize the rational word `B/E` on the active domain.  The label
`thm:normalform` explains why this local residue-line statement is relevant to
the all-line MCA problem.  The label `thm:closure` is branch discipline, not a
counting input.

The warning from `prop:noanchor` is respected.  This lemma does not discard an
anchor without proof.  In the fiberwise-saturated branch, complete pairwise
zero holonomy gives an actual synthetic anchor and then the already banked
zero-holonomy reanchoring theorem applies.  In the private branch, the payment
is a direct skeleton incidence count.  In the missing-edge branch, the result
is only an atom.

The quotient/phase, subfield, tangent, contained, fixed-pencil, same-slope,
and support-degenerate branches remain part of the global Paper-B ledger.
This lemma does not prove they are absent.

## 5. Remaining Wall

The lemma does not prove that nonzero Cech holonomy is paid.  It does not
prove that a local-unit atom pays many slopes.  A fixed determining skeleton
can be reused by many slopes, and a transition obstruction may be coefficiented
or split across several overlaps rather than supported on one missing edge.

The next local target is:

```text
M1-VERTEX-BOUNDARY-SPLIT-UNIT-EXTRACTION.
```

The next wall after that is:

```text
M1-PRIMITIVE-TRANSITION-GRAVER-ATOM-PAYMENT-OR-CONTACT-SHADOW-WALL.
```

That wall asks for a payment or classification of primitive transition
obstructions

```text
lambda in ker(d_h^*),       lambda(tau) != 0,
tau_ij=(z_j-z_i)B/E,
```

after the fiberwise zero-holonomy branch, private skeleton branch, and
single-edge local-unit branch have been separated.
