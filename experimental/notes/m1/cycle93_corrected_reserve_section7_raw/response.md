I'll start by reading the file index, then work through the source files systematically.The index is large. Let me read the key source files directly using the paths from the prompt, batching the reads. I'll start with the project state files and the two cycle notes.Let me read the core state files and locate the exact paths for the tex and experimental files.Let me find the exact paths for the tex and experimental files in the index.The index is huge. Let me directly read the key files using their likely paths under current_repo_snapshot. I'll batch the critical reads.Now let me read the cycle91 audit, the arithmetic script, and locate the tex files. Let me batch these reads.Now let me read the arithmetic script and find the tex files. Let me search for the tex paths in the index.bash_tool isn't available in this harness. Let me read the arithmetic script and locate the tex files by trying the standard repo path.Let me find the tex files. I'll try the standard repo path.The tex file exists. This is the core source. Let me read it to find Section 7, the corrected reserve definition, and the quotient profile. Let me read it in chunks to find the relevant sections.This is the core source paper. Let me continue reading to find Section 7 (extension-field examples) and the reserve/quotient-profile definitions.This is the core disproof paper. Section 7 is `\section{Extension-field towers and density variants}` (`sec:extension-towers`), with `lem:ext-coset-subgroup`, `lem:ext-tower-criterion`, `thm:ext-smooth-towers`, `prop:ext-density`, `cor:fermat-proth-towers`, `ex:goldilocks-density`. Now I need the corrected-reserve / quotient-profile definitions, which live in slackMCA_v3.tex. Let me read it.Let me read the table of contents and find the quotient-floor / corrected-reserve sections.This is the source of the corrected-reserve definitions. The key `def:taustar` is here. Now I need `prop:qfloor`, `thm:qnecessity`, `prop:prize`, the corrected-reserve two-scale floor, and the subfield-confinement theorem. Let me read the relevant Part II/III sections.Let me find the key MCA-side theorems. I'll search the later parts of the file. Let me read further in to find `prop:qfloor`, `thm:qnecessity`, `prop:prize`, and `thm:subfield`.The corrected reserve is now clear. I need the MCA-side quotient floor (`prop:qfloor`), quotient necessity (`thm:qnecessity`), prize cap (`prop:prize`), and the subfield-confinement theorem (`thm:subfield`). Let me locate them.This is essential. `thm:exactcount` gives the exact bad-slope count `A(N', ell')` which exactly matches the Cycle91/92 power-basis count. Note `N'=n/sigma`. Let me now find `prop:qfloor`, `thm:qnecessity`, and `prop:prize`.This is the heart of it. `prop:qfloor` is the prime-field quotient-exact floor. The threshold structure exactly matches the Cycle91 row. Now let me read `thm:qnecessity` and `prop:prize`, which come next.This is exactly the corrected-reserve / prize-cap machinery. Let me read the rest of `prop:prize` and then find the subfield-confinement theorem (`thm:subfield`) which governs extension fields.Now let me find the subfield-confinement theorem (`thm:subfield`, `cor:deflate`, `cor:decouple`) in Part III, which is the explicit extension-field MCA result and the key obstruction for splicing an extension-field row at corrected reserve.AUDIT / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL

I read the two source papers (`RS_disproof_v3.tex`, `slackMCA_v3.tex`), the Cycle91/92 audits, and the arithmetic checker. Here is the decision.

## 1. Executive verdict and confidence

The literal target — splice `L-CYCLE92-EXTENSION-FIELD-POWER-BASIS-COVERAGE` into the Section 7 ledger as an **above-corrected-reserve** companion — is **ROUTE_CUT**. A **repaired** companion (a finest-gap, cyclotomic-power-basis, generated-extension failure lemma) is **source-valid and bankable**. Confidence: high on the mathematics and on the reserve reading; moderate-high on the exact placement.

Three findings drive this:

- The row's mathematics is sound and is **not** deflated by subfield confinement (`thm:subfield`), because the order-256 subgroup *generates* `F_{5^64}` (`ord_256(5)=64 ⟹ F_5(ω)=F_{5^64}`). So `ε_mca ≥ 2^{-81.31}` is real.
- The row is **above the entropy reserve** `τ*(ρ,q_D)` but **below the quotient-profile scale** `Θ(1/\log n)` of the *full* corrected reserve. The "61.72-bit binomial reserve margin" Codex computed is the entropy/pigeonhole scale only; it is necessary, not sufficient, to call the row "above corrected reserve."
- The row is **not** a Section 7 scalar-coset instance. Section 7 (`thm:ext-smooth-towers`, `prop:ext-density`) needs `H≤F_p^×` in the base field with `ρm∈ℤ`; here `m=n/d=256/64=4` and `ρm=1/4∉ℤ`. The row uses a different mechanism (cyclotomic power basis, the `prop:qfloor`/`thm:exactcount` family of `slackMCA`), so it cannot be a corollary of Section 7's theorems — only a new sibling lemma.

## 2. Exact route cut and exact bankable companion

**Route cut (do not bank):** "The `F_{5^64}` order-256 row is above the corrected reserve and is a Section 7 (scalar-coset) corrected-reserve companion." Cut for two independent reasons: (i) mechanism mismatch (`ρm∉ℤ` kills the scalar-coset coverage of `thm:ext-smooth-towers`/`prop:ext-density`); (ii) the gap `1/N=1/256` clears only `τ*`, not the quotient-profile scale `Θ(1/\log n)`.

**Bankable companion (repaired), `L-CYCLE93-GENERATED-EXTENSION-CYCLOTOMIC-FLOOR`:**

> Let `p` be an odd prime, `N=2^s`, `d=ord_N(p)`, `q=p^d`, and let `H≤F_q^×` be the order-`N` subgroup generated by a primitive `N`-th root `ω`; then `F_p(ω)=F_q` and `1,ω,…,ω^{d-1}` is an `F_p`-basis (`lem:ext-coset-subgroup` converse). Fix `ρ` with `k=ρN∈ℤ`, `ℓ=k+1`, and the line `f=x^{k+1}, g=x^k` on `H`. Then every `z∈−ℓ^{∧}H` is support-wise MCA-bad at radius `1−ρ−1/N` (`lem:locator`, `a=1`, `D=H`), and the `F_p`-power-basis sign-digit slice gives the unconditional lower bound
> ```
> |ℓ^∧ H| ≥ Σ_{w ≤ min(ℓ,d), w ≡ ℓ (mod 2)} C(d,w) 2^w,
> ```
> hence `ε_mca(RS[F_q,H,k], 1−ρ−1/N) ≥ (that sum)/q`. Because `H` generates `F_q`, `thm:subfield` does **not** deflate this row (`q_gen=q_line=q_code=q_chal=q`). For `(p,N,d,ρ)=(5,256,64,1/16)`: `ℓ=17`, the bound is `Σ_{w∈{1,…,17}}C(64,w)2^w = 186{,}133{,}080{,}414{,}353{,}317{,}504 ≈ 2^{67.33}` (single-weight `C(64,17)2^{17}≈2^{67.29}`), so `ε_mca ≥ 2^{−81.31} > 2^{−128}`.

It is the **extension-field generalization of `prop:qfloor`/`thm:exactcount`**, with the prime-field antipodal count `A(N',ℓ')` using `C(N'/2,·)` replaced by the degree-`d`-truncated `C(d,·)` and the char-0 norm threshold replaced by direct `F_p`-linear independence. It must be banked there (and cross-listed as a Section 7 density variant), **not** as a scalar-coset corollary and **not** as a reserve breach.

## 3. Proof / obstruction

**Why the companion is correct (chain, all steps solid):**
1. `ord_256(5)=64 ⟹ deg_{F_5}(ω)=64 ⟹ F_5(ω)=F_{5^64}`; `1,ω,…,ω^{63}` `F_5`-independent.
2. `ω^{128}=−1` (unique order-2 element), so `ω^{j+128}=−ω^j`: antipodal pairing intact.
3. Sign-digit vectors `c∈{−1,0,1}^{64}` supported in `{0,…,63}` (genuine basis positions), `|supp|=w≡17 (2)`, `w≤17`, padded by `(17−w)/2` opposite pairs `{ω^j,ω^{j+128}}`, `j∈{64,…,127}`, give genuine 17-subsets of `H` with sum `Σ_{j<64}c_jω^j`.
4. Distinctness: `Σ(c_j−c'_j)ω^j=0` with `c_j−c'_j∈{−2,…,2}` (nonzero mod 5 unless equal) forces `c=c'` by `F_5`-independence. So the `Σ C(64,w)2^w` values are distinct in `F_{5^64}`.
5. `lem:locator` makes each `−Σ` MCA-bad at `1−1/16−1/256`; noncontainment holds since `g=x^{16}` has no degree-`<16` explanation on the 17-point set.
6. `ε_mca ≥ 2^{67.29}/5^{64} = 2^{−81.31}`.

**Why the splice as "above corrected reserve" is obstructed:** The corrected reserve is two-scale (`rem:corrected-reserve`, `conj:listprofile`, `conj:B`): `η ≳ max{τ*(ρ,q_D), Θ(1/\log n)}`, with `τ*` at the **generated** field.
- Entropy scale: `τ*(1/16, 5^64)≈0.002331` (leading `H_2(1/16)/\log_2 q=0.0022697`); gap `1/256=0.003906 > τ*`, margin ≈1.68×. **Cleared.**
- Quotient scale: `1/\log_2 n = 1/8 = 0.125`; gap `1/256` is `1/32` of it. The quotient profile is active: `Q_H(1/256)=\log_2 C(127,8)≈40.3` bits (at `M=2`), and the row *is itself* a quotient-floor failure (`prop:qfloor`/`thm:qnecessity` with `N'=n=256, σ=1`). **Not cleared.**

So the row lives in the band `τ* < η ≪ Θ(1/\log n)`, exactly where the corrected conjecture already concedes failure. It **corroborates** the corrected reserve; it does not breach it. This is the precise content of Cycle92's warning that the "simple finite binomial reserve" (entropy only) is not the full convention.

## 4. Verification requirements

- Recompute `Σ_{w≤17}C(64,w)2^w`, `C(64,17)2^{17}`, `\log_2 q`, and `\log_2 C(256,17)` — already in `cycle91_extension_power_two_arithmetic.py` (extend it to print the **proven** MCA margin `\log_2 q − 67.29 = 81.31` bits, distinct from the 61.72-bit pigeonhole margin).
- Confirm `H⊄B` for every proper subfield `B⊂F_{5^64}` (immediate from `deg ω=64`), so `thm:subfield` non-applicability is recorded explicitly.
- Confirm the `a=1`, `D=H`, `N=n` instantiation of `lem:locator` (the row is `σ=1`, finest gap), and that the padding indices `{64,…,127}` are disjoint from support indices.
- Record `q_gen=q_line=q_code=q_chal=5^64` (no ledger merge: they coincide because `H` generates `F`).

## 5. Next exact lemma or construction

The exact wall after banking: **the restricted-sum/cyclotomic mechanism is structurally capped at the entropy scale.** At quotient order `N'=n/σ`, the achievable count is `≈2^{β(ρ)·d_{N'}}` with `d_{N'}=ord_{N'}(p) ≤ N'/4`; reaching gap `η=σ/n ≳ 1/\log n` forces `N'≲\log n`, hence `d_{N'}=O(1)`, hence count `≪2^{−128}q`. This is the `sec:scope` floor `η ≳ H_2(ρ)/\log_2(ηq)=τ*`-scale, restated for extensions. So the next lemma is **not** another restricted-sum row.

Exact next target: `W-CYCLE94-EXTENSION-QUOTIENT-RESERVE-BREACH` — produce, at a generated extension `F_{p^d}`, a bad-slope family of size `≥ 2^{(H_2(ρ)−β(ρ))N'(1−o(1))}` *outside* the characteristic-zero quotient image (collision-borne or non-quotient slopes, `prob:perfiber` / `rem:margin`), which is the only way to exceed the quotient-profile reserve. Absent that, the lower/failure branch is entropy-scale-saturated and should stop absorbing cycles; the live frontier remains the positive/upper wall `W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD`.

## Self-audit (explicit answers)

**1. What I proved / did not prove.** Proved: over `F_{5^64}` with the generating order-256 subgroup, line `x^17+zx^16`, the noncontained MCA-bad set has size `≥2^{67.29}`, so `ε_mca(·,1−1/16−1/256)≥2^{−81.31}>2^{−128}`, and this is undeflated by `thm:subfield`. Did **not** prove: that the row is above the *full* (two-scale) corrected reserve; that it is a scalar-coset Section 7 instance; that it is an official prize counterpacket; any upper/positive bound.

**2. Prize-relevant or research certificate?** Research/model certificate only. `F_{5^64}` is not a deployed/prize prime field; `conj:capacity`'s `2^{−128}` is "for the prize fields." Promotion stays cut (Cycle92). The `2^{−128}` comparison is mechanism-validation, not prize-relevant.

**3. First line where the theorem could fail.** Not in the MCA chain (steps 1–6 are solid). It fails at the **classification** lines: "above corrected reserve" fails at the quotient-profile comparison (`gap 1/256 ≪ Θ(1/\log n)`); "Section 7 scalar-coset companion" fails at `ρm=1/4∉ℤ` (`lem:ext-coset-subgroup` coverage hypothesis); "official prize" fails at extension-field admissibility / `def:mca` (Definition-4.3) alignment.

**4. q_gen, q_line, q_code, q_chal, 2^−128.** Used correctly and not merged: all four equal `5^64` here precisely because `H` generates `F` and line/code/challenge are all over `F_{5^64}`. `τ*` is correctly taken at `q_D=q_gen=5^64`. The `2^{−128}` target is applied as the negligibility threshold (cleared by 46.7 bits), with the explicit caveat that the target is officially defined for prime prize fields, so this is a model clearance.

**5. Could a reduction shrink the numerator?** Checked all four: (a) same-slope collisions — none within the family (distinctness via `F_5`-independence); (b) quotient/periodic collisions — cannot shrink *this* bound, since it uses only the provably independent `1,…,ω^{63}` (this is why the count is `C(d=64,·)` not `C(N'/2=128,·)`; the sub-threshold deficits of `rem:thresholdneeded` are already paid for); (c) contained incidences — noncontainment is robust (`g=x^{16}`, 17>16 points); (d) affine-color/projectivization — `def:mca` counts raw density over `z∈F`, no normalization. Numerator `2^{67.29}` stands.

**6. PLAN → PROOF converter.** The repaired companion is bankable now, not a plan. To formalize into source: add the lemma statement+proof (sign-digit `F_p`-independence) adjacent to `prop:qfloor`/`thm:exactcount`, cross-listed as a Section 7 density variant; include the explicit `thm:subfield` non-applicability line; and extend the checker to emit the proven `81.31`-bit MCA margin alongside the `61.72`-bit pigeonhole margin so the two reserve scales are never conflated again.