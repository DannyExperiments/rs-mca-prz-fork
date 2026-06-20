# Cycle 67 Cross-Color Injectivity Audit

## Verdict

```text
EXACT_NEW_WALL / BANKABLE_LEMMA / ROUTE_CUT / PLAN
```

Confidence: high for the algebraic reductions and route cut; unknown for the
remaining multiplicity bound.

Cycle 67 does not prove the sevenfold occupancy target
`Occ(beta) >= 2^32`. It does, however, replace the loose cross-color shortcut
with a sharper exact finite decision target:

```text
W-CYCLE67-COLLISION-MULTIPLICITY
```

For the explicit Cycle 66 model, prove or kill:

```text
m_max(beta) <= 12,
```

where

```text
m_max(beta) = max_v #{T in P_0 : rho_beta(T) = v}.
```

This is the right next wall because

```text
|P_0| = 52,747,567,104 = 393 * 2^27 = 12.28125 * 2^32.
```

Thus

```text
m_max(beta) <= 12
  => Occ(beta) >= |P_0| / 12
  = 4,395,630,592
  > 2^32.
```

The threshold is sharp at this scale: `|P_0| / 13 < 2^32`, so the constant
`12` is not cosmetic.

## Bankable Lemmas

Cycle 67 banks the following reductions.

### Locator Evaluation

For each admissible tuple `T in P_0`,

```text
rho_beta(T) = prod_{x in T}(beta - x) = P_T(beta),
```

where `P_T(X)` is the degree-113 locator. Hence

```text
Occ(beta) = #{P_T(beta) : T in P_0}.
```

This restates the Cycle 66 reformulation in the cleanest decision language.

### Shared-Jet Collision Reduction

Every `T in P_0` has

```text
e_1(T)=1,
e_2(T)=e_3(T)=e_4(T)=e_5(T)=0.
```

Therefore all locator polynomials share their six highest coefficients, and for
distinct `T,T'`,

```text
deg(P_T - P_T') <= 107.
```

A collision is exactly the single equation

```text
(P_T - P_T')(beta) = 0.
```

This converts the occupancy problem into a finite fiber problem for one
evaluation functional on the locator-coefficient image.

### Multiplicity And Energy Bound

The elementary but decisive inequality is

```text
Occ(beta) * m_max(beta) >= |P_0|.
```

Equivalently, if

```text
E = #{(T,T') in P_0^2 : P_T(beta)=P_T'(beta)},
```

then

```text
Occ(beta) >= |P_0|^2 / E.
```

The exact sufficient energy form is approximately

```text
E <= 12.28 * |P_0|.
```

### Slot Product Oracle

For a fixed slot, product over a full parity class collapses to

```text
prod_{a in parity class} u_t(i,a)
  = (+/-1) * prod_{e in E_i}(((-1)^e) - gamma_t),

gamma_t = (beta^2 eta^{-2t})^8.
```

This is a useful consistency oracle for any future exact verifier.

## Route Cut

The literal proposed shortcut

```text
Occ(beta) >= 8^7 * (# independent color classes)
```

is not a viable pure color theorem. The color only records a coarse `Z/16`
projection. Within-class injectivity and cross-class disjointness live in the
full cyclic group of order

```text
N = 17^16 - 1.
```

Thus color is blind to the actual collision lattice of the elements
`{beta - x : x in mu_256}`. The shortcut may still be true for the explicit
model, but it cannot be proved from color data alone.

## Remaining Wall

The next exact wall is:

```text
W-CYCLE67-COLLISION-MULTIPLICITY
```

Prove or kill, for the explicit model

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
```

that

```text
m_max(beta) <= 12.
```

Failure mode:

```text
find 13 distinct tuples T with P_T(beta) equal.
```

Success mode:

```text
certify no value is attained more than 12 times.
```

## Next Action

Stage Cycle 68 against the bounded-multiplicity verifier problem rather than
the full distinct-value occupancy count. The desired output is either:

- a structural proof of `m_max(beta) <= 12`;
- an explicit 13-fold collision packet;
- or a precise verifier architecture that certifies the multiplicity bound
  without materializing all `> 2^32` distinct values.

Keep this model-level occupancy target separate from prize-level MCA
counterpacket claims.

