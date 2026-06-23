# Common Prompt: Cycle119 Role05 Two-Ended Upgrade / qchal Sampler / Goldilocks Fallback

You are one of nine fresh theorem-worker instances. Work only from the attached files and your own reasoning.

No Internet. Do not browse. Do not cite external sources. Take all the time to reason you need. Use MAX reasoning. Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. Do you see a route to a full solve? If yes, what is the next exact lemma, checker, or construction?

This round is proof-first and adversarial. Do not merely summarize the packet. Either prove the assigned target, produce a checkable verifier/spec, or find the exact fatal line.

## Current Critical State

Cycle116 is banked as a finite, source-scoped support-wise RS-MCA / `LD_sw` theorem:

```text
C = RS[F_17^32,H,256], |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128
```

Do not call that an official Proximity Prize solve. It is not ordinary list decoding, not protocol soundness, and not asymptotic.

Cycle118 likely removed the strict-ball mathematical objection at the finite/source level, but did not close official prize status. The remaining walls are:

```text
V-CYCLE118-TWO-ENDED-263-TRANSFER-CHECKER
V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT
V-CYCLE119-AUTHORITY-PINNED-STRICT264-ROW-EVENT-QCHAL-CONTRACT
V-CYCLE119-GOLDILOCKS-FIXED-JET-COMPILER-CHECKER
```

## Main Candidate Under Attack

Role05 claims:

```text
L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

The claimed mechanism is a two-ended locator functional:

```text
common top six locator coefficients
+ common nonzero constant coefficient P_T(0) = -1
```

using:

```text
A* = {theta eta^i : 0 <= i <= 119}, |A*|=120
R* = {theta eta^i : 120 <= i <= 255}, |R*|=136
J_T* = J_T union R*, |J_T*|=249
agreement = 512 - 249 = 263
```

Do not assume Role05 is correct. Treat it as a proposed theorem/preprint that must be proved, replayed, or killed.

Important danger: naive multiplication padding by a degree-120 polynomial is not enough by itself, because native explaining polynomials have degree `<137`, and `<137 + 120 = <257`, while the target code is degree `<256`. Role05 claims a two-ended parity-check/evaluator lemma avoids this. Settle that exact issue.

## qchal Discipline

Corrected Role07 says:

```text
attached-source MCA has no independent q_chal
sampled parameter field = q_line
direct scalar extension K -> E preserves bad-slope numerator but divides by |E|
proper scalar extension of the Cycle116 K-valued line kills the 2^-128 density
balanced challenge projection onto K preserves density only if the official contract explicitly defines that map
```

Therefore `q_chal` is not a free denominator. If you use `q_chal`, you must define:

```text
challenge_space
challenge_distribution
line_field
challenge_to_line_parameter_map
event pullback/filter
duplicate/quotient/charge treatment
```

## Required Output Format

Use this exact structure:

```text
LABEL:
one or more of PROOF / COUNTERPACKET / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / PLAN

EXECUTIVE VERDICT:
State whether the assigned target is proved, killed, conditionally repaired, or still open.

STANDALONE CERTIFICATE SECTION OR ROUTE CUT:
If proof: give a clean theorem statement with all hypotheses and exact constants.
If cut: name the exact false implication and give a minimal obstruction.

PROOF DETAILS:
Provide the full argument. Do not handwave degree bounds, field ledgers, noncontainment, or slope distinctness.

VERIFIER / CHECKER REQUIREMENTS:
Give deterministic checks or pseudo-code. State terminal strings.

FIELD AND PARAMETER LEDGER:
List q_gen, q_code, q_line, q_chal, n, k, agreement, radius, numerator, denominator.

SELF-AUDIT:
Answer the six questions from the addendum.

NEXT EXACT STEP:
One exact theorem/checker/counterpacket target.
```

Do not overclaim. If you prove a finite/source theorem but not an official prize theorem, say that literally.
