BANKABLE_LEMMA

## 1. Executive verdict and confidence

The wall `L-MODEL-GJ-MAXIMAL-KD-ASSIGNMENT` closes.

For arbitrary cyclic (H), there is an intrinsic assignment obtained by:

1. saturating every proposed (K)-description by selecting every full (K)-coset contained in the support;
2. minimizing the resulting defect size over all collapsing scales (|K|\ge \sigma);
3. among defect-minimizing scales, maximizing (|K|).

For the official dyadic domains (H\cong C_{2^m}), this has the sharper formula

[
K(T)=\operatorname{Stab}*H!\bigl(\operatorname{Core}*{K_0}(T)\bigr),
\qquad
D(T)=T\setminus \operatorname{Core}_{K_0}(T),
]

where

[
|K_0|=M_0:=2^{\lceil\log_2\sigma\rceil}.
]

The resulting canonical ((K,D))-classes are disjoint. More strongly, if (K^+) is the next dyadic subgroup above (K), then for every fixed defect, weight, and generalized-Jacobian target,

[
\boxed{
C_{K,D}=R_{K,D}-R_{K^+,D},
}
]

where (R_{K,D}) is the raw (K)-block count and (C_{K,D}) is the canonically assigned count. Thus there is no overlap factor at all.

The Cycle 62 order-(4) counterpacket is assigned entirely to its original pair ((K,D)); it is not fragmented among larger block scales.

**Confidence:** high, (0.99).

---

## 2. Formal theorem

Let (H) be a finite cyclic group of order (n), written multiplicatively, and let (1\le \sigma\le n). Put

[
\mathcal K_\sigma={K\le H:|K|\ge \sigma}.
]

For (T\subseteq H) and (K\le H), define

[
\mathcal F_K(T)={cK\in H/K:cK\subseteq T},
]

[
\operatorname{Core}*K(T)
=\bigcup*{C\in\mathcal F_K(T)}C,
\qquad
D_K(T)=T\setminus\operatorname{Core}_K(T).
]

Thus (\operatorname{Core}_K(T)) is the union of every fully occupied (K)-coset.

### Theorem A — canonical assignment for cyclic (H)

Call (T) (\sigma)-block-bearing if

[
\operatorname{Core}_K(T)\ne\varnothing
]

for at least one (K\in\mathcal K_\sigma). For such (T), define (K(T)) by lexicographically maximizing

[
\left(
|\operatorname{Core}*K(T)|,\ |K|
\right),
\qquad K\in\mathcal K*\sigma.
\tag{2.1}
]

Then set

[
D(T)=D_{K(T)}(T),
\qquad
S(T)=\mathcal F_{K(T)}(T).
\tag{2.2}
]

This assignment has the following properties.

1. **Fixed-scale minimality.**
   For fixed (K), (D_K(T)) is the unique inclusion-minimal and cardinality-minimal defect among all (K)-block descriptions of (T).

2. **Global defect minimality.**
   [
   |D(T)|=\min_{K\in\mathcal K_\sigma}|D_K(T)|.
   \tag{2.3}
   ]

3. **Maximal scale.**
   Among all scales attaining the minimum in (2.3), (K(T)) has maximum order. It is therefore inclusion-maximal among those scales.

4. **Uniqueness.**
   The maximum in (2.1) is unique.

5. **Canonicity.**
   The construction depends only on (T,H,\sigma). It is equivariant under every automorphism of (H).

6. **Description invariance.**
   Every block-plus-defect description of the same support (T) maps to the same pair ((K(T),D(T))).

7. **Exact non-double-counting.**
   The classes
   [
   \mathcal C_{K,D}
   ================

   {T:K(T)=K,\ D(T)=D}
   ]
   are pairwise disjoint and partition all (\sigma)-block-bearing supports.

Supports containing no full eligible block are assigned to a separate residual class (\bot).

---

### Theorem B — stabilizer form on prime-power cyclic domains

Assume now that

[
|H|=\ell^m
]

for a prime (\ell). This includes the official dyadic case (\ell=2).

Let

[
M_0=\ell^{\lceil\log_\ell\sigma\rceil},
]

and let (K_0\le H) be the unique subgroup of order (M_0). Define

[
U(T)=\operatorname{Core}_{K_0}(T),
\qquad
D_0(T)=T\setminus U(T).
\tag{2.4}
]

If (U(T)=\varnothing), then (T) is (\sigma)-block-free. Otherwise,

[
\boxed{
K(T)=\operatorname{Stab}_H(U(T))
:={h\in H:hU(T)=U(T)},
}
\tag{2.5}
]

and

[
\boxed{D(T)=D_0(T).}
\tag{2.6}
]

Thus the canonical procedure is:

* take every full block at the least collapsing scale (K_0);
* call their union (U(T));
* merge those blocks to the largest subgroup scale preserving (U(T)).

---

### Theorem C — exact quotient characterization

Keep the prime-power hypothesis. Fix (K_0\le K\le H), and let (D\subseteq H) satisfy

[
\operatorname{Core}_{K_0}(D)=\varnothing.
\tag{2.7}
]

Let

[
Q=H/K,
\qquad
\Omega_{K,D}
============

{cK\in H/K:cK\cap D=\varnothing}.
]

For nonempty (S\subseteq\Omega_{K,D}), put

[
U_S=\bigcup_{C\in S}C,
\qquad
T_{D,S}=D\sqcup U_S.
]

Then

[
\boxed{
(K(T_{D,S}),D(T_{D,S}))=(K,D)
\iff
\operatorname{Stab}_{Q}(S)={1_Q}.
}
\tag{2.8}
]

Here

[
\operatorname{Stab}_{Q}(S)
==========================

{q\in Q:qS=S}.
]

Hence “aperiodic” is not being used informally: the exact condition is trivial translation stabilizer in (H/K).

---

### Theorem D — exact overlap cancellation

Let (\mathcal R_{K,D}) denote the raw profile family

[
\mathcal R_{K,D}
================

\left{
D\sqcup U_S:
\varnothing\ne S\subseteq\Omega_{K,D}
\right},
]

and let (\mathcal C_{K,D}) be its canonically assigned subfamily.

Then

[
\boxed{
\mathcal R_{K,D}
================

\bigsqcup_{J:,K\le J\le H}
\mathcal C_{J,D}.
}
\tag{2.9}
]

If (K<H), let (K^+) be the unique subgroup satisfying

[
K<K^+,
\qquad
|K^+:K|=\ell.
]

Then

[
\boxed{
\mathcal C_{K,D}
================

\mathcal R_{K,D}\setminus\mathcal R_{K^+,D}.
}
\tag{2.10}
]

Consequently, after imposing any condition depending only on the support—fixed cardinality, fixed generalized-Jacobian target, or full-coordinate status—the corresponding counts satisfy

[
\boxed{
C_{K,D}=R_{K,D}-R_{K^+,D}.
}
\tag{2.11}
]

For (K=H), (C_{H,D}=R_{H,D}).

---

### Theorem E — exact model block charge

Assume (H\le F^\times), let

[
\Delta=[0]+\sigma[\infty],
]

and use the boundary coordinates

[
\Phi_\sigma(T)
==============

\left(
\prod_{x\in T}x,,
e_1(T),\ldots,e_{\sigma-1}(T)
\right).
]

Let (K\le H) have order (M\ge\sigma). For a coset (C=cK), define

[
\vartheta_K(C)=c^M.
]

Then

[
\vartheta_K:H/K\xrightarrow{\sim}H^M
\tag{2.12}
]

is a group isomorphism.

Fix a (K_0)-reduced defect (D), a weight (j), and a target

[
b=(P_b,\epsilon_1,\ldots,\epsilon_{\sigma-1}).
]

Put

[
d=|D|,
\qquad
L=\frac{j-d}{M},
\qquad
P_D=\prod_{x\in D}x.
]

If (L\notin\mathbf Z_{\ge1}), or if

[
e_r(D)\ne\epsilon_r
\quad(1\le r<\sigma),
\tag{2.13}
]

then the raw and canonical ((K,D))-charges are zero.

Otherwise define

[
g_{K,D,b}
=========

(-1)^{(M+1)L}P_bP_D^{-1}.
\tag{2.14}
]

The raw block charge is exactly

[
\boxed{
R_{K,D,j}(b)
============

#\left{
S\in\binom{\Omega_{K,D}}L:
\prod_{C\in S}\vartheta_K(C)=g_{K,D,b}
\right}.
}
\tag{2.15}
]

The canonical charge is

[
\boxed{
C_{K,D,j}(b)
============

#\left{
S\in\binom{\Omega_{K,D}}L:
\prod_{C\in S}\vartheta_K(C)=g_{K,D,b},
\operatorname{Stab}_{H/K}(S)=1
\right}.
}
\tag{2.16}
]

On a prime-power domain,

[
\boxed{
C_{K,D,j}(b)
============

R_{K,D,j}(b)-R_{K^+,D,j}(b).
}
\tag{2.17}
]

The raw charge also has the exact finite Fourier expression

[
R_{K,D,j}(b)
============

\frac1{|H^M|}
\sum_{\chi\in\widehat{H^M}}
\chi(g_{K,D,b}^{-1})
e_L\bigl(
\chi(\vartheta_K(C)):C\in\Omega_{K,D}
\bigr),
\tag{2.18}
]

with value zero when (g_{K,D,b}\notin H^M).

---

## 3. Full proof

### 3.1 Saturation and the unique minimal defect

A (K)-description of (T) is a decomposition

[
T=D\sqcup\bigcup_{C\in S}C,
\qquad S\subseteq H/K.
\tag{3.1}
]

Every selected coset must be fully contained in (T), so

[
S\subseteq\mathcal F_K(T).
]

The defect is then forced to be

[
D=T\setminus\bigcup_{C\in S}C.
]

Selecting another coset in (\mathcal F_K(T)\setminus S) removes exactly
(|K|) points from the defect. Therefore the unique minimal defect is obtained by selecting every full coset:

[
S=\mathcal F_K(T),
\qquad
D=D_K(T).
]

This proves fixed-scale uniqueness and minimality.

It also shows why saturation is necessary. If

[
f_K(T)=|\mathcal F_K(T)|,
]

then the number of nonsaturated (K)-descriptions is exactly

[
2^{f_K(T)}
]

when the empty selected set is allowed, and (2^{f_K(T)}-1) when at least one block is required. Thus nonsaturated descriptions have exponentially large overlap.

---

### 3.2 Existence and uniqueness of the general cyclic assignment

Because (H) is finite, the set of pairs

[
\left(
|\operatorname{Core}_K(T)|,\ |K|
\right)
]

has a lexicographic maximum.

A cyclic group has exactly one subgroup of every order dividing (n). Hence two maximizing subgroups cannot have the same order unless they are equal. The maximizing (K(T)) is therefore unique.

Since

[
|D_K(T)|=|T|-|\operatorname{Core}_K(T)|,
]

maximizing the first coordinate is equivalent to minimizing the defect size. Maximizing the second coordinate then chooses the largest scale among all defect minimizers.

The literal rule “choose the largest subgroup containing any full coset” is not adequate. For example, in additive (C_8), let (\sigma=2),

[
K_2={0,4},\qquad K_4={0,2,4,6},
]

and

[
T=K_4\cup(1+K_2).
]

At scale (K_2), all six points lie in full blocks, so the defect is empty. At scale (K_4), only four points lie in a full block and the defect has size two. Choosing the largest active scale would discard a strictly better block explanation. The lexicographic rule avoids this failure.

---

### 3.3 Canonicity and shear invariance

Let (\varphi\in\operatorname{Aut}(H)). Since (H) is cyclic, every subgroup is characteristic, so (\varphi(K)=K). Moreover,

[
\varphi(\operatorname{Core}_K(T))
=================================

\operatorname{Core}_K(\varphi(T)).
]

Core sizes and subgroup orders are preserved. Therefore

[
K(\varphi(T))=K(T),
\qquad
D(\varphi(T))=\varphi(D(T)).
]

In the apolar complete intersection, an admissible generator shear

[
B\longmapsto cB+AC,
\qquad c\ne0,
]

does not change the support (T), the generalized-Jacobian support fiber, or the full-coordinate property. Since the assignment uses only (T,H,\sigma), it is shear-invariant.

It is also independent of the auxiliary form (L_*), locator normalization, and the coefficient pair used to express the locator.

---

### 3.4 The prime-power stabilizer formula

Suppose (|H|=\ell^m). Its subgroup lattice is a chain. Every eligible subgroup (K) contains (K_0).

A (K)-coset is a union of (K_0)-cosets. Hence

[
\operatorname{Core}*K(T)
\subseteq
\operatorname{Core}*{K_0}(T)
=U(T).
\tag{3.2}
]

Thus (U(T)) is the largest possible block-covered core, and (D_0(T)) is the globally minimal defect.

Let

[
J=\operatorname{Stab}_H(U(T)).
]

Because (U(T)) is a union of (K_0)-cosets,

[
K_0\le J.
]

The (J)-orbits are its cosets, and (U(T)) is (J)-invariant, so (U(T)) is a union of (J)-cosets. Hence

[
U(T)\subseteq\operatorname{Core}_J(T).
]

Conversely, every (J)-coset is a union of (K_0)-cosets. If a (J)-coset is contained in (T), all its (K_0)-subcosets lie in (U(T)). Thus

[
\operatorname{Core}_J(T)\subseteq U(T).
]

Therefore

[
\operatorname{Core}_J(T)=U(T).
\tag{3.3}
]

So (J) attains the minimum defect. If another subgroup (K) attains the same core size, then (3.2) forces

[
\operatorname{Core}_K(T)=U(T),
]

so (U(T)) is (K)-invariant and (K\le J). Hence (J) is the unique largest defect-minimizing scale. This proves (2.5)–(2.6).

---

### 3.5 Quotient stabilizers and exact class decomposition

Let (\pi:H\to Q=H/K). For (S\subseteq Q),

[
U_S=\pi^{-1}(S).
]

For (h\in H),

[
hU_S=U_S
\iff
\pi(h)S=S.
]

Consequently,

[
\operatorname{Stab}_H(U_S)
==========================

\pi^{-1}(\operatorname{Stab}_Q(S)),
\tag{3.4}
]

and

[
\operatorname{Stab}_H(U_S)/K
\cong
\operatorname{Stab}_Q(S).
\tag{3.5}
]

Because (D) contains no full (K_0)-coset and is disjoint from (U_S),

[
\operatorname{Core}*{K_0}(T*{D,S})=U_S.
]

The canonical subgroup is therefore (\operatorname{Stab}_H(U_S)), proving (2.8).

Every raw (K)-profile has a unique stabilizer (J\ge K), and is canonically assigned to ((J,D)). Conversely, every canonical (J)-profile with (J\ge K) is also a raw (K)-profile. This gives the disjoint union (2.9).

In a cyclic (\ell)-group, every (J>K) contains the immediate successor (K^+). Hence

[
\bigsqcup_{J>K}\mathcal C_{J,D}
===============================

\mathcal R_{K^+,D},
]

which proves (2.10) and the count identity (2.11).

---

### 3.6 Model block-collapse and the charge formula

Let (K) have order (M). Since (K) is the group of (M)-th roots of unity inside (H),

[
\prod_{u\in K}(Y-u)=Y^M-1.
]

Substituting (Y=X/(cZ)) and homogenizing gives

[
\boxed{
\prod_{u\in K}(X-cuZ)=X^M-c^MZ^M.
}
\tag{3.6}
]

Because (M\ge\sigma),

[
X^M-c^MZ^M\equiv X^M\pmod{Z^\sigma}.
\tag{3.7}
]

Equivalently,

[
\prod_{x\in cK}(1-xz)
=====================

1-c^Mz^M
\equiv1\pmod{z^\sigma}.
\tag{3.8}
]

Thus full (K)-blocks do not alter (e_1,\ldots,e_{\sigma-1}).

The constant term of (3.6) gives

[
(-1)^M\prod_{x\in cK}x=-c^M,
]

so

[
\prod_{x\in cK}x=(-1)^{M+1}c^M.
\tag{3.9}
]

For

[
T=D\sqcup\bigcup_{C=cK\in S}C,
\qquad |S|=L,
]

equations (3.8)–(3.9) yield

[
e_r(T)=e_r(D)
\quad(1\le r<\sigma),
\tag{3.10}
]

and

[
\prod_{x\in T}x
===============

P_D(-1)^{(M+1)L}
\prod_{C\in S}c^M.
\tag{3.11}
]

This proves the compatibility conditions and product equation in (2.15).

The map (c\mapsto c^M) on (H) has kernel exactly (K), since (M\mid n). Therefore it induces the isomorphism (2.12). Character orthogonality on (H^M) gives (2.18).

Changing the representative (c) to (cu), (u\in K), does not change (c^M). All signs disappear automatically in characteristic two.

---

### 3.7 The Cycle 62 counterpacket remains one canonical class

For the official packet,

[
|H|=256,\qquad \sigma=4,\qquad K=K_0=\mu_4,
\qquad H/K\cong C_{64}.
]

The defect

[
D={1,\omega^{64},\omega,\omega^{65}}
]

partially occupies (C_0) and (C_1), but contains no full (K)-coset. Therefore the (K_0)-core of

[
T_S=D\cup\bigcup_{a\in S}C_a
]

is exactly the variable block union.

Suppose (S\subseteq C_{64}) had nontrivial translation stabilizer. Every nontrivial subgroup of (C_{64}) contains its unique element of order two, namely (32). Hence

[
S=S+32.
]

Thus (S) is a union of pairs

[
{a,a+32}.
]

Each pair has label sum

[
a+(a+32)=2a+32,
]

which is even modulo (64). Hence every such (S) has even label sum.

But the packet requires

[
\sum_{a\in S}a\equiv15\pmod{64},
]

which is odd. Therefore

[
\operatorname{Stab}*{C*{64}}(S)=1
]

for every packet member.

Consequently every one of the

[
\boxed{7{,}045{,}058{,}086{,}196{,}679}
]

supports is canonically assigned to the same pair

[
(K,D)=(\mu_4,D).
]

The counterpacket is therefore fully absorbed by one configuration-level charge, rather than being dispersed among larger accidental block scales.

---

## 4. Parameter ledger and exact finite relevance

| Quantity                                 | Exact definition                                      |     |                                      |   |   |
| ---------------------------------------- | ----------------------------------------------------- | --- | ------------------------------------ | - | - |
| domain order                             | (n=                                                   | H   | )                                    |   |   |
| slack                                    | (\sigma)                                              |     |                                      |   |   |
| least prime-power collapsing scale       | (M_0=\ell^{\lceil\log_\ell\sigma\rceil})              |     |                                      |   |   |
| least subgroup                           | (                                                     | K_0 | =M_0)                                |   |   |
| base block core                          | (\operatorname{Core}_{K_0}(T))                        |     |                                      |   |   |
| canonical subgroup                       | (\operatorname{Stab}*H(\operatorname{Core}*{K_0}(T))) |     |                                      |   |   |
| canonical defect                         | (T\setminus\operatorname{Core}_{K_0}(T))              |     |                                      |   |   |
| quotient                                 | (Q=H/K)                                               |     |                                      |   |   |
| block color                              | (cK\mapsto c^{                                        | K   | })                                   |   |   |
| selected block count                     | (L=(j-                                                | D   | )/                                   | K | ) |
| canonical quotient condition             | (\operatorname{Stab}_Q(S)=1)                          |     |                                      |   |   |
| raw/canonical relation                   | (C_{K,D}=R_{K,D}-R_{K^+,D})                           |     |                                      |   |   |
| overlap after assignment                 | exactly (0)                                           |     |                                      |   |   |
| number of saturated scales in dyadic (H) | at most (\max(0,\lfloor\log_2                         | T   | \rfloor-\lceil\log_2\sigma\rceil+1)) |   |   |

For arbitrary cyclic (H), the number of saturated eligible descriptions of a support of size (t) is at most

[
#{M:M\mid n,\ \sigma\le M\le t}.
]

Before saturation, a fixed scale with (f) full cosets has (2^f-1) nonempty descriptions, so no uniform raw overlap bound is possible.

For the Cycle 62 packet:

[
n=256,\quad \sigma=4,\quad |K|=4,\quad |D|=4,\quad j=124,\quad L=30.
]

Its canonical block charge is exactly

[
7{,}045{,}058{,}086{,}196{,}679,
]

against the finite target (21). The assignment therefore captures the entire route-cut packet explicitly; it does not itself prove that the resulting charge is small.

---

## 5. Bankable versus conditional

### Bankable

* Unique saturation and minimal defect at each subgroup scale.
* The automorphism-equivariant canonical assignment for every cyclic (H).
* The stabilizer formula on cyclic prime-power domains, especially dyadic domains.
* Exact characterization by trivial quotient translation stabilizer.
* Exact disjointness of canonical ((K,D))-classes.
* Exact telescoping identity (C_{K,D}=R_{K,D}-R_{K^+,D}).
* Exact finite subset-product and Fourier formulas for each charge.
* Generator-shear, auxiliary-form, and coset-representative invariance.
* Assignment of the entire Cycle 62 counterpacket to one ((\mu_4,D)) class.

### Conditional or still open

* No useful upper bound is yet proved for the sum of block charges over all possible defects (D).
* No finite local-limit bound is proved for supports containing no full (K_0)-coset.
* For non-prime-power cyclic domains, the general assignment remains exact, but the one-step dyadic subtraction is replaced by the full finite subgroup-poset decomposition.
* This lemma does not by itself close the near-split collision-class-mass wall.

---

## 6. Failure point

There is no failure inside the canonical-assignment theorem.

The remaining obstruction is quantitative rather than definitional. The assignment gives the exact decomposition

[
N_\Delta(b)
===========

N_\Delta^{\mathrm{block\text{-}free}}(b)
+
\sum_{\substack{D\subseteq H\
\operatorname{Core}*{K_0}(D)=\varnothing}}
\sum*{K_0\le K\le H}
C_{K,D,j}(b).
\tag{6.1}
]

By telescoping,

[
\sum_{K_0\le K\le H}C_{K,D,j}(b)
================================

R_{K_0,D,j}(b),
]

so

[
\boxed{
N_\Delta(b)
===========

N_\Delta^{\mathrm{block\text{-}free}}(b)
+
\sum_{\substack{D\subseteq H\
\operatorname{Core}*{K_0}(D)=\varnothing}}
R*{K_0,D,j}(b).
}
\tag{6.2}
]

Every block-bearing support occurs exactly once in the second term. The unresolved issue is bounding the block-free term and, where necessary, compressing the explicit defect sum.

---

## 7. Next exact lemma and route to a full solve

Yes, there is a route to a full solve.

The next exact wall should be sharpened to

```text
L-MODEL-GJ-K0-BLOCK-FREE-COLLISION-CLASS-MASS
```

Let

[
K_0=\mu_{2^{\lceil\log_2\sigma\rceil}}.
]

Prove an explicit finite bound for

[
N_\Delta^{\mathrm{block\text{-}free}}(b)
========================================

#\left{
T\in\binom Hj:
\Phi_\sigma(T)=b,
\operatorname{Core}_{K_0}(T)=\varnothing
\right}
]

in the near-split regime not covered by norm rigidity or the cyclotomic-rank cap.

The desired theorem can now take the exact form

[
N_\Delta(b)
\le
\underbrace{
\sum_D R_{K_0,D,j}(b)
}*{\text{exact block-trade charge}}
+
\underbrace{
\text{explicit finite bound for }
N*\Delta^{\mathrm{block\text{-}free}}(b)
}_{\text{remaining wall}}.
]

The configuration-level double-counting problem is solved; the next problem is precisely the mass of the block-free residual.
