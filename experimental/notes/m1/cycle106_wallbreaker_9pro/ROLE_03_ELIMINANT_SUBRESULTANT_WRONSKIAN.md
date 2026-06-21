# Role 03: Eliminant / Subresultant / Wronskian Route

Your role is to reduce the incidence wall to a smaller algebraic certificate.

Target a `k`-independent eliminant, subresultant, Wronskian, or rank statement
whose nonvanishing implies:

```text
|Gamma cap M_s| <= n^{O(1)}
```

uniformly in `s` and `k`.

You should work with:

```text
G(theta,X)=sum_{l=0}^{sigma+1} g_l(theta)X^l
```

and the condition:

```text
G(theta,X) == prod_{x in Sbar}(1-xX) mod X^(sigma+2)
```

for `|Sbar|=s`.

Concrete deliverables:

1. Define the exact eliminant/subresultant/Wronskian object.
2. State the exact nonvanishing or bounded-vanishing theorem needed.
3. Prove it if possible.
4. If not possible, give the smallest exact theorem/checker that would verify
   it.

Do not return a vague algebraic-geometry plan. The output must name the
polynomial, determinant, rank condition, or finite certificate explicitly.

Return `PROOF`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `ROUTE_CUT`, or `PLAN`.

