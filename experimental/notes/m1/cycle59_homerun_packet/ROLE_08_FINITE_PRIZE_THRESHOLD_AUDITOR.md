# ROLE 08 - Finite Prize Threshold Auditor

Do not try to prove the whole inverse theorem. Instead, make the finite target exact.

Given the official rates

```text
rho in {1/2, 1/4, 1/8, 1/16}
epsilon* = 2^-128
```

and a smooth-domain RS code `C=RS[F,L,k]`, determine what data are actually needed to certify

```text
epsilon_mca(C,delta) <= 2^-128
```

and

```text
|Lambda(C^{=m},delta)| <= 2^-128 |F|.
```

Build the finite ledger:

```text
N_total =
  occupancy/main term
  + tangent/common-envelope
  + quotient/action-rank profile
  + residual actual-list term
  + high-denominator affine-plane term
  + aperiodic transverse-secant term.
```

Then safety is:

```text
N_total <= |F| / 2^128.
```

Output:

1. A theorem statement with exact finite hypotheses.
2. The asymptotic entropy-only candidate as a corollary, not as the main theorem.
3. A list of constants/terms still unproved.
4. The exact finite checker inputs PRZ would need.

If a rate-only `delta_C^*` formula is impossible, state the strongest correct finite alternative.

