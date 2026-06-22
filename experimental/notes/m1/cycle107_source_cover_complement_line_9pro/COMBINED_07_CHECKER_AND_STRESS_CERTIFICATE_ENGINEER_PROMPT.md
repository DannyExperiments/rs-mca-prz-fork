# Combined Prompt: ROLE_07_CHECKER_AND_STRESS_CERTIFICATE_ENGINEER

## Common Prompt


Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, give the exact next lemma,
construction, checker, or counterpacket mechanism.

You are working inside the RS-MCA / Proximity Prize M1 upper-side route. Read
the uploaded context first, especially:

```text
context/CURRENT_CYCLE107_STATE.md
context/rs_mca_board_findings_for_codex_director_20260622.md
context/RS_MCA_CANONICAL_TRACKER.md
context/m1_cycle106_wallbreaker_9pro_returns_audit.md
context/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md
context/m1_cycle104_bandwidth_k_divisor_incidence_audit.md
context/m1_cycle103_e1_image_flat_variety_audit.md
context/cycle106_family_signature_analysis.md
context/scripts/
context/certificates/
context/auxiliary_tracks/
```

## Current Board State

The previous Cycle106 9-Pro round was significant, but it was not a proof and
not a source-valid counterpacket. Bank only:

```text
BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT
```

The strongest banked normal form is:

```text
d = sigma+1
V(X)=Uhat(X)^(-1) mod X^(d+1)=sum_{j=0}^d v_j X^j

theta active
<=> (v_j - theta*v_{j-1})_{j=1}^d in M_m
```

in the non-endpoint complement-duality range, with endpoint correction noted in
the Cycle106 audit.

The live problem is no longer vague moment-curve incidence. It is the two-gate
wall:

```text
Gate A:
L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER

Gate B:
L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE
```

Gate A must prove that the official M1 bad-slope / above-corrected-reserve
object really gives a source-valid `AP_corr(Uhat)` complement-line instance
whose active theta values count the official numerator.

Gate B must prove that `AP_corr(Uhat)` forces complement-line escape from the
bounded-degree exceptional closure of `M_m`. Equivalently, produce a
bounded-degree eliminant/subresultant/Wronskian `R_{m,D}(Uhat)` with:

```text
AP_corr(Uhat) => R_{m,D}(Uhat) != 0
```

so that:

```text
#{theta : L_U(theta) in M_m} <= D
```

with `D = n^{O(1)}` independent of `s` and `k`.

## Hard Constraints

- Do not claim Cycle106 was solved.
- Do not treat p97 finite stress as a source-valid counterpacket.
- Do not use raw D8B density as source-valid evidence.
- Do not revive q=3 D8; it is cut.
- Do not use generic Zariski closure without proving source escape.
- Do not replace distinct external theta values by witness multiplicity.
- Do not count periodic, quotient, coset-swap, contained-incidence, same-slope,
  or affine-normalization mass unless the numerator effect is charged exactly.
- Do not invoke q-ledger or `2^-128` frontier arithmetic unless your role is
  explicitly auditing official transfer. If used, identify `q_gen`, `q_line`,
  `q_code`, `q_chal`, and explain which one controls the statement.
- Do not claim a prize-level result unless every link from this wall to the
  official Proximity Prize statement is explicitly verified.

## Required Output Label

Begin with exactly one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Definitions:

`PROOF`: Gate A and Gate B proved under source-valid hypotheses.

`COUNTERPACKET`: a source-valid family satisfying the official/AP_corr
hypotheses with super-polynomially many distinct external active theta values.

`BANKABLE_LEMMA`: a strict proved reduction to a smaller named theorem/checker.

`ROUTE_CUT`: a rigorous reason the proposed route cannot prove the target, plus
the corrected replacement target.

`EXACT_NEW_WALL`: a strictly smaller exact theorem/checker with input/output
conditions.

`AUDIT`: a conservative source or logic audit identifying the first unsupported
implication.

`PLAN`: only if no proof/counterpacket/reduction is achieved.



## Self-Audit Addendum


Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/research
   certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would
   convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.



## Role Prompt


Your job is to produce an executable route.

Use the provided scripts and certificates as starting points:

```text
context/scripts/03_cycle106_complement_line_eliminant_check.py
context/scripts/07_cycle106_kfree_stress_checker.py
context/scripts/cycle106_kfree_incidence_stress.py
context/scripts/cycle106_family_signature_miner.py
context/scripts/cycle106_density_sensitivity_from_signatures.py
context/certificates/
```

Do not install dependencies. Prefer standard-library Python or self-contained
C++/Python.

Build one of:

1. A Gate A checker that validates source-cover normalization into `AP_corr`.
2. A Gate B checker that emits/validates `R_{m,D}(Uhat) != 0`.
3. A counterpacket verifier for a source-valid family.
4. A finite stress generator that explicitly reports why its output is not
   source-valid.

Required terminal decisions:

```text
SOURCE_COVER_VERIFIED
COMPLEMENT_LINE_ESCAPE_CERTIFIED
SOURCE_VALID_COUNTERPACKET_FOUND
FINITE_STRESS_ONLY_NO_CLAIM
RESOURCE_EXHAUSTED_NO_CLAIM
```

If you provide code, include exact invocation and expected output fields.

Return `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `AUDIT`,
or `PLAN`.
