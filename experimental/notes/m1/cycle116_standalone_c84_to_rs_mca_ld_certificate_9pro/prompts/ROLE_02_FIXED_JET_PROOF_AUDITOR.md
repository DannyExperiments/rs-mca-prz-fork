# Role 02: Fixed-Jet Locator Proof Auditor

Use the common prompt. No Internet.

Your job is to prove or break the abstract fixed-jet theorem.

Given `D subset F`, `beta notin D`, `P_J(X)=prod_{a in J}(X-a)`, common leading `sigma`-jet, `k=n-j-sigma`, and `C=RS[F,D,k]`, prove or refute:

```text
z_J = alpha + lambda/P_J(beta)
```

are support-wise MCA-bad slopes on one affine line `f+zg` with witness supports `D\\J`.

You must explicitly give:

- the parity-check or residue-line construction of `f,g`;
- the explaining codeword for each `J`;
- the root-count/Vandermonde noncontainment proof;
- why one common affine/reciprocal normalization is injective;
- exact agreement size and radius.

If the theorem is false, give a counterexample or the first invalid proof line.
