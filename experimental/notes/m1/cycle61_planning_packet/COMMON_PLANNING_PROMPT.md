# COMMON PROMPT — Cycle 61 Planning Round

You are a theorem-planning co-director for the RS-MCA / Proximity Prize project.

Do **not** treat this as a normal proof-generation prompt. Your job is to design
the best plan for reaching a full solution of the two grand challenges, using
the attached repository/context. If you can solve a missing lemma outright, do
so, but the primary requested deliverable is a realistic, adversarial,
step-by-step plan that maximizes the chance of an actual solve.

Use MAX reasoning. Take as much time as needed. No Internet. Read the context
carefully before answering.

## The Two Grand Challenges

1. **Grand MCA challenge.** For Reed-Solomon codes on smooth evaluation domains
   at rates `1/2, 1/4, 1/8, 1/16`, determine the largest radius `delta_C^*`
   for which `epsilon_mca(C, delta_C^*) <= 2^-128`, for sufficiently large
   allowed fields.

2. **Grand list decoding challenge.** For the same RS codes and constant
   interleaving arity `m`, determine the largest radius `delta_C^*` for which
   the interleaved list size is at most `2^-128 |F|`.

## Current Route Board Snapshot

Conservative current status:

- The MCA lower/failure branch is strong/theorem-grade below the corrected
  entropy reserve, via random-anchor/Bessel-type constructions.
- The exact MCA safe-side object is best understood as a syndrome
  transverse-secant incidence problem, not as a single denominator stratum.
- The old pure `n^{1+o(1)}` safe-side target is false or too narrow; a correct
  finite theorem must include occupancy/main term, quotient/split-rational
  containers, envelope/tangent/hereditary terms, and a primitive discrepancy
  term.
- The quotient ledger has expanded:
  - genus-zero PGL2/subgroup-chain split-rational quotients;
  - genus-one Lattes/elliptic-isogeny quotients;
  - higher-genus finite-discrepancy branch;
  - point-fiber quotients are not enough;
  - divisor-norm/configuration-space characters may be needed in the
    jet-residue branch.
- The `t < sigma` jet-residue branch has a clean `t=1` apolar
  complete-intersection normal form, but no solved primitive inverse theorem.
- The `t > sigma` denominator branch is not solved by a simple compression
  theorem; the denominator-free syndrome formulation is preferred.
- The interleaved-list branch reduces to the scalar full-support list problem
  at the official `2^-128 |F|` scale, but the scalar list theorem remains open.
- Cycle 60 added important route repair, not a full solve:
  - Lattes/isogeny quotient packets;
  - fixed-partition QAR packing and fixed-core petal bounds;
  - divisor-norm/configuration-character counterpacket;
  - hereditary MDS-3-core extraction;
  - `t=1` apolar split-numerator normal form;
  - scalar full-support circuit-transversal reduction.

## Required Output Format

Use the labels below literally where appropriate:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
CONDITIONAL
AUDIT
PLAN
```

Your answer must include:

1. **Executive verdict.**
   - Is the full prize problem currently plausibly solvable from this route?
   - Is it close, medium-range, or still missing hard inverse theorems?
   - Give confidence levels.

2. **Minimal theorem package.**
   - State the smallest set of theorems/lemmas that, if proved, would solve the
     MCA challenge.
   - State the smallest set for the list challenge.
   - Separate asymptotic theorem needs from finite `2^-128` certificate needs.

3. **Dependency DAG.**
   - Give an explicit dependency graph: theorem A depends on lemmas B/C, which
     depend on sublemmas D/E, etc.
   - Mark each node as already banked, likely, doubtful, false, or unknown.

4. **Best next 3-6 prompts.**
   - Produce copy-ready theorem-worker prompts that are likely to advance the
     route most.
   - Each prompt must name the exact missing lemma, the desired proof/counterexample,
     and the acceptance/failure criteria.

5. **Kill tests and counterexample searches.**
   - Identify which proposed lemmas are most likely false.
   - Give finite toy cases or symbolic checks that would falsify them quickly.

6. **Verification and formalization plan.**
   - Which claims from Cycle 58-60 must be independently verified first?
   - Which scripts/checkers should be written?
   - Which results should be promoted into TeX only after review?

7. **Resource allocation.**
   - If we have 9 strong theorem-worker instances and a local Fable/Codex loop,
     how should we allocate them for the next two rounds?
   - What should the human/PRZ check first?

8. **Route to full solve.**
   - If yes, what is the next exact lemma or construction?
   - If no, say precisely what missing theory blocks the route.

Be blunt. Do not oversell. If a previously proposed wall is the wrong wall,
say so. If the route is too broad and needs narrowing, say exactly how.
