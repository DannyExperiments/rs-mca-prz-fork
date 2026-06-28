# Fixed-Prefix Low-Tail Cauchy-Locator Packing

Status: PROVED local lemma / AUDIT.

This note proves a fixed-prefix support-packing lemma and records its
one-pole Cauchy-Pade form.  It is not an official prize solve, not a protocol
soundness claim, not an ordinary list-decoding theorem, not a Paper-A
no-slack example, not a proof of full arbitrary-anchor M1, not a proof of
`conj:B`, and not a proof of `conj:final-mca`.  It also does not show that
the quotient reserve or quotient-periodic separation can be ignored.

## 1. Fixed-Prefix Packing Lemma

Let `F` be a field and let `Y subset F` be a set of `n` distinct points.  Let
`a >= 1`, `h >= 0`, and `d=a+h <= n`.  For each `d`-subset `S subset Y`, set

```text
M_S(T) = prod_{y in S} (T-y)
       = T^d - e_1(S)T^(d-1) + e_2(S)T^(d-2) - ... + (-1)^d e_d(S).
```

Fix values of `e_1,...,e_(a-1)`, and let `F_c` be the family of all
`d`-subsets `S subset Y` with those values.  Then distinct `S,S' in F_c`
satisfy

```text
|S cap S'| <= h.
```

Consequently,

```text
|F_c| <= binom(n,h+1) / binom(a+h,h+1).
```

### Proof

For `S,S' in F_c`, the coefficients of

```text
T^(d-1), T^(d-2), ..., T^(h+1)
```

in `M_S-M_S'` vanish.  Since `d=a+h`, this gives

```text
deg(M_S-M_S') <= h.
```

Every point of `S cap S'` is a root of this difference.  If
`|S cap S'| >= h+1`, then `M_S-M_S'` has more distinct roots than its degree
and is therefore zero.  Since `M_S` and `M_S'` are monic and split over the
distinct set `Y`, equality of the polynomials implies `S=S'`.  Thus distinct
members of `F_c` intersect in at most `h` points.

Therefore no `(h+1)`-subset of `Y` lies in two distinct members of `F_c`.
Counting pairs `(U,S)` with `U subset S`, `|U|=h+1`, and `S in F_c`, gives

```text
|F_c| binom(a+h,h+1) <= binom(n,h+1),
```

as claimed.

## 2. One-Pole Cauchy-Pade Form

Let `H` be a finite subset of `F`, let `alpha notin H`, and put

```text
y_x = (alpha-x)^(-1).
```

For `P subset H`, define

```text
L_P(X) = prod_{p in P} (X-p),
lambda(P) = L_P(alpha),
M_P(T) = prod_{p in P} (T-y_p).
```

Let `|P|=|Q|=d=a+h`.  With

```text
T = (alpha-X)^(-1),
```

one has

```text
L_P(X) = lambda(P) T^(-d) M_P(T),
```

and hence

```text
lambda(Q)L_P(X) - lambda(P)L_Q(X)
  = lambda(P)lambda(Q)T^(-d)(M_P(T)-M_Q(T)).
```

Since `d=a+h`, the identity

```text
lambda(Q)L_P(X) - lambda(P)L_Q(X) = (X-alpha)^a R(X),
deg R <= h,
```

is equivalent to

```text
deg(M_P-M_Q) <= h.
```

Equivalently, `P` and `Q` have the same first `a-1` elementary symmetric
coefficients in the Cauchy coordinates `y_x=(alpha-x)^(-1)`.

## 3. Slope Counting In One Fixed Fiber

For Paper-B residue-line packing, slope counting needs one additional
noncontainedness observation.  Fix one residue-line datum `(E,B,w)`.  A single
support cannot witness two distinct noncontained slopes.

Indeed, if the same support `S` witnessed slopes `z != z'`, write

```text
Q_z  = zB  + E A_z,
Q_z' = z'B + E A_z',
```

with `deg A_z, deg A_z' < k`.  Since both witnesses equal `w` on `S`,

```text
(z-z')B + E(A_z-A_z') = 0  on S.
```

Thus `(A_z-A_z')/(z-z')` is a degree-`<k` polynomial agreeing with `-B/E` on
`S`.  Combining this direction explanation with either witness gives a
degree-`<k` polynomial agreeing with `w/E` on `S`.  This is containment,
contradicting noncontainedness.

Hence, after fixing a noncontained datum and a fixed Cauchy-prefix fiber, one
may select one witnessing support for each slope and obtain an injection from
slopes into supports.  The slope count in that fixed fiber is therefore
bounded by the support count in Section 1.

## 4. Corrected-Reserve Consequence

The exact packing bound gives

```text
|F_c| <= prod_{i=0}^h (n-i)/(a+h-i) <= (n/a)^(h+1).
```

If `a >= c n/log n` for fixed `c>0`, then

```text
|F_c| <= (O_c(log n))^(h+1).
```

Thus fixed `h` gives a polylogarithmic bound per fixed prefix fiber.  If

```text
h = o(log n/log log n),
```

then

```text
|F_c| = n^{o(1)}.
```

At the endpoint

```text
h+1 <= (1+o(1)) log n/log log n,
```

the same estimate gives `n^{1+o(1)}`.

At `h=0`, one fixed width-`a` Cauchy-prefix fiber has size at most `n/a`.
Thus width-`a` packets may exist, but a single fixed prefix fiber is
quantitatively small in the corrected-reserve range.

## 5. Relation To Paper B

In Paper B, `def:residue` and `lem:denom` introduce residue-line data and
witnesses, while `thm:normalform` reduces all-line MCA questions to bounding
the maximum noncontained residue-line packing number.  The proposition
`thm:closure` is only a coordinate normal form and gives no packing estimate.
The theorem `thm:onez` supplies the one-bad-parameter-per-support principle
used in Section 3.  The lemma `lem:pairwise` contains the same
prefix-intersection spine in the locator-fiber setting; the present note
isolates its low-tail Cauchy-Pade packing consequence.

The quotient-periodic separation in `rem:aper` remains external to this
lemma.  The global aperiodic packing prediction in `conj:B` and the final
MCA statement `conj:final-mca` remain open.

## 6. Remaining Obstruction

This lemma bounds one fixed prefix fiber.  It does not bound a union of many
moving prefix fibers, nor does it handle the medium or wide Pade-tail range
where the binomial estimate is no longer enough.

The next low-tail target is:

```text
M1-MOVING-PREFIX-NO-TENSOR-AMPLIFICATION.
```

The companion medium/wide-tail target is:

```text
M1-MID-TAIL-TO-WIDE-PADE-GRAVER-RIGIDITY.
```
