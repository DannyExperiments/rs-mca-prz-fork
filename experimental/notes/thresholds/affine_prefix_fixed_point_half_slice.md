# Affine-prefix fixed-point half-slice

## Status

This note records the independently audited finite layer of R32 Role 10. It
isolates an exact fixed-point half of the `j=0` affine-prefix stratum, proves
that its locator family has common monic gcd exactly `X-p`, and records the
conditional owner-or-exponent inequality forced by any later paid partition.

It is not a semantic first-match theorem. It gives no finite-ledger,
asymptotic-ledger, recurrence, Grand MCA, Grand List, or official-score
payment. The official score remains `0/2`.

The source base is
`3404d21b64c876c6d9b995ad3e29d7120ab27a54`. The exact live dependency
heads used in the overlap gate are PR #888 at
`7b4bb19875b41a46f6a637c14b37a8506ce10bdb`, PR #903 at
`7a216f1617d2cde1f0e5e52d39379664c6522b10`, and PR #959 at
`19d72e12082dad1348d0469322727e0e4536accf`. The hostile-proof audit hash is
`5d80191c49a2d9915ed6ba56e884e8fa77dd81448efa6965784506939fd8ecb8`;
the distinct source/compiler audit hash is
`56d1c489d3421d072cb031f3c5054d8631bdea37e79bb4fdc9379e3d2acf046f`.

## Source family

For every integer `B >= 2`, use the characteristic-five row from PR #903:

```text
F_B = F_(5^(3B)),  n = 4B,  k = 2B-1,  m = 2B = k+1,
D_B = {a_i + eps*u_i + eta*v_i :
       1 <= i <= B and eps,eta in {0,1}},
```

where

```text
a_1,u_1,v_1,...,a_B,u_B,v_B
```

is an `F_5`-basis of `F_B`. Put `p=a_1`. For a support `S` of size `2B`,
write

```text
Q_S(X) = product_(x in S)(X-x)
       = X^(2B) + c_1(S) X^(2B-1) + ... .
```

In one four-point block, call a size-two local subset a diagonal when it is
one of

```text
{(0,0),(1,1)},  {(1,0),(0,1)}.
```

Let `U_B` be the family of all `2B`-supports for which no local size-two
slice is a diagonal. Let

```text
P_B = {S in U_B : p in S},
Q(y) = 1 + 4y + 4y^2 + 4y^3 + y^4,
c_B = [y^(2B)] Q(y)^B.
```

## Exact half-census and slope incidence

The local non-diagonal support counts are the coefficients of `Q`, so

```text
|U_B| = c_B.
```

Complementation inside `D_B` preserves support size `2B` and preserves the
non-diagonal rule: it exchanges the two forbidden diagonals and maps every
allowed edge to its opposite edge. It also exchanges membership and
nonmembership of `p`. Therefore

```text
|P_B| = c_B/2.                                      (1)
```

The local signature

```text
(local size, sum eps, sum eta) in F_5^3
```

is injective on the fourteen non-diagonal local subsets. Because the block
coordinates form an `F_5`-basis, equality of the global point sums forces
equality block by block. Hence

```text
S |-> c_1(S) = -sum_(x in S) x
```

is injective on `U_B`, and in particular on `P_B`.

For

```text
R_gamma(X) = X^(2B) + gamma X^(2B-1),
gamma = c_1(S),
h_S = R_gamma - Q_S,
```

the leading two coefficients cancel, so `deg h_S <= 2B-2 < k`. The explicit
factorization of `Q_S` shows that the complete agreement set of `h_S` with
`R_gamma` on `D_B` is exactly `S`. Since `|S|=k+1`, the usual degree-`k`
root argument gives the source's support-wise nontriviality condition. Thus
every support in `P_B` supplies exactly one distinct slope and one exact
nontrivial RS witness:

```text
slopes(P_B) = witnesses(P_B) = c_B/2,
image-normalized mean = 1.                           (2)
```

These are algebraically planted boundary-profile witnesses. Equations (1)
and (2) do not assign them to a semantic C1--C9 owner.

## Exact common divisor

Every locator in the fixed-point family is divisible by `X-p`. Conversely,
for every `x in D_B` with `x != p`, there is a support in `P_B` omitting
`x`: choose two points forming an allowed edge in every block, choose an edge
through `p` but not `x` in the first block when needed, and choose an edge
avoiding `x` in its own block otherwise. Since every locator is the displayed
product of its distinct linear factors, no point outside its support is a
root. Therefore the common monic gcd is exactly

```text
gcd_(S in P_B) Q_S(X) = X-p.                         (3)
```

Equation (3) is an exact planted-divisor statement, not a proof that the
family is a paid C3 cell. PR #888 explains why a common locator factor alone
does not supply the required semantic census or image-scale payment.

## Conditional retained-slope inequality

Let `E_B` be the set of slopes assigned to actual earlier semantic owners and
put

```text
e_B = |slopes(P_B) intersect E_B|.
```

Suppose the retained slopes are partitioned into `r_B` later cells, and each
cell is paid with loss `K_B` at its actual inherited `j=0` source mean. Since
that mean is one, each such cell contains at most `2 K_B` retained slopes.
Summing disjoint cells gives the exact conditional inequality

```text
2 K_B r_B >= c_B/2 - e_B.                            (4)
```

The central coefficient has raw exponential rate

```text
lim_(B->infinity) (1/(4B)) log c_B = (1/4) log 14.
```

Consequently, if `K_B` and `r_B` are subexponential in `n=4B`, then (4)
forces only

```text
0 <= c_B/2 - e_B <= exp(o(n)),
e_B >= c_B/2 - exp(o(n)).
```

This is an owner-or-exponent route cut. It is not an unconditional payment:
the source does not bound `e_B` or prove survival through earlier owners.

## Replay

Run

```bash
python3 experimental/scripts/verify_affine_prefix_fixed_point_half_slice.py
python3 -O experimental/scripts/verify_affine_prefix_fixed_point_half_slice.py
```

Both outputs must equal the checked-in expected transcript. The verifier
checks the pinned source files; proves the two field moduli irreducible;
reconstructs `F_(5^6)` and `F_(5^9)`; enumerates all `B=2,3` source supports;
checks the exact `50/25` and `568/284` full/fixed-point censuses; verifies
depth-one injectivity, degree cancellation, exact source-row zero sets,
support-wise nontriviality, and the family gcd `X-p`; and rejects eighteen
semantic mutations across the two cases.

## Nonclaims and remaining wall

This note does not prove:

- a semantic C1--C9 owner for the fixed-point family;
- survival through C1/C2 or any bound on `e_B`;
- an unconditional image-scale payment;
- a complete raw-witness or first-match atlas;
- a row-uniform theorem outside the displayed characteristic-five family;
- a finite or asymptotic ledger payment;
- Grand MCA hard input 2, a recurrence parent, or a Grand List theorem;
- any official-score movement.

The exact remaining wall is to classify and pay the earlier owners covering
all but at most `exp(o(n))` of the fixed-point slopes, or else to prove a
source-valid lower bound on the retained set and reconcile it with (4).
