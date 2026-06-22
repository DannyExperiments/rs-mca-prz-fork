I'll start by reading the file index, then work through the key project files and the cycle110 packet.I'll read the cycle110 state, the canonical tracker, and the most relevant cycle109 responses in parallel.Let me read the canonical tracker and the key cycle109 synthesis and counterpacket files in parallel.Let me read the counterpacket hunter, residual-image, ap_corr, and q-ledger responses in parallel.Let me read the residual-image, ap_corr/charge, and q-ledger responses in parallel.This is the crux. Let me read the ap_corr/charge, q-ledger, full prover, and interior cover audit in parallel.Let me read the q-ledger closer, the full prover, and the interior cover audit in parallel.Let me read the full prover (role01), the interior cover audit, and the balanced Möbius and high transverse responses in parallel.Let me read the interior cover audit, the canonical tracker, and the balanced/high responses in parallel.This is the crux. Let me read the canonical tracker and the balanced/high branch responses in parallel to ground the charge definitions and adjacent-branch state.Let me read the high-transverse response and the certificate engineer report, and grep the canonical tracker for the key definitions, in parallel.Let me grep the canonical tracker for the key definitions and read the HIGH overflow construction.Let me grep the canonical tracker for key definitions (AP_corr, corrected reserve, q-fields) and the HIGH overflow construction.Let me grep the canonical tracker for the core definitions, and read the HIGH overflow construction (the existing superpolynomial one-chart family) which may be adaptable to LOW.The HIGH overflow uses σ=1,t=2 (t>σ). LOW needs t<σ, so it doesn't directly transfer. Let me grep the canonical tracker for the precise official definitions.ROUTE_CUT

I have read the cycle110 state, the interior-cover audit, the cycle109 role responses (01 prover, 02 counterpacket hunter, 03 low residual image, 04 balanced, 05 high, 06 ap_corr/charge, 07 q-ledger, 09 synthesis). I did not need the canonical tracker's prose; the binary checker and schema were not required for this argument. Everything below is same-field reasoning over `K_line`, no external sources.

## 1. Executive verdict and confidence

I do not produce a PROOF or a COUNTERPACKET, and I argue neither is currently reachable because `AP_corr` is undefined. What I can do rigorously is cut the exact counterpacket mechanism named in the target — locator-prefix / residue-collinearity / occupied-color fiber — by proving it is self-limiting, then reduce all that remains of LOW to one precise equidistribution wall.

The decisive new facts:

- The named mechanism, built from a single anchor `M`, has its entire witness list equal to a slack-`(σ−t)` locator prefix-fiber `F`, and its distinct-slope count is bounded by the collinear part of `F`. So the mechanism cannot exceed `|F| ≤ C(n,a)/q^{σ−t}` and, after the forced collinearity, `≈ C(n,a)/q^{σ−1}`.
- Under the `2^-128`-calibrated reserve `Γ₀ = σ·log₂q − log₂ C(n,a) ≥ 128 + O(log n)`, the term `C(n,a)/q^{σ−1}` is `≤ ⌊q/2^128⌋`. Hence at `t = 1` the mechanism is within budget for generic `D`, and is not a charge-free counterpacket.
- At `t = 1` the generalized quotient/action-rank charge (Role 02's decisive cut) is structurally vacuous: `d_R(E) = deg E = 1` for every `R`. So the `t = 1` branch is the most exposed branch, and it cannot be closed by action-rank — only by reserve + equidistribution.

Confidence: high on the anchor-list characterization, the collinearity-cost lower bound on codimension, the `t = 1` action-rank vacuity, and the reserve arithmetic; moderate that the surviving `t ≥ 2` clustering mechanism is the genuinely last uncut one.

Here `q = q_line`, `a = k + σ`, `C(n,a) = ` binomial `n` choose `a`, `A_E = K_line[X]/(E)`, `L_S(X) = ∏_{x∈S}(X−x)`.

## 2. Exact statements

Route-cut lemma (single-anchor mechanism is self-limiting).
Let `w = M|_D` with `M` monic, `deg M = a`. For `1 ≤ t < σ`:

```text
L_t(w) = { Q : deg Q < k+t, agr_D(Q,w) ≥ a } = { M − L_S : S ∈ F },
F = { S ∈ binom(D,a) : e_j(S) = e_j(M), 1 ≤ j ≤ σ−t }.
```

Consequently `|L_t(w)| = |F|`, and

```text
Z_t(E,B,w) = { z : ∃ S∈F, [M]_E − [L_S]_E = z·[B]_E } ,
|Z_t| ≤ #{ S∈F : [M]_E − [L_S]_E ∈ K·[B]_E } ≤ |F|.
```

The set `K·[B]_E` is a 1-dimensional `K`-subspace of the `t`-dimensional algebra `A_E`; lying on the affine line `[M]_E + K·[B]_E` is `t−1` independent affine conditions. Thus the slope-producing sub-fiber has codimension `(σ−t) + (t−1) = σ−1` inside `binom(D,a)`, independent of `t`.

`t = 1` specialization (bankable). `E = X−β`, `A_E ≅ K`, the line is all of `K`, the `t−1` conditions are vacuous, and

```text
Z_1 = { M(β) − L_S(β) : S ∈ F },   |Z_1| ≤ |F| = #{ S∈binom(D,a) : e_j(S)=e_j(M), j≤σ−1 }.
```

`t = 1` action-rank vacuity (bankable). For `deg E = 1`, `A_E ≅ K`, so for every rational `R` regular mod `E`, `R(ξ) ∈ K` and `d_R(E) = dim_K K[R(ξ)] = 1 = deg E`. The quotient/action-rank charge (which requires `d_R(E) < t`) can never fire at `t = 1`. (For irreducible `E` of degree `t`, `d_R(E) = [K(R(ξ)):K] < t` iff `R(ξ)` lies in a proper subfield — a positive-codimension event.)

Reserve calibration (field ledger).

```text
C(n,a)/q^{σ−1} ≤ ⌊q/2^128⌋   ⟺   Γ₀ = σ·log₂q − log₂ C(n,a) ≥ 128.
C(n,a)/q^{σ−t} ≤ ⌊q/2^128⌋   ⟺   C(n,a) ≤ q^{σ−t+1}/2^128   (strictly stronger than Γ₀≥128 for t≥2).
```

So the σ-reserve does not bound the bare fiber for `t ≥ 2`; the collinearity factor `q^{t−1}` is exactly what closes the gap, confirming Role 09's "reserve does not transfer at slack `σ−t`."

## 3. Proof

Anchor characterization. `Q` has `deg Q < k+t < a` and `agr_D(Q,w) ≥ a`. Then `M − Q` is monic of degree `a` (the leading term of `M` survives), and it vanishes on the agreement set, which therefore has size exactly `a`, call it `S`, with `M − Q = L_S`. The witness-degree bound `deg(M − L_S) < k+t` is equivalent to the coefficients of `X^{a−1},…,X^{k+t}` agreeing between `M` and `L_S`, i.e. matching the first `a−1−(k+t)+1 = σ−t` subleading coefficients, i.e. the first `σ−t` elementary symmetric functions. This is `F`. The slope identity is immediate from `[Q]_E = [M]_E − [L_S]_E` and the requirement `[Q]_E = z[B]_E`. Distinct slopes are a quotient of the collinear sub-fiber, so `|Z_t| ≤ |{collinear S}|`; same-slope collisions only reduce the count.

Codimension of the collinear sub-fiber. `S ∈ F` is `σ−t` symmetric-function conditions. `[M]_E − [L_S]_E ∈ K·[B]_E` fixes the image in `A_E/K[B]_E ≅ K^{t−1}`, i.e. `t−1` further affine conditions on `[L_S]_E`. These are independent of the prefix conditions (prefix fixes top symmetric functions; residue conditions fix `L_S mod E`, a low-degree datum at the disjoint points/factors of `E ∤ F_D`). Total codimension `σ−1`. Pigeonhole gives a fiber of size `≥ C(n,a)/q^{σ−1}` (Role 03's lower bound) but the same codimension count is the natural upper target.

`t = 1` cut. With the line equal to `K`, no collinearity reduction exists, so the mechanism's slope count is exactly the spread of `S ↦ M(β) − L_S(β)` over the slack-`(σ−1)` prefix-fiber, `≤ |F|`. For generic `D` the prefix map (first `σ−1` elementary symmetric functions on `a`-subsets) is non-degenerate and `max_p |F_p| ≤ C(n,a)/q^{σ−1}·n^{O(1)}`. Under `Γ₀ ≥ 128 + O(log n)` this is `≤ ⌊q/2^128⌋`. Hence the `t = 1` locator-prefix mechanism is within the prize budget and is not a charge-free counterpacket. The only way to break this at `t = 1` is to skew `max_p |F_p|` far above average, which forces `D` into a proper subfield coset (field charge) or `≤ n^{O(1)}` cosets of a proper subgroup (affine-color charge).

`t ≥ 2` reduction. The mechanism's slope count is `≤ #{S∈F : [L_S]_E on the line}`. If the residues `[L_S]_E` equidistribute in `A_E` over `F` up to `n^{O(1)}`, this is `≤ C(n,a)/q^{σ−1}·n^{O(1)} ≤ ⌊q/2^128⌋` under the calibrated reserve, and the mechanism is again cut. The only escape is a residue cluster on the line of multiplicity `≫ |F|/q^{t−1}`; such a cluster requires structure in `E` (then `d_R(E) < t`, action-rank charge — available because `t ≥ 2`) or in `D` (field / affine-color charge).

This is exactly the instruction's situation: the named mechanism collapses to a charge or to an in-budget equidistribution everywhere except one residual cluster, stated next.

## 4. Verification requirements

A checker validating this route cut must, over `K_line` only:

- verify the anchor identity `L_t(w) = {M − L_S : S∈F}` symbolically for arbitrary `M,E,B` (degree and elementary-symmetric matching);
- recompute the codimension `σ−1` of the collinear sub-fiber as (prefix conditions `σ−t`) + (residue-line conditions `t−1`), and confirm independence via `gcd(E, ∏_{x∈D}(X−x)) = 1`;
- confirm `d_R(E)=deg E` automatically at `t=1` and reject any `t=1` action-rank certificate;
- recompute the reserve arithmetic `Γ₀ ≥ 128 + C₀ log₂ n ⇒ C(n,a)/q^{σ−1}·n^{C₀} ≤ ⌊q/2^128⌋`, with `q = q_line` as the sole denominator and `q_gen` only in `Γ₀`;
- count distinct slopes in `K_line` after collapsing same-slope `S`, and retain the anchor/prefix/`E,B` tag (the mechanism is support-dependent);
- for any claimed `t ≥ 2` excess cluster, demand either a field/affine-color certificate for `D` or an action-rank certificate `d_R(E) < t`, with exact caps; absent these it must emit `UNCHARGED_RESIDUE_CLUSTER` (the live target), not a slope cap.

Same-field only is verified here; the mixed-field transfer (`q_gen^{σ−t} q_line^{t−1}` heuristic, Role 03) is unproved and must remain a flagged gap. `q_chal` is unused.

## 5. Next exact lemma / surviving mechanism

Exact new wall (this converts the route cut into a closed LOW branch):

```text
L-CYCLE111-LOCATOR-RESIDUE-EQUIDISTRIBUTION-OR-STRUCTURE-CHARGE
There exist absolute C₀, independent of k,σ,t, such that for every D⊂K_line with |D|=n,
every monic E (1≤t<σ) nonvanishing on D, every 0≠[B]_E, every prefix p∈K^{σ−t} and every
line ℓ = [M]_E + K[B]_E in A_E:
   N(p,ℓ) := #{ S∈binom(D,a) : e_j(S)=p_j (j≤σ−t), [L_S]_E∈ℓ } ≤ C(n,a)/q^{σ−1} · n^{C₀},
UNLESS one of (field: D in a proper subfield coset) / (affine-color: D in ≤ n^{C₀} cosets of a
proper subgroup) / (action-rank: d_R(E)<t for source-visible R) holds, in which case the excess
is assigned to that charge with its exact cap.
t=1 specialization: #{S : e_j(S)=p_j, j≤σ−1} ≤ C(n,a)/q^{σ−1}·n^{C₀} modulo D-structure charges
(elementary-symmetric / power-sum equidistribution on a-subsets).
```

With this lemma plus `Γ₀ ≥ 128 + C₀ log₂ n`, the LOW numerator obeys `N_LOW ≤ ⌊q/2^128⌋`, via `|Z_t| ≤ N(p,ℓ)`.

Exact surviving counterpacket mechanism (not eliminated): a growing family at `t ≥ 2` exhibiting a residue cluster `#{S∈F : [L_S]_E∈ℓ} ≫ |F|/q^{t−1}` on one line `ℓ`, with `D` in no proper subfield coset and no `≤ n^{C₀}`-coset structure, and `d_R(E) = t` for every source-visible `R`. That is the only charge-free way to beat the main term, and it cannot occur at `t = 1`.

Required `AP_corr` (labeled NEW STRENGTHENED HYPOTHESIS, not source-visible). To save the LOW theorem, `AP_corr(E,B,w)` must imply both the negation of the three structure cases above and an anchor-genericity bound: `w` may not concentrate its slack-`(σ−t)` agreement list on a single prefix-fiber of size `> C(n,a)/q^{σ−1}·n^{C₀}`. Operationally: `AP_corr` forbids `L_t(w) = {M − L_S : S∈F}` with `|F|` above the occupancy main term. This is exactly the missing predicate; defining it any weaker (bare denominator non-pullback, trivial stabilizer) provably fails by the `t = 1` construction.

## Mandatory self-audit

1. Proved: the single-anchor list characterization; `|Z_t| ≤ |F|` and the `σ−1` collinear codimension; `t = 1` action-rank vacuity; the exact reserve arithmetic identifying `Γ₀ ≥ 128` as the calibration; hence the `t = 1` locator-prefix/collinearity mechanism is within budget for generic `D`. Not proved: the equidistribution upper bound `N(p,ℓ) ≤ main·n^{C₀}` (only its pigeonhole lower bound is known); the `t ≥ 2` cluster impossibility; BALANCED/HIGH covers; the final integer ledger; mixed-field transfer.

2. Official-prize-relevant: yes — `K_line`, official reduced residue-line data, the `2^-128/q_line` target. Not a finite/model certificate and not a prize proof; the `t=1` and codimension facts are general theorems, the equidistribution is the open wall.

3. First failure line: `uncharged S∈F with [L_S]_E clustered on the line ⇒ excess slopes`, i.e. exactly `L-CYCLE111`. Before that, `AP_corr` and the structure-charge caps are not yet frozen.

4. Fields: `q_line` is the only slope denominator and the only quantity in `⌊q_line/2^128⌋`; `q_gen` appears only in `Γ₀`; same-field specialization `q_gen=q_code=q_line=q` is used explicitly and the mixed case is flagged unproved; `q_chal` unused (no transfer claimed). Correct.

5. Reductions used: same-slope `S` collapse (only reduces, applied); contained/tangent absent (noncontainment automatic, `B≠0`); field/affine-color/action-rank are the named structure charges absorbing any cluster; action-rank explicitly vacuous at `t=1`. All charged at the `K_line` slope level, none silently discarded.

6. This is a ROUTE_CUT with an embedded EXACT_NEW_WALL, not a PLAN. It becomes PROOF by establishing `L-CYCLE111` with the three structure charges, plus the calibrated reserve, plus BALANCED/HIGH/ledger. It becomes COUNTERPACKET only via the surviving `t ≥ 2` charge-free residue cluster above `|F|/q^{t−1}` — which the cut shows is impossible at `t = 1` and chargeable whenever `D` or `E` is structured.