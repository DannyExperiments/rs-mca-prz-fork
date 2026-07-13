# Affine-section reduction for the deployed one-row list wall

## Status

`PROVED` under the hypotheses below.

This note gives a stateful affine-section bound for one-row Reed--Solomon
lists.  At the deployed Grand List parameters it proves that any list violating
the current base-field target has affine hull dimension at least `15`.

## Setup

Let `F` be a field, let `H subset F` contain `n` distinct points, and let

```text
C = RS[F,H,K].
```

For a received word `U:H -> F`, define

```text
L_s(U) = {P in F[X]_<K : |{x in H : P(x)=U(x)}|>=s}.
```

Let `A=P_0+V` be an affine `d`-flat in `F[X]_<K`.  Its universal agreement
count is

```text
z_U(A) = |{x in H : P(x)=U(x) for every P in A}|.
```

Assume `s>=K`.

## Stateful affine-section theorem

Define `F_{s,0}(z)=1`.  For `d>=1`, put

```text
D_s(u) = (s-u)^2 - (n-u)(K-1-u),

J_s(u) = floor((n-u)(s-K+1)/D_s(u))  if D_s(u)>0,
         +infinity                   otherwise,

G_{s,d}(u)
  = min(
      floor((n-u) F_{s,d-1}(u+1)/(s-u)),
      J_s(u)
    ),

F_{s,d}(z) = max_{z<=u<=K-d} G_{s,d}(u).
```

Then every affine `d`-flat `A` with `z_U(A)>=z` satisfies

```text
|L_s(U) intersect A| <= F_{s,d}(z).                       (1)
```

### Proof

Let `Z` be the actual universal agreement set of `A`, with `|Z|=u`.  Every
direction polynomial in `V` vanishes on `Z`, so division by
`prod_{x in Z}(X-x)` embeds `V` in the polynomials of degree `<K-u`.  Hence

```text
d<=K-u,              u<=K-d.                              (2)
```

Every listed polynomial has at least `s-u` agreements outside `Z`.  For
`x notin Z`, the slice

```text
A_x={P in A:P(x)=U(x)}
```

is empty or an affine `(d-1)`-flat whose universal agreement set contains
`Z union {x}`.  Induction and double counting give

```text
M(s-u) <= (n-u) F_{s,d-1}(u+1),                           (3)
```

where `M=|L_s(U) intersect A|`.

For the second bound, choose exactly `s-u` nonuniversal agreement points from
each listed polynomial.  Two selected sets meet in at most `K-1-u` points,
because the polynomial difference already vanishes on `Z`.  The usual
selected-support second-moment inequality gives, when `D_s(u)>0`,

```text
M <= floor((n-u)(s-K+1)/D_s(u)).                          (4)
```

Taking the better of (3) and (4), then maximizing over the unknown actual
`u` allowed by (2), proves (1).

The theorem is field-uniform.  It applies over both a base field and an
extension field; no extension-degree factor appears in the recurrence.

## Exact deployed evaluation

Use

```text
p = 2,130,706,433,
n = 2,097,152,
K = 1,048,576,
m = 1,116,047.
```

The all-arity shell-compression theorem reduces the deployed sextic Grand List
safe candidate to the base one-row target

```text
L_p^*(m) <= T,
T = 274,854,110,496,187,592.                              (5)
```

The exact recurrence gives

```text
F_{m,14}(0) =  19,559,637,074,221,362,
F_{m,15}(0) = 284,377,931,860,724,492.                    (6)
```

Therefore

```text
T-F_{m,14}(0) = 255,294,473,421,966,230,
F_{m,15}(0)-T =   9,523,821,364,536,900.                  (7)
```

Any received word whose one-row list exceeds `T` has affine hull dimension at
least `15`: an affine hull of smaller dimension can be extended to a 14-flat
in the `K`-dimensional polynomial space and then bounded by (1) with `z=0`.
Equation (6) does not say that the dimension-15 upper bound is
attained.  It also does not control higher-dimensional lists by controlling
their 15-flat sections; a high-rank list may distribute mass across many such
sections.

## Forced high-rank certificate

If a violating list exists, choose 16 affinely independent listed polynomials
`P_0,...,P_15`, and choose an `m`-subset of the agreement set of each.  At each
evaluation point, connect the indices containing that point by a spanning
tree.  The resulting difference-evaluation matrix has at least

```text
16m-n = 15,759,600
```

rows and `15K=15,728,640` columns.  The vector formed by the 15 independent
polynomial differences lies in its kernel.  Thus the matrix rank is at most
`15K-1`, and the left-kernel dimension is at least

```text
15,759,600-(15,728,640-1) = 30,961.                       (8)
```

This is an exact diagnostic certificate emitted by every counterexample.  It
is not yet a rank contradiction: all but one of the displayed row dependencies
already follow from having more rows than columns.

## Ledger impact and nonclaims

The theorem removes every affine-rank-`<=14` candidate from the deployed
base-field one-row wall.  The exact remaining sector is

```text
affdim L_m(U) >= 15,
```

beginning with the dimension-15 recurrence gap in (7).

This note does not prove:

- the base one-row target (5);
- a bound on all high-affine-rank lists from their 15-flat sections;
- an adjacent safe certificate or the official Grand List theorem;
- any Grand MCA atlas or slope payment;
- that the upper value `F_{m,15}(0)` is realizable.
