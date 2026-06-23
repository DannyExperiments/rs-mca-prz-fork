# Cycle119 Cold Packet: Strict-263 Two-Ended RS-MCA Candidate

Date: 2026-06-23

Status:

```text
PROOF at finite/source LD_sw and support-wise MCA level.
PRIZE-CANDIDATE only after official row/predicate/sampler admissibility is confirmed.
```

## 1. Executive Theorem

Let

```text
K = F_17^32,
H = <theta>, |H| = 512,
C = RS[K,H,256].
```

Using the Cycle84 finite census and the Cycle119 two-ended locator transfer, one obtains

```text
LD_sw(C,263) >= 52,747,567,092.
```

Thus every certified bad slope has an explaining codeword at distance at most

```text
512 - 263 = 249 < 250 = (125/256)*512.
```

Consequently, under the source support-wise MCA definition with line parameter sampled uniformly from `K`,

```text
epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32
  > 2^-128.
```

This is not an ordinary fixed-word list-decoding lower bound, not protocol soundness, and not yet an official Proximity Prize claim.

The exact official question is:

```text
Does the grand MCA challenge admit this row, this support-wise predicate,
and uniform gamma sampling from F_17^32 without an additional endpoint,
quotient, challenge-map, charge, or event-retention filter?
```

## 2. Two-Ended Locator Theorem

Let `F` be a finite field, let `D subset F^*` have `n` distinct points, and let `beta in F \ D`. Let `J` range over a family `mathcal J` of `j`-subsets of `D`, with monic locators

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
P_J(0) = c in F^*.
```

Then there are common words `f,g in F^D` such that for every `J`,

```text
z_J = -P_J(beta)^(-1)
```

is support-wise bad with witness support

```text
S_J = D \ J,
|S_J| = n - j.
```

In particular,

```text
LD_sw(C,n-j) >= #{ P_J(beta) : J in mathcal J }.
```

## 3. Proof of the Two-Ended Theorem

Write

```text
P_J(X) = sum_{u=0}^j p_u^(J) X^u,
```

with `p_j^(J)=1`. The degree hypothesis says the coefficients in degrees

```text
j, j-1, ..., j-sigma+2
```

are common across `J`.

Let

```text
A(X) = a_0 + a_1 X + ... + a_{sigma-1} X^{sigma-1}
```

and set

```text
Q(X) = P_J(X) A(X) = sum q_d X^d.
```

The constant coefficient is

```text
q_0 = c a_0.
```

For `1 <= s <= sigma-1`,

```text
q_{j+s}
  = sum_{m=s}^{sigma-1} p_{j+s-m} a_m.
```

Only the common top coefficients of `P_J` occur in these equations. The system in

```text
a_1, ..., a_{sigma-1}
```

is triangular with diagonal entries `1`, because `P_J` is monic. Together with `q_0=c a_0`, the selected coordinates

```text
q_0, q_{j+1}, ..., q_{j+sigma-1}
```

recover all coefficients of `A` by one linear map independent of `J`.

Therefore there is a global linear functional

```text
ell : F[X]_{<r} -> F
```

such that

```text
ell(P_J A) = A(beta)
```

for every `J` and every `deg A < sigma`.

Now use the standard weighted Vandermonde parity-check matrix for `C`:

```text
h_a = V_D'(a)^(-1) (1,a,...,a^{r-1})^T,
V_D(X)=prod_{a in D}(X-a).
```

Its kernel is `RS[F,D,k]`. For each `J`, define

```text
W_J = span{ h_a : a in J }.
```

Under coefficient-vector pairing,

```text
W_J^perp = P_J F[X]_{<sigma}.
```

Let `y_0` represent `ell`, and set

```text
y_1 = (1,beta,...,beta^{r-1})^T.
```

For `Q=P_J A in W_J^perp`,

```text
<Q, y_0 + z y_1>
  = A(beta) + z P_J(beta) A(beta).
```

At

```text
z_J = -P_J(beta)^(-1),
```

this vanishes for every `A`, so

```text
y_0 + z_J y_1 in W_J.
```

Choose common words `f,g` satisfying

```text
H f = y_0,
H g = y_1.
```

For each `J`, choose an error vector `e_J` supported on `J` with

```text
H e_J = y_0 + z_J y_1.
```

Then

```text
c_J = f + z_J g - e_J
```

lies in `C`, and on `S_J=D\J` the error `e_J` vanishes, so

```text
(f+z_J g)|_{S_J} = c_J|_{S_J}.
```

For noncontainment, suppose `g` were code-explainable on `S_J`. Then `g-c_g` would be supported on `J`, so

```text
y_1 in W_J.
```

But `W_J` is the span of the Vandermonde columns at the `j` points of `J`, while `y_1` is the column at `beta`. The `j+1` points `J union {beta}` are distinct, and

```text
j+1 <= j+sigma = r.
```

Hence the `j+1` Vandermonde columns are independent, contradiction. Thus `g` is not code-explainable on `S_J`, which is stronger than failure of simultaneous explanation of `f` and `g`.

## 4. Cycle84 Instantiation

The Cycle84 transfer supplies native supports `J_T subset D_0=<eta>` of size `113` with locators

```text
P_T(X) = X^113 - X^112 + O(X^107)
```

and evaluation identity

```text
P_T(beta) = 4(beta-1) Phi(T).
```

The exact imported finite occupancy is

```text
#{ Phi(T) : T in P_0 } = 52,747,567,092.
```

Now work in

```text
K = F_17^32,
H = <theta> = D_0 union theta D_0,
theta^2 = eta,
ord(eta)=256,
ord(theta)=512.
```

Partition the odd coset as

```text
A* = { theta eta^i : 0 <= i <= 119 }, |A*|=120,
R* = { theta eta^i : 120 <= i <= 255 }, |R*|=136.
```

Define

```text
J_T* = J_T union R*,
P_T* = P_R* P_T.
```

This union is disjoint: `J_T subset D_0`, while `R* subset theta D_0`, and
`H = D_0 disjoint_union theta D_0`. Thus `P_T*` is the square-free locator of
`J_T*`.

Then

```text
|J_T*| = 113 + 136 = 249,
|H \ J_T*| = 512 - 249 = 263.
```

Since `deg P_R*=136` and `deg(P_T-P_T') <= 107`,

```text
deg(P_T* - P_T'*) <= 136 + 107 = 243.
```

For

```text
j=249,
sigma=7,
```

this is exactly

```text
j - sigma + 1 = 243.
```

So the augmented locators have the common top six coefficients required by the two-ended theorem.

The constant coefficient is also common and nonzero. The block-color identity gives

```text
P_T(0) = -1
```

for every Cycle84 shell tuple, hence

```text
P_T*(0) = -P_R*(0) != 0.
```

The evaluation identity becomes

```text
P_T*(beta)
  = P_R*(beta) 4(beta-1) Phi(T),
```

where the prefactor is fixed and nonzero because `beta notin H`.

Multiplication by a fixed nonzero scalar, inversion, and negation are bijections. Therefore the distinct slope count remains

```text
52,747,567,092.
```

Applying the two-ended theorem with

```text
n=512,
j=249,
sigma=7,
r=256,
k=256
```

gives

```text
LD_sw(RS[K,H,256],263) >= 52,747,567,092.
```

## 5. Strict Radius Arithmetic

At radius

```text
delta = 125/256
```

and length `512`,

```text
delta*n = 250.
```

The Cycle119 witnesses have agreement `263`, hence distance at most

```text
512 - 263 = 249.
```

Thus they satisfy the strict inequality

```text
d_H < 250.
```

This removes the Cycle116 endpoint concern.

## 6. Numerical Threshold

The source line field is

```text
|K| = 17^32
    = 2,367,911,594,760,467,245,844,106,297,320,951,247,361.
```

Exactly,

```text
floor(17^32 / 2^128) = 6.
```

Since

```text
52,747,567,092 > 6,
```

one has

```text
52,747,567,092 / 17^32 > 2^-128.
```

## 7. Local Verification Receipt

The Cycle119 local replay emitted:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

with the checked fields:

```text
n = 512
k = 256
j = 249
sigma = 7
agreement = 263
strict_hamming_distance_upper_bound = 249
distinct_slopes = 52,747,567,092
hidden_seventh_top_coefficient_used = false
two_ended_selector_degrees = [0,250,251,252,253,254,255]
q_gen = q_code = q_line = 17^32
q_chal = null
```

Raw artifacts and replay receipts are stored under:

```text
experimental/notes/m1/cycle119_role05_twoended_qchal_goldilocks_9pro_returns_raw/
```

The director audit is:

```text
experimental/notes/m1/m1_cycle119_role05_twoended_qchal_goldilocks_returns_audit.md
```

## 8. Non-Claims

This packet does not claim:

```text
ordinary fixed-word list decoding;
protocol soundness failure;
an asymptotic theorem;
an official Proximity Prize solve without definition matching;
a prime-field theorem for this exact Cycle84 row;
any independent q_chal denominator;
any challenge-map or event-retention theorem.
```

It claims a finite/source support-wise MCA and `LD_sw` theorem. Prize status depends on whether the official grand MCA challenge uses this same row/predicate/sampler convention.

## 9. Exact Question for PRZ / ABF

```text
Does the official grand MCA challenge admit the row

  RS[F_17^32,H,256], |H|=512,

with H a smooth multiplicative subgroup, gamma sampled uniformly from F_17^32,
and epsilon_mca interpreted as the support-wise same-support noncontainment
predicate used above?

If yes, the Cycle119 theorem appears to give a counterexample candidate at
delta=125/256 with epsilon_mca > 2^-128.

If no, what is the first rejected clause?
```
