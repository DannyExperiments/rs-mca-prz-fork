# Cycle 104 Prompt: Bandwidth-k Divisor Incidence

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solution? If yes, what is the next exact lemma or
construction?

## Context

You are working inside the RS-MCA / proximity-prize M1 upper-side route. Read
the current project source files first, especially:

```text
CURRENT_CYCLE103_BRIEF.md
current_repo_snapshot/experimental/notes/m1/m1_cycle103_e1_image_flat_variety_audit.md
current_repo_snapshot/experimental/notes/m1/cycle103_e1_image_flat_variety_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle104_bandwidth_k_divisor_incidence_prompt.md
```

Cycle103 closes the bandwidth-`1` wall:

```text
|Theta_U| = |e_1(V)| <= (n-sigma+1)(sigma+1) = O(n^2)
```

for `k=1`, uniformly in `Uhat`.

Do not re-attack `k=1`. Do not revive the false short-window Padé/BM divisor
route killed in Cycle102. The correct divisor statement for `k=1` used the full
co-locator:

```text
G(theta,X) = [(1-theta X)^(-1) Uhat(X)]_{deg_X <= sigma+1},
theta active <=> G(theta,X) | 1-X^n.
```

## Target

Attack:

```text
W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE
```

For general bandwidth `k>=2`, set `s=sigma+k`. The active congruence fixes only
the first `sigma+2` coefficients of the co-locator, so activity becomes:

```text
theta active
<=> exists rho in F_p[X], deg rho <= k-2, such that
    G(theta,X) + X^(sigma+2) rho(X) divides 1-X^n.
```

The first exact case to attack is `k=2`:

```text
theta active
<=> exists r in F_p such that
    G(theta,X) + r X^(sigma+2) divides 1-X^n.
```

Prove or kill a polynomial bound for the distinct active theta values in the
aperiodic branch:

```text
#{theta : exists rho, G(theta,X)+X^(sigma+2)rho divides 1-X^n}
    <= n^{O(1)}.
```

## What Counts

Return one of:

```text
PROOF
```

A source-valid proof for `k=2`, or for all fixed/general `k>=2`, that the
active theta set is polynomial after quotient/periodic branches are charged.

```text
COUNTERPACKET
```

A source-valid aperiodic family above corrected reserve with superpolynomially
many active theta values for some `k>=2`.

```text
BANKABLE_LEMMA
```

A proved strict reduction to a smaller named theorem, preferably an explicit
non-vanishing/elimination statement for the affine divisor family.

```text
ROUTE_CUT
```

A rigorous reason this divisor-incidence route cannot prove the needed upper
bound, with the corrected replacement target.

```text
EXACT_NEW_WALL
```

Only if the wall is reduced to a strictly smaller exact theorem/checker.

## Self-Audit Required Before Finalizing

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T14-45-40-594Z-cycle104-bandwidth-k-divisor-incidence-d1888115/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---