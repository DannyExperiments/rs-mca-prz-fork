# New theorem package: generated-field entropy floors and deep-point MCA conversion

Status: PROVED / NEW-LOCAL, intended for `experimental/experiments.tex`.

## Result 1: generated-field prefix list floor

For `K ⊆ F`, `D ⊂ K`, `|D| = n`, and `C = RS[F,D,k]`, at agreement

```text
a = k + sigma
```

there exists a `K`-valued received word with list size at least

```text
ceil( binom(n,a) / |K|^sigma ).
```

This makes the generated-field entropy floor explicit: any worst-case list theorem with list bound `L0` must have

```text
|K|^sigma >= binom(n,a) / L0.
```

At fixed rate, this is the reserve condition

```text
sigma log2 |K| >= H2(a/n) n - log2 L0 + lower-order terms.
```

For the prize rates, `H2(rho)` is:

```text
rho = 1/2   -> 1.000000
rho = 1/4   -> 0.811278
rho = 1/8   -> 0.543564
rho = 1/16  -> 0.337290
```

## Result 2: quotient-fiber prefix list floor

If `D` has a quotient map `x -> x^c` with fibers of size `c`, `N = n/c`, and `a = c m`, then the same entropy construction restricted to fiber-union supports gives list size at least

```text
ceil( binom(N,m) / |K|^(m - ceil(k/c)) ).
```

This is the clean quotient-core floor. It is not a BCHKS import; it is the elementary locator-entropy pigeonhole on periodic supports.

## Result 3: base-list floors embed into interleaved lists

Any base-code list of size `L` at agreement `a` gives a `mu`-row interleaved received word with common-support interleaved list size at least `L`, by using

```text
(U, 0, ..., 0)
```

and tuples `(P_i, 0, ..., 0)`.

Therefore interleaving cannot remove the generated-field or quotient-core list floors; it can only help after those floors are budgeted.

## Result 4: general deep-point list-to-MCA conversion

Let `C = RS[F,D,k]`, `C+ = RS[F,D,k+1]`, `q = |F|`, and `n < q`. If a word `U` has `L` distinct `C+` codewords agreeing with it on at least `a > k` points, then there is `alpha in F \ D` such that the line

```text
f_alpha(x) = U(x)/(x-alpha)
g_alpha(x) = -1/(x-alpha)
```

has at least

```text
L / (1 + k(L-1)/(q-n))
```

distinct support-wise noncontained bad slopes at agreement `a`. Hence

```text
epsilon_mca(C, 1-a/n)
  >= L(q-n) / ( q (q-n + k(L-1)) ).
```

This generalizes the earlier cap-style dependency split: it works for any sufficiently large augmented-code list, not only quotient-locator packets.

## Result 5: generated-field entropy MCA floor

Combining Results 1 and 4, for `a >= k+1`, define

```text
L_ent_plus(a) = ceil( binom(n,a) / |K|^(a-k-1) ).
```

Then

```text
epsilon_mca(C, 1-a/n)
  >= L_ent_plus(a)(q-n) / ( q (q-n + k(L_ent_plus(a)-1)) ).
```

With quotient fibers and `a = c m`, one may replace `L_ent_plus` by

```text
L_quot_plus(a,c)
  = ceil( binom(n/c,m) / |K|^(m - ceil((k+1)/c)) ).
```

These are mandatory lower floors for any positive MCA threshold theorem.

## Result 6: subfield confinement for base-valued lines

If `K ⊆ F`, `D ⊂ K`, and `f,g:D -> K`, then any support-wise noncontained bad slope at agreement at least `k` lies in `K`. Slopes in `F \ K` force simultaneous explanation of `f` and `g` on the same support.

This means extension-field MCA witnesses must use genuinely `F`-valued line endpoints. Searching only among `K`-valued lines cannot prove extension-field bad-slope density over `F`.

## Result 7: strict264 quotient-floor obstruction over `F_17^32`

For the concrete row

```text
F = F_{17^32}
|H| = 512
C = RS[F,H,256]
a = 264
```

the quotient map `x -> x^8` on the cyclic subgroup `H` has fibers of size `8` and image size `64`.  The augmented code

```text
C+ = RS[F,H,257]
```

has a quotient-fiber list of size

```text
L = binom(64,33)
```

at agreement `264`, with no generated-field denominator, because

```text
33 - ceil(257/8) = 0.
```

The deep-point conversion therefore gives at least

```text
L / (1 + 256(L-1)/(17^32 - 512))
```

distinct support-wise MCA-bad slopes for `C` at agreement `264`.  Since

```text
L > 16,
256(L-1) < 2^72 < 17^32 - 512,
```

this is greater than `8`, hence at least `9` slopes.  And since

```text
7 * 2^128 > 17^32,
```

even seven slopes beat the prize budget.  Thus

```text
epsilon_mca(RS[F_17^32,H,256], 31/64) > 2^-128.
```

This is a quotient-core proof of strict264.  It does not pin the full threshold; the next prize-shaped target is still the agreement-265 upper bound.

## Immediate agent tasks

1. Add scripts computing `L_ent_plus(a)` and `L_quot_plus(a,c)` for candidate prize rows.
2. Compare the exact MCA floor

```text
L(q-n) / ( q (q-n + k(L-1)) )
```

against `2^-128` before attempting a positive theorem.
3. Treat rows where the floor exceeds `2^-128` as lower-bound/certificate targets, not positive-theorem targets.
4. Once all floors are below budget, focus on the remaining aperiodic residue-line local-limit theorem.
