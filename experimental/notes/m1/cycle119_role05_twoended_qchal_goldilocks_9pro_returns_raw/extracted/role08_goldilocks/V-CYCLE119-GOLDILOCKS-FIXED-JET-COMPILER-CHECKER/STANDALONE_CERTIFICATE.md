# Standalone finite Goldilocks certificate

Let `q=2^64-2^32+1`, `F=F_q`, and
`theta=7^((q-1)/512)=1803076106186727246 mod q`. The deterministic check
`7^((q-1)/2)=-1 mod q`, together with the Proth form
`q=(2^32-1)2^32+1` and `2^32-1<2^32`, proves q prime: every prime divisor r
would have `2^32 | r-1`, hence `r>=2^32+1`, contradicting the existence of a
prime divisor at most `sqrt(q)<2^32` if q were composite. Moreover
`theta^256=-1` and `theta^512=1`, so theta has order 512.

Put `H=<theta>`, `G=H^8`, and let A range over the 31-subsets of G. The map
`x -> x^8` has image size 64 and fiber size 8. Define

```text
J_A={x in H:x^8 in A},  |J_A|=248,
P_A(X)=prod_{x in J_A}(X-x)=prod_{c in A}(X^8-c).
```

There are `M=binom(64,31)` locators. If A differs from B, their degree-31
monic Y-polynomials differ and their difference has degree at most 30; hence
`deg(P_A-P_B)<=240=248-8`. Thus the locators share their top eight
coefficients, which are `1,0,...,0` in degrees 248 through 241.

For beta outside H, pairwise collisions `P_A(beta)=P_B(beta)` contribute at
most 240 beta-values per unordered pair. Averaging over `q-512` choices gives
some beta with collision count at most

```text
floor(240*binom(M,2)/(q-512))
=20,543,782,425,128,147,188.
```

If U is the number of distinct values and the fibers have sizes m_i, then
`sum m_i^2=M+2C`; Cauchy gives `U>=M^2/(M+2C)`. Hence

```text
U >= ceil(M^2/(M+2C))
  = 73,674,899,375,228,060.
```

For completeness, the common-line transfer is proved directly. Let
`r=j+sigma=256`, `k=512-r=256`, and let H_C be the weighted Vandermonde
parity check for `RS[F,H,k]`. For each J, the orthogonal complement of the
span W_J of the J-columns is `P_J F[X]_{<8}`. The common top eight locator
coefficients make the high-coefficient multiplication map
`A -> top_8(P_J A)` independent of J and invertible. Define the linear
functional `ell(Q)=(M^{-1}top_8(Q))(beta)`, let y0 represent ell, and let
`y1=(1,beta,...,beta^255)`. For `Q=P_J A`,

```text
<Q,y0+z y1> = A(beta)*(1+z P_J(beta)).
```

Thus for `z_J=-1/P_J(beta)`, `y0+z_J y1` lies in W_J. Choose common words
f,g with syndromes y0,y1; one may take
`g(x)=(beta^512-1)/(beta-x)`. For each J choose an error word e_J supported
on J with syndrome `y0+z_J y1`; then
`c_J=f+z_J g-e_J` is a degree-<256 RS codeword and agrees with the line point
on `S_J=H\J`, of size 264.

Noncontainment is uniform. If g were degree-<256 explainable on S_J, then its
syndrome y1 would lie in W_J. But the 249 Vandermonde columns indexed by
`J union {beta}` are independent because `249<=256` and all points are
distinct. Therefore y1 is not in W_J.

Distinct nonzero P_J(beta) values give distinct slopes. This proves

```text
LD_sw(RS[F_q,H,256],264) >= 73,674,899,375,228,060.
```

The construction is existential in beta. A fully explicit subpacket is also
available at beta=0. Let gamma=theta^8 and
`A_s={gamma^(s+i):0<=i<=30}`. Translation changes the exponent sum by 31s;
since gcd(31,64)=1, the 64 slopes are distinct. The common line is

```text
u_z(x)=x^263+z*x^(-1).
```

For `S_s=H\J_s`, define

```text
P_{S_s}(X)=prod_{c notin A_s}(X^8-c),
c_s(X)=(X^264+z_s-P_{S_s}(X))/X.
```

Here `P_{S_s}(0)=z_s`, the leading X^264 terms cancel, and all remaining
powers of `P_{S_s}` are multiples of 8, so `deg(c_s)<=255`. On S_s,
`c_s(x)=u_{z_s}(x)`. If a degree-<256 polynomial h agreed with x^(-1) on
264 points, `Xh-1` would be a nonzero degree-at-most-256 polynomial with 264
roots, impossible. Thus the explicit 64-slope packet is support-wise
noncontained.

Scope: finite attached-source `LD_sw`/MCA only. No official row/event/challenge
contract is certified.
