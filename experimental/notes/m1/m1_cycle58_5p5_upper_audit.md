# Cycle 58 5.5 Pro Upper-Wall Audit

## Claim

The Cycle 58 nine-lane external run does **not** solve the Proximity Prize.
It substantially sharpens the upper-side MCA target.

The pure upper target

```text
bad slopes <= n^{1+o(1)}
```

is too strong in finite and low-reserve regimes. The corrected target is a
main-term-plus-inverse theorem in syndrome space:

```text
bad slopes
  <= n^{1+o(1)}
     + unavoidable occupancy/main term
     + explicit quotient/action-rank templates
     + tangent/common-envelope templates.
```

The most stable global wall remains:

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

but it must be stated with an occupancy term and a stronger quotient-template
classification.

## Status

AUDIT / EXPERIMENTAL, with several COUNTEREXAMPLE or ROUTE_CUT subresults to
overbroad targets.

Conservative banking:

- **BANKABLE_LEMMA:** exact syndrome transverse-secant reformulation is the
  right denominator-free object for scalar MCA.
- **ROUTE_CUT:** a balanced `t=sigma` theorem alone does not imply the full
  scalar MCA upper theorem.
- **COUNTEREXAMPLE:** the absolute `n^{1+o(1)}` target for `t=2` high-`j`
  split counts is false without an occupancy/main term.
- **COUNTEREXAMPLE:** literal quotient pullback exclusion `E=E_0(X^M)` is too
  narrow; quotient-action-rank templates must be included.
- **ROUTE_CUT:** high-denominator `t>sigma` data cannot be ignored by proving
  only a `t<=sigma` theorem.
- **CONDITIONAL:** the interleaved list problem reduces to a scalar/full-support
  syndrome-fiber theorem at the official scale, but that scalar theorem remains
  open.

## Parameters

The run concerns scalar Reed-Solomon MCA and list problems with:

```text
C = RS[F,L,k]
n = |L|
rho = k/n in {1/2, 1/4, 1/8, 1/16}
a = k + sigma
j = n - a = n-k-sigma
r = n-k
epsilon* = 2^-128
```

Ledgers remain separate:

```text
q_gen    generated field / entropy field
q_line   line or slope field
q_chal   verifier challenge field
B        base or generated field
F        ambient field
```

No external answer justifies using `q_line` or `q_chal` to pay a `q_gen`
entropy bill without an explicit transfer theorem.

## Existing paper dependency

Primary dependency: Paper B, especially the corrected-reserve MCA/residue-line
normal form and the all-denominator MCA maximum.

Relevant repo target: M1, corrected MCA / residue-line local limit.

Companion list target: L1/L2, actual scalar list or full-support syndrome-fiber
local limit, with interleaving treated by projection only after the scalar
theorem is proved.

## Proof idea or experiment

Nine lanes were run against the Cycle 58 handoff. Raw returns are preserved in:

```text
experimental/notes/m1/cycle58_5p5_raw/
```

### Lane summary

| Lane | Raw file | Returned status | Conservative bank |
| --- | --- | --- | --- |
| 01 Global syndrome inverse | `01_global_syndrome_inverse.md` | CONJECTURAL | exact syndrome correspondence; support-incidence interpretation cut; next wall is split-locator multi-minor ratio-image inverse |
| 02 Locator scroll circuit | `02_locator_scroll_circuit_inverse.md` | CONJECTURAL | resonant-circuit extraction and mixed Kronecker-scroll formulation; circuit-by-circuit classification cut |
| 03 `t=2` high-`j` quadric | `03_t2_high_j_quadric_split_count.md` | COUNTEREXAMPLE | pure `n^{1+o(1)}` split-count target false; occupancy term `binom(n,j)/Q` appears |
| 04 Quotient component | `04_quotient_component_counterpacket_hunter.md` | COUNTEREXAMPLE | literal pullback exclusion too narrow; quotient-action-rank `d_M(E)` required; full quotient profile may be necessary |
| 05 All-denominator audit | `05_all_denominator_mca_auditor.md` | AUDIT | balanced-only assembly incomplete; `t<sigma` residual-unsafe and `t>sigma` affine-plane branches remain |
| 06 Overbalanced compression | `06_overbalanced_thick_residue_compression.md` | COUNTEREXAMPLE | general high-denominator compression to `t'<=sigma` false; syndrome formulation absorbs high-denominator as a chart but not as a class of lines |
| 07 Scalar list local limit | `07_scalar_list_local_limit.md` | CONDITIONAL | interleaved projection reduction is strong; scalar full-support syndrome-fiber theorem remains open |
| 08 Finite threshold audit | `08_finite_prize_threshold_auditor.md` | AUDIT | no rate-only finite `delta_C^*`; exact threshold needs finite syndrome inverse and scalar list theorem |
| 09 Referee formalizer | `09_referee_formalizer.md` | AUDIT | lower branch and exact reductions banked; upper theorem still open; calibrated quotient-free envelope-free bound is next |

## Ledger impact

### MCA upper theorem

The target should be restated in syndrome space. Let `H_RS` be a parity-check
matrix and let

```text
V_T = span{H_RS(:,x) : x in T},     |T| = j.
```

For an affine syndrome line

```text
ell(z) = u + z v,
```

bad slopes are transverse incidences:

```text
ell(z) in V_T,    v notin V_T.
```

The live theorem is not a fixed-denominator residue-cloud theorem. It is a
denominator-free transverse secant inverse theorem for these incidences.

### Corrected main term

The `t=2` high-`j` lane indicates that an absolute `n^{1+o(1)}` count is false
before accounting for the baseline occupancy term. A calibrated same-field
bound should look like:

```text
bad slopes
  <= n^{1+o(1)}
     + O(binom(n,k+t) / Q^{t-1})
     + quotient/template contribution.
```

Equivalently, normalized MCA error includes an entropy term on the order of:

```text
binom(n,k+t) / Q^t.
```

Under strict asymptotic entropy margin with `t=Theta(n/log Q)`, this term may
be negligible, but finite and low-reserve statements must include it.

### Quotient ledger

The quotient-component lane says the old syntactic test

```text
E(X) = E_0(X^M)
```

is too narrow. The correct invariant is closer to:

```text
d_M(E) = deg minpoly([X^M] mod E).
```

Arbitrary-anchor all-line MCA may need the full quotient support profile

```text
2^{Q_H(eta)}
```

rather than the smaller canonical `beta(rho)/H_2(rho)` exponent, unless an
additional theorem restricts admissible quotient-component anchors.

### All-denominator ledger

The all-denominator lanes agree that:

- `t<sigma` requires an actual-list or residue-sliced list theorem; raw
  support-fiber counts are false.
- `t=sigma` is the balanced point-cloud stratum.
- `t>sigma` is a support-dependent affine-plane incidence in residue
  coordinates.
- Syndrome space is the only clean formulation that covers all three at once.

### List ledger

The interleaved challenge likely reduces to scalar/full-support syndrome fibers
at the official `2^-128` scale by linear projection, but the scalar theorem is
still open. The right list object is actual list size, full agreement supports,
or sparse syndrome fibers, not raw feasible support sets.

## Constants

No official finite `delta_C^*(2^-128)` value is banked.

Finite threshold audits require the exact target numerator:

```text
T = floor(q_line / 2^128).
```

For MCA, finite safety requires bounding transverse syndrome-line incidences by
`T`, after adding tangent, quotient/action-rank, residual-list, and occupancy
terms.

For same-field scalar MCA, the external answers suggest the finite upper should
track at least the additive surplus:

```text
sigma log_2 Q - log_2 binom(n,k+sigma),
```

and not merely the sign of the surplus.

## Reproducibility

Raw external outputs:

```text
experimental/notes/m1/cycle58_5p5_raw/
```

Checksums:

```text
experimental/notes/m1/cycle58_5p5_raw/SHA256SUMS.txt
```

The raw answers are evidence for this audit, not promoted theorem statements.

## Next exact wall

The next theorem should be stated as:

```text
W-MCA-CALIBRATED-SYNDROME-TRANSVERSE-SECANT-INVERSE
```

Prove, above generated-field entropy margin, finite surplus, and quotient
reserve, that every affine syndrome line satisfies

```text
|Bad_j(ell)|
  <= n^{1+o(1)}
     + occupancy_main_term
     + full quotient/action-rank templates
     + tangent/common-envelope templates.
```

The first attackable subcase is the quotient-free, envelope-free, same-field
bound:

```text
|Bad_j(ell)| <= n^{1+o(1)} + Q*lambda*n^{o(1)},
```

where the occupancy term is the one supplied by the calibrated Bessel/random
anchor baseline. A counterpacket would have to beat this calibrated bound at an
official rate while clearing entropy, quotient, and finite-surplus hypotheses.
