BANKABLE_LEMMA

Yes. The exact route is a **complement-line eliminant**. Everything reduces to one explicit aperiodicity-to-rank-escape lemma, which I do not prove here.

Let
[
d=\sigma+1,\qquad m=n-s,\qquad
V(X)=\widehat U(X)^{-1}\pmod{X^{d+1}}
=\sum_{j=0}^{d}v_jX^j,
]
where (v_0=1). Cycle105 supplies the (k)-free incidence formulation and complement duality. 

## 1. Exact complement-line reduction

The definition of (g_\ell(\theta)) gives
[
(1-\theta X)G(\theta,X)\equiv \widehat U(X)\pmod{X^{d+1}}.
\tag{1}
]

Suppose (S\subset H), (|S|=s), witnesses activity, and put (T=H\setminus S), so (|T|=m). Since (d<n),
[
g_S(X)g_T(X)=1-X^n\equiv1\pmod{X^{d+1}}.
]
Multiplying (1) by (g_T) gives
[
\widehat U(X)g_T(X)\equiv1-\theta X\pmod{X^{d+1}},
]
and hence
[
g_T(X)\equiv (1-\theta X)V(X)\pmod{X^{d+1}}.
\tag{2}
]

Conversely, (2), multiplied by (\widehat U), and then complemented using
(g_Sg_T\equiv1), recovers (g_S\equiv G(\theta,X)). Therefore
[
\boxed{
\theta\text{ active}
\iff
\exists T\subset H,\ |T|=m,\quad
g_T(X)\equiv(1-\theta X)V(X)\pmod{X^{d+1}}.
}
\tag{3}
]

In coefficient coordinates define the affine line
[
\ell_U(T)=
\bigl(v_1-T,\ v_2-v_1T,\ldots,v_d-v_{d-1}T\bigr).
\tag{4}
]
Then
[
\boxed{
|\Gamma\cap M_s|
================

|\ell_U(\mathbb F_p)\cap M_m|.
}
\tag{5}
]
There is no parameter collision: the first coordinate is (v_1-T), so
(T\mapsto\ell_U(T)) is injective.

This is sharper than the previously banked statement that complement is merely a triangular automorphism: after complementing, the rational moment curve becomes an actual affine line.

## 2. Exact eliminant and rank certificate

Let
[
\mathcal P_D=\mathbb F_p[Y_1,\ldots,Y_d]*{\deg*{\mathrm{tot}}\le D},
\qquad
N_D=\dim\mathcal P_D=\binom{D+d}{d}.
]
Index its monomial basis by
[
\mathcal A_D={\alpha\in\mathbb Z_{\ge0}^d:|\alpha|\le D},
\qquad Y^\alpha=\prod_{j=1}^dY_j^{\alpha_j}.
]

Use the **distinct** point set (M_m), not the collection of subset witnesses. Define
[
A_{m,D}[y,\alpha]=y^\alpha,
\qquad y\in M_m,\ \alpha\in\mathcal A_D,
\tag{6}
]
and define the line-restriction coefficient matrix
[
B_{U,D}[q,\alpha]
=================

[T^q]\prod_{j=1}^d
(v_j-v_{j-1}T)^{\alpha_j},
\qquad 0\le q\le D.
\tag{7}
]

For a coefficient vector (c=(c_\alpha)), let
[
F_c(Y)=\sum_{\alpha}c_\alpha Y^\alpha.
]
Then exactly:
[
A_{m,D}c=0
\iff F_c|*{M_m}=0,
\tag{8}
]
while
[
B*{U,D}c=0
\iff F_c(\ell_U(T))\equiv0
\quad\text{as a formal polynomial in }T.
\tag{9}
]

Consequently,
[
\boxed{
\rank
\begin{bmatrix}
A_{m,D}\ B_{U,D}
\end{bmatrix}

>

\rank A_{m,D}
}
\tag{10}
]
if and only if there is some (F\in\mathcal P_D) such that
[
F|_{M_m}=0,
\qquad
F(\ell_U(T))\not\equiv0.
\tag{11}
]

Every active (\theta) is then a root of the nonzero univariate polynomial
(F(\ell_U(T))), whose degree is at most (D). Thus
[
\boxed{
\rank
\begin{bmatrix}
A_{m,D}\ B_{U,D}
\end{bmatrix}

>

\rank A_{m,D}
\quad\Longrightarrow\quad
|\Gamma\cap M_s|\le D.
}
\tag{12}
]

### Escape matrix

Let (K_{m,D}) be any matrix whose columns form a basis of
(\ker A_{m,D}). Define
[
\boxed{
R_{m,D}(U)=B_{U,D}K_{m,D}.
}
\tag{13}
]
Then
[
R_{m,D}(U)\ne0
\iff \text{the rank jump in (10) occurs}.
\tag{14}
]

This condition is independent of the chosen kernel basis.

### Canonical restriction-gcd eliminant

If the columns of (R_{m,D}) represent polynomials
[
r_b(T)=\sum_{q=0}^D R_{m,D}[q,b]T^q,
]
define
[
\boxed{
\mathcal E_{m,U,D}(T)
=====================

\gcd{r_b(T):r_b\ne0},
}
\tag{15}
]
monic, and put (\mathcal E_{m,U,D}=0) if every (r_b) is zero.

This is basis-independent because it is the gcd of the restriction ideal
[
{F(\ell_U(T)):F\in I(M_m)\cap\mathcal P_D}\subseteq\mathbb F_p[T].
]
If (\mathcal E_{m,U,D}\ne0), then
[
\boxed{
{\theta:\theta\text{ active}}
\subseteq Z(\mathcal E_{m,U,D}),
\qquad
\deg\mathcal E_{m,U,D}\le D.
}
\tag{16}
]
A standard subresultant chain applied to the nonzero (r_b)'s computes this eliminant.

### Explicit determinant family

Let (r=\rank A_{m,D}), and choose row and column sets (I,J), each of size (r), such that
[
A_0=A_{m,D}[I,J]
]
is invertible. For (0\le q\le D) and every monomial column (a\notin J), define
[
\boxed{
\Delta_{q,a}(V)=
\det
\begin{pmatrix}
A_0&A_{m,D}[I,a]\
B_{U,D}[q,J]&B_{U,D}[q,a]
\end{pmatrix}.
}
\tag{17}
]
Then
[
\boxed{
R_{m,D}(U)\ne0
\iff
\Delta_{q,a}(V)\ne0
\text{ for at least one }(q,a).
}
\tag{18}
]
Each (\Delta_{q,a}) is an explicit polynomial of total degree at most (D) in (v_1,\ldots,v_d).

## 3. Uniform polynomial degree at reserve scale

Set
[
q_*=\min{q\ge1:q^d\ge2^n},
\qquad
D_*=d(q_*-1).
\tag{19}
]
Then
[
\binom{D_*+d}{d}
================

\prod_{i=1}^d\left(1+\frac{D_*}{i}\right)
\ge
\left(1+\frac{D_*}{d}\right)^d
=q_*^d
\ge2^n.
\tag{20}
]
Since
[
|M_m|\le\binom nm<2^n,
]
we obtain
[
\boxed{
\ker A_{m,D_*}\ne0
\quad\text{for every }m.
}
\tag{21}
]

If the corrected-reserve hypothesis supplies the numerical consequence
[
d\ge c_0\frac n{\log_2 n}
\tag{22}
]
for a fixed (c_0>0), then
[
q_*\le \left\lceil2^{n/d}\right\rceil
\le \left\lceil n^{1/c_0}\right\rceil
]
and hence
[
\boxed{
D_*
\le
d\left\lceil n^{1/c_0}\right\rceil
==================================

n^{1+1/c_0+o(1)}.
}
\tag{23}
]
The exponent is independent of (s) and (k).

Thus the desired incidence theorem follows from one nonvanishing statement.

## 4. Exact next lemma

Name the next theorem
[
\boxed{\textsf{L-CYCLE106-APERIODIC-COMPLEMENT-LINE-ESCAPE}.}
]

Its precise statement is:

> For every (m\in{0,\ldots,n}), every above-corrected-reserve aperiodic (\widehat U), and (D_*) from (19),
> [
> \boxed{R_{m,D_*}(U)\ne0.}
> \tag{24}
> ]
> Equivalently, for some explicit pair ((q,a)),
> [
> \boxed{\Delta_{q,a}(\widehat U^{-1})\ne0.}
> \tag{25}
> ]
> Equivalently,
> [
> I(M_m)*{\le D**}\not\subseteq I(\ell_U).
> \tag{26}
> ]

Equations (12) and (23) would then give
[
|\Gamma\cap M_s|\le D_*=n^{O(1)}
]
uniformly in (s) and (k).

This is where the aperiodicity hypothesis must be consumed. The Cycle105 source explicitly requires such a use and leaves the uniform theorem open.  

Define the determinantal bad locus
[
\mathcal B_{m,D}
================

{V:R_{m,D}(V)=0}.
\tag{27}
]
The exact structural theorem needed is
[
\boxed{
\mathcal B_{m,D_*}(\mathbb F_p)
\subseteq
\mathcal P_{\mathrm{charged}},
}
\tag{28}
]
where (\mathcal P_{\mathrm{charged}}) is the quotient-periodic/coset-swap locus excluded by the actual project aperiodicity predicate.

If that charged locus has defining ideal (I_{\mathrm{charged}}), and
[
J_{m,D_*}
=========

\left\langle (R_{m,D_*})*{q,b}\right\rangle,
]
an exact algebraic certificate for (28) is
[
\boxed{
I*{\mathrm{charged}}
\subseteq
\sqrt{J_{m,D_*}}.
}
\tag{29}
]
A Nullstellensatz certificate would exhibit, for each generator (f) of
(I_{\mathrm{charged}}),
[
f^{N_f}
=======

\sum_{q,b}H_{f,q,b}(V)(R_{m,D_*})_{q,b}.
\tag{30}
]

## 5. The exceptional locus is genuinely proper

The rank target is not vacuous.

Choose a nonzero (F\in\ker A_{m,D_*}), which exists by (21), and regard
(v_1,\ldots,v_d) as independent variables. Then
[
F(\ell_V(0))=F(v_1,\ldots,v_d)\ne0
]
as a formal polynomial. Hence
[
F(\ell_V(T))\not\equiv0
]
over (\mathbb F_p[v_1,\ldots,v_d,T]). Therefore at least one entry of
(R_{m,D_*}(V)) is a nonzero polynomial, and
[
\boxed{
\mathcal B_{m,D_*}
\subsetneq\mathbb A^d.
}
\tag{31}
]

Moreover, truncated inversion
[
(u_1,\ldots,u_d)\longleftrightarrow(v_1,\ldots,v_d)
]
is a triangular polynomial automorphism, since recursively
[
v_j=-u_j-\sum_{i=1}^{j-1}u_i v_{j-i}.
]
Thus the bad locus is proper in (\widehat U)-coefficient space as well.

This proves the incidence bound for Zariski-generic (\widehat U). It does **not** prove it for every aperiodic (\widehat U).

## 6. Why a curve-only Wronskian cannot close Cycle106

Define the Newton-coordinate automorphism
[
\mathcal N_j(a_1,\ldots,a_d)
============================

-j[X^j]\log\left(1+\sum_{i=1}^da_iX^i\right).
\tag{32}
]
Because (p>d), this is triangular with invertible diagonal coefficient (-j). It sends (M_s) to subset power-sum coordinates.

Using
[
(1-\theta X)G_\theta=\widehat U,
]
we get
[
\mathcal N_j(G_\theta)
======================

-j[X^j]\log\widehat U-\theta^j.
\tag{33}
]
Thus (\Gamma) is a translate of the standard moment curve
[
(\theta,\theta^2,\ldots,\theta^d).
]

Equivalently, (1,g_1,\ldots,g_d) are a unitriangular basis change from
(1,\theta,\ldots,\theta^d), and therefore
[
\boxed{
\operatorname{Wr}(1,g_1,\ldots,g_d)
===================================

\prod_{j=0}^{d}j!\ne0.
}
\tag{34}
]
This Wronskian is independent of (\widehat U). It cannot distinguish aperiodic from periodic anchors and therefore cannot prove the incidence bound by itself. The certificate must involve (M_m) and the position of the complement line.

There is also a useful lower barrier. Give (Y_j) weight (j). If (d\le m) and a nonzero (F(Y_1,\ldots,Y_d)) vanishes on (M_m), then
[
\operatorname{wt}(F)\ge n-m+1.
\tag{35}
]
Indeed, substitute (Y_j=(-1)^je_j(z_1,\ldots,z_m)) and multiply by the Vandermonde. The resulting polynomial vanishes on (H^m). If
(\operatorname{wt}(F)\le n-m), its degree in each (z_i) is at most
[
(m-1)+(n-m)=n-1,
]
so tensor interpolation on (H^m) forces it to be zero, contradicting the algebraic independence of (e_1,\ldots,e_d). Complement duality gives, when (d\le\min(m,n-m)),
[
\boxed{
\operatorname{wt}(F)\ge\max(m,n-m)+1.
}
\tag{36}
]
Hence a central-layer eliminant cannot be an (O(\sigma))-weighted-degree identity.

## Exact checker

The checker constructs (M_m) as a distinct point set, builds (A_{m,D}), (B_{U,D}), and (R_{m,D}), compares the ranks, and outputs an explicit separator and its univariate restriction when the line escapes:

[Exact complement-line eliminant checker](sandbox:/mnt/data/cycle106_complement_line_eliminant_check.py)

It is exhaustive and exact over the chosen finite field, but exponential in (n). It does not implement the project’s aperiodicity predicate and is therefore a finite/model certificate only.

## Self-audit

1. **Exact implication proved.**
   [
   R_{m,D_*}(U)\ne0
   \Longrightarrow
   |\Gamma\cap M_s|\le D_*,
   ]
   together with the exact complement-line reduction, explicit determinant family, canonical gcd eliminant, uniform nonempty relation space, and properness of the exceptional locus.

   **Not proved:**
   [
   \operatorname{Aper}*{\mathrm{corr}}(\widehat U)
   \Longrightarrow
   R*{m,D_*}(U)\ne0.
   ]

2. **Prize status.** This is prize-relevant structural progress at the Cycle106 wall, not a Proximity Prize proof. The official chain beyond this wall has not been verified. The checker is finite/model evidence only.

3. **First possible failure.** The first mathematical failure line is exactly
   [
   \operatorname{Aper}*{\mathrm{corr}}(\widehat U)
   \Longrightarrow
   \widehat U^{-1}\notin\mathcal B*{m,D_*}.
   ]
   There is also a source-definition checkpoint: the formal corrected-reserve condition must imply (d=\Omega(n/\log n)) for (23).

4. **Field ledgers.** (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and the (2^{-128}) target are not used. This remains a single-(\mathbb F_p) structural argument.

5. **Numerator integrity.**

   * (M_m) is deduplicated before evaluation; no weighted subset count replaces distinct support.
   * Multiple subset witnesses for one (\theta) do not increase the numerator.
   * Distinct (\theta)'s cannot have the same line point because the first coordinate is (v_1-\theta).
   * Contained incidences are included, not subtracted.
   * Quotient/periodic structure may be precisely what forces all determinants to vanish; that is the unresolved classification.
   * No affine color normalization is used.
   * If a later official numerator excludes (\theta\in H), this all-(\theta) bound is stronger; internal values contribute at most (n).

6. **Exact conversion to PROOF.** Prove `L-CYCLE106-APERIODIC-COMPLEMENT-LINE-ESCAPE`, equivalently the pointwise containment (28), or supply the radical-membership certificates (29)–(30) after the charged periodic locus is formally defined.

**Confidence:** high for the complement-line reduction, rank/eliminant equivalence, degree threshold, properness, Wronskian cut, and checker; unknown for the decisive aperiodicity-to-determinant-nonvanishing implication.
