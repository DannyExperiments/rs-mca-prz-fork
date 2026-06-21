I'll start by reading the file index and key project files to understand the current state.Let me read the key project state files in parallel.Now let me read the Cycle 96 brief and the key technical files for this cycle.Let me find the key technical files referenced. Let me search the file index.Let me read the key technical files for this cycle. I'll search the index for the exact paths first.Let me locate the specific Cycle 96 and Cycle 97 files referenced in the prompt.Let me directly read the key Cycle 96/97 technical files referenced in the prompt.Now let me read the Cycle97 prompt and the Cycle96 raw response in parallel, plus locate the slackMCA tex.Now let me read the Cycle97 prompt and the toy script, plus locate the slackMCA tex.Now let me find the Cycle97 prompt and the slackMCA tex path. Let me search the index.Let me find the Cycle97 prompt and slackMCA tex paths using grep.Let me locate the Cycle97 prompt and the slackMCA tex file directly.Found the Cycle97 prompt. Let me read it and the key L1 aperiodic prefix collision note, which is directly relevant.Now let me read the crucial L1 aperiodic prefix collision note and the slackMCA tex source. These contain the core machinery I need.I have the core machinery from the L1 note (b=0 layer) and Cycle96 response. Now I need the tex source for the exact fiber definitions, reserve, and q-ledger. Let me locate it.Let me find the slackMCA tex source path directly.Found the tex source at `current_repo_snapshot/tex/slackMCA_v3.tex`. Let me read the key sections. I'll grep for the relevant labels first by reading targeted portions. Let me read the list-side machinery: locator fibers, the per-fiber problem, conjectures.Let me read the Part I list-side machinery — locator fibers and the collision sieve. Let me find the right section.This is the core machinery. Now let me read the crucial sections: characteristic-zero rigidity (thm:upstairs), the Galois sieve (thm:no-collision), and the per-fiber problem and conjectures. Let me find those sections.This is the core. Now let me read the Galois sieve (thm:no-collision) which is the b=0 proof, and then the per-fiber problem and conjectures (Part IV frontier).This is the heart of the matter. Now let me read the per-fiber problem (prob:perfiber), prop:noanchor, and the frontier conjectures (conj:B, conj:final-locator), which are referenced as the wall.Now let me find the per-fiber problem (prob:perfiber), prop:noanchor, conj:B, and conj:final-locator referenced in Cycle96. Let me search the latter part of the tex.Now let me read the residue-line normal form, prop:noanchor, and prob:perfiber sections, which are the MCA-side per-fiber wall.Now let me read the residue-line normal form (thm:normalform), prop:noanchor, and prob:perfiber. Let me search for these in the tex.Now let me find the residue-line normal form (thm:normalform), prop:noanchor, prob:perfiber, and rem:aper. These are referenced as the bridge between the MCA side and the per-fiber wall.PROOF (of the bandwidth‑1 reduction) + EXACT_NEW_WALL (the residual object below b=1). I did not produce a full b=1 collision bound and I did not produce a counterpacket.

---

## 1. Executive verdict and confidence

I can prove, rigorously and unconditionally, that the `b=1` two‑support problem **decomposes exactly** into (i) two bandwidth‑0 prefix‑fiber problems and (ii) one genuinely new scalar object: the **active‑external‑root count**. This both isolates the smallest algebraic object below `b=1` and shows that `b=1` is *not* equivalent to the full arbitrary‑word local limit, so the "ROUTE_CUT: b=1 ⟺ full" option is **false**. The clean conceptual statement is:

> **Bandwidth = number of root‑configuration points allowed off the subgroup `H`.**
> `Fib_U(s)` for `deg U = s+b` is governed by configurations `W` of `s+b` points with `|W ∩ H| ≥ s` and prescribed prefix `Φ_{σ+b}(W)=c`; `b` is the number of points of `W` outside `H`. `b=0` is the pure prefix fiber (all in `H`); `b=1` allows exactly one external point `θ∈F_p∖H`.

Confidence: **high** on the decomposition theorem (it is elementary polynomial algebra over `F_p`, verifiable by a finite checker). **High** that the residual wall is the active‑external‑root count and that it is fixed‑prime (the norm sieve dies at `b=1` at the *same* `p`-range as `b=0`, so Cycle96 transfers verbatim). **Moderate** that the wall is closable without new equidistribution; I give the exact character sum but do not close it.

---

## 2. Exact statement

**Convention.** `H=⟨ω⟩≅μ_n`, `n=2^m`, `p≡1 (mod n)`, `k=ρn`, `s=k+σ`, `σ≥Cn/log n`, `q_gen=q_line=q_code=q_chal=p` (prime, generated). Residue convention `deg(U mod L_S)<k` (dimension‑`k` code; the prompt's `≤k` is the dimension‑`(k+1)` relabeling `σ↦σ−1`, immaterial). WLOG `U` monic of degree `s+1`; let `c=(c_1,…,c_{σ+1})` be its top `σ+1` subleading coefficients read as elementary symmetric data (`[X^{s+1−j}]U=(−1)^j c_j`, `c_0=1`).

**Theorem B1 (bandwidth‑1 decomposition).**
The list `List(U,1−s/n)` of degree‑`<k` codewords `P` agreeing with `U` on `≥s` points is in bijection (`P↦V:=U−P`) with
```
V = { V monic, deg V = s+1, top σ+1 coeffs = those of U, #(roots of V in H) ≥ s }.
```
Every `V∈V` has exactly `s` or `s+1` roots in `H`, giving a disjoint split `V = V_A ⊔ V_B`:

- **`V_A`** (all `s+1` roots in `H`): `V=L_R`, `R∈C(H,s+1)`, `Φ_{σ+1}(R)=c`. This is a **bandwidth‑0 prefix fiber** at `(k,σ+1)` on `(s+1)`-subsets.
- **`V_B`** (exactly `s` roots `S⊆H`, one external root `θ∈F_p∖H`): `V=(X−θ)L_S`. The external root is *forced* by the leading subleading coefficient,
```
            θ = c_1 − e_1(S),
```
and for each fixed `θ` the slice `{S}` is the **bandwidth‑0 prefix fiber** `Φ_{σ+1}^{-1}(c(θ))` on `C(H,s)` at `(k−1,σ+1)`, where
```
            c(θ)_j = Σ_{i=0}^{j} (−θ)^{j−i} c_i      (j=1,…,σ+1),     deg_θ c(θ)_j = j.
```

Consequently, with `Θ_U := { θ∈F_p∖H : Φ_{σ+1}^{-1}(c(θ)) ≠ ∅ }` the **active‑external‑root set**, and writing `Γ(θ)=(c(θ)_1,…,c(θ)_{σ+1})` for the explicit **degree‑`(σ+1)` external‑root curve** in `F_p^{σ+1}`,
```
   |List(U,1−s/n)|  ≤  |Φ_{σ+1}^{-1}(c)|_{(k,σ+1)}            (Type A, b=0)
                    +  Σ_{θ∈Θ_U} |Φ_{σ+1}^{-1}(c(θ))|_{(k−1,σ+1)}   (Type B, each b=0)
```
and `|Fib_U(s)| ≤ (s+1)·|List(U,1−s/n)|`, `#{S' : S△S' aperiodic} ≤ (s+1)·|List^{aper}(U)|`.

**Corollary (the wall is one scalar).** Granting the bandwidth‑0 prefix local limit (every aperiodic prefix fiber `≤ n^{B_0}` after charging quotient cores — this is `conj:prefix-local`/`thm:upstairs`, proven for `p>exp(O((log n)^2))` by `thm:no-collision`), then
```
   |List^{aper}(U)|  ≤  n^{B_0} · ( 1 + |Θ_U^{aper}| ).
```
Therefore **S1 for `b=1` ⟺ ( bandwidth‑0 prefix local limit ) ∧ ( |Θ_U^{aper}| ≤ n^{O(1)} )**. The first conjunct is the existing `b=0` wall; the second is the new object.

**`EXACT_NEW_WALL` (S1‑B1‑WALL).** For `deg U=s+1`, after charging quotient‑periodic fibers,
```
   |Θ_U^{aper}|  =  | Γ ∩ Φ_{σ+1}(C(H,s)) |   ≤   n^{O(1)},
```
i.e. the explicit degree‑`(σ+1)` curve `Γ⊂F_p^{σ+1}` meets the prefix image of `s`-subsets of `H` in polynomially many points. Equivalently (power sums, `p>σ+1`): writing `u=p_1(S)` free, `S` must satisfy the `σ` constraints `p_j(S)=P_j−(P_1−u)^j` for `2≤j≤σ+1` — a prefix target sliding along a **degree‑`(σ+1)` algebraic curve** parametrized by the single freedom `u`.

---

## 3. Proof of Theorem B1, and the obstruction at the wall

**Proof of B1.** `P↦V=U−P` is an affine bijection from `{deg P<k}` onto `{monic deg s+1 with top σ+1 coeffs = U's}`, because `deg U=s+1>k>deg P` forces `deg V=s+1` and matching of all coefficients in degrees `k,…,s+1` (that is `σ+1` of them, namely `e_1,…,e_{σ+1}`). Agreement of `P` with `U` on `S` ⟺ `V` vanishes on `S` ⟺ `S⊆` roots of `V`. Since `deg V=s+1`, `V` has `≤s+1` roots, so a listed `V` has `s` or `s+1` roots in `H`; the agreement set has size `≤ s+1`, giving `binom(|Agr|,s)≤s+1` subsets per codeword, hence `|Fib_U(s)|≤(s+1)|List|`.

*Type A.* `s+1` roots in `H` ⟹ `V=L_R`, `R∈C(H,s+1)`; the prescribed `e_1,…,e_{σ+1}` of `V` are `Φ_{σ+1}(R)=c`. Pure `b=0`.

*Type B.* `V=(X−θ)L_S`, `S⊆H`, `θ∉H`. Then `e_j(V)=e_j(S∪{θ})=e_j(S)+θe_{j−1}(S)`. The constraint `e_1(V)=c_1` gives `θ=c_1−e_1(S)`; recursively `e_j(S)=c_j−θe_{j−1}(S)`, so fixing `θ` prescribes the entire prefix `(e_1(S),…,e_{σ+1}(S))=c(θ)`, a `b=0` fiber on `C(H,s)`. Solving the recursion gives the closed form `c(θ)_j=Σ_{i=0}^j(−θ)^{j−i}c_i`. ∎

**Why the wall is genuinely new (not reducible to `b=0`).** The fixed‑`θ` slices are each `b=0`, but `θ` ranges over the **size‑`p` continuum** `F_p∖H`. Picking one `S_θ` per active `θ` yields distinct residue codewords, hence pairwise `|S_θ∩S_{θ'}|≤k−1`: a constant‑weight code of length `n`, weight `s`, distance `≥2(σ+1)`. Such codes are exponentially large by Gilbert–Varshamov, so the pairwise/BCH shadow (`sec:pairwise`, `lem:pairwise`) **cannot** bound `|Θ_U|`. The bound must come from the simultaneous algebraic constraint that *all* configurations share the prefix `c` along the single curve `Γ` — a fixed‑prime incidence between a degree‑`(σ+1)` curve and the combinatorial set `Φ_{σ+1}(C(H,s))`, which is exactly the technology `prob:perfiber` names (FFT‑grid character sums on `H`).

**Why the norm sieve does not help (consistency with Cycle96).** A Type‑B configuration `S∪{θ}` lifted to `Z[ζ]` carries the arbitrary‑word coset height `≥p^{1−ρ−o(1)}` (`L-CYCLE96-WORD-HEIGHT-FLOOR`) in the `S`-part, *plus* an uncontrolled external coordinate `θ∈F_p` with no cyclotomic structure at all. `lem:galois-amp` still needs height `<p^{(σ+1)/n}/n`. So the norm contradiction fails at `b=1` at exactly the same `p`-range as `b=0`: **bandwidth‑1 raises neither the prime threshold nor the height floor.** The wall is purely fixed‑prime, confirming `L-CYCLE96-NORM-SIEVE-IS-DEAD` transfers.

**Why this is not equivalent to the full word.** For `deg U=s+b` the same argument gives configurations `W` with `|W|=s+b`, `|W∩H|≥s`, `Φ_{σ+b}(W)=c`, with **up to `b` external points**. The bandwidth filtration `F_b` adds external points one at a time; the full word (`deg U=n−1`) has `b=m−1=n−s−1` external points and an `(m−1)`-dimensional external family, versus the `1`-dimensional curve `Γ` here. So `b=1` is strictly the "one external point" layer: the ROUTE_CUT claiming `b=1≡full` is **false**.

---

## 4. Verification requirements

All finite, deterministic, in the existing toy range (extend `cycle96_word_height_floor_toy.py`):

1. **Decomposition checker.** For small `p≡1 mod n`, `n∈{8,16}`, random monic `U` of degree `s+1`: enumerate `List(U,1−s/n)` directly by trying all `P` of degree `<k`; independently enumerate `V_A` (prefix fibers on `(s+1)`-subsets) and `V_B` (for each `θ∈F_p∖H`, the prefix fiber `Φ_{σ+1}^{-1}(c(θ))` on `s`-subsets). Assert the two counts and the bijection `P↦V` agree, and `θ=c_1−e_1(S)` holds for every Type‑B solution. This certifies Theorem B1.
2. **Active‑root growth.** For a sweep of `(n,k,σ)` along the reserve `σ≈Cn/log n` and increasing `p`, log `|Θ_U|` and `|Θ_U^{aper}|` (after removing `θ` whose fiber is a `μ_M`-coset class with `M>σ`). Test whether `|Θ_U^{aper}|` stays `≤ poly(n)` (evidence for PROOF) or grows superpolynomially (COUNTERPACKET).
3. **Curve‑image incidence.** Directly compute `|Γ ∩ Φ_{σ+1}(C(H,s))|` and compare with the random prediction `≈ binom(n,s)/p^σ`‑scale to detect structured `U` that inflate the incidence on a coset.

---

## 5. Next exact lemma / construction

The route to a full solve is: **(a)** bandwidth‑0 prefix local limit (existing); **(b)** for each `b`, the active external‑configuration bound; **(c)** induction on `b` to `b=m−1`. The next exact lemma is the `b=1` instance:

> **Lemma S1‑B1 (to prove or kill).** There is `B=B(ρ)` such that for `σ≥Cn/log n`, all `p≡1 mod n` with `n^{c_0}≤p≤2^{o(n)}`, and every monic `U` of degree `s+1`,
> ```
>   #{ θ∈F_p∖H : Φ_{σ+1}^{-1}(c(θ)) ≠ ∅, fiber not a single μ_M-coset class (M>σ) }  ≤ n^B.
> ```

**Exact character‑sum form to attack (fixed‑prime, no `Z[ζ]` lift).** With `e_θ(j):=Σ_{x∈H}1_S(x)ω^{jx}` notation replaced by the prefix indicator, `θ` is active iff the system `p_j(S)=P_j−(P_1−u)^j` (`2≤j≤σ+1`, `u=P_1−p_1(S)−... `) has a `0/1` weight‑`s` solution on `H`; counting active `θ` is
```
  |Θ_U| = Σ_{u∈F_p} 1[ ∃ S⊆H,|S|=s : p_j(S)=P_j−(P_1−u)^j, j=2,…,σ+1 ],
```
and the natural majorant is the even‑moment / Stepanov count of `s`-subsets whose first `σ+1` power sums lie on the rational curve `u↦(u,P_2−(P_1−u)^2,…)`. The crisp sublemma that converts this to PROOF: **a Weil/Stepanov bound for the number of `F_p`-points of the curve `Γ` lying in the prefix image, after quotient‑periodic `θ` are removed** — i.e. show `Γ` is not contained in (and meets polynomially) the periodicity strata, the only place the count can blow up.

**Counterpacket shape (to refute).** A monic `U` of degree `s+1` (above reserve, generated prime field) for which `Γ` lies on a `μ_M`-coset translate forcing superpolynomially many aperiodic active `θ`. By the decomposition this is the *only* way `b=1` can beat `b=0`; the toy sweep in §4.2 is the decisive test. The two‑moment fullness theory (`thm:twomoment`) suggests the `j=2` parabola constraint already equidistributes `(p_1,p_2)`, which would *prevent* such a packet — but this is exactly the unproven fixed‑prime input.

---

## Self‑audit

1. **Proved / not proved.** Proved: the exact bandwidth‑1 decomposition `List(U)≅V_A⊔V_B` with `V_A` a `b=0` fiber at `(k,σ+1)`, `V_B` a `θ`-union of `b=0` fibers at `(k−1,σ+1)`, `θ=c_1−e_1(S)`, external curve degree `σ+1`; and the reduction "S1 for `b=1` ⟺ (`b=0` local limit) ∧ (`|Θ_U^{aper}|≤n^{O(1)}`)". Not proved: the active‑root bound `|Θ_U^{aper}|≤n^{O(1)}` itself, and hence not the `b=1` collision bound; no counterpacket produced.
2. **Prize relevance.** Upper‑side, direction of `ε_mca` over `thm:normalform`, `q_chal=q_line=q=p`, target `|L_w|≤2^{-128}q`. It kills a candidate shortcut (`b=1≡full`) and isolates the exact missing scalar; it is a route‑structuring lemma + restated wall, **not** a finite prize certificate and **not** a counterpacket.
3. **First line that could fail.** `L-CYCLE95-ANCHORED-T1-EVAL-LIST` and Theorem B1 are unconditional. The first failure point is **the active‑external‑root bound** `|Γ∩Φ_{σ+1}(C(H,s))|≤n^{O(1)}` — the genuinely new fixed‑prime incidence — and, upstream of it, the `b=0` prefix local limit at the polynomial‑field reserve (open beyond `p>exp((log n)^2)`).
4. **Field/`2^{-128}` usage.** Correct. Slopes `z=P(α)/B∈F_p`; list normalized by `q=q_line=q_code=q_chal=p`; covering‑radius/height and the curve `Γ` live in the generated field `q_gen=q_D=p`; `2^{-128}` enters as `|List|≤2^{-128}p`, which B1 reduces to `b=0`-fibers `+` `|Θ_U^{aper}|`. No ledger merge; binomial reserve not conflated with corrected `τ*`/quotient reserve.
5. **Numerator reductions.** Quotient/periodic: each fixed‑`θ` slice and Type A are charged into the separated `2^{(β/H)Q_H}` term (`rem:aper`); my claim concerns `Λ^aper`. Contained incidences: noncontainment automatic (Cycle95). Same‑slope `P(α)=P'(α)`: only shrinks `|eval_α(L_w)|` below `|List|`, so it can only help the upper bound (adversary takes `α∉D` off the `≤k` roots of each pairwise difference). Affine color: scaling `U` rescales `θ` bijectively (count‑invariant); additive translation does not preserve `H`, so is unavailable — and crucially none of these removes the external‑root continuum, which is the whole obstruction.
6. **PLAN→PROOF / COUNTERPACKET.** PROOF: establish Lemma S1‑B1 via a Stepanov/Weil incidence bound for the degree‑`(σ+1)` curve `Γ` against the prefix image, with periodic `θ` charged; combine with the `b=0` local limit and induct on `b`. COUNTERPACKET: a monic degree‑`(s+1)` `U` over a generated prime field, above reserve, whose curve `Γ` sits on a coset translate yielding superpolynomially many aperiodic active `θ` — detected by the §4.2 toy sweep showing superpolynomial growth of `|Θ_U^{aper}|`.