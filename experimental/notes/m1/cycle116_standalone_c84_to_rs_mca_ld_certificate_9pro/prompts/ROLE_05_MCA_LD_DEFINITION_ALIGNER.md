# Role 05: MCA / LD_sw Definition Aligner

Use the common prompt. No Internet.

Your job is to align the theorem with the manuscript definitions.

Read `slackMCA_v3.tex`, `RS_disproof_v3.tex`, and `m2_line_decoding_mca_bridge.md`. Decide whether the proposed theorem proves:

```text
support-wise MCA bad-slope lower bound
LD_sw lower bound
line-decoding lower bound in the source's official sense
ordinary list-decoding lower bound
```

Be ruthless about definitions. The likely correct answer is MCA/`LD_sw`, not ordinary list decoding. But verify it.

Deliverable:

- exact definition of `LD_sw(C,A)` used;
- exact identity or implication relating it to `epsilon_mca(C,delta)`;
- exact radius/agreement rounding;
- paragraph of non-overclaim language for the standalone certificate.
