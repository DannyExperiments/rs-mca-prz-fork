# COUNTERPACKET

**Confidence:** high for the construction and counts; moderate for the word “counterpacket” only because the phrase “explicit quotient/action-rank contribution” is not yet formally defined. The packet is uncharged by the banked (d_M(E)=\deg\minpoly([X^M]\bmod E)) ledger. A quotient term already closed under all projective RS automorphisms would charge it.

## 1. Exact counterpacket

There is a same-field, dyadic smooth-domain, official-rate Reed–Solomon instance with:

[
\rho=\frac14,\qquad q_{\rm gen}=q_{\rm line}=q_{\rm chal}<2^{256},
]

a balanced reduced residue datum of degree

[
t=\sigma=\frac n{256},
]

and one envelope-free syndrome line having more than (2^{200}) distinct noncontained bad slopes at radius

[
\delta=\frac{191}{256}.
]

For this datum:

[
d_D(E)=t
\qquad
\text{for every }D\mid \gcd(n,k),
]

including every active monomial quotient scale (D>\sigma). Thus the banked (X^D)-action-rank quotient term sees no low-rank denominator.

Meanwhile:

[
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}<1,
]

and every active ordinary multiplicative quotient profile has fewer than (2^{128}) possibilities—indeed, its maximal logarithm is below (100) bits under the Cycle 58 profile convention.

The finite prize threshold is

[
T=\left\lfloor\frac q{2^{128}}\right\rfloor<2^{126},
]

so the constructed line exceeds (T) by more than (2^{74}).

The missing structure is a **Möbius-conjugated quotient**. In the correct rational-action coordinate its action rank is one, even though every fixed-coordinate monomial action rank is full.

---

## 2. Construction and proof

### 2.1 Field and smooth domain

Use the classical Mersenne prime

[
p=2^{127}-1.
]

Set

[
F=\mathbf F_{p^2},\qquad q=|F|=p^2,
]

and take the norm-one subgroup

[
H={x\in F^\times:x^{p+1}=1}.
]

Then

[
n=|H|=p+1=2^{127}.
]

Thus the domain is exactly dyadic smooth.

A primitive element of (H) does not lie in (\mathbf F_p), and Frobenius acts on it by inversion. Hence (H) generates (F):

[
\mathbf F_p(H)=\mathbf F_{p^2}=F.
]

Therefore this is genuinely same-field:

[
q_{\rm gen}=q_{\rm line}=q.
]

Take

[
M=2^{119},
\qquad
N=\frac nM=256,
]

and

[
k=\frac n4=64M,
\qquad
t=\sigma=M.
]

Then

[
a=k+\sigma=65M,
\qquad
j=n-a=191M,
\qquad
\delta=\frac jn=\frac{191}{256}.
]

### 2.2 A nonmonomial automorphism of the domain

Define

[
\psi(X)=\frac{X+2}{2X+1}.
]

For (x\in H), using (x^p=x^{-1}),

[
\psi(x)^p
=========

# \frac{x^{-1}+2}{2x^{-1}+1}

# \frac{1+2x}{2+x}

\psi(x)^{-1}.
]

Hence

[
\psi(H)=H.
]

Its pole (-1/2) is not in (H), because

[
H\cap\mathbf F_p={\pm1}.
]

This (\psi) is not in the ordinary multiplicative dihedral normalizer: it sends

[
0\mapsto2,\qquad \infty\mapsto\frac12.
]

Let

[
\Omega=H^M.
]

Since (H) is cyclic,

[
|\Omega|=\frac nM=N=256.
]

For (y\in\Omega), define the block

[
B_y={x\in H:\psi(x)^M=y}.
]

These (256) blocks partition (H), and every block has size (M).

Its monic locator is

[
L_y(X)
======

\frac{(X+2)^M-y(2X+1)^M}
{1-y2^M}.
\tag{1}
]

The scalar (1-y2^M) is nonzero. Indeed, if it vanished, then (2^{-M}\in H\cap\mathbf F_p={\pm1}), forcing (2^M=\pm1). But the (2)-part of (p-1) is only (2), while (2\not\equiv\pm1\pmod p).

### 2.3 Denominator family

For a parameter (\vartheta\in F), define

[
E_\vartheta(X)
==============

\frac{(X+2)^M-\vartheta(2X+1)^M}
{1-\vartheta2^M}.
\tag{2}
]

We will select (\vartheta) such that:

[
\vartheta\notin\Omega,
\qquad
\vartheta\ne0,2^M,2^{-M}.
\tag{3}
]

Then (E_\vartheta) is monic of degree (M), has no root on (H), and is squarefree.

The no-domain-root statement follows immediately: if (x\in H) were a root, then

[
\vartheta=\psi(x)^M\in H^M=\Omega.
]

For separability, at a root one has (\psi(x)\ne0,\infty), and

[
\psi'(X)=\frac{1-4}{(2X+1)^2}\ne0.
]

Since (p\nmid M), every nonzero finite fiber of (\psi^M) is reduced.

Modulo (E_\vartheta),

[
(X+2)^M\equiv \vartheta(2X+1)^M.
\tag{4}
]

Combining (1) and (4),

[
L_y(X)
\equiv
\frac{\vartheta-y}{1-y2^M}(2X+1)^M
\pmod{E_\vartheta}.
\tag{5}
]

### 2.4 Full fixed-coordinate action rank

Let (\alpha,\beta) be roots of (E_\vartheta). If

[
\alpha^D=\beta^D
]

for some (D\mid k), then

[
\beta=h\alpha
\qquad\text{for some }h\in\mu_D\subseteq\mu_k.
]

Since both points lie in the same (\psi^M)-fiber,

[
\psi(\beta)=\zeta\psi(\alpha)
\qquad\text{for some }\zeta\in\mu_M.
]

Thus (\alpha) solves

[
\psi(hX)=\zeta\psi(X).
\tag{6}
]

For fixed ((h,\zeta)\ne(1,1)), equation (6) is a nonzero rational equation of degree at most two.

It cannot be an identity. If

[
\psi\circ(X\mapsto hX)
======================

(X\mapsto\zeta X)\circ\psi
]

held identically with (h\ne1), then (\psi) would map the fixed-point set ({0,\infty}) of multiplication by (h) to ({0,\infty}). But

[
\psi(0)=2,\qquad \psi(\infty)=1/2.
]

Hence each pair ((h,\zeta)) produces at most two bad values of (\vartheta=\psi(\alpha)^M).

There are at most (kM) such pairs, so fewer than

[
2kM=128M^2
\tag{7}
]

parameters (\vartheta) cause any collision under any power (X^D), (D\mid k).

Let (\mathcal G) be the set obtained by removing:

* (\Omega);
* (0,2^M,2^{-M});
* the at most (2kM) action-collision values.

Since

[
q=(256M-1)^2
]

and (2kM=128M^2),

[
|\mathcal G|>\frac q2.
\tag{8}
]

For every (\vartheta\in\mathcal G), the map

[
\alpha\longmapsto \alpha^D
]

is injective on the (M) roots of (E_\vartheta), for every (D\mid k). Since (E_\vartheta) is squarefree,

[
\boxed{d_D(E_\vartheta)=M=t
\quad\text{for every }D\mid k.}
\tag{9}
]

In particular:

* (E_\vartheta) is not a literal (E_0(X^D));
* no active (X^D)-action rank is low;
* even (d_M(E_\vartheta)=t).

### 2.5 The slope family

Let

[
h=\frac{k+t}{M}=65.
]

For every

[
\mathcal A\in\binom{\Omega}{65},
]

put

[
S_{\mathcal A}
==============

\bigsqcup_{y\in\mathcal A}B_y.
]

Then

[
|S_{\mathcal A}|=65M=k+t.
]

The support locator is

[
L_{\mathcal A}(X)
=================

\prod_{y\in\mathcal A}L_y(X).
]

By (5),

[
L_{\mathcal A}
\equiv
\kappa_{\mathcal A}(\vartheta)(2X+1)^{65M}
\pmod{E_\vartheta},
\tag{10}
]

where

[
\kappa_{\mathcal A}(\vartheta)
==============================

\prod_{y\in\mathcal A}
\frac{\vartheta-y}{1-y2^M}.
\tag{11}
]

Set

[
B_{\rm num}
===========

\operatorname{rem}*{E*\vartheta}(2X+1)^{65M}.
\tag{12}
]

Since (2X+1) is a unit modulo (E_\vartheta),

[
\gcd(E_\vartheta,B_{\rm num})=1.
\tag{13}
]

Define

[
z_{\mathcal A}=-\kappa_{\mathcal A}(\vartheta).
\tag{14}
]

### 2.6 Distinct-slope count

Let

[
L=\binom{256}{65}.
]

For two distinct (65)-sets (\mathcal A,\mathcal A'), the equation

[
\kappa_{\mathcal A}(\vartheta)
==============================

\kappa_{\mathcal A'}(\vartheta)
\tag{15}
]

is a nonzero polynomial equation in (\vartheta) of degree at most (65).

It is nonzero because its two sides are nonzero scalar multiples of split polynomials with different root sets (\mathcal A) and (\mathcal A').

Let (C(\vartheta)) be the number of unordered colliding pairs at parameter (\vartheta). Summing over (\vartheta\in\mathcal G),

[
\sum_{\vartheta\in\mathcal G}C(\vartheta)
\le
65\binom L2.
]

Therefore some (\vartheta\in\mathcal G) satisfies

[
C(\vartheta)
\le
\frac{65\binom L2}{|\mathcal G|}.
\tag{16}
]

If a slope has multiplicity (\nu), deleting all but one representative costs (\nu-1\le\binom\nu2). Hence

[
|\operatorname{im}z|
\ge
L-C(\vartheta)
\ge
L\left(
1-\frac{65(L-1)}{2|\mathcal G|}
\right).
\tag{17}
]

The standard type-class bounds give

[
\frac{2^{256H_2(65/256)}}{257}
\le
L
\le
2^{256H_2(65/256)}.
]

Numerically,

[
H_2(65/256)=0.8174108828\ldots,
]

so

[
L>2^{201.25},
\qquad
L<2^{209.26}.
\tag{18}
]

Also

[
q>2^{252},
\qquad
65<2^7.
]

Using (|\mathcal G|>q/2),

[
\frac{65L}{q}<2^{-35}.
]

Thus (17) gives the conservative exact bound

[
\boxed{|\operatorname{im}z|>2^{200}.}
\tag{19}
]

The actual logarithm of (L) is

[
\log_2\binom{256}{65}
=====================

205.129530\ldots,
]

and the averaging loss is negligible.

### 2.7 The residue datum and syndrome line

Fix a parameter (\vartheta) satisfying both (9) and (16). Write

[
E=E_\vartheta.
]

Take

[
w(X)=E(X)X^k.
]

Thus

[
f(x)=\frac{w(x)}{E(x)}=x^k
\qquad(x\in H).
]

Let

[
g(x)=-\frac{B_{\rm num}(x)}{E(x)}.
]

For (\mathcal A\in\binom{\Omega}{65}), define

[
Q_{\mathcal A}(X)
=================

E(X)X^k-L_{\mathcal A}(X).
\tag{20}
]

Both terms in (20) are monic of degree

[
k+t=65M,
]

so their leading terms cancel:

[
\deg Q_{\mathcal A}<k+t.
\tag{21}
]

On (S_{\mathcal A}),

[
L_{\mathcal A}=0,
]

and hence

[
Q_{\mathcal A}=EX^k=w.
\tag{22}
]

Modulo (E), equations (10)–(14) give

[
Q_{\mathcal A}
\equiv
-L_{\mathcal A}
\equiv
z_{\mathcal A}B_{\rm num}
\pmod E.
\tag{23}
]

Therefore

[
P_{\mathcal A}
==============

\frac{Q_{\mathcal A}-z_{\mathcal A}B_{\rm num}}E
]

is a polynomial of degree (<k). From (22),

[
f+z_{\mathcal A}g=P_{\mathcal A}
\qquad\text{on }S_{\mathcal A}.
]

Thus every distinct value (z_{\mathcal A}) is an MCA-bad slope at agreement (k+\sigma).

This gives one explicit residue datum

[
(E,B_{\rm num},w)
]

and one syndrome line

[
\ell(z)
= ======

\operatorname{syn}(x^k)
+
z,\operatorname{syn}(-B_{\rm num}/E)
]

with more than (2^{200}) distinct bad slopes.

### 2.8 Noncontainment and envelope exclusion

For any active support (S_{\mathcal A}), suppose the direction (g) agreed with a degree-(<k) polynomial (G). Then

[
EG+B_{\rm num}
]

would vanish at all (k+t) points of (S_{\mathcal A}), while

[
\deg(EG+B_{\rm num})<k+t.
]

It would vanish identically, contradicting

[
\gcd(E,B_{\rm num})=1.
]

Hence every incidence is transverse:

[
v\notin W_{H\setminus S_{\mathcal A}}.
]

The line is also completely envelope-free. If

[
u=\operatorname{syn}(x^k)\in W_R
]

for some (|R|<r=n-k), then (x^k) would agree with a polynomial of degree (<k) on more than (k) domain points. Their difference is a nonzero degree-(k) polynomial, which is impossible.

Therefore

[
\boxed{
\operatorname{span}(u,v)
\nsubseteq W_R
\quad\text{for every }|R|<r.
}
\tag{24}
]

There is no tangent or proper common-envelope charge.

The packet also has no fixed block or common support core: (\mathcal A) ranges over all (65)-subsets of the (256) blocks.

### 2.9 Denominator minimality

This is not a higher-degree chart hiding a lower-degree direction.

Suppose the same word (g) had a reduced representation

[
-\frac{B'}{E'}
]

with

[
\deg E'=t'<M,\qquad \deg B'<t'.
]

Equality on all (n) domain points gives

[
B_{\rm num}E'-B'E=0
\qquad\text{on }H.
]

Its degree is less than

[
M+t'<2M<n.
]

Hence it is the zero polynomial. Since (\gcd(E,B_{\rm num})=1),

[
E\mid E',
]

contradicting (t'<M).

Thus the degree (t=M) is minimal.

### 2.10 Why the current action-rank ledger misses it

In the quotient coordinate (\psi),

[
[\psi(X)^M]_E=\vartheta.
]

Consequently the rational-action rank

[
d_{\psi,M}(E)
:=
\deg\minpoly_F!\left(
\left[
\left(\frac{X+2}{2X+1}\right)^M
\right]_E
\right)
]

equals

[
\boxed{d_{\psi,M}(E)=1.}
\tag{25}
]

By contrast, (9) says

[
d_D(E)=t
]

for every fixed-coordinate monomial (X^D).

Thus:

[
\boxed{
\text{the invariant }d_D(E)\text{ is not closed under projective RS automorphisms.}
}
]

Indeed, (\psi) induces a monomial automorphism of the RS code through the homogeneous change of variable

[
P(X)
\longmapsto
(2X+1)^{k-1}P!\left(\frac{X+2}{2X+1}\right).
]

So this is a code-automorphic quotient packet invisible to the currently banked affine-coordinate quotient invariant.

---

## 3. Parameter ledger

[
\begin{aligned}
p&=2^{127}-1,\
F&=\mathbf F_{p^2},\
q_{\rm gen}=q_{\rm line}=q_{\rm chal}
&=(2^{127}-1)^2<2^{254}<2^{256},\
n&=2^{127},\
H&=\mu_n(F),\
\rho&=\frac14,\
k&=\frac n4=64M,\
M=t=\sigma&=2^{119}=\frac n{256},\
k+\sigma&=65M,\
j&=n-k-\sigma=191M,\
\delta&=\frac{191}{256}.
\end{aligned}
]

### Occupancy term

Using

[
\binom n{65M}
\le
2^{nH_2(65/256)}
================

2^{209.2572\ldots M}
]

and (q>2^{252}),

[
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
<
2^{209.258M-252(M-1)}
=====================

2^{-42.742M+252}
<1.
\tag{26}
]

The packet is therefore not an occupancy fluctuation.

### Active ordinary quotient term

Every active multiplicative quotient scale satisfies

[
D>\sigma=M,
]

so (D\ge2M). Its quotient universe has at most

[
\frac nD\le128
]

points.

Under the Cycle 58 full-profile convention, the largest active profile is at (D=2M):

[
\binom{127}{32},
\qquad
\log_2\binom{127}{32}=99.8062\ldots.
]

Even an extremely generous sum of all active fixed-coordinate quotient profiles is below (2^{131}), while the packet has more than (2^{200}) slopes.

### Finite (2^{-128}) relevance

[
T
=

\left\lfloor\frac q{2^{128}}\right\rfloor
<
2^{126}.
]

But

[
|\Gamma|>2^{200}.
]

Therefore

[
\frac{|\Gamma|}{q}

>

# \frac{2^{200}}{2^{254}}

2^{-54}

>

2^{-128}.
\tag{27}
]

This is not merely asymptotically superlinear; it fails the finite challenge by at least (74) bits in numerator size.

### Residual size

Since

[
n=2^{127},
]

the conservative bound (2^{200}) is

[
2^{200}=n^{200/127}>n^{1.57}.
]

The actual packet before the negligible collision loss is approximately

[
2^{205.13}=n^{1.615\ldots}.
]

---

## 4. Route-board impact

The current calibrated theorem is missing a structural branch.

The quotient ledger cannot be based only on

[
d_M(E)
======

\deg\minpoly([X^M]\bmod E)
]

in one fixed affine coordinate. That quantity is not invariant under monomial automorphisms of the RS code.

The necessary repair is at least:

[
\boxed{
d_{\phi,M}(E)
=============

\deg\minpoly!\left(
[\phi(X)^M]_E
\right),
}
]

where (\phi) ranges over relevant projective automorphisms of the domain, and the denominator of (\phi) is a unit modulo (E).

More invariantly, one should define a **split rational quotient**

[
R(X)=\frac{P(X)}{Q(X)}
]

of degree (M) by requiring that many values (y) have disjoint full fibers

[
P(X)-yQ(X)
]

splitting into (M) points of (H). Then define

[
d_R(E)
======

\deg\minpoly([R(X)]_E).
]

The present packet has:

[
R(X)=\psi(X)^M,
\qquad
d_R(E)=1.
]

Two route-board changes are forced:

1. Quotient templates must be closed under projective RS automorphisms or, more generally, split rational quotients.
2. The boundary scale (M=t=\sigma) cannot automatically be omitted. The current active convention (M>t) misses a full-profile packet at equality.

A corrected wall is therefore:

[
\boxed{
\texttt{W-MCA-PROJECTIVE-SPLIT-RATIONAL-ACTION-RANK-INVERSE}.
}
]

---

## 5. What remains open

This is not an unconditional asymptotic refutation of every possible calibrated theorem.

First, a theorem whose phrase “explicit quotient contribution” was already intended to include all projective or split-rational conjugates would charge this packet. The current attached audits do not yet contain that invariant classification; they bank only (X^M)-action rank and ordinary multiplicative quotient profiles.

Second, this exact finite construction uses a Mersenne unit-circle domain. An infinite asymptotic counterfamily would follow from infinitely many suitable Mersenne primes with appropriate dyadic spacing, which is not known. The finite official counterpacket itself is unconditional.

Third, after the quotient ledger is made projectively invariant, the original hard problem remains: prove the occupancy-calibrated bound for syndrome lines that are simultaneously:

[
\text{envelope-free},
\qquad
\text{split-rational-quotient-free},
\qquad
\text{full action-rank at every relevant quotient}.
]

## Do you see a route to a full solve? ROLE 03 - Counterpacket Hunter Against The Calibrated Theorem

Yes, but the quotient classification must be repaired before attacking the final inverse theorem.

The next exact lemma should be:

> **Split-rational quotient classification lemma.**
> Let (H=\mu_n\subset F), and let (R=P/Q\in F(X)) have degree (M\asymp\sigma), with (Q) nonvanishing on (H). Suppose (R) has (N_0) disjoint full (M)-point fibers contained in (H), where (N_0) is large enough that unions of fibers can produce more than (n^{1+\varepsilon}) constant-weight supports. Then either:
>
> 1. (R) is a monomial, dihedral, or projective-subline/unit-circle group quotient, up to pre- and post-composition by Möbius maps preserving the RS code; or
> 2. the number of full split fibers is too small to produce a superlinear distinct-slope packet.
>
> For every classified quotient (R), charge packets according to
> [
> d_R(E)=\deg\minpoly([R]_E)
> ]
> and the corresponding full support profile.

The first concrete sublemma is the projective stabilizer classification:

[
\operatorname{Stab}_{\mathrm{PGL}_2(F)}(\mu_n)
]

is dihedral in the generic case, with the exceptional norm-one/projective-subline cases explicitly identified. Once those exceptional automorphism-rich domains and the equality scale (M=\sigma) are charged, the remaining theorem is again the genuinely quotient-free, envelope-free calibrated syndrome transverse-secant inverse.
