# Cycle 99 B1 Aperiodic Moment-Curve Incidence Audit

## Verdict

**BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

Cycle99 does **not** prove the aperiodic moment-curve incidence bound and does
not produce a counterpacket. It banks three exact reformulations of the Cycle98
wall and cuts the agreement-only/list-decoding route below Johnson.

## Bankable Content

Cycle99 reformulates the active external branch as:

```text
theta in F_p \ H active
<=> exists monic f | X^n - 1, deg f = s, with deg(U - (X-theta)f) < k
<=> exists deg-<k RS codeword r = U - (X-theta)f.
```

It also gives the reciprocal affine-line form. With:

```text
U_rev(X) = X^(s+1) U(1/X),
W = U_rev^(-1) mod X^(sigma+2),
S' = H \ S, |S'| = n-s,
g_{S'}(X)=prod_{x in S'}(1-xX),
```

the active external condition is:

```text
g_{S'}(X) == (1-theta X) W(X) mod X^(sigma+2).
```

Equivalently, the elementary-symmetric image of `(n-s)`-subsets of `H`
intersects an explicit affine line. This is the dual form of Cycle98's
moment-curve incidence.

The final reduction is the exact additive-character identity:

```text
N = p^(-(sigma+1)) sum_t psi(-<t,P>)
      e_s({psi(L_t(x))}_{x in H}) sum_{theta notin H} psi(L_t(theta)).
```

The `t=0` main term is at most `1` in the intended reserve scale, so the next
wall is cancellation in the nonzero-frequency error term.

## Route Cut

The agreement-only RS list-decoding route is cut. Johnson gives a polynomial
list bound only when:

```text
s > sqrt(k n).
```

In the live reserve range:

```text
s = rho n + sigma,    sigma = O(n/log n),
```

this is below Johnson for fixed `rho < 1`. Therefore any proof must use the
special subgroup structure and aperiodicity, not generic RS agreement bounds.

## Local Verification

Codex added and ran:

```text
experimental/scripts/cycle99_divisor_line_incidence_check.py
```

The checker verifies the power-sum, divisor/remainder, codeword-injection, and
reciprocal affine-line equivalences for small prime-field cases. It also checks
a small additive-character identity numerically in the tiny cases, and includes
constructed active-external examples so the nonempty branch is exercised.

Run result:

```text
cycle99 divisor-line incidence check
cases_checked: 20
constructed_cases_checked: 10
total_external_theta: 0
total_external_pairs: 0
constructed_external_pairs: 11
total_codewords: 0
PASS
```

During checker construction Codex caught and fixed an implementation mistake:
the reciprocal branch must use `prod(1-xX)` for `S'`, not the monic locator
`prod(X-x)`. The banked lemma uses the corrected reciprocal form.

## What Is Not Proved

- No proof of `|v(F_p \ H) cap (P-M_s)_aper| <= n^{O(1)}`.
- No official prize theorem.
- No nonperiodic external-root counterpacket.
- No proven cancellation bound for the elementary-symmetric character
  transform below Johnson.

## Next Exact Wall

The next prompt should attack:

```text
W-CYCLE100-SUBGROUP-ELEMSYM-MOMENT-CHARACTER-SUM
```

Target:

```text
| sum_{t != 0} psi(-<t,P>)
    e_s({psi(L_t(x))}_{x in H})
    sum_{theta notin H} psi(L_t(theta)) |
<= p^(sigma+1) n^{O(1)}
```

after quotient-periodic resonances are charged.

This is the first exact line where the current route can fail. A proof converts
Cycle99 into the desired `B1` incidence theorem. A nonperiodic prefix `P`
producing superpolynomial error gives the counterpacket mechanism.

