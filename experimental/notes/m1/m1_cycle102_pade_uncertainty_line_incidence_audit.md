# M1 Cycle 102 Padé / Uncertainty Line-Incidence Audit

## Verdict

```text
ROUTE_CUT / BANKABLE_LEMMA / EXACT_NEW_WALL
```

Confidence: high for the finite falsifier, the corrected full-locator statement,
and the algebraic readout identity. Unknown for the new Cycle103 uncertainty
wall.

Cycle102 does not prove the RS-MCA upper theorem and does not produce a
superpolynomial counterpacket to the prize statement. It kills a proposed
short-window Padé/Berlekamp-Massey route and replaces it with a sharper exact
wall.

## Route Cut

The proposed implication

```text
theta active
=> the short-window Padé/BM denominator of (theta^j - P_j)_{j=1}^{sigma+1}
   is compatible with a divisor of X^n - 1
```

is false.

Cycle102 gives an explicit aperiodic finite falsifier over `F_29`:

```text
p = 29
n = 7
H = mu_7 = {1, 7, 16, 20, 23, 24, 25}
sigma = 3
S' = {1, 16, 24}
theta = 2
window = (12, 21, 28, 13)
P = (19, 12, 9, 3)
```

The window has a degree-2 recurrence

```text
a_j = 24 a_{j-1} - a_{j-2}  (mod 29)
```

with reciprocal characteristic polynomial

```text
T^2 - 24T + 1.
```

Its discriminant is `21`, a non-square in `F_29`, so the short-window
denominator is irreducible over `F_29`. Since `X^7 - 1` splits completely over
`F_29`, that short-window denominator cannot divide or be compatible with any
divisor of `X^7 - 1`.

Codex locally verified the arithmetic with:

```text
experimental/scripts/cycle102_pade_falsifier_check.py
```

The checker emits `PASS`.

## Bankable Correction

The true divisor statement applies only to the full locator of a witness:

```text
g_{S'}(t) = product_{x in S'} (1 - x t)
```

or equivalently the ordinary locator

```text
product_{x in S'} (X - x) | X^n - 1.
```

The length-`sigma+1` Padé/BM window is underdetermined in the live range because
one would need at least `2|S'|` consecutive terms to recover the full
denominator, while the corrected-reserve range only supplies about `n/log n`
terms.

## Bankable Reformulation

Multiplying the active-root congruence by `Uhat = W^{-1} mod X^{sigma+2}` gives

```text
g_{S'}(X) Uhat(X) == 1 - theta X  (mod X^{sigma+2}).
```

Thus theta is not a free nonlinear parameter. It is the linear readout

```text
theta = -[X] (g_{S'} Uhat) = e_1(S') - Uhat_1,
```

after the theta-free flatness constraints

```text
[X^i](g_{S'} Uhat) = 0,  i = 2,...,sigma+1.
```

So the exact distinct numerator is

```text
|Theta_U| =
#{ distinct e_1(S') :
   S' subset mu_n, |S'| = m,
   [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

This is the useful content of the round: it focuses the upper-side wall on the
image of one linear statistic over a theta-free flatness locus, not on the size
of the whole solution set.

## Exact New Wall

```text
L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY
```

Prove or kill:

```text
|e_1(V)| <= n^{O(1)}
```

where

```text
V = { S' subset mu_n :
      |S'| = m,
      [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

A proof must use the actual shifted-moment/flatness structure. A bound on
`|V|`, a min-distance argument, or a revived short-window Padé divisor claim is
not sufficient.

## Not Proved

- No full RS-MCA upper theorem.
- No prize-level finite frontier certificate.
- No proof that `|Theta_U| <= n^{O(1)}`.
- No source-valid superpolynomial aperiodic counterpacket.

## Next Action

Send Cycle103 against `L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY`, asking for either a
proof of the e1-image bound, a source-valid aperiodic counterpacket, or a
strictly smaller exact wall/checker.

