# Strict264 quotient-floor obstruction

Status: PROVED under the support-wise finite-slope MCA convention.

## Row

```text
F = F_{17^32}
H <= F^* cyclic subgroup of order 512
C = RS[F,H,256]
a = 264
delta = 1 - 264/512 = 31/64
```

## Quotient construction

Use the quotient map

```text
phi(x) = x^8
```

on `H`.  Since `H` has order `512`, `phi` has fibers of size `8` and image size `64`.

For every `33`-subset `A` of `H^8`, define

```text
L_A(X) = product_{y in A} (X^8 - y).
```

Then `deg L_A = 264`, and `L_A` vanishes on a fiber-union support `S_A` of size `264`.

For the augmented code

```text
C+ = RS[F,H,257]
```

take the received word

```text
U(x) = x^264.
```

Modulo `L_A`, the remainder of `X^264` has only degrees `0,8,16,...,256`, hence has degree at most `256 < 257`.  Therefore each `A` gives a distinct `C+` codeword agreeing with `U` on `264` points.

Thus the augmented list size is at least

```text
L = binom(64,33).
```

## Deep-point conversion

For `alpha in F \ H`, define

```text
f_alpha(x) = U(x)/(x-alpha)
g_alpha(x) = -1/(x-alpha).
```

Every listed augmented codeword `P_A` gives a slope

```text
z_A = P_A(alpha)
```

and a degree-`<256` codeword

```text
Q_A(X) = (P_A(X) - P_A(alpha))/(X-alpha)
```

agreeing with `f_alpha + z_A g_alpha` on the same `264` points.

The explanation is support-wise noncontained because `g_alpha` cannot agree with a degree-`<256` polynomial on more than `256` points.

By the collision-average bound, for some `alpha`, the number `M` of distinct slopes is at least

```text
M >= L / (1 + 256(L-1)/(17^32 - 512)).
```

Since

```text
L > 16
L < 2^64
256(L-1) < 2^72 < 17^32 - 512
```

the denominator is `< 2`, so `M > 8`, hence `M >= 9`.

Finally,

```text
7 * 2^128 > 17^32
```

so seven slopes already beat the `2^-128` budget.  Therefore

```text
epsilon_mca(RS[F_17^32,H,256], 31/64) > 2^-128.
```

## What this does and does not settle

This proves an agreement-264 lower obstruction by quotient-core entropy plus deep-point conversion.  It does not determine the full threshold `delta_C^*`; the next prize-shaped target is the agreement-265 upper bound.
