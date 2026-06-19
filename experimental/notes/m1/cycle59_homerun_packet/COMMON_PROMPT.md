# COMMON PROMPT FOR ALL CYCLE 59 INSTANCES

Try to fully solve the problem. If you cannot fully solve it, progress it as much as possible. No Internet. Take all the time to reason you need. Use MAX reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?

You are working on the RS-MCA / Proximity Prize problem for Reed-Solomon codes. Read the attached context carefully, especially:

1. `m1_cycle58_5p5_upper_audit.md`.
2. The raw Cycle 58 files in `cycle58_5p5_raw/`.
3. The Cycle 49-57 compact Fable-loop audits and `PRZ_REVIEW_INDEX.md`.
4. `experimental/agents-log.md`.

If the files are available, use them. If any file is not readable, continue from the summary below without asking for missing context.

## Current State To Treat As Banked Unless You Find A Defect

The Cycle 45-57 lower/failure branch for scalar MCA is strong. The random-anchor/Bessel mechanism gives source-valid lower/failure constructions below the entropy boundary. In smooth-domain same-field language, for

```text
C = RS[F,L,k],  n = |L|,  rho = k/n,
a = k + t,      j = n-a,
N = binom(n,a),
lambda = N / q^t,
```

there is a line producing many/all bad slopes when `lambda` dominates the Johnson/Bessel local shell. This is not the upper/safe side.

The exact denominator-free MCA upper object is the syndrome transverse-secant formulation. Let `H_RS` be a parity-check matrix for `RS[F,L,k]`; for a `j`-set `T subset L`, define

```text
V_T = span{ H_RS(:,x) : x in T }.
```

For an affine syndrome line

```text
ell(z) = u + z v,
```

bad MCA slopes at radius `delta = j/n` correspond to transverse incidences

```text
ell(z) in V_T,      v notin V_T.
```

This formulation covers all residue-denominator degrees `t`, including `t < sigma`, `t = sigma`, and `t > sigma`.

Cycle 58 cut the old overbroad upper target

```text
bad slopes <= n^{1+o(1)}.
```

The corrected target is calibrated:

```text
bad slopes
  <= n^{1+o(1)}
     + unavoidable occupancy/main term
     + explicit quotient/action-rank templates
     + tangent/common-envelope templates.
```

A same-field bound should allow an occupancy term of the form

```text
O( binom(n,k+t) / q^{t-1} )
```

or equivalently normalized MCA contribution roughly

```text
binom(n,k+t) / q^t.
```

The stable upper wall is:

```text
W-MCA-CALIBRATED-SYNDROME-TRANSVERSE-SECANT-INVERSE
```

The old literal quotient-pullback exclusion `E(X)=E_0(X^M)` is too narrow. The quotient invariant must also see quotient-action rank

```text
d_M(E) = deg minpoly( [X^M] mod E ).
```

Arbitrary anchors can produce quotient-component or fixed-defect quotient packets. A valid theorem must either subtract them explicitly or charge them at the correct quotient profile.

Balanced `t=sigma` alone is not enough. The exact MCA normal form ranges over all denominator degrees. In residue language:

- `t < sigma`: residual or jet-residue regime; raw feasible support fibers are false, actual lists/full-support objects are needed.
- `t = sigma`: balanced point-cloud regime.
- `t > sigma`: thick residue-plane / support-dependent affine-plane incidence regime; no general compression to `t <= sigma` is banked.

The interleaved list problem at the official `epsilon* = 2^-128` scale appears reducible to scalar list/full-support local limit by linear projection, but the scalar list theorem is still open.

## Official Challenge Constraints To Keep In View

Rates:

```text
rho in {1/2, 1/4, 1/8, 1/16}.
```

The official target is finite, with `epsilon* = 2^-128`. Do not output only a rate-asymptotic slogan. Track dependence on:

```text
n, q, q_gen, q_line, q_chal, quotient profile, tangent floor, occupancy term.
```

Do not merge `q_gen`, `q_line`, and `q_chal` unless you prove the transfer.

## Output Contract

Give a verdict label at the top, using one of:

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

1. The exact theorem, counterexample, or lemma you are asserting.
2. Full proof or construction details, not a sketch unless you label it as incomplete.
3. Parameter ledger.
4. How it changes the route board.
5. What remains open.
6. A final section titled exactly:

```text
Do you see a route to a full solve?
```

In that final section, state the next exact lemma or construction. Be concrete. If you think a full solve is not currently reachable, say so and give the precise blocker.

