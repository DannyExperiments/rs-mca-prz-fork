# Cycle 95 Anchored Per-Fiber T=1 Audit

## Verdict

**BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle95 does not prove the arbitrary-anchor `t=1` polynomial bad-slope bound.
It gives a sharp exact reduction: the `t=1` anchored MCA cloud is precisely the
evaluation-at-`alpha` image of the arbitrary-word RS list at dimension `k+1`.

Thus the `t=1` MCA wall is not a new independent wall. It collapses onto the
arbitrary-word locator/list wall.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle95_anchored_perfiber_t1_raw/
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-07-59-605Z-cycle95-anchored-perfiber-t1-c34e9889
model: claude-opus-4-8
mode: artifact_stream
status: OK
elapsed: 742196 ms
cost: 3.7723535 USD
capture warning: none
stop reason: end_turn
```

Checksums were generated in:

```text
experimental/notes/m1/cycle95_anchored_perfiber_t1_raw/SHA256SUMS.txt
```

## Bankable Lemma

```text
L-CYCLE95-ANCHORED-T1-EVAL-LIST
```

Let:

```text
E = X - alpha
B = 1
alpha notin D
w: D -> F arbitrary
```

Let `L_w` be the RS list of degree-`<=k` polynomials agreeing with `w` on at
least `k+sigma` points, equivalently the dimension-`k+1` arbitrary-word list:

```text
L_w = { P in F[X] : deg P <= k, |{x in D : P(x)=w(x)}| >= k+sigma }.
```

Then the support-wise noncontained bad slope set of:

```text
y_z(x) = w(x)/(x-alpha) - z/(x-alpha)
```

is exactly:

```text
Z = { P(alpha) : P in L_w }.
```

Consequently:

```text
Lambda^NC_{1,delta}((X-alpha,1,w)) = |eval_alpha(L_w)| <= |L_w|.
```

For nonzero constant `B`, slopes are only rescaled:

```text
z = P(alpha)/B.
```

## Automatic Noncontainment

In this stratum, noncontainment is automatic on every support of size `>k`.
If `g=-1/(X-alpha)` were represented by a polynomial `G` of degree `<k` on
`S`, then:

```text
(X-alpha)G + 1
```

would vanish on more than `k` points while having degree at most `k`, forcing
an impossible identity.

## Route Cut

The `t=1` anchored wall is now identified with the arbitrary-word locator/list
wall. A proof of the `t=1` polynomial cloud bound requires the arbitrary-word
list theorem at dimension `k+1`, with quotient-periodic list cores charged.

This cuts the route:

```text
t=1 anchored MCA special argument
  -> full arbitrary-anchor residue-cloud upper theorem
```

unless that special argument actually proves the arbitrary-word list theorem.

## Codex Local Follow-Up

Codex added and ran:

```text
experimental/scripts/cycle95_t1_eval_list_check.py
```

The script enumerates small finite fields, arbitrary anchors `w`, and all
degree-`<=k` list codewords. It checks:

```text
bad slopes = {P(alpha): P in L_w}
```

and verifies automatic noncontainment on every support witness.

Run result:

```text
cases_checked: 70
total_bad_slopes_seen: 224
total_list_polys_seen: 235
PASS
```

The difference between list polynomials and bad slopes records exact
same-slope collisions from `P(alpha)=P'(alpha)`.

## Claim Level

Bank as:

```text
official-upper-side exact reduction
not a proof of t=1 RCUT
not a finite prize certificate
not a counterpacket
```

## Exact New Wall

Cycle95 points to:

```text
L-CYCLE96-ARBITRARY-WORD-NORM-SIEVE
```

Target statement:

Prove an arbitrary-word replacement for the monomial Galois/norm sieve. The
missing point is archimedean control for an arbitrary lift `U` of the word
`w`; the monomial proof uses small `{ -1,0,1 }` coefficients and has no direct
analogue once `w` is arbitrary.

Equivalently, prove the arbitrary-word locator/list theorem at dimension
`k+1`, after quotient cores are charged. A counterpacket would be an
aperiodic, non-quotient arbitrary word with a superpolynomial list whose
evaluation at `alpha` remains superpolynomial.

