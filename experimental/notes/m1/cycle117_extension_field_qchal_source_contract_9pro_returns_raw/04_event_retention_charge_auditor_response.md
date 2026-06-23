## LABEL

**BANKABLE_LEMMA**

## EXECUTIVE VERDICT

Under the attached source definitions, all

[
N=52{,}747{,}567{,}092
]

Cycle116 designated slopes survive as distinct support-wise MCA-bad parameters for

[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],\qquad |H|=512
]

at agreement (262). Thus the surviving source numerator is exactly

[
N_{\mathrm{surv}}=N.
]

No attached source clause deletes, quotients, charges, or forbids any designated slope. The only unresolved item is an external protocol challenge-field/retention contract. Consequently this is a source-MCA retention lemma, not an official protocol-soundness or ordinary list-decoding result.

Confidence: **high** for source-level retention; **unknown** for protocol challenge filtering.

## SOURCE-PINNED THEOREM OR ROUTE CUT

### Source-MCA retention lemma

Let

[
K=\mathbb F_{17^{32}},\qquad H=\langle\theta\rangle,\qquad |H|=512,
\qquad C=\operatorname{RS}[K,H,256].
]

Let (\mathcal P_0) be the Cycle84 shell and put

[
V={\Phi(\tau):\tau\in\mathcal P_0}.
]

Cycle116 certifies

[
|V|=52{,}747{,}567{,}092
]

and, using (\beta=X+2),

[
P_\tau(\beta)=\kappa\Phi(\tau),\qquad
\kappa=4(\beta-1)\ne0.
]

Define the designated slope set

[
\Gamma=\left{-\frac1{\kappa v}:v\in V\right}\subseteq K.
]

Then:

1. (|\Gamma|=|V|=N).
2. There is one affine line (\widetilde f+z\widetilde g) over (K^H) such that every (z\in\Gamma) has a witness support (S'_z\subseteq H) of size (262).
3. On (S'_z), the line point is the restriction of a degree-(<256) polynomial.
4. No degree-(<256) pair simultaneously explains (\widetilde f,\widetilde g) on (S'_z).

Therefore

[
\Gamma\subseteq
\operatorname{Bad}_{C,\widetilde f,\widetilde g}(125/256)
]

in the definitions of `RS_disproof_v3.tex:110–115` and
`slackMCA_v3.tex:639–653`, and hence

[
\operatorname{LD}*{\rm sw}(C,262)\ge N,
\qquad
\epsilon*{\rm mca}!\left(C,\frac{125}{256}\right)
\ge\frac{N}{17^{32}}.
]

The source bad-parameter set might contain additional slopes; the claim is that all (N) designated slopes remain present.

## PROOF DETAILS

### 1. Extension-field row admissibility

The source defines smooth multiplicative RS codes over a finite field (\mathbb F), with a power-of-two multiplicative subgroup as domain; see `RS_disproof_v3.tex:91–95` and `slackMCA_v3.tex:153–154`.

The extension-field section explicitly admits generated extension-field subgroups; see `RS_disproof_v3.tex:369–424`. The present row fits its tower parameters:

[
p=17,\qquad m=16,\qquad d=32,\qquad md=512.
]

Indeed,

[
17^{16}\equiv257\not\equiv1\pmod{512},
\qquad
17^{32}\equiv1\pmod{512},
]

so

[
\operatorname{ord}_{512}(17)=32.
]

An element (\theta) of order (512) therefore has degree (32) over (\mathbb F_{17}). Consequently

[
\mathbb F_{17}(\theta)=\mathbb F_{17^{32}}=K.
]

Thus (H=\langle\theta\rangle) is smooth, has order (512), and generates the full code field. The generated-field warning in `slackMCA_v3.tex:600–602` is fully satisfied.

### 2. No product-to-slope loss

Cycle116 gives

[
P_\tau(\beta)=\kappa\Phi(\tau),\qquad \kappa\ne0,
\qquad
z_\tau=-P_\tau(\beta)^{-1}.
]

Multiplication by (\kappa) and inversion on (K^\times) are bijections. Hence distinct occupied product values give distinct slopes.

The finite occupancy is already the distinct-value count:

[
|V|=N.
]

The 12 double fibers are pairs of supports producing an already-counted common slope; they are not 12 additional slopes. There are no packet fibers of multiplicity at least three. This is recorded in the Cycle116 certificate at lines `246–274` and in `19_cycle116_checker_receipt.json`.

### 3. Every native event survives the smooth lift

For every native bad slope (z), Cycle116 has a native support (S_z) of size (143). It chooses a fixed set (A\subset H\setminus D_0) of size (119), with locator (L_A), and sets

[
S'_z=S_z\cup A,\qquad |S'_z|=143+119=262.
]

If (p_z) is the native degree-(<137) explaining polynomial, then

[
\widetilde p_z=L_Ap_z
]

has degree (<256) and explains the lifted line point on (S'_z).

Suppose degree-(<256) polynomials (F,G) simultaneously explained the lifted anchor and direction on (S'_z). Both vanish on all 119 points of (A), so

[
F=L_AF_0,\qquad G=L_AG_0,
\qquad \deg F_0,\deg G_0<137.
]

Dividing by (L_A) on (S_z) would give simultaneous native explanations, contradicting native noncontainment. This is the exact argument in the Cycle116 certificate at lines `327–372`.

### 4. The source definition retains the witnesses directly

The source event is simply a field parameter (z) satisfying the two support-wise conditions. It does not subsequently pass the event through an endpoint evaluator, color quotient, charge map, or retained-event registry:

[
\epsilon_{\rm mca}(C,\delta)
============================

\max_{f,g}
\frac{#{z\in K:z\text{ is bad}}}{|K|}.
]

Each Cycle116 (z) satisfies the source predicate on a support of size

[
262
===

\left(1-\frac{125}{256}\right)512.
]

Therefore every element of (\Gamma) is counted.

## FIELD AND PARAMETER LEDGER

| Quantity          |                                           Value | Reason                                                                                             |   |    |
| ----------------- | ----------------------------------------------: | -------------------------------------------------------------------------------------------------- | - | -- |
| (q_{\rm gen})     |                                       (17^{32}) | (H=\langle\theta\rangle) generates (K), since (\operatorname{ord}_{512}(17)=32).                   |   |    |
| (q_{\rm code})    |                                       (17^{32}) | The code is (\operatorname{RS}[K,H,256]).                                                          |   |    |
| (q_{\rm line})    |                                       (17^{32}) | The source definitions quantify (z\in K) and divide by (                                           | K | ). |
| (q_{\rm chal})    |                       **null / uninstantiated** | No separate protocol challenge field is defined in the attached source contract.                   |   |    |
| Certified bad set | (\Gamma\subseteq\mathbb F_{17^{16}}\subseteq K) | The certified bad slopes originate in the native field and remain distinct after scalar extension. |   |    |
| Agreement         |                                           (262) | Exact source threshold at (\delta=125/256).                                                        |   |    |

The fact that the certified subset happens to lie in (\mathbb F_{17^{16}}) does not change (q_{\rm line}). The affine line is parameterized over all of (K), and the source denominator is the full line-parameter field.

## EVENT RETENTION / CHARGE AUDIT

| Possible loss                                  | Status                       | Audit result                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint deletion                              | **ABSENT_FROM_SOURCE**       | The definitions count every finite (z\in K). There is no projective point at infinity or distinguished finite endpoint deletion. Moreover every Cycle116 slope is nonzero because (z=-1/P_\tau(\beta)).                                                                           |
| Periodic quotienting                           | **PRESENT_BUT_IRRELEVANT**   | Quotient-periodic structure occurs in list-fiber classifications and the conjectural aperiodic packing statistic. It does not quotient the raw bad-parameter set. `slackMCA_v3.tex:1255–1256` explicitly adds the separated quotient contribution back into the raw MCA ledger.   |
| Quotient profile / quotient-core charge        | **PRESENT_BUT_IRRELEVANT**   | Quotient cores are principally a list-decoding construction. `slackMCA_v3.tex:633–635` states that quotient-core list inflation does not itself refute an MCA statement. The quotient-profile term is an upper-bound reserve, not a charge registry or event deletion.            |
| Tangent floor                                  | **PRESENT_BUT_IRRELEVANT**   | `slackMCA_v3.tex:667–674` proves a lower bound on MCA error. A lower-bound family cannot remove Cycle116 events.                                                                                                                                                                  |
| Contained-line exception                       | **PRESENT_AND_PAID**         | Source condition (ii) excludes supports simultaneously explaining the anchor and direction. Cycle116 proves the stronger fact that the direction is not code-explainable on each native support and proves preservation after lifting.                                            |
| Contained incidence deletion                   | **PRESENT_AND_PAID**         | Each lifted support (S'_z) remains noncontained by the (L_A)-divisibility argument. No designated event fails the source predicate.                                                                                                                                               |
| Affine-color normalization                     | **PRESENT_AND_PAID**         | Cycle84’s color restriction was imposed before computing (N); the certificate explicitly says it is already paid. The subsequent reciprocal-affine product-to-slope map is bijective. The source defines no further affine-orbit quotient on slopes.                              |
| Same-slope collisions beyond Cycle84 occupancy | **PRESENT_AND_PAID**         | (N) is the distinct product occupancy, not the raw support count. The 12 double fibers are already collapsed once. Multiplication by (\kappa) and inversion create no additional collision.                                                                                       |
| Retained-event map                             | **ABSENT_FROM_SOURCE**       | The source event is the finite parameter (z) itself. Equality in (K) is the only deduplication. No later retained-event quotient is defined.                                                                                                                                      |
| Source `AP_corr` or charge registry            | **ABSENT_FROM_SOURCE**       | None of `RS_disproof_v3.tex`, `slackMCA_v3.tex`, or `m2_line_decoding_mca_bridge.md` defines `AP_corr`, a charge registry, charge ownership, or a (q_{\rm line}) allocation mechanism. Such a mechanism cannot be invented or imported from the unrelated P190/C284 audits.       |
| Protocol challenge-field filtering             | **UNKNOWN_MISSING_CONTRACT** | The code/MCA source has no separate (q_{\rm chal}) or challenge-subset filter. `RS_disproof_v3.tex:505–511` expressly says protocol-specific constraints are absent and protocol soundness is untouched. This blocks protocol promotion but does not reduce the source numerator. |

There are no `PRESENT_AND_FATAL` entries. Therefore

[
\boxed{N_{\rm source;surv}=52{,}747{,}567{,}092}.
]

For an unspecified external protocol challenge set, the packet does not determine the surviving intersection. That uncertainty is not a valid source-side subtraction.

## LINE-DECODING VS `LD_SW` ADAPTER

The exact attached adapter is `context/source/m2_line_decoding_mca_bridge.md:14–53`:

[
\operatorname{LD}_{\rm sw}(C,a)
===============================

\max_{f,g\in K^H}
#\left{
z\in K:
\begin{array}{l}
\exists S,\ |S|\ge a,\ (f+zg)|_S\in C|_S,\
\text{but no }c_f,c_g\in C\text{ explain }f,g\text{ on }S
\end{array}
\right},
]

and

[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{
\operatorname{LD}_{\rm sw}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)
}{|K|}.
]

Here

[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil
=262.
]

Thus Cycle116 proves a support-wise `LD_sw` lower bound and the exactly equivalent source-MCA lower bound.

It does **not** prove ordinary list decoding: no single received word has been shown to possess (N) distinct nearby codewords. It also does not automatically prove a stronger close-point line-decoding statement whose predicate ignores common-support containment.

## VERIFIER / REVIEWER CHECKLIST

* Source row is a valid smooth generated extension-field row: **passed**.
* (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}): **passed**.
* (q_{\rm chal}) separately defined: **no; remains null**.
* Distinct occupancy (N=52{,}747{,}567{,}092): **passed**.
* Twelve double fibers counted only once: **passed**.
* Product-to-slope map injective: **passed**.
* Agreement (143+119=262): **passed**.
* Lifted code degree (<256): **passed**.
* Lifted support-wise noncontainment: **passed**.
* Source endpoint/periodic/color/charge deletion: **none applicable**.
* Official protocol challenge adapter: **missing**.
* Ordinary list-decoding lower bound: **not claimed**.

## SELF-AUDIT

1. **Finite versus official:** the result is promoted only to the attached source’s support-wise MCA/`LD_sw` definition, not to protocol soundness or an official prize counterpacket.
2. **Exact source acceptance:** `RS_disproof_v3.tex:91–95, 369–424` and `slackMCA_v3.tex:153–154` admit generated extension-field smooth subgroup rows.
3. **Field ledger:** all four (q)-quantities are separated; (q_{\rm chal}) was not invented.
4. **Extension field:** (H) generates (\mathbb F_{17^{32}}); it is not confined to a proper subfield.
5. **Event retention:** every requested loss mechanism was classified.
6. **Ordinary list decoding:** not claimed.
7. **Line adapter:** the exact equality with `LD_sw(C,ceil((1-delta)n))` is stated.
8. **Security arithmetic:**
   [
   \left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6,
   \qquad N>6.
   ]
   The threshold crossing is correct but is not the main mathematical contribution; the substantive content is the construction of (N) distinct noncontained slopes at agreement (262).
9. **Primitive-log gauge:** executable slot logs use (\beta=X+2); old prose displays an (X+1) gauge. Both reproduce the same field product, but numerical logarithms must retain their named base.
10. **Terminal label:** `BANKABLE_LEMMA` is used because source retention is proved while protocol challenge filtering remains externally unspecified.

## NEXT EXACT STEP

Produce an authority-pinned protocol adapter specifying:

[
Z_{\rm chal}\subseteq K,\qquad
\text{its sampling distribution},\qquad
q_{\rm chal},\qquad
\text{and any final event map}.
]

The decisive condition is either

[
\Gamma\subseteq Z_{\rm chal}
]

with no subsequent quotient or charge, or an exact computable formula for the image/intersection of (\Gamma). Until that contract exists, no protocol filtering loss may be asserted.
