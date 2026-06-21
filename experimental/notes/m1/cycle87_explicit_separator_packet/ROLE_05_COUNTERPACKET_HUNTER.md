# ROLE 05 - Counterpacket Hunter

Your job is to attack the two-copy route as hard as possible.

Try to find a fatal flaw in:

```text
L-CYCLE86-TWO-BLOCK-SHORTENED-GENERIC-TRANSLATE-464
L-CYCLE86-TWO-BLOCK-GENERIC-TRANSLATE-RECIPROCAL-PRODUCT-COMPOSITION
V-CYCLE86-U-PROJECTIVE-MMAX8-CENSUS
```

Required attacks:

1. Check whether two block copies can really be fused into one RS/GRS code and
   one affine syndrome line.
2. Check whether affine color normalization collapses the numerator.
3. Check whether quotient/periodic structure charges the packet away.
4. Check whether contained incidences or same-slope collisions are being
   double-counted.
5. Check whether the `464` shortening changes the code dimension or destroys
   transversality.
6. Check whether projective multiplicity `<=8` is actually sufficient.
7. Check whether the field-size/target comparison uses the wrong `q`.

If the route fails, produce a concrete COUNTERPACKET with the first false
implication. If it survives, identify the narrowest exact theorem still needed.

