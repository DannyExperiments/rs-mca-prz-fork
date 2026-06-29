# Row-Minimal Absolute-Cocycle Normal Form

Status: PROVED local lemma / AUDIT.

This note records a local linear-algebra lemma for the absolute-offset
obstructions that arise in the Paper-B residue-line MCA route.  It is not an
official prize solve, not a public leaderboard row, not a protocol soundness
claim, not an ordinary list-decoding theorem, not a Paper-A no-slack example,
and not a proof of `conj:B` or `conj:final-mca`.

The point is narrow: once an offset system fails, a row-minimal obstruction is
only a point-conflict or a Vandermonde divided-difference circuit.  This
reduces the next M1 bridge step to charging these two concrete local objects.

## 1. Setup

Let `F` be a field and let

```text
V = F[X]_<r,     r > 0.
```

Rows are labels `e=(i,x)` with evaluation functional

```text
ev_e = ev_x : V -> F,     f -> f(x),
```

and a chosen anchor value

```text
y_e = y_i(x) in F.
```

In the residue-line application,

```text
y_i(x) = (w_P(x) - z_i B_P(x))/E(x) - c_i(x),
```

where `E` is nonzero on the active domain.  Thus division by `E(x)` is
legitimate.

Call a finite row set `U` row-minimal absolute-defective if there are
coefficients `mu_e in F^*`, `e in U`, such that

```text
sum_{e in U} mu_e f(x_e) = 0       for every f in V,
sum_{e in U} mu_e y_e != 0,
```

and no proper nonempty subset of `U` supports a nonzero annihilator of `V`
with nonzero anchor defect.

## 2. Normal Form

Every row-minimal absolute-defective set `U` is exactly one of the following.

### Type A: Point Conflict

There are two rows at the same field point:

```text
U = {(i,x), (j,x)},
```

with

```text
y_i(x) != y_j(x).
```

The weights are proportional to `(1,-1)`.

### Type B: Vandermonde Circuit

There are `r+1` rows at `r+1` distinct field points

```text
x_0, ..., x_r.
```

The weights are unique up to scalar and are proportional to the barycentric
weights

```text
mu_t = c / prod_{s != t} (x_t - x_s),     c in F^*.
```

The selected anchor values have nonzero `r`-th divided difference:

```text
[x_0, ..., x_r] y != 0.
```

Equivalently,

```text
sum_{t=0}^r mu_t y_t
```

is nonzero.

For `r=1`, two distinct field points form the Type-B case.  Type A is reserved
for repeated rows at the same field point.

## 3. Proof

The only subtle point is that row-minimality is defined using nonzero anchor
defect, not ordinary linear dependence.  Nevertheless it forces ordinary
matroid-circuit minimality.

Let `U` be row-minimal absolute-defective with coefficient vector `mu`.  Suppose
a proper nonempty subset `C subsetneq U` supports an ordinary annihilator
`nu`:

```text
sum_{e in C} nu_e f(x_e) = 0       for every f in V.
```

If

```text
sum_{e in C} nu_e y_e != 0,
```

then `C` itself contradicts row-minimality.

If instead

```text
sum_{e in C} nu_e y_e = 0,
```

choose `e_0 in C` with `nu_{e_0} != 0` and set

```text
mu' = mu - (mu_{e_0}/nu_{e_0}) nu,
```

extending `nu` by zero outside `C`.  Then `mu'` is still an annihilator of
`V`, its anchor defect is still nonzero, and the `e_0` coefficient vanishes.
Since `C` is a proper subset of `U` and every coefficient of `mu` on `U` is
nonzero, `mu'` is supported on a proper nonempty subset of `U`.  This again
contradicts row-minimality.

Thus `U` is an ordinary circuit in the evaluation-row matroid of `F[X]_<r`.

The ordinary circuits are elementary.  If two rows have the same field point,
their evaluation functionals are identical.  A two-row parallel dependence is
therefore a circuit, so row-minimality forces the whole circuit to be exactly
those two rows.  Its anchor defect is nonzero precisely when the two selected
anchor values differ.  This is Type A.

If all field points in `U` are distinct, then any `s <= r` evaluation rows are
independent by Lagrange interpolation: for each selected point one can build a
polynomial of degree `< s <= r` that is `1` there and `0` at the others.  Hence
a distinct-point circuit has at least `r+1` rows.

Any `r+1` distinct evaluation rows are dependent because `dim V=r`, and every
`r` of them are independent.  Therefore the distinct-point circuits are exactly
the `r+1` point circuits.  Solving the Vandermonde relation gives the
barycentric weights

```text
mu_t = c / prod_{s != t} (x_t - x_s).
```

The usual divided-difference identity gives

```text
sum_t mu_t y_t = c [x_0, ..., x_r] y,
```

up to the same nonzero scalar convention for the barycentric weights.  Thus the
anchor defect is nonzero exactly when the selected `r`-th divided difference is
nonzero.  This is Type B.

No characteristic restriction is needed beyond working over a field and using
distinct field points, so all displayed denominators are nonzero.

## 4. Relation To Paper B

The labels `def:residue` and `lem:denom` supply the residue-line and
denominator language, including the condition that `E` is nonzero on the active
domain.  The labels `thm:normalform` and `thm:closure` justify the coordinate
normal form but do not provide a packing estimate.  The warning
`prop:noanchor` remains central: the anchor values `y_i(x)` cannot be deleted
or replaced by a word-free support condition.

The quotient separation in `rem:aper` is not used here.  Type-A and Type-B
absolute cocycles are local obstructions inside a residue-line packet; they are
not themselves quotient-periodic denominator families.

## 5. Consequence For The M1 Route

The previous offset audit showed:

```text
O_i != empty for every retained slope
  => genuine individual marked low-tail witnesses
  => paid by the marked low-tail skeleton theorem.
```

If offset realization fails, the obstruction can now be chosen row-minimal and
therefore has only the two types above.  This is a useful grammar reduction,
but not a packing theorem.

The next local target is:

```text
M1-TYPE-A-AND-MIXED-TYPE-B-PRUNING.
```

The expected statement is that after retaining only slopes with `O_i=empty`,
Type-A point conflicts and mixed-slope Type-B circuits are not primitive
packing walls: they either are common-offset artifacts already bypassed by
individual low-tail payment, or they point to a same-slope Type-B obstruction
inside one unpaid slope.

After that pruning, the genuine hard branch should be:

```text
M1-SAME-SLOPE-VANDERMONDE-DIVIDED-DIFFERENCE-CHARGE.
```

This would ask for a packing or structure theorem for many same-slope
Vandermonde divided-difference defects after quotient, subfield, complete
fiber, complete-shadow, product-collapse, and low-rank branches have been
removed.
