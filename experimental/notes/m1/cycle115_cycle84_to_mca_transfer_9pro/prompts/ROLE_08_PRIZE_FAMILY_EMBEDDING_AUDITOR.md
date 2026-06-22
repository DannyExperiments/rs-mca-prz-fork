# Role 08: Prize-Family / Smooth-Domain Embedding Auditor

Use the common prompt. No Internet.

Your role is to decide whether the Cycle84 transfer lands in the official smooth multiplicative RS family, or only in an arbitrary finite/GRS/model row.

The source papers repeatedly emphasize smooth multiplicative domains: subgroups or cosets, usually power-of-two order. Cycle84 lives over `F_17^16` with a constructed seven-slot color/product model. A paper-facing theorem may tolerate a finite RS/GRS row; a prize-facing theorem may require more.

Audit:

1. Does the Cycle85 one-copy row have an evaluation domain that is an official smooth multiplicative subgroup/coset?
2. Does the Cycle88/89 `[464,232]` row over `F_17^48` have an official smooth multiplicative subgroup/coset domain?
3. If the row is GRS, can it be converted to RS without changing support-wise MCA/list/line-decoding?
4. Is there an embedding theorem from the Cycle84 finite packet into a smooth multiplicative RS domain?
5. Is arbitrary-domain MCA enough for PRZ's paper goals, or not?
6. Does any quotient/periodic/domain-symmetry condition remove the claimed bad slopes?

Output one of:

```text
PRIZE_FAMILY_EMBEDDING_PROVED
FINITE_RS_ONLY
ARBITRARY_DOMAIN_ONLY
GRS_EQUIVALENCE_MISSING
SMOOTH_DOMAIN_EMBEDDING_MISSING
ROUTE_CUT
```

State the exact theorem that would be needed to upgrade the row.
