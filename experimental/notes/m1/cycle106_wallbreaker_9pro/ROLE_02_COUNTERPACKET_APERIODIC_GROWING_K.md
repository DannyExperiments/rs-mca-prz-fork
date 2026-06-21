# Role 02: Counterpacket Hunter - Aperiodic Growing k

Your role is adversarial. Try to kill the Cycle106 wall by constructing a
source-valid counterpacket:

```text
aperiodic Uhat above corrected reserve
and some growing-k / growing-s layer M_s
with |Gamma cap M_s| superpolynomial in n.
```

Periodic/coset-swap families do not count unless you prove they survive the
above-reserve aperiodicity condition. Weighted multiplicity does not count; the
counterpacket must give superpolynomially many distinct active theta values.

Try these mechanisms first:

1. Quotient or subgroup-periodic structure that evades the current
   aperiodicity definition.
2. Same-slope or affine-color normalization causing many theta values to map
   to the same elementary-symmetric prefix layer.
3. Contained incidences where Gamma is forced into a low-dimensional component
   of some `M_s`.
4. A central-rate construction using complement duality `M_s ~= M_{n-s}`.

If you find a counterpacket, specify all parameters and verify exactly which
source hypotheses it satisfies. If you cannot find one, give the strongest
failed mechanism and the exact extra condition that blocks it.

Return `COUNTERPACKET`, `ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, or `PLAN`.

