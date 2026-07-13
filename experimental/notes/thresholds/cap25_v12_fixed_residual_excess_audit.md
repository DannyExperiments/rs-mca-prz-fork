# CAP25 v12 fixed residual excess sparse-sigma audit

Status: PROVED / AUDIT / EXACT_NEW_WALL.

This note records a fixed-layer extension of the sparse mutual layer audit in
`tex/towards-prize.tex`.  It uses the exact closed-ball Pade-Hankel formulation
from `experimental/notes/thresholds/cap25_v12_sparse_sigma_first_layer_audit.md`
and proves a q-free polynomial bound for every fixed residual excess layer.

This is not a proof of the Johnson-transfer hypothesis in `thm:transfer`.  It
does not improve a finite leaderboard row and it does not by itself complete
the CAP25 v12 cap machinery.  It pays every fixed layer above the sparse
half-distance wall and leaves the uniform-in-layer aggregation problem open.

## Setup

Let

```text
C = RS[F,D,k],   n = |D|,   m = n-k,   r = floor(delta n),
```

with `1 <= r <= m-1`.  We use the sparse mutual numerator
`sigma_C(delta)` from `towards-prize.tex`: the maximum number of finite
`delta`-MCA-bad slopes over sparse pairs `(epsilon_1,epsilon_2)` whose support
union has size at most `r`.

Set

```text
h = 2r - m - 1.
```

For a word `Y:D -> F`, write `Syn(Y)` for the Reed-Solomon syndrome and
`H_r(Syn(Y))` for the `(m-r) x (r+1)` closed-ball Hankel window.  For a sparse
pair, put

```text
H_i = H_r(Syn(epsilon_i)),   M(gamma) = H_1 + gamma H_2.
```

For `T subset D`, `|T|=r`, let

```text
L_T(X) = product_{x in T} (X-x),
```

and let `ell_T` be its coefficient vector in `F^{r+1}`.

The exact closed-ball formulation used below is:

```text
gamma is sparse delta-MCA-bad
iff there exists T subset D, |T|=r, such that

  (H_1 + gamma H_2) ell_T = 0,
  H_2 ell_T != 0.
```

The second condition is the same-support noncontainment condition.  It is
load-bearing.

## Theorem

With the setup above:

```text
h < 0  =>  sigma_C(delta) <= r.
```

If `h >= 0`, then

```text
sigma_C(delta)
  <= r + (m-r) + (h+2)(m-r) binom(n,h+2).
```

In particular, for every fixed `h`,

```text
sigma_C(delta) = O_h(n^(h+3)).
```

This extends the first residual layer `h=0` from the prior audit to every fixed
positive residual layer.  At `h=0` the bound has the same `O(n^3)` order as
the projective first-layer argument, though it is not optimized for constants.

## Proof

Fix a sparse pair and let

```text
E = supp(epsilon_1) union supp(epsilon_2),   e = |E| <= r,
v_gamma = epsilon_1 + gamma epsilon_2.
```

A slope is tangent if `v_gamma(x)=0` for some `x in E`.  There are at most
`e <= r` tangent slopes.

If `h<0`, then `2r <= m`, so `e <= r <= m-r`.  By `thm:sparse-threshold`, every
sparse MCA-bad slope is tangent.  Hence `sigma_C(delta) <= r`.

Assume now that `h>=0` and count non-tangent bad slopes.  If `e <= m-r`, the
same sparse-threshold theorem again gives no non-tangent bad slopes.  Thus any
non-tangent bad slope has `e >= m-r+1`.

For a word `w` supported on `B` and nonzero on every point of `B`, the Hankel
matrix factors as

```text
H_r(Syn(w)) = U_B diag(lambda_x w(x)) V_B^t,
```

where the rows of `U_B` are powers `0,...,m-r-1` and the rows of `V_B` are
powers `0,...,r`.  Since `D` has distinct points and `|B| <= r`, this gives

```text
rank H_r(Syn(w)) = min(|B|, m-r).
```

For a non-tangent slope, `v_gamma` is nonzero exactly on `E`; hence

```text
rank M(gamma) = m-r.
```

Therefore

```text
dim ker M(gamma) = (r+1) - (m-r) = h+2.
```

If there are no non-tangent bad slopes, we are done.  Otherwise choose one
non-tangent bad slope `gamma_0`.  Pick a nonzero `(m-r) x (m-r)` column minor
of `M(gamma_0)`, with determinant

```text
Delta(gamma).
```

Since entries of `M(gamma)` are affine in `gamma`,

```text
Delta not identically zero,   deg Delta <= m-r.
```

Thus slopes with `Delta(gamma)=0` contribute at most `m-r`.

On the open chart `Delta(gamma) != 0`, Cramer's rule gives `h+2` polynomial
kernel vectors

```text
Q_1(gamma), ..., Q_{h+2}(gamma) in F[X]_{<=r}
```

which form a basis of `ker M(gamma)`.  Each coefficient of each `Q_i` has
`gamma`-degree at most `m-r`.

For every subset `Y subset D`, `|Y|=h+2`, define the evaluation eliminant

```text
E_Y(gamma) = det( Q_i(gamma)(y) )_{y in Y, 1 <= i <= h+2}.
```

Then

```text
deg E_Y <= (h+2)(m-r).
```

Let `gamma_*` be a non-tangent bad slope with `Delta(gamma_*) != 0`.  By the
closed-ball formulation, choose `T subset D`, `|T|=r`, with

```text
M(gamma_*) ell_T = 0,   H_2 ell_T != 0.
```

Because `ell_T` lies in the Cramer-basis kernel and the locator `L_T` vanishes
on every point of `T`, the evaluation matrix

```text
( Q_i(gamma_*)(y) )_{y in T, 1 <= i <= h+2}
```

has rank less than `h+2`.  Hence

```text
E_Y(gamma_*) = 0
```

for every `Y subset T`, `|Y|=h+2`.

If some such `E_Y` is not identically zero, then `gamma_*` is charged to a root
of a nonzero polynomial of degree at most `(h+2)(m-r)`.  Summing over all
`binom(n,h+2)` possible `Y` gives at most

```text
(h+2)(m-r) binom(n,h+2)
```

non-tangent bad slopes in this branch.

It remains to rule out the all-eliminants-zero branch.  Suppose that, for a
bad witness `T`, all `E_Y` with `Y subset T`, `|Y|=h+2`, vanish identically.
Then, for every `gamma` with `Delta(gamma) != 0`, some nonzero kernel
polynomial of degree at most `r` vanishes on all `r` points of `T`.  Such a
polynomial is a scalar multiple of `L_T`.  Thus

```text
ell_T in ker M(gamma)
```

for every `gamma` with `Delta(gamma) != 0`.

Since `deg Delta <= m-r` and `D subset F` has size `n`, there are two distinct
field values outside the root set unless the total number of slopes is already
absorbed by the displayed bound.  Taking two such values `gamma_1 != gamma_2`
gives

```text
(H_1 + gamma_1 H_2) ell_T = 0,
(H_1 + gamma_2 H_2) ell_T = 0.
```

Subtracting yields

```text
H_2 ell_T = 0,
```

contradicting the noncontainment condition.  Therefore the
all-eliminants-zero branch contributes no sparse MCA-bad slope.

Combining the tangent slopes, the minor-root slopes, and the eliminant-root
slopes gives

```text
sigma_C(delta)
  <= r + (m-r) + (h+2)(m-r) binom(n,h+2).
```

This proves the theorem.

## Guardrail: the noncontainment gate cannot be dropped

The condition

```text
H_2 ell_T != 0
```

is not cosmetic.  Without it, common-extension locators can produce all-slope
kernel incidence that is not MCA-bad.

The moving-zero construction from the first-layer audit gives the model
example.  For `k>=2`, choose

```text
Pi(X) = product_{z in Z_*} (X-z),   |Z_*| = k-2,
epsilon_1(j) = j Pi(j),
epsilon_2(j) = -Pi(j)
```

on a sparse support.  Then

```text
epsilon_1 + gamma epsilon_2 = (X-gamma) Pi(X)
```

has a closed-ball kernel witness for many, and in higher layers potentially all,
slopes.  These witnesses are common extensions, so the same-support
noncontainment condition removes them from the MCA-bad count.  This is why the
degenerate eliminant branch above is empty only after enforcing
`H_2 ell_T != 0`.

## Remaining wall

The Johnson transfer in `thm:transfer` needs a polynomial bound for
`sigma_C(delta)` uniformly in the whole Johnson range.  In that range

```text
h = 2r - (n-k) - 1
```

can grow linearly in `n`, so the fixed-layer bound `O_h(n^(h+3))` is not
enough.

The exact next problem is uniform sparse-sigma pencil aggregation:

```text
For every eta > 0, prove or refute a polynomial P_eta(n) such that,
for all r <= (1 - sqrt(k/n) - eta)n and every sparse pair,

#{ gamma in F :
   exists T subset D, |T| = r,
   (H_1 + gamma H_2) ell_T = 0,
   H_2 ell_T != 0 }
<= P_eta(n).
```

The fixed-layer proof charges slopes to `binom(n,h+2)` evaluation charts.  The
uniform problem is to compress or amortize those active charts when `h` grows,
or to construct a genuine growing-`h` sparse pair with superpolynomially many
non-tangent, noncontained bad slopes.

## Nonclaims

This note does not prove `thm:transfer`, does not settle the Johnson band, does
not determine the exact value of `delta_C^*`, and does not improve a finite
leaderboard row.  It is a fixed-residual-layer proof inside the sparse mutual
problem.
