# ROLE 03 - Separator Existence / Root Count

Your job is to prove or kill the generic separator existence theorem.

Target statement:

There exists a separator `y` in a controlled extension of the Cycle84 base
field such that

```text
mu_proj(y) <= 8
```

or ideally `mu_proj(y)=1`.

Required tasks:

1. Formalize the projective collision condition

```text
P_T(y) / P_T'(y) in F0^x
```

for distinct supports.
2. Bound the number of bad `y` by a rigorous polynomial root count.
3. Use the correct ambient field size. Do not confuse `F0`, `F_17^48`,
   `q_gen`, `q_line`, or `q_chal`.
4. Account for zero values, poles, same products, and affine normalization.
5. Decide whether a cubic extension candidate such as `F0[U]/(U^3-beta)` is
   enough, or whether the proof only works in the full `F_17^48`.
6. If the proposed root-count theorem is false, give the counterexample
   mechanism.

The best possible output is a theorem that turns the separator search into a
small finite exclusion certificate.

