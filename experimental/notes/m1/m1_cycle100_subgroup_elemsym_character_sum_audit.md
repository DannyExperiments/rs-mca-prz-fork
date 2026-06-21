# Cycle 100 Subgroup Elemsym Character Sum Audit

## Verdict

**BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle100 does **not** prove the nonzero-frequency cancellation bound and does
not produce an aperiodic counterpacket. It banks a route correction: the
character-sum target counts the **fiber-weighted** number of active pairs,
while the prize numerator counts **distinct external roots**.

## Bankable Content

Let:

```text
F(theta) = #{S subset H, |S|=s : p_j(S)=P_j-theta^j for j<=sigma+1}
N = sum_{theta notin H} F(theta)
Theta_U = {theta : F(theta)>0}.
```

Cycle100 records the exact identity:

```text
Sigma = p^(sigma+1)(N - main),
main = binom(n,s)(p-n)/p^(sigma+1).
```

Thus the proposed character-sum bound is equivalent to `N <= n^{O(1)}`.
But:

```text
N <= n^{O(1)}
<=> |Theta_U| <= n^{O(1)} and F_max <= n^{O(1)},
F_max = max_theta F(theta).
```

The prize-relevant target is `|Theta_U|`, not the weighted pair count `N`.
Therefore the literal Cycle100 character-sum wall is stronger than needed and
can fail through a large fiber even if the distinct-root numerator remains
small.

Cycle100 also banks the PTE min-distance observation:

```text
S1 != S2 in one fiber => |S1 triangle S2| >= 2(sigma+2).
```

This gives a polynomial cap for disjoint-swap generated fibers when
`sigma >= C n/log n`, but does not prove the overlapping-pattern case.

## Route Cut

Do not keep trying to prove the weighted character-sum bound as the primary
route. It smuggles in the auxiliary multiplicity theorem `F_max <= poly`.

The main wall should return to the distinct-point reciprocal affine-line
incidence:

```text
|Theta_U| = | line cap E_m |_distinct <= n^{O(1)}.
```

Then treat `F_max <= n^{O(1)}` as a separate subgroup PTE-multiplicity lemma.

## Local Verification

Codex added and ran:

```text
experimental/scripts/cycle100_support_fiber_split_check.py
```

The checker computes active external-root fibers directly for small prime
fields, including constructed nonempty cases, and verifies:

```text
N = sum_theta F(theta)
support = #{theta : F(theta)>0}
F_max = max_theta F(theta)
max(support,F_max) <= N <= support * F_max
```

It also checks the PTE min-distance lower bound on nontrivial fibers.

Run result:

```text
cycle100 support-fiber split check
cases_checked: 26
total_support: 14
total_N: 15
max_F_max: 2
PASS
```

## What Is Not Proved

- No proof of the distinct-root incidence bound.
- No proof of the full `F_max <= n^{O(1)}` overlapping-PTE multiplicity bound.
- No official prize theorem.
- No aperiodic superpolynomial-error counterpacket.

## Next Exact Wall

The next prompt should attack the actual distinct-root target:

```text
L-CYCLE101-DISTINCT-LINE-INCIDENCE-OR-PTE-FIBER-SPLIT
```

It should prove or kill one of:

```text
L2: |Theta_U| = |line cap E_m|_distinct <= n^{O(1)}
L1: F_max <= n^{O(1)} for subgroup PTE fibers after periodic charging
```

Priority is `L2`, because it is the prize numerator. `L1` is a secondary
multiplicity control needed only if the weighted character-sum route is used.

