# Cycle 95 Prompt: Anchored Per-Fiber Collision, T=1

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

Cycle94 returned to the upper side and banked:

```text
L-CYCLE94-ANCHORED-SECANT-INTERSECTION
```

For a degree-`t` residue datum `(E,B,w)` with `B != 0`, if distinct slopes
`z != z'` have bad witnesses with maximal supports `S_z`, `S_z'`, then:

```text
|S_z cap S_z'| <= k + t - 1.
```

This is an elementary degree-count lemma. It is official-upper-side relevant,
but it does not prove the arbitrary-anchor residue-cloud theorem. Cycle94 also
cuts the pairwise/secant-only route: constant-weight families with this
intersection bound can still be exponentially large.

The open upper wall remains:

```text
W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
```

The smallest named atom is now:

```text
L-CYCLE95-ANCHORED-PERFIBER-COLLISION-T1
```

## Target

Work in the minimal arbitrary-anchor residue case:

```text
t = 1
E = X - alpha
B = 1
w arbitrary
line: y_z(x) = w(x)/(x-alpha) - z/(x-alpha)
```

Assume a smooth generated-field multiplicative domain `H` of order `n`, an RS
code of dimension `k = rho n`, reserve `sigma >= C n/log n`, and corrected
reserve above the entropy threshold with quotient-periodic exceptions charged.

Prove or kill:

```text
For non-quotient / aperiodic data, the number of distinct slopes z admitting a
noncontained exact (k+sigma)-agreement witness is n^{O(1)}.
```

If the exact statement above is too strong, find the sharpest source-valid
replacement. If it is false, give a source-valid counterpacket mechanism:

```text
t=1 arbitrary anchor w
smooth generated-field domain
noncontained witnesses
stable super-polynomial or exponential bad-slope cloud
not explained by quotient periodicity
```

## Required Tasks

1. Read the normal-form definitions and Cycle94 audit.
2. State the exact `t=1` theorem in source-valid notation.
3. Decide whether the inhomogeneous arbitrary anchor can be removed, normalized,
   or charged.
4. Try to prove the `t=1` bound directly.
5. If direct proof fails, reduce it to the smallest exact finite local-limit,
   norm-sieve, or collision-count statement.
6. If the route is false, construct or outline a checkable counterpacket.

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
experimental/notes/m1/m1_cycle94_upper_wall_return_audit.md
experimental/notes/m1/cycle94_upper_wall_return_raw/response.md
experimental/scripts/cycle94_anchored_secant_toy_check.py
```

## Required Output Format

Start with one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. Exact theorem/counterpacket/route cut.
3. Proof or obstruction.
4. Verification requirements.
5. Next exact lemma or construction.

Do not return another lower-side quotient-floor construction. This is an upper
side arbitrary-anchor prompt.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---