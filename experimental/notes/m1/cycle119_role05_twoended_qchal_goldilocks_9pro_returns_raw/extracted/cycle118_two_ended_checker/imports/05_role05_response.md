LABEL:

**PROOF — `L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE`**

Scope: finite attached-packet/source-scoped support-wise `LD_sw` theorem. Not an official/prize-adopted theorem and not ordinary fixed-word list decoding.

EXECUTIVE VERDICT:

There is a full agreement-263 construction preserving the entire Cycle84 numerator

[
N=52{,}747{,}567{,}092.
]

A common top seven-jet does **not** exist for the certified Cycle84 family, and no fixed odd-coset padding polynomial can create one. The successful replacement is a **two-ended locator functional**:

[
\text{common top six coefficients}
\quad+\quad
\text{common nonzero constant coefficient}
]

recover all seven coefficients of the multiplier polynomial required by the locator-to-MCA argument.

Move one odd-coset point from the fixed co-support padding (R) to the common agreement padding (A):

[
A^\star={\theta\eta^i:0\le i\le119},
\qquad
R^\star={\theta\eta^i:120\le i\le255}.
]

Then

[
|A^\star|=120,\qquad |R^\star|=136,
]

and the resulting packet co-supports have size

[
j=113+136=249.
]

The theorem obtained is

[
\boxed{
\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[\mathbb F*{17^{32}},H,256],263\bigr)
\ge N.
}
]

Consequently,

[
\boxed{
\epsilon_{\rm mca}
\left(
\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\frac{249}{512}
\right)
\ge
\frac{N}{17^{32}}

>

2^{-128}.
}
]

It also supplies exactly what an external convention using strict distance

[
d(\cdot,C)<\frac{125}{256},512=250
]

would require, because every constructed point has at most (249) disagreements.

THEOREM / COUNTERPACKET / ROUTE CUT:

### Theorem 1 — Two-ended locator-to-MCA lemma

Let (F) be a finite field, let (D\subset F^\times) contain (n) distinct points, and let (\beta\in F\setminus D). Let (\mathcal J) be a family of (j)-subsets of (D), with monic locators

[
P_J(X)=\prod_{a\in J}(X-a).
]

Let (\sigma\ge2), (j+\sigma\le n), and suppose:

[
\deg(P_J-P_{J'})\le j-\sigma+1
\qquad
(J,J'\in\mathcal J),
\tag{1}
]

so the locators have a common top (\sigma-1) coefficients, and suppose additionally that

[
P_J(0)=c\in F^\times
\qquad
(J\in\mathcal J)
\tag{2}
]

for one common nonzero (c).

Put

[
r=j+\sigma,\qquad k=n-r,\qquad C=\operatorname{RS}[F,D,k].
]

Then one affine line contains, for every (J\in\mathcal J), a support-wise noncontained bad point at slope

[
z_J=-P_J(\beta)^{-1}
]

with agreement support (D\setminus J). Hence

[
\operatorname{LD}_{\rm sw}(C,n-j)
\ge
#{P_J(\beta):J\in\mathcal J}.
\tag{3}
]

This is strictly weaker than requiring a common top (\sigma)-jet. The missing top coefficient is replaced by the common constant coefficient.

### Theorem 2 — Cycle118 agreement-263 row

For the packet’s Cycle84 shell, let (J_T\subset D_0=\langle\eta\rangle) be the certified (113)-point co-support and let

[
P_T(X)=\prod_{a\in J_T}(X-a).
]

Use the new fixed odd-coset set

[
R^\star={\theta\eta^i:120\le i\le255},
\qquad |R^\star|=136,
]

and define

[
J_T^\star=J_T\cup R^\star,
\qquad
P_T^\star=P_{R^\star}P_T.
]

Then the hypotheses of Theorem 1 hold with

[
(n,j,\sigma,k)=(512,249,7,256).
]

Moreover,

[
#{P_T^\star(\beta):T\in\mathcal P_0}
=N.
]

Therefore

[
\operatorname{LD}*{\rm sw}
\bigl(\operatorname{RS}[\mathbb F*{17^{32}},H,256],263\bigr)
\ge N.
]

### Route cut — fixed padding cannot manufacture a common seventh jet

For the current family there are shell tuples (T,T') with

[
\deg(P_T-P_{T'})=107.
]

For every fixed nonzero polynomial (Q),

[
\deg\bigl(QP_T-QP_{T'}\bigr)
============================

\deg Q+107.
]

Thus a fixed (P_R) cannot cancel the variable seventh coefficient. With (\deg P_R=136), the difference degree is (243), whereas a genuine common seven-jet at total degree (249) would require degree at most (242).

PROOF DETAILS:

### 1. Proof of the two-ended locator lemma

Set (r=j+\sigma), and use the standard weighted Vandermonde parity check

[
h_a=L_D'(a)^{-1}(1,a,\ldots,a^{r-1})^{\mathsf T},
\qquad a\in D.
]

For

[
W_J=\operatorname{span}{h_a:a\in J},
]

identifying coefficient vectors with polynomials of degree (<r) gives

[
W_J^\perp=P_JF[X]_{<\sigma}.
\tag{4}
]

Write

[
A(X)=a_0+a_1X+\cdots+a_{\sigma-1}X^{\sigma-1}.
]

Consider the coefficients of (P_JA) in degrees

[
j+1,j+2,\ldots,j+\sigma-1.
]

The term (a_0P_J) contributes nothing above degree (j). These (\sigma-1) top coefficients therefore depend only on

[
(a_1,\ldots,a_{\sigma-1}).
]

Condition (1) makes this dependence independent of (J). Because every (P_J) is monic, the resulting linear map is triangular with diagonal entries (1); it is therefore invertible. Thus those top coefficients recover (a_1,\ldots,a_{\sigma-1}).

The constant coefficient gives the remaining coefficient:

[
[X^0](P_JA)=P_J(0)a_0=ca_0.
]

Since (c\ne0), it recovers (a_0).

Consequently, there is a single linear functional

[
\ell:F_{<r}\longrightarrow F
]

such that

[
\ell(P_JA)=A(\beta)
\qquad
\text{for every }J\in\mathcal J,\ A\in F[X]_{<\sigma}.
\tag{5}
]

Let (y_0\in F^r) represent (\ell) under coefficient pairing, and set

[
y_1=(1,\beta,\ldots,\beta^{r-1})^{\mathsf T}.
]

For (Q=P_JA\in W_J^\perp),

[
\langle Q,y_0+zy_1\rangle
=========================

A(\beta)+zP_J(\beta)A(\beta).
]

At

[
z_J=-P_J(\beta)^{-1},
]

this vanishes for every (A), so

[
y_0+z_Jy_1\in W_J.
]

Surjectivity of the parity check produces words (f,g) with syndromes (y_0,y_1). Hence (f+z_Jg) differs from a codeword only on (J), and agrees with that codeword on (D\setminus J).

Noncontainment follows exactly as in Cycle116: the (j) Vandermonde columns indexed by (J), together with the column at (\beta), are independent because

[
j+1\le j+\sigma=r.
]

This proves (3).

### 2. The Cycle84 color shell fixes the missing constant coefficient

Let the seven moving block locators be

[
L_{t,i,a}(X)
============

\prod_{b\in B_{i,a}}
\bigl(X^2-\eta^{2t}3^b\bigr),
\qquad t=1,\ldots,7.
]

Each (B_{i,a}) has eight elements. Therefore

[
\begin{aligned}
L_{t,i,a}(0)
&=
\prod_{b\in B_{i,a}}
\bigl(-\eta^{2t}3^b\bigr)\
&=
\eta^{16t}3^{\sum_{b\in B_{i,a}}b}\
&=
3^{,t+\operatorname{color}(i,a)},
\end{aligned}
\tag{6}
]

using (\eta^{16}=3).

Let

[
Q_T(X)=\prod_{t=1}^7L_{t,i_t,a_t}(X).
]

For the Cycle84 shell,

[
\sum_{t=1}^7\operatorname{color}(i_t,a_t)\equiv4\pmod{16}.
]

Since (\sum_{t=1}^7t=28), equation (6) gives

[
Q_T(0)
======

# 3^{28+4}

# 3^{32}

1.

\tag{7}
]

The native locator includes the fixed singleton (1):

[
P_T(X)=(X-1)Q_T(X).
]

Hence, for every shell tuple,

[
\boxed{P_T(0)=-1.}
\tag{8}
]

This is the missing seventh invariant.

### 3. New (A/R) partition

Keep the same order-512 domain

[
H=D_0\sqcup\theta D_0.
]

Replace the Cycle116 partition by

[
A^\star={\theta\eta^i:0\le i\le119},
\qquad
R^\star={\theta\eta^i:120\le i\le255}.
]

Thus

[
|A^\star|=120,\qquad |R^\star|=136.
]

For each Cycle84 tuple,

[
J_T^\star=J_T\cup R^\star
]

has size

[
|J_T^\star|=113+136=249.
]

Its agreement support is

[
H\setminus J_T^\star
====================

(D_0\setminus J_T)\cup A^\star
]

and has size

[
143+120=263.
\tag{9}
]

### 4. Common top six after padding

Cycle116 proved

[
P_T(X)=X^{113}-X^{112}+O(X^{107}),
]

equivalently,

[
\deg(P_T-P_{T'})\le107.
]

Since (P_{R^\star}) is fixed and has degree (136),

[
\deg(P_T^\star-P_{T'}^\star)
\le136+107=243.
\tag{10}
]

For total degree (j=249) and (\sigma=7),

[
j-\sigma+1=249-7+1=243.
]

Thus (10) is exactly the common-top-six hypothesis of Theorem 1.

The constant coefficient is also common:

[
P_T^\star(0)
============

# P_{R^\star}(0)P_T(0)

-P_{R^\star}(0).
]

Every point in (R^\star) is nonzero, so

[
-P_{R^\star}(0)\ne0.
\tag{11}
]

Equations (10) and (11) provide the seven-dimensional evaluator.

### 5. Full numerator is retained

The certified native evaluation identity is

[
P_T(\beta)
==========

(\beta-1)3^{28}\Phi(T).
]

Therefore

[
P_T^\star(\beta)
================

P_{R^\star}(\beta)(\beta-1)3^{28}\Phi(T).
\tag{12}
]

Because (\beta\notin H),

[
P_{R^\star}(\beta)\ne0.
]

The factor multiplying (\Phi(T)) in (12) is fixed and nonzero. Multiplication by it, followed by inversion and negation, is bijective on (K^\times). Hence

[
#{P_T^\star(\beta):T\in\mathcal P_0}
====================================

# #\Phi(\mathcal P_0)

N.
\tag{13}
]

Applying Theorem 1 with

[
(n,j,\sigma,k)=(512,249,7,256)
]

and using (9) and (13) proves the claimed agreement-263 theorem.

### 6. Exact strict-ball interpretation

At length (512),

[
\frac{125}{256},512=250.
]

Strict distance (<250) means at most (249) disagreements, equivalently at least

[
512-249=263
]

agreements. Thus every one of the (N) constructed slopes satisfies the strict-ball convention at radius (125/256).

Under the attached source definition, the exact radius naturally attached to agreement (263) is

[
\delta^\star=\frac{249}{512},
]

since

[
\left\lceil
\left(1-\frac{249}{512}\right)512
\right\rceil
=263.
]

### 7. Why there is no hidden common seventh jet

Let (c_i) denote the (Y^5)-coefficient of the packet’s three base polynomials. The certificate gives

[
(c_1,c_2,c_3)=(4,9,11).
]

The (X^{10})-coefficient of a block locator is

[
[X^{10}]L_{t,i,a}
=================

c_i\eta^{6t}3^{3a}.
\tag{14}
]

Take the packet reference tuple

[
T_4=((1,4),(2,10),(3,14),(1,12),(3,0),(2,6),(3,8))
]

and replace only its first state by ((1,6)), obtaining (T_6). Since (4) and (6) have the same parity, their colors are equal, so both tuples remain in the color shell.

At the first slot, equation (14) changes by

[
\begin{aligned}
4\eta^6(3^{18}-3^{12})
&=
4\eta^6(9-4)\
&=
20\eta^6\
&=
3\eta^6
\ne0
\end{aligned}
]

in characteristic (17). Therefore

[
\deg(Q_{T_6}-Q_{T_4})=106,
\qquad
\deg(P_{T_6}-P_{T_4})=107.
]

So six is the exact maximal common **top-jet** order for the certified family.

A fixed padding polynomial cannot improve this:

[
P_RP_{T_6}-P_RP_{T_4}
=====================

P_R(P_{T_6}-P_{T_4}),
]

whose degree is (\deg P_R+107). Changing the fixed singleton changes neither this leading variation nor its nonvanishing. Changing (\beta) cannot change locator coefficients at all.

### 8. Block-template seven-jet obstruction

There is also a structural obstruction to replacing the current templates by genuine seven-jet shifted templates.

Let (E\subset\mathbb F_{17}^\times) have eight elements and suppose

[
f_E(Y)=\prod_{u\in E}(Y-u)
]

has zero (Y^7,Y^6,Y^5) coefficients. Let (g) be the locator of the complementary eight elements. Since

[
f_Eg=Y^{16}-1,
]

write

[
\begin{aligned}
f_E&=Y^8+aY^4+bY^3+cY^2+dY+e,\
g&=Y^8-aY^4-bY^3-cY^2-dY+h.
\end{aligned}
]

Coefficient comparison gives

[
eh=-1,\qquad e+h-a^2=0,
]

together with

[
d(h-e)=0,\qquad
c(h-e)-d^2=0,\qquad
b(h-e)-2cd=0
]

and

[
-2ab=0,\qquad
-2ac-b^2=0,\qquad
-2ad-2bc=0.
]

If (h\ne e), the first three displayed equations force

[
d=c=b=0.
]

If (h=e), then (a^2=2e\ne0), so (a\ne0), and the last three equations again force

[
b=c=d=0.
]

Thus necessarily

[
f_E(Y)=Y^8+aY^4+e.
]

Its root set is invariant under multiplication by the order-four subgroup

[
\mu_4\subset\mathbb F_{17}^\times.
]

Hence it is a union of two of the four (\mu_4)-cosets. There are only

[
\binom42=6
]

such root sets. Genuine seven-jet templates would therefore supply at most six distinct blocks per slot, and at most

[
6^7=279{,}936
]

distinct seven-slot supports even before imposing the color shell. They cannot retain the Cycle84 occupancy (N).

FIELD AND PARAMETER LEDGER:

| Quantity                       |                 Cycle116 |   Cycle118 construction |
| ------------------------------ | -----------------------: | ----------------------: |
| Base smooth field (K)          |    (\mathbb F_{17^{32}}) |   (\mathbb F_{17^{32}}) |
| Domain                         | (H=\langle\theta\rangle) |                    same |
| (n)                            |                      512 |                     512 |
| Native Cycle84 co-support      |                      113 |                     113 |
| Odd-coset fixed co-support (R) |                      137 |                     136 |
| Odd-coset common support (A)   |                      119 |                     120 |
| Total (j)                      |                      250 |                     249 |
| Common top coefficients        |                        6 |                       6 |
| Additional invariant           |                none used | common nonzero constant |
| Evaluator dimension (\sigma)   |                        6 |                       7 |
| (k=n-j-\sigma)                 |                      256 |                     256 |
| Agreement (n-j)                |                      262 |                     263 |
| Exact source radius            |        (250/512=125/256) |               (249/512) |
| Strict external radius handled |          not necessarily |              (<125/256) |
| Distinct numerator             |                      (N) |                     (N) |
| (q_{\rm gen})                  |                (17^{32}) |               (17^{32}) |
| (q_{\rm code})                 |                (17^{32}) |               (17^{32}) |
| (q_{\rm line})                 |                (17^{32}) |               (17^{32}) |
| (q_{\rm chal})                 |                     null |                    null |

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved, under the finite attached-packet and attached-manuscript support-wise definitions,

   [
   \operatorname{LD}*{\rm sw}
   (\operatorname{RS}[\mathbb F*{17^{32}},H,256],263)
   \ge52{,}747{,}567{,}092.
   ]

   This is not yet an official/prize-adopted theorem.

2. **Field ledger.**
   (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}). No separate challenge field occurs, so (q_{\rm chal}=\text{null}). No challenge denominator was invented.

3. **Numerator losses.**
   No endpoint, quotient, periodic, tangent, contained-line, affine-color, final-event, or charge operation occurs in the source-scoped `LD_sw` theorem. Same-slope collisions were already paid by using the distinct occupancy (N). The new padding changes every evaluation by one fixed nonzero scalar and therefore causes no further loss. Official event rules remain unpinned.

4. **Type of decoding result.**
   This is support-wise `LD_sw` on one affine line. It is not ordinary fixed-word list decoding. It supplies a strict-close-point statement only when the external convention is literally distance (<125/256).

5. **First clause still blocking official promotion.**
   The first missing item remains an independently authenticated authority contract satisfying `cycle117.official_source_contract.v1`: an external SHA-256 trust pin together with the required `authority`, `source_document`, `row.decision=ACCEPT`, `line_parameter`, `q_chal`, nine exhaustive `event_rules`, and `exhaustive_event_registry=true`. The packet contains the schema, not an authority-issued contract satisfying it.

6. **Next worker target.**
   The next exact artifact should be `V-CYCLE118-TWO-ENDED-263-TRANSFER-CHECKER`: a fail-closed checker for the common constant identity, the (120/136) partition, the two-ended evaluator lemma, full numerator retention, agreement (263), and noncontainment.

Confidence: **high**.

NEXT EXACT STEP:

Build and replay a deterministic checker with the following mandatory clauses:

```text
CYCLE84_SHELL_CONSTANT:
    for every block,
    L_{t,i,a}(0)=3^(t+color(i,a));
    therefore Q_T(0)=3^(28+4)=1 and P_T(0)=-1.

NEW_AR_PARTITION:
    A*=theta*eta^[0..119], |A*|=120;
    R*=theta*eta^[120..255], |R*|=136;
    A* disjoint R*, A* union R*=theta<D0>.

TWO_ENDED_COMMON_DATA:
    deg(P_R*(P_T-P_T')) <= 243;
    P_R(0)P_T(0) is one fixed nonzero constant.

EVALUATOR_BASIS:
    for m=0,...,6,
    ell(P_R P_T X^m)=beta^m.

PARAMETERS:
    n=512, j=249, sigma=7, r=256, k=256, agreement=263.

PRODUCT_SCALAR:
    P_R(beta)P_T(beta)
      = P_R(beta)(beta-1)3^28 Phi(T);
    distinct evaluations = 52,747,567,092.

NONCONTAINMENT:
    j+1=250 <= r=256.

TERMINAL:
    CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED.
```
