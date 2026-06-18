# Cycle 32 T2J4 Quartic Monodromy Base-Field Audit

Status: ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is audited conservatively.

Source artifacts:

- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RAW.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RUN_RESULT.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Branch: off `R0`, source-valid separated quadratic `E=X^2+cX+d`
  nonzero on `F_p`, with `c_b != 0` when that branch is used.

This is only a residue-line / bad-slope incidence calculation. It is not a
corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Route Cut

Cycle 32 correctly cuts the one-variable framing of the Cycle 31 wall.

The family should not be modeled as a one-variable function field over
`B(z)` or `F(z)`. Write

```text
z = z_0 + alpha z_1,       z_0,z_1 in B.
```

Multiplication by `z` on `A=F[X]/E` is `B`-linear:

```text
m_z = z_0 I_4 + z_1 A_alpha.
```

Thus the Cycle 29 columns

```text
C_i(z) = P_i - m_z(R_i)
```

are affine-linear in the two `B`-coordinates `(z_0,z_1)`. The square matrix
`M(z)` has entries of degree at most one in `(z_0,z_1)`, so

```text
Delta(z_0,z_1) = det_B M(z)
```

is a plane curve of degree at most four. Off this curve,

```text
tau_i(z) = det_B M_i(z) / Delta(z)
```

is a rational map from the affine `B`-surface `A^2_B` to the space of monic
quartics. The relevant split count is therefore a two-dimensional `B`-surface
count of `F_p`-points, not a one-variable Chebotarev count.

## Banked Reduction

The next invariant remains quartic monodromy, but with corrected base:

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4-A2B
```

For

```text
L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
```

the standard cubic resolvent is

```text
R(y) =
  y^3 - tau_2 y^2
      + (tau_1 tau_3 - 4 tau_4)y
      - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2).
```

Substituting `tau_i=det_B M_i/Delta` gives rational functions on `A^2_B`;
after clearing denominators, the discriminant numerator has degree at most 24
in `(z_0,z_1)`. The unproved geometric target is:

```text
G_geom(L_tau / \bar B(z_0,z_1)) = S_4
```

or at least a transitive arithmetic/geometric monodromy group whose identity
class is realized with positive density.

## Local Checker

Codex added
`local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`, implementing the
Cycle 29/30 affine equation

```text
(u - z b) * [L_tau]_E - ell * [Q_tau]_E = 0 in A.
```

For every `z in F_{p^2}` it solves the resulting `4x4` `B`-linear system for
`tau`, forms `L_tau`, and records the factorization type over `B=F_p`. It also
compares the `1111` count to the older direct support enumeration.

Representative certificate lines:

```text
p=11 solved_z=110 singular_z=11 hist_C2=3 direct_C2=3 singular_split_C2=0 match=True
p=13 solved_z=156 singular_z=13 hist_C2=3 direct_C2=3 singular_split_C2=0 match=True
p=17 solved_z=269 singular_z=20 hist_C2=8 direct_C2=8 singular_split_C2=0 match=True
p=19 seed=0 hist_C2=13 direct_C2=14 singular_split_C2=1 match=False
p=29 seed=0 hist_C2=33 direct_C2=34 singular_split_C2=1 match=False
```

The Cramer-system histogram agrees with direct support enumeration away from
the determinant curve. The small mismatches are explicitly recorded as
`singular_split_C2`; these are boundary contributions on `Delta=0` and remain
experimental.

## Audit Judgment

What is bankable:

1. The base model is `A^2_B` with coordinates `(z_0,z_1)`, not `B(z)` or
   `F(z)`.
2. The Cycle 29/30 Cramer system can be implemented directly and reproduces
   the direct split-slope count off the singular determinant curve.
3. The next proof target is now a surface monodromy/singular-bound theorem,
   not another scan interpretation.

What is not bankable:

- No proof of `G=S_4`.
- No proof of arithmetic monodromy equals geometric monodromy.
- No proof of a Chebotarev/Lang-Weil density constant.
- No proof that `C2=Theta(q_line)`.
- No source-valid counterpacket.
- No proof that the determinant-curve contribution is always `O(p)`.

## Next Exact Wall

```text
W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE
```

Prove or refute the following restricted local statement:

1. The singular determinant curve `Delta(z_0,z_1)=0` contributes only `O(p)`
   split slopes.
2. Off that curve, the quartic family over `A^2_B` has arithmetic/geometric
   monodromy whose identity Frobenius class occurs with positive density.
3. If the group is `S_4`, then the main term should be `p^2/24` up to the
   correct surface error term; if it is a smaller transitive group, record the
   corresponding density.

The immediate practical target is to turn the local histogram checker into a
certificate for either `S_4`, a smaller transitive group, or a constant-field
obstruction.

## Rejected Overclaims

- Do not cite Cycle 32 as a proof of `Theta(q_line)`.
- Do not cite the local checker as a proof of monodromy.
- Do not merge `q_gen=p` and `q_line=p^2`.
- Do not promote this local sub-reserve `t=2,j=4` audit into corrected-reserve,
  MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize
  status.
