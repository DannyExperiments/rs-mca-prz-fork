# Fixed-Jet and Two-Ended Locator Transfers

Date: 2026-06-24

Status: Transfer lemmas proved, assuming the stated computed input in the
example section.

## Purpose

This note extracts the reusable mathematics from the recent explicit-row work.
The main objects are two locator-to-MCA transfer lemmas. The 84-state product
data enter only as one computed input for the example at the end.

The note is meant to be read without the cycle history.

## 1. Support-wise line-MCA notation

Let `C = RS[F,D,k]`, where `D subset F` has `n` distinct points. For an affine
line of words

```text
u_z = f + z g,       z in F,
```

call a parameter `z` support-wise bad at agreement `a` if there exists
`S subset D`, `|S| >= a`, such that:

1. `u_z|_S` is explained by a codeword of `C`;
2. `f|_S` and `g|_S` are not simultaneously explained by codewords of `C`.

Let `LD_sw(C,a)` be the maximum, over affine lines `f+zg`, of the number of
distinct support-wise bad parameters at agreement `a`.

This is the same support-wise same-support event used by ABF Definition 4.3
for `epsilon_mca`, once the line parameter is sampled uniformly from `F`.

## 2. Fixed-jet locator transfer

Let `D subset F`, `|D|=n`, and let `beta in F \ D`. Let `mathcal J` be a family
of `j`-subsets of `D`. For `J in mathcal J`, write

```text
P_J(X) = prod_{a in J} (X-a).
```

Assume that, for some `sigma >= 1`,

```text
deg(P_J - P_J') <= j - sigma
```

for all `J,J' in mathcal J`. Put

```text
k = n - j - sigma,
C = RS[F,D,k].
```

Assume `k >= 1`.

Then

```text
LD_sw(C, n-j) >= #{ P_J(beta) : J in mathcal J }.
```

More precisely, one affine line realizes the right-hand side after the
reciprocal-affine change

```text
P_J(beta) |-> alpha + lambda / P_J(beta),
lambda != 0.
```

### Proof

Let

```text
V_D(X) = prod_{a in D} (X-a),
L_J(X) = V_D(X) / P_J(X).
```

Thus `L_J` is the locator of `S_J = D \ J`, and

```text
deg L_J = n-j = k+sigma.
```

Since `P_J L_J = P_J' L_J' = V_D`,

```text
P_J (L_J - L_J') = (P_J' - P_J) L_J'.
```

The right side has degree at most

```text
(j-sigma) + (n-j) = n - sigma = j + k.
```

Dividing by the monic degree-`j` polynomial `P_J`, we get

```text
deg(L_J - L_J') <= k.
```

Hence all `L_J` have the same coefficients in degrees

```text
k+1, k+2, ..., k+sigma.
```

Let `W(X)` be this common high-degree truncation and define

```text
Q_J(X) = W(X) - L_J(X).
```

Then `deg Q_J <= k`.

Define a single line on `D` by

```text
f(x) = W(x) / (x-beta),
g(x) = -1 / (x-beta).
```

For each `J`, set

```text
z_J = Q_J(beta),
c_J(X) = (Q_J(X) - z_J) / (X-beta).
```

The numerator of `c_J` vanishes at `X=beta`, so `c_J` is a polynomial. Since
`deg Q_J <= k`, we have `deg c_J < k`, hence `c_J` is a codeword of
`RS[F,D,k]`.

On `S_J = D \ J`, the polynomial `L_J` vanishes, so `Q_J(x)=W(x)`. Therefore

```text
c_J(x)
  = (W(x)-z_J)/(x-beta)
  = f(x) + z_J g(x)
```

for every `x in S_J`. Thus `f+z_J g` agrees with the codeword `c_J` on
`|S_J|=n-j` points.

It remains to prove noncontainment. Suppose a polynomial `G` of degree `< k`
explained `g` on `S_J`. Then

```text
R(X) = (X-beta)G(X) + 1
```

would have degree at most `k` and would vanish on all `n-j=k+sigma` points of
`S_J`. Since `sigma >= 1`, this is more than `k` roots. Hence `R` would be the
zero polynomial. But `R(beta)=1`, contradiction.

Finally,

```text
z_J
  = W(beta) - L_J(beta)
  = W(beta) - V_D(beta)/P_J(beta).
```

Because `beta notin D`, `V_D(beta) != 0`. Thus the map from `P_J(beta)` to
`z_J` is injective on `F^*`. This proves the claimed lower bound.

## 3. Two-ended locator transfer

The previous lemma uses a full common top `sigma`-jet. The following variant
uses only the top `sigma-1` coefficients and one common nonzero constant
coefficient.

Let `D subset F`, `|D|=n`, and let `beta in F \ D`. Let `mathcal J` be a family
of `j`-subsets of `D`, with monic locators

```text
P_J(X) = prod_{a in J} (X-a).
```

Fix `sigma >= 2`, put

```text
r = j + sigma,
k = n - r,
C = RS[F,D,k].
```

Assume:

```text
deg(P_J - P_J') <= j - sigma + 1
```

for all `J,J'`, and assume the constant coefficient is common and nonzero:

```text
P_J(0) = c in F^*
```

for every `J`.

Then

```text
LD_sw(C, n-j) >= #{ P_J(beta) : J in mathcal J }.
```

### Proof

Write

```text
P_J(X) = sum_{u=0}^j p_u^(J) X^u,
p_j^(J) = 1.
```

The degree hypothesis says that the coefficients in degrees

```text
j, j-1, ..., j-sigma+2
```

are common across `J`. The coefficient in degree `j-sigma+1` is not assumed to
be common.

Let

```text
A(X) = a_0 + a_1 X + ... + a_{sigma-1} X^{sigma-1}
```

and put

```text
Q(X) = P_J(X) A(X) = sum q_d X^d.
```

Use the selected coordinates

```text
q_0, q_{j+1}, q_{j+2}, ..., q_{j+sigma-1}.
```

The constant coordinate is

```text
q_0 = c a_0.
```

For `1 <= s <= sigma-1`,

```text
q_{j+s} = sum_{m=s}^{sigma-1} p_{j+s-m}^(J) a_m.
```

Every locator coefficient appearing here has degree at least

```text
j+s-(sigma-1) >= j-sigma+2.
```

These are exactly among the common top coefficients. Ordered from high `s` down
to low `s`, the equations form a triangular system for

```text
a_1, ..., a_{sigma-1}
```

with diagonal entries `p_j=1`. Together with `q_0=c a_0`, the selected
coordinates recover all coefficients of `A` by one invertible linear map
independent of `J`.

Therefore there is a linear functional

```text
ell : F[X]_{<r} -> F
```

such that

```text
ell(P_J A) = A(beta)
```

for every `J` and every `A` with `deg A < sigma`.

Now use the weighted Vandermonde parity-check matrix for `C`. Let

```text
V_D(X) = prod_{a in D} (X-a),
h_a = V_D'(a)^(-1) (1,a,...,a^{r-1})^T.
```

Let `H_C` be the `r x n` matrix with columns `h_a`. Then

```text
ker H_C = RS[F,D,k].
```

The inclusion `RS[F,D,k] subset ker H_C` follows from the standard Lagrange
coefficient identity: for `deg p < k` and `0 <= m < r`, the polynomial
`X^m p(X)` has degree at most `n-2`, so the coefficient of `X^{n-1}` in its
interpolation on `D` is zero. The reverse inclusion follows by dimension,
because any `r` columns form a weighted Vandermonde matrix of rank `r`.

For `J in mathcal J`, let

```text
W_J = span{ h_a : a in J }.
```

Under coefficient-vector pairing,

```text
W_J^perp = P_J F[X]_{<sigma}.
```

Indeed, a polynomial of degree `<r` annihilates all columns indexed by `J`
exactly when it vanishes on all points of `J`, equivalently when it is
divisible by `P_J`.

Let `y_0 in F^r` represent `ell`, and put

```text
y_1 = (1,beta,...,beta^{r-1})^T.
```

For `Q=P_J A in W_J^perp`,

```text
<Q, y_0 + z y_1>
  = A(beta) + z P_J(beta) A(beta).
```

Since `beta notin D`, `P_J(beta) != 0`. At

```text
z_J = -P_J(beta)^(-1),
```

the pairing vanishes for every `A`, so

```text
y_0 + z_J y_1 in W_J.
```

The parity-check map is surjective, so choose common words `f,g in F^D` with

```text
H_C f = y_0,
H_C g = y_1.
```

For each `J`, choose an error word `e_J` supported on `J` with

```text
H_C e_J = y_0 + z_J y_1.
```

Then

```text
c_J = f + z_J g - e_J
```

lies in `ker H_C = C`, and on `S_J = D \ J` it satisfies

```text
c_J|_{S_J} = (f+z_J g)|_{S_J}.
```

Thus `f+z_J g` is code-explained on `n-j` points.

For noncontainment, suppose `g` were code-explained on `S_J`. Then for some
`c_g in C`, the word `g-c_g` would be supported on `J`, hence

```text
y_1 = H_C g = H_C(g-c_g) in W_J.
```

But `W_J` is the span of the weighted Vandermonde columns at the points of
`J`, while `y_1` is the unweighted Vandermonde column at `beta`. The weights
are nonzero, and the `j+1` columns indexed by `J union {beta}` are independent
because the points are distinct and

```text
j+1 <= j+sigma = r.
```

Thus `y_1 notin W_J`, contradiction. This proves support-wise noncontainment.

The map

```text
P_J(beta) |-> -P_J(beta)^(-1)
```

is injective on `F^*`, giving the stated count.

## 4. Example from the 84-state product computation

This section records one example using a computed product count. The proof
above is independent of how the count is obtained.

Let

```text
F0 = F_17[xi] / (xi^16 + xi^8 + 3),
eta = 6 xi^9,
beta = xi + 2,
D0 = <eta>.
```

The checked field arithmetic gives

```text
ord(eta) = 256,
eta^16 = 3,
beta notin D0.
```

The 84-state construction gives a family of 113-point subsets

```text
J_T subset D0
```

with locators `P_T`. The computed input is:

```text
P_T(X) = X^113 - X^112 + O(X^107),
P_T(beta) = (beta-1) 3^28 Phi(T),
#{ Phi(T) } = 52,747,567,092.
```

The equality `P_T(beta)=(beta-1)3^28 Phi(T)` uses the 336 local slot
identities. The product count already accounts for the twelve double product
fibers.

Applying the fixed-jet lemma with

```text
n = 256,
j = 113,
sigma = 6,
k = 137
```

gives

```text
LD_sw(RS[F0,D0,137],143) >= 52,747,567,092.
```

## 5. Smooth [512,256] row at agreement 262

Let

```text
K = F0(theta),        theta^2 = eta.
```

Since `eta` is not a square in `F0`, this is

```text
K = F_17^32.
```

Moreover `theta` has order 512, and the checked field arithmetic gives
`beta notin H`. Put

```text
H = <theta> = D0 disjoint_union theta D0.
```

Choose a fixed 137-point subset `R` of the odd coset `theta D0`, and set

```text
J_T^+ = J_T union R.
```

Then

```text
|J_T^+| = 250,
|H \ J_T^+| = 262.
```

Since the fixed locator `P_R` has degree 137,

```text
deg(P_R P_T - P_R P_T') <= 137 + 107 = 244.
```

For the smooth row

```text
n = 512,
j = 250,
sigma = 6,
k = 256,
```

we have `j-sigma=244`, so the fixed-jet lemma applies directly. Also

```text
(P_R P_T)(beta) = P_R(beta)(beta-1)3^28 Phi(T),
```

with fixed nonzero prefactor, since `beta notin H`. Thus

```text
LD_sw(RS[K,H,256],262) >= 52,747,567,092.
```

For ABF Definition 4.3 at `delta=125/256`, the support threshold is

```text
(1-delta) |H|
  = (1 - 125/256) 512
  = 262.
```

Therefore this example gives

```text
epsilon_mca(RS[K,H,256],125/256)
  >= 52,747,567,092 / 17^32.
```

The exact integer comparison is

```text
17^32 =
2367911594760467245844106297320951247361,

floor(17^32 / 2^128) = 6,

52,747,567,092 > 6.
```

Hence the displayed ratio is strictly larger than `2^-128`.

## 6. Strict-threshold strengthening at agreement 263

The two-ended transfer gives a one-coordinate stronger version on the same
row.

Partition the odd coset as

```text
A* = { theta eta^i : 0 <= i <= 119 },
R* = { theta eta^i : 120 <= i <= 255 }.
```

Then `|A*|=120`, `|R*|=136`, and `R* subset theta D0` is disjoint from every
`J_T subset D0`. Put

```text
J_T* = J_T union R*.
```

Then

```text
|J_T*| = 249,
|H \ J_T*| = 263.
```

The fixed locator `P_R*` has degree 136, so

```text
deg(P_R* P_T - P_R* P_T') <= 136 + 107 = 243.
```

For

```text
j = 249,
sigma = 7,
```

this is `j-sigma+1 = 243`, the two-ended hypothesis.

The common nonzero constant coefficient comes from:

```text
P_T(0) = -1,
P_R*(0) != 0.
```

Thus

```text
(P_R* P_T)(0) = -P_R*(0) != 0.
```

The evaluation at `beta` is

```text
(P_R* P_T)(beta)
  = P_R*(beta)(beta-1)3^28 Phi(T),
```

again with fixed nonzero prefactor. The two-ended transfer gives

```text
LD_sw(RS[K,H,256],263) >= 52,747,567,092.
```

This implies distance at most

```text
512 - 263 = 249,
```

which is strictly less than

```text
(125/256) 512 = 250.
```

The agreement-263 strengthening is not needed for ABF's printed closed
threshold, but it is useful against strict-ball conventions.

## 7. What this does not claim

This note does not claim:

- an ordinary fixed-word list-decoding lower bound;
- protocol soundness failure;
- an asymptotic theorem;
- exact determination of the ABF threshold for the row;
- that the computed 84-state product count has been replaced by a symbolic
  product-spectrum theorem.

The main reusable mathematics is the pair of transfer lemmas. The main
remaining theory direction is to replace isolated computed product spectra by
parametric families, or to prove positive local-limit theorems above the
corrected reserve in Paper B.

## 8. First lines to audit

A hostile audit should focus on:

1. Does the definition of `LD_sw` match the ABF support-wise MCA event?
2. Is the fixed-jet proof correct, especially the passage from common locator
   jet to common complementary-locator truncation?
3. Is the two-ended functional really independent of `J`, and does it avoid
   the missing coefficient in degree `j-sigma+1`?
4. Is the parity-check construction exactly the Reed-Solomon parity check?
5. Is the computed 84-state input correct?
6. Does the ABF closed threshold use `|S| >= (1-delta)n` with no strict
   endpoint deletion?

If any answer is no, that is the first mathematical line to fix or cut.
