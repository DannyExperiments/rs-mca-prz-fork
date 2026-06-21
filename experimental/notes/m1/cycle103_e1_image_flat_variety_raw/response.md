I'll start by reading the file index and key project files.The index is large. Let me read the key files directly as specified in the prompt.Let me find the specific m1 files mentioned in the prompt.Now I have the key file paths. Let me read the cycle103 prompt, the cycle102 audit, and response files.Now let me read the cycle102 audit and response, which contain the corrected identity derivation.Let me read the cycle102 audit and the cycle101 prompt/response to understand the upstream setup and the e1-image structure.Let me read the ACTIVE_WALLS and BANKED_LEMMAS to lock the definitions, then the cycle102 audit.I've read the cycle103 prompt, the cycle102 brief/audit/response, and the banked lemmas and active-wall files. I have what I need. Here is the cycle103 deliverable.

Note on environment: this harness exposes only the `Read` tool, so I cannot write a `response.md` or run a checker. All algebra below is hand-derived and self-contained; I flag exactly one finite check that a future Codex run should replay.

---

## Classification

```text
PROOF            (bandwidth-1 / "B1" case k=1: |e_1(V)| <= (n-sigma+1)(sigma+1) = O(n^2),
                  UNCONDITIONAL in Uhat — no aperiodicity hypothesis needed)
+ EXACT_NEW_WALL (general bandwidth k>=2: the affine-family-contains-a-divisor
                  incidence, reduced to a k-parameter pseudo-remainder non-vanishing)
```

The current wall has been named `B1` (bandwidth 1) since Cycle 99, and the live regime of Cycles 99–103 is exactly `k=1` (`s=sigma+1`, `m=n-sigma-1`). For that regime I prove the target `|e_1(V)| <= n^{O(1)}` outright. I do **not** prove general `k>=2`; I reduce it to a precisely stated wall and give the next checker.

Route to a full solution: **yes for B1, now closed.** For `k>=2` I see a route (same resultant mechanism) but it requires one more non-vanishing lemma stated in §4.

---

## 1. Exact reduction of activity to a divisibility in a single variable

Setup (banked): `p` prime, `n | p-1`, `H = mu_n <= F_p^*`, `Uhat` with `Uhat(0)=1`, `s=n-m=k+sigma`, flatness window `i=2,...,sigma+1`. Write `Uhat(X)=sum_{j>=0} u_j X^j`, `u_0=1`. For `S' subset mu_n` put `g_{S'}(X)=prod_{x in S'}(1-xX)` and let `bar S = mu_n \ S'`, `|bar S|=s`.

Two exact identities I use:

```text
(A)  g_{S'}(X) g_{bar S}(X) = 1 - X^n            (since prod_{x in mu_n}(1-xX)=1-X^n)
(B)  g_{S'}(X) Uhat(X) == 1 - theta X  (mod X^{sigma+2})   [banked active-root form]
```

In the live regime `sigma+2 <= n`, so `1-X^n == 1 (mod X^{sigma+2})`, and (A) gives `g_{S'} == g_{bar S}^{-1} (mod X^{sigma+2})` (both have constant term 1, hence are invertible). Substituting into (B):

```text
theta active  <=>  exists bar S subset mu_n, |bar S|=s,
                   g_{bar S}(X) == (1 - theta X)^{-1} Uhat(X)   (mod X^{sigma+2}).
```

Define the bivariate truncation

```text
G(theta, X) := [ (1-theta X)^{-1} Uhat(X) ]_{deg_X <= sigma+1}
            = sum_{l=0}^{sigma+1} g_l(theta) X^l,   g_l(theta) = sum_{j=0}^{l} u_{l-j} theta^j.
```

Each `g_l` is a polynomial in `theta` of degree exactly `l` with leading coefficient `u_0=1`; in particular `g_0=1`, `g_1=u_1+theta`, and `g_{sigma+1}` is monic of degree `sigma+1`.

---

## 2. Bandwidth-1: activity is exactly `G(theta,X) | 1 - X^n`

For `k=1` we have `s = sigma+1`, so `g_{bar S}` has degree `sigma+1` and the congruence `mod X^{sigma+2}` pins **all** of its coefficients. Hence

```text
theta active (k=1)  <=>  g_{bar S}(X) = G(theta, X) exactly,  for some bar S,
                    <=>  G(theta, X) is a genuine size-(sigma+1) co-locator,
                    <=>  G(theta, X) | 1 - X^n.
```

The last equivalence is exact because `1-X^n` is squarefree (`n | p-1 => gcd(n,p)=1`), so any degree-`(sigma+1)` divisor with constant term `1` is automatically `prod_{x in bar S}(1-xX)` for a unique `(sigma+1)`-subset `bar S`, and then `S'=mu_n \ bar S` has `|S'|=m`. (If `g_{sigma+1}(theta)=0`, then `deg_X G < sigma+1` and `theta` cannot be active with a full-size witness; at most `sigma+1` such `theta`, absorbed below.)

This is the key collapse: in B1, **`theta` is not a free nonlinear parameter** — the entire candidate co-locator `G(theta,X)` is an explicit polynomial in `theta`, and activity is the single condition that it divides `1-X^n`.

---

## 3. PROOF that `|e_1(V)| <= (n-sigma+1)(sigma+1)` for `k=1`

Pseudo-divide `1-X^n` by `G(theta,X)` over `F_p[theta]`. With `L(theta):=g_{sigma+1}(theta)` (the `X`-leading coefficient, `deg_theta L = sigma+1`) and `N := n-sigma`,

```text
L(theta)^N (1 - X^n) = Qtil(theta,X) G(theta,X) + Rtil(theta,X),
deg_X Rtil <= sigma,   Rtil_i(theta) in F_p[theta].
```

For every `theta_0` with `L(theta_0) != 0`:  `G(theta_0,X) | 1-X^n  <=>  Rtil(theta_0,X)=0  <=>  Rtil_i(theta_0)=0 for all i`.

**Claim: `Rtil` is not the zero polynomial.** If `Rtil ≡ 0`, then over `F_p(theta)` we have `G(theta,X) | 1-X^n`. Taking reverses, the monic polynomial `G^*(X)=X^{sigma+1}G(theta,1/X)` divides `X^n-1`. But `X^n-1` splits into the linear factors `(X-x)`, `x in mu_n subset F_p`, which remain the only monic irreducibles of `X^n-1` in the UFD `F_p(theta)[X]`. Hence every monic divisor of `X^n-1` lies in `F_p[X]` and is **independent of `theta`**. Yet the coefficients of `G^*` are the reversed coefficients of `G`, and `g_1(theta)=u_1+theta` is non-constant in `theta` — contradiction. So `Rtil != 0`, and some coefficient `Rtil_{i}(theta)` is a nonzero element of `F_p[theta]`. ∎(claim)

Therefore every active `theta` (with `L(theta)!=0`) is a root of the fixed nonzero polynomial `Rtil_i`. Counting:

```text
|e_1(V)| = #{active theta}
         <= deg_theta Rtil_i  +  #{theta : L(theta)=0}
         <= (n-sigma)(sigma+1) + (sigma+1)
         = (n-sigma+1)(sigma+1)  <=  (n+1)^2 / 4  =  O(n^2).
```

Here `|e_1(V)| = |Theta_U| = #{active theta}` because `theta = e_1(S') - u_1` is an affine bijection (banked linear readout). The bound is **independent of `Uhat`** (no aperiodicity needed) and **independent of `p`**: if `p <= (n+1)^2/4` the bound is trivial (`#theta <= p`), and otherwise the root count applies. This proves the wall `L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY` in the bandwidth-1 regime. ∎

Three remarks on robustness: (i) the bound counts *all* `theta` with `G(theta,X)|1-X^n`, a superset of the external active roots `Theta_U subset F_p \ H`, so it is a valid upper bound; (ii) the argument never separated periodic from aperiodic prefixes — quotient/periodic structure can only *shrink* the active set, so it needs no separate charging here; (iii) the empirical Cycle101 result `max_distinct_theta = 1` is consistent: generically `Rtil_i` is "generic" and active `theta` are far fewer than the worst-case `O(n^2)`.

---

## 4. EXACT_NEW_WALL — general bandwidth `k >= 2`

For `k>=2`, `g_{bar S}` has degree `s = sigma+k`, but the congruence `mod X^{sigma+2}` fixes only coefficients `0..sigma+1`. The top `k-1` coefficients (degrees `sigma+2,...,s`) are free. So activity becomes an **affine-family-contains-a-divisor** question:

```text
W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE.
theta active  <=>  exists rho in F_p[X], deg rho <= k-2, such that
                   G(theta,X) + X^{sigma+2} rho(X)   divides   1 - X^n,
                   (a degree-s polynomial with constant term 1).
```

Equivalently, eliminating `rho` by a resultant/Bezout system in the `k-1` free coefficients, activity is the vanishing of a `theta`-polynomial system `{Delta_a(theta)}` obtained from the `k`-parameter pseudo-remainder of `1-X^n` modulo the affine family. The exact missing input is:

> **Needed non-vanishing lemma.** For `k>=2` and aperiodic `Uhat` above corrected reserve, the elimination ideal `<Delta_a(theta)>` is nonzero (the family is not "divisor-degenerate"), with `max_a deg_theta Delta_a = n^{O(1)}`.

What converts this to PROOF or COUNTERPACKET:
- **PROOF**: show some `Delta_a != 0` with `deg = n^{O(1)}`. The B1 proof is the `k=1` instance where the family is a single polynomial and non-vanishing is forced by the `g_1=u_1+theta` argument; for `k>=2` one must rule out a positive-dimensional `(theta,rho)` family of divisors, which is exactly where a periodic `Uhat=Uhat^*(X^d)`, `d|n`, could create degeneracy (the chargeable branch).
- **COUNTERPACKET**: a source-valid aperiodic `Uhat` above reserve with `k>=2` for which the affine family meets `1-X^n` in superpolynomially many `theta`. By §3 this cannot occur for `k=1`; the danger lives only at `k>=2`.

Decisive next checker (replayable, small): for primes `p` with `n|p-1`, sweep `k=2,3`, growing `sigma`, adversarial aperiodic `Uhat`; for each `theta` test whether the affine family `G(theta,X)+X^{sigma+2}rho` meets a degree-`s` divisor of `1-X^n` (gcd with `X^n-1`); report `#active theta` vs `(n-sigma+1)(sigma+1)`. Counterpacket trigger: `#active` growing superpolynomially across a reproducible aperiodic family. (I could not run this here — Read-only harness.)

---

## Self-audit (the six required questions)

**1. What exact implication did I prove / not prove?**
Proved, for bandwidth `k=1` (`s=sigma+1`, `m=n-sigma-1`): `theta active <=> G(theta,X) | 1-X^n`, where `G(theta,X)=[(1-theta X)^{-1}Uhat]_{deg_X<=sigma+1}`; and the pseudo-remainder of `1-X^n` mod `G` is a nonzero element of `F_p[theta]`, giving `|e_1(V)| = #{active theta} <= (n-sigma+1)(sigma+1) = O(n^2)`, unconditionally in `Uhat` and `p`. **Not** proved: the general bandwidth `k>=2` bound; I reduced it to the non-vanishing of a `k`-parameter elimination system (§4).

**2. Official-prize-relevant or only research?** The B1 bound is **directly prize-relevant** for the bandwidth-1 upper-side numerator: it is the exact wall `L-CYCLE103` named since Cycle 99 (`B1-APERIODIC`), and it closes it as a theorem (not a finite/model certificate). It does not by itself complete the full RS-MCA upper theorem, which also needs the `k>=2` strata and the downstream ledger merge.

**3. First line where the chain could fail.** In the B1 proof, the only nontrivial step is "`Rtil != 0`", which rests on `X^n-1` splitting over `F_p` (true since `n|p-1`) and `g_1=u_1+theta` non-constant (true). Both are unconditional, so B1 has no conjectural step. The chain *does* fail to extend at the `k=1 -> k>=2` boundary: with `k>=2` the single polynomial `G(theta,X)` becomes a `(k-1)`-dimensional affine family, and divisor-degeneracy is no longer excluded by the `g_1` argument.

**4. Are `q_gen, q_line, q_code, q_chal, 2^-128` used correctly?** They are **not invoked**, correctly: this cycle is single-field upper-side structure on `|Theta_U|`. I assert no `2^-128` crossing and merge no ledger. The bound is `p`-uniform, so it composes safely with any later `q`-instantiation.

**5. Could quotient/periodic, contained incidences, same-slope collisions, or affine color normalization reduce the numerator?** For B1, **no separation is needed**: the bound `O(n^2)` holds for every `Uhat`; periodic/quotient `Uhat` can only *shrink* the active set, and same-slope/contained incidences only merge `theta`-values (the count is already distinct-support `|e_1(V)|`, with `e_1` the affine-normalized invariant `theta=e_1(S')-u_1`). For `k>=2`, periodic `Uhat=Uhat^*(X^d)` is exactly the candidate degeneracy in §4 and must be charged there.

**6. If PLAN, what converts it to PROOF/COUNTERPACKET?** §1–§3 are PROOF (definite). §4 is the residual PLAN; it converts to PROOF via the stated non-vanishing lemma (`some Delta_a != 0`, `deg_theta = n^{O(1)}`, for aperiodic `Uhat`, `k>=2`), or to COUNTERPACKET via an aperiodic `Uhat` with `k>=2` and superpolynomially many `theta` meeting the affine family — found by the `gcd`-with-`X^n-1` sweep checker above, **not** via the dead short-window Padé route (Cycle 102).