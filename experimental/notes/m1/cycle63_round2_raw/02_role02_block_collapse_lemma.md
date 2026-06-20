BANKABLE_LEMMA

## 1. Executive verdict and confidence

The block-collapse lemma is valid over every finite field and after arbitrary field extension, including nonsplit cosets, provided the model boundary map is put in its canonical degree-normalized coordinates.

There is one essential wording correction. For the older auxiliary-form definition
[
\alpha_\Delta^{L_*}(x)=\left[\left.\frac{L_x}{L_*}\right|*\Delta\right],
]
the raw product generally has a fixed (L**)-dependent jet. The invariant statement is
[
\partial_\Delta(L_*)^M
\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
=====================================

(-c^M,1),
]
or equivalently that every raw block product lies in one fixed translate of the toric subgroup. After the standard target translation already used in the model boundary map, all jet coordinates vanish.

**Confidence: high, (0.999).**

---

## 2. Formal theorem

Let (F) be a field, let (\sigma\ge 1), and put
[
\Delta=[0]+\sigma[\infty]\subset \mathbf P^1_F.
]
Write (z=Z/X) at infinity. Then
[
R_\Delta=H^0(\Delta,\mathcal O_\Delta)
\cong F\times F[z]/(z^\sigma),
\qquad
G_\Delta=R_\Delta^\times/F^\times.
]

The two components of (\Delta) admit the canonical piecewise trivialization of
(\mathcal O_{\mathbf P^1}(1)|*\Delta) given by (Z) at (0) and (X) at
(\sigma[\infty]). For a homogeneous form (Q) of degree (d), nonvanishing
on (\Delta), define
[
\partial*{\Delta,d}(Q)
======================

\left[
\left(
Q(0,1),,
Q(1,z)\bmod z^\sigma
\right)
\right]\in G_\Delta.
]
This map is multiplicative:
[
\partial_{\Delta,d+e}(QR)
=========================

\partial_{\Delta,d}(Q)\partial_{\Delta,e}(R).
]

For (x\ne0), put
[
L_x=X-xZ,
\qquad
\alpha_\Delta(x)=\partial_{\Delta,1}(L_x)
=[(-x,1-xz)].
]

Let (E/F) be any extension, let (H\le E^\times) be cyclic of order (N),
let (K\le H) have order
[
M\ge \sigma,
]
and let (c\in E^\times). For the coset (C=cK), define
[
\beta_K(C)=\prod_{u\in K}\alpha_\Delta(cu).
]

Then:

1. **Exact canonical collapse**
   [
   \boxed{\beta_K(cK)=[(-c^M,1)].}
   ]
   Hence its jet coordinates in degrees (1,\ldots,\sigma-1) are all zero.

2. **Exact color dependence**
   The block depends on (cK) only through (c^M). More precisely,
   [
   \prod_{x\in cK}x=(-1)^{M+1}c^M,
   ]
   while the normalized toric boundary coordinate is (-c^M).

3. **Auxiliary-form invariance**
   If (L_*) is any linear form nonvanishing on (\Delta_E), and
   [
   \alpha_\Delta^{L_*}(x)
   ======================

   \left[\left.\frac{L_x}{L_*}\right|*{\Delta_E}\right],
   \qquad
   \ell**=\partial_{\Delta,1}(L_*),
   ]
   then
   [
   \boxed{
   \ell_*^M\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
   =[(-c^M,1)].
   }
   ]
   Thus changing (L_*) only translates every order-(M) block by the same
   degree-dependent element.

4. **Scalar and representative invariance**
   Replacing (c) by (ck), (k\in K), leaves (c^M) unchanged. Scaling any
   locator (L_{cu}) by a nonzero scalar also leaves its class in (G_\Delta)
   unchanged.

5. **Base change and nonsplit descent**
   If the divisor (cK) is realized over (F), then (a=c^M\in F^\times) and
   the block class descends to
   [
   [(-a,1)]\in G_\Delta(F).
   ]
   This remains true when neither (K) nor its individual points split over
   (F).

---

## 3. Full proof

### 3.1 The canonical model coordinates

Because the reduced point (0) and the thickened point at infinity are
disjoint,
[
\Delta=[0]\amalg \sigma[\infty].
]
On the first component, (Z) is a unit. On the second component, (X) is a
unit. Consequently the pair
[
(Z\text{ at }0,;X\text{ at }\sigma[\infty])
]
is a legitimate trivialization of
(\mathcal O_{\mathbf P^1}(1)|_\Delta).

For a degree-(d) form (Q), division by its (d)-th power gives
[
Q/Z^d\big|*0=Q(0,1),
\qquad
Q/X^d\big|*{\sigma[\infty]}
=Q(1,z)\bmod z^\sigma.
]
Multiplying (Q) by a scalar multiplies both components by the same scalar,
which is trivial in the quotient by (F^\times). Therefore
(\partial_{\Delta,d}(Q)) is well-defined.

The definition immediately gives multiplicativity:
[
(QR)(0,1)=Q(0,1)R(0,1)
]
and
[
(QR)(1,z)=Q(1,z)R(1,z).
]

For (L_x=X-xZ),
[
L_x(0,1)=-x,
\qquad
L_x(1,z)=1-xz,
]
so
[
\alpha_\Delta(x)=[(-x,1-xz)].
]

### 3.2 The block polynomial

Since (K) is a finite subgroup of the multiplicative group of a field, its
elements are distinct and (\operatorname{char}E\nmid M). Every (u\in K)
satisfies (u^M=1). Hence the two monic degree-(M) polynomials
[
\prod_{u\in K}(T-u)
\quad\text{and}\quad
T^M-1
]
have the same (M) roots, and therefore
[
\prod_{u\in K}(T-u)=T^M-1.
]

Substituting (T=X/(cZ)), or directly homogenizing, gives
[
\boxed{
\prod_{u\in K}(X-cuZ)=X^M-c^MZ^M.
}
]

Let
[
P_{cK}(X,Z)=X^M-c^MZ^M.
]
By multiplicativity of the boundary map,
[
\beta_K(cK)=\partial_{\Delta,M}(P_{cK}).
]
At (0),
[
P_{cK}(0,1)=-c^M.
]
At infinity,
[
P_{cK}(1,z)=1-c^Mz^M.
]
Thus
[
\beta_K(cK)
===========

[(-c^M,1-c^Mz^M\bmod z^\sigma)].
]

Because (M\ge\sigma),
[
z^M=0\quad\text{in }E[z]/(z^\sigma).
]
Therefore
[
\boxed{
\beta_K(cK)=[(-c^M,1)].
}
]

This proof uses no logarithms, Newton identities, or division by
(1,\ldots,\sigma-1). It is valid in every characteristic.

### 3.3 Vanishing of the elementary symmetric jet coordinates

Expanding the local factor gives
[
\prod_{u\in K}(1-cu,z)
======================

# \sum_{r=0}^M(-1)^r e_r(cK)z^r

1-c^Mz^M.
]
Hence
[
e_r(cK)=0
\qquad(1\le r\le M-1).
]
Since (M\ge\sigma),
[
e_1(cK)=\cdots=e_{\sigma-1}(cK)=0.
]

The product of the block points is read from the final coefficient:
[
(-1)^M\prod_{u\in K}cu=-c^M,
]
so
[
\prod_{x\in cK}x=(-1)^{M+1}c^M.
]
Thus either the actual product coordinate or the normalized toric coordinate
determines, and is determined by, (c^M), up to a fixed sign depending only on
(M).

### 3.4 Exact classification by the color (c^M)

If (c'=ck) for some (k\in K), then
[
(c')^M=c^Mk^M=c^M.
]
Thus (c^M) is independent of the representative of (cK).

Conversely, if
[
c_1^M=c_2^M,
]
then
[
(c_1/c_2)^M=1.
]
The (M)-th roots of unity in a splitting field are precisely the (M)
elements of (K). Hence (c_1/c_2\in K), and
[
c_1K=c_2K.
]

In particular, when (c\in H), the map
[
H/K\longrightarrow H^M,
\qquad
cK\longmapsto c^M
]
is an isomorphism. Indeed its kernel is the unique order-(M) subgroup (K),
and both sides have order (N/M).

Thus (c^M) is not merely an invariant: it is an exact coordinate on the set
of (K)-cosets.

### 3.5 Auxiliary-form invariance

Let
[
L_*=AX+BZ
]
be nonvanishing on (\Delta_E). Nonvanishing at (0) and at the thickened
point at infinity is equivalent to
[
A\ne0,\qquad B\ne0.
]

Put
[
\ell_*=\partial_{\Delta,1}(L_*).
]
The restriction of a quotient of sections equals the quotient of their
restrictions, so
[
\alpha_\Delta^{L_*}(x)
======================

\partial_{\Delta,1}(L_x),
\partial_{\Delta,1}(L_*)^{-1}
=============================

\alpha_\Delta(x)\ell_*^{-1}.
]
Consequently
[
\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
=====================================

\ell_*^{-M}\prod_{u\in K}\alpha_\Delta(cu),
]
and hence
[
\boxed{
\ell_*^M
\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
=[(-c^M,1)].
}
]

This proves auxiliary-form independence in the precise sense required for
generalized-Jacobian fibers: changing (L_*) produces a fixed translation
depending only on the total degree (M), not on the block (cK).

There is also a completely invariant ratio statement. For any two cosets
(cK,dK),
[
\frac{\prod_{u\in K}\alpha_\Delta^{L_*}(cu)}
{\prod_{u\in K}\alpha_\Delta^{L_*}(du)}
=======================================

\left[\left(\frac{c^M}{d^M},1\right)\right].
]
Thus a trade replacing (dK) by (cK) has identically zero jet charge,
without making any choice of auxiliary form.

For an explicit coordinate formula, let
[
\lambda=B/A.
]
After normalizing the infinity component to constant term (1),
[
\ell_*=(\lambda,1+\lambda z),
]
and therefore
[
\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
=====================================

\left(
-c^M\lambda^{-M},
(1+\lambda z)^{-M}
\right).
]
The jet factor is independent of (cK); multiplying by (\ell_*^M) removes
it exactly.

### 3.6 Scalar normalization

There are two possible scalar ambiguities.

First, replacing the representative (c) by (ck), (k\in K), leaves
(c^M) unchanged, as proved above.

Second, a point locator is defined only up to scalar:
[
L_{cu}'=\rho_uL_{cu},
\qquad \rho_u\in E^\times.
]
But
[
\partial_{\Delta,1}(\rho_uL_{cu})
=================================

[(\rho_u,\rho_u)],
\partial_{\Delta,1}(L_{cu})
===========================

\partial_{\Delta,1}(L_{cu})
]
in (G_\Delta(E)). Equivalently,
[
\prod_{u\in K}L_{cu}'
=====================

\left(\prod_{u\in K}\rho_u\right)P_{cK},
]
and the prefactor is a diagonal scalar, hence trivial in (G_\Delta).

Thus the block class is independent of every projective or locator
normalization.

### 3.7 Extension fields and nonsplit cosets

Let (E/F) contain (c) and the points of (K). Over (E),
[
P_{cK}(X,Z)=X^M-c^MZ^M.
]

Suppose the effective divisor (cK) is defined over (F). Its monic
homogeneous polynomial is then Galois invariant. Since the only non-leading
coefficient of (P_{cK}) is (-c^M), it follows that
[
a:=c^M\in F^\times.
]
Therefore
[
P_{cK}=X^M-aZ^M\in F[X,Z]
]
and
[
\beta_K(cK)=[(-a,1)]\in G_\Delta(F).
]
Base change from (F) to (E) sends this class to the product of the split
atoms.

Conversely, if (a=c^M\in F^\times), then (X^M-aZ^M) is defined over (F)
and its geometric zero set is (cK). Since a finite multiplicative subgroup
has order prime to the characteristic, this polynomial is separable. Hence
(cK) is a finite étale, possibly nonsplit, divisor over (F).

Equivalently, in the nonsplit description with finite étale algebra
[
A=F[t]/(t^M-a),
]
one has
[
\operatorname{Nm}_{A/F}(X-tZ)=X^M-aZ^M.
]
The same boundary calculation therefore applies without enumerating any
geometric point.

All formulas commute with arbitrary further field extension.

### 3.8 Edge cases

* **(\sigma=1).** There are no jet coordinates. The formula remains
  (\beta_K(cK)=(-c^M,1)).

* **(M=\sigma).** The term (z^M) is exactly zero modulo (z^\sigma), so
  the endpoint is included.

* **(M=1).** Necessarily (\sigma=1); the statement reduces to the
  one-point toric boundary value.

* **Characteristic (2).** The sign (-1) equals (1), but all identities
  remain valid. No division by (2) or by (M) occurs.

* **Small characteristic.** Since (K) is a subgroup of a field's
  multiplicative group, its order is automatically prime to the
  characteristic. No additional hypothesis is required.

* **(c=0).** This is excluded: (cK) would not be an order-(M) coset in
  the multiplicative group.

---

## 4. Parameter ledger and exact finite relevance

For (F=\mathbf F_q):

| Quantity                     |                 Exact value |   |              |
| ---------------------------- | --------------------------: | - | ------------ |
| modulus                      |        ([0]+\sigma[\infty]) |   |              |
| degree of modulus            |                  (\sigma+1) |   |              |
| number of jet coordinates    |                  (\sigma-1) |   |              |
| generalized-Jacobian order   |         ((q-1)q^{\sigma-1}) |   |              |
| domain order                 |                         (N= | H | )            |
| block order                  |                         (M= | K | ), (M\mid N) |
| characteristic condition     |    automatically (p\nmid M) |   |              |
| number of (K)-cosets         |                       (N/M) |   |              |
| color group                  |              (H^M\cong H/K) |   |              |
| canonical block boundary     |                  ((-c^M,1)) |   |              |
| block elementary coordinates | (e_1=\cdots=e_{\sigma-1}=0) |   |              |
| raw (L_*)-boundary           |       (\ell_*^{-M}(-c^M,1)) |   |              |

There is an exact block-plus-defect consequence. Let
[
T=D;\dot\cup;c_1K;\dot\cup\cdots\dot\cup;c_bK
]
be a disjoint support profile. Then
[
\prod_{x\in T}\alpha_\Delta(x)
==============================

\left(
(-1)^{|D|+b}
\left(\prod_{d\in D}d\right)
\left(\prod_{i=1}^b c_i^M\right),
;
\prod_{d\in D}(1-dz)\bmod z^\sigma
\right).
]

Therefore:

* every jet coordinate is determined solely by (D);
* the selected full blocks affect only
  [
  \prod_{i=1}^b c_i^M\in H^M;
  ]
* for fixed (D) and (b), the exact block charge is the finite subset-product
  count
  [
  #\left{
  S\in\binom{H/K}{b}:
  \prod_{C\in S}\operatorname{col}_K(C)=\tau
  \right},
  ]
  for an explicitly determined (\tau\in H^M).

No asymptotic estimate is involved.

---

## 5. Bankable versus conditional

### Bankable

1. The homogeneous block identity
   [
   \prod_{u\in K}(X-cuZ)=X^M-c^MZ^M.
   ]
2. Vanishing of all jet coordinates (1,\ldots,\sigma-1) when (M\ge\sigma).
3. Exact dependence on the color (c^M).
4. The isomorphism (H/K\cong H^M).
5. Auxiliary-form covariance and the invariant block-trade ratio.
6. Independence of locator and coset representatives.
7. Base-change compatibility and nonsplit descent.
8. The exact block-plus-defect boundary formula.

### Still conditional

This lemma does not provide:

* a canonical choice of (K) when one support admits several block scales;
* a canonical defect assignment across competing scales;
* an overlap/non-double-counting inequality;
* a finite residual local limit outside the charged block families.

Those are the remaining parts of
`L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE`.

---

## 6. Failure point and normalization warning

The proof closes. The only false variant is the literal, ungauged assertion
that
[
\prod_{u\in K}\alpha_\Delta^{L_*}(cu)
]
itself has zero jets for an arbitrary (L_*).

For example, take
[
F=\mathbf F_5,\qquad
\sigma=M=2,\qquad
H=K={1,-1},\qquad
c=1,\qquad
L_*=X+Z.
]
Then, modulo (z^2),
[
\prod_{u\in K}\alpha_\Delta^{L_*}(u)
====================================

# \left(-1,(1+z)^{-2}\right)

# (-1,1-2z)

(-1,1+3z),
]
which has a nonzero degree-one jet.

However,
[
\partial_\Delta(L_*)^2
\prod_{u\in K}\alpha_\Delta^{L_*}(u)
=(-1,1).
]
Thus this is a notation/gauge issue, not a failure of block collapse or of the
block-trade route.

---

## 7. Next exact lemma or construction

A canonical fixed-(K) extraction is immediate:
[
\mathcal B_K(T)={cK\in H/K:cK\subseteq T},
]
[
U_K(T)=\bigcup_{C\in\mathcal B_K(T)}C,
\qquad
D_K(T)=T\setminus U_K(T).
]
For a fixed (K), this extracts every available full (K)-block and gives the
unique minimum defect.

The next exact wall is:

```text
L-MODEL-GJ-COVERAGE-MAXIMAL-KD-NONDOUBLECOUNTING
```

One concrete assignment to prove or kill is to choose (K_T) maximizing
lexicographically
[
\bigl(|U_K(T)|,\ |K|\bigr)
]
over subgroups (K\le H) with (|K|\ge\sigma), and then assign
[
T\longmapsto (K_T,D_{K_T}(T)).
]
If no such full block exists, assign (T) to the residual class.

The required next theorem is that competing block descriptions either coarsen
to this assigned profile or have an explicit finite overlap bound permitting
their charges to be summed once.

**Route to a full solve:** yes, conditionally. Block collapse is now closed.
The next decisive step is the canonical maximal ((K,D)) assignment together
with an exact overlap/non-double-counting theorem; after that, the remaining
wall is the finite near-split collision-class local limit.
