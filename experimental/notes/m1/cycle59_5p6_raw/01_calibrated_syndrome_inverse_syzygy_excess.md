# BANKABLE_LEMMA

I do not have a proof of the calibrated transverse-secant inverse. I do have a new exact reduction that substantially narrows the missing theorem: a large transverse slope packet is possible only when an associated split-locator syzygy bundle has positive (\sigma)-excess. This criterion is denominator-free, deterministic, and maximum-over-lines.

## 1. Exact theorem/lemma

Let

[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,
]
[
r=n-k,\qquad a=k+\sigma,\qquad j=r-\sigma=n-a.
]

Use the standard syndrome pairing between (F^r) and (F[X]_{<r}). For a (j)-set (T\subseteq L), put

[
p_T(X)=\prod_{x\in T}(X-x).
]

Then

[
V_T^\perp=p_TF[X]_{<\sigma}.
]

Consider a syndrome line

[
\ell(z)=u+zv.
]

Select distinct transverse bad slopes (z_1,\dots,z_m), and for each (z_i) select one exact (j)-set (T_i) such that

[
u+z_i v\in V_{T_i},
\qquad
v\notin V_{T_i}.
]

Write (p_i=p_{T_i}).

### Lemma 1: exact packet Macaulay criterion

Define

[
\Psi_{\mathcal P}:
\bigoplus_{i=1}^m F[X]*{<\sigma}
\longrightarrow
F[X]*{<r}^{,2}
]

by

[
\Psi_{\mathcal P}\bigl((Q_i)_i\bigr)
====================================

\left(
\sum_i p_iQ_i,,
\sum_i z_ip_iQ_i
\right).
\tag{1}
]

Then the vector space of syndrome pairs realizing every selected incidence is exactly

[
\mathcal C(\mathcal P)
======================

\left(\operatorname{coker}\Psi_{\mathcal P}\right)^*.
\tag{2}
]

In particular, the selected packet can be realized by a nonzero syndrome pair only if

[
\Psi_{\mathcal P}\text{ is not surjective}.
\tag{3}
]

This is an exact statement, not a dimension heuristic.

---

### Lemma 2: deterministic two-core extraction

Assume the syndrome plane

[
U=\operatorname{span}(u,v)
]

is not contained in any proper column envelope (V_R), (|R|<r).

Let (S_i=L\setminus T_i), so (|S_i|=a). Starting from the hypergraph with edges (S_i), repeatedly remove an edge that contains a vertex of current degree one.

At most (n) edges are removed. Thus either

[
m\le n,
]

or there is a subpacket (\mathcal P_0) of size

[
m_0\ge m-n
\tag{4}
]

with the following properties.

Let

[
C_0=L\setminus\bigcup_{i\in\mathcal P_0}S_i
=\bigcap_{i\in\mathcal P_0}T_i.
]

After deleting (C_0) from the domain and factoring

[
p_i=p_{C_0},\widetilde p_i,
]

we have parameters

[
n_0=n-|C_0|,\qquad
j_0=j-|C_0|,\qquad
r_0=r-|C_0|=j_0+\sigma,
\tag{5}
]

and:

1. every point of the reduced domain belongs to at least two of the agreement supports (S_i);
2. the reduced compatible syndrome pair is nonzero;
3. transversality is preserved;
4. because the original line is envelope-free,

   [
   |T_i\setminus T_h|\ge \sigma
   \qquad(i\ne h).
   \tag{6}
   ]

The bound of (n) removed slopes is exact: each removed edge is charged to a distinct degree-one vertex.

---

### Lemma 3: exact syzygy-excess formula

Homogenize the reduced locators to binary forms

[
P_i(X_0,X_1)\in F[X_0,X_1]_{j_0}.
]

Form the (2\times m_0) split-locator matrix

[
M_{\mathcal P_0}
================

\begin{pmatrix}
P_1 & P_2 & \cdots & P_{m_0}\
z_1P_1 & z_2P_2 & \cdots & z_{m_0}P_{m_0}
\end{pmatrix}.
\tag{7}
]

Because each reduced domain point is active in at least two supports, and the (z_i) are distinct, this matrix has rank two at every point of (\mathbf P^1). Hence there is an exact vector-bundle sequence

[
0\longrightarrow\mathcal K
\longrightarrow
\mathcal O_{\mathbf P^1}(-j_0)^{m_0}
\xrightarrow{,M_{\mathcal P_0},}
\mathcal O_{\mathbf P^1}^{,2}
\longrightarrow0.
\tag{8}
]

Write the Birkhoff–Grothendieck splitting as

[
\mathcal K
\simeq
\bigoplus_{\nu=1}^{m_0-2}
\mathcal O_{\mathbf P^1}(-j_0-d_\nu).
\tag{9}
]

Then

[
d_\nu\ge0,
\qquad
\sum_{\nu=1}^{m_0-2}d_\nu=2j_0.
\tag{10}
]

Define the (\sigma)-syzygy excess

[
\operatorname{Exc}*{\sigma}(\mathcal P_0)
:=
\sum*{\nu=1}^{m_0-2}(d_\nu-\sigma)_+.
\tag{11}
]

Then

[
\boxed{
\dim_F\mathcal C(\mathcal P_0)
==============================

\operatorname{Exc}_{\sigma}(\mathcal P_0).
}
\tag{12}
]

Consequently every nonzero envelope-free two-core packet satisfies

[
\boxed{
\operatorname{Exc}*{\sigma}(\mathcal P_0)>0,
\qquad
\max*\nu d_\nu\ge \sigma+1.
}
\tag{13}
]

This is the new exact obstruction.

A packet with

[
d_\nu\le \sigma\quad\text{for all }\nu
\tag{14}
]

cannot occur on any nonzero syndrome line, regardless of the anchor.

---

### Finite balanced-splitting corollary

If the syzygy degrees of the reduced packet are balanced—differing by at most one—then

[
\max_\nu d_\nu
==============

\left\lceil\frac{2j_0}{m_0-2}\right\rceil.
]

Combining this with (13) gives

[
m_0
\le
1+\left\lceil\frac{2j_0}{\sigma}\right\rceil.
\tag{15}
]

Therefore, under balanced locator-syzygy splitting,

[
\boxed{
|\operatorname{Bad}_j(\ell)|
\le
n+1+\left\lceil\frac{2j}{\sigma}\right\rceil.
}
\tag{16}
]

At the corrected reserve (\sigma=\Theta(n/\log q)), the last term is (O(\log q)). Thus balanced locator-syzygy packets are much smaller than the required (n^{1+o(1)}) allowance.

The relevant balance condition is not merely balanced right minimal indices of the original Hankel pencil. It is balance of the selected split-locator syzygy bundle (8).

---

## 2. Proof details

### 2.1 Syndrome incidence gives the Macaulay map

Since

[
V_{T_i}^{\perp}=p_iF[X]_{<\sigma},
]

the incidence (u+z_iv\in V_{T_i}) is equivalent to

[
(u+z_iv)(p_iQ)=0
\qquad
\text{for all }Q\in F[X]_{<\sigma}.
\tag{17}
]

For a tuple ((Q_i)),

[
u!\left(\sum_i p_iQ_i\right)
+
v!\left(\sum_i z_ip_iQ_i\right)
===============================

\sum_i(u+z_iv)(p_iQ_i).
]

Thus ((u,v)) realizes all incidences exactly when it annihilates the image of (1). This proves (2).

No denominator degree occurs anywhere in this construction.

---

### 2.2 Why common locator factors may be removed

Suppose every selected (T_i) contains a common set (C_0), with locator (g=p_{C_0}). Write (p_i=g\widetilde p_i) and define reduced functionals

[
\widetilde u(H)=u(gH),\qquad
\widetilde v(H)=v(gH).
]

If both reduced functionals were zero, then (u) and (v) would annihilate

[
gF[X]_{<r-|C_0|}
================

V_{C_0}^{\perp}.
]

Hence

[
u,v\in V_{C_0},
]

so (U\subseteq V_{C_0}). Since (|C_0|\le j<r), this would be a proper common envelope, contrary to the envelope-free hypothesis.

Therefore common locator roots can be stripped while retaining a nonzero compatible syndrome line.

---

### 2.3 Why the two-core matrix is basepoint-free

At (x\in L),

[
P_i(x)\ne0
\iff
x\in S_i.
]

After peeling, every remaining point lies in at least two (S_i). Hence at least two matrix columns are nonzero at (x). Their constant direction vectors

[
(1,z_i),\qquad(1,z_h)
]

are independent because (z_i\ne z_h). Thus (M_{\mathcal P_0}(x)) has rank two.

Outside (L), none of the (P_i) vanish. At infinity, all homogenized monic locators are nonzero. Therefore the matrix has rank two over the algebraic closure at every point of (\mathbf P^1).

---

### 2.4 Cohomology computes the exact obstruction

Twist (8) by (\mathcal O(r_0-1)). Since (r_0=j_0+\sigma),

[
0\to
\bigoplus_\nu
\mathcal O(\sigma-1-d_\nu)
\to
\mathcal O(\sigma-1)^{m_0}
\to
\mathcal O(r_0-1)^2
\to0.
\tag{18}
]

The map on global sections is precisely the homogenization of (\Psi_{\mathcal P_0}).

Because

[
H^1(\mathbf P^1,\mathcal O(\sigma-1))=0,
]

its cokernel is

[
\bigoplus_\nu
H^1!\left(\mathbf P^1,\mathcal O(\sigma-1-d_\nu)\right).
]

Using

[
\dim H^1(\mathbf P^1,\mathcal O(t))
===================================

\max(0,-t-1),
]

we obtain

[
\dim\operatorname{coker}\Psi_{\mathcal P_0}
===========================================

\sum_\nu(d_\nu-\sigma)_+.
]

This proves (12).

The degree identity follows from (8):

[
-\sum_\nu(j_0+d_\nu)=-m_0j_0,
]

and therefore

[
\sum_\nu d_\nu
==============

# m_0j_0-(m_0-2)j_0

2j_0.
]

---

### 2.5 Check against the Cycle 58 mixed-scroll packet

For the (F_{17}) packet in `02_locator_scroll_circuit_inverse.md`,

[
n=8,\qquad k=2,\qquad \sigma=2,\qquad j=4,\qquad m=11.
]

Its agreement-incidence degrees are

[
4,4,5,5,6,6,7,7,
]

so it is already a basepoint-free two-core with no common locator root.

Finite-field row reduction of its Macaulay maps gives cokernel dimensions

[
\begin{array}{c|ccc}
\text{coefficient degree }s&0&1&2\ \hline
\dim\operatorname{coker}\Psi_s&2&1&0.
\end{array}
]

The corresponding syzygy degrees are

[
(d_\nu)
= ======

(3,1,1,1,1,1,0,0,0).
]

They sum to (8=2j), and

[
\operatorname{Exc}_2
====================

(3-2)=1.
]

Thus the exact invariant detects the known mixed-Kronecker obstruction with one-dimensional excess. This also shows that positive syzygy excess is not automatically a quotient packet at small (\sigma); an entropy-scale inverse theorem is genuinely required.

---

## 3. Parameter ledger

For the same-field calibrated theorem, set

[
q=q_{\rm gen}=q_{\rm line}=|F|,
\qquad
N=\binom nj=\binom n{k+\sigma}.
]

The unavoidable line-occupancy term is

[
B_{\rm occ}
===========

\frac{N}{q^{\sigma-1}}.
\tag{19}
]

Equivalently, the normalized MCA contribution is

[
\frac{N}{q^\sigma}.
]

Under a fixed multiplicative entropy margin

[
\sigma\log_2q
\ge
(1+\varepsilon)\log_2N
]

and (\log q=o(n)),

[
B_{\rm occ}
===========

# q,2^{-(\sigma\log_2q-\log_2N)}

2^{-\Omega(n)}.
]

For quotient exceptions, the invariant is not the syntactic condition (E=E_0(X^M)). For a reduced minimal residue chart of intrinsic degree (t), write

[
A_E=F[X]/(E),\qquad \xi=[X],
]

and define

[
d_M(E)
======

# \deg\minpoly_F(\xi^M)

\dim_FF[\xi^M].
\tag{20}
]

An action-rank defect is

[
d_M(E)<t.
]

It becomes a chargeable MCA template when a large witness subpacket aligns with a rank-one module over (F[\xi^M]). The concrete full-profile model is

[
S_A=T_0\sqcup\pi_M^{-1}(A),
\qquad
\pi_M(x)=x^M,
]

with locators of the form

[
p_A(X)=R_{T_0}(X)Q_A(X^M).
]

The punctured-fiber construction proves that arbitrary-anchor MCA requires the full quotient-profile charge

[
2^{\mathcal Q_H(\sigma/n)+o(\mathcal Q_H)},
\tag{21}
]

not

[
2^{(\beta/H_2)\mathcal Q_H}.
]

The latter is too small.

The new syzygy lemma itself is valid over any field and any distinct evaluation domain. Smooth multiplicativity is needed only in the still-open classification of positive syzygy excess and in charging the quotient/action packets.

---

## 4. Route-board impact

The all-denominator wall can now be replaced by the more precise packet-level wall

[
\boxed{
\texttt{W-MCA-CALIBRATED-SPLIT-LOCATOR-SYZYGY-EXCESS-INVERSE}.
}
]

For an envelope-free line, select one witness per distinct slope. After losing at most (n) slopes and stripping a common error-coordinate core, every surviving packet is:

[
\begin{aligned}
&\text{basepoint-free},\
&\sigma\text{-separated in exchange distance},\
&\operatorname{Exc}_{\sigma}>0.
\end{aligned}
]

Therefore it is enough to prove the following finite theorem:

[
\boxed{
|\mathcal P|
\le
n^{1+o(1)}
+
O!\left(\frac{\binom nj}{q^{\sigma-1}}\right)
}
\tag{22}
]

for every basepoint-free, (\sigma)-separated, quotient-action-clean split-locator packet satisfying

[
\operatorname{Exc}_{\sigma}(\mathcal P)>0.
\tag{23}
]

Aligned action-rank packets are then added with the full-profile charge (21).

This reduction is stronger than the previous multi-minor formulation in three respects:

1. It removes the anchor and denominator from the remaining extremal problem.
2. It gives an exact necessary-and-sufficient linear invariant for incidence realizability.
3. It identifies the obstruction as an unbalanced syzygy summand of degree at least (\sigma+1), rather than an unspecified failure of character cancellation.

It also explains the failure of several earlier routes. Pairwise support separation only says the degree-(\sigma) spaces (p_iF[X]_{<\sigma}) intersect trivially pairwise. A line exists because their graph sum has a global high-degree syzygy; pairwise geometry cannot see that obstruction.

---

## 5. What remains open

The calibrated inverse is not proved. The remaining mathematical problem is now:

> Classify large basepoint-free families of fully (L)-split forms (P_i), with distinct labels (z_i), whose matrix ((P_i,z_iP_i)) has a syzygy degree exceeding (\sigma).

The required classification must prove that excess beyond

[
n^{1+o(1)}+\frac{N}{q^{\sigma-1}}
]

comes from one of:

[
\begin{aligned}
&\text{an aligned }F[X^M]\text{ or low-}d_M\text{ module},\
&\text{a common-envelope or tangent degeneration},\
&\text{a declared finite-surplus/occupancy packet}.
\end{aligned}
]

Positive syzygy excess by itself is not enough to infer quotient structure—the Cycle 58 (F_{17}) packet is a finite counterexample to that overstatement. The missing theorem must use the corrected reserve and the smooth multiplicative domain.

The external common-envelope branch also remains to be charged quantitatively. The fixed-envelope internal branch is only linear, but witnesses with (|R\cup T|>r) are not covered by that argument.

Extension-field lines require a separate multiplication-slice theorem. Nothing above permits (q_{\rm line}) or (q_{\rm chal}) to pay the (q_{\rm gen}) entropy bill.

## Do you see a route to a full solve? ROLE 01 - Prove The Calibrated Syndrome Transverse-Secant Inverse

**Yes, with moderate confidence.** The next exact lemma is:

> **Calibrated syzygy-excess inverse.**
> Let (L=\alpha H) be a smooth multiplicative domain at an official rate. Let (\mathcal P={(z_i,T_i)}) be a basepoint-free packet of distinct slopes and (j)-set locators satisfying
> [
> |T_i\setminus T_h|\ge\sigma,
> \qquad
> \operatorname{Exc}_{\sigma}(\mathcal P)>0.
> ]
> Assume no reduced minimal chart has an aligned quotient-action defect
> [
> d_M(E)<\deg E
> ]
> for an active (M\mid\gcd(n,k)), and assume no tangent/common-envelope packet. Then
> [
> |\mathcal P|
> \le
> n^{1+o(1)}
> +
> O!\left(
> \frac{\binom n{k+\sigma}}{q^{\sigma-1}}
> \right).
> ]

A proof should attack the Harder–Narasimhan summand with (d_\nu>\sigma): show that, over a smooth multiplicative root set, such a long syzygy either factors through (X^M) or supports only the calibrated occupancy number of split locator columns.

A decisive counterconstruction would instead be a fixed-margin sequence of basepoint-free, (\sigma)-separated packets with

[
\operatorname{Exc}_{\sigma}>0,
\qquad
|\mathcal P|\gg
n^{1+o(1)}+\frac{N}{q^{\sigma-1}},
]

while all (d_M) are full and no large subpacket lies in a rank-one (F[X^M])-module. No packet in the supplied context meets those conditions.
