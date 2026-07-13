# Rank-15 hybrid recurrence and exact common-word Pade wall

## Status

`PROVED` for the field-uniform affine-section recurrence, the deployed
rank-15 reductions, and the common-word Pade/minimal-index identity stated
below.

This is a narrow Grand List contribution. It does **not** prove

```text
L_p^*(1,116,047) <= 274,854,110,496,187,592.
```

In particular, affine dimension at least `16` remains wholly unpaid. Every
displayed recurrence value above the target is a failed upper bound, not a
realized list and not a counterexample. No official endpoint or score moves.

## Deployed field and denominator ledger

The deployed row is

```text
B = F_p,                  p = 2^31-2^24+1 = 2,130,706,433,
F = F_(p^6),              [F:B] = 6,
H subset B^*,             |H| = n = 2^21 = 2,097,152,
K = 2^20 = 1,048,576,     m = 1,116,047,
sigma = m-K = 67,471,     n-m = 981,105.
```

The verifier checks that `p` is prime and that

```text
(p-1)/n = 1,016,
```

so a cyclic evaluation subgroup of order `n` exists in `B^*`. The extension
field is the ambient/list field in the sextic compiler; the one-row theorem
below is over the base/evaluation field `B`. The literal list denominator and
budget remain

```text
q_list = |F| = p^6
       = 93,571,093,019,388,561,295,270,373,781,649,880,353,786,165,192,103,559,169,

B* = floor(q_list/2^128) = 274,980,728,111,395,087.
```

The all-arity shell compression uses the base-field factor

```text
p-n+m = 2,129,725,328
```

and asks for the exact one-row ceiling

```text
T = floor(((B*+1)(p-n+m)-1)/p)
  = 274,854,110,496,187,592.                              (1)
```

No extension-field size is used to pay a base-field one-row deficit.

Everything below is unchanged for a weighted generalized Reed--Solomon code:
multiplication by the nonzero coordinate multipliers is an invertible diagonal
equivalence, and applying the inverse diagonal map to the received word
preserves agreement supports, list cardinalities, universal sets, and affine
dimensions.

## Source and overlap ledger

The publication base is `origin/main@c23dcaa0`.  That integration commit
contains PRs `#702`, `#703`, and `#719`--`#722`.

The exact source anchors in the R13 packet are:

```text
source/experimental/notes/l2/affine_interleaved_shell_compression.md
source/experimental/notes/l2/affine_section_one_row_rank_reduction.md
source/R12_ROLE_03_L2_DIM15_EQUALITY_BREAKER_RESPONSE.txt
source/R12_ROLE_09_OFFICIAL_ENDGAME_RESPONSE.txt
source/R12_ROLE_02_L2_HIGH_RANK_HYPERPLANES_RESPONSE.txt
```

Their ownership is retained literally:

- integrated `#702` supplies the all-arity shell compiler and target (1);
- integrated `#703` already excludes affine dimension at most `14` and supplies
  the raw actual-universal-state recurrence;
- integrated `#722` supplies a complementary locator-saturation normal form
  for the top two-flat sector; it does not own the hybrid recurrence or the
  Pade/minimal-index classification proved here;
- R12 Role 03 supplies the projective-direction two-flat bound;
- R12 Role 09 supplies the collision-class recurrence;
- R12 Role 02 supplies the primitive locator/gcd normalization, the existing
  `c>=153` exclusion, and the earlier `30,961+e` locator-kernel lower bound.

The new rank-15 step is the recursive composition of the Role 03 two-flat row
with the Role 09 collision operator. The `c>=153` conclusion is credited to
the prior Role 02 work; it is reproduced here so that the exact residual
ledger and verifier are self-contained. The Pade theorem strengthens the
prior kernel lower bound to an equality with an explicit nonnegative defect.

## Setup

Let `F` be any field, let `H subset F` consist of `n` distinct points, and let

```text
C = RS[F,H,k] = {ev_H(P): P in F[X]_<k}.
```

Fix `s>=k` and a received word `U:H -> F`, and write

```text
L_s(U) = {P in F[X]_<k : |{x in H:P(x)=U(x)}|>=s}.
```

For an exact affine `d`-flat `A=P_0+V`, define its actual universal-agreement
set and count by

```text
Z_U(A) = {x in H : P(x)=U(x) for every P in A},
u = |Z_U(A)|.
```

All state bounds below use this actual `u`, not merely a lower bound for it.

## Hybrid exact-state recurrence

Put

```text
N_u = n-u,                         a_u = s-u,
Delta_k(u) = a_u^2-N_u(k-1-u),

J_k(u) = floor(N_u(s-k+1)/Delta_k(u))  if Delta_k(u)>0,
         +infinity                      otherwise.
```

At dimension one define

```text
D_1(u) = min(floor(N_u/a_u), J_k(u)),
F_1(z) = max_{z<=v<=k-1} D_1(v).                         (2)
```

For the directional two-flat correction, set

```text
lambda_u = k-u-1,                  q_u = F_1(u+1),
B_j(M) = floor(M floor((M-1)/(j-1))/j),

Cap_u(M) = N_u + sum_{j=2}^{q_u} min(N_u,lambda_u B_j(M)).  (3)
```

Let the raw two-flat state bound be

```text
G_2(u) = min(floor(N_u F_1(u+1)/a_u), J_k(u)),
```

and define

```text
H_2(u) = max{M in Z : 0<=M<=G_2(u), M a_u<=Cap_u(M)}.     (4)
```

For the collision operator in dimension `d>=2`, let

```text
r = d-1,                   h = k-u-1,
c_max = k-u-d+1,           g(c) = D_(d-1)(u+c).
```

For

```text
1<=t<=min(c_max,floor(h/r))
```

put

```text
R_t = max_{1<=c<=t} g(c),

Lambda_t = max_{t<c<=c_max} c(g(c)-R_t)_+/(c-t),          (5)
```

with `Lambda_t=0` when the range is empty, and set

```text
P_d(u) = floor(
  max_t {N_u R_t+(h-rt)Lambda_t}/a_u
).                                                        (6)
```

Also put

```text
R_* = max_{1<=c<=c_max} g(c),
R_0 = max_{1<=c<=min(c_max,floor(h/r))} g(c),

Q_d(u) = floor((h R_*+(N_u-h)R_0)/a_u).                  (7)
```

The hybrid exact-state rows are

```text
D_2(u) = min(H_2(u),P_2(u),Q_2(u),J_k(u)),

D_d(u) = min(P_d(u),Q_d(u),J_k(u))       for d>=3,        (8)
```

where an infinite `J_k(u)` is simply omitted. In (8), `D_2=H_2`: choosing
`t=h=c_max` shows `P_2` is no smaller than the raw incidence bound, while
`Q_2` equals that bound, and `H_2` already includes `J_k`.

### Theorem 1: hybrid affine-section bound

For every field `F`, every set `H` of `n` distinct points, every `s>=k`, every
received word `U`, every `1<=d<=k`, and every exact affine `d`-flat `A` with
actual universal count `u`,

```text
|L_s(U) intersect A| <= D_d(u).                           (9)
```

The theorem is field-uniform and introduces no extension-degree factor.

### Proof

For `x notin Z_U(A)`, the agreement slice

```text
A_x = {P in A:P(x)=U(x)}
```

is empty or an affine hyperplane of `A`. Group the nonempty slices by
equality. Write the distinct occupied hyperplanes as `A_i`, and let `c_i` be
the number of coordinates inducing `A_i`.

The actual universal set of `A_i` is exactly its `c_i` coordinates together
with `Z_U(A)`. Inclusion in one direction is immediate. Conversely, if an
additional nonuniversal coordinate were universal on `A_i`, then `A_i` would
be contained in the occupied hyperplane induced by that coordinate. Two
affine hyperplanes of the same affine flat cannot be properly nested, so the
two slices would be equal. Induction therefore gives

```text
|L_s(U) intersect A_i| <= D_(d-1)(u+c_i).                (10)
```

Take any `j<=d-1` classes. Their evaluation normals have rank at most `j`, so
their common direction space has dimension at least `d-j`. Divide by the
universal locator

```text
L_Z(X) = product_{z in Z_U(A)} (X-z).
```

The resulting polynomial subspace lies in `F[X]_{<k-u}` and vanishes on the
union of the selected classes. A `q`-dimensional subspace of
`F[X]_{<k'}` has at most `k'-q` common roots. Hence, after sorting
`c_1>=c_2>=...`,

```text
c_1<=c_max,                  c_1+...+c_(d-1)<=h.          (11)
```

If `M_A=|L_s(U) intersect A|`, agreement-incidence counting and (10) give

```text
M_A a_u <= sum_i c_i g(c_i).                              (12)
```

The assertion is trivial when `M_A=0`. Otherwise there are at least `d`
occupied classes: if there were at most `d-1`, (11) would bound their total
coordinate weight by `h`, whereas every listed point needs
`a_u=h+(s-k+1)>h` nonuniversal agreements. Thus `c_(d-1)` exists.

Set `t=c_(d-1)`. Every tail class has size at most `t` and contributes at
most `c_i R_t`. For a top class with `c_i>t`, definition (5) gives

```text
c_i(g(c_i)-R_t) <= (c_i-t)Lambda_t.
```

Equation (11) gives

```text
sum_{i=1}^{d-1}(c_i-t) <= h-(d-1)t.
```

Using `N_u` as an upper bound for total occupied coordinate weight in (12)
proves (6). Independently, the top `d-1` classes have total weight at most
`h`, while each tail class has size at most `floor(h/(d-1))`; charging the
top weight at `R_*` and the remaining weight at `R_0` proves (7). The
selected-support second-moment argument gives `J_k(u)`. Taking the minimum
proves (8) for `d>=3`.

For `d=2`, divide a direction basis by `L_Z` and call the resulting
polynomials `R_1,R_2`. The normal direction at an active coordinate is

```text
[R_1(x):R_2(x)] in P^1(F).
```

A fixed direction occurs at no more than `lambda_u=k-u-1` coordinates,
because those coordinates are roots of a nonzero linear combination of
`R_1,R_2`. For each `j`, choose one `j`-rich listed line in every direction
that supports one. Distinct directions through a listed point have disjoint
sets of other listed points, so at most `floor((M_A-1)/(j-1))` chosen lines
pass through it. Double counting gives at most `B_j(M_A)` such directions.
Integer layer cake now gives

```text
M_A a_u <= Cap_u(M_A),
```

which proves (4). This closes the induction and proves (9).

## Exact deployed rank-15 scan

Call a state *recurrence-unsafe* when its proved upper bound exceeds `T`.
The raw `#703` dimension-15 row is recurrence-unsafe exactly on

```text
1,040,879 <= u <= 1,043,582              (2,704 states).
```

The hybrid recurrence (2)--(8) is recurrence-unsafe exactly on

```text
1,042,375 <= u <= 1,043,582              (1,208 states). (13)
```

The transition and endpoint values are

```text
D_15(1,042,373) = 274,848,095,090,415,020 < T,
D_15(1,042,374) = 274,851,640,267,880,631 < T,
D_15(1,042,375) = 274,858,628,070,449,169 > T,
D_15(1,042,376) = 274,869,098,154,375,130 > T,
D_15(1,043,582) = 283,039,300,733,528,044 > T.           (14)
```

Thus the first unpaid hybrid inequality is

```text
274,858,628,070,449,169 <= 274,854,110,496,187,592,
```

which fails as an upper-bound certificate by `4,517,574,261,577`.

## Primitive degree deficit

Let `A=P_0+V` be an exact affine 15-flat in the deployed base-field code, let
`Z=Z_U(A)`, and let `u=|Z|`. Divide every direction by `L_Z`, and then by the
monic gcd of the quotient direction space. Denote the resulting primitive
15-dimensional space by `W` and put

```text
k_A = 1+max_{0!=w in W} deg(w),
c = (K-u)-k_A.                                             (15)
```

### Theorem 2: primitive normalization and exact deficit cut

The listed points in `A` inject into a normalized affine 15-flat list with
parameters

```text
(n-u, k_A, m-u).
```

Equivalently, its recurrence is the deployed recurrence at state `u` with
effective ceiling `K-c`. For every integer `c>=0` and every valid exact state
`0<=u<=K-c-15`, the following deployed consequences hold:

```text
c>=153  =>  D_15^(c)(u) <= 274,820,133,549,158,646
                             = T-33,976,947,028,946;       (16)

c=152   =>  D_15^(152)(u)>T exactly for
             u in {1,043,403,1,043,404,1,043,405,1,043,406}.
```

The four `c=152` values are

```text
u=1,043,403: 274,854,274,902,114,747 = T+164,405,927,155,
u=1,043,404: 274,857,797,694,413,816,
u=1,043,405: 274,861,320,583,703,395,
u=1,043,406: 274,864,843,569,987,490.                    (17)
```

Every putative rank-15 violation therefore lies in exactly one of

```text
c<=151 and 1,042,375<=u<=1,043,582,

c=152 and 1,043,403<=u<=1,043,406.                       (18)
```

### Proof

Every direction vanishes on `Z`, so division by `L_Z` is exact. At a root of
the residual gcd outside `Z`, every point of `A` has the same value. That
value cannot equal `U(x)`, since otherwise `x` would already lie in the
actual universal set. Removing the gcd therefore loses no nonuniversal
agreement. This proves the normalized injection.

Substitution of `k_A=K-u-c` gives the shift identity

```text
D_15(n-u,K-u-c,m-u;0) = D_15(n,K-c,m;u).
```

Exact evaluation gives (16)--(17). A smaller polynomial ceiling cannot
increase any term of the valid affine-section bound, so the `c=153` maximum
also excludes every `c>153`. This is the previously identified Role 02 cut,
now replayed with the hybrid child recurrence.

## Second-pivot slicing and alternant defects

Choose a row-echelon basis `w_1,...,w_15` of `W` with distinct leading
degrees

```text
0<=e_1<...<e_15=k_A-1.
```

Define the alternant defect

```text
delta(W) = sum_i e_i - binom(15,2) = sum_i e_i-105.       (19)
```

Fixing the coefficient of `w_15` partitions the affine 15-flat into at most
`p` affine 14-flat fibers parallel to `span(w_1,...,w_14)`. These fibers have
polynomial ceiling `e_14+1` on the normalized domain.

Across all 1,208 states in (13), a ceiling of `4,986` gives the exact uniform
rank-14 bound

```text
15,703,201,

p * 15,703,201 = 33,458,911,389,392,033 < T.             (20)
```

Hence every surviving rank-15 violation has

```text
e_14>=4,986,             e_15>=4,987,
delta(W)>=78+4,986+4,987-105=9,946.                      (21)
```

For the four `c=152` states, a ceiling of `5,010` gives the uniform bound

```text
45,706,459,

p * 45,706,459 = 97,387,046,220,950,747 < T.             (22)
```

The product in (22) is the repaired value; `97,386,551,033,218,347` is
incorrect. Thus `e_14>=5,010` in this sector. Here

```text
e_15=K-u-153>=5,017,
delta(W)>=78+5,010+5,017-105=10,000.                     (23)
```

At the endpoint `u=1,043,582`, the prior primitive saturation result gives
`e_15=4,993`. Equations (20)--(21) sharpen the penultimate pivot to

```text
4,986<=e_14<=4,992,
delta(W)>=78+4,986+4,993-105=9,952.                      (24)
```

The `78` in (21), (23), and (24) is the minimum sum `0+1+...+12` of the
first thirteen distinct nonnegative pivots.

## Exact common-word Pade identity

The next theorem is independent of the rank-15 recurrence and applies to any
selected 16-tuple.

Choose distinct `P_0,...,P_15 in L_m(U)`. For each `i`, choose exactly `m`
agreement coordinates `S_i`, and put

```text
E_i = H\S_i,                 |E_i|=n-m,
e = |intersection_i E_i|.
```

Let

```text
G_H(X) = product_{x in H}(X-x),
A_i(X) = product_{x in S_i}(X-x),
Lambda_i(X) = G_H(X)/A_i(X) = product_{x in E_i}(X-x).
```

Let `U_tilde` be the degree-`<n` interpolation polynomial of `U`, and define

```text
Q_i(X) = (U_tilde(X)-P_i(X))/A_i(X).
```

Then

```text
deg Lambda_i = n-m = 981,105,       deg Q_i<n-m.
```

### Theorem 3: bounded kernel and minimal-index decomposition

For every tuple `R_i in F[X]_{<sigma}`,

```text
sum_i Lambda_i R_i=0
```

implies simultaneously

```text
sum_i Q_i R_i=0,             sum_i Lambda_i P_i R_i=0.   (25)
```

Thus the bounded locator kernel is exactly the degree-`<sigma` right-syzygy
space of the full-row-rank matrix

```text
M_Pade(X) = [ Lambda_0 ... Lambda_15 ]
            [ Q_0      ... Q_15      ].                  (26)
```

Its minors have the literal common-received-word form

```text
Delta_ij
  = Lambda_i Q_j-Lambda_j Q_i
  = G_H(P_i-P_j)/(A_i A_j).                              (27)
```

Writing

```text
C_ij = product_{x in S_i intersect S_j}(X-x),
E_ij = product_{x in E_i intersect E_j}(X-x),
```

equation (27) means the polynomial identity

```text
Delta_ij = E_ij (P_i-P_j)/C_ij.                          (28)
```

In particular, every minor is divisible by the common-error locator, and

```text
deg Delta_ij <= D = n+K-2m-1 = 913,633.                  (29)
```

Let `g_M` be the monic gcd of the nonzero minors, let

```text
d_M = max_{i<j, Delta_ij!=0} deg(Delta_ij/g_M),
```

and let `nu_1,...,nu_14` be the right minimal indices of `M_Pade`. Then

```text
sum_j nu_j = d_M,

dim ker(M_Pade:F[X]_{<sigma}^16 -> F[X]^2)
  = sum_j max(sigma-nu_j,0).                              (30)
```

Define

```text
eta = (D-e-d_M) + sum_j (nu_j-sigma)_+.                  (31)
```

Since `d_M<=D-e`, `eta>=0`, and (30) becomes the exact identity

```text
dim ker M_Pade = 14 sigma-D+e+eta
               = 30,961+e+eta.                          (32)
```

If

```text
Eval(E_i) = span{ev_x:x in E_i} subset (F[X]_{<n-K})^*,
```

then equivalently

```text
dim intersection_i Eval(E_i) = e+1+eta.                 (33)
```

The common-error evaluation span has dimension `e`, so its exact quotient
excess is

```text
1+eta.                                                    (34)
```

### Proof

The agreement condition gives

```text
U_tilde-P_i=A_i Q_i.
```

If `sum_i Lambda_i R_i=0`, then

```text
G_H sum_i Q_i R_i
  = sum_i Lambda_i(U_tilde-P_i)R_i
  = -sum_i Lambda_i P_i R_i.                             (35)
```

The right side has degree at most

```text
(n-m)+(K-1)+(sigma-1)=n-2.
```

It is divisible by the degree-`n` polynomial `G_H`, so both sides of (35)
are zero. This proves (25).

Direct substitution gives (27). The polynomial `P_i-P_j` vanishes on
`S_i intersect S_j`, so division by `C_ij` in (28) is exact. Formula (28)
also shows that `E_i intersect E_j`, hence `intersection_i E_i`, divides
every minor. This proves (29) and `d_M<=D-e`.

Because the `P_i` are distinct, at least one minor is nonzero, so (26) has
full row rank. The polynomial minimal-basis identity equates the degree of
the primitive maximal-minor vector with the sum of the fourteen right
minimal indices, giving `sum_j nu_j=d_M`. Predictable degree gives the unique
bounded-syzygy count in (30). Finally,

```text
sum_j max(sigma-nu_j,0)
  = 14 sigma-d_M+sum_j(nu_j-sigma)_+
  = 14 sigma-D+e+eta,
```

and

```text
14 sigma-D = 14*67,471-913,633 = 30,961.
```

The locator multiplication map has domain dimension `16 sigma` and codomain
dimension `n-K`. Its cokernel therefore has dimension

```text
(n-K)-16 sigma+(30,961+e+eta)=e+1+eta.
```

The standard dual-RS annihilator identity identifies this cokernel with the
intersection in (33). Since `e<n-K`, the `e` common moment-curve evaluations
are independent. Subtracting their span proves (34).

The two exact high-rank strata are therefore

```text
eta=0: d_M=D-e and every nu_j<=sigma;

eta>0: additional determinantal degree/gcd loss or some nu_j>sigma.
```

This is a classification, not a list-size bound.

## Finite ledger impact

Combining the owned theorem objects gives the following exact necessary
conditions for any violation of (1):

```text
affdim<=14: excluded by #703;

affdim=15:
  1,042,375<=u<=1,043,582,
  c<=152,
  e_14>=4,986,
  e_15>=4,987,
  delta(W)>=9,946;

c=152:
  u in {1,043,403,1,043,404,1,043,405,1,043,406},
  e_14>=5,010,
  delta(W)>=10,000;

u=1,043,582:
  e_15=4,993,
  4,986<=e_14<=4,992,
  delta(W)>=9,952;

affdim>=16:
  every selected 16-tuple has exact quotient excess 1+eta,
  but no uniform list-size bound follows yet.
```

## Nonclaims

This note does not claim any of the following:

- the one-row inequality (1), the sextic Grand List theorem, or an official
  safe endpoint;
- realizability of a recurrence extremizer or of any number above `T`;
- a counterexample to the desired upper bound;
- any bound for affine dimension at least `16`;
- that `eta=0` is impossible, or that `eta>0` by itself forces rank descent;
- the weighted two-flat ceiling `217` in the marginal effective-ceiling row;
- an adjacent safe/unsafe bracket, a Grand MCA payment, or a score change.

No stable TeX file is modified by this packet.

## Remaining wall

The first unpaid rank-15 recurrence inequality is (14) at `u=1,042,375`. The
smallest isolated deficit is the first `c=152` value in (17), which exceeds
`T` by `164,405,927,155`.

The sharp local next step is to lower the directional two-flat ceiling from
`218` to `217` for effective ceiling

```text
K' = K-152 = 1,048,424
```

on the plateau `1,043,552<=u<=1,043,774`. At its first state,

```text
N_u=1,053,600,   a_u=72,495,   lambda_u=4,871,   q_u=15,
218 a_u=15,803,910,             Cap_u(218)=15,804,000.
```

Only `90` incidences remain, but current pair packing and projective-direction
inequalities permit them. Paying that exact slack removes the four-state
`c=152` sector. The broader `c<=151` sector still needs a dependent-normal or
weighted higher-codimension payment.

For affine dimension at least `16`, the exact remaining task is to convert
either Pade stratum into a uniform count:

- in `eta>0`, turn the gcd/degree loss or large minimal index into a larger
  universal set, a common primitive factor, rank descent, or an integral
  nested-extension constraint;
- in `eta=0`, pay the full-degree rigid Pade system using literal GRS support
  geometry or an integral complete joint enumerator.

Until both the residual rank-15 sector and all `affdim>=16` lists are bounded
by `T`, the official Grand List endpoint remains open.

## Reproducibility

Run

```text
python3 experimental/scripts/verify_rank15_hybrid_recurrence_and_pade_wall.py
```

The standard-library verifier:

1. checks the prime/subgroup, sextic denominator, budget, and target;
2. rebuilds the raw `#703` recurrence and exact 2,704-state window;
3. evaluates the directional/collision hybrid with exact rational upper
   hulls and checks the optimized hull against a slow literal evaluator;
4. scans the original, `c=152`, and `c=153` rows;
5. regenerates every rank-14 second-pivot table entry and both products;
6. checks the defect floors and Pade dimension identities.

No floating-point comparison is load-bearing.
