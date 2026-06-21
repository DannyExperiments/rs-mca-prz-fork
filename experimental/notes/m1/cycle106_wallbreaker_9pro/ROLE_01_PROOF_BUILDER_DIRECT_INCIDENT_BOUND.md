# Role 01: Proof Builder - Direct Incidence Bound

Your role is to try to prove the Cycle106 wall directly:

```text
For aperiodic Uhat above corrected reserve and every s,
|Gamma cap M_s| <= n^{O(1)}
```

with exponent independent of `s` and `k`.

Do not spend your answer restating the setup. Build an actual proof attempt.
You must consume the aperiodicity/above-reserve hypothesis in a visible way.

Preferred route:

1. Express `Gamma cap M_s` as equality between the prefix of `G(theta,X)` and
   the first `sigma+1` elementary symmetric coefficients of an `s`-subset of
   `mu_n`.
2. Use the above-reserve aperiodicity of `Uhat` to forbid long structured
   families of `Sbar` prefixes.
3. Prove a polynomial upper bound on the number of possible theta values.

If you cannot close the proof, isolate the first exact obstruction. Do not call
it a proof unless every quantifier over `s`, `k`, and aperiodic `Uhat` is
handled.

Return `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`, or `PLAN`.

