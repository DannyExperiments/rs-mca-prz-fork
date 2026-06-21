# Cycle 102 - Padé / Uncertainty Line-Incidence Wall

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solution? If yes, what is the next exact lemma or
construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Read First

Read the project source files first, especially:

```text
CURRENT_CYCLE101_BRIEF.md
BANKED_LEMMAS.md
ACTIVE_WALLS.md
CUTS_AND_FALSE_ROUTES.md
ROUTE_BOARD_CURRENT.md
current_repo_snapshot/experimental/notes/m1/m1_cycle101_distinct_line_incidence_pte_split_audit.md
current_repo_snapshot/experimental/notes/m1/cycle101_distinct_line_incidence_pte_split_raw/response.md
current_repo_snapshot/experimental/notes/m1/m1_cycle100_subgroup_elemsym_character_sum_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle99_b1_aperiodic_moment_curve_incidence_audit.md
```

Cycle101's response is truncated in section 6. Treat the complete parts as
usable, but do **not** rely on the unfinished BKR/counterpacket paragraph.

## Current State

We are attacking the corrected upper-side, bandwidth-1 external-root wall after
quotient-periodic branches are charged.

Let:

```text
p prime, n | p-1, H = mu_n <= F_p^*
U monic, deg U = s+1
s = k + sigma
m = n-s
P_j = first sigma+1 power-sum prefix attached to U
Theta_U = {theta in F_p \ H : theta is an active external root}
```

The banked equivalences are:

```text
theta active
<=> exists S subset H, |S|=s :
    p_j(S)=P_j-theta^j for j=1,...,sigma+1

<=> exists S' subset H, |S'|=m :
    p_j(S')=theta^j-P_j for j=1,...,sigma+1

<=> exists S' subset H, |S'|=m :
    g_{S'} ≡ (1-theta X) W mod X^{sigma+2},
    W = U_tilde^{-1}
```

Equivalently, with indicator `c:H->{0,1}` for `S'`:

```text
chat(0)=m
chat(j)=sum_{x in H} c(x)x^j = theta^j-P_j, j=1,...,sigma+1.
```

The prize-relevant numerator is **distinct support**:

```text
|Theta_U| = #{theta : F(theta)>0},
```

not the weighted count:

```text
N = sum_theta F(theta).
```

Do not replace `|Theta_U|` by `N` unless you also prove a separate
`F_max <= n^{O(1)}` multiplicity theorem.

## Target

Attack:

```text
L-CYCLE102-PADE-UNCERTAINTY-LINE-INCIDENCE
```

Primary desired theorem:

```text
|Theta_U| = |ell cap E_m|_distinct <= n^{O(1)}
```

above corrected reserve, for aperiodic prefixes after quotient-periodic
charging.

Here:

```text
ell = { ((-1)^i(W_i - theta W_{i-1}))_{i=1}^{sigma+1}
        : theta in F_p }

E_m = { ((-1)^i e_i(S'))_{i=1}^{sigma+1}
        : S' subset H, |S'|=m }.
```

## First Critical Implication To Verify Or Kill

Cycle101 suggested a Padé/Berlekamp-Massey lane:

For the length-`sigma+1` window

```text
a_j(theta)=theta^j-P_j, j=1,...,sigma+1,
```

construct a minimal recurrence / Padé denominator `Q_theta`.

Potential implication:

```text
theta active
=> Q_theta is compatible with a divisor of X^n-1
```

or more strongly:

```text
Q_theta | X^n-1
```

after the correct normalization / enough-window hypothesis.

Your first job is to decide whether this implication is actually true as
stated. If it is false, produce the corrected exact implication or a concrete
finite counterpacket. Do not build on a false Padé divisor premise.

## Acceptable Outputs

Return one of:

```text
PROOF
```

with a theorem-grade proof of `|ell cap E_m|_distinct <= n^{O(1)}` or a
smaller theorem that directly implies it;

```text
COUNTERPACKET
```

with a source-valid aperiodic family where `|Theta_U|` is superpolynomial
above corrected reserve, or a finite falsifier to the claimed Padé implication;

```text
BANKABLE_LEMMA
```

with a source-valid corrected Padé/uncertainty lemma that materially advances
the exact wall;

```text
ROUTE_CUT
```

if a proposed lane is false or too strong, with the exact reason and the next
smaller wall;

```text
EXACT_NEW_WALL
```

only if you name the first missing theorem precisely enough for the next worker
to attack.

## Strong Constraints

- Preserve the distinction between `|Theta_U|` and `N=sum_theta F(theta)`.
- Do not prove only a min-distance/packing bound; Cycle101 cut that route.
- Do not use generic RS agreement/list-decoding below Johnson as a substitute
  for the line-incidence bound.
- Separate quotient-periodic branches from the aperiodic core.
- If using finite checks, state exactly what they verify and what theorem they
  do not prove.
- If using uncertainty principles, state the exact finite-field support and
  Fourier-window hypothesis.
- If using Padé/linear complexity, state the exact window length needed, the
  normalization, and whether the conclusion is `Q_theta | X^n-1`, extension to
  a divisor, or only a weaker recurrence compatibility condition.
