# BANKABLE_LEMMA

The ROLE-04 problem is solvable at the level of an individual quotient packet. The resulting classification is invariant under denominator padding, cancellation, codeword gauges, and affine reparametrization of the slope.

The decisive conclusions are:

[
\boxed{\text{The canonical }\frac{\beta(\rho)}{H_2(\rho)}
\text{ quotient exponent is false for arbitrary anchors.}}
]

For a fixed quotient scale and fixed defect anchor, the sharp universal bound is the full quotient-support profile

[
\boxed{\min\left{|F|,\binom{n/M-c_T}{k/M}\right}},
]

where (c_T) is the number of (M)-fibres met by the defect set (T). Rank-one quotient action attains this bound with (c_T=1). Consequently a universal quotient charge must permit

[
\boxed{\min{|F|,2^{\mathcal Q_H(\eta)}}},
]

not (2^{(\beta/H_2)\mathcal Q_H(\eta)}).

What is not yet proved is that the union of all quotient packets occurring on one line is coverable by only (n^{o(1)}) fixed-defect packets. Thus the full profile is sharp per packet and necessary globally, but is not yet proved sufficient globally.

The relevant source material is the [Cycle 58 upper audit](sandbox:/mnt/data/cycle59_context/context/experimental/notes/m1/m1_cycle58_5p5_upper_audit.md), the [raw quotient counterpacket](sandbox:/mnt/data/cycle59_context/context/experimental/notes/m1/cycle58_5p5_raw/04_quotient_component_counterpacket_hunter.md), and the [all-denominator audit](sandbox:/mnt/data/cycle59_context/context/experimental/notes/m1/cycle58_5p5_raw/05_all_denominator_mca_auditor.md).

## 1. Exact theorem/counterexample/lemma

Let

[
C=\operatorname{RS}[F,D,k],\qquad D=\alpha H\subseteq F^\times,
\qquad |H|=n,
]

with (H) cyclic. Put (r=n-k), and fix target agreement

[
a=k+s,\qquad j=n-k-s.
]

Assume throughout the short-denominator condition

[
2s\le r.
]

This holds eventually in the official reserve regime (s=\Theta(n/\log n)).

### Lemma 1: canonical reduced denominator and intrinsic action rank

A reduced rational presentation of a non-codeword direction (\bar g\in F^D/C) is

[
g=G-\frac BE\quad\text{on }D,
]

where

[
\deg G<k,\qquad \deg E=\tau,\qquad \deg B<\tau,
\qquad E|_D\ne0,\qquad \gcd(E,B)=1.
]

Suppose the same direction has two reduced presentations with denominator degrees (\tau,\tau') and

[
k+\tau+\tau'\le n.
]

Then the two denominators are associates. If both are monic, they are equal; the numerators and polynomial parts are then equal as well.

Hence, when the intrinsic denominator degree is at most (s), the monic reduced denominator (E_{\bar g}) is canonical.

For every (M\ge1), define

[
A_E=F[X]/(E),\qquad \theta_M=[X^M]_E,
]

[
C_M(E)=F[\theta_M]\subseteq A_E,
\qquad
d_M(E)=\dim_F C_M(E).
]

Then

[
\boxed{
d_M(E)
======

# \deg\minpoly_F(\theta_M)

\min{\deg m:0\ne m\in F[Y],\ E(X)\mid m(X^M)}.
}
]

Thus the invariant is to be evaluated on the canonical reduced denominator, not on a padded displayed denominator.

If (E) is squarefree and split, with root set (R_E), then

[
d_M(E)=|{r^M:r\in R_E}|.
]

A literal pullback (E_0(X^M)) is therefore only one special way for (d_M(E)) to be small.

### Proof of denominator uniqueness

If

[
G-\frac BE=G'-\frac{B'}{E'}
\quad\text{on }D,
]

then

[
P=(G-G')EE'-BE'+B'E
]

vanishes on all (n) points of (D). Its degree is less than (k+\tau+\tau'\le n), so (P=0) identically.

Reducing modulo (E) gives (E\mid BE'). Since (\gcd(E,B)=1),

[
E\mid E'.
]

Similarly (E'\mid E). Hence the denominators are associates. Once the denominators are made monic and equal, degree comparison gives (G=G') and (B=B').

This also proves that a reduced degree-(\tau) packet cannot secretly descend to a smaller denominator in the short range.

---

### Definition: invariant fixed-defect quotient-action-rank packet

Choose an active quotient scale

[
M\mid\gcd(n,k),\qquad M>s.
]

Set

[
N=\frac nM,\qquad b=\frac kM,
\qquad
\pi_M:D\to\Omega,\quad \pi_M(x)=x^M,
]

so (|\Omega|=N) and every fibre has size (M).

Let (T\subset D) have size (s), and write

[
\Delta_T=\pi_M(T),\qquad c_T=|\Delta_T|,
\qquad
L_T(X)=\prod_{x\in T}(X-x).
]

The packet universe is

[
D_{M,T}
= ======

T\cup\pi_M^{-1}(\Omega\setminus\Delta_T).
]

Let (E) be the canonical reduced denominator of degree (\tau\le s), and put

[
\theta=[X^M]_E,\qquad C_M(E)=F[\theta].
]

A line (\mathcal L=f+Fg) is an ((M,T;\Phi,R)) fixed-defect QAR packet if, after adding a line of Reed–Solomon codewords and applying an affine reparametrization of the slope, its restriction to (D_{M,T}) has the form

[
f(x)=\frac{L_T(x)\Phi(x^M)}{E(x)},
\qquad
g(x)=-\frac{L_T(x)R(x^M)}{E(x)},
]

where

[
\Phi\in F[Y]\text{ is monic of degree }b,
\qquad
\deg R<b,
]

and

[
R(\theta)\in C_M(E)^\times.
]

The unit condition is essential: it says that the displayed fraction is already reduced. If (R(\theta)) is a zero-divisor, a denominator factor remains to be cancelled.

Equivalently, after multiplying the residue line by the unit ([L_T]_E^{-1}), its affine residue line is

[
\Phi(\theta)+F R(\theta)\subseteq C_M(E).
]

This definition is invariant because:

* padding and common-factor multiplication are discarded by canonical reduction;
* codeword gauges change numerators only by multiples of (E);
* affine slope changes preserve the affine residue line;
* the definition is equality of affine lines in the punctured quotient
  (F^{D_{M,T}}/C|*{D*{M,T}}), not equality of a particular displayed triple.

The complete fixed-packet invariant is not the integer (d_M(E)) alone. It is the triple

[
\boxed{
\left(
C_M(E),
\Phi(\theta)+F R(\theta),
\mathcal P_{M,T}^{(b)}(E)
\right),
}
]

where the quotient-locator image is

[
\mathcal P_{M,T}^{(b)}(E)
=========================

\left{
P_A(\theta):
A\in\binom{\Omega\setminus\Delta_T}{b}
\right},
\qquad
P_A(Y)=\prod_{y\in A}(Y-y).
]

The action rank (d_M(E)) is the dimension of the algebra containing this incidence. It is not by itself the complete packet count.

---

### Theorem 2: exact finite fixed-defect packet theorem

For an invariant packet as above, define

[
\Gamma_{M,T}
============

\left{
z\in F:
\Phi(\theta)-zR(\theta)
\in
\mathcal P_{M,T}^{(b)}(E)
\right}.
]

Then:

[
\boxed{
|\Gamma_{M,T}|
==============

\left|
\mathcal P_{M,T}^{(b)}(E)
\cap
\bigl(\Phi(\theta)-F R(\theta)\bigr)
\right|.
}
]

Every (z\in\Gamma_{M,T}) is a noncontained MCA-bad slope witnessed by a support

[
S_A=T\sqcup\pi_M^{-1}(A),
\qquad
|S_A|=s+Mb=k+s.
]

The exact finite bound is

[
\boxed{
|\Gamma_{M,T}|
\le
\min\left{
|F|,
\binom{N-c_T}{b}
\right}.
}
]

Since (T\ne\varnothing), (c_T\ge1), and hence

[
|\Gamma_{M,T}|
\le
\min\left{
|F|,
\binom{N-1}{b}
\right}.
]

#### Exact slope-collision criterion

If (A,A') both land, then

[
\boxed{
z_A=z_{A'}
\iff
P_A(\theta)=P_{A'}(\theta)
\iff
m_{M,E}(Y)\mid P_A(Y)-P_{A'}(Y)
}
]

where (m_{M,E}) is the minimal polynomial of (\theta).

Equivalently,

[
z_A=z_{A'}
\iff
E(X)\mid
\bigl(P_A-P_{A'}\bigr)(X^M).
]

Thus slope distinctness is an exact quotient-action statement, not a genericity assertion.

---

### Corollary 3: sharp full-profile replacement

Define the active full quotient profile

[
\boxed{
\mathcal Q_H(s/n)
=================

\max_{\substack{M\mid\gcd(n,k)\M>s}}
\log_2
\binom{n/M-1}{k/M}.
}
]

Every fixed-defect QAR packet contributes at most

[
\boxed{
\min{|F|,2^{\mathcal Q_H(s/n)}}.
}
]

This is sharp.

Indeed, choose (T) inside one (M)-fibre, so (c_T=1), and choose an external (M)-th power (c\notin\Omega). Let

[
E\mid X^M-c,\qquad \deg E=s<M.
]

Then

[
[X^M]_E=c,
\qquad
d_M(E)=1.
]

Take

[
\Phi(Y)=Y^b,\qquad R(Y)=1.
]

All quotient subsets land, with

[
z_A=c^b-P_A(c).
]

If (A\mapsto P_A(c)) is injective, then

[
\boxed{
|\Gamma_{M,T}|=\binom{N-1}{b}.
}
]

Therefore the full profile is necessary even for a single reduced, balanced, noncontained line.

## 2. Proof or construction details

For

[
A\in\binom{\Omega\setminus\Delta_T}{b},
]

put

[
U_A=\pi_M^{-1}(A),\qquad
S_A=T\sqcup U_A,
]

and define

[
Q_A(X)
======

L_T(X)
\left(
\Phi(X^M)-P_A(X^M)
\right).
]

Because (\Phi) and (P_A) are monic of degree (b), their leading terms cancel:

[
\deg(\Phi-P_A)\le b-1.
]

Hence

[
\deg Q_A
\le
s+M(b-1)
========

k-M+s
<
k,
]

using (M>s).

On (T), both (Q_A) and (L_T\Phi(X^M)) vanish. On (U_A),

[
P_A(x^M)=0,
]

so

[
Q_A(x)=L_T(x)\Phi(x^M).
]

Thus (Q_A) agrees with the anchor numerator on (S_A).

If

[
\Phi(\theta)-P_A(\theta)=z_A R(\theta),
]

then

[
E(X)\mid
Q_A(X)-z_A L_T(X)R(X^M).
]

Consequently,

[
C_A(X)
======

\frac{
Q_A(X)-z_A L_T(X)R(X^M)
}{E(X)}
]

is a polynomial of degree (<k). On (S_A), it agrees with (f+z_Ag). This proves badness.

For noncontainment, suppose a polynomial (G) of degree (<k) explained the direction on (S_A). Then

[
EG+L_TR(X^M)
]

would vanish on all (k+s) points of (S_A). But

[
\deg(EG+L_TR(X^M))
<
k+\tau
\le
k+s.
]

Hence the polynomial would vanish identically, forcing

[
E\mid L_TR(X^M).
]

This is impossible because ([L_T]_E) and (R(\theta)) are units. Therefore every packet witness is noncontained.

### Finite injectivity condition

Let

[
L=\binom{N-1}{b}.
]

For distinct (A,A'), the polynomial (P_A-P_{A'}) is nonzero and has degree at most (b-1). Hence the number of field elements causing any collision is at most

[
D_{\mathrm{coll}}
=================

(b-1)\binom L2.
]

If (M\mid |F^\times|) and

[
\boxed{
\frac{|F|-1}{M}

>

D_{\mathrm{coll}}+N,
}
]

there is an (M)-th power (c\notin\Omega) avoiding every collision. This gives the exact full-profile packet above.

### Exact (\mathbf F_{97}) certificate

The Cycle 58 certificate is:

[
n=16,\quad k=8,\quad M=4,\quad N=4,\quad b=2,\quad s=\tau=3.
]

Take (H=\langle8\rangle\le\mathbf F_{97}^\times),

[
T={1,22,96},
\qquad
c=4,
]

and choose three roots of (X^4-4):

[
R_E={14,17,80}.
]

Then

[
E=X^3+83X^2+2X+69,
]

[
L_T=X^3+75X^2+96X+22,
]

and

[
B=L_T\bmod E=89X^2+94X+50.
]

The three two-subsets of

[
H^4\setminus{1}={22,75,96}
]

give slopes

[
96,\qquad9,\qquad80.
]

Thus

[
|\Gamma|=3=\binom{N-1}{b}.
]

Moreover,

[
d_4(E)=1,\qquad E\ne E_0(X^4),
\qquad \gcd(E,B)=1.
]

I independently checked the polynomial expansions, remainder, quotient fibres, and all three slope values modulo (97).

## 3. Parameter ledger

For the exact finite theorem:

[
\begin{aligned}
q&=|F|,\
n&=|D|,\
k&=\dim C,\
s&=a-k,\
j&=n-k-s,\
\tau&=\deg E\le s,\
M&\mid\gcd(n,k),\quad M>s,\
N&=n/M,\
b&=k/M,\
c_T&=|\pi_M(T)|,\
d&=d_M(E)=\dim_FF[[X^M]_E].
\end{aligned}
]

The number of available supports is exactly

[
\binom{N-c_T}{b}.
]

The number of distinct slopes is the quotient-locator image size on one affine (F)-line in the (d)-dimensional algebra (C_M(E)).

The worst fixed-defect case is (c_T=1), not an arbitrary (T).

### Official-rate asymptotic separation

Let

[
h=H_2(\rho),
]

and let (\beta(\rho)) denote the old canonical exponent. At every official rate under discussion,

[
\beta(\rho)<h.
]

Choose

[
\boxed{\beta(\rho)<C<h.}
]

Let

[
N_v=2^v,\qquad
n_v=2^{\lfloor CN_v\rfloor},\qquad
M_v=n_v/N_v,
]

[
s_v=M_v-1,\qquad k_v=\rho n_v.
]

Then (M_v\mid k_v) for large (v), and

[
s_v
===

(C+o(1))
\frac{n_v}{\log_2n_v}.
]

The full packet profile satisfies

[
\log_2\binom{N_v-1}{\rho N_v}
=============================

hN_v+o(N_v),
]

so

[
|\Gamma_v|
==========

n_v^{h/C+o(1)}.
]

Since (C<h),

[
h/C>1.
]

By contrast, the old canonical charge is

[
2^{(\beta/h)\mathcal Q_H}
=========================

n_v^{\beta/C+o(1)},
]

and because (C>\beta),

[
\beta/C<1.
]

Hence

[
\boxed{
n^{\beta/C+o(1)}
<
n
<
|\Gamma_v|
==========

n^{h/C+o(1)}.
}
]

This proves that the (\beta/H_2) profile is not merely quantitatively loose: it gives the wrong side of the linear threshold for arbitrary anchors.

A same-field finite realization follows by taking a split prime sufficiently large that

[
\frac{q-1}{M}>D_{\mathrm{coll}}+N
]

and that the generated-field entropy reserve is cleared. The raw construction uses a polynomial-size prime progression; no extension-field entropy transfer is required.

## 4. Route-board impact

The following old criterion must be retired:

[
E\ne E_0(X^M)
\quad\Longrightarrow\quad
\text{quotient-free}.
]

Its denominator-level replacement is

[
d_M(E)=\deg E
\quad
\text{for every active }M.
]

But even this is only a component test. It does not itself prove that quotient-anchor packet intersections are small. The complete fixed-packet quantity is

[
\Xi_{M,T}(\mathcal L)
=====================

\left|
\mathcal P_{M,T}^{(b)}(E)
\cap
\mathcal A_{M,T}(\mathcal L)
\right|,
]

where (\mathcal A_{M,T}) is the normalized affine residue line.

Thus the correct hierarchy is:

[
\text{literal pullback}
\subsetneq
\text{low action rank}
\subsetneq
\text{realized QAR packet data}.
]

The first inclusion is strict. The second is not an equivalence because action rank describes the quotient algebra, whereas packet mass also depends on the anchor line and quotient-locator image.

### Quotient-clean MCA upper statement

Let (Q=q_{\rm line}), and let

[
\operatorname{Bad}_j(\ell)
==========================

\left{
z:
\ell(z)\in V_T,\ v\notin V_T
\text{ for some }|T|=j
\right}
]

be the syndrome transverse-secant bad-slope set.

Define (\operatorname{QAR}_j(\ell)) to be the union of slopes belonging to invariant realized QAR packets, and let (\operatorname{TE}_j(\ell)) be the tangent/common-envelope exceptional set.

The corrected quotient-clean theorem should be:

[
\boxed{
\left|
\operatorname{Bad}_j(\ell)
\setminus
\bigl(
\operatorname{QAR}_j(\ell)
\cup
\operatorname{TE}_j(\ell)
\bigr)
\right|
\le
n^{1+o(1)}
+
\frac{\binom{n}{k+s}}{Q^{s-1}},n^{o(1)}.
}
]

Equivalently, before subtracting tangent envelopes,

[
\left|
\operatorname{Bad}_j(\ell)
\setminus\operatorname{QAR}_j(\ell)
\right|
\le
n^{1+o(1)}
+
\frac{\binom{n}{k+s}}{Q^{s-1}},n^{o(1)}
+
|\operatorname{TE}_j(\ell)|.
]

The exact unsubtracted form is therefore

[
|\operatorname{Bad}_j(\ell)|
\le
n^{1+o(1)}
+
\frac{\binom{n}{k+s}}{Q^{s-1}},n^{o(1)}
+
|\operatorname{QAR}_j(\ell)\cup\operatorname{TE}_j(\ell)|.
]

One may replace the exact QAR union by

[
n^{o(1)}\min{Q,2^{\mathcal Q_H(s/n)}}
]

only after proving a packet-cover or packet-consolidation theorem. That step is currently missing.

The (\beta/H_2) quotient term should not occur in an arbitrary-anchor all-line theorem.

## 5. What remains open

The per-packet classification and bound are complete. Three global points remain.

First, several distinct defect sets (T) may potentially produce packets on the same affine line. The bound

[
|\Gamma_{M,T}|
\le
2^{\mathcal Q_H}
]

does not by itself bound their union.

Second, low (d_M(E)) must be converted into a realized packet by an inverse theorem. Small action rank is a denominator defect; it does not automatically supply the quotient-compatible anchor and full-fibre support family.

Third, after quotient and tangent packets are removed, the calibrated syndrome transverse-secant inverse remains open:

[
|\operatorname{Bad}^{\rm clean}_j(\ell)|
\stackrel{?}{\le}
n^{1+o(1)}
+
\frac{\binom n{k+s}}{Q^{s-1}}n^{o(1)}.
]

This is the main safe-side MCA wall and automatically includes the (t<s), (t=s), and (t>s) denominator charts.

Confidence is high for the canonical-denominator lemma, the invariant packet definition, the exact finite packet theorem, and the full-profile counterpacket. Confidence is moderate that the packet-cover route below is the correct next reduction.

## Do you see a route to a full solve? ROLE 04 - Quotient-Action-Rank Template Classifier

Yes.

The next exact lemma is not another estimate for (d_M(E)). It is the following cover theorem:

[
\boxed{\texttt{W-MCA-QAR-FIXED-DEFECT-COVER}}
]

> For every affine syndrome line (\ell), after tangent/common-envelope slopes are removed, the quotient-structured bad slopes are coverable by (n^{o(1)}) invariant fixed-defect QAR packets:
> [
> \operatorname{QAR}*j(\ell)\setminus\operatorname{TE}*j(\ell)
> \subseteq
> \bigcup*{\nu=1}^{n^{o(1)}}
> \Gamma*{M_\nu,T_\nu}.
> ]

By the theorem proved above, this would immediately imply

[
|\operatorname{QAR}_j(\ell)\setminus\operatorname{TE}_j(\ell)|
\le
n^{o(1)}
\min{|F|,2^{\mathcal Q_H(s/n)}}.
]

A natural inverse formulation is:

> If a quotient-correlated family of transverse slopes cannot be covered by (n^{o(1)}) fixed-defect packets, then its varying defect locators have a common positive-dimensional envelope, which must be charged to the tangent/common-envelope term.

That is the exact bridge from action-rank deficiency to a nonvacuous total slope budget.

If the cover lemma is false, the required counterconstruction is equally precise: one affine line, no common-envelope certificate, and

[
|\operatorname{QAR}_j(\ell)|

>

n^{o(1)}2^{\mathcal Q_H(s/n)}
]

arising from superpolynomially many inequivalent defect anchors. Such a construction would prove that even the full profile is insufficient as a global charge.

After the cover lemma, the remaining prize-level step is the quotient-free, envelope-free calibrated syndrome transverse-secant inverse.
