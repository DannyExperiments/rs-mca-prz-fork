# Cycle109 RS-MCA Stratified-Cover Checker

## Scope

This bundle is a proof-carrying finite stress harness for
`L-CYCLE109-INTERIOR-STRATIFIED-CHARGE-OR-DECORATED-COVER`.
It is not, by itself, a universal prize proof. The finite core recomputes the
official support-wise MCA bad-slope set exactly. The audit core then checks
field discipline, distinct-slope accounting, retained chart tags, same-field
injective normalizations, Gate-B rank escape, cap arithmetic, and the
`2^-128` numerator floor.

The code is standard-library Python. Field elements of `GF(p^e)` are encoded by
integers `0,...,p^e-1`, using base-`p` coefficients in the power basis defined
by the monic irreducible `line_modulus`, listed low coefficient first.

## Commands

```bash
python3 cycle109_checker.py enumerate instance.json --output truth.json
python3 cycle109_checker.py audit certificate.json --output report.json
```

Strict mode is the default. It refuses to trust a JSON boolean purporting to be
an external theorem-prover result. `--non-strict` is research-only and may be
used to exercise the state machine before a proof-kernel wrapper exists.

## Exact finite truth kernel

Let `s=k+sigma`. For each `s`-subset `S` of the evaluation domain, the checker
forms the `|S| x k` Vandermonde matrix `V_S` and a basis `H_S` of its left
nullspace. Put

```text
a_S = H_S f|S,    b_S = H_S g|S.
```

Then `S` supports a bad slope exactly when `b_S != 0` and there is a scalar
`z` with `a_S + z b_S = 0`; that scalar is unique. The checker computes it
from one nonzero coordinate and verifies every syndrome coordinate. It groups
all supports by the canonical field element `z`, so support collisions at the
same slope never increase `N_off`.

Enumerating only supports of size exactly `s` is exact for Reed--Solomon codes:
if a witness exists on a larger support and every `s`-subset simultaneously
explained both `f` and `g`, uniqueness from any fixed `k` points would glue the
local degree-`<k` explanations to explanations on the whole larger support,
contradicting badness.

## Certificate layers

1. **Source truth**
   - `EXHAUSTIVE_SOURCE`: recompute every bad slope from `(D,k,sigma,f,g)`.
   - `PROOF_CARRYING_SOURCE`: consume a separately checked completeness proof.

2. **Primary partition**
   Every distinct bad slope receives exactly one primary branch:

```text
ENDPOINT
QUOTIENT_PERIODIC
CONTAINED_DELETE_ONE
TANGENT
FIELD_CONFINEMENT
AFFINE_COLOR
HIDDEN_ACTION_RANK
INTERNAL_NORMALIZATION
LOW
BALANCED
HIGH
```

`SAME_SLOPE` is not a primary numerator branch. It is the alias relation among
support witnesses grouped under one canonical slope.

3. **Residual charts**
   Every LOW/BALANCED/HIGH slope references exactly one chart. A chart tag must
retain, at minimum:

```text
source_object_id
support_selector_id
normalization_id
field_embedding_id
```

Anchor, denominator gauge, and action-rank signatures should also be retained
when they affect the normalization. A support-dependent affine or Möbius map
without its tag is rejected.

4. **Normalization**
   The chart supplies a map on its assigned slopes. The checker requires
`K_line -> K_line`, exact domain equality, and pairwise injectivity.

5. **Gate B**
   For an exceptional layer evaluation matrix `A` and restriction-coefficient
matrix `R`, the checker verifies

```text
rank(A) < rank([A;R]).
```

For a one-parameter line/pencil this yields a nonzero univariate separator and
a degree cap. For a two-parameter affine plane it does **not** yield a finite
`n^C` slope cap by itself. HIGH charts therefore need one of:

- a certified curve constraint with no common component (`CURVE_BEZOUT`);
- two certified independent separators (`TWO_SEPARATOR_BEZOUT`);
- an exact finite image; or
- a separately proved symbolic bound.

A bare plane rank-escape receipt is rejected as `UNPAID_HIGH_PLANE`.

6. **AP_corr**
   Each uncharged chart carries a versioned, source-visible `AP_corr` receipt.
If source AP_corr is verified but rank escape fails and no official failure
charge is attached, the terminal label is `AP_DESCENT_FAILURE`.

The current bundle does not define the missing official repaired AP predicate.
It records and checks a proof receipt for it. The missing universal theorem is
precisely that the official source predicate implies one of the accepted chart
certificates or an official charge.

7. **Field ledger**

```text
q_gen  = size of the smallest subfield containing D
q_code = size of the code alphabet subfield
q_line = size of the actual slope field
q_chal = metadata unless a protocol-transfer proof is checked
```

The security denominator must be `q_line`. The exact target is

```text
N_cap <= floor(q_line / 2^128).
```

Field confinement may reduce a branch cap to a proper subfield size, but the
probability denominator remains `q_line`.

8. **Family promotion**
   `SOURCE_VALID_COUNTERPACKET` is emitted only after proof-kernel verification
of all five family receipts:

```text
official source construction for an unbounded family
unbounded parameter set
corrected-reserve hypotheses
all known charges paid or absent
growth/systematic-failure theorem
```

Without all five, finite data terminates as `MODEL_ONLY_STRESS_FAMILY`.

## Deterministic terminal precedence

```text
FIELD_LEDGER_MISMATCH
UNPAID_LOW_RESIDUAL
UNPAID_BALANCED_COVER
UNPAID_HIGH_PLANE
AP_DESCENT_FAILURE
SOURCE_VALID_COUNTERPACKET or MODEL_ONLY_STRESS_FAMILY
STRATIFIED_COVER_CERTIFIED
```

`INVALID_CERTIFICATE` and detailed structural violations are additional
engineering labels.

## Trusted boundary

The finite-field arithmetic, exact support enumeration, finite matrix ranks,
normalization injectivity, set unions, and integer ledger are checked by this
kernel. The following remain external proof obligations in strict mode:

- official branch semantics not reducible to the built-in finite checks;
- intrinsic denominator minimality for large instances;
- source `AP_corr` and its visibility;
- uniformity of a chart exponent independent of `k`, `sigma`, and degree;
- symbolic branch caps;
- source-valid asymptotic family promotion.

A production wrapper should invoke Lean, Coq, Isabelle, or another fixed proof
kernel on those receipts and pass only kernel-verified theorem hashes to this
state machine.
