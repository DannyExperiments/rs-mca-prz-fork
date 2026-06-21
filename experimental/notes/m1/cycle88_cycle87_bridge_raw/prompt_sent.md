# Cycle 88 Prompt - Cycle87 Certificate To Official MCA Bridge

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Context

You are working on the RS-MCA / Proximity Prize research lane. The latest
banked result is Cycle87, a certificate-level pass for an explicit
`U`-separator 464-point construction.

Attached context includes:

- `m1_cycle87_explicit_separator_returns_audit.md`
- `02_CYCLE87_U_SEPARATOR_PROOF.md`
- `02_cycle87_master_certificate.json`
- `02_cycle87_u_separator_replay_bundle.zip`
- `02_cycle87_explicit_two_copy_separator_certificate.zip`
- `06_cycle87_u_separator_pass.json`
- `06_cycle87_u_smooth_census_result.json`
- `08_cycle87_certificate_engineer_bundle.zip`
- raw-folder checksums and agents log excerpt

Codex local audit already verified:

- downloaded bundle internal SHA256SUMS;
- `cycle87_verify_master.py`;
- setup verifier;
- 464 GRS artifact verifier;
- projective census aggregation;
- symbolic threshold verifier;
- Role08 checker-bundle smoke verifiers.

Codex did **not** independently rerun the full 52,747,567,104-record census.
Treat Cycle87 as:

`PROOF_CERTIFICATE_PASS / BANKABLE_LEMMA / INDEPENDENT_REPLAY_PENDING`

not as a main-paper theorem.

## Decisive Cycle87 Certificate Values

The certificate claims:

```text
profile: (n,k,sigma,j,t) = (464,232,6,226,1)
q_gen = q_code = q_line = q_chal = 17^48
records P = 52,747,567,104
projected distinct keys = 52,747,567,062
projected ordered off-diagonal energy = 84
projected max multiplicity = 2
smooth/projective histogram: m1 = 52,747,567,020; m2 = 42; m_ge_3 = 0
floor(q_line / 2^128) = 338,617,018,271,848,945,628
certified distinct slopes = 1,391,152,917,379,006,070,784
margin over target = 1,052,535,899,107,157,125,156
```

The construction is said to be one fresh `[464,232]` GRS code over
`L = F_17^48`, not ordinary puncturing of the previous one-copy code. It uses a
single affine syndrome line and the explicit separator `U` where
`L = F0[U]/(U^3-(X+2))`, `F0 = F_17[X]/(X^16+X^8+3)`.

## Task

Audit and either prove or kill the exact bridge:

```text
L-CYCLE87-464-U-OFFICIAL-MCA-FAIL-ROW
```

Meaning:

> The Cycle87 certificate package, if its finite replay is trusted, yields a
> valid official finite MCA failure row at rate `rho = 1/2` with
> `(n,k,sigma)=(464,232,6)`, field/challenge size `17^48`, and numerator
> exceeding `floor(q_line / 2^128)`.

You must decide whether the bridge is theorem-valid, conditionally valid, or
false.

## Required Self-Audit

Before finalizing, explicitly answer:

1. What exact implication did you prove, and what exact implication did you not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, projectivization, or affine color normalization reduce the
   claimed numerator?
6. If your answer is a `PLAN`, what exact theorem/checker/counterpacket would
   convert it into `PROOF` or `COUNTERPACKET`?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Output Format

Start with one label:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `PLAN`

Then include:

1. Executive verdict and confidence.
2. Exact theorem or counterpacket statement.
3. Proof or obstruction, with all field/cardinality arithmetic explicit.
4. Certificate/replay requirements.
5. Next exact lemma or construction.

If the certificate package is insufficient, say exactly what is missing. If the
bridge is valid only conditional on independent full replay, state that
condition precisely.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- LOCAL FILE ATTACHMENTS ---
The following files are available in this read-only attachment directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_attachments

Original staged files:
- 20260621_cycle88_cycle87_bridge_context.zip (application/zip, 2123910 bytes)

Extracted zip contents:
- 20260621_cycle88_cycle87_bridge_context.zip extracted to /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/input_attachments/20260621_cycle88_cycle87_bridge_context_extracted
  - experimental/notes/m1/m1_cycle87_explicit_separator_returns_audit.md (7999 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/SHA256SUMS.txt (4372 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/02_CYCLE87_U_SEPARATOR_PROOF.md (20973 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/02_cycle87_master_certificate.json (5617 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/02_cycle87_u_separator_replay_bundle.zip (1972310 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/02_cycle87_explicit_two_copy_separator_certificate.zip (49533 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/06_cycle87_u_separator_pass.json (1501 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/06_cycle87_u_smooth_census_result.json (655 bytes)
  - experimental/notes/m1/cycle87_explicit_separator_returns_raw/08_cycle87_certificate_engineer_bundle.zip (60317 bytes)
  - experimental/agents-log.md (81823 bytes)

Use the available Read, Glob, and Grep tools to inspect staged and extracted files when needed. If a binary file cannot be meaningfully read, say so explicitly rather than inventing contents.
--- END LOCAL FILE ATTACHMENTS ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-35-07-288Z-cycle88-cycle87-official-mca-bridge-edc9cb8b/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---