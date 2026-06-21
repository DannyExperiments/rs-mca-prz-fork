# Cycle 90 Prompt: Prize-Family Embedding Or Cut

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. Do you see a route to a full solve? If yes, what is the next exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing hypothesis, or exact counterexample mechanism.

## Context

The currently banked chain is:

- Cycle84/Cycle85: exact finite product/occupancy certificate for the model.
- Cycle87: explicit separator/census certificate for a `[464,232]` GRS/RS row over `17^48`, with profile `(n,k,sigma,j,t)=(464,232,6,226,1)`.
- Cycle88: conditional bridge from the Cycle87 certificate to a finite MCA failure row.
- Cycle89: conditional official-definition bridge against `def:mca`, `def:residue`, and `thm:normalform`.

Cycle89's key conclusion:

```text
L-CYCLE89-OFFICIAL-MCA-ROW-IDENTIFICATION := BANKABLE_LEMMA / CONDITIONAL

Assuming the Cycle84/Cycle85/Cycle87 finite facts, the Cycle87 counted slopes
are genuine support-wise line-MCA bad slopes for the explicit finite row.

q_gen = q_code = q_line = q_chal = 17^48

#bad >= N*P/2
     = 1,391,152,917,379,006,070,784

floor(17^48 / 2^128)
     = 338,617,018,271,848,945,628

So the finite row clears the 2^-128 MCA numerator threshold by a large margin.
```

Cycle89's important caveat:

```text
This is an official-definition MCA row, but not yet an official prize
counterpacket. The row has n=464=2^4*29 and is a contrived finite GRS/RS row.
The prize-facing source language emphasizes smooth multiplicative domains,
especially power-of-two multiplicative subgroup RS codes.
```

## Target

Attack the exact wall:

```text
W-CYCLE90-PRIZE-FAMILY-EMBEDDING
```

Decide, source-validly, whether the Cycle87/Cycle89 row is already admissible for the official prize, or whether it is only a finite arbitrary-GRS/RS model row.

You must prove or kill at least one of the following:

### Branch A: Official Admissibility

Prove from the source definitions that the official prize formulation admits arbitrary finite RS/GRS rows, not only smooth power-of-two multiplicative subgroup rows. If this is true, state exactly which source lines permit it and whether diagonal GRS isometry is allowed.

If Branch A succeeds, the next remaining task is independent replay of the Cycle87 finite certificate.

### Branch B: Prize-Family Embedding

Exhibit a smooth power-of-two multiplicative subgroup domain

```text
D' <= F_q'^*
n' = 2^a
rate rho in {1/2,1/4,1/8,1/16}
```

and a degree-`t` residue-line datum over `RS[F_q',D',rho*n']` whose noncontained packing exceeds `floor(q'/2^128)`, by embedding, padding, shortening, inducing, quotienting, or otherwise porting the Cycle87 occupancy mechanism.

If you use padding/shortening/puncturing from `n=464` to a power-of-two domain, prove that:

- the code remains a Reed-Solomon code on a smooth multiplicative subgroup or allowed coset;
- support sizes and radius convert correctly;
- noncontainment survives;
- distinct slopes remain distinct over the correct `q_line`;
- the `2^-128` numerator comparison survives with the new field size.

### Branch C: Route Cut

If neither A nor B is valid, prove the route cut:

```text
Cycle87/Cycle89 is a source-valid finite arbitrary-RS/GRS MCA failure row,
but it is not yet a Proximity Prize counterpacket.
```

Then name the exact extension theorem or construction required to make it prize-relevant.

## Source Files To Read

Use the mounted project source. In particular read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
tex/RS_disproof_v3.tex
experimental/notes/m1/m1_cycle87_explicit_separator_returns_audit.md
experimental/notes/m1/m1_cycle88_cycle87_bridge_audit.md
experimental/notes/m1/m1_cycle89_official_mca_row_audit.md
experimental/notes/m1/cycle89_official_mca_row_raw/response.md
```

Relevant source questions:

1. Does the official prize quantify over arbitrary finite RS/GRS codes, or only smooth multiplicative subgroup/coset RS codes?
2. Is `n=464=2^4*29` admissible under the official challenge as written?
3. Does "smooth" mean any smooth integer or specifically power-of-two subgroup in the formal theorem/prize statement?
4. Can a GRS row be converted to an RS row without leaving the challenge class?
5. Can the 464-point construction be realized inside a power-of-two subgroup/coset by embedding, shortening, padding, or quotient pullback?
6. Can the two-copy/affine-color construction be reinterpreted as a subgroup/coset block system?
7. If not, what is the smallest exact theorem/checker that would bridge it?

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

Do not promote Cycle87/Cycle89 to a prize counterpacket unless you have source-validly discharged the prize-family issue.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---