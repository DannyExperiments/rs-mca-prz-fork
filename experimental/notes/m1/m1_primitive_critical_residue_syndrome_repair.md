# M1 Primitive Critical Residue-Syndrome Repair

Status: PROVED / AUDIT / COUNTEREXAMPLE TO THE TOY `T_res=82` CAP / EXPERIMENTAL FINITE PACKETS.

This note records the reusable part of the Paper-B residue-line audit around
`def:residue`, `lem:denom`, `thm:normalform`, `thm:closure`,
`prop:noanchor`, `conj:B`, and `rem:aper`.  It is not an official prize solve,
not a protocol soundness claim, not an ordinary list theorem except where a
list-transfer injection is explicitly stated, and not a refutation of Paper B's
corrected positive theory above its full reserve.

## 1. Primitive and Minimal Normalization

Let `C_k = RS[F,D,k]`.  For a direction class `[g] in F^D/C_k`, define

```text
tau_k([g]) = min deg E
```

over representations

```text
g = R - B/E on D,  deg R < k,  deg B < deg E,  E|_D nonzero,
```

with `tau_k(0)=0`.

If `C | gcd(E,B)` and `E` is nonzero on `D`, pointwise division

```text
(E,B,w,Q) -> (E/C, B/C, w/C, Q/C)
```

gives a slope- and support-preserving bijection of residue-line witnesses.  It
also preserves tangent, contained, and noncontained status.  Thus common
displayed denominator factors are gauge, not structure.

The displayed denominator degree is not intrinsic.  Primitive
`gcd(E,B)=1` does not imply minimality, and minimal denominators need not be
unique in general.  Quotient-periodicity in `rem:aper` should therefore be
attached to the direction class, for example by the priority rule:

```text
[g] is quotient-periodic if some tau_k([g])-minimizing representation
has denominator E(X)=E0(X^M), up to scalar, for a proper M | gcd(n,k).

[g] is aperiodic if no minimizing representation has such a denominator.
```

When `t=tau_k([g])` and `2t <= n-k`, the minimizing denominator is unique up to
scalar by cross-multiplication and reduced-fraction uniqueness; in that range
the quotient test is unambiguous.

## 2. Fixed-Support Trichotomy

For a support `S`, define

```text
V_S(E,B,w) = { z in F : exists A in F[X]_<k with E A + z B = w on S }.
```

If two distinct slopes lie in `V_S`, subtraction gives a direction explanation
`E G + B = 0` on `S`; combining with one witness also gives an anchor
explanation `E A0 = w` on `S`.  Hence `S` is contained and `V_S = F`.
Therefore every noncontained support carries at most one slope:

```text
V_S is empty, a singleton, or all of F;
the all-of-F case is contained.
```

This kills the attempted support-local environmental term.  There is no
separate `Z_env` paid term at this level; the surviving hard object is the
aperiodic noncontained packing problem already represented by `conj:B`.

## 3. Low-Denominator List Transfer

For a minimal representation

```text
g = R - B/E,  deg E = t > 0,  deg B < t,
```

each witnessed bad slope `z` injects into the ordinary list for
`RS[D,k+t]` at the same agreement threshold.  If `P_z` is the codeword agreeing
with `f+zg` on `S_z`, set

```text
Q_z = E(P_z - zR) + zB.
```

Then `deg Q_z < k+t` and `Q_z` agrees with `E f` on `S_z`.  Distinct slopes
give distinct `Q_z`, because equality modulo `E` would force
`(z-z')B == 0 mod E`.

Thus at agreement `k+sigma`,

```text
|Gamma_[g]| <= L_D(k+t, k+sigma).
```

For `t < sigma` this is a low-denominator/list-reducible proof branch whenever
an ordinary list bound is available for `RS[D,k+t]` at residual reserve
`sigma-t`.  That reserve is not automatic from the original rate, so this is a
proof reduction, not a new numerical term in `conj:B`.

The earlier all-97-slope toy datum

```text
E=X^3, B=X^2
```

is low-denominator after primitive normalization:

```text
(X^3, X^2, w) -> (X, 1, w/X^2)
```

where the intrinsic direction has `tau=1`.  It is not high-denominator
evidence and not a Paper-A quotient descent example.

## 4. Critical Residue-Syndrome Image

The hard finite boundary starts at `tau >= sigma`.  At `t=sigma`, for a
support `S` of size `s=k+sigma` and `W_S` the degree-`<s` interpolant of
`w|_S`,

```text
S supports slope z  iff  W_S mod E = z B in F[X]/(E).
```

For general `t >= sigma`, put `mu=t-sigma`, `L_S=prod_{x in S}(X-x)`, and
`P_S=rem_{L_S} W`.  Since `E` is nonzero on `D`, `L_S` is invertible modulo
`E`.  In the terminal quotient

```text
T_{E,mu} = (F[X]/(E)) / F[X]_<mu
```

define

```text
a_S = [P_S L_S^{-1}],   b_S = [B L_S^{-1}].
```

Then

```text
V_S(E,B,w) = { z : a_S = z b_S in T_{E,mu} }.
```

Off the tangent-direction degeneracy `b_S=0`, every nonempty fiber is a
singleton.  The remaining Paper-B-native frontier is to bound

```text
{ z : exists S, a_S = z b_S, b_S != 0 }
```

for primitive minimal nonquotient residue data in the positive range.

## 5. Verified Finite Hard Packets

The deterministic verifier
`experimental/notes/m1/m1_primitive_critical_residue_syndrome_verifier.py`
checks the following two packets over `F_97`, with

```text
H=<8>, n=16, k=8, sigma=2, |S|=10.
```

### Quadratic hard packet

```text
E = X^2 + 45X + 64,
B = 1 - X,
W = 27X + 73X^10 + 6X^11 + 49X^12 + 21X^13 + 77X^14 + 36X^15,
w = W|_H
  = [95,3,8,94,31,18,68,18,12,3,9,38,58,29,10,88].
```

The verifier finds:

```text
successful 10-subsets: 145
antipodal successful supports: 0
distinct witness polynomials: 125
agreement distribution: {10:123, 11:2}
distinct slopes: 85
missing slopes: [0,24,37,42,49,52,54,57,60,63,67,71]
support multiplicity range: 1..12
```

It also checks that `E` has no root on `H`, `gcd(E,B)=1`, no denominator of
degree `<2` represents the direction, and the unique minimal denominator is
not a quotient pullback.

This kills the repaired finite toy cap

```text
every hard primitive nonquotient tau=sigma datum has <= 82 residual-counted slopes
```

The original arbitrary degree-3 version had already been killed by the
all-97-slope `(E,B)=(X^3,X^2)` datum; the point here is that the obstruction
survives after moving to the hard primitive `tau=sigma=2` layer.

### Shifted-cubic reverse-locator packet

With `Y=X-2`,

```text
E = Y^3,
B = 1 + 46Y + 53Y^2,
W = Y^11 + 15Y + 13Y^2,
w = W|_H
  = [94,57,13,58,26,92,64,0,47,78,25,61,43,70,80,47].
```

The verifier finds:

```text
successful 10-subsets: 133
tangent successful supports: 0
distinct slopes: 83
missing slopes: [3,6,13,16,19,32,38,46,49,56,59,76,84,89]
support multiplicities: {1:52, 2:21, 3:8, 4:1, 11:1}
```

It checks that `2 notin H`, `E` is nonzero on `H`, `gcd(E,B)=1`, and no
denominator of degree `<3` represents the direction.  Since `2*3 <= n-k`, the
minimal denominator is unique up to scalar; degree `3` cannot be a pullback
through `X -> X^M` for proper `M | gcd(16,8)`.  This is a genuine primitive
nonquotient hard packet, but it is still finite evidence below the asymptotic
reserve, not a disproof of `conj:B`.

## 6. Next Exact Target

The next Paper-B-aligned target is:

```text
M1-CRITICAL-TAU-SIGMA-RESIDUE-IMAGE
```

Either prove an upper bound for the hard primitive nonquotient residue image in
the positive range, or exhibit a positive-range family where the image has
superlinear size after quotient-periodic and contained supports are removed.

The finite subproblem is now clean:

```text
For fixed primitive minimal nonquotient (E,B,w), bound or maximize
{ z : exists S in binom(H,k+sigma), W_S mod E = zB }
at t=sigma, and its terminal-quotient analogue at t>sigma.
```

The first possible fatal line is that the critical residue-syndrome image may
remain large in the positive Paper-B reserve range, not merely in the small
`F_97,n=16` toy window.
