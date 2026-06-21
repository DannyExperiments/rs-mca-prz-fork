# Role 07: Finite Stress Checker / Counterexample Search Spec

Your role is computational-theorem engineering. Design a bounded finite stress
checker that can either find a real aperiodic counterpacket pattern or provide
evidence for the next exact theorem.

Do not propose another enormous brute force. Use the k-free collapse:

```text
theta active <=> Gamma(theta) in M_s
```

and exploit:

```text
M_s = elementary-symmetric prefixes of s-subsets of mu_n.
```

Deliverables:

1. Exact input parameters: prime `p`, subgroup order `n`, reserve `sigma`,
   subset layer `s`, and Uhat model.
2. Exact aperiodicity predicate to test.
3. Exact output certificate:
   - `PASS_NO_SUPERPOLY_PATTERN_IN_WINDOW`, or
   - `COUNTERPACKET_CANDIDATE` with all theta values and subsets, or
   - `ROUTE_CUT_FINITE_MODEL_TOO_WEAK`.
4. Pseudocode precise enough for Codex to implement.
5. Explanation of what a finite hit would and would not prove.

Best outcome: identify a small finite falsifier or a replayable checker that
tests the exact periodic/aperiodic obstruction named by the proof roles.

Return `COUNTERPACKET`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `AUDIT`, or `PLAN`.

