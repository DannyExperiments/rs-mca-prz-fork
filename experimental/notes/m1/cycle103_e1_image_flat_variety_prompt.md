# Cycle 103 Prompt: e1-Image On The Uhat-Flat Variety

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solution? If yes, what is the next exact lemma or
construction?

## Context

You are working inside the RS-MCA / proximity-prize M1 upper-side route. Read the
current project source files first, especially:

```text
CURRENT_CYCLE102_BRIEF.md
current_repo_snapshot/experimental/notes/m1/m1_cycle102_pade_uncertainty_line_incidence_audit.md
current_repo_snapshot/experimental/notes/m1/cycle102_pade_uncertainty_line_incidence_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle103_e1_image_flat_variety_prompt.md
```

Cycle102 killed the short-window Padé / Berlekamp-Massey divisor route. Do not
revive it. The false implication was:

```text
theta active
=> the short-window Padé/BM denominator of (theta^j-P_j)_{j=1}^{sigma+1}
   is compatible with a divisor of X^n - 1.
```

An explicit aperiodic falsifier exists over `F_29`, `n=7`, `sigma=3`, with
`S'={1,16,24}`, `theta=2`, window `(12,21,28,13)`, and short-window recurrence
polynomial `T^2 - 24T + 1`, irreducible over `F_29`.

The corrected identity is:

```text
g_{S'}(X) Uhat(X) == 1 - theta X  (mod X^{sigma+2}),
```

where `g_{S'}(X)=prod_{x in S'}(1-xX)` and `Uhat=W^{-1} mod X^{sigma+2}`.

Therefore, after the theta-free flatness constraints

```text
[X^i](g_{S'} Uhat)=0,  i=2,...,sigma+1,
```

theta is forced by a linear statistic:

```text
theta = -[X](g_{S'} Uhat) = e_1(S') - Uhat_1.
```

Thus the prize-relevant distinct numerator is exactly:

```text
|Theta_U| =
#{ distinct e_1(S') :
   S' subset mu_n, |S'| = m,
   [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

Do not replace this distinct-support problem by the weighted count
`N=sum_theta F(theta)`.

## Target

Attack:

```text
L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY
```

Let

```text
V = { S' subset mu_n :
      |S'| = m,
      [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

Prove or kill:

```text
|e_1(V)| <= n^{O(1)}
```

in the aperiodic corrected-reserve regime, after quotient/periodic branches are
charged.

## What Counts

Return one of:

```text
PROOF
```

A source-valid proof that the flatness constraints force
`|e_1(V)| <= n^{O(1)}`. A mere bound on `|V|` is not enough unless it is
actually polynomial in the live range.

```text
COUNTERPACKET
```

A source-valid aperiodic family above corrected reserve with superpolynomial
`|e_1(V)|`, including the precise construction and why it avoids periodic /
quotient charging.

```text
BANKABLE_LEMMA
```

A strict, proved reduction to a smaller named theorem, preferably a shifted
moment-curve uncertainty statement or a finite checker whose pass/fail would
decide the wall.

```text
ROUTE_CUT
```

A rigorous reason why this e1-image route cannot prove the needed bound, with
the corrected replacement target.

```text
EXACT_NEW_WALL
```

Only if you reduce the problem to a strictly smaller exact wall. Name it
explicitly and state the exact theorem/checker/counterpacket needed next.

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

