# Cycle117 Source-Contract Checker

This is a self-contained, fail-closed reviewer package for the Cycle116 extension-field row.

## Current decision

```bash
./run_checker.sh
```

Expected primary result:

```text
label            = BANKABLE_LEMMA
primary_terminal = SOURCE_CONTRACT_MISSING_NO_CLAIM
```

The same receipt separately certifies the pinned manuscript profile:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
QCHAL_UNDEFINED_FINITE_MCA_ONLY
EVENT_RETAINED
```

This is not an official-prize promotion. It is the strongest source-backed result available from the attached packet: the manuscripts mathematically admit the extension-field smooth row and retain the raw support-wise events, while no authority-pinned official challenge contract is present.

## Nonmutating tests

```bash
./run_self_tests.sh
```

The harness runs the finite replay once. Every destructive test uses a temporary copy, and official-contract state-machine tests use temporary synthetic documents. It rejects swapped A/R names, invented `q_chal`, an `X+1` canonical gauge, untrusted contracts, and an undefined-`q_chal`/challenge-filter contradiction. It verifies all requested semantic terminals and leaves the package tree byte-identical. It never runs the legacy Cycle116 self-test that overwrites pinned receipts.

## Files to review first

```text
CHECKER_SPEC.md             terminal semantics, inputs, hashes, pseudocode
SOURCE_CLAUSE_LEDGER.md     exact source clauses and line-slice hashes
SYMBOLIC_LEMMAS.md          semantic implications not machine-proved
EVENT_AUDIT.json            endpoint/periodic/quotient/tangent/etc. ledger
ROW_CONTRACT.json           canonical row, fields, A/R, and gauge
EXPECTED_RECEIPT.json       immutable expected checker output
verify_source_contract.py   standard-library checker
PACKAGE_PROVENANCE.json     input packet and extraction provenance
SHA256SUMS.txt              every delivered file except itself
```

## Official contract input

The attached packet contains no authority-pinned official challenge contract. To test a future one:

```bash
./run_checker.sh \
  --official-contract official_contract.json \
  --official-document official_source.txt \
  --trusted-official-contract-sha256 <trusted-64-hex-pin>
```

`OFFICIAL_CONTRACT_SCHEMA.json` documents the required structure. It requires an exhaustive nine-family event registry, including `challenge_filter`, so a defined `q_chal` cannot silently alter the line event. A defined challenge field is recorded as data; the checker does not invent a new q-terminal. A contract cannot establish its own authority merely by including a hash—the trust pin must be supplied independently.
