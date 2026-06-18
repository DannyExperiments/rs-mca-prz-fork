**Verdict:** both requested walls close. The Subcase A failure is not bad reduction and not a route cut. It is a line-specific tame (e=3) ramification point, compounded by a removable scalar factor in the unsaturated Cramer quartic. A clean horizontal line gives the ordinary Cycle-41 certificate. Subcase B is source-valid and globalizes to split-slope density (1/24+O(p^{-1/2})).

[
q_{\rm gen}=p,\qquad B=\mathbf F_p,\qquad
F=\mathbf F_{p^2}=B(\alpha),\qquad
q_{\rm line}=p^2,\qquad q_{\rm chal}\text{ unused}.
]

## PROOF

### 1. Independent characteristic-zero reconstruction

Put (K=\mathbf Q(i)) and

[
A_K=K[x]/(x^2+ix+1).
]

The coordinates (z_0,z_1,\tau_1,\dots,\tau_4) are restriction-of-scalars coordinates: they are (\mathbf Q)-coordinates, with

[
z=z_0+iz_1.
]

Thus the construction is over (K), but the resulting four scalar equations and the integral quartic descend to (\mathbf Q). Treating the (\tau_j) as arbitrary (K)-scalars would give the wrong dimension.

In (A_K),

[
x^2=-1-ix,\qquad x^3=i-2x,\qquad x^4=2+3ix.
]

For

[
L_\tau=x^4-\tau_1x^3+\tau_2x^2-\tau_3x+\tau_4
]

write (\lambda=[L_\tau]_E=a+cx). Direct reduction gives

[
a=2-i\tau_1-\tau_2+\tau_4,\qquad
c=3i+2\tau_1-i\tau_2-\tau_3.
]

The quotient polynomial determined by

[
W_{p-1},W_{p-2},W_{p-3},W_{p-4}
=1,i,1+i,1
]

has residue

[
[Q_S]_E=r_0+r_1x,
]

where

[
r_0=1-\tau_3+i(\tau_2-\tau_1),\qquad
r_1=\tau_2+i.
]

Let (d=1-z). Since (u-zb=1+dx),

[
(u-zb)\lambda
=(a-dc)+(c+da-idc)x.
]

Therefore the exact graph equations are

[
\begin{aligned}
\text{A: }& (a-dc)-ir_0=0,\qquad
(c+da-idc)-ir_1=0,\
\text{B: }& (a-dc)-2r_1=0,\qquad
(c+da-idc)+2r_0-2ir_1=0.
\end{aligned}
]

Taking real and imaginary parts gives (M_\epsilon(z)\tau+c_\epsilon(z)=0).

For Subcase A,

[
M_A=
\begin{pmatrix}
2z_0-3&z_1&1-z_0&1\
2z_1-1&1-z_0&1-z_1&0\
2-3z_1&2z_0-2&z_1-1&1-z_0\
3z_0-3&2z_1-2&1-z_0&-z_1
\end{pmatrix},
]

[
c_A=
\begin{pmatrix}
2-3z_1\
3z_0-4\
6-5z_0\
3-5z_1
\end{pmatrix}.
]

For Subcase B,

[
M_B=
\begin{pmatrix}
2z_0-2&z_1-3&1-z_0&1\
2z_1-1&1-z_0&-z_1&0\
2-3z_1&2z_0-2&z_1-3&1-z_0\
3z_0-5&2z_1-1&1-z_0&-z_1
\end{pmatrix},
]

[
c_B=
\begin{pmatrix}
2-3z_1\
3z_0-5\
9-5z_0\
3-5z_1
\end{pmatrix}.
]

Writing (\Delta_\epsilon=\det M_\epsilon),

[
\begin{aligned}
\Delta_A={}&-z_0^4+3z_0^3-2z_0^2z_1^2+2z_0^2
+3z_0z_1^2+3z_0z_1-11z_0\
&-z_1^4+4z_1^2-9z_1+9,
\end{aligned}
]

and

[
\begin{aligned}
\Delta_B={}&-z_0^4+6z_0^3-2z_0^2z_1^2-4z_0^2z_1-19z_0^2
+6z_0z_1^2\
&+4z_0z_1+30z_0-z_1^4-4z_1^3+5z_1^2+2z_1-19.
\end{aligned}
]

Let (N_{\epsilon,j}) be the Cramer determinant replacing column (j) by (-c_\epsilon). Then

[
\tau_j=\frac{N_{\epsilon,j}}{\Delta_\epsilon},
]

and the integral binary-quartic model is

[
P_\epsilon(z_0,z_1;X)
=\Delta_\epsilon X^4-N_{\epsilon,1}X^3
+N_{\epsilon,2}X^2-N_{\epsilon,3}X+N_{\epsilon,4}.
]

Consequently

[
\operatorname{disc}*X P*\epsilon
=\Delta_\epsilon^6\operatorname{disc}*X L*\tau.
]

This independently verifies the patched model. All bivariate Cramer numerators are recorded in the attached certificate.

---

### 2. Exact diagnosis of the A-side diagonal obstruction

Restrict Subcase A to (z_1=z_0=s). Then

[
\begin{aligned}
\Delta_A&=-(s-1)^2(4s^2+2s-9),\
N_{A,1}&=-12(s-1)^3,\
N_{A,2}&=-(s-1)^2(12s^2-2s-13),\
N_{A,3}&=-(s-1)(28s^2-60s+35),\
N_{A,4}&=-(s-1)^2(4s^2-18s+17).
\end{aligned}
]

Thus every coefficient of (P_A(s;X)) has the common factor (s-1). The checker did not saturate this vertical factor. Put

[
\widetilde P_A=P_A/(s-1).
]

Then

[
\operatorname{disc}*X P_A=(s-1)^8H*{16}(s),
\qquad
\operatorname{disc}*X\widetilde P_A=(s-1)^2H*{16}(s),
]

where (H_{16}) is squarefree at (p=7), satisfies (H_{16}(1)\ne0\pmod7), and has

[
\operatorname{Res}(H_{16},H_{16}')=3\pmod7.
]

The remaining factor ((s-1)^2) is not another removable artifact. It records genuine ramification of index (3).

Indeed, set (h=s-1) and use the infinity chart (y=V/U) in the binary quartic. The local equation is

[
\begin{aligned}
\Phi(h,y)={}&3y^3
+h(3+3y^2-4y^3-3y^4)\
&+h^2(-10+12y-22y^2+28y^3+10y^4)\
&+h^3(-4-12y^2-4y^4).
\end{aligned}
]

At ((h,y)=(0,0)),

[
\frac{\partial\Phi}{\partial h}=3\ne0.
]

Hence the total curve is smooth there and

[
h=-y^3+O(y^4).
]

The projection therefore has tame ramification index (e=3) whenever the residue characteristic is not (3). In particular, at (p=7) this is good tame reduction.

So the four proposed interpretations resolve as follows:

* It is **not** a branch collision causing bad reduction.
* It is partly a line artifact: the diagonal creates a special (e=3) branch point.
* The reconstructed characteristic-zero model is correct.
* The Cycle-41 test is overstrong: squarefree discriminant and disjointness from (\Delta) impose simple branching away from the Cramer divisor, not general tame good reduction.
* It is not a Subcase A route cut.

The original diagonal line is usable after primitive saturation and local normalization. Nevertheless, a different line gives the simpler Cycle-41-style certificate.

---

### 3. Clean Subcase A line

Take

[
L_A:\quad z_1=0,\qquad z_0=s.
]

Then

[
\Delta_{A,L}=-s^4+3s^3+2s^2-11s+9,
]

and

[
\begin{aligned}
N_1&=-3(s-1)(2s^2-5s+4),\
N_2&=-3s^4+10s^3-5s^2-12s+13,\
N_3&=-15s^3+55s^2-73s+35,\
N_4&=-s^4+4s^3-15s^2+25s-17.
\end{aligned}
]

The coefficients have gcd (1). Its primitive discriminant (H_A) has degree (24). At (p_0=7),

[
\begin{array}{c|ccccc}
&\operatorname{lc}\Delta&\operatorname{lc}H_A&
\operatorname{Res}(\Delta,\Delta')&
\operatorname{Res}(H_A,H_A')&
\operatorname{Res}(\Delta,H_A)\ \hline
\bmod 7&6&1&4&4&4
\end{array}
]

so the complete simple good-reduction gate passes.

The finite factorization certificate is:

[
s=1,\qquad \tau=(0,5,1,5),
]

giving

[
X^4-2X^2-X-2,
]

irreducible over (\mathbf F_7), hence type (4); and

[
s=0,\qquad \tau=(6,3,0,2),
]

giving

[
X^4+X^3+3X^2+2
=(X-1)(X^3+2X^2-2X-2),
]

where the cubic has no (\mathbf F_7)-root, hence type (13).

The full histogram is

[
{"13":4,\ "4":2,\ "112":1},
]

with no Cramer-singular (s\in\mathbf F_7).

A (4)-cycle and a (3)-cycle force arithmetic monodromy (S_4). The degree-one type (13) Frobenius is even, so the possible sign constant-field quotient is trivial. Therefore

[
G_{\rm geom}=G_{\rm arith}=S_4
]

at (p=7), and tame good reduction gives

[
G_{\rm geom}\bigl(\overline{\mathbf Q}(s)\bigr)=S_4
]

for the characteristic-zero A-line cover.

---

### 4. Clean Subcase B certificate

Retain the Cycle-40 line

[
L_B:\quad z_1=z_0=s.
]

Then

[
\Delta_{B,L}=-4s^4+4s^3-10s^2+32s-19,
]

and

[
\begin{aligned}
N_1&=4(2s^3-13s^2+14s-1),\
N_2&=-12s^4+4s^3-38s^2+120s-99,\
N_3&=2(16s^3-60s^2+76s-31),\
N_4&=-4s^4-20s^3-62s^2+244s-205.
\end{aligned}
]

Here

[
\operatorname{disc}_X P_B=16H_B(s),
\qquad \deg H_B=24.
]

At (p_0=19),

[
\begin{array}{c|ccccc}
&\operatorname{lc}\Delta&\operatorname{lc}H_B&
\operatorname{Res}(\Delta,\Delta')&
\operatorname{Res}(H_B,H_B')&
\operatorname{Res}(\Delta,H_B)\ \hline
\bmod 19&15&9&11&13&17
\end{array}
]

so all gates pass.

For the (S_4) witnesses,

[
s=6,\qquad \tau=(10,16,4,2),
]

gives the irreducible quartic

[
X^4+9X^3-3X^2-4X+2,
]

while

[
s=2,\qquad \tau=(14,0,12,7)
]

gives

[
X^4+5X^3+7X+7
=(X-5)(X^3-9X^2-7X-9),
]

with irreducible cubic factor.

Thus the B line also has characteristic-zero geometric monodromy (S_4).

---

### 5. Explicit sufficient bad-prime sets over (\mathbf Z[i])

For (\epsilon=A,B), define the conservative Cycle-41 integer

[
\begin{aligned}
\mathcal N_\epsilon={}&30,
\operatorname{lc}(\Delta_{\epsilon,L})
\operatorname{lc}(H_\epsilon),
\operatorname{Res}(\Delta_{\epsilon,L},\Delta_{\epsilon,L}')\
&\cdot\operatorname{Res}(\Delta_{\epsilon,L},H_\epsilon)
\operatorname{Res}(H_\epsilon,H_\epsilon').
\end{aligned}
]

A sufficient Gaussian bad-prime set is

[
\mathcal S_\epsilon
={\mathfrak p\subset\mathbf Z[i]:
\mathfrak p\mid(\mathcal N_\epsilon)}.
]

This is explicit but not claimed minimal. Intrinsically, (\Delta) is a Cramer divisor rather than the branch divisor, so the two (\Delta)-resultants may be omitted after using a normalized binary-quartic model.

For the relevant inert rational primes, the conservative sets reduce to:

[
\begin{aligned}
p\equiv3,7\pmod{20}\quad\text{(A):}\qquad
p\notin{&
3,\ 23,\ 4141312303,\ 65954521205827,\
&185013443251818763385500528775698067},
\end{aligned}
]

and

[
p\equiv11,19\pmod{20}\quad\text{(B):}\qquad
p\notin
{11,\ 986904239,\ 6003144422654343011}.
]

Because every branch prime satisfies (p\equiv3\pmod4), ((p)) is itself the unique inert prime ideal above (p) in (\mathbf Z[i]).

The fully factored resultants and all Gaussian-prime bookkeeping are in the attached bad-prime certificate.

---

### 6. Surface monodromy and split density

Let

[
D_\epsilon(z_0,z_1)
=\operatorname{disc}*X P*\epsilon(z_0,z_1;X).
]

Since its restriction to the certified line is nonzero, (D_\epsilon) is not the zero polynomial. Define

[
U_{\epsilon,p}
={(z_0,z_1)\in\mathbf A^2(\mathbf F_p):
\Delta_\epsilon D_\epsilon\ne0}.
]

The restricted line-cover monodromy is a subgroup of the two-dimensional generic monodromy. Since the line group is (S_4), the surface group, already contained in (S_4), must also be (S_4). This holds in characteristic zero and, for every relevant prime outside (\mathcal S_\epsilon), after reduction.

Over (U_{\epsilon,p}), form the ordered-root cover

[
Y_{\epsilon,p}\longrightarrow U_{\epsilon,p}
]

whose fiber consists of orderings ((r_1,r_2,r_3,r_4)) such that

[
P_\epsilon(z;X)
=\Delta_\epsilon(z)\prod_{j=1}^4(X-r_j).
]

It is a finite étale cover of degree (24). Geometric monodromy (S_4) says that this ordered-root torsor is geometrically irreducible. Hence Lang–Weil gives, for constants depending only on the fixed A or B model,

[
#Y_{\epsilon,p}(\mathbf F_p)
=p^2+O_\epsilon(p^{3/2}).
]

A fiber contributes (24) rational points exactly when its quartic splits completely with four distinct roots in (\mathbf F_p), and contributes none otherwise. Therefore

[
N_{\epsilon,\mathrm{split}}(p)
=\frac{p^2}{24}+O_\epsilon(p^{3/2})
=\left(\frac1{24}+O_\epsilon(p^{-1/2})\right)q_{\rm line}.
]

This proves the requested B-side global density step, and the same conclusion now holds for A.

---

### 7. Exact source-witness verification

Here

[
n=p,\qquad k=p-6,\qquad t=\sigma=2,\qquad
a=k+t=p-4,\qquad j=n-a=4,\qquad \delta=\frac4p.
]

Choose (W_p) with the prescribed top coefficients and residue (1+X):

[
W_p=X^{p-1}+\alpha X^{p-2}+(1+\alpha)X^{p-3}
+X^{p-4}+R_p,
]

where (\deg R_p<2) is chosen so that

[
[W_p]_E=1+X.
]

For a split quartic, let (T={r_1,r_2,r_3,r_4}\subset D), put (S=D\setminus T), and write

[
L_D=X^p-X=L_SL_T.
]

Divide

[
W_p=L_SQ_S+I_S,\qquad \deg I_S<p-4.
]

Set

[
\lambda=[L_T]_E,\qquad \ell=[L_D]_E.
]

Since (E) has no root on (D), (\lambda) is a unit modulo (E), and

[
[L_S]_E\lambda=\ell.
]

The defining surface equation is

[
(u-zb)\lambda-\ell[Q_S]_E=0.
]

Using (u=[W_p]_E), this becomes

[
\lambda([I_S]_E-zb)=0.
]

Therefore

[
[I_S]_E=zb.
]

Thus ((I_S,S)) is a residue-line witness:

[
\deg I_S<k+t,\qquad |S|=p-4=s_\delta,\qquad
I_S\equiv zb\pmod E,\qquad I_S=W_p\text{ on }S.
]

It is noncontained. Indeed, if some (G\in F[X]) with (\deg G<k) satisfied

[
G=-b/E\quad\text{on }S,
]

then (EG+b) would have (p-4) roots but degree (<p-4). Hence (EG+b=0), contradicting (b=X\ne0) and (\deg b<\deg E).

Therefore every counted split slope is a source-valid noncontained slope.

## AUDIT

The two Codex repairs are **mathematically correct but insufficient as a good-reduction audit**.

| Repair                                                                          | Judgment               | Reason                                                                                                                                   |
| ------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Replace bare Gaussian (i) by the residue pair ((i,0))                           | Correct                | Elements of (K[X]/E) are pairs (c_0+c_1X); bare (i) was being misread as such a pair and caused the type failure.                        |
| Wrap flattened real/imaginary equations as ((r,0)) before Gaussian determinants | Correct                | The four equations are (\mathbf Q)-scalar equations. Embedding each rational scalar in (K) gives the same determinant and Cramer system. |
| Treat (\Delta_L) as part of the branch divisor                                  | Insufficient           | (\Delta_L=0) is principally the Cramer/leading-coefficient locus. A root can move through infinity without ramification.                 |
| Require the discriminant numerator to be squarefree                             | Insufficient           | Tame (e=3) ramification gives a discriminant zero of multiplicity (2), as occurs at the A diagonal point (s=1).                          |
| Use the unsaturated integral quartic                                            | Wrong as a branch test | On the A diagonal it contains a common vertical factor (s-1), contributing an artificial sixth power to the discriminant.                |

The patched checker reconstructs the right algebra. Its conclusion “A has no good prime on this line” does not follow because its gate is stronger than tame good reduction.

## BANKABLE_LEMMA

For all sufficiently large primes in either congruence branch, outside the explicit finite bad set,

[
\Lambda^{\rm NC}*{2,,4/p}
\bigl(D=\mathbf F_p,\ k=p-6;\ F=\mathbf F*{p^2}\bigr)
\ge \frac{p^2}{24}-C_\epsilon p^{3/2}.
]

Equivalently,

[
\Lambda^{\rm NC}*{2,,4/p}
\ge \left(\frac1{24}-O*\epsilon(p^{-1/2})\right)q_{\rm line}.
]

All residue-line hypotheses have been checked: denominator nonvanishing, degree bounds, exact support size, congruence, anchor agreement, and noncontainment.

Moreover, the exact-normal-form theorem’s auxiliary hypothesis also holds: (E^3) is a degree-(6=n-k) polynomial nonzero on (D). Consequently the following restricted MCA corollary is source-valid:

[
\epsilon_{\rm mca}
\left(\operatorname{RS}
[\mathbf F_{p^2},\mathbf F_p,p-6],,\frac4p\right)
\ge \frac1{24}-C_\epsilon p^{-1/2}.
]

This is the only MCA promotion justified here. It is a high-rate, full-base-field, sub-reserve statement—not a corrected-reserve or smooth-multiplicative-domain theorem.

## ROUTE_CUT

The route

[
\text{“A fails G2/G3 on }z_1=z_0
\Longrightarrow\text{ A cannot globalize”}
]

is cut.

Also cut is the direct denominator-padding idea for reaching corrected reserve. Suppose one replaces (E_0) by (E_0R), with (R) nonzero on (D), and tries to make the (R)-component automatic. Since ([L_T]_R) is a unit, eliminating the (z)-coefficient forces (b\equiv0\pmod R). The natural elimination of the constant component forces (W\equiv0\pmod R). The graph equation then forces

[
Q_S\equiv0\pmod R.
]

But

[
\deg Q_S\le j-1.
]

Hence if (\deg R>j-1), then (Q_S=0), destroying the nontrivial top-symbol/quartic mechanism. A naïve CRT factor or denominator multiplication cannot lift the present construction to large (t).

## EXACT_NEW_WALL

The good-reduction and density walls are closed. The next exact wall is

```text
W-F1-AA-RES-T2J4-TO-CORRECTED-RESERVE-SLOPE-PRESERVING-LIFT
```

A useful exact formulation is:

For fixed (0<\rho<1) and smooth generated-field domains (H_n\subset B_n^\times), construct—or rule out—aperiodic residue-line data over extensions (F_n/B_n) satisfying

[
k_n=\rho n+O(1),\qquad
t_n=\sigma_n\gtrsim \frac{n}{\log q_{\rm gen}},
]

together with

[
\Lambda^{\rm NC}*{t_n,\delta_n}(H_n,k_n)
\ge c,q*{\rm line}
]

for a constant (c>0), while preserving denominator nonvanishing, noncontainment, and exclusion of quotient-periodic components.

The most concrete attempted construction is a **high-order automatic-constraint lift**: take (E_n=E_0R_n) but arrange the (R_n)-CRT component of

[
(u-zb)[L_T]*{E_n}-[L_D]*{E_n}[Q_S]_{E_n}
]

to be algebraically implied by the fixed degree-two (E_0)-component rather than identically zero. The route cut above shows that simple divisibility padding cannot achieve this; one needs Hermite, Frobenius-conjugate, or another genuinely redundant high-order residue structure.

## COUNTERPACKET

No corrected-reserve or prize-level `COUNTERPACKET` is established.

The proved family has

[
\rho=1-\frac6p,\qquad
\eta=\frac2p,\qquad
D=\mathbf F_p,
]

so it is neither fixed-rate nor a smooth multiplicative-domain construction above the corrected reserve. It is a complete restricted local (S_4)/density packing result and an exact restricted MCA lower bound, but not a corrected-reserve refutation, CA theorem, list-decoding theorem, line-decoding theorem, protocol statement, SNARK statement, or prize solve.

## EXPERIMENTAL

The attached checker independently reconstructs the source algebra; it imports no Cycle-41 checker code. Its symbolic identities, exact integer resultants, finite-field factorizations, and bad-prime factorizations reproduce cleanly.

* [Independent symbolic checker](sandbox:/mnt/data/cycle42_goodred_density_checker.py)
* [Full algebra and certificate](sandbox:/mnt/data/cycle42_goodred_density_certificate.json)
* [Exact integer resultants](sandbox:/mnt/data/cycle42_exact_resultants.json)
* [Factored Gaussian bad-prime sets](sandbox:/mnt/data/cycle42_bad_prime_sets.json)

**Do you see a route to a full solve?** Yes, but no further work on Subcase A good reduction is needed: that branch is closed. The next exact lemma is the corrected-reserve slope-preserving high-order residue lift above. Proving that construction would turn this (1/24)-density mechanism into a genuine fixed-rate corrected-reserve result; proving it impossible would identify the structural reason the present (t=2,j=4) mechanism cannot reach the full problem.
