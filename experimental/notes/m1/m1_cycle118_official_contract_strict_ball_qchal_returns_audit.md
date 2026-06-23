# M1 Cycle118 Official Contract / Strict Ball / qchal Returns Audit

Date: 2026-06-23

## Verdict

`BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`

Cycle118 is significant. It does not prove an official Proximity Prize solve,
but it moves the mathematical obstruction materially.

The official-status wall remains:

```text
attached-source finite theorem
  does not imply
authority-pinned official row/event/challenge contract
```

The new mathematical progress is that the strict-ball concern is no longer a
fatal blocker at the finite/source level. Several roles produced strict-inside
support-wise `LD_sw` constructions on the same smooth row

```text
C = RS[F_17^32,H,256], |H|=512
```

with agreement at least `264`, hence Hamming distance at most `248 < 250`.
Since `floor(17^32 / 2^128) = 6`, any authority-retained uniform-line packet
with at least seven surviving slopes is enough for the `2^-128` threshold.

The strongest pasted claim, Role 05's two-ended transfer preserving the full
Cycle84 numerator at agreement `263`,

```text
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

is plausible and important, but is not yet promoted as fully replayed theorem
state until a fail-closed local checker verifies the two-ended evaluator lemma,
the common constant coefficient, the `120/136` partition, and full numerator
retention.

## Raw Preservation

Raw pasted returns are preserved under:

```text
experimental/notes/m1/cycle118_official_contract_strict_ball_qchal_9pro_returns_raw/
```

with `SHA256SUMS.txt`.

Role 07 was corrected after the initial audit. The earlier duplicated Role 06
text has been replaced by the missing qchal/scalar-extension dichotomy return;
`SHA256SUMS.txt` was regenerated and verified after replacement.

Generated `sandbox:/mnt/data/...` links mentioned inside Pro answers were not
downloadable from the pasted text. Their theorem claims are therefore audited
from visible prose only unless separately downloaded later.

## Role Ledger

| Role | Visible label | Conservative audit | Usefulness |
|---|---|---|---|
| 01 | `ROUTE_CUT / BANKABLE_LEMMA / FINITE-CHECKER COUNTERPACKET` | Banks official non-entailment and shows the v1 source-contract checker is underbound. A schema-valid synthetic contract can pass while its source text uses strict radius and excludes Cycle116 agreement-262 events. | Useful checker-design counterpacket. Requires v2 authority contract schema. |
| 02 | `ROUTE_CUT / BANKABLE_LEMMA / CHECKER_COUNTERMODEL` | Same core conclusion as Role 01, plus a clean closed-ball close-point adapter: support-wise agreement `262` gives close line points at distance `<=250`. Strict ball requires `263`. | Strong semantic clarification. Closed-ball external line-decoding adapter is bankable. |
| 03 | `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL` | Proposes a v2 deterministic official-contract state machine with explicit terminals for missing contract, row rejection, event loss, qchal density loss, and acceptance. | Bankable schema design; no official contract supplied. |
| 04 | `PROOF / BANKABLE_LEMMA / ROUTE_CUT` | Claims a strict-inside construction with `LD_sw(C,264) >= 2,630,383` using a new native `j=112, sigma=8` family and `120` padding points. Local spot checks verified the advertised `B0`, `G`, and `P` counts, but not the full field-evaluation injectivity checker. | Significant strict-ball progress; promote as `BANKABLE_LEMMA / PENDING_FULL_REPLAY`. |
| 05 | `PROOF` for `L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE` | Claims full Cycle84 numerator survives at agreement `263` via a new two-ended locator lemma: common top six coefficients plus common nonzero constant coefficient replace a common top seven-jet. The linear algebra is plausible and route-changing, but needs local fail-closed replay. | Most important new mathematical claim. Next exact checker target. |
| 06 | `PROOF / BANKABLE_LEMMA / ROUTE_CUT` | Shows Cycle116 direct line gives `N` exact closed-ball close points at distance `250`, cuts strict radius for the canonical line, and proves no spike/common-support discrepancy above agreement `262`. | Bankable adapter and route cut. |
| 07 | `BANKABLE_LEMMA / ROUTE_CUT / SOURCE-SCOPED PROOF` | Closes `L-CYCLE118-QCHAL-FIELD-THICKENING-OR-DENSITY-LOSS` as a dichotomy. In the attached MCA definition there is no independent `q_chal`; the sampled field is `q_line`. Direct scalar extension of a `K`-valued line to `E/K` adds no new bad slopes, so density dilutes and proper scalar extension kills Cycle116-type lines below `2^-128`. No-loss requires either a balanced challenge-to-slope projection or a genuinely `E`-valued replacement line. Fixed `[512,256]` extensions are support-count cut for `[E:K] >= 5`; degrees `2,3,4` remain open only for genuinely `E`-valued lines. | Important qchal route cut and sampler-map target. Does not supply an official contract. |
| 08 | `PROOF` for Goldilocks prime-field compiler | Claims a fresh prime-field construction over `q=2^64-2^32+1` with `LD_sw(C,264) >= 73,674,899,375,228,060`. Local arithmetic checks verified the Goldilocks prime/order data, `M`, collision-average bound, and `L(q)`. | Very significant fallback if official contract rejects extension fields but accepts this prime row. Needs a deterministic checker and official row decision. |
| 09 | `PROOF / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL` | Synthesizes a smaller same-row strict-inside construction with `LD_sw(C,264) >= 2187`. Local check over bundled slot logs verified all `3^7=2187` selected products are distinct. | Safest immediate strict-ball finite theorem candidate; more than enough for `2^-128` if official retention/sampling accepts it. |

## Local Spot Checks

The following independent spot checks were run locally:

```text
G^7 selected strict packet:
  total tuples = 2187
  distinct product logs = 2187

Role 04 finite subset counts:
  |B0| = 102
  e2 distribution = (6,7,7,5,7,5,5,5,7,7,5,5,5,7,5,7,7)
  |G| = 7
  |P| = 613

Goldilocks:
  q = 18,446,744,069,414,584,321
  7^((q-1)/2) = -1 mod q
  theta = 1,803,076,106,186,727,246
  theta^256 = -1 mod q
  theta^512 = 1 mod q
  M = binom(64,31) = 1,777,090,076,065,542,336
  L(q) = 73,674,899,375,228,060
  251*L(q)-q = 45,655,673,767,658,739 > 0
```

These checks support the visible claims, but they do not replace a dedicated
reviewer-facing verifier for Roles 04, 05, 08, or 09.

## What Changed

Before Cycle118, the live risk was:

```text
Cycle116 proves agreement 262.
If official convention is strict distance < 125/256, then agreement 263 is
needed and Cycle116 might sit exactly on the deleted boundary.
```

After Cycle118:

```text
Closed-ball convention:
  Cycle116's full N = 52,747,567,092 remains enough.

Strict-ball convention:
  At least one same-row finite construction gives agreement 264 with 2187
  distinct slopes, and Role 04 gives a larger 2,630,383-slope construction
  pending full replay.

Possible stronger result:
  Role 05 may preserve the full Cycle84 numerator at agreement 263 via the
  two-ended locator lemma.
```

Thus the strict-ball mathematical wall is likely no longer decisive. The first
official wall returns to the semantic/admissibility layer:

```text
OFFICIAL_TRUST_PIN_MISSING
OFFICIAL_ROW_DECISION_MISSING
OFFICIAL_DISTANCE_CONVENTION_MISSING
OFFICIAL_CHALLENGE_TO_SLOPE_MAP_MISSING
OFFICIAL_EVENT_RETENTION_LEDGER_MISSING
```

Role 07 additionally sharpens the q-field wall:

```text
direct scalar extension of the Cycle116 K-valued line to E/K
  preserves numerator
  but divides by |E|
  hence loses the 2^-128 violation for every proper extension

balanced challenge projection onto K
  preserves density exactly
  but only if the official contract explicitly defines that sampler map
```

So `q_chal` is not a free denominator. The exact missing object is a sampler-map
receipt, not merely a larger field size.

## Claim Discipline

Do not claim:

```text
official Proximity Prize solve
ordinary fixed-word list decoding lower bound
q_chal = q_line
lossless scalar field thickening
full Cycle84 numerator at agreement 263 as locally replayed
```

Safe current claims:

```text
Cycle116 remains banked for source/manuscript closed-ball support-wise MCA.
Cycle118 cuts the v1 official-contract checker as underbound.
Cycle118 provides strict-inside finite/source constructions above the 2^-128
integer threshold, with the 2187-slope packet the safest currently checked one.
Goldilocks prime-field compiler is a serious fallback target, but official
acceptance and full checker replay are pending.
Direct scalar field thickening of the Cycle116 line is route-cut; only balanced
challenge projection or a genuinely larger-field replacement can avoid density
loss.
```

## Next Exact Targets

1. `V-CYCLE118-TWO-ENDED-263-TRANSFER-CHECKER`

   Verify Role 05's full-numerator agreement-263 theorem:

   ```text
   common constant P_T(0) = -1
   A*=theta*eta^[0..119], |A*|=120
   R*=theta*eta^[120..255], |R*|=136
   deg(P_R*(P_T-P_T')) <= 243
   two-ended evaluator basis for sigma=7
   distinct evaluations = 52,747,567,092
   LD_sw(C,263) >= 52,747,567,092
   ```

2. `V-CYCLE119-AUTHORITY-PINNED-STRICT264-ROW-EVENT-QCHAL-CONTRACT`

   Ask the official/source authority to decide the exact row/event/challenge
   semantics. Acceptance needs at least seven final retained slopes and either
   uniform line sampling over `F_17^32` or an explicit challenge-to-slope
   pushforward mass certificate.

3. `V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT`

   Pin the actual challenge source:

   ```text
   challenge_space
   challenge_distribution
   q_chal
   line_field
   challenge_to_line_parameter_map
   bad_event_pullback_or_filter
   duplicate/quotient/charge treatment
   ```

   The useful terminal decisions are:

   ```text
   DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
   BALANCED_CHALLENGE_PROJECTION_NO_LOSS
   IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
   UNDEFINED_MAP_NO_OFFICIAL_CLAIM
   ```

4. `V-CYCLE119-GOLDILOCKS-FIXED-JET-COMPILER-CHECKER`

   Build a deterministic checker for Role 08's prime-field fallback. This is
   the main route if the authority rejects `F_17^32` extension-field rows but
   accepts a large prime smooth multiplicative RS row.

## Bottom Line

Cycle118 is a real progress round. It does not solve the prize by itself, but
it likely removes the strict-ball mathematical objection and exposes the
remaining hard wall as official/admissibility plus challenge/event retention.

In terms of a full solve, the route is now:

```text
finite strict-inside RS-MCA packet
  +
authority-pinned official row/event/challenge contract retaining >=7 slopes
  =
official threshold violation
```

The missing object is no longer primarily "more computation." It is a trusted
contract/sampler-map/replay layer, plus one local verifier for the strongest new
two-ended/full-numerator theorem.
