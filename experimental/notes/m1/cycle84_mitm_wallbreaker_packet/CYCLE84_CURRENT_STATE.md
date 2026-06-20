# Cycle 84 Current State

## Executive State

The prize problem is not solved.

The active finite obstruction route is now sharply localized. Cycles 64-83
reduced the Role 05 thickened-color model to an explicit seven-slot product
occupancy problem over `F_{17^16}`. The exact current target is:

```text
prove m_max(beta) <= 12
or find an explicit 13-fold colored packet.
```

If `m_max(beta) <= 12`, then the occupied thickened-color count clears the
`2^32` model threshold for the explicit packet. If `m_max(beta) >= 13`, an
explicit 13-fold packet cuts this attempted route.

This remains a finite model route, not a full prize theorem by itself. It must
still be paired with the finite frontier ledger before claiming prize-level
relevance.

## Banked Finite Reductions

Key banked facts:

- Cycle 65 reduces thickened-color occupancy to an explicit constrained
  sevenfold product set in `F_{17^16}^*`.
- Cycle 66 corrects admissibility to `beta notin mu_256` and represents
  occupancy by distinct locator evaluations `rho_beta(T)`.
- Cycle 67 cuts the pure color shortcut and exposes `m_max(beta) <= 12`.
- Cycle 68 proves the disjoint-coset factorization into a seven-slot table.
- Cycle 69 banks the energy gate `D <= 155 => m_max <= 12`.
- Cycle 70 cuts a false t-independent normalization, but preserves the
  t-dependent polynomial-evaluation identity.
- Cycle 71 cuts the `(color, product)` key shortcut. Product-only equality is
  the valid target unless color is proved forced by product.
- Cycle 75 locally certifies product injectivity for left slots `{1,2,3}`.
- Cycle 76 locally certifies product injectivity for right slots `{4,5,6,7}`.
- Cycle 77 locally certifies all singleton and pair slot-product maps.
- Cycle 81 locally certifies all 35 three-slot product maps are injective.
- Cycle 82 locally certifies all 35 four-slot product maps are injective.
- Cycle 83 says minimum distance 5 is still insufficient; the exact wall is a
  color-filtered MITM threshold census.

## Exact MITM Form

Let:

```text
L_img = products on slots {1,2,3}, |L_img| = 48^3 = 110592.
R_img = products on slots {4,5,6,7}, |R_img| = 48^4 = 5308416.
```

For each field element `v`, the multiplicity is:

```text
m(v) = #{
  l in L_img :
  v*l^{-1} in R_img
  and colorL(l) + colorR(v*l^{-1}) = 4 mod 16
}.
```

The target is:

```text
max_v m(v) <= 12.
```

Equivalently, abort with a counterpacket if any `v` accumulates 13 compatible
left/right representations.

Cycle 83 estimates:

```text
|P0| = 52,747,567,104 compatible products.
|F| = 17^16 approximately 4.866e19.
random expected accidental colliding pairs approximately 28.5.
```

The recommended execution routes were:

1. Bloom duplicate detector plus exact recount, about 66GB RAM.
2. Deterministic shard/reduce, about 0.5-0.85TB scratch.
3. Low-disk recompute sharding, slow and many-pass.

Local machine state is not suitable for the full census.

## Current Wall Name

```text
W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION
```

Acceptable next results:

```text
PROOF / BANKABLE_LEMMA:
  a source-valid proof or reproducible exact certificate that m_max(beta) <= 12.

COUNTERPACKET:
  an explicit 13-fold colored packet with all data needed for verification.

ROUTE_CUT:
  proof that the Cycle84 target is irrelevant, false as formulated, or cannot
  imply the intended obstruction.

EXACT_NEW_WALL:
  a strictly sharper finite theorem or checker target below m_max(beta) <= 12.
```

