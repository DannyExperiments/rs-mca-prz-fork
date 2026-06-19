# BANKABLE_LEMMA

**Confidence:** high for the exact bridge, pair-rank lemma, occupancy calculation, and counterpackets below; moderate for the proposed completion-lemma route; the primitive inverse theorem itself remains open.

## 1. Exact theorem: jet–residue conservation and the actual-list bridge

Let

[
\mathcal P_m:=F[X]_{<m},\qquad
a=k+\sigma,\qquad
j=n-a,
]

and consider a reduced datum

[
E\in F[X],\quad \deg E=t,\quad
1\le t\le \sigma,\quad
E(x)\ne0\ \ (x\in D),
]

[
B\in\mathcal P_t,\qquad \gcd(E,B)=1.
]

Put

[
s:=\sigma-t,\qquad
A_E:=F[X]/(E),\qquad b:=[B]_E.
]

Thus (b) is a unit in (A_E). For (P=\sum p_iX^i\in\mathcal P_a), define

[
\operatorname{Top}*s(P)
:=(p*{k+t},p_{k+t+1},\ldots,p_{k+\sigma-1}).
]

When (s=0), this component is absent.

### Theorem 1: exact jet–residue sequence

The map

[
J_{E,s}:\mathcal P_a\longrightarrow F^s\oplus A_E,
\qquad
P\longmapsto
\bigl(\operatorname{Top}_s(P),[P]_E\bigr)
]

fits into the short exact sequence

[
\boxed{
0\longrightarrow E\mathcal P_k
\longrightarrow \mathcal P_a
\xrightarrow{J_{E,s}}
F^s\oplus A_E
\longrightarrow0.
}
\tag{1}
]

Consequently,

[
\boxed{
\mathcal P_a/E\mathcal P_k
;\simeq;
F^s\oplus A_E,
}
\tag{2}
]

and the preimage of the target slice

[
\Lambda_b:=0^s\oplus Fb
]

is exactly

[
\boxed{
U_{E,B}:=
E\mathcal P_k\oplus FB.
}
\tag{3}
]

Thus (U_{E,B}) has dimension (k+1), independent of (t).

The entropy conservation is exact:

[
\underbrace{s}*{\text{zero top jets}}
+
\underbrace{(t-1)}*{\text{residue constrained to a line}}
=========================================================

\boxed{\sigma-1}.
\tag{4}
]

This is the missing entropy ledger. Passing to the full shifted code
(\mathcal P_{k+t}) discards the (t-1) residue-line constraints; retaining
(U_{E,B}) does not.

---

### Theorem 2: exact support, slope, and actual-list identities

For (S\in\binom Da), let (I_S(w)\in\mathcal P_a) be the unique interpolant of (w) on (S). Then

[
\boxed{
J_{E,s}(I_S(w))=(0,zb)
\iff
I_S(w)=EG+zB
\quad\text{for a unique }G\in\mathcal P_k.
}
\tag{5}
]

Define

[
A_w(Q):={x\in D:Q(x)=w(x)},
]

[
\mathcal L_{U,z}(w,a):=
{Q\in U_{E,B}:|A_w(Q)|\ge a,\ \lambda_B(Q)=z},
]

where

[
\lambda_B(EG+zB):=z.
]

Then the bad-slope set is exactly

[
\boxed{
Z_{E,B,w}
=========

{z\in F:\mathcal L_{U,z}(w,a)\ne\varnothing}.
}
\tag{6}
]

It is not merely bounded by an actual list: it is the color image of an actual list in the one-dimensional extension code (U_{E,B}).

For each (z), the raw support fiber decomposes as

[
\boxed{
\left{
S\in\binom Da:
J_{E,s}(I_S(w))=(0,zb)
\right}
= ======

\bigsqcup_{Q\in\mathcal L_{U,z}(w,a)}
\binom{A_w(Q)}a.
}
\tag{7}
]

Hence

[
\boxed{
#\mathscr F_z
=============

\sum_{Q\in\mathcal L_{U,z}(w,a)}
\binom{|A_w(Q)|}{a}.
}
\tag{8}
]

This is the exact diagnostic for raw-support overcounting.

Distinct listed polynomials in (U_{E,B}) have distinct full agreement supports. Indeed, if (Q,Q') have the same full agreement support of size at least (a), then (Q-Q') has at least (a) roots but

[
\deg(Q-Q')<k+t\le a,
]

so (Q=Q'). Therefore

[
\boxed{
|\mathcal L_U(w,a)|
===================

#{A_w(Q):Q\in\mathcal L_U(w,a)}.
}
\tag{9}
]

Full agreement supports, unlike raw (a)-subsets, are canonical.

---

### Theorem 3: exact scalar RS-list relationship

For (z\in F), define the received word

[
y_z(x):=\frac{w(x)-zB(x)}{E(x)}.
\tag{10}
]

Then

[
EG+zB=w\quad\text{on a set }A
\iff
G=y_z\quad\text{on }A.
]

Thus

[
\boxed{
\mathcal L_{U,z}(w,a)
;\simeq;
\left{
G\in\mathcal P_k:
|{x:G(x)=y_z(x)}|\ge a
\right}.
}
\tag{11}
]

Writing (L_{\rm RS}(y_z,a)) for the actual scalar RS list size,

[
\boxed{
Z_{E,B,w}
=========

{z:L_{\rm RS}(y_z,a)>0},
}
\tag{12}
]

and

[
\boxed{
|\mathcal L_U(w,a)|
===================

\sum_{z\in F}L_{\rm RS}(y_z,a).
}
\tag{13}
]

The corresponding full agreement supports are literally equal:

[
A_w(EG+zB)=A_{y_z}(G).
\tag{14}
]

This resolves the requested relationship to actual scalar lists:

* an individual slope fiber is an actual scalar (\operatorname{RS}[F,D,k]) list at the **original reserve (\sigma)**;
* the bad-slope count is the number of nonempty fibers;
* the one-dimensional extension list is the sum of the fiber sizes;
* the raw support cloud is the binomially weighted sum in (8).

A scalar list bound for each (y_z) alone does not bound the number of nonempty (z)-fibers. The colored line-local-limit theorem is still necessary.

---

### Automatic noncontainment

For (t\le\sigma), every witness is transverse. If some (G_0\in\mathcal P_k) explained the direction (B/E) on an (a)-set, then

[
EG_0-B
]

would have at least (a) roots but degree (<k+t\le a). It would therefore be zero, contradicting (\gcd(E,B)=1).

Thus there is no separate noncontainment loss in this branch.

---

## 2. Proof details and further exact reductions

### 2.1 Proof of the short exact sequence

The condition (\operatorname{Top}_s(P)=0) is equivalent to

[
\deg P<k+t.
]

If additionally ([P]_E=0), then (P=EG), and

[
\deg G<k.
]

Therefore

[
\ker J_{E,s}=E\mathcal P_k.
]

The domain has dimension (k+\sigma), the kernel has dimension (k), and the codomain has dimension

[
s+t=\sigma.
]

Hence (J_{E,s}) is surjective, proving (1).

If (J_{E,s}(P)\in0^s\oplus Fb), then (\deg P<k+t) and

[
[P]_E=z[B]_E.
]

Therefore (P-zB=EG) with (G\in\mathcal P_k). This proves (3) and (5).

---

### 2.2 Fat-infinity balanced completion

There is a useful geometric interpretation of (1).

Let (E^h(X,Z)) be the degree-(t) homogenization of (E), and define the degree-(\sigma) divisor on (\mathbf P^1)

[
\mathfrak D_{E,s}:=V!\left(E^h(X,Z)Z^s\right).
\tag{15}
]

It consists of the finite divisor (V(E)) together with a fat point (s\cdot\infty). The exact sequence

[
0\to\mathcal O_{\mathbf P^1}(k-1)
\xrightarrow{\cdot E^hZ^s}
\mathcal O_{\mathbf P^1}(a-1)
\to
\mathcal O_{\mathfrak D_{E,s}}(a-1)
\to0
]

gives

[
\mathcal P_a/E\mathcal P_k
\simeq
H^0!\left(\mathfrak D_{E,s},
\mathcal O_{\mathfrak D_{E,s}}(a-1)\right).
\tag{16}
]

Under the finite/infinity decomposition,

[
H^0(\mathfrak D_{E,s})
\simeq
A_E\oplus F^s.
]

The (F^s) coordinates are precisely the top coefficients of (P), up to reversal of basis.

Thus the correct balanced completion of a (t<\sigma) denominator is:

[
\boxed{
V(E)+(\sigma-t)\infty,
}
\tag{17}
]

not affine common-factor padding such as (EX^{\sigma-t}). The latter creates a descended finite component; the former is exactly the jet–residue quotient actually seen by interpolation.

---

### 2.3 Canonical colored syndrome formulation

Let (I_D:F^D\to\mathcal P_n) be full-domain interpolation. Choose

[
\rho_b:A_E\longrightarrow A_E/Fb
]

and a linear form (\ell_b:A_E\to F) satisfying (\ell_b(b)=1).

Define

[
H^{\rm JR}*{E,B}(y)
:=
\left(
\operatorname{coeff}*{k+t,\ldots,n-1}(I_D(y)),
\ \rho_b([I_D(y)]_E)
\right).
\tag{18}
]

Its target dimension is

[
(n-k-t)+(t-1)=n-k-1.
]

Moreover,

[
\boxed{
\ker H^{\rm JR}_{E,B}
=====================

\operatorname{ev}*D(U*{E,B}).
}
\tag{19}
]

Define the color functional

[
\lambda(y):=\ell_b([I_D(y)]_E).
\tag{20}
]

On (U_{E,B}), this is exactly (\lambda_B).

Let (H) be a matrix for (H^{\rm JR}_{E,B}), with columns (h_x), and write

[
\lambda(y)=\sum_{x\in D}\lambda_xy(x).
]

For (e) supported on (T), write its nonzero coordinates as
(c\in(F^\times)^T). Then the bad slopes satisfy the exact formula

[
\boxed{
Z_{E,B,w}
=========

\left{
\lambda(w)-\sum_{x\in T}\lambda_xc_x:
\begin{array}{l}
T\subseteq D,\ |T|\le j,\
c\in(F^\times)^T,\
H_Tc=H(w)
\end{array}
\right}.
}
\tag{21}
]

This is the correct canonical full-support object.

The augmented map

[
\widehat H:=(H^{\rm JR}_{E,B},\lambda)
]

has kernel

[
\boxed{
\ker\widehat H
==============

\operatorname{ev}_D(E\mathcal P_k),
}
\tag{22}
]

which is coordinatewise monomially equivalent to
(\operatorname{RS}[F,D,k]). Thus the diagram is

[
E\operatorname{RS}*k
\subset
U*{E,B},
\qquad
U_{E,B}/E\operatorname{RS}_k\simeq F.
\tag{23}
]

Equivalently, (\widehat H) is an RS parity check and (H^{\rm JR}) is its quotient along the syndrome direction of (B). The colors recover the lost syndrome coordinate.

This proves that the jet–residue construction is exactly the syndrome transverse-secant line viewed through a one-dimensional code extension.

---

### 2.4 Exact occupancy term

Let

[
R:=n-(k+1)=n-k-1=j+\sigma-1.
]

Every nonzero polynomial in (U_{E,B}) has degree (<k+t), so

[
d(U_{E,B})\ge n-k-t+1=j+s+1>j.
\tag{24}
]

Hence every (r\le j) columns of (H) are independent.

For a uniformly random syndrome, the exact average number of full-support representations of weight (r\le j) is

[
\mu_r
=====

\frac{\binom nr(Q-1)^r}{Q^R},
\qquad Q:=|F|.
\tag{25}
]

At the boundary (r=j),

[
\boxed{
\mu_j
=====

\frac{\binom nj}{Q^{\sigma-1}}
\left(1-\frac1Q\right)^j.
}
\tag{26}
]

The total actual-list occupancy is

[
\boxed{
\mu_{\le j}
===========

\frac1{Q^{j+\sigma-1}}
\sum_{r=0}^j\binom nr(Q-1)^r.
}
\tag{27}
]

Furthermore,

[
\frac{\mu_{r-1}}{\mu_r}
=======================

\frac{r}{(n-r+1)(Q-1)}.
\tag{28}
]

For a multiplicative domain (D\subseteq F^\times), (Q-1\ge n), so at fixed rate

[
\mu_{\le j}
===========

\left(1+O_\rho(n^{-1})\right)\mu_j.
\tag{29}
]

Thus the near-balanced occupancy numerator is

[
\boxed{
\frac{\binom n{k+\sigma}}{Q^{\sigma-1}},
}
\tag{30}
]

not (\binom n{k+\sigma}/Q^s). After division by the same-field slope count (Q), its normalized MCA contribution is

[
\boxed{
\frac{\binom n{k+\sigma}}{Q^\sigma}.
}
\tag{31}
]

Writing

[
\Gamma_\sigma
:=
\sigma\log_2Q-\log_2\binom n{k+\sigma},
]

one has

[
\frac{\mu_j}{Q}
===============

2^{-\Gamma_\sigma}
\left(1-\frac1Q\right)^j.
\tag{32}
]

Thus an additive (128)-bit entropy surplus pays the occupancy term at the official (2^{-128}) scale, before tangent and quotient terms.

---

### 2.5 Exact two-support jet–residue rank lemma

Let

[
V:=\mathcal P_a/E\mathcal P_k,
\qquad \dim V=\sigma,
]

and identify the target line with

[
\Lambda_b=F\overline B\subset V.
]

Let (S,S'\in\binom Da), put

[
C=S\cap S',\qquad
d=|S\setminus S'|=|S'\setminus S|,
]

and let (L_C) be the locator of (C). Define

[
K_C:=
\frac{L_C\mathcal P_d+E\mathcal P_k}{E\mathcal P_k}
\subseteq V.
]

Then

[
\boxed{
\operatorname{Im}(J_S,J_{S'})
=============================

{(u,v)\in V^2:u-v\in K_C},
}
\tag{33}
]

and

[
\boxed{
\dim K_C=\min(d,\sigma).
}
\tag{34}
]

Consequently,

[
\boxed{
\operatorname{rank}(J_S,J_{S'})
===============================

\sigma+\min(d,\sigma).
}
\tag{35}
]

The intersection with the zero-jet residue block has dimension

[
\boxed{
\dim\bigl(K_C\cap(0^s\oplus A_E)\bigr)
======================================

\begin{cases}
0,&d\le s,\
d-s,&s<d<\sigma,\
t,&d\ge\sigma.
\end{cases}
}
\tag{36}
]

For (d<\sigma), the target line is resonant exactly when

[
\boxed{
[B]*E
\in
[L_C\mathcal P*{d-s}]_E.
}
\tag{37}
]

In particular, two supports carrying different slopes must satisfy

[
d\ge s+1.
\tag{38}
]

If (d<\sigma), the two distinct-slope witnesses force a proper syndrome common envelope. In the envelope-free branch,

[
\boxed{
d(S,S')\ge\sigma
}
\tag{39}
]

for every pair of distinct slopes.

For uniformly random (w), a single support lands with probability

[
Q^{1-\sigma}.
]

For two supports at distance (d<\sigma),

[
\Pr(\text{both land})
=====================

\begin{cases}
Q^{,2-\sigma-d},&\Lambda_b\subseteq K_C,\
Q^{,1-\sigma-d},&\Lambda_b\nsubseteq K_C.
\end{cases}
\tag{40}
]

In the nonresonant case, the only simultaneous landings have the same slope. For (d\ge\sigma),

[
\Pr(\text{both land})=Q^{2-2\sigma},
\tag{41}
]

the independent value.

This exactly generalizes the Cycle 58 (t=\sigma=2) pair-rank calculation.

---

### 2.6 Critical full-support kernel certificate

Suppose (\sigma\ge2), and put

[
\ell_*:=
\left\lceil
\frac{n-k-1}{\sigma-1}
\right\rceil.
\tag{42}
]

Select (\ell_*) distinct slopes and one canonical full error support
(T_i), with coefficient vector (c_i\in(F^\times)^{T_i}), for each slope.
They satisfy

[
H_{T_i}c_i=H(w).
]

Define

[
\mathcal K_{\mathbf T}:
\bigoplus_{i=1}^{\ell_*}F^{T_i}
\longrightarrow
(F^{n-k-1})^{\ell_*-1}
]

by

[
\mathcal K_{\mathbf T}(v_1,\ldots,v_{\ell_*})
=============================================

\bigl(
H_{T_1}v_1-H_{T_{\ell_*}}v_{\ell_*},
\ldots,
H_{T_{\ell_*-1}}v_{\ell_*-1}
-H_{T_{\ell_*}}v_{\ell_*}
\bigr).
\tag{43}
]

Then

[
(c_1,\ldots,c_{\ell_*})\in\ker\mathcal K_{\mathbf T},
]

every coordinate of every (c_i) is nonzero, and the colors

[
\lambda(w)-\lambda_{T_i}c_i
]

are pairwise distinct.

Moreover,

[
\sum_i|T_i|
\le
\ell_*j
\le
(\ell_*-1)(n-k-1).
\tag{44}
]

Therefore (\mathcal K_{\mathbf T}) has at least as many rows as columns but is rank deficient.

At corrected reserve (\sigma=\Theta(n/\log n)),

[
\boxed{\ell_*=O(\log n).}
\tag{45}
]

This is the exact finite certificate the inverse theorem must classify.

---

## 2.7 Quotient/action-rank counterpacket: the full rank-(d) bucket construction

The Cycle 58 (d_M(E)=1) packet extends uniformly to (t<\sigma) and to arbitrary action rank.

Let (H\le F^\times) have order (n). Choose

[
M\mid\gcd(n,k),\qquad M>\sigma,
]

and put

[
N_M:=n/M,\qquad b_0:=k/M,\qquad \Omega:=H^M.
]

Choose (y_0\in\Omega), its (M)-fiber (C_0), and

[
T_0\subset C_0,\qquad |T_0|=\sigma.
]

For (A\in\binom{\Omega\setminus{y_0}}{b_0}), let

[
R_A(Y):=\prod_{y\in A}(Y-y).
]

Choose distinct external (M)-th powers

[
c_1,\ldots,c_d\notin\Omega,
\qquad 1\le d\le t,
]

such that

[
A\longmapsto
(R_A(c_1),\ldots,R_A(c_d))
\tag{46}
]

is injective. It suffices that the first coordinate be injective; the Cycle 58 finite collision inequality supplies such a (c_1).

Choose a squarefree (E) of degree (t) whose roots lie in the (d) external fibers (x^M=c_i), using at least one root from each. Then

[
\boxed{d_M(E)=d.}
\tag{47}
]

Put

[
B:=L_{T_0}\bmod E.
]

Map the quotient subsets into

[
F^d/F\mathbf1.
]

There are (Q^{d-1}) quotient classes, so one class (\mathcal A_0) has size at least

[
\boxed{
|\mathcal A_0|
\ge
\left\lceil
\frac{\binom{N_M-1}{b_0}}{Q^{d-1}}
\right\rceil.
}
\tag{48}
]

Choose (A_*\in\mathcal A_0), and define

[
w(X):=
L_{T_0}(X)R_{A_*}(X^M)
\quad\text{on }H,
\tag{49}
]

[
Q_A(X):=
L_{T_0}(X)
\bigl(
R_{A_*}(X^M)-R_A(X^M)
\bigr).
\tag{50}
]

Because the two quotient polynomials are monic of degree (b_0),

[
\deg Q_A\le k-M+\sigma<k.
\tag{51}
]

Moreover,

[
w-Q_A=L_{T_0}(X)R_A(X^M),
]

so the full agreement support is exactly

[
\boxed{
A_w(Q_A)=T_0\sqcup{x\in H:x^M\in A},
}
\tag{52}
]

of size (k+\sigma=a).

For (A\in\mathcal A_0),

[
R_{A_*}(c_i)-R_A(c_i)=z_A
]

is independent of (i). Hence

[
Q_A\equiv z_AB\pmod E.
\tag{53}
]

Injectivity of (46) makes the slopes (z_A) distinct. Therefore

[
\boxed{
|Z_{E,B,w}|
\ge
\left\lceil
\frac{\binom{n/M-1}{k/M}}{Q^{d_M(E)-1}}
\right\rceil.
}
\tag{54}
]

This packet has exact full supports and actual listed polynomials. It is not a raw-fiber artifact.

Important consequences:

1. (d_M(E)=1) gives the full quotient profile
   [
   \binom{n/M-1}{k/M}.
   ]

2. Even when (d_M(E)=t), an (M)-fiber quotient packet of size
   [
   \binom{n/M-1}{k/M}/Q^{t-1}
   ]
   remains possible.

3. At (t=1),
   [
   d_M(E)=1=t
   ]
   automatically, but the full quotient-profile packet survives.

Therefore the condition

[
d_M(E)<t
]

is not a complete quotient classifier for the near-balanced branch. It detects denominator action-rank defect, but quotient structure must ultimately be classified at the level of the colored code/support packet ((U_{E,B},\lambda,w)).

The quotient supports satisfy

[
d(S_A,S_{A'})=M|A\setminus A'|\ge M>\sigma,
]

so this packet survives all pairwise common-envelope stripping.

---

### Finite Cycle 58 certificate across every (t\le\sigma)

Over (F_{97}), take

[
n=16,\quad H=\langle8\rangle,\quad k=8,\quad
\sigma=3,\quad M=4,
]

[
T_0={1,22,96},\qquad c=4,
]

and the external fiber

[
{14,17,80,83}={x:x^4=4}.
]

For (t=1,2,3), respectively choose the first (t) external roots. Then:

[
\begin{array}{c|c|c|c}
t&E&B&d_4(E)\ \hline
1&X+83&89&1=t\
2&X^2+66X+44&40X+14&1<t\
3&X^3+83X^2+2X+69&
89X^2+94X+50&1<t
\end{array}
]

All three data have the same three exact full-support slopes

[
\boxed{96,\ 9,\ 80}
]

at agreement (11=k+\sigma).

This gives a literal finite test that the quotient packet persists uniformly from the balanced endpoint (t=3) down to (t=1).

---

### 2.8 Tangent/common-envelope packet and its exact ceiling

Suppose a listed subfamily lies on one affine polynomial line

[
Q_z=Q_*+zG,\qquad 0\ne G\in\mathcal P_{k+t}.
]

Let

[
C_G:={x\in D:G(x)=0},
\qquad c:=|C_G|\le k+t-1.
]

Outside (C_G), each coordinate can agree with (w) for at most one (z). Every listed (Q_z) needs at least (a-c) agreements outside (C_G). Therefore

[
\boxed{
|{z:|A_w(Q_z)|\ge a}|
\le
\left\lfloor\frac{n-c}{a-c}\right\rfloor
\le
\left\lfloor
\frac{n-k-t+1}{\sigma-t+1}
\right\rfloor.
}
\tag{55}
]

The bound is attained by taking

[
C\subset D,\quad |C|=k+t-1,\quad G=L_C,
]

choosing disjoint petals (T_i\subset D\setminus C) of size (s+1), and defining (w=z_iG) on (T_i) and (w=0) on (C).

This gives

[
\left\lfloor
\frac{j+s+1}{s+1}
\right\rfloor
]

distinct slopes with exact supports (C\cup T_i). It is always at most linear and is absorbed by the (n^{1+o(1)}) term, but it shows why that term cannot be replaced by (O(1)).

---

### 2.9 Raw-fiber test

Take (w=Q_0\in U_{E,B}). If another (Q\in U_{E,B}) agrees with (Q_0) on (a) points, then

[
\deg(Q-Q_0)<k+t\le a,
]

so (Q=Q_0). The actual list and slope set therefore have size one.

Nevertheless every (a)-subset of (D) is a raw feasible support for (Q_0):

[
|\mathscr F_{\lambda(Q_0)}|=\binom na.
]

This is the sharpest possible demonstration that raw support fibers cannot be upper-bounded in place of actual lists or full supports.

---

### 2.10 Test against the (t=2) occupancy counterpacket

At the balanced point

[
t=\sigma=2,\qquad s=0,
]

the code (U_{E,B}) has redundancy

[
R=j+1,
]

and its exact boundary occupancy is

[
\mu_j
=====

\frac{\binom nj}{Q}
\left(1-\frac1Q\right)^j.
]

The Cycle 58 high-(j) construction produces reduced nonquotient, core-clean data with

[
|Z|
===

(1-o(1))\frac{\binom nj}{Q},
]

using distinct slopes and exact full supports. Thus it saturates the jet–residue occupancy term.

It does not violate the corrected theorem. It proves that:

[
\boxed{
\text{primitive does not imply }n^{1+o(1)};
\text{ primitive only implies occupancy }+n^{1+o(1)}.
}
]

For (t=2<\sigma), the (s=\sigma-2) top-jet constraints add exactly the factor (Q^{-s}). The balanced (N/Q) packet does not automatically persist at (N/Q); the correct generic baseline becomes

[
N/Q^{\sigma-1}.
]

---

## 3. Parameter ledger

| Quantity                        |                      Exact value | Role                             |
| ------------------------------- | -------------------------------: | -------------------------------- |
| Target agreement                |                     (a=k+\sigma) | Fixed original radius            |
| Full error limit                |                   (j=n-k-\sigma) | Canonical support size           |
| Denominator degree              |                     (t\le\sigma) | Low/balanced stratum             |
| Infinity-jet depth              |                     (s=\sigma-t) | Missing residual coordinates     |
| Jet–residue dimension           |                     (s+t=\sigma) | Original entropy dimension       |
| Extension code                  | (U_{E,B}=E\mathcal P_k\oplus FB) | Actual-list code                 |
| Extension-code dimension        |                            (k+1) | Independent of (t)               |
| Extension-code redundancy       |               (n-k-1=j+\sigma-1) | Occupancy denominator            |
| Minimum distance lower bound    |                          (j+s+1) | Full-support uniqueness          |
| Boundary occupancy numerator    |         (\binom nj/Q^{\sigma-1}) | Distinct-slope main term         |
| Normalized occupancy            |             (\binom nj/Q^\sigma) | Same-field MCA error             |
| Critical arity                  | (\lceil(n-k-1)/(\sigma-1)\rceil) | (O(\log n)) at corrected reserve |
| Rank-(d) quotient packet        |     (\binom{n/M-1}{k/M}/Q^{d-1}) | Necessary quotient/action scale  |
| Tangent polynomial-line ceiling |                ((n-k-t+1)/(s+1)) | At most linear                   |

Field ledgers remain separate:

* The exact algebra above is over (F), with (Q=|F|).
* In a same-field theorem, (Q=q_{\rm gen}=q_{\rm line}).
* If (D) generates a proper subfield, (q_{\rm gen}) cannot replace (Q) without a descent or interleaved transfer theorem.
* (q_{\rm chal}) enters only in the final protocol comparison.
* The finite target is
  [
  T_*=\left\lfloor q_{\rm line}/2^{128}\right\rfloor.
  ]

A same-field ROLE 06 upper theorem would need

[
n^{1+o(1)}
+
\mu_{\le j}n^{o(1)}
+
\mathsf Q_{\rm JR}
+
\mathsf{Env}*{\rm JR}
\le T**.
\tag{56}
]

---

## 4. Route-board impact

1. **The jet–residue bridge itself is solved.**
   The correct low-denominator object is the one-dimensional code flag
   [
   E\operatorname{RS}*k\subset U*{E,B},
   ]
   together with its quotient color. It is not the full shifted code
   (\operatorname{RS}_{k+t}).

2. **The original entropy boundary is restored exactly.**
   The top jets contribute (s) constraints and the residue line contributes (t-1), for total (\sigma-1). The normalized occupancy is therefore (N/Q^\sigma).

3. **The correct balanced completion is a fat point at infinity.**
   The low branch is a balanced degree-(\sigma) principal-parts problem on
   [
   V(E)+s\infty.
   ]
   A balanced theorem that excludes all descended/fat-point data does not cover this branch.

4. **Denominator action rank alone is not a classifier.**
   The rank-(d) quotient packet shows that quotient support families pay only (d_M(E)-1) conditions, because their infinity jets vanish identically. At (t=1), (d_M(E)=t) but the full quotient profile remains.

5. **The scalar list theorem is necessary but not sufficient.**
   Each slope is an actual scalar RS list fiber, but bounding every fiber does not bound how many fibers are nonempty. ROLE 06 needs a colored line-local-limit theorem.

6. **Pairwise geometry is now completely calibrated.**
   Distances below (s+1) cannot carry distinct slopes; distances in
   (s+1,\ldots,\sigma-1) are common-envelope resonances; distances at least
   (\sigma) are pairwise generic. Quotient and occupancy packets both live in the far-support regime, so a higher-order theorem is unavoidable.

7. **The residual-safe branch remains usable.**
   For (s\ge R_{\rm list}), an actual shifted-list theorem may still be the simpler tool. The jet–residue bridge is uniform for all (s), including the overlap.

---

## 5. What remains open

The exact unproved statement is the following.

### `W-JR-PRIMITIVE-COLORED-FULL-SECANT-LOCAL-LIMIT`

In the same-field smooth-domain regime, uniformly for

[
0\le s=\sigma-t<R_{\rm list},
]

let (Z^{\rm prim}_{E,B,w}) denote the distinct colors represented by canonical full error supports after removing:

1. proper syndrome common envelopes and boundary tangent/common-polynomial-envelope containers;
2. fixed-defect (M)-fiber quotient families;
3. rank-one modules over the quotient subalgebras (F[[X^M]]), calibrated by their actual mixed jet/action rank.

Prove

[
\boxed{
|Z^{\rm prim}*{E,B,w}|
\le
n^{1+o(1)}
+
n^{o(1)}
\frac1{Q^{j+\sigma-1}}
\sum*{r=0}^j\binom nr(Q-1)^r.
}
\tag{57}
]

Equivalently,

[
|Z^{\rm prim}_{E,B,w}|
\le
n^{1+o(1)}
+
n^{o(1)}
\frac{\binom n{k+\sigma}}{Q^{\sigma-1}}.
\tag{58}
]

The inverse form should say that any violation produces a large subfamily in either:

* a proper/common-envelope container; or
* an active (M)-fiber quotient module whose effective jet–action rank is smaller than the generic (\sigma)-dimensional rank.

The quotient term must at least permit

[
\boxed{
\frac{\binom{n/M-1}{k/M}}{Q^{d_M(E)-1}},
}
\tag{59}
]

and in particular the full profile when (d_M(E)=1).

What remains unresolved is not the list canonicalization, the entropy ledger, or the local pair geometry. It is the higher-order worst-case completion bound for the (O(\log n))-arity full-coordinate kernels in (43).

The global prize also still requires the independent (t>\sigma) thick-residue/affine-plane theorem.

## Do you see a route to a full solve? ROLE 06 - t < sigma Residual / Jet-Residue / Actual-List Bridge

**Yes, for the ROLE 06 branch.** The next exact lemma should be:

### `W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION`

Fix a full-coordinate, distinct-color critical seed

[
(T_1,c_1),\ldots,(T_{\ell_*},c_{\ell_*})
]

for (H^{\rm JR}_{E,B}), with

[
H_{T_i}c_i=s_0,
\qquad
\ell_*=
\left\lceil\frac{n-k-1}{\sigma-1}\right\rceil.
]

Assume:

1. the seed is not contained in a proper syndrome envelope;
2. it does not descend, up to a fixed defect, to unions of fibers of any active (x\mapsto x^M);
3. its jet–residue variations do not lie in a lower-rank module over (F[[X^M]]);
4. all representations use their full coordinate supports.

Then the number of additional distinct colors completing this seed through the same syndrome is at most

[
\boxed{
n^{1+o(1)}+\mu_{\le j}n^{o(1)}.
}
\tag{60}
]

Conversely, an excess completion family must yield a proper envelope or an (M)-quotient/action-rank container.

The concrete proof route is:

1. Use the pair-rank lemma to remove all (d<\sigma) completions as envelope/tangent structure.
2. Represent the remaining kernel determinant in the fat-infinity divisor model
   [
   V(E)+(\sigma-t)\infty,
   ]
   giving a confluent Vandermonde/locator determinant.
3. Show that persistent determinant degeneracy on a (\sigma)-separated split-support family either factors through (X^M) or has a common-envelope factor.
4. Count all nonpersistent completions by the finite-field occupancy term.
5. Charge the (X^M) factors by the rank-(d) quotient buckets in (54).

Proving this completion lemma would close the residual-unsafe (t<\sigma) gap without using raw feasible supports and without paying the false residual entropy (Q^{-s}). It would not by itself close the (t>\sigma) branch.
