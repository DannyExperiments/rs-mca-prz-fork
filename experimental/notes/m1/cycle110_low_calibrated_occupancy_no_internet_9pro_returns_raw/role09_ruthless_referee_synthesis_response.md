I'll start by reading the file index, then the key project and packet files.I'll read the core state files first, then the cycle109 responses that bear directly on the LOW branch.Let me read the project anchor files and the most decision-relevant cycle109 responses in parallel.The referee synthesis gives me the exact wall. Let me read the most relevant role responses: the residual-image route (role03), the counterpacket hunter (role02), the AP_corr/charge analysis (role06), and the q-ledger closer (role07).Let me read the remaining decisive responses: the AP_corr/charge descent (role06), q-ledger closer (role07), full prover (role01), and the two returns audits.I have the core picture. Let me read the two returns audits, the full prover (role01), and grep the canonical tracker for the official AP_corr and reserve definitions.I have the full picture of the LOW branch. Let me check the canonical tracker and the cycle108 adapter audit for the exact official definitions of AP_corr, corrected reserve, and the occupancy/inverse theorem, since those determine whether a real proof is reachable.Let me search the canonical tracker for the precise official definitions that determine whether LOW can close: AP_corr, corrected reserve, and the occupancy/inverse theorem.The bash tool isn't available. Let me read the canonical tracker directly to find the official AP_corr, reserve, and occupancy definitions.EXACT_NEW_WALL

I read the packet (CURRENT_CYCLE110_STATE, the cycle109 role responses 01–07/09, the cycle108/109 returns audits, and the canonical tracker rows M1-C105…C110). I did not browse. Below I verify role03's construction, prove a new charge‑vacuity lemma at `t=1`, cut the pure‑polynomial reading, and reduce the first LOW stratum to one explicit honest estimate.

## 1. Executive verdict and confidence

No full solve, and no clean route to one, because the LOW target is not yet a well‑posed implication: `AP_corr` has no frozen noncircular source predicate (role06 proved the "weakest predicate forcing Gate B" is circular). But the branch can be advanced concretely, and I can localize the entire difficulty.

The decisive new finding: **at `t = 1` the quotient / periodic / hidden‑action‑rank charges are structurally vacuous**, so the `t=1` LOW stratum admits no charging escape at all. Its bound is forced to be a bare occupancy/residual‑image estimate. I verify role03's construction is a legitimate uncharged noncontained intrinsic‑degree‑1 MCA instance, which (a) refutes the pure‑polynomial readings of target options 1–2, and (b) ties the prize reserve quantitatively to the occupancy constant. The remaining `t=1` task is an honest list/local‑limit upper bound that no charge can dodge; it is the right linchpin to attack next.

Confidence: high on the `t=1` charge‑vacuity lemma, the slope ↔ subset‑product reformulation, and the route cut (all are short algebra over `K_line` I check below); high that this is the earliest charge‑irreducible obstruction; moderate on whether the `t=1` occupancy upper bound is provable with an absolute constant. This is official‑route‑relevant; it is not a prize proof and not a counterpacket.

## 2. Exact statements

Write `K = K_line`, `q = q_line`, `a = k + σ`, `A_E = K[X]/(E)`.

**Lemma A (t=1 charge‑vacuity).** Let `(E,B,w)` be an intrinsic LOW datum with `t = deg E = 1`, so `E = X − β`, `β ∉ D`, `B ∈ K^×` constant. Then:
- the quotient/periodic charge and the generalized hidden‑action‑rank charge of role02 cannot fire: for every source‑visible rational `R` invertible mod `E`, `d_R(E) = dim_K K[R(ξ)] = 1 = deg E`, never `< t`; and `E = E_0(X^M)` needs `deg E ≥ 2`;
- contained = 0 and tangent absent (role01/role03 noncontainment);
- endpoint contributes `≤ 1`, affine‑color is count‑preserving, field‑confinement reduces only genuinely subfield‑defined instances.

Hence `Z_1 = Z_1^{free} ⊔ (≤1 endpoint)`, and the calibrated theorem at `t=1` is exactly an occupancy upper bound with **no charging degree of freedom**.

**Lemma B (slope ↔ symmetric‑coordinate image).** For the role03 same‑field family (`E = ∏_{i≤t}(X−β_i)` split squarefree, `B` constant, `w = M|_D` with `M` monic of degree `a`), after the signature reduction the slope is the affine‑linear functional
```
z_S = const − Σ_{j=σ}^{a} (−1)^j e_j(S) · ⟨β-powers⟩,
```
of the *high* elementary‑symmetric coordinates `(e_σ(S),…,e_a(S))` of the support. For `t = 1` this is exactly
```
Z_1 ⊇ { M(β) − ∏_{x∈S}(β − x) : S ∈ F },   F = { S ∈ C(D,a) : e_j(S)=c_j, 1≤j≤σ−1 },
```
so `|Z_1|` equals (affinely, hence bijectively) the number of distinct subset products `∏_{x∈S}(β−x)` over the elementary‑symmetric prefix fiber `F`, with `|F| ≥ ⌈ C(n,a)/q^{σ−1} ⌉ =: L_0`.

**Route cut C (pure polynomial is false).** Target options 1 and 2 in their literal "`n^C` independent of `k,σ,t`" / "`n^A` charts × `n^B` slopes" form are refuted: role03's family is a source‑valid, uncharged, noncontained intrinsic‑degree‑1 LOW instance with
```
|Z_1| ≥ ½·min{ L_0, (q−n)/k },   L_0 = ⌈C(n,a)/q^{σ−1}⌉,
```
which exceeds every fixed `n^C` whenever the reserve is only assumed positive (`Γ_0 > 0`) and `q` sits in the window `n^{2C} ≪ q ≤ 2^{n/(σ−1/2)}`. So only option 3 (charge) or the **main‑term‑calibrated** form of option 1 can survive.

**The new wall — L-CYCLE110-LOW-T1-OCCUPANCY-UPPER.** Prove an absolute `C` with: for every `w` and every `β ∉ D`,
```
| { Q(β) : Q∈K[X], deg Q ≤ k, agr_D(Q,w) ≥ k+σ } |  ≤  C · C(n, k+σ) / q_gen^{σ−1}.
```
Equivalently (Lemma B): the single linear functional `(e_σ,…,e_a) ↦ z` has image of size `≤ C·C(n,a)/q_gen^{σ−1}` on every elementary‑symmetric prefix fiber. By Lemma A this is charge‑irreducible, and it is the exact first LOW arrow.

## 3. Proofs / construction

**Lemma A.** `t=1` ⇒ `deg E = 1` ⇒ `A_E = K[X]/(X−β) ≅ K`, evaluation `ξ ↦ β`. For any source‑visible `R = P/Q` invertible mod `E`, `R(ξ) = R(β) ∈ K` is a scalar, so `K[R(ξ)] = K` and `d_R(E) = 1`. Role02's charge fires only when `d_R(E) < deg E = t = 1`, impossible; the rank‑one full‑fiber charge and periodic `E_0(X^M)` (degree `≥2`) likewise cannot occur. Noncontainment: if `G`, `deg G < k`, explained `−B/E` on an `a`‑support, then `EG+B` would have `≥ a` roots while `deg(EG+B) ≤ k+t−1 = k < k+σ = a`, forcing `EG+B≡0`, i.e. `E | B`, contradicting `0 ≠ B`, `deg B < t`. The remaining list members (endpoint `≤1`, affine‑color bijective, field‑confinement only for subfield instances) cannot absorb a generic full‑field noncontained family. ∎

**Lemma B / construction check (verifying role03 over `K_line`).** With `E = X−β`, the bad‑slope condition is `Q(β)=z`, `deg Q ≤ k`, `agr_D(Q,w) ≥ a`. Take `w = M|_D`, `M` monic of degree `a`; for `S` with `L_S = ∏_{x∈S}(X−x)`, set `Q_S = M − L_S`. Leading terms cancel, and `Q_S` has degree `≤ k` iff `M` and `L_S` share their top `σ−1` subleading coefficients, i.e. `e_j(S)=c_j` for `1≤j≤σ−1` (the fiber `F`). On `S`, `L_S=0` so `Q_S = M = w`: agreement `≥ a`. Then
```
z_S = Q_S(β) = M(β) − ∏_{x∈S}(β − x).
```
Collisions `z_S = z_{S'}` ⇔ `β` is a root of `L_S − L_{S'}`, which has degree `≤ a−σ = k` (they share the top `σ−1` coefficients), hence `≤ k` roots; choosing `β` to minimize collisions gives `|Z_1| ≥ L_0/(1+\tfrac{k}{q−n}(L_0−1)) ≥ ½ min{L_0,(q−n)/k}`. This is a genuine MCA line `f=w/E`, `g=−B/E` over `K_line`; the slopes are distinct in `K_line`; same‑slope supports are already collapsed. ∎

**Reserve dichotomy (quantitative).** The prize budget is `⌊q/2^{128}⌋`. The occupancy main term is `≈ L_0 = C(n,a)/q_gen^{σ−1}`. With same‑field `q_gen = q`, requiring `C·L_0 ≤ q/2^{128}` is exactly
```
Γ_0 := σ·log_2 q_gen − log_2 C(n,a)  ≥  128 + log_2 C.
```
So: (i) if "corrected reserve" only means `Γ_0 > 0`, role03's family blows every polynomial and even `q/2^{128}` (it can reach `~q/k` when `Γ_0 = O(log k)`), but those instances sit *below* prize reserve, so they are not prize counterpackets; (ii) under prize‑strength reserve `Γ_0 ≥ 128 + log_2 C` the family fits, but the LOW main term then **saturates the budget to within the occupancy constant** — there is no separate additive `+n^{C_0}` budget on top; the main term essentially *is* the budget. This sharpens role03/role07: the calibrated bound must be `|Z_t| ≤ C·C(n,a)/q_gen^{σ−1}` (charged remainder `O(1)` at `t=1`), and the prize reserve must dominate `128 + log_2 C`.

**Why option 2 also fails.** `~L_0` distinct slopes coming from one linear functional cannot be packed into `n^A` charts of `≤ n^B` slopes once `L_0 ≫ n^{A+B}`; no support‑independent normalization shrinks a single‑functional image. ∎

## 4. Verification requirements

A checker for these results must, over `K_line` only (no `q_gen/q_code/q_chal` substitution):
- replay Lemma B finitely: given `(K,D,k,σ,β,M)`, enumerate `F`, compute `z_S = M(β)−∏_{x∈S}(β−x)`, confirm `deg Q_S ≤ k`, `agr ≥ a`, `Q_S(β)=z_S`, and count **distinct** `z_S` (dedup in `K_line`); compare to `½min{L_0,(q−n)/k}`;
- certify intrinsic degree `t=1` (not a padded presentation) and noncontainment by the degree inequality `k+t−1 < a`;
- assert charge‑vacuity mechanically: `deg E = 1 ⇒ d_R(E)=1`, reject any quotient/periodic/HAR certificate at `t=1`;
- for any claimed prize closure, evaluate the integer `Γ_0` and check `Γ_0 ≥ 128 + log_2 C` with the actual occupancy constant `C`, and `2^{128}·N_off ≤ q_line`.

A finite checker can validate a proposed instance/constant; it cannot establish the universal occupancy exponent.

## 5. Next exact lemma or construction

Two moves, in order:

1. **Prove L-CYCLE110-LOW-T1-OCCUPANCY-UPPER** (the displayed `t=1` bound). Concretely (Lemma B): bound the image of the linear functional `(e_σ,…,e_a) ↦ z` on a prescribed elementary‑symmetric prefix fiber by `C·C(n,a)/q_gen^{σ−1}`. The banked packing/list bound gives only `C(n,a)/C(a,k+1)` (too weak by `q^{σ−1}/C(k+σ,σ−1)`); the missing input is a residue‑collinearity/local‑limit estimate that uses that all `a`‑support interpolants agree at `β`. This is the charge‑free core and the only honest target at `t=1`.

2. **For `t ≥ 2`, freeze `AP_corr` first.** Here `d_R(E) < t` *is* possible, so the LOW set splits into a low‑action‑rank charged part (role02 cap) plus a full‑rank free part governed again by the codimension‑`(σ−1)` occupancy term (the signature step costs `q^{t−1}`, restoring exponent `σ−1` uniformly in `t`). The exact missing object is a noncircular source predicate `AP_corr` plus the inverse lemma `full action rank + no module descent ⇒ occupancy‑scale free image`. Without the `AP_corr` definition this branch is not yet a theorem statement.

The matching counterpacket construction to keep alive: a **non‑fibered, full‑action‑rank** growing family whose high‑symmetric‑coordinate functional has superpolynomial fiber image *under prize‑strength reserve* `Γ_0 ≥ 128 + log_2 C` — i.e. an instance forcing the occupancy constant `C` to grow with `n`. Role03's family does not do this (it respects the main term); a refuter must beat the main term itself.

## Mandatory self-audit

1. **Proved vs not.** Proved: `t=1` charge‑vacuity (Lemma A); slope ↔ subset‑product/symmetric‑coordinate reformulation (Lemma B); verification that role03's family is a source‑valid uncharged noncontained intrinsic‑LOW instance over `K_line`; the route cut on pure‑polynomial options 1–2; the quantitative reserve relation `Γ_0 ≥ 128 + log_2 C`. Not proved: the occupancy upper bound itself (any `t`), the `AP_corr` definition, the `t≥2` charge/free split inverse lemma, field transfer `q_gen → q_line`, and the final `N_off ≤ ⌊q_line/2^128⌋`.
2. **Relevance.** Official‑route‑relevant (actual line field, official residue‑line/noncontainment objects). Not a prize certificate and not a finite/model‑only certificate; the finite role03 instance is used only to cut pure‑polynomial readings, which is a valid route cut, not a counterpacket claim.
3. **First failure line.** `uncharged intrinsic LOW (t=1) ⇒ |Z_1| ≤ C·C(n,a)/q_gen^{σ−1}`. Lemma A removes every charging escape before this line, so it is exactly the first unsupported arrow; for `t≥2` the prior failure is the absence of a frozen `AP_corr`.
4. **Field/`2^{-128}` use.** `q_gen`: reserve/entropy and the `C(n,a)/q_gen^{σ−1}` main term. `q_line`: slope count and sole denominator; role03 same‑field uses `q_gen=q_code=q_line=q` as an explicit typed equality, not a collapse. `q_code`,`q_chal`: unused; `q_chal` would need a protocol‑transfer theorem. Target kept as `2^{128}·N_off ≤ q_line`. The mixed‑field main term `q_gen^{σ−t} q_line^{t−1}` remains an unproved transfer and I did not assume it.
5. **Numerator reductions.** At `t=1`: quotient/periodic/HAR vacuous (proved); contained `=0`; tangent absent; endpoint `≤1`; same‑slope collisions already collapsed in Lemma B; affine‑color count‑preserving; field‑confinement caps only subfield instances (doesn't reach the worst case). So none reduce the generic `t=1` free count below occupancy scale. For `t≥2`, quotient/HAR/field‑confinement can genuinely reduce, but only with explicit caps and a frozen `AP_corr`.
6. **PLAN conversion.** Not a PLAN. To reach PROOF: establish L-CYCLE110-LOW-T1-OCCUPANCY-UPPER with absolute `C`, then freeze `AP_corr` and prove the `t≥2` full‑rank ⇒ occupancy inverse with role02's cap on the low‑rank part, then field transfer and the integer ledger. To reach COUNTERPACKET: a full‑action‑rank non‑fibered family that forces the occupancy constant `C` to grow under reserve `Γ_0 ≥ 128 + log_2 C`.