# Current Cycle105 Brief

Cycle105 is complete and audited as:

```text
BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Banked reduction:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s,
M_s = {((-1)^l e_l(Sbar))_{l=1}^{sigma+1}: Sbar subset mu_n, |Sbar|=s}.
```

All bandwidths share one fixed rational curve:

```text
Gamma = {(g_1(theta),...,g_{sigma+1}(theta)): theta in F_p}.
```

Thus `k` only changes the subset-size layer `M_s`; the `binom(n,k)` factor from
Cycle104 is a union-bound artifact.

Banked duality:

```text
M_s ~= M_{n-s}
```

through a fixed triangular complement automorphism induced by
`g_Sbar g_{H\Sbar} = 1 - X^n`.

Route cut:

The prize reserve lies beyond the Johnson radius. Generic RS list-size,
characteristic-free, and unconditional divided-difference routes cannot prove
the uniform bound. Any proof must use the above-reserve aperiodicity of `Uhat`.

Current target:

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill:

```text
For aperiodic Uhat above corrected reserve and every s,
|Gamma cap M_s| <= n^{O(1)}
```

with exponent independent of `s` and `k`.
