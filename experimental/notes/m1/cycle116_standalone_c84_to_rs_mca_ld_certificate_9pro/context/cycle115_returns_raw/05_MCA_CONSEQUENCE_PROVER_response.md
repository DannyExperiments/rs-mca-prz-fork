LABEL: **PROOF**

EXECUTIVE VERDICT:

Cycle84 admits a complete, explicit transfer to a genuine finite Reed–Solomon list-decoding and support-wise line-MCA theorem.

For
[
\mathbb F_0=\mathbb F_{17}[\theta]/(\theta^{16}+\theta^8+3),\qquad
D=\langle \eta\rangle,\quad \eta=6\theta^9,\quad |D|=256,
]
and
[
C=\operatorname{RS}[\mathbb F_0,D,137],
]
there is:

[
\operatorname{Lst}!\left(C,\frac{113}{256}\right)
\ge 52{,}747{,}567{,}104,
]

and one explicit affine line (u_z=f+zg) with at least

[
52{,}747{,}567{,}092
]

distinct support-wise MCA-bad slopes, each witnessed on exactly (143=137+6) coordinates. Consequently,

[
\boxed{
\epsilon_{\rm mca}!\left(C,\frac{113}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}
{48{,}661{,}191{,}875{,}666{,}868{,}481}
}
]

and equivalently

[
\operatorname{LD}_{\rm sw}(C,143)
\ge 52{,}747{,}567{,}092.
]

Numerically, this MCA error is approximately (1.0839761\times10^{-9}=2^{-29.781\ldots}).

This is a paper-facing finite RS-MCA/list/line-decoding theorem, not an official Proximity Prize counterpacket. The one-copy row has the nonofficial rate (137/256). The Cycle88/Cycle89 ([464,232]) extension-field row satisfies the MCA implication conditionally, but the packet does not expose the actual support-wise residue witnesses needed to verify every counted slope independently. Moreover, (464=16\cdot29) is not an admissible power-of-two smooth-domain length.

---

EXACT THEOREM OR OBSTRUCTION:

### BANKABLE_LEMMA: Fixed-jet locator-to-list/MCA transfer

Let (\mathbb F) be a finite field, let (D\subseteq\mathbb F) have size (n), and let
[
V_D(Y)=\prod_{x\in D}(Y-x).
]
Fix (k,\sigma\ge1), put
[
j=n-k-\sigma,
]
and let (\mathcal J) be a family of distinct (j)-subsets (J\subseteq D). Define
[
P_J(Y)=\prod_{x\in J}(Y-x),\qquad
L_J(Y)=\frac{V_D(Y)}{P_J(Y)}
=\prod_{x\in D\setminus J}(Y-x).
]

Assume that there are two distinct points
[
\alpha,\beta\in\mathbb F\setminus D
]
such that:

1. **Common top (\sigma)-jet:** the coefficients of (L_J) in degrees
   [
   k+1,k+2,\ldots,k+\sigma
   ]
   are independent of (J).

2. **Common basepoint value:**
   [
   L_J(\alpha)=\lambda
   ]
   is independent of (J).

Choose a polynomial (A_*(Y)) carrying the common degree-(>k) coefficients and satisfying (A_*(\alpha)=\lambda). Then
[
\deg(L_J-A_*)\le k,\qquad
Y-\alpha\mid L_J-A_*.
]
Define
[
C_J(Y)=\frac{L_J(Y)-A_*(Y)}{Y-\alpha},
\qquad
r(x)=-\frac{A_*(x)}{x-\alpha}\quad(x\in D).
]

Then:

1. (\deg C_J<k), so (C_J) is an RS codeword polynomial.

2. On
   [
   S_J=D\setminus J,\qquad |S_J|=k+\sigma,
   ]
   one has
   [
   C_J(x)=r(x).
   ]

3. Distinct (J)'s give distinct RS codewords, and hence
   [
   \operatorname{Lst}!\left(\operatorname{RS}[\mathbb F,D,k],
   1-\frac{k+\sigma}{n}\right)
   \ge |\mathcal J|.
   ]

4. Define the external-evaluation slope
   [
   z_J=C_J(\beta).
   ]
   Set
   [
   f(x)=\frac{r(x)}{x-\beta},
   \qquad
   g(x)=-\frac1{x-\beta}.
   ]
   Then (z_J) is support-wise MCA-bad for (f+zg), witnessed by (S_J).

5. The slope is reciprocal-affine in the complement-locator value:
   [
   z_J=
   \frac{V_D(\beta)}
   {(\beta-\alpha)P_J(\beta)}
   -\frac{A_*(\beta)}{\beta-\alpha}.
   ]
   Because (\beta\notin D) and (\beta\ne\alpha), the coefficient of
   (1/P_J(\beta)) is nonzero. Therefore
   [
   |{z_J:J\in\mathcal J}|
   ======================

   |{P_J(\beta):J\in\mathcal J}|.
   ]

Consequently,
[
\boxed{
\epsilon_{\rm mca}
\left(\operatorname{RS}[\mathbb F,D,k],
1-\frac{k+\sigma}{n}\right)
\ge
\frac{|{P_J(\beta):J\in\mathcal J}|}{|\mathbb F|}
}.
]

If only a maximum-fiber bound (m_{\max}) is known, this gives the weaker but automatic estimate
[
\epsilon_{\rm mca}\ge \frac{|\mathcal J|}{m_{\max}|\mathbb F|}.
]
Cycle84 provides the sharper exact image size (\operatorname{Occ}(\beta)).

### Proof of the MCA clause

For (z_J=C_J(\beta)), the polynomial
[
R_J(Y)=\frac{C_J(Y)-z_J}{Y-\beta}
]
has degree (<k). On (S_J),
[
R_J(x)
=\frac{r(x)-z_J}{x-\beta}
=f(x)+z_Jg(x).
]
Thus (u_{z_J}) agrees with an RS codeword on (S_J).

For noncontainment, suppose a degree-(<k) polynomial (G) explained (g) on (S_J). Then
[
(Y-\beta)G(Y)+1
]
would have degree at most (k) and at least
[
|S_J|=k+\sigma>k
]
distinct roots. It would therefore be identically zero. Evaluating at (Y=\beta) gives (1=0), impossible. Hence (g|*{S_J}\notin C|*{S_J}), so no pair of codewords can simultaneously explain (f|*{S_J}) and (g|*{S_J}).

Thus every counted slope satisfies both conditions of `def:mca`.

Importantly, (|S|>k) does **not** make noncontainment automatic for an arbitrary line. It makes the root-counting argument work here because the chosen direction is the special rational word
[
g=-\frac1{Y-\beta}.
]

---

PROOF / DISPROOF / ROUTE CUT:

### PROOF: Cycle84 satisfies the transfer theorem

Write
[
\beta=\theta+2.
]
The packet verifies (\beta^{256}\ne1), so (\beta\notin D).

For a Cycle84 state ((i,a)), let
[
B_{i,a}=a+E_i\pmod {16}.
]
The 16 roots in slot (t) form eight opposite pairs, and their locator can be written
[
F_{t,i,a}(Y)
============

\prod_{b\in B_{i,a}}
\left(Y^2-\eta^{2t}3^b\right).
]

The packet’s three degree-eight polynomials
[
\prod_{e\in E_i}(Z-3^e)
]
have zero (Z^7)- and (Z^6)-coefficients. Therefore every slot locator has the exact shape
[
F_{t,i,a}(Y)=Y^{16}+{\text{terms of degree at most }10}.
]

For a seven-tuple (T), define the complement set
[
J_T={1}\cup
\bigcup_{t=1}^{7}
{\text{the 16 roots selected in slot }t}.
]
The seven slot cosets occupy different residue classes modulo (8), so they are disjoint. Hence
[
|J_T|=1+7\cdot16=113,
\qquad
|S_T|=|D\setminus J_T|=143.
]

The complement locator has the form
[
P_T(Y)
=(Y-1)\prod_{t=1}^{7}F_{t,i_t,a_t}(Y)
=Y^{113}-Y^{112}
+{\text{terms of degree at most }107}.
]

Since (V_D(Y)=Y^{256}-1), the support locator
[
L_T(Y)=\frac{Y^{256}-1}{P_T(Y)}
]
therefore has the fixed top-six jet
[
L_T(Y)
======

Y^{143}+Y^{142}+Y^{141}+Y^{140}+Y^{139}+Y^{138}
+{\text{terms of degree at most }137}.
]

This is precisely the Cycle85 “fixed (6[\infty])-jet” condition.

### What the color shell actually does

The support size (143) does **not** come from the color shell. It comes from the rigid (1+7\cdot16) complement construction.

The fixed top-six jet also does **not** come from the color shell. It comes from the two vanishing high coefficients of each degree-eight state polynomial.

The color shell supplies the common finite basepoint normalization. For a slot,
[
\prod_{\text{slot roots }x}x=3^{t+\operatorname{color}(i,a)}.
]
Thus, on the shell
[
\sum_{t=1}^{7}\operatorname{color}(i_t,a_t)\equiv4\pmod{16},
]
one has
[
\prod_{x\in J_T}x
=================

# 3^{1+\cdots+7+4}

# 3^{32}

1.

]
Since (|J_T|=113) is odd,
[
P_T(0)=-1.
]
Also (V_D(0)=-1), so
[
L_T(0)=1
]
for every shell tuple.

Therefore the transfer theorem applies with
[
\alpha=0
]
and
[
A_*(Y)
======

Y^{143}+Y^{142}+Y^{141}+Y^{140}+Y^{139}+Y^{138}+1.
]

Define
[
C_T(Y)=\frac{L_T(Y)-A_*(Y)}{Y}.
]
Then
[
\deg C_T\le136<137.
]

The received word
[
r(x)=-\frac{A_*(x)}x
]
is well-defined because (D\subseteq\mathbb F_0^\times), and
[
C_T(x)=r(x)
\quad\text{for every }x\in S_T.
]

The 48 possible sets in each slot are distinct, and the seven slot cosets are disjoint. Hence different Cycle84 tuples give different (J_T), different (L_T), and different (C_T). Thus
[
\boxed{
\operatorname{Lst}
\left(\operatorname{RS}[\mathbb F_0,D,137],
\frac{113}{256}\right)
\ge 52{,}747{,}567{,}104
}.
]

### Exact product-to-slope relation

Cycle84’s slot factorization gives
[
P_T(\beta)
==========

(\beta-1)3^{28}\Phi(T).
]
The multiplier is fixed and nonzero, so the product fibers and the (P_T(\beta))-fibers are identical.

Set
[
z_T=C_T(\beta).
]
Then
[
z_T
===

\frac{\beta^{256}-1}{\beta P_T(\beta)}
-\frac{A_*(\beta)}{\beta}.
]
Thus
[
z_T=a+\frac b{\Phi(T)}
\qquad(b\ne0),
]
after absorbing the common factor ((\beta-1)3^{28}). This is the reciprocal-affine correction identified in Cycle85.

Hence there is no additional affine-normalization loss:
[
|{z_T}|
=======

# |{\Phi(T)}|

52{,}747{,}567{,}092.
]

The 12 double fibers are exactly the already-paid same-slope collisions. No fibers of size at least three exist.

### Explicit residue-line datum

The preceding line is exactly the (t=1) residue datum
[
E(Y)=Y-\beta,\qquad
B(Y)=1,\qquad
w=r.
]

For a representative tuple (T) of each distinct slope, take
[
Q_{z_T}=C_T.
]
Then

[
\deg Q_{z_T}<137+1,
]
[
Q_{z_T}\equiv z_T\pmod{Y-\beta},
]
and
[
Q_{z_T}=w\quad\text{on }S_T.
]

The noncontainment argument above proves that this is a noncontained witness in the exact sense of `def:residue`. Applying the ((\ge)) direction of `thm:normalform` gives the same line
[
f=\frac wE,\qquad g=-\frac BE.
]

Therefore this is simultaneously:

* a finite RS list-decoding lower bound;
* a support-wise line-decoding lower bound;
* a support-wise line-MCA lower bound under `def:mca`;
* a lower bound for ordinary close-point line decoding, since every bad slope is also a close line point.

It is not a CA theorem under any different, non-support-wise CA predicate, and no protocol/source conversion is being asserted.

### BANKABLE_LEMMA / CONDITIONAL: Cycle88–Cycle89

The logical Cycle89 implication is correct:

If the ([464,232]) construction supplies, for every counted slope (z),

[
|S_z|=238,\qquad
\deg Q_z<233,\qquad
Q_z\equiv zB\pmod E,\qquad
Q_z=w\text{ on }S_z,
]
with (\deg E=1), (E) nonzero on the domain, and the witness noncontained, then `thm:normalform(≥)` proves that every such (z) is support-wise MCA-bad at
[
\delta=1-\frac{238}{464}
=\frac{226}{464}
=\frac{113}{232}.
]

Under those antecedents,
[
\epsilon_{\rm mca}
\ge
\frac{1{,}391{,}152{,}917{,}379{,}006{,}070{,}784}{17^{48}}

> 2^{-128}.
> ]

However, the compact packet contains audits of the Cycle87 residue/support package, not the actual domain, (E,B,w,Q_z,S_z) witness objects or a checker exposing them. Therefore I prove the implication but do not independently certify that every Cycle87 counted projective key satisfies its antecedent.

The first unproved line is:

> For every retained Cycle87 slope key, there exists a (238)-point support and a degree-(<233) polynomial satisfying the displayed residue congruence, support agreement, and noncontainment.

### ROUTE_CUT: official prize upgrade

The unconditional one-copy theorem is not an official prize counterpacket:

* (D) has the correct power-of-two size (256), but
  [
  \rho=\frac{137}{256}
  ]
  is not one of the official rates (1/2,1/4,1/8,1/16).

* The one-copy line field is only (17^{16}<2^{128}). Thus
  [
  \left\lfloor \frac{17^{16}}{2^{128}}\right\rfloor=0.
  ]
  Any nonzero bad-slope numerator already violates a literal (2^{-128}) target, so this field cannot supply a meaningful 128-bit frontier row.

The Cycle88/Cycle89 candidate repairs the rate and field size but has
[
n=464=2^4\cdot29.
]
Cycle90 correctly cuts any literal padding, shortening, subgroup inclusion, or quotient-pullback port of that row into a pure power-of-two multiplicative subgroup. A new smooth-domain construction is required.

---

FIELD AND PARAMETER LEDGER:

| Object                                | Cycle84/Cycle85 theorem |                                  Cycle88/Cycle89 candidate |
| ------------------------------------- | ----------------------: | ---------------------------------------------------------: |
| Field                                 |   (\mathbb F_{17^{16}}) |                                      (\mathbb F_{17^{48}}) |
| (n)                                   |                   (256) |                                                      (464) |
| (k)                                   |                   (137) |                                                      (232) |
| rate                                  |               (137/256) |                                                      (1/2) |
| reserve (\sigma)                      |                     (6) |                                                        (6) |
| complement (j=n-k-\sigma)             |                   (113) |                                                      (226) |
| support size                          |                   (143) |                                                      (238) |
| radius                                |               (113/256) |                                          (226/464=113/232) |
| residue degree (t)                    |                     (1) |                                                        (1) |
| bad-slope numerator                   |  (52{,}747{,}567{,}092) | (1{,}391{,}152{,}917{,}379{,}006{,}070{,}784), conditional |
| (q_{\rm code})                        |               (17^{16}) |                                     (17^{48}), conditional |
| (q_{\rm line})                        |               (17^{16}) |                                     (17^{48}), conditional |
| (q_{\rm gen})                         |               (17^{16}) |                                     (17^{48}), conditional |
| (q_{\rm chal})                        |                not used |                                not used by the MCA theorem |
| (\lfloor q_{\rm line}/2^{128}\rfloor) |                     (0) |                  (338{,}617{,}018{,}271{,}848{,}945{,}628) |

For the one-copy row,
[
q_{\rm gen}=17^{16}
]
because (D) contains an element of order (256), while
[
\operatorname{ord}_{256}(17)=16.
]
Thus the domain itself generates the full degree-16 extension.

The MCA denominator is (q_{\rm line}), not (q_{\rm gen}) merely because an entropy calculation used (q_{\rm gen}), and not (q_{\rm chal}). In the one-copy theorem the fields happen to coincide.

The pure code theorem makes no verifier-challenge assertion. Assigning
[
q_{\rm chal}=q_{\rm line}
]
requires an additional protocol/source adapter and is not justified by `def:mca` or `thm:normalform`.

For the conditional ([464,232]) row,
[
\frac{1{,}391{,}152{,}917{,}379{,}006{,}070{,}784}{17^{48}}
=2^{-125.961\ldots}>2^{-128},
]
and its numerator exceeds the integer target by
[
1{,}052{,}535{,}899{,}107{,}157{,}125{,}156.
]

---

SELF-AUDIT:

1. **Exact implication proved and not proved**

   Proved:
   [
   \text{Cycle84 structural model + exact occupancy}
   \Longrightarrow
   \text{finite }[256,137]\text{ RS list and support-wise MCA bounds}.
   ]

   More explicitly:
   [
   \operatorname{Lst}(C,113/256)\ge52{,}747{,}567{,}104,
   ]
   [
   \operatorname{LD}*{\rm sw}(C,143)\ge52{,}747{,}567{,}092,
   ]
   [
   \epsilon*{\rm mca}(C,113/256)
   \ge52{,}747{,}567{,}092/17^{16}.
   ]

   Not proved:

   * an official-rate one-copy row;
   * an unconditional independently inspectable Cycle87 ([464,232]) witness package;
   * an embedding of the 464-point row into a power-of-two subgroup;
   * any protocol conversion involving (q_{\rm chal});
   * an asymptotic or full Proximity Prize theorem.

   The four finite numbers (m_{\max},\operatorname{Occ},D), and the double-fiber count alone would not prove MCA. The additional locator/support/fixed-jet/basepoint structure is essential.

2. **Claim level**

   The result is a **paper-facing finite RS-MCA/list/line-decoding theorem**. It is stronger than a finite product-model certificate. It is not official-prize-relevant as a counterpacket because its rate is nonofficial, and the rate-corrected 464 row has the wrong domain length.

3. **First possible failure line**

   In the abstract transfer theorem, the first possible failure is the assertion that the finite objects are actual complement locators (P_J) whose support locators (L_J) have:

   * a common top (\sigma)-jet; and
   * a common value at one external normalization point (\alpha).

   Cycle84 passes both conditions symbolically.

   For Cycle88/Cycle89, the first currently unsupported line is the existence of an explicit residue witness ((Q_z,S_z)) for every counted slope.

   For the official-prize chain, the first failure after the finite ([464,232]) row is smooth-domain admissibility.

4. **Field ledger and (2^{-128})**

   In the unconditional theorem:
   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}.
   ]
   The denominator is (q_{\rm line}). No (q_{\rm chal}) is used.

   The (2^{-128}) integer threshold is zero at (17^{16}), making the comparison literal but non-frontier-informative.

   In the extension candidate, the correct slope denominator is (17^{48}), not (17^{16}). The (17^{48}) threshold arithmetic is correct conditionally.

5. **Possible numerator losses**

   * **Quotient/periodic structure:** cannot remove a direct `def:mca` witness. Any product-value identifications are already reflected in (\operatorname{Occ}(\beta)). It could matter only for an additional official source predicate.
   * **Contained incidences:** impossible in the one-copy construction because (g=-1/(Y-\beta)) has no degree-(<k) explanation on a (143>137)-point support.
   * **Same-slope collisions:** exactly paid by Cycle84 occupancy. There are 12 double fibers and no larger fibers.
   * **Endpoint or tangent losses:** absent; the proof invokes no endpoint deletion or source-line normalization.
   * **Affine color normalization:** no loss because
     [
     z=a+b/P_T(\beta),\quad b\ne0,
     ]
     is injective in (P_T(\beta)).
   * **Color shell:** already applied before the finite census. Its mathematical role in the transfer is to fix (L_T(0)=1), not to create the support size.
   * **Two-copy losses:** the audits claim projective and same-slope losses are paid, but this remains conditional until the retained slope/support witness map is exposed.

6. **What would convert the remaining conditional claim**

   The exact missing artifact is not another occupancy census. It is a support-wise residue-witness contract tying the census keys to `def:mca`.

---

NEXT EXACT STEP:

Create and verify

```text
V-CYCLE115-464-SUPPORTWISE-RESIDUE-WITNESS-CONTRACT
```

with a machine-readable contract containing:

1. the degree-48 field modulus and a canonical encoding of every field element;
2. the 464 evaluation points and any GRS multipliers;
3. the diagonal GRS-to-RS isometry;
4. the fixed residue datum (E,B,w);
5. the exact retained slope-key set;
6. for every retained key—or an algebraic generator proving the statement uniformly—
   [
   z,\quad S_z,\quad Q_z;
   ]
7. checks that
   [
   |S_z|=238,\qquad \deg Q_z<233,
   ]
   [
   E(x)\ne0\quad(x\in D),
   ]
   [
   Q_z\equiv zB\pmod E,
   ]
   [
   Q_z(x)=w(x)\quad(x\in S_z);
   ]
8. a direct noncontainment certificate, either by an explicit root-count argument or a verified Vandermonde/rank certificate;
9. an exact final projection count proving
   [
   |{z}|
   =====

   1{,}391{,}152{,}917{,}379{,}006{,}070{,}784;
   ]
10. the integer check
    [
    2^{128}|{z}|>17^{48};
    ]
11. a field ledger that leaves (q_{\rm chal}) unclaimed unless a protocol adapter is separately supplied.

Passing this checker would convert the Cycle88/Cycle89 statement into an unconditional finite arbitrary-domain RS/GRS MCA proof.

It would still not be an official Proximity Prize counterpacket. That requires a genuinely new theorem or construction on a power-of-two multiplicative subgroup at an official rate, preserving the support-wise residue witnesses and final slope numerator. Cycle90 proves that this cannot be obtained by a literal port of the 464-point domain.
