LABEL: **BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL**

EXECUTIVE VERDICT:

Cycle84 transfers exactly to a Reed–Solomon **support-wise line-obstruction numerator** only after supplying a single-line RS witness contract. Under that contract, the transfer is lossless:

[
\operatorname{Occ}(\beta)=52{,}747{,}567{,}092
\quad\Longrightarrow\quad
LD_{\rm sw}(C,A)\ge 52{,}747{,}567{,}092,
]

and therefore

[
\epsilon_{\rm mca}(C,\delta)\ge
\frac{52{,}747{,}567{,}092}{q_{\rm line}},
\qquad
A=\left\lceil(1-\delta)n\right\rceil .
]

But (LD_{\rm sw}) is exactly the MCA numerator under another name. It does not avoid support-wise noncontainment bookkeeping.

There is a potentially cleaner route through a stronger, self-contained **close-point line-decoding** predicate: if Cycle84 supplies (N) distinct close points on one line and the line is globally not contained in the code, then per-slope noncontainment need not be checked. However, the packet does not contain the exact official definition of “((\delta,a_{\rm LD},b))-line-decodable,” so that cleaner predicate cannot be identified with the manuscript or protocol-facing notion.

List decoding is not a valid transfer route. Cycle84 counts many distinct slopes/received words; list decoding requires many codewords near one fixed received word. The small fiber bound (m_{\max}=2) points in the opposite direction.

The Cycle88/89 row can consequently be stated as a finite arbitrary-domain RS/GRS support-wise line/MCA obstruction. Rephrasing it as line decoding adds no official status and does not repair the power-of-two smooth-domain failure.

Confidence: **high**.

EXACT THEOREM OR OBSTRUCTION:

### Bankable transfer theorem

Let (F) be finite, let

[
C=\operatorname{RS}_F(D,k)\subseteq F^D,\qquad |D|=n,
]

and fix an integer (A\ge k+1). Let (\mathcal T) be a finite packet family and let

[
p:\mathcal T\longrightarrow F^\times
]

be its product/color map. Assume there exist:

* fixed words (f,g\in F^D);
* fixed (\alpha\in F) and (\lambda\in F^\times);
* for each (T\in\mathcal T), a support (S_T\subseteq D) with (|S_T|\ge A);
* for each (T), a codeword (c_T\in C);

such that, with

[
z_T=\alpha+\frac{\lambda}{p(T)},
]

one has

[
(f+z_Tg)|*{S_T}=c_T|*{S_T},
]

and no (c_f,c_g\in C) simultaneously satisfy

[
f|*{S_T}=c_f|*{S_T},
\qquad
g|*{S_T}=c_g|*{S_T}.
]

Then, for

[
\delta=1-\frac{A}{n},
]

the following hold:

[
LD_{\rm sw}(C,A)\ge |\operatorname{im}p|,
]

[
\epsilon_{\rm mca}(C,\delta)
\ge \frac{|\operatorname{im}p|}{|F|},
]

and, if the witnesses are supplied by one degree-(t) residue-line datum,

[
\Lambda^{\rm NC}_{t,\delta}(D,k)\ge |\operatorname{im}p|.
]

For the Cycle85/Cycle88 realizations, (t=1).

Here

[
LD_{\rm sw}(C,A)
================

\max_{f,g}
#\left{
z\in F:
\begin{array}{l}
\exists S,\ |S|\ge A,\ (f+zg)|_S\in C|_S,\
\nexists c_f,c_g\in C\text{ explaining }f,g\text{ on }S
\end{array}
\right}.
]

This is the exact line-decoding definition proved in the packet’s M2 note. It satisfies the identity

[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{LD_{\rm sw}!\left(C,\lceil(1-\delta)n\rceil\right)}
{|F|}.
]

#### Proof

Every (T) supplies a support-wise MCA-bad slope (z_T) by the two witness conditions. The map

[
x\longmapsto \alpha+\lambda/x
]

is injective on (F^\times), so distinct values of (p(T)) yield distinct slopes. Hence the number of packet-generated bad slopes is exactly (|\operatorname{im}p|). The identities with (LD_{\rm sw}), MCA, and residue-line packing then follow from the packet’s exact bridge and normal-form theorem.

### What Cycle84 contributes

For Cycle84,

[
P=|\mathcal P_0|=52{,}747{,}567{,}104,
]

[
N=|\operatorname{im}\Phi|
=\operatorname{Occ}(\beta)
=52{,}747{,}567{,}092.
]

Thus the theorem consumes (N), not merely (m_{\max}=2). The latter alone would only imply

[
|\operatorname{im}\Phi|\ge \left\lceil P/2\right\rceil.
]

The exact occupancy, together with the 12 double fibers and no larger fibers, gives the stronger lossless numerator (N).

The Cycle84 product set is not literally the RS bad-slope set. Under the common reciprocal-affine normalization, the packet-generated slope set is

[
\alpha+\lambda\bigl(\operatorname{im}\Phi\bigr)^{-1}.
]

It is canonically bijective to the Cycle84 product image and is a subset of the full RS bad-slope set; additional bad slopes may exist.

### Cleaner close-point line-decoding theorem

Define the close-point slope set

[
CP_\delta(f,g)
==============

{z\in F:\operatorname{dist}(f+zg,C)\le\delta}.
]

Suppose the same reciprocal-affine construction gives (U) distinct slopes (z_T) satisfying only

[
\operatorname{dist}(f+z_Tg,C)\le\delta,
]

and suppose the affine line (f+Fg) is not contained in (C). Then

[
|CP_\delta(f,g)|\ge U.
]

Consequently the code fails the self-contained property

[
f+Fg\not\subseteq C
\quad\Longrightarrow\quad
|CP_\delta(f,g)|\le L
]

for every (L<U), in particular for (L=U-1).

This route replaces per-slope support-wise noncontainment by one global check that the line is not contained. It is genuinely cleaner. But it is not yet the packet’s official ((\delta,a_{\rm LD},b)) notion: the exact quantifiers and exceptional code-line alternative for that notion are absent.

PROOF / DISPROOF / ROUTE CUT:

**PROOF.** The occupancy-to-(LD_{\rm sw})-to-MCA theorem above is exact. The reciprocal-affine normalization causes no loss when (\alpha,\lambda) are common and (\lambda\ne0).

**PROOF.** A support-wise bad-slope packet with (U) distinct slopes also disproves any close-point line-decoding bound allowing fewer than (U) close slopes on a noncontained line.

**ROUTE CUT.** The packet does not provide the authoritative definition of

[
(\delta,a_{\rm LD},b)\text{-line-decodable}.
]

It supplies only the interface statement

[
(\delta,a_{\rm LD},n+1)\text{-line-decodable}
\Longrightarrow
\epsilon_{\rm mca}(C,\delta)\le a_{\rm LD}/|F|.
]

Therefore the contrapositive line-decoding failures below are conditional on that missing source contract. The meaning of (b=n+1), the exact radius convention, and any “close to a code-line” exception are not specified sufficiently to promote them to official line-decoding theorems.

**ROUTE CUT.** (LD_{\rm sw}) does not eliminate support bookkeeping. It is definitionally the support-wise MCA numerator.

**ROUTE CUT.** List decoding does not follow. A list-decoding obstruction requires one (y\in F^D) with many distinct codewords in its radius-(\delta) ball. Cycle84 supplies many distinct parameters (z), hence many centers (f+zg), normally with one witness codeword per center. Even a double product fiber does not prove two distinct codewords around one received word. No nontrivial list lower bound follows from the finite anchor.

**Cycle88/89 status.** The two-copy row can be paper-facing as a conditional finite arbitrary-domain RS/GRS MCA or (LD_{\rm sw}) theorem. It cannot become an official Proximity Prize result merely by changing terminology to line decoding:

[
464=2^4\cdot29
]

is not a power-of-two smooth multiplicative-domain length, and Cycle90 cuts the simple subgroup/padding/shortening port.

FIELD AND PARAMETER LEDGER:

Let (a_{\rm LD}) denote the allowed number of exceptional slopes in the external shorthand; let (A) denote agreement size.

| Row                 | RS parameters                        | Agreement/radius                   | Certified numerator                                  | Nominal conditional line-decoding failure            |
| ------------------- | ------------------------------------ | ---------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| Cycle85 one-copy    | ((t,n,k,\sigma,j)=(1,256,137,6,113)) | (A=k+\sigma=143), (\delta=113/256) | (N=52{,}747{,}567{,}092)                             | not (\bigl(113/256,\ N-1,\ 257\bigr))-line-decodable |
| Cycle88/89 two-copy | ((t,n,k,\sigma,j)=(1,464,232,6,226)) | (A=238), (\delta=226/464=113/232)  | (B=NP/2=1{,}391{,}152{,}917{,}379{,}006{,}070{,}784) | not (\bigl(113/232,\ B-1,\ 465\bigr))-line-decodable |

These two nominal failures mean “not line-decodable for any integer slope budget below the certified numerator,” conditional on the missing implication contract.

For the one-copy row,

[
q_{\rm line}=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481,
]

so

[
\epsilon_{\rm mca}\ge N/q_{\rm line}
\approx 2^{-29.781}.
]

Also,

[
\left\lfloor q_{\rm line}/2^{128}\right\rfloor=0.
]

Thus any positive bad-slope numerator exceeds (2^{-128}) as a literal finite inequality. This does not make the row an official 128-bit protocol counterexample: its rate is (137/256), and no protocol contract identifies this small line field with the actual challenge experiment.

For the two-copy row,

[
q_{\rm line}=17^{48}
====================

115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641,
]

and

[
\left\lfloor q_{\rm line}/2^{128}\right\rfloor
==============================================

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

Hence

[
B-\left\lfloor q_{\rm line}/2^{128}\right\rfloor
================================================

1{,}052{,}535{,}899{,}107{,}157{,}125{,}156>0,
]

or equivalently

[
B/q_{\rm line}\approx 2^{-125.961}>2^{-128}.
]

The denominator is always (q_{\rm line}):

* (q_{\rm gen}) records the field generated by the construction/data. It is not an MCA denominator.
* (q_{\rm code}) is the code alphabet. It is not automatically the slope denominator.
* (q_{\rm line}) is the field over which (z) ranges and is the sole denominator in the finite MCA/line experiment.
* (q_{\rm chal}) is usable only after proving that the protocol challenge is exactly this line experiment.

For the direct (17^{48}) finite row, (q_{\rm code}=q_{\rm line}=17^{48}). Treating (q_{\rm chal}) as the same field is an additional protocol/source contract, not a consequence of the code construction.

SELF-AUDIT:

1. **Exact implication proved.** I proved that an RS packet satisfying the common-line, reciprocal-affine, support, codeword, and noncontainment hypotheses yields at least (\operatorname{Occ}(\beta)) support-wise bad slopes, hence the corresponding (LD_{\rm sw}), residue-line, and MCA lower bounds. I also proved the weaker-hypothesis close-point line-decoding failure theorem.

   **Not proved.** I did not prove that the packet’s external ((\delta,a_{\rm LD},n+1)) line-decoding terminology has the close-point or (LD_{\rm sw}) definition. I did not prove a list-decoding failure, protocol attack, prize-family embedding, or official Proximity Prize result.

2. **Claim level.** The abstract theorem is paper-facing and exact. The one-copy and two-copy instantiations are finite RS/GRS research certificates to the extent their audited witness antecedents are accepted. The two-copy row is not official-prize-relevant because its domain length is not an admissible power-of-two smooth multiplicative length. Neither row is protocol-facing without a protocol reduction.

3. **First possible failure.** The first line is the common RS-line realization:

   [
   \chi_T=\alpha+\lambda/\rho_\beta(T)
   ]

   with the same (\alpha,\lambda,f,g) for every (T). In Cycle85 language, this is the fixed six-jet/common-(\gamma_T=1) assertion. If the normalization depends on (T), Cycle84 product occupancy does not control distinct slopes. The next failure is support-wise noncontainment.

4. **Field use.** The numerator is divided only by (q_{\rm line}). No credit from (q_{\rm gen}), (q_{\rm code}), or (q_{\rm chal}) is legitimate without a proved field-transfer or protocol identity. The (2^{-128}) comparison is the integer test

   [
   2^{128}U>q_{\rm line}
   \quad\Longleftrightarrow\quad
   U>\left\lfloor q_{\rm line}/2^{128}\right\rfloor.
   ]

5. **Potential numerator losses.**

   * Same-slope collisions must be removed before division. Cycle84 uses exact occupancy (N), not packet count (P).
   * A common reciprocal-affine normalization is bijective and causes no loss; packet-dependent normalization can invalidate the count.
   * Contained incidences do not count for support-wise MCA and must be excluded. Cycle88/89 claim a Vandermonde exclusion.
   * The two-copy projective/same-slope loss is already represented by the conservative division by two.
   * Quotient or periodic labels do not automatically remove genuine distinct bad slopes under `def:mca`; they matter only through actual collisions or an explicit source-retention rule.
   * Endpoint and tangent slopes are not automatically deleted by the canonical MCA definition. A protocol may delete, merge, or charge them only through an explicit official contract.
   * List-decoding requires an additional numerator-changing concentration theorem and receives no numerator from Cycle84 as presently stated.

6. **Exact missing conversion.** The missing external theorem is:

   [
   \boxed{
   (\delta,L,n+1)\text{-line-decodable}
   \Longrightarrow
   LD_{\rm sw}
   !\left(C,\left\lceil(1-\delta)n\right\rceil\right)
   \le L
   }
   ]

   with a verbatim definition of the left side, exact treatment of code-line exceptions, radius rounding, and the role of (n+1). Without that theorem, the displayed ((\delta,a_{\rm LD},b)) failures remain conditional.

NEXT EXACT STEP:

Run a fail-closed checker/source-contract task:

[
\texttt{V-CYCLE115-OFFICIAL-LINE-DECODING-ADAPTER-AND-RS-WITNESS-REPLAY}.
]

It must ingest:

1. An authority-pinned verbatim definition of ((\delta,a_{\rm LD},b))-line-decodability and a proved adapter either to (LD_{\rm sw}) or to the close-point predicate.
2. A machine-readable Cycle85 or Cycle88/89 witness contract containing:

   * code and domain fingerprint;
   * common (f,g), or common residue datum ((E,B,w));
   * support threshold and witness codeword for every compressed packet class;
   * the common reciprocal-affine slope formula;
   * proof that all product values are nonzero;
   * noncontainment certificates for MCA, or one global noncontained-line certificate for close-point line decoding;
   * exact collision/projective quotient accounting.
3. A field ledger fixing (q_{\rm gen},q_{\rm code},q_{\rm line},q_{\rm chal}) and the integer (2^{-128}) comparison.

Its terminals should be:

```text
FINITE_RS_LINE_DECODING_FAILURE
FINITE_RS_MCA_ONLY
OFFICIAL_LINE_DEFINITION_MISMATCH
PRIZE_DOMAIN_REJECTED
SOURCE_RECEIPT_MISSING_NO_CLAIM
```

For an official prize result, one further theorem is indispensable: an above-reserve realization on an actual power-of-two multiplicative subgroup/coset that preserves the Cycle84-derived slope surplus. Cycle90 already rules out a simple port of the length-464 row.
