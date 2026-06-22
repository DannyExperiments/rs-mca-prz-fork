# Role 03: Gate B Complement-Line Escape Prover

Assume Gate A is true and you are handed a source-valid `AP_corr(Uhat)`.

Your target is:

```text
L-CYCLE107-APERIODIC-COMPLEMENT-LINE-ESCAPE
```

Prove or reduce:

```text
AP_corr(Uhat)
=> complement line L_U(theta) is not contained in the bounded-degree
   exceptional closure of M_m.
```

Use the Cycle106 normal form:

```text
V(X)=Uhat(X)^(-1) mod X^(d+1)
L_U(theta)=(v_j - theta*v_{j-1})_{j=1}^d
```

A successful proof should produce an eliminant/subresultant/Wronskian
certificate:

```text
R_{m,D}(Uhat) != 0
```

under `AP_corr(Uhat)`, with `D = n^{O(1)}` independent of `s` and `k`.

Required:

1. State the polynomial family whose vanishing defines the exceptional closure.
2. State the degree bound `D`.
3. Prove why AP_corr excludes line containment.
4. Explain endpoint correction if your proof uses complement duality.
5. Separate distinct theta count from witness multiplicity.

Return `PROOF`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `ROUTE_CUT`, or `PLAN`.
