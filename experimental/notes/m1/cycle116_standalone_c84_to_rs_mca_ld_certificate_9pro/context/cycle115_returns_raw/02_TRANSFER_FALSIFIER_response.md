LABEL: **PROOF**

EXECUTIVE VERDICT:

Cycle84 admits an exact **fixed-jet reciprocal-locator transfer** to Reed–Solomon MCA, support-wise line-decoding, and list-decoding.

It proves three distinct levels of result:

1. A direct smooth-subgroup one-copy row over (\mathbb F_{17^{16}}).
2. A fixed-marker rate repair giving an exact rate-(1/2), length-(256) smooth-subgroup MCA row.
3. An existential two-copy ([464,232]) ordinary RS row over (\mathbb F_{17^{48}}), with
   [
   2{,}782{,}305{,}834{,}758{,}012{,}141{,}568
   ]
   distinct support-wise bad slopes, exceeding the (2^{-128}) numerator threshold by a factor (8.216).

The third row is **not** an official Proximity Prize row: its evaluation domain is a union of two scaled, shortened blocks of size (232), not a power-of-two multiplicative subgroup or coset. The one-copy smooth row is genuine but cannot move the intended (q_{\rm line}=17^{48}) frontier.

Confidence: **high** for the finite RS theorems and route cuts; **unknown** for official-prize admissibility without the missing source contract.

EXACT THEOREM OR OBSTRUCTION:

### PROOF: fixed-jet reciprocal-locator transfer

Let (F) be a finite field, (D\subset F) with (|D|=n), and let (\beta\notin D). For a set (A\subseteq D), write
[
L_A(Y)=\prod_{x\in A}(Y-x).
]

Let (\Omega) index distinct supports (T_\omega\subset D), all of size (j), and put
[
S_\omega=D\setminus T_\omega,\qquad |S_\omega|=k+\sigma,
]
where (\sigma\ge1).

Assume:

[
\tag{J}
[Y^{>k}],L_{S_\omega}(Y)=U(Y)
]
is independent of (\omega); equivalently,
[
Q_\omega(Y):=U(Y)-L_{S_\omega}(Y)
\quad\text{satisfies}\quad
\deg Q_\omega\le k.
]

Assume also that there are (c\in F^\times) and (\Phi:\Omega\to F^\times) such that
[
\tag{E}
L_{T_\omega}(\beta)=c,\Phi(\omega).
]

Then, for
[
C=\operatorname{RS}[F,D,k],\qquad
f(x)=\frac{U(x)}{x-\beta},\qquad
g(x)=-\frac1{x-\beta},
]
define
[
z_\omega=Q_\omega(\beta)
=U(\beta)-\frac{L_D(\beta)}{c,\Phi(\omega)}.
]

The map
[
v\longmapsto U(\beta)-\frac{L_D(\beta)}{cv}
]
is injective on (F^\times). Moreover,
[
R_\omega(Y)=\frac{Q_\omega(Y)-z_\omega}{Y-\beta}
]
has degree (<k), and on (S_\omega),
[
R_\omega=f+z_\omega g.
]

The witness is support-wise noncontained. Indeed, if (G\in F[Y]*{<k}) explained (g) on (S*\omega), then
[
(Y-\beta)G(Y)+1
]
would be a nonzero polynomial of degree at most (k) with (k+\sigma>k) roots.

Therefore, at radius
[
\delta=\frac{j}{n},
]
the packet supplies

[
LD_{\rm sw}(C,k+\sigma)\ge |\Phi(\Omega)|,
]
and hence
[
\epsilon_{\rm mca}(C,\delta)
\ge \frac{|\Phi(\Omega)|}{|F|}.
]

Within the constructed packet, the slope-fiber multiplicities are exactly the (\Phi)-fiber multiplicities.

There is also a list consequence. For
[
C^+=\operatorname{RS}[F,D,k+1],
]
each (Q_\omega) is a codeword agreeing with (U|*D) on (S*\omega). If (\omega\mapsto S_\omega) is injective, then
[
\operatorname{ListSize}_{C^+}(\delta)\ge|\Omega|.
]

This theorem identifies the precise missing hypothesis in any naive transfer: Cycle84 product fibers are insufficient without the common fixed jet (J) and common evaluation scalar (E).

---

### PROOF: Cycle84 satisfies the hypotheses

Put
[
F_0=\mathbb F_{17}[\theta]/(\theta^{16}+\theta^8+3),
\qquad
\eta=6\theta^9,
\qquad
\beta=\theta+2.
]
The packet verifies
[
\operatorname{ord}(\eta)=256,\qquad \eta^{16}=3,\qquad \beta^{256}\ne1.
]
Let
[
D=\langle\eta\rangle,\qquad |D|=256,\qquad H=\langle\eta^8\rangle,\quad |H|=32.
]

For a Cycle84 tuple (\tau=((i_t,a_t))*{t=1}^7), its support is
[
T*\tau={1}\cup\bigcup_{t=1}^7\eta^tA(i_t,a_t),
\qquad |T_\tau|=113.
]

The 48 possible sets (A(i,a)) are distinct, and the seven cosets are disjoint, so (\tau\mapsto T_\tau) is injective.

The three packet polynomials satisfy
[
P_i(Z)=Z^8+O(Z^5);
]
their (Z^7) and (Z^6) coefficients vanish. Consequently every slot locator satisfies
[
\deg!\left(
L_{\eta^tA(i,a)}(Y)-Y^{16}
\right)\le10.
]
Hence
[
\deg!\left(
L_{T_\tau}(Y)-(Y^{113}-Y^{112})
\right)\le107.
]

Since
[
Y^{256}-1=L_{T_\tau}(Y)L_{S_\tau}(Y),
\qquad S_\tau=D\setminus T_\tau,
]
formal division gives
[
L_{S_\tau}(Y)
=============

Y^{143}+Y^{142}+Y^{141}+Y^{140}+Y^{139}+Y^{138}
+R_\tau(Y),
]
with
[
\deg R_\tau\le137.
]

Thus the fixed jet is
[
U_0(Y)=Y^{143}+Y^{142}+Y^{141}+Y^{140}+Y^{139}+Y^{138},
]
with
[
(k,\sigma,j)=(137,6,113).
]

The slot-factorization identities in the packet give
[
L_{T_\tau}(\beta)
=(\beta-1)\prod_{t=1}^7F_{t,i_t,a_t}(\beta)
=4(\beta-1)\Phi(\tau),
]
because (3^{1+\cdots+7}=3^{28}=4) in (\mathbb F_{17}).

Therefore, on the Cycle84 color shell (P_0),

[
LD_{\rm sw}\bigl(\operatorname{RS}[F_0,D,137],143\bigr)
\ge 52{,}747{,}567{,}092,
]
and
[
\epsilon_{\rm mca}
\left(\operatorname{RS}[F_0,D,137],\frac{113}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{16}}.
]

The packet contribution has exactly

[
\begin{aligned}
52{,}747{,}567{,}080&\text{ singleton slope fibers},\
12&\text{ double slope fibers},\
0&\text{ fibers of size at least }3.
\end{aligned}
]

This is a packet-fiber statement, not an upper bound on all possible witnesses of the line.

For list decoding,
[
\operatorname{ListSize}_{\operatorname{RS}[F_0,D,138]}
\left(\frac{113}{256}\right)
\ge
52{,}747{,}567{,}104.
]

---

### BANKABLE_LEMMA: fixed-marker rate repair

Every Cycle84 support (T_\tau) contains only the point (1) from (H). Thus
[
H\setminus{1}\subseteq S_\tau
]
for every (\tau).

Choose
[
M_m={\eta^{8r}:1\le r\le m}\subset H\setminus{1},
\qquad 0\le m\le31.
]
Move these fixed points into every error support:
[
T_{\tau,m}=T_\tau\cup M_m,\qquad
S_{\tau,m}=S_\tau\setminus M_m.
]

Let (A_m=L_{M_m}). Since
[
L_{S_\tau}=A_mL_{S_{\tau,m}}
]
and
[
\deg(L_{S_\tau}-L_{S_{\tau'}})\le137,
]
we have
[
\deg(L_{S_{\tau,m}}-L_{S_{\tau',m}})\le137-m.
]

Thus the fixed six-jet survives with
[
k_m=137-m,\quad
|S_{\tau,m}|=143-m=k_m+6,\quad
|T_{\tau,m}|=113+m.
]

Also
[
L_{T_{\tau,m}}(\beta)
=A_m(\beta),4(\beta-1)\Phi(\tau),
]
so the fixed marker introduces only one common nonzero scalar and causes no slope loss.

Taking (m=9) gives the exact prize rate
[
(n,k,\sigma,j)=(256,128,6,122),
]
and therefore
[
LD_{\rm sw}\bigl(\operatorname{RS}[F_0,D,128],134\bigr)
\ge52{,}747{,}567{,}092,
]
at radius
[
\delta=\frac{122}{256}=\frac{61}{128}.
]

Taking (m=10) makes the list code have exact rate (1/2):
[
\operatorname{ListSize}_{\operatorname{RS}[F_0,D,128]}
\left(\frac{123}{256}\right)
\ge52{,}747{,}567{,}104.
]

So the Cycle85 rate-normalization gap can be closed exactly by fixed markers; padding to a different domain length is unnecessary.

---

### PROOF: existential cubic-separator two-copy transfer

There is also a nontrivial (q_{\rm line}=17^{48}) transfer, but its domain is not prize-admissible.

Let
[
q_0=17^{16},\qquad L=\mathbb F_{q_0^3}=\mathbb F_{17^{48}},
\qquad P=52{,}747{,}567{,}104.
]

Remove a fixed set of 24 universally unused points:
[
M_{24}={\eta^{8r}:1\le r\le24},
\qquad D^-=D\setminus M_{24},
\qquad |D^-|=232.
]
The original (T_\tau) remain subsets of (D^-). Put
[
S_\tau^-=D^-\setminus T_\tau,\qquad |S_\tau^-|=119.
]

The locators (L_{S_\tau^-}) have a common six-jet:
[
\deg(L_{S_\tau^-}-L_{S_{\tau'}^-})\le113.
]

Now consider the (P) distinct monic degree-(113) polynomials
[
L_{T_\tau}(Y),\qquad \tau\in P_0.
]

There exists (y\in L\setminus F_0) such that their projective values are pairwise distinct modulo (F_0^\times):
[
[L_{T_\tau}(y)]\ne[L_{T_{\tau'}}(y)]
\quad\text{in }L^\times/F_0^\times
\quad(\tau\ne\tau').
]

Indeed, for each (\tau\ne\tau') and (c\in F_0^\times),
[
L_{T_\tau}(Y)-cL_{T_{\tau'}}(Y)
]
is a nonzero polynomial of degree at most (113). Hence the total number of excluded elements of (L), including (F_0), is at most
[
q_0+
113(q_0-1)\binom{P}{2},
]
and the exact packet values satisfy
[
q_0+
113(q_0-1)\binom{P}{2}
<q_0^3.
]

Choose such a (y), and put
[
\alpha=\frac{\beta}{y}\notin F_0.
]
Define the length-(464) domain
[
\mathcal D=D^-\cup\alpha D^-.
]
The two blocks are disjoint.

For ((\tau,\upsilon)\in P_0^2), define
[
\mathcal T_{\tau,\upsilon}
=T_\tau\cup\alpha T_\upsilon,
\qquad |\mathcal T_{\tau,\upsilon}|=226,
]
and
[
\mathcal S_{\tau,\upsilon}
=S_\tau^-\cup\alpha S_\upsilon^-,
\qquad |\mathcal S_{\tau,\upsilon}|=238.
]

The combined complement locators have a common six-jet. Indeed,
[
L_{\alpha S_\upsilon^-}(Y)
=\alpha^{119}L_{S_\upsilon^-}(Y/\alpha),
]
and differences in each block have degree at most (113). Therefore differences of products have degree at most
[
113+119=232.
]

Applying the transfer theorem with
[
(n,k,\sigma,j)=(464,232,6,226)
]
gives a single ordinary RS code and a single affine line.

The combined error locator satisfies
[
L_{\mathcal T_{\tau,\upsilon}}(\beta)
=====================================

4(\beta-1)\alpha^{113}
\Phi(\tau)L_{T_\upsilon}(y).
]

Because the projective values (L_{T_\upsilon}(y)) are distinct modulo
(F_0^\times), equality
[
\Phi(\tau)L_{T_\upsilon}(y)
===========================

\Phi(\tau')L_{T_{\upsilon'}}(y)
]
forces
[
\upsilon=\upsilon',
\qquad
\Phi(\tau)=\Phi(\tau').
]

Thus the Cycle84 fiber spectrum is replicated once for every
(\upsilon\in P_0). The number of distinct slopes is exactly

[
\begin{aligned}
N_{464}
&=52{,}747{,}567{,}092
\cdot52{,}747{,}567{,}104\
&=2{,}782{,}305{,}834{,}758{,}012{,}141{,}568.
\end{aligned}
]

Consequently,
[
LD_{\rm sw}
\bigl(\operatorname{RS}[L,\mathcal D,232],238\bigr)
\ge N_{464},
]
and
[
\epsilon_{\rm mca}
\left(\operatorname{RS}[L,\mathcal D,232],
\frac{226}{464}\right)
\ge \frac{N_{464}}{17^{48}}

> 2^{-128}.
> ]

The exact target is
[
\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor
================================================

338{,}617{,}018{,}271{,}848{,}945{,}628,
]
so the margin is
[
2{,}443{,}688{,}816{,}486{,}163{,}195{,}940.
]

The corresponding list row is
[
\operatorname{ListSize}_{\operatorname{RS}[L,\mathcal D,233]}
\left(\frac{226}{464}\right)
\ge P^2
=======

2{,}782{,}305{,}835{,}390{,}982{,}946{,}816.
]

This proof is existential in the separator (y). It does not use or certify the specific Cycle87 element (U).

PROOF / DISPROOF / ROUTE CUT:

### First generic failure line

The false unqualified theorem is:

> A multiplicity bound for the Cycle84 product values automatically gives the same multiplicity bound for RS slopes.

That is false without the fixed-jet and common-scalar hypotheses. In general, the slope could have the form
[
z_\tau=a_\tau+\frac{b_\tau}{\Phi(\tau)}
]
with support-dependent (a_\tau,b_\tau). Such normalizations can collapse arbitrarily many distinct products to one slope.

The minimal repair is exactly:

[
[Y^{>k}]L_{S_\tau}\text{ is common},
\qquad
L_{T_\tau}(\beta)=c\Phi(\tau)
\text{ with one common }c\ne0.
]

Cycle84 passes this repaired theorem.

### Projective two-copy transfer is not implied by (m_{\max}(\beta))

The false theorem is:

> If (P_i(\beta)) have fibers of size at most two, then
> ([P_i(y)]\in L^\times/F^\times) also have bounded fibers.

A general algebraic route cut is immediate. Let (y) have minimal polynomial
(M) over (F), take a monic polynomial (P_0), and choose (R) so that
(M(\beta)R(\beta)\ne0). For distinct (c_i\in F), put
[
P_i=P_0+c_iMR.
]
Then
[
P_i(y)=P_0(y)
]
for every (i), while the values (P_i(\beta)) are distinct.

This is not an official RS counterpacket because it does not impose split-locator/support constraints. It is a decisive route cut to the logical implication. The existential two-copy proof above repairs it by choosing (y) after seeing the entire locator family and proving projective injectivity by root counting.

### One-copy scalar extension to (17^{48}) is impossible as a frontier route

For a code over an extension (L/F_0), if (D,f,g) are (F_0)-valued, every support-wise bad slope lies in (F_0). A coordinate-projection argument shows that any agreement at a slope (z\notin F_0) simultaneously explains (f) and (g) on that support.

Therefore a scalar extension of the one-copy line to (\mathbb F_{17^{48}}) has at most (17^{16}) bad slopes, and
[
\frac{17^{16}}{17^{48}}=17^{-32}<2^{-128}.
]

Independently, the direct packet has only (P) supports, and
[
P<
\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor.
]
No injective normalization can create more slopes than supports. A genuine two-copy or larger support family is necessary.

### The (464)-point row does not transfer to the official smooth family

The two-copy domain has size
[
464=2^4\cdot29,
]
and is explicitly
[
D^-\cup\alpha D^-.
]
It is not a power-of-two multiplicative subgroup or coset.

Moreover,
[
v_2(17^{48}-1)=8,
]
so the largest power-of-two subgroup of (\mathbb F_{17^{48}}^\times) has order (256). There is no order-(512) subgroup into which the construction could be padded.

The first official-prize failure line is therefore:

[
\text{arbitrary-domain }[464,232]\text{ RS row}
;\not\Rightarrow;
\text{smooth power-of-two subgroup/coset row}.
]

### (m_{\max}=2) does not imply a small list

The same support family gives
[
\operatorname{ListSize}*{\operatorname{RS}[F_0,D,138]}
(113/256)\ge P.
]
Thus (m*{\max}=2) controls the fibers of a particular projection from packet incidences to slopes. It is not a global list-size upper bound.

### GRS diagonal equivalence is not the actual failure

For standard support-wise MCA, Hamming list decoding, and close-point line decoding, multiplication by nonzero coordinate multipliers is an exact isometry. It preserves supports, simultaneous explanations, affine slope parameters, and distances.

Thus a genuinely established GRS row can be transferred to its diagonally equivalent RS formulation. The dangerous step is not diagonal equivalence; it is establishing the one-line row, its domain, and its official admissibility.

FIELD AND PARAMETER LEDGER:

Let
[
q_0=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481.
]

**Direct one-copy row**
[
(n,k,\sigma,j,a)=(256,137,6,113,143).
]
[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_0.
]
(q_{\rm chal}) is not used.
[
\left\lfloor q_{\rm line}/2^{128}\right\rfloor=0.
]
Thus the (2^{-128}) comparison is arithmetically true but security-vacuous.

**Fixed-marker exact-rate MCA row**
[
(n,k,\sigma,j,a)=(256,128,6,122,134).
]
The same base-field ledger applies. The domain remains the order-(256) subgroup.

**Scalar extension of the exact-rate row to (\mathbb F_{17^{32}})**
[
q_{\rm gen}=17^{16},\qquad
q_{\rm code}=q_{\rm line}=17^{32},\qquad
q_{\rm chal}\text{ unset}.
]
The same explicit witnesses remain noncontained even against extension-field codewords.
[
\left\lfloor17^{32}/2^{128}\right\rfloor=6,
]
so
[
52{,}747{,}567{,}092/17^{32}>2^{-128}.
]
This is not frontier-moving: the generic tangent floor already supplies at least (122>6) bad slopes at this radius.

**Existential two-copy row**
[
(n,k,\sigma,j,a)=(464,232,6,226,238).
]
Because the domain contains (\eta) and (\alpha),
[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{48}.
]
Again (q_{\rm chal}) is not part of the theorem and is unset.

The native numerator is
[
N_{464}=2{,}782{,}305{,}834{,}758{,}012{,}141{,}568,
]
against threshold
[
338{,}617{,}018{,}271{,}848{,}945{,}628.
]

At no point is (q_{\rm chal}) substituted for (q_{\rm line}). The MCA denominator is always the field over which the affine line parameter ranges. (q_{\rm code}) is not a denominator, and (q_{\rm gen}) is not used to pay the MCA target.

SELF-AUDIT:

1. **Exact implication proved and not proved.**
   Proved: Cycle84 plus the packet’s support-factorization identities implies explicit finite RS support-wise MCA and (LD_{\rm sw}) lower bounds, exact packet slope-fiber spectra, and finite list lower bounds. It also implies an existential arbitrary-domain ([464,232]) row over (17^{48}) crossing (2^{-128}).
   Not proved: an official smooth-domain Proximity Prize theorem, the specific Cycle87 separator certificate, a global line-fiber upper bound, an asymptotic list theorem, or a protocol soundness result.

2. **Claim level.**
   The one-copy and two-copy statements are **paper-facing finite RS-MCA/list/line-decoding proofs** under the packet’s `def:mca` and (LD_{\rm sw}) definitions. The one-copy rate-repaired domain is smooth. The (464)-point row is arbitrary-domain. None is an official-prize frontier proof.

3. **First possible failure line.**
   For a generic Cycle84-to-RS transfer, the first failure is the common fixed-jet/common-scalar step.
   For the audited two-copy route, the first unsupported implication from Cycle84 alone is
   [
   m_{\max}(\beta)\le2
   \Rightarrow
   \mu_{\rm proj}(y)\le2.
   ]
   For the proved existential (464) row, the first official failure is the power-of-two smooth-domain requirement.

4. **Field usage.**
   (q_{\rm line}) alone supplies the MCA denominator. (q_{\rm code}) is the code alphabet. (q_{\rm gen}) is recorded separately. (q_{\rm chal}) is unused. The base, scalar-extension, and two-copy ledgers are not conflated.

5. **Possible numerator losses.**

   * **Same-slope collisions:** exactly the 12 Cycle84 double fibers in the one-copy packet; in the generic two-copy row they are replicated (P) times. No additional packet collision occurs.
   * **Affine normalization:** one fixed injective reciprocal-affine map; no loss.
   * **Contained incidences:** excluded by the root-count proof.
   * **Tangent incidences:** excluded because the direction word is not code-explainable on any witness support.
   * **Quotient/periodic structure:** does not quotient the raw support-wise numerator; the denominator (Y-\beta) is degree one and not a proper quotient pullback.
   * **Endpoint losses:** no endpoint or projective point at infinity is used in the finite affine slope count.
   * **External source charges:** could matter only in a separate protocol/source adapter. No such official retained-event claim is made.

6. **Status of the answer.**
   This is not a PLAN. The finite transfer theorem is proved. What remains is a separate official-family theorem or source contract.

NEXT EXACT STEP:

First, emit a lightweight checker:

```text
V-CYCLE115-FIXED-JET-RECIPROCAL-LOCATOR-TRANSFER
```

It should import the Cycle84 histogram as a black box and verify only:

```text
eta has order 256 and beta is outside D;
the 48 slot supports are distinct;
each slot locator is Y^16 + terms of degree <= 10;
the complement locators have the common six-jet;
L_T(beta) = 4(beta-1) Phi(T);
the m=9 and m=10 marker quotients preserve the six-jet;
the root-count noncontainment checks;
the exact q-ledgers and emitted RS rows.
```

Second, emit the symbolic two-copy checker:

```text
V-CYCLE115-GENERIC-CUBIC-SEPARATOR-464-RS
```

It should verify the exact separator inequality, two-block disjointness, combined common jet, product slope identity, field generation, and the (NP) threshold comparison. It need not recompute Cycle84 or find the specific Cycle87 (U).

The exact official-prize wall is:

```text
L-CYCLE115-SMOOTH256-TWO-COPY-LOCATOR-COMPRESSOR
```

A sufficient statement is an injective family
[
\Psi:P_0^2\longrightarrow\binom{D}{122}
]
on the order-(256) subgroup (D), with

[
[Y^{>128}]L_{D\setminus\Psi(\tau,\upsilon)}
\quad\text{independent of }(\tau,\upsilon),
]
and
[
L_{\Psi(\tau,\upsilon)}(\beta')
===============================

c,\Phi(\tau)L_{T_\upsilon}(y)
]
for one (\beta'\notin D) and one common (c\ne0).

Together with an authority-pinned contract accepting the extension-field line and setting (q_{\rm line}=17^{48}), that lemma would turn the (NP) count into a smooth, rate-(1/2), official-prize-relevant RS-MCA row. Its failure would be the exact counter-route.
