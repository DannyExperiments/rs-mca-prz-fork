# Role 07 - Fail-Closed Replay Checker Engineer

Your task is to design, and if possible specify executable pseudocode for, a
fail-closed checker:

```text
V-CYCLE113-FROZEN-SOURCE-CONTRACT-REPLAY
```

The checker must ingest a candidate interval/P190 packet and the frozen
official contract. It must emit exactly one terminal decision:

```text
SOURCE_REJECTED
COLOR_COMPRESSED_OR_CHARGED
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_APCORR_LOCAL_LIMIT
SOURCE_RECEIPT_MISSING_NO_CLAIM
RESOURCE_EXHAUSTED_NO_CLAIM
```

Specify:

```text
input schema
official source/APcorr receipts
final retained color map
charge registry schema
integer q_line ledger
hashes / reproducibility fields
no-false-positive proof
no-false-negative proof
minimal replay tests
```

If you can prove the checker would decide the current packet from available
data, say so and give the terminal result. If not, return `PLAN` or
`EXACT_NEW_WALL` with the exact missing receipt. Do not claim proof from a
checker design alone.

