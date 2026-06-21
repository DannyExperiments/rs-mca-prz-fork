# Cycle 100 Prompt: Subgroup Elemsym Moment Character Sum

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

Cycle98 banked:

```text
L-CYCLE98-MOMENT-CURVE-INCIDENCE
```

Cycle99 banked three exact equivalent forms:

```text
theta active in F_p \ H
<=> exists f | X^n - 1, deg f = s, deg(U - (X-theta)f) < k
<=> reciprocal affine-line incidence against elementary-symmetric images
<=> exact additive-character count N = main + error.
```

Cycle99 also cuts the generic RS list-decoding route: the live reserve
`sigma = O(n/log n)` is below Johnson, so the proof must use subgroup
structure and aperiodicity.

Do not re-prove the Cycle98/Cycle99 equivalences unless you find a real error.

## Target

Attack:

```text
W-CYCLE100-SUBGROUP-ELEMSYM-MOMENT-CHARACTER-SUM
```

Let:

```text
L_t(X) = sum_{j=1}^{sigma+1} t_j X^j,
E_s(t) = e_s({ psi(L_t(x)) }_{x in H}),
S(t) = sum_{theta in F_p \ H} psi(L_t(theta)).
```

Prove or kill the aperiodic cancellation bound:

```text
| sum_{t != 0} psi(-<t,P>) E_s(t) S(t) |
    <= p^(sigma+1) n^{O(1)}
```

for aperiodic prefix `P`, after quotient-periodic resonances are charged.

This would imply the Cycle99 active external incidence bound because the
`t=0` main term is already at most `1` in the intended reserve scale.

## What A Successful Answer Must Do

One of:

1. **PROOF:** Give a theorem-grade cancellation bound for the above sum in the
   corrected reserve range.
2. **COUNTERPACKET:** Construct a nonperiodic prefix `P` for which the error
   term is superpolynomial, and explain how it survives quotient-periodic
   charging.
3. **BANKABLE_LEMMA:** Reduce the full sum to a strictly smaller named
   theorem, preferably starting with a single-frequency or low-rank pencil
   bound for `E_s(t)`.
4. **ROUTE_CUT:** Prove that this character-sum route cannot work and state
   the next viable exact object.

## Required Precision

- Separate resonant periodic frequency support from aperiodic prefixes.
- State exactly how quotient-periodic cores are charged.
- If using Weil/Gauss-sum estimates, identify whether they bound `S(t)`,
  `E_s(t)`, or only a single-frequency slice.
- If using Cauchy-Schwarz/energy, state the exact moment being bounded and
  why it is strong enough for a pointwise prefix `P`.
- If you cannot prove the full sum, give the next exact lemma: e.g.
  monomial `L_t=cX^j`, bounded-rank `L_t`, or major/minor arc split.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T13-10-38-559Z-cycle100-subgroup-elemsym-character-sum-e95a5f28/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---