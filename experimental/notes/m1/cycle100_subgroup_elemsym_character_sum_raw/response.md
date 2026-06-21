I'll start by reading the file index and the key project files to understand the current state.Let me read the key project files in parallel to understand the current state.Let me read the core state files and the cycle100 prompt note.Let me find the key cycle99/cycle100 note files and the wall/lemma files in the index.The index is very long. Let me grep for the specific cycle99/cycle100 note files I need.The key note files are referenced relative to `current_repo_snapshot/`. Let me locate them in the index and read the cycle99/cycle100 notes directly.Let me read the Cycle99 raw response and the Cycle98 audit to nail down the exact definitions and reduction chain.I have the complete picture now. Cycle98 reduced the active external root problem to `Θ_U = {θ∈F_p∖H : v(θ)∈P−M_s}`; Cycle99 banked the divisor/line/character-sum equivalences and the exact identity. Cycle100 asks me to prove or kill the cancellation bound. Let me work the mathematics and deliver.

---

# Cycle 100 — Subgroup Elemsym Moment Character Sum

**Classification: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

I do **not** prove the cancellation bound and I do **not** produce an aperiodic counterpacket. I bank an exact equivalence that shows the bound is *not a relaxation* of anything, then I expose the decisive structural fact that the literal character sum targets a **fiber-weighted** count `N` strictly larger than the prize numerator `|Θ_U|`. This splits Cycle100 into two genuinely separate sublemmas, cuts the termwise/Weil approach, makes the periodic-charging mechanism explicit, and proves the fiber bound in the structured (reserve-capped) cases.

## 0. Setup (not re-deriving Cycle98/99)

`p` prime, `n|p−1`, `H=μ_n≤F_p^*`, `∏_{x∈H}(X−x)=X^n−1`. `U` monic, `deg U=s+1`, `s=k+σ`, `k=ρn`, reserve `σ≥Cn/\log n`. `P=(P_1,…,P_{σ+1})` the power-sum prefix of `U`. `ψ` a nontrivial additive character. `L_t(X)=∑_{j=1}^{σ+1}t_jX^j`, `E_s(t)=e_s(\{ψ(L_t(x))\}_{x∈H})`, `S(t)=∑_{θ∉H}ψ(L_t(θ))`. Goal numerator: `Θ_U=\{θ∈F_p∖H : v(θ)∈P−M_s\}`, target `|Θ_U|≤n^{O(1)}`.

## 1. The reduction is an exact identity, not a bound (bankable)

Let `F(θ)=\#\{S⊆H,|S|=s : p_j(S)=P_j−θ^j,\ j≤σ+1\}` and `N=∑_{θ∉H}F(θ)`. Expanding the indicator `1[p_j(S)=c_j∀j]=p^{-(σ+1)}∑_tψ(∑_jt_j(p_j(S)−c_j))` with `c_j=P_j−θ^j`, using `∑_{x∈S}L_t(x)=∑_jt_jp_j(S)` and `∑_{|S|=s}∏_{x∈S}ψ(L_t(x))=E_s(t)`:

```
N = p^{-(σ+1)} Σ_t ψ(-<t,P>) E_s(t) S(t).
```

The `t=0` term is `E_s(0)=C(n,s)`, `S(0)=p−n`, so with `main:=C(n,s)(p−n)/p^{σ+1}`,

```
Σ := Σ_{t≠0} ψ(-<t,P>) E_s(t) S(t)  =  p^{σ+1}( N − main ).
```

`main≤2^n/(n+1)^σ≤2^{n(1−C/\ln 2)}≤1` for `C≥\ln 2` (side condition, holds in the intended reserve). Since `N∈ℤ_{≥0}`:

> **Lemma 1 (exact equivalence).** `|Σ| ≤ p^{σ+1}n^{O(1)} ⟺ N ≤ n^{O(1)}`.

This is an **identity**, so the character-sum form gives *no slack*: proving the boxed bound is *exactly* as hard as the combinatorial statement `N≤n^{O(1)}`. In particular:

> **Route-cut 1 (no pointwise estimate can work).** Any termwise/Weil/Gauss-sum bound is hopeless. Weil gives `|S(t)|≤σ√p+n`, but the only available bound on the symmetric transform is the trivial `|E_s(t)|≤C(n,s)`, so the termwise bound is `|Σ|≤p^{σ+1}·C(n,s)·(σ√p+n)` — off the target by the full factor `C(n,s)·√p`. The content lives entirely in the `t`-average, i.e. in `N` itself. Weil controls only `S(t)`; it never touches `E_s(t)`, which is the obstruction.

## 2. The decisive observation: `N` is fiber-weighted, `|Θ_U|` is support (ROUTE_CUT)

`N=∑_{θ∉H}F(θ)` counts **pairs** `(θ,S)`. The prize numerator is the **support** `|Θ_U|=\#\{θ:F(θ)≥1\}`. Writing `F_max:=\max_{c∈F_p^{σ+1}}\#\{S⊆H,|S|=s:p_{≤σ+1}(S)=c\}`:

> **Lemma 2 (split).** `N≤n^{O(1)} ⟺ ( |Θ_U|≤n^{O(1)} ) ∧ ( F_max≤n^{O(1)} )`.
> Proof: `N=∑_{θ∈Θ_U}F(θ)` gives `\max(|Θ_U|,F_max)≤N≤|Θ_U|·F_max`. ∎

So the literal character-sum bound silently bundles a **fiber-multiplicity bound `F_max≤n^{O(1)}`** that the prize goal does *not* require. `F_max≤poly` is **not** implied by `|Θ_U|≤poly`: a single external `θ` can have many `s`-subsets `S` with `S∪\{θ\}` carrying the prescribed prefix (`S_1,S_2` are Prouhet–Tarry–Escott-equivalent on `μ_n` to order `σ+1`). Hence:

> **Route-cut 2.** If `F_max` is superpolynomial for some aperiodic `P`, the boxed character-sum bound is **false** even though the prize target `|Θ_U|≤n^{O(1)}` may hold. The character sum as written is the **wrong object**: it weights each active root by its PTE-fiber. The correct target is the **distinct-point line incidence** of Cycle99's Lemma B (`θ` is recovered as `θ=e_1(S')+W_1`, so distinct points ↔ distinct `θ`), which deflates fibers automatically. To salvage the character-sum route one must separately prove the fiber bond `F_max≤n^{O(1)}`.

The support count is **not** itself a clean character sum: `1[F(θ)≥1]` is non-linear; `1[F(θ)≥1]≤F(θ)` recovers `N`, and the reverse needs `F_max`. This is precisely why the route cannot avoid `F_max`.

## 3. Which `t` resonate, and how the periodic core is charged (bankable)

`|E_s(t)|=C(n,s)` only at `t=0`. `E_s(t)` is *large* exactly when `\{ψ(L_t(x))\}_{x∈H}` is concentrated, i.e. when `L_t` factors through a quotient `H↠H/μ_M=μ_{n/M}` (`M|n`, `M>1`). Since `x↦x^j` is constant on `μ_M`-cosets iff `M|j`:

> **Resonant frequency support.** `L_t` descends to `μ_{n/M}` ⟺ `t` is supported on `Mℤ` (`t_j=0` for `M∤j`). These are the only `t` without symmetric-function cancellation.

The phase `ψ(-<t,P>)` pairs these with the projection of `P` onto coordinates `Mℤ`. **`P` aperiodic** (not supported on any `Mℤ`, `M|n`, `M>1`) is exactly the hypothesis that dephases the resonant `t`.

> **Charging the quotient-periodic core.** On resonant `t` (supported on `Mℤ`), set `\tilde L(y)=∑_i t_{Mi}y^i` (`deg≤⌊(σ+1)/M⌋`), so `L_t(x)=\tilde L(x^M)`. Then `\{ψ(L_t(x))\}_{x∈μ_n}` is the `M`-fold repetition of `\{ψ(\tilde L(y))\}_{y∈μ_{n/M}}`, and `S(t)=∑_{θ∉μ_n}ψ(\tilde L(θ^M))`. The resonant block is **the same problem one level down**: subgroup `μ_{n/M}`, reserve `σ'=⌊(σ+1)/M⌋−1≈σ/M`, same field. Recursing terminates at the aperiodic core. The combinatorial witness (union of `μ_M`-cosets) auto-satisfies the prefix only when `M>σ+1`, which forces `n/M<\log n`, capping that contribution at `2^{\log n}=n^{O(1)}`.

## 4. Partial proof of the fiber bound `F_max ≤ n^{O(1)}` (new, unconditional in structured cases)

> **Lemma 3 (PTE min-distance).** Distinct `S_1,S_2` in any fiber satisfy `|S_1△S_2|≥2(σ+2)`.
> Proof: equal `e_{≤σ+1}` gives `∏_{A}(1−xX)≡∏_{B}(1−xX)\pmod{X^{σ+2}}` for `A=S_1∖S_2,B=S_2∖S_1`, `|A|=|B|=w`. The difference has degree `≤w`; if `w≤σ+1` it vanishes, forcing `A=B=∅`. So `w≥σ+2`. (Equivalently: any nonzero `c∈\{∑c_xx^j=0,\,j≤σ+1\}` has Hamming weight `≥σ+2` by Vandermonde.) ∎

> **Lemma 4 (reserve cap on independent flips).** Any fiber generated from a base `S_0` by pairwise-disjoint balanced PTE swaps `(A_i,B_i)` has size `≤2^{\,n/(2(σ+2))}=2^{O(\log n)}=n^{O(1)}`, since each swap consumes `≥2(σ+2)` distinct points and `σ+2≥Cn/\log n`. ∎

All structured large fibers I can build — coset-pair swaps `(γμ_M,γ'μ_M)` with `M>σ+1`, nested-subgroup swaps, periodic patterns — are of this disjoint type and are capped at `n^{O(1)}` by Lemma 4, **even when the common prefix is aperiodic** (the periodicity hides in the swaps, not the prefix). This is strong evidence that `F_max≤n^{O(1)}` is **true** and that the reserve `σ≈n/\log n` is exactly the threshold that enforces it. The open case is fibers built from *overlapping* PTE patterns, where min-distance + packing only yields exponential bounds.

## 5. Exact next lemmas (PLAN → PROOF)

Cycle100 cleanly resolves into:

- **L1 (subgroup PTE-multiplicity / fiber bound).** `F_max=\max_c \#\{S⊆H,|S|=s:p_{≤σ+1}(S)=c\}≤n^{O(1)}` for aperiodic `c`, after periodic charging. Status: proved for disjoint/structured fibers (§4); open for overlapping null-patterns. This is the *smaller, more tractable* target and is where I have real partial progress.
- **L2 (support / line incidence).** `|Θ_U|=\#(ℓ∩E_{\le σ+1}(\binom{H}{m}))_{\text{distinct}}≤n^{O(1)}` — the prize numerator; sub-Johnson list decoding on a multiplicative subgroup for a structured received word. The dominant remaining wall.
- **Single-frequency seed.** Bound `e_s(\{ψ(c\,x^j)\}_{x∈H})` for one monomial `L_t=c\,x^j` (a Gauss-sum symmetric function); ladder to the full `(σ+1)`-frequency pencil with aperiodicity removing the `Mℤ`-support.

`N≤n^{O(1)} ⟺ L1∧L2`. **Proving L1∧L2 ⟹ PROOF** of the boxed bound and of Cycle99. A superpolynomial overlapping fiber for aperiodic `P` ⟹ **COUNTERPACKET to the bound as stated** (but not to the prize goal — see §2).

## 6. Checker spec (for Codex)

Extend `cycle99_divisor_line_incidence_check.py`. On small `(p,n,k,σ)`: (i) recompute `N` two ways — direct pair count vs. `p^{-(σ+1)}∑_tψ(-<t,P>)E_s(t)S(t)` — and assert equality and `Σ=p^{σ+1}(N−main)`; (ii) compute `F_max`, `|Θ_U|`, and verify `\max(|Θ_U|,F_max)≤N≤|Θ_U|·F_max`; (iii) sweep `P` periodic vs aperiodic; (iv) for each fiber, record `\min|S_1△S_2|` (assert `≥2(σ+2)`) and whether it is disjoint-swap-generated. Certificate: `{p,n,k,sigma,s, aperiodic, N, main, support=|Θ_U|, F_max, min_symdiff, johnson_gap=s²−kn, status}`. **Counterpacket trigger:** aperiodic family with `F_max/n^c→∞` (kills the literal bound) or `|Θ_U|/n^c→∞` (kills the prize goal).

## Self-audit

1. **Proved:** the exact identity `Σ=p^{σ+1}(N−main)` with `main≤1` (so the boxed bound ⟺ `N≤n^{O(1)}`, an *identity* — Lemma 1); the split `N≤poly ⟺ |Θ_U|≤poly ∧ F_max≤poly` (Lemma 2); PTE min-distance `≥2(σ+2)` (Lemma 3); the reserve cap `n^{O(1)}` on disjoint-swap fibers (Lemma 4); the resonant-`t`-support characterization and the periodic descent. **Not proved:** the boxed cancellation bound itself; L2 (`|Θ_U|≤poly`); L1 in the overlapping case. So **not** the polynomial bound in the live range.
2. **Research/model + bankable reduction**, not an official-prize theorem. (Even the boxed bound, if proven, only feeds the upper/safe side; it is not itself a prize statement.)
3. **First failure line:** the boxed bound targets the **fiber-weighted `N`, not the support `|Θ_U|`** (§2). If `F_max` is superpolynomial for aperiodic `P` (overlapping PTE patterns), the bound is *false as stated* while the prize goal can still hold. This is the exact line where the route, not the theorem, breaks.
4. **Ledgers:** single field, `p=q_gen=q_line=q_code=q_chal`, `n|p−1`, `k=ρn`, reserve `σ≥Cn/\log n`; the `2^{-128}` target ↔ requiring a polynomial list/support size. Used consistently; `main≤1` needs `C≥\ln 2`, flagged.
5. **Yes, decisively.** Quotient/periodic structure produces the resonant `t` (support `Mℤ`) and PTE swaps, which (a) need charging and (b) **inflate `N` above `|Θ_U|` via fibers** — the central reduction of the claimed numerator. Same-slope/contained collisions: `θ↦r` injective (Cycle99) so distinct points ↔ distinct `θ`; the inflation is purely the fiber `F(θ)`, capped to `n^{O(1)}` in all structured cases (§4). Affine color normalization does not further reduce the numerator here.
6. **PLAN→PROOF:** prove L1 (subgroup PTE-multiplicity, overlapping case) and L2 (sub-Johnson subgroup-RS support bound); together they give `N≤poly` and the boxed bound. **PLAN→COUNTERPACKET:** an aperiodic `P` with a superpolynomial overlapping fiber (kills the boxed bound) — but the prize-relevant falsifier must instead make the *support* `|Θ_U|` superpolynomial.

**Route to a full solve?** Yes, conditional on **L2** (the real wall) plus **L1** (now the cleaner secondary target, with §4 as genuine partial progress). The single sharpest recommendation: **stop bounding `N`; bound the distinct-point line incidence `|Θ_U|` directly** (Cycle99 Lemma B), and treat `F_max≤n^{O(1)}` as a separate, reserve-capped PTE-multiplicity lemma rather than smuggling it inside the character sum. The next exact object is the single-monomial slice `e_s(\{ψ(c\,x^j)\}_{x∈H})`, building to the aperiodic `(σ+1)`-frequency pencil.