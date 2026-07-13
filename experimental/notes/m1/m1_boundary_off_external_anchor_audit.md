# M1 Boundary-Off External-Anchor Audit

Date: 2026-06-29

Source PR: #131, AllenGrahamHart.

Status: PROVED-LOCAL / PROOF-PROGRAM / AUDIT.

## Claim Distilled

The PR isolates the one-outside `Boundary_off` residual in the M1 Hankel-pencil
program.  For a domain shadow `S subset D` of size `j-1` and an external anchor
`beta notin D`, the one-outside locator has the affine form

```text
ell_{S,beta} = ell_S^+ - beta ell_S^0.
```

Consequently the Hankel landing matrix

```text
M_S(beta) =
[ H(u) ell_{S,beta}   H(v) ell_{S,beta} ]
```

has columns affine-linear in `beta`, and the rank-one landing condition is
equivalent to quadratic minor equations in `beta`.

For fixed `S`, either one of these quadratic minors is nonzero, giving at most
two external anchors, or all minors vanish identically and the branch is a ruled
rank-one pencil.  In the `t=2` case this gives a three-scalar coefficient test
for the ruled branch.

## Integration Decision

The full PR was not merged wholesale.  It included a very large generated
draft, stale site/Paper D changes, and proof-program material that should not
be promoted as a solved M1 theorem.  The useful content is this local normal
form and the suggested exact primitive quotient-normal target.

The exact target proposed in the PR is:

```text
|Bad_nc(f,g,a)| <= M1QuotBudget(f,g,a) + n^B
```

after tangent, contained, quotient-periodic, presentation, reciprocal, and
finite-domain alias contributions have been charged.  This remains
CONJECTURAL / FALSIFICATION-FIRST.

## Use

This note is useful for the M1 residue-line local-limit program because it
turns the opaque one-outside boundary image into an explicit external-anchor
incidence problem.  It gives a route for future agents:

1. Prove polynomial bounds for the non-ruled external-anchor branch.
2. Classify the ruled branch without mixing it into quotient-periodic mass.
3. Keep the primitive quotient-normal target separate from exact quotient
   support budgets.

## Non-Claims

This note does not prove the all-line M1 polynomial packing theorem.  It does
not bound `|Boundary_off|`, does not give a leaderboard row, and does not change
any public MCA or interleaved-list threshold.
