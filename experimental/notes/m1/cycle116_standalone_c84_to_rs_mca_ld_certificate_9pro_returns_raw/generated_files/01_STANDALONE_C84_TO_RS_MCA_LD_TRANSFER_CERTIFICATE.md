# V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE

## Status

**PROOF.** This note proves a finite support-wise Reed--Solomon MCA / `LD_sw`
certificate. It does not claim an ordinary list-decoding lower bound for the
stated code, a protocol soundness failure, an asymptotic theorem, an official
Proximity Prize counterpacket, or an accepted/deployed prime-field theorem.

## 1. Fixed-jet locator theorem

Let `F` be a finite field, let `D subset F` have size `n`, and let `beta notin D`.
For each member `J` of a family of `j`-subsets of `D`, put

```text
P_J(Y) = product_{a in J} (Y-a).
```

Assume `sigma >= 1`, put `k=n-j-sigma >= 1`, and assume

```text
deg(P_J-P_J') <= j-sigma
```

for every pair. Let

```text
V_D(Y) = product_{a in D}(Y-a),
L_J(Y) = V_D(Y)/P_J(Y) = product_{a in D\J}(Y-a).
```

Then

```text
P_J(L_J-L_J') = (P_J'-P_J)L_J',
```

so

```text
deg(L_J-L_J') <= k.
```

Therefore the coefficients of `L_J` in degrees `k+1,...,k+sigma` are common.
Let `U(Y)` be this common high-degree truncation, and put

```text
E(Y)=Y-beta,     B=1,     w=U|_D,
f(x)=U(x)/(x-beta),     g(x)=-1/(x-beta).
```

For each `J`, define

```text
Q_J(Y)=U(Y)-L_J(Y),
z_J=Q_J(beta),
C_J(Y)=(Q_J(Y)-z_J)/(Y-beta).
```

Because `deg Q_J <= k` and `Q_J(beta)=z_J`, `C_J` is a polynomial of degree
strictly less than `k`. On the support `S_J=D\J`, `L_J` vanishes, hence

```text
C_J(x) = (U(x)-z_J)/(x-beta) = f(x)+z_J g(x).
```

Thus the codeword `C_J|_D` explains the line point on exactly the designated
support of size

```text
|S_J|=n-j=k+sigma.
```

Moreover

```text
z_J = U(beta)-L_J(beta)
    = U(beta)-V_D(beta)/P_J(beta).
```

Hence the common reciprocal-affine constants are

```text
alpha=U(beta),     lambda=-V_D(beta) != 0.
```

The witness is support-wise noncontained. If a polynomial `G` of degree less
than `k` agreed with `g` on `S_J`, then

```text
(Y-beta)G(Y)+1
```

would have at least `k+sigma>k` roots and degree at most `k`, while its value at
`Y=beta` is `1`, a contradiction.

This is also exactly a degree-one residue-line datum: `E=Y-beta`, `B=1`,
`w=U|_D`, and `Q_J` has degree less than `k+1`, satisfies `Q_J == z_J B mod E`,
and equals `w` on `S_J`.

The parity-check form is equivalent. With redundancy `r=j+sigma`, use columns

```text
h_x=V_D'(x)^(-1)(1,x,...,x^(r-1))^T.
```

The syndrome of `g=-1/(Y-beta)` is the nonzero scalar
`V_D(beta)^(-1)(1,beta,...,beta^(r-1))^T`. If `g` were explained on `S_J`, this
vector would lie in the span of the `j` Vandermonde columns indexed by `J`,
contradicting independence of the `j+1 <= r` columns indexed by `J union {beta}`.

Since `P_J(beta) != 0`, the map

```text
p -> alpha+lambda/p
```

is injective on `F^*`. Any other prescribed common pair `(alpha',lambda')` with
`lambda' != 0` is obtained by one affine reparameterization of the same line.
Consequently

```text
LD_sw(RS[F,D,k],k+sigma) >= #{P_J(beta):J},

epsilon_mca(RS[F,D,k],j/n) >= #{P_J(beta):J}/|F|.
```

## 2. Cycle84 native instantiation

Let

```text
F0=F_17[xi]/(xi^16+xi^8+3),
eta=6 xi^9,
beta=xi+2,
D0=<eta>.
```

The packet checks `ord(eta)=256`, `eta^16=3`, and `beta notin D0`.
For

```text
E1={0,1,2,3,5,11,12,13},
E2={0,1,2,3,4,8,9,14},
E3={0,1,2,4,5,7,11,14},
```

put `B_{i,a}=a+E_i mod 16` and

```text
Y_{i,a}={y in <eta^8>: y^2 in {3^b:b in B_{i,a}}}.
```

For a seven-state tuple `T=((i_t,a_t))_{t=1}^7`, define the co-support

```text
J_T={1} union union_{t=1}^7 eta^t Y_{i_t,a_t}.
```

Each block has size `16`, the seven cosets are disjoint, and therefore
`|J_T|=113`.

The explicit packet polynomials satisfy

```text
product_{e in E_i}(Z-3^e)=Z^8+O(Z^5),
```

where the coefficients of `Z^7` and `Z^6` vanish. Therefore every block locator
is

```text
R_{t,i,a}(Y)=product_{b in B_{i,a}}(Y^2-eta^(2t)3^b)
            =Y^16+O(Y^10).
```

It follows that

```text
P_T(Y)=product_{a in J_T}(Y-a)
      =(Y-1) product_{t=1}^7 R_{t,i_t,a_t}(Y)
      =Y^113-Y^112+O(Y^107),
```

where `O(Y^107)` means degree at most `107`. Thus the common jet has length
`sigma=6`.

The 336-state factorization checked in the packet is

```text
R_{t,i,a}(beta)=3^t u_t(i,a).
```

Hence

```text
P_T(beta)
=(beta-1)3^(1+...+7) product_t u_t(i_t,a_t)
=(beta-1)3^28 Phi(T)
=4(beta-1)Phi(T).
```

Thus `kappa=4(beta-1) != 0`. The Cycle84 finite certificate gives

```text
#{Phi(T)}=52,747,567,092,
m_max=2,
12 designated double fibers,
no designated fiber of size >=3.
```

The fixed-jet theorem gives

```text
LD_sw(RS[F0,D0,137],143) >= 52,747,567,092,

epsilon_mca(RS[F0,D0,137],113/256)
  >= 52,747,567,092 / 17^16.
```

The fiber statements are statements about the designated Cycle84 packet; the
line may have additional witnesses outside that packet.

## 3. Smooth `[512,256]` lift

The 2-adic valuation of `17^16-1` is `8`. Since `eta` has order `256`, it is a
nonsquare in `F0`. Let

```text
K=F0(theta),     theta^2=eta.
```

Then `K=F_17^32`, `theta^256=-1`, `ord(theta)=512`, and

```text
H=<theta>=D0 disjoint_union theta D0.
```

Choose

```text
A={theta eta^i:0<=i<=118},       |A|=119,
R={theta eta^i:119<=i<=255},     |R|=137.
```

For every native co-support put `J_T^+=J_T union R`. Its locator is
`P_T^+=P_R P_T`, and

```text
deg(P_T^+-P_T'^+) <= 137+107 = 244 = 250-6,
P_T^+(beta)=P_R(beta) kappa Phi(T),
```

with the common scalar nonzero. Applying the fixed-jet theorem with

```text
n=512,     j=250,     sigma=6,     k=256
```

gives witness support

```text
H\J_T^+ = (D0\J_T) union A,
```

of size `143+119=262`. Therefore, for

```text
C=RS[F_17^32,H,256],     |H|=512,
```

one has

```text
LD_sw(C,262) >= 52,747,567,092,

epsilon_mca(C,125/256)
  >= 52,747,567,092 / 17^32.
```

Literal agreement padding preserves the same slopes and noncontainment. Given
the native line and its explaining polynomial `p_z`, multiply both line words
on `D0` by `L_A`, set them to zero on `A union R`, and use `L_A p_z` as the new
explaining polynomial. If degree-`<256` polynomials simultaneously explained
the lifted anchor and direction on `S_z union A`, both would vanish on all 119
points of `A`, hence would be divisible by `L_A`; division would produce
simultaneous degree-`<137` explanations on `S_z`, contradicting the native
noncontainment.

## 4. Field ledger and exact comparison

For the smooth row,

```text
q_gen=q_code=q_line=17^32
=2,367,911,594,760,467,245,844,106,297,320,951,247,361.
```

The MCA denominator is `q_line`, because the line parameter ranges over the
code field. `q_chal` is not instantiated by this finite certificate.

Exactly,

```text
floor(17^32/2^128)=6,
52,747,567,092>6,
```

so

```text
52,747,567,092/17^32 > 2^-128.
```

## 5. Scope

Proved: a finite smooth-domain support-wise MCA / `LD_sw` row with the displayed
parameters and lower bound.

Not proved: an ordinary list-decoding lower bound for this target code, a
protocol soundness failure, an asymptotic theorem, an official Proximity Prize
counterpacket, or an accepted/deployed prime-field theorem.
