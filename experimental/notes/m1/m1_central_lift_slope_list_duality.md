# M1 Central-Lift Slope/List Duality

Status: PROVED / REPAIR / ROUTE_CUT / AUDIT.

This note records a Paper-B-native identity for the central-lift branch of
residue-line packing.  It concerns `def:residue`, `thm:normalform`,
`thm:closure`, `prop:noanchor`, `conj:B`, and `conj:final-mca`.

This is not an official prize solve, not a protocol soundness claim, not an
ordinary list-decoding theorem for arbitrary anchors, and not a Paper-A
no-slack example.  The point is narrower: a central residue-line slope count
is exactly a reciprocal leading-coefficient count for ordinary polynomial
agreements with the rational word `B/E`.  The arbitrary-anchor problem remains
the stronger affine residue-code local-list problem.

## 1. Algebraic Identity

Let `F` be a field, let `H subset F`, and let `k>=1`, `a>=1`.  Put `s=k+a`.
Let `E in F[X]` be monic of degree `a`, with `E(x) != 0` for all `x in H`.
Let `B in F[X]_<a` be nonzero.

For `S subset H`, `|S|=s`, define

```text
L_S(X)=prod_{x in S}(X-x).
```

Then for `z in F^*`,

```text
L_S == -zB mod E
```

if and only if there is a unique polynomial `P in F[X]`, `deg P<=k`, such that

```text
P(x)=B(x)/E(x) for all x in S,
[X^k]P=1/z.
```

The maps are

```text
P=(L_S+zB)/(zE)
```

and conversely, with `c=[X^k]P`,

```text
EP-B=cL_S,    c != 0,    z=1/c.
```

Proof.  If `L_S == -zB mod E`, then `E` divides `L_S+zB`, and the displayed
formula defines `P`.  Since `L_S` and `E` are monic of degrees `k+a` and `a`,
and `deg B<a`, one has `deg P=k` and `[X^k]P=1/z`.  On `S`, the locator
vanishes, so `P=B/E`.  Uniqueness follows because two degree-`<=k`
polynomials agreeing on `k+a>k` points are equal.

Conversely, suppose `P=B/E` on `S` and `c=[X^k]P`.  If `c=0`, then `EP-B`
has degree `<k+a` and `k+a` roots, so `EP-B=0`, forcing `B=EP`; this is
impossible for nonzero `B` with `deg B<a`.  Thus `c!=0`.  Now `EP-B` has
degree `k+a`, leading coefficient `c`, and vanishes on all points of `S`.
Hence `EP-B=cL_S`, and reducing modulo `E` gives `L_S == -c^{-1}B mod E`.

The proof is field-level degree/root-counting.  It does not use finiteness or
squarefreeness of `E`.  Monicity fixes the exact coefficient normalization; if
the leading coefficient of `E` is `lambda`, the coefficient rule becomes
`[X^k]P=1/(lambda z)`.

## 2. Residue-Line Realization

For the central anchor

```text
w(x)=E(x)x^k on H
```

define

```text
Q_z=E X^k-L_S.
```

Then

```text
deg Q_z<k+a,
Q_z == zB mod E,
Q_z=w on S.
```

Indeed, the leading terms of `E X^k` and `L_S` cancel, while modulo `E` one
has `Q_z == -L_S == zB`.  On `S`, `L_S` vanishes.

Moreover,

```text
(Q_z-zB)/E = X^k-zP in F[X]_<k,
```

because `[X^k]P=1/z`.  Thus this is a valid instance of Paper B's residue-line
normal form for the central-lift datum `(E,B,w)`.

These witnesses are noncontained in the central branch.  No degree-`<k`
polynomial agrees with `X^k` on `k+a` points.  Likewise, if
`G in F[X]_<k` agreed with `-B/E` on `S`, then `EG+B` would have degree
`<k+a` and `k+a` roots, forcing `EG=-B`, impossible for nonzero `B` with
`deg B<a`.

## 3. Slope Spectrum

The central-lift bad-slope set is therefore

```text
{ z in F^* :
  exists P in F[X], deg P<=k,
  |{x in H : P(x)=B(x)/E(x)}| >= k+a,
  z=1/[X^k]P }.
```

For nonzero `B`, the agreement threshold `>=k+a` is automatically exact for
each counted polynomial: if agreement were larger, `EP-B` would have more than
`k+a` roots while having degree `k+a`, hence would vanish identically and
force `E` to divide `B`.

Thus central-lift slope counting is not full list-size counting.  It is
counting distinct nonzero leading coefficients among the corresponding
rational-word agreements.

## 4. Route Cut for Arbitrary Anchors

The preceding identity does not reduce arbitrary Paper-B residue lines to
ordinary Reed-Solomon list decoding of `B/E`.

For a general residue-line datum `(E,B,w)`, a witness is equivalently

```text
E R+zB=w on S,    R in F[X]_<k.
```

After dividing by `E` on `H`, this becomes

```text
R+z(B/E)=w/E on S.
```

Only the special central anchor `w/E=X^k` turns this into ordinary polynomial
agreement with the fixed rational word `B/E` and converts the slope into a
leading coefficient.  More generally, polynomial anchors `w=EW` with
`deg W=k` and leading coefficient `lambda` give `[X^k]P=lambda/z` after
scaling.  Arbitrary anchors require a slope-coordinate local-list bound for
the affine residue-extension code

```text
E RS_<k + <B>.
```

The false line is therefore:

```text
Every residue-line datum (E,B,w) reduces to ordinary RS list decoding of B/E.
```

## 5. Next Exact Targets

The central-lift target is the leading-coefficient rational-word local limit:

```text
|{ [X^k]P in F^* :
    deg P<=k,
    |{x in H : P(x)=B(x)/E(x)}| >= k+a }|
<= n^{1+o(1)}
```

after quotient-periodic, fixed-pencil, low-rank, complete-fiber, PGL2, and
subfield branches are removed or separately budgeted.

The full Paper-B target remains stronger:

```text
|{ z in F :
    exists R in F[X]_<k with
    |{x in H : E(x)R(x)+zB(x)=w(x)}| >= s_delta,
    noncontained }|
<= n^{1+o(1)}
```

after the floor, quotient, and aperiodic corrections of `conj:B`.
