# Role 01 - Official Source Contract Reconstructor

Your task is to reconstruct the strongest source contract that is actually
available in the packet. You are not allowed to invent missing official
predicates.

Work backward from the canonical tracker, Cycle110-112 audits, and the director
report. Produce a formal contract with clauses for:

```text
source adapter
official AP_corr
endpoint convention
final retained K_line color map
retained-tag normalization
charge registry
field transfer / q_gen-to-q_line transfer
integer q_line ledger
```

Then decide whether the contract is sufficient to replay the interval/P190
packet.

Try to prove one of:

```text
SOURCE_REJECTED
COLOR_COMPRESSED_OR_CHARGED
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_APCORR_LOCAL_LIMIT
```

If impossible, return `EXACT_NEW_WALL` or `AUDIT` with the exact missing
contract clause and the minimum additional source receipt needed.

Be ruthless: if the packet does not define official `AP_corr`, say so and name
the first formal object that must be supplied. If it does, write the predicate
and apply it to the interval/P190 target.

