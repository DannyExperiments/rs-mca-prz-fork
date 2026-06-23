# Cycle117 Extension-Field q-Chal Source Contract Returns Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Date: 2026-06-23.

Auditor: Codex.

## Executive Verdict

Cycle117 was significant, but it is not an official prize solve.

The conservative synthesis is:

```text
ATTACHED MANUSCRIPT SOURCE: accepted
q_line ledger: accepted
q_chal: undefined / null for the finite source theorem
raw event retention: accepted under the manuscripts
external line-decodable predicate: missing
official Proximity Prize promotion: route cut, missing authority-pinned contract
```

In plain terms: Cycle116 is no longer merely an isolated finite/checker row. Under
the attached manuscript definitions (`RS_disproof_v3.tex`, `slackMCA_v3.tex`,
and the M2 `LD_sw` bridge note), it promotes to a source-compatible finite
support-wise MCA / `LD_sw` theorem:

```text
C = RS[F_17^32,H,256], H=<theta>, |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128
q_gen = q_code = q_line = 17^32
q_chal = null
```

The promotion stops before official prize status because the packet still lacks
an authority-pinned official contract adopting the manuscript definition,
admitting this exact extension-field row, identifying the challenge/line
sampling field, and exhaustively specifying retained-event / endpoint / quotient
/ periodic / tangent / charge rules.

## Raw Preservation

Raw pasted returns and Role 08 generated files were preserved under:

```text
experimental/notes/m1/cycle117_extension_field_qchal_source_contract_9pro_returns_raw/
```

Important files:

```text
01_source_contract_extractor_response.md
02_extension_field_admissibility_response.md
03_qchal_qledger_referee_response.md
04_event_retention_charge_auditor_response.md
05_line_decoding_adapter_response.md
06_official_implication_assembler_response.md
07_accepted_field_compiler_response.md
08_reviewer_checker_engineer_files/
09_skeptical_referee_response.md
SHA256SUMS.txt
```

Role 08 supplied:

```text
cycle117_source_contract_checker.zip
cycle117_source_contract_checker.zip.sha256
CHECKER_SPEC.md
EXPECTED_RECEIPT.json
observed_checker_receipt.json
observed_self_tests.out
```

Zip SHA-256:

```text
56d632b38bce0484b7d56fb66cd02abfcce5c9c65df988e526a32e06f71f7ffb
```

All raw-return checksums verify via:

```bash
cd experimental/notes/m1/cycle117_extension_field_qchal_source_contract_9pro_returns_raw
shasum -a 256 -c SHA256SUMS.txt
```

## Local Validation

Role 08's checker package was unpacked and inspected before running. It uses
only Python standard-library code, emits JSON to stdout, and does not run the
legacy mutating Cycle116 self-test.

Validation performed:

```text
shasum -a 256 -c SHA256SUMS.txt
python3 -m py_compile verify_source_contract.py nonmutating_self_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B verify_source_contract.py
PYTHONDONTWRITEBYTECODE=1 ./run_self_tests.sh
```

Default checker result:

```json
{
  "label": "BANKABLE_LEMMA",
  "primary_terminal": "SOURCE_CONTRACT_MISSING_NO_CLAIM",
  "attached_manuscript_source": {
    "basis": "PINNED_SOURCE_TEXT_PLUS_SYMBOLIC_LEMMAS_L1_L4",
    "event": "EVENT_RETAINED",
    "q_chal": "QCHAL_UNDEFINED_FINITE_MCA_ONLY",
    "row": "SOURCE_ACCEPTED_CYCLE116_ROW"
  },
  "official_contract": {
    "reason": "No authority-pinned official contract was supplied.",
    "row": "SOURCE_CONTRACT_MISSING_NO_CLAIM"
  },
  "cycle116_decision": "CYCLE116_TRANSFER_CERTIFICATE_VERIFIED"
}
```

Nonmutating self-tests pass:

```text
NONMUTATING_SELF_TESTS_PASS
```

The self-tests include:

```text
baseline_expected_receipt
source_hash_tamper_rejected
canonical_A_R_swap_rejected
invented_q_chal_rejected
X_plus_1_canonical_gauge_rejected
untrusted_official_contract_rejected
official_accept_terminal_verified
official_reject_terminal_verified
official_charged_or_excluded_terminal_verified
defined_qchal_recorded_without_invented_terminal
undefined_qchal_challenge_filter_contradiction_rejected
package_tree_unchanged
```

One local note: an initial `py_compile` created `__pycache__`, which caused the
checker self-test's package-cleanliness assertion to fail. Removing only those
generated cache directories from the unpacked copy and rerunning gave the clean
pass above. The original zip was unchanged.

## Role Ledger

| Role | Visible label | Conservative audit | Useful content |
|---|---|---|---|
| 01 Source Contract Extractor | ROUTE_CUT | Correct as official/prize audit; accepts manuscript source but cuts official promotion. | Names the missing authority/version/adoption clause and separates manuscript semantics from governing prize semantics. |
| 02 Extension-Field Admissibility | PROOF | `PROOF` is valid only for attached-manuscript admissibility, not official prize status. | Shows the row is an exact extension-tower specialization with `p=17,m=16,d=32,n=512,rho=1/2`. |
| 03 q-Chal / q-Ledger | BANKABLE_LEMMA | Bankable. | Establishes `q_gen=q_code=q_line=17^32`, `q_chal=null`, denominator is only `q_line`, and no extra challenge denominator may be invented. |
| 04 Event Retention / Charge | BANKABLE_LEMMA | Bankable for raw manuscript definitions. | Shows no attached-source endpoint/periodic/quotient/tangent/affine-color/charge deletion applies; contained-line and same-slope losses are already paid. |
| 05 Line-Decoding Adapter | ROUTE_CUT | Correct. | Proves the `epsilon_mca` / `LD_sw` bridge at agreement `262`, and cuts the external `(delta,a_LD,n+1)` line-decodable predicate because it is not defined in the packet. |
| 06 Official Implication Assembler | PROOF plus explicit official route cut | Use as synthesis, but do not quote `SOURCE_ACCEPTED_MCA_COUNTERPACKET` without the manuscript-scope qualifier. | Gives the strongest theorem statement and a useful PRZ-facing formulation. |
| 07 Accepted-Field Compiler | PROOF | Valid for attached-source row acceptance; official status remains missing. | Correctly says the accepted-field compiler is not activated by this packet unless an official contract rejects extension fields. |
| 08 Reviewer Checker Engineer | BANKABLE_LEMMA package | Most bankable artifact in the round. | Provides a fail-closed source-contract checker, schema, clause ledger, expected receipt, event audit, and nonmutating self-tests. |
| 09 Skeptical Referee | ROUTE_CUT | Correct and should control public claim language. | Strongly identifies the first broken arrow: raw manuscript theorem does not imply authority-approved Proximity Prize row/predicate. |

## What Was Proved

### 1. Source-manuscript extension-field admissibility

The attached manuscripts admit smooth multiplicative RS rows over prime-power
fields, including generated extension-field examples. The Cycle116 row fits the
source vocabulary:

```text
K = F_17^32
H = <theta> <= K^*
|H| = 512 = 2^9
C = RS[K,H,256]
ord_512(17)=32
F_17(H)=K
```

This makes Cycle116 a valid row under the attached manuscript definitions. It
does not make it an official prize row.

### 2. q-ledger and denominator

The finite/source theorem uses:

```text
q_gen = 17^32
q_code = 17^32
q_line = 17^32
q_chal = null
```

The MCA denominator is `q_line`. There is no source-defined second denominator,
and `q_chal` cannot be silently equated with or multiplied by `q_line`.

Exact arithmetic:

```text
17^32 = 2367911594760467245844106297320951247361
floor(17^32 / 2^128) = 6
52,747,567,092 > 6
```

So the `2^-128` comparison is true. It is not the hard part: seven bad slopes
would cross the threshold. The substantive theorem is the explicit common line
with `52,747,567,092` distinct support-wise noncontained slopes.

### 3. Raw event retention

Under the attached manuscript MCA definitions:

```text
endpoint deletion: absent
periodic quotienting: present analytically, irrelevant as raw-event deletion
quotient profile/core charge: present analytically, not a raw numerator charge
tangent floor: lower-bound mechanism, not deletion
contained-line exclusion: present and paid by Cycle116 noncontainment
same-slope collision: present and paid by Cycle84 occupancy deduplication
affine-color normalization: absent
retained-event map: absent
AP_corr / charge registry: absent
protocol challenge filtering: missing external contract
```

Thus all `N=52,747,567,092` designated slopes survive as manuscript-source
support-wise MCA bad parameters.

### 4. `LD_sw` adapter

Cycle117 banks the exact attached-source adapter:

```text
epsilon_mca(C,delta)
  = LD_sw(C,ceil((1-delta)n)) / |F|
```

For Cycle116:

```text
n = 512
delta = 125/256
ceil((1-delta)n) = 262
```

This is enough for the support-wise MCA / `LD_sw` theorem. It is not enough for
an external `(delta,a_LD,n+1)-line-decodable` statement because that predicate is
not formally defined in the supplied source packet. The strict-vs-closed ball
issue matters: Cycle116 proves agreement `262`, not a strict-ball agreement
`263` claim.

## What Was Not Proved

Cycle117 does not prove:

```text
official Proximity Prize counterpacket
protocol soundness failure
ordinary list-decoding lower bound
asymptotic theorem
accepted/deployed prime-field theorem
external line-decodability failure
```

The official branch remains:

```text
SOURCE_CONTRACT_MISSING_NO_CLAIM
```

This is not a mathematical rejection of the extension-field row. It is a missing
authority/adoption layer.

## Conflicts and Resolution

The visible labels were split:

```text
PROOF: roles 02, 06, 07
BANKABLE_LEMMA: roles 03, 04, 08
ROUTE_CUT: roles 01, 05, 09
```

This is not real mathematical disagreement after scoping. The consistent
resolution is:

```text
PROOF under attached manuscript/source semantics.
BANKABLE_LEMMA for q-ledger, event retention, and checker package.
ROUTE_CUT for official prize promotion and external line-decodability.
```

Therefore the round's terminal conservative label is:

```text
BANKABLE_LEMMA / ROUTE_CUT / AUDIT
```

## Significance

Yes, significant.

Cycle116 answered PRZ's request for a standalone finite transfer certificate.
Cycle117 now answers the next semantic layer:

```text
Does the attached mathematical source accept the Cycle116 extension-field row?
```

Answer:

```text
Yes, under the attached manuscripts.
```

The round also packages a checker that makes the boundary reviewable:

```text
attached manuscript row: SOURCE_ACCEPTED_CYCLE116_ROW
attached manuscript q_chal: QCHAL_UNDEFINED_FINITE_MCA_ONLY
attached manuscript events: EVENT_RETAINED
official/prize contract: SOURCE_CONTRACT_MISSING_NO_CLAIM
```

That is progress toward a paper-facing result. It is not the final prize claim.

## Next Exact Target

The next exact object is not another occupancy computation. It is an
authority-bearing semantic adapter:

```text
V-CYCLE118-AUTHORITY-PINNED-OFFICIAL-ROW-EVENT-CONTRACT
```

Required clauses:

```text
1. The official/protocol source admits or rejects RS[F_17^32,H,256].
2. The official line/challenge parameter is sampled from F_17^32, or else q_chal is explicitly defined.
3. The official bad-event predicate is identified with the manuscript support-wise MCA predicate, or the first difference is named.
4. Endpoint, periodic, quotient, tangent, contained-line, affine-color, retained-event, AP_corr, and charge rules are exhaustively classified.
5. The external line-decodability predicate is formally defined, including closed vs strict ball convention and whether agreement 262 is enough.
```

If such a contract accepts the raw manuscript semantics, Cycle116 composes into
an official/source counterpacket. If it rejects extension fields or changes the
event map, the next math target becomes:

```text
L-CYCLE117-ACCEPTED-FIELD-FIXED-JET-OCCUPANCY-COMPILER
```

but that compiler should not be attacked until the official rejection clause is
actually known.
