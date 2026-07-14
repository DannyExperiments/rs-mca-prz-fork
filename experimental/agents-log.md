Warning: truncated output (original token count: 47328)
Total output lines: 3127

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
- **What is being added:** State the claim, note, scan, script, proof,
  heuristic, or computation
  in one or two sentences.
- **How it is useful:** Say which paper, theorem, problem, ledger, or toy case
  the material supports.
- **What to do next:** Give the next verification, cleanup, proof step,
  experiment, or promotion decision.
```

## Entries

### 2026-07-14 - Exact Hahn payment at Grand List state u=1,043,460

- **Agent/model:** External ChatGPT Pro theorem worker; independently audited
  and integrated by `gpt-5.6-sol` Ultra and Codex.
- **Files added or changed:**
  `experimental/notes/l2/rank16_u1043460_hahn_lp_payment.md`,
  `experimental/scripts/verify_rank16_u1043460_hahn_lp_payment.rb`,
  `experimental/data/certificates/rank16-u1043460-hahn-lp-payment/verifier_output.txt`,
  `experimental/lean/grande_finale/GrandeFinale/Rank16U1043460HahnPaymentTarget.lean`,
  and `experimental/agents-log.md`.
- **Status:** PROVED / EXACT FINITE CERTIFICATE.
- **What is being added:** A degree-five normalized Hahn/Delsarte certificate
  bounds the entire selected-support family at the exact state `u=1,043,460`
  by `41,358,983,685,320,209`, below the one-row target by
  `233,495,126,810,867,383`, uniformly in affine rank.
- **How it is useful:** It pays the fixed state `u=1,043,460` without line,
  two-flat, locator, or recurrence inputs.  It does not compile or assert the
  global first-unpaid frontier.
- **What to do next:** Compose this fixed-state theorem only through a separately
  audited frontier ledger.  Formalize the explicit Hahn certificate in the
  included statement target before calling the result Lean-certified.

### 2026-07-14 - L1/L2 threshold PR integration wave

- **Agent/model:** Codex integrating PRs #742--#754 from DannyExperiments,
  manifoldcontrol, holmbuar, avdeevvadim, AllenGrahamHart, and scottdhughes.
- **Files added or changed:** Added L1/L2/threshold/audit notes under
  `experimental/notes/`, certificate data and verifier transcripts under
  `experimental/data/certificates/`, verifier scripts under
  `experimental/scripts/`, and Lean modules/packages under `experimental/lean/`.
  Rehomed `experimental/rsmca_certificates_notes.md` into
  `experimental/notes/certificates/`.  Imported the L1 official-row crosswalk
  as `experimental/notes/l1/l1_official_rows_crosswalk_20260713.md` rather than
  applying its root `towards-prize.md` promotion text.  Contributor
  `experimental/agents-log.md` edits were not imported.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT,
  as stated in the individual notes. No stable paper `.tex` or `.pdf` theorem
  is promoted by this entry.
- **What is being added:** Rank-15 and rank-16 Grand List route cuts, weighted
  GRS packing and cyclic half-footprint compilers, selector-free exact-weight
  and LineRay refinements, selected-owner unit-layer equivalence/audit data,
  the heavy-fiber hypothesis repair, toy-case Lean certificates, an official-row
  L1 crosswalk, and the deployed axis g-damping lattice sublemma.
- **How it is useful:** The wave repairs a previously false heavy-fiber center
  hypothesis, adds several narrow theorem/counterexample packets for the current
  finite threshold program, and records a potentially important L1 official-row
  discharge as an experimental crosswalk pending in-repo audit of its external
  proof trail.
- **What to do next:** Audit the L1 crosswalk against in-repo proof artifacts
  before promoting roadmap language; run the verifier scripts and Lean builds in
  a dedicated environment; decide whether the rank-15/16 and axis-g-damping
  packets should be summarized in `asymptotic_rs_mca.md` or `grande_finale.tex`.

### 2026-07-13 - Threshold, C9, LineRay, Lean, and audit PR wave

- **Agent/model:** Codex integrating PRs #723--#741 from holmbuar and
  DannyExperiments.
- **Files added or changed:** Added threshold/audit/L2 notes under
  `experimental/notes/`, exact certificate JSON and verifier output under
  `experimental/data/certificates/`, verifier scripts under
  `experimental/scripts/`, and Lean modules/packages under `experimental/lean/`.
  Shared Lean aggregators were edited manually to keep all imports:
  `experimental/lean/grande_finale/GrandeFinale.lean` and
  `experimental/lean/first_match_atlas/FirstMatchAtlas.lean`. Contributor
  `experimental/agents-log.md` edits were not imported; this entry is the
  integration log.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT,
  as stated in the individual notes. No stable paper `.tex` or `.pdf` theorem
  is promoted by this entry.
- **What is being added:** A large experimental wave around the v13 threshold
  program: signed-minor clause census, exact deep MCA Lean numerators, C3
  planted census, general-R Weil-cycle flatness, first-match signed-gain and
  pruned signed bounds, rational-host nonpositive extraction, owner-rooted and
  pay-per-bit audits, charge-preserving split decomposition, heavy-prefix
  precursor emission, Sidon-paired staircase-concentration counterexample,
  full-slice C9 odd-axis Fourier budget, all-LineRay affine-core and
  direction-distance packets, plus Danny's L2 rank-15 degree floor and
  anti-host prefix compiler.
- **How it is useful:** These packets sharpen the current finite/asymptotic
  threshold proof program while preserving conservative status labels. Several
  items are route-cuts or audits rather than new leaderboard records; the Lean
  additions expand formalization coverage but were not lake-built here.
- **What to do next:** Human-audit the notes before promotion into
  `asymptotic_rs_mca.tex`, `grande_finale.tex`, or Paper D; run the verifier
  scripts and Lean builds in a dedicated environment; decide whether the C9,
  LineRay, signed-minor, and planted-census packets close specific residual
  proof obligations or only narrow them.

### 2026-07-13 - Reed--Solomon MCA Thresholds exact-threshold draft

- **Agent/model:** Maintainer-added paper, integrated and audited by Codex.
- **Files added or changed:** `experimental/rs_mca_thresholds.tex`,
  `experimental/rs_mca_thresholds.pdf`,
  `experimental/rs_mca_thresholds_audit.md`, `AGENTS.md`, `readme.md`,
  `site/index.html`, `experimental/agents-log.md`.
- **Status:** SUBMISSION DRAFT / PROVED WHERE STATED / AUDIT.
- **What is being added:** A coherent exact-threshold paper that packages the
  CA/sparse MCA decomposition, exact deep and quadratic MCA staircases,
  self-contained half-Johnson bounds, four certified Proth prime rows at the
  official rates, the `F_17^32` 6/7 gate, smooth/circle transports, and
  target-aware certificate formulas.
- **How it is useful:** This is now the cleanest entry point for exact MCA
  threshold work.  It is better organized than `asymptotic_rs_mca_frontiers.tex`
  for finite/deep theorems, while the older frontiers draft remains useful for
  broader conditional profile-envelope and cell-budget machinery.
- **What to do next:** Independently audit the four Proth certificates, endpoint
  conventions, exact CA/sparse decomposition, and quadratic mean-overlap theorem;
  then decide whether to promote this as the main experimental submission draft
  and produce machine-readable row certificates.

### 2026-07-13 - Lower-reserve, A6, L2, dense-band, and LineRay PR wave

- **Agent/model:** Codex integrating PRs #699--#722 from
  DannyExperiments, holmbuar, avdeevvadim, and latifkasuli.
- **Files added or changed:** Added threshold, L2, and audit notes under
  `experimental/notes/`, verifier/reproducer scripts under
  `experimental/scripts/`, and certificate JSON under
  `experimental/data/certificates/`.  Updated the existing A6
  line-section compiler and corridor-diameter-map packets.  Contributor
  `experimental/agents-log.md` changes and `experimental/scripts/README.md`
  churn were not imported; this entry is the integration log.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT,
  as stated in the individual notes.  No stable paper `.tex` or `.pdf`
  theorem is promoted by this entry.
- **What is being added:** A follow-up wave for the current frontier program:
  lower-reserve O5c/two-regime/deep-remainder packets, LineRay
  re-recording and rational-host compiler material, L2 affine/interleaved
  reductions, A6 transverse/all-witness and atlas-print audits, rooted
  order-two/dense-band localization packets, heavy-fiber admissibility
  transfer, growing-characteristic R2 flatness, signed local-minority
  fixed-composition Q, projective-line lift wall, and rank-15 locator
  saturation normal form.  The wave also records negative route decisions:
  the fenced-window repair, energy-pincer failure, habitat denominator
  wall, field-drop/deep-remainder correction, and remaining LineRay/list
  walls.
- **How it is useful:** The batch sharpens several active obligations rather
  than hiding them.  It converts lower-reserve list routes through more exact
  objects, moves raw support-count targets toward deduplicated `LineRay`
  counts, reduces all-arity L2 to a one-row maximum, strengthens A6
  per-line transverse payments, and localizes dense-band failures to
  owner-rooted packets that still need a signed or semantic payment.
- **What to do next:** Do not promote these claims into Paper D/frontiers
  without a separate audit.  Immediate useful follow-ups are: finish the
  LineRay/saturated-BC target, prove the remaining one-row list inequality
  after the L2 reductions, decide the deep-remainder scaling opened by
  #714, and connect the owner-rooted dense-band packets to a genuine
  CAT/RC/Sidon payment rather than an arbitrary-mask model.

### 2026-07-12 - A6, L2, ILO, B2, and lower-reserve PR wave

- **Agent/model:** Codex integrating PRs #658--#698 from
  DannyExperiments, holmbuar, avdeevvadim, latifkasuli, and
  scottdhughes.
- **Files added or changed:** Added notes under `experimental/notes/`,
  verifier/reproducer scripts under `experimental/scripts/`, and JSON or
  text certificates under `experimental/data/certificates/`.  Updated
  `experimental/notes/l2/l2_sharp_target_conjecture.md` and
  `experimental/notes/roadmaps/b2_hankel_gauss_reduction.md`.  The B2
  CHG bridge note was patched during integration to mark the B53 target as
  refuted by the new B53 packet.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT,
  as stated in the individual notes.  No stable paper `.tex` or `.pdf`
  theorem is promoted by this entry.
- **What is being added:** A large experimental batch around the active
  asymptotic and finite-threshold program.  The L2 notes correct the repeated
  row target, add baseline-plus-excess codegree recursion, and expose the
  exact low layer before the doubly-high residual.  The A6 notes add
  projective/descent, completed-Cramer, zero-mask, higher-order mask-rank,
  and selector-free line-section payments.  The ILO/image-face chain records
  Fourier/Bohr route cuts, Danny's VC-compression image atom, the
  unconditional `rho <= log(3/2)` cap, corridor audits, and a new computed
  champion `rho=0.160847`.  The B2 packets add a twisted Hankel transform and
  CHG normalization bridge, then the Scott Hughes refutation showing the B53
  sufficient target is false at reachable rows.  Lower-reserve and profile
  packets add exact full-field first-row MCA lower bounds, moved-pair dyadic
  rung audits, and profile-envelope completeness audits.
- **How it is useful:** Several old walls become sharper: ILO image-size
  payment is no longer merely conjectural in the stated image atom form;
  B53 is no longer a live target; the L2 and R1 notes prevent raw support
  overcounting; and the A6 packets pay additional strict strata while naming
  the central remaining bands.  The finite lower-reserve notes make the
  first unsafe rows and moved deployed-pair rung margins more auditable.
- **What to do next:** Do not cite any of these as Paper-D authority until
  separately promoted.  For proof progress, reconcile the closed ILO-image
  atom with the still-open post-atlas block/fiber typing, replace B53 with a
  viable signed or positive-band B2 target, keep the L2 doubly-high residual
  explicit, and audit the lower-reserve packets against the current
  `asymptotic_rs_mca_frontiers.tex`/`cap25` drafts.

### 2026-07-11 - ADE repair and ILO threshold PR wave

- **Agent/model:** Codex integrating PRs #647--#657 from holmbuar and
  DannyExperiments.
- **Files added or changed:** Added threshold notes under
  `experimental/notes/thresholds/`, updated
  `experimental/notes/audits/lean_frontiers_primitive_boolean.md`, added
  verifier/reproducer scripts under `experimental/scripts/`, and added JSON
  certificates under `experimental/data/certificates/`.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT,
  as stated in the individual notes.  No main-paper theorem is promoted by
  this entry.
- **What is being added:** A follow-up threshold batch after the #637 M31 ADE
  packet.  PR #648 independently audits #637: the census counts are confirmed,
  while one integral-coordinate `D_s` proof subcase is identified as a narrow
  proof-completeness gap.  PR #653 supplies the repair, and PR #654 extends
  the repaired M31 `kappa=2` classifier from `t>=277868` to `t>=276416`,
  adding 1,452 exclusions and reducing the two-shell residual ledger to
  2,985,960 rows.  The remaining notes cover collapse-field-cost
  counterexamples, characteristic-three Witt carries, span-face synthesis,
  Case-B equidistribution evidence, Boolean-energy self-contained bounds,
  fiber-image tradeoff and `(ILO-moment)` reductions, and a weighted
  quotient-major compiler.
- **How it is useful:** The M31 line changes the status of #637 from
  "proved but audit pending" to "audited, repaired, and extended" inside
  `experimental/`.  The ILO/fiber-image notes isolate a concrete
  exponential-concentration inverse Littlewood--Offord style lemma as the
  remaining wall for that route.  The collapse and Case-B notes prevent
  overclaiming by showing where simple counting or field-cost shortcuts fail.
- **What to do next:** Treat the repaired ADE classifier as experimental
  theorem material until it is cited or promoted by a separate paper edit.
  Do not run the heavier reproducer scripts casually.  For proof progress,
  focus on the named `(ILO-moment)`/exponential inverse-LO input and the
  remaining M31 residual ledger rows.

### 2026-07-11 - Routing, saturation, and M31 ADE PR wave

- **Agent/model:** Codex integrating PRs #622--#646 from holmbuar,
  DannyExperiments, and the `grande_finale` Lean formalization track.
- **Files added or changed:** Added threshold and roadmap notes under
  `experimental/notes/`, verifier/reproducer scripts under
  `experimental/scripts/`, M31/orientation JSON certificates under
  `experimental/data/`, and `GrandeFinale/CollisionAwarePole.lean` plus its
  correspondence note under `experimental/lean/grande_finale/`.
- **Status:** PROVED / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT /
  FORMALIZATION, as stated in the individual notes.  No main-paper theorem is
  promoted by this entry.
- **What is being added:** A routing/saturation batch for the active
  frontiers program: C7 routing-spectrum and collapse-payment repairs,
  orientation and thick-form comparisons, PTE/moment-map max-fiber results,
  field-of-definition and FI-field discharge notes, simple-pole saturation
  controls, and M31 finite-grid reductions.  PR #637 is integrated as a
  genuine proved experimental theorem: the common-height ADE cut excludes
  113,864 additional M31 `kappa=2` residual rows and reduces that two-shell
  residual ledger to 2,987,412 rows.
- **How it is useful:** The batch sharpens several previously vague hard-input
  walls into specific route cuts or paid cells.  The M31 ADE cut is a concrete
  finite improvement to the residual-row ledger, while #646 decides the
  degree-2 moment-map max-fiber rate `phi* = log 2`, revising #643's earlier
  conjectural constant.
- **What to do next:** Audit #637's ADE/root-count argument and exact ledger
  delta before citing it outside `experimental/`.  Continue treating the
  remaining saturation/collapse/profile statements as input-specific until
  their hypotheses are matched against `asymptotic_rs_mca_frontiers.tex`.

### 2026-07-11 - Aperiodic one-ray saturation route cut

- **Agent/model:** Codex integrating PR #621 by DannyExperiments.
- **Files added or changed:** `experimental/notes/thresholds/aperiodic_one_ray_saturation.md`,
  `experimental/scripts/verify_aperiodic_one_ray_saturation.py`, and
  `experimental/agents-log.md`.
- **Status:** PROVED route cut / AUDIT, as stated in the note.
- **What is being added:** A characteristic-two smooth-family example showing
  that an exponentially large, multiplicatively aperiodic refined prefix fiber
  can project to a single pole-line slope after constant-coefficient
  saturation.
- **How it is useful:** Clarifies that positive prefix entropy plus
  aperiodicity is not enough for an unsafe primitive lower reserve; future
  unsafe-side compilers need a distinct-ray theorem or a quantitative
  first-match saturation-overlap bound.
- **What to do next:** Audit the route cut against the current first-match
  ordering used in the frontiers paper before promoting any wording beyond
  `experimental/`.

### 2026-07-11 - L1/C9/frontiers PR integration wave

- **Agent/model:** Codex integrating PRs #562--#620 from LegaSage,
  scottdhughes, latifkasuli, avdeevvadim, AllenGrahamHart,
  DannyExperiments, and holmbuar.
- **Files added or changed:** Added Lean packages under `experimental/lean/`
  for exact adjacent rows, first-match atlas bounds, deep-regime upper bounds,
  threshold brackets, first-occurrence/disjoint-union/sum-of-squares lemmas,
  Boolean-fiber growth, and `grande_finale` challenge/profile-window modules;
  added audit/certificate JSON under `experimental/data/`; added threshold,
  roadmap, DLI, EF, and audit notes under `experimental/notes/`; added verifier
  and exploratory scripts under `experimental/scripts/`.
- **Status:** PROVED / CONDITIONAL / COUNTEREXAMPLE / EXPERIMENTAL / AUDIT /
  FORMALIZATION, as stated in the individual notes.  No main-paper theorem is
  promoted by this entry.
- **What is being added:** A large support batch for the current asymptotic and
  finite-threshold program: L1/B2 max-fiber reduction material, C9/Sidon and
  packed-flatness packets, first-match atlas exhaustiveness checks, profile
  window and challenge-intersection formalization, finite F2/F3 guardrail
  packets, M31/subgroup recursion audits, and new ray/occupancy compiler notes.
- **How it is useful:** The batch expands the audit trail for the five active
  hard inputs while keeping unresolved hypotheses explicit.  Several notes
  sharpen failures or walls rather than closing them; those are integrated as
  useful counterexample/guardrail material.  The Lean additions increase the
  reusable formalization surface but were not built during this integration.
- **What to do next:** Audit each claimed proof before moving anything into
  `experimental/asymptotic_rs_mca_frontiers.tex` or Paper D.  Some L1/B2
  literature-search scripts call the TheoremSearch API and were not executed;
  run them only deliberately.  Continue focusing on the remaining max-fiber,
  Sidon/payment, profile-envelope, and finite unsafe/safe comparison inputs.

### 2026-07-10 - Syndrome, profile, and finite-kernel PR packets

- **Agent/model:** Codex integrating PRs #544--#561 from holmbuar,
  LegaSage, DannyExperiments, avdeevvadim, and local maintainer-facing Lean
  additions.
- **Files added or changed:** Added threshold notes and verifier scripts for
  simple-pole realizability, Gap-2/Frobenius-collapse routing, M31
  rank-inertia and multi-anchor SOS cuts, direction-distance ray compilation,
  and the primitive-profile character-frame certificate; added Lean packages
  under `experimental/lean/` for saturation identity, bounded-kernel rays,
  second-moment identity, effective closure, razor-band witness, rigidity
  census, petal fiber, integer staircase, moment-to-max, syndrome-line,
  syndrome-secant, and the `grande_finale` syndrome-line compiler.
- **Status:** PROVED / EXPERIMENTAL / AUDIT / FORMALIZATION, as stated in the
  individual notes.  No main-paper claim is promoted by this entry.
- **What is being added:** A new frontiers-support batch around the remaining
  hard inputs: unsafe-side simple-pole realizability, profile/envelope routing,
  residual-ray compiler branches, primitive-profile character-frame payment,
  M31 finite reductions, and Lean formalization anchors for exact finite
  identities and syndrome-line normal forms.
- **How it is useful:** The simple-pole and Gap-2 packets strengthen the
  audit trail for lower-reserve and profile-envelope routing.  The
  character-frame packet offers a possible replacement interface for absolute
  Fourier/MI+MA payment while explicitly leaving the source-specific packing
  input open.  The Lean additions expand the formalization surface without
  running repository-wide builds.
- **What to do next:** Audit the mathematical hypotheses before moving any
  statement into `experimental/asymptotic_rs_mca_frontiers.tex`.  For Lean,
  build each small package only in isolation when needed; continue formalizing
  the `grande_finale` and v13/frontiers targets.

### 2026-07-10 - Identity-window and finite-prize theory packets

- **Agent/model:** Codex integrating PR #542 by holmbuar and PR #543 by
  AllenGrahamHart.
- **Files added or changed:** `experimental/notes/thresholds/envelope_identity_window.md`,
  `experimental/scripts/verify_envelope_window.py`,
  `experimental/notes/thresholds/cap25_finite_census_necessary_hypotheses.md`,
  `experimental/notes/thresholds/cap25_finite_signed_census_frame.md`,
  `experimental/notes/thresholds/cap25_finite_deep_regime_exactness.md`,
  `experimental/notes/roadmaps/finite_prize_kernel_basis.md`, and their
  verifier scripts.
- **Status:** PROVED / AUDIT / EXPERIMENTAL / ROADMAP, as stated in the
  individual notes.
- **What is being added:** A profile-envelope identity-dominance window note
  that turns the comparison premise into a row-checkable two-window criterion,
  plus finite-track packets recording necessary hypotheses for census
  statements, signed census identities, deep-regime exactness, and a
  three-kernel finite-prize roadmap.
- **How it is useful:** #542 directly targets the complete profile-envelope
  comparison hard input by separating no-field-drop rows from field-drop
  failure bands. #543 parks finite-prize theory infrastructure without
  changing the asymptotic submission draft.
- **What to do next:** Audit the identity-window criterion against
  `experimental/asymptotic_rs_mca_frontiers.tex` before promotion.  Keep the
  finite-track packets parked until the project pivots from the asymptotic
  proof to exact finite-prize threshold closure.

### 2026-07-10 - Frontiers hard-input PR integration

- **Agent/model:** Codex integrating PRs #494--#541 from holmbuar,
  LegaSage, DannyExperiments, scottdhughes, and latifkasuli.
- **Files added or changed:** Added audit/certificate JSON under
  `experimental/data/`, verifier scripts under `experimental/scripts/`, notes
  under `experimental/notes/audits/`, `experimental/notes/thresholds/`, and
  `experimental/notes/roadmaps/`, plus Lean source packages under
  `experimental/lean/`.  Contributor edits to `experimental/agents-log.md`
  and generated `.lake` build artifacts were deliberately not imported.
- **Status:** AUDIT / EXPERIMENTAL / COUNTEREXAMPLE / FORMALIZATION.
- **What is being added:** A large reviewed batch around the current
  `asymptotic_rs_mca_frontiers` hard inputs: first-match atlas audits,
  image-scale MI/MA and Sidon-payment audits, residual-ray compiler audits,
  profile-envelope and lower-reserve comparisons, finite-source and deployed
  replay templates, M31/KoalaBear threshold packets, C9/Route-D notes, and
  several small zero-sorry Lean formalization packages for toy anchors,
  deployed brackets, first-match partitioning, anticode packing, moving-root
  incidence, profile-envelope/staircase cores, and Vandermonde/prefix-flatness
  scaffolding.
- **How it is useful:** Banks the current open-PR work without changing the
  main papers.  The strongest practical value is a sharper map of what is
  already audited, what remains an open gap, and what has a small formal or
  executable witness.  The batch also records a split-pencil raw-census
  counterexample/repair direction and keeps it separate from slope-deduplicated
  statements.
- **What to do next:** Audit theorem claims one by one before promotion into
  `asymptotic_rs_mca_frontiers.tex` or Paper D.  Treat the submitted verifier
  scripts as replay aids only until their mathematical assumptions are checked.
  Continue the five hard-input program: witness-exhaustive first-match atlas,
  image-scale MI+MA or direct Sidon payment, residual ray compiler, complete
  profile-envelope comparison, and lower reserve / unsafe-side comparison.

### 2026-07-10 - Asymptotic RS--MCA Frontiers replacement draft

- **Agent/model:** Maintainer-added replacement paper, integrated by Codex.
- **Files added or changed:** `experimental/asymptotic_rs_mca_frontiers.tex`,
  `experimental/asymptotic_rs_mca_frontiers.pdf`,
  `experimental/rs_mca_entropy_frontiers.tex`,
  `experimental/rs_mca_entropy_frontiers.pdf`, `AGENTS.md`,
  `experimental/agents-log.md`.
- **Status:** SUBMISSION DRAFT / CONDITIONAL / AUDIT.
- **What is being added:** Replaced the earlier `RS--MCA Entropy Frontiers`
  draft with the current `Asymptotic RS--MCA Frontiers` manuscript.  The new
  draft is larger and more explicit: it records exact deep-target and
  shallow-prefix results, exact quotient/remainder and partial-occupancy
  infrastructure, effective-span Fourier inversion, finite occupancy and
  ray/compiler interfaces, and a clearer statement of what remains conditional.
- **How it is useful:** This is now the main self-contained asymptotic RS MCA
  submission draft.  It consolidates the theorem package while making the
  remaining hard inputs explicit instead of hiding them behind older Q/BC/SP
  shorthand.
- **What to do next:** Attack the five remaining inputs directly:
  witness-exhaustive first-match atlas; image-scale MI+MA or direct Sidon
  payment; residual ray compiler for higher-dimensional balanced cores;
  complete profile-envelope comparison with the target; and lower
  reserve/unsafe-side comparison.

### 2026-07-10 - RS--MCA Entropy Frontiers submission draft

- **Agent/model:** Maintainer-added paper, read and logged by Codex.
- **Files added or changed:** `experimental/rs_mca_entropy_frontiers.tex`,
  `experimental/rs_mca_entropy_frontiers.pdf`, `experimental/agents-log.md`.
- **Status:** SUBMISSION DRAFT / CONDITIONAL / AUDIT.
- **What is being added:** A long self-contained asymptotic RS MCA paper draft
  intended to become the submission track once finished.  It consolidates the
  RS/MCA definitions, exact finite-row syndrome geometry, locator-prefix and
  collision-aware pole-line lower bounds, quotient/remainder profile
  obstructions, the profile-envelope compiler, the primitive Sidon/BSG/Q
  implication, smooth/circle domain interfaces, target-aware threshold
  bookkeeping, row-by-row verification templates, and finite-source certificate
  integration.
- **How it is useful:** This is now the most complete single-paper presentation
  of the asymptotic RS MCA program: it is designed to replace scattered notes by
  a coherent submission manuscript with proofs, hypotheses, counterexamples,
  and explicit remaining ledger obligations in one place.
- **What to do next:** Audit it theorem by theorem against
  `experimental/asymptotic_rs_mca.tex`, `experimental/cap25_cap_v13_raw.tex`,
  `experimental/grande_finale.tex`, and the latest C9/profile-envelope audit
  packets.  In particular, verify that every conditional compiler input,
  Fourier/Sidon payment, major-arc aggregate, profile-envelope comparison, and
  ray-compiler claim is either proved in the paper or clearly labeled as an
  assumption before treating it as the final asymptotic submission.

### 2026-07-10 - Audit-safe Asymptotic RS MCA paper update

- **Agent/model:** Codex, using latest audit/support PR packets from holmbuar,
  LegaSage, and DannyExperiments.
- **Files added or changed:** `experimental/asymptotic_rs_mca.tex`,
  `experimental/asymptotic_rs_mca.pdf`, `experimental/asymptotic_rs_mca.md`,
  `experimental/agents-log.md`.
- **Status:** PROMOTED / AUDIT.
- **What is being added:** Updated the asymptotic paper to incorporate the safe
  consequences of the latest PR wave: the abstract now uses the defined
  target-adjusted crossing language; the C8 split-pencil paragraph no longer
  overstates residual higher-dimensional chart closure; the C9 paragraph
  records restricted payments and route cuts without claiming full exhaustion;
  and a new audit-status remark cites the profile-envelope audit, numerical
  spine, C9 support packets, and finite star3 threshold packets.
- **How it is useful:** Aligns the paper with the current audit record while
  preserving the conditional status of the remaining safe-side proof
  obligations.
- **What to do next:** Prove or refute the residual split-pencil/C9 obligations
  at the printed profile scale, then promote only those pieces with exact RC
  image bounds or clearly named assumptions.

### 2026-07-10 - Profile-envelope audits, C9 support, and threshold wall packets

- **Agent/model:** holmbuar via PRs #481, #482, #483, #484, #490, and #492;
  LegaSage via PR #491; DannyExperiments via PRs #485, #486, #487, #488, and
  #489; Codex for selective integration, audit synthesis, and lightweight
  checks.
- **Files added or changed:** Added audit notes under
  `experimental/notes/audits/`, threshold notes under
  `experimental/notes/thresholds/`, JSON/data artifacts under
  `experimental/data/`, verifier scripts under `experimental/scripts/`, a Lean
  package under `experimental/lean/m31_few_shell/`, and a consolidated entry in
  `experimental/asymptotic_rs_mca.md`.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT.
- **What is being added:** Integrated the latest non-paper PR artifacts without
  changing `experimental/asymptotic_rs_mca.tex` or its PDF.  The batch includes
  a profile-envelope line-by-line audit, deployed-row numerical checks, five
  C9 support/route-cut packets, KoalaBear `star3` point-count and second-moment
  wall notes, an M31 shell-pair LP ruleout packet, and Lean formalization of
  the M31 few-shell theorem core.
- **How it is useful:** This preserves the new material in the right layer:
  the profile-envelope paper gets an audit checklist first, C9 receives local
  tools but not an overclaimed theorem, and the threshold notes identify
  concrete next analytic targets rather than hiding them in prose.
- **What to do next:** Audit PR #483's two open gaps before paper edits; use the
  C9 packets only when their hypotheses match the residual class; continue the
  `star3` work from the explicit point-count/signed-cancellation target; and
  keep the Lean package under `experimental/lean/` until it is independently
  built by a formalization contributor.

### 2026-07-10 - Promote profile-envelope Asymptotic RS MCA draft

- **Agent/model:** Maintainer-added TeX reviewed and promoted by Codex.
- **Files added or changed:** `experimental/asymptotic_rs_mca.tex`,
  `experimental/asymptotic_rs_mca.pdf`, `experimental/asymptotic_rs_mca.md`,
  `experimental/agents-log.md`.
- **Status:** PROMOTED / CONDITIONAL / COUNTEREXAMPLE.
- **What is being added:** Replaced the earlier compact asymptotic paper with
  the stricter profile-envelope version.  The new draft keeps the
  BSG/quasicube high-energy elimination but makes the main theorem conditional
  on a closed profile ledger, residual Sidon payment, and a distinct-ray
  compiler.  It also adds a smooth quotient/Sidon/MCA obstruction showing that
  the identity-prefix average alone is not a valid unconditional upper scale.
- **How it is useful:** This incorporates the main audit findings from the
  `asymptotic_rs_mca.md` ledger: B1/image normalization, add-back, lower-side
  pole collisions, literal C9, and Q/SP-vs-ray issues are now visible in the
  statement rather than hidden in the proof.
- **What to do next:** Audit every cell payment and the new obstruction proof
  against `experimental/cap25_cap_v13_raw.tex`,
  `experimental/grande_finale.tex`, and the recent audit packets.  The next
  paper revision should either prove the remaining profile/RC hypotheses in a
  named setting or keep them explicitly conditional.

### 2026-07-10 - Remaining PR integration: asymptotic audits and threshold packets

- **Agent/model:** holmbuar via PRs #431, #433, #437, #443, #446, #447,
  #479, and #480; LegaSage via PRs #450, #452, #453, #454, #455, #456,
  #457, and #458; DannyExperiments via PRs #432, #449, and #451;
  scottdhughes via PR #448; avdeevvadim via PR #444; latifkasuli via PR #436;
  Codex for review, selective integration, audit-ledger synthesis, and
  lightweight checks.
- **Files added or changed:** Added audit and threshold notes under
  `experimental/notes/`, `experimental/notes/audits/`,
  `experimental/notes/m1/`, and `experimental/notes/thresholds/`; certificates
  and data under `experimental/data/`; verifier scripts under
  `experimental/scripts/`; updated the paper-audit companion
  `experimental/asymptotic_rs_mca.md`.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT /
  COUNTEREXAMPLE.
- **What is being added:** Integrated the remaining non-paper artifacts around
  the asymptotic proof audit, B1/image normalization, C9 specification and
  subregimes, Route-D barrier map, M31/KoalaBear threshold walls, Q-to-SP,
  BC/tangent/extension/SPI toy audits, L1 petal residuals, and finite-vs-
  asymptotic frontier checks.
- **How it is useful:** This batch preserves the proof-review trail without
  directly editing `experimental/asymptotic_rs_mca.tex` or its PDF.  The
  imported material identifies concrete paper-revision candidates, hard
  residual cells, and several route cuts or toy confirmations while keeping
  deployed adjacent safe rows unclaimed.
- **What to do next:** Do not promote these notes by copy-paste.  First write a
  maintainer-authored paper revision using `experimental/asymptotic_rs_mca.md`
  as the checklist, reconcile the C9/Q residual predicate, and run selected
  verifier scripts only when their cost is acceptable.  PRs #438, #440, #445,
  and #434 were reviewed as superseded by later integrated material rather than
  applied over the newer Lean/threshold files.

### 2026-07-10 - Asymptotic paper audit ledger and C9 support packets

- **Agent/model:** DannyExperiments via PRs #463 and #464; scottdhughes via
  PRs #465 and #466; LegaSage via PRs #459, #460, #461, and #462; Codex for
  selective integration, audit-ledger synthesis, and lightweight checks.
- **Files added or changed:** Created `experimental/asymptotic_rs_mca.md`.
  Added C9/endpoint notes under `experimental/notes/thresholds/`, second-opinion
  audit notes under `experimental/notes/audits/`, certificates under
  `experimental/data/certificates/`, Lean Frobenius support under
  `experimental/lean/powersum_rigidity/`, and verifier scripts under
  `experimental/scripts/`.
- **Status:** PROVED / EXPERIMENTAL / AUDIT.
- **What is being added:** A paper-level audit ledger for
  `experimental/asymptotic_rs_mca.tex`, plus support packets for endpoint
  Plotkin shortening, split-prime Parseval descent, C9 major-arc value-set
  structure, Frobenius-closure Lean backing, and independent second-opinion
  checks of Stirling/`g*`, sigma-block diagonal, BSG/quasicube, and pole-line
  division steps.
- **How it is useful:** Preserves proposed or supporting paper-level material
  without directly changing the `.tex`/`.pdf`.  The imported packets help audit
  the asymptotic proof route, especially the primitive C9/Q discussion, while
  keeping the deployed finite adjacent safe row unclaimed.
- **What to do next:** If `asymptotic_rs_mca.tex` is revised, use
  `experimental/asymptotic_rs_mca.md` as the source audit checklist.  Full
  verifier runs and Lean builds were intentionally not run here; only Python
  syntax, JSON validity, and Lean placeholder-marker scans were checked.

### 2026-07-10 - PR batch: Lean spine and threshold audit packets

- **Agent/model:** holmbuar via PRs #474, #475, #476, #477, and #478;
  LegaSage via PRs #469, #470, #471, #472, and #473; holmbuar via PRs #467
  and #468; Codex for selective integration, lightweight review, and log
  consolidation.
- **Files added or changed:** Added the new
  `experimental/lean/asymptotic_spine/` package and updated
  `experimental/lean/grande_finale/` with `QFiniteTables` and the sharper
  `SP` diagonal-subtraction formulation. Added audit/certificate packets under
  `experimental/notes/audits/`, `experimental/notes/thresholds/`, and
  `experimental/data/`, with corresponding verifier scripts under
  `experimental/scripts/`.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT.
- **What is being added:** The batch records formalization support for the
  asymptotic spine and Grande Finale finite Q tables, plus small certificate
  packets for first-match, entropy-threshold, Fourier/Sidon, Boolean-prefix,
  bad-line-strata, Route-D sparse-arc, KoalaBear mixed-orbit, Mersenne-31
  Chebyshev/signed-`e_m`, and KoalaBear signed-`e_m` scaled-toy audits.
- **How it is useful:** These packets support the current `asymptotic_rs_mca`
  and v13/Grande Finale proof program without changing the paper TeX/PDFs.
  They mostly sharpen audit infrastructure, formalization maps, and local
  threshold evidence; none is promoted here as a deployed adjacent safe row.
- **What to do next:** Review the mathematical claims before paper promotion,
  especially the Q/BC/SP safe-side uses. Full verifier runs and Lean builds were
  intentionally not run in this integration pass; only Python syntax, JSON
  validity, and Lean `sorry`/`admit`/`axiom` marker scans were checked.

### 2026-07-09 - Asymptotic RS MCA closed-ledger proof paper

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/asymptotic_rs_mca.tex`,
  `experimental/asymptotic_rs_mca.pdf`, `experimental/agents-log.md`.
- **Status:** PROVED / CONDITIONAL.
- **What is being added:** A compact amsart paper titled `Asymptotic RS MCA`
  consolidating the moduli-ledger drafts with the v13 raw and Grande Finale
  ledgers.  It states the closed paid ledger package explicitly, defines the
  cells `(C1)--(C9)`, cites the existing ledger results for their payments, and
  proves the asymptotic MCA frontier via the Sidon/Fourier cut, BSG, quasicube
  difference growth, primitive Q, Q-to-SP, and the identity-prefix lower side.
- **How it is useful:** This is the current compact prize-facing proof route
  for the asymptotic RS-MCA threshold: once the imported closed-ledger package
  is accepted from `cap25_cap_v13_raw.tex`, `grande_finale.tex`, and the
  moduli-ledger notes, no additional entropy-Freiman or rank-derivative
  theorem is needed for primitive Q.
- **What to do next:** Audit the cited closed-ledger package line by line
  against v13 raw and Grande Finale labels, then decide whether to promote this
  paper or merge its theorem/proof into the next main Paper D/towards-prize
  revision.

### 2026-07-09 - Reviewed PR integration for entropy-inverse, row-sharp Q, BC, and Route-D packets

- **Agent/model:** Holm Buar via PRs #414-#418, #420-#422, and #427-#430;
  AllenGrahamHart via PR #419; Scott Hughes via selected material from PR #423;
  DannyExperiments via PRs #424 and #426; Vadim Avdeev via PR #425; Codex for
  review, selective integration, and log consolidation.
- **Files added or changed:** Added Q/threshold notes under
  `experimental/notes/thresholds/`; a BC note under
  `experimental/notes/bc_near_pencil_chart_reduction.md`; a Lean audit under
  `experimental/notes/audits/lean_grande_finale_correspondence_audit.md`; L1
  stabilization material under `experimental/notes/l1/`; data and certificates
  under `experimental/data/`; verifier and audit scripts under
  `experimental/scripts/`; updated `experimental/scripts/README.md` with the
  singleton top-seam verifier commands.  PR #423 was deliberately reduced to its
  canonical status note and the high-signal packets v25, v45, v46, v48, v49,
  v51, v53, and v54 rather than importing the full v1-v54 archive.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT / COUNTEREXAMPLE.
- **What is being added:** Integrated a batch of experimental packets around the
  current v13/Grande Finale bottlenecks: signed-`e_m` and masked participation
  ratio reformulations, the lift-class cost-model refutation, entropy-inverse
  toy dichotomy and missing-cell hunts, the `F_p`-span cell and its codimension,
  surjection, connectivity, and residual-control follow-ups, a row-sharp Q
  singleton top-seam Route-D compiler, a Q moment-floor route cut, the M31
  Chebyshev fixed-remainder floor audit, the BC near-pencil chart reduction,
  an L1 k3 record-stabilization extension, and a textual correspondence audit
  for the Grande Finale Lean package.
- **How it is useful:** The batch sharpens the proof map without claiming a
  deployed adjacent safe row.  The entropy-inverse material identifies and
  measures an `F_p`-span obstruction cell and distinguishes theorem-level toy
  facts from measured evidence.  The Q and Route-D packets clarify which
  shortcut payment routes are dead, conditional, or still open.  The BC packet
  reduces one saturated-chart family to a split-in-subspace residual tied to
  the existing Q/BC frontier.  The Lean audit records concrete docstring/label
  drift to fix before relying on the formalization as a paper map.
- **What to do next:** Do not promote these packets into Paper D or
  `grande_finale.tex` as theorem rows without separate proof review.  The next
  useful steps are: prove the row-sharp Q max-fiber bound or a precise residual
  cell theorem; close the BC chart decomposition beyond the near-pencil family;
  attack Scott's remaining Route-D wall `|T| <= H2`; fix the documented Lean
  label drift; and run selected verifier scripts only when their cost is
  acceptable for the local environment.

### 2026-07-08 - Grande Finale Lean package normalization

- **Agent/model:** Maintainer-added Lean files integrated by Codex.
- **Files added or changed:** `experimental/lean/grande_finale/GrandeFinale.lean`;
  `experimental/lean/grande_finale/GrandeFinale/BC.lean`;
  `experimental/lean/grande_finale/GrandeFinale/SP.lean`;
  `experimental/lean/grande_finale/GrandeFinale/Frontier.lean`;
  `experimental/lean/grande_finale/GrandeFinale/QFourierTao.lean`;
  `experimental/lean/grande_finale/GrandeFinale/QEntropyInverse.lean`;
  `experimental/lean/grande_finale/GrandeFinale/QPrimitiveCollision.lean`;
  `experimental/lean/grande_finale/README.md`;
  `experimental/lean/grande_finale/FORMALIZATION_SUMMARY.md`;
  `experimental/lean/grande_finale/lakefile.toml`;
  `experimental/lean/grande_finale/lake-manifest.json`.
- **Status:** FORMALIZATION / AUDIT.
- **What is being added:** Normalized the new Grande Finale Lean files away
  from placeholder `RequestProject` module names.  The package root is now
  `GrandeFinale`, with submodules under `GrandeFinale/`; package docs summarize
  the formalized kernels around Q, BC, SP, the frontier ledger, and
  log-moment/Fourier reductions.
- **How it is useful:** Gives the current `grande_finale.tex` program a cleaner
  Lean workbench focused on the real bottleneck: Q, namely the primitive
  entropic inverse theorem / row-sharp prefix-fiber bound.  The package records
  theorem-level reductions and deterministic atoms; it does not prove the full
  adjacent safe rows.
- **What to do next:** Build only in a controlled Mathlib-enabled environment.
  Audit correspondence between the Lean declaration docstrings and the labels
  in `experimental/grande_finale.tex`, then extend the formalization toward the
  Q inverse theorem and finite row-sharp Q constants.

### 2026-07-08 - Entropic inverse route and asymptotic closure in Grande Finale

- **Agent/model:** Maintainer-added TeX drafts integrated by Codex.
- **Files added or changed:** `experimental/grande_finale.tex`,
  `experimental/grande_finale.pdf`, `experimental/agents-log.md`.
- **Status:** CONDITIONAL / PROVED / AUDIT.
- **What is being added:** Integrated the standalone primitive entropic inverse
  theorem for Vandermonde slice sums as the clean additive-combinatorics atom
  behind Q.  Added the conditional asymptotic RS--MCA closure theorem showing
  that this inverse theorem, together with the printed first-match ledger
  hypotheses, gives the entropy--subfield threshold formula.  Also added a
  Fourier-flat sufficient condition for Q in large-characteristic leaves.
- **How it is useful:** This separates the remaining Q proof from RS-MCA
  language and makes the asymptotic prize route precise: prove the primitive
  inverse theorem, or find a new algebraic obstruction cell.  The Fourier
  theorem gives a theorem-level route in leaves where the explicit character
  sum error fits the frontier ledger.
- **What to do next:** Prove or refute the primitive entropic inverse theorem,
  including the entropy BSG/PFR or free-energy branch and the slice derivative
  back to Vandermonde rank defect.  For finite deployed rows, do not use the
  asymptotic theorem unless all constants fit the printed adjacent margins.

### 2026-07-08 - Reviewed PR integration for Q, BC, L1, and Lean packets

- **Agent/model:** DannyExperiments/Gia via PRs #389, #409, #411, and #413;
  Holm Buar/Claude Fable 5 via PRs #392, #393, #395, #396, #399, #400,
  #403, #407, #408, #410, and #412; AllenGrahamHart/Claude Opus 4.8 via PRs
  #404, #405, and #406; Scott Hughes via PRs #390, #391, #398, #401, and
  #402; Vadim Avdeev via PR #397; Codex for review, selective integration,
  deconflicting overlapping Lean updates, and logging.
- **Files added or changed:** Added threshold/Q/BC audit notes under
  `experimental/notes/thresholds/`; L1 notes under `experimental/notes/l1/`;
  route-cut notes under `experimental/notes/roadmaps/`; certificate/data
  packets under `experimental/data/`; verifier/evidence scripts under
  `experimental/scripts/`; Lean packages and modules under
  `experimental/lean/grande_finale/`, `experimental/lean/l1_threshold_ledger/`,
  and `experimental/lean/powersum_rigidity/`; updated
  `experimental/grande_finale.tex` with a mass-aware logmoment caveat.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT / COUNTEREXAMPLE.
- **What is being added:** Integrated the reviewed PR packets without importing
  their individual log edits.  The batch adds Q route-cut audits
  (`p^{w/2}` concentration floor, signed-`e_m` masked residual audit,
  logmoment mass-awareness, moment-floor reconciliation, popular-fiber probe
  confound), row-sharp Q atom reductions and calibration, an independent replay
  of the four v13 adjacent pairs, a toy complete adjacent list-staircase
  certificate, BC L4 chart/second-moment reductions, L1 k3 and m=19 packets,
  the x4b moment-column subproblem packet, and Lean/finite-data certificates
  for Grande Finale composite-prefix descent and the L1 W3 collapse-edge
  mechanism.  The overlapping L1 Lean PRs were combined so the compact gate now
  includes origin summary, structural wrapper, graph mechanism, origin-dot, and
  origin-arithmetic checks.
- **How it is useful:** The Q material narrows the current bottleneck by ruling
  out several shortcut proof routes and by identifying the masked residual
  signed-prefix atom as the right target.  The v13 adjacent replay and toy
  staircase packet improve the certificate-scanner workflow.  The BC/L1 packets
  provide scoped reductions and counterexamples that help prevent overclaiming.
  The Lean additions improve formalization coverage for two high-priority
  tracks, but remain partial and do not prove Q or the adjacent safe rows.
- **What to do next:** Do not promote any of these packets into Paper D without
  a separate audit.  Run the lightweight verifiers individually before citing a
  certificate; run Lake only in a controlled Mathlib-enabled environment.  The
  open mathematical task remains row-sharp Q with finite constants, plus the
  finite BC chart-decomposition audit needed for the adjacent deployed rows.

### 2026-07-07 - Grande finale logarithmic-moment Q route

- **Agent/model:** Maintainer-added Q/Tao notes integrated by Codex.
- **Files added or changed:** `experimental/grande_finale.tex`,
  `experimental/grande_finale.pdf`,
  `experimental/agents-log.md`.
- **Status:** PROVED / CONJECTURAL / AUDIT.
- **What is being added:** Integrated the theorem-level equivalence between
  primitive logarithmic collision moments and primitive asymptotic Q, under
  the condition `w log |B| / r = o(n)`.  The paper now isolates the remaining
  additive-combinatorics input as an entropy-scale inverse theorem for
  primitive moment-curve subset sums, with a Vandermonde-rank closure showing
  why a low-rank output would finish asymptotic Q after paid cells are removed.
- **How it is useful:** This sharpens the asymptotic route: Q is no longer a
  vague max-fiber target but is equivalent to a logarithmic moment theorem.
  It also clarifies that standard polynomial-scale inverse Littlewood-Offord
  and Green-Ruzsa/Freiman results are templates, not black-box proofs at the
  exponential fiber scale.
- **What to do next:** Prove or refute the entropy-scale inverse theorem in
  `prob:entropy-inverse-q`.  For finite deployed adjacent rows, do not use the
  asymptotic `e^{o(n)}` statement as a certificate; the row still needs
  audited constants fitting the printed margins and the BC chart-decomposition
  audit.

### 2026-07-07 - Grande finale Q-attempt promotion and Lean cleanup

- **Agent/model:** Maintainer-added `grande_finale_q_attempt` reviewed and
  integrated by Codex.
- **Files added or changed:** `experimental/grande_finale.tex`;
  `experimental/grande_finale.pdf`; `experimental/lean/grande_finale/`;
  deleted `experimental/lean-certificates/`; updated `AGENTS.md` and
  `experimental/agents-log.md`.
- **Status:** PROVED / CONDITIONAL / AUDIT.
- **What is being added:** Promoted the Q-attempt version to the canonical
  `experimental/grande_finale.tex`, preserving the composite-prefix
  `gcd(e,N)` multiplicity repair.  The note now records that SP is downstream
  from max-fiber Q, primitive one-parameter BC pencils are paid by the
  moving-root theorem, and the adjacent safe rows remain open at row-sharp Q
  plus the finite BC chart-decomposition audit.  The new
  `experimental/lean/grande_finale/` package was normalized under its Lake
  module layout and documented as a partial formalization.
- **How it is useful:** This makes the final-resolution target sharper:
  proving Q is now the main bottleneck, while BC/SP are either paid in the
  one-parameter case or downstream of Q subject to the finite chart audit.  The
  guide now also states that all Lean packages belong under `experimental/lean/`.
- **What to do next:** Attack `def:q-row-atom` / `prob:row-sharp-q` in
  `experimental/grande_finale.tex` and the corresponding v13 raw source
  ledger.  Build `experimental/lean/grande_finale/` in a Mathlib-enabled
  environment before calling any declaration Lean-certified, and add missing
  formalization for the row-sharp Q atom theorem and finite BC chart audit.

### 2026-07-07 - Reviewed PR integration for v13 adjacent ledgers

- **Agent/model:** Scott Hughes via PRs #362, #367, #377, #381, and #387;
  Holm Buar via PRs #363, #364, #365, #366, #368, #378, #379, #382, #383,
  and #384; Vadim Avdeev via PRs #385 and #386; Danny/Gia via PRs #376,
  #380, and #388; LegaSage/Ken via PRs #371--#375; Latif Kasuli via PR #369;
  Manifold Control via PR #370; Codex for review, selective integration, and
  site/log updates.
- **Files added or changed:** Added reviewed packets under
  `experimental/data/certificates/`, `experimental/notes/thresholds/`,
  `experimental/notes/l1/`, `experimental/notes/m1/`,
  `experimental/notes/certificate_scanner/`, `experimental/notes/roadmaps/`,
  `experimental/lean/`, and `experimental/scripts/`; repaired
  `experimental/grande_finale.tex` and
  `experimental/grande_finale_work/q_next_section.tex`; updated
  `experimental/scripts/README.md`; added #381 near-capacity cap examples to
  `site/data/rate-leaderboards.json` and the embedded site fallback.
- **Status:** PROVED / CONDITIONAL / EXPERIMENTAL / AUDIT / COUNTEREXAMPLE,
  depending on the individual packet.  No packet is promoted to Paper D here.
- **What is being added:** Banks a broad reviewed PR wave: Q first-match
  leakage and composite-multiplicity repairs; a conditional KB-MCA `A=1116048`
  first-match ledger; Gamma-r and saturated-BC budget audits; M31/KB Q-rung
  route cuts; BC lower-floor Lean formalization; L1 bounded-excess, T=7,
  min-`j`, W3 collapse-edge, ell=19, and dim-Syz refutation packets; M1/CAPG
  finite-testability, split-pencil, adjacent-pair, shift-pair, Q/R1, and
  nonconsecutive-window packets; multi-rate LD_sw adjacent pins and board cap
  examples; small standalone Lean toy certificates were reviewed later and
  removed as redundant with stronger Lean tracks.
- **How it is useful:** Turns the v13 adjacent program into a much more
  explicit proof ledger.  The unsafe/lower rows and arithmetic margins are
  better audited; several false or overstrong L1/Q routes are cut; and the
  remaining safe-side work is more sharply named as primitive Q/max-fiber,
  saturated BC/split-pencil, and finite first-match residual payment with
  exact constants.  The site now exposes Scott's near-capacity Paper D cap
  examples as public leaderboard rows while keeping them separate from exact
  threshold claims.
- **What to do next:** Do not run the heavier verifiers casually.  For paper
  promotion, replay the relevant certificates independently, then distill only
  theorem-level material into the next CAP25 draft.  The live finite target is
  still the adjacent safe ledger at the v13 rows, especially KB-MCA
  `A=1116048`, with every residual branch paid by theorem, exact certificate,
  or explicitly labelled conjectural input.  Draft PR #355 remains unintegrated.

### 2026-07-06 - PRs #356-#361 experimental integration

- **Agent/model:** Holm Buar via PRs #358, #359, and #361; LegaSage via
  PRs #356 and #357; Scott Hughes via PR #360; Codex for static review,
  cleanup, and integration.
- **Files added or changed:** `experimental/data/certificates/annulus-corrected-cluster/`;
  `experimental/data/certificates/finite-reachability-map/`;
  `experimental/data/certificates/frontier-adjacent/kb_mca_conjq_rung_audit_v1.json`;
  `experimental/data/certificates/l1-e3-law/`;
  `experimental/data/certificates/l1-ell19/`;
  `experimental/notes/m1/annulus_corrected_cluster.md`;
  `experimental/notes/m1/finite_reachability_map.md`;
  `experimental/notes/thresholds/cap25_v13_qfin_rung_audit.md`;
  `experimental/notes/l1/l1_e3_*.md`;
  `experimental/notes/l1/l1_ell19_attainment.md`;
  `experimental/notes/roadmaps/l1_e3_*.md`;
  `experimental/lean/l1_e3_level_set/`;
  `experimental/l1_e3_obligation*.md`;
  `experimental/scripts/verify_annulus_corrected_cluster*.py`;
  `experimental/scripts/verify_finite_reachability_map*.py`;
  `experimental/scripts/verify_kb_mca_conjq_rung_audit.py`;
  `experimental/scripts/verify_l1_e3_*.sage`;
  `experimental/scripts/verify_l1_e3_flint_crosscheck.py`;
  `experimental/scripts/verify_l1_e3_law_refuted.py`;
  `experimental/scripts/verify_l1_ell19_attainment.py`;
  and supporting Sage/GP/M2/Python scripts.
- **Status:** AUDIT / EXPERIMENTAL / COUNTEREXAMPLE / FORMALIZATION-SKELETON.
- **What is being added:** Banks five additive PR packets and a sanitized L1
  E3 proof-program packet.  The M1 packets add finite-reachability and
  annulus bounded-cluster insufficiency scope maps.  The threshold packet
  audits the KB-MCA `a0+1` divisor-lattice rungs and leaves the primitive
  `conj:Q` fiber as the named residual.  The L1 packets refute the proposed
  `E_3<=ell` law at `T>=5`, add an `ell=19` attainment witness, and reduce
  the sharper `E_3<=ell-2` ceiling to the `dim Syz<=K` rank crux with CAS
  cross-checks and a Lean skeleton containing an explicit `sorry`.
- **How it is useful:** Clarifies the current proof boundary for the v13 raw
  adjacent program: nonprimitive quotient rungs are ledger-audited for the
  KB-MCA row, while the finite max-fiber/L1 problem is narrowed to a concrete
  cyclotomic level-set rank statement.  The M1 maps mark which finite checks
  are only scope evidence and which growing-dimensional aperiodic branches
  remain live.
- **What to do next:** Do not promote these packets into Paper D without
  independent replay.  The expensive KB-MCA rung verifier should be run only
  intentionally.  The next proof work is the primitive `conj:Q` max-fiber
  bound, the L1 `dim Syz<=K` theorem for `K>=3`, and a growing-dimensional
  M1 aperiodic upper ledger.  Draft PR #355 was not integrated because it
  overwrites existing M1 triage paths and carries a large route-cut evidence
  archive that should be split or summarized first.

### 2026-07-06 - Threshold and F1 audit PR integration

- **Agent/model:** DannyExperiments via PRs #352 and #354; Latif Kasuli via
  draft PR #353; Codex for review and integration.
- **Files added or changed:** `experimental/notes/thresholds/cap25_v13_qfin_primitive_wall_synthesis.md`;
  `experimental/notes/thresholds/cap25_v13_near_rational_support_mismatch_audit.md`;
  `experimental/notes/frontier-adjacent/f1_effective_slack_translation_v1.md`;
  `experimental/notes/frontier-adjacent/f1_simple_pole_tge2_obstruction_v1.md`;
  `experimental/data/certificates/frontier-adjacent/f1_effective_slack_translation_v1.json`;
  `experimental/data/certificates/frontier-adjacent/f1_simple_pole_tge2_obstruction_v1.json`;
  `experimental/scripts/verify_f1_effective_slack_translation.py`;
  `experimental/scripts/verify_f1_simple_pole_tge2_obstruction.py`;
  `experimental/agents-log.md`.
- **Status:** AUDIT / EXPERIMENTAL / PROVED-FOR-NAMED-PENCIL.
- **What is being added:** Two CAP25 v13 threshold notes and two F1
  frontier-adjacent packets.  The threshold notes isolate the live KB-MCA
  Q-fin primitive max-orbit wall and repair a near-rational support-mismatch
  overclaim.  The F1 packets translate deployed adjacent rows to the toy
  slack variable `t=a-k` and prove that the named simple-pole pencil has no
  `t>=2` bad slopes by a degree/root-count obstruction.
- **How it is useful:** Narrows the safe-side proof obligations without
  promoting them to solved results: the current KB-MCA adjacent row remains
  open, the near-rational branch needs an exp…17328 tokens truncated… promoting
  finite local data.

### 2026-07-01 - Paper D v10 milestone integration

- **Agent/model:** Codex.
- **Files added or changed:** `tex/cs25_cap_v10.tex`;
  `cs25_cap_v10.pdf`; `scripts/cs25_v10_*.py`;
  `experimental/data/certificates/cs25-v10-regular-hankel-examples/`;
  `experimental/notes/audits/paperD_v10_milestone_integration_audit.md`;
  `towards-prize.md`; `experimental/agents-log.md`.
- **Status:** AUDIT / VERSION-PROMOTION / PROVED-CERTIFICATE-FRAMEWORK.
- **What is being added:** Integrated the four v10 milestone folders into Paper
  D v10: quantitative deep-list floors, heaviest prefix-fiber quotient lower
  ledgers, exact divisor-block support-union coefficients, gcd/lcm quotient
  image ledgers, extension-pole simple-pole witnesses, and canonical regular
  Hankel rank-drop gcd/lcm ledgers.
- **How it is useful:** This strengthens Paper D's completion program from a
  v9 chart atlas into scanner-ready lower, quotient, extension, and regular
  Hankel ledgers.  It also narrows the remaining prize-side work to structural
  exhaustion, singular buckets, and safe-side extension classification.
- **What to do next:** Run the regular Hankel checker on the `F_17^32` row in
  the `385 <= A <= 426` window, combine paid-root subtraction with quotient and
  tangent ledgers, and build pivot eliminants for any singular buckets.  For
  current citations, use Paper D v12 rather than this v10 milestone note.

### 2026-06-30 - M2 Hankel smoke packet

- **Agent/model:** Codex.
- **Files added or changed:**
  `experimental/data/certificates/hankel-smoke-f17-506-507/`;
  `experimental/notes/thresholds/hankel_smoke_f17_506_507.md`;
  `experimental/scripts/verify_hankel_smoke_f17_506_507.py`;
  `towards-prize.md`; `tex/cs25_cap_v9.pdf`.
- **Status:** PROVED-SMOKE-PACKET / AUDIT.
- **What is being added:** The duplicate `tex/cs25_cap_v9.pdf` was removed,
  and the M2 v9 smoke packet was added for the settled
  `RS[F_17^32,H,256]`, `n=512`, `k=256` high-agreement threshold.  The packet
  records `A=506` with numerator `7` as unsafe and `A=507` with numerator `6`
  as safe, with declared aperiodic numerator `0` after tangent ledger removal.
- **How it is useful:** This validates the v9 packet format on a row whose
  answer is already known, giving future agents a concrete template before
  attacking the regular non-tangent window.
- **What to do next:** Use the same packet/checker workflow for M3:
  agreements `385 <= A <= 426`, where regular Hankel minors may close rows not
  covered by tangent exactness.

### 2026-06-30 - Aperiodic Hankel packet checker

- **Agent/model:** AllenGrahamHart / Codex, integrated by Codex.
- **Files added or changed:** `scripts/check_aperiodic_eliminant_packet.py`;
  `experimental/data/certificates/aperiodic-hankel-regular-minor-toy/`;
  `experimental/notes/m1/aperiodic_hankel_regular_minor_toy_certificate.md`;
  `experimental/scripts/verify_aperiodic_hankel_regular_minor_toy.py`;
  `experimental/agents-log.md`.
- **Status:** AUDIT / PROVED for the toy certificate.
- **What is being added:** A reusable checker for
  `scripts/aperiodic_eliminant_schema.json`, a deterministic `F_17`,
  `n=16`, `k=8`, `a=13` regular-overdetermined Hankel-minor toy packet, and
  an intentionally invalid packet for negative testing.
- **How it is useful:** This is the first concrete replay target for the Paper
  D v9 Hankel certificate workflow.  It checks schema conformance, `j=n-A`,
  `t=A-k`, regular-minor degree/root hashes, residual labels, and declared
  root-union numerators.
- **What to do next:** Extend the checker to real prize-facing rows and
  singular/residual buckets; keep every new packet tied to the v9 schema and a
  deterministic verifier.

### 2026-06-30 - Late PR M1/audit integration

- **Agent/model:** Codex, auditing and distilling PRs from AllenGrahamHart and
  Scott Hughes.
- **Files added or changed:** M1/audit notes and verifiers from PRs #150--#156
  and #158 under `experimental/notes/` and `experimental/scripts/`;
  `experimental/data/step5-envelope-map/envelope_map.json`;
  `experimental/notes/m1/m1_packet_sift_popularity_digest.md`;
  `experimental/scripts/verify_m1_packet_sift_popularity_digest.py`;
  `experimental/notes/m1/m1_a327_rim_route_cut_digest.md`;
  `experimental/data/m1_a327_rim_route_cut_digest.json`;
  `experimental/scripts/verify_m1_a327_rim_route_cut_digest.py`;
  `experimental/notes/triage/pr-triage-2026-06-30-late.md`.
- **Status:** PROVED-LOCAL / CONDITIONAL / AUDIT / EXPERIMENTAL.
- **What is being added:** AllenGrahamHart's M1 local lemmas, sampler
  reconciliation audit, Step 5 high-agreement envelope map, and agreement-265
  status audit were integrated as experimental material.  Allen's oversized
  packet-sift PR #157 was distilled to a compact packet-overlap/popularity-gate
  digest.  Scott Hughes's draft a=327 RIM obstruction PR #145 was distilled to
  a compact interleaved-list route-cut digest and self-contained JSON ledger.
- **How it is useful:** The batch preserves useful local M1 proof machinery,
  audit corrections, and high-agreement bookkeeping without promoting any
  conditional packet branch to a full M1 theorem or leaderboard row.
- **What to do next:** Rebase future M1 packets against the v9 Hankel
  certificate schema.  For the packet-sift branch, prove the nonlocal
  model-entry/multiplicity theorem or isolate a new residual obstruction.  For
  the a=327 RIM branch, turn RREF-derived pivots into deterministic pivot
  schedules before claiming a global bound.

### 2026-06-30 - Paper D v9 Hankel certificate atlas promotion

- **Agent/model:** Codex.
- **Files added or changed:** `tex/cs25_cap_v9.tex`,
  `scripts/aperiodic_eliminant_schema.json`,
  `experimental/notes/audits/paperD_v9_vs_v8_audit.md`, `AGENTS.md`,
  `README.md`, site paper/update metadata, and compiled Paper D v9 PDFs.
- **Status:** AUDIT / VERSION-PROMOTION / PROVED-CERTIFICATE-FRAMEWORK.
- **What is being added:** Paper D v9 preserves the v8 universal cap,
  first-grid cap, quotient-support ledger, and quotient-image ledger, then adds
  the aperiodic Hankel chart atlas: regular overdetermined minors, affine
  pivots, projective infinity, curve coefficient pivots, and named singular
  residual buckets.
- **How it is useful:** It turns the M1 safe-side task into concrete Hankel
  certificate packets. Contributors can now emit JSON against
  `scripts/aperiodic_eliminant_schema.json` instead of inventing an atlas or
  hiding singular charts under a generic aperiodic label.
- **What to do next:** Build actual eliminant certificates for meaningful rows,
  starting with exact agreements where the regular minor test applies. Every
  unresolved chart should be labelled as quotient, tangent, extension,
  candidate new obstruction, or unknown.

### 2026-06-30 - PR #137--#149 integration and triage

- **Agent/model:** Codex, auditing PRs from AllenGrahamHart, Holm Buar,
  Jose Brox, and Scott Hughes.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-30.md`,
  Lean ledger files under `experimental/lean/rs_mca_formalization/`,
  new notes under `experimental/notes/m1/`, `experimental/notes/f1/`,
  `experimental/notes/audits/`, and `experimental/notes/thresholds/`, new
  certificate data under `experimental/data/certificates/`, updated audit
  scripts under `experimental/scripts/`, and `experimental/experiments.tex`.
- **Status:** CONDITIONAL / PROVED-LOCAL / AUDIT / EXPERIMENTAL, depending on
  the individual note.  No full M1, F1, exact-threshold, or prize-solve claim is
  promoted.
- **What is being added:** The batch integrates Holm Buar's `{2,3}`-smooth Paper
  B exact canonical slope count, Lean arithmetic ledgers, finite toy databases,
  M1 numerical audit scans, and Cycle120 finite witness audit; Jose Brox's L3
  path cleanup; and AllenGrahamHart's width-one update, high-agreement compiler
  package, and independent V1 algebra checker.
- **How it is useful:** The new material improves Paper B combinatorics,
  high-agreement threshold reproducibility, formalized integer ledgers, and
  audit coverage without mixing them into the public leaderboard as new best
  rows.
- **What to do next:** Split AllenGrahamHart's very large same-slope PR #138
  into smaller local lemmas, ask for a compact replay target for Scott Hughes's
  #145 route-cut packet, and run Lean/certificate checks in a controlled
  environment if maintainers want independent replay beyond source inspection.

### 2026-06-30 - Paper D v8 quotient ledger promotion

- **Agent/model:** Codex.
- **Files added or changed:** `tex/cs25_cap_v8.tex`, `cs25_cap_v8.pdf`,
  `site/papers/cs25_cap_v8.pdf`,
  `experimental/notes/audits/paperD_v8_vs_v7_audit.md`, scanner status labels,
  `readme.md`, and site paper/leaderboard/update data.
- **Status:** AUDIT / VERSION-PROMOTION / PROVED_PAPERD_V8_CAP /
  PROVED_PAPERD_V8_FIRST_GRID.
- **What is being added:** Paper D v8 is promoted as the current public Paper D
  source. It preserves the v7 universal and first-grid caps, restores the
  explicit `q>n` and endpoint-radius fixes, and adds quotient-support plus
  distinct-parameter quotient image ledgers.
- **How it is useful:** The new ledgers give future staircase scanners and
  proof notes a safe way to account for declared quotient-remainder branches
  without double-counting supports or slope images.
- **What to do next:** Treat these ledgers as branch accounting only. The
  full safe-side theorem still needs the aperiodic Hankel-packing and
  extension-line completion inputs.

### 2026-06-29 - Paper D v7 first-grid cap promotion

- **Agent/model:** Codex.
- **Files added or changed:** `tex/cs25_cap_v7.tex`, `cs25_cap_v7.pdf`,
  `site/papers/cs25_cap_v7.pdf`,
  `experimental/notes/audits/paperD_v7_vs_v6_audit.md`, scanner status labels,
  `readme.md`, and site paper/leaderboard/update data.
- **Status:** AUDIT / VERSION-PROMOTION / PROVED_PAPERD_V7_CAP /
  PROVED_PAPERD_V7_FIRST_GRID.
- **What is being added:** Paper D v7 is promoted as the current public Paper D
  source. It preserves the v6 universal fixed-divisor MCA cap, extends the
  no-loss CA endpoint to `floor(delta n) <= n-k-1`, and adds the first-grid
  deep-point cap for large official-envelope rows.
- **How it is useful:** The public board can now show two Paper D theorem
  layers: the older uniform fixed-divisor cap and the stronger large-row
  first-grid cap `delta*_C(2^-128) <= 1-rho-1/n`.
- **What to do next:** Keep first-grid rows separate from exact-threshold
  claims. The missing safe-side work remains the L1/M1/F1/M2 completion package.

### 2026-06-29 - PR #136 width-one fixed-root closure

- **Agent/model:** AllenGrahamHart / Codex audit.
- **Files added or changed:** `experimental/notes/m1/m1_width_one_fixedroot_closure.md`,
  `experimental/experiments.tex`, `experimental/experiments.pdf`, and
  `experimental/agents-log.md`.
- **Status:** PROVED-LOCAL / CONDITIONAL-CLOSURE / AUDIT.
- **What is being added:** A compact width-one M1 closure note: width-one
  maximal root shadows are bounded-complement rank tests, descend losslessly
  under fixed-root absorption, and inject into one-root fixed-divisor/root-slice
  ledgers.
- **How it is useful:** It reduces the width-one critical-tail branch to the
  existing one-root fixed-root ledger in fixed surplus, giving a smaller target
  for the M1 proof program without promoting a full all-line theorem.
- **What to do next:** Prove or import the polynomial fixed-surplus bound for
  `FixedRootOneRoot_{r1}` after quotient-periodic, tangent, fixed-root, and
  aperiodic charges; do not treat this as a leaderboard row.

### 2026-06-29 - PR #131--#135 triage and frontier rows

- **Agent/model:** Codex, auditing PRs from AllenGrahamHart, Scott Hughes, and
  Vadim Avdeev.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-29.md`,
  `experimental/notes/m1/m1_boundary_off_external_anchor_audit.md`,
  `experimental/notes/m1/m1_a507_adjacent_bridge_theorem.md`,
  `experimental/notes/m1/m1_a507_plus_one_slope_hunt.md`,
  `experimental/notes/m1/m1_interleaved_list_*.md`,
  `experimental/notes/m1/m1_random_simple_pole_entropy_floor.md`,
  `experimental/notes/m1/m1_coset_packet_finite_slope_floors.md`,
  matching JSON certificates under `experimental/data/`, matching verifiers
  under `experimental/scripts/`, `experimental/experiments.tex`, and site data.
- **Status:** PROVED-LOCAL / PROOF-PROGRAM / PROOF_RECORD / LOWER_BOUND /
  ROUTE_CUT / AUDIT.
- **What is being added:** The PR wave adds three useful frontier-facing
  packets: Scott Hughes's interleaved-list hybrid certificate
  `Lambda_mu(C,326) >= 7`, Vadim Avdeev's random simple-pole finite-slope floors
  for `a=257..260`, and Vadim Avdeev's coset-packet finite-slope floors for
  `a=261..288`. AllenGrahamHart's boundary-off external-anchor M1 normal form is
  distilled into a compact proof-program audit, and Scott Hughes's `a=507`
  adjacent-bridge packet is integrated as a route cut rather than a new row.
- **How it is useful:** The finite-slope floors strengthen the low-agreement
  side of the `F_17^32, n=512, k=256` MCA ledger, while the interleaved-list
  packet moves the separate list-track lower-bound row up to agreement `326`.
  The route-cut notes prevent accidental mixing of adjacent line/list
  numerators into the same finite-slope MCA denominator.
- **What to do next:** Human-review the finite-slope-to-MCA noncontainment
  convention before paper promotion, keep #131 as proof-program material until
  it proves a global M1 bound, and treat the Sage scripts in #133 as optional
  independent audits rather than required local verification.

### 2026-06-29 - Paper D v6 promotion and completion-program audit

- **Agent/model:** Codex.
- **Files added or changed:** `tex/cs25_cap_v6.tex`, `cs25_cap_v6.pdf`,
  `site/papers/cs25_cap_v6.pdf`,
  `experimental/notes/audits/paperD_v6_vs_v5_audit.md`, scanner status labels,
  `readme.md`, and site paper/leaderboard/update data.
- **Status:** AUDIT / VERSION-PROMOTION / PROVED_PAPERD_V6_CAP.
- **What is being added:** Paper D v6 is promoted as the current public Paper D
  source. It keeps the v5 universal MCA cap constants and CS25-free route,
  tightens the conversion collision-count derivation, and adds the
  prize-facing integer-staircase/completion program.
- **How it is useful:** Public rows now cite the strongest Paper D package:
  same cap theorem, clearer prize posture, and explicit conditional MCA/list
  completion theorems for turning the one-sided cap into a full threshold
  determination.
- **What to do next:** Use `PROVED_PAPERD_V6_CAP` for verified Paper D cap rows,
  while keeping the missing L1/M1/F1/M2 completion obligations separate from
  the proved cap itself.

### 2026-06-27 - Root-level paper PDF relocation

- **Agent/model:** Codex.
- **Files added or changed:** `cs25_cap_v5.pdf`, `slackMCA_v4.pdf`,
  `snarks_v5.pdf`, removed generated PDF outputs from `tex/`,
  `site/data/papers.json`, `site/index.html`, `experimental/agents-log.md`.
- **Status:** AUDIT / RELEASE-HYGIENE.
- **What is being added:** The generated Paper B/C/D PDFs are moved out of
  `tex/` into the repository root, matching the README convention that TeX
  sources live under `tex/` and PDFs live at the root. Site-local mirrors under
  `site/papers/` remain for static hosting.
- **How it is useful:** Keeps GitHub PDF links and repository layout aligned
  with the public paper set: B v4, C v5, and D v5.
- **What to do next:** Keep future TeX compile outputs copied to root and, when
  needed, mirrored into `site/papers/` for static-site serving.

### 2026-06-27 - Paper B/C/D version promotion and leaderboard source audit

- **Agent/model:** Codex.
- **Files added or changed:** `tex/slackMCA_v4.tex`,
  `slackMCA_v4.pdf`, `tex/snarks_v5.tex`, `snarks_v5.pdf`,
  `site/papers/slackMCA_v4.pdf`, `site/papers/snarks_v5.pdf`, `readme.md`,
  `site/data/rate-leaderboards.json`, `site/data/updates.json`,
  `site/index.html`, `experimental/agents-log.md`.
- **Status:** PROVED / AUDIT.
- **What is being added:** Two clarification edits are added to the promoted
  Paper B/C versions: the Paper B unsplit curve-envelope lower bound is
  explicitly the line witness embedded as a degree-`d` curve, and Paper C now
  says the curve compiler applies to the finite power-curve/evaluation-domain
  model rather than arbitrary protocol samplers. The README records the current
  public versions B v4, C v5, and D v5.
- **How it is useful:** Keeps the paper prose aligned with the public board:
  Paper D v5 cap rows are proved under their printed scanner hypotheses,
  high-agreement/list rows cite Paper B v4 after promotion, and Paper C v5 is
  framed as protocol-ledger packaging rather than a new cap row.
- **What to do next:** Commit the version promotion after final review, and
  keep future leaderboard rows explicit about whether they are Paper B
  high-agreement theorem rows, Paper D v5 cap rows, or Paper C protocol-ledger
  packaging rows.

### 2026-06-27 - M1 variable-line packet and singleton lemmas

- **Agent/model:** AllenGrahamHart / Codex audit.
- **Files added or changed:**
  `experimental/notes/m1/m1_hankel_variable_line_packet_lemma.md`,
  `experimental/experiments.tex`, `site/data/updates.json`,
  `site/index.html`, `experimental/agents-log.md`.
- **Status:** PROVED-LOCAL / PROOF-PROGRAM / AUDIT.
- **What is being added:** Local packet lemmas for non-fixed variable Hankel
  determinant lines: active-new packet mass is reduced to active domain
  singletons, quotient defects, and a different-slope two-exchange codegree
  image.  The singleton term is then reduced to contained/tangent and
  one-outside target images, with the zero-lower class eliminated in the
  high-agreement range `a>(n+1)/2`.
- **How it is useful:** This extracts a reviewable M1 reduction from the
  all-line Hankel packet while keeping it out of the leaderboard.  It narrows
  the remaining non-fixed variable-line branch to explicit target-image and
  codegree estimates.
- **What to do next:** Prove polynomial bounds for the active different-slope
  two-exchange codegree and the one-outside boundary target image inside the
  quotient-aware residue-line ledger; do not cite this as the final M1 theorem.

### 2026-06-27 - Paper D v5 cap status promotion in scanner and board

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/notes/certificate_scanner/certificate_scanner.py`,
  `experimental/notes/certificate_scanner/README.md`,
  `experimental/notes/certificate_scanner/outputs/`,
  `experimental/notes/audits/a0_cs25_rational_constant_derivation.md`,
  `experimental/notes/audits/theorem_label_map.md`,
  `experimental/notes/audits/codex-f1-l1-20260617/README.md`,
  `experimental/agents-log.md`.
- **Status:** PROVED / ARITHMETIC-AUDIT.
- **What is being added:** The scanner then emitted `PROVED_PAPERD_V5_CAP` for
  then-active Paper D v5 cap rows whose divisor, binomial, and field hypotheses pass,
  and `NO_ACTIVE_PAPERD_V5_CAP` when no such row is found. Existing scanner
  reports and leaderboard-sweep outputs are regenerated or mechanically updated
  to remove the old draft/CS25-import status, and stale experimental audit notes
  now mark that import route as relevant only to older CA/list comparisons.
- **How it is useful:** Aligns the public leaderboard and scanner with Paper D
  v5's self-contained MCA cap route. Verified Paper D cap rows are no longer
  marked with the older conditional-import or draft-example statuses.
- **What to do next:** Keep CA/list comparison statements separate from the MCA
  cap status, and update any remaining paper-level prose that still discusses
  the older CS25-dependent route as the main Paper D theorem.

### 2026-06-27 - Finite-row threshold note and pure-MCA scanner profile

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/notes/thresholds/f17_32_finite_mca_threshold.tex`,
  `experimental/notes/thresholds/f17_32_finite_mca_threshold.pdf`,
  `experimental/notes/certificate_scanner/examples/f17_512_mca_only.json`,
  `experimental/notes/certificate_scanner/outputs/f17_512_mca_only.report.json`,
  `experimental/notes/certificate_scanner/outputs/f17_512_mca_only.report.md`,
  `experimental/agents-log.md`.
- **Status:** PROVED / AUDIT / EXPERIMENTAL-SCANNER.
- **What is being added:** A standalone finite-row threshold note packages the
  \(\F_{17^{32}}, n=512,k=256\) row as an exact finite-slope support-wise MCA
  threshold: agreement \(506\) is unsafe, agreement \(507\) is safe, and the
  closed-real safe interval is \([0,6/512)\). A pure-MCA scanner profile is
  added so the 506/507 endpoint is not mixed with the optional line-plus-list
  protocol ledger.
- **How it is useful:** Supersedes the old strict264-next threshold plan for
  this finite row and gives the clean packaging needed for the public board and
  `towards-prize.md`. It also isolates the next theorem target: the
  row-independent high-agreement threshold compiler with
  \(B_Q=\lfloor Q/2^{128}\rfloor\).
- **What to do next:** Audit the official MCA sampler definition against the
  finite/projective slope conventions and decide whether to promote the
  row-independent compiler from experimental notes into a paper-level theorem.

### 2026-06-27 - Prime192 leaderboard sweep rows

- **Agent/model:** Codex, auditing `leaderboard_sweep_192`.
- **Files added or changed:** `experimental/notes/certificate_scanner/outputs/leaderboard_sweep_192/`,
  `experimental/notes/certificate_scanner/certificate_scanner.py`,
  `site/data/rate-leaderboards.json`, `site/data/updates.json`, and
  `site/index.html`.
- **Status:** PROVED_PAPERD_V5_CAP / AUDIT.
- **What is being added:** The scanner sweep contributes four concrete
  prime-field rows with `q` near `2^192`, `k=2^40`, smooth power-of-two
  subgroup domains, and one row per official prize rate. It also records a
  small `F_17^32` Paper D example at agreement `258`.
- **How it is useful:** These rows instantiate the Paper D v5 cap with exact
  field/domain arithmetic, making the theorem-envelope rows concrete without
  claiming a new theorem beyond Paper D or an explicit slope census.
- **What to do next:** Regenerate the sweep from a checked-in sweep script if
  the scanner API changes, and keep CA/list comparison statements separate from
  the proved MCA cap status.

### 2026-06-27 - PR #122--#129 triage and selective integration

- **Agent/model:** Codex, auditing PRs from AllenGrahamHart, Scott Hughes,
  and Vadim Avdeev.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-27.md`,
  `experimental/notes/l1/l1_prefix_dual_d3_subgroup_twisted_collision_bound.md`,
  `experimental/notes/l1/l1_monomial_dyadic_descent_survivors.md`,
  `experimental/notes/f1/f1_arbitrary_anchor_locator_split.md`,
  `experimental/notes/m1/m1_all_line_hankel_aperiodic_packet_audit.md`,
  `experimental/data/adjacent-ledgers/`, selected verifier scripts, and
  `experimental/experiments.tex`.
- **Status:** PROVED / IMPORTED-STANDARD-INPUT / AUDIT / PROOF PROGRAM /
  EXPERIMENTAL.
- **What is being added:** New bounded L1/F1/M2 notes are integrated, while
  PR #127's large M1 generated packet is distilled into a smaller audit note.
  The public board is updated only for tangent-floor-backed status corrections:
  Cycle116/119 gates are unconditional but their exact Cycle84 numerator remains
  conditional, and reserve272/288/313 are marked as proved only because they are
  subsumed by tangent/strict352 floors.
- **How it is useful:** Adds useful L1 `d=3` proper-subgroup and monomial-prefix
  toy theorems, sharpens the F1 arbitrary-anchor ledger, and records
  challenge-map pullback accounting for protocol-facing high-agreement ledgers
  without promoting non-verified material to theorem status.
- **What to do next:** Split the M1 all-line aperiodic packet into small
  separately auditable verifiers before considering any stronger theorem claim;
  human-review the imported Katz/Gauss inputs in the L1 `d=3` note before moving
  it toward Paper B.

### 2026-06-27 - Promoted high-agreement TeX split

- **Agent/model:** Codex, verifying and promoting the user-supplied
  `experiments_v2.tex` split.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/experiments.pdf`, `experimental/notes/high_agreement/`,
  `experimental/scripts/verify_promoted_high_agreement_ledgers.py`,
  `experimental/agents-log.md`.
- **Status:** PROVED / CONDITIONAL-PROTOCOL-LEDGER / AUDIT.
- **What is being added:** The bulky high-agreement tangent, CA/projective,
  curve, interleaved-list, current-row protocol, and general threshold compiler
  material is split into reusable TeX fragments under
  `experimental/notes/high_agreement/` and included from the canonical
  `experimental/experiments.tex` wrapper.
- **How it is useful:** Keeps the stable high-agreement theorem package
  reviewable in smaller files while preserving the compiled experimental memo.
  The split also fixes the stale missing backslash before the
  `Towards-Prize Finite-Threshold Theorems` section header.
- **What to do next:** Human-review the curve sampler caveat before citing the
  curve statements in protocol settings, and keep protocol query/folding,
  extension-lift, challenge-field, and cryptographic losses as separate ledger
  terms.

### 2026-06-26 - Generalized high-agreement ledgers

- **Agent/model:** GPT-5.5 Pro generalized-ledgers packet, audited and
  integrated by Codex.
- **Files added or changed:** `experimental/data/generalized-ledgers/`,
  `experimental/experiments.tex`, `experimental/experiments.pdf`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`,
  `experimental/data/README.md`, `site/data/updates.json`, `site/index.html`.
- **Status:** PROVED / CONDITIONAL-PROTOCOL-LEDGER / ARITHMETIC-AUDIT.
- **What is being added:** A row-independent high-agreement ledger calculus for
  `RS[F,D,k]` rows: with `R=n-k`, `r=n-a`, and `B_Q=floor(Q/2^128)`, the exact
  line/CA/projective numerator is `r+1` in the range `r <= floor(R/3)`, the
  degree-`d` curve numerator is `d(r+1)` in the range
  `r <= floor(R/(d+2))`, and interleaved-list uniqueness holds for
  `r <= floor(R/2)`.
- **How it is useful:** This moves the adjacent-ledger conclusions beyond the
  special `F_17^32` row.  It gives a reusable integer calculator for deciding
  when tangent-star high-agreement terms alone can pin a `2^-128` threshold,
  and shows that at prize-scale dimensions the method stops pinning thresholds
  once field sizes are roughly above `2^166` to `2^170`, depending on rate.
- **What to do next:** Use this calculator before adding any new row to the
  public board, and keep quotient-core, generated-field entropy, challenge
  field, folding, query, and cryptographic terms as separate ledgers.

### 2026-06-26 - High-agreement adjacent CA/curve/list ledgers

- **Agent/model:** GPT-5.5 Pro adjacent-ledgers packet, audited and integrated
  by Codex.
- **Files added or changed:** `experimental/data/adjacent-ledgers/`,
  `experimental/experiments.tex`, `experimental/experiments.pdf`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`,
  `site/data/frontier.json`, `site/data/updates.json`,
  `site/data/rate-leaderboards.json`, `site/index.html`.
- **Status:** PROVED / CONDITIONAL-PROTOCOL-LEDGER / ARITHMETIC-AUDIT.
- **What is being added:** The high-agreement tangent staircase is extended to
  no-loss CA, projective-slope support-wise MCA, finite-parameter degree-`d`
  curve CA/MCA, and MDS interleaved-list uniqueness.  For
  `RS[F_17^32,H,256]`, the line-plus-list coding ledger is unsafe at
  agreement `a=507` and safe at `a=508` when no query/folding loss is added.
- **How it is useful:** This answers the immediate adjacent-ledger question
  past the finite-slope `506/507` gate: the high-agreement CA/projective/curve
  and interleaved-list coding objects are now pinned by explicit integer
  formulae, rather than left as open checks.
- **What to do next:** Human-review protocol reductions before using the
  conditional ledger in SNARK claims, and add any query, folding, hash,
  extension-lift, or cryptographic error terms explicitly.

### 2026-06-26 - Tangent-star extremizer barrier

- **Agent/model:** GPT-5.5 Pro tangent-star packet, audited and integrated by
  Codex.
- **Files added or changed:** `experimental/data/tangent-star/`,
  `experimental/experiments.tex`, `experimental/agents-log.md`,
  `site/data/frontier.json`, `site/data/updates.json`,
  `site/data/rate-leaderboards.json`, `site/index.html`.
- **Status:** PROVED / NEW-LOCAL / FINITE-SLOPE STRUCTURAL BARRIER.
- **What is being added:** A refinement of the high-agreement tangent
  staircase: in the exact range `3a-2n >= k`, extremal finite-slope
  support-wise `LD_sw` lines are tangent-star lines.  For
  `RS[F_17^32,H,256]`, this rules out a seventh finite-slope bad branch at
  every agreement `a >= 507`.
- **How it is useful:** It closes the previous finite-slope follow-up question
  left by the tangent staircase: no non-tangent mechanism can push the current
  `F_17^32`, `n=512`, `k=256` row past the `506/507` gate under the
  finite-slope support-wise MCA convention.
- **What to do next:** Use the adjacent-ledgers packet for the high-agreement
  CA/projective/curve/list coding objects, and keep protocol, challenge-field,
  extension-lift, folding, query, and cryptographic losses as separate ledgers.

### 2026-06-26 - High-agreement tangent staircase

- **Agent/model:** GPT-5.5 Pro tangent packet, audited and integrated by Codex.
- **Files added or changed:** `experimental/data/tangent/`,
  `experimental/experiments.tex`, `experimental/experiments.pdf`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`.
- **Status:** PROVED / ARITHMETIC-AUDIT / FINITE-SLOPE-THRESHOLD.
- **What is being added:** A generic moving-root tangent floor
  `LD_sw(C,a) >= n-a+1` for Reed--Solomon codes, plus a matching upper bound in
  the very-high-agreement range `3a-2n >= k` using the common code-line
  residual budget.
- **How it is useful:** For `RS[F_17^32,H,256]` with `|H|=512`, this proves
  `LD_sw(C,a)=513-a` for every `a>=427`, so `LD_sw(C,506)=7` and
  `LD_sw(C,507)=6`.  Thus the finite-slope support-wise `2^-128` staircase is
  pinned between agreements `506` and `507`; agreement `353` and the strict352
  quotient-core frontier are superseded by the tangent floor.
- **What to do next:** Human-review the endpoint convention and use the
  adjacent-ledgers packet for the high-agreement CA/projective/curve/list
  coding objects; protocol-facing losses still need separate ledgers.

### 2026-06-26 - L1 d=2 cubic subgroup twisted bound

- **Agent/model:** Scott Hughes PR #121, integrated by Codex.
- **Files added or changed:**
  `experimental/notes/l1/l1_prefix_dual_d2_cubic_subgroup_twisted_bound.md`,
  `experimental/notes/triage/l1-prefix-dual-d2-cubic-subgroup-twisted-bound-import-audit-2026-06-26.md`,
  `experimental/scripts/verify_l1_prefix_dual_d2_cubic_subgroup_twisted_bound.py`,
  `experimental/notes/triage/pr-triage-2026-06-26-round2.md`,
  `experimental/agents-log.md`.
- **Status:** PROVED / STANDARD-WEIL-INPUT / AUDIT.
- **What is being added:** A `d=2` cubic proper-subgroup collision bound for
  the actual `H^{2k}` object, using exact Fourier reconstruction,
  multiplicative-character expansion of `1_H`, and a conservative
  one-variable mixed character-sum bound.
- **How it is useful:** Separates proper-subgroup counting from full-affine
  Hooley--Katz geometry and gives an L1 template for higher odd-moment twisted
  subgroup bounds.  It is not a new MCA leaderboard row.
- **What to do next:** Pin the imported Katz/Gauss source constants and test
  whether the method extends to higher odd moments with reserve-scale margins.

### 2026-06-26 - L1 odd-moment Hooley-Katz audit

- **Agent/model:** Scott Hughes PR #120, integrated by Codex.
- **Files added or changed:**
  `experimental/notes/l1/l1_prefix_dual_odd_moment_projective_geometry.md`,
  `experimental/notes/triage/l1-prefix-dual-odd-moment-hooley-katz-import-audit-2026-06-26.md`,
  `experimental/scripts/verify_l1_prefix_dual_odd_moment_hooley_katz_audit.py`,
  `experimental/notes/triage/pr-triage-2026-06-26-round2.md`,
  `experimental/agents-log.md`.
- **Status:** PROVED / IMPORTED-VERIFIED / AUDIT / ROUTE CUT.
- **What is being added:** A projective odd-moment collision-geometry theorem
  for `k>d`, affine-cone conversion, and a Hooley--Katz/Ghorpade--Lachaud
  constant ledger for the full-affine point-count route.
- **How it is useful:** Records why the generic full-affine point-count route
  is not enough for the subgroup L1 reserve-scale problem and prevents ledger
  mixing between full-affine, full-torus, and proper-subgroup counts.
- **What to do next:** Human-check imported theorem citations and use the
  audit as a route cut unless sharper geometry-specific constants are found.

### 2026-06-26 - Strict352 dyadic quotient-core MCA floor audit

- **Agent/model:** Codex, auditing user-supplied strict352 packet.
- **Files added or changed:** `experimental/data/strict352/`,
  `experimental/agents-log.md`.
- **Status:** PROVED / AUDIT / SUPPORT-WISE-MCA-LOWER-BOUND.
- **What is being added:** A dyadic quotient-core proof packet for
  `RS[F_17^32,H,256]`, `|H|=512`, showing `LD_sw(C,a) >= 7` for every
  agreement `264 <= a <= 352`, with `LD_sw(C,352) >= 16` under the
  finite-slope support-wise MCA convention.
- **How it is useful:** Records a quotient-core mechanism for agreements up to
  `352`.  This was briefly the lower-bound frontier, but it is now superseded
  by the generic tangent floor, which gives `LD_sw(C,352) >= 161` and
  `LD_sw(C,353) >= 160`.
- **What to do next:** Keep the packet as a quotient-core mechanism record and
  compare it against any non-tangent mechanisms that might survive past
  agreement `507`.

### 2026-06-26 - Strict264 quotient-floor proof packet

- **Agent/model:** Codex, with user-supplied strict264 packet.
- **Files added or changed:** `experimental/data/strict264/`,
  `experimental/agents-log.md`.
- **Status:** PROVED / AUDIT.
- **What is being added:** A strict264 quotient-core proof packet: generated
  field entropy/list-floor notes, a deep-point list-to-MCA conversion section,
  a calculator for entropy/MCA floors, and the concrete
  `RS[F_17^32,H,256]`, `|H|=512`, agreement-264 quotient-floor obstruction.
  The local audit fixed two TeX transcription errors and regenerated the saved
  calculator output with the exact value `log2(17^32)`.
- **How it is useful:** Gives a direct quotient-core route to
  `epsilon_mca(C,31/64)>2^-128`: `binom(64,33)` augmented-code list points
  imply at least nine support-wise bad slopes after the deep-point conversion,
  while seven slopes already clear the `F_17^32` denominator.
- **What to do next:** Keep the theorem package as a quotient-core mechanism
  record.  The moving-root tangent floor supersedes the old strict264/265
  target by giving `LD_sw(C,264) >= 249`.

### 2026-06-26 - Towards-prize finite-threshold theorem section

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/agents-log.md`.
- **Status:** PROVED / CONDITIONAL / AUDIT.
- **What is being added:** A new `Towards-Prize Finite-Threshold Theorems`
  section for `experiments.tex`: certificate-to-`LD_sw`, fixed-locator
  unique-slope, base-valued subfield confinement, the exact seven-slope
  arithmetic gate over `F_17^32`, and the one-step staircase pinning criterion.
- **How it is useful:** Converts the strict264 and 265 goals into theorem-level
  proof obligations that agents can attack without claiming a new numerator or a
  corrected-reserve MCA theorem.
- **What to do next:** Use the fixed-locator principle to build
  duplicate-aware strict264 and 265 search certificates.

### 2026-06-26 - One-by-one experiment run

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/data/experiment-run-2026-06-26.json`,
  `experimental/notes/triage/experiment-run-2026-06-26.md`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`,
  `site/data/updates.json`.
- **Status:** AUDIT / EXPERIMENTAL RUN.
- **What is being added:** A sequential run of the current Cycle120,
  strict264, reserve-ladder, F1, L2, A0, and M2 validators.  All executed
  scripts passed, but no script produced a new retained-slope certificate or
  improved frontier numerator.
- **How it is useful:** Confirms that the current proof infrastructure is
  internally consistent and isolates the exact next strict264 blocker:
  seven explicit retained bad slopes at agreement `264` for the
  `RS[F_17^32,H,256]` row.
- **What to do next:** Build the strict264 seven-slope certificate and an
  independent replayable certificate for the existing `52,747,567,092` count.

### 2026-06-26 - PR #108--#119 proof and audit integration

- **Agent/model:** AllenGrahamHart PRs #108--#112, #114--#118, Scott Hughes
  PRs #113 and #119, reviewed and integrated by Codex with topic-split validity
  checks.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-26.md`,
  `experimental/data/pr-triage-2026-06-26.json`,
  `experimental/experiments.tex`, `experimental/experiments.pdf`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`, plus new or updated
  notes and scripts under `experimental/notes/{audits,f1,l1,l2,m1,m2}/` and
  `experimental/scripts/`.
- **Status:** PROVED / CONDITIONAL / AUDIT / EXPERIMENTAL.
- **What is being added:** A one-by-one integration of PRs #108--#119.  The
  theorem-level additions are the F1 syndrome-pencil normal form, the L2
  codegree reduction, the A0 deep-point MCA-cap dependency split, and the M2
  common code-line residual budget.  The remaining material is kept as route
  cuts, audits, or proof programs.
- **How it is useful:** Gives future theory work cleaner local statements for
  F1, L2, Paper D/A0, and M2, while preserving conservative public status.  No
  new prize-worthy numerator or frontier point is claimed.
- **What to do next:** Human-review the theorem-level additions before any
  main-paper promotion, citation-check the mixed-Weil route in PR #119, and
  require a retained-slope proof before treating strict264 as more than a
  target.

### 2026-06-25 - Latest PR integration and estimate audit

- **Agent/model:** AllenGrahamHart PRs #101--#107, ScottDHughes PR #99, and
  Cycle120 audit material from PR #100/#105, integrated by Codex.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-25.md`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`, plus new or updated
  notes and scripts under `experimental/notes/{audits,f1,l1,l2,m1,m2,x1}/`,
  `experimental/scripts/`, and `experimental/lean/rs_mca_formalization/`.
- **Status:** AUDIT / EXPERIMENTAL / PROOF-CHECK-NEEDED / CONDITIONAL.
- **What is being added:** A one-by-one integration of PRs #99--#107. The
  Cycle120 numerator is unchanged at `52,747,567,092`; the useful improvements
  are the standalone Cycle120 `LD_sw` proof note, the exact M2
  `epsilon_mca = LD_sw/|F|` bridge, stronger F1 extension-line lower floors,
  an M1 beta-pushforward spectral audit, and sharper L1/L2 proof-program
  targets.
- **How it is useful:** Gives future theory work better normalized estimates
  without editing Papers A--D. In particular, the current ABF-row obstruction
  still points to `epsilon_mca(C,125/256)>2^-128` and the Cycle119 strict
  endpoint `delta*_C <= 249/512`, while L1/L2/F1/X1 now have cleaner
  follow-up notes and standard-library verifiers.
- **What to do next:** Do a human proof review of the standalone Cycle120
  proof chain, then run selected nonmutating verifiers in a controlled pass.
  Treat PR #100's raw generated packet as superseded by the compact audit and
  standalone proof note unless a reviewer explicitly needs the raw replay
  material.

### 2026-06-23 - Cycle119 admissibility review

- **Agent/model:** DannyExperiments PR #96, reviewed by Codex.
- **Files added or changed:**
  `experimental/notes/m1/m1_cycle119_strict263_admissibility_review.md`,
  `experimental/notes/triage/pr-triage-2026-06-23.md`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`, plus wording cleanup
  in the prior Cycle84 public replay audit.
- **Status:** AUDIT / PROOF-CHECK-NEEDED / COMPUTATION-DEPENDENT.
- **What is being added:** A compact review of the Cycle119 strict-263 claim:
  `LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092`, with `|H|=512`, and an
  admissibility check against the local ABF-aligned definitions and public
  Proximity Prize page.
- **How it is useful:** Separates the potentially important theorem claim from
  Danny's raw/generated PR branch. The branch is not integrable as-is, but the
  two-ended locator transfer is now the right object to demand as a clean proof.
  If the proof and finite computation check out, the right public framing is a
  prize-facing negative counterexample candidate under the printed ABF
  formulation, not an accepted prize solution.
- **What to do next:** Independently fetch and check the ABF PDF, then ask Danny
  for a standalone human-readable proof of the two-ended locator transfer and a
  separate minimal record of the Cycle84 finite computation it consumes.

### 2026-06-23 - Cycle120 ABF counterexample candidate integration

- **Agent/model:** DannyExperiments PR #96, reviewed by Codex.
- **Files added or changed:**
  `experimental/notes/m1/m1_cycle120_abf_counterexample_candidate.md`,
  `experimental/notes/m1/m1_cycle119_strict263_admissibility_review.md`,
  `experimental/notes/triage/pr-triage-2026-06-23.md`,
  `experimental/SUMMARY.md`, and `experimental/agents-log.md`.
- **Status:** CONDITIONAL / PROOF-SPINE-CHECKED / COMPUTATION-DEPENDENT /
  SOURCE-AUDIT.
- **What is being added:** A cleaned integration of the Cycle120 ABF-facing
  negative result. It records that Cycle116 agreement `262` is enough for the
  printed ABF closed threshold at `delta=125/256`, while Cycle119 agreement
  `263` checks as a strict-ball strengthening. The note now states explicitly
  that this is only a negative obstruction to
  `epsilon_mca(C,125/256) <= 2^-128` for one row, not ordinary list decoding,
  protocol soundness, or an exact determination of `delta*_C`. It also records
  the endpoint nuance: Cycle116 gives `delta*_C <= 125/256` under a supremum
  convention, while Cycle119 gives `delta*_C <= 249/512 < 125/256`.
- **How it is useful:** Moves the useful part of PR #96 into a compact
  experimental note without importing zips, generated checkers, copied PDFs,
  rendered pages, or raw prompt archives. It gives the project a concrete
  human-review target: the Cycle84/Cycle116 finite proof chain plus the
  optional Cycle119 strict-ball proof.
- **What to do next:** Independently retrieve the ABF PDF, review the finite
  count and fixed-jet transfer, and ask Danny for a minimal nonmutating reviewer
  packet in proof/computation/audit language.

### 2026-06-22 - PR #96-#98 experimental triage

- **Agent/model:** DannyExperiments, avdeevvadim, scottdhughes; integrated by
  Codex.
- **Files added or changed:**
  `experimental/notes/triage/pr-triage-2026-06-22.md`,
  `experimental/notes/m1/m1_cycle84_public_replay_audit.md`,
  `experimental/notes/f1/f1_deep_point_list_to_ca_mca.md`,
  `experimental/scripts/f1_deep_point_list_to_ca_mca_sanity.py`,
  `experimental/notes/l1/l1_prefix_fourier_orbit_cancellation.md`,
  `experimental/scripts/verify_l1_fourier_orbit_cancellation.py`,
  `experimental/SUMMARY.md`, `experimental/README.md`,
  `experimental/scripts/README.md`, and `experimental/agents-log.md`.
- **Status:** AUDIT / FINITE_MODEL_PROOF / PROVED / CONDITIONAL /
  EXPERIMENTAL.
- **What is being added:** A conservative triage of PRs #96--#98. PR #96's
  useful Cycle84 public replay record is kept as an inert audit note:
  `m_max(beta)=2`, `Occ(beta)=52,747,567,092`, `D=24`, twelve double fibers,
  and no fibers of size at least three. PR #97 adds the F1 simple-pole
  deep-point list-to-CA/MCA conversion note and sanity script. PR #98 adds the
  L1 dual-dilation Fourier orbit-kernel reduction note and verifier.
- **How it is useful:** Cycle84 now has a public replay record for the finite
  M1 wall without importing the live workflow or raw archive. The F1 note gives
  a direct special list-to-CA/MCA mechanism to audit against Paper D. The L1
  note moves prefix-local work from individual Fourier frequencies to orbit
  kernels and records a concrete route cut for pointwise kernel saving.
- **What to do next:** Do not treat Cycle84 as a prize-level theorem until a
  transfer theorem is proved. Audit #97 against the exact main-paper `eca` and
  `emca` predicates before any promotion. Run the new scripts only after
  reviewer approval; this triage pass inspected them as text but did not
  execute PR code.

### 2026-06-19 - Experimental folder streamlining

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/README.md`,
  `experimental/notes/README.md`, `experimental/scripts/README.md`,
  `experimental/data/README.md`, plus repository moves under
  `experimental/notes/`, `experimental/scripts/`, `experimental/data/`, and
  `experimental/lean/`.
- **Status:** AUDIT.
- **What is being added:** Reorganized the experimental workspace into four
  durable buckets: notes, scripts, compact data, and Lean. Removed generated
  Python caches and raw/prompt transcript dumps from dated AI-loop outputs.
- **How it is useful:** Future agents now have a small root surface and a clear
  placement policy. Audited summaries and reproducible scripts remain, while
  bulky model-run provenance that was not needed for review is gone.
- **What to do next:** Keep new work inside the existing buckets, update
  `README.md` if a genuinely new bucket is needed, and avoid adding raw
  transcript archives unless they are the only reproducibility record.

### 2026-06-19 - PR #82/#84-#95 experimental integration

- **Agent/model:** AllenGrahamHart, scottdhughes, latifkasuli,
  DannyExperiments PRs, integrated by Codex.
- **Files added or changed:** `experimental/notes/triage/pr-triage-2026-06-19.md`,
  `experimental/SUMMARY.md`, `experimental/agents-log.md`,
  `experimental/notes/l1/l1_prefix_divisor_count.md`,
  `experimental/notes/l1/l1_quotient_defect_closure.md`,
  `experimental/notes/l1/l1_repaired_locator_theorem_package.md`,
  `experimental/notes/l2/l2_interleaved_dilation_constants.md`,
  the NFB frontier JSON data folder,
  `experimental/notes/m1/m1_residue_line_roadmap.md`, M1 depth-two Kummer notes and
  verifiers, L1/L2 verifier scripts, and the selected
  `experimental/notes/f1/fable-loop/PRZ_REVIEW_INDEX.md` Cycle 49--57 audit
  layer.
- **Status:** PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT, as
  marked per file.
- **What is being added:** Manual integration of the useful recent PRs:
  PR #93 supersedes #85--#91 as the Scott L1 consolidation; PR #84 adds the
  L1 prefix/divisor/Fourier split; PR #92 adds L2 interleaved dilation and
  quotient-core constants; PR #94 adds a compact `F\B` deep-hole proof
  record; PR #82 adds the M1 low-slack Kummer/depth-two packet; PR #95 is
  integrated only as review index plus cycle audits, not as a raw 225k-line
  archive.
- **How it is useful:** Gives future work clear entry points: L1 quotient
  floors versus aperiodic Fourier cancellation, M1 two-coordinate/conductor
  targets, L2 aligned interleaved constants, an F1/Paper D explicit-line
  proof target, and a compact Fable-loop upper-side route map.
- **What to do next:** Run and review the integrated verifiers, add a
  standalone verifier for the NFB JSON record, audit the M1 Kummer imports
  before consuming constants, and continue the Fable-loop program from the
  high-`j` constant-rate prompt rather than the cut `t=2,j=2` toy regime.

### 2026-06-18 - PR #79-#81 experimental integration

- **Agent/model:** AllenGrahamHart and scottdhughes PRs, integrated by Codex.
- **Files added or changed:** `experimental/m1_depth_two_lift_window_theorem.md`,
  `experimental/m1_kummer_weil_import_contract.md`,
  `experimental/m1_support_coefficient_test.md`,
  `experimental/m1_support_occupancy_scan.py`,
  `experimental/m1_support_occupancy_scan.md`,
  `experimental/verify_m1_kummer_divisor_geometry.py`,
  `experimental/verify_m1_slack_two_depth_two_kummer_saturation.py`,
  `experimental/l1_arbitrary_fiber_repair.md`,
  `experimental/verify_l1_arbitrary_fiber_repair.py`,
  `experimental/a0_external_import_source_check_20260618.md`,
  `experimental/a0_import_source_probe.py`,
  `experimental/pr-triage-2026-06-18-round3.md`, and
  `experimental/agents-log.md`.
- **Status:** CONDITIONAL / AUDIT / EXPERIMENTAL / COUNTEREXAMPLE.
- **What is being added:** Manual integration of PR #79's M1 depth-two
  Kummer-window material, PR #80's L1 arbitrary-fiber repair note, and PR
  #81's A0 external-import source check.  The M1 material is explicitly
  conditional on the isolated Kummer-Weil import; the L1 material repairs a
  false raw-support arbitrary-fiber route; the A0 material records source
  reachability without closing the Paper D import audit.
- **How it is useful:** Narrows three active ledgers without editing Papers
  A--D: M1 gains a sharper lift-window/saturation audit, L1 gets a corrected
  list-object target, and A0 has a reproducible source-access record for the
  universal-cap import chain.
- **What to do next:** Prove or cite the M1 `16p` Kummer estimate, decide
  whether Paper B should promote `ImgFib_U(s)` or another repaired L1 object,
  and obtain the CS25/ABF PDFs needed to close the remaining A0 checks.

### 2026-06-18 - Four-item packet label clarification

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/experiments.pdf`, `experimental/agents-log.md`.
- **Status:** AUDIT / CLARIFICATION.
- **What is being added:** Adds a self-contained explanation of what the
  AI-packet labels (a)--(d) mean: weak-slack positive regime, finite
  Fermat-prime packet, exponential-field construction, and imported BCHKS
  quotient-locator packet.
- **How it is useful:** Makes the experimental PDF readable without knowing
  the earlier discussion, and separates imported locator material from the
  independent local Paper B divisibility-gate theorem.
- **What to do next:** If the original four-item packet is archived in the
  repo, cross-link this clarification to the exact source file or PR.

### 2026-06-18 - Streamlined imported-locator ledger

- **Agent/model:** Human-provided streamlined note, logged by Codex.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/experiments.pdf`, `experimental/agents-log.md`.
- **Status:** AUDIT / IMPORTED / WRAPPER / TARGET / NEW-LOCAL.
- **What is being added:** Replaces the narrower attribution note with a
  unified experimental ledger titled *Experimental Theorems and
  Imported-Locator Ledger for RS-MCA*.  The note explicitly imports the
  Ben-Sasson--Carmon--Habock--Kopparty--Saraf quotient-locator construction,
  gives the smooth-quotient notation dictionary, records the shared locator
  identity as imported rather than new, adds a list-fiber pigeonhole wrapper,
  states a slack-two/subfield target for the Paper D route, and preserves the
  Cycle 14--18 Paper B divisibility-gate theorem.
- **How it is useful:** Streamlines promotion decisions for Papers A--D:
  locator proofs from BCHKS must be cited at theorem and proof entry points;
  repository-side contributions are limited to dictionary/wrapper/ledger
  packaging unless separately proved; Paper D gets a precise augmented-code
  and subfield-pigeonhole target; Paper B keeps the independent restricted
  resonance gate as local experimental mathematics.
- **What to do next:** When editing the main papers, add the `BCHKS25`
  bibliography entry and cite Theorems 7.1 and 1.13 exactly where the locator
  construction is used.  Audit the augmented-code rung, slope field
  (`B` versus `F`), locator-codeword distinctness, and slack normalization
  before promoting any wrapper to a theorem.  Continue scanner work on the
  `G==0` divisibility-gate branch for the Paper B resonance window.

### 2026-06-18 - Proximity-gap attribution audit

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/experiments.pdf`, `experimental/agents-log.md`.
- **Status:** AUDIT / ATTRIBUTION.
- **What is being added:** Records that the AI-generated result (d) should be
  treated as an imported adaptation of Theorem 1.13 of
  Ben-Sasson--Carmon--Habock--Kopparty--Saraf, *On proximity gaps for
  Reed--Solomon codes*, rather than as a new repository contribution.  Also
  records the limitations of items (a)--(c): `1/sqrt(n)` slack, only three
  Fermat primes, and exponential field size.
- **How it is useful:** Gives Papers B/D/C a conservative integration plan:
  cite the external theorem, separate it from the Crites--Stewart import, and
  audit the consumed object before any MCA, line-decoding, or protocol ledger
  claim.
- **What to do next:** Add the bibliographic entry and exact theorem
  cross-reference when the main papers are edited, then verify whether item
  (d) converts to the RS-MCA object actually needed by Paper B.

### 2026-06-18 - PR #78 M1 residual-depth hierarchy

- **Agent/model:** AllenGrahamHart / Codex, integrated by Codex.
- **Files added or changed:** `experimental/m1_support_coefficient_test.md`,
  `experimental/m1_support_occupancy_scan.py`,
  `experimental/m1_support_occupancy_scan.md`,
  `experimental/verify_m1_slack_two_depth_two_full_domain.py`,
  `experimental/agents-log.md`.
- **Status:** PROVED / AUDIT / EXPERIMENTAL.
- **What is being added:** Integrated Allen's PR #78 M1 residual-depth
  hierarchy: the depth-two/next-slack transition theorem, terminal pure-zero
  residual-depth ledger, first-nonzero frontier partition, full-domain
  slack-two depth-two saturation verifier, and a high-index ceiling for the
  slack-two depth-two frontier.
- **How it is useful:** Separates inherited zero strata from genuinely new
  first-nonzero coefficient images in the M1 canonical-support scanner, giving
  sharper targets for Paper B's corrected MCA residue-line program.
- **What to do next:** Use the new verifier and scanner fields to attack
  proper-subgroup coset-image bounds, especially intermediate-index cases not
  decided by full-domain saturation or the coarse high-index ceiling.

### 2026-06-18 - Experimental theorem note

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/experiments.tex`,
  `experimental/experiments.pdf`, `experimental/agents-log.md`.
- **Status:** PROVED / HEURISTIC / AUDIT.
- **What is being added:** A standalone LaTeX note collecting restricted
  Cycle 14--18 theorems and heuristics, including the Cycle 18
  divisibility-gate theorem with proof.
- **How it is useful:** Gives the experimental proof material a citable,
  compiled form without editing Papers A--D.
- **What to do next:** Extend the scanner to test the `G==0` gate and decide
  whether any source-valid growing-prime family has two-dimensional slope-map
  image.

### 2026-06-18 - Cycle 18 resonance slope-map reconstruction

- **Agent/model:** Codex.
- **Files added or changed:**
  `experimental/notes/f1/fable-loop/audits/20260618_CYCLE18_RESONANCE_SLOPE_MAP_COLLAPSE_AUDIT.md`,
  `experimental/scripts/fable_loop/local_checks/20260618_cycle18_resonance_slope_symbolic.py`,
  `experimental/notes/f1/fable-loop/README.md`,
  `experimental/agents-log.md`.
- **Status:** PROOF-SKETCH / EXACT_NEW_WALL / AUDIT.
- **What is being added:** A local reconstruction of Danny's Cycle 18
  `t=2,j=3` resonance reduction: `Delta` becomes a monic quadratic in
  `tau3`, the alpha component is at most linear, and the non-coprime branch
  reduces to either `Delta1==0` or the graph `tau3=-h/s`. The audit also
  records the divisibility-gate theorem: if the cleared graph polynomial
  `G=s^2 Delta0(tau1,tau2,-h/s)` is nonzero, the branch is already
  curve-sized and contributes only `O(p)` slopes.
- **How it is useful:** Sharpens the Paper B/F1 restricted toy-window wall
  from the Cycle 16 `Q==0` split to a concrete rational slope-map collapse
  question.
- **What to do next:** Extend the Cycle 17 scanner to compute the graph branch
  and projective map image on source-valid split cubics across growing primes,
  with `G==0` as the first exact gate for possible `Theta(p^2)` behavior.

### 2026-06-18 - Paper B counterexample comparison

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/paper_b_counterexample_comparison.md`,
  `experimental/agents-log.md`.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** A theory-side comparison between recent
  experimental counterexamples and Paper B's locator-fiber, residue-line,
  extension-field, tangent-floor, and line-decoding statements.
- **How it is useful:** Identifies the raw arbitrary locator-fiber conjecture
  as needing repair, while separating route-cut counterexamples from genuine
  threats to the corrected MCA conjecture.
- **What to do next:** Review the proposed Paper B repairs, especially the
  replacement of raw `Fib_U` by a pruned/full-support arbitrary-word object.

### 2026-06-18 - Experimental summary

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/SUMMARY.md`,
  `experimental/agents-log.md`.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** A high-level summary of the recent PR wave and the
  current contents of `experimental/`, organized by how the material advances
  the corrected MCA program.
- **How it is useful:** Gives new agents and human reviewers a map of which
  experimental notes support L1, M1, M2, F1, L2, A0/A1, protocol ledgers, and
  formalization, while keeping proof status conservative.
- **What to do next:** Use the summary as an orientation map, then verify
  individual claims from their source notes and scripts before promotion.

### 2026-06-18 - New PR triage integration

- **Agent/model:** Codex.
- **Files added or changed:** Integrated experimental material from PRs #67,
  #69, #70, #71, #72, #73, #74, #75, and #77; recorded #68 and #76 as
  superseded by #77; added `experimental/pr-triage-2026-06-18.md`.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** Second open-PR triage pass covering M1, F1, L2,
  M2, L1, A1, Fable-loop, and locator-fiber cross-check contributions.
- **How it is useful:** Banks useful experimental notes, verifiers, scanners,
  and audit provenance while preserving the rule that main papers remain
  unchanged and new material stays in `experimental/`.
- **What to do next:** Run full verifier coverage, review mathematical claims
  before promotion, and close the source PRs as manually integrated or
  superseded once this commit is pushed.

### 2026-06-17 - Open PR triage integration

- **Agent/model:** Codex.
- **Files added or changed:** Integrated experimental material from PRs #1,
  #2, #3, and #46 through #66; added
  `experimental/pr-triage-2026-06-17.md`; renamed PR #55's dither scanner to
  `experimental/quotient_profile_dither.py` with matching `.md` note.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** One-by-one triage of the open PR queue and local
  integration of accepted experimental notes, scanners, proof records, and
  audit bundles.
- **How it is useful:** Preserves useful agent contributions while enforcing
  the repository rule that new material starts in `experimental/` and Papers
  A-D remain unchanged.
- **What to do next:** Run verifiers and audits on the integrated material,
  review mathematical notes before promotion, and close the original PRs as
  manually integrated once the integration commit is pushed.
