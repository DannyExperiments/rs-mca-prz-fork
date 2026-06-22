# Role 01 - Full Adapter Prover

Attempt a direct proof of:

```text
L-CYCLE108-OFFICIAL-RESIDUAL-SLOPE-PARTITION-INJECTIVE-NORMALIZATION-AND-AP-DESCENT
```

Your job is to build the complete theorem, not just a Gate B lemma. Start from
the official residual bad-slope object in the source files. Define the residual
slope partition exactly. For each branch, either give the charge already banked
in the context or construct the tagged endpoint-corrected complement-line
normalization.

You must prove injectivity of the source-slope-to-tagged-object map and bound
the number of tags by `n^O(1)` with exponent independent of `s` and `k`.

If you cannot prove the full theorem, return `EXACT_NEW_WALL` with the strongest
subtheorem you did prove and the first missing clause.
