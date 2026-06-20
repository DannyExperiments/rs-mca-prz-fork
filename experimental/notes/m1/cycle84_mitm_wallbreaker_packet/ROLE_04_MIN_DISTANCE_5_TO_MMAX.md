# ROLE 04: MIN-DISTANCE-5 TO MMAX BOUND

Your role is obstruction reducer.

We know every product collision among seven representations must differ in at
least 5 slots, because all product maps on subsets of size up to 4 are
injective.

Investigate whether this plus the color constraint forces:

```text
m_max <= 12.
```

Do not repeat the known failure "minimum distance 5 alone is insufficient."
Instead, add the missing data:

- constant-composition/color sum 4 mod 16;
- slot table structure from Cycle68;
- left/right split;
- tau symmetry;
- finite field product constraints.

Possible deliverables:

1. a proof of `m_max<=12`;
2. a sharper coding-theoretic upper bound below 13;
3. a construction showing min-distance-5 plus color still allows 13 in an
   abstract model, hence product algebra is essential;
4. a smaller exact wall.

