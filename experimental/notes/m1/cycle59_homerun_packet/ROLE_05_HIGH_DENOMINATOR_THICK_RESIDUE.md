# ROLE 05 - High-Denominator `t > sigma` Thick-Residue Branch

Focus on the part that balanced proofs miss.

For `a=k+sigma` and denominator degree `t>sigma`, every witness polynomial agreeing on an `a`-set `S` has the form

```text
Q = I_S(w) + L_S H,   deg H < t-sigma.
```

The slope condition is an affine-plane incidence:

```text
z[B]_E in [I_S(w)]_E + [L_S F[X]_{<t-sigma}]_E.
```

Noncontainment is equivalent to

```text
[B]_E notin [L_S F[X]_{<t-sigma}]_E.
```

Goal: either prove a high-cloud denominator-compression theorem or kill it with a counterpacket.

Desired theorem:

```text
t > sigma and many noncontained slopes
=> equivalent datum of degree <= sigma
   OR quotient/action-rank packet
   OR tangent/common-envelope packet
   OR occupancy/main-term-only packet.
```

If false, construct an overbalanced packet that survives syndrome-space calibration and quotient charging. If true only in syndrome language, state the exact syndrome theorem and prove why residue-degree `t` should be ignored.

