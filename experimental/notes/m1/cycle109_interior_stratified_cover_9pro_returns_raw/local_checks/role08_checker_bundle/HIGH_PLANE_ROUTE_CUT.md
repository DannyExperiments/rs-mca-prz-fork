# Exact route cut: one separator on an affine plane is insufficient

Let `K` be any finite field and let the Gate-B parameter space be the affine
plane `P=K^2`. Let the exceptional layer be

```text
M = {(0,y): y in K}.
```

The degree-one polynomial `F(X,Y)=X` vanishes on `M` but not identically on
`P`. Thus the usual rank-escape/separator premise holds. Nevertheless the map

```text
z |-> (0,z)
```

injects all `|K|` slopes into `M`. Consequently a single nonzero separator on a
2-dimensional plane yields no `n^C` bound independent of `|K|`; the generic
finite-field zero bound is only `O(deg(F)|K|)`.

A valid HIGH certificate must therefore supply at least one additional
zero-dimensionality mechanism:

1. a curve equation `G=0` with no common component with `F`, giving a Bezout
   cap `deg(F) deg(G)`;
2. a second separator with zero-dimensional common zero set;
3. an injective reduction to a one-parameter slice on which the separator is
   nonzero; or
4. an exact finite image / separately proved symbolic cap.

This is why the reference checker emits `UNPAID_HIGH_PLANE` for a bare plane
rank-escape certificate.
