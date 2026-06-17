# Agents Log

This file is the working ledger for agent-created material in `experimental/`.
Use it to record every new note, script, scan, formalization stub, or audit before
the material is promoted into `tex/` or `scripts/`.

The log is not a proof-status authority. It is a coordination record: what was
added, why it might matter, and what a human or later agent should check next.
Keep entries concise and link to the relevant files.

## Entry Format

```markdown
### YYYY-MM-DD - Short title

- **Agent/model:** Name the agent or model, for example `GPT-5.5 Pro`,
  `Claude Fable 5`, or `Codex`.
- **Files added or changed:** List paths under `experimental/`, `tex/`,
  or `scripts/`.
- **Status:** PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT /
  COUNTEREXAMPLE.
- **What is being added:** State the claim, note, scan, script, or certificate
  in one or two sentences.
- **How it is useful:** Say which paper, theorem, problem, ledger, or toy case
  the material supports.
- **What to do next:** Give the next verification, cleanup, proof step,
  experiment, or promotion decision.
```

## Entries

### 2026-06-17 - Open PR triage integration

- **Agent/model:** Codex.
- **Files added or changed:** Integrated experimental material from PRs #1,
  #2, #3, and #46 through #66; added
  `experimental/pr-triage-2026-06-17.md`; renamed PR #55's dither scanner to
  `experimental/quotient_profile_dither.py` with matching `.md` note.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** One-by-one triage of the open PR queue and local
  integration of accepted experimental notes, scanners, certificates, and
  audit bundles.
- **How it is useful:** Preserves useful agent contributions while enforcing
  the repository rule that new material starts in `experimental/` and Papers
  A-D remain unchanged.
- **What to do next:** Run verifiers and audits on the integrated material,
  review mathematical notes before promotion, and close the original PRs as
  manually integrated once the integration commit is pushed.

### 2026-06-18 - Fable loop cycle 1, F1 arbitrary anchors

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Audit of an Opus 4.8 artifact-stream response on
  balanced arbitrary anchors in `def:residue`. The bankable part is the
  quadratic reduction from arbitrary extension anchors to a paired base
  interpolation-residue readout modulo `Ehat=lcm(E,E^tau)`.
- **How it is useful:** Narrows F1: arbitrary anchors do not introduce a new
  extension-only invariant in the quadratic case, but they enlarge the base
  object beyond the monic locator image.
- **What to do next:** Audit or prove the resulting base-field slope-image
  packing statement. Do not use the raw generalized per-fiber endpoint from the
  model answer without repair, since arbitrary low-degree anchors can create
  huge raw fibers.

### 2026-06-18 - Fable loop cycle 2 first attempt hung

- **Agent/model:** Codex supervising `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_HUNG_RUN.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle2_retry_paired_base_readout_short.md`.
- **Status:** AUDIT / HARNESS_FAILED.
- **What is being added:** The first Cycle 2 paired-base-readout audit attempt
  exceeded the normal answer window, ended with
  `CLAUDE_CAPTURE_WARNING_FATAL`, and produced no final theorem classification.
- **How it is useful:** Prevents later agents from treating the partial
  source-reading trace as mathematics and records the shortened retry prompt.
- **What to do next:** Retry the same target with the short prompt and a
  20-minute external watchdog. Bank only a clean `response.md` with an explicit
  final classification.

### 2026-06-18 - Codex local paired-base-readout audit

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_PAIRED_BASE_READOUT_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** A bounded local audit of the Cycle 1 arbitrary-anchor
  reduction. It confirms the factor-through paired base readout, isolates slope
  uniqueness for nonzero numerator residue, and records that shrinking to an
  `a`-subset preserves interpolation but not necessarily noncontainment.
- **How it is useful:** Refines the live F1 target into slope-image/bad-locus
  packing rather than raw arbitrary-anchor fiber bounds.
- **What to do next:** Compare against the Opus retry answer when available,
  then package only the agreed bankable statements for PR review.

### 2026-06-18 - Fable loop cycle 2 retry, paired base readout

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The shortened retry completed cleanly and confirmed
  the paired base interpolation-residue factorization for quadratic balanced
  arbitrary anchors, while sharpening the remaining target into slope-image /
  bad-locus packing rather than raw arbitrary-anchor fiber size.
- **How it is useful:** Refines F1: the balanced quadratic arbitrary-anchor
  issue is now a base-field packing wall `W-F1-AA`, not an extension-only
  invariant problem.
- **What to do next:** Ask the next worker to attack `W-F1-AA` directly:
  prove a slope-image packing bound, or produce a finite/source-valid
  arbitrary-anchor counterpacket after tangent/contained separation.

### 2026-06-18 - Codex local balanced noncontainment subset lemma

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_NONCONTAINMENT_SUBSET_LEMMA.md`.
- **Status:** BANKABLE_LEMMA / AUDIT.
- **What is being added:** In a degree-`t` residue-line datum with nonzero
  numerator and balanced support size `a=k+t`, no degree-`<k` polynomial can
  agree with `-Bnum/E` on an `a`-subset. Thus balanced nonzero-numerator
  supports are automatically noncontained.
- **How it is useful:** Removes one suspected obstruction in `W-F1-AA`: in the
  balanced nonzero-numerator case, shrinking to an `a`-subset does not lose
  noncontainment.
- **What to do next:** Verify this lemma against the Cycle 3 Opus answer, then
  retarget `W-F1-AA` to the remaining slope-image packing problem.

### 2026-06-18 - Fable loop cycle 3, W-F1-AA noncontainment

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle3_w_f1_aa_noncontainment.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The run confirms the noncontainment subset issue is
  not the live balanced nonzero-numerator obstruction: supports of size at
  least `a=k+t` are automatically noncontained. The next wall is
  `W-F1-AA-AGR`, an agreement-rigidity/collision problem for paired readouts.
- **How it is useful:** Sharpens `W-F1-AA`: future work should control the
  high-agreement condition `nu(S)>=s_delta`, not ask whether noncontainment
  survives shrinking to an `a`-subset.
- **What to do next:** Attack `W-F1-AA-AGR`: prove a high-agreement collision
  rigidity theorem for arbitrary base anchors, or produce a finite
  high-agreement counterpacket.

### 2026-06-18 - Fable loop cycle 4, balance-notation route cut

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle4_audit_cycle3_balance_notation.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE4_BALANCE_NOTATION_AUDIT_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE4_BALANCE_NOTATION_ROUTE_CUT_AUDIT.md`.
- **Status:** ROUTE_CUT / BANKABLE_LEMMA / AUDIT.
- **What is being added:** Cycle 4 cuts Cycle 3's `W-F1-AA-AGR` as a balanced
  wall. Source notation has `a=ceil((1-delta)n)` and `sigma=a-k`, so balanced
  `t=sigma` gives `k+t=a=s_delta`; no extra high-agreement layer remains.
- **How it is useful:** Prevents a false detour. The balanced live target is
  restored to slope-image/bad-locus packing for the paired base readout, while
  retaining the noncontainment subset lemma.
- **What to do next:** Attack restored `W-F1-AA`: bound distinct slopes whose
  paired readout lands on `F*[Bnum]_E`, after tangent/zero-numerator and
  quotient-periodic contributions are separated.
