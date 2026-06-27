# M1 Skew-Shadow Matching Inverse Audit

Status: PROVED / REPAIR / EXACT_NEW_WALL / AUDIT.

This note records a Paper-B-native repair in the residue-line packing route.
It concerns `def:residue`, `lem:denom`, `thm:normalform`, `thm:closure`,
`prop:noanchor`, `rem:aper`, and `conj:B`.

This is not an official prize solve, not a protocol soundness claim, not an
ordinary list-decoding theorem, and not a Paper-A no-slack example.  The point
is narrower: the skew-shadow obstruction reduces to an exact all-witness
matching alternative.  The remaining wall is payment of the trace-separated
Pade fixed-skeleton branch, especially the full-cover case.

## 1. One-Pole Packet

Work in the one-pole local-unit coordinate used by the residue-line normal
form.  Let `H=X sqcup Y`, fix a local order `a`, support size `s`, and local
unit `W`.  For active choices indexed by `nu`, write

```text
A_nu subset X,
V_nu = J_{A_nu},
a_nu = lambda(A_nu),
B_nu = Pi_Y(s-|A_nu|, W V_nu^{-1}),
Q_nu subset a_nu B_nu,
Q_nu cap Q_mu = empty for nu != mu.
```

For each private scalar `q in Q_nu`, define the full support-witness fiber

```text
Rep(q) = { A_nu union T :
  T subset Y,
  |T| = s-|A_nu|,
  J_T = W V_nu^{-1},
  lambda(T) = q/a_nu }.
```

Then every `S in Rep(q)` satisfies

```text
|S|=s,  J_S=W,  lambda(S)=q.
```

## 2. Matching Inverse

For witnesses `S in Rep(q)` and `T in Rep(q')` with `q != q'`, set

```text
D(S,T)=1_{S\T}-1_{T\S}.
```

Since `J_S=J_T=W`, cancellation of the common local-unit factor
`J_{S cap T}` gives

```text
Psi_a(D(S,T)) = 1.
```

Moreover overlap cancels in the scalar ratio, so

```text
Lambda(D(S,T)) = lambda(S)/lambda(T) = q/q'.
```

Thus every pair of witnesses with distinct private scalars gives a reduced
Pade kernel defect.

Build the all-witness packet-defect hypergraph on vertex set `H`, with an edge
`S triangle T` for each such pair.  Let `R=ceil(c log_2 n)`.  A maximum
support-disjoint matching gives a priority alternative:

```text
1. There are R support-disjoint reduced Pade kernel defects.
2. Every such R-tuple has small Lambda Boolean cube; this is product-collapse.
3. A union U of fewer than R defect supports has pairwise disjoint trace
   shadows Tr_U(q)={S cap U : S in Rep(q)} for distinct private scalars q.
```

The third branch is a reduction, not an already-paid Paper B conclusion.

## 3. What This Repairs

The earlier trace-blocking formulation could depend on one arbitrary selected
support per scalar.  The all-witness version is canonical: if two private
scalars have witnesses with the same trace on the matching union `U`, their
symmetric difference is an edge disjoint from `U`, contradicting maximality.

So skew-shadow itself is no longer the terminal wall.  The wall is payment of
the trace-separated Pade skeleton produced by the matching inverse.

## 4. What Is Not Proved

The false line is:

```text
trace separation by U implies an already paid fixed-skeleton branch.
```

This is not a theorem in Paper B as currently written.  In the full-cover case
`U=H`, trace separation is essentially tautological, since the full trace
remembers the whole support.  The nontrivial remaining data are that `H` is
covered by fewer than `R` support-disjoint Pade kernel supports and that the
scalar packet avoids quotient, tangent/contained, fixed-pencil, complete
local-unit, subfield, Frobenius, product-collapse, and recursive-descent
payments.

## 5. Next Exact Target

The conservative next theorem is:

```text
M1-FULL-COVER-PAIR-TOGGLE-INVERSE.
```

Equivalently:

```text
M1-PADE-FIXED-SKELETON-PAYMENT.
```

First split:

```text
U subsetneq H  -> full-local-unit recursive descent, if the descent predicate
                  is explicitly admitted and paid;
U = H          -> full-cover pair-toggle / signed-Cauchy Pade blocker.
```

The next proof target is to show that a scalar-rich, noncollapsed full-cover
Pade pair-toggle packet with fewer than `c log n` support-disjoint kernel
blocks must pay to an existing algebraic branch, or else to construct a
primitive full-cover counterpacket.
