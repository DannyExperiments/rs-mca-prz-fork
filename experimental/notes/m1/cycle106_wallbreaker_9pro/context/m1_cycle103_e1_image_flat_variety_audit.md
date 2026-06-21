# M1 Cycle 103 e1-Image Flat-Variety Audit

## Verdict

```text
PROOF / EXACT_NEW_WALL
```

Confidence: high for the bandwidth-`1` proof after local finite replay of the
divisor equivalence. Unknown for the residual `k>=2` wall.

Cycle103 proves the named Cycle103 wall in the bandwidth-`1` stratum:

```text
|e_1(V)| = |Theta_U| <= (n-sigma+1)(sigma+1) = O(n^2).
```

This is not a full RS-MCA upper theorem. It closes the current `B1` numerator
wall and moves the route to general bandwidth `k>=2`.

## Proof Content Banked

Let `k=1`, so `s=sigma+1`. Let

```text
G(theta,X) = [(1-theta X)^(-1) Uhat(X)]_{deg_X <= sigma+1}.
```

The active-root congruence and the complement identity give:

```text
theta active
<=> G(theta,X) = g_{\bar S}(X) for some |\bar S|=sigma+1
<=> G(theta,X) | 1 - X^n.
```

Pseudo-dividing `1-X^n` by `G(theta,X)` over `F_p[theta]` gives a remainder
polynomial. If the pseudo-remainder vanished identically, the reverse of
`G(theta,X)` would be a monic divisor of `X^n-1` over `F_p(theta)`. Since
`n | p-1`, `X^n-1` splits over `F_p`, so every such monic divisor has
theta-independent coefficients. This contradicts the nonconstant coefficient
`g_1(theta)=Uhat_1+theta`.

Therefore at least one nonzero theta-polynomial cuts out all active roots
outside the leading-coefficient exceptional set, giving:

```text
|Theta_U| <= (n-sigma)(sigma+1) + (sigma+1)
           = (n-sigma+1)(sigma+1).
```

The proof is uniform in `Uhat`; aperiodicity is not needed in this stratum.

## Local Replay

Codex added and ran:

```text
experimental/scripts/cycle103_b1_divisor_bound_check.py
```

The checker enumerates small finite cases and verifies:

```text
theta active by subset enumeration
==
theta active by G(theta,X) | 1-X^n
```

and checks the polynomial bound. It emits `PASS`.

## Exact New Wall

```text
W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE
```

For `k>=2`, `s=sigma+k`, and the congruence only fixes coefficients through
degree `sigma+1`. Activity becomes:

```text
theta active
<=> exists rho in F_p[X], deg rho <= k-2, such that
    G(theta,X) + X^(sigma+2) rho(X) divides 1-X^n.
```

The next missing theorem is a non-vanishing/elimination lemma for this affine
family in the aperiodic branch, or a source-valid aperiodic counterpacket with
superpolynomially many active theta values.

## Not Proved

- No general `k>=2` upper-side proof.
- No full RS-MCA upper theorem.
- No downstream finite-frontier/prize ledger merge.

## Next Action

Attack `W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE`, preferably beginning with
`k=2`. The next worker should either prove the non-vanishing elimination lemma,
produce a source-valid aperiodic counterpacket, or return a replayable checker
that decides the first `k=2` obstruction.

