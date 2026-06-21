# Cycle 89 Prompt: Official MCA Row Identification

You are auditing the RS-MCA / Proximity Prize repository as a skeptical mathematical research director.

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. No Internet. Take all the time to reason you need. Use MAX reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?

## Target

Prove or kill the official-definition bridge:

```text
L-CYCLE89-OFFICIAL-MCA-ROW-IDENTIFICATION
```

This is not a request to rerun the Cycle84/Cycle87 finite census. Treat those finite certificate facts as conditional antecedents. Your job is to check whether the Cycle87/Cycle88 counted object is exactly an official support-wise line-MCA bad-slope numerator for one finite Reed--Solomon code row.

## Source Files To Read

Read these repository files directly:

```text
tex/slackMCA_v3.tex
tex/RS_disproof_v3.tex
readme.md
agents.md
experimental/notes/m1/m1_cycle87_explicit_separator_returns_audit.md
experimental/notes/m1/m1_cycle88_cycle87_bridge_audit.md
experimental/notes/m1/cycle88_cycle87_bridge_raw/response.md
```

The decisive source definitions appear near:

```text
tex/slackMCA_v3.tex:640-646
tex/slackMCA_v3.tex:1189-1201
tex/slackMCA_v3.tex:1206-1210
tex/RS_disproof_v3.tex:110-113
readme.md:206-210
```

But do not rely only on those line hints. Search the source for `def:mca`, `def:residue`, `thm:normalform`, `q_line`, `q_chal`, `2^-128`, `delta_C^*`, `noncontained`, and `support-wise`.

## Conditional Facts To Assume

Assume the following finite facts only as antecedents:

```text
Cycle84/Cycle85/Cycle87 finite certificate facts:
P = 52,747,567,104
Occ_beta = 52,747,567,092
smooth/projective max fiber <= 2
(n,k,sigma,j,t) = (464,232,6,226,1)
q_gen = q_code = q_line = q_chal = 17^48
certified distinct slopes >= 1,391,152,917,379,006,070,784
floor(q_line / 2^128) = 338,617,018,271,848,945,628
```

Do not upgrade these antecedents to independently replayed proof.

## Required Questions

Answer each item explicitly.

1. Does `tex/slackMCA_v3.tex` define the official support-wise MCA numerator as `# bad z / |F|` over the line/challenge field?
2. For the Cycle87 package, is the counted `z` set a set of slopes in exactly that field, with no hidden base-field or generated-field denominator replacing `q_line`?
3. Does the witness threshold match the official radius:

```text
delta = 1 - (k + sigma)/n = 1 - 238/464
```

and does `j = n-k-sigma = 226` have any official role beyond complement size?
4. Does a degree-`t=1` residue-line datum fit `def:residue` with `1 <= t <= r = n-k`?
5. Is Cycle87 noncontainment exactly the noncontained condition in `def:residue` and the support-wise line-MCA condition (ii) in `def:mca`?
6. Does `thm:normalform` convert noncontained residue-line witnesses into support-wise MCA bad slopes without requiring multiplicative subgroup domains, quotient separation, aperiodicity, asymptotic reserve, or `t=sigma`?
7. Can same-slope collisions, same-support collisions, contained incidences, quotient periodicity, affine-color normalization, or projectivization reduce the official numerator below the conservative `N*P/2` bound?
8. Is the comparison against `floor(q_line / 2^128)` the right finite challenge comparison for an MCA error target `<= 2^-128`?
9. Is this an official-prize-relevant finite counterpacket row, or only a model certificate? State the exact remaining dependency.

## Required Output Format

Use one of these labels:

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
2. Exact theorem or counterexample statement.
3. Proof or obstruction, line-by-line against the source definitions.
4. Field ledger: `q_gen`, `q_code`, `q_line`, `q_chal`, and `2^-128` target.
5. Verification requirements.
6. Next exact lemma or construction.

Before finalizing, do a self-audit:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing hypothesis, or exact counterexample mechanism.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---