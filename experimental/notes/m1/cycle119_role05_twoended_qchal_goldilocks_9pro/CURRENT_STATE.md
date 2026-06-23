# Cycle119 Current State: Role05 Two-Ended Upgrade / qchal Sampler / Goldilocks Fallback

Date: 2026-06-23

## Director Verdict Before This Round

Cycle116 is banked as a finite, source-scoped support-wise RS-MCA / `LD_sw`
theorem:

```text
C = RS[F_17^32,H,256], |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128
```

Do not call that an official Proximity Prize solve. It is not ordinary
fixed-word list decoding, not protocol soundness, not asymptotic, and not an
accepted prime-field theorem.

Cycle118 was significant but not terminal. It likely removed the strict-ball
mathematical objection at the finite/source level, but the official
row/event/challenge contract is still missing.

## Central Candidate To Attack

Role05 from Cycle118 claims:

```text
L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

The claimed mechanism is a two-ended locator functional:

```text
common top six locator coefficients
+ common nonzero constant coefficient P_T(0) = -1
```

then move one odd-coset point from fixed co-support padding to common agreement:

```text
A* = {theta eta^i : 0 <= i <= 119}, |A*|=120
R* = {theta eta^i : 120 <= i <= 255}, |R*|=136
J_T* = J_T union R*, |J_T*|=249
agreement = 512 - 249 = 263
```

The proof must not use naive multiplication padding unless it resolves the
degree issue. Since a native explaining polynomial has degree `<137`, multiplying
by a degree-120 vanishing polynomial naively gives degree `<257`, not `<256`.
Role05 instead claims a two-ended parity-check/evaluator lemma that avoids this
loss. That exact lemma is the live target.

## What We Need The Four Role05 Attackers To Say

A successful proof answer should return all of:

```text
LABEL: PROOF / BANKABLE_LEMMA
Theorem statement for the two-ended fixed-jet locator-to-LD_sw lemma
Proof that the common top sigma-1 coefficients plus common constant coefficient
  produce one global evaluator functional ell
Proof that y0 + z_J y1 lies in W_J for z_J = -1/P_J(beta)
Construction of one common affine line f+zg
Construction of explaining codewords and supports of size 263
Uniform noncontainment proof by Vandermonde independence
Cycle84 verification of P_T(0) = -1 and P_T*(beta) scalar Phi(T)
Proof that distinct slope count remains 52,747,567,092
Exact strict-ball interpretation: distance < 250 iff agreement >=263
Checker spec or pseudo-code with terminal CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

A successful kill answer should return:

```text
LABEL: ROUTE_CUT / COUNTERPACKET
The exact first false line in Role05
A minimal counterexample or symbolic obstruction
Whether failure is in the two-ended linear functional, constant coefficient,
  augmented locator value, noncontainment, degree/k ledger, or full-N retention
The strongest repaired theorem that remains true
```

## qchal / Sampler State

Corrected Cycle118 Role07 closed the qchal field-thickening branch as a dichotomy:

```text
attached-source MCA has no independent q_chal
sampled parameter field = q_line
direct scalar extension K -> E preserves bad-slope numerator but divides by |E|
proper scalar extension of the Cycle116 K-valued line kills the 2^-128 density
balanced challenge projection onto K preserves density, but only if official
  contract explicitly defines that sampler map
```

So `q_chal` is not a free denominator. The next semantic target is:

```text
V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT
```

with terminal decisions:

```text
DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
BALANCED_CHALLENGE_PROJECTION_NO_LOSS
IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

## Goldilocks Fallback State

Cycle118 Role08 claims a prime-field fallback over:

```text
q = 2^64 - 2^32 + 1
LD_sw(C,264) >= 73,674,899,375,228,060
```

Local arithmetic spot checks passed:

```text
theta^256 = -1
theta^512 = 1
251*L(q) - q > 0
```

This is not banked until a deterministic checker proves the construction and
the official contract accepts the row. It is the fallback if `F_17^32` extension
rows are rejected.

## Do Not Claim

```text
official Proximity Prize solve
ordinary fixed-word list decoding
q_chal = q_line as an official protocol claim
lossless direct scalar field thickening
Role05 full-N agreement-263 theorem as banked before replay
Goldilocks theorem as accepted before checker and official row decision
```

## Best Current Route

```text
1. Prove or kill Role05: V-CYCLE118-TWO-ENDED-263-TRANSFER-CHECKER
2. Pin qchal sampler map: V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT
3. If extension fields rejected, replay Goldilocks:
   V-CYCLE119-GOLDILOCKS-FIXED-JET-COMPILER-CHECKER
```
