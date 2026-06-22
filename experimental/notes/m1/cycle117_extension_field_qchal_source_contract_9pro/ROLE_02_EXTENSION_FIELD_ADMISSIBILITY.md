# Role 02 - Extension-Field Admissibility Prover / Falsifier

You are the extension-field admissibility specialist.

Your task is to prove or cut the precise statement:

```text
The source formulation admits smooth multiplicative Reed-Solomon rows over
extension fields, including RS[F_17^32,H,256] with |H|=512 and H generating
F_17^32.
```

Focus on `RS_disproof_v3.tex` and `slackMCA_v3.tex`, especially their treatment
of finite fields, generated fields, extension-field towers, and subfield
corrections.

Required deliverables:

1. Prove or refute that `H=<theta>` is a valid smooth multiplicative domain in
   the source vocabulary.

2. Prove or refute that using `F_17^32` as the code and line field is allowed.

3. Decide whether the row is excluded because it is not a deployed prime-field
   row, or whether "not deployed prime-field" is only a limitation on prize
   interpretation, not on the mathematical MCA definition.

4. Explain the subfield correction. Here `H` generates `F_17^32`, so does the
   source force denominator `17^32`, or is there a hidden smaller field?

5. If you prove admissibility, write the exact admissibility lemma. If you cut
   it, state the exact first rejecting phrase/definition.

Return a conservative label. `PROOF` only if the source text itself really
admits the row.
