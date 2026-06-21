# Cycle 93 Prompt: Corrected Reserve And Section 7 Splice

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

Cycle92 classified the Cycle91 row as:

```text
AUDIT / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Banked lemma:

```text
L-CYCLE92-EXTENSION-FIELD-POWER-BASIS-COVERAGE
```

For `p=5`, `N=256`, `d=ord_256(5)=64`, `q=5^64`, `H <= F_q^*` the order-256
subgroup, `rho=1/16`, `k=16`, `ell=17`, and line:

```text
f(x)=x^17
g(x)=x^16
```

the noncontained bad slopes include `ell^wedge H`, and the sign-digit lower
bound gives:

```text
binom(64,17) * 2^17
  = 180,796,807,614,761,533,440
  ~= 2^67.2929.
```

Since:

```text
q = 5^64 ~= 2^148.6034
floor(q/2^128) = 1,593,091
```

the row has:

```text
epsilon_mca >= 2^-81.31 > 2^-128.
```

Cycle92 did **not** promote this to an official prize counterpacket. It called
it an extension-field research certificate and lower/failure-side
corroboration.

Codex local arithmetic also found:

```text
log2 binom(256,17) = 86.87894707796833
log2(5^64) = 148.60339807279118
exact binomial reserve margin = 61.724450994822845 bits
```

This suggests the simple finite binomial reserve condition clears strongly for
`sigma=1`, but Cycle92 warned that the full corrected `tau_star` /
quotient-profile convention must be source-audited before calling the row
"above reserve" in the official ledger.

## Target

Attack:

```text
W-CYCLE93-CORRECTED-RESERVE-AND-SECTION-7-SPLICE
```

Decide whether `L-CYCLE92-EXTENSION-FIELD-POWER-BASIS-COVERAGE` can be
source-validly inserted into the Section 7 extension-field lower/disproof
ledger as a corrected-reserve companion lemma.

## Required Tasks

1. Read the source definitions of corrected reserve, quotient profile, and
   Section 7 extension-field examples.
2. Compute or state the exact finite corrected-reserve condition for the
   Cycle91 row, not just the leading proxy `H2(rho)/log2(q)`.
3. Decide whether the row is above corrected reserve under the source
   convention.
4. Decide whether Section 7 can accept this row as a companion theorem, or
   whether a hidden condition blocks the splice.
5. State the exact theorem text that should be banked if the splice succeeds.
6. If the splice fails, give the exact failed hypothesis and the repaired
   target.

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/RS_disproof_v3.tex
tex/slackMCA_v3.tex
experimental/notes/m1/m1_cycle91_above_reserve_power_two_audit.md
experimental/notes/m1/m1_cycle92_extension_field_admissibility_audit.md
experimental/scripts/cycle91_extension_power_two_arithmetic.py
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

Do not promote this row to an official prize counterpacket. The question is
whether it is a source-valid Section 7 extension-field companion at corrected
reserve, and what exact wall remains after that.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-26-48-319Z-cycle93-corrected-reserve-section7-splice-a024e30d/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---