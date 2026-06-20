# Cycle 64 Prompt - Prefix-Collision Gadget Charge

You are a theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve the assigned wall. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do not brainstorm from scratch. This prompt follows Cycle 63 Round 2.

## Current Situation

The scalar-apolar route is not dead, but the naive full-block residual theorem
is dead.

Banked or nearly banked from Cycles 62-63:

```text
L-LIST-APOLAR-ALL-LAYER-CI
L-LIST-MINIMAL-CI-GJ-FIBER       with strict j>d=sigma+1
L-MODEL-GJ-RELATIVE-BLOCK-COLLAPSE
L-MODEL-GJ-MAXIMAL-KD-ASSIGNMENT
L-MODEL-GJ-DYADIC-KD-OVERLAP-NONDOUBLECOUNTING
```

Cut or false:

```text
one-atom Q_per model local limit
block-free residual is tame after full-block trades
direct scalar full-block charge => one t=1 MCA color
```

Cycle 63 Role 05 gives the route-changing counterpacket:

```text
F_0 = F_{17^16}
H_0 = mu_256
sigma = 6
j = 113
b_0 = (prod T, e_1(T),...,e_5(T)) = (1,1,0,0,0,0)
|P_0| = 52,747,567,104 > 2^32
```

Every support in this packet is `sigma`-block-free: no coset `cK` with
`|K| >= sigma` is fully contained in the support. Thus full-block trades alone
cannot bound the residual.

The proposed repair is to enlarge the charge from full blocks to local
prefix-collision gadgets.

## Read Order

Read from the project source copy:

1. `current_repo_snapshot/experimental/notes/m1/m1_cycle63_round2_audit.md`
2. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/05_role05_near_split_collision_mass.md`
3. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/09_role09_referee_route_board.md`
4. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/03_role03_maximal_kd_assignment.md`
5. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/04_role04_kd_overlap_nondoublecounting.md`
6. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/02_role02_block_collapse_lemma.md`
7. `current_repo_snapshot/experimental/notes/m1/m1_cycle62_round1_audit.md`
8. Main source only as needed:
   - `current_repo_snapshot/tex/slackMCA_v3.tex`
   - `current_repo_snapshot/tex/RS_disproof_v3.tex`
   - `current_repo_snapshot/tex/cs25_cap_v4.tex`
   - `current_repo_snapshot/tex/snarks_v4.tex`

Treat previous planning/referee files as `AUDIT / PLAN / CONDITIONAL`, not
proof, unless a later audit explicitly banks the claim.

## Target Wall

Prove or kill:

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-PARTITION-AND-CHARGE
```

A useful first formulation:

Let `H` be cyclic, `Delta=[0]+sigma[infinity]`, and let the model boundary map
be

```text
Phi_sigma(T) = (prod_{x in T} x, e_1(T),...,e_{sigma-1}(T)).
```

For a divisor subgroup `J <= H`, define a finite local equivalence on
subsets of one or several `J`-cosets:

```text
A ==_sigma B
iff |A|=|B| and E_A(z) == E_B(z) mod z^sigma,
```

where `E_A(z)` is the elementary-symmetric generating polynomial or the
equivalent truncated locator-prefix data. Include product color if the
boundary uses product separately; do not silently identify product and jet
coordinates.

Attach to each equivalence class `C` its exact product-color enumerator

```text
W_C = sum_{A in C} Y^{log_J(prod A)}
```

or an equivalent finite group-ring object.

The desired theorem should give:

1. a canonical maximal assignment of supports to such local prefix-collision
   gadget classes;
2. a non-double-counting or bounded-overlap theorem across subgroup scales;
3. an explicit total charge formula/bound for one fiber
   `Phi_sigma(T)=b`;
4. verification that the Role 05 packet is absorbed as one or finitely many
   charged gadget classes, **or** a stronger counterpacket showing this
   gadget formalism is still insufficient.

## Hard Requirements

- Keep finite statements exact. Do not use `n^{1+o(1)}` as a prize-level
  certificate.
- If you define a "gadget", specify its ground set, subgroup scale, prefix
  modulus, product color, target, and multiplicity exactly.
- If you claim bounded overlap, prove it; do not say "canonical" as a synonym
  for disjoint.
- If the Role 05 packet is absorbed, compute or specify the exact charge
  object that absorbs it.
- If the Role 05 packet is not absorbed, state the sharper wall and give a
  concrete falsifier.
- Distinguish scalar-list support mass from `t=1` MCA color occupancy.
- Do not promote this model result to the full prize theorem unless all
  source hypotheses and all remaining strata are explicitly handled.

## Required Output Format

Start with exactly one of:

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
2. Formal theorem, reduction, or counterpacket statement.
3. Full proof/construction, with edge cases.
4. Parameter ledger and finite relevance.
5. What is bankable versus conditional.
6. Failure point if unresolved.
7. The next exact lemma or construction.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-09-24-153Z-cycle64-prefix-collision-gadget-charge-78d0dd73/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---