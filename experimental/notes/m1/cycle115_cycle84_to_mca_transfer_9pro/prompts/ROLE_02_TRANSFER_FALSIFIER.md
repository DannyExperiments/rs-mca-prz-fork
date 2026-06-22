# Role 02: Transfer Falsifier / Counterexample Hunter

Use the common prompt. No Internet.

Your role is adversarial. Try to break every proposed transfer from Cycle84 to RS-MCA / list / line-decoding.

Assume someone claims:

```text
Cycle84 m_max(beta)=2
therefore a paper-facing or prize-facing RS-MCA/list/line-decoding lower-bound row follows.
```

Find the first false implication or missing hypothesis. Be precise enough that the theorem can be repaired or abandoned.

Attack surfaces:

- finite color shell may not equal official support-wise MCA bad-slope set;
- product values may map to slopes only after a normalization that is not injective;
- one-copy `F_17^16` may not meet the `2^-128` denominator target;
- two-copy `F_17^48` may use independence, product, projective smoothing, or kernel-lift hypotheses not proved by Cycle84;
- arbitrary finite row may not be a smooth multiplicative RS subgroup/coset row;
- GRS diagonal equivalence may fail for the exact MCA/list/line-decoding object;
- quotient/periodic/contained/same-slope/tangent/endpoint/affine-color reductions may collapse the numerator below threshold;
- `q_chal` may be used as a denominator where only `q_line` is legitimate.

If you can build a clean counterexample to a natural transfer theorem, output `COUNTERPACKET` or `ROUTE_CUT` and state the false theorem exactly. If the transfer can be repaired, state the minimal additional hypothesis needed.

Your deliverable should be a theorem-quality "do not overclaim" audit, not general skepticism.
