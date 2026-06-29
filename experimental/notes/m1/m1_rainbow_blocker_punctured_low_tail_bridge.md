# Rainbow Blocker And Punctured Low-Tail Bridge

Status: PROVED local bridge / ROUTE_CUT / AUDIT.

This note records a local bridge in the Paper-B residue-line MCA route.  It is
not an official prize solve, not a public leaderboard row, not a protocol
soundness claim, not an ordinary list-decoding theorem, not a Paper-A
no-slack example, and not a proof of `conj:B` or `conj:final-mca`.

The point is narrow: after the Type-A / mixed-Type-B pruning step, every
residual unpaid slope has a same-slope Type-B divided-difference obstruction.
A false next move is to bound the multiplicity of a fixed rejecting skeleton.
Rejecting skeletons are usually abundant, not scarce.  The correct local
replacement is a rainbow matching / blocker alternative.

## 1. Setup

Let `F` be a field and let `H subset F` have distinct points.  Work in one
Paper-B residue-line datum `(E,B,w)` with `E(x) != 0` on `H`.  For each retained
slope `i`, write its slope parameter as `z_i`, active support as
`T_i subset H`, and residual values as

```text
y_i(x) = (w(x)-z_i B(x))/E(x) - c_i(x),     x in T_i.
```

Fix `r>0` and define

```text
O_i = { c in F[X]_<r : c(x)=y_i(x) for every x in T_i },
```

and

```text
R_i = { U subset T_i : |U|=r+1 and [U]y_i != 0 }.
```

The previous pruning lemma gives the local equivalence

```text
O_i = empty
  <=> R_i != empty.
```

Thus every residual unpaid slope has at least one rejecting same-slope Type-B
skeleton.

## 2. Rainbow Matching / Blocker Lemma

Let `Gamma` be a finite set of residual unpaid slopes and assume
`R_i != empty` for every `i in Gamma`.  For any integer `M>=1`, either:

```text
1. there are M distinct slopes i_1,...,i_M and pairwise disjoint
   skeletons U_j in R_{i_j};
```

or:

```text
2. there are I subset Gamma and W subset H such that
      |I| <= M-1,
      |W| <= (M-1)(r+1),
   and every U in R_i intersects W for every i in Gamma \ I.
```

Proof.  Choose a maximal rainbow disjoint family

```text
(i_1,U_1), ..., (i_m,U_m),     U_j in R_{i_j}.
```

If `m>=M`, the first alternative holds.  If `m<M`, set

```text
I = {i_1,...,i_m},
W = U_1 union ... union U_m.
```

Then `|I|<=M-1` and `|W|<= (M-1)(r+1)`.  If some `i in Gamma \ I` had a
rejecting skeleton `U in R_i` disjoint from `W`, the pair `(i,U)` could be
added to the maximal family.  This contradiction proves the blocker branch.

The deletion of the selected slopes `I` is necessary.  An all-slope blocker
statement is false: with one slope, `|H|=2(r+1)`, and
`R_i=binom(H,r+1)`, no blocker of size `r+1` need meet all
`(r+1)`-subsets.

## 3. Punctured Interpolation Consequence

In the blocker branch, define literal puncturing by

```text
T_i^W = T_i \ W,
y_i^W = y_i|_{T_i^W},
O_i^W = { c in F[X]_<r : c(x)=y_i(x) for every x in T_i^W }.
```

Then

```text
O_i^W != empty       for every i in Gamma \ I.
```

Indeed, if `O_i^W=empty`, the divided-difference criterion gives a subset
`U subset T_i^W` with `|U|=r+1` and `[U]y_i^W != 0`.  Since `y_i^W` is a
restriction of `y_i`, this says `U in R_i`; since `U subset T_i \ W`, it is
disjoint from `W`, contradicting the blocker property.

This implication is only a literal restriction statement.  It does not allow
one to rechoose `E`, `B`, or the anchor word after puncturing.

## 4. Payment Requires Reserve

The conclusion `O_i^W != empty` is not by itself a packing theorem.  It becomes
payable by the marked/punctured low-tail skeleton lemma only when enough support
survives the puncture.

In the unmarked form, put `a=deg E`.  If every retained slope satisfies

```text
|T_i \ W| >= a+r,
```

then the low-tail incidence count on `H \ W` gives the weighted bound

```text
sum_i binom(|T_i\W|-1,r) <= binom(n-|W|,r+1).
```

In particular, if all retained slopes have at least `a+r` surviving points,

```text
|Gamma \ I| <= binom(n-|W|,r+1) / binom(a+r-1,r),
```

and

```text
|Gamma| <= (M-1) + binom(n-|W|,r+1) / binom(a+r-1,r).
```

If some slopes have `|T_i\W|<a+r`, they must be carried as a support-deficiency
error term.  Treating punctured interpolation as automatic low-tail payment is
the first false line in the unrepaired bridge.

## 5. The Disjoint Branch Is A Real Wall

The first alternative gives a precise object: pairwise domain-disjoint
same-slope Type-B cocycles.  For `U={u_0,...,u_r}`, let

```text
L_U(phi) = sum_{u in U} phi(u) / prod_{v in U, v != u}(u-v).
```

Then `L_U(f)=0` for all `f in F[X]_<r`, and `U in R_i` means

```text
L_U(w/E) - z_i L_U(B/E) - L_U(c_i) != 0.
```

Disjointness gives a direct-sum packet of nonzero barycentric syndromes.  It
does not by itself imply quotient, subfield, PGL2, complete-shadow, low-rank,
or low-tail structure.

One route cut is the common-core/private-tail absorber.  Take disjoint sets

```text
C, P_1, ..., P_M subset H,
```

put `E=X-alpha`, `B=1`, and choose private tails

```text
phi_i = L_C psi_i
```

on the private blocks.  Define `w` so that the slope `z_i` witness agrees with
`w` on `C union P_i`, and choose the correction `c_i` to remove the common-core
part.  Then `y_i=phi_i`, so the common core forces `O_i=empty`, while private
blocks provide pairwise disjoint Type-B skeletons.  Small punctures do not make
the slope low-tail unless they delete almost all of the common core or all of
the corresponding private block.

This construction is not a counterexample to Paper B.  It cuts only the
overclaim that the disjoint Type-B branch is automatically paid by existing
branches.  The missing structural term is a private-tail / CRT-absorber
holonomy theorem.

## 6. Relation To Paper B

The labels `def:residue` and `lem:denom` supply the residue-line witness and
division by `E`.  The labels `thm:normalform` and `thm:closure` supply the
coordinate setting but no packing estimate.  The warning `prop:noanchor` is
essential: the proof uses the actual anchor values `y_i`, and the
common-core/private-tail construction exploits anchor freedom.  The
quotient-periodic separation in `rem:aper` does not cover generic
private-tail absorbers.  The conjecture `conj:B` remains the target, not an
input.

## 7. Next Target

The next target is not fixed-skeleton multiplicity.  It is:

```text
M1-CRT-ABSORBER-HOLONOMY-OR-PRIVATE-BLOCK-PAYMENT.
```

Given a branch-clean residue-line packet with many disjoint same-slope Type-B
skeletons, form the support-overlap graph with transition constraints

```text
A_i - A_j = (z_j-z_i)B/E       on T_i cap T_j.
```

One should prove one of:

```text
1. acyclic/star absorber: paid by private-block volume or support reserve;
2. cyclic zero-holonomy absorber: integrates to marked/punctured low-tail;
3. cyclic nonzero-holonomy absorber: forces a coefficiented cocycle or wide
   squarefree local-unit / Pade-Graver atom;
4. structured overlap: quotient, PGL2, subfield, or complete local-jet branch.
```

The first possible fatal line is the existence of a dense primitive overlap-CRT
absorber whose holonomy avoids all these outcomes.
