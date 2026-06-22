# Cycle111 Current State: LOW t=1 Occupancy Wall

Status before dispatch: EXACT_NEW_WALL / BANKABLE_LEMMA / ROUTE_CUT.

Cycle110 did not solve the LOW theorem and did not produce a source-valid
counterpacket. It did narrow the target. Intrinsic LOW slopes are a residue
image line intersection in `K_line[X]/(E)`. After fixing one witness, the LOW
slope set is an affine copy of a base correlated-agreement bad-slope set for
the rational direction `B/E`.

The old broad prompt "prove LOW calibrated occupancy" is now too vague. The
first charge-irreducible obstruction is the `t=1` stratum:

```text
L-CYCLE111-LOW-T1-OCCUPANCY-UPPER.
For E = X - beta, beta notin D, and any word w:D -> K_line,
bound the number of distinct evaluation colors
  { Q(beta) : deg Q <= k, agr_D(Q,w) >= k+sigma }
by C * binom(n,k+sigma) / q_gen^(sigma-1),
with q_line/q_gen transfer and corrected-reserve ledger receipts explicit.
```

Equivalent support/product formulation:

```text
For the monic-anchor family w = M|_D, bound the image size of
  S -> prod_{x in S}(beta-x)
on every elementary-symmetric prefix fiber
  e_j(S) = c_j, 1 <= j <= sigma-1,
by C * binom(n,k+sigma) / q_gen^(sigma-1).
```

If `L-CYCLE111-LOW-T1-OCCUPANCY-UPPER` is false, the desired counterpacket is:

```text
SOURCE_VALID_LOW_T1_COUNTERPACKET:
  prize-strength corrected reserve,
  source AP_corr true,
  t=1 intrinsic LOW,
  endpoint/field/affine-color/tangent/contained charges absent or paid,
  quotient/action-rank vacuous,
  distinct K_line slopes exceed the calibrated occupancy budget.
```

If the `t=1` theorem is proved, the next wall is:

```text
L-CYCLE111-LOW-COLLINEARITY-NONDEGENERACY-OR-CHARGE.
Residue-line concentration in K_line[X]/(E) costs the expected t-1 dimensions
unless the datum charges to quotient/periodic, field-confinement,
affine-color, tangent, hidden-action-rank, or retained normalization.
```

Important guardrails:

1. No prize proof is currently banked.
2. No source-valid counterpacket is currently banked.
3. `q_gen`, `q_line`, `q_code`, and `q_chal` are typed ledgers. Do not pay a
   generated-field entropy term with a line-field or challenge-field
   denominator without an explicit transfer theorem.
4. `q_chal` is not a free denominator for this wall.
5. A pure polynomial cap such as `|Z_t| <= n^C` is miscalibrated unless the
   corrected-reserve main term is explicitly paid.
6. Shifted-list, Johnson, sunflower, distance-only, and support-packing routes
   are cut in the super-Johnson/prize band unless they introduce a new
   table-specific or source-valid mechanism.
7. A finite/model certificate is useful but not enough unless it is lifted to
   the official source predicate and q-ledger.

Files to read first:

- `context/RS_MCA_CANONICAL_TRACKER.md`
- `context/m1_cycle110_low_calibrated_occupancy_returns_audit.md`
- `context/cycle110_returns_raw/role01_full_low_prover_response.md`
- `context/cycle110_returns_raw/role03_occupied_color_inverse_response.md`
- `context/cycle110_returns_raw/role07_qledger_low_budget_response.md`
- `context/cycle110_returns_raw/role09_ruthless_referee_synthesis_response.md`

