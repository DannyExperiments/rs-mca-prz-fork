# Role 01: Gate A Source-Cover Formalizer

Your target is:

```text
L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER
```

Prove, repair, or precisely fail the official-source-to-AP_corr reduction.

You must formalize the exact chain:

```text
official M1 bad slope / above-corrected-reserve object
=> Uhat object
=> AP_corr(Uhat)
=> complement-line instance L_U(theta)
=> distinct active theta values counted by the official M1 numerator
```

Required work:

1. State the exact official source hypotheses needed.
2. Define `AP_corr(Uhat)` in source-valid terms, not just model language.
3. Prove the normalization into `Uhat` preserves numerator-relevant distinct
   theta values.
4. Identify how endpoint correction affects the source map.
5. State the first unsupported implication if you cannot prove it.

Do not work on Gate B except to state the output object Gate B receives.

Return `PROOF`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `AUDIT`, or `PLAN`.
