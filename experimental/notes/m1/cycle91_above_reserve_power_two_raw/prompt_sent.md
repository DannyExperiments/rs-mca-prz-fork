# Cycle 91 Prompt: Above-Reserve Power-Of-Two Occupancy

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

## Current State

Cycle89 closed the official-definition bridge:

```text
L-CYCLE89-OFFICIAL-MCA-ROW-IDENTIFICATION := BANKABLE_LEMMA / CONDITIONAL
```

Given the Cycle84/Cycle85/Cycle87 finite facts, the `n=464=2^4*29`
construction is a genuine support-wise line-MCA bad-slope row under
`def:mca`, `def:residue`, and `thm:normalform`.

Cycle90 cut the direct prize upgrade:

```text
The n=464 row is not a smooth power-of-two subgroup row.
The literal 464 -> 2^a port is blocked by the factor 29.
```

Cycle90 also banked a separate smooth subgroup failure row:

```text
L-CYCLE90-PRIZE-FAMILY-EMBEDDING-BELOW-RESERVE := BANKABLE_LEMMA / CONDITIONAL
```

It uses:

```text
q = 17^48
|H| = 256
rho = 1/2
k = 128
t = 1
delta = 127/256
gap = 1/256
```

This clears `2^-128`, but is below the corrected reserve:

```text
1/256 < tau_star(1/2,17^48) ~= 1/log2(17^48)
```

The remaining wall is therefore:

```text
W-CYCLE91-ABOVE-RESERVE-POWER-OF-TWO-OCCUPANCY
```

## Target

Prove or kill the existence of an **above-reserve** smooth power-of-two subgroup MCA failure row in the current field-size band.

You must attack this exact statement:

```text
Find q <= 2^256, a smooth power-of-two subgroup H <= F_q^*
with |H| = 2^a, rate rho in {1/2,1/4,1/8,1/16},
and a residue-line datum over RS[F_q,H,rho|H|]
such that:

  gap = t/|H| > (1+epsilon) tau_star(rho,q)

and

  Lambda_NC_{t,delta}(H,k) > floor(q/2^128),

where delta = 1 - rho - gap.
```

If this exact target is too broad, reduce it to the smallest rigorous theorem/checker/counterpacket.

## Required Branches

### Branch A: Constructive Above-Reserve Packet

Try to adapt the Cycle84/Cycle87 occupancy mechanism to a pure power-of-two subgroup domain.

You must explicitly check:

- subgroup order is exactly a power of two;
- rate is one of the prize rates;
- support size and radius match `def:mca`;
- denominator degree and residue datum match `def:residue`;
- noncontainment is proved;
- same-slope/projective/quotient/affine-color collisions are paid;
- `q_line` is the true slope field;
- the count exceeds `floor(q_line/2^128)`;
- the gap is genuinely above corrected reserve.

### Branch B: Quotient-Floor Extension

Try to extend the unconditional quotient-floor reach (`prop:prize` / `prop:qfloor`) from roughly `2^162` to the `2^196` to `2^256` band.

If possible, prove a concrete finite statement at one prize rate. If impossible,
name the exact fixed-prime collision/equidistribution wall.

### Branch C: Route Cut / Impossibility Of Current Mechanism

If above-reserve power-of-two occupancy cannot be produced from the current
Cycle84/Cycle87 gadget, prove that route cut.

Identify the exact obstruction:

- pure 2-group block systems cannot realize the 29-color/two-copy separator;
- quotient floors cap below `2^-128`;
- Bessel/second-moment occupancy dies above reserve;
- projective multiplicity cannot be bounded strongly enough;
- or another explicit mechanism.

Do not merely say "open". Produce a useful exact wall.

## Source Files To Read

Use the mounted project source. In particular read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
tex/RS_disproof_v3.tex
experimental/notes/m1/m1_cycle87_explicit_separator_returns_audit.md
experimental/notes/m1/m1_cycle89_official_mca_row_audit.md
experimental/notes/m1/m1_cycle90_prize_family_embedding_audit.md
experimental/notes/m1/cycle90_prize_family_embedding_raw/response.md
```

Relevant source questions:

1. What exact above-reserve gap is needed at each rate and field size?
2. Which fields `q <= 2^256` have enough `2`-adic subgroup order to host the attempt?
3. Can the Cycle84/Cycle87 two-copy/affine-color separator be rebuilt on a pure 2-group?
4. Can a quotient/coset/chosen-subset construction beat the known quotient floor?
5. If not, what is the exact next checker or theorem needed?

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

Do not upgrade below-reserve failure to an above-reserve result.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-29-25-252Z-cycle91-above-reserve-power-two-4dee6dbe/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---