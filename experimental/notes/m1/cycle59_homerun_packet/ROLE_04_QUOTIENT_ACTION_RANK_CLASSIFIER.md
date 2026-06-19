# ROLE 04 - Quotient-Action-Rank Template Classifier

Classify the quotient/action-rank exceptions correctly.

The old exclusion

```text
E(X)=E_0(X^M)
```

is too narrow. The invariant should involve

```text
d_M(E) = deg minpoly( [X^M] mod E ).
```

Cycle 58 found that quotient-component and fixed-defect quotient-anchor packets can beat naive upper bounds while not being literal pullbacks.

Goal: produce a theorem-level template classification:

1. Define quotient-action-rank packets in a way invariant under equivalent residue data and denominator reductions.
2. Prove that each template contributes at most the proposed quotient profile term, or show that the full profile `2^{Q_H(eta)}` is necessary.
3. Give exact finite bounds for fixed-defect packets:

```text
S_A = T union pi_M^{-1}(A)
```

including slope distinctness and noncontainment.
4. State the quotient-clean version of the MCA upper theorem after these packets are subtracted.

If the canonical `beta(rho)/H_2(rho)` quotient exponent is false for arbitrary anchors, say so and prove the replacement.

