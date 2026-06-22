# Role 03 - C284 Overlapping Chain Replay

Your task is to replay the stronger Cycle113 C284 overlapping-chain stress
packet. It was introduced to remove the easy disjoint-block objection and widen
the displayed gap.

Start from:

```text
C284 displayed colors = 284
C284 after one endpoint = 283
floor(q_line / 2^128) = 130
displayed gap after endpoint = 153
support intersections form a path/overlapping-chain pattern, not disjoint blocks
```

Decide whether official source machinery rejects, compresses, charges, or
accepts this packet. In particular, test:

```text
overlap/path incidences
same-slope or endpoint collapse
periodic/quotient structure
affine stabilizer or affine-color normalization
retained-tag normalization
interpolation-defect Fourier charge
```

Try to produce a source-valid `COUNTERPACKET`; if you cannot, produce the
first exact official rejection/compression/charge receipt. If the source root
needed to replay C284 is absent, return `SOURCE_RECEIPT_MISSING_NO_CLAIM`.

Do not claim C284 is a counterpacket from model arithmetic alone.

