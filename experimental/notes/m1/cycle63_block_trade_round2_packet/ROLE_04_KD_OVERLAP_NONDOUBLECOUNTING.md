# ROLE 04 - `(K,D)` Overlap And Non-Double-Counting

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-MODEL-GJ-KD-OVERLAP-NONDOUBLECOUNTING
```

## Objective

Assume a candidate maximal `(K,D)` assignment exists. Prove or kill the finite
overlap/non-double-counting theorem needed to sum block-trade charges.

Given two descriptions

```text
D1 union union S1/K1,
D2 union union S2/K2,
```

bound the intersection of their support families unless they share a common
coarsening/color structure that should be charged once.

## Required Output

Give an exact finite inequality. Avoid asymptotic language.

You may use:

- subgroup lattice of dyadic `H`;
- defect-size bookkeeping;
- block-incidence bipartite graphs;
- common-left-composite/common-color closure;
- entropy of quotient support families.

## Success Criteria

Output `BANKABLE_LEMMA` if you prove a usable finite overlap theorem.

## Failure Criteria

Output `COUNTERPACKET` if overlapping `(K,D)` profiles can exceed the proposed
charge by more than any finite residual compatible with prize thresholds.

