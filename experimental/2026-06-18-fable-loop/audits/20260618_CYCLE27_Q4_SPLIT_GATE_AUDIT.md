# Cycle 27 Q4 Split-Gate Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is source-audited against the previously banked Cycle 15/16/20/25
objects.

Source artifacts:

- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RAW.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RUN_RESULT.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`: generated/base field size for this toy calculation.
- `B = F_p`.
- `F = F_{p^2}`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, `j = n-a = r-t = 3`.
- Branch: off `R0`, `kappa = u wedge b != 0`, source-valid denominator
  `E=X^2+cX+d` separated and nonzero on `F_p`, with `c_b != 0`.

This is a residue-line / bad-slope incidence calculation only. It is not a
list-decoding, CA, MCA, line-decoding, curve-MCA, protocol, `q_gen`, or SNARK
claim.

## What Cycle 27 Claims

Cycle 27 independently attacks the `Q==0` obstruction left by Cycle 26. It
works with the Cycle 25 six-term Plucker/Laplace expansion for the determinant
consistency polynomial `Q(z_0,z_1)` and extracts the degree-4 part.

The bankable candidate is the corrected top coefficient

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

Equivalently, writing `c=c_0+alpha c_1`, `d=d_0+alpha d_1`,

```text
Q_4 = N(c_b) * (c_1^2 d_0 - c_0 c_1 d_1 + d_1^2).
```

The recovered answer also explains why the apparent `P`-dependence in the
Cycle 26 displayed formula cancels: the `P`-part of `q2` is along the same
rank-one direction `eta` as `q1`. In source-compatible notation this uses the
previously banked forms

```text
q1 = c_b eta,
q2 = lambda_0^(0) + P eta,
lambda_0^(0) = c d + d tau_1,
eta = (c^2-d) + c tau_1 + tau_2.
```

This is consistent with the Cycle 20 audit, which banked the same structural
forms up to the local scalar conventions.

## Banked Narrow Lemma

Under the restricted ledger above, subject to independent confirmation of the
Cycle 20/Cycle 25 column conventions, the degree-4 coefficient of `Q` is
controlled by the locator norm:

```text
if c notin B:
  Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

Therefore

```text
Q_4 = 0
iff E has a root in F_p
iff prod_{a in F_p} E(a) = 0.
```

The last product is the same locator norm `N(ell)` banked in Cycle 24.
Source-valid residue-line denominators are nonzero on `F_p`, so this branch
forces `Q_4 != 0`.

On the residual `c in B` branch, Cycle 27 gives

```text
Q_4 = N(c_b) * Im(d)^2.
```

Separatedness excludes `d in B` in that branch, so `Im(d) != 0` and again
`Q_4 != 0`.

Thus, in the restricted source-valid separated off-`R0` `t=2,j=3` window,

```text
Q_4 != 0
=> Q is not identically zero
=> affine-consistent slopes are O(p)
```

by the Cycle 16 safe side.

The distinct split-cubic gate is separate but only shrinks the affine-consistent
set, so it does not enlarge the `O(p)` upper bound once `Q` is nonzero.

## Why This Matters

This appears to cut the last live `Q==0` branch in the restricted
`D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3` toy window. If Cycle 28
confirms the derivation directly from the column definitions, the restricted
branch should be promotable from `BANKABLE_LEMMA / AUDIT` to a local proof of
`C2=O(p)` in this window.

This is still sub-reserve (`eta=2/n`) and local. It does not solve the
Proximity Prize and does not prove Paper B/C positive MCA statements.

## Rejected Overclaims

- Do not promote the recovered answer's internal "PROOF" wording yet. The
  harness produced no clean `response.md`, and the `q2`/`Q_4` derivation still
  deserves an independent source audit.
- Do not cite this as a corrected-reserve theorem.
- Do not merge `q_gen` and `q_line`.
- Do not use this as a protocol, list-decoding, CA, MCA, line-decoding,
  curve-MCA, or SNARK ledger result.
- Do not forget the distinct split-cubic gate when translating from affine
  `tau in B^3` consistency to actual line-incidence.

## Next Exact Wall

`W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT`: independently rederive `Q_4` from the Cycle
15/16/20/25 source objects, verify the cancellation and nonvanishing, and
decide whether this restricted `t=2,j=3` branch can be promoted to `PROOF`.

If confirmed, the next mathematical wall is likely:

```text
W-F1-AA-RES-T2-HIGHER-J-LOCATOR-NORM
```

namely whether the top slope-consistency symbol for general `t=2`, higher `j`
is a nonzero scalar times a power of the same locator norm
`prod_{a in F_p}E(a)`.
