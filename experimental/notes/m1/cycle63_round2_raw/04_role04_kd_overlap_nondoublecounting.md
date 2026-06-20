BANKABLE_LEMMA

## 1. Executive verdict and confidence

For cyclic dyadic (H), the overlap wall closes after imposing the necessary canonical-defect normalization.

For every subgroup (K\le H), remove from a support all full (K)-cosets and call the remainder its canonical (K)-defect. Canonical block-profile families are then **laminar**:

[
\text{two profiles are either disjoint, equal, or one contains the other.}
]

More precisely, if (K_1\le K_2), any nonempty intersection is exactly the (K_2)-profile. The (K_2)-partition is the common coarsening, and its block color is the common-left-composite color. Hence there is no additional overlap residual: the common part can be charged once by an exact subtraction rule.

**Confidence: high.**

---

## 2. Formal theorem

Let (F) be a finite field and let

[
H\le F^\times,\qquad |H|=n=2^m.
]

Fix (\sigma\ge1). Only subgroups (K\le H) with

[
M:=|K|\ge \sigma
]

are considered.

For (T\subseteq H), define its canonical (K)-defect by

[
\partial_K(T)
:=
T\setminus
\bigcup_{\substack{C\in H/K\ C\subseteq T}} C.
\tag{2.1}
]

Thus (\partial_K(T)) consists exactly of the points lying in partially occupied (K)-cosets. A set (D\subseteq H) is called (K)-reduced when

[
\partial_K(D)=D,
]

equivalently, (D) contains no full (K)-coset.

For a (K)-reduced (D), put

[
\mathcal A_K(D)
===============

{C\in H/K:C\cap D=\varnothing}.
\tag{2.2}
]

For a coset (C=cK), define its exact point-product color

[
\tau_K(C):=\prod_{x\in C}x
=(-1)^{M+1}c^M.
\tag{2.3}
]

The normalized prompt color is (c^M); the factor ((-1)^{M+1}) is constant at a fixed scale and is absorbed into the target.

For an integer (\ell) and (\gamma\in F^\times), define the canonical profile

[
\mathcal F(K,D;\ell,\gamma)
:=
\left{
D\sqcup\bigcup_{C\in\mathcal S}C:
\begin{array}{l}
\mathcal S\in\binom{\mathcal A_K(D)}{\ell},[1mm]
\prod_{C\in\mathcal S}\tau_K(C)=\gamma
\end{array}
\right}.
\tag{2.4}
]

Write

[
N_K(D;\ell,\gamma)
:=
|\mathcal F(K,D;\ell,\gamma)|.
\tag{2.5}
]

### Theorem A — exact model-fiber profile charge

Let the model boundary target be

[
b=(p_b,J_b(z)),
]

where (p_b\in F^\times) is the product coordinate and

[
J_b(z)\in 1+zF[z]/(z^\sigma)
]

encodes (e_1,\ldots,e_{\sigma-1}). For fixed support size (j), define

[
\mathcal F_K(D;j,b)
===================

{T\subseteq H:|T|=j,\ \Phi_\sigma(T)=b,\ \partial_K(T)=D}.
]

Put

[
\ell_D=\frac{j-|D|}{M},
\qquad
\gamma_D=\frac{p_b}{\prod_{d\in D}d}.
\tag{2.6}
]

Then

[
\boxed{
|\mathcal F_K(D;j,b)|
=====================

\mathbf 1_{\substack{
D\text{ is }K\text{-reduced}\
\ell_D\in\mathbf Z\
E_D(z)\equiv J_b(z)\pmod{z^\sigma}
}}
N_K(D;\ell_D,\gamma_D),
}
\tag{2.7}
]

where

[
E_D(z)=\prod_{d\in D}(1-dz).
]

In particular,

[
\boxed{
N_K(D;\ell,\gamma)
\le
\binom{n/M-\nu_K(D)}{\ell},
}
\tag{2.8}
]

where

[
\nu_K(D)
========

|{C\in H/K:C\cap D\ne\varnothing}|.
]

For (M>1),

[
\nu_K(D)\ge
\left\lceil\frac{|D|}{M-1}\right\rceil,
]

so

[
\boxed{
N_K(D;\ell,\gamma)
\le
\binom{
n/M-\left\lceil |D|/(M-1)\right\rceil
}{\ell}.
}
\tag{2.9}
]

All binomial coefficients are interpreted as zero when the lower argument is not an integer in the permitted range.

---

### Theorem B — exact two-profile overlap

Let

[
K_1\le K_2\le H,
\qquad
M_i=|K_i|,
\qquad
r_{12}=\frac{M_2}{M_1}.
]

Let (D_i) be (K_i)-reduced. Define

[
D_{2\to1}:=\partial_{K_1}(D_2).
\tag{2.10}
]

If (D_1=D_{2\to1}), then

[
E_{12}:=D_2\setminus D_1
]

is a disjoint union of full (K_1)-cosets. Put

[
a_{12}:=\frac{|E_{12}|}{M_1},
\qquad
\pi(E_{12}):=\prod_{x\in E_{12}}x.
\tag{2.11}
]

For

[
\mathcal F_i=\mathcal F(K_i,D_i;\ell_i,\gamma_i),
]

one has the exact formula

[
\boxed{
|\mathcal F_1\cap\mathcal F_2|
==============================

\begin{cases}
N_{K_2}(D_2;\ell_2,\gamma_2),
&
\begin{array}{l}
D_1=\partial_{K_1}(D_2),\
\ell_1=a_{12}+r_{12}\ell_2,\
\gamma_1=\pi(E_{12})\gamma_2,
\end{array}
[5mm]
0,&\text{otherwise.}
\end{cases}
}
\tag{2.12}
]

In the compatible case,

[
\boxed{\mathcal F_2\subseteq\mathcal F_1}
\tag{2.13}
]

and hence

[
\mathcal F_1\cap\mathcal F_2=\mathcal F_2.
]

Consequently,

[
\boxed{
|\mathcal F_1\cap\mathcal F_2|
\le
\binom{n/M_2-\nu_{K_2}(D_2)}{\ell_2}.
}
\tag{2.14}
]

For two profiles in the same model fiber ((j,b)), the size and color equations in (2.12) are automatic. Therefore

[
\boxed{
\mathcal F_{K_1}(D_1;j,b)
\cap
\mathcal F_{K_2}(D_2;j,b)
=========================

\begin{cases}
\mathcal F_{K_2}(D_2;j,b),
& D_1=\partial_{K_1}(D_2),\
\varnothing,&\text{otherwise.}
\end{cases}
}
\tag{2.15}
]

This is the requested finite overlap theorem.

---

### Theorem C — exact non-double-counting charge

After identifying profiles that define the same support family, all nonempty canonical profiles in a fixed ((j,b))-fiber form a laminar family.

For any finite collection (\mathscr C) of such profiles, let
(\operatorname{ch}(v)) be the maximal proper subprofiles of (v) occurring in (\mathscr C). Define

[
N_v^\circ
:=
N_v-\sum_{w\in\operatorname{ch}(v)}N_w.
\tag{2.16}
]

Then

[
\boxed{N_v^\circ\ge0}
\tag{2.17}
]

and

[
\boxed{
\left|
\bigcup_{v\in\mathscr C}\mathcal F_v
\right|
=======

\sum_{v\in\mathscr C}N_v^\circ.
}
\tag{2.18}
]

Thus an overlap belonging to a larger-subgroup/common-color profile is charged once at that profile, and is subtracted exactly from every containing finer-scale charge.

---

## 3. Proof

### 3.1 Block collapse and the exact profile count

For (C=cK),

[
\prod_{x\in C}(X-xZ)=X^M-c^MZ^M.
\tag{3.1}
]

Equivalently,

[
\prod_{x\in C}(1-xz)=1-c^Mz^M.
\tag{3.2}
]

Since (M\ge\sigma),

[
1-c^Mz^M\equiv1\pmod{z^\sigma}.
\tag{3.3}
]

Hence, for

[
T=D\sqcup\bigcup_{C\in\mathcal S}C,
]

one has

[
E_T(z)
======

E_D(z)\prod_{C=cK\in\mathcal S}(1-c^Mz^M)
\equiv E_D(z)\pmod{z^\sigma}.
\tag{3.4}
]

The product coordinate is

[
\prod_{x\in T}x
===============

\left(\prod_{d\in D}d\right)
\prod_{C\in\mathcal S}\tau_K(C).
\tag{3.5}
]

Also

[
|T|=|D|+M|\mathcal S|.
\tag{3.6}
]

Equations (3.4)–(3.6) give the bijection and count in Theorem A.

For a representative (c) of (C), replacing (c) by (ck), (k\in K), does not change (c^M). Moreover, evaluating (3.1) at (X=0,Z=1) gives

[
(-1)^M\tau_K(C)=-c^M,
]

which proves (2.3).

---

### 3.2 Canonicality of the defect

Every support (T) has the decomposition

[
T=
\partial_K(T)
\sqcup
\bigcup_{\substack{C\in H/K\ C\subseteq T}}C.
\tag{3.7}
]

The defect (\partial_K(T)) contains no full (K)-coset.

Conversely, suppose

[
T=D\sqcup\bigcup_{C\in\mathcal S}C
]

with (D) (K)-reduced and every selected block disjoint from (D). Then the selected blocks are exactly the full (K)-cosets contained in (T), and consequently

[
D=\partial_K(T).
]

Thus the reduced decomposition is unique.

A nonreduced description canonically reduces as follows. Let

[
\mathcal R={C\in H/K:C\subseteq D}.
]

Replace

[
D\longmapsto D\setminus\bigcup_{C\in\mathcal R}C,
\qquad
\mathcal S\longmapsto\mathcal S\cup\mathcal R.
\tag{3.8}
]

The support is unchanged, and the resulting defect is the unique canonical one.

---

### 3.3 Functoriality of defects along the dyadic subgroup chain

Let (K_1\le K_2). Every (K_2)-coset is a disjoint union of (K_1)-cosets.

Write

[
T=
\partial_{K_2}(T)
\sqcup
\bigcup_{\substack{B\in H/K_2\B\subseteq T}}B.
]

Every full (K_2)-coset contributes only full (K_1)-cosets and hence contributes nothing to the (K_1)-defect. Therefore

[
\boxed{
\partial_{K_1}(T)
=================

\partial_{K_1}\bigl(\partial_{K_2}(T)\bigr).
}
\tag{3.9}
]

This is the key identity.

In particular, if (T) has defects (D_1,D_2) at the two scales, then necessarily

[
D_1=\partial_{K_1}(D_2).
\tag{3.10}
]

---

### 3.4 Necessity of the overlap conditions

Suppose (T\in\mathcal F_1\cap\mathcal F_2). By (3.9),

[
D_1=\partial_{K_1}(D_2).
]

The difference

[
E_{12}=D_2\setminus D_1
]

is exactly the union of those full (K_1)-cosets contained in (D_2).

Let (\mathcal E_{12}) denote this collection of (a_{12}) fixed (K_1)-blocks. If (\mathcal S_2) is the selected (K_2)-block set of (T), then its selected (K_1)-block set is exactly

[
\mathcal S_1
============

\mathcal E_{12}
\sqcup
\bigcup_{B\in\mathcal S_2}
{C\in H/K_1:C\subseteq B}.
\tag{3.11}
]

Each (K_2)-block contains (r_{12}) (K_1)-blocks, so

[
\ell_1=a_{12}+r_{12}\ell_2.
\tag{3.12}
]

Also,

[
\prod_{C\in\mathcal E_{12}}\tau_{K_1}(C)
========================================

# \prod_{x\in E_{12}}x

\pi(E_{12}),
]

and for each (K_2)-block (B),

[
\tau_{K_2}(B)
=============

\prod_{\substack{C\in H/K_1\C\subseteq B}}\tau_{K_1}(C),
\tag{3.13}
]

since both sides are the product of all points of (B). Hence

[
\gamma_1=\pi(E_{12})\gamma_2.
\tag{3.14}
]

All compatibility conditions in (2.12) are necessary.

---

### 3.5 Sufficiency

Assume the three compatibility conditions in (2.12), and let (T\in\mathcal F_2).

Equation (3.9) gives

[
\partial_{K_1}(T)=\partial_{K_1}(D_2)=D_1.
]

Its selected (K_1)-blocks are given by (3.11), so their number is (\ell_1) and their product color is (\gamma_1). Therefore

[
T\in\mathcal F_1.
]

Thus

[
\mathcal F_2\subseteq\mathcal F_1.
]

If any compatibility condition fails, the necessity argument shows that no common support exists. This proves Theorem B.

For profiles in the same ((j,b))-fiber, let (E_{12}=D_2\setminus D_1). Since (E_{12}) is a union of full (K_1)-blocks and (M_1\ge\sigma),

[
E_{D_2}(z)
==========

E_{D_1}(z)E_{E_{12}}(z)
\equiv E_{D_1}(z)\pmod{z^\sigma}.
\tag{3.15}
]

Moreover,

[
\frac{p_b}{\prod D_1}
=====================

\left(\prod E_{12}\right)
\frac{p_b}{\prod D_2}.
\tag{3.16}
]

The size and color conditions are therefore automatic, proving (2.15).

---

### 3.6 Common-left-composite and incidence-graph interpretation

For a subgroup (K) of order (M), its coset partition is the fiber partition of

[
R_K(x)=x^M.
]

If (K_1\le K_2), then (M_1\mid M_2), and

[
R_{K_2}(x)
==========

A_{12}(R_{K_1}(x)),
\qquad
A_{12}(y)=y^{M_2/M_1}.
\tag{3.17}
]

Thus (R_{K_2}) is the common left composite/common color of the two block systems.

In the bipartite incidence graph of (K_1)- and (K_2)-cosets, every (K_1)-coset lies in one (K_2)-coset. The connected components are exactly the (K_2)-cosets. Therefore the common unions of the two partitions are exactly unions of (K_2)-cosets.

The fixed defect (D_2) records the partially occupied components, while the remaining movable common unions are selected (K_2)-components. This is precisely the profile (\mathcal F_2) appearing in (2.12).

The Role 09 coprime-degree component proliferation cannot occur here because the subgroup lattice of cyclic (2)-groups is a chain.

---

### 3.7 Exact profile-tree decomposition

For any (K_1\le K_2), equation (3.9) yields the disjoint partition

[
\boxed{
\mathcal F_{K_1}(D_1;j,b)
=========================

\bigsqcup_{\substack{
D_2\text{ is }K_2\text{-reduced}\
\partial_{K_1}(D_2)=D_1
}}
\mathcal F_{K_2}(D_2;j,b).
}
\tag{3.18}
]

Indeed, every support on the left has the unique defect
(D_2=\partial_{K_2}(T)), and Theorem B gives the converse inclusion.

Consequently,

[
\boxed{
N_{K_1}(D_1;j,b)
================

\sum_{\substack{
D_2\text{ is }K_2\text{-reduced}\
\partial_{K_1}(D_2)=D_1
}}
N_{K_2}(D_2;j,b).
}
\tag{3.19}
]

This is an exact finite identity, not an upper bound.

---

### 3.8 Exact exclusive charge

By Theorem B, any two nonempty canonical profiles are disjoint or nested. After equal families are identified, the collection is laminar.

For a node (v), its children are pairwise disjoint. Hence

[
\mathcal F_v^\circ
:=
\mathcal F_v
\setminus
\bigcup_{w\in\operatorname{ch}(v)}\mathcal F_w
]

has cardinality

[
|\mathcal F_v^\circ|
====================

# N_v-\sum_{w\in\operatorname{ch}(v)}N_w

N_v^\circ.
]

Every support lying in the union of the chosen profiles belongs to a unique minimal-by-inclusion profile containing it. Equivalently, it belongs to a unique maximal-subgroup profile under the candidate priority rule. Therefore the sets (\mathcal F_v^\circ) form a disjoint partition of the union, proving (2.18).

---

### 3.9 Gauge, shear, and field edge cases

Changing the auxiliary form (L_*) multiplies every atom (\alpha_\Delta(x)) by one fixed group element (u). For a support of size (j), its target is multiplied by (u^j). A profile with defect size (|D|) and (\ell) full (M)-blocks acquires the factor

[
u^{|D|}(u^M)^\ell=u^j.
]

Thus every support family and every overlap relation is unchanged.

Under generator shear

[
B\longmapsto cB+AC,\qquad c\ne0,
]

the generalized-Jacobian target is unchanged in the quotient by (F^\times). The support, its canonical defects, and all profile counts are therefore shear-invariant.

Other edges:

* If (K_1=K_2), compatibility forces
  (D_1=D_2,\ell_1=\ell_2,\gamma_1=\gamma_2); otherwise the profiles are disjoint.
* If (M=1), every occupied singleton is a full block, so the only reduced defect is empty. The formulas remain valid.
* If (K=H), the quotient has one block. Every profile has at most two possible block counts, (0) or (1).
* Empty profiles satisfy all identities with cardinality zero.
* The theorem is unchanged by finite field extension.
* For a multiplicative coset (\alpha\mu_n), scaling by (\alpha^{-1}) reduces to the subgroup formulation.

---

## 4. Parameter ledger and exact finite relevance

For two nested profiles:

| Parameter  | Exact meaning                                 |     |            |
| ---------- | --------------------------------------------- | --- | ---------- |
| (n)        | (                                             | H   | =2^m)      |
| (M_i)      | (                                             | K_i | \ge\sigma) |
| (N_i)      | number of (K_i)-blocks, (n/M_i)               |     |            |
| (r_{12})   | (M_2/M_1)                                     |     |            |
| (d_i)      | (                                             | D_i | )          |
| (\nu_i)    | number of (K_i)-blocks touched by (D_i)       |     |            |
| (A_i)      | available blocks, (N_i-\nu_i)                 |     |            |
| (\ell_i)   | selected block count                          |     |            |
| (a_{12})   | ((d_2-d_1)/M_1) in the compatible case        |     |            |
| (\gamma_i) | exact selected-block point-product color      |     |            |
| overlap    | (0) or exactly (N_{K_2}(D_2;\ell_2,\gamma_2)) |     |            |

If (H=\langle\omega\rangle), label the (K)-cosets by

[
C_t=\omega^tK,
\qquad t\in\mathbf Z/(n/M)\mathbf Z.
]

After removing the fixed sign in (2.3), the exact charge is a cyclic subset-sum count

[
N_K(D;\ell,\gamma)
==================

#\left{
S\in\binom{A}{\ell}:
\sum_{t\in S}t\equiv g\pmod{n/M}
\right}.
\tag{4.1}
]

It is computable by the exact recurrence

[
Q_i(h,r)
========

Q_{i-1}(h,r)
+
Q_{i-1}(h-1,r-t_i).
\tag{4.2}
]

For the Cycle 62 official counterpacket,

[
n=256,\quad M=4,\quad n/M=64,\quad \nu_K(D)=2,\quad \ell=30.
]

The exact relevant color bucket is

[
7{,}045{,}058{,}086{,}196{,}679.
]

Any overlap of this profile with an order-(8), (16), (32), or larger subgroup profile is exactly one child profile in (3.18). Such overlap is subtracted once; it cannot generate an additional multiplicative overlap factor. Conversely, this theorem does not reduce the original (7.0\times10^{15}) mass automatically: the child counts sum exactly to the parent count.

---

## 5. Bankable versus conditional

### Bankable

1. The canonical defect operator (\partial_K).
2. Uniqueness of the reduced (D+)full-block description.
3. The exact fixed-profile subset-product charge.
4. Defect functoriality
   [
   \partial_{K_1}(T)=\partial_{K_1}(\partial_{K_2}(T)).
   ]
5. The exact zero-or-coarser-profile intersection formula.
6. The common-left-composite interpretation
   [
   x^{M_2}=(x^{M_1})^{M_2/M_1}.
   ]
7. Laminarity of dyadic canonical profiles.
8. The exact exclusive-charge formula (2.18).
9. Auxiliary-form and generator-shear invariance.
10. Exact finite DP evaluation of every charge.

### Conditional

1. Which profile nodes should be declared chargeable or heavy.
2. Whether the candidate maximal assignment has a total exclusive charge below the prize threshold.
3. A finite bound for supports lying outside all chargeable block profiles.
4. The near-split collision-class mass theorem.
5. Extension from the model modulus to arbitrary (\Delta).

---

## 6. Failure point

The overlap theorem itself closes.

Canonical reduction is essential. Without it, even one support can have exponentially many descriptions. If

[
T=C_1\sqcup\cdots\sqcup C_s
]

is a union of (s) full (K)-blocks, then for every
(I\subseteq{1,\ldots,s}),

[
D_I=\bigcup_{i\in I}C_i,
\qquad
\mathcal S_I={C_i:i\notin I}
]

gives another description of the same support. There are (2^s) such aliases. They all reduce to

[
D=\varnothing,\qquad
\mathcal S={C_1,\ldots,C_s}.
]

Thus any theorem allowing nonminimal defects is false as a non-double-counting statement.

The remaining obstacle is aggregate mass, not overlap: exact child charges can still sum to an enormous parent charge.

---

## 7. Next exact lemma or construction

There is a route to a full solve, conditional on controlling the residual mass.

The next exact construction is to make the maximal assignment a stopping rule on the canonical profile tree. For example, let (\mathsf H(K,D;j,b)) be any exact shear-invariant predicate declaring a profile chargeable. Assign each support to the largest (K) on its profile path satisfying (\mathsf H). Its exact block-trade charge is

[
\boxed{
\operatorname{BT}(b)
====================

\sum_{v:\mathsf H(v)}
\left(
N_v-\sum_{w\in\operatorname{ch}_{\mathsf H}(v)}N_w
\right).
}
\tag{7.1}
]

No overlap factor is permitted or needed.

After a concrete predicate (\mathsf H) is banked, the next wall is precisely

```text
W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS
```

in the corrected form

[
N_\Delta(b)
\le
\operatorname{BT}(b)
+
C_\sigma\frac{\binom nj}{|G_{\mathrm{eff}}|}
+
R_{\mathrm{near\text{-}split}}(n,p,\sigma),
]

with every term finite and explicit.
