# Cycle 42 External 5.5 Pro Good-Reduction / Density Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

External-model claim status: four returned 5.5 Pro answers independently claim
that the two active restricted `t=2,j=4` walls close. Codex preserves and banks
the result conservatively: the false-negative diagnosis is strong and route
actionable; the full restricted density theorem is recorded as a bankable
external machine certificate pending local SymPy/Sage reproduction or PRZ
review.

## Source Artifacts

Raw external answers:

- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_A.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_B.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_C.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_D.md`

Returned output files:

- `raw/cycle42_external_5p5_pro/cycle42_goodred_density_checker.py`
- `raw/cycle42_external_5p5_pro/cycle42_goodred_density_certificate.json`
- `raw/cycle42_external_5p5_pro/cycle42_exact_resultants.json`
- `raw/cycle42_external_5p5_pro/cycle42_bad_prime_sets.json`
- `raw/cycle42_external_5p5_pro/cycle42_corrected_char0_goodred_checker_result.json`
- `raw/cycle42_external_5p5_pro/cycle42_corrected_char0_density_certificate.md`
- `raw/cycle42_external_5p5_pro/cycle42_t2j4_goodred_checker.py`
- `raw/cycle42_external_5p5_pro/cycle42_t2j4_goodred_checker_result.json`

Codex local copies / execution logs:

- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_goodred_density_checker_external.py`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_external.py`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_localrun.py`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_goodred_density_checker_localrun_stderr.txt`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_localrun_stderr.txt`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`, with `alpha^2 = -1`.
- `q_line = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`.
- Restricted regime: `t = sigma = 2`, `j = 4`, `k = p-6`,
  agreement `a = p-4`.

This remains a restricted local extension-line / surface branch. It is not a
corrected-reserve result, fixed-rate result, final generated-field theorem,
smooth multiplicative-domain theorem, CA/list/line-decoding/curve-MCA theorem,
protocol statement, SNARK statement, Proximity Prize solution, or final
`COUNTERPACKET`.

## Consensus Across External Answers

The four answers agree on the following points.

1. The two Cycle 41 type repairs were correct:
   - `ell=i` must be represented as `(i,0)` in `K[X]/E`;
   - after flattening into rational real/imaginary equations, scalar entries
     can be embedded as Gaussian scalars `(r,0)` for determinant code.

2. The patched Cycle 41 checker used an overstrong good-reduction criterion.
   It treated the affine Cramer determinant and `Delta^6 disc(L)` as an
   intrinsic reduced branch divisor. That is only a sufficient simple-branch
   chart test. It is not necessary for tame/projective good reduction.

3. The A-side failures of `G2` and `G3` are false negatives. They are caused by
   unsaturated Cramer/common-factor/projective-infinity behavior, not by a
   source-valid Subcase A route cut.

4. Subcase A admits a corrected good-reduction certificate at `p=7`; depending
   on the answer, either the original diagonal line works after primitive
   projective normalization, or the horizontal line `z_1=0` gives a simpler
   simple-branch certificate.

5. Subcase B admits a corrected/source-valid good-reduction certificate at
   `p=19` or `p=31`.

6. The fixed restricted `t=2,j=4` branch should have split-slope density
   `p^2/24 + O(p^{3/2})`, equivalently
   `q_line/24 + O(q_line^{3/4})`, outside an explicit finite bad-prime set.

## Machine Certificate Highlights

From `cycle42_goodred_density_certificate.json`:

- A horizontal line `z_1=0`, `p0=7`:
  - `PASS_simple_gate=true`;
  - `PASS_S4_types=true`;
  - finite histogram `{"13":4, "4":2, "112":1}`.
- B diagonal line `z_1=z_0`, `p0=19`:
  - `PASS_simple_gate=true`;
  - `PASS_S4_types=true`;
  - finite histogram
    `{"1111":1, "112":3, "13":4, "22":5, "4":4}`.
- A diagonal generalized/projective certificate:
  - `PASS_generalized_good_reduction_p7=true`.

From `cycle42_corrected_char0_goodred_checker_result.json`:

- `A.corrected_good_reduction_p7=true`.
- `A.finite_hist_p7.S4_hist_gate=true`.
- `A.independent_char0_S4_specialization.S4_certificate=true`.
- `B.corrected_good_reduction_p19=true`.
- `B.finite_hist_p19.S4_hist_gate=true`.
- `B.independent_char0_S4_specialization.S4_certificate=true`.
- Conclusion field: the Cycle 41 gate is
  `wrong/overstrong: raw Delta and Delta^6*disc(L) are not the reduced branch divisor`.

From `cycle42_t2j4_goodred_checker_result.json`:

- `all_checks_pass=true`.
- `A_same_line_corrected_good=true`.
- `A_good=true`.
- `B_same_line_good=true`.
- `B_good=true`.
- `A_raw_checker_false_negative_factor=true`.
- Clean-line A histogram is `{"112":1, "13":4, "4":2}`.
- Clean-line B histogram is `{"1111":1, "112":2, "13":3, "22":2, "4":3}`.

From `cycle42_bad_prime_sets.json`:

- Conservative A rational-prime support:
  `{2,3,5,11,13,23,29,109,353,6133,6299,51899,58758059,
  134773673,4141312303,65954521205827,
  185013443251818763385500528775698067}`.
- Conservative B rational-prime support:
  `{2,3,5,11,29,41,2063,234007,287341,1149593,4711367,
  429182827,986904239,20558103118321,6003144422654343011,
  87979847046285199339509999686219951947}`.

The finite bad-prime sets are sufficient supports, not asserted minimal.

## Codex Local Reproduction Status

Security/source inspection:

- The two Python checkers import `sympy` and standard-library modules only.
- No network, subprocess, shell, credential, browser, wallet, or package-manager
  behavior was found.
- The scripts syntax-check under `python3 -m py_compile`.

Execution status:

- Local execution is blocked because neither system Python nor bundled Codex
  Python has `sympy` installed.
- No dependency was fetched or installed.
- The failed local execution logs are preserved in the local-check directory.

Therefore Codex did not independently recompute the large symbolic resultants
locally in this turn. The result is banked as an external-machine certificate
with strong cross-answer agreement, not as a locally re-executed proof.

## Bankable Lemmas

### 1. Cycle 41 Good-Reduction Gate Was Sufficient, Not Necessary

The Cycle 41 `(G1,G2,G3)` gate is a sufficient criterion for a simple-branch
affine Cramer presentation. It is not a necessary criterion for tame
projective good reduction.

Consequently, the implication

```text
A fails G2/G3 on the raw affine/Cramer data
=> A cannot globalize
```

is invalid.

### 2. Restricted A/B Characteristic-Zero S4 Certificates

External certificates give:

- Subcase A has corrected good reduction and geometric `S_4` at `p=7`.
- Subcase B has corrected good reduction and geometric `S_4` at `p=19`
  or `p=31`.

This closes the Cycle 41 A-side obstruction at the level of the fixed
`t=2,j=4` branch, pending local symbolic rerun or PRZ review of the attached
certificate code.

### 3. Restricted Split-Slope Density

For relevant primes outside the finite bad-prime support, the restricted
surface has split-slope count

```text
N_split(p) = p^2/24 + O(p^(3/2))
           = q_line/24 + O(q_line^(3/4)).
```

This is a restricted local density theorem for the fixed branch. It does not
solve the corrected-reserve problem because here `sigma=2`, `rho=(p-6)/p -> 1`,
and `q_gen=p` remains distinct from `q_line=p^2`.

## Route Cuts

Cut:

```text
W-F1-AA-RES-T2J4-A2B-S4-SUBCASEA-GOODRED-OBSTRUCTION
as a claim that Subcase A cannot globalize.
```

More precisely, the following routes are false:

1. `Subcase A cannot globalize`.
2. `Failure of G2/G3 on z_1=z_0 proves a non-etale obstruction`.
3. `The raw Cycle 41 discriminant numerator is intrinsic`.
4. `Every good-reduction certificate must have a squarefree affine quartic
   discriminant`.

Not cut: the Subcase A branch itself.

## Not Banked

Do not promote this to:

- a corrected-reserve `COUNTERPACKET`;
- a fixed-rate counterpacket;
- a generated-field theorem with `q_gen=q_line`;
- a smooth multiplicative-domain result;
- a CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize
  statement.

Do not treat the external result files as locally recomputed by Codex until
`sympy`/Sage reproduction has actually run.

## Exact New Wall

The current fixed `t=2,j=4` monodromy/good-reduction branch is, subject to
review, effectively closed. The next wall is no longer another quartic
good-prime search.

Canonical next wall:

```text
W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT
```

Equivalent names proposed by the external answers:

- `W-F1-AA-RES-T2J4-TO-CORRECTED-RESERVE-SLOPE-PRESERVING-LIFT`
- `W-F1-AA-RES-RESERVE-SCALED-GENERATED-FIELD-QUARTIC-CORE-LIFT`

Useful theorem-sized formulation:

For fixed `rho in (0,1)`, construct or rule out source-valid data with

```text
k_n = rho n + O(1),
t_n = sigma_n >= C n/log n,
j_n = n-k_n-t_n = Theta(n),
```

with separated, nonvanishing, quotient-aperiodic denominator data and a
structured co-support/reserve lift that preserves a positive proportion
`c q_line` of noncontained split slopes. Equivalently, prove a reserve-scale
small-monodromy/structure dichotomy showing that any above-reserve aperiodic
incidence cover with enough completely split fibers must be tangent, contained,
or quotient-periodic.

This is the next high-value target after discussion.
