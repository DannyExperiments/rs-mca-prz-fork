AUDIT

**Verdict:** The prize problem is not solved, and the current route is not one lemma from a full solve. The lower/failure side of same-field scalar MCA is theorem-grade; the syndrome reformulation and scalar-to-interleaved projection are exact. The MCA safe side and scalar list safe side remain separate major inverse theorems.

The proposed calibrated MCA statement does **not** yet imply the official finite challenge. Its occupancy variable is not correctly quantified, its quotient and envelope terms are not canonical or finitely budgeted, and it has no extension-field or explicit (2^{-128}) constants.

## 1. Exact theorem, counterexample, and conjecture ledger

Let

[
C=\operatorname{RS}[F,D,k],\qquad |D|=n,\qquad r=n-k,
]

and at reserve (\sigma) put

[
a=k+\sigma,\qquad j=r-\sigma=n-a.
]

Let (H\in F^{r\times n}) be an RS parity-check matrix, with columns (h_x), and define

[
V_T=\operatorname{span}_F{h_x:x\in T}.
]

### Referee ledger

| Branch                             | Exact statement                                                                      |             Status | Scope or defect                                                    |                    |                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------ | -----------------: | ------------------------------------------------------------------ | ------------------ | --------------------------------- |
| Scalar MCA lower/failure           | Bessel–Paley residue-line theorem below                                              |          **PROOF** | Same field; support-wise MCA                                       |                    |                                   |
| MCA denominator-free reformulation | Bad slopes are transverse incidences with (V_T)                                      | **BANKABLE_LEMMA** | Exact; counts slopes, not incidences                               |                    |                                   |
| Exact-(j) reduction                | Witnesses of size (<j) can be padded while preserving transversality                 | **BANKABLE_LEMMA** | Uses the RS/MDS full-spark property                                |                    |                                   |
| Hankel/locator formulation         | Bad locators satisfy the simultaneous rank-one minor system                          | **BANKABLE_LEMMA** | A normal form, not an upper bound                                  |                    |                                   |
| Close-support reduction            | Exchange distance (d<\sigma) forces a proper common envelope                         | **BANKABLE_LEMMA** | The strict inequality (d<\sigma) is essential                      |                    |                                   |
| Fixed-envelope internal witnesses  | A minimal (V_R) controls witnesses with (                                            |            R\cup T | \le r) linearly                                                    | **BANKABLE_LEMMA** | Does not control external secants |
| External-envelope shortening       | External witnesses are smaller punctured-domain MCA witnesses with the same (\sigma) | **BANKABLE_LEMMA** | New formal reduction below                                         |                    |                                   |
| Pure (n^{1+o(1)}) MCA upper        | False without occupancy                                                              | **COUNTEREXAMPLE** | Cycle 58 (t=2), high-(j) packet                                    |                    |                                   |
| Calibrated MCA upper               | Main term plus canonical quotient/envelope containers                                |    **CONJECTURAL** | Not currently a well-formed finite theorem                         |                    |                                   |
| Quotient action rank (d_M(E))      | (d_M(E)=\dim_FF[[X^M]_E])                                                            | **BANKABLE_LEMMA** | Datum-dependent, not intrinsically line-level                      |                    |                                   |
| Literal pullback test              | “(E\ne E_0(X^M)) means aperiodic”                                                    | **COUNTEREXAMPLE** | Explicit (F_{97}) packet                                           |                    |                                   |
| Old reduced quotient exponent      | Smaller ((\beta/H_2)\mathcal Q_H) charge suffices                                    | **COUNTEREXAMPLE** | Arbitrary anchors require at least full profile (2^{\mathcal Q_H}) |                    |                                   |
| All-denominator compression        | Every (t>\sigma) datum compresses to (t'\le \sigma)                                  | **COUNTEREXAMPLE** | Explicit (F_{17}), (t=3>\sigma=2) packet                           |                    |                                   |
| Scalar list identity               | Actual list equals a sum of full-support syndrome fibers                             |          **PROOF** | Includes all overagreement layers                                  |                    |                                   |
| Scalar full-support local limit    | Uniform finite upper on those fibers                                                 |    **CONJECTURAL** | Main scalar list wall                                              |                    |                                   |
| Scalar-to-interleaved reduction    | Scalar bound transfers under a collision inequality                                  |          **PROOF** | At the official same-field scale, holds for every (m)              |                    |                                   |
| Finite reserve formula             | Exact threshold is determined by the first safe integer reserve                      |          **PROOF** | No safe reserve has been evaluated                                 |                    |                                   |
| Cycle 55 conic fluctuation         | Produces an (\Omega(\sqrt q)) counterpacket                                          |     **NOT PROVED** | Only an (O(\sqrt q))-type calculation exists                       |                    |                                   |

### Exact scalar MCA lower theorem

Fix the same field (F=\mathbb F_Q), a degree-(t) polynomial (E) with no roots in (D), and interpret (t=\sigma), so

[
a=k+t,\qquad j=n-k-t,\qquad N=\binom na.
]

For every (a)-set (S), let (I_S(w)) be the degree-(<a) interpolant and

[
R_S(w)=[I_S(w)]_E\in A=F[X]/(E).
]

If (S,S') have exchange distance (d), then

[
\operatorname{rank}*F(R_S,R*{S'})=t+\min(t,d).
]

Define

[
K_d=\binom ad\binom jd,\qquad
\lambda=\frac{N}{Q^t},
]

and

[
V=\sum_{0\le d<t}K_d\left(Q^{-d}-Q^{-t}\right).
]

Then some anchor gives

[
\boxed{
\epsilon_{\mathrm{mca}}!\left(C,\frac jn\right)
\ge
\max\left{
\frac{\lambda}{\lambda+V},
\left(1-\frac V\lambda\right)_+
\right}.
}
]

Moreover,

[
\lambda>QV
\quad\Longrightarrow\quad
\epsilon_{\mathrm{mca}}!\left(C,\frac jn\right)=1.
]

With

[
J=\sum_{d<t}K_dQ^{-d},
]

one has (V\le J) and

[
J\le \exp!\left(2\sqrt{aj/Q}\right)\le \exp(n/\sqrt Q).
]

One correction to the raw file is necessary: (\lambda>QJ) is a **stronger**, not weaker, sufficient condition than (\lambda>QV).

If

[
t=(c+o(1))\frac{n}{\log_2Q},\qquad \log Q=o(n),
]

then (c<H_2(\rho)) implies all slopes are bad for sufficiently large (n). This is a theorem only when the anchor, code, residue algebra and slopes all use the same field (Q).

### Exact syndrome theorem

For (u,v\in F^r), define

[
\operatorname{Bad}_{\sigma}(u,v)
================================

\left{
z\in F:
\exists T\subseteq D,\ |T|\le j,\quad
u+zv\in V_T,\quad v\notin V_T
\right}.
]

Then the support-wise scalar MCA numerator is exactly

[
\boxed{
M_C(\sigma)=
\max_{u,v}
|\operatorname{Bad}_{\sigma}(u,v)|.
}
]

When (\sigma\ge1), (|T|\le j) may be replaced by (|T|=j).

This is the definitive all-denominator object. There is no (t<\sigma), (t=\sigma), or (t>\sigma) in the final statement.

### The canonical occupancy scale

Set

[
N_\sigma=\binom nj=\binom n{k+\sigma}.
]

Choose a direction (v) with (v\notin V_T) for every (j)-set (T). For uniformly random (u),

[
\mathbb E_u
#{(z,T):u+zv\in V_T}
====================

q_{\mathrm{line}}^{,1-\sigma}N_\sigma.
]

Therefore the intrinsic line-occupancy scale at fixed reserve is

[
\boxed{
\frac{N_\sigma}{q_{\mathrm{line}}^{\sigma-1}}.
}
]

This counts support incidences, not necessarily distinct slopes, but it is the unavoidable main scale and is attained up to shell factors by the lower constructions.

Consequently, the expression

[
\frac{\binom n{k+t}}{q^{t-1}}
]

is well-typed only when (t) itself specifies the radius, namely (a=k+t). In the fixed-reserve syndrome theorem, (t) is not a free parameter and the numerator must be (N_\sigma).

## 2. Proof and construction details

### 2.1 Syndrome equivalence and exact-(j) padding

Let a word line be (f+zg), and put

[
u=Hf,\qquad v=Hg.
]

A word (f+zg) is within error support (T) of the code precisely when

[
H(f+zg)\in V_T.
]

The same support explains the entire line precisely when both (u,v\in V_T). Under a landing (u+zv\in V_T), this is equivalent to (v\in V_T). Hence transversality is exactly (v\notin V_T).

Suppose (|T|=s<j) and (v\notin V_T). At an intermediate span (W=V_T), a new column (h_x) is bad for padding only if

[
v\in\operatorname{span}(W,h_x),
]

which implies (h_x\in\operatorname{span}(W,v)). Since the RS columns are full spark, the ((s+1))-dimensional space (\operatorname{span}(W,v)) contains at most (s+1) domain columns. Thus at most one column outside (T) is bad. Because (s<j<r\le n), a good padding column exists. Iteration gives an exact (j)-set while keeping (v\notin V_T).

### 2.2 Proof of the lower theorem

For two agreement sets (S,S') with common part (C) and exchange (d), the interpolants differ by

[
I_S(w)-I_{S'}(w)=L_C A,\qquad \deg A<d.
]

Modulo (E), multiplication by ([L_C]_E) is invertible because (E) has no root in (D). This gives

[
\operatorname{Im}(R_S,R_{S'})
=============================

{(x,y):x-y\in [L_CF[X]_{<d}]_E}
]

and rank (t+\min(t,d)).

For fixed (z), let

[
\nu_w(z)=#{S:R_S(w)=z[1]_E}.
]

The rank formula gives

[
\mathbb E_w\nu_w(z)^2=\lambda^2+\lambda V.
]

Paley–Zygmund yields

[
\Pr_w(\nu_w(z)>0)\ge\frac{\lambda}{\lambda+V}.
]

Summing over (z), some anchor occupies at least

[
Q\frac{\lambda}{\lambda+V}
]

slopes.

Likewise,

[
\mathbb E_w\sum_z(\nu_w(z)-\lambda)^2=Q\lambda V.
]

For some anchor the number of missed slopes is at most (QV/\lambda), producing the second bound. If (\lambda>QV), that integer is (<1), so no slope is missed.

Finally, if (R_S(w)=z), then

[
P_z=\frac{I_S(w)-z}{E}
]

has degree (<k). Noncontainment follows because a degree-(<k) polynomial agreeing with (-1/E) on (k+t) points would make (EG+1) a nonzero polynomial of degree (<k+t) with (k+t) roots.

### 2.3 Scalar full-support identity and interleaved projection

For (s\in F^r), define

[
\nu_e^\circ(s)
==============

#\left{
E\subseteq D:
|E|=e,\
\exists c\in(F^\times)^E,\ H_Ec=s
\right}.
]

The coefficient vector is unique because (e<r) and (H_E) has full column rank.

For a received word of syndrome (s),

[
\boxed{
L_{C,1}(\sigma;s)=
\sum_{e=0}^{r-\sigma}\nu_e^\circ(s).
}
]

The nonzero-coordinate condition is essential: it records the full error support and eliminates padding multiplicity.

Now let (C\subseteq K^n), (|K|=q), and suppose

[
L_1(\delta)\le \widehat L,
\qquad
\binom{\widehat L+1}{2}<q.
]

If an (m)-interleaved list contained (\widehat L+1) tuples, then for each pair of tuples the linear projections

[
\pi_\lambda(c_1,\ldots,c_m)=\sum_{i=1}^m\lambda_i c_i
]

that collide form a proper hyperplane in (K^m), of size at most (q^{m-1}). The union of all collision hyperplanes has size strictly below (q^m). A projection outside this union produces (\widehat L+1) distinct scalar codewords, all preserving the common agreement coordinates, contradicting the scalar bound.

Thus

[
L_m(\delta)\le\widehat L.
]

Diagonal embedding gives the reverse inequality, so whenever

[
\binom{L_1(\delta)+1}{2}<q,
]

one has

[
\boxed{L_m(\delta)=L_1(\delta)}
]

for every (m), not merely constant (m).

At the official same-field scale,

[
T=\left\lfloor\frac q{2^{128}}\right\rfloor,\qquad q\le2^{256},
]

and

[
\binom{T+1}{2}<q.
]

Therefore scalar safety and interleaved safety are exactly equivalent at every radius.

#### Base-field to extension-field transfer

Suppose (B\subseteq F), ([F:B]=e), and (D\subseteq B). If the scalar list bound over (B) is (L_B), coordinate expansion in a (B)-basis gives

[
\boxed{
L_{C_F,1}(\delta)\le L_B^e.
}
]

Indeed, each (F)-polynomial decomposes into (e) (B)-polynomials, and every agreement coordinate is an agreement in all (e) components.

Consequently, a base-field theorem implies the official (F)-valued grand list statement if

[
L_B^e\le T
]

and

[
\binom{T+1}{2}<|F|.
]

A stronger no-loss transfer (L_{C_F,1}\le L_B) follows if

[
\binom{L_B+1}{2}<q_{\mathrm{gen}}.
]

Thus a theorem over the actual alphabet immediately solves interleaving. A theorem only over (q_{\mathrm{gen}}) needs one of these explicit transfer conditions.

### 2.4 New bankable lemma: external-envelope shortening

This sharpens the unresolved common-envelope branch.

Assume the syndrome line is contained in a proper envelope:

[
u,v\in V_R,\qquad |R|=j+d<r,\qquad 0\le d<\sigma.
]

Because (H_R) is injective, choose unique word representatives (f_R,g_R) supported on (R) with syndromes (u,v).

Let (T) be an exact (j)-set witnessing a bad slope (z). Put

[
P=T\setminus R,\qquad e=|P|,
]

[
A=(D\setminus R)\setminus P,\qquad
B=R\setminus T,
]

and define the excess

[
h=e-(\sigma-d)=|R\cup T|-r.
]

For an external secant, (h\ge1). Direct counting gives

[
|A|=k-h,\qquad |B|=\sigma+h.
]

Landing provides a polynomial (p_z\in F[X]_{<k}) agreeing with (f_R+zg_R) on (A\cup B). On (A), the supported word is zero, so (p_z) vanishes on (A). Therefore

[
p_z=L_Aq_z,\qquad \deg q_z<h.
]

On (B),

[
q_z(x)=\frac{f_R(x)+zg_R(x)}{L_A(x)}.
]

Define a smaller word line on the punctured domain (R):

[
\widetilde f_A(x)=\frac{f_R(x)}{L_A(x)},\qquad
\widetilde g_A(x)=\frac{g_R(x)}{L_A(x)}.
]

Then (B), of size (h+\sigma), witnesses that

[
\widetilde f_A+z\widetilde g_A
]

is close to (\operatorname{RS}[F,R,h]). Moreover,

[
v\notin V_T
]

is equivalent to the absence of a degree-(<h) polynomial agreeing with (\widetilde g_A) on (B). Thus it is exactly a transverse MCA witness for the smaller code, with the **same reserve (\sigma)**:

[
|R|-(h+\sigma)
==============

(|R|-h)-\sigma.
]

Conversely, any such smaller-code witness lifts by multiplying its polynomial and word line by (L_A), extending the word by zero outside (R).

Hence:

[
\boxed{
\text{External common-envelope MCA contains smaller punctured-domain MCA as an exact subproblem.}
}
]

This has two consequences:

1. An external-envelope term is not automatically (n^{1+o(1)}).
2. Recursion leaves the smooth multiplicative-domain class: (R) is generally an arbitrary punctured set, and its rate (h/|R|) need not be one of the four official rates.

### 2.5 Quotient action rank is not a line invariant

For a fixed residue datum,

[
d_M(E)=\deg\minpoly_F([X^M]\bmod E)
]

is exact and useful. But it depends on the denominator chart.

Every word admits a degree-(r) denominator chart: choose any degree-(r) polynomial (E) with no root in (D), interpolate (E(x)g(x)) by a polynomial (Q) of degree (<n), and divide

[
Q=ER+B,\qquad \deg R<k,\quad \deg B<r.
]

Then

[
g=R+\frac BE
\quad\text{on }D.
]

On a multiplicative domain, one can choose (E=X^r-c), giving

[
d_r(E)=1.
]

Thus a classifier saying “there exists a denominator chart with small (d_M(E))” can classify essentially every line as quotient.

A concrete chart-dependence packet is:

[
F=\mathbb F_{17},\quad D=\langle2\rangle,\quad n=8,\quad k=r=4,
]

and (g(x)=x^{-1}). It has the degree-one chart

[
g=\frac1X.
]

It also has the reduced degree-four chart

[
E_2=X^4-2,\qquad
g=-2X^3+\frac{14X^3}{X^4-2}
\quad\text{on }D.
]

For (M=2),

[
d_2(X)=1,\qquad d_2(X^4-2)=2,
]

while for (M=4), (d_4(X^4-2)=1).

Therefore quotient/action rank must be tied to a canonical minimal datum or, preferably, to the witnessed support packet and the coordinate-group action. It cannot be inserted into a denominator-free syndrome theorem without such a definition.

### 2.6 Smallest explicit counterpackets in the supplied archive

“Smallest” here means the smallest explicit packet supplied or immediately extracted from the archive, not a proof of global minimality.

| Overstrong claim                                                   | Counterpacket                                                                                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Raw feasible supports approximate actual list size                 | (n=4,k=2,\sigma=1), received word a codeword. All four (3)-sets are feasible, but the actual list has size (1).                                                                                                    |
| Support incidences can replace distinct slopes                     | (n=8,k=4,\sigma=1,j=3). Take (u=h_{x_0}), (v=\operatorname{syn}(x^4)). The slope (z=0) has (\binom72=21) transverse support incidences but is one slope. The line has no proper envelope.                          |
| (Q^\sigma>N_\sigma) plus literal nonquotient implies (O(n)) slopes | (F=\mathbb F_{5^{64}},n=256,k=128,\sigma=2). Here (Q^2>N_\sigma) by (45.58) bits, yet the Bessel theorem gives more than (2^{100}) bad slopes and normalized error (>2^{-48}).                                     |
| Non-literal pullback means quotient-free                           | (F_{97}), (n=16,k=8,M=4,t=3), with (E=X^3+83X^2+2X+69) and (B=89X^2+94X+50). One has (d_4(E)=1), (E\ne E_0(X^4)), and slopes (96,9,80).                                                                            |
| The smaller canonical quotient exponent charges arbitrary anchors  | The punctured-fiber packet gives exactly (\binom{n/M-1}{k/M}=2^{\mathcal Q_H}) distinct slopes. With (\beta<C<H_2(\rho)), this exceeds (n^{1+o(1)}) while the older ((\beta/H_2)\mathcal Q_H) charge is sublinear. |
| Every high-denominator line compresses to (t'\le\sigma)            | (F_{17}), (D=\langle2\rangle), (n=8,k=2,\sigma=2), (g(x)=-x^{-3}). Its minimal denominator degree is (3>\sigma), yet (z=0) is active.                                                                              |
| Exact-boundary full-support control gives the whole list           | Use the quotient packet with agreement (k+\sigma+h), or tangent petals of size (\sigma+h+1). All codewords occur in weight layer (j-h), while the boundary layer (\nu_j^\circ) sees none.                          |
| Tangent/common-core list contribution is (O(1))                    | Fix a core of size (k-1) and disjoint petals of size (\sigma+1). The resulting actual list has size (\lfloor(n-k+1)/(\sigma+1)\rfloor), which is (\Theta(\log n)) at (\sigma=\Theta(n/\log n)).                    |
| (V_T\cap V_{T'}=V_{T\cap T'}) without a distance hypothesis        | Over (F_7), take (n=6,k=1,r=5,j=3,\sigma=2), and disjoint (3)-sets (T,T'). Their spans meet in dimension (1), while (T\cap T'=\varnothing). Here (d=3>\sigma).                                                     |
| Cycle 55 already gives a conic counterexample                      | No packet exists in the supplied files. An (O(\sqrt q)) upper fluctuation is not an (\Omega(\sqrt q)) construction.                                                                                                |

## 3. Parameter ledger

The following quantities must remain separate.

| Symbol                                       | Meaning                                                                                |   |                                                                                              |
| -------------------------------------------- | -------------------------------------------------------------------------------------- | - | -------------------------------------------------------------------------------------------- |
| (q_{\mathrm{gen}}=                           | B                                                                                      | ) | Field generated by the evaluation domain; pays base-field entropy and quotient constructions |
| (q_{\mathrm{line}}=                          | F                                                                                      | ) | Actual code alphabet and MCA slope field                                                     |
| (q_{\mathrm{chal}})                          | Protocol challenge field, if different; irrelevant without a protocol transfer theorem |   |                                                                                              |
| (r=n-k)                                      | Syndrome dimension                                                                     |   |                                                                                              |
| (\sigma)                                     | Reserve                                                                                |   |                                                                                              |
| (j=r-\sigma)                                 | Maximum error support                                                                  |   |                                                                                              |
| (a=k+\sigma)                                 | Required agreement                                                                     |   |                                                                                              |
| (N_\sigma=\binom n{k+\sigma})                | Number of boundary supports                                                            |   |                                                                                              |
| (T=\lfloor q_{\mathrm{norm}}/2^{128}\rfloor) | Exact finite numerator target                                                          |   |                                                                                              |
| (t)                                          | Residue-denominator chart degree; not intrinsic to a syndrome line                     |   |                                                                                              |
| (M)                                          | Multiplicative quotient-fiber size                                                     |   |                                                                                              |
| (d_M(E))                                     | Quotient-action rank of a fixed denominator datum                                      |   |                                                                                              |

### Finite necessary inequalities

In the same-field mathematical challenge, (q_{\mathrm{norm}}=q_{\mathrm{line}}).

The occupancy contribution fits under the prize budget only if

[
\frac{N_\sigma}{q_{\mathrm{line}}^{\sigma-1}}
\lesssim
\frac{q_{\mathrm{line}}}{2^{128}},
]

equivalently, before constants and floors,

[
\boxed{
\sigma\log_2q_{\mathrm{line}}
-\log_2N_\sigma
\ge128.
}
]

This is why a merely positive entropy surplus is insufficient.

The tangent floor requires

[
\max(1,j)\le T.
]

Every active quotient packet requires

[
\binom{n/M-1}{k/M}\le T
\qquad
\text{for every }M\mid\gcd(n,k),\ M>\sigma.
]

For the scalar list problem, generated-field entropy requires

[
\left\lceil\frac{N_\sigma}{q_{\mathrm{gen}}^\sigma}\right\rceil\le T,
]

or

[
\log_2N_\sigma-\sigma\log_2q_{\mathrm{gen}}
\le\log_2T.
]

The interleaved projection requires

[
\binom{T+1}{2}<q_{\mathrm{code}}.
]

It is automatic when

[
q_{\mathrm{code}}=q_{\mathrm{chal}}=q_{\mathrm{line}}\le2^{256},
]

but not if (q_{\mathrm{chal}}) is larger than the actual projection field.

### Smoothness and generated-field dependencies

* The syndrome equivalence, padding lemma and projection theorem do not require a smooth domain.
* The finite Bessel lower theorem is domain-uniform in the same field; smoothness is not its essential input.
* Quotient packets require multiplicative subgroup/coset structure and divisibility such as (M\mid\gcd(n,k)).
* The proposed upper inverse has only been formulated convincingly on smooth multiplicative domains.
* External-envelope descent produces arbitrary punctured domains, so a proof by recursion would need a theorem beyond the smooth-domain class.
* A base-field list theorem and an extension-field MCA theorem are different objects.
* The official finite caps (k\le2^{40}) and the four rates imply (n\le2^{44}). Therefore an unspecified (n^{1+o(1)}) estimate cannot certify the finite prize range.

## 4. Route-board impact

### Does the proposed calibrated theorem imply the official grand MCA challenge?

**No.**

There are seven independent failures.

1. **The occupancy variable is wrong unless (t=\sigma).**
   At fixed radius the canonical term is

   [
   \binom n{k+\sigma}/q_{\mathrm{line}}^{\sigma-1}.
   ]

   Every line admits a (t=r) chart. Plugging that chart into
   (\binom n{k+t}/q^{t-1}) would give (1/q^{r-1}), demonstrating that a free chart degree cannot define the global main term.

2. **The exception terms are undefined.**
   “Quotient/action-rank templates” and “tangent/common-envelope templates” are not predicates on a syndrome line with proved total budgets.

3. **The exception clause is currently vacuous.**
   Without a canonical partition and bounded overlap, every rich line can simply be declared a template.

4. **(d_M(E)) is chart-dependent.**
   It cannot be used as a denominator-free line classifier without a canonical datum theorem.

5. **External common envelopes are recursively MCA-hard.**
   The shortening lemma shows that this branch contains smaller punctured-domain MCA problems, not merely a linear tangent star.

6. **The theorem is asymptotic rather than finite.**
   The official challenge requires the entire explicit sum to be at most (T), not (n^{1+o(1)}).

7. **It lacks field and threshold closure.**
   A same-field theorem does not prove extension-valued MCA, and an upper at reserve (\sigma) does not identify the threshold without a certified failure at (\sigma-1).

A repaired structural theorem would imply safety only if it supplied explicit quantities

[
P_{\mathrm{prim}},\quad P_{\mathrm{occ}},\quad
P_{\mathrm{quot}},\quad P_{\mathrm{env}}
]

satisfying, uniformly over every official line,

[
|\operatorname{Bad}*\sigma(\ell)|
\le
P*{\mathrm{prim}}+P_{\mathrm{occ}}
+P_{\mathrm{quot}}+P_{\mathrm{env}}
\le T.
]

Nothing currently proves the second inequality.

### Does the scalar full-support theorem imply the official grand list challenge?

**Yes in the actual alphabet; conditionally over a generated subfield.**

If the theorem proves

[
\max_s\sum_{e=0}^{r-\sigma}\nu_e^\circ(s)\le T
]

over the actual code field (F), then the projection theorem gives the same bound for every interleaving arity (m). Matching lower bounds transfer by diagonal embedding. Thus the scalar and interleaved thresholds are identical.

If the theorem is only over (B\subsetneq F), it suffices to prove either

[
\binom{L_B+1}{2}<q_{\mathrm{gen}}
]

for a no-loss projection, or

[
L_B^{[F:B]}\le T
]

for the coordinate-product transfer. A bound stated only relative to (q_{\mathrm{line}}) does not automatically satisfy either condition.

The conjectural Cycle 58 scalar theorem does not yet close the challenge because:

* its quotient-periodic term is not an upper-classified object;
* it needs explicit finite constants;
* it must sum every weight layer, not only (\nu_j^\circ);
* its field-transfer inequality has not been instantiated.

### Minimal formal prize-solving statements

For MCA, define

[
\sigma_{\mathrm{MCA}}^*
=======================

\min{\sigma:M_C(\sigma)\le T}.
]

A minimal exact solution at a proposed reserve (\widehat\sigma) is

[
\boxed{
\begin{aligned}
&\forall u,v,\quad
|\operatorname{Bad}*{\widehat\sigma}(u,v)|\le T,\
&\exists u,v,\quad
|\operatorname{Bad}*{\widehat\sigma-1}(u,v)|>T.
\end{aligned}
}
]

For scalar list decoding, a minimal exact solution is

[
\boxed{
\begin{aligned}
&\max_s\sum_{e=0}^{r-\widehat\sigma}\nu_e^\circ(s)\le T,\
&\max_s\sum_{e=0}^{r-\widehat\sigma+1}\nu_e^\circ(s)>T.
\end{aligned}
}
]

Under the projection inequality, the second statement determines every interleaved threshold.

With the convention in the finite audit,

[
\delta_C^*
==========

1-\rho-\frac{\widehat\sigma}{n}+\frac1n.
]

No value of (\widehat\sigma) is currently proved.

### Correct route-board names

The current MCA wall should be strengthened to

[
\boxed{
\texttt{W-MCA-FINITE-CANONICAL-HEREDITARY-AFFINE-SECANT-CONTAINER}.
}
]

“Finite” is needed for (2^{-128}); “canonical” for nonvacuous templates; “hereditary” because of punctured-envelope descent; and “affine secant” because distinct slopes, not support incidences, are counted.

The scalar list wall is

[
\boxed{
\texttt{W-LIST-FINITE-FULL-SUPPORT-POINT-SECANT-KERNEL-CONTAINER}.
}
]

The interleaved projection wall is closed in the same-field official regime.

## 5. What remains open

The MCA branch still lacks:

* an explicit finite bound for envelope-free, quotient-primitive affine syndrome lines;
* a line-intrinsic quotient classifier capturing low action rank without becoming vacuous;
* a bounded-overlap accounting of all quotient scales and defect patterns;
* control of external common envelopes or a terminating hereditary recursion;
* an extension-valued (F/B) theorem;
* constants small enough to compare with (T);
* a proof that the internal support-wise definition is exactly the official protocol definition.

The list branch still lacks:

* a finite worst-syndrome bound on

  [
  \sum_{e\le r-\sigma}\nu_e^\circ(s);
  ]

* a canonical upper classification of quotient-core and overagreement packets;

* an upper theorem for the dimension-critical full-coordinate block secant kernels;

* explicit finite constants and generated-field transfer.

The Cycle 55 conic route has not produced a counterexample. The Cycle 58 high-(j), (t=2) packet cuts the uncalibrated target but does not attack the corrected reserve. No official-rate counterpacket presently beats the occupancy-calibrated, full-profile, envelope-aware conjecture.

## Do you see a route to a full solve?

A coherent route exists, but it is not close to completion and it is not one lemma.

The next indispensable **construction** is a syndrome-line-intrinsic quotient/envelope container system. For every selected bad-slope witness family it must:

1. assign each slope canonically to exactly one primitive, quotient, or envelope-descendant container;
2. capture every balanced low-(d_M(E)) packet without referring to a noncanonical denominator chart;
3. charge all (M)-quotient containers by an explicit full-profile budget;
4. descend external envelopes through the shortening lemma with bounded branching;
5. leave a primitive family to which an explicit finite occupancy bound applies.

After that construction, the next exact MCA lemma is:

[
\boxed{
|\operatorname{Bad}^{\mathrm{primitive}}*\sigma(\ell)|
\le
C*{\mathrm{occ}}
\frac{\binom n{k+\sigma}}{q_{\mathrm{line}}^{\sigma-1}}
+
P(n,\sigma),
}
]

for every envelope-free line, with explicit (C_{\mathrm{occ}}) and (P) valid throughout (n\le2^{44}), and with the resulting bound at most (T).

A potentially unifying formulation uses small-arity full-support secant certificates. Excessive scalar lists yield a point-secant certificate of arity about

[
\ell_1=\left\lceil\frac r\sigma\right\rceil,
]

while excessive MCA lines yield affine-rank-two certificates at arity about

[
\ell_2\asymp\frac{2r}{\sigma}.
]

A theorem classifying all such dimension-critical certificates into quotient, overagreement, envelope descent, or a finitely bounded primitive container could attack both remaining walls.

No such classification is currently proved. The strongest accurate assessment is therefore: **the route is identifiable, but the full solve is at least two major inverse/container theorems plus finite and field-transfer closure away.**
