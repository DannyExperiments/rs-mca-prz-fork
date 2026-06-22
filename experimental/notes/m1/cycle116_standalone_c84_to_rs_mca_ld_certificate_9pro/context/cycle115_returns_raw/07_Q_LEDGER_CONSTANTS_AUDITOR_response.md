LABEL: **BANKABLE_LEMMA**

EXECUTIVE VERDICT:

The arithmetic passes exactly. Conditional on a directly constructed (\mathbb F_{17^{48}})-valued ([464,232]) RS/GRS line satisfying the stated witness and final-slope multiplicity contracts, Cycle84 yields

[
1{,}391{,}152{,}917{,}379{,}006{,}070{,}784
]

distinct support-wise noncontained bad slopes, exceeding the (2^{-128}) threshold by

[
1{,}052{,}535{,}899{,}107{,}157{,}125{,}156.
]

This proves a conditional finite arbitrary-domain RS-MCA and support-wise line-decoding statement. It does **not** prove:

* that Cycle84 alone supplies the required RS line;
* any list-decoding statement;
* an official Proximity Prize counterpacket;
* that (q_{\rm chal}=17^{48});
* that (q_{\rm gen}=17^{48}) without a generated-field certificate.

The denominator (17^{48}) is legitimate only if the code and affine line are genuinely defined over (\mathbb F_{17^{48}}), with the line parameter ranging over that field. Merely taking extension-field challenges does not justify it.

Confidence: **high** on the arithmetic and typed transfer theorem; **moderate** on the claimed Cycle87 field/domain identities because the compact packet contains audit summaries but not the coefficient-level Cycle87 row bundle.

EXACT THEOREM OR OBSTRUCTION:

### Typed Cycle84 product-to-RS-line transfer theorem

Let

[
F_0=\mathbb F_{17^{16}},\qquad
L=F_0[U]/(U^3-\beta),\qquad \beta=X+2.
]

Let (\mathcal P_0) be the Cycle84 color shell, with

[
|\mathcal P_0|=P=52{,}747{,}567{,}104,
]

and let

[
\rho:\mathcal P_0\to F_0^\times,\qquad
\Omega=\rho(\mathcal P_0),\qquad
|\Omega|=N=52{,}747{,}567{,}092.
]

Suppose there exist:

1. a single code
   [
   C=\operatorname{GRS}_{232}(L,D,\lambda)\subseteq L^{464};
   ]

2. a single affine line (f+zg), with (f,g\in L^D) and (z\in L);

3. for every ((v,T)\in\Omega\times\mathcal P_0), a support
   [
   S_{v,T}\subseteq D,\qquad |S_{v,T}|=238,
   ]
   on which (f+z(v,T)g) agrees with a codeword of (C), and the witness is support-wise noncontained;

4. a common slope normalization
   [
   z(v,T)=A+\frac{B}{v,\pi(T)},
   \qquad A\in L,\quad B\in L^\times,\quad
   \pi(T)=P_T(U)\in L^\times;
   ]

5. the final projective-fiber bound
   [
   \max_{\kappa\in L^\times/F_0^\times}
   #{T\in\mathcal P_0:[\pi(T)]=\kappa}\le \mu.
   ]

Then

[
\operatorname{LD}_{\rm sw}(C,238)
\ge
\left\lceil \frac{NP}{\mu}\right\rceil,
]

and at

[
\delta=1-\frac{238}{464}=\frac{113}{232},
]

[
\epsilon_{\rm mca}(C,\delta)
\ge
\frac{\lceil NP/\mu\rceil}{|L|}.
]

For (\mu=2),

[
\operatorname{LD}_{\rm sw}(C,238)
\ge
\frac{NP}{2}
============

1{,}391{,}152{,}917{,}379{,}006{,}070{,}784.
]

#### Counting proof

If (z(v,T)=z(v',T')), the common affine-reciprocal normalization gives

[
v\pi(T)=v'\pi(T').
]

Since (v,v'\in F_0^\times),

[
[\pi(T)]=[\pi(T')]
\quad\text{in }L^\times/F_0^\times.
]

There are at most (\mu) possible (T)'s in that projective class, and once (T) and the final slope are fixed, (v) is uniquely determined. Thus every final slope has at most (\mu) preimages. Every retained final slope is support-wise MCA-bad by the noncontainment hypothesis.

This is the precise transfer theorem. Cycle84 supplies (P), (N), and the base product-fiber information. It does not supply hypotheses 1–5.

PROOF / DISPROOF / ROUTE CUT:

### 1. Exact finite-field identity

The Cycle84 verifier checks that (\beta=X+2) is primitive in (F_0^\times). Since

[
3\mid (17^{16}-1),
]

a primitive element cannot be a cube in (F_0). Therefore (U^3-\beta) has no root in (F_0); as a cubic, it is irreducible. Hence

[
|L|=|F_0|^3=17^{48}.
]

The exact field sizes are

[
q_0=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481,
]

[
q_{\rm line}=17^{48}
====================

115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641.
]

Also,

[
|L^\times/F_0^\times|
=q_0^2+q_0+1,
]

which is the correct projective quotient in the multiplicity condition.

### 2. Cycle84 consistency checks

[
P-N=12,
\qquad
D=24=2(P-N).
]

Thus the supplied data are consistent with exactly twelve double fibers and no fibers of size at least three.

### 3. Exact threshold arithmetic

Let

[
T_{48}=\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor.
]

Then

[
T_{48}
======

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

For an integer bad-slope count (B),

[
\frac{B}{17^{48}}>2^{-128}
\iff
B>T_{48}.
]

The candidate two-copy count is

[
NP
==

2{,}782{,}305{,}834{,}758{,}012{,}141{,}568,
]

[
\frac{NP}{2}
============

1{,}391{,}152{,}917{,}379{,}006{,}070{,}784.
]

Its exact margin is

[
\frac{NP}{2}-T_{48}
===================

1{,}052{,}535{,}899{,}107{,}157{,}125{,}156.
]

Equivalently,

[
\frac{NP/2}{17^{48}}
\approx 4.1083372728\cdot 2^{-128}
\approx 2^{-125.9614454}.
]

The alternative count is

[
N^2
===

2{,}782{,}305{,}834{,}125{,}041{,}336{,}464,
]

and (N^2) is divisible by (8), so

[
\left\lfloor\frac{N^2}{8}\right\rfloor
======================================

347{,}788{,}229{,}265{,}630{,}167{,}058.
]

Its exact margin is

[
\left\lfloor\frac{N^2}{8}\right\rfloor-T_{48}
=============================================

9{,}171{,}210{,}993{,}781{,}221{,}430.
]

Thus it gives only a (2.7084%) surplus:

[
\frac{\lfloor N^2/8\rfloor}{17^{48}}
\approx 1.0270843180\cdot2^{-128}.
]

The multiplicity wall is exact:

[
\left\lfloor\frac{N^2}{8}\right\rfloor>T_{48},
]

but

[
\left\lfloor\frac{N^2}{9}\right\rfloor
======================================

309{,}145{,}092{,}680{,}560{,}148{,}496
<T_{48}
]

by

[
29{,}471{,}925{,}591{,}288{,}797{,}132.
]

Therefore a total final collision/normalization loss bounded by (8) can work; a factor (9) cannot.

### 4. One-copy arithmetic and the illegitimate-denominator cut

For the one-copy field,

[
\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor=0.
]

Consequently any nonzero bad-slope count already exceeds the formal (2^{-128}) threshold over (F_0). In particular,

[
\frac{N}{17^{16}}
\approx 1.083976061\times10^{-9}
\approx 2^{-29.7810}.
]

This is mathematically valid but security-trivial: (q_0<2^{128}).

If one merely regards the same (N) slopes as lying in (L), without constructing new extension-valued bad slopes, then

[
N<T_{48}
]

by

[
338{,}617{,}018{,}219{,}101{,}378{,}536.
]

Thus the implication

[
\text{one-copy Cycle84 packet}
+\ q_{\rm chal}=17^{48}
\Longrightarrow
\text{(2^{-128}) failure using denominator (17^{48})}
]

is false. Either:

* the proven line field remains (F_0), so the denominator is (17^{16}); or
* one constructs the extension code and extension-valued line directly, in which case a new numerator theorem such as the projective-fiber theorem above is required.

A large (q_{\rm chal}) alone never supplies the denominator.

### 5. Official-prize route cut

Even if the ([464,232]) row is fully verified, its domain size is

[
464=2^4\cdot29,
]

not a power of two. Therefore it is not itself a power-of-two multiplicative subgroup or coset row. Cycle90 correctly cuts any simple padding, shortening, subgroup-inclusion, or quotient-pullback promotion of this exact domain into the official smooth power-of-two family.

FIELD AND PARAMETER LEDGER:

| Object           |                   One-copy row |             Candidate two-copy row | Audit                                                                    |
| ---------------- | -----------------------------: | ---------------------------------: | ------------------------------------------------------------------------ |
| Base field (F_0) |          (\mathbb F_{17^{16}}) |                    subfield of (L) | proved from Cycle84 field model                                          |
| (q_{\rm code})   |                      (17^{16}) |                          (17^{48}) | two-copy value requires an actual (L)-valued RS/GRS code                 |
| (q_{\rm line})   |                      (17^{16}) |                          (17^{48}) | this is the MCA denominator when (z) ranges over the corresponding field |
| (q_{\rm chal})   | not part of the finite theorem |     not part of the finite theorem | may equal (q_{\rm line}) only after a protocol transfer                  |
| (q_{\rm gen})    |                      (17^{16}) | requires a generated-field receipt | cannot be inferred merely from the ambient code field                    |
| Denominator      |                 (q_{\rm line}) |                     (q_{\rm line}) | never (q_{\rm code}) or unused (q_{\rm chal}) merely by relabeling       |

For the candidate row,

[
(n,k,\sigma,j,t)=(464,232,6,226,1),
]

[
\rho=\frac12,
\qquad
k+\sigma=238,
\qquad
j=n-k-\sigma=226,
]

[
\delta=1-\frac{k+\sigma}{n}
=\frac{226}{464}
=\frac{113}{232},
]

and the capacity gap is

[
\frac12-\delta=\frac{3}{232}.
]

For the one-copy row,

[
(n,k,\sigma,j,t)=(256,137,6,113,1),
]

[
\delta=1-\frac{143}{256}
=\frac{113}{256}.
]

The compact packet does not contain the explicit 464-point domain. Therefore (q_{\rm gen}=17^{48}) is not independently established here. A sufficient certificate would verify

[
\mathbb F_{17}(D,f,g)=L
]

under the prompt’s domain/received-data convention, or (\mathbb F_{17}(D)=L) under the narrower Paper C domain-only convention. This can be checked exactly by Frobenius subfield tests.

SELF-AUDIT:

1. **Exact implication proved and not proved.**
   Proved: the typed projective-fiber transfer theorem and all displayed arithmetic. An explicit (L)-valued RS line with full noncontained witness coverage and projective multiplicity at most (2) has at least (NP/2) bad slopes and therefore MCA error (>2^{-128}).
   Not proved: that Cycle84 alone constructs that line, that the compact Cycle87 summaries constitute an independent replay, any list-size consequence, or any official smooth-domain counterpacket.

2. **Claim level.**
   Conditional paper-facing finite arbitrary-domain RS-MCA and exact support-wise line-decoding. Not an official-prize result. Not a list-decoding theorem.

3. **First possible failure line.**
   Starting from Cycle84 alone, the first failure is
   [
   \text{color-filtered product packet}
   \Longrightarrow
   \text{one fixed RS/GRS line with noncontained witnesses}.
   ]
   If the Cycle85 one-copy bridge is accepted, the next failure is the two-copy extension-row contract:
   [
   (v,T)\mapsto A+B/(vP_T(U))
   ]
   on one ([464,232]) line with final projective multiplicity at most (2).

4. **Use of the four fields and the (2^{-128}) target.**
   The finite MCA denominator is (q_{\rm line}). (q_{\rm chal}) is irrelevant absent a protocol theorem. (q_{\rm code}) types the code but is not independently a probability denominator. (q_{\rm gen}) controls entropy/reserve claims, not the finite bad-slope fraction. The strict target is
   [
   N_{\rm bad}>\left\lfloor q_{\rm line}/2^{128}\right\rfloor.
   ]

5. **Possible numerator reductions.**
   Yes. (NP/2) is valid only after:

   * quotient/projective collisions are bounded by (2);
   * all witnesses are noncontained;
   * the final same-slope fibers are bounded after every normalization;
   * every reciprocal denominator is nonzero;
   * affine normalization uses one common (A,B) with (B\neq0);
   * any endpoint, tangent, periodic, affine-color, or retained-event deletion is applied before the final count.

   A common affine reciprocal map itself is bijective and causes no loss. Varying affine gauges may cause loss. Cycle84’s (m_{\max}=2) does not by itself bound the final extension-field slope multiplicity.

6. **What converts this to proof or counterpacket.**
   A typed coefficient-level replay of the exact row contract converts it to a finite RS-MCA/line-decoding proof. A separate smooth power-of-two domain construction and source-admissibility contract are necessary for an official-prize counterpacket.

NEXT EXACT STEP:

Run

```text
V-CYCLE115-TYPED-C84-TO-464-RS-LINE-TRANSFER
```

with the following mandatory outputs:

```text
FIELD:
  verify F0 and L=F0[U]/(U^3-beta);
  verify |L|=17^48.

DOMAIN:
  emit all 464 distinct evaluation points and GRS multipliers;
  compute q_gen by Frobenius subfield tests.

CODE_AND_LINE:
  emit the [464,232] GRS/RS code and one pair f,g in L^D;
  verify the line parameter ranges over L.

WITNESS_IDENTITY:
  prove symbolically that every retained (v,T) gives
  z(v,T)=A+B/(v P_T(U))
  and a size-238 RS agreement witness.

NONCONTAINMENT:
  verify the Vandermonde/rank obstruction for every witness class.

FINAL_MULTIPLICITY:
  perform the projective-fiber census after all quotient, endpoint,
  affine-color, periodic, and normalization maps;
  return mu_final <= 2, or at minimum <= 8 for the N^2 route.

INTEGER_CLOSE:
  output the final retained slope count B_final and verify
  2^128 * B_final > 17^48.
```

Passing this checker gives a finite arbitrary-domain RS-MCA and support-wise line-decoding **PROOF**. It cannot by itself give an official-prize **COUNTERPACKET**; that requires replacing the (464)-point domain with an admitted smooth power-of-two subgroup/coset row and separately fixing the extension-field/source contract.
