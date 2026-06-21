# Role 04: Aperiodic Dephasing to Distinct Support

Your role is to convert the banked aperiodicity machinery into a distinct
support bound.

Cycle100/Cycle101-style routes often control weighted counts or Fourier mass.
Cycle106 needs distinct support:

```text
#{theta : Gamma(theta) in M_s}
```

not a sum over witnesses.

Try to prove an exact lemma of this form:

```text
L-CYCLE106-APERIODIC-DEPHASING-DISTINCT-SUPPORT:
For above-reserve aperiodic Uhat, any family of many distinct theta with
Gamma(theta) in M_s yields a forbidden periodic/dephased structure in Uhat.
```

Your answer must identify:

1. The dephasing map.
2. The periodic structure it would create.
3. Why that structure violates the actual above-reserve aperiodicity
   hypothesis.
4. Why witness multiplicity cannot invalidate the distinct theta conclusion.

If this route fails, give the exact witness-multiplicity mechanism that breaks
weighted-to-distinct transfer.

Return `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`, or `PLAN`.

