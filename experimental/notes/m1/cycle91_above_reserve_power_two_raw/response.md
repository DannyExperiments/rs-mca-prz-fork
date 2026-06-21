I'll start by reading the file index, then work through the key project files to understand the current state before attacking the Cycle 91 target.The index is huge. Let me read the core state files directly, starting with the most important ones for understanding current state.Let me read the director state and the key cycle briefs and audits in parallel.Now let me read the key recent audit files and the cycle91 prompt. Let me find the m1 notes paths first.Let me search the index for the specific m1 note files.Let me directly read the key recent audit files referenced in the prompt.Now the Cycle89 and Cycle87 audits, plus the cycle90 raw response.Now the Cycle87 audit and the cycle91 prompt file:Now let me read the cycle90 raw response and the cycle91 prompt to understand the framing and the tau_star definition.I have a clear picture of the state. Now I need the actual source definitions (`def:mca`, `def:residue`, `thm:normalform`, `prop:prize`, `prop:qfloor`, `thm:cap`, reserve $\tau^*$, quotient floor $A_{cl}$). Let me locate the tex files.Let me find and read the source tex files for the precise definitions. Let me grep the index for the tex paths.Now let me find the tex files. Let me search the index around where tex/ files would appear.I have strong context. Let me get the precise source definitions. Let me locate the tex files in the index.Let me read the key source tex files. RS_disproof_v3.tex defines the prize and reserve; let me read it.This is the core source. Let me continue reading for the quotient floor, $A_{cl}$, and prize-tier propositions.I have enough to give a rigorous answer. Let me verify the one arithmetic fact I'm leaning on hardest before writing — the multiplicative order of 5 mod 256 and the 2‑adic valuation — by hand, and cross-check the locator lemma statement I read in `RS_disproof_v3.tex` (lem:locator + lem:dsh). Both are confirmed in the source I read. Here is the result.

---

BANKABLE_LEMMA / CONDITIONAL  (with an EXACT_NEW_WALL on the deployed‑prime case)

It progresses `W-CYCLE91` substantially: the literal target is **achievable** over an odd‑characteristic extension field, by a mechanism Cycle90 did not try. I do **not** upgrade this to a deployed‑prize counterpacket.

## 1. Executive verdict and confidence

The literal Cycle91 statement — *find `q ≤ 2^256`, a power‑of‑two subgroup `H ≤ F_q^*`, prize rate `ρ`, residue‑line datum with `gap = t/|H| > (1+ε)τ*` and `Λ^{NC} > floor(q/2^128)`* — is **satisfiable**, and I give an explicit instance:

```text
p = 5,  q = 5^64,  H = the order-256 power-of-two subgroup of F_q^*,
|H| = N = 256 = 2^8,  rho = 1/16,  k = rho*N = 16,
t = 1  (residue-line datum: line f = x^{17}, g = x^{16}; a = n/N = 1),
delta = 1 - rho - 1/N = 1 - 1/16 - 1/256,
gap = t/|H| = 1/256.
```

Confidence ~0.8 that this meets the **literal** target (it is built from the published `lem:locator`/`lem:dsh` of `RS_disproof_v3.tex` plus one elementary linear‑independence count). Confidence ~0.9 that it is **not** a deployed‑prize counterpacket (extension field `F_{5^64}`, not a deployed prime/Goldilocks field), i.e. it is research/model‑grade unless the prize admits extension fields.

The mechanism Cycle90 missed: at the **small** rate `ρ=1/16` the corrected reserve `τ* = H₂(ρ)/log₂q` is small, so a fixed gap `1/N` lands **above** reserve; and the structured (monomial‑locator) bad‑slope count is bounded **below** unconditionally by a *power‑basis* count over the extension — no global cyclotomic‑norm injectivity, and no 52.7B‑record census.

## 2. The exact lemma

> **Lemma (Cycle91 above‑reserve power‑of‑two occupancy, extension‑field form).**
> Let `p` be an odd prime, `N = 2^s`, and `d = ord_N(p)` (multiplicative order of `p` mod `N`). Set `q = p^d`, so the order‑`N` subgroup `H = ⟨ω⟩ ≤ F_q^*` (where `ω` is a primitive `N`‑th root of unity) **generates** `F_q` as a field (`[F_p(ω):F_p] = d`). Fix a prize rate `ρ` with `k = ρN ∈ Z`, `ℓ = ρN + 1`, and the locator line `f = x^{k+1}, g = x^{k}` (`a = 1`, `t = 1`). Then for the radius `δ = 1 - ρ - 1/N`:
> ```
> Λ^{NC}_{1,δ}(H,k) = |ℓ^∧ H|  ≥  Σ_{w ≤ ℓ, w ≡ ℓ (2)}  C(d, w) 2^w  ≥  C(d, min(ℓ,d)) · 2^{min(ℓ,d)}.
> ```
> Consequently `ε_mca(RS[F_q, H, k], δ) ≥ (that bound)/q`.

**Instance check (`p=5, N=256, ρ=1/16, d=64, q=5^64`):**

```text
v2(5^64 - 1) = v2(4)+v2(6)+v2(64) - 1 = 2+1+6-1 = 8   => 256 | 5^64-1, 2-Sylow = 256.
ord_256(5) = 2^{8-2} = 64   (5 ≡ 5 mod 8 has maximal 2-adic order)  => H generates F_{5^64}.
log2 q = 64 log2 5 = 148.585        (<= 256, prize band OK)
floor(q/2^128) = floor(5^64/2^128) = 2^{148.585-128} ≈ 2^{20.6} ≈ 1.6e6
count >= C(64,17)*2^17 ≈ 2^{70.47} ≈ 1.6e21      (clears floor by ~50 bits)
eps_mca >= 2^{70.47}/2^{148.585} = 2^{-78.1}      (>> 2^-128)
gap = 1/256 = 0.003906 ;  tau* = H2(1/16)/log2 q = 0.33729/148.585 = 0.002270
gap/tau* = 1.72        (above reserve by 72%)
```

## 3. Proof / obstruction

**(i) Badness (this is published `lem:locator`).** With `a=1`, the locator `L_A(X) = Π_{b∈A}(X - b)` for `A ⊆ H`, `|A| = ℓ = k+1`, expands as `X^{k+1} + (−Σ_{b∈A} b)X^{k} + R_A`, `deg R_A < k`. So `u_z = f + zg = x^{k+1} + z x^{k}` is explained on `S_A = A` (size `k+1 > k`) by `−R_A ∈ RS[F_q,H,k]` whenever `z = −Σ_{b∈A} b`. Since `g = x^{k}` agrees with no degree‑`<k` polynomial on `k+1 > k` points, condition (ii) of `def:mca` holds (for `g` alone) for **every** such `z`. Hence every `z ∈ −ℓ^∧H` is bad and noncontained: `Λ^{NC} = |ℓ^∧H|`.

**(ii) The unconditional count (the new step).** Because `d = ord_N(p)`, the power basis `{1, ω, …, ω^{d−1}}` is `F_p`‑linearly independent, and `d = ord_N(p) ≤ N/4 < N/2`, so for `j ∈ {0,…,d−1}` the indices `j` and `j+N/2` are distinct elements of `{0,…,N−1}`, with `ω^{j+N/2} = −ω^j` (the unique order‑2 element of `H` is `−1 = ω^{N/2}`). For any sign‑digit vector `c ∈ {−1,0,1}^d` of Hamming weight `w ≤ ℓ`, `w ≡ ℓ (mod 2)`, realize
`Σ_{j<d} c_j ω^j` by the `ℓ`‑subset `A = {ω^j : c_j=1} ∪ {ω^{j+N/2} : c_j=−1} ∪ (b opposite pairs)`, `b = (ℓ−w)/2` (room: `b ≤ N/2 − w`). Distinct `c` give **distinct** field elements (linear independence over `F_p`), each a genuine `ℓ`‑subset sum. Therefore `|ℓ^∧H| ≥ Σ_{w≤ℓ, w≡ℓ(2)} C(d,w)