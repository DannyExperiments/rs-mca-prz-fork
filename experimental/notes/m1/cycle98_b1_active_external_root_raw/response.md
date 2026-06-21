I'll start by reading the file index, then the required project files.I'll read the key project files. Let me start with the orientation files and the Cycle97-specific sources in parallel.This is a substantial research project. Let me read the Cycle97-specific files and the route board in parallel.Let me find the Cycle97 source files and the key reference files. Let me search the index for the exact paths.The bash tool isn't available in this harness; only Read works. Let me locate the Cycle97/98 files by reading sections of the index.Now let me read the core Cycle97/98 files: the audit correction, the raw response, the Cycle98 prompt, and the decomposition check script.Now the critical Cycle97 audit correction and raw response.Now the raw Cycle97 response and the decomposition check script.This is the key prior work. Now let me read the decomposition check script and look at the slackMCA tex source for the core definitions (prefix fiber, no-collision theorem, per-fiber problem).Right, no bash. Let me read the decomposition check script via the index path.Now I have the core machinery. Let me read the banked lemmas, active walls, and the key tex definitions to anchor my analysis to the source conventions.This is stale (Cycle 83-era). The live machinery is in the banked lemmas and the tex. Let me read the banked lemmas and locate the tex source.I need the tex source. Let me find its exact path in the index.Let me find the tex source path in the index.I have the core Cycle97 machinery. Now let me read the readme for prize context and the key tex sections (per-fiber problem, two-moment, aperiodicity, reserve).I have the essential Cycle97 machinery. Now I need the exact `b=0` collision-sieve mechanism and the two-moment/aperiodicity definitions from the source paper to determine whether the external point breaks the proof. Let me read the relevant sections of the tex.Let me search for the key theorems referenced (thm:no-collision, thm:upstairs, prob:perfiber, thm:twomoment, rem:aper) by grepping the tex. Since I can't grep, let me look at the structure. Let me search for the per-fiber and two-moment sections, which are the heart of the b=0 mechanism.Let me read the characteristic-zero rigidity and the Galois sieve sections, which are the b=0 mechanism that I need to test against the external root.Now let me read the characteristic-zero rigidity (thm:upstairs) and the Galois sieve (thm:no-collision), which are the central b=0 mechanism. Let me find them.Now let me finish the no-collision proof and find the per-fiber problem, aperiodicity remark, and conjecture B.Let me read the conjecture B / per-fiber / aperiodicity remark sections, which the prompt names as the bridge. Let me look further in the conjectures and the frontier.This is exactly the machinery I need. The key technical fact is Theorem `thm:upstairs` (char-0 inverse quotient) and `thm:no-collision` (Galois sieve). Now I understand the b=0 mechanism precisely. 

Let me now read the per-fiber problem and aperiodicity definitions, which the Cycle97 response references. Let me look at the boundary section and conj:B.Let me read the boundary section with the residue-line normal form, per-fiber problem, and aperiodicity remark (the bridge the Cycle97 response cited).Let me find the boundary/normalform/per-fiber section. Let me search the latter part of the tex for "prob:perfiber" and "rem:aper".Now I have a thorough understanding of conj:B and aperiodicity. Let me read the residue-line normal form (thm:normalform), prop:noanchor, and prob:perfiber, which describe the MCA→prefix-fiber bridge and the per-fiber problem the wall reduces to.EXACT_NEW_WALL  /  BANKABLE_LEMMA (reduction + non-reducibility)  /  ROUTE

I read the corrected Cycle97 audit (`m1_cycle97_fixed_prime_two_support_audit.md`), the raw response, the decomposition checker, and the source machinery in `slackMCA_v3.tex` (`thm:upstairs`, `thm:no-collision`, `cor:quasipoly-upper`, `thm:stable`/`thm:exactcount`, `thm:twomoment`, `thm:normalform`, `prob:perfiber`, `rem:aper`, `conj:prefix-local`, `conj:B`). What follows uses the corrected decomposition, not the raw external‑only branch.

---

## 1. Executive verdict and confidence

I did **not** prove the polynomial active‑external‑root bound and I did **not** produce a counterpacket. What I can establish rigorously is a sharp structural reduction plus a non‑reducibility theorem:

- **(Bankable, proven.)** In power‑sum coordinates the active‑external‑root set is *exactly* the intersection of the subgroup power‑sum image with a translate of the moment (rational‑normal) curve. This is the smallest exact form of the wall.
- **(Bankable, proven.)** This wall is **not** implied by the bandwidth‑0 prefix local limit (`conj:prefix-local`), and — sharper than Cycle97 claimed — it is **not even covered by the stable large‑prime range** `thm:stable`/`cor:quasipoly-upper` that proves the b=0 bound. The external point has no bounded‑height cyclotomic lift, so the Galois/norm sieve (`lem:galois-amp`) is structurally inapplicable. **b=1 is strictly harder than b=0.**
- **(Verdict.)** The polynomial bound is a genuine new fixed‑prime curve‑incidence wall, in the same difficulty class as `prob:perfiber` but logically independent of it.

Confidence: **high** on the moment‑curve reduction and on non‑reducibility/strict‑hardness (these are elementary identities + a clean obstruction, finitely checkable). **Moderate‑leaning‑true** that the bound itself holds (two‑moment equidistribution + removal of the only known clustering mechanism point that way), but **unprovable with current technology**, exactly like the per‑fiber problem.

---

## 2. Exact objects, the reduction, and the smallest statement

**Convention.** `H=⟨ω⟩≅μ_n`, `n=2^m`, `p≡1 (mod n)`, `q_gen=q_line=q_code=q_chal=p` (prime ⇒ no proper subfield ⇒ `H` generated), `k=ρn`, `s=k+σ`, `σ≥Cn/log n`, `U` monic of degree `s+1` with prefix `c=(c_1,…,c_{σ+1})`, `c_0=1`. Since `p>σ+1`, Newton converts `c` to power sums `P_1,…,P_{σ+1}` (the power sums of the top part of `U`).

**Corrected split (respecting the audit; `θ∈H` is charged, not ignored).** A degree‑`<k` codeword `P` agreeing with `U` on `≥s` points ↔ `V=U−P` monic of degree `s+1`, prefix `c`, `≥s` roots in `H`:

```
θ∈H  branch :  V=L_R (R⊆H, |R|=s+1, Type A)  OR  V=(X−θ)L_S with θ∈S (repeated root in H).
               Exactly the n values θ∈H; each is one bandwidth-0 fiber slice; the
               repeated-root case is the branch the raw answer omitted (Codex F_17 toy).
               These, together with all μ_M-periodic fibers, are charged to the
               quotient-profile term 2^{(β/H₂)Q_H} of rem:aper / conj:B.
θ∉H  branch :  V=(X−θ)L_S, S⊆H, |S|=s, θ∈F_p∖H  — the active external-root wall.
```

**Power‑sum normal form (the clean object).** For `θ∉H`, write `v(θ)=(θ,θ²,…,θ^{σ+1})` (the **moment curve**) and
```
        M_s := { (p_1(S),…,p_{σ+1}(S)) : S∈C(H,s) }  ⊂ F_p^{σ+1}
```
the subgroup power‑sum image at level `σ+1` on `s`‑subsets. Because `V=(X−θ)L_S` ⇒ `p_j(S)+θ^j=P_j`,
```
        θ active  ⇐⇒  P − v(θ) ∈ M_s  ⇐⇒  v(θ) ∈ P − M_s ,
        θ = c_1 − e_1(S)  (the j=1 row fixes θ from S).
```

> **BANKABLE LEMMA (L‑CYCLE98‑MOMENT‑CURVE‑INCIDENCE).**
> `|Θ_U| = | v(F_p∖H) ∩ (P − M_s) |`, the number of `F_p`‑points where the moment curve meets the reflected subgroup power‑sum image; and `|Θ_U^{aper}|` is the same count after deleting `θ` whose fiber `Φ_{σ+1}^{-1}(c(θ))` is a `μ_M`‑coset union (`M>σ`).
> The target wall is `|Θ_U^{aper}| ≤ n^{O(1)}`.

This is the smallest exact statement (Task 3). It exposes the precise relationship to b=0 on the **same set** `M_s`:

```
b=0 (conj:prefix-local)  =  "vertical fibers of M_s are small"      (fiber sizes).
b=1 (this wall)          =  "M_s meets a moment curve in few points" (transverse incidence).
```

Neither implies the other. The moment curve is the maximally non‑degenerate curve (any `σ+1` of its points are affinely independent), so the only way it can meet a sparse set superpolynomially is if that set *clusters* — and the only known clustering of `M_s` is quotient‑periodicity, which `rem:aper` removes.

**Character‑sum form (for Task 3 / the checker).** With `Λ_λ(x)=Σ_{j=1}^{σ+1}λ_j x^j` and `Ξ(λ)=e_s({e_p(Λ_λ(x))}_{x∈H})` (the `s`‑th elementary symmetric of the `n` phases),
```
   N(θ)=p^{-(σ+1)} Σ_{λ∈F_p^{σ+1}} \overline{Ξ(λ)} · e_p(Σ_j λ_j(P_j−θ^j)),   θ active ⇔ N(θ)>0,
```
and the wall is `#{θ∉H : N^{aper}(θ)>0} ≤ n^{O(1)}` — a moment‑curve‑vs‑subgroup‑power‑sum‑image incidence governed by the same `Ξ(λ)` subgroup exponential sums as `prob:perfiber`.

---

## 3. Proof of the structural lemma, and the exact obstruction

**Proof of the normal form.** `V=(X−θ)L_S` has root multiset `S∪{θ}`, so its first `σ+1` power sums are `p_j(S)+θ^j`; matching `V`'s prefix to `c` means these equal `P_j` for `j≤σ+1` (Newton, `p>σ+1`). Hence `p_j(S)=P_j−θ^j`, i.e. `P−v(θ)∈M_s`. The `j=1` row gives `θ=P_1−p_1(S)=c_1−e_1(S)`, the forced external root. `V↦(S,θ)` is injective (roots determine `S,θ`), so distinct active `θ` give distinct `V`; thus `|Θ_U|≤|V_B|=Σ_θ N(θ)`, and `|Θ_U|` equals the number of nonempty fibers. ∎

**Why it is genuinely new (defeats the Galois sieve).** Take two active externals `θ≠θ′` with witnesses `S,S′`. Subtracting the power‑sum rows,
```
   p_j(S)−p_j(S′) = θ′^j − θ^j     (1 ≤ j ≤ σ+1),
```
equivalently `(S∖S′)∪{θ}` and `(S′∖S)∪{θ′}` have **equal power sums to order `σ+1`** — a *balanced prefix collision with exactly one external point on each side*, each side of size `|S△S′|/2+1 ≥ σ+2` (by `lem:pairwise`, `|S∩S′|≤k−1`). The b=0 engine (`thm:upstairs`, `thm:no-collision`) lifts subgroup configurations to `Z[ζ]` and bounds `|Norm(F(ζ))|`; here each side carries one coordinate `θ∈F_p∖H` with **no cyclotomic lift** (`L-CYCLE96` height floor governs only the subgroup part; the external coordinate is height `≈p`). So `lem:galois-amp` cannot certify the collision as characteristic‑zero. 

**Sharper than Cycle97: not even the stable range helps.** In the stable range `p>(2s)^{n/2}`, `thm:stable` proves the b=0 bound because every subgroup prefix collision is forced char‑0 by a norm bound `≤(2s)^{n/2}<p`. For b=1 the integer rep `[θ]∈[0,p)` makes the relevant quantity `[θ_1]^j−[θ_i]^j (mod p)` neither zero nor a bounded‑height cyclotomic integer, so **no `p`, however large, lets the norm argument bound `|Θ_U|`.** Hence b=1 is strictly harder than b=0: it is open even where b=0 is fully proved. (This corrects the implicit Cycle97 reading that b=1 fails “at the same `p`‑range”; it actually fails at *all* ranges.)

**Why no averaging trick closes it.** Let `T=|Θ_U|`, `R=Σ_θ N(θ)`, `E=Σ_θ N(θ)²`. Cauchy–Schwarz gives `T≥R²/E` and `conj:prefix-local` gives `N(θ)≤n^B ⇒ T≥R/n^B`: both are *lower* bounds on `T`. Upper‑bounding `T` is exactly the curve‑incidence content and is not produced by any moment/energy identity — it needs genuine fixed‑prime input, terminating at the same subgroup‑exponential‑sum barrier as `prob:perfiber` (in the polynomial range `n=p^{1/c_0}<p^{3/7}` the known ranges do not apply).

---

## 4. Self‑audit (the six required questions)

1. **Proved / not proved.** Proved: the moment‑curve normal form `|Θ_U|=|v(F_p∖H)∩(P−M_s)|`; the corrected `θ∈H`/`θ∉H` split with the repeated‑root branch charged; non‑reducibility to b=0 and strict hardness over b=0 (stable range included). Not proved: `|Θ_U^{aper}|≤n^{O(1)}` itself, hence not the b=1 collision bound; no counterpacket.
2. **Prize relevance.** Upper side, direction of `ε_mca` over `thm:normalform`, `q_chal=q_line=p`, target `|List|≤2^{-128}p`. It is a route‑structuring lemma + sharpened wall, **not** a finite prize certificate and **not** a counterpacket.
3. **First line that could fail.** The reduction (Theorem B1, normal form) is unconditional and finitely checked. The first failure point is the new incidence bound `|v(F_p∖H)∩(P−M_s)^{aper}|≤n^{O(1)}`; upstream of it, the b=0 prefix local limit at the polynomial reserve (`conj:prefix-local`, proved only for `p>exp(O((log n)²))`) is also still open.
4. **Field / `2^{-128}` usage.** Correct and unmerged. `θ`, `v(θ)`, `M_s`, `P` all live in `q_gen=q_D=p`; list normalized by `q_chal=q_line=p`; reserve is the corrected two‑scale `σ≥Cn/log n`; `2^{-128}` enters as `|List|≤2^{-128}p`, which B1 reduces to (b=0 fibers) + `|Θ_U^{aper}|`. Both targeted as `n^{O(1)}`, fine in the deployed window `k≤2^{40}, |F|<2^{256}` provided `p≥2^{128}n^{O(1)}`.
5. **Could quotient/periodic, contained, same‑slope, or affine‑color reduce the numerator?** (i) *Quotient/periodic:* `θ∈H` (n slices) and all `μ_M`‑coset‑union fibers are charged to `2^{(β/H₂)Q_H}` via `rem:aper`; `Θ_U^{aper}` is precisely what remains, and **external `θ` are not chargeable to quotient cores** (an external point lies in no `μ_M`‑coset), so they cannot be absorbed. (ii) *Contained:* noncontainment automatic (`deg U=s+1>k`; Cycle95). (iii) *Same‑slope `P(α)=P′(α)`:* only shrinks the eval image below the list, can only help the upper bound. (iv) *Affine color:* scaling by `λ∈H` sends `θ↦λθ` bijectively (count‑invariant); additive shift does not preserve the subgroup `H`, so is unavailable. None reduces the count.
6. **PLAN→PROOF / COUNTERPACKET.** See §5.

---

## 5. Next exact lemma / construction, and verification

**Route to a full solve** = (a) b=0 prefix local limit (existing open input); (b) for each `b`, the active external‑configuration incidence; (c) induct on `b` to `b=m−1`. The b=1 instance is:

> **Lemma S1‑B1 (to prove or kill).** There is `B=B(ρ)` such that for `σ≥Cn/log n`, all `p≡1 (mod n)` with `n^{c_0}≤p≤2^{o(n)}`, and every monic `U` of degree `s+1`,
> `| v(F_p∖H) ∩ (P−M_s) |_{aper} ≤ n^B`,
> i.e. the moment curve meets the aperiodic part of the subgroup power‑sum image in polynomially many points.

**Exact analytic input that converts it to PROOF.** A transversality/incidence bound for the moment curve against `M_s`, equivalently a subgroup even‑moment bound on `Ξ(λ)` along the `1`‑parameter pencil `λ↦` (dual of `v`), in the polynomial‑field range. Cleanest sufficient form: extend `conj:prefix-local` to “≤ 1 external point” configurations and show the **count of nonempty fibers along `v`** (not their sizes) is polynomial. By the two‑moment fullness theorem `thm:twomoment` (under its square‑root hypothesis, satisfied here since `p≈\binom ns^{1/σ}≪\sqrt{\binom ns}`), the `j≤2` layer imposes **no** restriction on `θ` — every `θ` clears the parabola `e_2(S)=u²−P_1u−(P_2−P_1²)/2`, `u=e_1(S)` — so the entire restriction lives in `j=3,…,σ+1`; the operative lemma is genuinely about the higher moment curve, not the parabola.

**Exact counterpacket target (to kill it).** A monic `U` of degree `s+1` over a generated prime field at corrected reserve with `≥n^{ω(1)}` aperiodic active externals — i.e. a translated moment curve `P−v(·)` that aligns with `M_s` along a **non‑quotient** family. The only known clustering of `M_s` is `μ_M`‑periodicity (charged away), and two‑moment equidistribution forbids `(e_1,e_2)`‑clustering; so the natural quotient‑core source (`thm:qcore`, which produces *all‑in‑`H`*, periodic configurations) **cannot** supply an external point. I therefore expect no counterpacket; the decisive test is the §‑verification sweep.

**Verification requirements (finite, deterministic; extend `cycle97_bandwidth1_decomposition_check.py` and `cycle96_word_height_floor_toy.py`).**
1. *Normal‑form checker.* For small `p≡1 (mod n)`, `n∈{8,16,32}`, random `U` of degree `s+1`: confirm `Θ_U = {θ∉H : P−v(θ)∈M_s}` and `θ=c_1−e_1(S)` for every Type‑B solution. (Already partially done: Cycle97 reports 40/40 PASS, `external_theta=7`.)
2. *Reserve‑regime growth.* Sweep `(n,k,σ)` along `σ≈Cn/log n` with increasing `p` (incl. `θ∈H`/periodic removed via `μ_M`‑coset detection); log `|Θ_U|`, `|Θ_U^{aper}|`. Polynomial ⇒ evidence for PROOF; superpolynomial ⇒ COUNTERPACKET.
3. *Moment‑curve incidence.* Directly compute `|v(F_p∖H)∩(P−M_s)|` and compare to the random prediction `≈ p·|M_s|/p^{σ+1}` to detect structured `U` that inflate the incidence on a non‑periodic family (the would‑be counterpacket signature).
4. *Stable‑range probe.* Confirm experimentally that increasing `p` past `(2s)^{n/2}` does **not** drive `|Θ_U^{aper}|` to its char‑0 value (corroborating §3’s strict‑hardness claim), in contrast to the b=0 count which does collapse there.

**One‑line route map.** `Θ_U^{aper}` = (moment curve) ∩ (aperiodic subgroup power‑sum image). b=0 controls fiber *sizes* of that image; b=1 needs its *transverse incidence* with the rational‑normal curve — a strictly new, strictly harder fixed‑prime input that the norm/Galois sieve cannot reach at any `p`.