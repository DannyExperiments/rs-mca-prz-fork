I'll start by reading the file index, then the key project files to understand the context before attacking the problem.Let me read the key files mentioned in the prompt. I'll start with the most relevant cycle 104/105 files and project state.Let me find the exact paths in the file index by searching for the cycle104 and cycle105 m1 files.Now I have the exact paths. Let me read the key M1 cycle files: the Cycle105 prompt, the Cycle104 proof response, and the Cycle104 prompt, in parallel.This is a deep algebraic problem. Let me read the surrounding context: the Cycle104 prompt, Cycle103 brief, and the foundational state files to lock the exact definitions (reserve, aperiodic, Θ_U, the q-ledger).Let me read the Cycle103 materials and the project state files in parallel to lock the foundational definitions.This is a deep algebraic problem. I've extracted the core reformulation already, but I need to lock down the exact regime, the meaning of "reserve", "aperiodic", and the q-ledger. Let me read the state files in parallel.I have the core reformulation. Now I need the foundational definitions: the meaning of σ, "reserve", "aperiodic", and the q-ledger. Let me read the state files in parallel.I now have the precise mathematical structure. Let me read the moment-curve incidence work (cycles 98-100) and the cuts file, since the problem reduces exactly to that incidence question. These will tell me whether a counterpacket or uniform bound is the right call. ## Classification

```text
BANKABLE_LEMMA   (k-independent collapse: bandwidth-k activity is incidence of ONE
                  fixed degree-(σ+1) curve in A^{σ+1} with the symmetric-prefix image
                  M_s; the C(n,k) of Cycle104 is a union-bound artifact, not intrinsic)
+ BANKABLE_LEMMA (complement duality ι: M_s ≅ M_{n-s} under a fixed triangular
                  automorphism, so WLOG s ≤ n/2)
+ ROUTE_CUT      (in the prize reserve σ = o(n) the activity radius is BEYOND the
                  Johnson radius; no characteristic-free / list-generic / per-word
                  list-size proof can give the uniform bound — it must consume
                  aperiodicity)
+ EXACT_NEW_WALL (the uniform bound = a k-free eliminant-degree bound for the
                  aperiodic moment-curve / symmetric-prefix incidence)
```

I do **not** prove the uniform-in-`k` bound and I do **not** produce an aperiodic counterpacket. I prove the reduction that makes the problem `k`-independent, prove the regime fact that forces any solution to use the reserve, and state the single residual lemma plus the checker that converts it. All algebra is hand-derived (Read-only harness); one finite checker is flagged for Codex.

Notation as banked: `p` prime, `n∣p−1`, `H=μ_n⊆F_p^*`, `∏_{x∈H}(X−x)=X^n−1` (squarefree, split). `Uhat=Σu_jX^j`, `u_0=1`. Fix `σ≥1`, bandwidth `k`, `s=σ+k`, `m=n−s`. Co-locator `G(θ,X)=Σ_{l=0}^{σ+1}g_l(θ)X^l`, `g_l(θ)=Σ_{i=0}^l u_{l−i}θ^i` monic of degree `l` in `θ`.

---

## 1. The k-independent collapse (main bankable lemma)

Cycle104 unioned over `C(n,k)` `k`-subsets. That cost is **not intrinsic**. The activity predicate lives in a space whose dimension is `σ+1`, independent of `k`.

**Lemma C (collapse).** For `g_{S̄}(X)=∏_{x∈S̄}(1−xX)=Σ_l(−1)^l e_l(S̄)X^l`,

```text
θ active  ⟺  ∃ S̄⊆μ_n, |S̄|=s,  with  g_{S̄}(X) ≡ G(θ,X)  (mod X^{σ+2})
          ⟺  ( g_1(θ),…,g_{σ+1}(θ) )  ∈  M_s,
M_s := { ( (−1)^l e_l(S̄) )_{l=1}^{σ+1}  :  S̄⊆μ_n, |S̄|=s }  ⊆  A^{σ+1}.
```

*Proof.* From `(♦)` (banked Cycle104), `θ` active iff `B_θ(X)−ψ(X)=∏_{x∈S̄}(X−x)` for some `s`-set `S̄` and `degψ≤k−2`. Reversing (multiply by `X^{−s}`, substitute `X→1/X`) turns the monic divisor into `g_{S̄}`, turns `B_θ` into `G(θ,·)`, and turns the free `ψ` (degrees `0..k−2`) into the free top coefficients of `g_{S̄}` (degrees `σ+2..s`). Matching the *pinned* coefficients `0..σ+1` gives `(−1)^l e_l(S̄)=g_l(θ)`, `l=1..σ+1` (`l=0` is `1=1`). ∎

Two consequences that are the whole point:

- **The incidence variety is one fixed curve.** `Γ := {(g_1(θ),…,g_{σ+1}(θ)) : θ∈F_p}` is a rational curve of degree `σ+1` (since `g_l` is monic of degree `l`; `g_1=θ+u_1` recovers `θ` linearly). `Γ` depends only on `(Uhat,σ)` — **not on `k`**. The only `k`-dependence in the entire problem is the subset size `s` selecting which finite point set `M_s` we hit. So `|Θ_U| = |Γ ∩ M_s|_{distinct θ}` and *all bandwidths share the same curve.* This is the exact `k`-free reformulation; it strictly reduces `W-CYCLE105` to "`s`-uniform moment-curve / symmetric-prefix incidence," and it folds `k=1` (Cycle103) and every fixed `k` (Cycle104) into one statement.

- **Newton coordinates.** Via the fixed triangular Newton bijection, `M_s ↔ P_s := {(p_1(S̄),…,p_{σ+1}(S̄))}` and `Γ ↔ {(q_1(θ),…,q_{σ+1}(θ))}` with `deg q_j=j`. So the object is literally the **moment curve against the power-sum image of `s`-subsets of a multiplicative subgroup** — exactly the Cycle98–100 normal form `v(F_p)∩(P−M_s)`, now seen to be `k`-uniform.

---

## 2. Complement duality (bankable)

Let `a_l=(−1)^l e_l(S̄)`, `b_l=(−1)^l e_l(S')` for the complement `S'=μ_n∖S̄`, `|S'|=m`. From `g_{S̄}g_{S'}=1−X^n≡1 (mod X^{σ+2})` (valid since `n≥σ+2`):

```text
Σ_{i+j=t} a_i b_j = 0   (t=1..σ+1),   a_0=b_0=1.
```

This triangular system is a **fixed polynomial automorphism** `ι:A^{σ+1}→A^{σ+1}`, `(a_l)↦(b_l)`, independent of `s,m,k,Uhat`. Hence `M_s = ι^{-1}(M_m)` and

```text
|Θ_U(k)| = |Γ ∩ M_s| = | ι(Γ) ∩ M_m |,    m = n−s.
```

So bandwidth `s` and bandwidth `n−s` carry the same incidence up to bending the curve by the fixed `ι`. **WLOG `s ≤ n/2`** (equivalently `k ≤ n/2−σ`); the small side has `|M_{\min(s,m)}|≤C(n,\min(s,m))`. This collapses the two extreme regimes (small `k`, and `k` near `n−σ`) but does **not** by itself break the central `k=ρn`, `m=(1−ρ)n` regime, where both `C(n,s)` and `C(n,m)` are exponential.

---

## 3. Regime fact and route-cut: the bound must consume the reserve

This is the decisive structural statement, and it determines what kind of proof is even possible.

Activity = `B_θ|_{μ_n}` lies within Hamming distance `m=n−σ−k` of the RS code `RS_{k−1}` (= evaluations of `degψ≤k−2`). In the prize regime `k=ρn`, reserve `σ=Θ(n/\log n)=o(n)`:

```text
relative agreement   s/n = ρ + o(1),       code rate  R = (k−1)/n ≈ ρ,
Johnson agreement     √R = √ρ  >  ρ          (for 0<ρ<1).
```

So `s/n ≈ ρ < √ρ`: the agreement is **below the Johnson bound**, i.e. the decoding radius `m` is **beyond the Johnson radius**. (Concretely `m≤Johnson ⟺ σ ≥ √ρ(1−√ρ)n`, i.e. only when `σ` is *linear* in `n`. The prize reserve is sublinear, so we are beyond Johnson.)

**Route-cut 3.** Beyond the Johnson radius, RS codes over multiplicative-subgroup evaluation points are known to admit **superpolynomial list sizes** (BKR-type subgroup/subfield configurations). Therefore:

- No characteristic-free, list-decoding-generic, or per-received-word list-size bound can prove `|Θ_U|≤n^{O(1)}` here; the worst received word in the tube genuinely has a superpolynomial list.
- Any valid uniform proof **must use aperiodicity of `Uhat` above the corrected reserve** to exclude exactly those subgroup-periodic configurations. This is the precise reason the Cycle104 divided-difference tool (which is unconditional in `Uhat`) cannot extend: an unconditional method would also "prove" the false periodic case.

This is consistent with the program's design: the superpolynomial-list configurations are the *periodic/below-reserve* branch that is **charged**; above reserve the bound is conjecturally true *because* aperiodicity kills them. The counterpacket hunt therefore belongs in the charged branch, not against the claimed (aperiodic) statement.

---

## 4. Why C(n,k) is not intrinsic, and the exact residual lemma

By §1 the eliminant of `S̄` from the `σ+1` equations `g_l(θ)=(−1)^l e_l(S̄)` is a single principal-type object: a nonzero `Ψ_{Uhat,σ,s}(θ)∈F_p[θ]` vanishing on `Θ_U`. The minimal such `Ψ` has `degΨ = |Θ_U|`, so a degree bound *is* the theorem. The `C(n,k)` (resp. `n^{O(k)}` resultant) bound comes from eliminating the `(k−1)`-dimensional free-`ψ` space coordinate-by-coordinate; but the free space never enters `Γ` (§1), so the honest elimination is `S̄` against the **fixed** curve `Γ⊆A^{σ+1}`.

**Residual Lemma (what converts this to PROOF).** *For aperiodic `Uhat` above corrected reserve, the moment-curve incidence `Γ∩M_s` has size `n^{O(1)}` with the exponent independent of `s` (hence of `k`).* Equivalently, there is a nonzero `Ψ(θ)` of degree `poly(n,σ)` (not `poly·n^k`) vanishing on `Θ_U`.

The most promising concrete vehicle, in order:

1. **Single subresultant eliminating `S̄`, not `k`-subsets.** Build the order-`(σ+1)` obstruction *once* on `Γ` (a Wronskian/Hankel determinant in `θ` of the `σ+1` power-sum coordinates against the subgroup), whose degree is governed by `n,σ` only. The `k`-subset union of Cycle104 is the wasteful expansion of this single determinant.
2. **Aperiodic dephasing on the resonant frequencies** (Cycle100 §3): the only frequencies `t` with no symmetric-function cancellation are supported on `Mℤ`, `M∣n`; aperiodic `Uhat` dephases them, capping the surviving (periodic) contribution at `2^{\log n}=n^{O(1)}`. Porting that cap from the weighted count `N` to the distinct support `|Θ_U|` is the same residual lemma viewed analytically.

Both routes reduce to: *bound `|Γ∩M_s|` using only that `μ_n` is a multiplicative subgroup and `Uhat` is aperiodic.* That is the wall.

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE  (sharpened, k-free form):
For aperiodic Uhat above corrected reserve and every s∈[σ+1, n],
| Γ ∩ M_s |_distinct ≤ n^{O(1)},   Γ = {(g_1(θ),…,g_{σ+1}(θ))} fixed, deg σ+1.
```

---

## 5. Counterpacket template (and why it lands in the charged branch)

To kill the bound one needs aperiodic `Uhat`, growing `k`, superpolynomially many distinct active `θ`. By §1 (take `Uhat=1` as the cleanest probe, giving `Γ` = the moment curve) this is:

```text
many distinct s-subsets S̄⊆μ_n  with  e_2(S̄)=⋯=e_{σ+1}(S̄)=0  and distinct e_1(S̄)
   ⟺  S̄∪{−θ}  has its top σ+1 elementary symmetric functions zero, θ = Σ_{x∈S̄}x.
```

i.e. `(X+θ)∏_{x∈S̄}(X−x)` has vanishing coefficients in degrees `s,…,k`. Every explicit large family I can build for this is a **coset-pair / nested-subgroup swap** (the PTE min-distance is `≥2(σ+2)`, Cycle100 Lemma 3), which is periodic and reserve-capped at `n^{O(1)}` (Cycle100 Lemma 4) — i.e. it is exactly the **charged** branch. A genuine counterpacket would require an *aperiodic* such family, which would simultaneously be a beyond-Johnson superpolynomial-list configuration that survives aperiodic dephasing — the open overlapping-PTE case. So the template confirms: any counterpacket either is periodic (charged, not a counterexample to the aperiodic claim) or *is* the missing overlapping-fiber object.

---

## 6. Replayable checker (for Codex)

Deterministic, `O(C(n,s)·σ)` or via the curve `O(p·σ)`. For primes `p`, `n∣p−1`, `μ_n⊆F_p`, aperiodic random `Uhat`, sweep `σ` fixed and `k=⌈cn⌉` growing:

1. **Collapse check.** Verify `active₁={θ: gcd(B_θ+ψ, X^n−1) has degree s for some degψ≤k−2}` equals `{θ:(g_1(θ),…,g_{σ+1}(θ))∈M_s}` (compute `M_s` once).
2. **Duality check.** Verify `(g_l(θ))∈M_s ⟺ ι(g_l(θ))∈M_m`; assert `ι` is the fixed triangular map (independent of the instance).
3. **k-free wall probe.** Hold `Γ` fixed; sweep `s` and log `|Γ∩M_s|`. Reproducible superpolynomial growth at fixed `Uhat,σ` with `aperiodic=True` ⇒ **counterpacket trigger** (kills the bound); flat `poly(n)` growth ⇒ evidence for the residual lemma.
4. **Charge separation.** For each large fiber, record `min|S̄₁△S̄₂|` (assert `≥2(σ+2)`) and whether it is coset/nested-swap-generated (periodic ⇒ charged) vs overlapping (the dangerous case).

`PASS` = collapse + duality hold and growth is `poly` on all aperiodic samples.

---

## Self-audit

**1. Proved vs not proved.** *Proved:* the `k`-independent collapse (Lemma C) — bandwidth-`k` activity is `|Γ∩M_s|` for one fixed degree-`(σ+1)` curve `Γ⊆A^{σ+1}`, so the `C(n,k)` factor is a union-bound artifact; the complement duality `M_s=ι^{-1}(M_m)` via a fixed triangular automorphism, giving WLOG `s≤n/2`; and the regime fact that `σ=o(n)` puts the radius beyond Johnson. *Not proved:* the uniform `n^{O(1)}` bound itself; I reduce it to the `s`-uniform aperiodic incidence wall.

**2. Prize-relevant or research-only.** The collapse and duality are prize-relevant upper-side structure (they make the named numerator `|Θ_U|` a single `k`-free incidence and subsume Cycle103/104). They do not by themselves close the wall or merge any ledger; they are bankable reductions, not the prize theorem.

**3. First line that could fail.** The chain is exact through §2. It first becomes conjectural at §4: the existence of a `k`-free `Ψ(θ)` of degree `poly(n)` on `Θ_U` for aperiodic `Uhat`. §3 shows this step *cannot* be filled by any unconditional/list-generic method — it must invoke aperiodicity — so a proof that does not use the reserve is the precise failure mode to avoid.

**4. q_gen, q_line, q_code, q_chal, 2^{−128}.** Correctly **not invoked**. This is single-field (`p=q_gen=q_line=q_code=q_chal`, `n∣p−1`) upper-side structure on `|Θ_U|`; no `2^{−128}` crossing asserted; the statement is `p`-uniform and composes safely with any later `q`-instantiation. Ledgers stay unmerged.

**5. Could quotient/periodic, contained incidences, same-slope collisions, or affine color normalization reduce the numerator?** They can only shrink the truth, never invalidate the bound. `θ=−e_1(S̄)−u_1` is the affine-normalized invariant, so distinct points ↔ distinct `θ` (color normalization absorbed; contained/same-slope collisions only merge `θ`-values, deflating fibers `F(θ)`). Periodic `Uhat=U^*(X^d)` is exactly the resonant/charged branch of §3,§5 and is where superpolynomial lists (the beyond-Johnson danger) live; it is charged, not a counterexample to the aperiodic claim.

**6. If PLAN, what converts it.** §1–§3 are PROOF. The residual wall (§4) converts to **PROOF** via a single `k`-independent subresultant/Wronskian determinant on `Γ` of degree `poly(n,σ)` vanishing on `Θ_U` (equivalently, porting the Cycle100 aperiodic-dephasing cap from the weighted `N` to the distinct support), or to **COUNTERPACKET** via an *aperiodic* overlapping-PTE family realizing `e_2=⋯=e_{σ+1}=0` with superpolynomially many distinct `e_1` — found by checker step 3/4, never by a periodic coset-swap family (which is reserve-capped and charged).

**Route to a full solution?** Yes in principle, and now `k`-uniform: the target is no longer "`k` separate problems" but the single incidence `|Γ∩M_s|` of one fixed degree-`(σ+1)` curve. The sharpest next step is the residual lemma — a `k`-free eliminant-degree bound for the aperiodic moment-curve / multiplicative-subgroup symmetric-prefix incidence — together with the explicit recognition (§3) that it must, and may, consume the reserve.