ROUTE_CUT

## 1. Executive verdict and confidence

**Verdict:** the Cycle84 count transfers to an exact finite MCA numerator lower certificate for the original Role05 packet, but ordinary tensor/block amplification does **not** produce an (R)-fold (t=1) Reed–Solomon MCA packet.

There are two distinct failures:

1. The literal block product has (R) independent color coordinates. It is a (t=R), block-direct-sum object, not a single (t=1) RS syndrome line.
2. The canonical one-variable fusion, obtained by multiplying block locators, collapses the colors to an (R)-fold product set inside one copy of (\mathbf F_{17^{16}}^\times). Its occupancy is not (\operatorname{Occ}_1^R).

There is, however, a useful new exact lemma: nine fixed marker points convert the base packet from
[
(n,k,\sigma,j)=(256,137,6,113)
]
to the official rate-(\frac12) parameters
[
(256,128,6,122)
]
without changing its occupied-color spectrum.

**Confidence:** high.

---

## 2. Exact theorem and counterpacket statement

Put
[
F_0=\mathbf F_{17^{16}},\qquad
q_0=17^{16}=48,661,191,875,666,868,481,
]
and let
[
\mathcal A={\rho_\beta(T):T\in\mathcal P_0}\subset F_0^\times .
]
The Cycle84 certificate gives
[
|\mathcal A|=O=52,747,567,092,
]
with
[
|\mathcal P_0|=P=52,747,567,104,\qquad
m_{\max}=2,\qquad D=24.
]

### Theorem A — exact base occupancy transfer

Under the banked Cycle62 Role05 support-plus-color theorem and the Cycle65 identification of (\rho_\beta(T)) with the (\Delta^+)-lift coordinate up to a fixed nonzero scalar,
[
M_C(\sigma=6)\ge O
]
for the explicit
[
(n,k,\sigma,j)=(256,137,6,113)
]
Role05 instance over (F_0).

More precisely, among the supports (T\in\mathcal P_0), there are exactly (O) distinct transverse MCA slopes. This is a lower bound on the whole MCA numerator, not a scalar-list statement.

### Lemma B — fixed-marker official-rate normalization

Let (K_0=\langle\eta^8\rangle), so (|K_0|=32). In the Cycle65 coset decomposition every (T\in\mathcal P_0) has the form
[
T={1}\cup\bigcup_{t=1}^7\eta^t\widetilde A_t.
]
Thus every support avoids (K_0\setminus{1}).

Since (\deg\Delta=6), choose
[
M\subset K_0\setminus\bigl({1}\cup\operatorname{Supp}\Delta\bigr),
\qquad |M|=9.
]
Define
[
\mathcal P_0^\sharp={T\cup M:T\in\mathcal P_0}.
]

Then (\mathcal P_0^\sharp) is a valid (t=1) packet with
[
(n,k^\sharp,\sigma,j^\sharp)=(256,128,6,122),
]
and it has exactly the same occupied-color spectrum:
[
\operatorname{Occ}(\mathcal P_0^\sharp)=O,\qquad
m_{\max}(\mathcal P_0^\sharp)=2,\qquad D^\sharp=24.
]

Consequently the base obstruction can be rate-normalized to (k/n=1/2). This does not amplify its numerator.

### Theorem C — exact tensor dichotomy

For (R\ge2), the literal Cartesian product of the rate-normalized packet has formal parameters

[
\begin{aligned}
n_R&=256R,\
k_R&=128R,\
\sigma_R&=6R,\
j_R&=122R,\
|\mathcal P_R|&=P^R.
\end{aligned}
]

Its independent thickening is
[
\Delta_{\mathrm{ind}}^+
=\coprod_{r=1}^R\bigl(\Delta_r+[\beta_r]\bigr),
]
of degree (7R), and its occupied color vectors form
[
\mathcal A^R,
\qquad
|\mathcal A^R|=O^R,
\qquad
m_{\max}=2^R.
]

But this is a (t=R) product-color object. A (t=1) Role05 packet would have only
[
\Delta_R^+=\Delta_R+[\beta],
]
of degree (6R+1), with one slope coordinate rather than (R) independent coordinates.

Indeed, for every affine line (L\subseteq K^R),
[
|L\cap\mathcal A^R|\le O.
]
Thus restricting the (R)-fold product object to one syndrome line destroys the (O^R) amplification.

### Counterpacket D — canonical locator-product tensor

Consider affine block copies
[
\phi_r(x)=\beta_*+a_r(x-\beta)
]
with disjoint images. For block supports (T_r^\sharp),
[
\rho_{\beta_*}!\left(\bigcup_{r=1}^R\phi_r(T_r^\sharp)\right)
=============================================================

\left(\prod_{r=1}^R a_r^{122}\right)
\prod_{r=1}^R\rho_\beta(T_r^\sharp).
]

Therefore the scalar occupied set is a translate of the product set
[
\mathcal A^{\cdot R}
====================

{a_1\cdots a_R:a_r\in\mathcal A},
]
not the Cartesian set (\mathcal A^R).

Since (\mathcal A\subset F_0^\times),
[
|\mathcal A^{\cdot R}|\le q_0-1.
]
Already for (R=2),
[
O^2
===

2,782,305,834,125,041,336,464

>

# q_0-1

48,661,191,875,666,868,480.
]
Hence
[
\boxed{\operatorname{Occ}_2\ge O^2}
]
is impossible for the canonical affine locator-product tensor.

---

## 3. Proof

### 3.1 Base transfer

Cycle62 Theorem C identifies colors with the occupied (\Delta^+)-lift classes, and its equation (4.4) gives
[
T,T'\text{ have the same slope}
\iff
g_T^+=g_{T'}^+.
]

Cycle65–66 identify, on (\mathcal P_0),
[
g_T^+=c,\rho_\beta(T)
]
in a fixed trivialization, with (c\ne0) independent of (T). Multiplication by (c) is injective. Therefore
[
#{\text{slopes represented by }\mathcal P_0}
============================================

#{\rho_\beta(T):T\in\mathcal P_0}
=O.
]

The Cycle62 noncontainment theorem applies to every slope counted in this (t=1) slice, so no contained-incidence subtraction occurs.

### 3.2 Marker padding

Let (P_M(X)=\prod_{m\in M}(X-m)). Write the original apolar pair as
[
I_s=(A,B),\qquad \deg A=6,\quad \deg B=113.
]
For each (T\in\mathcal P_0),
[
P_T=A,U_T+\gamma_TB,\qquad \gamma_T\ne0.
]

Set
[
B^\sharp=P_MB.
]
Because (M\cap\operatorname{Supp}\Delta=\varnothing),
[
\gcd(A,B^\sharp)=1,
\qquad
\deg B^\sharp=122.
]
Moreover,
[
P_{T\cup M}
=P_MP_T
=A(P_MU_T)+\gamma_TB^\sharp.
]

The complete intersection
[
(A,B^\sharp)
]
has socle degree
[
6+122-2=126,
]
so binary apolar duality produces a nonzero syndrome for redundancy
[
R^\sharp=127=n-k^\sharp-1.
]
Thus
[
k^\sharp=256-127-1=128.
]

In (G_{\Delta^+}),
[
g_{T\cup M}^+
=============

\left(\prod_{m\in M}\alpha_{\Delta^+}(m)\right)g_T^+.
]
The multiplier is fixed and invertible. It preserves every fiber equality, hence preserves occupancy, maximum multiplicity, and (D).

### 3.3 Why the direct tensor is not an RS (t=1) packet

The direct sum of (R) copies of the ([256,128]) RS code has parameters
[
[256R,128R],
]
but its minimum distance is only
[
129.
]
A generalized Reed–Solomon code with the same length and dimension would have minimum distance
[
256R-128R+1=128R+1.
]
For (R\ge2), these are different. Hence the block-direct-sum code is not GRS.

It also has (R) independent extension directions. Its bad colors live in an affine (R)-space. For a line
[
L={u+zv:z\in K}\subset K^R,\qquad v\ne0,
]
choose a coordinate (r) with (v_r\ne0). Projection onto that coordinate is injective on (L), so
[
|L\cap\mathcal A^R|
\le|\mathcal A|
=O.
]
Thus the Cartesian occupancy (O^R) is unavailable on one MCA slope line.

### 3.4 Why canonical scalar fusion does not multiply occupancy

For an affine copy fixing the external point,
[
\beta_*-\phi_r(x)=a_r(\beta-x).
]
Taking products over a (122)-point support gives the formula in Counterpacket D. All variable factors remain in the unique embedded copy of (F_0^\times); the block scalings contribute only one fixed coset multiplier.

Consequently, quotient descent and same-slope collisions are exactly the multiplicative collisions in (\mathcal A^{\cdot R}). A final global affine color normalization
[
\chi\mapsto u\chi+v,\qquad u\ne0,
]
preserves its cardinality. Independent affine normalizations of the individual blocks cannot be used after fusion: one global MCA line has only one such normalization.

---

## 4. Exact field and frontier comparison

Use
[
q_{\rm gen}=q_{\rm code}=q_0.
]
For native MCA, scalar-extend the line to
[
q_{\rm line}=q_0^s=17^{16s}.
]
The challenge field (q_{\rm chal}) is unused by this lower certificate.

Because (F_0) must embed into the line field, the permitted line-field degrees are multiples of (16). Under the strict official condition (q_{\rm line}<2^{256}), only (s=1,2,3) are possible:

| (s) | (T_{\rm line}=\lfloor q_0^s/2^{128}\rfloor) | Consequence                                   |
| --: | ------------------------------------------: | --------------------------------------------- |
|   1 |                                         (0) | Trivial no-safe-field regime                  |
|   2 |                                         (6) | The tangent lower bound (j=122) already fails |
|   3 |               (338,617,018,271,848,945,628) | First nontrivial tensor-relevance window      |

At (s=3),
[
O<T_{\rm line},
]
so the single Cycle84 packet does not fail the row.

An abstract two-block tensor would give
[
O^2
===

2,782,305,834,125,041,336,464

>

# 338,617,018,271,848,945,628

T_{\rm line},
]
with margin
[
2,443,688,815,853,192,390,836.
]

But the canonical scalar product is bounded by
[
q_0-1
=====

48,661,191,875,666,868,480
<
T_{\rm line}.
]

Therefore:

[
\boxed{
\text{the unique useful two-block amplification window exists numerically,
but the canonical tensor cannot reach it.}
}
]

---

## 5. Verification requirements

The following are needed before any promotion to an official counterpacket:

1. Record the explicit original apolar pair ((A,B)), syndrome, domain digest, and the exact Cycle65 map from (\rho_\beta) to the (\Delta^+)-lift.
2. Emit nine explicit marker points (M), and verify
   [
   M\cap\left(\bigcup_{T\in\mathcal P_0}T\right)=\varnothing,
   \qquad
   M\cap\operatorname{Supp}\Delta=\varnothing.
   ]
3. Verify the complete-intersection syndrome for ((A,P_MB)) and its
   [
   (n,k,\sigma,j)=(256,128,6,122)
   ]
   fingerprint.
4. For any proposed tensor fusion, verify a single global degree-(12) modulus, degree-(244) second generator, and one common syndrome for every block pair. Componentwise validity is insufficient.
5. Verify the global color formula in the line field and count lift classes after all quotients. No new Cycle84 census is needed.

---

## 6. Next exact lemma or construction

The exact next target is:

```text
L-CYCLE86-TWO-BLOCK-T1-RS-FUSION-AND-COLOR-SEPARATION
```

It should assert the existence of

[
F_0\subset K=\mathbf F_{17^{48}},
\qquad \theta\in K\setminus F_0,
]
two disjoint (256)-point blocks (D_1,D_2), and one global (t=1) RS packet with

[
(n,k,\sigma,j)=(512,256,12,244),
]
such that:

1. every pair
   [
   (T_1,T_2)\in(\mathcal P_0^\sharp)^2
   ]
   produces one full-coordinate support
   [
   \Phi_1(T_1)\cup\Phi_2(T_2);
   ]
2. all such supports represent one fixed global syndrome;
3. after one global affine color normalization, the slope is either
   [
   \chi(T_1,T_2)=\rho_\beta(T_1)+\theta\rho_\beta(T_2),
   ]
   or
   [
   \chi(T_1,T_2)=\rho_\beta(T_1)\bigl(\theta+\rho_\beta(T_2)\bigr).
   ]

Either displayed encoding is injective on (\mathcal A^2). For example,
[
a(\theta+b)=a'(\theta+b')
]
with (a,a',b,b'\in F_0) forces (a=a') and then (b=b'), because
(1,\theta) are linearly independent over (F_0).

This lemma would give
[
M_C(12)\ge O^2>T_{\rm line},
]
a rate-(\frac12), strict-field-cap, frontier-active MCA counterpacket.

The alternative terminal result is a universal no-fusion theorem proving that every two-block (t=1) RS fusion factors through
[
u,c_1(T_1)c_2(T_2)+v
]
with both (c_i) contained in one (F_0^\times)-coset. That would force occupancy at most (q_0-1) and permanently cut the tensor route.

---

## Self-audit

1. **Exact implication proved:**
   [
   \operatorname{Occ}(\beta)=52,747,567,092
   \Longrightarrow
   M_C(6)\ge52,747,567,092
   ]
   for the banked explicit Role05 packet. The same bound survives nine-marker rate normalization to (k/n=1/2).

   **Not proved:**
   [
   \operatorname{Occ}_R\ge\operatorname{Occ}_1^R
   ]
   for any single (t=1) RS instance.

2. **Prize relevance:** the current result is a finite MCA/model certificate and an official-rate normalization lemma. It is not yet a frontier-active official counterpacket.

3. **First failing reduction line:**
   [
   (\mathcal P_0^\sharp)^R
   \longrightarrow
   \text{one common full-coordinate fiber of a single (t=1) RS code}.
   ]
   The literal product is (t=R) and non-GRS.

4. **Field usage:** (T_{\rm line}), not (T_{\rm code}), is used for MCA.
   (q_{\rm gen}=q_{\rm code}=17^{16}), (q_{\rm line}=17^{48}) in the useful window, and (q_{\rm chal}) pays no bill. The informal (2^{32}) comparison is not the native prize comparison.

5. **Possible numerator losses:** base quotienting, affine normalization, same-slope collisions, and containment do not reduce the certified base value. Under tensoring, multiplicative collisions and subfield periodicity do reduce the putative (O^R), down to at most (q_0-1) in the canonical fusion.

6. **Conversion condition:** proving `L-CYCLE86-TWO-BLOCK-T1-RS-FUSION-AND-COLOR-SEPARATION` converts this route cut into an official MCA counterpacket.
