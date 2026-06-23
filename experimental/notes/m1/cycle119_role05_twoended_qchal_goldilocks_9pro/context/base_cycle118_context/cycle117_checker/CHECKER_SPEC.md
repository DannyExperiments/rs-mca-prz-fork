# Cycle117 Source-Contract Checker Specification

## Primary label

```text
BANKABLE_LEMMA
```

The attached manuscript source profile accepts the Cycle116 row and retains its raw support-wise events, but the packet does not contain an authority-pinned official challenge contract. The package therefore does not emit `PROOF` as its current primary label.

## Current terminal vector

```text
attached manuscript row    SOURCE_ACCEPTED_CYCLE116_ROW
attached manuscript q_chal QCHAL_UNDEFINED_FINITE_MCA_ONLY
attached manuscript events EVENT_RETAINED
official/prize contract    SOURCE_CONTRACT_MISSING_NO_CLAIM
```

These decisions are not contradictory. The first three are scoped to the pinned manuscript definitions; the last is the fail-closed official-promotion gate.

## Decision vocabulary

The checker reserves these exact semantic terminals:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
SOURCE_REJECTED_CYCLE116_ROW
SOURCE_CONTRACT_MISSING_NO_CLAIM
QCHAL_UNDEFINED_FINITE_MCA_ONLY
EVENT_RETAINED
EVENT_CHARGED_OR_EXCLUDED
```

A defined official `q_chal` is recorded as structured data, not as an invented terminal. A malformed or tampered package produces `CHECKER_REJECTED` with a named failure clause; it does not guess a semantic terminal.

## Verified finite row

```text
C = RS[F_17^32,H,256], H=<theta>, |H|=512
agreement = 262
delta = 125/256
N = 52,747,567,092 distinct support-wise noncontained slopes
LD_sw(C,262) >= N
epsilon_mca(C,125/256) >= N / 17^32
```

Claim scope is exactly:

```text
FINITE_RAW_SUPPORTWISE_MCA_AND_LD_SW_ONLY
```

The checker rejects promotion to ordinary list decoding, protocol soundness failure, an asymptotic theorem, an official prize counterpacket, or an accepted/deployed prime-field theorem unless a separately authenticated contract closes the relevant source gate.

## Field ledger

```text
q_gen  = 17^32
q_code = 17^32
q_line = 17^32
q_chal = null
```

`q_line` is the only MCA denominator. `q_chal` is not inferred from `q_line` and is not counted a second time.

The exact threshold audit is:

```text
floor(17^32 / 2^128) = 6
2^128 * 52,747,567,092 > 17^32
```

The crossing is true but not the substantive theorem: seven slopes already cross. The mathematical content is the explicit one-line packet of more than fifty-two billion distinct support-wise noncontained slopes.

## Extension-field admissibility

The attached manuscript acceptance is pinned to:

```text
RS_disproof_v3.tex:91-95    general RS row over a field; smooth power-of-two subgroup
RS_disproof_v3.tex:369-383  generated extension-field subgroup construction
RS_disproof_v3.tex:416-426  smooth extension-tower theorem over F_{p^d}
```

The machine arithmetic is:

```text
p=17
m=2^v2(17-1)=16
d=32
n=md=512
ord_512(17)=32
rho=1/2
k=256
rho(1-rho)m^2=64 >= 17
```

The Cycle116 verifier separately proves `|H|=512` and that `H` generates `F_17^32`. Lemma L1 states the natural-language implication from these pinned clauses to `SOURCE_ACCEPTED_CYCLE116_ROW` for the manuscript profile. This is not an authority-pinned official-prize acceptance.

## Canonicalization fixes

### Canonical A/R naming

```text
A = {theta eta^i : 0 <= i <= 118}
|A| = 119
role = padding/support-zero points

R = {theta eta^i : 119 <= i <= 255}
|R| = 137
role = unused/fixed co-support points
```

The checker rejects the swapped convention.

### Primitive-log gauge

```text
canonical executable gauge = beta = X+2 = [2,1] low-to-high
legacy display gauge        = X+1    = [1,1] low-to-high
```

Only `beta=X+2` numerical logs are accepted. The `X+1` master-display field is retained as `QUARANTINED_NOT_CONSUMED`; this package asserts no mixed-gauge numerical identity and needs no unproved reindexing map.

## Exact checking phases

### Phase 1 — byte integrity

1. Verify hard-coded SHA-256 pins for the source files, Cycle116 theorem, row contract, event audit, source-clause ledger, symbolic lemmas, official-contract schema, and provenance record.
2. Verify every one of the 18 files listed by the embedded Cycle116 `MANIFEST.sha256`.
3. Verify each source clause by whole-file hash, exact line range, line-slice hash, and embedded local text.

Any mismatch terminates with `CHECKER_REJECTED`.

### Phase 2 — nonmutating finite replay

1. Hash the complete embedded Cycle116 verifier tree.
2. Run `verify_transfer.py` directly with `-B` and `PYTHONDONTWRITEBYTECODE=1`.
3. Capture JSON in memory; do not redirect into package receipts.
4. Require `CYCLE116_TRANSFER_CERTIFICATE_VERIFIED`.
5. Rehash the verifier tree and require byte identity.

The legacy `run_self_tests.sh` is never executed because it overwrites manifest-pinned receipt files.

### Phase 3 — row and source admissibility

Machine checks:

```text
p=17, m=16, d=32, n=512, k=256
ord_512(17)=32
rho(1-rho)m^2 = 64 >= 17
H_order=512
H_generates_K=true
```

Source-text checks bind the general smooth RS definition, generated extension-field construction, explicit extension-field theorem, and finite Cycle116 row. The compact semantic implication is Lemma L1 in `SYMBOLIC_LEMMAS.md`.

Result for the attached manuscript profile:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
```

### Phase 4 — q-ledger

Require exact equality of `q_gen`, `q_code`, and `q_line` with `17^32`; require `q_chal=null`. The attached source quantifies `z` over the code/line field and divides by its cardinality. The generated-domain check prevents an improper-subfield denominator.

Result:

```text
QCHAL_UNDEFINED_FINITE_MCA_ONLY
```

### Phase 5 — event retention

The audit covers:

```text
endpoint
periodic
quotient
tangent
contained-line
affine-color
retained-event
charge/AP_corr
same-slope collision
protocol challenge filtering
```

Under the raw attached-source definition:

- endpoint deletion, affine-color normalization, retained-event maps, `AP_corr`, and charge registries are absent;
- periodic/quotient structure appears in later analytic bounds and is explicitly separated as a floor, but it does not quotient the raw set of bad field parameters;
- the tangent floor is an additional lower bound, not a deletion;
- contained-support exclusion is paid by the Cycle116 noncontainment proof;
- same-slope collisions are already deducted: `52,747,567,104 - 12 = 52,747,567,092`;
- protocol challenge filtering is not defined because the authority-pinned contract is missing.

Result for the attached manuscript profile:

```text
EVENT_RETAINED
```

Any official wrapper may impose different processing only through a supplied, authority-pinned contract.

### Phase 6 — official-contract gate

Without all three of the following, the checker emits `SOURCE_CONTRACT_MISSING_NO_CLAIM`:

```text
--official-contract <contract.json>
--official-document <authoritative source file>
--trusted-official-contract-sha256 <64-hex trust pin>
```

The optional contract must use `cycle117.official_source_contract.v1`, bind an authority/version/valid ISO date, hash the authoritative document, match its filename, provide exact row and line-parameter clauses, define or explicitly leave `q_chal` undefined, and exhaustively classify nine event-rule families:

```text
endpoint
periodic
quotient
tangent
contained_line
affine_color
retained_event
charge_registry
challenge_filter
```

Every cited clause is verified by exact line-slice SHA-256. A defined `q_chal` has no implied effect: `challenge_filter` must separately say whether the line events are retained, excluded, identified, or charged. An undefined `q_chal` combined with a non-retaining challenge filter is rejected as contradictory.

An untrusted JSON assertion is rejected; it cannot self-authorize by carrying its own hash.

## Event-rule outcomes under an official contract

```text
row decision REJECT                         -> SOURCE_REJECTED_CYCLE116_ROW
row decision ACCEPT, every event RETAIN     -> SOURCE_ACCEPTED_CYCLE116_ROW + EVENT_RETAINED
row decision ACCEPT, any exclusion/charge   -> EVENT_CHARGED_OR_EXCLUDED
no trusted exhaustive contract              -> SOURCE_CONTRACT_MISSING_NO_CLAIM
```

`PROOF` is emitted only in the second case, after the finite verifier, row/field checks, external trust pin, exact source clauses, and exhaustive event registry all pass. A defined `q_chal` is reported under `q_chal_definition`; it is not conflated with `q_line` or converted into a new terminal.

## `LD_sw` adapter

The exact attached-source adapter is:

```text
epsilon_mca(C,delta)
  = LD_sw(C,ceil((1-delta)n)) / |F|.
```

For Cycle116:

```text
ceil((1-125/256) * 512) = 262.
```

The package does not claim an external `(delta,a_LD,n+1)` line-decodability theorem. The bridge source explicitly leaves matching that external definition as a follow-up check. Close-point line decoding is recorded only as a stronger sufficient predicate.

## MCA versus ordinary list decoding

The certified numerator counts distinct bad slopes on one affine line. It does not exhibit one received word with `N` close codewords. Therefore ordinary list decoding is not a claimed consequence.

## Symbolic/source-text lemmas

The checker cannot machine-prove these semantic implications and leaves them explicitly hash-pinned:

```text
L1 attached-manuscript row admissibility
L2 q_gen/q_code/q_line ledger and q_chal nonpromotion
L3 event retention under the raw source definition
L4 exact LD_sw/MCA adapter and external line-decodability cut
L5 2^-128 interpretation
L6 primitive-log gauge normalization
L7 official-contract wall
L8 optional official-contract semantic attestation
```

L8 is important: a program can verify hashes and consistency, but not natural-language entailment. A future official contract must be externally authenticated as the authority's semantic extraction; the checker never treats keyword matches or a self-pinned JSON file as authority.

## Minimal inputs and hashes

### Primary source files

```text
681905d6de89697dafb8dccfc64d23cd6895050427d19f01ce504e13e0e799bd  inputs/source/RS_disproof_v3.tex
99e2b292e88526a9ba8cf289bf8255c91d4bd49dde799cf1be10d98e18d63bbc  inputs/source/slackMCA_v3.tex
e3fe7497eecd82a3f7db102b01586895cc90e366f190e9513a4c29ebff76f1cd  inputs/source/m2_line_decoding_mca_bridge.md
```

### Cycle116 theorem and verifier root

```text
3072bf3e63ca07038c6d12cdde80c5fe411764810e180eb5df91ca652a1ce3d9  inputs/cycle116/CYCLE116_CERTIFICATE.md
f1d95792e563aed890070f234f8d9361c7df1afd319bb41ea562f184b81dc5c4  inputs/cycle116/verifier/MANIFEST.sha256
```

The manifest transitively requires its 18 listed files. The source-contract checker does not replace the Cycle116 finite verifier; it wraps and replays it read-only.

### Compact contract layer

The exact current hashes are emitted in `EXPECTED_RECEIPT.json` under `machine_verification.critical_file_hashes` and in `SHA256SUMS.txt`. The critical compact files are:

```text
ROW_CONTRACT.json
EVENT_AUDIT.json
SYMBOLIC_LEMMAS.md
SOURCE_CLAUSES.json
SOURCE_CLAUSE_LEDGER.md
OFFICIAL_CONTRACT_SCHEMA.json
PACKAGE_PROVENANCE.json
```

### Input packet provenance

```text
943938c43f453cce08c922b65f37689b2c3b4d1cc4eaf5c7c1da9d9b3d71eb78  cycle117_extension_field_qchal_source_contract_9pro_packet(1).zip
```

`PACKAGE_PROVENANCE.json` records the original packet, selected internal paths, and verification of its internal SHA-256 manifest.

## Nonmutating harness

`run_self_tests.sh` runs one full baseline replay, then uses only temporary copies or temporary synthetic official contracts. It verifies:

```text
baseline expected receipt
source hash tamper rejection
canonical A/R swap rejection
invented q_chal rejection
X+1 canonical-gauge rejection
untrusted official-contract rejection
SOURCE_ACCEPTED_CYCLE116_ROW path
SOURCE_REJECTED_CYCLE116_ROW path
EVENT_RETAINED path
EVENT_CHARGED_OR_EXCLUDED path
defined q_chal recorded without invented terminal
undefined q_chal / challenge-filter contradiction rejection
package tree unchanged
```

No self-test receipt is mutated or regenerated in place.

## Pseudocode

```text
verify all hard-coded critical hashes
verify every source line-slice hash
verify embedded Cycle116 manifest
hash Cycle116 verifier tree
run Cycle116 verifier read-only
require tree hash unchanged

validate canonical row, A/R naming, beta=X+2 gauge
validate N distinct slopes and q ledger
validate extension-row arithmetic and agreement ceiling

attached.row   := SOURCE_ACCEPTED_CYCLE116_ROW     [L1]
attached.qchal := QCHAL_UNDEFINED_FINITE_MCA_ONLY [L2]
attached.event := EVENT_RETAINED                   [L3]

if no trusted official contract:
    primary := SOURCE_CONTRACT_MISSING_NO_CLAIM
    label   := BANKABLE_LEMMA
else:
    verify external trust pin and authoritative source hash
    verify every cited clause and all nine event families
    require challenge_filter to resolve any q_chal effect
    classify accepted/rejected row and retained/charged event terminal
    emit PROOF only for accepted row plus fully retained events
```
