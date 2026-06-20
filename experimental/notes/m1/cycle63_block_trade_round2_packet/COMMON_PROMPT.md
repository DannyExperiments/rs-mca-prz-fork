# COMMON PROMPT - Cycle 63 Block-Trade Repair Round 2

You are one theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve your assigned wall. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do not brainstorm from scratch. This round follows the Cycle 62 route cut:

```text
The scalar-apolar algebraic spine survived.
L-LIST-APOLAR-ALL-LAYER-CI appears bankable.
L-LIST-MINIMAL-CI-GJ-FIBER appears bankable.
The one-atom Q_per model local-limit route is false.
The next wall is configuration-level block trades.
```

The central wall for this round is:

```text
L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE
```

Secondary residual wall:

```text
W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS
```

This is a proof/kill round. Treat all prior planning/referee material as
`AUDIT / PLAN / CONDITIONAL`, not proof. Treat Cycle 62 Roles 01, 02, 05, 07,
08 as promising but still reviewable unless your role explicitly audits them.

## Read Order

Read these files from the uploaded context zip first:

1. `rs-mca/experimental/notes/m1/m1_cycle62_round1_audit.md`
2. `rs-mca/experimental/notes/m1/cycle62_round1_raw/04_role04_model_gj_counterpacket_result.md`
3. `rs-mca/experimental/notes/m1/cycle62_round1_raw/03_role03_model_gj_local_limit_result.md`
4. `rs-mca/experimental/notes/m1/cycle62_round1_raw/02_role02_minimal_ci_gj_fiber_result.md`
5. `rs-mca/experimental/notes/m1/cycle62_round1_raw/01_role01_scalar_apolar_all_layer_ci_result.md`
6. `rs-mca/experimental/notes/m1/cycle62_round1_raw/05_role05_t1_mca_gj_color_result.md`
7. `rs-mca/experimental/notes/m1/m1_cycle61_master_referee_audit.md`
8. Main source only as needed:
   - `rs-mca/tex/slackMCA_v3.tex`
   - `rs-mca/tex/RS_disproof_v3.tex`
   - `rs-mca/tex/cs25_cap_v4.tex`
   - `rs-mca/tex/snarks_v4.tex`

## Core Definitions To Use

In the model modulus

```text
Delta = [0] + sigma [infinity],
```

the boundary map records product plus elementary symmetric coordinates

```text
prod_{x in T} x,
e_1(T),...,e_{sigma-1}(T).
```

For a subgroup `K <= H` of order `M >= sigma`, define the block product

```text
beta_K(cK) = prod_{u in K} alpha_Delta(cu).
```

The basic block-collapse identity to prove/use is:

```text
prod_{u in K}(X-cuZ) = X^M - c^M Z^M
                     ≡ X^M mod Z^sigma   when M >= sigma.
```

Thus a full `K`-block kills all jet coordinates of degrees
`1,...,sigma-1` and remembers only a toric/block color `c^M`.

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
2. Formal theorem/claim/counterpacket statement.
3. Full proof or construction, with all edge cases checked.
4. Parameter ledger and exact finite relevance when applicable.
5. What is bankable versus conditional.
6. Failure point if the proof does not close.
7. Next exact lemma or construction.

Do not use `n^{1+o(1)}` as a finite prize certificate. Do not hide behind
undefined words like primitive, generic, regular, or random-like. If you use
such a word, define it as an exact finite condition.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```

