# M1 Davenport-Cauchy Width-a Repair

Status: REPAIR / ROUTE_CUT / AUDIT.

This note records a local repair in the Paper-B M1 residue-line route.  It
concerns `def:residue`, `lem:denom`, `thm:normalform`, `thm:closure`,
`prop:noanchor`, `rem:aper`, `conj:B`, and `conj:final-mca`.

This is not an official prize solve, not a protocol soundness claim, not an
ordinary list-decoding theorem, and not a Paper-A no-slack example.  The point
is narrower: the minimal width-`a` Cauchy-Pade identity is exactly a fixed
osculating pencil.  It is not forced by quotient, subfield, Frobenius, or
PGL2 symmetry alone.  The correct next object is a quantitative low-tail
payment theorem.

## 1. Minimal Pade Normal Form

Let `F` be a field, let `alpha in F`, and let

```text
A(X)=prod_{p in P}(X-p),   B(X)=prod_{q in Q}(X-q)
```

be monic degree-`a` polynomials with `A(alpha)B(alpha) != 0`.  The identity

```text
B(alpha)A(X)-A(alpha)B(X)=c(X-alpha)^a,   c != 0
```

is equivalent to

```text
A(X)-rB(X)=(1-r)(X-alpha)^a,
r=A(alpha)/B(alpha),   r != 1.
```

Thus `[A]`, `[B]`, and `[(X-alpha)^a]` are collinear in projective polynomial
space.  This is the fixed-osculating-pencil normal form.

If `P,Q subset H` for a subgroup `H <= F^*`, and `alpha notin H`, then the
identity also forces

```text
P cap Q = empty.
```

Indeed, a common root `x in P cap Q` would give
`0=c(x-alpha)^a`, impossible.

## 2. Cauchy Constant-Translate Form

Put

```text
y_x=(alpha-x)^(-1),
M_P(T)=prod_{p in P}(T-y_p),
M_Q(T)=prod_{q in Q}(T-y_q).
```

Then the same minimal identity is equivalent to

```text
M_P(T)-M_Q(T)=Delta in F^*.
```

Equivalently,

```text
e_j(y_p : p in P) = e_j(y_q : q in Q),  1 <= j <= a-1,
```

and the top elementary symmetric sums differ.  In characteristic `0` or
`>a`, this may also be written as equality of Cauchy power sums through order
`a-1`.

This is the exact width-`a` signed Cauchy-Pade atom condition.  It is a
fixed-pencil condition, not an ordinary Cauchy matroid circuit.

## 3. Wronskian Repair

The naive Davenport/Wronskian line

```text
W(A,B)=A'B-AB' = c'(X-alpha)^(a-1)
```

does not follow from the minimal identity.

The correct formula is

```text
W(A,B)
 = c/B(alpha) * (X-alpha)^(a-1) * (aB(X)-(X-alpha)B'(X))
 = c/A(alpha) * (X-alpha)^(a-1) * (aA(X)-(X-alpha)A'(X)).
```

So `A/B` has a critical point of multiplicity `a-1` at `alpha`, but generally
has a residual critical divisor

```text
G_B(X)=aB(X)-(X-alpha)B'(X)
```

of degree at most `a-1`.  The pure Wronskian statement holds only in special
cases, for example when this polar factor is constant.  In safe
characteristic this means

```text
B(X)=(X-alpha)^a + constant.
```

That is a special power-map or fixed-Mobius branch, not the general minimal
width-`a` case.

## 4. Small Prime-Core Packets

The following computations were checked locally.  They show that literal
prime-core nonexistence is false.

### F23, n=11, a=3

Let

```text
F=F_23,
H=<2>={1,2,4,8,16,9,18,13,3,6,12},
alpha=7,
P={1,2,8},
Q={18,3,12}.
```

Then

```text
A=(X-1)(X-2)(X-8)=X^3+12X^2+3X+7,
B=(X-18)(X-3)(X-12)=X^3+13X^2+7X+19,
A(7)=16,
B(7)=13,
13A(X)-16B(X)=20(X-7)^3.
```

Here `|H|=11` is prime and `F_23` has no proper subfield.  There is no
nontrivial quotient, no subfield descent, and no Frobenius explanation.

### F67, n=11, a=3

Let

```text
F=F_67,
H=<64>={1,64,9,40,14,25,59,24,62,15,22},
alpha=30,
P={1,40,64},
Q={9,15,59}.
```

Then

```text
A=X^3+29X^2+51X+53,
B=X^3+51X^2+10X+8,
A(30)=11,
B(30)=44,
44A(X)-11B(X)=33(X-30)^3.
```

Again the group order is prime, the field is prime, and the packet is not
explained by quotient, subfield, or Frobenius mechanisms.

### F43, n=7, a=3

Let

```text
F=F_43,
H={1,4,16,21,41,35,11},
alpha=2,
P={1,35,11},
Q={4,16,21}.
```

Then

```text
A=X^3+39X^2+X+2,
B=X^3+2X^2+11X+32,
A(2)=39,
B(2)=27,
27A(X)-39B(X)=31(X-2)^3.
```

For this packet the Wronskian has a nonconstant residual critical factor, so
the pure Wronskian/PGL2 route is false.

These packets are finite algebraic audits.  They do not claim large slope
packing or an MCA lower bound.  They only kill the proposed width-`a`
nonexistence and quotient/PGL-only classification.

## 5. Route Cuts

The following lines are false:

```text
prime-core width-a packets do not exist;
minimal Pade identity implies pure Wronskian collapse;
quotient/subfield/Frobenius/PGL2 branches classify all width-a packets.
```

The only universal payment visible from the identity is the fixed-pencil /
minimal Pade branch itself.  If this branch is not quantitatively paid, the
small packets above mark the missing structural term.

One further propagation line is also suspect:

```text
low-tail d=a+h datum implies the existence of a width-a subdatum.
```

A local `d=a+1` example from the audit shows this implication can fail.  Thus
the next theorem should be stated directly at low Pade-tail rank, not derived
from the endpoint `h=0`.

## 6. Next Target

The correct next target is:

```text
M1-LOW-TAIL-PADE-PAYMENT.
```

A useful form is:

```text
lambda(Q)L_P(X)-lambda(P)L_Q(X) = (X-alpha)^a R(X),
deg R <= h,
|P|=|Q|=a+h.
```

For low `h`, prove that these fixed-tail packets contribute only
`n^{1+o(1)}` to the quotient-separated aperiodic residue-line packing after
quotient, subfield, Frobenius, PGL2/fixed-skeleton, tangent/contained,
product-collapse, and recursive descent branches are removed.  If this fails,
produce a growing prime-core fixed-pencil or low-tail family.

After this low-tail branch is paid, the remaining obstruction is the genuinely
wide signed Cauchy-Pade Graver atom.
