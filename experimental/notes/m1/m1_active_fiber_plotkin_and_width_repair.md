# M1 Active-Fiber Plotkin and Width Repair

Status: PROVED / REPAIR / ROUTE_CUT / AUDIT.

This note records a Paper-B-native repair to the shifted-local residue-line
route.  It concerns `def:residue`, `lem:denom`, `thm:normalform`,
`thm:closure`, `prop:noanchor`, `conj:B`, and `conj:final-mca`.

This is not an official prize solve, not a protocol soundness claim, not an
ordinary list-decoding theorem, and not a Paper-A no-slack example.  The point
is narrower: fixed-base active-fiber packing gives a real local payment, but it
does not by itself pay the global Paper-B slope ledger.  The correct next
object is a fibered convolution ledger plus a primitive no-tensor-amplification
theorem.

## 1. Shifted-Local Setup

Let `F=F_q` be a prime field, let `H <= F^*` be cyclic of order `n`, and let

```text
alpha in F^* \ H,    1 <= a < n,    M=2^ceil(log_2 a),    M | n.
```

Put `Q=H^M`, and write

```text
C_beta={x in H : x^M=beta},    beta in Q.
```

For a support `S subset H`, define

```text
L_S(X)=prod_{x in S}(X-x),
J_S(Y)=L_S(alpha+Y)/L_S(alpha).
```

For a fixed truncation `W in 1+Y F[Y]/(Y^a)` and fixed support size `s`, write

```text
F(W,s)={S subset H : |S|=s, J_S(Y) == W(Y) mod Y^a}.
```

This is the one-pole shifted-local support fiber attached to the residue-line
denominator `E=(X-alpha)^a`.

## 2. Fixed-Base Active-Fiber Packing

Fix `S_0 in F(W,s)`.  Let

```text
U=C_{beta_1} union ... union C_{beta_r},    |U|=rM,
```

and define the anchored active-fiber packet

```text
F_U(S_0)={S in F(W,s) : S triangle S_0 subset U}.
```

Then every two distinct `S,T in F_U(S_0)` satisfy

```text
|S triangle T| >= 2a.
```

Indeed, put

```text
A=S \ T,    B=T \ S,    C=S cap T.
```

Since all supports have the same size, `|A|=|B|=:m`.  The congruence
`J_S == J_T mod Y^a` allows cancellation of the common locator `L_C`, because
`alpha notin H`, and gives

```text
L_A(X) - Lambda L_B(X) divisible by (X-alpha)^a,
Lambda = L_A(alpha)/L_B(alpha).
```

If `0<m<a`, then the left side has degree `<a`, hence vanishes identically.
Both locators are monic, so `Lambda=1` and `L_A=L_B`; since `A` and `B` are
disjoint, this forces `A=B=empty`, contradicting `S != T`.  Hence `m>=a`.

Thus the words

```text
1_{S cap U},    S in F_U(S_0),
```

form a constant-weight binary code of length `rM` and minimum Hamming distance
at least `2a`.  In particular, the ordinary Plotkin bound gives, whenever
`rM<4a`,

```text
|F_U(S_0)| <= 4a/(4a-rM).
```

For `r=2`,

```text
|F_{C_beta union C_gamma}(S_0)| <= 2a/(2a-M).
```

Summing over all two-fiber pairs in the positive-reserve window
`a >= C n/log n`, `a <= M < 2a`, gives

```text
O((n/M)^2 * 2a/(2a-M)) <= O_C(n log n)=n^{1+o(1)}.
```

So anchored two-fiber support packets are paid.

## 3. Local Packet-To-Slope Injection

The preceding bound is useful for Paper B only after translating supports to
residue-line slopes in the one-pole normal form.

Let

```text
E=(X-alpha)^a,    B(X)=W(X-alpha).
```

For `S in F(W,s)`, one has

```text
L_S(X) == L_S(alpha) B(X) mod E.
```

In the standard one-pole residue-line datum with

```text
w=(E X^k)|_H,    s=k+a,
```

the polynomial

```text
Q_S(X)=E(X)X^k - L_S(X)
```

satisfies `Q_S=w` on `S` and has residue

```text
Q_S == -L_S(alpha) B mod E.
```

Thus the Paper-B slope attached to `S` is

```text
z_S=-L_S(alpha).
```

Consequently, inside any fixed anchored packet `F_U(S_0)`, support counts bound
slope counts.  This is a local packet-to-slope injection, not a global slope
ledger theorem.

## 4. High-Width Lemma

Let `I subset Q`, `|I|=r`, and set

```text
H_I=union_{beta in I} C_beta,
D_I(X)=prod_{beta in I}(X^M-beta).
```

For a nonzero defect `tau:H_I -> {-1,0,1}`, define

```text
F_tau(X)=sum_{x in H_I} tau(x)/(X-x)=N_tau(X)/D_I(X).
```

Assume the shifted-local moment equations

```text
sum_x tau(x)(alpha-x)^(-j)=0,    1 <= j < a.
```

Since `alpha notin H`, `D_I(alpha) != 0`, and the moment equations are
equivalent to

```text
ord_{X=alpha} N_tau >= a-1.
```

Write the numerator in global `M`-residue classes:

```text
N_tau(X)=sum_{u=0}^{M-1} X^u N_u(X^M),
w_M(N_tau)=#{u : N_u != 0}.
```

Each nonzero summand `X^u N_u(X^M)` is a lacunary polynomial with at most `r`
monomials.  A nonzero polynomial supported on `L` distinct monomials of degree
`<q` cannot vanish to order `L` at a nonzero point.  Applying this to the sum
of `w_M(N_tau)` residue classes gives

```text
w_M(N_tau) >= ceil(a/r).
```

The off-by-one matters: the moments `1 <= j < a` force multiplicity `a-1`,
not `a`.  The balance equation `sum tau=0` is a condition at infinity, not an
extra vanishing condition at `alpha`.

This kills complete-fiber, bounded-character, low-mode cyclic, and small
dyadic-subfiber skeletons in the shifted-local branch with `alpha != 0`.  It
does not by itself count the scalar products

```text
prod_x (alpha-x)^tau(x).
```

## 5. Route Cut: The Naive Global Bridge Fails

The false line is:

```text
fixed-base support-family packing pays the Paper-B slope ledger.
```

Fixed-base Plotkin packing pays anchored active-coordinate multiplicity.  Paper
B counts distinct noncontained slopes for one fixed residue-line datum.  A
bounded active packet can be tensored with many background supports unless the
background spectrum is separately charged, bounded, or reduced.

The corrected slope-level object is the fibered convolution ledger.  For
disjoint `X,Y subset H`, define

```text
P_Z(m,V)={L_A(alpha) : A subset Z, |A|=m, J_A == V mod Y^a}.
```

Then

```text
|P_{X union Y}(s,W)|
 <= sum_{m,V} |P_X(m,V)| * |P_Y(s-m, W V^{-1})|.
```

The Plotkin theorem controls the active factor `P_X(m,V)` when `X` is a union
of a small number of `M`-fibers.  It does not control the background factor.

The missing bridge is therefore a primitive no-tensor-amplification theorem:
a primitive aperiodic residue line cannot be a nontrivial tensor product of a
bounded active collision and a slope-rich background shifted-local fiber unless
the background is charged to quotient compression, fixed-pencil,
low-affine-rank, complete-fiber, affine-cyclic/PGL2-fixed skeleton,
tangent/contained behavior, or to a smaller active-fiber problem.

## 6. Equivalent Divisor Form of the Wall

For an active set `I subset Q`, put

```text
P_I(Z)=prod_{x in union_{beta in I} C_beta} (Z-(alpha-x)^(-1)).
```

A fixed-base active packet can be expressed as a family of monic divisors
`A(Z) | P_I(Z)` with fixed degree and fixed top coefficients, because

```text
J_A(Y)=prod_{x in A} (1+Y/(alpha-x))
```

fixes the leading elementary symmetric data of the reciprocal points
`(alpha-x)^(-1)`.

The central algebraic wall is:

```text
primitive coefficient-isospectral divisor lemma:
monic divisors A(Z) | P_I(Z) with fixed degree and fixed top a coefficients
have only n^{o(1)} primitive constant terms A(0), unless the divisor family is
quotient-compressed, fixed-pencil, low-affine-rank, complete-fiber, or
affine-cyclic/PGL2-fixed.
```

This is equivalent to scalar anti-compensation for the lifted product
coordinate.  A proof only in truncated moment space is insufficient, because
the scalar product is invisible to the bare osculating incidence.

## 7. Remaining Target

The current Paper-B-aligned target is:

```text
M1-PRIMITIVE-NO-TENSOR-AMPLIFICATION-COLD-AUDIT
```

Prove either:

```text
fibered convolution ledger + no-tensor-amplification
```

or equivalently:

```text
central-window coefficient-isospectral divisor rigidity.
```

A genuine counterpacket must produce a scaling primitive residue-line family in
which every bounded active slice is Plotkin-paid, but a slope-rich background
survives all charged branches and yields more than `n^epsilon` distinct slopes;
or produce a primitive divisor family with fixed top `a` coefficients and more
than `n^epsilon` distinct constant terms.
