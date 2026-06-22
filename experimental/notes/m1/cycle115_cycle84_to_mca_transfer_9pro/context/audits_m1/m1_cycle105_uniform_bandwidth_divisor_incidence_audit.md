# M1 Cycle 105 Uniform Bandwidth Divisor-Incidence Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Confidence: moderate-high for the algebraic k-free collapse and complement
duality after local finite replay. Confidence: moderate for the Johnson/list
route-cut framing. The uniform upper theorem remains open.

Cycle105 does not prove:

```text
|Theta_U| <= n^{O(1)}
```

for growing bandwidth `k`. It reduces the wall to a single `k`-free incidence
problem and identifies the first line where a proof must use aperiodicity.

## Bankable Lemma: k-Free Collapse

Let `s=sigma+k`, `H=mu_n`, and:

```text
G(theta,X)=sum_{l=0}^{sigma+1} g_l(theta) X^l,
g_l(theta)=sum_{i=0}^l u_{l-i} theta^i.
```

For an `s`-subset `Sbar` of `H`, set:

```text
g_Sbar(X)=prod_{x in Sbar}(1-xX).
```

Then bandwidth-`k` activity is exactly:

```text
theta active
<=> exists Sbar subset H, |Sbar|=s, with
    g_Sbar(X) == G(theta,X) mod X^{sigma+2}.
```

Equivalently:

```text
(g_1(theta),...,g_{sigma+1}(theta)) in M_s,
M_s = {((-1)^l e_l(Sbar))_{l=1}^{sigma+1}: |Sbar|=s}.
```

Thus all bandwidths share the same rational curve:

```text
Gamma = {(g_1(theta),...,g_{sigma+1}(theta)): theta in F_p}
```

and `k` only changes the subset-size layer `M_s`.

This makes the `binom(n,k)` factor in Cycle104 a union-bound artifact rather
than an intrinsic dimension of the active-root problem.

## Bankable Lemma: Complement Duality

For `S'=H\Sbar`, the identity:

```text
g_Sbar(X) g_S'(X) = 1 - X^n == 1 mod X^{sigma+2}
```

gives a fixed triangular polynomial automorphism:

```text
iota: M_s -> M_{n-s}
```

independent of `s`, `k`, and `Uhat`. Therefore:

```text
|Gamma cap M_s| = |iota(Gamma) cap M_{n-s}|.
```

This collapses extreme bandwidth regimes but does not solve the central
constant-rate case where both `s` and `n-s` are linear in `n`.

## Route Cut

The response correctly separates the current target from generic RS list-size
methods. In the prize regime `sigma=o(n)` and `k=rho n`, the activity radius is
beyond the Johnson radius. Therefore an unconditional or list-generic argument
cannot prove the required `n^{O(1)}` support bound. Any valid proof must use the
above-reserve aperiodicity of `Uhat` to remove subgroup-periodic configurations.

This cuts attempts that only repackage the problem as a generic RS list-decoding
bound or another unconditional divided-difference union bound.

## Local Replay

Codex added and ran:

```text
experimental/scripts/cycle105_kfree_collapse_check.py
```

The checker verifies small finite cases for:

- equality of the Cycle104 divisor predicate and the Cycle105 `Gamma cap M_s`
  predicate;
- the fixed triangular complement map `M_s -> M_{n-s}`.

It emits `PASS`.

## Exact New Wall

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill:

```text
For aperiodic Uhat above corrected reserve and every s,
|Gamma cap M_s| <= n^{O(1)}
```

with exponent independent of `s` and `k`.

The proof must consume aperiodicity. The response proposes two possible routes:

- a single `k`-independent subresultant/Wronskian/eliminant on `Gamma`;
- a port of the Cycle100 aperiodic dephasing cap from weighted count to distinct
  support.

## Not Proved

- No uniform-in-`k` active-root bound.
- No finite-frontier or prize-ledger merge.
- No aperiodic growing-`k` counterpacket.
- No proof that the residual moment-curve incidence is polynomially bounded.

## Next Action

Attack `W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE` directly. A valid
answer must either prove the aperiodic incidence bound, produce an aperiodic
counterpacket, or reduce it to a strictly smaller named theorem/checker.
