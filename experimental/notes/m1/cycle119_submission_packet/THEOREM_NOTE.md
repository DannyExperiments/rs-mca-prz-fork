# Cycle119 Strict-263 Two-Ended RS-MCA Theorem

Date: 2026-06-23

## Abstract

We prove a finite support-wise Reed-Solomon MCA lower bound for the smooth multiplicative row

```text
C = RS[F_17^32,H,256], |H|=512.
```

Assuming the imported Cycle84 finite census, the Cycle119 two-ended locator transfer gives

```text
LD_sw(C,263) >= 52,747,567,092.
```

Since `512-263=249<250=(125/256)512`, this is a strict-ball witness at radius `125/256`. Under the source definition where the line parameter is sampled uniformly from `F_17^32`,

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

This note does not claim ordinary list decoding, protocol soundness, asymptotics, or official Proximity Prize status without row/predicate/sampler admissibility.

## 1. Imported Finite Certificate

We import the Cycle84 finite census:

```text
N = 52,747,567,092
```

distinct product values `Phi(T)` on the designated Cycle84 shell. The import includes:

```text
maximum product fiber size = 2
exactly 12 double fibers
no product fiber of size >= 3
all 336 slot bridge identities
```

The Cycle116 transfer certificate already gives a finite agreement-262 theorem. Cycle119 upgrades the same numerator to agreement 263 by replacing naive agreement padding with a two-ended locator theorem.

## 2. The Two-Ended Locator Theorem

Let `F` be a finite field, `D subset F^*` a set of `n` distinct points, and `beta in F \ D`. Let `mathcal J` be a family of `j`-subsets `J subset D`, with monic locators

```text
P_J(X) = prod_{a in J}(X-a).
```

Let `sigma >= 2`, set

```text
r = j + sigma,
k = n - r,
C = RS[F,D,k].
```

Assume:

```text
deg(P_J - P_J') <= j - sigma + 1
```

for all `J,J'`, and

```text
P_J(0) = c in F^*
```

independently of `J`.

Then there are common words `f,g in F^D` such that for every `J`,

```text
z_J = -P_J(beta)^(-1)
```

has a support-wise noncontained witness on

```text
S_J = D \ J,
|S_J| = n - j.
```

Consequently,

```text
LD_sw(C,n-j) >= #{P_J(beta): J in mathcal J}.
```

## 3. Proof of the Theorem

Write

```text
P_J(X)=sum_{u=0}^j p_u^(J) X^u,
p_j^(J)=1.
```

The degree hypothesis makes the coefficients in degrees

```text
j, j-1, ..., j-sigma+2
```

common across `J`.

Let

```text
A(X)=a_0+a_1X+...+a_{sigma-1}X^{sigma-1},
Q(X)=P_J(X)A(X)=sum q_d X^d.
```

The constant coefficient is

```text
q_0 = c a_0.
```

For `1 <= s <= sigma-1`,

```text
q_{j+s} = sum_{m=s}^{sigma-1} p_{j+s-m}^(J) a_m.
```

Only common top coefficients of `P_J` appear. Ordered from `s=sigma-1` down to `s=1`, this is a triangular system for

```text
a_1, ..., a_{sigma-1}
```

with diagonal entries `1`. Together with `q_0=c a_0`, the selected coordinates

```text
q_0, q_{j+1}, ..., q_{j+sigma-1}
```

recover `A` by one common linear map independent of `J`.

Therefore there is a global linear functional

```text
ell : F[X]_{<r} -> F
```

satisfying

```text
ell(P_J A) = A(beta)
```

for all `J` and all `deg A < sigma`.

Let

```text
V_D(X)=prod_{a in D}(X-a)
```

and define the standard weighted Vandermonde parity-check matrix `H` by columns

```text
h_a = V_D'(a)^(-1) (1,a,...,a^{r-1})^T.
```

Then

```text
ker H = RS[F,D,k].
```

For `J`, set

```text
W_J = span{h_a : a in J}.
```

Under coefficient-vector pairing,

```text
W_J^perp = P_J F[X]_{<sigma}.
```

Let `y_0` represent `ell`, and set

```text
y_1 = (1,beta,...,beta^{r-1})^T.
```

For `Q=P_JA in W_J^perp`,

```text
<Q,y_0+z y_1>
  = A(beta) + z P_J(beta) A(beta).
```

At `z=z_J=-P_J(beta)^(-1)`, this vanishes for every `A`, hence

```text
y_0 + z_J y_1 in W_J.
```

Choose `f,g in F^D` with

```text
Hf = y_0,
Hg = y_1.
```

For each `J`, choose `e_J` supported on `J` with

```text
H e_J = y_0 + z_J y_1.
```

Then

```text
c_J = f + z_J g - e_J
```

is in `C`, and on `S_J=D\J`,

```text
c_J = f + z_J g.
```

Thus `f+z_J g` is code-explained on `S_J`.

For noncontainment, suppose `g` were code-explainable on `S_J`. Then `g-c_g` would be supported on `J`, so

```text
y_1 in W_J.
```

But `y_1` is the Vandermonde column at `beta`, while `W_J` is the span of the columns at the `j` points of `J`. The `j+1` points `J union {beta}` are distinct and `j+1 <= j+sigma = r`, so the corresponding Vandermonde columns are independent. Contradiction.

Therefore each `z_J` is support-wise noncontained.

## 4. Cycle84 Instantiation

Work in

```text
K = F_17^32,
theta^2 = eta,
ord(theta)=512,
D0 = <eta> = <theta^2>, |D0|=256,
H = <theta> = D0 disjoint_union theta D0, |H|=512.
```

The native Cycle84 supports `J_T subset D_0=<eta>` have size `113` and locators

```text
P_T(X) = X^113 - X^112 + O(X^107).
```

They satisfy

```text
P_T(beta) = 4(beta-1) Phi(T).
```

Partition the odd coset:

```text
A* = {theta eta^i : 0 <= i <= 119}, |A*|=120,
R* = {theta eta^i : 120 <= i <= 255}, |R*|=136.
```

Define

```text
J_T* = J_T union R*,
P_T* = P_R* P_T.
```

The union is disjoint. Indeed,

```text
J_T subset D0,
R* subset theta D0,
H = D0 disjoint_union theta D0.
```

Then

```text
|J_T*| = 113 + 136 = 249,
|H \ J_T*| = 512 - 249 = 263.
```

Moreover, because the roots are disjoint, `P_T*` is the square-free locator of
`J_T*`, not merely a product with possible repeated factors.

Since `deg(P_T-P_T') <= 107` and `deg P_R*=136`,

```text
deg(P_T* - P_T'*) <= 243.
```

For

```text
j=249,
sigma=7,
```

this is precisely `j-sigma+1`.

The common constant condition holds because the shell block-color identity gives

```text
P_T(0) = -1
```

for every `T`, hence

```text
P_T*(0) = -P_R*(0) != 0.
```

The augmented evaluation is

```text
P_T*(beta) = P_R*(beta) 4(beta-1) Phi(T),
```

with fixed nonzero prefactor. Here `beta notin H`; hence `P_R*(beta) != 0`,
and also `beta-1 != 0` because `1 in H`. Therefore the number of distinct
augmented locator evaluations equals the imported Cycle84 occupancy:

```text
#{P_T*(beta)} = #{Phi(T)} = 52,747,567,092.
```

Applying the two-ended theorem with

```text
n=512,
j=249,
sigma=7,
r=256,
k=256
```

proves

```text
LD_sw(RS[K,H,256],263) >= 52,747,567,092.
```

## 5. Strict Radius And Threshold

The constructed witnesses have distance at most

```text
512 - 263 = 249.
```

At radius `125/256`, length `512` gives

```text
(125/256)*512 = 250.
```

Hence all witnesses lie in the strict ball `d < 250`.

Also,

```text
17^32 = 2,367,911,594,760,467,245,844,106,297,320,951,247,361
floor(17^32 / 2^128) = 6
52,747,567,092 > 6.
```

Therefore

```text
52,747,567,092 / 17^32 > 2^-128.
```

## 6. Verification

Local replay terminal:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

Key receipt fields:

```text
agreement = 263
strict_hamming_distance_upper_bound = 249
distinct_slopes = 52,747,567,092
hidden_seventh_top_coefficient_used = false
two_ended_selector_degrees = [0,250,251,252,253,254,255]
q_gen = q_code = q_line = 17^32
q_chal = null
```

## 7. Non-Claims

This note does not prove:

```text
ordinary fixed-word list decoding;
protocol soundness failure;
an asymptotic theorem;
official Proximity Prize status without admissibility confirmation;
an independent q_chal theorem;
any challenge-map/event-retention theorem.
```

## 8. Official Question

Does the official grand MCA challenge admit:

```text
RS[F_17^32,H,256], |H|=512,
gamma sampled uniformly from F_17^32,
support-wise same-support epsilon_mca,
no extra endpoint/quotient/charge/event filter?
```

If yes, this theorem appears to be a Proximity Prize counterexample candidate at `delta=125/256`.
