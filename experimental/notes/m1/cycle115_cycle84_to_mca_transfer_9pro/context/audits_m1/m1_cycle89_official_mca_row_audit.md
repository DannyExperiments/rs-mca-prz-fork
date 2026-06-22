# Cycle 89 Official MCA Row Identification Audit

## Verdict

**BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL.**

Cycle89 proves the conditional official-definition bridge:

```text
L-CYCLE89-OFFICIAL-MCA-ROW-IDENTIFICATION
```

Assuming the Cycle84/Cycle85/Cycle87 finite certificate facts, the Cycle87 counted slopes are support-wise line-MCA bad slopes in the sense of `def:mca` / `def:residue` in `tex/slackMCA_v3.tex`, via the `(>=)` direction of `thm:normalform`.

This is not yet an official prize counterpacket. The live wall is now:

```text
W-CYCLE90-PRIZE-FAMILY-EMBEDDING
```

Cycle87/Cycle89 give a contrived finite GRS/RS row with `n=464=2^4*29`. The prize-facing source language emphasizes smooth multiplicative domains, especially power-of-two multiplicative subgroups. The next step is to prove either that the prize formulation admits this arbitrary finite row, or that the construction embeds/ports to an actual smooth power-of-two subgroup row.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle89_official_mca_row_raw/
```

Files preserved:

```text
FILE_INDEX_FOR_MODEL.md
input_manifest.json
prompt_sent.md
raw_response.json
raw_response.jsonl
response.md
run_result.json
run_status.json
SHA256SUMS.txt
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T08-48-00-324Z-cycle89-official-mca-row-identification-131b06b0
model: claude-opus-4-8
mode: artifact_stream
status: OK
elapsed: 347821 ms
cost: 2.54018825 USD
capture warning: none
```

## Banked Claim

Conditional theorem:

```text
(t,n,k,sigma,j) = (1,464,232,6,226)
delta = 1 - (k+sigma)/n = 1 - 238/464
q_line = q_gen = q_code = q_chal = 17^48
```

Given the Cycle84/Cycle85/Cycle87 antecedents, the explicit `[464,232]` GRS row over `17^48` has at least

```text
N*P/2 = 1,391,152,917,379,006,070,784
```

distinct noncontained bad slopes. The exact integer target is

```text
floor(17^48 / 2^128) = 338,617,018,271,848,945,628
```

so the conditional row clears the `2^-128` MCA numerator threshold by

```text
1,052,535,899,107,157,125,156
```

## Definition Check

Cycle89 checks the following source identifications.

- `def:mca` counts bad parameters `z` for a line `f+zg` with denominator `|F|`.
- `def:residue` supplies exactly the noncontained witness datum used by the Cycle87 construction.
- `t=1` is legal because `1 <= t <= r = n-k = 232`.
- `|S|=238` equals `s_delta = ceil((1-delta)n)`.
- `j=226` is only the complement/co-support size `n-k-sigma`; it is not an extra condition in the MCA definition.
- Noncontainment is exactly `def:mca(ii)`.
- Same-slope collisions and projective/quotient collapsing are already paid by the Cycle87 multiplicity bound and the conservative division by two.
- `q_line=17^48` is the only denominator in the MCA error. The base `17^16` field is not the slope field.

The GRS-vs-RS issue is harmless for the numerator: diagonal scaling preserves support-wise agreement and noncontainment, so the row can be read as an isometric RS row on the same finite domain.

## Source-Scope Audit

The bounded local source check supports the new wall rather than an immediate prize upgrade.

Relevant source facts:

- `tex/slackMCA_v3.tex` abstract: the document studies RS codes on smooth multiplicative domains, specifically subgroups `H <= F_q^*` of power-of-two order `n`.
- `tex/RS_disproof_v3.tex` says the Proximity Prize concerns smooth multiplicative domains and states that the paper's counterexamples use multiplicative subgroups of power-of-two order.
- `readme.md` keeps the field ledger separate and describes smooth multiplicative domains, usually subgroup/coset power-of-two domains.

Therefore Cycle89 closes the *definition* gap but not the *prize-family* gap.

## Dependencies Still Open

1. Independent replay or reviewer acceptance of the Cycle84/Cycle85/Cycle87 finite census chain.
2. `W-CYCLE90-PRIZE-FAMILY-EMBEDDING`:

```text
Either:
  A. exhibit a smooth power-of-two multiplicative subgroup RS row
     inheriting the Cycle87 bad-slope surplus; or
  B. prove that the official prize formulation accepts arbitrary finite
     RS/GRS rows, in which case Cycle89 plus replay becomes a counterpacket.
```

## Next Prompt

Cycle90 should attack the prize-family admissibility wall directly, not re-check the MCA definition.

