## LABEL

**ROUTE_CUT**

## EXECUTIVE VERDICT

**Terminal source-contract verdict:** `SOURCE_CONTRACT_MISSING_NO_OFFICIAL_PROMOTION`

**Confidence: high.**

The attached manuscripts **do accept**
[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],\qquad H=\langle\theta\rangle,\quad |H|=512
]
as a smooth multiplicative-domain Reed–Solomon row. Under their raw support-wise line-MCA definition:

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},
\qquad q_{\rm chal}\text{ is unset},
]
and Cycle116 yields
[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}

> 2^{-128}.
> ]

None of the attached raw MCA definitions deletes or charges the counted slopes through endpoint, periodic, quotient, tangent, affine-color, retained-event, or charge rules. The sole relevant exclusion is support-wise containment, and Cycle116 proves noncontainment.

The official/prize promotion nevertheless fails at an earlier wall: **the packet contains no authority-pinned rule saying that the prize adopts the manuscript’s “natural reading” or “transcribed” support-wise formulation.** The manuscript is a mathematical source, not the governing prize contract.

Thus:

* **Attached-manuscript admissibility:** yes.
* **Official/prize admissibility:** not established.
* **Official counterpacket:** not established.
* **First blocking item:** missing authority/version/adoption clause, not an extension-field rejection.

## SOURCE-PINNED THEOREM OR ROUTE CUT

### The theorem actually supported by the attached text

Let
[
K=\mathbb F_{17^{32}},\qquad H=\langle\theta\rangle\le K^\times,
\qquad |H|=512,
]
and let
[
C=\operatorname{RS}[K,H,256].
]

The attached manuscripts and Cycle116 jointly imply:

1. (H) is a smooth multiplicative domain.
2. (H) generates (K).
3. The source line parameter is (z\in K).
4. At (\delta=125/256),
   [
   \left\lceil(1-\delta)|H|\right\rceil
   ====================================

   \left\lceil\frac{131}{256}\cdot512\right\rceil
   =262.
   ]
5. Therefore
   [
   \epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
   =================================================

   \frac{\operatorname{LD}_{\rm sw}(C,262)}{|K|}
   \ge
   \frac{52{,}747{,}567{,}092}{17^{32}}.
   ]

This is a **source-definition-compatible finite theorem**.

### The exact route cut

The missing implication is:

[
\text{attached manuscript definition}
\quad\Longrightarrow\quad
\text{governing official/prize definition}.
]

No attached authority document supplies it.

The decisive manuscript language is itself qualified:

* `context/source/RS_disproof_v3.tex:91-95` describes the support-wise endpoint as the authors’ **“natural reading”** of the challenge.
* `context/source/RS_disproof_v3.tex:106-107` says the conjecture is a **“transcribed”** minimal no-slack, same-support, line formulation and expressly distinguishes formulations with slack, curves, or different agreement notions.
* `context/source/RS_disproof_v3.tex:86` disclaims negative conclusions for formulations with protocol-specific agreement restrictions.
* `context/source/slackMCA_v3.tex:1043-1044` says whether raw or quotient-adjusted counts are operational depends on the protocol definition.
* `context/source/slackMCA_v3.tex:1525-1526` says extension-field sampling normalization must be checked against the external imported definition.
* `context/source/m2_line_decoding_mca_bridge.md:408-414` leaves matching the external line-decodability predicate as a follow-up check.

The packet’s own index, `FILE_INDEX_FOR_MODEL.md:18-22`, identifies the governing materials only as two manuscripts and one bridge note. No official rules document, adopted challenge version, evaluator specification, or authority-root hash is included.

The prior audit reaches the same textual conclusion at `context/audits/m1_cycle114_pinned_official_source_root_decider_returns_audit.md:150-173`: the archive defines MCA machinery but lacks the official endpoint, retained-event, charge, and field-allocation contract.

Accordingly, the first missing clause is:

> **An authority-pinned adoption clause identifying the official challenge with the attached support-wise line-MCA definition, including its admissible field/domain universe and challenge-sampling/event-retention semantics.**

## PROOF DETAILS

### 1. Smooth-domain and extension-field admissibility

The manuscript’s general notation says:

* (q) may be a general prime power;
* (D) or (H\le\mathbb F_q^\times);
* “smooth” means the domain order is a power of two;
* (C=\operatorname{RS}[\mathbb F_q,D,k]).

This is explicit at `context/source/slackMCA_v3.tex:153-154`.

The abstract likewise defines smooth multiplicative domains as subgroups
[
H\le\mathbb F_q^\times
]
of power-of-two order at `slackMCA_v3.tex:95-96`.

Extension fields are not merely implicit. The source proves and discusses rows
[
\operatorname{RS}[\mathbb F_{p^d},D,k]
]
over generated extension fields at:

* `context/source/RS_disproof_v3.tex:369-425`;
* in particular the theorem statement at lines `416-425`;
* and the any-prime-power smooth-domain theorem at `context/source/slackMCA_v3.tex:1488-1499`.

Cycle116 proves:

[
K=F_0(\theta)\cong\mathbb F_{17^{32}},
\qquad \theta^2=\eta,
\qquad \operatorname{ord}(\theta)=512,
]
and
[
H=\langle\theta\rangle,\qquad |H|=512
]
at `context/cycle116_verifier/14_V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE.md:278-305`.

Since (512=2^9), this is exactly a smooth multiplicative domain under the source definition.

Moreover (H) generates (K): it contains (\theta), its square (\eta) generates (F_0), and (F_0(\theta)=K). This is recorded at Cycle116 certificate lines `582-598`.

Therefore the attached manuscript formulation does **not** reject the row because it is an extension-field row.

### 2. Exact raw MCA normalization

The source defines a bad parameter for a line
[
u_z=f+zg
]
using a common agreement support (S), together with failure of simultaneous explanations for (f) and (g). It then defines

[
\epsilon_{\rm mca}(C,\delta)
============================

\max_{f,g}
\frac{#{z\in\mathbb F:z\text{ is bad}}}{|\mathbb F|}.
]

See:

* `context/source/RS_disproof_v3.tex:110-114`;
* `context/source/slackMCA_v3.tex:639-647`.

For the Cycle116 code, the (\mathbb F) appearing in that definition is (K=\mathbb F_{17^{32}}). Hence the source sampling set is exactly
[
z\in\mathbb F_{17^{32}},
]
and the denominator is
[
q_{\rm line}=17^{32}.
]

This remains true even if the constructed bad slopes happen to lie in a proper subset or subfield: the source error is normalized by the full field over which (z) is quantified.

### 3. Composition with Cycle116

The finite theorem gives
[
\operatorname{LD}_{\rm sw}(C,262)
\ge 52{,}747{,}567{,}092
]
at Cycle116 certificate lines `374-386`.

Since
[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil=262,
]
the exact bridge gives
[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}.
]

The exact calculation is recorded at Cycle116 certificate lines `389-404`.

Finally,
[
17^{32}
=======

2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361
]
and
[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
]

Because
[
52{,}747{,}567{,}092>6,
]
the strict (2^{-128}) crossing follows. Numerically, the certified lower bound is approximately (2^{-95.18}).

The threshold comparison is correct but is not the substantive theorem: the substantive content is the construction of one line with more than (5.27\times10^{10}) distinct support-wise noncontained slopes.

### 4. Why this does not complete official promotion

The phrase “for the prize fields” in `RS_disproof_v3.tex:100-101` does not identify (\mathbb F_{17^{32}}) as an official prize field. The attached manuscript’s mathematical universe is broader than any attached authority-defined challenge universe—because no such authority-defined universe is attached.

Likewise, descriptive uses of “challenge,” “deployed,” or “prize rates” are not an admission predicate. No attached clause has the form:

[
\operatorname{Admissible}*{\rm official}
(\mathbb F*{17^{32}},H,512,256)=\mathrm{true}.
]

## FIELD AND PARAMETER LEDGER

| Parameter      | Meaning in the attached material                                  | Cycle116 value | Status                         |
| -------------- | ----------------------------------------------------------------- | -------------: | ------------------------------ |
| (q_{\rm gen})  | Size of the field generated by the domain, or field of definition |      (17^{32}) | Fixed                          |
| (q_{\rm code}) | Size of the RS alphabet/coefficient field                         |      (17^{32}) | Fixed                          |
| (q_{\rm line}) | Size of the field through which (z) ranges in (f+zg)              |      (17^{32}) | Fixed; MCA denominator         |
| (q_{\rm chal}) | Separate protocol/verifier challenge field, if any                |     unset/null | Not defined by attached source |

The source’s field-of-definition correction appears at:

* `context/source/slackMCA_v3.tex:238-247`;
* `context/source/slackMCA_v3.tex:600-602`.

That correction prevents one from improperly using a large ambient alphabet field when the domain is defined over a smaller subfield.

Here it causes no mismatch because (H) generates (K). Thus
[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}.
]

The source files do not define a symbol or independent object (q_{\rm chal}). For the code/line-MCA theorem there is only one random-line parameter universe: (z\in K). Setting (q_{\rm chal}=17^{32}) would therefore add an unsupported second field. The correct ledger entry is:

[
q_{\rm chal}=\text{uninstantiated}.
]

A future protocol contract could introduce a separate challenge field or restricted challenge set, but no attached clause does so.

## EVENT RETENTION / CHARGE AUDIT

| Possible rule                   | Attached raw-source status                                                | Effect on Cycle116’s (52{,}747{,}567{,}092) slopes                 |
| ------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Endpoint removal                | Absent                                                                    | No removal                                                         |
| Periodic-event removal          | Absent from raw MCA                                                       | No removal                                                         |
| Quotient-periodic normalization | Appears only in separate corrected/aperiodic packing conjectures          | No removal from raw (\epsilon_{\rm mca})                           |
| Tangent exclusion               | No such exclusion; tangent witnesses themselves form a lower-bound family | No removal                                                         |
| Contained-line exclusion        | Present through the simultaneous-explanation condition                    | Paid by Cycle116 noncontainment proof                              |
| Affine-color quotient           | Absent                                                                    | No removal; color restriction was already paid in the finite shell |
| Retained-event map              | Absent                                                                    | Official retention remains undefined                               |
| Charge registry                 | Absent                                                                    | No slope is source-charged                                         |
| Duplicate-slope quotient        | Ordinary set cardinality only                                             | Already paid by distinct-value occupancy                           |

### Endpoint

The source uses the affine parameter set (z\in\mathbb F), not a projective line with an extra (z=\infty) endpoint. There is consequently no endpoint deletion rule.

Cycle116’s slopes are finite because (P_T(\beta)\neq0). This is included in the certificate’s loss audit at lines `600-608`.

### Periodic and quotient rules

Raw MCA is defined directly by counting bad (z). It contains no periodicity equivalence relation.

`context/source/slackMCA_v3.tex:1255-1256` defines a separate “aperiodic packing normalization” for corrected positive conjectures. It does not amend the earlier raw definition at lines `643-647`.

The same manuscript explicitly distinguishes:

* the raw bad-slope count; and
* a quotient-separated count that a future protocol might use,

and says the operational choice depends on the protocol definition at `slackMCA_v3.tex:1043-1044`.

Therefore quotient structure does not pay or remove any Cycle116 slope under the attached raw definition.

Caution: the native Cycle116 row has an explicit degree-one residue denominator (E=X-\beta), so it is not a pullback through a proper quotient. The lifted row, however, is certified directly by support-wise MCA; Cycle116 does **not** prove that the lifted line remains in the same degree-one residue coordinate. Consequently, should a future official contract impose an aperiodicity filter, the lifted line would require a new classification theorem. That issue is irrelevant to the current raw definition.

### Tangent

The “tangent floor” at `slackMCA_v3.tex:667-674` is a construction of bad slopes:
[
\epsilon_{\rm mca}(C,\delta)\ge \lfloor\delta n\rfloor/q.
]
It is not an exclusion or payment rule.

Cycle116’s certificate additionally reports that its contained/tangent concerns are ruled out by the Vandermonde noncontainment argument; see certificate lines `500-514` and `600-608`.

### Contained-line condition

This is the one genuine source-side exclusion.

For every witness support (S_J), Cycle116 proves that (g|_{S_J}) cannot be explained by a codeword. The proof is the Vandermonde independence argument at certificate lines `500-514`. This is stronger than merely proving failure of simultaneous explanations.

Hence all certified slopes satisfy the source’s noncontainment requirement.

### Affine color and same-slope collisions

Cycle116 certificate lines `225-274` establish:

* the finite shell’s color condition was already imposed before occupancy was counted;
* multiplication by the nonzero scalar (\kappa=4(\beta-1)) is bijective;
* inversion is bijective;
* the reported (N) is the number of distinct slope values.

The 12 double fibers have already been collapsed in the occupancy count. No further division by a color or fiber multiplicity is permitted.

### Official event retention

No attached file defines:

* an official retained-event map;
* retained-tag equivalence;
* an endpoint policy;
* an exhaustive charge registry;
* an official periodic or quotient deletion;
* a protocol-specific challenge subset.

Thus the correct conclusion is:

> All (N) slopes are retained under the attached raw support-wise MCA definition; their retention under an official protocol definition is undefined.

## LINE-DECODING VS LD_SW ADAPTER

The bridge note defines
[
a(\delta)=\left\lceil(1-\delta)n\right\rceil
]
and
[
\operatorname{LD}_{\rm sw}(C,a)
===============================

\max_{f,g}
#{z:\text{(z) is support-wise noncontained at agreement at least (a)}}.
]

It proves the exact identity
[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{
\operatorname{LD}_{\rm sw}
\left(C,\left\lceil(1-\delta)n\right\rceil\right)
}{|\mathbb F|}.
]

See `context/source/m2_line_decoding_mca_bridge.md:12-53`.

Therefore Cycle116 proves, without qualification:

[
\operatorname{LD}_{\rm sw}(C,262)
\ge52{,}747{,}567{,}092
]
and the corresponding raw support-wise MCA lower bound.

It also conditionally obstructs any stronger close-point line-decoding theorem of the form
[
\text{either the line is contained in (C), or }
#{z:\operatorname{dist}(f+zg,C)\le\delta}\le a_{\rm LD},
]
whenever (a_{\rm LD}<N). Every support-wise bad slope is a close line point, and Cycle116 proves that the line is not contained. This sufficient implication is stated at `m2_line_decoding_mca_bridge.md:249-259`.

But the packet does not contain an official definition of the external notation
[
(\delta,a_{\rm LD},n+1)\text{-line-decodable}.
]
Indeed, the bridge note itself lists matching that external definition as unfinished at lines `408-414`.

Hence the conservative implication ledger is:

* **Support-wise (LD_{\rm sw}) failure:** proved.
* **Raw support-wise MCA threshold crossing:** proved.
* **Failure of a stronger close-point cap:** conditional on matching its exact definition.
* **Official line-decodability failure:** not source-pinned.
* **Ordinary list-decoding lower bound:** not proved.

The construction does not provide one received word with (N) nearby codewords. Different slopes may use different explaining codewords and supports. It must not be advertised as ordinary list decoding.

## VERIFIER / REVIEWER CHECKLIST

* [x] Packet SHA-256:
  `943938c43f453cce08c922b65f37689b2c3b4d1cc4eaf5c7c1da9d9b3d71eb78`.
* [x] Every entry in the packet’s `SHA256SUMS.txt` verifies.
* [x] Cycle116 used only as the banked finite theorem authorized by the prompt.
* [x] Smooth-domain source definition pinned to `slackMCA_v3.tex:95-96,153-154`.
* [x] Explicit extension-field source rows pinned to `RS_disproof_v3.tex:369-425`.
* [x] (H) order and generated-field property pinned to the Cycle116 certificate.
* [x] Support-wise bad-event definition pinned to both manuscript definitions.
* [x] Exact (LD_{\rm sw})-to-MCA identity pinned to the bridge note.
* [x] (q_{\rm gen}), (q_{\rm code}), and (q_{\rm line}) distinguished.
* [x] (q_{\rm chal}) left unset rather than invented.
* [x] Agreement conversion (125/256\mapsto262) checked.
* [x] Contained-line exclusion paid by the Vandermonde argument.
* [x] Endpoint, periodic, quotient, affine-color, retained-event, and charge rules audited as absent from raw MCA.
* [x] Same-slope collisions already deducted in the certified occupancy.
* [x] No ordinary list-decoding claim.
* [x] No claim that the lifted row remains degree-one residue-line or aperiodic.
* [x] No claim that a single finite row disproves a general asymptotic (\operatorname{negl}(q)) statement.
* [x] No claim that (\mathbb F_{17^{32}}) is an official “prize field.”
* [x] Primitive-log gauge warning preserved: old prose uses an (X+1) log base, while executable slot logs use (\beta=X+2). Both are primitive and reproduce the same field product, but numerical logarithms must always identify their base; see Cycle116 certificate lines `560-568`.

## SELF-AUDIT

1. **Finite versus official:** The finite theorem is accepted; official promotion is not claimed.
2. **Extension-field status:** The attached mathematical source accepts prime-power extension fields and this generated smooth subgroup.
3. **First cut:** The cut is the missing authority/adoption contract, earlier than any field or event-filter issue.
4. **Denominator:** The raw source denominator is (17^{32}), not (17^{16}), because (z) ranges over the lifted code field.
5. **Challenge field:** No independent (q_{\rm chal}) is defined.
6. **Event retention:** All (N) distinct slopes survive the raw definition; official retention is undefined.
7. **Line decoding:** Only (LD_{\rm sw}), raw MCA, and conditional obstruction to stronger close-point caps are asserted.
8. **List decoding:** No single-word list lower bound is asserted.
9. **Threshold:** (\lfloor17^{32}/2^{128}\rfloor=6), but the (2^{-128}) comparison is secondary.
10. **Asymptotics:** One finite threshold crossing does not independently refute an asymptotic negligibility assertion unless the governing contract includes this row and its concrete threshold.

## NEXT EXACT STEP

There is a direct route to a full solve, but the next step is contractual rather than algebraic.

The next exact theorem should be:

### `V-CYCLE117-AUTHORITY-PINNED-ROW-ADMISSION-AND-EVENT-SEMANTICS`

Given an authority-identified rules document and version, prove all of the following:

1. **Adoption**
   [
   \operatorname{BadEvent}_{\rm official}
   ======================================

   \operatorname{BadEvent}_{\rm support\text{-}wise\ MCA}
   ]
   or provide an explicit adapter between them.

2. **Row admission**
   [
   \operatorname{RS}[\mathbb F_{17^{32}},H,256],
   \quad H=\langle\theta\rangle,\quad |H|=512
   ]
   lies in the official admissible code/domain universe.

3. **Sampling field**
   The official line parameter is sampled uniformly from (\mathbb F_{17^{32}}), or else the contract explicitly defines (q_{\rm chal}), its embedding into the code field, and its relation to (q_{\rm line}).

4. **Event processing**
   The contract specifies endpoint, periodic, quotient, tangent, contained-line, affine-color, retained-event, and charge rules.

5. **Retention**
   The Cycle116 slope set maps injectively—or with an explicitly bounded loss—into the official retained-event set.

6. **Line-decoding semantics**
   Any claimed official line-decodability consequence is matched exactly to (LD_{\rm sw}(C,262)) or to the stronger close-point predicate.

If that theorem adopts the raw attached definition with (z) uniform in (K), Cycle116 composes immediately into an official counterpacket.

If an authority-pinned contract instead rejects extension fields, the next construction becomes:

### `L-CYCLE117-ACCEPTED-FIELD-FIXED-JET-OCCUPANCY-COMPILER`

It must compile the fixed-jet locator family into an accepted field/domain while preserving:

[
P_T(X)=X^{113}-X^{112}+O(X^{107}),
]
a common affine line, agreement supports, noncontainment, and at least (N') officially retained distinct slopes satisfying
[
N'>\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor.
]

That compiler is conditional and premature here: **the attached mathematical source does not reject the extension-field row. The missing authority contract is the next exact wall.**
