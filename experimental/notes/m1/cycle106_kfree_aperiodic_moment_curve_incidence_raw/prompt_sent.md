# Cycle 106 Prompt: k-Free Aperiodic Moment-Curve Incidence

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solution? If yes, what is the next exact lemma or
construction?

## Context

You are working inside the RS-MCA / proximity-prize M1 upper-side route. Read
the current project source files first, especially:

```text
CURRENT_CYCLE105_BRIEF.md
current_repo_snapshot/experimental/notes/m1/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md
current_repo_snapshot/experimental/notes/m1/cycle105_uniform_bandwidth_divisor_incidence_raw/response.md
current_repo_snapshot/experimental/scripts/cycle105_kfree_collapse_check.py
current_repo_snapshot/experimental/notes/m1/cycle106_kfree_aperiodic_moment_curve_incidence_prompt.md
```

Cycle105 banks the exact k-free collapse:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s,
M_s = {((-1)^l e_l(Sbar))_{l=1}^{sigma+1}: Sbar subset mu_n, |Sbar|=s}.
```

Thus all bandwidths share one fixed curve:

```text
Gamma = {(g_1(theta),...,g_{sigma+1}(theta)): theta in F_p},
```

and `k` only changes the subset-size layer `M_s`. Cycle105 also banks the
triangular complement duality `M_s ~= M_{n-s}`.

## Target

Attack:

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill:

```text
For aperiodic Uhat above corrected reserve and every s,
|Gamma cap M_s| <= n^{O(1)}
```

with exponent independent of `s` and `k`.

## Constraints

- You must use the aperiodicity/above-reserve hypothesis. Cycle105 cuts generic
  RS list-size, Johnson-radius, and unconditional divided-difference routes.
- Do not replace distinct support by a weighted count.
- Do not count periodic/coset-swap families as counterpackets unless they
  survive the above-reserve aperiodicity condition.
- Do not invoke q-ledger or `2^-128` frontier arithmetic; this is still a
  single-field upper-side structural wall.

## What Counts

Return one of:

```text
PROOF
```

A source-valid proof of the aperiodic incidence bound.

```text
COUNTERPACKET
```

A source-valid aperiodic growing-`k` family with superpolynomially many distinct
active `theta` values.

```text
BANKABLE_LEMMA
```

A strict proved reduction to a smaller named theorem, such as a
`k`-independent eliminant/subresultant/Wronskian statement or an exact
aperiodic-dephasing-to-distinct-support lemma.

```text
ROUTE_CUT
```

A rigorous reason this residual incidence route cannot prove the upper bound,
with the corrected replacement target.

```text
EXACT_NEW_WALL
```

Only if the wall is reduced to a strictly smaller exact theorem/checker.

## Self-Audit Required Before Finalizing

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---