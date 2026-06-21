# ROLE 06 CONTINUATION: Build The Two-Copy Syndrome Line

Continue from your Cycle85 Role06 answer.

You gave a direct reciprocal-slope syndrome gauge for the one-copy packet.
Now build or kill the two-copy version in syndrome coordinates.

Required output:

1. Start from your one-copy parity-check/syndrome construction.
2. Define two embedded/disjoint copies over `F_17^48`.
3. Construct one combined parity-check system for one RS/GRS code.
4. Construct one affine syndrome line `u + z v`.
5. Prove the witnessed slopes have the form
   ```text
   z = z1 + alpha z2
   ```
   or another explicitly injective two-copy formula.
6. Prove every pair of one-copy supports gives one exact support of the
   required size.
7. Prove transversality.
8. State final `(n,k,sigma,j,q_line,T_line)` and compare to `2^-128`.

If the syndrome construction cannot be made one-line, return `ROUTE_CUT` with
the first exact linear-algebra obstruction.
