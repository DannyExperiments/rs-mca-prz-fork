# Cycle106 9-Pro Wallbreaker Returns Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.

Date: 2026-06-22.

Raw return folder:
`experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/`.

## Executive Verdict

This round was significant, but it did not solve Cycle106 and did not prove a
prize-level statement.

The positive result is that several independent roles converged on the same
structural normal form for the active upper-side numerator. Cycle106 is no
longer just a vague "moment-curve incidence" wall. It has a concrete
complement-line/rank-one eliminant formulation.

The negative result is also important: the compact source packet does not yet
define the exact "aperiodic above corrected reserve" predicate strongly enough
to promote the structural reductions to a theorem. The source auditor also
identified an endpoint defect in the ordinary complement-duality line when
`sigma+1=n`; the corrected all-endpoint map must use `(1-X^n)A^{-1}` modulo
`X^(sigma+2)`.

Conservative conclusion:

```text
No PROOF.
No source-valid COUNTERPACKET.
Bank complement-line/rank-one reductions as BANKABLE_LEMMA.
Cut literal Zariski-closure and finite-stress-only routes as ROUTE_CUT.
Promote the missing source AP predicate and rank-escape theorem as EXACT_NEW_WALL.
```

## Exact Implications Banked

### 1. Complement-Line Eliminant Reduction

Let `d=sigma+1`, `m=n-s`, and write

```text
V(X)=Uhat(X)^(-1) mod X^(d+1)=sum_{j=0}^d v_j X^j,  v_0=1.
```

For the non-endpoint range where ordinary complement duality is valid, activity
is equivalent to the affine line meeting the `m`-subset elementary-symmetric
layer:

```text
theta active
<=> (v_j - theta*v_{j-1})_{j=1}^d in M_m.
```

For total-degree `D` polynomials in `d` variables, if a polynomial vanishes on
`M_m` but does not vanish identically on this affine line, then

```text
#{theta: line(theta) in M_m} <= D.
```

The finite checker
`03_cycle106_complement_line_eliminant_check.py` implements the exact rank
criterion:

```text
rank(A) < rank([A;B])
```

where `A` evaluates degree-`<=D` polynomials on `M_m` and `B` restricts them to
the complement line.

This is bankable as a reduction. The unproved theorem is:

```text
AP_corr(Uhat) => complement line escapes the low-degree closure of M_m.
```

### 2. Dephased Rank-One Locator-Jet Reduction

Using one active basepoint, Roles 07 and 09 reduce the remaining active values
to a rank-one determinant/readout problem on support changes `T`.

The bankable form is:

```text
Cycle105 activity + one active basepoint
<=> rank-one equations Delta_j(T)=0, with active value read from -b_1(T).
```

This gives an exact finite stress-checking object and strong local restrictions:

- distinct external readouts have a petal/support-distance lower bound;
- close collisions are classified;
- same-slope multiplicity does not inflate the distinct numerator;
- internal values contribute separately and do not by themselves create the
  dangerous external numerator.

This does not prove the central polynomial incidence bound. It gives the
right object to attack.

### 3. Boolean Fourier Shell Reformulation

Role 06 gives another exact reformulation. After passing to logarithmic moments,
activity becomes incidence between a shifted Boolean shell and a moment curve:

```text
theta active <=> P - v_d(theta) in P_s.
```

This correctly removes witness multiplicity and isolates the needed theorem as
an aperiodic Boolean-shell inverse bound. It is useful as a parallel language,
but the round did not prove that inverse theorem.

### 4. Pairwise External-Witness Separation

Roles 01, 02, 04, 07, and 09 all give versions of the same rigid fact: distinct
external active parameters force substantial support separation or a PTE/petal
trade. This is reliable local structure.

It is not enough by itself. Packing alone still leaves central regimes too
large, so it is a guardrail rather than a closure.

## What Was Not Proved

The round did not prove:

- `|Gamma cap M_s| <= n^{O(1)}` under the actual source hypotheses;
- that above-reserve aperiodicity implies complement-line rank escape;
- that every official bad slope normalizes into the `Uhat` object satisfying
  the stated aperiodicity predicate;
- a complete M1 numerator bound;
- a Proximity Prize theorem;
- a source-valid aperiodic counterpacket.

The first consequential failure line is:

```text
undefined "aperiodic above corrected reserve"
plus absent L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER.
```

The first mathematical failure line inside the preferred eliminant route is:

```text
AP_corr(Uhat) => R_{m,D}(U) != 0
```

or equivalently:

```text
AP_corr(Uhat) => the complement line is not contained in the bounded-degree
exceptional closure of M_m.
```

## Generated Files And Local Replay

Files preserved from the Pro returns:

- `03_cycle106_complement_line_eliminant_check.py`
- `07_cycle106_kfree_stress_checker.py`
- `07_cycle106_sample_p29_n7_s4_1.json`
- `07_cycle106_sample_p29_n7_s4_2.json`
- `07_cycle106_cycle102_replay_p29_1.json`
- `07_cycle106_candidate_p97_n16_s8_1.json`

Raw checksums:

```bash
cd experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw
shasum -a 256 -c SHA256SUMS.txt
```

Result: all raw response and downloaded files verified `OK`.

Safe local checks run:

```bash
python3 -m py_compile \
  experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/03_cycle106_complement_line_eliminant_check.py \
  experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/07_cycle106_kfree_stress_checker.py

python3 experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/03_cycle106_complement_line_eliminant_check.py \
  --p 29 --n 7 --sigma 3 --s 4 --uhat 1,10,15,7,0

python3 experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/07_cycle106_kfree_stress_checker.py \
  --mode all-u --p 29 --n 7 --sigma 3 --s 4 --side complement --alarm-external 2 --top 1

python3 experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/07_cycle106_kfree_stress_checker.py \
  --mode local-exchange --p 29 --n 7 --sigma 3 --s 4 \
  --base-theta 2 --base-support 3,4,5,6 --qmax 3 --alarm-external 2

python3 experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/07_cycle106_kfree_stress_checker.py \
  --mode local-exchange --p 97 --n 16 --sigma 2 --s 8 \
  --base-theta 13 --base-support 0,3,7,8,10,12,14,15 --qmax 8 --alarm-external 6
```

Local replay outputs are under:

```text
experimental/notes/m1/cycle106_wallbreaker_9pro_returns_raw/local_checks/
```

The two p29 stress outputs and the p97 candidate output reproduced the supplied
JSON certificates byte-for-byte. The p29 complement-line run returned:

```text
decision = LINE_ESCAPES_DEGREE_D_CLOSURE
active_theta_count = 1
```

The p97 finite candidate returned:

```text
decision = ROUTE_CUT_FINITE_MODEL_TOO_WEAK
prospective_decision_if_source_gate_were_verified = COUNTERPACKET_CANDIDATE
distinct_theta_count = 7
distinct_external_theta_count = 6
```

That p97 object is useful stress data. It is not a source-valid counterpacket,
because the checker explicitly states that the source aperiodicity/reserve gate
is unavailable.

## Role Ledger

| Role | Visible label | Conservative audit | Usefulness |
|---|---|---|---|
| 01 Proof Builder | BANKABLE_LEMMA | Banks pairwise external-support distance and a quasi-polynomial profile bound; does not prove the central inverse theorem. | Good guardrail. |
| 02 Counterpacket Hunter | AUDIT | No source-valid counterpacket; identifies locator-twist/quotient mechanisms and source-definition defect. | Useful falsifier/audit. |
| 03 Eliminant Route | BANKABLE_LEMMA | Best exact reduction: complement line plus rank/eliminant certificate. | Main route. |
| 04 Dephasing Distinct | BANKABLE_LEMMA | Dephased transversal and PTE/petal packing reduction; packing alone does not close. | Good secondary route. |
| 05 Symmetric Geometry | ROUTE_CUT | Cuts literal Zariski closure and relaxed-root geometry; points to bounded weighted-degree closure. | Important route cut. |
| 06 Fourier Cap | BANKABLE_LEMMA | Exact Boolean-shell/moment reformulation; leaves aperiodic shell inverse unproved. | Useful alternate language. |
| 07 Finite Stress | BANKABLE_LEMMA / ROUTE_CUT | Supplies checker and finite candidate, but checker itself refuses theorem promotion. | Good stress harness. |
| 08 Source Audit | AUDIT | Identifies missing AP predicate, endpoint complement defect, and missing official cover theorem. | Controls promotion. |
| 09 Referee | BANKABLE_LEMMA | Selects eliminant/rank-one route with mandatory source gate. | Good synthesis. |

## Field Ledger And Prize Status

The round did not use `q_gen`, `q_line`, `q_code`, `q_chal`, or the `2^-128`
target. That is correct for this local single-field M1 numerator wall. No
probability or protocol denominator conclusion is claimed.

This is official-prize-relevant only as a structural M1 upper-side reduction.
It is not an official prize certificate, because the path from official bad
slopes to the normalized `Uhat` aperiodic incidence object is still missing, and
other paper/frontier branches remain outside this round.

## Exact Next Wall

The next exact target should be split into two gates.

### Gate A: Source Cover

```text
L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER
```

Prove that every official residual bad slope either:

1. is already charged to a banked periodic/quotient/contained branch, or
2. normalizes to a `Uhat` satisfying the formal corrected-reserve aperiodicity
   predicate used by Cycle106.

This must also state the endpoint convention when `sigma+1=n`.

### Gate B: Complement-Line Rank Escape

```text
L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE
```

Given the formal `AP_corr(Uhat)` predicate, prove that for `D=n^C`:

```text
R_{m,D}(U) != 0
```

equivalently, the complement line

```text
theta -> (v_j - theta*v_{j-1})_{j=1}^d
```

is not contained in the bounded-degree exceptional closure of `M_m`.

Terminal outputs:

```text
PROOF:
  AP_corr(Uhat) => |Gamma cap M_s| <= n^C.

COUNTERPACKET:
  explicit AP_corr-valid Uhat family with superpolynomial many distinct active theta.

ROUTE_CUT:
  formal construction showing AP_corr still permits bounded-degree containment.
```

## Significance

This was a good round. It did not close the wall, but it made the wall sharper.
Before this round, Cycle106 could be attacked as several loosely related
incidence formulations. After this round, the live object is a precise
complement-line/rank-one escape problem plus a source-valid aperiodicity cover.

That is meaningful progress because it gives the next worker a falsifiable
target instead of another broad "prove an incidence bound" prompt.
