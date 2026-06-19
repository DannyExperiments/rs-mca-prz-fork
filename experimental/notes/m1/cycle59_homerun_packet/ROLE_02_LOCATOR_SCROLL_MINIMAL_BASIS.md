# ROLE 02 - Locator Scroll / Kronecker Minimal-Basis Route

Use the locator-scroll formulation from Cycle 58 and try to turn it into a proof.

Balanced residue setup:

```text
a=k+t,   j=n-a,
p_z = Lambda_{T_z},   deg p_z = j.
```

Successful locators satisfy a pencil equation

```text
C_w(p_z) = z D_B(p_z),
```

or equivalently lie on the determinantal rank-one scroll of the matrix

```text
( C_w(p), D_B(p) ).
```

Cycle 58 banked that a cloud larger than `j+1` forces an `E`-resonant locator circuit:

```text
sum_i c_i p_i = 0,
sum_i c_i z_i p_i = E H != 0.
```

Goal: prove that, after quotienting the common kernel and excluding quotient/action-rank templates, many divisor locators on the pencil must either:

1. lie on a low-degree polynomial section `Pi(Z,X)` with `deg_Z Pi <= t+o(t)`, so the root-budget lemma gives the calibrated bound; or
2. synchronize into a fixed tangent/common-envelope packet; or
3. produce quotient-action-rank compression.

Work out the Kronecker/minimal-basis algebra explicitly. If the route fails, give a precise counterexample to the extraction step.

