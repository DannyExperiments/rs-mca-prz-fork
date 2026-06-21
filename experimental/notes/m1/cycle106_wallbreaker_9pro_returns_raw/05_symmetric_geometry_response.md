ROUTE_CUT

**Verdict:** the literal Zariski-closure/degree route cannot yield the required uniform bound. There is, however, an exact smaller replacement: a bounded weighted-degree elimination theorem whose exceptional locus must be identified with the formally charged periodic locus.

### 1. Why ordinary closure fails

Put (d=\sigma+1) and work over (K=\overline{\mathbb F}_p).

For fixed (n,s,d), (M_s\subset K^d) is finite. Hence its reduced Zariski closure is exactly (M_s), and every irreducible component is a point. Therefore

[
\Gamma\text{ is not contained in a positive-dimensional component of }\overline{M_s}
]

is automatically true for every (\widehat U), periodic or aperiodic. It contains no quantitative information.

The two obvious repairs also fail:

1. If one drops the conditions (x_i^n=1) and lets the (s) roots vary freely, the map

   [
   (x_1,\ldots,x_s)\longmapsto
   \bigl((-1)^\ell e_\ell(x_1,\ldots,x_s)\bigr)_{\ell=1}^d
   ]

   is dominant whenever (s\ge d). For (s=d), its Jacobian is a Vandermonde; for (s>d), fix the last (s-d) roots and use the triangular invertibility of multiplication by their locator modulo (X^{d+1}). Thus this relaxed closure is all of (K^d), and contains every (\Gamma).

2. The degree of the literal finite closure is unusably large. When (s=d), the displayed prefix is the entire degree-(d) locator, so the subset map is injective:

   [
   |M_d|=\deg M_d=\binom nd.
   ]

   This is superpolynomial for growing (d), even though Cycle103 proves the actual (s=d) incidence is only (O(nd)). Thus ordinary Bézout loses exactly the structure one needs. Quotienting by the (H)-scaling action can reduce this example by at most a factor (n), which does not repair the loss.

So the closure/degree approach is cut, not the broader elimination approach.

---

## 2. Exact finite geometry of (M_s)

Introduce full locator coordinates (Y_1,\ldots,Y_s):

[
A_Y(X)=1+Y_1X+\cdots+Y_sX^s.
]

Define inverse coefficients (c_r(Y)) by

[
A_Y(X)^{-1}=\sum_{r\ge0}c_r(Y)X^r,
\qquad c_0=1.
]

Give (Y_j) weight (j). Then (c_r) is weighted-homogeneous of weight (r).

### Full-divisor presentation

The full coefficient vectors of the (s)-subsets of (\mu_n) are exactly the zero set of

[
J_{n,s}
=======

\left(
c_{n-s+1},c_{n-s+2},\ldots,c_{n-1},c_n-1
\right).
\tag{2.1}
]

Indeed, for (A_S(X)=\prod_{x\in S}(1-xX)),

[
\frac{1-X^n}{A_S(X)}
====================

\prod_{x\in\mu_n\setminus S}(1-xX)
]

has degree (n-s). Hence (c_{n-s+1}=\cdots=c_{n-1}=0) and (c_n=1).

Conversely, if these equations hold and

[
B_Y(X)=\sum_{r=0}^{n-s}c_r(Y)X^r,
]

the inverse recurrence gives

[
A_Y(X)B_Y(X)=1-X^n.
]

Since (1-X^n) is split and squarefree, (A_Y) is exactly the locator of an (s)-subset of (\mu_n).

Consequently, for the projection to the first (d) coefficients,

[
I(M_s)
======

\sqrt{J_{n,s}}\cap K[Y_1,\ldots,Y_d].
\tag{2.2}
]

This is the exact squarefree-divisor elimination ideal; it replaces an arbitrary finite-point description of (M_s).

Complement duality is simply truncated inversion:

[
\iota(Y_1,\ldots,Y_d)
=====================

(c_1(Y),\ldots,c_d(Y)).
]

Each (\iota_j) has weight (j), and (\iota) is an involutive weighted-triangular automorphism satisfying

[
\iota(M_s)=M_{n-s}.
\tag{2.3}
]

---

## 3. A sharp low-weight relation barrier

This is the strongest unconditional geometric obstruction I can prove.

### Lemma: relation-free range

Suppose (d\le s). If

[
0\ne F\in I(M_s)
]

has weighted degree (D), then

[
D\ge n-s+1.
\tag{3.1}
]

#### Proof

Pull (F) back to (s) ordered roots:

[
Q(x_1,\ldots,x_s)
=================

F\bigl((-1)e_1(x),\ldots,(-1)^de_d(x)\bigr).
]

Every monomial of weighted degree at most (D) pulls back to a polynomial of total degree at most (D), hence of degree at most (D) in each (x_i).

Because (F) vanishes on (M_s), (Q) vanishes on every tuple of distinct elements of (H=\mu_n). Let

[
\Delta(x)=\prod_{i<j}(x_i-x_j).
]

Then (Q\Delta) vanishes on all of (H^s): on distinct tuples because (Q=0), and on repeated tuples because (\Delta=0). Moreover,

[
\deg_{x_i}(Q\Delta)\le D+s-1.
]

If (D\le n-s), every individual degree is (<n). Tensor-product interpolation on the (n)-point grid (H^s) therefore gives (Q\Delta=0) identically. Since the polynomial ring is a domain, (Q=0). But (e_1,\ldots,e_d) are algebraically independent for (d\le s), forcing (F=0), a contradiction. ∎

Applying complement duality gives:

[
d\le \min(s,n-s)
\quad\Longrightarrow\quad
\boxed{
\operatorname{wdeg}F\ge \max(s,n-s)+1
}
\tag{3.2}
]

for every nonzero (F\in I(M_s)).

Thus central layers admit no constant-degree or sublinear-degree algebraic separator. This rigorously cuts any proposed “fixed-degree hypersurface containing (M_s)” argument.

---

## 4. Correct replacement: bounded weighted-degree closure

For (D\ge0), define

[
I_{s,\le D}
===========

{F\in I(M_s):\operatorname{wdeg}F\le D},
]

and the finite-degree closure

[
\operatorname{Cl}^{,w}_D(M_s)
=============================

V(I_{s,\le D}).
\tag{4.1}
]

Unlike the literal Zariski closure, this can have positive-dimensional components, and those components are exactly relevant to a large curve intersection.

### Bounded-closure incidence lemma

Let

[
L=
#{\theta\in\mathbb F_p:\Gamma_{\widehat U}(\theta)\in M_s}.
]

Then

[
\boxed{
L>D
\quad\Longrightarrow\quad
\Gamma_{\widehat U}(K)
\subseteq
\operatorname{Cl}^{,w}_D(M_s).
}
\tag{4.2}
]

Equivalently,

[
\boxed{
\Gamma_{\widehat U}
\not\subseteq
\operatorname{Cl}^{,w}_D(M_s)
\quad\Longrightarrow\quad
L\le D.
}
\tag{4.3}
]

#### Proof

For (F\in I_{s,\le D}), set

[
h_F(T)=F(g_1(T),\ldots,g_d(T)).
]

Because (\deg g_j\le j),

[
\deg_T h_F\le\operatorname{wdeg}F\le D.
]

Every active (\theta) is a root of (h_F). If there are more than (D) distinct active parameters, then (h_F\equiv0). This holds for every (F\in I_{s,\le D}), proving the containment.

This argument counts distinct (\theta), not witnesses or weighted fibers. ∎

Complement duality preserves the construction:

[
\iota\bigl(\operatorname{Cl}^{,w}_D(M_s)\bigr)
==============================================

\operatorname{Cl}^{,w}*D(M*{n-s}).
\tag{4.4}
]

---

## 5. Relations exist generically, but aperiodicity must control the exceptions

Let (N_s=|M_s|). Choose

[
m=\lfloor N_s^{1/d}\rfloor+1.
]

The (m^d>N_s) monomials

[
Y_1^{\alpha_1}\cdots Y_d^{\alpha_d},
\qquad 0\le\alpha_j<m,
]

are linearly dependent as functions on (M_s). Therefore (I(M_s)) contains a nonzero relation of weighted degree at most

[
D_0
===

\frac{d(d+1)}2(m-1)
\le
\frac{d(d+1)}2,2^{n/d}.
\tag{5.1}
]

For any fixed nonzero such relation (F), the condition

[
F(g_1(T),\ldots,g_d(T))\equiv0
\tag{5.2}
]

is a proper algebraic condition on ((u_1,\ldots,u_d)): at (T=0), the left side is (F(u_1,\ldots,u_d)), which is not the zero polynomial in the (u_j).

Hence, outside a proper Zariski-closed exceptional locus,

[
|\Gamma_{\widehat U}\cap M_s|\le D_0.
\tag{5.3}
]

This proves a generic-(\widehat U) result. It does **not** prove the required result for every source-valid aperiodic (\widehat U). “Aperiodic” cannot be replaced by “Zariski generic.”

---

## 6. Exact next lemma that would give the full incidence bound

Define the weighted separation index

[
\operatorname{sep}_{n,s,d}(\widehat U)
======================================

\min
\left{
\operatorname{wdeg}F:
\begin{array}{l}
F\in I(M_s),\
F(g_1(T),\ldots,g_d(T))\not\equiv0
\end{array}
\right}.
\tag{6.1}
]

The bounded-closure lemma gives immediately

[
|\Gamma_{\widehat U}\cap M_s|
\le
\operatorname{sep}_{n,s,d}(\widehat U).
\tag{6.2}
]

The exact next theorem is therefore:

### `L-CYCLE107-APERIODIC-BOUNDED-WEIGHT-ELIMINATION`

There is an absolute constant (C) such that, for every source-valid above-reserve tuple and every (s),

[
\widehat U\text{ aperiodic}
\quad\Longrightarrow\quad
\operatorname{sep}_{n,s,d}(\widehat U)\le n^C.
\tag{6.3}
]

Equivalently,

[
\Gamma_{\widehat U}
\subseteq
\operatorname{Cl}^{,w}_{n^C}(M_s)
\quad\Longrightarrow\quad
\widehat U
\text{ belongs to the officially charged periodic/quotient locus}.
\tag{6.4}
]

Equation (6.4) is the exact point where above-reserve aperiodicity must be used. Proving it immediately yields

[
|\Gamma_{\widehat U}\cap M_s|\le n^C
]

with exponent independent of (s) and (k).

There is a source-level blocker: the uploaded packet repeatedly invokes “above corrected reserve aperiodicity” but does not provide its formal predicate, the exact charged periodic locus, or the numerical reserve condition. Consequently, the inclusion in (6.4) cannot yet be verified against the source definition. The packet does establish the Cycle105 reduction, but does not supply the hypothesis needed for the decisive final inclusion. See the [Cycle105 audit](sandbox:/mnt/data/cycle106_packet/cycle106_wallbreaker_9pro/context/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md) and [Cycle106 prompt](sandbox:/mnt/data/cycle106_packet/cycle106_wallbreaker_9pro/context/cycle106_kfree_aperiodic_moment_curve_incidence_prompt.md).

---

## 7. Exact checker

For weighted monomials (\mathcal B_D={Y^\alpha:\sum j\alpha_j\le D}), define:

[
A_{m,\alpha}=m^\alpha,
\qquad m\in M_s,
]

and

[
B_{r,\alpha}
============

[T^r],
\prod_{j=1}^d g_j(T)^{\alpha_j},
\qquad 0\le r\le D.
]

Then

[
\Gamma_{\widehat U}
\subseteq
\operatorname{Cl}^{,w}_D(M_s)
\iff
\ker A\subseteq\ker B
\iff
\rank A=\rank!\begin{pmatrix}A\B\end{pmatrix}.
\tag{7.1}
]

A rank increase gives an explicit (F\in I(M_s)) with nonzero restriction and therefore an exact (D)-point incidence bound.

I implemented and replayed this checker:

[Download the weighted-closure separator checker](sandbox:/mnt/data/cycle107_weighted_closure_separator_check.py)

SHA-256:

```text
1fba6e5d6f770d8a58e3359cce8b37d62ed88a2882cd0ce6a09eed8aa1a51406
```

For the finite test

[
(p,n,\sigma,s,D)=(17,8,2,5,6),
\qquad
\widehat U=(1,1,4,2,8,16),
]

it found:

[
\rank A=22,\qquad
\rank\binom AB=23,
]

an explicit weight-(6) separator, and one active parameter. The theoretical no-relation threshold from (3.2) is also (6). This is an exact finite/model certificate, not asymptotic evidence.

---

## Self-audit

**Exact implication proved.** Literal closure and relaxed-root closure cannot provide the bound. The squarefree-divisor elimination presentation (2.1)–(2.2), the relation-free range (3.1)–(3.2), and the implication

[
\Gamma\not\subseteq\operatorname{Cl}^{,w}_D(M_s)
\Longrightarrow
|\Gamma\cap M_s|\le D
]

are proved.

**Not proved.** I did not prove that above-reserve aperiodicity excludes bounded-weight containment, and therefore did not prove the Cycle106 incidence target.

**Prize relevance.** This is an M1 upper-side structural reduction and finite research checker. It is not an official Proximity Prize result. Even a proof of (6.3) would still require verification of the complete source reduction and all other prize branches.

**First possible failure.** After supplying the missing formal definition, the first mathematical failure point is exactly

[
\Gamma_{\widehat U}
\subseteq\operatorname{Cl}^{,w}_{n^C}(M_s)
\Longrightarrow
\widehat U\text{ periodic/charged}.
]

An aperiodic (\widehat U) in that exceptional determinantal locus would kill this route.

**Ledgers.** (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and the (2^{-128}) target are not used. Everything above is a single-field incidence statement over (\mathbb F_p). No ledger transfer is asserted.

**Potential numerator reductions.** Quotient/periodic structure may account for the exceptional bounded-closure components, but only after an explicit charging theorem. Literal contained incidence is impossible because (M_s) is finite; bounded-degree contained incidence is the exact obstruction. Same-slope collisions do not occur because, in the active normalization,

[
g_1(\theta)=u_1+\theta.
]

Invertible affine normalization preserves the count, and quotienting by (H)-scaling can collapse by at most (n). Complement duality preserves the incidence cardinality. No witness multiplicity was used.
