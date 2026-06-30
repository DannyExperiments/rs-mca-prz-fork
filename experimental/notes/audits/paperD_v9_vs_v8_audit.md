# Paper D v9 versus v8 audit

Date: 2026-06-30

Status: AUDIT / VERSION-PROMOTION

## Verdict

`tex/cs25_cap_v9.tex` is strictly better than `tex/cs25_cap_v8.tex` as a Paper
D package after preserving the v8 endpoint and `q>n` fixes.  It keeps the v8
universal field-size cap, first-grid cap, quotient-support ledger, and
quotient-image ledger, and adds a new aperiodic Hankel chart atlas for
safe-side MCA certificates.

This is not a new numerical leaderboard row and not a proof of the full M1
aperiodic local limit.  It is a proved certificate framework: if a contributor
supplies the listed minors, pivot eliminants, empty-chart certificates, or
dimension-degree fallbacks, the paper explains how to turn them into
bad-parameter bounds.

## What v9 adds

The new section `Aperiodic Hankel chart atlas` splits the remaining aperiodic
branch into concrete buckets:

- regular overdetermined Hankel minors;
- finite affine noncontainment pivot charts `B_h != 0`;
- the projective-infinity chart `B=0, A!=0`;
- finite-parameter curve coefficient pivots `(V_i)_h != 0`;
- a named singular residual bucket.

The regular bucket gives a direct root-containment certificate: for exact
agreement `A`, with `j=n-A` and `t=A-k`, if `t >= j+1` and a maximal minor
`Delta_A(Z)` is nonzero, then every finite bad slope with exact witness size
`A` is a root of `Delta_A`, hence contributes at most `deg Delta_A <= j+1`.

The affine and curve pivot theorems are certificate theorems: a nonzero
univariate eliminant in the saturated pivot ideal bounds the bad parameters in
that chart by its degree.  The projective theorem adds the single infinity
point as an explicit chart.  The dimension-degree fallback is safe but marked as
diagnostic rather than expected to settle a `2^-128` threshold.

## Integration notes

The companion schema `scripts/aperiodic_eliminant_schema.json` is useful for
agents because it fixes the expected fields for Hankel certificate packets:
row data, exact agreement levels, removed ledgers, regular minors, chart data,
pivot records, eliminants, fallback dimensions, and residual labels.

The schema was tightened during integration so each packet declares
`schema_version = "aperiodic-hankel-eliminant-v1"` and pivot records end as
`eliminant`, `empty`, `dimension_degree`, or `residual_obstruction`.  This
matches the v9 workflow and avoids hiding unresolved singular charts under a
generic failed status.

## Remaining work

The next useful PRs should provide actual certificate instances:

1. pick a row and exact agreement threshold;
2. remove tangent/common-code-line and quotient-image ledgers;
3. test regular minors when `t >= j+1`;
4. build affine/projective/curve pivot charts for singular buckets;
5. emit JSON conforming to `scripts/aperiodic_eliminant_schema.json`;
6. classify every residual obstruction as quotient, tangent, extension,
   candidate new obstruction, or unknown.

The missing theorem is still the construction of small eliminants, or a
classification of the singular residual buckets, for meaningful prize rows.
