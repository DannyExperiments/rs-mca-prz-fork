I'll start by reading the file index, then the core project files to understand the current state.Let me read the core project files in parallel to understand the current state.Now let me read the most recent cycle briefs and the active route board, banked lemmas, and walls.Let me read the cycle101 prompt, the recent briefs (99, 98), and the route board / banked lemmas / active walls.Now let me find and read the cycle101 prompt and the recent audit files. Let me locate them in the index.Let me read the key strategic files: route board, active walls, banked lemmas, and cuts.Now let me read the active walls, banked lemmas, and the cycle101 prompt. Let me find the snapshot files in the index first.Now let me read the banked lemmas and the key snapshot files (cycle101 prompt, cycle100 audit/response, cycle99 audit). Let me locate them in the index.Let me read the key Cycle 101 prompt and the Cycle 100/99 audit and response files directly.Now let me read the Cycle 100 and Cycle 99 audit/response files to get the precise mathematical setup.Let me read the Cycle 99 audit and response, which contain the divisor/reciprocal-affine-line forms central to this cycle.Let me read the Cycle 98 audit (for the moment-curve normal form) and the Cycle 100 raw response (for PTE detail), plus the Cycle 99 raw response.Let me read the Cycle 99 and Cycle 100 raw responses to get the full mathematical detail, plus the Cycle 99 prompt for setup context.This is very thorough. Now let me read the Cycle 100 raw response for the PTE detail and the precise definitions, plus the Cycle 100 prompt.I have a complete picture of the state. I've read the Cycle 98/99/100 audits and raw responses, the route board, active walls, banked lemmas, and the Cycle 101 prompt. Only the `Read` tool is wired up in this run (consistent with the Cycle 99/100 notes that they could not write files), so I deliver the complete worked answer inline, with a checker spec for Codex.

---

# Cycle 101 — Distinct Line Incidence Or PTE Fiber Split

**Classification: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

I do **not** prove `L2` (`|Θ_U| ≤ n^{O(1)}`) and I do **not** produce a counterpacket. I bank: (i) a new exact reformulation of `L2` as a **finite-field uncertainty / prescribed-Fourier-coefficient** problem for `0/1` indicators; (ii) a rigorous **reserve-threshold calibration** showing `σ ≥ n/log₂p` is *exactly* the line where the first moment drops to `≤ 1`; (iii) a rigorous **route-cut**: the witness sets of distinct active roots form a constant-weight code of minimum distance `≥ 2σ+2`, and such codes can be superpolynomial, so packing/min-distance alone cannot prove `L2` — the proof must use the one-parameter (line) structure, not pairwise distance; (iv) the **exact transversality wall** and the **exact multiplicative-BKR counterpacket target**, with the precise reason large `p` blocks it.

## 0. Setup (not re-deriving Cycle 98/99)

`p` prime, `n | p−1`, `H = μ_n ≤ F_p^*`, so `∏_{x∈H}(X−x) = X^n−1`. `U` monic, `deg U = s+1`, `s = k+σ`, `k = ρn`, reserve `σ ≥ Cn/log n`. `P = (P_1,…,P_{σ+1})` the power-sum prefix of `U`. `m = n−s`. Banked equivalent forms:

```text
θ∈F_p∖H active
 ⟺ ∃ S⊆H,|S|=s : p_j(S)=P_j−θ^j  (j≤σ+1)                       [moment, C98]
 ⟺ ∃ S'⊆H,|S'|=m : p_j(S') = θ^j − P_j  (j≤σ+1)                 [complement]
 ⟺ ∃ S'⊆H,|S'|=m : g_{S'} ≡ (1−θX)W mod X^{σ+2}, W=Ũ^{-1}        [reciprocal line, C99]
 ⟺ ∃ deg-s divisor f|X^n−1 : deg(U−(X−θ)f)<k                     [divisor/codeword, C99]
```

`θ ↦ S'` is well-defined and the map `θ ↦ (witness S')` is injective on distinct active roots, because `θ = p_1(S') + P_1` is recovered from `S'` (Cycle 99). Hence

```text
|Θ_U| = #{ distinct θ } = #( ℓ ∩ E_m )_distinct,
ℓ = { ((−1)^i(W_i−θ W_{i−1}))_{i=1}^{σ+1} : θ∈F_p } ⊂ A^{σ+1},
E_m = { ((−1)^i e_i(S'))_{i=1}^{σ+1} : S'⊆H, |S'|=m }.
```

This is the exact prize numerator. Below I keep everything at `|Θ_U|`; I never sum over witnesses (that would give the weighted `N` cut in Cycle 100).

## 1. New exact reformulation: prescribed-Fourier-coefficient / uncertainty form (BANKABLE)

> **Lemma 1 (DFT-indicator form).** Identify `S'⊆μ_n` with its indicator `c:μ_n→{0,1}`. Because `x^n=1`, the power sums are the group-algebra Fourier coefficients
> ```text
> p_j(S') = Σ_{x∈μ_n} c(x) x^j = ĉ(j),    ĉ(0)=|S'|=m,
> ```
> and `ĉ(j)` depends only on `j mod n`. Therefore
> ```text
> θ∈F_p∖H active  ⟺  ∃ c∈{0,1}^{μ_n} with ĉ(0)=m and ĉ(j)=θ^j−P_j (j=1,…,σ+1).
> ```
> Consequently `|Θ_U| = #{θ∉H : the window (θ^j−P_j)_{j=1}^{σ+1} is the spectrum of a weight-m 0/1 indicator on μ_n}`.

**Proof.** Characters of `μ_n` are exactly `x↦x^j`, `j∈Z/n`; `p_j(S')=Σ_{x∈S'}x^j=ĉ(j)` is the evaluation of `c` against that character. The active condition `p_j(S')=θ^j−P_j` is the prescription of `ĉ(j)` on `j=1,…,σ+1`, and `ĉ(0)=m` fixes the weight. ∎

This is the source-correct way to keep the **support indicator** `1[F(θ)>0]` without reverting to `N`: the count is a per-`θ` **feasibility** (does an indicator with the prescribed spectral window exist), not a sum `Σ_c` over witnesses. The tension is now explicit and classical: `θ^j` for `θ∉μ_n` is the restriction of a *non-`μ_n`-character* geometric sequence (aperiodic in `j`), while `ĉ(j)` is the spectrum of a genuine `μ_n`-subset (which is `n`-periodic in `j`). `L2` asks how many external frequencies `θ` can be matched on the length-`(σ+1)` window by an honest weight-`m` `0/1` spectrum. This is a finite-field uncertainty-principle question (Tao-type / BCH-spectral), and it is the right home for the problem.

## 2. Quotient-periodic charging, in DFT terms (BANKABLE, matches C100 §3)

Call `P` **`M`-periodic** (`M|n`, `M>1`) if `P_j=0` for `M∤j` (equivalently `U(X)=V(X^M)`). 

> **Lemma 2 (periodic descent).** If `P` is `M`-periodic and `M>σ+1`, the only constraints are `ĉ(j)=θ^j` for `j=1,…,σ+1`, and the contribution of indicators `c` that are unions of full `μ_M`-cosets is **at most one** `θ` (forced `θ=P_1`), because such `c` have `ĉ(j)=0` for `0<j<M`, forcing `θ^j=0`, impossible unless the window is degenerate. General `M`-periodic `P` (`M≤σ+1`) reduces the whole problem to the subgroup `μ_{n/M}` with reserve `σ' ≈ σ/M`, same field; recursing terminates at the **aperiodic core** `P` (not supported on any proper `MZ`). The aperiodic core is the only place `L2` has content; the periodic strata are charged by descent and the `M>σ+1` cap forces `n/M<log n`, capping that contribution at `n^{O(1)}`.

So from here `P` is aperiodic. (This also kills the naive counterpacket: any union-of-cosets witness family gives a single `θ`.)

## 3. Rigorous reserve-threshold calibration (BANKABLE)

The exact first-moment identity (Cycle 99/100) gives `|Θ_U| ≤ N = main + error` with

```text
main = C(n,s)(p−n)/p^{σ+1} ≤ 2^n / p^σ = 2^{ n − σ·log₂ p }.
```

> **Lemma 3 (threshold).** `main ≤ 1 ⟺ σ ≥ n/log₂ p`. Since `p ≥ n+1`, `σ ≥ n/log₂ n` (i.e. the banked reserve with `C ≥ ln2`) already forces `main ≤ 1`. Hence in the entire live reserve range the *main term contributes ≤ 1 active root*; **`L2` is equivalent to bounding the pure error character sum `|error| ≤ n^{O(1)}`**, and any superpolynomial `|Θ_U|` must come entirely from the error term, i.e. from algebraic concentration of `E_m` on the line `ℓ`.

This pins the hardness location exactly: reserve `σ ≈ n/log n` is the precise threshold where the "expected" count drops below `1`, and the problem is whether a *specific* aperiodic `U` can force the error to be large for large `p`.

## 4. Rigorous route-cut: min-distance/packing cannot prove L2 (BANKABLE, ROUTE_CUT)

> **Lemma 4 (witness min-distance — and its insufficiency).** For distinct active `θ≠θ'` with witnesses `S'_θ, S'_{θ'}`,
> ```text
> g_{S'_θ}(1−θ'X) ≡ g_{S'_{θ'}}(1−θX) ≡ (1−θX)(1−θ'X)W  (mod X^{σ+2}),
> ```
> so the size-`(m+1)` multisets `S'_θ∪{θ'}` and `S'_{θ'}∪{θ}` share the first `σ+1` power sums; by the generating-function degree argument (`g_A=g_B` if `deg<σ+2`) their symmetric difference is `≥ 2(σ+2)`, whence
> ```text
> |S'_θ △ S'_{θ'}| ≥ 2σ+2.
> ```
> Thus the witnesses form a length-`n`, constant-weight-`m`, **minimum-distance-`(≥2σ+2)` code**. But a binary constant-weight code at distance `δ ≈ 2σ ≈ 2n/log n` can have size `2^{Ω(n loglog n / log n)}` (linear-programming/Plotkin regime), which is **superpolynomial**. Therefore packing/minimum-distance bounds **cannot** prove `L2`.

This is a clean, rigorous statement of *why* the Cycle 100 min-distance lemma (`≥2(σ+2)`) is structurally insufficient for the distinct-root target: distance alone permits superpolynomially many witnesses. The proof of `L2` must use that the witnesses are not an arbitrary distance-`2σ` code but are pinned to the **one-parameter family `a(θ)=W−θ·XW`** on the line `ℓ`. So the live object is genuinely a **line–incidence / transversality** statement for `E_m`, not a coding-distance statement.

## 5. The exact transversality wall (EXACT_NEW_WALL)

> **L2 ⟺ line-incidence transversality.** `|ℓ ∩ E_m|_distinct ≤ n^{O(1)}`, where `E_m ⊂ A^{σ+1}` is the truncated elementary-symmetric image of `{S'⊆μ_n : |S'|=m}` and `ℓ` is the explicit affine line of §0.

The two sub-routes, each with a precise object:

- **(Padé/linear-complexity form of the wall).** The truncated window `(θ^j−P_j)_{j=1}^{σ+1}` has a Padé/Berlekamp–Massey denominator `Q_θ(X)` of degree `≤ ⌈(σ+1)/2⌉` whose coefficients are rational functions of `θ` of bounded degree. `θ` active ⟹ `Q_θ` divides `X^n−1` (its roots, reciprocally, lie in `μ_n`) **and** extends to a degree-`m` divisor. **Wall:** show the family `{Q_θ}` meets the (finite) set of divisors of `X^n−1` in only `n^{O(1)}` parameters `θ`, i.e. the parametrized divisibility `Q_θ(X) | X^n−1` is a *nontrivial* condition in `θ` of controlled degree. The danger is exactly that `Q_θ` could be *constant in degree* (low essential support) while sweeping many divisors.

- **(Uncertainty form of the wall, from §1).** Bound the number of external frequencies `θ` whose length-`(σ+1)` geometric window is a weight-`m` `μ_n`-subset spectrum. **Wall:** a quantitative finite-field uncertainty principle saying a `0/1` indicator on `μ_n` cannot have its spectrum agree with `σ+1` distinct external geometric windows unless `θ` ranges over an `n^{O(1)}`-size set.

## 6. The exact counterpacket target, and why large `p` blocks it (EXACT_NEW_WALL)

By §3 a counterpacket must drive the **error** term superpolynomial with **aperiodic** `P`. The only mechanism that concentrates `E_m` on a line is a **multiplicative analogue of Ben-Sasson–Kopparty–Radhak