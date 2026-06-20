# ROLE 01: DIRECT PROOF OF `m_max(beta) <= 12`

Your role is proof-builder.

Try to prove:

```text
max_v m(v) <= 12
```

for the explicit Cycle84 seven-slot product/color model.

Use all banked structure:

- all 4-slot product maps are injective;
- product-fiber minimum distance is at least 5;
- color compatibility is mod 16 with target color 4;
- tau symmetry from Cycle79 gives `m(v)=m(K/v)`;
- the left/right MITM split is `{1,2,3}` versus `{4,5,6,7}`.

Do not use a Singleton-style bound unless it reaches 12. It probably will not.

The desired output is a finite theorem:

```text
For every v, no more than 12 compatible L/R representations exist.
```

If you cannot prove 12, prove the strongest explicit upper bound you can and
state exactly what missing lemma would close the gap.

