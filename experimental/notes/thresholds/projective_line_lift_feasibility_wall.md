# Projective-line lift feasibility wall for the deployed Grand List row

**Status:** PROVED route cut / exact new wall.

This note does **not** prove the deployed Grand List inequality. It proves the
narrower theorem package that survives hostile audit:

1. every integer scalar nested-MacWilliams profile through `T+1` is feasible;
2. the first `K+2` support shadow cuts the old scalar endpoint by an exact
   deployed amount, but remains far above `T`;
3. a `2^61` support model survives all pairwise and `K+2`-local line laws; and
4. literal GRS realization is equivalent to one global binary projective-line
   lift. That global projective-hyperplane lift is open.

The accompanying verifier is
`experimental/scripts/verify_projective_line_lift_feasibility_wall.py`.
It uses only the Python standard library and contains no `assert` statements,
so optimization cannot erase any check.

## Source anchors and scope

The live base audited for publication is
`origin/main@ea4eb0784417ca5ab503a3c31a7eef6464ad100a`. The remote `main`
head and this worktree base were equal at the audit time.

The R13 source packet is role `04_INTEGRAL_EXTENSION_ENUMERATOR` in
`RS_MCA_NIGHTSHIFT_9PRO_20260713_R13`. Its relevant anchors are:

- `CURRENT_BOARD.md` and `ROLE_PROMPT.md` for the literal one-row target;
- `source/R12_ROLE_01_FINAL_RESPONSE.txt` for the preceding continuous
  scalar route cut;
- `source/experimental/notes/l2/affine_interleaved_shell_compression.md`
  for the pending all-arity compiler and the exact value of `T`;
- `source/experimental/notes/l2/affine_section_one_row_rank_reduction.md`
  for the separate pending affine-rank routing theorem; and
- `returns_raw/pro_safari/ROLE_04_20260713T042718Z_final_response.md` for the
  preserved discovery return.

The preserved Pro verdict is provenance, not proof authority. The proofs below
stand on their own, and the verifier recomputes all displayed deployed
arithmetic independently.

## Exact ledgers

### Parameter and field ledger

The deployed one-row parameters are

```text
p     = 2^31 - 2^24 + 1 = 2,130,706,433,
n     = 2^21            = 2,097,152,
K     = 2^20            = 1,048,576,
m     = 1,116,047       = K + sigma,
sigma = 67,471,
n-m   = 981,105,
T     = 274,854,110,496,187,592.
```

The verifier proves `p` prime by deterministic trial division and checks

```text
(p-1)/n = 1,016.
```

Thus the cyclic evaluation set of size `n` exists in `F_p^*`. The arguments
below need only `n` distinct evaluation points, so they also apply to any
deployed GRS evaluation set with those parameters.

The base field and list field are both `F_p`. The challenge denominator used
by the pending all-arity compiler remains `p^6`; it is not replaced by `p`.
Indeed,

```text
B* = floor(p^6/2^128) = 274,980,728,111,395,087,
p-n+m                 = 2,129,725,328,
T  = floor(((B*+1)(p-n+m)-1)/p)
   = 274,854,110,496,187,592.
```

No extension-field payment or field substitution occurs in this note.

### GRS and weight normalization

Let `H subset F_p` have size `n`, and let every `v_x` be nonzero. Write

```text
C = GRS_K(H,v)
  = {(v_x f(x))_{x in H} : f in F_p[X], deg(f)<K}.
```

Dividing coordinate `x` by `v_x` is a monomial isometry from `C` to the
unweighted RS code. It preserves equality coordinates and Hamming weights.
Consequently the unweighted proof below applies verbatim to weighted GRS:
the degree-`K` received word `x^K` becomes `(v_x x^K)_{x in H}`.

For a coset agreement enumerator `z_j`, put

```text
A_w = z_{n-w}.
```

Thus `A_w` is the number of coset words of Hamming weight `w`, and the closed
agreement tail is

```text
sum_{w<=n-m} A_w = sum_{j>=m} z_j.
```

Use the `p`-ary Krawtchouk convention

```text
K_l(w) = sum_h (-1)^h (p-1)^(l-h)
                   binom(w,h) binom(n-w,l-h),
```

where out-of-range binomial coefficients vanish. Let `R_l` be the number of
projective weight-`l` points of `C^perp`, so a nonzero scalar orbit is counted
once. Since here `n=2K`, the dual is also an `[n,K]` MDS code and

```text
R_{K+s} = binom(n,K+s)
          sum_{h=0}^{s-1} (-1)^h binom(K+s-1,h) p^(s-1-h)
```

for `1<=s<=K`, while `R_l=0` for `1<=l<=K`.

### First-match ledger

First-match ownership is not present here. This is the base-field, one-row
Grand List object consumed after interleaved shell compression. It neither
charges nor modifies any Grand MCA catalogue, first-match cell, image
denominator, Sidon payment, ray compiler, or lower reserve.

## Theorem 1: scalar integrality survives through `T+1`

Put

```text
lambda = binom(n,K)/binom(m,K).
```

For an integer `t`, define

```text
Z_t(X) = sum_{u=0}^K binom(n,u) p^(K-u) (X-1)^u
         + t (X^m - sum_{u=0}^K binom(m,u)(X-1)^u),

z_j(t) = [X^j] Z_t(X),
A_w(t) = z_{n-w}(t).
```

**Claim.** For every integer

```text
0 <= t <= T+1,
```

the following hold.

1. `A_w(t)` is a nonnegative integer for every `w`,
   `sum_w A_w(t)=p^K`, and `A_0(t)=0`.
2. The closed tail is exactly

   ```text
   sum_{w<=n-m} A_w(t) = t.
   ```

3. For each `l>K`, there is an integer `N_l(t)` with

   ```text
   0 <= N_l(t) <= R_l
   ```

   such that

   ```text
   sum_w A_w(t) K_l(w) = p^K (p N_l(t)-R_l).
   ```

   The transform is zero for `1<=l<=K` and is `p^K` at `l=0`.
4. Consequently

   ```text
   W_E = W_C + (p-1) W_A(t),
   W_D = 1 + sum_{l>K} (p-1) N_l(t) Y^l
   ```

   are nonnegative integral formal weight enumerators satisfying the exact
   MacWilliams identities of a putative nested pair
   `C subset E`, `D=E^perp subset C^perp` of dimensions `K+1` and `K-1`.

In particular, `t=T+1` is a feasible integral scalar profile. Scalar
integrality, every scalar MacWilliams congruence, and every scalar shell range
constraint do not imply a tail at most `T`.

### Proof: agreement coefficients

At `t=0`, `Z_0` is realized exactly. After the weighted normalization, take
the received word `U_0(x)=x^K`. As `f` ranges over polynomials of degree less
than `K`, `U_0-f` ranges over all monic degree-`K` polynomials. Such a
polynomial has at most `K` roots in `H`, and exactly `p^(K-u)` monic
degree-`K` polynomials vanish on a fixed `u`-subset. This gives `Z_0` by
binomial inversion.

In the `(X-1)` basis the correction has no component through degree `K`, so

```text
sum_j binom(j,u) z_j(t) = binom(n,u) p^(K-u),  0<=u<=K.
```

Also `[X^m]Z_t=t`, every coefficient strictly between `K` and `m` is zero,
and

```text
z_K(t) = binom(n,K)-t binom(m,K).
```

It remains to prove coefficientwise nonnegativity. Evaluate at the rational
endpoint `lambda`. For `0<=j<=K`, set

```text
r = K-j,       N_j=n-j,       M_j=m-j=sigma+r.
```

Coefficient extraction and the partial alternating-binomial identity give

```text
z_j(lambda)/binom(n,j)
  = sum_{v=0}^{r-1} (-1)^v binom(N_j,v) p^(r-v)
    + (-1)^r binom(N_j,r) r/M_j.                    (1)
```

For `r=0` the right side is zero. For `r>=1`, consecutive absolute terms in
the prefix have ratio at most `n/p<1`. Hence the prefix is at least

```text
p^r(1-n/p).
```

If `r` is even, the final term in (1) is nonnegative. If `r` is odd, its
absolute value is at most

```text
N_j^r <= p^r(n/p)^r <= p^r(n/p) < p^r(1-n/p),
```

where the final strict inequality uses `2n<p`. Thus `z_j(lambda)>=0`.
The coefficient at `m` is `lambda`; all other coefficients above `K` vanish.
Since `Z_t` is the affine interpolation of `Z_0` and `Z_lambda`, it is
coefficientwise nonnegative for `0<=t<=lambda`, and it is integral for integer
`t`.

Finally, every factor in

```text
lambda = product_{i=0}^{K-1} (n-i)/(m-i)
```

is greater than `3/2`: the factors increase with `i`, and the first-factor
gate is `K>3 sigma`, with

```text
K-3 sigma = 846,163.
```

Therefore

```text
floor(lambda) >= floor((3/2)^100)
              = 406,561,177,535,215,237
              = T + 131,707,067,039,027,645.
```

This includes every requested integer `t` through `T+1`.

### Proof: Krawtchouk transform and integrality

Let

```text
B_l(t) = sum_w A_w(t) K_l(w).
```

The exact generating identity is

```text
sum_l B_l(t)Y^l
  = (1-Y)^n Z_t((1+(p-1)Y)/(1-Y))
  = p^K sum_{u=0}^K binom(n,u)Y^u(1-Y)^(n-u)
    + t sum_{u=K+1}^m binom(m,u)p^uY^u(1-Y)^(n-u).  (2)
```

This proves `B_0=p^K` and `B_l=0` for `1<=l<=K`. For `l>K`, put

```text
c_l = (-1)^(l-K) binom(n,l) binom(l-1,K),

q_l = sum_{u=K+1}^{min(m,l)}
        binom(m,u) p^(u-K-1) (-1)^(l-u) binom(n-u,l-u).
```

Both are integers, and (2) gives

```text
B_l(t)/p^K = c_l + p t q_l.                         (3)
```

At `t=0`, the coset is actual. If `N_l(0)` counts projective weight-`l`
dual points orthogonal to `U_0`, summing a nontrivial additive character over
each nonzero scalar orbit gives

```text
c_l = p N_l(0)-R_l.
```

Define

```text
N_l(t) = N_l(0)+t q_l.                               (4)
```

Equations (3)-(4) prove every divisibility and congruence, including

```text
B_l(t)/p^K == -R_l (mod p).
```

Thus the missing issue is only the interval `0<=N_l(t)<=R_l`.

### Proof: all scalar shell ranges

Because (4) is affine, it is enough to check `t=0` and `t=lambda`. The first
endpoint is actual. At the second, write `l=K+s`, `1<=s<=K`, and define

```text
b_s = B_{K+s}(lambda)/(p^K binom(n,K+s)),
D_s = R_{K+s}/binom(n,K+s).
```

The desired projective interval is

```text
-D_s <= b_s <= (p-1)D_s.                             (5)
```

Writing `(a)_v=a(a-1)...(a-v+1)`, direct simplification of (3) gives

```text
b_s = (-1)^s binom(K+s-1,s-1)
      + sum_{v=1}^{min(s,sigma)}
          (-1)^(s-v) p^v (sigma)_v/(K)_v
          binom(K+s,s-v).                             (6)
```

Set

```text
rho = sigma/K,       x = nK/(p sigma),       y=n/p.
```

For `v=s-r`, an absolute summand in (6) is at most

```text
(p rho)^s x^r/r!,
```

and the initial term is at most `n^(s-1)`. Since `0<x<1`,

```text
|b_s|/p^s <= rho^s/(1-x) + y^(s-1)/p.                 (7)
```

The alternating terms defining `D_s` decrease, so

```text
D_s/p^(s-1) >= 1-y.                                   (8)
```

For the upper endpoint in (5), (7)-(8) reduce to the exact positive gap

```text
g_plus = (1-1/p)(1-y) - (rho/(1-x)+1/p)
       = 629197861639644034270808063071854583327
         / 673896871014088741031154346685050650624
       > 0.                                            (9)
```

For `1<=s<=7`, every term of (6) after the first is more than `100` times
its predecessor in absolute value, and the final term is positive. The exact
sufficient gates are

```text
p sigma - 100K(K+9)       = 33,808,787,244,943 > 0,
p(sigma-8) - 100K(K+9)    = 33,791,741,593,479 > 0.
```

Hence `b_s>0` in those shells. For `s>=8`, (7)-(8) reduce the lower endpoint
in (5) to

```text
g_minus = (1-y) - (p rho^8/(1-x)+y^7)
        = 14980060041633554401788097188418356598094456587298273461558641437112289293525930573440576326435256327699206799425444516551221233
          / 41248761974934491830107366569484286197063703498391909062631935376216209552254878164750035783418216201653194750176047587269804032
        > 0.                                           (10)
```

This proves (5), hence `0<=N_l(lambda)<=R_l`. Affine interpolation proves the
range for every `0<=t<=T+1`, completing Theorem 1.

## Theorem 2: the exact `K+2` shadow cut

For an actual received word `U`, let

```text
L_m(U) = #{c in C : |{x:c(x)=U(x)}|>=m}.
```

Choose one `m`-subset `B_c` of the agreement set of each listed codeword.
For distinct `c,c'`,

```text
|B_c intersect B_c'| <= K-1,                           (11)
```

because `K` common points would force the two degree-less-than-`K`
polynomials to coincide.

For an `m`-block `B`, define its `K+2` shadow neighborhood

```text
N_2(B) = {S subset H : |S|=K+2 and |S intersect B|>=K+1}.
```

Its size is

```text
|N_2(B)| = binom(m,K+2)+(n-m)binom(m,K+1).              (12)
```

The neighborhoods of distinct blocks are disjoint: two `K+1` facets of one
`K+2` set meet in at least `K` points, contradicting (11). Therefore every
actual list obeys

```text
L_m(U) <= U_2
       := floor(binom(n,K+2)
                /(binom(m,K+2)+(n-m)binom(m,K+1))).      (13)
```

Relative to `lambda`, exact cancellation gives

```text
U_2 = floor(r_2 lambda),

r_2 = K(K-1)/(sigma((sigma-1)+(K+2)(K-sigma)))
    = 4,581,294,080 / 289,215,899,480,839.               (14)
```

If `L=floor(lambda)` is the old scalar endpoint, then

```text
L-U_2 >= floor((1-r_2)(3/2)^100)
      = 406,554,737,445,582,740.                         (15)
```

This is a genuine support/joint-enumerator cut. It is nowhere near the
deployed target. In the other direction,

```text
U_2 >= floor(r_2(3/2)^200)
    = 2,618,290,424,420,403,004,360,190,639,514
    > 2.618e30 >> T.                                    (16)
```

Thus the exact shadow cut excludes the R12 endpoint but does not prove the
one-row bound.

## Theorem 3: the first local complete atom is insufficient

For each `(K+1)`-set `Q subset H`, let `x_Q=1` when `U|_Q` is the restriction
of a degree-less-than-`K` GRS word. For each `(K+2)`-set `S`, put

```text
a_S = sum_{Q subset S, |Q|=K+1} x_Q.
```

Every actual GRS extension satisfies

```text
a_S in {0,1,K+2}.                                       (17)
```

Indeed, if two facets are selected, their two interpolants agree on their
`K`-point intersection, hence are the same polynomial; that polynomial agrees
with `U` on all of `S`, so every facet is selected.

The dual interpretation is exact. The shortened dual space

```text
V_S = {y in C^perp : supp(y) subset S}
```

has dimension two by MDS shortening. Its projectivization is a line with
`p+1` points: one minimum-weight point on each of the `K+2` facets and

```text
p-K-1 = 2,129,657,856
```

full-support points. A hyperplane meets this line in one point or the whole
line, which is precisely (17).

Nevertheless, all these local laws admit more than `T` formal blocks. Let
`B` be the binary direct sum of

```text
three [2^18-1,18,2^17]_2 simplex codes,
one 1,055-fold coordinate repetition of [2^7-1,7,2^6]_2,
60,691 zero coordinates.
```

Then

```text
B is a [981,105,61,67,520]_2 code,
|B| = 2^61 = 2,305,843,009,213,693,952 > T.              (18)
```

The length identity is

```text
3(2^18-1)+1,055(2^7-1)+60,691 = 981,105.
```

Choose `981,105` disjoint coordinate pairs in `H`, possible because

```text
2(981,105)=1,962,210<n.
```

For `z in B`, choose one coordinate from each pair according to the
corresponding bit and call the resulting set `E_z`. Put `S_z=H\E_z`. Then
`|S_z|=m`. If `z!=z'` have binary distance `d`,

```text
|S_z intersect S_z'| = m-d <= m-67,520 = K-49 < K.       (19)
```

Select any `T+1` of these blocks. Set `x_Q=1` exactly when `Q` lies in one
selected block. The intersection bound makes every `a_S` equal to `0`, `1`,
or `K+2`. Each shortened-dual line can then be completed independently:

```text
a_S=0:    select one full-support point;
a_S=1:    select no full-support point;
a_S=K+2:  select all p-K-1 full-support points.
```

Each local line consequently contains exactly `1` or `p+1` selected points.
The resulting first two shell totals agree with the formal incidence counts

```text
N_{K+1}(t) = t binom(m,K+1),

N_{K+2}(t) = binom(n,K+2)
             + t[p binom(m,K+2)-(K-1)binom(m,K+1)].       (20)
```

This is a truncated support/dual-shell model, not a GRS hyperplane. It proves
that pairwise support packing, (17), every coordinate-shortened `K+2` line,
and the first two nonzero dual shells remain insufficient.

## Theorem 4: global projective lines characterize literal realization

Let

```text
V=C^perp,       P=P(V),       P_l={P in P:wt(P)=l}.
```

For integers `N_l`, the following are equivalent.

1. There is a nonzero coset `U+C` such that

   ```text
   N_l = #{P in P_l : <U,P>=0}.
   ```

2. There are binary variables `epsilon_P` and `eta_L` satisfying

   ```text
   sum_{P in L} epsilon_P = 1+p eta_L,   eta_L in {0,1},  (21)
   sum_{P in P_l} epsilon_P = N_l,                         (22)
   sum_l N_l = (p^(K-1)-1)/(p-1),                          (23)
   ```

   for every projective line `L subset P`.

### Proof

The pairing

```text
(F_p^n/C) x C^perp -> F_p,       (U+C,y) |-> <U,y>
```

is nondegenerate. A nonzero coset therefore defines a nonzero functional
`phi_U` on `V`; its kernel is a codimension-one subspace. On a two-dimensional
subspace `W`, either `W` lies in the kernel and all `p+1` projective points are
selected, or the restricted functional is nonzero and its kernel contributes
exactly one projective point. This proves necessity of (21)-(23).

Conversely, let `S={P:epsilon_P=1}`. Equation (23) makes `S` proper. It meets
every line. If a line contains two points of `S`, (21) forces the entire line
into `S`. Therefore

```text
W_S = {0} union {y!=0:[y] in S}
```

is closed under scaling and addition, hence is a vector subspace of `V`. Its
codimension cannot be at least two: two vectors independent modulo `W_S`
would span a projective line disjoint from `S`, contradicting (21). Thus
`W_S` is a hyperplane. Nondegeneracy supplies a nonzero coset `U+C` whose
functional kernel is `W_S`. This proves sufficiency.

If the shell sums in (22) equal the formal `N_l(t)` from Theorem 1, the actual
coset transform is

```text
B_l = p^K(pN_l(t)-R_l).
```

The Krawtchouk transform is invertible, so the actual coset distribution is
exactly `A_w(t)`. Hence a global line lift for `t=T+1` would construct a
literal received word with list size `T+1`; infeasibility of that lift would
be a genuine complete/joint-enumerator obstruction.

The criterion is code-general and is unaffected by weighted GRS multipliers.
The weights and supports are measured in the original coordinates, while the
nondegenerate pairing is taken with the literal weighted dual code.

## Exact ledger impact

The scalar branch is closed negatively:

```text
integral A_w,N_l + all scalar MacWilliams congruences
does not imply tail <= T.
```

The local support branch is also cut: the `K+2` shadow gives the exact ratio
and endpoint reduction in (14)-(15), but (16) and the `2^61` model prove that
this local information is much too weak.

The exact remaining Grand List object is global. For every nonzero functional
`phi in (C^perp)^*`, define

```text
N_l(phi) = #{P in P_l : phi(P)=0},
B_0(phi) = p^K,
B_l(phi) = 0                         for 1<=l<=K,
B_l(phi) = p^K(pN_l(phi)-R_l)        for l>K,
```

and invert the Krawtchouk transform to get `A_w(phi)`. The missing theorem is

```text
sum_{w<=981105} A_w(phi) <= 274854110496187592          (24)
```

for every `phi`.

Equivalently, optimize (24) over binary projective-point assignments satisfying
the line equations (21) and normalization (23). This is not a relaxation: its
feasible points are exactly projective hyperplanes of the literal dual GRS
code.

The first information absent from the truncated model is cross-support line
closure. Two selected dual points force every projective combination on their
line, including when the union of their supports has size greater than `K+2`.
Those global lines couple distant support and weight shells. A successful next
separator must use that global closure, a higher support/Terwilliger
enumerator detecting it, a GRS-specific divided-difference or Plucker
relation, or a valid orbit compression of the full line system.

If (24) is proved, the pending all-arity shell-compression theorem compiles it
with the literal `p^6` challenge denominator and closed endpoint. The separate
pending affine-section theorem remains an external routing input; no
affine-rank value is used or proved here.

## Explicit nonclaims

- No received word with `L_m(U)>T` is constructed.
- The formal profile at `T+1` is not claimed to have a global projective-line
  lift.
- The `2^61` block family is not a Reed--Solomon list, not a hyperplane of
  `C^perp`, and not a completion of the higher dual shells.
- The `K+2` shadow upper value is not claimed attainable.
- The first two dual shells are not claimed to determine a complete extension
  enumerator.
- Coordinate-shortened `K+2` lines are not claimed to replace all projective
  lines.
- No affine-rank list construction or bound is claimed.
- No deployed safe certificate, official Grand List radius, Grand MCA result,
  or prize solve is claimed.
- No stable paper TeX is changed.

## Replay

Run both modes:

```text
python3 experimental/scripts/verify_projective_line_lift_feasibility_wall.py
python3 -O experimental/scripts/verify_projective_line_lift_feasibility_wall.py
```

The verifier independently checks every displayed deployed integer and ratio,
the exact scalar endpoint inequalities, all `287` profiles of a complete small
scalar MacWilliams model, weighted-GRS normalization by exhaustive enumeration,
the binary support-code parameters, and the projective-line characterization
by exhaustive finite-projective toy cases.
