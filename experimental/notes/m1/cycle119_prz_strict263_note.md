# Note for PRZ: Cycle119 Strict-263 Finite Transfer

Przemek,

Codex here. We reran the Cycle84-to-RS transfer through a stricter target than the earlier agreement-262 certificate.

The finite/source-scoped theorem now verified locally is:

```text
K = F_17^32
H = <theta>, |H| = 512
C = RS[K,H,256]

LD_sw(C,263) >= 52,747,567,092.
```

Equivalently, the same Cycle84 numerator survives with distance at most:

```text
512 - 263 = 249 < 250 = (125/256)*512.
```

So the strict-ball off-by-one issue is no longer the mathematical obstruction.

The key repair is a two-ended locator functional. It uses:

```text
common top six locator coefficients
+
common nonzero constant coefficient
```

For the augmented degree-249 locators, the selected coefficient coordinates are:

```text
0,250,251,252,253,254,255
```

The local replay explicitly checks that the varying degree-243 coefficient is not used, so this is not silently assuming a seventh common top coefficient. It also avoids the invalid naive padding proof: we do not multiply a native degree-<137 explaining polynomial by a degree-120 padding locator and pretend degree <256 survives. The final line is constructed directly in the `[512,256]` parity-check space.

Local checker terminal:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

with:

```text
agreement = 263
distance_upper_bound = 249
distinct_slopes = 52,747,567,092
q_gen = q_code = q_line = 17^32
q_chal = null
```

What this does not prove: official Proximity Prize status, ordinary fixed-word list decoding, protocol soundness, or any independent `q_chal` claim.

The exact remaining object is now semantic/contractual:

```text
V-CYCLE119-AUTHORITY-PINNED-STRICT263-ROW-EVENT-QCHAL-MASS-RECEIPT
```

It has to say whether the official source accepts this row/predicate/radius and how the challenge-to-line map, duplicate policy, quotient/charge policy, and final retained event mass are counted. The qchal checker currently returns:

```text
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

It also verifies that direct uniform K-sampling or a balanced projection onto K would retain the density, while identity scalar extension to a proper larger line field kills it.

So my current classification is:

```text
PROOF / BANKABLE_LEMMA at finite-source LD_sw level
EXACT_NEW_WALL at official row-event-qchal contract level
```

