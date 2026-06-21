# Cycle 96 Prompt: Arbitrary-Word Norm Sieve

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

Cycle95 banked:

```text
L-CYCLE95-ANCHORED-T1-EVAL-LIST
```

For `E=X-alpha`, `B=1`, `alpha notin D`, and arbitrary anchor `w`, the
support-wise noncontained bad slopes of:

```text
y_z(x) = w(x)/(x-alpha) - z/(x-alpha)
```

are exactly:

```text
{ P(alpha) : deg P <= k, |{x in D : P(x)=w(x)}| >= k+sigma }.
```

Noncontainment is automatic. Therefore the `t=1` anchored MCA cloud collapses
onto the arbitrary-word list problem at dimension `k+1`.

Cycle95 cuts any attempt to solve the `t=1` wall without solving the
arbitrary-word locator/list wall or producing a counterpacket to it.

## Target

Attack the exact new wall:

```text
L-CYCLE96-ARBITRARY-WORD-NORM-SIEVE
```

The monomial proof uses Galois/norm sieve estimates with small coefficients,
ultimately bounding norms using a small `l1` coefficient bound. For arbitrary
anchor words, a lift:

```text
U in Z[zeta_n][X]
```

can have uncontrolled archimedean coefficients. This is the first line where
the Cycle95 conditional reduction can fail.

Prove, kill, or sharply reduce:

```text
Arbitrary-word locator/list local limit:
after quotient-periodic cores are charged, the number of degree-<=k
polynomials agreeing with an arbitrary aperiodic word w on k+sigma points is
n^{O(1)} above corrected reserve.
```

Equivalently, prove a replacement for the monomial norm sieve that survives an
arbitrary lift `U`, or construct a source-valid aperiodic non-quotient
arbitrary word with a superpolynomial list.

## Required Tasks

1. Read the normal-form/list source definitions and Cycle95 audit.
2. State the exact arbitrary-word list theorem needed at dimension `k+1`.
3. Identify whether any normalization of `w` gives bounded archimedean data.
4. Try to prove an arbitrary-word norm sieve, fixed-prime local limit, or
   alternative collision bound.
5. If the theorem is false, output a source-valid counterpacket mechanism:
   aperiodic `w`, smooth generated-field domain, superpolynomial list, not
   charged by quotient-periodic cores.
6. If no proof/counterpacket is possible, name the smallest exact sublemma
   below this wall.

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
experimental/notes/m1/m1_cycle95_anchored_perfiber_t1_audit.md
experimental/notes/m1/cycle95_anchored_perfiber_t1_raw/response.md
experimental/scripts/cycle95_t1_eval_list_check.py
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

Do not return a lower-side quotient-floor construction. This is the arbitrary
word upper-side wall.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---