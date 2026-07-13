# Deep-remainder partial-occupancy image theorem

**Status:** proved experimental theorem and exact finite counterexample.

**Lane:** lower reserve / profile envelope.  This corrects the deep-remainder
domination claim in pending PR #712.  It is not a primitive-residual theorem
and does not settle either prize question.

## Statement

Use a degree-`c` folding with `N` quotient fibers and descended coefficient
field `B_phi`.  Normalize the complete-fiber polynomial `phi(X)` to be monic,
so its reciprocal `Phi(Z)=Z^c phi(Z^{-1})` has constant coefficient one.
(For a nonmonic source polynomial, divide by its fixed leading coefficient.)
Assume the quotient points lie in one scalar copy of `B_phi`.  In the
canonical partial-occupancy cell
`Omega_{t,m,p,r}`, a support has the unique form

```text
S=T disjoint_union R disjoint_union phi^{-1}(E),
|T|=t, |E|=m,
R occupies p fibers partially and has |R|=r.            (1)
```

Let `b` be the size of the exceptional set from which `T` is selected, and
put

```text
J_{t,p,r}=binom(b,t) binom(N,p)
            [x^r]((1+x)^c-1-x^c)^p.                   (2)
```

Assume the cell is nonempty, equivalently `J_{t,p,r}>0`.  Then
`J_{t,p,r}` is the exact number of remainder labels `(T,R)`, and

```text
|Omega_{t,m,p,r}|=J_{t,p,r} binom(N-p,m).              (3)
```

For the depth-`w` reciprocal-locator prefix map `Phi_w`, define

```text
d=min(m,floor(w/c)).                                   (4)
```

Then

```text
|Phi_w(Omega_{t,m,p,r})| <= J_{t,p,r}|B_phi|^d,        (5)

|Omega_{t,m,p,r}|/|Phi_w(Omega_{t,m,p,r})|
  >= binom(N-p,m)|B_phi|^{-d}.                         (6)
```

Consequently one prefix fiber has size at least

```text
L_{t,m,p,r}=ceil(binom(N-p,m)/|B_phi|^d).              (7)
```

Equations (5)--(7) hold for arbitrary remainder degree `r`; in particular
they still hold in the strictly deep regime `w<r`.  They do not say that
every deep cell has a large fiber: the right side of (7) may be one.

## Proof

Fix one remainder label `u=(T,R)`.  Write

```text
U_u(X)=Q_T(X)P_R(X).
```

The arbitrary-remainder locator identity gives

```text
Q_S^vee(Z)=U_u^vee(Z)
  (Phi(Z)^m + sum_{j=1}^m v_j(E)Z^{cj}Phi(Z)^{m-j}),   (8)
```

where `Phi(Z)=Z^c phi(Z^{-1})` has constant coefficient one.  The reciprocal
`U_u^vee` also has constant coefficient one, so multiplication by it is an
automorphism of the truncated prefix ring `B[Z]/(Z^{w+1})`.

Modulo `Z^{w+1}`, the bracket in (8) depends only on

```text
v_1(E),...,v_d(E),  d=min(m,floor(w/c)).               (9)
```

The quotient points lie in one scalar copy of `B_phi`, so
`v_j(E)` lies in the corresponding scalar copy of `B_phi`.  The tuple in
(9) therefore has at most `|B_phi|^d` values.  Multiplication by the fixed
unit `U_u^vee` does not increase that number.  Hence every fixed label
produces at most `|B_phi|^d` depth-`w` prefixes.

There are exactly `J_{t,p,r}` labels, proving (5).  Dividing (3) by (5)
proves (6), and pigeonholing proves (7).  The remainder-label multiplicity
cancels; no global recovery of `R` from the prefix is required.

This is the precise failure in the pending #712 domination argument.
Coordinatewise full-field remainder variation does not imply that the joint
prefix image is the Cartesian space `B^w`.  The fixed-remainder unit in (8)
preserves the descended quotient image.

## Exact strict-deep counterexample

Let

```text
B=F_169=F_13[T]/(T^2-2),
theta=2+T,
H=<theta^7>,
D=theta H,
phi(x)=x^2.
```

The element `theta` has order `168`, `|H|=24`, and

```text
D^2=theta^2 F_13^x.
```

Thus squaring is two-to-one on `D`, `N=12`, `c=2`, and `B_phi=F_13`.
Take

```text
(n,a,k,w,c,m,p,r)=(24,12,8,3,2,4,4,4).               (10)
```

This is strictly deep because `w=3<4=r`.  Four partial fibers each contribute
one of two roots, and four complete fibers are chosen from the remaining
eight.  Therefore

```text
J=binom(12,4)2^4=7920,
|Omega|=7920 binom(8,4)=554400,
d=1.                                                   (11)
```

The theorem gives

```text
|Phi_3(Omega)| <= 7920*13=102960,
max_z |Omega intersect Phi_3^{-1}(z)| >= ceil(70/13)=6. (12)
```

The ambient identity pigeonhole floor is only

```text
ceil(binom(24,12)/169^3)=1.                            (13)
```

Hence this strict-deep canonical cell has a proved profile list larger than
the identity floor.  It directly refutes the pending #712 assertion that
deep-remainder cells are identity-dominated.

The exact verifier enumerates every support in (11) and strengthens (12) to

```text
realized prefix image = 86320,
maximum prefix fiber  = 20,
average fiber         = 6930/1079.                     (14)
```

Run

```bash
python3 experimental/scripts/verify_deep_remainder_partial_occupancy_counterexample.py --check
python3 experimental/scripts/verify_deep_remainder_partial_occupancy_counterexample.py --tamper-selftest
```

The verifier is stdlib-only.  Its tamper mode checks the three corresponding
bad quantities for a nonprimitive generator, an incomplete partial-root mask
census, and the wrong full-field denominator in place of `|B_phi|`.

## Exact finite impact

For the full challenge set over `F_169`, the theorem-only list `L=6` gives
the collision-aware pole floor `5`; the exact enumerated list `L=20` gives
pole floor `10`.  The tangent floor at (10) is

```text
min(168,n-a+1)=13.                                     (15)
```

Thus this finite example corrects the profile ledger but does not improve
the row's final lower reserve and does not move a deployed adjacent crossing.

## Asymptotic consequence

In the square tower

```text
n=2(p-1), B=F_{p^2}, B_phi=F_p, c=2,
```

fix `0<alpha<1/2`, take `a/n->alpha`, choose an even identity-crossing depth
`w`, and choose `w<r=o(n)`.  In the cell with one selected point in each of
the `r` partial fibers and

```text
m=(a-r)/2,
```

equation (6) gives

```text
log(|Omega|/|Phi_w(Omega)|)
  >= (h(alpha)/4+o(1))n.                               (16)
```

Indeed, the quotient binomial contributes `(h(alpha)/2+o(1))n`, while
`p^{-w/2}` costs `(h(alpha)/4+o(1))n`.  Choosing, for example,
`r` of order `n/log n` leaves only `exp(o(n))` remainder labels.  Strictly
deep cells therefore retain the quotient field-drop exponent rather than
returning automatically to the identity scale.

For a positive-density remainder `r/n->delta`, assume an admissible square-fold
sequence with one selected point in each partial fiber, `p=r`, `a-r` even,
and `0<delta<alpha<1/2`.  The same calculation gives

```text
e_DR(alpha,delta)
 = (1/2-delta)h((alpha-delta)/(1-2delta))-h(alpha)/4.   (17)
```

At `(alpha,delta)=(1/4,1/16)`, this exponent is positive.  This is a
profile-floor statement, not a distinct-slope upper payment.

## Source compiler

The proof consumes the source interfaces in this order:

1. `thm:exact-partial-occupancy` for (2)--(3);
2. `prop:complete-support-factorization` and the arbitrary-remainder QR5
   identity for (8);
3. `eq:profile-envelope` for the realized-image normalization (6);
4. `prop:exact-prefix-list` for conversion of (7) into a one-row list;
5. the collision-aware pole compiler for the finite lower reserve.

The corrected upper profile envelope must retain this natural cell scale.
A sufficient PEU safety comparison that drops it is invalid.  Failure of
that sufficient comparison is not proof of actual unsafety.

## Nonclaims

This note does not prove:

- a primitive-PEU counterexample; canonical partial-occupancy profiles are
  removed before the primitive residual;
- that the deep cell exceeds the unknown actual maximum fiber of the full
  identity family; the strict comparison is to the identity pigeonhole
  floor used by the ledger;
- a Q, SP, Sidon, Fourier, or residual-ray upper payment at the natural scale;
- catalogue exhaustivity or line uniformity;
- a deployed KoalaBear or M31 threshold crossing;
- Grand MCA, Grand List, or either prize question.

The official score remains `0/2`.  The next exact wall is a natural-scale
upper payment for these deep cells, followed by a source-valid distinct-ray
compiler.
