# CAP25 v12 sparse sigma first-layer audit

Status: PROVED / AUDIT / ROUTE_CUT.

This note records three small consequences of the sparse mutual layer in
`tex/towards-prize.tex`.  The first is a linear lower-bound branch for
`sigma_C(delta)` immediately above the sparse half-distance threshold.  The
second repairs the literal affine split-pencil target at the first residual
layer by projectivizing the locator image.  The third records an exact
closed-ball Pade-Hankel formulation of sparse MCA bad slopes.

This is not a proof of the Johnson-transfer hypothesis in
`thm:transfer`.  It does not improve a finite leaderboard row and it does not
by itself complete the CAP25 v12 cap machinery.  It narrows the local sparse
residue: the first layer is polynomially controlled, while the higher
positive-residual Pade-Hankel/split-locator incidence remains open.

## Setup

Let

```text
C = RS[F,D,k],   n = |D|,   m = n-k,   r = floor(delta n).
```

We use the sparse mutual layer `sigma_C(delta)` from `towards-prize.tex`:
the maximum number of `delta`-MCA-bad finite slopes over sparse pairs
`(epsilon_1,epsilon_2)` with support union size at most `r`.  The relevant
source labels are:

```text
lem:line
thm:sparsify
thm:sparse-threshold
thm:pinning
thm:rigidity
rem:valuewall
thm:transfer
prob:mutual / prob:sparse-mutual
```

## 1. Moving-zero lower bound

Assume

```text
k >= 2,   2 <= r <= m-1,   2r >= m+1.
```

Choose disjoint sets

```text
Z_* subset D,        |Z_*| = k-2,
E'  subset D \ Z_*,  |E'|  = r,
Pi(X) = product_{z in Z_*} (X-z).
```

Define a sparse pair supported on `E'` by

```text
epsilon_1(j) = j Pi(j),
epsilon_2(j) = -Pi(j)       for j in E',
epsilon_i(j) = 0            for j not in E'.
```

Then this one sparse pair has at least

```text
r + (m-r+2) = m+2 = n-k+2
```

distinct `delta`-MCA-bad slopes.  Hence

```text
sigma_C(delta) >= n-k+2.
```

Proof.  For every

```text
x in D \ (E' union Z_*),
```

put

```text
z_x(X) = (X-x) Pi(X).
```

Then `deg z_x = k-1 < k`.  On `E'`,

```text
epsilon_1 + x epsilon_2 = (X-x) Pi(X).
```

Thus the set

```text
S_x = E' union Z_* union {x}
```

has size

```text
|S_x| = r + (k-2) + 1 = r+k-1 = n-(m-r+1) >= n-r,
```

where the last inequality is `2r >= m+1`.  Therefore `(z_x,S_x)` is a
proximity witness for slope `x`.

The witness fails mutually.  If `epsilon_2|_{S_x}` were the restriction of a
degree `< k` polynomial `p`, then `p` would vanish on the `k-1` distinct
points `Z_* union {x}`.  Hence

```text
p = c (X-x) Pi(X)
```

for some scalar `c`.  Matching `epsilon_2=-Pi` on `E'` would require

```text
c(j-x) = -1                 for every j in E',
```

which is impossible because `|E'| >= 2` and the points of `E'` are distinct.
So each `x in D \ (E' union Z_*)` gives a non-tangent MCA-bad slope.  There
are

```text
n-r-(k-2) = m-r+2
```

such slopes.

For every `j_0 in E'`, the slope `gamma=j_0` is tangent because

```text
epsilon_1(j_0) + j_0 epsilon_2(j_0) = 0.
```

The zero codeword on `(D \ E') union {j_0}` gives a failing witness, since
`epsilon_2` is nonzero on `E'`.  These `r` tangent slopes are distinct and
disjoint from the displayed moving-zero slopes.

The wording above is intentionally one-sided.  The construction exhibits
`m-r+2` non-tangent slopes, but these need not be all non-tangent bad slopes
of the sparse pair.  Extra slopes belong to the split-pencil residue below.

## 2. Minimal-layer projective split-pencil bound

The literal affine formulation is false.  If

```text
LVar(E) =
{ lambda product_{z in Z}(X-z)|_E :
    Z subset D\E, |Z| = k-1, lambda in F^* } subset F^E,
```

then every radial affine line through one locator vector contains `q-1`
points of `LVar(E)`.  This is a fixed-`n`, growing-`q` counterpacket to any
literal affine-line bound.  It is not a sparse-MCA counterexample: the radial
copies are the same projective locator direction and are mutually extendable
in the same-support test.

At the first residual layer

```text
2r = m+1 = n-k+1,
```

the projective repair is polynomial.

Let `E subset D`, `|E|=r`, and let `D_0 = D \ E`.  For
`Z subset D_0`, `|Z| = k-1 = n-2r`, define

```text
u_Z = ( product_{z in Z}(x-z) )_{x in E} in F^E.
```

Let

```text
X_E = { [u_Z] : Z subset D_0, |Z|=k-1 } subset P(F^E).
```

Then every projective line `ell subset P(F^E)` satisfies

```text
|ell intersection X_E| <= 1 + binom(n-r,2)(r-1) = O(n^3).
```

This note records the conservative `O(n^3)` form.  Some audits suggest a
sharper `O(n^2)` projective bound after further quotienting, but that
sharpening is not needed for the first-layer conclusion below.

Sketch of proof.  Write `A=D_0` and pass to complements
`W=A\Z`, so `|W|=r`.  Multiplying all coordinates by the fixed nonzero
diagonal factor

```text
P_A(e) = product_{a in A} (e-a)
```

identifies `X_E` projectively with

```text
U_E = { [ 1 / Q_W(e) ]_{e in E} : W subset A, |W|=r },
Q_W(X) = product_{w in W} (X-w).
```

Parametrize a genuine projective line by `[a+t b]`.  For parameters with no
zero coordinate, let `R_t` be the unique polynomial of degree `< r` satisfying

```text
R_t(e) = 1/(a_e+t b_e)       for e in E.
```

If `[1/Q_W(e)]` lies on the line, then for some scalar `mu`,

```text
Q_W(X) = Q_E(X) + mu R_t(X),
```

because both sides are monic degree-`r` polynomials agreeing on `E`.  For any
two distinct `x,y in W`,

```text
Q_E(x) R_t(y) - Q_E(y) R_t(x) = 0.
```

After clearing the coordinate denominators, this is a polynomial equation in
the line parameter of degree at most `r-1`, unless it is identically zero.
If all pair equations inside `W` were identically zero, the line would be
constant on the locator point.  Hence each counted point is charged to some
unordered pair `{x,y} subset A` with a nonzero equation, and each pair receives
at most `r-1` parameters, plus the omitted point at infinity.  This gives

```text
|ell intersection X_E| <= 1 + binom(n-r,2)(r-1).
```

Consequently, at the minimal layer `2r=m+1`,

```text
sigma_C(delta) <= r + 1 + binom(n-r,2)(r-1) = O(n^3).
```

Indeed, if the sparse support has size `< r`, then `thm:sparse-threshold`
leaves only tangent slopes.  If the support has size `r`, then
`thm:pinning` and `thm:rigidity` force every non-tangent bad slope to give a
projective intersection between the slope line

```text
epsilon_1 + F epsilon_2 subset F^E
```

and `X_E`, with the radial mutually extending case excluded.  Tangent slopes
contribute at most `r`.

This proves only the first residual layer.  It does not control the whole
Johnson band, where the witness polynomial has a positive-degree factor and
the sparse value-set problem becomes a higher-dimensional budget-coupled
incidence problem.

## 3. Exact Pade-Hankel formulation

Let `r <= m-1`.  For `x in D`, set

```text
lambda_x = ( product_{y in D, y != x} (x-y) )^{-1}.
```

For a word `Y:D -> F`, define syndrome coordinates

```text
Syn(Y)_a = sum_{x in D} lambda_x x^a Y(x),    0 <= a < m.
```

Then `Y in C` iff `Syn(Y)=0`.  For a syndrome vector `s`, define the
closed-ball Hankel window

```text
H_r(s)_{a,b} = s_{a+b},       0 <= a < m-r, 0 <= b <= r.
```

For a sparse pair, write `s_i=Syn(epsilon_i)` and `H_i=H_r(s_i)`.
For `T subset D`, `|T|=r`, write

```text
L_T(X) = product_{x in T}(X-x) = ell_0 + ell_1 X + ... + ell_r X^r.
```

Then a finite slope `gamma` is `delta`-MCA-bad for the sparse pair iff there
exists `T subset D`, `|T|=r`, such that

```text
(H_1 + gamma H_2) ell_T = 0,
H_2 ell_T != 0.
```

The first equation says `epsilon_1 + gamma epsilon_2` is explained by a
codeword on `S=D\T`.  The second equation is the same-support noncontainment
test: `epsilon_2` is not explained on that same `S`, so the witness fails
mutually by `lem:line`.

This statement is exact only after two repairs:

1. The closed ball may be taken with `|T|=r`.  If an MCA witness exists on a
   larger set, MDS restriction detects noncontainment on a subset of size
   `k+1`; enlarge inside the original witness set to a set of size `n-r`.
2. The phrase "excess kernel" is not correct without the second condition
   `H_2 ell_T != 0`.  Common/contained locators can lie in
   `ker(H_1+gamma H_2)` and certify no MCA failure.

In the regular overdetermined buckets, this Hankel form gives ordinary
rank-drop/eliminant handles.  At and beyond the first residual layer, the
matrix can have generic kernel, so the problem is not just rank drop.  The
remaining wall is:

```text
Bound the number of gamma for which H_1+gamma H_2 has a D-split squarefree
locator in the relevant kernel outside the same-support/common-extension
kernel, after removing tangent, quotient, subfield, and moving-zero branches.
```

That is precisely the split-locator incidence form of `prob:mutual`.

## Consequences

What is new here:

```text
1. The moving-zero branch gives a public-safe O(n) lower bound,
   sigma_C(delta) >= n-k+2, starting at 2r >= n-k+1.
2. The first residual layer 2r=n-k+1 is polynomially controlled:
   sigma_C(delta) = O(n^3).
3. The Pade-Hankel restatement is exact only with fixed closed-ball support
   size and the same-support noncontainment test.
```

What is still missing:

```text
1. A polynomial bound for sigma_C(delta) throughout
   delta <= 1 - sqrt(rho) - eta.
2. A higher positive-residual split-locator incidence theorem.
3. A proof that all dominant Hankel projections are paid by tangent,
   quotient, subfield, moving-zero, or another explicit branch.
```

First possible fatal line for the CAP25-v12 transfer route:

```text
There may be a higher positive-residual Hankel/split-locator chart whose slope
projection is dominant after all currently paid branches are removed.
```

The next exact target is therefore not another finite row example.  It is a
higher-layer version of the projective split-pencil theorem, phrased in the
closed-ball Pade-Hankel coordinates above.
