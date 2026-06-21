# Cycle 101 Prompt: Distinct Line Incidence Or PTE Fiber Split

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. Do you see a route to a full solve? If yes, what is the next
exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Current State

Cycle98 banked the active external-root moment-curve incidence normal form.

Cycle99 banked divisor/remainder, reciprocal affine-line, and character-sum
forms.

Cycle100 cut the weighted character-sum route as the primary target:

```text
N = sum_theta F(theta)
```

is fiber-weighted, while the prize-relevant numerator is:

```text
|Theta_U| = #{theta : F(theta)>0}.
```

The character-sum bound `N <= poly` requires both:

```text
L2: |Theta_U| <= n^{O(1)}
L1: F_max <= n^{O(1)}.
```

The real priority is `L2`, the distinct external-root line incidence. `L1` is
secondary multiplicity control for the weighted route.

## Target

Attack:

```text
L-CYCLE101-DISTINCT-LINE-INCIDENCE-OR-PTE-FIBER-SPLIT
```

Using the reciprocal affine-line form:

```text
g_{S'}(X) = prod_{x in S'}(1-xX),
g_{S'}(X) == (1-theta X) W(X) mod X^(sigma+2),
|S'| = m = n-s.
```

Prove or kill the distinct-point bound:

```text
|{theta in F_p \ H : exists S' with g_{S'} == (1-theta X)W mod X^(sigma+2)}|
  <= n^{O(1)}
```

after quotient-periodic branches are charged.

If you cannot prove `L2`, attack the secondary multiplicity wall:

```text
F_max <= n^{O(1)}
```

for subgroup PTE fibers, including overlapping patterns. Cycle100 already
proved the disjoint-swap/generated case only.

## What A Successful Answer Must Do

One of:

1. **PROOF:** Prove the distinct-root line-incidence bound `L2`.
2. **COUNTERPACKET:** Construct a nonperiodic family with superpolynomially
   many distinct external `theta` values.
3. **BANKABLE_LEMMA:** Prove a smaller exact lemma, preferably an overlapping
   subgroup-PTE multiplicity theorem or a line-incidence transversality theorem
   for the elementary-symmetric image.
4. **ROUTE_CUT:** Show that this distinct-line route cannot work and give the
   next viable exact object.

## Required Precision

- Do not replace distinct `theta` count with weighted `N` unless you also prove
  `F_max <= poly`.
- Separate quotient-periodic/core branches from aperiodic residuals.
- If using PTE relations, state whether patterns are disjoint or overlapping.
- If using coding/list-decoding language, address the below-Johnson obstruction
  from Cycle99.
- If using characters, explain how the support indicator is handled without
  silently reverting to `N`.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-31-30-770Z-cycle101-distinct-line-incidence-pte-split-fba7d85d/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---