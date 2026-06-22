# Role 07 - Fail-Closed Checker Spec Engineer

Your task is to specify `V-CYCLE114-PINNED-OFFICIAL-SOURCE-ROOT-P190-OR-C284-DECIDER`
as a fail-closed replay checker.

The checker must ingest:

```text
official source-root bundle
candidate packet: P190 or C284
source adapter receipts
official AP_corr receipts
endpoint and final retained color/event map
charge registry
q_line ledger allocations
```

It must emit exactly one terminal:

```text
SOURCE_REJECTED
COLOR_COMPRESSED_OR_CHARGED
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_APCORR_LOCAL_LIMIT
SOURCE_RECEIPT_MISSING_NO_CLAIM
RESOURCE_EXHAUSTED_NO_CLAIM
```

Give:

```text
input schema
required hashes / file roots / theorem labels
validation order
terminal decision conditions
no-false-positive proof
no-false-negative proof
minimal replay tests
what can be verified from the current packet
what is missing
```

If possible, give executable pseudocode or Python-like schemas. Do not claim
the checker proves anything unless the current packet supplies every required
official receipt.

