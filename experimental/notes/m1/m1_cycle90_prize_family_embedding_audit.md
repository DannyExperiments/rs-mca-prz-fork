# Cycle 90 Prize-Family Embedding Audit

## Verdict

**ROUTE_CUT / BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL.**

Cycle90 cuts the direct upgrade of the Cycle87/Cycle89 `n=464` row to a
Proximity Prize counterpacket. It also banks a separate, cleaner smooth
power-of-two subgroup construction in the below-reserve regime.

The result should **not** be read as an above-reserve prize-frontier solve.

## Raw Artifacts

Raw Fable artifacts were preserved under:

```text
experimental/notes/m1/cycle90_prize_family_embedding_raw/
```

Files preserved:

```text
FILE_INDEX_FOR_MODEL.md
input_manifest.json
prompt_sent.md
raw_response.json
raw_response.jsonl
response.md
run_result.json
run_status.json
SHA256SUMS.txt
```

Run metadata:

```text
run path: /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-21T09-03-30-413Z-cycle90-prize-family-embedding-9e532f17
model: claude-opus-4-8
mode: artifact_stream
status: OK_WITH_NONFATAL_STREAM_WARNING
elapsed: 1230945 ms
capture warning: Claude CLI stream-json parse warning: 1 malformed line(s)
fatal warning: false
```

The stream warning is nonfatal because `response.md`, `raw_response.jsonl`,
`raw_response.json`, and `run_result.json` were all produced and checksummed.

## Main Route Cut

Cycle90 cuts Branch A:

```text
The official prize family is smooth multiplicative subgroup/coset RS,
with smooth meaning power-of-two subgroup order in the source paper.
```

The `n=464=2^4*29` Cycle87/Cycle89 row is therefore a valid finite
arbitrary-RS/GRS MCA row, but it is not itself an official Proximity Prize
counterpacket.

Cycle90 also cuts the literal 464-to-power-of-two port:

```text
464 = 2^4 * 29
```

The factor `29` cannot be realized by padding, shortening, subgroup inclusion,
or quotient pullback inside a pure 2-group multiplicative subgroup domain.
Thus the 464 occupancy mechanism does not transfer to a power-of-two subgroup
by a simple domain operation.

## Bankable Conditional Lemma

Cycle90 banks the following below-reserve power-of-two construction:

```text
L-CYCLE90-PRIZE-FAMILY-EMBEDDING-BELOW-RESERVE
```

Let:

```text
q = 17^48
H <= F_q^*
|H| = 256
rho = 1/2
k = 128
t = 1
delta = 1 - 129/256 = 127/256
```

Since:

```text
v2(17^48 - 1) = 8
```

`F_q^*` contains a power-of-two subgroup `H` of order `256`.

With the degree-`1` residue-line datum `(E,B,w)=(X,1,w)` on `H`, Cycle90
re-derives the `t=1` Bessel/second-moment argument: for a suitable full-field
anchor `w`, almost every `z in F_q` is an occupied, noncontained bad slope.

Local arithmetic check:

```text
q = 115225400457255426923013053222916919834651165519677685328641
log2(q) = 196.1982163800163
v2(q-1) = 8
binom(256,129) =
5723940537996111715313858835708315671556179053122641396696743260541537985280
log2 binom(256,129) = 251.6616158015476
log2(lambda = binom(256,129)/q) = 55.463399421531335
floor(q/2^128) = 338617018271848945628
```

The conservative integer lower bound

```text
q - ceil(q^2 / binom(256,129))
```

is still:

```text
115225400457255424603475870332653609286684532522645220533191
```

which exceeds `floor(q/2^128)` by:

```text
115225400457255424603475870332653609286345915504373371587563
```

## Why This Is Not The Same As The 464 Row

The construction is below the corrected reserve:

```text
gap = 1/256 ~= 0.00390625
tau_star(1/2,17^48) ~= 1/log2(17^48) ~= 0.005096
```

So this is a genuine smooth power-of-two subgroup MCA failure row, but it is in
the easy lower/failure branch already expected by the entropy reserve.

The Cycle87 `n=464` row was interesting because:

```text
gap = 6/464 ~= 0.01293
```

which is above the corrected reserve at the same field size. That above-reserve
power-of-two version remains open.

## Exact New Wall

Cycle90 names the next wall:

```text
W-CYCLE91-ABOVE-RESERVE-POWER-OF-TWO-OCCUPANCY
```

Target:

```text
Produce a smooth power-of-two subgroup H <= F_q^*
with |H|=2^a, q in roughly (2^162,2^256),
rho in {1/2,1/4,1/8,1/16},
and a residue-line datum whose noncontained packing exceeds floor(q/2^128)
at gap t/2^a > (1+epsilon) tau_star(rho,q).
```

Equivalently, build a power-of-two subgroup bad-slope family beating the known
quotient-floor count in the above-reserve regime, or prove that this cannot be
obtained from the current Cycle84/Cycle87 mechanism.

## Source/Definition Status

What is closed:

- `n=464` is not a power-of-two smooth subgroup row.
- The direct 464-to-power-of-two port is cut by the factor-29 obstruction.
- A separate power-of-two subgroup row over `17^48` exists below reserve.

What remains:

- Independent replay or reviewer acceptance of the Cycle87 finite census is
  still useful for the arbitrary-RS/GRS finite row, but is no longer the main
  prize-family blocker.
- The live prize-frontier problem is the above-reserve power-of-two occupancy
  wall, not definition matching and not the literal 464 row.

