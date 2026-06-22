# Cycle 96 Arbitrary-Word Norm Sieve Audit

## Verdict

**ROUTE_CUT / BANKABLE_LEMMA / EXACT_NEW_WALL.**

Cycle96 cuts the arbitrary-word norm-sieve route. The monomial norm sieve works
because prefix fibers produce word-independent height-one collision
polynomials. Arbitrary words do not preserve that invariant; any analogous
cyclotomic invariant carries the archimedean height of the arbitrary word.

The exact next wall is therefore fixed-prime arbitrary-word collision counting,
not a repaired `Z[zeta]` norm argument.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle96_arbitrary_word_norm_sieve_raw/
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T11-28-52-491Z-cycle96-arbitrary-word-norm-sieve-717ada65
model: claude-opus-4-8
mode: artifact_stream
status: OK
elapsed: 750379 ms
cost: 3.4085462499999997 USD
capture warning: none
stop reason: end_turn
```

Checksums were generated in:

```text
experimental/notes/m1/cycle96_arbitrary_word_norm_sieve_raw/SHA256SUMS.txt
```

## Route Cut

```text
L-CYCLE96-NORM-SIEVE-IS-DEAD
```

The monomial proof uses a prefix-fiber invariant with small coefficients:

```text
F_{S,T} = 1_S - 1_T
```

For arbitrary words, the fiber equations are weighted by the arbitrary
interpolant coefficients of `U`. Subtracting two support conditions gives a
`U`-weighted symmetric-function relation, not a word-independent power-sum
identity.

Even if one grants a hypothetical cyclotomic invariant with coefficient height
`H`, the Galois/norm contradiction requires roughly:

```text
H < p^(sigma/n) / n.
```

For arbitrary words this threshold is incompatible with the natural coset
height scale in the live range `sigma <= (1-rho)n`, especially
`sigma = Theta(n/log n)`.

## Bankable Lemma

```text
L-CYCLE96-WORD-HEIGHT-FLOOR
```

For the dimension-`k+1` RS code, define the characteristic-zero height of a word
as the minimum infinity norm of a balanced integer lift after adding a
codeword. Counting cosets gives:

```text
H(w) >= p^(1-rho-o(1))
```

for a `1-o(1)` fraction of arbitrary words.

Codeword normalization, scalar rescaling, and affine color changes do not
remove this height. Therefore the monomial norm-sieve threshold is too small
for arbitrary-word fibers across the admissible reserve range.

## Codex Local Follow-Up

Codex added and ran:

```text
experimental/scripts/cycle96_word_height_floor_toy.py
```

The script enumerates small RS word cosets and measures the minimum balanced
lift height in each coset.

Run result:

```text
cycle96 word-height floor toy check
PASS
```

This is a sanity check only; the bankable claim is the coset-counting height
floor above.

## Claim Level

Bank as:

```text
upper-side route cut
arbitrary-word height obstruction
not a proof of arbitrary-word local limit
not a counterpacket
not a finite prize certificate
```

## Exact New Wall

```text
S1 / L-CYCLE97-FIXED-PRIME-TWO-SUPPORT-APERIODIC-COLLISION
```

For fixed support `S` in an arbitrary-word fiber, bound the number of aperiodic
supports `S'` in the same fiber with `S triangle S'` not explained by quotient
cosets. This is the fixed-prime local-limit replacement for the failed norm
route.

Cycle96 suggests attacking this through the syndrome-bandwidth filtration:

```text
F_b = { w : deg U <= s+b }.
```

The `b=0` layer is the monomial/prefix case. The first useful new target is a
proof or counterpacket for `b=1` or `b=O(log n)` before trying full arbitrary
bandwidth.

