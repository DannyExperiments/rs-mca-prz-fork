# COMMON PROMPT FOR CYCLE 60 FIND-THE-THEOREM INSTANCES

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

You are working on the RS-MCA / Proximity Prize problem for Reed-Solomon codes.
Read the attached context carefully, especially the Cycle 58 and Cycle 59
audits and raw returns if available.

## Banked State

The same-field scalar MCA lower/failure branch is theorem-grade.

The exact denominator-free upper object is syndrome transverse-secant
incidence. Let `H_RS` be a parity-check matrix for `RS[F,L,k]`; for a `j`-set
`T`, put

```text
V_T = span{H_RS(:,x): x in T}.
```

For an affine syndrome line

```text
ell(z)=u+zv,
```

bad MCA slopes at reserve `sigma` correspond to transverse incidences

```text
ell(z) in V_T,    v notin V_T,    |T|=n-k-sigma.
```

The old pure target `bad slopes <= n^{1+o(1)}` is false. The corrected target
must include:

```text
occupancy/main term
+ quotient/action-rank templates
+ tangent/common-envelope/hereditary templates
+ primitive finite discrepancy.
```

Cycle 59 further showed that quotient templates must be stronger than monomial
`X -> X^M` action rank. The quotient ledger likely must include split-rational
maps

```text
R(X)=P(X)/Q(X)
```

with many equal-size split fibers in the evaluation domain and action rank

```text
d_R(E)=deg minpoly([R(X)] mod E).
```

The route is not one lemma from solved. We need canonical finite container
theorems. Your job is to either find/prove one, or kill it with a precise
counterpacket.

## Output Contract

Give a verdict label:

```text
PROOF
PROOF_CANDIDATE
COUNTEREXAMPLE
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
CONDITIONAL
```

Then provide:

1. Exact theorem/counterexample/lemma.
2. Full proof or construction details.
3. Parameter ledger.
4. Route-board impact.
5. What remains open.
6. Final section titled exactly:

```text
Do you see a route to a full solve?
```

In that final section, state the next exact lemma or construction.

