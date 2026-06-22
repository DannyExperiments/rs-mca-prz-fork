# M1 Cycle 104 Bandwidth-k Divisor-Incidence Audit

## Verdict

```text
PROOF / EXACT_NEW_WALL
```

Confidence: high for `k=2` and every fixed `k` after local finite replay of the
fixed-`k` divisor-incidence equivalence. Unknown for a uniform-in-growing-`k`
bound.

Cycle104 proves the next fixed-bandwidth stratum:

```text
|Theta_U| <= binom(n,k)(sigma+1)
```

and in particular for `k=2`:

```text
|Theta_U| <= binom(n,2)(sigma+1) = O(n^2 sigma).
```

This is not a full RS-MCA upper theorem because constant-rate cases require a
bound with exponent independent of growing `k`.

## Proof Content Banked

Reverse the co-locator. For `s=sigma+k`, activity is equivalent to:

```text
theta active
<=> exists psi, deg psi <= k-2, such that
    B_theta(X)+psi(X) is a degree-s divisor of X^n-1.
```

Equivalently, for some `s`-subset `Sbar` of `mu_n`, the values
`B_theta(x)` on `Sbar` lie on a polynomial of degree at most `k-2`.

For `k=2`, this means a constant polynomial, so an active theta forces a pair
collision:

```text
B_theta(x)=B_theta(y), x != y.
```

For a fixed pair, the collision polynomial has degree exactly `sigma+1` in
theta, with nonzero leading coefficient. Union over pairs gives:

```text
|Theta_U| <= binom(n,2)(sigma+1).
```

For fixed `k`, replace pair collision by the order-`k-1` divided difference.
For every `k`-subset of `mu_n`, the divided-difference obstruction is monic of
degree `sigma+1` in theta, so:

```text
|Theta_U| <= binom(n,k)(sigma+1).
```

The proof is uniform in `p` and `Uhat` for fixed `k`; no aperiodicity hypothesis
is needed at this level.

## Local Replay

Codex added and ran:

```text
experimental/scripts/cycle104_fixed_k_divisor_incidence_check.py
```

The checker enumerates small finite cases, verifies the divisor-incidence
predicate, and checks the pair/divided-difference obstruction for active theta
values. It emits `PASS`.

## Exact New Wall

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE
```

Prove or kill a bound:

```text
|Theta_U| <= n^{O(1)}
```

with exponent independent of `k`, allowing `k` to grow up to `Theta(n)`.

The current fixed-`k` proof gives `binom(n,k)(sigma+1)`, which is
superpolynomial for growing `k`.

## Not Proved

- No uniform-in-`k` polynomial upper bound.
- No full RS-MCA upper theorem.
- No finite-frontier or prize ledger merge.

## Next Action

Attack `W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE`: either prove a
`k`-independent elimination/subresultant bound for the affine divisor family, or
construct a source-valid aperiodic growing-`k` counterpacket with
superpolynomially many active theta values.

