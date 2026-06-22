LABEL:
**PROOF — finite ([256,137]) RS support-wise MCA / line-decoding transfer.**
**ROUTE_CUT — official Proximity Prize promotion.**
Confidence: **high** for the finite theorem; **unknown** for official-prize admission.

EXECUTIVE VERDICT:

The Cycle84 product is **not literally the RS slope**. The exact slope is

[
\boxed{
z_\tau=-P_\tau(\beta)^{-1}
=-\bigl(4(\beta-1)\bigr)^{-1}\Phi(\tau)^{-1}.
}
]

Thus

[
\Phi(\tau)=\Phi(\tau')
\iff
P_\tau(\beta)=P_{\tau'}(\beta)
\iff
z_\tau=z_{\tau'}.
]

Reciprocal evaluation and the common scalar are bijections on (F^\times), so the complete Cycle84 packet fiber spectrum transfers without loss:

[
\begin{aligned}
#{\text{packet slopes}}&=52{,}747{,}567{,}092,\
\max_z#{\tau:z_\tau=z}&=2,\
#{\text{double packet slope fibers}}&=12,\
#{\text{packet fibers of size}\ge3}&=0.
\end{aligned}
]

This produces one affine line for

[
C=\operatorname{RS}[F,\langle\eta\rangle,137],
\qquad |D|=256,
]

having at least (52{,}747{,}567{,}092) distinct support-wise noncontained bad slopes at agreement (143), equivalently radius (113/256).

The color equation (c_L+c_R=4\bmod16) is **not** an official MCA support or witness condition. It is exactly the Cycle84 packet filter and fixes the support product:

[
\prod_{x\in T_\tau}x=1,\qquad P_\tau(0)=-1.
]

No additional division by (16), affine-color loss, or endpoint loss is justified.

This is a paper-facing finite RS-MCA/line-decoding theorem, not an official Proximity Prize proof. The one-copy rate is (137/256), not an official target rate, and (q_{\rm chal}) is not instantiated.

EXACT THEOREM OR OBSTRUCTION:

### BANKABLE_LEMMA: fixed-jet reciprocal-slope transfer

Let (D\subset F), (|D|=n), and let (T) range over distinct (j)-subsets of (D), with monic locators

[
P_T(X)=\prod_{x\in T}(X-x).
]

Fix (\beta\notin D), (\sigma\ge1), and put

[
r=j+\sigma,\qquad k=n-r.
]

Suppose the locators have a common top (\sigma)-jet:

[
Z^jP_T(Z^{-1})\equiv p(Z)\pmod {Z^\sigma},
]

independently of (T). Then there is one affine line (u_z=f+zg) in
(F^D) such that every (T) gives a support-wise noncontained bad slope

[
z_T=-P_T(\beta)^{-1}
]

with witness support (S_T=D\setminus T), of size

[
|S_T|=n-j=k+\sigma.
]

Consequently,

[
\operatorname{LD}_{\rm sw}(\operatorname{RS}[F,D,k],n-j)
\ge
#{P_T(\beta):T},
]

and

[
\epsilon_{\rm mca}!\left(\operatorname{RS}[F,D,k],\frac jn\right)
\ge
\frac{#{P_T(\beta):T}}{|F|}.
]

Moreover, if exactly (m) distinct supports have one common value (P_T(\beta)), then the corresponding received line point has at least (m) distinct codewords at Hamming distance exactly (j). Thus locator-value fiber multiplicity transfers to a classical list-size lower bound.

### Cycle84 instantiation

Take

[
F=\mathbb F_{17}[X]/(X^{16}+X^8+3),\qquad
\eta=6X^9,\qquad
\beta=X+2,
]

and

[
D=\langle\eta\rangle,\qquad |D|=256.
]

For a state ((i,a)), write

[
B_{i,a}=a+E_i\pmod {16},
]

and

[
Y_{i,a}=
{y\in\langle\eta^8\rangle:y^2\in{3^b:b\in B_{i,a}}}.
]

For a seven-tuple (\tau=((i_t,a_t))_{t=1}^7), define

[
T_\tau={1}\cup\bigcup_{t=1}^7\eta^tY_{i_t,a_t}.
]

Then:

[
|T_\tau|=1+7\cdot16=113.
]

The cosets (\eta^t\langle\eta^8\rangle), (t=0,\ldots,7), are disjoint, and the 48 sets (B_{i,a}) are distinct, so distinct tuples give distinct co-supports.

Define the locator

[
P_\tau(X)=\prod_{x\in T_\tau}(X-x).
]

The exact theorem is:

[
\boxed{
\begin{gathered}
C=\operatorname{RS}[F,D,137],\
\delta=\frac{113}{256},\qquad |S_\tau|=143,\
\operatorname{LD}*{\rm sw}(C,143)
\ge 52{,}747{,}567{,}092,\
\epsilon*{\rm mca}(C,113/256)
\ge \frac{52{,}747{,}567{,}092}{17^{16}}.
\end{gathered}
}
]

There are also at least 12 distinct line points whose radius-(113) list contains at least two distinct codewords. Hence

[
\operatorname{Lst}(C,113/256)\ge2.
]

The packet does not prove list size (3), nor that those lists have exactly size (2).

PROOF / DISPROOF / ROUTE CUT:

### PROOF 1: exact meaning of the color condition

The packet color satisfies

[
c(i,a)=\sum_{b\in B_{i,a}}b\pmod {16}.
]

Since (\eta^{16}=3), the product of the 16 points in block
(\eta^tY_{i,a}) is

[
\prod_{x\in\eta^tY_{i,a}}x
=\eta^{16t}\prod_{y\in Y_{i,a}}y
=3^{t+\sum_{b\in B_{i,a}}b}.
]

Therefore

[
\prod_{x\in T_\tau}x
=3^{1+\cdots+7+\sum_t c(i_t,a_t)}
=3^{28+\sum_t c(i_t,a_t)}.
]

On the Cycle84 shell (\sum_t c(i_t,a_t)=4\bmod16),

[
\prod_{x\in T_\tau}x=3^{32}=1.
]

Since (|T_\tau|=113) is odd,

[
P_\tau(0)=(-1)^{113}\prod_{x\in T_\tau}x=-1.
]

Thus the color equation is exactly a constant-product/constant-term condition.

**DISPROOF of claim 2 as phrased:** it is not “exactly the required support/witness condition” in the attached support-wise MCA definition. That definition only requires:

[
|S|\ge143,\qquad
(f+zg)|_S\in C|_S,
]

and failure of simultaneous code explanations for (f) and (g) on (S). It contains no color or support-product condition. The color shell is required only because the Cycle84 finite census was performed on that subfamily.

### PROOF 2: common six-jet

For each block,

[
R_{t,i,a}(X)
=\prod_{y\in Y_{i,a}}(X-\eta^ty)
=\prod_{b\in B_{i,a}}(X^2-\eta^{2t}3^b).
]

The three degree-eight polynomials encoded by `P_COEFFS` have zero coefficients in degrees (7) and (6). Scaling their roots by (3^a) and substituting (X^2/\eta^{2t}) preserves these zeros. Hence every block locator has the form

[
R_{t,i,a}(X)=X^{16}+O(X^{10}).
]

It follows that

[
\prod_{t=1}^7R_{t,i_t,a_t}(X)
=X^{112}+O(X^{106}),
]

and therefore

[
\boxed{
P_\tau(X)
=X^{113}-X^{112}+O(X^{107}).
}
]

Thus all packet locators have the common top six coefficients

[
[X^{113},X^{112},X^{111},X^{110},X^{109},X^{108}]
=================================================

[1,-1,0,0,0,0].
]

This property holds for all seven-tuples; the color condition is not needed for it.

### PROOF 3: exact product-to-locator identity

The Cycle84 slot definition gives

[
u_t(i,a)
========

3^{-t}
\prod_{x\in\eta^tY_{i,a}}(\beta-x).
]

Therefore

[
\begin{aligned}
P_\tau(\beta)
&= (\beta-1)
\prod_{t=1}^7
\prod_{x\in\eta^tY_{i_t,a_t}}(\beta-x)\
&= (\beta-1)3^{1+\cdots+7}
\prod_{t=1}^7u_t(i_t,a_t)\
&= (\beta-1)3^{28}\Phi(\tau).
\end{aligned}
]

In (\mathbb F_{17}),

[
3^{28}=4,
]

so

[
\boxed{
P_\tau(\beta)=\kappa\Phi(\tau),
\qquad
\kappa=4(\beta-1)=4(X+1)=4+4X\ne0.
}
]

All factors are nonzero because (\beta\notin D).

### PROOF 4: construction of the common syndrome line

Let

[
H_D(X)=\prod_{x\in D}(X-x)=X^{256}-1.
]

For (y\in F^D), define its (119)-coordinate syndrome by

[
\operatorname{Syn}(y)_m
=======================

\sum_{x\in D}\frac{x^my_x}{H_D'(x)},
\qquad 0\le m\le118.
]

Its kernel is (C=\operatorname{RS}[F,D,137]).

For each (\tau), define an error word supported exactly on (T_\tau):

[
e_\tau(x)=
\begin{cases}
\dfrac{H_D'(x)}
{(x-\beta)P_\tau'(x)},&x\in T_\tau,[6pt]
0,&x\notin T_\tau.
\end{cases}
]

The residue theorem gives

[
\operatorname{Syn}(e_\tau)_m
============================

A_m-\frac{\beta^m}{P_\tau(\beta)},
]

where the common six-jet gives the fixed vector

[
A_m=
\begin{cases}
0,&0\le m\le112,[2pt]
1+\beta+\cdots+\beta^\ell,
&m=113+\ell,\quad 0\le\ell\le5.
\end{cases}
]

Let

[
B=(1,\beta,\ldots,\beta^{118}).
]

Choose (f) with (\operatorname{Syn}(f)=A), and set

[
g(x)=\frac{H_D(\beta)}{\beta-x}.
]

Lagrange interpolation gives

[
\operatorname{Syn}(g)=B.
]

For

[
z_\tau=-P_\tau(\beta)^{-1},
]

we consequently have

[
\operatorname{Syn}(f+z_\tau g)
==============================

# A-\frac{B}{P_\tau(\beta)}

\operatorname{Syn}(e_\tau).
]

Hence

[
c_\tau:=f+z_\tau g-e_\tau\in C.
]

On

[
S_\tau=D\setminus T_\tau,
]

the error vanishes, so

[
(f+z_\tau g)|*{S*\tau}=c_\tau|*{S*\tau},
\qquad |S_\tau|=143.
]

Because every coordinate of (e_\tau) on (T_\tau) is nonzero, this constructed codeword is at Hamming distance exactly (113).

### PROOF 5: noncontainment and transversality

Suppose (g|*{S*\tau}) were explained by a codeword (c_g\in C). Then

[
h=g-c_g
]

would be supported on (T_\tau), with

[
\operatorname{Syn}(h)=\operatorname{Syn}(g)=B.
]

Every syndrome of a word supported on (T_\tau) lies in

[
\operatorname{span}{v(x):x\in T_\tau},
\qquad
v(x)=(1,x,\ldots,x^{118}).
]

But

[
B=v(\beta).
]

The (114) columns

[
{v(x):x\in T_\tau}\cup{v(\beta)}
]

are Vandermonde columns at distinct field elements, and (114\le119). They are linearly independent. Therefore

[
v(\beta)\notin\operatorname{span}{v(x):x\in T_\tau},
]

a contradiction.

Thus (g) is not code-explainable on (S_\tau). In particular, no pair of codewords can simultaneously explain (f) and (g) there. Every packet incidence is support-wise noncontained and non-tangent.

### PROOF 6: exact slope fibers

Combining the locator evaluation with the syndrome slope,

[
\boxed{
z_\tau
======

-\kappa^{-1}\Phi(\tau)^{-1}.
}
]

The map

[
v\longmapsto-\kappa^{-1}v^{-1}
]

is a bijection of (F^\times). Therefore the Cycle84 product fibers and packet slope fibers are exactly identical as set partitions.

The 12 double fibers produce 12 slopes with two distinct supports. Their error words are distinct because their supports are distinct and every active error coordinate is nonzero. Therefore their associated codewords are also distinct.

“No product fiber of size at least three” proves only that there are no packet triples. It does not exclude codewords or supports outside the Cycle84 packet from witnessing one of the same slopes.

### PROOF 7: exact (t=1) residue-line form

The same construction is a degree-one residue-line datum in the attached `def:residue` sense. Set

[
E(X)=X-\beta,\qquad
B_0=H_D(\beta),\qquad
w(x)=E(x)f(x).
]

Then

[
g=-\frac{B_0}{E}.
]

If (C_\tau(X)) is the degree-(<137) polynomial representing (c_\tau), define

[
Q_\tau(X)=E(X)C_\tau(X)+z_\tau B_0.
]

Then

[
\deg Q_\tau<138,\qquad
Q_\tau\equiv z_\tau B_0\pmod E,
]

and on (S_\tau),

[
Q_\tau=Ef=w.
]

The Vandermonde argument proves noncontainment. Thus this is an exact (t=1) residue-line packing with at least (52{,}747{,}567{,}092) slopes.

### ROUTE_CUT: direct one-copy official-rate repair

At the explicit one-copy parameters,

[
j=113,\qquad n=256.
]

The common six-jet forces

[
r=j+6=119,\qquad k=256-119=137.
]

A rate-(1/2) row with (k=128) would have (r=128) and would require

[
\sigma=r-j=15
]

common leading locator coefficients, not six.

The color shell does not supply the missing coefficients. Indeed, the following two shell tuples both have total color (4):

[
\begin{aligned}
\tau_A={}&((1,8),(3,4),(1,4),(2,0),(1,7),(2,15),(2,0)),\
\tau_B={}&((2,12),(2,14),(3,9),(2,8),(1,13),(1,6),(1,0)).
\end{aligned}
]

But their (X^{107}) locator coefficients—the first coefficient beyond the common six-jet—are respectively

[
13+14X^2+14X^4+5X^6+9X^8+7X^{10}+16X^{12}+3X^{14},
]

and

[
4+10X^2+11X^4+11X^6+8X^8+5X^{10}+16X^{12}+10X^{14}.
]

They differ. Thus even a common seventh coefficient fails on the color shell.

This does not prove that every conceivable rate-repair theorem is impossible. It proves that the direct fixed-jet syndrome construction cannot simply replace (k=137) by (k=128).

FIELD AND PARAMETER LEDGER:

| Object           |                                      Exact value | Use                                                    |           |                                |
| ---------------- | -----------------------------------------------: | ------------------------------------------------------ | --------- | ------------------------------ |
| Field (F)        |                            (\mathbb F_{17^{16}}) | Code alphabet and line field                           |           |                                |
| (q_{\rm gen})    |                                        (17^{16}) | The line data contain (\beta=X+2), which generates (F) |           |                                |
| (q_{\rm code})   |                                        (17^{16}) | RS code alphabet                                       |           |                                |
| (q_{\rm line})   | (17^{16}=48{,}661{,}191{,}875{,}666{,}868{,}481) | Sole denominator in (\epsilon_{\rm mca})               |           |                                |
| (q_{\rm chal})   |                             **Not instantiated** | Cannot be substituted without a protocol transfer      |           |                                |
| Domain           |                        (D=\langle\eta\rangle), ( | D                                                      | =256=2^8) | Smooth multiplicative subgroup |
| Code             |                                   ([256,137]) RS | Standard RS; no GRS conversion is needed               |           |                                |
| Redundancy       |                                          (r=119) | Syndrome length                                        |           |                                |
| Co-support       |                                          (j=113) | Error weight                                           |           |                                |
| Slack            |                                       (\sigma=6) | Common jet length                                      |           |                                |
| Agreement        |                                   (143=k+\sigma) | Witness support size                                   |           |                                |
| Radius           |                                 (\delta=113/256) | Exact relative radius                                  |           |                                |
| Rate             |                                   (\rho=137/256) | Not in ({1/2,1/4,1/8,1/16})                            |           |                                |
| Packet numerator |                         (N=52{,}747{,}567{,}092) | Distinct certified slopes                              |           |                                |

The finite MCA error lower bound is

[
\frac{N}{q_{\rm line}}
======================

1.0839760609804655\times10^{-9}
\approx 2^{-29.781}.
]

Therefore, as a bare finite inequality,

[
\epsilon_{\rm mca}(C,113/256)>2^{-128}.
]

Equivalently,

[
2^{128}N>q_{\rm line}.
]

However,

[
\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor=0.
]

Thus the (2^{-128}) integer comparison is degenerate at this field size: one bad slope would already clear it. This is not an official frontier claim. The internal comparison (N>2^{32}) is not the MCA denominator calculation.

SELF-AUDIT:

1. **What exact implication did I prove, and what did I not prove?**
   I proved

   [
   \text{Cycle84 shell and product certificate}
   \Longrightarrow
   \text{one explicit finite ([256,137]) RS support-wise MCA line}
   ]

   with at least (52{,}747{,}567{,}092) distinct noncontained slopes, exact reciprocal-product slope map, and packet fiber maximum two.

   I did not prove that the global bad-slope set of this line has exactly that size, that global slope fibers have maximum two, that classical list size is large beyond (2), that the two-copy ([464,232]) construction is valid, or that this row is an official Proximity Prize counterpacket.

2. **Claim level.**
   This is **paper-facing finite RS-MCA/support-wise line-decoding**. It is stronger than a finite product/model certificate because it constructs the RS code, line, witnesses, and noncontainment proof. It is not official-prize terminal because the rate, challenge/source contract, and official-family admission are unresolved.

3. **First possible failure line.**
   In the one-copy mathematical transfer, the first dangerous line is the common fixed-jet assertion. It passes exactly for six coefficients.

   In the prize reduction, the first unsupported line is

   [
   [256,137]\text{ finite extension-field RS row}
   \Longrightarrow
   \text{official prize-admissible row}.
   ]

   A direct rate-(1/2) port already fails the fixed-jet hypothesis: it requires a 15-jet, while the seventh coefficient varies.

4. **(q)-ledger and (2^{-128}).**
   Here

   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}.
   ]

   Only (q_{\rm line}) divides the bad-slope numerator. (q_{\rm code}) is not a second denominator. (q_{\rm gen}) supplies no extra entropy credit. (q_{\rm chal}) is unused because no protocol conversion is present. The bare (2^{-128}) inequality holds, but only with the trivial integer threshold zero.

5. **Potential numerator losses.**

   * **Reciprocal/scalar normalization:** no loss; (v\mapsto-\kappa^{-1}v^{-1}) is bijective.
   * **Common affine reparameterization:** no loss for (z\mapsto a+bz), (b\ne0).
   * **Support-dependent normalization:** invalid and not used.
   * **GRS scaling:** no loss if the same nonzero diagonal map is applied to the code, line, and witnesses. The theorem already uses standard RS.
   * **Contained incidences:** ruled out by the (114)-column Vandermonde argument.
   * **Tangencies:** ruled out because (g|*{S*\tau}\notin C|*{S*\tau}).
   * **Same-slope collisions:** exactly the Cycle84 product fibers; 12 doubles and no packet triples.
   * **Endpoint loss:** none in the attached affine definition; every (z_\tau\in F^\times).
   * **Color normalization:** already paid in the Cycle84 count; no second color quotient is permitted.
   * **Quotient/periodic structure:** does not reduce the numerator under `def:mca`, which counts actual slopes. An external official source contract might charge or exclude such slopes; no such retained-slope contract is supplied.
   * **Outside-packet witnesses:** may increase list multiplicity or add bad slopes, but cannot reduce the certified distinct packet slope set.

6. **What converts this into a fuller proof or counterpacket?**
   The finite theorem itself can be machine-packaged by:

   [
   \boxed{\texttt{V-CYCLE115-C84-FIXED6JET-RECIPROCAL-SLOPE-BRIDGE}}
   ]

   checking only the 336 block states—not rerunning the Cycle84 census:

   * (\eta) has order (256) and (\beta\notin D);
   * all block locators are (X^{16}+O(X^{10}));
   * tuple-to-support injectivity;
   * the color/product identity;
   * (P_\tau(\beta)=4(\beta-1)\Phi(\tau));
   * the common syndrome vector (A);
   * the Vandermonde noncontainment rank.

   Official promotion requires the separate fail-closed contract

   [
   \boxed{\texttt{L-CYCLE115-OFFICIAL-FAMILY-ADMISSION-OR-FIXEDJET-PORT}}
   ]

   specifying:

   * admitted fields and extension fields;
   * admitted rates;
   * subgroup/coset domain requirements;
   * (q_{\rm line})-to-(q_{\rm chal}) relation;
   * endpoint policy;
   * quotient/periodic and affine-color charges;
   * the final retained-slope map.

NEXT EXACT STEP:

Build `V-CYCLE115-C84-FIXED6JET-RECIPROCAL-SLOPE-BRIDGE` as a compact independent bridge certificate, then request an authority-pinned ruling on `L-CYCLE115-OFFICIAL-FAMILY-ADMISSION-OR-FIXEDJET-PORT`.

If the one-copy row is rejected, the next mathematical theorem must construct an official-rate power-of-two subgroup family with common

[
\sigma=n-k-j
]

top locator coefficients and a retained reciprocal-evaluation image exceeding

[
\left\lfloor q_{\rm line}/2^{128}\right\rfloor.
]

The existing Cycle84 one-copy family cannot supply the (n=256,k=128) case by direct normalization: it needs a common 15-jet and already fails at the seventh coefficient.
