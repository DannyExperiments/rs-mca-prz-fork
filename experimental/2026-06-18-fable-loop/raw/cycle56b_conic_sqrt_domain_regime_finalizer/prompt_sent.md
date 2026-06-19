# Cycle 56b Prompt: Conic Sqrt Domain-Regime Finalizer

You are a theorem worker for the RS-MCA / Proximity Prize project.

This is a compact retry after Cycle56 failed with `PROVIDER_API_ERROR_403`.
Do **not** broad-scan the project. Use the facts supplied below, and read only
one or two named files if absolutely necessary. Preserve the labels `PROOF`,
`COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and `EXACT_NEW_WALL`
literally.

## Banked Facts To Use

Cycle54:

- In the balanced `t=2` stratum, the slope variable can be eliminated.
- For each split locator `T`,

```text
R=#{T split : D(T)=0, b(T)!=0},
D(T)=a_0(T)b_1(T)-a_1(T)b_0(T).
```

- The `j=1` case has `R<=2=O(j)`.

Cycle55:

- For `j=2` and `T={s,s'}`,

```text
e_1=s+s',
e_2=ss',
ell_T=(e_2,-e_1,1).
```

- With `M_ab=u_a v_b-u_b v_a`, the determinant conic is

```text
D(e_1,e_2)
= M12 e_1^2 - M02 e_1 e_2 + M01 e_2^2
  - M13 e_1 + (M03-M12)e_2 + M23.
```

- The split-pair curve is

```text
F(s,s')=D(s+s',ss')=0.
```

- Cycle55 banked only the corrected generic curve-count bound

```text
R=binomial(n,2)/Q+O(sqrt(Q))
```

after removing tangent/core and quotient/coset components.

- Cycle55 did **not** bank a `COUNTERPACKET`; it only suggested a possible
  `Theta(sqrt(Q))` excess seed from Frobenius trace fluctuations of a
  genus-one curve.

Cycle56 partial observation before provider failure:

- The `sqrt(Q)` seed is coherent if one uses `L=mu_{Q-1}=F_Q^*`, so `n≈Q`.
- Earlier banked `t=2,j=2` executable checks were in an additive/base-field
  ledger `D=F_p` with line field `F_{p^2}`, so `n=p=sqrt(Q)`.
- This domain/regime distinction may decide whether the seed is source-valid
  or only a relaxed curve-count obstruction.

## Your Task

Give a final verdict on the Cycle55 `sqrt(Q)` seed.

Answer these exact questions:

1. Is the multiplicative-domain choice

```text
L=mu_{Q-1}=F_Q^*
```

with `n≈Q`, `t=2`, and `j=2` admissible for the official smooth-domain scalar
MCA branch? Or does the source ledger / generated-field condition / rate
condition / reserve condition exclude it?

2. Does the fact that `t=2,j=2` implies

```text
k=n-j-t=n-4
```

make this a near-rate-one toy subcase rather than one of the official rates
`1/2,1/4,1/8,1/16`? If yes, say exactly how this affects the route board.

3. If `n≈Q` is admissible as a smooth multiplicative domain, can the
`Theta(sqrt(Q))` excess be promoted to a source-valid `COUNTERPACKET` against
the literal `+O(1)` conic split-pair target? Check core/tangent,
quotient/coset, low `d_M(E)`, same-witness, and `b(T)=0`.

4. If `n≈Q` is not admissible, does the remaining source-valid additive ledger
`n=sqrt(Q)` make the Weil error `O(sqrt(Q))=O(n)` harmless, already within the
tangent-scale or `n^{1+o(1)}` upper target?

5. What is the correct next wall after this verdict?

## Required Output Options

Return exactly one of:

1. `COUNTERPACKET`: a genuinely source-valid growing family with unbounded
   excess against the literal `+O(1)` conic split-pair target.
2. `ROUTE_CUT`: the Cycle55 `sqrt(Q)` seed cannot be promoted because it uses
   the wrong domain/rate/reserve ledger, or because the literal `+O(1)` target
   was not the actual source target.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a stricter domain-regime lemma that
   precisely replaces the malformed target.
4. `PROOF`: the actual source-valid `t=2,j=2` branch satisfies the intended
   upper bound.

Be blunt. Do not write a long exploration transcript. Produce the verdict and
the proof/audit.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 8000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T12-04-15-570Z-cycle56b-conic-sqrt-domain-regime-finalizer-c8dc99b5/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---