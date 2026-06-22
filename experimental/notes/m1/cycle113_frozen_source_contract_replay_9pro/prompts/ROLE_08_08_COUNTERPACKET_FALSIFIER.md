# Role 08 - Counterpacket Falsifier

Your task is adversarial. Try to build a source-valid low-`t=1` counterpacket
that survives the obvious charges. If the P190 packet fails, try to repair it.

Allowed directions:

```text
interval / overlapping-prefix variants
Prouhet-like prefix designs
trivial-stabilizer affine variants
same-field q_gen = q_code = q_line constructions
endpoint-balanced constructions
Fourier-concentrated APcorr survivors
```

The counterpacket bar is high. You must provide:

```text
source adapter acceptance
official AP_corr true
final retained colors > floor(q_line / 2^128)
all charges absent or exactly paid
no quotient/periodic escape
no contained-incidence overcount
no same-slope or endpoint collapse below threshold
```

If you cannot produce a source-valid `COUNTERPACKET`, report the strongest
failed mechanism and the exact obstruction. A good `ROUTE_CUT` is useful if it
shows a whole counterpacket family is inevitably charged or compressed.

If you find only model/finite evidence, label it as such and give the source
receipt needed to promote it.

