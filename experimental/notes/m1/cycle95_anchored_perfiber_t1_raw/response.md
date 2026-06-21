I'll start by reading the file index, then the required source files.The file index is large. Let me read the key project state files and the required source files directly using the paths from the prompt.Let me find the specific Cycle94 files and the tex source by searching the index.Let me locate the specific files I need to read. Let me search the file index for the relevant paths.The index is large and sorted by path. Let me jump ahead to find the `current_repo_snapshot`, `tex`, and cycle94/95 entries.The index is too large to page through. Let me grep it for the exact files I need.The required files are deep in the index. Let me jump to where the cycle94/95 files and the tex file should be listed. The tex file is at `tex/slackMCA_v3.tex`. Let me look at a later section of the index.Let me look near the end of the index where cycle94/95 and the tex files appear.I have the key paths now. Let me read the Cycle94 audit, Cycle94 response, the Cycle95 prompt, and the toy check script in parallel.I have strong context on the lemma and route. Now let me read the toy check script and the core tex definitions. Let me find their exact paths in the index.Now let me read the toy check script and find the tex file. Let me read the toy script and search for the tex path.Now I need the tex source. Let me find the tex file paths in the index.I found the tex file at `current_repo_snapshot/tex/slackMCA_v3.tex`. Let me read the relevant definitions. The file is 163KB. Let me read the parts containing the key definitions: normal form, def:mca, def:residue, prob:perfiber, prop:noanchor, and the reserve/quotient material. Let me start at the beginning to get the macros and main definitions.Let me read the integrated theorem package and continue to find the key labels.Let me find the residue normal-form and per-fiber sections. Let me grep for the key labels by reading the latter parts of the tex.Let me search for the normal form section using grep-like reading. I'll read further into the file where the residue normal form (thm:normalform), prop:noanchor, prob:perfiber, and conj:B appear.The file is 1987 lines. Let me read the latter portion where the normal form and conjectures appear.Now let me find the residue normal-form section, prop:noanchor, prob:perfiber, and conj:B. They're before the appendix. Let me read the MCA Part II sections.This is rich context. Now let me read the central section: the residue-line normal form (thm:normalform), def:mca, def:residue, prop:noanchor, and prob:perfiber. Let me read the section before this, where Part II MCA and the normal form are.I have the normal-form, def:residue, prop:noanchor, prob:perfiber, conj:B, prop:qfloor. Now let me read def:mca and the canonical slack calculus / lem:pairwise, which Cycle94 generalized. Let me find def:mca (Part II start) and lem:pairwise.Now let me read def:mca and the locator slack calculus, which is the canonical line (lem:tlocator, thm:slackt, thm:exactslack, lem:pairwise). Let me read the start of Part II.Let me read the Part I rigidity and Galois-collision sieve sections, which contain the norm-sieve machinery that the Cycle94 plan says must be transferred.Let me read the Galois-amplified collision sieve (thm:no-collision and surrounding norm argument), which is the precise norm-sieve archimedean machinery the Cycle94 plan references for the monomial case.BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL

I read `readme.md`/director state, `tex/slackMCA_v3.tex` (`def:mca`, `def:residue`, `thm:normalform`, `prop:noanchor`, `prob:perfiber`, `conj:B`, `conj:final-locator`/`conj:final-mca`, the slack calculus `thm:exactslack`/`lem:tlocator`/`thm:slackt`, the list side `def:locator-fiber`/`prop:arb-fiber`/`thm:qcore`/`cor:upstairs-poly`, and the Galois sieve `lem:galois-amp`/`thm:no-collision`/`prop:qfloor`), the Cycle94 audit and raw response, and the Cycle94 toy checker. Below is the Cycle95 result.

## 1. Executive verdict and confidence

I did not find an independent elementary proof of the `t=1` arbitrary‑anchor bound, and I can show cleanly why one should not exist by the proposed route. What I can bank is an **exact reduction**: the `t=1`, `E=X−α`, `B=1` residue cloud is, slope for slope, the evaluation‑at‑`α` image of the **dimension‑`(k+1)` arbitrary‑word locator list** of `w`. Three consequences are unconditional and checkable: (i) noncontainment is automatic in this stratum; (ii) the bad‑slope set is *exactly* `{P(α) : P∈List(RS[F,D,k+1], w) at agreement k+σ}`; (iii) hence the cloud has size `≤ |List|`. The headline finding is therefore that `L-CYCLE95-ANCHORED-PERFIBER-COLLISION-T1` is **not a new wall** — it collapses onto the already‑isolated arbitrary‑word list local limit `conj:final-locator` (at dimension `k+1`), so the `t=1` MCA wall and the list wall are the same wall.

Confidence: high on the reduction and on automatic noncontainment (elementary, and exactly what the Cycle94 toy checker already computes). High on the route cut (it is `prop:noanchor` made quantitative). Moderate‑to‑high that the only place a genuinely `t=1`‑specific theorem could beat `conj:final-locator` is the eval‑at‑`α` collapse, which I argue the adversary defeats by choosing `α` whenever `q` is large.

## 2. Exact `t=1` theorem in source‑valid notation

Fix the slope field `F=F_q` with `q=q_line=q_code=q_chal`, `C=RS[F,D,k]`, `D≤F^×` smooth generated‑field of order `n`, `k=ρn`, `s=k+σ`, `δ=1−(k+σ)/n=1−ρ−η`, `η=σ/n`. Take the datum `(E,B,w)=(X−α, 1, w)` with `α∈F∖D`, `w:D→F` arbitrary (`def:residue`, `t=1`). Write `L_w := List(RS[F,D,k+1], w, δ) = {P∈F[X] : deg P≤k, |{x∈D:P(x)=w(x)}|≥k+σ}` (the dimension‑`(k+1)` list of `w`; `def:locator-fiber`, `prop:arb-fiber` with `k→k+1`).

L‑CYCLE95‑ANCHORED‑T1‑EVAL‑LIST (bankable, exact).
```
(a) Automatic noncontainment: for every witness with |S|>k, the direction word
    g = -B/E = -1/(X-α) is NOT explained by any G∈F_{<k}[X] on S; so every
    (k+σ)-agreement witness is noncontained.
(b) Exact slope identity: the set of support-wise MCA-bad slopes of the line
    y_z = w/(X-α) - z/(X-α) at radius δ is EXACTLY
        Z = { P(α) : P ∈ L_w }.
(c) Count: Λ^NC_{1,δ}((X-α,1,w)) = |Z| = |eval_α(L_w)| ≤ |L_w|.
(d) For a general nonzero constant B, z = P(α)/B; the count is identical
    (affine color rescaling).
```

The exact source‑valid `t=1` RCUT statement is then conditional, and it is the cleanest sharp replacement:
```
THEOREM (t=1 anchored RCUT, conditional on conj:final-locator at dim k+1).
For aperiodic w (w not in a dimension-(k+1) quotient-core class, rem:aper),
σ≥Cn/log n and σ·log₂ q_gen ≥ (1+ε)·log₂ C(n,k+σ):
        Λ^NC_{1,1-ρ-η}((X-α,1,w)) ≤ |L_w| ≤ n^{B}.
The quotient-periodic w contribute the separated 2^{(β/H)Q_H(η)} term, exactly
as in conj:B / rem:aper, transferred through ρ→ρ+1/n.
```

## 3. Proof of the bankable lemma, and the obstruction to the strong claim

Proof of (a). A witness needs `G∈F_{<k}[X]` with `(x−α)G(x)=−1` for `x∈S`. Then `(X−α)G(X)+1` has degree `≤k` and vanishes on `S`, `|S|=k+σ>k`; a nonzero polynomial of degree `≤k` cannot have `>k` roots, so `(X−α)G+1≡0`, forcing `(X−α)∣1` — impossible. So `g=−1/(X−α)` is never contained on a `>k` support; noncontainment holds for free. (This is exactly why the simple‑pole direction is a *genuine* line, `def:mca`(ii) always active; it uses only `B≠0`, `deg B<t=1`, so it holds for every `t=1` datum.)

Proof of (b),(c). A witness is `(Q_z,S_z)` with `deg Q_z<k+t=k+1`, `Q_z≡zB≡z (mod X−α)` i.e. `Q_z(α)=z`, and `Q_z=w` on `S_z`, `|S_z|≥k+σ`. So `Q_z` is a degree‑`≤k` polynomial agreeing with `w` on `≥k+σ` points: `Q_z∈L_w`, and `z=Q_z(α)`. Conversely any `P∈L_w` yields the bad slope `z=P(α)` with witness `(P, {P=w})` (noncontained by (a)). Distinct slopes force distinct `P` (since `z=P(α)`), so `Z=eval_α(L_w)` exactly, and `|Z|≤|L_w|`. ∎ This is precisely the computation in `cycle94_anchored_secant_toy_check.py`: for `t=1` it interpolates `w` on each support, keeps it iff `deg<k+1`, and reads the slope as `q_poly mod (X−α)=Q_S(α)`.

Why the strong (unconditional) claim is blocked. By (b)–(c), bounding the aperiodic `t=1` cloud is bounding the **arbitrary‑word** dimension‑`(k+1)` list. Three facts pin this as genuinely the open list problem, not an easier secant problem:

- We are *beyond Johnson*: radius `1−ρ−η` with `η=Θ(1/log n)` and `ρ+η<√ρ` for fixed `ρ`, so combinatorial list‑decoding bounds do not apply; quotient cores (`thm:qcore`) give superpolynomial lists here, exactly the periodic part we must charge.
- `prop:noanchor`: an arbitrary anchor `w` admits no word‑free/characteristic‑zero condition — `f=w/E` is an arbitrary word — so every prime‑averaging device (`thm:diag`, `prop:qfloor`, `thm:stable`, `thm:no-collision`) is structurally inapplicable. The monomial sieve `thm:no-collision` used coefficients in `{−1,0,1}` (`|N(G(ξ))|≤(2n)^{n/2M}`); the arbitrary‑word lift `U∈Z[ζ][X]` has *unbounded* archimedean coefficients, so the norm bound `‖h‖₁≤2s` of `prop:qfloor` has no analogue. This is the exact inhomogeneous obstruction the Cycle94 plan flagged, now localized to the missing archimedean bound.
- Cycle94 secant route: distinct slopes give codewords `P_i` with `|S_i∩S_j|≤k+t−1=k` (the difference vanishes on the common agreement and is degree `≤k`); the `S_i` are a constant‑weight code of distance `2σ`, which is GV‑exponential — so the secant bound alone yields nothing, and the extra fact "`P_i−P_j` does not vanish at `α`" does not improve the count. Route cut re‑confirmed at `t=1`.

Can the anchor be removed / normalized / charged? Removed: no — `w=0` gives `Q_z≡0` and `z=0` only (`Λ=1`); the entire content is in `w`. Normalized: yes but harmlessly — adding a degree‑`≤k` codeword to `w` translates all slopes by `P_0(α)` (count‑invariant), and `B≠1` only rescales `z↦z/B`; so only the coset `w+RS[F,D,k+1]` (the syndrome) matters, still an arbitrary high‑degree word. Charged: the quotient‑periodic `w` (dimension‑`(k+1)` quotient cores) are separated into the `2^{(β/H)Q_H(η)}` term exactly as `rem:aper`/`conj:B`, leaving the aperiodic `n^{1+o(1)}` target.

Is there a counterpacket? A source‑valid `t=1` counterpacket (aperiodic `w`, stable superpolynomial cloud, not quotient‑periodic) would be, by (b)–(c), an aperiodic superpolynomial dimension‑`(k+1)` list whose `eval_α` image stays superpolynomial — i.e. a refutation of `conj:final-locator`, the paper's expected positive theorem. The only known superpolynomial source is quotient cores, which are periodic and excluded. So no counterpacket is available here; producing one would be a far bigger event (killing the list conjecture), and I do not have a mechanism for it.

## 4. Verification requirements

- (a),(b),(c) are reproducible by the existing `cycle94_anchored_secant_toy_check.py` restricted to `t=1`: it already computes `slope = Q_S(α)` and groups supports by slope. Add two assertions: (i) for every random `(α,w)` over toy `F_p`, the set of bad slopes equals `{P(α)}` over the enumerated dimension‑`(k+1)` codeword list of `w` (re‑interpolate, dedupe by codeword), confirming the exact identity and `|Z|≤|codeword list|`; (ii) confirm noncontainment fires for *every* support (no `G` exists), i.e. the `t=1` cloud loses nothing to containment.
- The conditional theorem needs nothing new beyond `conj:final-locator`; to test the eval‑collapse question, extend `scripts/run_frontier.py` to sweep `α∈F∖D` for fixed superpolynomial quotient‑core `w` and record `|eval_α(list)|` vs `|list|` as `q` grows — this measures whether the projection can ever rescue an exponential list (it should not, for large `q`).

## 5. Next exact lemma / construction

The single statement that converts the `t=1` (and, with the dimension shift absorbed, the general) arbitrary‑anchor RCUT from PLAN to PROOF is the arbitrary‑word generalization of `thm:no-collision`:

L‑CYCLE96‑ARBITRARY‑WORD‑NORM‑SIEVE (target).
```
Let p≡1 (mod n), H≅μ_n, U∈Z[ζ_n][X] a lift of an arbitrary word w:H→F_p,
deg U<n, dimension k+1. For (k+σ)-supports S,S' with deg(U mod L_S),
deg(U mod L_{S'})≤k and P_S≡P_{S'} (mod 𝔭): if σ≥Cn/log n and
p>exp(C·n log n/σ), then either S△S' is quotient-periodic (a union of cosets
of a subgroup of order M>σ), or P_S≡P_{S'} over Z[ζ].
```
The crux is exactly the missing archimedean control: replace the `{−1,0,1}`‑coefficient bound `‖h‖₁≤2s` (valid only for monomial‑prefix `U_c=X^s+…`) by a bound that survives an arbitrary lift `U`, or by a genuine fixed‑prime local‑limit substitute (the `rem:galois-limit` last `log n` factor). The smallest honest milestone toward it: prove the **eval‑collapse never helps** in the large‑field regime — i.e., for `q≥` a suitable polynomial threshold, `|eval_α(L_w)|=Θ(|L_w|)` for adversarial `α` — which shows the `t=1` cloud cannot be polynomially small unless `L_w` already is, closing the equivalence and proving that no `t=1`‑specific shortcut exists.

Dependency DAG for Cycle95:
```
thm:normalform ── Λ^NC at one datum (E,B,w)
        │  t=1, E=X-α, B=1
        ▼
L-CYCLE95-ANCHORED-T1-EVAL-LIST  (PROVED)
   bad slopes = eval_α(dimension-(k+1) arbitrary-word list of w)
   noncontainment automatic; secant/norm-sieve route CUT (=arbitrary-word list)
        │  collapses onto
        ▼
conj:final-locator (dim k+1)  ⟸  L-CYCLE96-ARBITRARY-WORD-NORM-SIEVE (open)
        │                         crux: archimedean control of arbitrary lift
        ▼
RCUT = W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
```

## Self‑audit (six required questions)

1. Proved: the exact identity `Λ^NC_{1,δ}((X−α,1,w)) = |eval_α(L_w)| ≤ |L_w|` and automatic noncontainment for every `t=1` datum (`B≠0`, `deg B<1`). Not proved: the `t=1` polynomial bound itself, in any nontrivial field regime — it is reduced to, and is morally as hard as, `conj:final-locator` at dimension `k+1`.

2. Official‑prize‑relevant in direction (it is about `emca` over `thm:normalform`, `q_chal=q_line=q`, target `2^-128`), but the deliverable is a reduction lemma plus a route cut, not a finite counterpacket and not a positive threshold certificate. It is upper‑side progress that *identifies the wall*, not a finished safe‑side theorem.

3. First line that could fail: none in L‑CYCLE95‑ANCHORED‑T1‑EVAL‑LIST (unconditional, degree count). In the conditional theorem the first failure point is `conj:final-locator` itself; concretely, the archimedean step of `prop:qfloor`/`thm:no-collision` (`‖h‖₁≤2s`) has no analogue for an arbitrary lift `U`, exactly `prop:noanchor`.

4. Field usage: correct. `Λ^NC` is normalized by `q=q_line=q_code=q_chal` in `emca` (`thm:normalform`); slopes `z=P(α)/B∈F_q`. The reserve uses `q_gen=q_D` via `τ*(ρ,q_gen)` and the entropy condition, transferred under `ρ→ρ+1/n`, `σ→σ−1` (asymptotically unchanged). The `2^-128` target enters as `Λ_1/q≤|L_w|/q`: beating it on the safe side is exactly `|L_w|≤2^{-128}q`, i.e. a polynomial aperiodic list over a large field — the `conj:final-locator` content. I did not conflate the simple binomial reserve with the corrected `τ*`/quotient reserve.

5. Reductions of the numerator. Quotient/periodic: yes, charged — periodic `w` (dimension‑`(k+1)` quotient cores) give the superpolynomial part, separated into `2^{(β/H)Q_H(η)}` (`rem:aper`), excluded from `Λ^aper`. Contained incidences: removed by noncontainment, but here noncontainment is *automatic*, so it removes nothing — the `t=1`,`B=1` cloud is the full eval‑image, no slope is lost to containment. Same‑slope collisions: these are exactly the `eval_α` collisions `P(α)=P'(α)`; they are the *only* mechanism that can push `|Z|` below `|L_w|`, and the adversary defeats them by choosing `α∈F∖D` avoiding the `≤k` roots of each pairwise difference whenever `q` is large. Affine color normalization: `B≠1` rescales `z↦z/B` and a degree‑`≤k` codeword added to `w` translates `z↦z+P_0(α)`; both are count‑invariant bijections, so they do not reduce the numerator.

6. This PLAN converts to PROOF via L‑CYCLE96‑ARBITRARY‑WORD‑NORM‑SIEVE (equivalently `conj:final-locator` at dim `k+1`), which makes the aperiodic `t=1` cloud `≤n^B`; it converts to COUNTERPACKET via an aperiodic, non‑quotient‑periodic `w` whose dimension‑`(k+1)` list is superpolynomial and survives `eval_α` — which would simultaneously refute `conj:final-locator`. Either resolves the headline wall, and both now point at the same object: arbitrary‑word locator collisions, not anchored secants.