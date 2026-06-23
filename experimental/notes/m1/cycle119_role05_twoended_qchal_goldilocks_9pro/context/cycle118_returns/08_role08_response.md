LABEL:

**PROOF — L-CYCLE118-GOLDILOCKS-PRIME-FIELD-FIXED-JET-COMPILER**

Scope: finite attached-manuscript support-wise MCA / `LD_sw` theorem. Official adoption is conditional on an authority-pinned Goldilocks row/event contract.

Confidence: high for the finite theorem; unknown for official adoption.

EXECUTIVE VERDICT:

Yes. Field descent is unnecessary.

There is a new fixed-jet construction over the prime Goldilocks field

[
q=2^{64}-2^{32}+1
=18{,}446{,}744{,}069{,}414{,}584{,}321
]

and an order-(512) multiplicative subgroup (H\subseteq\mathbb F_q^\times) such that

[
C=\operatorname{RS}[\mathbb F_q,H,256]
]

satisfies

[
\operatorname{LD}_{\rm sw}(C,264)
\ge 73{,}674{,}899{,}375{,}228{,}060.
]

In particular,

[
\operatorname{LD}*{\rm sw}(C,263),
\operatorname{LD}*{\rm sw}(C,262)
\ge 73{,}674{,}899{,}375{,}228{,}060

> 52{,}747{,}567{,}092.
> ]

Thus the Cycle116 numerator survives with enormous slack, and the construction also clears the strict-ball agreement-(263) issue: every witness has agreement (264), hence distance at most (248<250=(125/256)512).

The attached-source field ledger is

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=q,
\qquad q_{\rm chal}=\mathrm{null},
]

and

[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{73{,}674{,}899{,}375{,}228{,}060}
{18{,}446{,}744{,}069{,}414{,}584{,}321}

> \frac1{251}>2^{-128}.
> ]

THEOREM / COUNTERPACKET / ROUTE CUT:

### Prime-field fixed-jet compiler theorem

Put

[
N=52{,}747{,}567{,}092,
\qquad
M=\binom{64}{31}
=1{,}777{,}090{,}076{,}065{,}542{,}336.
]

For every prime (q) satisfying

[
512\mid q-1
]

define

[
L(q)=
\left\lceil
\frac{M^2}
{M+
2\left\lfloor
\dfrac{240\binom M2}{q-512}
\right\rfloor}
\right\rceil .
]

Then there is an order-(512) subgroup (H\le\mathbb F_q^\times) and one affine line over

[
C_q=\operatorname{RS}[\mathbb F_q,H,256]
]

with at least (L(q)) distinct support-wise MCA-bad slopes, each having an agreement support of size (264). Therefore

[
\operatorname{LD}_{\rm sw}(C_q,264)\ge L(q).
]

In particular, every such prime satisfying

[
q\ge
512+
\left\lceil
\frac{240N(M-1)}{M-N}
\right\rceil
============

12{,}659{,}416{,}478{,}349
]

admits the full Cycle116 numerator (N) without loss.

Goldilocks satisfies these hypotheses and gives the stronger numerator displayed above.

There is also a sharp elementary obstruction at the other end:

[
q_{\rm line}<N
\quad\Longrightarrow\quad
\text{no affine line over }\mathbb F_q
\text{ can have }N\text{ distinct slopes}.
]

Thus exact preservation of the Cycle116 numerator is impossible in any smaller challenge/line field, independent of trace, norm, or support construction.

PROOF DETAILS:

### 1. Goldilocks is prime and has an explicit order-(512) element

Write

[
q=(2^{32}-1)2^{32}+1.
]

This is a Proth number. Direct repeated squaring gives

[
7^{(q-1)/2}
===========

7^{9{,}223{,}372{,}034{,}707{,}292{,}160}
\equiv -1\pmod q.
]

For completeness, let (r) be a prime divisor of (q). The displayed congruence implies that the multiplicative order of (7\bmod r) has (2)-adic valuation (32). Hence

[
2^{32}\mid r-1,
\qquad r\ge2^{32}+1.
]

But

[
q<2^{64}.
]

If (q) were composite, it would have a prime divisor at most (\sqrt q<2^{32}), a contradiction. Hence (q) is prime.

Set

[
\theta
======

# 7^{(q-1)/512}

# 7^{36{,}028{,}797{,}010{,}575{,}360}

1{,}803{,}076{,}106{,}186{,}727{,}246
\pmod q.
]

Then

[
\theta^{256}=7^{(q-1)/2}=-1,
\qquad
\theta^{512}=1.
]

Therefore (\theta) has exact order (512). Put

[
H=\langle\theta\rangle.
]

### 2. A (1.777\times10^{18})-member common-jet family

Let

[
G=H^8=\langle\theta^8\rangle,
\qquad |G|=64.
]

The map

[
\pi:H\to G,\qquad x\mapsto x^8
]

is surjective and has kernel of size (8).

For every (31)-subset (A\subseteq G), define the co-support

[
J_A={x\in H:x^8\in A}.
]

Then

[
|J_A|=8|A|=248.
]

Its monic locator is

[
\begin{aligned}
P_A(X)
&=\prod_{x\in J_A}(X-x)\
&=\prod_{c\in A}(X^8-c).
\end{aligned}
]

There are exactly

[
M=\binom{64}{31}
]

such co-supports.

Writing

[
Q_A(Y)=\prod_{c\in A}(Y-c),
]

we have (P_A(X)=Q_A(X^8)). For (A\ne B), the polynomials (Q_A,Q_B) are distinct monic degree-(31) polynomials, so

[
\deg(Q_A-Q_B)\le30.
]

Consequently,

[
\deg(P_A-P_B)\le 8\cdot30=240.
]

Thus the Cycle116 fixed-jet theorem applies with

[
n=512,\qquad
j=248,\qquad
\sigma=8,
]

because

[
j-\sigma=240.
]

The associated code dimension is

[
k=n-(j+\sigma)
=512-256
=256,
]

and every witness support has size

[
n-j=264=k+\sigma.
]

This is a fresh prime-field template; it does not require the characteristic-(17) Cycle84 block identities.

### 3. Average-specialization lemma

Let (P_1,\ldots,P_M) be pairwise distinct polynomials over (\mathbb F_q) satisfying

[
\deg(P_i-P_j)\le d.
]

Let (D\subseteq\mathbb F_q), (|D|=n). Then some (\beta\in\mathbb F_q\setminus D) has at least

[
\left\lceil
\frac{M^2}
{M+
2\left\lfloor
\dfrac{d\binom M2}{q-n}
\right\rfloor}
\right\rceil
]

distinct values among (P_1(\beta),\ldots,P_M(\beta)).

Indeed, for (\beta\notin D), let (C_\beta) be the number of unordered colliding pairs

[
{i,j},\qquad P_i(\beta)=P_j(\beta).
]

Every nonzero (P_i-P_j) has at most (d) roots, so

[
\sum_{\beta\notin D} C_\beta
\le d\binom M2.
]

Hence some (\beta\notin D) satisfies

[
C_\beta\le
\left\lfloor
\frac{d\binom M2}{q-n}
\right\rfloor.
]

If the evaluation fibers at this (\beta) have sizes (m_1,\ldots,m_U), then

[
\sum_{\nu=1}^U m_\nu=M
]

and

[
\sum_{\nu=1}^U m_\nu^2=M+2C_\beta.
]

Cauchy–Schwarz gives

[
M^2
\le
U\sum_{\nu=1}^U m_\nu^2
=======================

U(M+2C_\beta),
]

which proves the lemma.

### 4. Goldilocks arithmetic

Apply the lemma with

[
D=H,\qquad n=512,\qquad d=240.
]

The collision-average integer is

[
\left\lfloor
\frac{240\binom M2}{q-512}
\right\rfloor
=============

20{,}543{,}782{,}425{,}128{,}147{,}188.
]

Therefore some (\beta\in\mathbb F_q\setminus H) produces at least

[
\begin{aligned}
L(q)
&=
\left\lceil
\frac{M^2}
{M+
2(20{,}543{,}782{,}425{,}128{,}147{,}188)}
\right\rceil\
&=
73{,}674{,}899{,}375{,}228{,}060
\end{aligned}
]

distinct locator values (P_A(\beta)).

Because (\beta\notin H), every (P_A(\beta)\ne0). Thus inversion preserves distinctness.

### 5. Fixed-jet transfer

The banked fixed-jet locator-to-MCA theorem now produces one affine line

[
f+zg
]

such that every distinct value (P_A(\beta)) yields the distinct slope

[
z_A=-\frac1{P_A(\beta)}
]

with witness support

[
S_A=H\setminus J_A,
\qquad |S_A|=264,
]

and with no simultaneous degree-(<256) explanations of (f) and (g) on (S_A).

Hence

[
\operatorname{LD}_{\rm sw}(C,264)
\ge73{,}674{,}899{,}375{,}228{,}060.
]

The same witnesses count at thresholds (263) and (262).

At the target radius,

[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil=262,
]

so the attached-source bridge gives

[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge\frac{L(q)}q.
]

Finally,

[
251L(q)-q
=========

45{,}655{,}673{,}767{,}658{,}739>0,
]

and therefore

[
\frac{L(q)}q>\frac1{251}>2^{-128}.
]

### 6. Why this is reconstruction rather than field descent

No unital field homomorphism

[
\mathbb F_{17^{32}}\longrightarrow\mathbb F_p
]

can perform the desired descent. Such a homomorphism would force (p=17), and every finite-field homomorphism is injective, which is impossible from (\mathbb F_{17^{32}}) into (\mathbb F_{17}).

Restriction of scalars produces a vector-valued code over (\mathbb F_{17}), not a scalar Reed–Solomon code over an accepted prime field. Trace has only (17) possible outputs and destroys the numerator. Norm is not additive and does not carry affine lines (f+zg) to affine lines.

The successful compiler therefore replaces the characteristic-(17) blocks by order-(8) subgroup fibers and replaces the Cycle84 product census by the average-specialization lemma.

FIELD AND PARAMETER LEDGER:

```text
field:
    q = 2^64 - 2^32 + 1
      = 18,446,744,069,414,584,321
    characteristic = q
    extension degree = 1

domain:
    theta = 1,803,076,106,186,727,246 mod q
    H = <theta>
    |H| = 512
    ord(theta) = 512

RS row:
    n = 512
    k = 256
    rate = 1/2

fixed-jet data:
    j = 248
    sigma = 8
    j + sigma = 256
    agreement = n - j = 264
    witness distance <= 248

target conventions:
    closed-radius agreement threshold = 262
    strict-radius agreement threshold = 263
    constructed agreement = 264

numerator:
    M = binom(64,31)
      = 1,777,090,076,065,542,336
    certified distinct slopes
      >= 73,674,899,375,228,060
    Cycle116 target
      = 52,747,567,092

field ledger:
    q_gen  = 18,446,744,069,414,584,321
    q_code = 18,446,744,069,414,584,321
    q_line = 18,446,744,069,414,584,321
    q_chal = null

MCA:
    epsilon_mca(C,125/256)
      >= 73,674,899,375,228,060 / q
      > 1/251
      > 2^-128
```

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved a finite attached-manuscript source theorem: a smooth prime-field Goldilocks ([512,256]) Reed–Solomon row has at least (73{,}674{,}899{,}375{,}228{,}060) support-wise MCA-bad slopes at agreement (264). I did not prove official/prize adoption.

2. **Field ledger.**
   Because the code is over a prime field, it has no proper subfields:

   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=q.
   ]

   The finite MCA theorem does not define a protocol challenge field, so

   [
   q_{\rm chal}=\mathrm{null}.
   ]

   I did not identify (q_{\rm chal}) with (q_{\rm line}).

3. **Event reductions.**
   Under the attached source definitions, no endpoint, quotient, periodic, tangent, affine-color, or charge rule reduces the numerator. All slopes are nonzero because (z_A=-1/P_A(\beta)). The fixed-jet theorem gives support-wise noncontainment, so a contained-line exception does not absorb the events. Official event actions remain unpinned.

4. **Decoding notion.**
   This concerns support-wise `LD_sw` and source MCA. It is not an ordinary fixed-word list-decoding lower bound and not, by itself, a protocol soundness failure.

5. **First official failure.**
   The existing `cycle117.official_source_contract.v1` schema hardcodes

   ```text
   row.field = F_17^32
   line_parameter.field_size = 17^32
   ```

   and therefore cannot even represent this Goldilocks row. The first missing official clause is an authority-pinned row decision

   ```text
   ACCEPT:
       field = F_(2^64-2^32+1)
       domain_order = 512
       dimension = 256
       agreement_consumed >= 263
       line_parameter.field_size = 2^64-2^32+1
   ```

   Only after that clause is supplied do the official event registry and `q_chal` clauses become the next blockers.

6. **Next worker target.**
   The next exact target is

   ```text
   V-CYCLE119-AUTHORITY-PINNED-GOLDILOCKS-ROW-EVENT-CONTRACT
   ```

   backed by a deterministic checker for the Proth residue, (\theta)-order, common-jet identity, collision-average bound, fixed-jet transfer, strict-ball margin, and q-ledger.

NEXT EXACT STEP:

Construct `V-CYCLE119-GOLDILOCKS-FIXED-JET-COMPILER-CHECKER` with the following terminal receipt:

```text
GOLDILOCKS_PRIME_PROTH_VERIFIED
ORDER_512_DOMAIN_VERIFIED
MU8_COSET_COMMON_JET_VERIFIED
AVERAGE_SPECIALIZATION_NUMERATOR >= 73,674,899,375,228,060
AGREEMENT_264_VERIFIED
STRICT_BALL_263_SURVIVES
q_gen = q_code = q_line = 2^64-2^32+1
q_chal = null
ATTACHED_SOURCE_ROW_EVENT_ACCEPTED
OFFICIAL_CONTRACT_PENDING
```

Mathematically, the accepted-prime-field compiler is complete. The remaining first wall is the authority-pinned admission of this exact Goldilocks row.
