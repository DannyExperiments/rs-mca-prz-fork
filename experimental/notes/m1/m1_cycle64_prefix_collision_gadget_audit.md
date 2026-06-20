# Cycle 64 Prefix-Collision Gadget Audit

## Executive Verdict

**Status:** `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL`.

**Significance:** high for route narrowing, not a prize solve. Cycle 64 closes
the qualitative prefix-gadget bookkeeping layer and simultaneously proves that
this layer cannot be the scalar-list smallness theorem.

The answer should be banked as follows:

- `BANKABLE_LEMMA`: exact per-coset prefix-collision gadget convolution.
- `BANKABLE_LEMMA`: Role 05 characteristic-17 packet is absorbed exactly by
  seven gadget-class enumerators plus one marker.
- `ROUTE_CUT`: total gadget charge equals the scalar support mass, so it
  cannot prove smallness once Role 05 gives
  `52,747,567,104 > 2^32` supports.
- `EXACT_NEW_WALL`: the relevant surviving object is thickened MCA color
  occupancy, not scalar support mass.

## Bankable Lemma

The worker's bankable structural lemma is:

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-CONVOLUTION
```

For cyclic `H`, a divisor subgroup `J <= H`, and

```text
E_T(z) = prod_{x in T}(1 - x z),
pi(T) = prod_{x in T} x,
Phi_sigma(T) = (pi(T), E_T(z) mod z^sigma),
```

partition `H` into `J`-cosets. For one coset `C`, define

```text
Z_C(q) =
sum_{A subseteq C} q^{|A|} [E_A mod z^sigma] [pi(A)].
```

Equivalently, regroup terms by local prefix-collision classes

```text
A ==_sigma B
iff |A|=|B| and E_A(z) == E_B(z) mod z^sigma,
```

with each class carrying a product-color enumerator

```text
W_C = sum_{A in class} Y^{pi(A)}.
```

Then

```text
prod_C Z_C(q)
= sum_{T subseteq H} q^{|T|} [E_T mod z^sigma] [pi(T)].
```

Thus every model fiber count is an exact coefficient extraction:

```text
N_Delta(b)
= [q^j g_b p_b] prod_C Z_C(q).
```

This is a genuine partition for fixed `J`, so overlap is zero at that chosen
scale. Full coset-block trades are the singleton-gadget special case.

## Role 05 Absorption

The Role 05 near-split packet is not random residual mass. It is exactly the
coefficient of seven local gadget enumerators plus one marker. In the
characteristic-17 model:

```text
F_0 = F_{17^16},
H_0 = mu_256,
sigma = 6,
j = 113,
K = <eta^8>, |K|=32.
```

The seven active `K`-cosets each contribute one gadget class with

```text
W_t(Y) =
8 Y^t (Y^1 + Y^4 + Y^7 + Y^9 + Y^12 + Y^15).
```

The marker `{1}` supplies the fixed jet `1-z`. The count is

```text
[Y^0] prod_{t=1}^7 W_t(Y)
= 8^7 c_7(4)
= 52,747,567,104.
```

This verifies that prefix gadgets absorb Role 05 descriptively.

## Route Cut

The same exactness cuts the hoped scalar smallness theorem. For any fixed
`J`, the total gadget charge is exactly `N_Delta(b)`. Therefore no
canonicality, maximal assignment, or bounded-overlap repair can turn this
charge into a small scalar-list bound: the partition has already removed the
overlap.

Cycle 64 therefore kills the route:

```text
scalar apolar CI/GJ fiber
-> block trades
-> prefix gadget partition
-> small scalar support mass
```

The scalar support mass can still be exponentially large after the prefix
gadget partition is made exact.

## New Wall

The next exact wall is:

```text
W-MODEL-GJ-THICKENED-GADGET-COLOR-OCCUPANCY
```

For the thickened divisor

```text
Delta^+ = Delta + [beta],
```

push the gadget enumerators by

```text
rho_beta(T) = prod_{x in T}(beta - x)
```

and count occupied colors, not total support mass:

```text
Occ(b)
= |supp of the pushed gadget product at scalar boundary b|.
```

The live question is whether `Occ(b)` is large or collapses below the finite
line target. The worker gives the concrete next falsifier: in the Role 05
packet, compute the 48 values per active coset

```text
v_{t,A} = prod_{x in eta^t A~}(beta - x),
```

then count distinct sevenfold products under the product-color constraint.

## What Is Not Proved

- No prize-level safe-side theorem is proved.
- No scalar-list local limit is proved.
- No `t=1` MCA transfer is proved.
- The finite relevance of the `(n,sigma,j)=(256,6,113)` model packet remains
  unresolved.
- The thickened occupancy may still be either a new counterpacket or an
  absorbed finite-irrelevant stratum.

## Recommended Next Step

Do not launch another broad proof attempt. The next work should target one of
two concrete tasks:

1. `W-MODEL-GJ-THICKENED-GADGET-COLOR-OCCUPANCY`: prove/kill the Role 05
   thickened color occupancy calculation.
2. `RS-PRIZE-FRONTIER-V1-REGISTRY-FIRST-RUN`: place the banked lower packets,
   quotient/projective/Lattes packets, scalar apolar block charges, and new
   prefix-gadget residual charge in a finite reserve ledger.

The highest-value immediate worker prompt is the thickened color occupancy
falsifier, because it decides whether the scalar-apolar to `t=1` MCA spine is
cut at the model level or merely redirected to the frontier checker.

## Raw Provenance

Raw artifacts and checksums are preserved in
`experimental/notes/m1/cycle64_prefix_collision_gadget_raw/`.
