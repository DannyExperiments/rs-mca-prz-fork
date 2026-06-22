# Role 07: Certificate Engineer

Design a replayable checker/certificate format for Cycle112.

The checker must accept an explicit block/prefix/affine-involution packet and
emit exactly one terminal:

```text
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_BLOCK_PACKET_CHARGED
T1_APCORR_LOCAL_LIMIT_CERTIFIED
SOURCE_RECEIPT_MISSING_NO_CLAIM
```

Specify inputs, hashes, exact arithmetic, proof obligations, and what is and is
not mathematically certified. If feasible, give pseudocode or source-level
structure.
