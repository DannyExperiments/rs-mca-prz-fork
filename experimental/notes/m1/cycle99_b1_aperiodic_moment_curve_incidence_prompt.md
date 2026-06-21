# Cycle 99 Prompt: B1 Aperiodic Moment-Curve Incidence

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. Do you see a route to a full solve? If yes, what is the next
exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Current State

Cycle97 banked the corrected bandwidth-`1` root-configuration decomposition.

Cycle98 banked:

```text
L-CYCLE98-MOMENT-CURVE-INCIDENCE
```

For monic `U` of degree `s+1`, after charging the `theta in H` and repeated
root branches, active external bandwidth-`1` roots are exactly:

```text
Theta_U = { theta in F_p \ H : v(theta) in P - M_s },
v(theta) = (theta, theta^2, ..., theta^{sigma+1}),
M_s = { (p_1(S), ..., p_{sigma+1}(S)) : S subset H, |S| = s }.
```

Here `P=(P_1,...,P_{sigma+1})` is the power-sum prefix of `U`, and
`s=k+sigma`.

Cycle98 also cuts the naive route:

```text
b=0 prefix local limit controls vertical fibers of M_s;
b=1 needs transverse incidence of M_s with the moment curve.
```

Do not spend the answer re-proving this normal form unless you find a real
error in it.

## Target

Attack:

```text
L-CYCLE99-B1-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill:

```text
|v(F_p \ H) cap (P - M_s)_aper| <= n^{O(1)}
```

for `p == 1 mod n`, `H <= F_p^*` generated of order `n`, `k=rho n`,
`s=k+sigma`, `sigma >= C n/log n`, and after quotient-periodic cores are
charged.

## What A Successful Answer Must Do

One of:

1. **PROOF:** Give a theorem-grade incidence or character-sum argument proving
   the polynomial bound in the live corrected-reserve range.
2. **COUNTERPACKET:** Construct a nonperiodic family of prefixes `P` for which
   the translated moment curve hits `M_s` in superpolynomially many external
   `theta`, with the quotient-periodic branch removed.
3. **BANKABLE_LEMMA:** Reduce the target to a strictly smaller named theorem,
   for example a concrete bound on the elementary-symmetric transform
   character sum along the moment-curve pencil.
4. **ROUTE_CUT:** Prove that a proposed route cannot work, by naming the exact
   obstruction and the next viable object.

## Required Precision

- Separate `theta in H` from `theta in F_p \ H`.
- Do not claim the result follows from `b=0` fiber-size control unless you
  explicitly prove why vertical fiber bounds imply transverse moment-curve
  incidence.
- If using characters, state the exact character sum and the needed bound.
- If using quotient periodicity, state exactly which `mu_M` cores are removed
  and why external points are or are not charged.
- If giving a counterpacket, verify nonperiodicity and explain how it survives
  the corrected reserve convention.

