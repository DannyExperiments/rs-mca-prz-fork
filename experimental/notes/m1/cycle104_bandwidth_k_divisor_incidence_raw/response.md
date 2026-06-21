I'll start by reading the file index, then the core project files to understand the current state of the research.Let me read the key project files referenced in the prompt. I'll start with the core state files and the cycle103/104 specific files.Now the key technical files: the cycle103 audit and raw response.I have the core bandwidth-1 proof. Now let me read the foundational definitions and the cycle102 false route to understand the exact setup, "reserve", "aperiodic", and what was killed.Now let me read the state files and the briefs for the recent cycles to lock down the setup, "reserve", "aperiodic", and the q-parameters.Let me read the active walls, banked lemmas, cuts, and the cycle 99-101 briefs to lock the exact definitions of reserve, aperiodicity, and the setup.Let me read the ACTIVE_WALLS and BANKED_LEMMAS files for exact definitions of the setup, reserve, and the q-ledger.Let me read more of ACTIVE_WALLS to understand the foundational setup, and key earlier cycle briefs.Now let me read the BANKED_LEMMAS for the exact foundational definitions and the cycle100/98 briefs.Let me continue reading the banked lemmas and the foundational cycle 97/98 setup, then the cuts file.Let me read the CUTS file and the foundational cycle 97/98 briefs to lock the setup and the meaning of "reserve" and "aperiodic".Let me read the cycle98, cycle100 briefs and the route board to fully lock the foundational setup and definitions of reserve.Let me read the route board and the cycle 97, 96 briefs for the full foundational setup.## Classification

```text
PROOF             (bandwidth k=2, s=σ+2:  |Θ_U| ≤ C(n,2)(σ+1) = O(n²σ) ≤ O(n³),
                   UNCONDITIONAL in Uhat and p — no aperiodicity, no reserve hypothesis)
+ PROOF           (every FIXED k≥2:  |Θ_U| ≤ C(n,k)(σ+1) = O(n^k·σ), via divided differences)
+ EXACT_NEW_WALL  (UNIFORM-in-k bound: the C(n,k) factor is superpolynomial for growing k;
                   the divided-difference / elimination tools give only n^{O(k)}.)
```

Route to a full solution: **yes, and now closed, for the named first target k=2** (and for each fixed bandwidth). The danger the Cycle103 response flagged — a positive-dimensional "divisor-degeneracy" family in `(θ,ρ)` created by periodic `Uhat` — **does not exist for any k**; I prove the incidence variety is always finite. The only thing that degrades with growing `k` is the *degree* of the certificate, not its existence. I give the exact residual lemma in §6.

I work read-only (only a file reader is exposed), so all algebra is hand-derived and self-contained; I flag one finite checker for Codex replay in §7, mirroring the Cycle103 `b1_divisor_bound_check.py`.

---

## 1. Setup and the reverse reformulation

Banked data (Cycle102/103): `p` prime, `n | p-1`, `H = μ_n ⊆ F_p^*`, `Uhat(0)=1`, write `Uhat = Σ_{j≥0} u_j X^j` (`u_0=1`). Fix `σ ≥ 1`, bandwidth `k`, `s = σ+k`, `m = n-s`. Co-locator:

```text
G(θ,X) = [(1-θX)^{-1} Uhat(X)]_{deg_X ≤ σ+1} = Σ_{l=0}^{σ+1} g_l(θ) X^l,
g_l(θ) = Σ_{i=0}^{l} u_{l-i} θ^i.
```

Each `g_l` is **monic of degree exactly `l`** in `θ` (leading term `u_0 θ^l = θ^l`); in particular `g_0 = 1`, `g_1 = u_1+θ`, and `g_{σ+1}` is monic of degree `σ+1`. The banked activity equivalence (the prompt's target form) is

```text
θ active  ⟺  ∃ ρ∈F_p[X], deg ρ ≤ k-2,  G(θ,X) + X^{σ+2}ρ(X)  |  1 - X^n.      (★)
```

**Reverse it.** A polynomial `f` with `f(0)=1` and `deg f = s` divides `1-X^n` iff its reverse `f̃(X)=X^s f(1/X)` (monic, degree `s`) divides `X^n-1 = ∏_{x∈μ_n}(X-x)`, iff `f̃ = ∏_{x∈ S̄}(X-x)` for a unique `S̄ ⊆ μ_n`, `|S̄|=s` (`X^n-1` is squarefree and split since `n|p-1`). Reversing `f = G(θ,X)+X^{σ+2}ρ` gives

```text
f̃(X) = B_θ(X) + ψ(X),   B_θ(X) = X^s + g_1(θ)X^{s-1} + … + g_{σ+1}(θ)X^{k-1},
```

where `ψ = ρ̃` ranges over **all** polynomials of degree `≤ k-2` (it fills the bottom `k-1` coefficients, degrees `0,…,k-2`). So `(★)` is equivalent to:

```text
θ active  ⟺  ∃ ψ, deg ψ ≤ k-2,  B_θ(X)+ψ(X)  splits completely over μ_n
          ⟺  ∃ S̄⊆μ_n, |S̄|=s, and deg-(k-2) poly ψ, with B_θ(x)=-ψ(x) ∀x∈S̄.   (♦)
```

In words: **`θ` is active iff the `s` points `{(x, B_θ(x)) : x∈S̄}` lie on the graph of a single polynomial of degree `≤ k-2`, for some `s`-subset `S̄⊆μ_n`.** (This is exactly Cycle99's "`deg(U-(X-θ)f)<k`" and the RS-proximity statement "`B_θ|_{μ_n}` is within distance `m` of the degree-`(k-2)` RS code".) Distinct active `θ` ↔ distinct `e_1(S̄) = -[X^{s-1}]B_θ = -g_1(θ) = -(u_1+θ)`, an **affine bijection in `θ`**, so `|Θ_U| = #{active θ}` with no color/normalization slack to recover.

---

## 2. PROOF for k = 2

Here `k-2=0`, so `ψ = c` is a constant, `s=σ+2`, and `B_θ(X)=X^s+g_1(θ)X^{s-1}+…+g_{σ+1}(θ)X` has zero constant term. By `(♦)`:

```text
θ active  ⟺  ∃ c∈F_p, ∃ S̄⊆μ_n, |S̄|=s,  B_θ(x) = -c  for all x∈S̄.
```

That is, **`B_θ` takes one common value `-c` at `s` distinct points of `μ_n`** (a fiber of size `s`). Since `s = σ+2 ≥ 3 ≥ 2`, any active `θ` forces at least one coincidence:

> there exist **distinct** `x,y∈μ_n` with `B_θ(x) = B_θ(y)`.

For a fixed unordered pair `{x,y}`, `x≠y`, define the single-variable polynomial

```text
Δ_{x,y}(θ) := B_θ(x) - B_θ(y) = (x^s-y^s) + Σ_{l=1}^{σ+1} g_l(θ)(x^{s-l}-y^{s-l}).
```

The term `g_l(θ)(x^{s-l}-y^{s-l})` has degree `l` in `θ`; the highest is `l=σ+1` (giving `x^{s-σ-1}-y^{s-σ-1}=x^{k-1}-y^{k-1}=x-y` for `k=2`). Hence

```text
[θ^{σ+1}] Δ_{x,y} = ([θ^{σ+1}]g_{σ+1})·(x-y) = 1·(x-y) ≠ 0,
```

so **`Δ_{x,y}` is a nonzero polynomial in `θ` of degree exactly `σ+1`**, with at most `σ+1` roots. Every active `θ` is a root of `Δ_{x,y}` for the pair `{x,y}` realized inside its `S̄`. Therefore

```text
Θ_U ⊆ ⋃_{ {x,y}⊆μ_n, x≠y } { θ : Δ_{x,y}(θ)=0 },

|Θ_U|  ≤  C(n,2)·(σ+1)  =  (σ+1)·n(n-1)/2  =  O(n²σ)  ≤  O(n³).        ∎
```

The bound is **unconditional in `Uhat`** (no aperiodicity), **uniform in `p`** (if `p ≤ C(n,2)(σ+1)` it is trivial; otherwise the root count applies), and counts a *superset* of the external roots `Θ_U ⊆ F_p\H`, so it is a valid upper bound. Periodic/quotient `Uhat` is a special case and can only shrink the active set; nothing must be charged separately. This **closes the bandwidth-2 wall**, exactly paralleling Cycle103's `k=1` closure.

The leading coefficient `(x-y)≠0` is the whole mechanism: it is the precise `k=2` analogue of the Cycle103 fact that the pseudo-remainder cannot vanish because `g_1=u_1+θ` is non-constant. **No periodic degeneracy can defeat it**, answering the open worry from the Cycle103 response.

---

## 3. PROOF for every fixed k ≥ 2 (divided differences)

For `k≥3`, the `s` points of `S̄` lie on a *non-constant* degree-`(k-2)` graph, so two `B_θ`-values need not coincide — the `k=2` argument is genuinely special. Replace "two equal values" by the order-`(k-1)` divided difference, which annihilates degree-`(k-2)` polynomials.

By `(♦)`, `B_θ = -ψ` on `S̄` with `deg ψ ≤ k-2`. Since `s = σ+k ≥ k`, pick any `k`-subset `{x_1,…,x_k}⊆S̄`. The divided difference of `B_θ` over these `k` nodes equals that of `-ψ`, which is `0` (order-`(k-1)` divided difference of a degree-`≤k-2` polynomial). Using the classical identity (the order-`(k-1)` divided difference of `X^e` over `k` distinct nodes is the complete homogeneous symmetric polynomial `h_{e-(k-1)}`, with `h_{<0}=0`):

```text
P_{x_1..x_k}(θ) := B_θ[x_1,…,x_k] = Σ_{l=0}^{σ+1} g_l(θ)·h_{σ+1-l}(x_1,…,x_k)      (s-(k-1)=σ+1)
```

Top `θ`-term: `l=σ+1` gives `g_{σ+1}(θ)·h_0 = g_{σ+1}(θ)`, so `[θ^{σ+1}]P_{x_1..x_k} = 1` **regardless of the nodes**. Thus `P_{x_1..x_k}` is **monic of degree `σ+1` in `θ`** — in particular nonzero — and every active `θ` is a root of `P_{x_1..x_k}` for some `k`-subset of `μ_n`. Hence

```text
|Θ_U|  ≤  C(n,k)·(σ+1)  =  O(n^k · σ).        ∎  (polynomial in n for each fixed k)
```

For `k=2` this recovers §2 (`B_θ[x,y]=Δ_{x,y}/(x-y)`, monic degree `σ+1`).

---

## 4. No divisor-degeneracy for any k (finiteness of the incidence variety)

This directly kills the Cycle103-response worry that periodic `Uhat=Uhat^*(X^d)` could create a positive-dimensional `(θ,ρ)` family. Work over `K=F̄_p`. Divide `X^n-1` by the monic `Φ(θ,c,X)=B_θ(X)+ψ_c(X)` (`c=(c_0,…,c_{k-2})` the free low coefficients): `X^n-1 = QΦ + R`, `R=Σ_{i<s}R_i(θ,c)X^i`. Then

```text
V(I) := { (θ,c) : R_i(θ,c)=0 ∀i } = { (θ,c) : B_θ+ψ_c = ∏_{x∈S̄}(X-x), some S̄⊆μ_n, |S̄|=s }.
```

For each of the `C(n,s)` target polynomials `∏_{x∈S̄}(X-x)`, matching coefficients of `X^{s-1},…,X^{k-1}` gives `g_1(θ)=-e_1(S̄)` (so `θ = -e_1(S̄)-u_1` is **forced uniquely**) plus `σ` consistency equations; matching `X^{k-2},…,X^0` then forces `c`. So each `S̄` contributes **at most one** point. Therefore

```text
|V(I)| ≤ C(n,s) < ∞    for every k.
```

`V(I)` is `0`-dimensional, so it contains **no curve** — neither one dominating the `θ`-axis (the "degeneracy" family) nor a vertical line — and the elimination ideal `I_θ = I∩K[θ]` is nonzero. Hence the active set is finite for every `k`; the only open issue is its *size/degree*, not its finiteness.

---

## 5. Why this is prize-relevant and what it is not

The result is **official-upper-side structure for the bandwidth-stratified numerator** `|Θ_U|=|e_1(V)|`, the exact object named since Cycle99. It closes the `k=2` stratum as a theorem (parallel to Cycle103's `k=1`) and each fixed-`k` stratum, **uniformly in `p` and in `Uhat`**. It does **not** complete the full RS-MCA upper theorem, which needs the bound *uniform over growing `k`* (constant-rate codes have `k=Θ(n)`), and it does not merge the finite-frontier / prize ledger. No `q`-ledger or `2^{-128}` crossing is invoked; the count is a single-field structural bound that composes safely with any later `q`-instantiation.

---

## 6. EXACT_NEW_WALL — the uniform-in-k bound

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE.
Prove |Θ_U| ≤ n^{O(1)} with the exponent INDEPENDENT of k (k up to Θ(n)),
or produce an aperiodic Uhat (above corrected reserve) with k≥3 and
superpolynomially many distinct active θ.
```

Why the present tools stop here, exactly:
- The divided-difference union (§3) needs one `k`-subset of `μ_n` per active `θ`, costing `C(n,k)` — superpolynomial once `k` grows.
- The elimination of the `k-1` free coefficients `c` (§4) by iterated resultants inflates the degree of the certificate `Ψ(θ)` to `n^{O(k)}`; and the *minimal* `Ψ∈I_θ` has degree `=|Θ_U|` (its squarefree vanishing set), so bounding `deg Ψ` by `poly(n)` is logically equivalent to the target — not a shortcut.

The exact next lemma (what converts this to full PROOF): **a `k`-uniform degree bound** — a nonzero `Ψ(θ)∈F_p[θ]` of degree `n^{O(1)}` (independent of `k`) vanishing on `Θ_U`. A promising concrete form: bound `#{x∈μ_n : B_θ(x)=-ψ(x)}≥s` simultaneously over the `(k-1)`-dimensional `ψ`-space by a *single* subresultant/Wronskian determinant in `θ` whose degree is controlled by `n` and `σ` but not `k`. The complementary deliverable (COUNTERPACKET): an aperiodic above-reserve `Uhat` with `k≥3` for which `B_θ|_{μ_n}` lies within distance `m` of the degree-`(k-2)` RS code for `n^{ω(1)}` distinct `θ`. By §2 this is impossible at `k=2`; the danger, if any, lives only at `k≥3`.

---

## 7. Replayable checker spec (for Codex, like cycle103)

Deterministic, small, `O(n²σ)`-cheap. For primes `p` with `n|p-1`, choose `μ_n⊆F_p`, random aperiodic `Uhat` (`Uhat(0)=1`), `k∈{2,3,4}`, growing `σ`:
1. **Ground truth.** `active₁ = { θ∈F_p : ∃ S̄⊆μ_n,|S̄|=s, deg(B_θ - interp_{≤k-2}) … }` computed directly as `{ θ : ∃ψ, deg ψ≤k-2, gcd(B_θ+ψ, X^n-1) has degree s }`, equivalently `min over degree-s divisors f|X^n-1 of deg(B_θ mod f) ≤ k-2`.
2. **Predicate equivalence.** Check `active₁` equals the `(★)` form `{ θ : ∃ρ, G(θ,X)+X^{σ+2}ρ | 1-X^n }` (sanity vs the banked equivalence and the Cycle102 `F_29` instance).
3. **Bound certificate (k=2).** Verify `|active₁| ≤ C(n,2)(σ+1)` and, sharper, that every `θ∈active₁` is a root of some `Δ_{x,y}` (`x≠y∈μ_n`); report `max_distinct_theta` (expect tiny, consistent with Cycle101's `=1`).
4. **k≥3.** Verify every `θ∈active₁` is a root of some order-`(k-1)` divided difference `B_θ[x_1,…,x_k]` over a `k`-subset, and `|active₁| ≤ C(n,k)(σ+1)`.
5. **Wall probe.** Sweep growing `(σ,k)` with `k=⌈c·n⌉` and log `|active₁|` vs `C(n,k)(σ+1)`; a reproducible superpolynomial growth in `|active₁|` would be a `k≥3` counterpacket trigger.
`PASS` = predicate equivalence holds and the fixed-`k` bounds hold on all sampled instances.

---

## Self-audit

**1. Proved vs not proved.** Proved: `(★)⟺(♦)` (reverse co-locator form); for `k=2`, active `θ` force a value-coincidence of `B_θ` on `μ_n`, giving `|Θ_U|≤C(n,2)(σ+1)=O(n²σ)`; for every fixed `k≥2`, the order-`(k-1)` divided difference over any `k`-subset of `S̄` is a monic degree-`(σ+1)` polynomial in `θ`, giving `|Θ_U|≤C(n,k)(σ+1)`; and the incidence variety `V(I)` is finite (`≤C(n,s)` points) for all `k`, so no divisor-degeneracy. **Not proved:** a `k`-uniform `poly(n)` bound (so not the constant-rate `k=Θ(n)` case); not the full RS-MCA upper theorem; no ledger merge.

**2. Prize-relevant or research-only.** Prize-relevant upper structure for the named wall `W-CYCLE104` at fixed bandwidth — it closes the `k=2` stratum (and each fixed `k`) as a `p`-uniform, `Uhat`-uniform theorem, the same status Cycle103 gave `k=1`. It is not by itself the full prize.

**3. First line that could fail.** For `k=2`: the necessary coincidence needs `s≥2` (here `s=σ+2≥3`), and `Δ_{x,y}` nonzero needs `[θ^{σ+1}]g_{σ+1}=1`, i.e. `Uhat(0)=u_0=1` (given) — both unconditional, so the `k=2` chain has no conjectural step. For fixed `k`: additionally `s≥k` (true) and the standard divided-difference/`h`-identity (characteristic-free). The chain first breaks at the `fixed-k → growing-k` boundary, where the `C(n,k)` union (or the `n^{O(k)}` resultant) ceases to be polynomial.

**4. q_gen, q_line, q_code, q_chal, 2^{-128}.** Correctly **not invoked**: this is single-field upper-side structure on `|Θ_U|`. No `2^{-128}` crossing is asserted; the bound is `p`-uniform, so it composes safely with any later `q`-instantiation. Field ledgers stay unmerged.

**5. Could quotient/periodic, contained incidences, same-slope collisions, or affine color normalization reduce the numerator?** None reduce *validity* — each can only *shrink* the active set. Periodic `Uhat=Uhat^*(X^d)` is a special case obeying the same `O(n^k σ)` bound. The count is on **distinct** `θ` from the start, and `θ=-e_1(S̄)-u_1` is already the affine-normalized invariant `e_1(V)`, so same-slope collisions and color normalization are absorbed (they make the truth smaller, not the bound invalid).

**6. If PLAN, what converts it.** §2–§4 are PROOF, not PLAN. The residual §6 wall converts to full PROOF via a `k`-uniform nonzero `Ψ(θ)` of degree `n^{O(1)}` on `Θ_U` (e.g. a single subresultant/Wronskian determinant eliminating the `(k-1)`-dim `ψ`-space with `k`-independent `θ`-degree), or to COUNTERPACKET via an aperiodic above-reserve `Uhat` with `k≥3` and `n^{ω(1)}` distinct active `θ` — found by step 5 of the checker, never by the dead Cycle102 short-window Padé route.