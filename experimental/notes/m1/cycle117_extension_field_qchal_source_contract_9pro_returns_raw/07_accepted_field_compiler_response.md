## LABEL

**PROOF**

## EXECUTIVE VERDICT

The extension-field row is **accepted by the attached mathematical source**:

[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\qquad H=\langle\theta\rangle,\qquad |H|=512.
]

It is **not established as an official/deployed Proximity Prize row**. The packet contains no authority-pinned official adapter, retained-event map, endpoint policy, charge registry, or separate challenge-field definition. Official status is therefore **missing, not rejected**.

Consequently, the fallback compiler target

[
\texttt{L-CYCLE117-ACCEPTED-FIELD-FIXED-JET-OCCUPANCY-COMPILER}
]

is **not activated by this packet**. No accepted-field arithmetic compiler is needed for the attached source definition.

Confidence: **high**.

## SOURCE-PINNED THEOREM

### Exact admissibility clauses

The source defines smooth-domain Reed–Solomon codes over a general field (\mathbb F), with smooth meaning that the multiplicative subgroup has power-of-two order:
`context/source/RS_disproof_v3.tex:91-95` and `context/source/slackMCA_v3.tex:153-154`.

More decisively, the source has an explicit section titled “Extension-field towers” and says it constructs “generated extension-field examples”:
`context/source/RS_disproof_v3.tex:369-372`.

Its smooth extension-tower theorem is at:

```text
context/source/RS_disproof_v3.tex:416-426
```

Substitute

[
p=17,\qquad m=2^{v_2(16)}=16,\qquad d=32,\qquad
n=md=512,\qquad \rho=\frac12.
]

The hypotheses hold:

[
r=\rho m=8\in\mathbb Z,
\qquad
\rho(1-\rho)m^2=\frac14\cdot256=64\ge17.
]

Thus the source theorem itself treats

[
\operatorname{RS}[\mathbb F_{17^{32}},D,256]
]

for the order-(512) subgroup (D). Since (\mathbb F_{17^{32}}^\times) is cyclic, its subgroup of order (512) is unique, so (D=H).

The source’s (2)-adic tower criterion also gives

[
\operatorname{ord}_{512}(17)=32,
]

from `RS_disproof_v3.tex:394-413`. Hence an element of order (512) has degree (32) over (\mathbb F_{17}), proving

[
\mathbb F_{17}(H)=\mathbb F_{17^{32}}.
]

There is no hidden smaller field of definition.

The source extension-tower theorem proves a separate error-one result for this row at radius (255/512). That fact is used here only to establish admissibility; it does **not** imply Cycle116’s deeper radius (250/512=125/256).

### Source-admitted Cycle116 theorem

Combining the source definition with the finite Cycle116 certificate gives:

> Let (K=\mathbb F_{17^{32}}), (H=\langle\theta\rangle) of order (512), and (C=\operatorname{RS}[K,H,256]). There exist one affine line (f+zg) and at least
> [
> N=52{,}747{,}567{,}092
> ]
> distinct parameters (z\in K) such that each (f+zg) agrees with a codeword on a support of size (262), while (f) and (g) have no simultaneous code explanations on that same support. Therefore
> [
> LD_{\rm sw}(C,262)\ge N
> ]
> and
> [
> \epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
> \ge\frac{N}{17^{32}}>2^{-128}.
> ]

The finite construction and padding/noncontainment proof are in
`context/cycle116_verifier/14_V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE.md:276-404`.

The raw source definition accepting precisely these events is at:

```text
context/source/RS_disproof_v3.tex:110-115
context/source/slackMCA_v3.tex:639-653
```

This is a **source-valid finite support-wise MCA/(LD_{\rm sw}) theorem**, not an official prize counterpacket or asymptotic theorem.

## FIELD AND PARAMETER LEDGER

| Ledger entry   |                  Value | Justification                                               |   |                                   |
| -------------- | ---------------------: | ----------------------------------------------------------- | - | --------------------------------- |
| (q_{\rm gen})  |              (17^{32}) | (H) generates (K), since (\operatorname{ord}_{512}(17)=32). |   |                                   |
| (q_{\rm code}) |              (17^{32}) | The code alphabet is (K=\mathbb F_{17^{32}}).               |   |                                   |
| (q_{\rm line}) |              (17^{32}) | The source samples (z\in K) and divides by (                | K | ); see `slackMCA_v3.tex:643-647`. |
| (q_{\rm chal}) |     `null` / undefined | No primary source clause defines a separate (q_{\rm chal}). |   |                                   |
| (n)            |                  (512) | (                                                           | H | =512).                            |
| (k)            |                  (256) | Rate (1/2).                                                 |   |                                   |
| agreement      |                  (262) | Cycle116 padded support size.                               |   |                                   |
| (\delta)       |              (125/256) | (1-262/512=125/256).                                        |   |                                   |
| numerator      | (52{,}747{,}567{,}092) | Distinct bad slopes after occupancy deduplication.          |   |                                   |

The exact line-MCA definition is

[
\epsilon_{\rm mca}(C,\delta)
============================

\max_{f,g}\frac{#{z\in K:z\text{ is bad}}}{|K|}.
]

There is only one denominator. Neither (q_{\rm gen}) nor (q_{\rm code}) supplies an additional factor, and (q_{\rm chal}) cannot be invented.

Although the certified bad slopes happen to lie in the embedded native subfield (\mathbb F_{17^{16}}), this does not change the denominator: the source line parameter ranges over all (K).

The exact arithmetic is

[
17^{32}
=======

2367911594760467245844106297320951247361,
]

and

[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
]

Thus an integer numerator of (7) already crosses the (2^{-128}) threshold. The certified numerator is much larger:

[
\frac{N}{17^{32}}\approx 2^{-95.1804}>2^{-128}.
]

The floor (6) makes the threshold crossing immediate; it is not the main mathematical content. The substantive content is the common affine line, fixed jet, distinct-slope occupancy, noncontainment, and accepted generated-field row.

## EVENT RETENTION / CHARGE AUDIT

| Potential loss                   | Status under attached raw source | Finding                                                                                                                                                                                                                   |
| -------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint deletion                | `ABSENT_FROM_SOURCE`             | The definition counts affine parameters (z\in K); no endpoint deletion is defined. All Cycle116 slopes are finite because (P_T(\beta)\ne0).                                                                               |
| Periodic quotienting             | `PRESENT_BUT_IRRELEVANT`         | Quotient-periodic witnesses are discussed as a structural class, but are included in the raw MCA count. See `slackMCA_v3.tex:1043-1045`.                                                                                  |
| Quotient-profile/core charge     | `PRESENT_BUT_IRRELEVANT`         | Quotient terms are bounds/decompositions, not deductions from the raw numerator. The separated aperiodic packing is conjectural bookkeeping, not a redefinition of (\epsilon_{\rm mca}); see `slackMCA_v3.tex:1255-1256`. |
| Tangent floor                    | `PRESENT_BUT_IRRELEVANT`         | The tangent floor is an additional lower-bound mechanism, not a subtraction or exclusion.                                                                                                                                 |
| Contained-line/support exclusion | `PRESENT_AND_PAID`               | This is exactly condition (ii) of the MCA definition. Cycle116 proves noncontainment before and after padding.                                                                                                            |
| Affine-color normalization       | `ABSENT_FROM_SOURCE`             | The Cycle84 color condition was already paid by restricting the counted shell; no source-level color quotient exists.                                                                                                     |
| Same-slope collision             | `PRESENT_AND_PAID`               | The source counts distinct (z). Cycle116 counts distinct (\Phi)-values and then applies nonzero scalar multiplication and inversion, both bijections. The twelve double fibers are already deduplicated.                  |
| Retained-event map               | `ABSENT_FROM_SOURCE`             | Under the raw definition, the retained event is simply the distinct parameter (z).                                                                                                                                        |
| `AP_corr` or charge registry     | `ABSENT_FROM_SOURCE`             | No such evaluator or exhaustive charge system is defined in the primary source.                                                                                                                                           |
| Protocol challenge filtering     | `ABSENT_FROM_SOURCE`             | No separate challenge field or filter is defined.                                                                                                                                                                         |

At an **official/protocol layer**, endpoint, retained-event, periodic absorption, and charge rules are not known to be absent; they are simply missing from the packet. The prior source-root audit states this explicitly at
`context/audits/m1_cycle114_pinned_official_source_root_decider_returns_audit.md:24-28,150-173`.

## LINE-DECODING VS (LD_{\rm sw})

The attached bridge defines

[
LD_{\rm sw}(C,a)
================

\max_{f,g}
#{z:\text{(z) has a support-wise noncontained witness of size }\ge a}.
]

It then proves the exact identity

[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{LD_{\rm sw}(C,\lceil(1-\delta)n\rceil)}{|K|}.
]

Source:
`context/source/m2_line_decoding_mca_bridge.md:14-53`.

Here,

[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil
============

262.

]

Therefore the Cycle116 (LD_{\rm sw}) bound converts exactly into the stated MCA bound.

No ordinary list-decoding theorem follows. Different slopes may use different supports and different explaining codewords; the construction does not exhibit one received word with (N) nearby codewords.

The primary TeX sources do not formally define the external phrase

[
(\delta,a_{\rm LD},n+1)\text{-line-decodable}.
]

The bridge records that phrase only as an interpretation under audit. Accordingly, no ordinary close-point line-decodability failure is claimed.

## BRIEF COMPILER AUDIT

Because the row is source-admissible, the fallback compiler is unnecessary. The existing construction already preserves all required objects:

| Required invariant           | Status                                                                           |   |            |
| ---------------------------- | -------------------------------------------------------------------------------- | - | ---------- |
| Common fixed jet             | Preserved: (P_T(X)=X^{113}-X^{112}+O(X^{107})).                                  |   |            |
| Product-to-locator scalar    | Preserved: (P_T(\beta)=4(\beta-1)\Phi(T)), with nonzero common scalar.           |   |            |
| Distinct slope numerator     | Preserved: (N=52{,}747{,}567{,}092) after deduplication.                         |   |            |
| Noncontainment               | Preserved by the native fixed-jet theorem and the common (L_A)-padding argument. |   |            |
| Smooth multiplicative domain | Preserved: (H) is the order-(512) subgroup and generates (K).                    |   |            |
| Correct denominator          | Preserved: (q_{\rm line}=                                                        | K | =17^{32}). |
| Threshold relation           | Preserved: (N/q_{\rm line}>2^{-128}).                                            |   |            |

There is therefore no arithmetic `ROUTE_CUT` and no need to search for a replacement prime/deployed row unless a future authority-pinned official contract specifically rejects this generated extension-field row.

## VERIFIER / REVIEWER CHECKLIST

The included verifier was replayed independently and returned:

```text
CYCLE116_TRANSFER_CERTIFICATE_VERIFIED
```

It confirms the fixed jet, all (336) slot identities, (H)-generation, order (512), support size (262), noncontainment receipt, field ledger, and strict threshold inequality.

The primitive-log warning must remain attached:

* old display prose uses the (X+1) logarithm gauge;
* executable `slot_logs.json` uses (\beta=X+2);
* both are primitive and exponentiate to the same field products;
* all executable slot-log references and the locator identity here use (\beta=X+2).

No numerical logarithm should be quoted without naming its base. See the Cycle116 certificate at lines `560-568`.

## SELF-AUDIT

1. Cycle116 is used only as a finite support-wise MCA/(LD_{\rm sw}) theorem.
2. Extension-field acceptance is pinned to exact source theorems, not inferred from prompt prose.
3. (q_{\rm gen},q_{\rm code},q_{\rm line},q_{\rm chal}) are separated.
4. (H) is proved to generate (\mathbb F_{17^{32}}).
5. Every requested event/charge category is classified; absent rules were not invented.
6. No ordinary list-decoding claim is made.
7. The exact (LD_{\rm sw})-to-MCA adapter and ceiling calculation are given.
8. The floor (6) arithmetic is stated and treated as secondary.
9. The (X+1) versus (X+2) primitive-log gauge warning is preserved.
10. The terminal label is `PROOF`, not `COUNTERPACKET`.

## NEXT EXACT STEP

The remaining wall is not an accepted-field compiler. It is the theorem-focused contract:

```text
V-CYCLE117-AUTHORITY-PINNED-EXTENSION-ROW-OFFICIAL-ADMISSION-AND-EVENT-ADAPTER
```

It must either accept or reject this exact row and define any official (q_{\rm chal}), endpoint rule, retained-event map, periodic/quotient absorption, and exhaustive charge registry. Until such a contract exists, the row is source-accepted but official-prize status remains unresolved.
