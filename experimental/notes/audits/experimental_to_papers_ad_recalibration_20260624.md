# Experimental Folder Recalibration Against Papers A-D

Date: 2026-06-24

Status: AUDIT / RECALIBRATION

Public baseline checked: `origin/main` at `a566dca`
(`Relate Cycle120 obstruction to proximity-gap framework`).

## Purpose

This note maps the current `experimental/` folder back to the four public
papers and identifies which objects should be promoted into ordinary theorem
notes, which should remain examples or computations, and which material should
stay out of the front-door story.

The goal is not to add another cycle. The goal is to prevent drift.

## Executive Read

The experimental folder contains useful material, but the reusable value is
not the raw sequence of cycles. The reusable value is a small set of proof
mechanisms:

1. fixed-jet locator transfer;
2. two-ended locator transfer;
3. residue-line normal forms and packing questions;
4. field-accounting and sampler-map lemmas;
5. quotient/local-limit and interleaving ingredients.

The Cycle116/119/120 line should be presented as a concrete negative example
and as evidence for reusable transfer lemmas, not as a new replacement for the
four-paper framework. Papers A and D already explain that broad "up to
capacity" statements fail or are capped. The new value is in the mechanism,
the exact row, and the transfer lemmas.

## Papers A-D as the Reference Frame

### Paper A: no-slack obstruction

Reference file: `tex/RS_disproof_v3.tex`.

Role: Paper A is the lower-bound and obstruction paper. It shows that a
no-slack support-wise line-MCA reading of near-capacity Reed-Solomon behavior
is false for smooth multiplicative domains.

Experimental material feeding Paper A:

- explicit smooth-domain negative examples;
- quotient-locator and restricted-sum constructions;
- Cycle84/Cycle116/Cycle119/Cycle120 as a concrete high-precision example;
- Goldilocks prime-field examples;
- small-field scans that reveal new obstruction patterns.

What can be strengthened:

- Turn the fixed-jet and two-ended transfer mechanisms into clean lemmas
  stated without cycle language.
- State the Cycle116/119 row as an example following those lemmas, with the
  computed product count as an input.
- Look for a parametric version of the Cycle84 construction, or prove why it
  is inherently isolated.

What should not happen:

- Do not claim that the example is the whole grand challenge.
- Do not present raw computation logs as a proof.
- Do not state "official prize solve" unless the prize submission criteria and
  peer review requirements are separately satisfied.

### Paper B: slack, quotient, and entropy theory

Reference file: `tex/slackMCA_v3.tex`.

Role: Paper B is the main theory paper. It is where corrected reserve
theorems, locator-fiber bounds, residue-line packing, quotient floors, and
local-limit questions belong.

Experimental material feeding Paper B:

- `experimental/notes/l1/`: generated-field locator-fiber material;
- `experimental/notes/m1/`: residue-line and slack-MCA material;
- `experimental/notes/m2/`: line-decoding bridge material;
- `experimental/notes/x1/`: CA/MCA separation material;
- `experimental/notes/domain/`: domain-shattering and quotient-profile work.

Most promising reusable proof targets:

1. **Fixed-jet locator transfer.**
   If a family of co-support locators has enough common leading coefficients,
   one affine line gives many support-wise bad parameters. This should be
   written as a standalone lemma in standard notation.

2. **Two-ended locator transfer.**
   A common nonzero constant coefficient can replace the missing next leading
   coefficient. This avoids the degree-overflow problem in naive padding and
   is a genuinely useful lemma for Paper B.

3. **Residue-line local-limit target.**
   The open positive MCA problem is still to bound arbitrary residue-line
   packing above the corrected reserve, after quotient-periodic components are
   removed.

4. **Generated-field locator local-limit target.**
   The list-side open problem remains a locator-fiber theorem over the
   generated field, not over a silently enlarged challenge field.

5. **Line-decoding bridge.**
   The MCA-to-line-decoding formulation in `experimental/notes/m2/` should be
   sharpened into an equivalence theorem or a separation theorem.

What can be strengthened:

- Replace long cycle packets with a short theorem note:
  fixed-jet lemma, two-ended lemma, proof, and one example.
- Promote only lemmas that have a symbolic proof independent of the Cycle84
  product computation.
- Treat computed product counts as inputs to examples, not as theorem
  mechanisms.

### Paper D: universal cap

Reference file: `tex/cs25_cap_v4.tex`.

Role: Paper D gives the universal threshold cap, conditional on the imported
list-to-agreement conversion.

Experimental material feeding Paper D:

- `experimental/notes/audits/a0_cs25_import_audit.md`;
- `experimental/notes/audits/a0_cs25_rational_constant_derivation.md`;
- cap-constant checks and external import audits;
- Goldilocks and other explicit examples only insofar as they test cap
  numerics or field-size regimes.

What can be strengthened:

- Finish the import audit for the Crites-Stewart conversion and record the
  exact hypotheses.
- Keep Paper D as the canonical source for universal constants.
- Do not let one-row examples compete with the cap theorem; they serve a
  different purpose.

### Paper C: SNARK and protocol ledger

Reference file: `tex/snarks_v4.tex`.

Role: Paper C is the field-accounting and protocol-facing ledger. It should
consume proved results from Papers A, B, and D without mixing:

- generated field;
- line-sampling field;
- verifier challenge field;
- base-code list size;
- interleaved list size;
- MCA, CA, line-decoding, and curve-MCA.

Experimental material feeding Paper C:

- `experimental/notes/protocol/protocol_ledger_template.md`;
- `experimental/data/` schemas and example JSON;
- `experimental/notes/l2/` interleaving notes;
- sampler-map and field-accounting audits from the Cycle117-120 line;
- extension-coordinate and scalar-extension material under `f1/`.

What can be strengthened:

- Prove a clean sampler-map lemma:
  direct uniform line sampling preserves density; balanced projection preserves
  density; identity scalar extension of a base-valued line dilutes density.
- Turn the field-accounting vocabulary into a small theorem-backed checklist.
- Keep protocol soundness claims separate from support-wise MCA examples.

## Experimental Folder Triage

### Keep as proof-facing notes

These folders contain material that can plausibly become reusable theorem
content after editing:

- `experimental/notes/l1/`
- `experimental/notes/m1/`
- `experimental/notes/m2/`
- `experimental/notes/f1/`
- `experimental/notes/l2/`
- `experimental/notes/x1/`
- `experimental/notes/domain/`

The best next move is not to add more labels. The best next move is to extract
the shortest theorem statements and proofs from these folders.

### Keep as computations and examples

These objects are useful, but should not be the main proof narrative:

- Cycle84 product count and replay scripts;
- Cycle116/119/120 explicit `F_17^32` row;
- Goldilocks explicit and existential-beta examples;
- small-field scans;
- JSON receipts and hash manifests;
- raw role returns.

They should appear in appendices, supplementary folders, or example sections.

### Move away from the front door

The front-door narrative should not start from:

- raw Pro/agent returns;
- zip file inventories;
- cycle-by-cycle drama;
- long provenance blocks;
- route labels;
- checker terminal strings.

Those are useful for reproducibility, but a mathematical reader needs the
definition, the theorem, the proof, the computed input, and the exact
non-claims.

## Reusable Lemmas to Promote First

### Lemma 1: fixed-jet locator transfer

Target paper: Paper B, with an example in Paper A style.

Content:

- co-support locators with common top coefficients;
- one affine line;
- support-wise noncontainment;
- slope count equal to distinct locator evaluations.

Current status:

- Symbolic proof exists in the Cycle116 material.
- It should be rewritten without cycle names and with the computed product
  count moved into the example.

### Lemma 2: two-ended locator transfer

Target paper: Paper B.

Content:

- common top `sigma-1` locator coefficients;
- common nonzero constant coefficient;
- global evaluator from selected coefficients;
- one affine line in final parity-check space;
- no naive padding multiplication.

Current status:

- Symbolic proof survived hostile audit.
- It is more reusable than the Cycle119 row itself.
- It should be written as a standalone lemma before more examples are added.

### Lemma 3: scalar-extension density cut

Target paper: Paper C, with relevance to F1.

Content:

- if a base-valued line over `K` is sampled by identity from a proper extension
  `E`, bad parameters remain inside `K`;
- density can drop by the extension factor;
- balanced projection is the safe no-loss alternative.

Current status:

- Useful and conceptually clean.
- Should be separated from the q-challenge discussion and written as a lemma
  about line sampling.

### Lemma 4: tangent CA/MCA separation

Target paper: Paper B or Paper C.

Content:

- clarify which correlated-agreement events imply support-wise MCA and which
  do not;
- prevent protocol proofs from silently switching predicates.

Current status:

- Existing `x1` material should be reviewed and reduced to a short separation
  statement.

### Lemma 5: interleaved support bridge

Target paper: Paper C and Paper D interface.

Content:

- compare base-code and interleaved list quantities at the exact field used by
  the protocol;
- avoid a Cartesian-product overcharge when the interleaved structure has more
  algebra.

Current status:

- Promising, but not as immediate as the two locator-transfer lemmas.

## Main Proof Targets After Recalibration

### Target P1: clean transfer note

Write one note with only:

1. fixed-jet locator transfer;
2. two-ended locator transfer;
3. the Cycle84 computed input as an example;
4. the ABF consequence as an example;
5. exact non-claims.

This should be the immediate next artifact.

### Target P2: parametric fixed-jet families

Try to generalize the Cycle84 mechanism:

- identify which parts are special to the 48 state templates;
- identify which parts are just fixed-jet linear algebra;
- search for a family of fixed-jet locator systems with product spectra that
  can be proved large without a giant computation.

This is the first route from example to theorem family.

### Target P3: corrected MCA local limit

Return to Paper B's main open problem:

- arbitrary residue-line packing;
- quotient-periodic components removed or charged;
- generated-field denominator kept honest.

This is the real positive theorem target.

### Target P4: generated-field locator local limit

Return to L1:

- locator-fiber bounds over the generated field;
- quotient cores handled explicitly;
- no extension-field denominator credit unless a transfer theorem gives it.

### Target P5: protocol ledger compiler

For Paper C:

- exact row;
- exact predicate;
- exact sampler;
- exact field ledger;
- exact interleaving/list/MCA theorem consumed.

This should be a compiler after theorems exist, not a substitute for them.

## Three-to-Four-Cycle Rule

Every 3-4 new experimental cycles should stop and answer:

1. Which paper does this strengthen: A, B, C, or D?
2. Which theorem, lemma, or definition does it improve?
3. Is the output a proof, a computation, a heuristic, or a prompt artifact?
4. What is the first unproved mathematical line?
5. What should be archived away from the front door?

If the answer to question 2 is unclear, the cycle should not continue.

## Immediate Recommendation

Do not spend the next round enlarging the same explicit row.

Do write the clean transfer note:

```text
experimental/notes/m1/fixed_jet_and_two_ended_transfer_note.md
```

The note should be short enough for a human mathematical reader to audit
without reading the raw cycle history. The Cycle84 product computation should
be cited as one computed input, not used as narrative scaffolding.

After that, send workers only against the first false mathematical line in
that note.
