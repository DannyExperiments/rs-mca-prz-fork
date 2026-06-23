# V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE

**Label: PROOF.** This note imports the hash-bound Cycle84 finite theorem and proves the remaining fixed-jet, Reed--Solomon, smooth-lift, and field-ledger implications. It does not rerun the Cycle84 census.

## 1. Fixed-jet locator-to-MCA lemma

Let `D` be an `n`-point subset of a finite field `F`, let `beta` lie outside `D`, and let `J` range over a family of `j`-subsets of `D`. Put

```text
P_J(X)=prod_{a in J}(X-a).
```

Assume

```text
deg(P_J-P_J') <= j-sigma
```

for every pair. Set `k=n-j-sigma`, `r=n-k=j+sigma`, and `C=RS[F,D,k]`. Define the parity check

```text
(Hw)_m = sum_{x in D} x^m w(x)/L_D'(x),  0<=m<r,
L_D(X)=prod_{x in D}(X-x).
```

Then `ker H=C`. For each `J`, define

```text
e_J(x)=L_D'(x)/((beta-x)P_J'(x))  for x in J,
e_J(x)=0                         for x notin J,
z_J=1/P_J(beta).
```

For `m<j+sigma`, the quotient in `X^m=Q_m P_J+R_{m,J}` is independent of `J`, because long division uses only the common leading `sigma` coefficients. Lagrange interpolation on `J` gives

```text
H e_J = A + z_J B,
A_m=-Q_m(beta),
B_m=beta^m.
```

Let

```text
g(x)=L_D(beta)/(beta-x).
```

Full-domain interpolation gives `Hg=B`. Fix one `J0` and put

```text
f=e_J0-z_J0 g.
```

Thus `Hf=A`, and for every `J`,

```text
c_J=f+z_J g-e_J belongs to C.
```

On `S_J=D\J`, `e_J` vanishes, so `f+z_J g` agrees with `c_J` on `n-j=k+sigma` points.

This witness is noncontained. If `g` agreed on `S_J` with a codeword, then a word supported on `J` would have syndrome `B=(1,beta,...,beta^(r-1))`. But the `j` weighted Vandermonde columns indexed by `J`, together with the column at `beta`, are linearly independent because the points are distinct and `j+1<=r`. Hence `B` is not in the span of the `J` columns.

Therefore one affine line `f+zg` has every `z_J` support-wise MCA-bad. Since inversion is injective on `F*`,

```text
LD_sw(C,n-j) >= #{P_J(beta):J},
epsilon_mca(C,j/n) >= #{P_J(beta):J}/|F|.
```

## 2. Cycle84 native family

Let

```text
F0=F_17[X]/(X^16+X^8+3),
eta=6X^9,
beta=X+2,
D0=<eta>, |D0|=256.
```

The verifier establishes irreducibility, `ord(eta)=256`, and `beta notin D0`.

For each Cycle84 state `(i,a)`, the eight-root polynomial

```text
prod_{e in E_i}(Z-3^e)
```

has zero `Z^7` and `Z^6` coefficients. Consequently every scaled 16-point slot locator is `X^16+O(X^10)`. For

```text
J_T={1} union union_{t=1}^7 eta^t lift(i_t,a_t)
```

this gives

```text
P_T(X)=X^113-X^112+O(X^107).
```

All 336 slot identities are checked exactly:

```text
L_{t,i,a}(beta)=3^t u_t(i,a).
```

Hence

```text
P_T(beta)=(beta-1)3^28 Phi(T)=kappa Phi(T),
kappa=4(beta-1)!=0.
```

The imported finite certificate gives exactly

```text
#{Phi(T): T in P0}=52,747,567,092.
```

Applying the lemma with `(n,j,sigma,k)=(256,113,6,137)` proves

```text
LD_sw(RS[F0,D0,137],143) >= 52,747,567,092,
epsilon_mca(RS[F0,D0,137],113/256)
  >= 52,747,567,092/17^16.
```

## 3. Smooth `[512,256]` row

Because `eta` is nonsquare, `K=F0(theta)` with `theta^2=eta` is `F_17^32`. Moreover `theta^256=-1`, so `ord(theta)=512`. Put

```text
H=<theta>=D0 disjoint_union theta D0.
```

Choose

```text
A={theta eta^i:0<=i<=118},  |A|=119,
R={theta eta^i:119<=i<=255}, |R|=137.
```

For each packet co-support let

```text
J_T^+=J_T union R,
S_T^+=H\J_T^+=(D0\J_T) union A.
```

Then `|J_T^+|=250`, `|S_T^+|=262`, and

```text
deg(P_T^+-P_T'^+) <= 137+107=244=250-6,
P_T^+(beta)=P_R(beta) kappa Phi(T),
P_R(beta) kappa !=0.
```

Applying the same fixed-jet lemma directly on `H`, with `(n,j,sigma,k)=(512,250,6,256)`, proves

```text
C=RS[F_17^32,H,256], |H|=512,
LD_sw(C,262) >= 52,747,567,092,
epsilon_mca(C,125/256)
  >= 52,747,567,092/17^32.
```

The verifier checks

```text
floor(17^32/2^128)=6,
52,747,567,092>6,
```

so the last lower bound is strictly greater than `2^-128`.

## 4. Field ledger and scope

```text
q_gen=q_code=q_line=17^32.
q_chal is unset and unused.
```

The domain contains `theta`, and Frobenius tests exclude every proper subfield of `F_17^32`, so `q_gen=17^32`. The MCA denominator is `q_line`, because the affine parameter ranges over `F_17^32`.

This proves a finite smooth-domain standard Reed--Solomon support-wise MCA / `LD_sw` lower bound. It does not prove an ordinary list-decoding lower bound, a protocol soundness failure, an asymptotic theorem, an official Proximity Prize counterpacket, or an accepted/deployed prime-field theorem.
