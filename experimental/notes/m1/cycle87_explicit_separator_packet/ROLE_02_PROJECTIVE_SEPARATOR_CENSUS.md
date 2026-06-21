# ROLE 02 - Projective Separator Census

Your job is to turn

```text
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

into a replayable exact checker.

Required tasks:

1. Define the field model for `F0 = F_17[X]/(X^16+X^8+3)` and the extension
   field used for the separator `y`.
2. Define exactly how to compute every `P_T(y)` for `T in P0`.
3. Define equality in `L^x / F0^x` without ambiguity.
4. Give a no-false-negative algorithm for computing

```text
mu_proj(y) =
  max_kappa #{ T in P0 : [P_T(y)] = kappa }.
```

5. Give memory/runtime estimates and certificate schema.
6. State exactly what output proves `mu_proj(y) <= 8`.
7. State exactly what output kills the route, including how to emit a
   high-multiplicity class.

You may propose code, pseudocode, or a deterministic sharding/replay protocol,
but it must be exact. Probabilistic hashing without exact replay is not a
proof.

