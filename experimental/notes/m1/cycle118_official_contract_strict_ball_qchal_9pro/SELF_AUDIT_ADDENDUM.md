# Self-Audit Addendum

Before finalizing, audit your own answer against these traps.

## Scope Traps

Do not collapse these claim levels:

```text
finite checker theorem
attached-manuscript source theorem
official/prize-adopted source theorem
ordinary list-decoding theorem
protocol soundness failure
asymptotic theorem
```

If you say `PROOF`, specify which one.

## Agreement / Radius Trap

Cycle116 proves agreement `262` in length `512`, so:

```text
ceil((1 - 125/256) * 512) = 262
```

If an external convention uses strict distance `< delta n` instead of closed
distance `<= delta n`, the target may require agreement `263`, not `262`.

If you need agreement `263`, explain exactly how it is obtained, or prove why
Cycle116 cannot be upgraded without a new fixed-jet/cosupport construction.

## Fixed-Jet Trap

The current smooth row uses:

```text
n = 512
k = 256
j = 250
sigma = 6
agreement = n - j = 262
```

At the same `n,k`, agreement `263` through the same fixed-jet framework would
require either:

```text
j = 249 and sigma = 7
```

or a different construction. Do not handwave this.

## q-Chal Trap

The attached finite theorem has:

```text
q_gen = q_code = q_line = 17^32
q_chal = null
```

Do not invent a challenge denominator. If an official protocol uses a separate
challenge field, pin it from source text or mark the contract missing.

If you propose field thickening, prove whether bad slopes remain confined to
the old subfield or thicken to the new line field.

## Event-Retention Trap

Cycle117 says raw events are retained under the attached manuscript
definitions. Official retention may still add endpoint, quotient, periodic,
tangent, contained-line, affine-color, final-event, or charge rules.

If you claim official retention, identify the exact rule text or contract field.

## PRZ-Facing Trap

Only write a PRZ-facing theorem/note if your result is genuinely prize-shaping:

```text
official-admissibility closure
strict-ball/agreement upgrade
accepted-field compiler
q_chal no-loss theorem
source-valid counterpacket
```

Otherwise give an internal route-board result only.

