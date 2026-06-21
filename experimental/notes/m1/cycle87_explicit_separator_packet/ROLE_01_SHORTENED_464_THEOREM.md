# ROLE 01 - Shortened 464 Theorem Formalizer

Your job is to prove or kill the shortened two-copy package:

```text
L-CYCLE86-TWO-BLOCK-SHORTENED-GENERIC-TRANSLATE-464
(n,k,sigma,j) = (464,232,6,226)
```

Focus only on the algebraic validity of the RS/GRS construction. Do not spend
time on implementation engineering unless it is needed for the proof.

Required tasks:

1. State the exact domain, including how the two shortened blocks are chosen.
2. Prove or refute that deleting 24 universally unused coordinates from each
   block preserves the needed six-jet/common local condition.
3. Prove or refute that the supports have exact size `j=226` or, after
   complementing, exact agreement size `k+sigma=238`, consistently with
   `n=464,k=232,sigma=6`.
4. Give the exact one-code/one-line GRS or syndrome-space formulation.
5. Prove transversality/noncontainment.
6. Identify precisely where same-slope collisions are controlled by the
   projective separator.

If the shortened package fails, give the first false line and say whether the
560-point padded package still survives.

