LABEL: **PROOF**

EXECUTIVE VERDICT:

Conditional only on the supplied Cycle84 finite certificate and its explicit slot-support factorization, there is a rigorous transfer to an ordinary Reed–Solomon support-wise MCA and line-decoding statement.

The strongest proved consequence is:

[
\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[\mathbb F*{17^{48}},D_\theta,232],238\bigr)
\ge
2{,}782{,}305{,}834{,}758{,}012{,}141{,}568,
]

for an existentially specified 464-point evaluation domain (D_\theta), and hence

[
\epsilon_{\rm mca}
\bigl(\operatorname{RS}[\mathbb F_{17^{48}},D_\theta,232],113/232\bigr)

>

2^{-128}.
]

This is a genuine, paper-facing finite RS-MCA theorem under `def:mca`; it also gives a non-code-contained affine line containing that many points within Hamming distance (226) of the code.

It is **not** a Proximity Prize counterpacket because (D_\theta) is an arbitrary 464-point affine-union domain, not a smooth power-of-two multiplicative subgroup or coset. It gives no ordinary list-size lower bound for one received word.

Confidence: **high**.

---

EXACT THEOREM OR OBSTRUCTION:

### Theorem A — Fixed-infinity-jet locator transfer

Let

[
C=\operatorname{RS}[\mathbb F,D,k]\subseteq \mathbb F^D,
\qquad |D|=n,\qquad r=n-k.
]

Fix

[
1\le \sigma\le r,\qquad j=r-\sigma,
\qquad \beta\in\mathbb F\setminus D.
]

Let (\mathcal T) be a family of (j)-subsets of (D), and write

[
P_T(X)=\prod_{x\in T}(X-x).
]

Assume that all (P_T) have the same first (\sigma) coefficients at infinity:

[
P_T(X)=X^j+c_1X^{j-1}+\cdots+c_{\sigma-1}X^{j-\sigma+1}
+O(X^{j-\sigma}),
]

with (c_1,\ldots,c_{\sigma-1}) independent of (T).

Then there is one affine line

[
u_z=f+zg,\qquad z\in\mathbb F,
]

and one degree-one residue-line datum

[
E=X-\beta,\qquad B=V_D(\beta),
\qquad V_D(X)=\prod_{x\in D}(X-x),
]

such that for every (T\in\mathcal T),

[
z_T=-P_T(\beta)^{-1}
]

is support-wise MCA-bad with witness support

[
S_T=D\setminus T,\qquad |S_T|=k+\sigma.
]

Moreover:

1. (g|_{S_T}) is not the restriction of a degree-(<k) polynomial, so the witness is noncontained.
2. The affine line is not contained in (C).
3. The map
   [
   P_T(\beta)\longmapsto -P_T(\beta)^{-1}
   ]
   is injective on nonzero values. Thus the supplied slope-fiber spectrum is exactly the locator-value fiber spectrum.
4. Consequently, with
   [
   \nu_\beta(\mathcal T)
   =#{P_T(\beta):T\in\mathcal T},
   \qquad \delta=j/n,
   ]
   one has
   [
   \Lambda^{\rm NC}*{1,\delta}(D,k)
   \ge \nu*\beta(\mathcal T),
   ]
   [
   \operatorname{LD}*{\rm sw}(C,k+\sigma)
   \ge \nu*\beta(\mathcal T),
   ]
   and
   [
   \epsilon_{\rm mca}(C,\delta)
   \ge \frac{\nu_\beta(\mathcal T)}{|\mathbb F|}.
   ]

These are lower bounds; the resulting line may have additional bad slopes arising from supports outside (\mathcal T).

### Cycle84 one-copy corollary

Let

[
\mathbb F_0=\mathbb F_{17}[X]/(X^{16}+X^8+3),
\qquad q_0=17^{16},
]

with the packet’s (\eta,\beta), and let

[
D_0=\langle\eta\rangle,\qquad |D_0|=256.
]

For each Cycle84 tuple, the associated co-support (T\subseteq D_0) has size (113), and its locator satisfies

[
P_T(X)=X^{113}-X^{112}+O(X^{107}).
]

Thus the common-jet hypothesis holds with

[
(n,k,r,j,\sigma)=(256,137,119,113,6).
]

Furthermore,

[
P_T(\beta)=\kappa,\Phi(T),
\qquad
\kappa=(\beta-1)3^{28}\ne0.
]

Therefore the Cycle84 product spectrum transfers without loss:

[
\operatorname{LD}_{\rm sw}
\bigl(\operatorname{RS}[\mathbb F_0,D_0,137],143\bigr)
\ge 52{,}747{,}567{,}092,
]

and

[
\epsilon_{\rm mca}
\bigl(\operatorname{RS}[\mathbb F_0,D_0,137],113/256\bigr)
\ge
\frac{52{,}747{,}567{,}092}{17^{16}}.
]

The packet witnesses retain exactly 12 double slope fibers and no fiber of size at least three.

There is also an exact rate-(1/2), smooth-domain repair. The nine points

[
F_9={\eta^{8m}:1\le m\le9}
]

are disjoint from every Cycle84 co-support. Replacing (T) by (T\cup F_9) gives

[
(n,k,j,\sigma)=(256,128,122,6)
]

and hence

[
\operatorname{LD}_{\rm sw}
\bigl(\operatorname{RS}[\mathbb F_0,D_0,128],134\bigr)
\ge 52{,}747{,}567{,}092,
]

at radius

[
\delta=\frac{122}{256}
=\frac12-\frac{3}{128}.
]

This row is genuinely on a smooth power-of-two multiplicative subgroup, but its native (q_{\rm line}=17^{16}) makes the (2^{-128}) integer target zero.

### Theorem B — Cycle84 two-copy extension-row transfer

Let

[
P=52{,}747{,}567{,}104,\qquad
N=52{,}747{,}567{,}092.
]

Remove the 24 universally unused points

[
F_{24}={\eta^{8m}:1\le m\le24}
]

and put

[
D^\flat=D_0\setminus F_{24},\qquad |D^\flat|=232.
]

Let

[
L=\mathbb F_{q_0^3}=\mathbb F_{17^{48}}.
]

There exists an element (\theta\in L\setminus\mathbb F_0) such that the projective values

[
[P_T(\theta)]\in L^\times/\mathbb F_0^\times,
\qquad T\in\mathcal T,
]

are pairwise distinct.

For such a (\theta), define

[
D_\theta
========

D^\flat
;\dot\cup;
(D^\flat+\beta-\theta).
]

Then (|D_\theta|=464), and for every ordered pair
((T_1,T_2)\in\mathcal T^2), define

[
U(T_1,T_2)
==========

T_1\cup(T_2+\beta-\theta).
]

These are 226-subsets of (D_\theta), their locators share a common six-term infinity jet, and

[
P_{U(T_1,T_2)}(\beta)
=====================

P_{T_1}(\beta)P_{T_2}(\theta).
]

The set of these locator values has cardinality exactly at least

[
NP
==

2{,}782{,}305{,}834{,}758{,}012{,}141{,}568.
]

Applying Theorem A with

[
(n,k,r,j,\sigma)
================

(464,232,232,226,6)
]

gives one ordinary RS affine line and one degree-one residue datum satisfying

[
\boxed{
\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[L,D*\theta,232],238\bigr)
\ge NP
}
]

and

[
\boxed{
\epsilon_{\rm mca}
\bigl(\operatorname{RS}[L,D_\theta,232],113/232\bigr)
\ge
\frac{NP}{17^{48}}

>

2^{-128}.
}
]

Equivalently, there is a non-code-contained affine line over (L) containing at least (NP) distinct points at Hamming distance at most (226) from this ([464,232]) RS code.

The supplied two-copy witness map still has maximum fiber size two: for every second-copy support, the first-copy Cycle84 fiber spectrum repeats inside a distinct (\mathbb F_0^\times)-coset.

---

PROOF / DISPROOF / ROUTE CUT:

### 1. Cycle84 locators have the required fixed jet

For a slot (t) and state ((i,a)), the packet’s selected 16-point set has locator

[
L_{t,i,a}(X)
============

\prod_{b\in a+E_i}
\left(X^2-\eta^{2t}3^b\right).
]

The supplied slot polynomials have zero (Y^7) and (Y^6) coefficients. Since the displayed locator is even, this gives

[
L_{t,i,a}(X)=X^{16}+O(X^{10}).
]

For seven slots,

[
Q_T(X)=\prod_{t=1}^7L_{t,i_t,a_t}(X)
=X^{112}+O(X^{106}).
]

The full Cycle84 co-support also contains the fixed point (1), so

[
P_T(X)=(X-1)Q_T(X)
=X^{113}-X^{112}+O(X^{107}).
]

Thus the six coefficients of degrees (113,112,\ldots,108) are fixed.

The slot factorization also gives

[
P_T(\beta)
==========

# (\beta-1)\prod_{t=1}^7 3^t u_t

(\beta-1)3^{28}\Phi(T).
]

The factor is common and nonzero, so color normalization causes no collision or deletion.

### 2. Syndrome realization of the fixed-jet theorem

Write

[
v(x)=(1,x,\ldots,x^{r-1})^{\mathsf T}.
]

An ordinary RS parity-check matrix can be taken with columns

[
h_x=V_D'(x)^{-1}v(x).
]

The column scalars are nonzero, so for (T\subseteq D),

[
W_T:=\operatorname{span}{h_x:x\in T}
====================================

\operatorname{span}{v(x):x\in T}.
]

A word (u) agrees with a codeword on (D\setminus T) exactly when

[
Hu\in W_T.
]

Identifying a dual vector with a polynomial (Q\in\mathbb F_{<r}[X]), one has

[
W_T^\perp
=========

P_T\mathbb F_{<\sigma}[X].
]

For (A\in\mathbb F_{<\sigma}[X]), the highest (\sigma) coefficients of
(P_TA) determine (A). Because all (P_T) have the same (\sigma)-jet, the linear map

[
A\longmapsto \operatorname{top}_\sigma(P_TA)
]

is independent of (T). It is invertible because (P_T) is monic.

Define a linear functional (\ell) on (\mathbb F_{<r}[X]) by

[
\ell(Q)
=======

\left(
\operatorname{top}*\sigma^{-1}
(\operatorname{top}*\sigma Q)
\right)(\beta).
]

Let (y_0\in\mathbb F^r) represent (\ell), and let

[
y_1=v(\beta).
]

For every (Q=P_TA\in W_T^\perp),

[
\langle Q,y_0+zy_1\rangle
=========================

A(\beta)\bigl(1+zP_T(\beta)\bigr).
]

Thus at

[
z_T=-P_T(\beta)^{-1},
]

the vector (y_0+z_Ty_1) annihilates (W_T^\perp), so

[
y_0+z_Ty_1\in W_T.
]

Choose words (f,g) with

[
Hf=y_0,\qquad Hg=y_1.
]

Then (f+z_Tg) agrees with a codeword on (S_T=D\setminus T).

### 3. Noncontainment is automatic

Since (|T|=r-\sigma), the (j+1) Vandermonde vectors

[
{v(x):x\in T}\cup{v(\beta)}
]

are linearly independent: (j+1\le r) and (\beta\notin D). Hence

[
y_1=v(\beta)\notin W_T.
]

Therefore (g) cannot agree with a codeword on (S_T). This is exactly `def:mca(ii)`, not merely a transversality surrogate.

It also follows that (g\notin C), so the complete affine line is not code-contained.

### 4. Explicit degree-one residue datum

Lagrange interpolation gives, for (0\le m<r),

[
\beta^m
=======

\sum_{x\in D}
\frac{x^mV_D(\beta)}
{(\beta-x)V_D'(x)}.
]

Thus the word

[
g(x)
====

# \frac{V_D(\beta)}{\beta-x}

-\frac{B}{E(x)},
\qquad
E=X-\beta,\quad B=V_D(\beta),
]

has syndrome (v(\beta)).

Set (w=Ef). If (c_z\in C) explains (f+zg) on (S_T), then

[
Q_z=Ec_z+zB
]

satisfies

[
\deg Q_z<k+1,\qquad
Q_z\equiv zB\pmod E,\qquad
Q_z=w\text{ on }S_T.
]

The preceding noncontainment argument is verbatim the noncontained clause of `def:residue`. The construction therefore lies directly in the paper’s (t=1) residue-line normal form.

### 5. Reciprocal-affine normalization loses nothing

All locator values are nonzero because (\beta\notin D). The map

[
x\longmapsto -x^{-1}
]

is a bijection of (\mathbb F^\times). More generally, every normalization

[
x\longmapsto a+\frac b x,\qquad b\ne0,
]

is injective on (\mathbb F^\times).

Hence the Cycle84 data transfer exactly as:

[
P\text{ supports},\qquad
N\text{ slopes},\qquad
12\text{ double fibers},\qquad
m_{\max}=2.
]

### 6. Existence of the cubic projective separator

The Cycle84 supports are distinct, hence their monic locators (P_T) are distinct.

For a pair (T\ne T') and (c\in\mathbb F_0^\times), the polynomial

[
P_T(X)-cP_{T'}(X)
]

is nonzero and has degree at most (113). Therefore the number of elements (\theta\in L) satisfying at least one projective collision

[
P_T(\theta)=cP_{T'}(\theta)
]

is at most

[
B_{\rm bad}
===========

113\binom P2(q_0-1)
]

which is

[
7{,}649{,}552{,}973{,}225{,}252{,}456{,}065{,}323{,}325{,}775{,}618{,}181{,}693{,}440.
]

Because the extension degree is prime, the number of degree-three elements of
(L/\mathbb F_0) is

[
q_0^3-q_0
=========

115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}602{,}504{,}327{,}802{,}018{,}460{,}160.
]

The latter is strictly larger, so a degree-three (\theta) with projective injectivity exists.

### 7. Two-copy product separation

For this (\theta),

[
D^\flat\cap(D^\flat+\beta-\theta)=\varnothing,
]

because an intersection would imply (\theta\in\mathbb F_0).

Translation preserves equality of the top six locator coefficients, and multiplying two common-six-jet degree-113 families gives a common-six-jet degree-226 family.

At (\beta),

[
P_{U(T_1,T_2)}(\beta)
=====================

P_{T_1}(\beta)P_{T_2}(\theta).
]

Let

[
\Omega={P_T(\beta):T\in\mathcal T}\subseteq\mathbb F_0^\times,
\qquad |\Omega|=N.
]

For fixed (T_2), the set

[
\Omega P_{T_2}(\theta)
]

has (N) elements. For different (T_2,T_2'), these sets lie in different
(\mathbb F_0^\times)-cosets, by projective injectivity. Therefore they are disjoint and their union has (NP) elements.

This removes the conservative factor (1/2) appearing in the Cycle88/89 audited row.

### 8. GRS versus RS

No GRS-to-RS assumption is needed: the proof above uses the ordinary unweighted RS code. The dual multipliers (V_D'(x)^{-1}) occur only in a parity-check matrix.

For completeness, diagonal scaling is exact for this predicate. If

[
C'=\Delta C
]

for a nonzero diagonal matrix (\Delta), then

[
(f,g,C)\longmapsto(\Delta f,\Delta g,\Delta C)
]

preserves:

* support-wise agreement on each (S);
* simultaneous explainability of (f) and (g);
* Hamming distance;
* the slope parameter (z);
* code-line containment.

Thus a genuine GRS version would transfer to RS with no numerator loss.

### 9. Line decoding versus list decoding

The M2 bridge gives the exact identity

[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{\operatorname{LD}_{\rm sw}
(C,\lceil(1-\delta)n\rceil)}
{|\mathbb F|}.
]

Moreover, each support-wise bad slope is an ordinary code-close point of the affine line. Hence the two-copy theorem also proves

[
#{z\in L:
d_H(f+zg,C)\le226}\ge NP.
]

It does **not** produce one received word with (NP) nearby codewords. Therefore no lower bound of (NP) on the ordinary RS list size follows.

### 10. Prize-family route cut

The two-copy theorem clears the correct numerical target:

[
q_{\rm line}
============

# 17^{48}

115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641,
]

[
\left\lfloor \frac{q_{\rm line}}{2^{128}}\right\rfloor
======================================================

338{,}617{,}018{,}271{,}848{,}945{,}628,
]

and

[
NP-
\left\lfloor \frac{q_{\rm line}}{2^{128}}\right\rfloor
======================================================

2{,}443{,}688{,}816{,}486{,}163{,}195{,}940.
]

Thus

[
\frac{NP}{q_{\rm line}}
\approx 2^{-124.961445}
=8.21667\ldots\times2^{-128}.
]

But

[
|D_\theta|=464=16\cdot29
]

is not a power of two, and (D_\theta) is not supplied as a multiplicative subgroup or coset.

Nor can one simply pad the construction to an order-512 subgroup in the same field:

[
v_2(17^{48}-1)
==============

v_2(16)+v_2(18)+v_2(48)-1
=8.
]

Hence (\mathbb F_{17^{48}}^\times) has no subgroup of order (512). The direct 464-to-512 smooth-domain repair is impossible.

---

FIELD AND PARAMETER LEDGER:

| Row                      | (q_{\rm gen}) | (q_{\rm code}) | (q_{\rm line}) | (q_{\rm chal}) | ((n,k,\sigma,j))  | Status                                          |
| ------------------------ | ------------: | -------------: | -------------: | -------------- | ----------------- | ----------------------------------------------- |
| Native Cycle85           |     (17^{16}) |      (17^{16}) |      (17^{16}) | Unused         | ((256,137,6,113)) | Exact finite RS-MCA transfer                    |
| Rate-(1/2) smooth repair |     (17^{16}) |      (17^{16}) |      (17^{16}) | Unused         | ((256,128,6,122)) | Smooth RS row; native (2^{-128}) target is zero |
| Two-copy row             |     (17^{48}) |      (17^{48}) |      (17^{48}) | Unused         | ((464,232,6,226)) | Paper-facing arbitrary-domain RS-MCA theorem    |

For the two-copy row, (q_{\rm gen}=17^{48}) is genuine, not bookkeeping:

* (D^\flat) contains (\eta);
* (\operatorname{ord}*{256}(17)=16), so (\mathbb F*{17}(\eta)=\mathbb F_0);
* the translated block and (\mathbb F_0) recover (\theta);
* hence the domain generates (L=\mathbb F_{17^{48}}).

The MCA denominator is (q_{\rm line}), not (q_{\rm gen}), (q_{\rm code}), or (q_{\rm chal}). Here the first three happen to agree. No protocol challenge experiment was supplied, so (q_{\rm chal}) is not used and must not be inserted into the denominator.

---

SELF-AUDIT:

1. **Exact implication proved.**
   The Cycle84 support/product packet implies a single (t=1) residue line with (N) support-wise bad slopes in one copy, and an existential ([464,232]) ordinary RS line over (\mathbb F_{17^{48}}) with at least (NP) support-wise bad slopes.

   **Not proved:** an official smooth-domain Proximity Prize counterpacket, a positive MCA upper theorem, or an ordinary list-size lower bound for one received word.

2. **Claim level.**
   This is a **paper-facing finite RS-MCA/support-wise-line-decoding proof**, not merely a model certificate. The two-copy conclusion directly satisfies `def:mca` and `def:residue`. It is not official-prize dispositive because of the domain-family restriction.

3. **First failure line in the prize chain.**
   The first unproved line is
   [
   \text{arbitrary translated 464-point domain}
   \Longrightarrow
   \text{admissible smooth power-of-two subgroup/coset domain}.
   ]
   The finite-product-to-slope, support-wise MCA, residue-line, GRS-to-RS, and (q_{\rm line}) arrows are proved.

4. **Field and (2^{-128}) use.**
   The nontrivial comparison uses
   [
   q_{\rm line}=17^{48}
   ]
   and the exact integer target
   [
   \lfloor q_{\rm line}/2^{128}\rfloor.
   ]
   (q_{\rm chal}) is unused. The native (17^{16}) row is not advertised as clearing a meaningful (2^{-128}) frontier.

5. **Numerator-loss audit.**

   * Reciprocal-affine normalization: no loss.
   * Affine color normalization: no loss; the scalar (\kappa) is common and nonzero.
   * Base same-slope collisions: exactly the 12 certified double fibers are paid by using (N), not (P).
   * Two-copy cross-block collisions: absent by projective separation.
   * Contained incidences: absent because (v(\beta)\notin W_T).
   * Endpoint loss: absent; all slopes are finite and (E=X-\beta) is nonzero on the domain.
   * Tangent loss: absent; (B=V_D(\beta)\ne0) and the direction is not code-explainable on the witness support.
   * Quotient/periodic structure: raw `def:mca` does not quotient these slopes out, so it cannot reduce the proved MCA numerator. A separate official charged/aperiodic source contract might classify some slopes as nonfree; no claim about that charged numerator is made.

6. **Why this is not labeled COUNTERPACKET.**
   It refutes any all-domain RS claim asserting a (2^{-128}) bound at these exact parameters, but the packet’s official prize family is narrower. Calling it a Proximity Prize counterpacket would therefore overstate the result.

---

NEXT EXACT STEP:

The exact missing theorem is:

[
\boxed{\texttt{L-C115-SMOOTH-SUBGROUP-FIXED-JET-FUSION}}
]

It must construct, from the Cycle84 packet, an official smooth-domain family with the following contract:

1. a permitted field (K) and a power-of-two subgroup or coset (H\subseteq K^\times);
2. an official rate, preferably (k=|H|/2);
3. a point (\beta'\notin H);
4. a family (\mathcal U) of
   [
   j=|H|-k-\sigma
   ]
   element co-supports whose locators share a common (\sigma)-jet;
5. more than
   [
   \left\lfloor |K|/2^{128}\right\rfloor
   ]
   distinct values (P_U(\beta')), after any source-required quotient, periodic, endpoint, tangent, containment, or affine-color charges;
6. an explicit ledger for (q_{\rm gen},q_{\rm code},q_{\rm line}), with (q_{\rm chal}) excluded unless a protocol transfer theorem supplies it.

Theorem A would then turn that output immediately into an official support-wise RS-MCA and line-decoding counterpacket.

A secondary replay step is:

[
\texttt{V-C115-CUBIC-PROJECTIVE-SEPARATOR-MATERIALIZATION},
]

which would materialize one concrete (\theta), the 464-point domain, and its projective-separation digest. That would make the present arbitrary-domain theorem a fully explicit finite certificate, but it would not remove the smooth-domain route cut.
