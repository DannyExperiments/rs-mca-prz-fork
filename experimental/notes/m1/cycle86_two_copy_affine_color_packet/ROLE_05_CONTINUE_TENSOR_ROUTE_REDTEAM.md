# ROLE 05 CONTINUATION: Red-Team Additive Separation Against Your Tensor Cut

Continue from your Cycle85 Role05 answer.

You cut naive tensor/block amplification because it creates separate colors,
non-`t=1` structure, or product collapse. Now test whether the proposed
additive-color construction escapes that cut.

Target:

```text
z(T1,T2) = rho_beta(T1) + alpha rho_beta(T2),
alpha in F_17^48 \ F_17^16.
```

Required analysis:

1. Does additive `F0`-linear separation fit the Role05 `Delta^+` color
   formalism?
2. Can two blocks be glued into one degree-`j` locator family with one support
   modulus?
3. Does the construction remain `t=1`, or does it inevitably become `t=2` or
   a higher denominator object?
4. Does a canonical RS/GRS realization exist after rate normalization?
5. If not, give the exact obstruction.
6. If yes, state the precise lemma that proves it escapes your tensor route cut.

Return a hard `ROUTE_CUT` if additive separation fails for the same reason as
ordinary tensoring. Return `BANKABLE_LEMMA` only if the escape is exact.
