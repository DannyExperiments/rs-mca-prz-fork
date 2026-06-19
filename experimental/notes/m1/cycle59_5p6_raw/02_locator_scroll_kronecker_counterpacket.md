# COUNTERPACKET

The pure Kronecker/minimal-basis extraction step is false. After quotienting the common kernel, imposing full quotient-action rank, removing tangent locators, and requiring the syndrome line to be contained in no proper secant envelope, a locator cloud larger than (j+1) still need not concentrate on any polynomial section of (Z)-degree (t).

The failure is precise: Kronecker theory controls the moving **fibers**, but it imposes no cross-slope constraint on the coefficients selecting a point inside each fiber.

## 1. Exact lemma and counterpacket

### Kronecker coefficient-trajectory lemma

Let
[
\mathcal P(Z)=C-ZD:V\otimes_F F[Z]\longrightarrow W\otimes_F F[Z],
\qquad \dim W=t,
]
and put
[
K_0=\ker C\cap\ker D.
]

After quotienting by (K_0), let the right minimal indices of the pencil be
[
\epsilon_1,\ldots,\epsilon_h\ge 1.
]
Let the regular part have size (s). Then:

1. There are polynomial minimal-basis vectors
   [
   u_\nu(Z)\in V[Z],\qquad \deg_Zu_\nu=\epsilon_\nu,
   ]
   such that, outside at most (s\le t) regular slopes,
   [
   \ker \mathcal P(z)
   ==================

   K_0\oplus
   \operatorname{span}{u_1(z),\ldots,u_h(z)}.
   ]

2. The row count in Kronecker canonical form gives
   [
   \sum_{\nu=1}^h\epsilon_\nu+s\le t.
   ]

3. If (K) is a matrix whose columns form a basis of (K_0), every polynomial nullsection has the unique form
   [
   \Pi(Z)
   ======

   K A(Z)+\sum_{\nu=1}^h u_\nu(Z)B_\nu(Z).
   ]

4. With a column-reduced minimal basis, the predictable-degree identity is
   [
   \deg_Z\Pi
   =========

   \max\left{
   \max_\ell\deg A_\ell,,
   \max_\nu\bigl(\epsilon_\nu+\deg B_\nu\bigr)
   \right}.
   ]

Consequently, if selected locators have unique fiber coordinates
[
p_i=K a_i+\sum_\nu b_{i,\nu}u_\nu(z_i),
]
then a projective section of degree at most (d) through them exists exactly when there are scalars (\lambda_i\ne0) and polynomials satisfying
[
A(z_i)=\lambda_i a_i,\qquad
B_\nu(z_i)=\lambda_i b_{i,\nu},
]
with
[
\deg A_\ell\le d,\qquad
\deg B_\nu\le d-\epsilon_\nu.
]

Thus minimal indices bound the degrees of the ruling (u_\nu(Z)), but do not bound the interpolation complexity of the coefficient trajectory
[
z_i\longmapsto (a_i,b_{i,1},\ldots,b_{i,h}).
]

That missing coefficient constraint is exactly where the proposed extraction fails.

---

### Explicit envelope-free (t=2) Reed–Solomon packet

All coefficients below lie in (\mathbb F_{17}). Take
[
L=\mu_8
= ======

{1,9,13,15,16,8,4,2},
]
and
[
n=8,\qquad k=2,\qquad t=\sigma=2,\qquad
a=k+t=4,\qquad j=n-a=4.
]

Set
[
E(X)=X^2+3X+5,
\qquad
B_{\rm num}(X)=14+6X.
]

The polynomial (E) is irreducible over (\mathbb F_{17}), since its discriminant is (6), a nonsquare.

Define the numerator anchor by

[
\begin{array}{c|cccccccc}
x&1&9&13&15&16&8&4&2\ \hline
w(x)&7&5&4&10&4&4&0&0 .
\end{array}
]

For each row below, let (S_z=L\setminus T_z). Direct substitution gives
[
w(x)=E(x)P_z(x)+zB_{\rm num}(x)
\qquad(x\in S_z).
]

[
\begin{array}{c|c|c}
z&T_z&P_z(X)\ \hline
0&{1,15,16,4}&14+10X\
2&{13,16,4,2}&2\
4&{9,15,8,4}&13+11X\
8&{1,9,16,2}&15\
9&{9,13,8,2}&14+14X\
10&{13,15,16,8}&16+6X\
12&{1,13,15,2}&10+X\
16&{1,9,13,4}&4
\end{array}
]

Hence these are eight distinct successful slopes.

Because every (P_z) has degree (<k=2), this is an exact balanced residue packet.

## 2. Proof and construction details

### 2.1 Reducedness and denominator minimality

Since (E) is irreducible and (B_{\rm num}\ne0),
[
\gcd(E,B_{\rm num})=1.
]

The direction is
[
g(x)=-\frac{B_{\rm num}(x)}{E(x)}.
]

It has no denominator representation of degree at most one. Indeed, suppose on all eight points of (L),
[
-\frac{B_{\rm num}}{E}
======================

R-\frac{B'}{E'},
]
where
[
\deg R<2,\qquad \deg E'\le1,\qquad \deg B'<\deg E'.
]
Clearing denominators gives a polynomial identity on (L) of degree at most four:
[
-B_{\rm num}E'
==============

REE'-B'E.
]
Since (4<8), it is an identity in (\mathbb F_{17}[X]). Reduction modulo (E) gives
[
B_{\rm num}E'\equiv0\pmod E.
]
Reducedness forces (E\mid E'), impossible. Thus the intrinsic denominator degree is exactly (t=2).

---

### 2.2 Syndrome pencil

Use the standard dual-GRS parity-check basis. Since
[
N(X)=X^8-1,
\qquad
N'(x)=8x^7=8x^{-1}\quad(x\in L),
]
the parity-check columns may be taken as
[
h_x=\frac{x}{8}(1,x,\ldots,x^5)^{\mathsf T}.
]

The anchor and direction syndromes are
[
u=(8,7,4,16,7,9),
\qquad
v=(0,1,14,4,3,5).
]

For coefficient vectors (p=(p_0,\ldots,p_4)^{\mathsf T}), define
[
C=
\begin{pmatrix}
8&7&4&16&7\
7&4&16&7&9
\end{pmatrix},
]
and
[
D=
\begin{pmatrix}
0&16&3&13&14\
16&3&13&14&12
\end{pmatrix}.
]

Here (D=-H(v)), so the successful locator equation is
[
Cp_z=zDp_z.
]

Equivalently, with
[
\mathcal P(Z)=C-ZD,
]
every listed locator satisfies
[
\mathcal P(z)p_z=0.
]

All eight slopes are singleton slopes: among all
[
\binom84=70
]
degree-four split locators, exactly the eight listed locators land, and no two have the same slope.

---

### 2.3 No tangent locators

The syndrome sequence (v) satisfies the order-two recurrence
[
5v_m+3v_{m+1}+v_{m+2}=0,
\qquad 0\le m\le3.
]

The corresponding Hankel matrix has rank two, so
[
\ker H(v)
=========

E\cdot F[X]_{\le2}.
]

No locator (p_T) split over (L\subset\mathbb F_{17}) is divisible by the irreducible polynomial (E). Hence
[
H(v)p_T\ne0
]
for every four-set (T). Every incidence in the packet is therefore transverse, and there is no tangent branch.

---

### 2.4 Full quotient-action rank

The only nontrivial divisor of
[
\gcd(n,k)=\gcd(8,2)
]
is (M=2).

Let (\xi=[X]\in A_E=\mathbb F_{17}[X]/(E)). From
[
\xi^2=-3\xi-5
]
one obtains
[
(\xi^2)^2+\xi^2+8=0.
]

The polynomial
[
Y^2+Y+8
]
is irreducible over (\mathbb F_{17}), since its discriminant is (3), also a nonsquare. Therefore
[
d_2(E)
======

# \deg\minpoly(\xi^2)

# 2

\deg E.
]

Thus there is no (M=2) quotient-action-rank compression.

---

### 2.5 The syndrome line is envelope-free

For a five-set (R\subset L), let (L_R(X)) be its locator. Since the parity-check columns are full spark,
[
u,v\in W_R
\quad\Longleftrightarrow\quad
\langle u,L_R\rangle
====================

# \langle v,L_R\rangle

0.

]

The only five-sets satisfying
[
\langle v,L_R\rangle=0
]
are:

[
\begin{array}{c|c}
R&\langle u,L_R\rangle\ \hline
{1,13,8,4,2}&4\
{9,13,15,4,2}&11\
{9,13,16,8,4}&6\
{15,16,8,4,2}&13
\end{array}
]

Every displayed value is nonzero. Thus
[
\operatorname{span}(u,v)\not\subset W_R
\qquad
\text{for every }|R|=5.
]

Any envelope of size (<5) could be enlarged to one of size five, so
[
\operatorname{span}(u,v)\not\subset W_R
\qquad
\text{for every }|R|<r=6.
]

This packet is globally common-envelope-free. In particular, by the Cycle 49 close-support lemma, the eight locator supports are pairwise at exchange distance at least (t=2).

Their total common root core is also empty.

---

### 2.6 Exact Kronecker decomposition

The common kernel is one-dimensional:
[
K_0=\langle\kappa\rangle,
]
where
[
\kappa(X)
=========

13+7X+X^2+11X^3+X^4.
]

There are two right minimal-index-one chains:
[
u_1(Z,X)
========

14+X
+
Z(6+X+X^2+9X^3),
]
and
[
u_2(Z,X)
========

12+6X^2+X^3
+
Z(5+3X+X^2).
]

They satisfy identically
[
\mathcal P(Z)\kappa=0,
\qquad
\mathcal P(Z)u_1(Z)=0,
\qquad
\mathcal P(Z)u_2(Z)=0.
]

Thus the Kronecker data are
[
\dim K_0=1,\qquad
h=2,\qquad
(\epsilon_1,\epsilon_2)=(1,1),
\qquad
\epsilon_1+\epsilon_2=t.
]

Each selected locator has the unique representation
[
p_z
===

\kappa+b_z u_1(z)+c_z u_2(z),
]
where

[
\begin{array}{c|cccccccc}
z&0&2&4&8&9&10&12&16\ \hline
b_z&12&7&6&6&11&2&14&8\
c_z&4&15&9&5&1&12&10&0
\end{array}
]

This is a genuinely mixed two-block trajectory.

---

### 2.7 No degree-two polynomial section contains four locators

Suppose a polynomial section
[
\Pi(Z,X),\qquad \deg_Z\Pi\le2,
]
is projectively equal to four selected locators:
[
\Pi(z_i,X)=\lambda_i p_{z_i}(X),
\qquad
\lambda_i\ne0.
]

Since
[
\deg_Z\bigl(\mathcal P(Z)\Pi(Z)\bigr)\le3
]
and it vanishes at four distinct slopes, it must vanish identically:
[
\mathcal P(Z)\Pi(Z)=0.
]

The predictable-degree property therefore forces
[
\Pi(Z)
======

\alpha(Z)\kappa
+
\beta(Z)u_1(Z)
+
\gamma(Z)u_2(Z),
]
with
[
\deg\alpha\le2,
\qquad
\deg\beta\le1,
\qquad
\deg\gamma\le1.
]

At a selected slope (z), uniqueness of the fiber coordinates gives
[
\beta(z)=b_z\alpha(z),
\qquad
\gamma(z)=c_z\alpha(z).
]

Write
[
\alpha=\alpha_0+\alpha_1Z+\alpha_2Z^2,
\quad
\beta=\beta_0+\beta_1Z,
\quad
\gamma=\gamma_0+\gamma_1Z.
]

For a four-subset (I) of the eight slopes, these conditions form the (8\times7) homogeneous system whose two rows for (z\in I) are
[
(-b_z,-b_zz,-b_zz^2,1,z,0,0)
]
and
[
(-c_z,-c_zz,-c_zz^2,0,0,1,z).
]

For every one of the
[
\binom84=70
]
four-subsets (I), this matrix has rank seven over (\mathbb F_{17}). Hence its only solution is zero, contradicting (\lambda_i=\alpha(z_i)\ne0).

Therefore
[
\boxed{\text{no four of the eight locators lie on a degree-}\le2
\text{ polynomial section}.}
]

The exact finite checker is available here:

[Verify the locator-scroll counterpacket](sandbox:/mnt/data/verify_locator_scroll_packet.py)

This proves the route cut without relying on the earlier Cycle 58 eleven-slope packet, whose syndrome line had a proper-envelope loophole.

## 3. Parameter ledger

[
\begin{array}{c|c}
\text{parameter}&\text{value}\ \hline
F&q_{\rm gen}=q_{\rm line}=17\
q_{\rm chal}&\text{not used}\
n&8\
k&2\
\rho&1/4\
r=n-k&6\
t=\sigma&2\
a=k+t&4\
j=n-a&4\
N=\binom nj&70\
\dim K_0&1\
\text{right minimal indices}&(1,1)\
d_2(E)&2=t\
\text{distinct transverse slopes}&8\
j+1&5
\end{array}
]

The raw entropy inequality holds:
[
Q^t=17^2=289>70=N.
]

The additive entropy surplus is only
[
2\log_2 17-\log_2 70\approx2.05\text{ bits}.
]

The occupancy scales are
[
\lambda=\frac{N}{Q^t}=\frac{70}{289},
\qquad
Q\lambda=\frac{N}{Q}=\frac{70}{17}\approx4.12.
]

Thus the packet lies in the finite occupancy window. It does not contradict the calibrated target
[
n^{1+o(1)}+\frac{N}{Q^{t-1}}+\text{templates}.
]
Indeed, (8) is exactly at the linear (n)-scale.

It also does not approach the official (2^{-128}) surplus requirement.

## 4. Route-board impact

The following implication is cut:
[
\text{many resonant circuits}
\Longrightarrow
\text{one low-degree locator section}.
]

More precisely, it is false even when:

* the cloud has more than (j+1) points;
* the common pencil kernel has been explicitly quotiented;
* all right minimal indices are balanced;
* their total is exactly (t);
* the denominator has full quotient-action rank;
* every locator is transverse;
* the syndrome line is contained in no proper column envelope;
* all slopes are singleton slopes;
* the locators have no global common root.

Kronecker theory only supplies
[
p_z=K a_z+\sum_\nu b_{z,\nu}u_\nu(z).
]
It does not control the functions
[
z\mapsto a_z,\qquad z\mapsto b_{z,\nu}.
]

Exterior powers do not repair this: the Plücker curve records the moving subspace
[
M_z=\operatorname{span}{u_1(z),\ldots,u_h(z)},
]
but forgets which point of (K_0+M_z) is selected by the divisor-locator condition.

Accordingly, the low-degree-section alternative cannot be the first consequence of circuit abundance. It can only be an **inverse conclusion for excess above the occupancy and linear floors**.

The appropriate route-board replacement is:

[
\boxed{
\text{occupancy-generic mixed-scroll remainder}
;+;
\text{structured excess}.
}
]

## 5. What remains open

This counterpacket does not refute the calibrated scalar MCA upper theorem. It only refutes the proposed algebraic extraction mechanism at the circuit threshold.

The unresolved balanced theorem is still to prove, after action-rank and envelope exclusions,
[
\sum_{z\in F}
#\left{
T:,
p_T\in
K_0+\operatorname{span}{u_1(z),\ldots,u_h(z)}
\right}
\le
\frac{\binom nj}{Q^{t-1}},n^{o(1)}
+
n^{1+o(1)},
]
or to classify any excess.

Even such a balanced result would not alone handle the primitive (t>\sigma) branch; the final theorem must ultimately be reassembled in the syndrome transverse-secant formulation.

The scalar full-support list theorem and the finite (2^{-128}) constants also remain open.

## Do you see a route to a full solve?

Yes, but the next lemma is not “many circuits imply a section.” The exact next target should be:

[
\boxed{
\texttt{W-MCA-MIXED-KRONECKER-EXCESS-TRAJECTORY-INVERSE}.
}
]

In the same-field balanced setting, write each transverse generic-fiber locator uniquely as
[
p_{T,z}
= ======

K a_{T,z}
+
\sum_{\nu=1}^h b_{T,z,\nu}u_\nu(z).
]

Assume:

[
d_M(E)=t
\quad\text{for every active }M,
]
the syndrome line is envelope-free, and tangent locators have been removed.

Prove the following dichotomy:

[
\sum_z
#{T:p_T\in\ker(C-zD),\ Dp_T\ne0}
\le
\frac{\binom nj}{Q^{t-1}},n^{o(1)}
+
n^{1+o(1)},
]
or there is a large subpacket and a pivot block (\nu_0) for which the coefficient ratios
[
\frac{a_{T,z,\ell}}{b_{T,z,\nu_0}},
\qquad
\frac{b_{T,z,\nu}}{b_{T,z,\nu_0}}
]
agree with rational functions of (z) having the predictable-degree bounds
[
\deg A_\ell\le t+o(t),
\qquad
\deg B_\nu\le t-\epsilon_\nu+o(t),
\qquad
\deg R\le t-\epsilon_{\nu_0}+o(t),
]
unless a fixed-root packet or quotient-action-rank compression occurs.

Such rational coefficient synchronization is equivalent to a genuine low-degree polynomial section after clearing the common denominator. The root-budget lemma would then finish that branch.

The plausible proof mechanism is:

1. express the Kronecker blocks in canonical coordinates as weighted Reed–Solomon rows
   [
   b_{z,\nu}(1,z,\ldots,z^{\epsilon_\nu});
   ]
2. show that incidence excess above (N/Q^{t-1}) forces an anomalously large intersection among the resulting weighted GRS row spaces;
3. use the multiplier-ratio identity for GRS intersections to obtain low-degree rational functions for the coefficient ratios;
4. classify imprimitive ratio functions as quotient-action packets and zero-heavy ratios as fixed-core/common-envelope packets;
5. apply the polynomial-section root budget.

The exact blocker is Step 2: an occupancy-calibrated theorem converting excess split-divisor incidence into weighted-GRS intersection or coefficient-ratio structure. Kronecker theory alone cannot supply it.
