# Symbolic lemmas used by the Cycle118 two-ended checker

These are the universal algebraic implications. The executable checker verifies every finite hypothesis used below.

## 1. Weighted Vandermonde parity check

Let `D` be an `n`-point subset of a field `F`, let `k<n`, put `r=n-k`, and set

```text
L_D(X)=prod_{x in D}(X-x),
h_x=L_D'(x)^(-1) (1,x,...,x^(r-1))^T.
```

Define `H:F^D -> F^r` by `Hw=sum_x w(x)h_x`. Then

```text
ker H = RS[F,D,k].
```

Indeed, for a polynomial `p` of degree `<k` and `0<=m<r`, the polynomial `X^m p(X)` has degree at most `n-2`. Its coefficient of `X^(n-1)` is zero, while Lagrange interpolation identifies that coefficient with

```text
sum_{x in D} x^m p(x)/L_D'(x).
```

Thus the Reed--Solomon code lies in `ker H`. Any `r` columns of `H` are a diagonal rescaling of an `r` by `r` Vandermonde matrix, hence independent. Therefore `rank H=r`, `dim ker H=n-r=k`, and equality follows.

## 2. Locator orthogonal complement

For a `j`-subset `J` of `D`, let

```text
P_J(X)=prod_{a in J}(X-a),
W_J=span{h_a:a in J} subset F^r.
```

Identify a vector `(q_0,...,q_(r-1))` with `Q(X)=sum q_i X^i`. Then

```text
W_J^perp = P_J F[X]_{<r-j}.
```

The vector `Q` is orthogonal to `h_a` exactly when `Q(a)=0`; hence it is orthogonal to every `h_a`, `a in J`, exactly when `P_J` divides `Q`. The degree bound gives the quotient degree.

## 3. Two-ended evaluator lemma

Let every `P_J` be monic of degree `j`. Fix `sigma>=2`, put `r=j+sigma`, and assume

```text
deg(P_J-P_J') <= j-sigma+1
P_J(0)=c != 0
```

for every pair. Thus the coefficients of degrees

```text
j, j-1, ..., j-sigma+2
```

are common: exactly `sigma-1` top coefficients.

Write

```text
A(X)=a_0+a_1 X+...+a_(sigma-1) X^(sigma-1).
```

Use the `sigma` coordinates of `P_J A` in degrees

```text
0, j+1, j+2, ..., j+sigma-1.
```

The degree-zero coordinate is `c a_0`. For `1<=s<=sigma-1`,

```text
[X^(j+s)] P_J A
  = sum_{m=s}^{sigma-1} [X^(j+s-m)]P_J * a_m.
```

Every locator coefficient appearing here has index between `j-sigma+2` and `j`, so it is common across the family. The resulting matrix from `(a_0,...,a_(sigma-1))` to the selected coordinates is block triangular: its first diagonal entry is `c`, and the remaining diagonal entries are the monic coefficient `1`. Its determinant is `c`, hence it is invertible.

Consequently one common linear functional `ell:F[X]_{<r}->F`, supported only on those selected coordinates, satisfies

```text
ell(P_J A)=A(beta)
```

for every `J` and every `A` of degree `<sigma`. This uses no common seventh top coefficient when `sigma=7`: the missing multiplier coefficient `a_0` is recovered from the constant endpoint.

## 4. Common affine line and all explaining codewords

Let `y_0` represent `ell` under coefficient pairing, and let

```text
y_1=(1,beta,...,beta^(r-1))^T.
```

For `Q=P_J A` in `W_J^perp`,

```text
<Q,y_0+z y_1>
 = A(beta) + z P_J(beta) A(beta).
```

Because `beta` lies outside `D`, `P_J(beta)` is nonzero. At

```text
z_J=-P_J(beta)^(-1),
```

the displayed pairing vanishes for every `A`, hence `y_0+z_J y_1` lies in `W_J`.

Choose any `f,g` with `Hf=y_0` and `Hg=y_1`. For each `J`, choose the unique `J`-supported word `e_J` with

```text
He_J=y_0+z_J y_1.
```

Uniqueness follows because the `j` columns indexed by `J` are independent. Then

```text
c_J=f+z_J g-e_J
```

lies in `ker H=RS[F,D,k]`, and `f+z_J g` agrees with `c_J` on `D\J`.

For the present instance, the checker fixes a deterministic right inverse using the even subgroup `D_0=<eta>` of size `r=256`. For any syndrome `y=(y_0,...,y_255)`, define a word supported on `D_0` by

```text
w_y(x)=L_H'(x) * (1/256) * sum_{m=0}^{255} y_m x^(-m),  x in D_0,
w_y(x)=0,                                                x in theta D_0.
```

Since `D_0` has order `256`,

```text
sum_{x in D_0} x^(m-s) = 256 if m=s, and 0 otherwise
```

for `0<=m,s<256`. Therefore `H w_y=y`. This deterministically defines the one common line by `f=w_(y_0)` and `g=w_(y_1)`.

## 5. Support-wise noncontainment

Suppose `g` agreed on `D\J` with a codeword. Then `g-c_g` would be supported on `J`, so `Hg=y_1` would lie in `W_J`. But `y_1` is the Vandermonde column at `beta`, whereas `W_J` is spanned by diagonally rescaled columns at the points of `J`. Since `beta` is distinct from all points of `J` and

```text
j+1 <= r,
```

the columns indexed by `J union {beta}` are independent. This is impossible. Hence no pair of codewords explains `f` and `g` on the same agreement support.

## 6. Cycle84 constant and common-jet identities

Every checked slot locator has the form

```text
L_(t,i,a)(X)=prod_{b in B_(i,a)} (X^2-eta^(2t) 3^b)
```

with eight factors and `eta^16=3`. Therefore

```text
L_(t,i,a)(0)=eta^(16t) 3^(sum B_(i,a))
            =3^(t+color(i,a)).
```

The imported Cycle84 shell is exactly the shell with total color `4 mod 16`. Since `sum_{t=1}^7 t=28`, its seven-block product has constant

```text
3^(28+4)=3^32=1 in F_17.
```

The native locator includes `(X-1)`, so every native locator satisfies `P_T(0)=-1`.

The executable checks every slot locator is `X^16+O(X^10)`. Hence the product of seven moving blocks is `X^112+O(X^106)`, and multiplication by `(X-1)` gives

```text
P_T(X)=X^113-X^112+O(X^107).
```

Thus `deg(P_T-P_T')<=107` for all shell tuples.

## 7. Cycle118 instantiation

Let

```text
A*={theta eta^i:0<=i<=119},
R*={theta eta^i:120<=i<=255}.
```

They partition the odd coset, with sizes `120` and `136`. Put

```text
J_T*=J_T union R*,
P_T*=P_R* P_T.
```

Then `|J_T*|=113+136=249`, and

```text
deg(P_T*-P_T'*) <= 136+107 = 243 = 249-7+1.
```

Moreover

```text
P_T*(0)=-P_R*(0) != 0.
```

The two-ended evaluator lemma applies with

```text
n=512, j=249, sigma=7, r=256, k=256.
```

The checked product identity is

```text
P_T*(beta)=P_R*(beta) * 4(beta-1) * Phi(T),
```

whose prefactor is fixed and nonzero. Therefore the exact imported occupancy

```text
#{Phi(T)}=52,747,567,092
```

is also the number of distinct locator evaluations and distinct slopes.

Every explaining error is supported on `249` coordinates, hence every constructed point has distance at most `249`. Since

```text
(125/256)*512=250,
```

every point is strictly inside the distance-`250` ball.
