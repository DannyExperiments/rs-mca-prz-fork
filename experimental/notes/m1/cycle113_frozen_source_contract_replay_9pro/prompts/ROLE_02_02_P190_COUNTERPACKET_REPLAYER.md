# Role 02 - P190 Counterpacket Replayer

Your task is to replay the strongest conditional P190 packet from Cycle112 as
if it were a candidate source-valid counterpacket, then try to kill or certify
it.

Start from:

```text
p = 130 * 2^128 + 1
floor(p / 2^128) = 130
claimed colors = 190
after one endpoint = 189
needed additional official loss to avoid counterpacket >= 59 colors
```

You must decide whether the official source adapter, `AP_corr`, final retained
normalization, endpoint convention, affine-color normalization,
quotient/periodic charges, contained incidences, same-slope collisions, or
charge ledger reduce the final count to at most 130.

Try to produce a source-valid `COUNTERPACKET`:

```text
SOURCE_VALID_LOW_T1_COUNTERPACKET
```

It must include:

```text
exact source data
official AP_corr verification
final retained color count
proof all official charges are absent or exactly paid
2^128 * N_free > q_line
```

If you cannot certify it, do not retreat to prose. Return:

```text
SOURCE_REJECTED
```

or

```text
COLOR_COMPRESSED_OR_CHARGED
```

with the exact first rejection clause or exact 59-plus color loss mechanism.

If neither can be decided from the packet, return `EXACT_NEW_WALL` with the
minimal replay certificate that would decide the P190 packet.

