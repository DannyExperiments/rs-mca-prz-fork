# Cycle106 Common Prompt

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. Use max reasoning. Do not browse the Internet.

Do you see a route to a full solution? If yes, give the exact next lemma,
construction, checker, or counterpacket mechanism.

You are working inside the RS-MCA / Proximity Prize M1 upper-side route. Read
the uploaded context first, especially:

```text
context/CURRENT_CYCLE106_BRIEF.md
context/CURRENT_CYCLE105_BRIEF.md
context/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md
context/m1_cycle106_kfree_aperiodic_moment_curve_incidence_audit.md
context/cycle106_kfree_aperiodic_moment_curve_incidence_prompt.md
context/cycle105_kfree_collapse_check.py
context/ROUTE_BOARD_CURRENT.md
context/ACTIVE_WALLS.md
context/BANKED_LEMMAS.md
context/CUTS_AND_FALSE_ROUTES.md
```

Important: the previous Cycle106 Fable run failed at the harness layer. It is
not a mathematical answer. Do not use it as evidence.

## Banked State

Cycle103 proved the bandwidth-1 upper-side numerator bound.

Cycle104 proved, for fixed bandwidth `k`:

```text
|Theta_U| <= binom(n,k)(sigma+1).
```

Cycle105 banks the k-free collapse. Let `s=sigma+k`, `H=mu_n`, and

```text
G(theta,X)=sum_{l=0}^{sigma+1} g_l(theta) X^l,
g_l(theta)=sum_{i=0}^l u_{l-i} theta^i.
```

For an `s`-subset `Sbar` of `H`, set:

```text
g_Sbar(X)=prod_{x in Sbar}(1-xX).
```

Then bandwidth-k activity is exactly:

```text
theta active
<=> exists Sbar subset H, |Sbar|=s, with
    g_Sbar(X) == G(theta,X) mod X^(sigma+2).
```

Equivalently:

```text
(g_1(theta),...,g_{sigma+1}(theta)) in M_s,
M_s = {((-1)^l e_l(Sbar))_{l=1}^{sigma+1}: Sbar subset H, |Sbar|=s}.
```

Thus all bandwidths share one fixed curve:

```text
Gamma = {(g_1(theta),...,g_{sigma+1}(theta)): theta in F_p},
```

and `k` only changes the subset-size layer `M_s`. Cycle105 also banks
triangular complement duality:

```text
M_s ~= M_{n-s}.
```

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

## Hard Constraints

- You must use the above-reserve aperiodicity hypothesis.
- Cycle105 cuts generic RS list-size, Johnson-radius, and unconditional
  divided-difference routes.
- Do not replace distinct support by a weighted count.
- Do not count periodic/coset-swap families as counterpackets unless they
  survive the above-reserve aperiodicity condition.
- Do not invoke q-ledger or `2^-128` frontier arithmetic; this is a
  single-field upper-side structural wall.
- Do not claim a prize-level result unless you explicitly verify every link
  from this wall back to the official Proximity Prize statement.

## Required Output Label

Begin with exactly one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Definitions:

```text
PROOF
```

A source-valid proof of the aperiodic incidence bound.

```text
COUNTERPACKET
```

A source-valid aperiodic growing-k family with superpolynomially many distinct
active theta values.

```text
BANKABLE_LEMMA
```

A strict proved reduction to a smaller named theorem, such as a k-independent
eliminant/subresultant/Wronskian statement or an exact
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

```text
AUDIT
```

A conservative source audit that identifies a precise missing hypothesis,
definition mismatch, or unsupported implication.

```text
PLAN
```

Only if no proof/counterpacket/reduction is achieved. The plan must name the
exact theorem/checker/counterpacket that would convert it into proof or
counterpacket.

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

