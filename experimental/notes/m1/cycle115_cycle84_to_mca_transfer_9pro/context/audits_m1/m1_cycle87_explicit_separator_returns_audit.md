# Cycle 87 Explicit Separator Returns Audit

Date: 2026-06-21

## Verdict

**Status: PROOF_CERTIFICATE_PASS / BANKABLE_LEMMA /
INDEPENDENT_REPLAY_PENDING.**

The round is highly significant. The visible-text conflict was resolved by the
downloaded Role 02/06 artifacts: they include a concrete `y = U` replay bundle,
certificate files, shard summaries, source, logs, and lightweight verifiers.
Those artifacts pass internal checksum and Python verification locally.

This is still not an independent full replay of the 52,747,567,104-record
census from source. The correct conservative statement is therefore:

> Cycle87 supplies a verified certificate package for the explicit
> `U`-separator 464-point MCA failure row. Treat as a proof certificate pending
> independent replay, not as a theorem promoted into the main papers.

## Raw Returns

Raw visible ChatGPT responses and page extracts are preserved in:

`experimental/notes/m1/cycle87_explicit_separator_returns_raw/`

Role 04 terminated with a network-error response and is not a mathematical
return.

Generated file cards observed in the browser and later downloaded:

- Role 02: `Replay bundle`, `Master certificate`, `PASS certificate`
- Role 03: `Generic separator replay script`
- Role 06: `Replay certificate bundle`
- Role 08: `Download the Cycle87 certificate-engineer bundle`

These generated files are now preserved in the raw folder. The top-level raw
folder has `SHA256SUMS.txt`.

Downloaded artifact files:

- `02_cycle87_explicit_two_copy_separator_certificate.zip`
- `02_cycle87_master_certificate.json`
- `02_cycle87_u_separator_replay_bundle.zip`
- `02_CYCLE87_U_SEPARATOR_PROOF.md`
- `03_cycle87_role03_generic_separator_certificate.py`
- `03_cycle87_role03_generic_separator_result.json`
- `06_cycle87_u_separator_pass.json`
- `06_cycle87_u_smooth_census_result.json`
- `08_cycle87_certificate_engineer_bundle.zip`

## Role Ledger

| Role | Visible label | Conservative audit | Usefulness |
| --- | --- | --- | --- |
| 01 | `BANKABLE_LEMMA` | Bankable conditional algebra | Validates the 464 package as a newly constructed GRS code, not ordinary puncturing. |
| 02 | `PROOF` | Certificate-level pass, independent replay pending | Supplies replay bundle and master certificate; local checksum/master verification passed. |
| 03 | `BANKABLE_LEMMA` | Bankable existential separator | Proves a generic cubic separator exists with projective multiplicity 1; not explicit. |
| 04 | network error | No usable return | Ignore except as dispatch/error provenance. |
| 05 | `BANKABLE_LEMMA` | Bankable red-team audit | Finds no fatal flaw in 464 construction, but says explicit separator census remains missing. |
| 06 | `PROOF` | Certificate-level pass, independent replay pending | Claims `y=U`, `mu_proj(U)<=2`, 464 one-GRS/one-line construction, and official target margin; local verifiers passed. |
| 07 | `AUDIT` | Bankable ledger audit / route cut | Says the official fail row follows from `mu_proj(y)<=8`, but no row can be added without projective census/materialization. |
| 08 | `BANKABLE_LEMMA` | Bankable checker reduction / exact wall | Discharges tau folding and 464 geometry, but states the numerical census is unrun. |
| 09 | `BANKABLE_LEMMA` | Bankable referee synthesis | Chooses 464 + exact projective occupancy as primary route; warns a ninefold class does not kill the route. |

## What Progressed

Cycle 87 substantially clarified the endgame:

1. The preferred package is now the direct 464-point construction
   `(n,k,sigma,j)=(464,232,6,226)`, not the 560 fallback.
2. The construction should be treated as one fresh `[464,232]` GRS code over
   `F_17^48`, with a single affine syndrome line.
3. The relevant slope count is governed by projective occupancy of
   `P_T(y)` over the banked one-copy packet, not by naive additive or tensor
   two-copy composition.
4. A sufficient explicit wall is
   `mu_proj(y) <= 8`; the sharper necessary occupancy condition is
   `Q_y >= 6,419,576,048`.
5. The exact checker wall is now:

   `V-CYCLE87-U-TAU-FOLDED-SMOOTH-MMAX8-CENSUS`

   with exact refinement if the smooth quotient has a threshold-crossing key.

## Why This Is Significant

If the Role 02/06 replay artifacts verify, this becomes an explicit
official-profile finite MCA failure row:

`q_gen = q_code = q_line = q_chal = 17^48`,

`(n,k,sigma)=(464,232,6)`,

and the claimed conservative numerator exceeds

`floor(17^48 / 2^128) = 338,617,018,271,848,945,628`.

That would be the strongest route-changing event so far in this lane: not a
full prize theorem, but a concrete finite official-rate obstruction candidate.

Conservatively, before file audit, the bankable result is still very strong:
the algebraic wrapper and exact checker target are sharply specified, and the
remaining work is reduced to a finite replayable occupancy/census certificate.

## Conflict To Resolve

The visible returns had an apparent conflict:

- Roles 02 and 06 claim an executed census proving `mu_proj(U) <= 2`.
- Role 08 says the full multiplicity census is still unrun.
- Role 07 says no ledger row can be added without the projective census and
  replayed 464 materialization.
- Role 09 says no supplied context proves `U` passed, but the generic theorem
  guarantees some cubic separator.

Resolution: Role 08 was a checker-specification return, while Role 02/06 later
supplied a concrete replay/certificate package. The downloaded package resolves
the visible conflict at certificate level. Independent full replay is still the
remaining external-validation step.

## Local Artifact Audit

Performed locally on 2026-06-21:

- Copied all downloaded Pro artifacts into
  `cycle87_explicit_separator_returns_raw/`.
- Generated raw-folder `SHA256SUMS.txt`.
- Extracted the three downloaded bundles under `/tmp/cycle87_audit_extract`.
- Ran `shasum -a 256 -c SHA256SUMS.txt` inside:
  - `cycle87_u_separator_replay_bundle`
  - `cycle87_explicit_two_copy_separator_certificate`
  - `cycle87_certificate_engineer_bundle`
- Ran Role 02 replay-bundle verifiers:
  - `python3 cycle87_verify_master.py`
  - `python3 cycle87_setup_verifier.py`
  - `python3 cycle87_verify_464_artifacts.py`
- Ran Role 02/06 certificate aggregation:
  - `python3 aggregate_cycle87_census.py`
  - `python3 verify_cycle87_symbolic.py`
- Ran Role 08 checker-bundle smoke verifiers:
  - `PYTHONPATH=src python3 src/verify_u_slot_logs.py examples/cycle87_u_slot_smooth_logs.json`
  - `PYTHONPATH=src python3 src/verify_geometry_464.py`
  - `PYTHONPATH=src python3 src/verify_result_envelope.py examples/REFINE_REQUIRED.example.json`

Observed decisive certificate values:

- Records: `52,747,567,104`
- Projected distinct keys: `52,747,567,062`
- Projected ordered off-diagonal energy: `84`
- Projected maximum multiplicity: `2`
- Smooth/projective histogram: `m1 = 52,747,567,020`,
  `m2 = 42`, `m_ge_3 = 0`
- Profile: `(n,k,sigma,j,t) = (464,232,6,226,1)`
- `q_gen = q_code = q_line = q_chal = 17^48`
- `floor(q_line / 2^128) = 338,617,018,271,848,945,628`
- Certified distinct slopes:
  `1,391,152,917,379,006,070,784`
- Margin over target:
  `1,052,535,899,107,157,125,156`

The downloaded Role 02 master verifier returned:

`CYCLE87_MASTER_CERTIFICATE_VERIFIED`

The symbolic verifier returned:

`CYCLE87_EXPLICIT_U_SEPARATOR_AND_464_GRS_V1 / PASS`

## Next Exact Step

Immediate:

`V-CYCLE87-INDEPENDENT-REPLAY-OR-PUBLIC-LIGHT-REPLAY`

Run an independent replay path where practical. At minimum, preserve the
certificate package publicly and ask PRZ or GitHub Actions to verify the
lightweight certificate chain. A full 52.7B-record rerun remains the strongest
external confirmation.

Assuming this certificate package survives review, promote:

`L-CYCLE87-464-U-OFFICIAL-MCA-FAIL-ROW`

Then the next bridge is:

`L-CYCLE88-464-U-OFFICIAL-MCA-FAIL-TO-PROXIMITY-PRIZE-BRIDGE`

If independent replay fails, fall back to:

`V-CYCLE87-U-TAU-FOLDED-SMOOTH-MMAX8-CENSUS`

or materialize a different explicit `y` using the generic separator theorem.
