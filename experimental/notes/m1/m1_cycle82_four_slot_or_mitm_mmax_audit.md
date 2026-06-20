# Cycle 82 Four-Slot Or MITM Mmax Audit

## Verdict

```text
PROOF / BANKABLE_LEMMA / PLAN
```

Confidence: high for the finite four-slot certificate and the minimum-distance
consequence. Moderate for the Cycle 82 worker's MITM execution plan, because it
is still a specification rather than a completed census.

Cycle 82 itself had read-only access and returned an unrun checker plus a
structural reduction. Codex preserved the raw answer, converted the four-slot
checker into an executable local verifier, and ran the full 35-subset check.

## Banked Lemma

### L-CYCLE82-FOUR-SLOT-PRODUCT-INJECTIVITY

For every four-slot subset

```text
{t1,t2,t3,t4} subset {1,...,7},
```

the product map

```text
(k1,k2,k3,k4) |-> u_t1(k1) u_t2(k2) u_t3(k3) u_t4(k4)
```

is injective on `48^4` tuples under the packed field-product key.

Codex added and ran:

```text
experimental/scripts/cycle82_four_slot_product_checker.py
experimental/notes/m1/cycle82_four_slot_product_certificate.json
```

The exact certificate decision is:

```text
ALL_4_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 5
self_test = scalar_pair_12_matches_vectorized
```

Every one of the 35 four-slot subsets has:

```text
tuple_count = 48^4 = 5308416
distinct_products = 5308416
max_multiplicity = 1
```

## Consequence

Together with the Cycle 77 singleton/pair certificate and the Cycle 81
three-slot certificate, this proves:

```text
L-CYCLE82-PRODUCT-FIBER-MINDIST-GE-5
```

Any two distinct product-equal seven-tuples differ in at least five slots.

Reason: if a collision differed in at most four slots, cancel all agreeing
nonzero slots. The remaining equality would be a product collision on one, two,
three, or four slots. Cycles 77, 81, and 82 exclude all such collisions.

## Worker Contribution

The Cycle 82 worker also supplied a useful structural reduction:

```text
u_t(i,a) = inv3t(t) prod_{b in bset(i,a)}
           (xi - eta^(2t+16b))
```

The exponent supports for different slots lie in disjoint cosets

```text
C_t = 2t + 16 Z / 256Z
```

for `t=1,...,7`. Thus each seven-slot tuple corresponds to a 56-element
balanced exponent set, eight exponents in each of seven disjoint cosets, and
the packed product key is equivalent to a scalar evaluation key:

```text
Phi(T) = const * g_M(xi),  g_M(Y)=prod_{e in M}(Y-eta^e).
```

This is not yet a proof of the maximum fiber bound, but it is the cleanest
current formulation of the remaining finite wall.

## What This Does Not Prove

This does not prove:

```text
m_max(beta) <= 12
```

Minimum distance at least `5` is a strong guardrail but not a small-list bound.
The actual finite prize-local target is still the color-filtered maximum fiber
or maximum intersection computation.

## Remaining Wall

```text
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

Use the Cycle 75/76 split, Cycle 78 incidence formula, Cycle 79 involution,
Cycle 81 three-slot certificate, and Cycle 82 four-slot certificate.

The next exact target is:

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
```

Either certify:

```text
m_max(beta) <= 12
```

with a reproducible threshold census capped at `13`, or produce an explicit
13-fold colored collision packet.

