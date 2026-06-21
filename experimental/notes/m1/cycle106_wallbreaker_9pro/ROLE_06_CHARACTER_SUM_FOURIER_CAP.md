# Role 06: Character-Sum / Fourier Cap Route

Your role is to attack Cycle106 through Fourier analysis on the subgroup
`H=mu_n` and elementary symmetric layers.

Do not give a generic character-sum estimate. It must be strong enough to bound
distinct theta values:

```text
|Gamma cap M_s| <= n^{O(1)}
```

uniformly in `s`.

Try to derive a cap theorem:

```text
For above-reserve aperiodic Uhat, nonzero Fourier modes of the indicator of
Gamma cap M_s have cancellation sufficient to force polynomial support.
```

Check carefully:

1. Which group is being Fourier-expanded?
2. What is the exact nonzero-frequency phase?
3. How does aperiodicity enter the cancellation?
4. Does the bound control distinct theta or only weighted witnesses?
5. Does central-rate `s` defeat the estimate?

If the character-sum approach fails, give the exact obstruction: periodic
resonance, phase degeneracy, same-slope collision, loss from witness
multiplicity, or closure too weak.

Return `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`, or `PLAN`.

