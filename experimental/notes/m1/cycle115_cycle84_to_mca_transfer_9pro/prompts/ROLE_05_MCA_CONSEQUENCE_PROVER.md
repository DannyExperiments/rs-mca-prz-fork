# Role 05: MCA Consequence Prover

Use the common prompt. No Internet.

Your role is to prove the MCA consequence, not just the finite slope count.

Starting from any slope set produced by Cycle84/Cycle85/Cycle88/Cycle89, prove or refute that each counted slope is support-wise MCA-bad under `def:mca` in `slackMCA_v3.tex` or the no-slack support-wise definition in `RS_disproof_v3.tex`.

You must explicitly handle:

- existence of a support `S` of the correct size;
- `u_z=f+zg` agrees with a codeword on `S`;
- no pair of codewords explains `f|_S` and `g|_S` simultaneously;
- whether `|S|>k` or another condition makes noncontainment automatic;
- how the Cycle84 color shell enforces the support size or residue datum;
- how the radius `delta` is computed;
- whether the final statement is MCA, CA, support-wise line-MCA, or something weaker.

If the MCA implication is valid only through `def:residue` and `thm:normalform`, state that theorem exactly. If it is invalid, give the first MCA-definition condition that is not proved.

End with an exact numerator and denominator:

```text
epsilon_mca >= numerator / q_line
```

or explain why this fraction cannot be asserted.
