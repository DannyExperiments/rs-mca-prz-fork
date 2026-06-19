## VERDICT

**Repository status: CONJECTURAL**

The full inverse theorem
`W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT`
remains unproved.

What is now proved:

* `PROOF`: an exact linearization of the balanced arbitrary-anchor cloud as a generalized-eigenvector section of the root-locator set.
* `PROOF`: minimal-support (E)-resonant circuit extraction, including (H\neq0).
* `BANKABLE_LEMMA`: superlinear clouds force a large space of synchronized two-moment relations.
* `BANKABLE_LEMMA`: synchronized relations impose exact root-multiplicity and common-core bounds.
* `BANKABLE_LEMMA`: a single polynomial locator envelope cannot support more than linearly many slopes unless almost all locator roots are fixed.
* `COUNTERPACKET`: classifying each minimal resonant circuit separately as quotient, fixed-core, or nonminimal is false. A genuinely mixed Kronecker-scroll template already occurs at the official rate (\rho=1/4).

The unresolved object is no longer “many abstract circuits.” It is the intersection of the root-locator configuration with **moving affine cosets of a large fixed kernel inside a low-index Kronecker scroll**.

Confidence: **high** for all algebraic lemmas and the finite packet; **moderate** that the Kronecker-scroll formulation is the correct route; **unknown** for the final mixed-scroll inverse.

---

## BANKABLE_LEMMA

### PROOF — Exact balanced locator-scroll linearization

Let (F) be a field and let (L\subset F) have (n) distinct elements. Write

[
N(X)=\Lambda_L(X)=\prod_{x\in L}(X-x).
]

Fix integers

[
n=k+t+j,\qquad a=k+t,
]

and assume the balanced case (t=\sigma). Let

[
E\in F[X],\qquad \deg E=t,\qquad \gcd(E,N)=1,
]

and let (B_{\rm num}\in F[X]) satisfy

[
0\neq B_{\rm num},\qquad \deg B_{\rm num}<t,\qquad
\gcd(E,B_{\rm num})=1.
]

Let (w:L\to F), and let (W\in F[X]_{<n}) be its interpolation polynomial.

For (p\in V_j:=F[X]_{\le j}), define the linear operator

[
\mathcal R_W(p):=\operatorname{rem}*N(Wp)\in F[X]*{<n}.
]

Let

[
A_E:=F[X]/(E),
]

and define two (F)-linear maps

[
\pi:V_j\to A_E,\qquad \pi(p)=[p]_E,
]

[
\tau:V_j\to A_E,\qquad
\tau(p)=[B_{\rm num}]_E^{-1}[\mathcal R_W(p)]_E.
]

The inverse exists because (B_{\rm num}) is a unit modulo (E).

For a (j)-subset (T\subset L), put

[
p_T=\Lambda_T,\qquad S=L\setminus T.
]

Then

[
\boxed{\mathcal R_W(p_T)=p_T,\operatorname{interp}_S(w).}
]

#### Proof

For (x\in T), (p_T(x)=0), so

[
\mathcal R_W(p_T)(x)=W(x)p_T(x)=0.
]

Thus (p_T\mid\mathcal R_W(p_T)). Write

[
\mathcal R_W(p_T)=p_TQ_T.
]

Since (\deg\mathcal R_W(p_T)<n),

[
\deg Q_T<n-j=a.
]

For (x\in S), (p_T(x)\neq0), and reduction modulo (N) preserves evaluation on (L), so

[
Q_T(x)
=\frac{\mathcal R_W(p_T)(x)}{p_T(x)}
=W(x)=w(x).
]

Hence (Q_T) is the unique degree-(<a) interpolant of (w) on (S). ∎

Because (E) has no roots in (L), every (p_T) is a unit modulo (E). Therefore

[
[\operatorname{interp}_S(w)]*E=z[B*{\rm num}]_E
]

is equivalent to

[
\boxed{\tau(p_T)=z,\pi(p_T).}
]

Conversely, if this generalized-eigenvector equation holds, then

[
Q_T:=\operatorname{interp}_S(w)
]

satisfies

[
Q_T-zB_{\rm num}=EP
]

for some (P\in F[X]_{<k}), because (\deg Q_T<a=k+t).

Thus the balanced residue cloud is exactly

[
\boxed{
\Gamma(E,B_{\rm num},w)
=======================

{z\in F:\exists,p\in\operatorname{Loc}_j(L),
\ \tau(p)=z\pi(p)},
}
]

where

[
\operatorname{Loc}_j(L)
=======================

{\Lambda_T: T\subset L,\ |T|=j}.
]

This is the exact locator-scroll section formulation. It holds for arbitrary domains; smooth multiplicativity has not yet been used.

---

### PROOF — Support uniqueness and automatic noncontainment

For one fixed (a)-set (S), there is at most one successful slope.

Indeed, suppose

[
EP+zB_{\rm num}=EP'+z'B_{\rm num}=w
\quad\text{on }S.
]

Then

[
E(P-P')+(z-z')B_{\rm num}
]

has at least (a=k+t) roots and degree at most (a-1), hence is zero. Reduction modulo (E) gives

[
(z-z')B_{\rm num}\equiv0\pmod E.
]

Reducedness gives (z=z').

Noncontainment is automatic. If (G\in F[X]_{<k}) explained the direction on an (a)-set,

[
G=-B_{\rm num}/E\quad\text{on }S,
]

then (EG+B_{\rm num}) would have (a) roots but degree at most (a-1). Hence (EG+B_{\rm num}=0), contradicting (\deg B_{\rm num}<\deg E) and (B_{\rm num}\neq0).

Thus each successful slope may be assigned a distinct exact (a)-support and distinct complement locator.

---

### PROOF — Resonant-circuit extraction with minimal support

Choose distinct successful slopes (z_1,\dots,z_m), exact supports (S_i), complements (T_i), and write

[
p_i=\Lambda_{T_i},\qquad \deg p_i=j,
]

[
Q_i=\operatorname{interp}*{S_i}(w)
=EP_i+z_iB*{\rm num},
\qquad \deg P_i<k.
]

Suppose

[
\sum_i c_i p_i=0.
]

By linearity of (\mathcal R_W),

[
0
=

# \sum_i c_i\mathcal R_W(p_i)

\sum_i c_iQ_ip_i.
]

Consequently,

[
E\sum_i c_iP_ip_i
+
B_{\rm num}\sum_i c_iz_ip_i
=0.
]

Reducedness gives

[
E\mid \sum_i c_iz_ip_i.
]

Hence there is (H\in F[X]) such that

[
\boxed{\sum_i c_ip_i=0,}
]

[
\boxed{\sum_i c_iz_ip_i=EH,}
]

[
\boxed{\sum_i c_iP_ip_i=-B_{\rm num}H.}
]

Since (\deg p_i=j),

[
\deg H\le j-t
]

whenever (H\neq0).

Now assume (m>j+1). The (p_i) lie in the ((j+1))-dimensional space (V_j), so choose an inclusion-minimal dependent subfamily (C). Let

[
\sum_{i\in C}c_ip_i=0
]

be its relation.

Minimality implies:

1. every (c_i\neq0);
2. the relation space on (C) is one-dimensional;
3. (|C|\le j+2);
4. (|C|\ge3), because distinct monic polynomials cannot be scalar multiples.

If (H=0), then

[
\sum_{i\in C}c_iz_ip_i=0
]

is another relation on (C). One-dimensionality gives a scalar (\lambda) with

[
c_iz_i=\lambda c_i
]

for every (i\in C). Since every (c_i\neq0),

[
z_i=\lambda
]

for all (i\in C), contradicting distinctness.

Therefore

[
\boxed{H\neq0}
]

for every minimal locator circuit extracted from distinct slopes.

In particular:

[
\boxed{j<t\quad\Longrightarrow\quad m\le j+1.}
]

This proves the requested resonant-circuit extraction, including minimal support and nonzero resonance.

---

### BANKABLE_LEMMA — Quantitative circuit synchronization

Let

[
A_0:F^m\to V_j,\qquad
A_0(c)=\sum_i c_ip_i,
]

and put

[
K=\ker A_0,\qquad r=\dim\operatorname{span}{p_i}\le j+1.
]

For (c\in K), define

[
\Theta(c)
=========

\frac{1}{E}\sum_i c_iz_ip_i
\in F[X]_{\le j-t}.
]

This is a well-defined linear map. Hence

[
\operatorname{rank}\Theta\le j-t+1.
]

Since

[
\dim K=m-r,
]

we obtain

[
\boxed{
\dim\ker\Theta
\ge
m-r-(j-t+1).
}
]

Every (c\in\ker\Theta) gives a synchronized relation

[
\sum_i c_ip_i=0,
\qquad
\sum_i c_iz_ip_i=0,
\qquad
\sum_i c_iP_ip_i=0.
]

Thus a sufficient condition for a nonzero synchronized relation is

[
m>r+j-t+1.
]

Using (r\le j+1), it suffices that

[
\boxed{m>2j-t+2.}
]

Moreover, the stacked column family

[
(p_i,z_ip_i)
]

has rank at most

[
r+j-t+1\le2j-t+2.
]

Therefore a support-minimal synchronized relation can be chosen with support size at most

[
\boxed{2j-t+3.}
]

A superlinear cloud therefore produces not merely one resonant circuit but a space of synchronized two-moment relations of dimension at least

[
m-O(n).
]

This is genuine synchronization, although it is not yet quotient synchronization.

---

### BANKABLE_LEMMA — Root-set multiplicity and common-core bounds

Let (C) be the support of a relation with all coefficients nonzero, and suppose

[
\sum_{i\in C}c_i z_i^s p_i=0
\qquad
(0\le s<d).
]

For (x\in L), define

[
I_x={i\in C:x\notin T_i}
={i\in C:x\in S_i}.
]

Evaluating at (x) gives

[
\sum_{i\in I_x}c_ip_i(x)z_i^s=0,
\qquad 0\le s<d.
]

If (1\le |I_x|\le d), the corresponding Vandermonde matrix in the distinct (z_i) has full column rank. Since every (c_ip_i(x)\neq0), this is impossible.

Thus

[
\boxed{|I_x|=0\quad\text{or}\quad |I_x|\ge d+1.}
]

Let

[
C_0=\bigcap_{i\in C}T_i
]

be the common root core. Since every support has size (a),

[
|C|a
====

\sum_{x\in L}|I_x|
\ge
(d+1)(n-|C_0|).
]

Therefore

[
\boxed{
|C_0|
\ge
n-\frac{|C|a}{d+1}.
}
]

Applications:

* An ordinary minimal circuit has (d=1), hence

  [
  |C_0|\ge n-\frac{|C|a}{2}.
  ]

* A synchronized two-moment circuit has (d=2), hence

  [
  |C_0|\ge n-\frac{|C|a}{3}.
  ]

This is the exact root-set consequence unavailable from abstract dimension alone.

If (g=\Lambda_{C_0}), write (p_i=g\widetilde p_i). Since (E) has no roots in (L),

[
\gcd(E,g)=1.
]

The circuit equations divide exactly:

[
\sum_i c_i\widetilde p_i=0,
]

[
\sum_i c_iz_i\widetilde p_i=E\widetilde H,
]

[
\sum_i c_iP_i\widetilde p_i=-B_{\rm num}\widetilde H.
]

Thus fixed common cores can be stripped without losing resonance.

---

### BANKABLE_LEMMA — Explicit line-field transfer, and no illicit entropy payment

Assume (L\subset\mathbb B), where (\mathbb B\subset K\subset F) are finite fields, and all slopes (z_i) lie in (K). Since the locators (p_i) are in (\mathbb B[X]), a minimal locator relation may be chosen with (c_i\in\mathbb B). Consequently

[
q(X):=\sum_i c_iz_ip_i\in K[X].
]

Let (\widehat E_K) be the monic generator of the contracted ideal

[
(E)F[X]\cap K[X].
]

Since (E\mid q) in (F[X]),

[
\boxed{\widehat E_K\mid q\quad\text{in }K[X].}
]

For a minimal circuit,

[
\deg\widehat E_K\le j.
]

This can replace (t) by the larger contracted degree (\deg\widehat E_K) in the circuit-nullity bounds.

This is a valid transfer from the slope field (q_{\rm line}=|K|). It is **not** an entropy argument and does not permit (q_{\rm line}) to pay a (q_{\rm gen}) locator-fiber bill.

---

## INVERSE_ATTEMPT

### The exact projected-scroll object

Define

[
\Phi=(\pi,\tau):V_j\longrightarrow A_E^2
]

and

[
K_0=\ker\pi\cap\ker\tau.
]

Explicitly,

[
K_0
===

{p\in V_j:
E\mid p
\ \text{and}
E\mid\mathcal R_W(p)}.
]

Since (\dim A_E=t),

[
\boxed{\dim(V_j/K_0)\le2t.}
]

In fact,

[
\dim K_0\ge j+1-2t.
]

At the entropy scale (t=o(n)), a large common pencil kernel is therefore usually unavoidable. Its existence is not evidence that the denominator is nonminimal.

Every locator satisfies (\pi(p_T)\neq0). If two successful locators have proportional images modulo (K_0),

[
\overline p_i=\lambda\overline p_h,
]

then

[
\pi(p_i)=\lambda\pi(p_h),\qquad
\tau(p_i)=\lambda\tau(p_h).
]

Using (\tau(p_i)=z_i\pi(p_i)) gives (z_i=z_h). Hence distinct slopes inject into projective locator images:

[
\boxed{
z_i\neq z_h
\quad\Longrightarrow\quad
[\overline p_i]\neq[\overline p_h]
\text{ in }\mathbb P(V_j/K_0).
}
]

The cloud is therefore a set of distinct projected locator points lying on the rank-one cone

[
{(u,v)\in A_E^2:u\neq0,\ u\wedge v=0}.
]

This is the exact “locator scroll section.”

---

### PROOF — Matrix-pencil/Kronecker alternative

Let (U=\operatorname{span}{p_i}), and consider the pencil

[
M(Z)=\tau|_U-Z\pi|_U.
]

If (M(Z)) has full column rank over (F(Z)), then (\dim U=r\le t), and some (r\times r) minor is a nonzero polynomial of degree at most (r). Every successful slope (z_i) is a root of this minor. Therefore

[
m\le r.
]

Consequently,

[
\boxed{m>r\quad\Longrightarrow\quad
M(Z)\text{ has a nonzero polynomial right-nullvector}.}
]

Thus there is

[
u(Z)=u_0+Zu_1+\cdots+Z^eu_e\in U[Z]\setminus{0}
]

with

[
M(Z)u(Z)=0.
]

Equating powers of (Z) gives the singular-chain equations

[
\tau u_0=0,
]

[
\tau u_s=\pi u_{s-1}
\qquad(1\le s\le e),
]

[
\pi u_e=0.
]

By Kronecker canonical form, the positive right minimal indices (e_h) satisfy

[
\boxed{\sum_h e_h\le t.}
]

The regular part contributes nonzero kernels at at most (t) distinct slopes. The remaining kernels are generated by:

* the constant common kernel (K_0);
* polynomial chains (u_h(z)) with total (z)-degree at most (t).

This is a complete linear-algebraic inverse classification. What remains is to classify root locators inside this scroll.

---

### PROOF — One-envelope split-root bound

Let

[
u(Z,X)=\sum_{\nu=0}^e Z^\nu u_\nu(X),
\qquad \deg_Xu_\nu\le j.
]

Suppose distinct (z_1,\dots,z_m) satisfy

[
p_i(X)=\lambda_i u(z_i,X),
\qquad
\lambda_i\neq0,
]

where every (p_i) is a degree-(j) locator with roots in (L).

Let

[
C={x\in L:u_\nu(x)=0\text{ for every }\nu},
\qquad c=|C|.
]

Then (C\subset T_i) for every (i).

For (x\notin C), the polynomial

[
u(Z,x)
]

is nonzero and has degree at most (e). Hence (x) belongs to at most (e) of the root sets (T_i). Double-counting the pairs

[
(i,x),\qquad x\in T_i\setminus C,
]

gives

[
\boxed{m(j-c)\le e(n-c).}
]

Therefore

[
\boxed{
m\le \frac{e(n-c)}{j-c}.
}
]

For a Kronecker chain, (e\le t). In particular, if

[
j-c\ge t,
]

then

[
m\le n.
]

Thus:

[
\boxed{
m>n
\quad\Longrightarrow\quad
j-c<t
}
]

for every subcloud lying on a single polynomial envelope. More than linearly many such locators force a fixed common root core of degree greater than (j-t).

If locators are block-pure across several right singular blocks, the same argument and (\sum e_h\le t) give a total of at most (n+t) slopes unless one block has moving root degree (<t).

So the regular and literal one-chain cases are controlled.

---

### Where entropy actually enters

Circuit extraction is field-free and starts once

[
m>j+1=O(n).
]

Circuit abundance therefore does not know the entropy boundary.

Locator divisibility records the codimension (t), and the contracted-denominator lemma may amplify it using a proved (q_{\rm line})-field transfer. That is still not entropy.

Entropy enters only when bounding root locators in the moving affine sections

[
K_0+\ker(\overline\tau-z\overline\pi).
]

There are approximately

[
\binom nj
=========

2^{(H_2(\rho)+o(1))n}
]

root locators. A generic residue condition has (q_{\rm gen}^{-t}) density per fixed slope, and a line section has (q_{\rm gen}^{1-t}) density only when the relevant map is actually defined over that generated field. This is where

[
t\log_2q_{\rm gen}
\approx H_2(\rho)n
]

arises.

No count involving (q_{\rm line}) can replace this unless a descent or contraction theorem has first been proved.

---

## COUNTERPACKET_SEARCH

### COUNTERPACKET — Reduced aperiodic mixed-scroll packet

This is a counterexample to the stronger claim that every superlinear finite cloud or every minimal resonant circuit must itself be quotient, fixed-core, single-chain, or nonminimal. It is **not** an asymptotic counterexample to the above-entropy theorem.

Work over (F_{17}). Let

[
L=F_{17}^{\times}
=================

{1,9,13,15,16,8,4,2},
]

so (n=8). Take the official rate

[
k=2,\qquad \rho=\frac14,
]

and

[
t=\sigma=2,\qquad a=4,\qquad j=4.
]

Set

[
E=X^2+3X+5,
\qquad
B_{\rm num}=5X+2.
]

The anchor is

[
\begin{array}{c|cccccccc}
x&1&9&13&15&16&8&4&2\ \hline
w(x)&10&16&14&3&2&6&0&5
\end{array}
]

All coefficients below are modulo (17). For each row, put (S_z=L\setminus T_z). Then

[
w=EP_z+zB_{\rm num}\quad\text{on }S_z,
]

with (\deg P_z<2):

[
\begin{array}{c|c|c}
z&T_z&P_z\ \hline
0&{1,9,13,16}&12+14X\
1&{1,13,16,2}&6+4X\
2&{15,16,8,4}&9X\
3&{9,13,16,2}&11+X\
4&{1,15,8,4}&15+16X\
5&{1,15,16,4}&14+11X\
9&{9,13,8,4}&13X\
10&{9,15,4,2}&2+14X\
13&{1,16,8,4}&6+5X\
15&{1,9,16,2}&7\
16&{1,9,13,2}&1+7X
\end{array}
]

Thus there are at least eleven distinct slopes, while (n=8).

The packet is reduced and aperiodic:

* (E) has no roots in (L).
* (\gcd(E,B_{\rm num})=1).
* The only proper quotient permitted by (M\mid\gcd(n,k)) is (M=2); (E\notin F_{17}[X^2]) because its (X)-coefficient is nonzero.
* The direction (-B_{\rm num}/E) has no degree-one denominator representation. For the nine possible monic linear denominators (X-\alpha), (\alpha\notin L), the interpolation degrees of
  ((X-\alpha)(-B_{\rm num}/E)) on (L) are

  [
  7,7,7,7,7,6,7,7,7,
  ]

  whereas a degree-one denominator representation would require degree (<k+1=3).
* The locator family has no global root core:

  [
  \bigcap_zT_z=\varnothing.
  ]

There is also a support-minimal, core-free resonant circuit. For

[
C={1,3,4,9,15}
]

and (p_z=\Lambda_{T_z}),

[
14p_1+11p_3+11p_4+14p_9+p_{15}=0,
]

while

[
14(1)p_1+11(3)p_3+11(4)p_4+14(9)p_9+15p_{15}
============================================

E(5+15X+11X^2)\neq0.
]

Every four of these five locators are independent, and

[
T_1\cap T_3\cap T_4\cap T_9\cap T_{15}=\varnothing.
]

Hence a minimal resonant circuit need not have a common root core.

The normalized locator-scroll maps, in bases

[
(1,X,X^2,X^3,X^4)
\quad\text{and}\quad
(1,X)\bmod E,
]

are

[
\pi=
\begin{pmatrix}
1&0&12&15&14\
0&1&14&4&3
\end{pmatrix},
]

[
\tau=
\begin{pmatrix}
7&8&2&3&1\
2&6&14&2&1
\end{pmatrix}.
]

Their common kernel is generated by

[
\kappa
======

3+9X+14X^2+16X^3+X^4.
]

There are two positive minimal-index-one chains:

[
u_1(z)
======

9+11X+4X^2+15X^3
+
z(5+3X+X^2),
]

[
u_2(z)
======

16+4X+13X^2
+
z(2+13X+X^3).
]

For every (z\in F_{17}),

[
\ker(\tau-z\pi)
===============

\langle\kappa,u_1(z),u_2(z)\rangle.
]

The eleven successful locators have the form

[
p_z=\kappa+b_zu_1(z)+c_zu_2(z),
]

with

[
\begin{array}{c|ccccccccccc}
z&0&1&2&3&4&5&9&10&13&15&16\ \hline
(b_z,c_z)&
(2,2)&(15,16)&(1,14)&(2,11)&(16,14)&
(0,10)&(6,9)&(1,16)&(14,0)&(1,4)&(15,11)
\end{array}
]

Most locators genuinely mix both moving blocks and the fixed kernel.

This packet establishes two route cuts:

1. minimal circuits cannot be classified one at a time;
2. a nonzero common pencil kernel does not imply denominator nonminimality.

The packet realizes the exact mixed-scroll obstruction that remains after the one-envelope bound.

---

## FAILED_STEP_IF_ANY

The failed implication is

[
\text{many resonant circuits}
\Longrightarrow
\text{one fixed core, one quotient, or one polynomial envelope}.
]

It is false without an additional concentration theorem. The finite packet above has:

* a minimal denominator;
* an aperiodic denominator;
* no global locator core;
* a core-free minimal resonant circuit;
* eleven slopes distributed through a fixed kernel plus two moving Kronecker blocks.

The third circuit equation does not create a third independent root moment. At a domain point (x\in S_i),

[
P_i(x)=\frac{w(x)-z_iB_{\rm num}(x)}{E(x)},
]

so the row (P_i(x)) is already an affine combination of the (1)-row and the (z_i)-row. Therefore

[
\sum c_iP_i(x)p_i(x)=0
]

does not improve “zero or at least three active supports” to “zero or at least four.”

A second failed shortcut is to call (K_0\neq0) denominator degeneracy. Since

[
\dim K_0\ge j+1-2t,
]

(K_0) is forced by dimension whenever (j\gg t), including the corrected entropy regime. Denominator minimality and a large fixed pencil kernel are compatible.

The missing step is therefore a root-locator inverse for **mixed moving cosets**, not another abstract circuit count.

---

## EXACT_NEW_WALL

### EXACT_NEW_WALL — Mixed Kronecker locator-scroll inverse

A precise next lemma is:

`W-MCA-AA-RES-MIXED-KRONECKER-LOCATOR-SCROLL-INVERSE`

Let (L_n\subset\mathbb B_n^\times) be a smooth multiplicative domain, with

[
n=k+t+j,\qquad k/n\to\rho
]

at one of the official rates, and suppose (t) clears the corrected (q_{\rm gen})-entropy and quotient reserve.

For every reduced, denominator-minimal, aperiodic balanced datum
((E,B_{\rm num},w)), form

[
\pi,\tau:V_j\to F[X]/(E)
]

as above, and put

[
K_0=\ker\pi\cap\ker\tau.
]

Let the quotient pencil have Kronecker decomposition

[
\ker(\overline\tau-z\overline\pi)
=================================

\operatorname{span}{
\overline u_1(z),\ldots,\overline u_h(z)
}
\oplus K_{\rm reg}(z),
]

where

[
\sum_{\nu=1}^h\deg_z u_\nu\le t
]

and (K_{\rm reg}(z)\neq0) at at most (t) slopes.

Prove that, for every fixed (\varepsilon>0),

[
#\left{
z\in F:
\exists,p=\Lambda_T,\ |T|=j,\quad
p\in
K_0+
\operatorname{span}{u_1(z),\ldots,u_h(z)}
\right}

> n^{1+\varepsilon}
> ]

forces at least one of:

1. **fixed core:** a subcloud of size (n^{1+\Omega(\varepsilon)}) has a common root core (C\subset L) with

   [
   j-|C|<t;
   ]

2. **quotient pullback:** a subcloud of size (n^{1+\Omega(\varepsilon)}) descends through

   [
   X\mapsto X^M,
   \qquad M>1,\quad M\mid\gcd(n,k);
   ]

3. **denominator descent:** the rational direction admits a denominator of degree (<t);

4. **field descent:** the pencil descends to a smaller field through an explicit contraction theorem, after which the appropriate (q_{\rm gen}) entropy bound applies.

The regular part and literal one-envelope part are already controlled by the lemmas above. The theorem is only needed for locators using variable (K_0)-lifts or genuinely mixing two or more moving blocks.

**Do you see a route to a full solve? If yes, what is the next exact lemma or construction?** Yes, at moderate confidence: prove the mixed Kronecker locator-scroll inverse above, most plausibly by an exterior-power theorem for projected root-locator configurations that classifies large rank-one sections as fixed-root or quotient-periodic. That would close the balanced arbitrary-anchor lane; the remaining (t>\sigma) regime would still require the syndrome affine-plane integration rather than an unsupported promotion from the balanced case.
