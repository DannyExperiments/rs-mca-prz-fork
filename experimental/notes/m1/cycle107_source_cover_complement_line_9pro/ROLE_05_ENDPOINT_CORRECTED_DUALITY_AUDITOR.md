# Role 05: Endpoint-Corrected Duality Auditor

Your target is the endpoint defect noted in Cycle106.

The ordinary complement-duality line can fail at the endpoint, especially when:

```text
sigma+1 = n
```

The corrected all-endpoint map must use:

```text
(1-X^n) A(X)^(-1) mod X^(sigma+2)
```

Audit and repair the complement-line normal form so it is valid in every
source range needed by the official M1 chain.

Required:

1. State the exact endpoint/non-endpoint split.
2. Prove the corrected map or give the missing algebraic identity.
3. Decide whether Gate A must exclude endpoints, include corrected endpoints,
   or charge endpoints separately.
4. Decide whether Gate B changes under the corrected map.
5. Produce the exact theorem statement that should replace the ordinary
   complement-line formula.

Return `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `AUDIT`, `ROUTE_CUT`, or `PLAN`.
