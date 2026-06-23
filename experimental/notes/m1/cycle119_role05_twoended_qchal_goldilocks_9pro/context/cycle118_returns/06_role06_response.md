LABEL:

**PROOF / BANKABLE_LEMMA / ROUTE_CUT**

`V-CYCLE118-CLOSE-POINT-LD-ADAPTER-AND-SPIKE-CUT`

`L-CYCLE118-FIXED-JET-EXACT-BOUNDARY-SHELL`

EXECUTIVE VERDICT:

**Confidence: high.**

Cycle116 can be strengthened, from the attached packet alone, to an ordinary close-point line-decoding lower bound under the standard closed-ball predicate.

There is a noncontained affine line in

[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],\qquad |H|=512,
]

with at least

[
N=52{,}747{,}567{,}092
]

distinct line points at **exact** Hamming distance (250) from (C). Its direction has maximum agreement exactly (256) with (C). Consequently:

[
\operatorname{CP}^{\rm nc}_{\le}
\left(C,\frac{125}{256}\right)\ge N,
]

and the result remains true even after excluding lines admitting a common code-line explanation on (262) coordinates.

Thus any external closed-ball line-decodability statement, with only a contained-line or target-scale common-support exception and with cap (a_{\rm LD}<N), is refuted.

For a strict-ball convention:

[
d_H(u_z,C)<\frac{125}{256}\cdot512=250
]

requires agreement (263). The direct fixed-jet line does not provide this. In fact, every nonzero parameter on that line has distance at least (250); hence the strict-ball count on this line is at most one. All (N) certified slopes lie exactly on the deleted boundary.

There is, however, a no-loss one-coordinate parameter shift:

[
\operatorname{CP}^{\rm nc}_{<}
\left(C,\frac{251}{512}\right)\ge N,
]

because (d_H=250<251). This radius is still below capacity (1/2).

THEOREM / COUNTERPACKET / ROUTE CUT:

### Theorem 1 — Fixed-jet exact-shell and deep-direction lemma

Let (C=\operatorname{RS}[F,D,k]), (|D|=n), and put (r=n-k). Let (\beta\notin D). Suppose the fixed-jet hypotheses hold for a family (\mathcal J) of (j)-subsets of (D), with

[
r=j+\sigma,
\qquad
\deg(P_J-P_{J'})\le j-\sigma
\quad(J,J'\in\mathcal J),
]

where (P_J(X)=\prod_{a\in J}(X-a)).

Let (u_z=f+zg) be the canonical line supplied by the Cycle116 fixed-jet construction. Then:

1. Its direction is

   [
   g(x)=\frac{V_D(\beta)}{\beta-x},
   \qquad
   V_D(X)=\prod_{a\in D}(X-a),
   ]

   and

   [
   \max_{c\in C}|{x:g(x)=c(x)}|=k.
   ]

2. For every nonzero (z\in F),

   [
   d_H(u_z,C)\ge j.
   ]

3. For each designated fixed-jet slope

   [
   z_J=-\frac1{P_J(\beta)},
   ]

   one has the exact equality

   [
   d_H(u_{z_J},C)=j.
   ]

4. At every agreement threshold (a>k), close-point and support-wise badness coincide on this line:

   [
   \begin{aligned}
   &{z:\exists c\in C,\
   |{x:u_z(x)=c(x)}|\ge a}\
   &\hspace{25mm}=
   {z:z\text{ is support-wise noncontained at agreement }a}.
   \end{aligned}
   ]

Thus this canonical line has no spike/common-support discrepancy above dimension (k).

### Cycle118 corollary

Let (K=\mathbb F_{17^{32}}), (H=D_0\sqcup\theta D_0), and use the Cycle116 sets

[
A={\theta\eta^i:0\le i\le118},
\qquad
R={\theta\eta^i:119\le i\le255}.
]

For every native Cycle84 support (T\subset D_0), (|T|=113), define

[
J_T=R\cup T.
]

Then

[
|J_T|=137+113=250.
]

The locators satisfy

[
P_{J_T}=P_RP_T
]

and therefore

[
\deg(P_{J_T}-P_{J_{T'}})
\le137+107
=244
=250-6.
]

Hence the fixed-jet theorem applies directly on (H) with

[
(n,k,j,\sigma)=(512,256,250,6).
]

Moreover,

[
P_{J_T}(\beta)=P_R(\beta)P_T(\beta),
]

and (P_R(\beta)\ne0). Multiplication by (P_R(\beta)), inversion, and negation preserve distinctness, so the Cycle84 occupancy gives (N) distinct slopes.

There is consequently one affine line (L=f+Kg) and a set (Z\subset K^\times), (|Z|=N), such that

[
d_H(f+zg,C)=250
\qquad(z\in Z).
]

Its direction satisfies

[
\operatorname{agr}(g,C)=256<262.
]

Therefore the line is not contained in (C), and no pair (c_f,c_g\in C) can explain (f,g) simultaneously on any support of size (262).

Under the standard definition

[
\operatorname{CP}^{\rm nc}_{\le}(C,\delta)
==========================================

\max_{\substack{g\ne0\ f+Fg\not\subset C}}
#{z:d_H(f+zg,C)\le\delta n},
]

we obtain

[
\boxed{
\operatorname{CP}^{\rm nc}_{\le}
\left(C,\frac{125}{256}\right)
\ge N.
}
]

Under strict distance,

[
\boxed{
\operatorname{CP}^{\rm nc}_{<}
\left(C,\frac{251}{512}\right)
\ge N.
}
]

If external notation ((\delta,a_{\rm LD},n+1))-line-decodable has precisely this close-point meaning, and the (n+1=513) slot adds no further filter, then

[
C\text{ is not }
\left(\frac{125}{256},a_{\rm LD},513\right)
\text{-line-decodable}
]

for every integer (a_{\rm LD}<N) under the closed-ball convention. Under the strict convention, the corresponding certified refutation is at radius (251/512), not (125/256).

### Strict-endpoint route cut

For the canonical direct line,

[
#{z:d_H(f+zg,C)<250}\le1.
]

Therefore the implication

[
LD_{\rm sw}(C,262)\ge N
\quad\Longrightarrow\quad
#{z:d_H(f+zg,C)<250}\ge N
]

fails at its first pointwise arrow. The strict-ball target at (125/256) requires agreement (263), and the (N) direct fixed-jet slopes contribute zero to it.

This does not prove that some entirely different line cannot witness a large (LD_{\rm sw}(C,263)). It proves that the canonical six-jet line cannot do so by reinterpreting its existing slopes.

PROOF DETAILS:

### 1. Direct smooth-domain locator construction

The native locators satisfy

[
P_T(X)=X^{113}-X^{112}+O(X^{107}),
]

so for all (T,T'),

[
\deg(P_T-P_{T'})\le107.
]

Since (R) is fixed and (|R|=137),

[
P_{J_T}-P_{J_{T'}}
=P_R(P_T-P_{T'}),
]

giving

[
\deg(P_{J_T}-P_{J_{T'}})\le244.
]

For (j=250) and (\sigma=6),

[
j-\sigma=244,
\qquad
j+\sigma=256=n-k.
]

These are exactly the fixed-jet hypotheses.

Also (\beta\notin H): the packet gives (\beta\in F_0\setminus D_0), while

[
H=D_0\sqcup\theta D_0
]

and (\theta D_0\cap F_0=\varnothing). Hence all locator evaluations at (\beta) are nonzero.

The packet certifies (N) distinct native values (P_T(\beta)). Therefore

[
-\frac1{P_R(\beta)P_T(\beta)}
]

also takes exactly (N) distinct values.

### 2. Exact-distance proof

Let (H_C) be the Reed–Solomon parity-check matrix used in the fixed-jet construction. For (U\subset D), write

[
W_U=\operatorname{span}{h_x:x\in U}.
]

Under the coefficient-polynomial pairing,

[
W_U^\perp=P_UF[X]_{<r-|U|}.
]

The canonical syndrome line is

[
s_z=y_0+zv(\beta),
]

where

[
\langle Q,y_0\rangle=\ell(Q),
\qquad
\langle Q,v(\beta)\rangle=Q(\beta).
]

The functional (\ell) depends only on the top (\sigma) coefficients in degrees

[
j,j+1,\ldots,j+\sigma-1.
]

Consequently,

[
\ell(Q)=0
\qquad\text{whenever }\deg Q<j.
]

Suppose (z\ne0) and (d_H(u_z,C)\le j-1). Then the syndrome (s_z) has an error representation supported on some (U) with (|U|\le j-1), so

[
s_z\in W_U.
]

Since (P_U\in W_U^\perp),

[
0=\langle P_U,s_z\rangle
=\ell(P_U)+zP_U(\beta).
]

But

[
\deg P_U=|U|<j
\quad\Longrightarrow\quad
\ell(P_U)=0,
]

while

[
z\ne0,
\qquad
P_U(\beta)\ne0.
]

This is a contradiction. Hence every nonzero parameter satisfies

[
d_H(u_z,C)\ge j.
]

For a designated slope (z_J=-P_J(\beta)^{-1}), the fixed-jet construction provides a codeword agreeing on (D\setminus J), so

[
d_H(u_{z_J},C)\le|J|=j.
]

Combining both inequalities gives

[
d_H(u_{z_J},C)=j.
]

For the smooth row, (j=250).

### 3. The direction is a deep hole

The canonical direction is

[
g(x)=\frac{V_H(\beta)}{\beta-x}.
]

Suppose a degree-(<256) polynomial (Q) agrees with (g) on a set (S\subset H). Then

[
R_Q(X)=(\beta-X)Q(X)-V_H(\beta)
]

vanishes on (S). This polynomial has degree at most (256), and it is not zero because

[
R_Q(\beta)=-V_H(\beta)\ne0.
]

Therefore

[
|S|\le256.
]

Conversely, interpolation on any (256) coordinates produces a degree-(<256) polynomial agreeing with (g) there. Hence

[
\operatorname{agr}(g,C)=256
]

exactly.

This immediately excludes:

[
f+Kg\subseteq C,
]

because that would require (g\in C), and it excludes any common-support/code-line exception requiring a support of size at least (262).

### 4. Why the spike separation does not apply to this line

The bridge note’s spike line has a direction that agrees with the zero codeword on (n-1) coordinates. Thus many close points can be explained on a support which already explains both line generators.

Here,

[
\operatorname{agr}(g,C)=256<262.
]

If (u_z) agrees with a codeword on any support (S) of size at least (262), no codeword can explain (g) on that same support. Therefore the slope is automatically support-wise noncontained.

Thus, on this line at agreement (262),

[
{\text{ordinary close slopes}}
==============================

{\text{support-wise bad slopes}}.
]

The spike example remains a valid global separation between the two notions, but it is irrelevant to this particular direct fixed-jet witness.

### 5. Strict versus closed radius

For integer Hamming distance (d):

[
d/n\le\delta
\quad\Longleftrightarrow\quad
d\le\lfloor\delta n\rfloor,
]

whereas

[
d/n<\delta
\quad\Longleftrightarrow\quad
d\le\lceil\delta n\rceil-1.
]

At

[
\delta_0=\frac{125}{256},
\qquad
\delta_0n=250,
]

the closed ball permits (d=250), while the strict ball permits only (d\le249). Equivalently:

[
a_{\le}(\delta_0)=262,
\qquad
a_{<}(\delta_0)=263.
]

All (N) certified points have (d=250), so all survive the closed convention and all are deleted by the strict convention.

At

[
\delta_1=\frac{251}{512},
\qquad
\delta_1n=251,
]

strict distance means (d\le250). Hence all (N) points survive.

FIELD AND PARAMETER LEDGER:

| Quantity                           | Cycle118 direct smooth line |
| ---------------------------------- | --------------------------: |
| Field (K)                          |       (\mathbb F_{17^{32}}) |
| (q_{\rm gen})                      |                   (17^{32}) |
| (q_{\rm code})                     |                   (17^{32}) |
| (q_{\rm line})                     |                   (17^{32}) |
| (q_{\rm chal})                     |                      `null` |
| Domain                             |    (H=\langle\theta\rangle) |
| Length (n)                         |                       (512) |
| Dimension (k)                      |                       (256) |
| Redundancy (r=n-k)                 |                       (256) |
| Native locator size                |                       (113) |
| Fixed (R)-padding size             |                       (137) |
| Direct smooth locator size (j)     |                       (250) |
| Fixed jet (\sigma)                 |                         (6) |
| Agreement (n-j)                    |                       (262) |
| Exact distance of certified slopes |                       (250) |
| Closed radius                      |           (250/512=125/256) |
| Strict no-loss shifted radius      |                   (251/512) |
| Direction agreement with (C)       |                       (256) |
| Certified numerator                |      (52{,}747{,}567{,}092) |

No challenge-field probability was introduced. If one separately samples the line parameter uniformly from (K), the corresponding density is (N/q_{\rm line}); that does not define or identify (q_{\rm chal}).

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved a finite packet-internal and attached-manuscript-source-valid theorem: the Cycle116 data yield a direct smooth-domain affine line with (N) distinct points at exact distance (250), with a deep-hole direction. This proves a standard closed close-point line-decoding lower bound and a strict lower bound after the exact shift to (251/512). It is not an official/prize-adopted theorem because the external predicate and authority contract remain unpinned.

2. **Field ledger.**
   (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}). The line, code, domain, locators, and slopes all lie in (K=\mathbb F_{17^{32}}). (q_{\rm chal}) remains `null`; it was not identified with (q_{\rm line}).

3. **Numerator losses.**
   Under the closed metric predicate, there is no endpoint loss, quotient loss, periodic loss, tangent loss, contained-line loss, common-support loss at agreement (262), affine-color loss, or charge loss. Under a strict ball at the same radius, the endpoint rule removes all (N) designated slopes because they have exact distance (250). Undefined official tangent, affine-color, final-event, or charge filters could still alter an official count.

4. **Object being proved.**
   The result simultaneously concerns support-wise (LD_{\rm sw}) and ordinary close-point line decoding on one line, because the deep direction makes the two slope sets equal at agreement (262). It is not fixed-word list decoding: the (N) objects are (N) distinct received words (f+zg), not (N) codewords near one received word.

5. **First missing or rejected official clause.**
   For a closed-ball external predicate with only contained-line or size-(262) common-support exceptions, the mathematical adapter is closed. Official promotion still lacks the authority-pinned definition of ((\delta,a_{\rm LD},n+1)), including the role of the (n+1) slot and any additional filters. If the official ball is strict at (125/256), the current certified numerator is affirmatively rejected by the endpoint rule, not merely unverified.

6. **Next worker target.**
   The next exact target is an agreement-(263) construction, not another adapter argument.

NEXT EXACT STEP:

Prove or refute the following explicit seventh-jet occupancy lemma:

[
\boxed{
\begin{gathered}
\text{There exists }\mathcal J'\subseteq\binom H{249}
\text{ such that}\
\deg(P_J-P_{J'})\le242
\quad\text{for all }J,J'\in\mathcal J',\
#{P_J(\beta):J\in\mathcal J'}
\ge52{,}747{,}567{,}092.
\end{gathered}
}
]

Here

[
249-7=242,
\qquad
249+7=256=n-k.
]

The fixed-jet theorem would then give one line with (N) distinct slopes at exact distance (249), hence agreement (263), closing the strict-ball endpoint at (125/256).

A logically distinct fallback is a cosupport-root theorem for the original padding line: prove that at least (N) designated explaining polynomials acquire one additional agreement coordinate in (R). No such root-incidence statement is present in the packet.
