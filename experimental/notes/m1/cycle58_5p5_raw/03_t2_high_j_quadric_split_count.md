## VERDICT

**Repository status: COUNTEREXAMPLE**

**COUNTERPACKET.** The proposed wall

[
\texttt{W-MCA-T2-HIGH-J-DETERMINANTAL-QUADRIC-SPLIT-COUNT}
]

is false as an absolute (n^{1+o(1)}) bound. For every official rate

[
\rho\in\left{\frac12,\frac14,\frac18,\frac1{16}\right},
]

there are generated-field smooth multiplicative domains, genuinely degree-two reduced nonquotient residue data, and anchors for which

[
|F|^2\gg \binom nj
]

but the determinant quadric contains

[
(1-o(1))\frac{\binom nj}{|F|}
]

transverse split locators with distinct slopes. This quantity is exponentially larger than (n^{1+o(1)}).

The obstruction is not the (O(\sqrt{|F|})) conic fluctuation from (j=2). It is the unavoidable codimension-one volume term (\binom nj/|F|).

This is a fixed-rate (t=2) counterpacket, not yet a counterexample to the full prize asymptotic: the construction has (|F|=2^{\Theta(n)}), whereas the final conjecture is normally posed with (|F|=2^{o(n)}), and (t=2) does not clear the (n/\log n) quotient reserve.

---

## T2_HIGH_J_NORMAL_FORM

### PROOF

Let (D\subset F) be an (n)-point domain and set

[
P_D(X)=\prod_{x\in D}(X-x).
]

Let (w:D\to F), and let (W\in F[X]_{<n}) be its full-domain interpolation polynomial. Fix

[
t=2,\qquad a=k+2,\qquad j=n-a.
]

For (T\in\binom Dj), put

[
S=D\setminus T,\qquad
L_T(X)=\prod_{x\in T}(X-x),
]

and let (Q_T=\operatorname{Interp}_S(w)), so (\deg Q_T<a).

Define the linear cyclic-multiplication operator

[
\mathcal C_W(L):=\operatorname{rem}_{P_D}(WL).
]

Then

[
\boxed{L_TQ_T=\mathcal C_W(L_T).}
\tag{1}
]

Indeed, both sides have degree (<n). On (S), they equal (L_Tw); on (T), both vanish.

Let

[
A_E:=F[X]/(E),
]

where (E) is a quadratic with no root in (D). Since (\gcd(E,L_T)=1), ([L_T]_E) is a unit. Equation (1) gives

[
[Q_T]_E=[\mathcal C_W(L_T)]_E[L_T]_E^{-1}.
\tag{2}
]

For a reduced numerator (B_{\rm num}\in F[X]_{<2}), the landing condition is

[
[Q_T]*E=z[B*{\rm num}]_E.
]

Multiplying by ([L_T]_E),

[
[\mathcal C_W(L_T)]_E
=====================

z[B_{\rm num}L_T]_E.
\tag{3}
]

Thus the two vectors

[
[\mathcal C_W(L_T)]*E,\qquad [B*{\rm num}L_T]_E
]

must be collinear in the two-dimensional (F)-space (A_E).

Choose the basis (1,X) of (A_E). Write

[
[\mathcal C_W(L)]*E=
\begin{pmatrix}u_0(L)\u_1(L)\end{pmatrix},
\qquad
[B*{\rm num}L]_E=
\begin{pmatrix}v_0(L)\v_1(L)\end{pmatrix}.
]

Each (u_i,v_i) is a linear form in the coefficients of (L). Therefore the exact landing equation is

[
\boxed{
\Delta_{E,B_{\rm num},W}(L)
===========================

u_0(L)v_1(L)-u_1(L)v_0(L)=0.
}
\tag{4}
]

If

[
L=X^j+c_{j-1}X^{j-1}+\cdots+c_0,
\qquad c_j:=1,
]

define

[
U_r=[\operatorname{rem}_{P_D}(WX^r)]*E,\qquad
V_r=[B*{\rm num}X^r]_E.
]

Then (4) is equivalently

[
\boxed{
\Delta(c_0,\ldots,c_j)
======================

\sum_{r,s=0}^j c_rc_s\det(U_r,V_s)=0,
\qquad c_j=1.
}
\tag{5}
]

It is a homogeneous determinantal quadric before imposing (c_j=1), and an affine quadric on the monic locator chart. Its quadratic rank is at most four, independently of (j).

### Split-root form

Suppose

[
E=(X-\alpha)(X-\beta),\qquad \alpha\ne\beta.
]

CRT identifies (A_E) with (F^2) by evaluation at (\alpha,\beta). Put

[
U_T=\operatorname{rem}_{P_D}(WL_T).
]

Then (4) becomes

[
\boxed{
U_T(\alpha)B_{\rm num}(\beta)L_T(\beta)
---------------------------------------

U_T(\beta)B_{\rm num}(\alpha)L_T(\alpha)=0.
}
\tag{6}
]

When it holds, the slope is uniquely

[
z_T=
\frac{U_T(\alpha)}
{B_{\rm num}(\alpha)L_T(\alpha)}
================================

\frac{U_T(\beta)}
{B_{\rm num}(\beta)L_T(\beta)}.
\tag{7}
]

For the multiplicative subgroup (H=\mu_n(F)),

[
P_D=X^n-1,\qquad P_D'(x)=nx^{-1},
]

and Lagrange interpolation gives the explicit linear functional

[
U_T(\gamma)
===========

\frac{\gamma^n-1}{n}
\sum_{x\in H}
\frac{x,w(x)L_T(x)}{\gamma-x}.
\tag{8}
]

Hence (6) is an explicit subgroup-locator incidence equation.

The relevant finite split-locator variety is

[
\operatorname{Split}_j(H)
=========================

\left{
\prod_{x\in T}(X-x):
T\in\binom Hj
\right}
\subset \mathbb A^j.
]

The high-(j) problem is exactly

[
#\bigl(
\operatorname{Split}*j(H)\cap V(\Delta*{E,B_{\rm num},W})
\bigr).
\tag{9}
]

---

## COUNTING_THEOREM_OR_COUNTERPACKET

### BANKABLE_LEMMA — generic transverse volume at (t=2)

Let

[
N=\binom nj,\qquad \mu=\frac NQ,\qquad Q=|F|.
]

Assume

[
\frac{N}{Q}\longrightarrow\infty,\qquad
\frac{N}{Q^2}\longrightarrow0,\qquad
\frac{n^3}{Q}\longrightarrow0.
\tag{10}
]

Then there exist:

* a separable split quadratic (E) with no root in (D);
* (E) not of the form (E_0(X^M)) for any (M>1);
* (B_{\rm num}=1);
* an anchor (w:D\to F);

such that, after deleting any prescribed locator family of size (o(N)), equation (4) has

[
\boxed{(1-o(1))\frac NQ}
\tag{11}
]

solutions (L_T) whose slopes are globally unique and whose supports have no tangent/common-((a-1))-core collision.

### Proof

For an (a)-set (S), write

[
R_S(w):=[\operatorname{Interp}_S(w)]_E\in A_E
]

and let

[
\ell=F\cdot[1]_E.
]

The support lands precisely when (R_S(w)\in\ell).

For two (a)-sets (S,S'), set

[
d=|S\setminus S'|,\qquad C=S\cap S'.
]

The domain-free pair-rank identity from the packet gives

[
\operatorname{Im}(R_S,R_{S'})
=============================

\left{
(u,v)\in A_E^2:
u-v\in[L_CF[X]_{<d}]_E
\right}.
\tag{12}
]

Hence

[
\operatorname{rank}(R_S,R_{S'})=2+\min(2,d).
\tag{13}
]

For (d=1), define the core direction

[
K_C=F\cdot[L_C]_E.
]

The core is resonant exactly when (K_C=\ell).

For uniformly random (w),

[
\Pr(R_S(w)\in\ell)=Q^{-1}.
]

Moreover,

[
\Pr(R_S,R_{S'}\in\ell)
======================

\begin{cases}
Q^{-1},&d=1,\ K_C=\ell,\
Q^{-2},&d=1,\ K_C\ne\ell,\
Q^{-2},&d\ge2.
\end{cases}
\tag{14}
]

The same-slope diagonal ({(z,z):z\in F}) is always contained in the image (12), so

[
\Pr\bigl(R_S=R_{S'}=z\text{ for some }z\bigr)
=============================================

Q^{-1-\min(2,d)}.
\tag{15}
]

#### Choosing a core-clean quadratic

Take (E=(X-\alpha)(X-\beta)). For (B_{\rm num}=1), an ((a-1))-core (C) is resonant iff

[
L_C(\alpha)=L_C(\beta).
\tag{16}
]

For fixed (C) and fixed (\alpha), equation (16), regarded as an equation in (\beta), has at most (a-1) solutions. Averaging over ordered pairs ((\alpha,\beta)\in(F\setminus D)^2) gives an (E) for which the number (R_E) of resonant cores satisfies

[
R_E
===

O\left(
\frac aQ\binom n{a-1}
\right).
\tag{17}
]

One may simultaneously exclude:

* (\alpha=\beta);
* roots in (D);
* (\alpha+\beta=0), which is the only possible degree-two quotient form;
* quadratics defined over a proper subfield.

These exclusions occupy (o(Q^2)) root pairs in the field sequences below.

A resonant core belongs to (j+1) supports. Since

[
\binom n{a-1}(j+1)=a\binom na=aN,
]

the total number of supports incident to resonant cores is at most

[
O\left(\frac{a^2}{Q}N\right)=o(N).
\tag{18}
]

Thus all core-template supports form a negligible locator family.

#### Landing count

Let

[
L(w)=#{S:R_S(w)\in\ell}.
]

Then

[
\mathbb E L=\mu=\frac NQ.
\tag{19}
]

By (14), all covariance outside resonant (d=1) cores vanishes. In fact,

[
\operatorname{Var}L
===================

N(Q^{-1}-Q^{-2})
+
R_E(j+1)j(Q^{-1}-Q^{-2}).
\tag{20}
]

Using (17),

[
\operatorname{Var}L
\le
\mu\left(1+O\left(\frac{a^2j}{Q}\right)\right)
=(1+o(1))\mu.
\tag{21}
]

Because (\mu\to\infty),

[
L(w)=(1+o(1))\mu
\tag{22}
]

with probability (1-o(1)).

#### Unique slopes

Let (\nu_w(z)) be the number of landing supports with slope (z), and put

[
C_{\rm same}(w)=\sum_z\binom{\nu_w(z)}2.
]

There are (aj) supports at exchange distance one from a fixed support. Equation (15) gives the exact expectation

[
\mathbb E C_{\rm same}
======================

\frac N2
\left(
\frac{aj}{Q^2}
+
\frac{N-1-aj}{Q^3}
\right).
\tag{23}
]

Dividing by (\mu=N/Q),

[
\frac{\mathbb E C_{\rm same}}{\mu}
==================================

\frac12
\left(
\frac{aj}{Q}
+
\frac{N-1-aj}{Q^2}
\right)
=o(1).
\tag{24}
]

Thus (C_{\rm same}=o(\mu)) for some anchor satisfying (22). The number of landing supports belonging to nonsingleton slope classes is at most (2C_{\rm same}=o(\mu)).

Deleting:

* resonant-core supports;
* any prescribed (o(N)) locator-template family;
* all nonsingleton slope classes;

leaves ((1-o(1))\mu) locators with globally unique slopes.

Finally, two retained supports cannot have exchange distance one. If they had common core (C), that core would be nonresonant, so (12) would imply that two landing residues in (\ell) are equal. They would therefore have the same slope, contradicting singletonness. Hence the retained intersections are transverse.

This proves (11).

---

### COUNTERPACKET — all four official rates

Let (n=2^s) and (k=\rho n). Put

[
a=k+2,\qquad j=n-k-2,\qquad
N=\binom nj=2^{H_2(\rho)n+o(n)}.
]

Use the following generated-field domain sequences:

| (\rho) | Base field (\mathbf B) | Ambient/generated field (F) | (\alpha=\frac1n\log_2|F|) | (2\alpha-H_2(\rho)) | (H_2(\rho)-\alpha) |
|---:|---:|---:|---:|---:|---:|
| (1/2) | (\mathbb F_5) | (\mathbb F_{5^{n/4}}) | (0.580482) | (0.160964) | (0.419518) |
| (1/4) | (\mathbb F_5) | (\mathbb F_{5^{n/4}}) | (0.580482) | (0.349686) | (0.230796) |
| (1/8) | (\mathbb F_3) | (\mathbb F_{3^{n/4}}) | (0.396241) | (0.248917) | (0.147324) |
| (1/16) | (\mathbb F_{17}) | (\mathbb F_{17^{n/16}}) | (0.255466) | (0.173643) | (0.081824) |

For (s) large,

[
\operatorname{ord}*{2^s}(5)=2^{s-2},\qquad
\operatorname{ord}*{2^s}(3)=2^{s-2},\qquad
\operatorname{ord}_{2^s}(17)=2^{s-4},
]

by the standard (2)-adic lifting formula. Therefore a primitive (n)-th root generates the displayed extension. Taking

[
H=\mu_n(F)
]

gives a smooth multiplicative domain with

[
q_{\rm gen}=q_{\rm line}=|F|=:Q.
]

No (q_{\rm chal}) assertion or field-transfer step is used.

In every row,

[
\frac{H_2(\rho)}2<\alpha<H_2(\rho).
]

Consequently,

[
\frac N{Q^2}
============

2^{-(2\alpha-H_2(\rho))n+o(n)}
\longrightarrow0,
\tag{25}
]

so this is strictly above the (t=2) entropy boundary, while

[
\frac NQ
========

2^{(H_2(\rho)-\alpha)n+o(n)}
\tag{26}
]

is exponential.

The lemma therefore supplies a reduced, nonquotient degree-two datum with

[
\boxed{
\Lambda^{\rm NC}_{2,,1-(k+2)/n}(H,k)
\ge
(1-o(1))\frac{\binom n{k+2}}Q
=============================

2^{(H_2(\rho)-\alpha)n+o(n)}.
}
\tag{27}
]

Every retained slope has a unique transverse split-locator witness.

In normalized MCA form, this line gives

[
\emca
\ge
(1-o(1))\frac N{Q^2}.
\tag{28}
]

Thus (Q^2>N) makes the error small, but it does not force the slope count down to (n^{1+o(1)}).

---

## QUOTIENT_TANGENT_STATUS

### Reduced and genuinely degree two

Take (B_{\rm num}=1). Then

[
\gcd(E,B_{\rm num})=1.
]

The direction word is

[
g=-\frac1E.
]

It has no degree-zero or degree-one denominator representation. For example, if

[
-\frac1E=R-\frac b{E'}
\quad\text{on }D,
\qquad
\deg R<k,\quad \deg E'=1,
]

then

[
REE'-bE+E'
]

vanishes on all (n) points of (D), while its degree is at most (k+2<n). Hence it is identically zero. Reducing modulo (E) gives (E'\equiv0\pmod E), impossible. The polynomial-denominator-zero case is even simpler.

Thus the minimal denominator degree really is (t=2).

### Nonquotient

For a quadratic, the only possible nontrivial multiplicative pullback is

[
E(X)=E_0(X^2),
]

which has zero (X)-coefficient. Choosing (\alpha+\beta\ne0) makes

[
E=(X-\alpha)(X-\beta)
]

nonquotient. Choosing its coefficients outside all proper subfields also removes a base-field/Frobenius core.

The random anchor can simultaneously be chosen not to factor through any proper quotient (x\mapsto x^M): the number of such words is at most

[
\sum_{\substack{M\mid n\M>1}}Q^{n/M}
\le n^{o(1)}Q^{n/2}=o(Q^n).
]

### Automatic noncontainment and no tangent branch

For every exact witness support (|S|=a=k+2), if some (G\in F[X]_{<k}) agreed with (g=-1/E) on (S), then

[
EG+1
]

would have (k+2) roots and degree at most (k+1). Hence (EG+1=0), impossible.

Therefore:

* every landing witness is noncontained;
* the direction is not explained on any active support;
* no witness lies in the tangent branch.

### Quotient locators can be deleted

Let (\mathcal X_{\rm quot}) be the exact quotient-periodic complements, namely (T)'s that are unions of fibers of (x\mapsto x^M) for some (M>1). Then

[
|\mathcal X_{\rm quot}|
\le
\sum_{\substack{M\mid n\M>1\M\mid j}}
\binom{n/M}{j/M}
================

2^{\frac12H_2(\rho)n+o(n)}
=o(N).
\tag{29}
]

They may therefore be included in the prescribed (o(N)) exceptional family in the counting lemma. The exponential count (27) survives their complete deletion.

### Same-witness and common-core templates can be deleted

The retained slopes are globally singleton: no second support has the same slope. They are also pairwise at exchange distance at least two.

Thus among the retained family:

* one support cannot witness two slopes;
* two supports cannot share the same witness polynomial;
* two supports cannot lie in one ((a-1))-core template;
* every Cycle 49-style intersection is transverse under the operational tests of unique slope, unique locator and no close-core collision.

---

## EXACT_NEW_WALL

### ROUTE_CUT — the (O(\sqrt Q)) conic fluctuation is not the high-(j) wall

Fixing (j-2) roots reduces the last two roots to the (j=2) conic problem. A naive summation of an (O(\sqrt Q)) error over all ((j-2))-cores gives

[
O\left(
\frac{\binom n{j-2}\sqrt Q}{\binom j2}
\right)
= ======

O\left(
\frac{\binom nj\sqrt Q}
{\binom{n-j+2}{2}}
\right).
\tag{30}
]

At fixed rate this is roughly

[
O\left(\frac{N\sqrt Q}{n^2}\right),
]

which is useless. In the entropy-safe (t=2) regime, (Q) is exponential in (n), so even the single-slice bound (O(\sqrt Q)) exceeds the trivial (O(n^2)) number of pair completions.

More importantly, perfect cancellation of all conic errors would still leave the main term

[
\frac NQ.
]

The random-anchor calculation proves that this main term is genuinely attained by transverse, unique-slope locators. The (j=2) fluctuation therefore neither needs to compound nor explains the counterpacket. The high-(j) obstruction is the main volume.

### EXACT_NEW_WALL

The corrected inverse theorem must include the transverse volume term. The next wall should be:

[
\boxed{
\texttt{W-MCA-SYNDROME-TRANSVERSE-SECANT-MAIN-TERM-PLUS-INVERSE}.
}
]

In the same-field case (q_{\rm gen}=q_{\rm line}=Q), its expected form is

[
#\Gamma_{\rm transverse}
\le
n^{1+o(1)}
+
O\left(
\frac{\binom n{k+t}}{Q^{t-1}}
\right)
+
\text{quotient/template contribution}.
\tag{31}
]

Equivalently, in normalized MCA form,

[
\emca
\le
\frac{n^{1+o(1)}}{Q}
+
O\left(
\frac{\binom n{k+t}}{Q^t}
\right)
+
\text{quotient/template error}.
\tag{32}
]

With distinct residue and slope fields, the unproved transfer must not be hidden. The literal volume term is

[
\frac{\binom n{k+t},q_{\rm line}}{|F|^t}
\tag{33}
]

for support landings, provided surjectivity is proved over the actual residue-coordinate field (F). It cannot automatically be rewritten using (q_{\rm gen}).

For (t=2), an (n^{1+o(1)}) transverse bound requires approximately

[
Q\ge
\frac{\binom nj}{n^{1+o(1)}},
\tag{34}
]

not merely

[
Q^2\ge\binom nj.
]

For the actual full-prize regime, where (t\to\infty), (\log Q=o(n)), and the entropy inequality has a fixed multiplicative margin, losing one factor of (Q) is only (2^{o(n)}). Thus the corrected main term vanishes there, and a main-term-plus-inverse theorem could still close the upper branch.

The next exact subgroup-variety lemma is therefore:

[
\boxed{
#\bigl(
\operatorname{Split}_j(H)\cap V(\Delta)
\bigr)
\le
\frac{\binom nj}{Q}
+
n^{1+o(1)}
}
\tag{35}
]

for every reduced nonquotient (t=2) datum after the precisely enumerated tangent/core/template families are removed, with an inverse classification whenever the left side exceeds the displayed main term by more than (n^{1+o(1)}).

For general (t), replace (N/Q) by (N/Q^{t-1}). The random-anchor construction supplies the matching lower baseline, so only excess above that baseline can force structure.

Yes. A route to a full solve remains: prove the main-term-plus-inverse lemma (31), then show that its volume term is (n^{o(1)}) under the strict official entropy and field-transfer hypotheses, while separately integrating (t<\sigma) residual lists and (t>\sigma) residue-quotient incidence.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
