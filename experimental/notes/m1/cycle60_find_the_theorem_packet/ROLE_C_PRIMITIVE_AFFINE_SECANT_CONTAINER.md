# ROLE C - Primitive Affine-Secant Container Theorem

Assume all split-rational quotient packets and tangent/common-envelope packets
have been canonically removed.

Find the primitive theorem:

```text
W-MCA-FINITE-CANONICAL-HEREDITARY-AFFINE-SECANT-CONTAINER
```

For every official same-field RS code and every affine syndrome line, prove a
finite bound of the form

```text
|Bad_primitive_sigma(ell)|
<= C_occ * binom(n,k+sigma)/q^{sigma-1} + P(n,sigma),
```

with explicit `C_occ` and `P`, not asymptotic handwaving.

Use the split-locator syzygy-excess criterion if helpful. A valid proof must be
maximum-over-lines, not random-anchor averaging.

If false, construct a quotient-free, envelope-free primitive packet with
positive syzygy excess beating the occupancy term.

