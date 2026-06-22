# Cycle 94 Upper Residue-Cloud Wall Return Audit

## Verdict

**PLAN / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle94 did not prove the arbitrary-anchor residue-cloud upper theorem. It did
bank a clean structural lemma for one residue datum and cut the pairwise/secant
packing route as insufficient for the full upper theorem.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle94_upper_wall_return_raw/
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T10-52-45-071Z-cycle94-upper-wall-return-3bc32639
model: claude-opus-4-8
mode: artifact_stream
status: OK
elapsed: 316374 ms
cost: 3.48709675 USD
capture warning: none
stop reason: end_turn
```

Checksums were generated in:

```text
experimental/notes/m1/cycle94_upper_wall_return_raw/SHA256SUMS.txt
```

## Bankable Lemma

```text
L-CYCLE94-ANCHORED-SECANT-INTERSECTION
```

For a degree-`t` residue datum `(E,B,w)` with `B != 0`, `deg B < t`, and
`E` root-free on the evaluation domain, if distinct slopes `z != z'` both have
bad witnesses with maximal support sets `S_z` and `S_z'`, then:

```text
|S_z cap S_z'| <= k + t - 1.
```

The proof is the elementary degree count:

- witnesses give polynomials `Q_z`, `Q_z'` of degree `< k+t`;
- `Q_z - Q_z'` vanishes on `S_z cap S_z'`;
- if the intersection has size at least `k+t`, then `Q_z = Q_z'`;
- reducing modulo `E` gives `(z-z')B == 0 mod E`;
- since `z != z'`, this forces `E | B`, impossible for `B != 0` and
  `deg B < deg E`.

Codex local follow-up:

```text
experimental/scripts/cycle94_anchored_secant_toy_check.py
```

The toy verifier enumerates small arbitrary-anchor residue data for `t=1` and
`t=2`. It checked 40 cases, saw 222 bad slopes, and confirmed the bound
`max |S_z cap S_z'| <= k+t-1` in every case. This is only a sanity check; the
lemma itself is the degree-count proof above.

## Route Cut

The lemma is not enough to prove the upper theorem. A family of `(k+sigma)`-sets
with pairwise intersections bounded by `k+t-1` is only a constant-weight code
condition. At the relevant reserve scale, such families can still be
exponentially large.

This cuts the route:

```text
pairwise/secant intersection bound alone
  -> arbitrary-anchor residue-cloud upper theorem
```

The monomial-prefix theory succeeds because it has extra moment/prefix
constraints; arbitrary anchors do not preserve those constraints. This is the
same obstruction recorded by `prop:noanchor`.

## Claim Level

Bank as:

```text
official-upper-side structural lemma
route cut for pairwise/secant-only method
not a proof of RCUT
not a finite prize certificate
not a lower-side counterpacket
```

## Exact New Wall

Cycle94 names the next atom:

```text
L-CYCLE95-ANCHORED-PERFIBER-COLLISION-T1
```

Start with the minimal case:

```text
t = 1,  E = X - alpha,  B = 1,  w arbitrary.
```

Decide whether the number of noncontained `(k+sigma)`-agreement slopes on one
arbitrary anchored line is polynomial above corrected reserve after quotient
exceptions are charged. A proof gives the first unconditional crack in the
arbitrary-anchor upper wall. A stable exponential `t=1` adversarial-anchor
cloud is a counterpacket to the residue-cloud upper route.

