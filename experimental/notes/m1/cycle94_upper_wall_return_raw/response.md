I'll start by reading the file index, then the key state and source files.The index is large. Let me read the key state files and the specific source files named in the prompt directly.Now let me read the Cycle 93 brief, the corrected reserve audit, and the key source files in parallel.Let me find the exact paths for the source files I need to read.I need to find the m1 audit files and tex files. Let me grep the index.The index is very large. Let me jump to where cycle 89-94 m1 files and the tex files would be listed.Let me read the key audit and source files directly using the path patterns I've observed.Now let me read the core source files: the slackMCA tex (normal-form, def:mca, def:residue, corrected reserve) and the cycle89 official MCA row audit.Now let me read the key tex source files for the normal-form theorem and the upper-side definitions. Let me find the tex paths.I have the core source. Let me read the remaining referenced audit and the project readme/agents files.PLAN / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL

I read `readme.md`, `tex/slackMCA_v3.tex` (normal form, `def:mca`, `def:residue`, `thm:normalform`, `prop:noanchor`, `prob:perfiber`, `conj:B`, `conj:final-mca`), and the three referenced m1 audits (cycle89/92/93). I did not need `RS_disproof_v3.tex` for the upper side; its role is the lower oracle and it does not constrain the safe-side numerator. Below is the cycle94 return to the upper wall.

## 1. Executive verdict and confidence

I do not have a proof of the upper residue-cloud theorem, and I can show cleanly why the natural route fails. What I can bank is a theorem-grade structural lemma that generalizes `lem:pairwise` from the monomial prefix stratum to arbitrary anchored residue-line data, and that lemma cuts the pairwise/packing route to the whole upper wall. The remaining gap is exactly one finite local-limit statement, the anchored generalization of `prob:perfiber`.

Confidence: high on the bankable lemma and the route cut (elementary degree counting, fully checkable). High on the claim that the arbitrary-anchor case strictly loses the moment structure the monomial theory uses (this is `prop:noanchor` made quantitative). Moderate on the proposed Cycle95 lemma being the genuinely minimal missing piece rather than one of several.

## 2. The exact finite upper theorem that would settle the safe side

Work over the single slope field `F`, `|F| = q_line = q_code = q_chal = q`, with `C = RS[F,D,k]`, `D` a smooth generated-field domain of order `n`, `k = ρn`, radius `δ = 1 − ρ − η`, agreement size `s = ⌈(1−δ)n⌉ = k + σ`, `σ = ηn`. By `thm:normalform`,

```text
emca(C,δ) = (1/q) · max_{1≤t≤r} Λ^NC_{t,δ}(D,k),   r = n−k.
```

The safe-side target (packing form of `conj:final-mca`, `rem:aper`) is the following.

Residue-cloud upper theorem (RCUT). For every fixed `ρ∈(0,1)`, `B_0>0`, `ε>0` there is `C` such that for all large smooth generated-field `n`, if

```text
η ≥ (1+ε)·τ*(ρ, q_gen)        (generated-field entropy reserve)
Q_H(η) ≤ B_Q·log₂ n + O(log log n)   (quotient profile charged)
```

then, after separating quotient-periodic denominators (E a pullback through `x↦x^M`, `M | gcd(n,k)`, `M>1`),

```text
max_t Λ^aper_{t,δ}(D,k) ≤ n^{1+o(1)},
```

so that

```text
emca(C,δ) ≤ ( n^{1+o(1)} + 2^{(β(ρ)/H(ρ))·Q_H(η)(1+o(1))} ) / q_gen.
```

All quantifiers matter: `t` ranges over every denominator degree `1≤t≤r`; the datum `(E,B,w)` is arbitrary (`E` deg `t` nonzero on `D`, `deg B<t`, `w` an arbitrary anchor word); slopes are noncontained per `def:mca(ii)`; the exception term is exactly `thm:qnecessity`’s floor and is provably not removable.

## 3. The bankable lemma, the proof, and the route cut

The content of RCUT is: at one datum `(E,B,w)`, bound the number of `z` for which the word-line

```text
y_z = (w − zB)/E = (w/E) − z·(B/E)
```

is `δ`-close to `C` and noncontained. (This is the `(≥)` direction of `thm:normalform`: `f = w/E`, `g = −B/E`. Conversely `prop:noanchor` says `f` is fully arbitrary, so the upper wall is genuinely “all lines”.)

L-CYCLE94-ANCHORED-SECANT-INTERSECTION (bankable). Let `(E,B,w)` be a degree-`t` residue datum, `B≠0`. If `z≠z'` are both bad with maximal witness sets `S_z, S_{z'}`, then

```text
|S_z ∩ S_{z'}| ≤ k + t − 1.
```

Proof. A witness gives `Q_z`, `deg Q_z < k+t`, `Q_z ≡ zB (mod E)`, `Q_z = w` on `S_z`. On `S_z∩S_{z'}`, `Q_z = w = Q_{z'}`, so `Q_z − Q_{z'}` (degree `< k+t`) vanishes there. If `|S_z∩S_{z'}| ≥ k+t`, then `Q_z = Q_{z'}` identically, whence `(z−z')B ≡ 0 (mod E)`, i.e. `E | (z−z')B`. With `z≠z'` this forces `E | B`, impossible since `0 ≤ deg B < deg E = t` and `B≠0`. ∎

This is the exact generalization of `lem:pairwise`: that lemma is the special monomial case `(E,B,w)=(X^r,−1,x^T)` with the extra prefix-vanishing `e_1=⋯=e_{T−1}=0`, which sharpens `k+t−1 = n−1` down to `k−1`. The sharpening is supplied entirely by the vanishing power sums of the monomial witness, not by the pairwise relation.

ROUTE CUT. A family of `(k+σ)`-subsets of `[n]` pairwise meeting in `≤ k+t−1` points is, for the reserve scale `σ = ηn`, only a constant-weight code of distance `2(σ+1−t)`; by Gilbert–Varshamov such codes are exponentially large (`sec:pairwise` records this for `t` absorbed in `σ`). Therefore the pairwise/secant/BCH-distance route cannot prove RCUT for arbitrary anchors. The monomial theory escaped this only because the prefix constraints `e_1=⋯=e_{σ−1}=0` are an algebraic moment condition that collapses each slab to `μ_{M_0}`-rearrangement classes (`thm:rigidity`, `thm:exactcount`). `prop:noanchor` shows that for an arbitrary anchor `w` no characteristic-zero moment condition is available — the word is quantified after the prime — so every prime-averaging device of Part II (`thm:diag(ii)`, `thm:allbases`, `thm:stable`, `prop:qfloor`) is structurally inapplicable to the anchored count. The upper wall is therefore a fixed-prime problem, and the only surviving handle is a local-limit collision count.

## 4. Which wall is next

Keep `W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD` as the headline, but it is not atomic. The lemma above shows it factors through, and is blocked at, the second wall on your list:

```text
primary headline:  W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
enabling sub-wall: W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

The secant lemma is literally a transverse-intersection (secant) statement; the missing inverse is “bounded secants ⇒ entropy/local-limit count,” i.e. the conversion the pairwise bound cannot do unaided. `W-LIST-FULL-SUPPORT-INTERSECTION-LOCAL-LIMIT` is the list-side mirror of the same inverse and should be solved jointly. `W-MCA-HIGH-DENOMINATOR-THICK-RESIDUE-COMPRESSION` (large `t`) is a special hard slice — note the secant bound degrades to `n−1` there — but it is not where a first proof should start. Do not reopen the lower quotient-floor branch (`L-CYCLE93-...`); it is banked context only.

## 5. Next exact lemma / construction for Cycle95

The single statement that converts RCUT from PLAN to PROOF in the polynomial-field window is the anchored generalization of `prob:perfiber`.

L-CYCLE95-ANCHORED-PERFIBER-COLLISION (target). Fix `ρ, B_0, ε`. There is `C` such that for every smooth generated-field `H ≤ F_q^×` of order `n`, `k=ρn`, every `σ ≥ Cn/log n` with `σ log₂ q_gen ≥ (1+ε) log₂ C(n,k+σ)`, every large `p ≡ 1 (mod n)` with `n^{c0} ≤ p ≤ 2^{o(n)}`, and every residue datum `(E,B,w)` whose denominator `E` is not a pullback through a proper quotient `x↦x^M`: the number of slopes `z` admitting a noncontained `(k+σ)`-agreement witness for `y_z = w/E − z·B/E` is at most `n^{B_0}`; quotient-periodic `E` contribute at most `2^{(β/H)Q_H(η)(1+o(1))}`.

The minimal sublemma inside it (the actual Cycle95 atom): within one word-line `{y_z}`, the number of ordered pairs `(S,S')` of `(k+σ)`-sets that are residue-equal mod `p` (`deg((U_{w/E}−zU_{B/E}) mod L_S) < k` for a common `z`, matching `S'`) but inequivalent over `Z[ζ]` is `n^{O(1)}`. For the monomial datum this is exactly `prob:perfiber`; the new difficulty is solely that the anchor `w` shifts the prefix map by an arbitrary `n`-dependent vector, so the norm-sieve archimedean bound `‖h‖_1 ≤ 2s` of `thm:stable`/`prop:qfloor` must be replaced by a bound that survives an adversarial inhomogeneous term. Producing that archimedean control (or a fixed-prime substitute) is the crux.

Concrete first move I recommend for Cycle95: prove the `t=1`, fixed simple direction case `E = X−α`, `B=1`, `w` arbitrary — there the line is `w/(X−α) − z/(X−α)` and the noncontainment forces the secant bound `|S∩S'| ≤ k`. Decide whether the inhomogeneous norm sieve closes there at `σ ≥ Cn/log n`. A clean `t=1` theorem-grade bound would be the first unconditional crack in the arbitrary-anchor wall; a `t=1` counterexample would be an official counterpacket to RCUT and should be escalated.

## Verification requirements

The secant lemma needs only the degree count above and is reproducible by hand and by a small finite-field script (`scripts/mca_slope_scan.py`-style): for random `(E,B,w)` over a toy `F_p`, enumerate bad slopes and confirm pairwise `|S∩S'| ≤ k+t−1`, and confirm GV-exponential families saturating it. The Cycle95 target needs the existing `run_frontier.py` meet-in-the-middle harness extended with a nonzero anchor term, scanning whether per-line collision counts stay `n^{O(1)}` as `p` grows at fixed `σ ≈ n/log n`.

## Self-audit (the six required questions)

1. Proved: the anchored secant intersection lemma `|S_z∩S_{z'}| ≤ k+t−1` for distinct bad slopes of any degree-`t` residue datum, and as a corollary the route cut that pairwise information yields only GV-exponential bounds for arbitrary anchors. Not proved: RCUT itself, in any anchored regime including `t=1`.

2. Relevance: official-prize-relevant in direction (it is about `emca` over the full normal form, `q_chal = q_line = q`, target `2^-128`), but the concrete deliverable is a structural lemma plus a route cut, not a finite counterpacket and not a positive threshold certificate. It is upper-side progress (it eliminates a method), not a finished safe-side theorem.

3. First line that could fail: none in the secant lemma (it is unconditional). In the PLAN, the first failure point is the archimedean norm bound in L-CYCLE95: `prop:qfloor`’s estimate `|Norm ĥ(1)| ≤ (2ℓ')^{N'/2}` has no analogue once an arbitrary anchor adds an inhomogeneous, `n`-dependent term to the prefix map, exactly the obstruction of `prop:noanchor`.

4. Field usage: correct. The numerator `Λ^NC` is normalized by `q = q_line = q_code = q_chal` in `emca` (`thm:normalform`); the entropy reserve uses `q_gen` via `τ*(ρ,q_gen)` (`rem:subfield`, `cor:genfield-pigeonhole`); the `2^-128` target is the prize numerator. I did not conflate the simple binomial reserve with the corrected `τ*`/quotient reserve — that was precisely the Cycle93 correction and it is respected here.

5. Reductions of the numerator: yes, and they are charged correctly. Quotient/periodic structure is separated into the explicit `2^{(β/H)Q_H}` term (`rem:aper`, `thm:qnecessity`) and excluded from `Λ^aper`. Contained incidences are removed by noncontainment (`def:mca(ii)`), which is exactly what powers the secant lemma’s `B≠0`/`E∤B` step. Same-slope collisions are the `z=z'` case (excluded). Affine color normalization is the slope rescaling `z↦λz` and anchor shift, both of which the lemma is invariant under since it only uses `z≠z'` and `deg`.

6. Conversion of this PLAN: L-CYCLE95-ANCHORED-PERFIBER-COLLISION (with its `t=1` first case) converts RCUT into PROOF for the polynomial-field window; a `t=1` adversarial anchor with a stable exponential bad-slope cloud surviving reduction would instead be a COUNTERPACKET to RCUT. Either resolves the headline wall.

Dependency DAG for Cycle95:

```text
thm:normalform ──▶ Λ^NC at one datum (E,B,w)
        │
        ▼
L-CYCLE94-ANCHORED-SECANT-INTERSECTION  (proved)
        │  cuts pairwise route
        ▼
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
        │  needs: anchored norm sieve (archimedean control vs inhomogeneous term)
        ▼
L-CYCLE95-ANCHORED-PERFIBER-COLLISION   (open; start at t=1, E=X−α)
        │
        ▼
RCUT = W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
```