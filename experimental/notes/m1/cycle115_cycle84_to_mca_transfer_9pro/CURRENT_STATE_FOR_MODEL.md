# Current State For Cycle115 Workers

## 1. The fixed finite anchor

The standalone finite certificate in `context/cycle84_finite_certificate/` verifies the explicit Cycle84 model over

```text
F = F_17[X]/(X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

with the seven-slot color-filtered packet model and color condition `c_L + c_R = 4 mod 16`.

The reviewable certificate verifies:

```text
compatible_pairs = 52,747,567,104
distinct_products = 52,747,567,092
ordered_offdiagonal_energy D = 24
true double fibers = 12
no fiber of size >= 3
m_max(beta) = 2
```

Treat this as a black-box finite theorem. Do not spend effort reproving Cycle84 unless you find a direct contradiction inside the supplied standalone certificate.

## 2. What Cycles85-114 already changed

Cycle84 alone is a finite/model theorem. The later cycles were not wasted; they are the accumulated transfer scaffolding and route cuts.

Key audited state:

- Cycle85 proposed a one-copy finite MCA slope lower certificate over `F0 = F_17^16`, with `(n,k,sigma,j)=(256,137,6,113)`. It is finite and useful, but not automatically prize-facing because `q_line=17^16` is too small for a `2^-128` denominator claim.
- Cycle88/Cycle89 proposed a two-copy / extension-field bridge producing a candidate `[464,232]` GRS/RS row over `q_line=17^48`, with numerator candidate
  `N*P/2 = 1,391,152,917,379,006,070,784`
  against
  `floor(17^48 / 2^128) = 338,617,018,271,848,945,628`.
  This would be far above threshold if all transfer hypotheses are official.
- Cycle90-114 repeatedly showed that the decisive wall is not another Cycle84 computation. It is the official source / prize-family / field-ledger / retained-slope transfer. In particular, arbitrary finite rows, arbitrary domains, or model stress packets are not prize statements unless they pass the official RS-MCA definitions and field-denominator ledger.
- The canonical tracker currently says the live wall is an authority-pinned official contract/replay problem for the later M1 low-`t=1` route. For this Cycle115 round, however, the focus is narrower: PRZ asked specifically whether the Cycle84 finite certificate has a clean transfer theorem into MCA/list/line-decoding over RS parameters.

## 3. The exact Cycle115 question

Give the strongest exact statement you can, with proof or a precise obstruction:

```text
What theorem would turn Cycle84's finite color-filtered
m_max(beta)=2 certificate into an MCA / list / line-decoding statement
over Reed--Solomon parameters?
```

The answer may be:

- a `PROOF` of a finite RS-MCA or line-decoding transfer statement;
- a `BANKABLE_LEMMA` giving a narrower transfer with clearly named remaining hypotheses;
- a `ROUTE_CUT` showing the proposed transfer cannot be official/prize-facing;
- an `EXACT_NEW_WALL` naming the first missing theorem or source contract;
- a `COUNTERPACKET` showing a stated transfer theorem is false.

## 4. Dangerous places to audit

Do not blur these:

- finite/model certificate versus official RS-MCA theorem;
- `q_gen`, `q_line`, `q_code`, and `q_chal`;
- support-wise MCA versus list-decoding versus line-decoding;
- arbitrary evaluation set versus smooth multiplicative subgroup/coset;
- GRS versus RS and whether diagonal scaling is harmless for the exact definition used;
- reciprocal-affine slope normalization and whether it is injective after quotient/periodic/contained/same-slope collapses;
- one-copy `17^16` arithmetic versus two-copy `17^48` arithmetic;
- bad-slope numerator before and after endpoint, tangent, contained, periodic, affine-color, and source charges.

## 5. Source files most likely to matter

Start with:

- `context/cycle84_finite_certificate/STANDALONE_FINITE_CERTIFICATE.md`
- `context/RS_MCA_CANONICAL_TRACKER.md`
- `context/rs_mca_board_findings_for_codex_director_20260622.md`
- `context/audits_m1/m1_cycle85_role05_transfer_returns_audit.md`
- `context/audits_m1/m1_cycle88_cycle87_bridge_audit.md`
- `context/audits_m1/m1_cycle89_official_mca_row_audit.md`
- `context/notes_m2/m2_line_decoding_mca_bridge.md`
- `context/tex/slackMCA_v3.tex`, especially `def:mca`, `def:residue`, `thm:normalform`
- `context/tex/RS_disproof_v3.tex`, especially the no-slack support-wise line-MCA definition
- `context/tex/snarks_v4.tex`, especially q-ledger and line-decoding interface language
- `context/readme.md`, especially the generated/line/challenge field ledger

Use Cycle90-114 audit files when you need to know why a tempting transfer was later cut.
