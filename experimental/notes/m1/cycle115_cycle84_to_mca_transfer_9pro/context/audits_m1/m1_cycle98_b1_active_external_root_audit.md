# Cycle 98 B1 Active External-Root Audit

## Verdict

**BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle98 does **not** prove the polynomial active-external-root bound and does
not produce a counterpacket. It does bank the clean structural reduction:

```text
L-CYCLE98-MOMENT-CURVE-INCIDENCE
```

For bandwidth `1`, after the corrected Cycle97 split charges the `theta in H`
and repeated-root branches, the real external branch is exactly:

```text
Theta_U = { theta in F_p \ H : v(theta) in P - M_s },
v(theta) = (theta, theta^2, ..., theta^{sigma+1}),
M_s = { (p_1(S), ..., p_{sigma+1}(S)) : S subset H, |S| = s }.
```

The target wall is therefore:

```text
|v(F_p \ H) cap (P - M_s)_aper| <= n^{O(1)}.
```

## What Is Bankable

- The power-sum normal form for active external roots is exact.
- The `theta in H` branch must remain separated; it is not the active external
  wall.
- The `b=1` wall is not a direct consequence of the `b=0` prefix local limit.
  The `b=0` theorem controls vertical fiber sizes of `M_s`; Cycle98 asks for
  transverse incidence of `M_s` with the moment curve.
- The monomial Galois/norm sieve does not automatically extend here, because
  the external point `theta in F_p \ H` has no bounded-height cyclotomic lift.

## What Is Not Proved

- No proof of the polynomial bound for aperiodic active external roots.
- No official prize-level upper theorem.
- No finite/model lower counterpacket.
- No replacement for the open prefix local-limit input in the live polynomial
  prime-field range.

## Local Verification

Codex added and ran:

```text
experimental/scripts/cycle98_moment_curve_incidence_check.py
```

It checks, for small prime fields with multiplicative subgroups, that the
external bandwidth-`1` prefix condition is equivalent to the moment-curve
incidence condition.

Run result:

```text
cycle98 moment-curve incidence check
cases_checked: 40
total_external_theta: 2
total_external_pairs: 2
PASS
```

This is only a finite sanity check of the reduction, not evidence for the
asymptotic polynomial incidence bound.

## Next Exact Wall

The next useful prompt should attack:

```text
L-CYCLE99-B1-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill the polynomial bound for:

```text
|v(F_p \ H) cap (P - M_s)_aper|.
```

The worker should not re-prove the Cycle98 normal form. It should either:

- prove a subgroup power-sum / moment-curve incidence theorem in the corrected
  reserve range;
- produce a nonperiodic translated-moment-curve alignment counterpacket; or
- identify a still-smaller exact sublemma, such as a character-sum bound for
  the elementary-symmetric transform along the moment-curve pencil.

