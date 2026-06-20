# Cycle 80 Mindistance / Symmetric-Energy Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / PLAN
```

Confidence: high for the exact reductions and checker specification; unknown
for the actual three-slot injectivity certificate because neither the worker
nor Codex completed the finite run in this cycle.

Cycle 80 does **not** prove:

```text
m_max(beta) <= 12
```

and it does **not** prove all three-slot product maps are injective. It also
does not produce a three-slot collision or a `13`-fold packet.

## Banked Lemmas

### L-CYCLE80-WEIGHT-3-STRUCTURE

Any three-slot product collision differs in all three slots.

Reason: if two assignments in a three-slot collision agree in one slot, cancel
that nonzero slot value. The remaining equality is a two-slot product
collision, contradicting the Cycle 77 pair-subset injectivity certificate.

### L-CYCLE80-RATIO-TRIPLE-REFORMULATION

For a slot `t`, define the nontrivial single-slot ratio set:

```text
R_t = {u_t(k)/u_t(k') : k != k'}.
```

Then the product map on slot triple `(t1,t2,t3)` is injective exactly when

```text
(R_t1 R_t2) cap R_t3 = empty.
```

Equivalently, there are no ratios

```text
r_i in R_ti,  r_1 r_2 r_3 = 1.
```

This is the exact finite rung below the coherent-ratio route.

## Checker Spec

Cycle 80 supplied an exact packed-product-only checker. Codex preserved it as:

```text
experimental/scripts/cycle80_three_slot_injectivity_checker.py
```

Its intended certificate outputs are:

```text
ALL_3_SUBSETS_PRODUCT_INJECTIVE
PRODUCT_COLLISION_FOUND
```

Color is recorded only in collision packets. It is not used as an equality key.

## Local Follow-Up

Codex attempted to run:

```text
python3 experimental/scripts/cycle80_three_slot_injectivity_checker.py --size 3
```

but interrupted it after roughly one minute because the pure-Python field
multiplication remained too slow for a heartbeat-local bounded follow-up. No
empty or partial certificate is banked.

This is a local execution gap, not a mathematical counterexample.

## Route Cut

The soft coding-theoretic consequence of a possible minimum-distance bound is
too weak to prove `m_max(beta)<=12`. Even if the three-slot rung passes, the
real prize-scale finite object remains a compiled MITM left/right coincidence
census with the color filter and Cycle 79 tau-folding.

The current route should therefore stop asking for more broad hand proofs of
`m_max<=12` and demand executable certificates.

## Remaining Wall

```text
V-CYCLE81-COMPILED-THREE-SLOT-CERTIFICATE
L-CYCLE80-MINDIST-CERTIFICATE
W-CYCLE80-COMPILED-MITM-MMAX-CENSUS
```

Acceptable next progress:

1. A compiled or vectorized exact certificate for all 35 three-slot product
   maps.
2. An explicit three-slot product collision packet.
3. A compiled MITM exact `m_max(beta)` census design with a certificate small
   enough for Codex to run or verify.

## What To Do Next

Stage Cycle 81 as a checker/certificate run, not another theorem brainstorm.
The prompt should ask for a C/Rust/Python-vectorized exact implementation or a
smaller algebraic proof of the same all-triples injectivity certificate.
