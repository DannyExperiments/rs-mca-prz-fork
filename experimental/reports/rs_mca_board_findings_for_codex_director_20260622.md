# RS-MCA Route-Board Findings For Codex Director

Status: AUDIT / ROUTE_BOARD_REVIEW / DIRECTOR_HANDOFF.

Date: 2026-06-22.

Prepared by: Codex.

Canonical board updated:
`experimental/RS_MCA_CANONICAL_TRACKER.md`.

## Executive Verdict

No hidden `PROOF` was found. No source-valid `COUNTERPACKET` was found. No
Proximity Prize theorem should be claimed from the current local material.

The board was missing or underweighting several important route corrections:

1. Cycle106 is now sharper than "moment-curve incidence". The 9-Pro returns
   bank a complement-line/rank-one eliminant reduction, but theorem promotion is
   blocked at the source gate. The next exact gates are:

   ```text
   L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER
   L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE
   ```

2. The q=3 D8 story is cut. Fixed-field p=61 shows q=4 has the largest
   distributed dense-tail family under the permissive toy gate.

3. Raw D8B mass is highly density-gate-sensitive. The distributed dense-tail
   family drops:

   ```text
   1/20:  67,696
   1/50:   5,831
   1/100:    866
   1/200:    456
   1/500:      0
   ```

   The possible strict residual is q=5 `(61,12,2)`, not the bulk q=4 family.
   If it survives source-valid filters, use:

   ```text
   D8C-CYCLE106-STRICT-DENSITY-RESIDUAL-TRANSVERSAL
   ```

4. L1 is no longer at "define the repaired object." The repaired objects are
   locally banked and replayed. The live L1 problem is the quantitative
   repaired-object local limit, especially sparse-syndrome/universal primitive
   incidence after quotient-periodic strata are paid.

5. F1 has a sharper arbitrary-anchor wall. The monic-anchor `hatE` base readout
   does not settle arbitrary anchors. The live object is the balanced
   arbitrary-anchor residue cloud:

   ```text
   S -> [Q_S^w]_E
   ```

   The local finite packet shows same locator readout modulo `hatE` can split
   into different support-wise bad slopes under arbitrary anchor, plus a
   sunflower floor term.

6. L2 known quotient-core interleaving is diagonal/sub-Cartesian in the checked
   packets. The product bound overcharges that known obstruction. The live L2
   wall is the aperiodic full-support/codegree remainder, not the already
   diagonal quotient-core packet.

7. X1 tangent CA-MCA separation was missing from the board. A clean same-radius
   same-line CA-to-support-wise-MCA implication is false without a tangent
   correction of scale:

   ```text
   floor(delta n) / q
   ```

8. A3 field-ledger anchors are present after fixing the audit script root path.
   The script finds all required Paper C/blueprint anchors and flags 64
   challenge/extension phrase hits for human review. That is citation hygiene,
   not a theorem failure.

9. The local worktree is far ahead of public upstream. `przchojecki/rs-mca`
   main is the public baseline; the local branch is a director workbench
   containing large experimental expansions and untracked Cycle106 artifacts.
   Do not assume local route-board state is public/reviewer-visible until a
   compact packet is staged.

## Scope And Evidence

### Upstream Comparison

Public upstream checked:

```text
https://github.com/przchojecki/rs-mca
main = 349b487d4d86843bb74ac59526736e7cb4211f04
```

Local worktree:

```text
branch = cycle58-5p5-audit
HEAD   = e557164f6edf085fad5f1a60b99cb9108a1edc84
```

Commands/evidence:

```bash
git ls-remote https://github.com/przchojecki/rs-mca HEAD refs/heads/main
git clone --depth 1 https://github.com/przchojecki/rs-mca /tmp/rs-mca-upstream-compare
git diff --shortstat 349b487d4d86843bb74ac59526736e7cb4211f04..HEAD
```

Observed:

```text
upstream temp clone file count: 271
local worktree file count:     1181
tracked delta local vs upstream main: 817 files, 801028 insertions
upstream-only files in temp comparison: none observed
```

Interpretation: local is a strict director-workbench superset of public main in
this comparison. The upstream repo already has an `experimental/` shell, but
not the expanded Cycle58-106 director artifacts, the canonical tracker, or the
latest Cycle106 stress/density/return-audit packet.

### Local Files Inspected

High-level ledgers:

```text
AGENTS.md
experimental/README.md
experimental/SUMMARY.md
experimental/agents-log.md
experimental/RS_MCA_CANONICAL_TRACKER.md
agent_context/02_STATUS_LEDGER.md
agent_context/03_OPEN_PROBLEMS_AND_BACKLOG.md
agent_context/09_MANAGER_HANDOFF_20260617.md
```

Key route notes:

```text
experimental/notes/m1/m1_cycle106_wallbreaker_9pro_returns_audit.md
experimental/notes/m1/cycle106_family_signature_analysis.md
experimental/notes/l1/l1_arbitrary_fiber_repair.md
experimental/notes/l1/l1_repaired_locator_theorem_package.md
experimental/notes/l1/l1_prefix_divisor_count.md
experimental/notes/f1/f1_arbitrary_anchor_locator_split.md
experimental/notes/f1/f1_extension_coordinate_transfer.md
experimental/notes/l2/l2_interleaved_support_bridge.md
experimental/notes/l2/l2_interleaved_dilation_constants.md
experimental/notes/x1/x1_tangent_ca_mca_separation.md
experimental/notes/audits/a0_cs25_import_audit.md
experimental/notes/audits/a0_external_import_source_check_20260618.md
experimental/notes/audits/a1_paperA_finite_verification_crosswalk.md
experimental/notes/protocol/protocol_ledger_template.md
experimental/notes/certificates/certificate_emit_certificate.md
```

### Replay Commands Run

M1 / Cycle106:

```bash
python3 -m py_compile \
  experimental/scripts/cycle106_kfree_incidence_stress.py \
  experimental/scripts/cycle106_family_signature_miner.py \
  experimental/scripts/cycle106_density_sensitivity_from_signatures.py

python3 experimental/scripts/cycle106_density_sensitivity_from_signatures.py \
  --signature-json experimental/notes/m1/cycle106_p61_family_signature_summary.json \
  --stress-jsonl experimental/notes/m1/cycle106_p61_quotient_index_stress_probe.jsonl \
  --json experimental/notes/m1/cycle106_p61_density_sensitivity_summary.json \
  --density-den 20 --density-den 50 --density-den 100 --density-den 200 --density-den 500
```

L1:

```bash
python3 agent_context/verify_l1_arbitrary_fiber_overcount.py
python3 experimental/scripts/verify_l1_arbitrary_fiber_repair.py
python3 experimental/scripts/verify_l1_repaired_locator_package.py
python3 experimental/scripts/verify_l1_prefix_divisor_count.py
python3 experimental/scripts/verify_l1_syndrome_catalecticant_shells.py
python3 experimental/scripts/verify_l1_quotient_defect_closure.py
```

F1:

```bash
python3 agent_context/verify_f1_extension_counterexample.py
python3 agent_context/verify_f1_fixed_rate_slice.py
python3 agent_context/verify_f1_sigma2_degree1.py
python3 experimental/scripts/codex_f1_l1_20260617/verifiers/verify_f1_arbitrary_anchor_split.py
python3 experimental/scripts/verify_f1_extension_witness.py
```

L2:

```bash
python3 experimental/scripts/verify_l2_interleaved_constants.py
python3 experimental/scripts/verify_l2_quotient_core_count.py
python3 experimental/scripts/verify_l2_extension_coordinate.py
```

P3/audit tooling:

```bash
python3 experimental/scripts/verify_q17_locator_mca.py \
  --check experimental/data/certificates/q17-locator-mca/q17_locator_mca_certificate.json

python3 experimental/scripts/restricted_sum_dp.py \
  --p 17 --subgroup-order 16 --r 9 --expect-full

python3 experimental/scripts/field_ledger_vocabulary_audit.py

python3 experimental/scripts/certificate_emit.py \
  --input experimental/data/certificates/certificate_emit_example.json \
  --format markdown
```

## Findings By Route

## M1 / Cycle106

### What Is Banked

Cycle105 remains the last clean `BANKABLE_LEMMA` spine:

```text
L-CYCLE105-KFREE-COLLAPSE-AND-COMPLEMENT-DUALITY
```

Cycle106 9-Pro returns added a bankable structural reduction. With
`d=sigma+1`, `m=n-s`, and

```text
V(X)=Uhat(X)^(-1) mod X^(d+1)=sum_{j=0}^d v_j X^j
```

activity is reduced to an affine complement line meeting the `m`-subset
elementary-symmetric layer:

```text
theta active <=> (v_j - theta*v_{j-1})_{j=1}^d in M_m.
```

A degree-`D` separator/rank-escape certificate would give:

```text
|Gamma cap M_s| <= D.
```

This is significant because it turns "incidence bound" into a falsifiable
rank-escape theorem.

### What Is Not Banked

The return audit explicitly blocks promotion:

```text
No PROOF.
No source-valid COUNTERPACKET.
```

The missing source gates are:

```text
formal AP_corr(Uhat) predicate
official bad-slope-to-aperiodic-Gamma cover
endpoint convention when sigma+1=n
```

The p97 finite candidate is useful stress data but not a counterpacket:

```text
active theta count:          7
external active theta count: 6
checker decision: ROUTE_CUT_FINITE_MODEL_TOO_WEAK
```

### What The Other Director May Have Missed

The finite stress families D3/D8 are not the top theorem gate anymore. They are
diagnostics for the source AP predicate and rank escape. The exact next theorem
work should be:

```text
Gate A: L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER
Gate B: L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE
```

D3/D8 still matter, but only after they are tested against the real source gate.

## D3 / D8 Stress Families

### D3A

Current label:

```text
D3A-CYCLE106-DOMINANT-H-COSET-OUTLIER-CHARGE
```

Finite signature:

```text
31,798 dominant-cluster rows in the original extended sigma-2 grid
31,086 / 31,798 are two-H-coset covers
30,234 are cluster-plus-one
1,564 are cluster-plus-two
```

Density sensitivity at p=61:

```text
1/20:  109,578
1/50:   11,658
1/100:   3,273
1/200:   1,623
1/500:      48
```

Read: D3A is real finite stress structure, but it shrinks hard. The right proof
target is to charge `[m,1]` and `[m,1,1]` profiles to quotient/near-coset
branches under the true AP predicate.

### D8B / D8C

Old D8A:

```text
D8A-CYCLE106-QUOTIENT-THREE-DENSE-TAIL-TRANSVERSAL
```

This is cut. Fixed p=61 gives:

```text
q=3 (61,20,2):  8,080 distributed dense-tail rows
q=4 (61,15,2): 59,160 distributed dense-tail rows
q=5 (61,12,2):    456 distributed dense-tail rows
q=6 (61,10,2):      0
```

So quotient index 3 is neither necessary nor the largest case in the fixed
field comparison.

Current D8B:

```text
D8B-CYCLE106-DENSITY-ADMITTED-DENSE-TAIL-TRANSVERSAL
```

But D8B is unstable under stricter density gates:

```text
1/20:  67,696
1/50:   5,831
1/100:    866
1/200:    456
1/500:      0
```

The strict-density residual at gate `1/200` is only q=5 `(61,12,2)` with 456
rows. That suggests a narrower possible target:

```text
D8C-CYCLE106-STRICT-DENSITY-RESIDUAL-TRANSVERSAL
```

Do not let a worker attack the entire raw D8B mass unless the real reserve
admits the toy `1/20` density layers. Most of that mass is probably an artifact
of permissive finite gating.

## L1 / Generated-Field Locator

### What The Board Had Stale

The old board phrased L1 as if the repaired object still needed definition.
That is stale.

The repo now has repaired identities and finite replay evidence:

```text
ImgFib/list equality:                PROVED identity
MaxFib/list equality for s>k:        PROVED identity
canonical selector fiber:            PROVED after ordering
primitive locator-cofactor shells:   PROVED identity
sparse syndrome shell formulation:   PROVED identity / CONJECTURAL bound
raw universal support fiber bound:   COUNTEREXAMPLE
```

Replay highlights:

```text
U=0 overcount packet:
|Fib_0(11)| = binom(16,11) = 4368
actual list size for U=0 = 1

L1 repaired fiber verifier: PASS
L1 repaired locator package verifier: PASS
L1 prefix divisor-count verifier: PASS
L1 syndrome catalecticant shells: PASS
L1 quotient-defect closure: PASS
```

### Correct Current Wall

The L1 live wall is not object repair. It is the quantitative local limit for
the repaired object:

```text
repaired image/maximal/full-support local limit
sparse-syndrome local limit
universal primitive incidence / RIM rank theorem
monomial-prefix Fourier/subgroup-sum bound
```

The prefix divisor note gives the clean split:

```text
quotient floor: exact and field-independent
entropy: controls only aperiodic remainder
dimension dithering target: gcd(n,k+sigma) <= sigma
```

Director prompt should not say "define a repaired L1 object." It should say:

```text
Prove or refute the aperiodic repaired-object local limit after quotient
strata are paid, beginning with sparse-syndrome/universal primitive incidence.
```

## F1 / Extension Lines

### What Is Firm

The unrestricted same-numerator extension-line lift is false.

Replay:

```text
B=F_7,  F=F_49:    extension bad slopes = 15/49
B=F_17, F=F_17^2:  extension bad slopes = 288/289
```

The fixed-rate and sigma-2 finite checks also pass:

```text
p=7, k=3, d=3:    slice slopes 6/49
p=17, k=8, d=3:   slice slopes 36/289
p=31, k=15, d=3:  slice slopes 120/961
p=97, k=48, d=5:  slice slopes 1176/9409

p=17,k=8,sigma=2,d=3: distinct slopes 238/289
p=19,k=9,sigma=2,d=2: distinct slopes 360/361
```

### What Was Missing On The Board

The arbitrary-anchor split is sharper than the old "arbitrary anchors remain
open" phrase.

The finite packet has:

```text
B = F_17
F = F_17[alpha], alpha^2 = 3
k = 3
sigma = t = 2
E = X(X-alpha)
N = 1
```

Supports:

```text
S = {1,3,4,7,9}
T = {1,2,11,12,16}
```

They have the same locator readout modulo:

```text
hatE = X(X-alpha)(X+alpha)
```

but arbitrary anchor splits slopes:

```text
z_S = 0
z_T = 1
```

The verifier also records a sunflower floor with six slopes.

### Correct Current Wall

The live F1 object is:

```text
S -> [Q_S^w]_E
```

where `Q_S^w` is the unique degree-`<a` interpolant of the arbitrary anchor
word `w` on `S`.

Any repaired theorem must include at least the structural lower term:

```text
floor((|D|-k)/sigma)
```

or an equivalent certificate term.

Director prompt:

```text
Bound or refute the balanced arbitrary-anchor residue cloud over F_{p^2} for
sigma=t=2, including the sunflower floor term.
```

## L2 / Interleaved Lists

### What Is Firm

The checked quotient-core interleaved packet is diagonal, not Cartesian.

Replay highlights:

```text
verify_l2_interleaved_constants.py: PASS
verify_l2_quotient_core_count.py: PASS
verify_l2_extension_coordinate.py: PASS
```

Prize-like quotient-core examples show:

```text
n=256,k=64,M=4,mu=2: L_mu = diagonal L, not L^2
n=256,k=64,M=4,mu=3: L_mu = diagonal L, not L^3
n=1024,k=256,M=8,mu=2: L_mu = diagonal L, not L^2
```

The extension-coordinate identity checks:

```text
B=F_17, F=F_17^2, n=16, k=6, a=8
|Lambda(C_F)| = 33 = coordinate-interleaved base list
```

### Correct Current Wall

Do not ask whether the known quotient-core packets multiply under
interleaving. They do not in the aligned checked cases.

The open problem is:

```text
aperiodic mu-fold full-support/codegree remainder
```

The certificate-facing object should track full-support intersections and
codegrees, not just row list sizes.

## X1 / CA-MCA Bridge Hygiene

This was absent from the board and should stay visible.

The note `experimental/notes/x1/x1_tangent_ca_mca_separation.md` proves a
pairwise separation:

```text
(f,g) is delta-close to C^2
same pair has at least floor(delta n) support-wise MCA-bad slopes
same-line CA predicate does not see them
```

Consequently, any same-radius bridge from CA to support-wise MCA needs:

```text
additive tangent term floor(delta n)/q
```

or an explicit support predicate excluding/certifying tangent patterns.

This is not a global comparison of `eca` and `emca`; it is a route cut against
a sloppy local bridge.

## A0 / Paper D Import

A0 remains conditional.

No internal arithmetic failure has been found in the existing audits, but the
primary Crites-Stewart/list-to-agreement import still needs a source-level
pass/fail table:

```text
admissible delta
augmented code C+
CA normalization
slope sampling field
radius/off-by-one conventions
contrapositive monotonicity
extension-field scope
constants
```

Do not promote Paper D universal cap to `PROVED`. Do not call it error-one.

## A1 / Paper A Finite Replay

Fresh local replay:

```text
verify_q17_locator_mca.py --check .../q17_locator_mca_certificate.json
result: certificate matches

restricted_sum_dp.py --p 17 --subgroup-order 16 --r 9 --expect-full
result: full coverage, missing_count = 0
```

A1 still needs complete deterministic certificates for all V1-V5 if the public
review layer wants full standalone reproduction, but the q17 and p17/r9
anchors are replayed.

## A3 / Field Ledger

I found and fixed an audit-script issue:

```text
field_ledger_vocabulary_audit.py repo_root() pointed at experimental/
instead of the repository root.
```

After the one-line root fix, the audit runs from repo root.

Replay result:

```text
all required Paper C and blueprint field-ledger anchors found
64 challenge/extension-field phrase hits lack same-line q_gen/q_line/q_chal macro
```

Interpretation: this is not a proof failure. It is a review queue for
field-ledger hygiene. Any protocol-facing report should keep `q_gen`, `q_line`,
`q_chal`, `B`, and `F` explicit.

## A4 / Certificate Compiler

`certificate_emit.py` renders the toy example:

```bash
python3 experimental/scripts/certificate_emit.py \
  --input experimental/data/certificates/certificate_emit_example.json \
  --format markdown
```

But A4 is not a full certificate compiler. It is sample tooling plus schema.
The next useful artifact is an obstruction-audit sample certificate that
actually consumes live A0/L1/L2/M1/F1 statuses.

## Public/Upstream Hygiene

Public upstream main is compact. Local is large and provenance-heavy.

Do not push raw local state wholesale. The reviewable package should be compact:

```text
experimental/RS_MCA_CANONICAL_TRACKER.md
this report
Cycle106 compact scripts and JSON summaries
Cycle106 9-Pro audit note, not necessarily all raw chat outputs
updated agents-log
minimal verifier receipts
```

Raw returns are valuable provenance but should not be the public-facing summary
unless a reviewer specifically asks for them.

## Board Corrections Applied

Updated:

```text
experimental/RS_MCA_CANONICAL_TRACKER.md
```

Key additions:

```text
Public upstream baseline checked
X1 row
L1 repaired-object correction
F1 arbitrary-anchor residue-cloud correction
L2 diagonal quotient-core correction
A3 replay/root-fix correction
A4 sample-emitter-only correction
new replay rows in Evaluation and Testing Ledger
new refinement decisions R-20260622-24 through R-20260622-29
query keys for CYCLE106_9PRO_RETURNS, X1_GAP, PUBLIC_BASELINE
```

## Exact Next Director Prompts

### M1 / Cycle107

```text
Prove or refute Gate A:
L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER.

Input: official residual bad-slope definitions, Cycle105 k-free collapse,
Cycle106 complement-line normal form, and all banked quotient/periodic cuts.

Output: either a proof that every official bad slope normalizes to AP_corr(Uhat)
or is charged to a banked branch, or a source-valid obstruction packet.
```

Then:

```text
Prove or refute Gate B:
L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE.

Input: formal AP_corr(Uhat), complement line
theta -> (v_j - theta*v_{j-1})_{j=1}^d, subset layer M_m.

Output: degree-D rank escape/separator theorem, or explicit AP_corr-valid
family contained in bounded-degree exceptional closure.
```

### L1

```text
Stop re-defining the repaired fiber object.
Prove or refute the repaired image/maximal/full-support local limit after
quotient strata are paid, beginning with sparse-syndrome/universal primitive
incidence and monomial-prefix Fourier/subgroup-sum reductions.
```

### F1

```text
Attack the balanced arbitrary-anchor residue cloud S -> [Q_S^w]_E over F_{p^2}
for sigma=t=2. Include the sunflower floor term. Decide whether the cloud is
bounded above reserve or yields a source-valid extension-valued stress family.
```

### L2

```text
Bound the aperiodic mu-fold full-support/codegree remainder after removing
diagonal quotient-core packets. Produce either a sharp-constant theorem, a
finite aperiodic counterpacket, or a protocol-ready codegree certificate.
```

### X1

```text
Thread the tangent support correction floor(delta n)/q through every CA/MCA
or line-decoding bridge before any protocol certificate consumes the bridge.
```

### A0

```text
Finish the primary-source Crites-Stewart import audit with a pass/fail table
for hypotheses, normalization, fields, constants, radius conventions, and
contrapositive monotonicity.
```

## What Not To Claim

Do not claim:

```text
RS-MCA prize solved
M1-C106 proved
Cycle106 p97 finite stress is a COUNTERPACKET
D8 is quotient-index-three
raw D8B mass is source-valid
raw arbitrary L1 support fibers are bounded
monic-anchor F1 settles arbitrary anchors
known L2 quotient-core packets multiply as L^mu
Paper D cap is unconditional
certificate_emit.py is a full protocol compiler
local branch state is already public upstream state
```

## Confidence

High confidence:

```text
local verifier outputs reported here
local-vs-upstream commit/file-count comparison
q=3 D8 cut under fixed p=61 finite probe
D8B density-gate sensitivity totals
L1 object-repair board correction
F1 arbitrary-anchor split board correction
L2 diagonal quotient-core board correction
X1 tangent separation board addition
```

Moderate confidence:

```text
route priority ordering after Cycle106 returns
which compact artifacts should be public-review staged first
```

Low/unknown:

```text
whether D8C survives the true AP_corr/reserve gate
whether complement-line escape is true under the eventual AP_corr predicate
whether the F1 arbitrary-anchor residue cloud has a polynomial bound above reserve
whether L1 sparse-syndrome/universal primitive incidence is true
whether A0 primary import fully matches without a corrected constant
```

Bottom line: the director board is now sharper and less misleading. The next
work should not be "more broad exploration"; it should be source-cover and
rank-escape on M1, quantitative repaired-object local limits on L1, arbitrary
anchor residue-cloud control on F1, aperiodic codegree constants on L2, and a
bounded primary-source audit on A0.
