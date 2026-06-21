# Cycle 105 Prompt: Uniform Bandwidth Divisor Incidence

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solution? If yes, what is the next exact lemma or
construction?

## Context

You are working inside the RS-MCA / proximity-prize M1 upper-side route. Read
the current project source files first, especially:

```text
CURRENT_CYCLE104_BRIEF.md
current_repo_snapshot/experimental/notes/m1/m1_cycle104_bandwidth_k_divisor_incidence_audit.md
current_repo_snapshot/experimental/notes/m1/cycle104_bandwidth_k_divisor_incidence_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle105_uniform_bandwidth_divisor_incidence_prompt.md
```

Cycle103 proved the bandwidth-`1` bound:

```text
|Theta_U| <= (n-sigma+1)(sigma+1).
```

Cycle104 proved the fixed-bandwidth bound:

```text
|Theta_U| <= binom(n,k)(sigma+1)
```

for every fixed `k`, via the reverse co-locator and divided-difference
obstruction. This closes `k=2` and every fixed `k`, but it is not enough when
`k` grows with `n`.

## Target

Attack:

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE
```

For `s=sigma+k`, activity is:

```text
theta active
<=> exists psi in F_p[X], deg psi <= k-2, such that
    B_theta(X)+psi(X) is a degree-s divisor of X^n-1.
```

Equivalently, some degree-`k-2` polynomial agrees with `-B_theta` on an
`s`-subset of `mu_n`.

Prove or kill:

```text
|Theta_U| <= n^{O(1)}
```

with exponent independent of `k`, after quotient/periodic branches are charged.

## What Counts

Return one of:

```text
PROOF
```

A source-valid uniform-in-`k` proof.

```text
COUNTERPACKET
```

A source-valid aperiodic above-reserve family with growing `k` and
superpolynomially many distinct active theta values.

```text
BANKABLE_LEMMA
```

A strict, proved reduction to a smaller named theorem, such as a
`k`-independent subresultant/Wronskian/elimination certificate.

```text
ROUTE_CUT
```

A rigorous reason the uniform divisor-incidence route cannot prove the upper
bound, with the corrected replacement target.

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

