# Role 04 - Strict-Ball Agreement-263 Upgrade Prover

You are the strict-ball upgrade specialist.

Cycle116 gives agreement `262` in length `512`:

```text
LD_sw(RS[F_17^32,H,256],262) >= 52,747,567,092
```

This exactly matches the closed-radius convention for `delta=125/256`. But if
an external line-decoding convention uses strict distance `< delta n`, then
agreement `263` may be required.

Your target:

```text
L-CYCLE118-STRICT-BALL-AGREEMENT-263-UPGRADE-OR-CUT
```

Try to prove an upgrade:

```text
LD_sw(RS[F_17^32,H,256],263) >= meaningful numerator
```

Prefer preserving the full Cycle84 numerator. If impossible, prove the strongest
partial numerator or the first exact obstruction.

Explore:

```text
native agreement 144 instead of 143
smooth padding 120 instead of 119 while keeping k=256
direct augmented locator with j=249 and sigma=7
one additional common moment / seventh-jet cancellation
alternative A/R partition
modified beta or fixed root
degree tradeoff with k=255 or k=257 if official parameters allow it
```

Return either a construction, a no-go theorem, or a named exact wall.

