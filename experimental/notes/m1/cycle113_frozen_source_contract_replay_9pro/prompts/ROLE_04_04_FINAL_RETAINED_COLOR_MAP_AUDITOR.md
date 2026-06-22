# Role 04 - Final Retained Color Map Auditor

Your task is to audit final retained colors. The whole round can fail if the
models count colors before endpoint, same-slope, affine, quotient, contained,
or retained-tag normalization.

Define the final retained color map in the strongest source-valid way supported
by the packet. Apply it to the interval/P190 target.

Questions to answer exactly:

1. What is a "color" at the final `q_line` ledger stage?
2. Which preliminary colors are identified by endpoint normalization?
3. Which are identified by affine color normalization?
4. Which are killed by same-slope collisions or contained incidences?
5. Which are charged by quotient/periodic structure?
6. Does the P190 target really retain more than 130 final colors after all
   official normalizations?

Try to return:

```text
COLOR_COMPRESSED_OR_CHARGED
```

with exact final retained count and exact color-loss ledger.

If instead the final retained count stays above threshold, give the exact
remaining source-valid counterpacket conditions. If the final color map is
missing from the packet, return `SOURCE_RECEIPT_MISSING_NO_CLAIM` and define
the replay receipt needed.

