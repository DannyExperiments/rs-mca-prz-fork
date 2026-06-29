# Zero-Holonomy Reanchoring Payment

Status: PROVED local lemma / REPAIR / AUDIT.

This note records a repaired local payment for one Paper-B M1 residue-line
branch.  It is not a prize solve, does not move or optimize any finite
leaderboard row, is not a Paper-A no-slack example, is not a protocol
soundness claim, does not prove full `conj:B`, and is not a reason to ignore
quotient, subfield, tangent, contained, or support-degenerate branches.  It
does not handle nonzero Cech holonomy, incomplete overlap saturation, or
post-puncture reserve loss.

## 1. Statement

Let `F` be a field and let `H subset F` be a finite set of `n` distinct
points.  Let `E in F[X]` be nonzero on `H`, with `deg E=a`, and let
`B in F[X]` satisfy `B != 0` and `deg B<a`.

Let `Gamma` be a finite set of distinct retained slope parameters `z_i`.  For
each `i`, suppose there are a support `T_i subset H` and a Paper-B
residue-line witness

```text
Q_i = z_i B + E A_i,   A_i in F[X]_<k,
Q_i = w on T_i.
```

Fix a puncture set `W subset H`, put

```text
H_W = H \ W,       S_i = T_i \ W,
```

and fix `h <= k`.  Assume there are polynomials `R_i in F[X]_<h` satisfying
complete pairwise punctured zero holonomy:

```text
R_i - R_j = (z_j-z_i) B/E on S_i cap S_j
```

for every retained pair `i,j`.  Then the values

```text
u(x) = z_i B(x) + E(x) R_i(x),   x in S_i,
```

glue to a well-defined word on `union_i S_i`, and hence extend arbitrarily to
a word `u:H_W -> F`.  Thus the same slopes form a low-tail arbitrary-anchor
packet

```text
z_i B + E R_i = u on S_i,       R_i in F[X]_<h.
```

If, in addition, every retained punctured support has reserve

```text
|S_i| >= a+h,
```

then

```text
sum_i binom(|S_i|-1,h) <= binom(|H_W|,h+1),
```

and in particular

```text
|Gamma| <= binom(|H_W|,h+1) / binom(a+h-1,h).
```

Consequently, if `a >= c n/log n` for fixed `c>0` and
`h=o(log n/log log n)`, this branch contributes at most `n^{1+o(1)}` slopes.

## 2. Proof

For `x in S_i cap S_j`,

```text
(z_iB+ER_i)(x) - (z_jB+ER_j)(x)
  = (z_i-z_j)B(x) + E(x)(R_i(x)-R_j(x)).
```

By complete punctured zero holonomy, the second term is
`(z_j-z_i)B(x)`, so the difference is zero.  Thus the displayed formula for
`u` is independent of the chosen support containing `x`.

After extending `u` arbitrarily to all of `H_W`, each retained slope satisfies

```text
z_iB + ER_i = u on S_i.
```

It remains to count low-tail skeletons.  Call an `(h+1)`-subset
`U subset H_W` denominator-determining if no polynomial `G in F[X]_<h`
agrees with `-B/E` on `U`; equivalently, the restriction map

```text
F B + E F[X]_<h -> F^U
```

is injective.

If `|S_i|>=a+h`, then `-B/E` is not degree `<h` on `S_i`.  Otherwise
`B+EG` would vanish on at least `a+h` distinct points for some
`G in F[X]_<h`, while `deg(B+EG)<a+h`; the polynomial would be identically
zero, impossible because `B != 0`, `deg B<a=deg E`, and hence `E` cannot
divide `B`.

The determining-skeleton lemma from the low-tail arbitrary-anchor payment
then gives at least

```text
binom(|S_i|-1,h)
```

denominator-determining `(h+1)`-subsets inside `S_i`.

No denominator-determining skeleton is contained in two distinct retained
supports.  If `U subset S_i cap S_j`, then the two low-tail witnesses are both
equal to `u` on `U`, so

```text
(z_i-z_j)B + E(R_i-R_j)
```

vanishes on `U`.  Since `U` is denominator-determining, this element of
`F B + E F[X]_<h` is the zero polynomial.  Reducing modulo `E` gives

```text
(z_i-z_j)B == 0 mod E.
```

As `deg B<a=deg E` and `B != 0`, this forces `z_i=z_j`.  The retained slopes
are distinct, so `i=j`.

Counting denominator-determining skeletons gives

```text
sum_i binom(|S_i|-1,h) <= binom(|H_W|,h+1).
```

The cardinal bound follows from `|S_i|>=a+h`.

## 3. Why The Reserve Is Post-Puncture

The hypothesis is not merely that the original support `T_i` is large.  It is
the punctured support

```text
S_i = T_i \ W
```

that must satisfy `|S_i|>=a+h`.

Without this, the weighted skeleton count is false.  Small punctured supports
can make `B/E` look like a polynomial of degree `<h`, so the support
contributes no denominator-determining skeletons even though the synthetic
anchor glues.  The hostile audit produced explicit finite examples of this
failure.  Those examples do not contradict the theorem above, because they
violate post-puncture reserve.

## 4. Why Complete Overlap Holonomy Is Needed

The displayed reanchored word `u` is a genuine word only if the low-tail
expressions agree at every point shared by retained supports.  Thus the
theorem assumes complete pairwise punctured zero holonomy on all overlaps
`S_i cap S_j`.

Graph-level holonomy on a selected set of overlaps is not enough unless it is
fiberwise saturated: for each point `x`, the graph on slopes whose supports
contain `x` must connect all such slopes through edges whose holonomy equation
holds at `x`.  Without this saturation, the local expressions may disagree at
an unchecked shared point, so no synthetic anchor word exists.

For a purely numerical skeleton-count variant, one can replace literal gluing
by the weaker condition that every shared denominator-determining
`(h+1)`-skeleton is saturated.  That variant is not the arbitrary-anchor
reanchoring theorem recorded here.

## 5. Relation To Paper B

The labels `def:residue` and `lem:denom` provide the residue-line datum and
legitimize the word `B/E` on `H`.  The label `thm:normalform` is the ambient
reason this local packing branch is relevant to all-line MCA.  The label
`thm:closure` is used only as branch discipline, not as a counting estimate.

The warning from `prop:noanchor` is respected.  The theorem does not assert
that the synthetic anchor has the special form `w-EC` for a global
`C in F[X]_<k`.  Failed absolute absorption says exactly that this special
form may not exist.  The point of the theorem is that the banked low-tail
arbitrary-anchor payment is uniform in the anchor word, so failed absorption is
not a slope-packing obstruction in the complete zero-holonomy,
post-puncture-reserving branch.

The quotient-periodic separation in `rem:aper` is not used.  Reanchoring keeps
the same denominator `E` and numerator `B`; it does not create or remove
quotient, subfield, tangent, contained, or support-degenerate structure.  Those
branches must remain in the global Paper-B ledger.

## 6. Remaining Wall

This note deletes only the zero-holonomy plus failed-absorption wall under
post-puncture reserve.  The next Paper-B-native target is:

```text
M1-NONZERO-LOW-TAIL-CECH-HOLONOMY-PADE-GRAVER-PAYMENT.
```

Namely, for the overlap cochain

```text
tau_ij = (z_j-z_i) B/E on S_i cap S_j,
```

if no family `R_i in F[X]_<h` satisfies `R_i-R_j=tau_ij` on all retained
punctured overlaps, the resulting nonzero Cech class must be converted into a
paid Pade/local-unit atom, a paid Pade-Graver atom, or one of the existing
quotient, subfield, fixed-pencil, tangent, contained, or support-degenerate
branches.
