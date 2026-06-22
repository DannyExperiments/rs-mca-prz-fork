I'll start by reading the file index and key project files before analyzing this LOW list/packing route audit.I'm operating as Role 06 (List/Packing Route Audit). Let me read the cycle state, my specific role prompt, and the most relevant context files.Now let me read the canonical tracker and the most relevant Cycle109 responses for the reserve-transfer question central to my role.Let me read the most relevant Cycle109 responses for the list/packing route — particularly the residual image, AP_corr descent, and q-ledger responses, plus the synthesis.Role 03 directly addresses the reserve-transfer warning. Let me read the AP_corr descent/charge response, the q-ledger response, and the ruthless referee synthesis to complete the picture.This is very rich. Let me read the q-ledger response, the counterpacket hunter, and the synthesis to round out the picture before writing my audit.Let me read the counterpacket hunter and the ruthless referee synthesis to complete the picture.Let me read the synthesis and the interior stratified cover audit to finalize my understanding before writing the Role 06 audit.ROUTE_CUT

(Primary label ROUTE_CUT for the list/packing/sunflower/distance family in the prize regime; it carries one conditional BANKABLE_LEMMA, the Johnson-type packing cap, which closes only the residual-safe subrange.)

## 1. Executive verdict and confidence

Pure list/packing reasoning cannot prove `L-CYCLE110-LOW-CALIBRATED-OCCUPANCY-OR-OFFICIAL-CHARGE`. I can prove exactly one nontrivial thing in this family and I can cut the rest with a precise dividing line.

What survives: a second-moment (Johnson-type) packing bound on distinct LOW slopes that is fully explicit in `k, σ, t`, source-valid, counts in `K_line`, and respects same-slope collisions. It closes the LOW wall (as a clean alternative-(1) occupancy bound) **only** in the Johnson-safe subrange `(k+σ)^2 > n(k+t-1)`.

What is cut: in the complementary super-Johnson regime — which contains the entire constant-rate prize band — pairwise support distance, sunflower structure, constant-weight distance, and list-size alone are provably insufficient. The exact obstruction is that the proven pairwise distance is only the constant `2(σ−t+1)`, and the residue-collinearity constructions (Role 03 / Role 09) realize a constant-weight code of superpolynomial size that satisfies every support constraint, so no support-only argument can separate it from a genuine counterpacket.

Confidence: high on both the conditional packing bound and the impossibility characterization (both are short, self-contained, and verified against the banked injection and lower-bound lemmas). The dividing line `(k+σ)^2 vs n(k+t-1)` is exact.

## 2. Exact statements

Notation: `K = K_line`, `q_line = |K|`, `D ⊆ K`, `|D| = n`, `a = k+σ`, surplus `s = σ−t ≥ 1`, shifted dimension `K_t = k+t`. For each `z ∈ Z_t(E,B,w)` fix one witness `Q_z` (deg `< k+t`, `agr_D(Q_z,w) ≥ a`, `Q_z ≡ zB mod E`) and one size-`a` agreement support `S_z`.

BANKABLE sub-lemma — `L-CYCLE110-LOW-JOHNSON-PACKING-CAP`.

Three valid facts, in increasing strength:

(i) Injection + intersection (re-derivation of the banked Role 09 lemma, used as input): `z ↦ Q_z` is injective, and for `z ≠ z'`, `|S_z ∩ S_{z'}| ≤ k+t−1`, hence `|S_z △ S_{z'}| ≥ 2(σ−t+1)`.

(ii) First-moment (Fisher) cap, unconditional:
```
|Z_t| ≤ C(n, k+t) / C(k+σ, k+t) = C(n, k+σ) / C(n−k−t, σ−t).
```
(iii) Second-moment (Johnson) cap, valid when `(k+σ)^2 > n(k+t−1)`:
```
|Z_t| ≤ n(σ−t+1) / ( (k+σ)^2 − n(k+t−1) ).
```
Corollary (clean exponent): if `(k+σ)^2 − n(k+t−1) ≥ σ−t+1` then `|Z_t| ≤ n`. So in the Johnson-with-margin subrange, `Z_t` satisfies wall alternative (1) with occupancy exponent `1`, independent of `k, σ, t`.

ROUTE_CUT — `L-CYCLE110-LIST-PACKING-INSUFFICIENT`.

If `(k+σ)^2 ≤ n(k+t−1)` (super-Johnson), then every bound derivable from {pairwise support distance, constant-weight distance, sunflower/Δ-system structure, shifted RS list size} is either vacuous or superpolynomial, and therefore cannot certify `|Z_t| ≤ n^{C}` with `C` independent of `k, σ, t`. This regime is nonempty and contains the constant-rate band: with `a = ρn`, `0 < ρ < 1` fixed, `(k+σ)^2 = ρ^2 n^2 < ρ n^2 ≈ n(k+t−1)` for all `t`.

Reserve-transfer identity (exact form of the Cycle109 warning). With generated-field margin `Γ_j = j·log₂ q_gen − log₂ C(n,a)`:
```
Γ_t = Γ_0 − t·log₂ q_gen,    and    max_w |L_t(w)| ≥ ⌈ C(n,a) / q_gen^{σ−t} ⌉.
```
So reserve at `σ` (`Γ_0 > 0`) does not give reserve at the shifted surplus `σ−t` (`Γ_t` can be `< 0`); reserve is consumed at rate `log₂ q_gen` per unit denominator degree.

## 3. Proofs

Injection and intersection (input recap). If `Q_z = Q_{z'}` then `(z−z')[B]_E = 0` in `K[X]/(E)`; `z−z'` is a scalar and `[B]_E ≠ 0` (since `0 ≠ B`, `deg B < deg E = t`), so `z = z'`. For `z ≠ z'`, `Q_z − Q_{z'}` is nonzero of degree `< k+t` and vanishes on `S_z ∩ S_{z'}`, so the intersection has `≤ k+t−1` points. Note this lives entirely on `D`; the residue datum `(E,B)` acts only at the roots of `E`, which lie off `D`, so support combinatorics is blind to it. That is the structural reason packing cannot see collinearity.

First-moment cap. Each `S_z` (size `a`) contains `C(a, k+t)` subsets of size `k+t`; two distinct supports share `≤ k+t−1` points, so no `(k+t)`-subset lies in two supports. Hence `|Z_t|·C(a,k+t) ≤ C(n,k+t)`. The identity `C(n,k+t)/C(k+σ,k+t) = C(n,k+σ)/C(n−k−t,σ−t)` follows from `C(n,k+t)C(n−k−t,σ−t) = C(n,k+σ)C(k+σ,σ−t)` and `C(k+σ,σ−t)=C(k+σ,k+t)`.

Second-moment cap. Let `d_x = #{z : x ∈ S_z}`. Then `Σ_x d_x = a|Z_t|` and `Σ_x C(d_x,2) = Σ_{z<z'} |S_z ∩ S_{z'}| ≤ C(|Z_t|,2)(k+t−1)`. Convexity gives `Σ_x C(d_x,2) ≥ n·C(ā,2)`, `ā = a|Z_t|/n`. Writing `V = |Z_t|`, `λ = k+t−1`:
```
V(a^2 − nλ) ≤ n(a − λ).
```
If `a^2 > nλ`, divide to get `V ≤ n(a−λ)/(a^2−nλ) = n(σ−t+1)/((k+σ)^2 − n(k+t−1))`. ∎ Both caps use only injection, the degree bound, and the proven intersection bound; all are source-valid, count distinct `K_line` slopes, and assign one support per slope (same-slope collisions never enter).

Why the cut is tight (super-Johnson). When `a^2 ≤ nλ` the second-moment inequality is vacuous (nonpositive denominator) and the first-moment ratio `C(n,k+σ)/C(n−k−t,σ−t)` is superpolynomial: with `k+σ = ρn` the numerator is `≈ 2^{H(ρ)n}` while the denominator is `≤ n^{σ−t}`. Crucially this is not mere looseness of the bounds — the banked constructions realize the largeness. Role 03's locator-prefix + difference-signature construction and Role 09's prefix-fiber lower bound produce `|Z_t| ≳ C(n,a)/q^{σ−1}` distinct, noncontained slopes whose supports necessarily obey `|S_z ∩ S_{z'}| ≤ k+t−1` (that bound is a theorem for all distinct slopes). So the constant-weight code with distance `2(σ−t+1)` genuinely attains superpolynomial size; pairwise distance / Johnson / sunflower cannot exclude it. At `t = σ−1` the distance is just `4`, and constant-weight codes of distance `4` are exponentially large, so the distance route dies hardest exactly where the prize regime sits.

Reserve identity. The shifted code has dimension `k+t`, so its agreement surplus over dimension is `a − (k+t) = σ−t`, not `σ`. The locator-prefix counting (record the `σ−t` nonleading coefficients of `L_S`, pigeonhole into `q_gen^{σ−t}` classes) yields `max_w |L_t| ≥ ⌈C(n,a)/q_gen^{σ−t}⌉`; the entropy form is the displayed `Γ_t = Γ_0 − t·log₂ q_gen`. This is the precise mechanism by which `σ`-reserve fails to transfer to `σ−t`.

## 4. Verification requirements

A checker `CHECK-CYCLE110-PACKING-CAP` should accept `(K, D, k, σ, t, {(z, Q_z, S_z)})` and verify: `D` distinct, `E(x)≠0` on `D`, `0≠B`, `deg B < t`; each `deg Q_z < k+t`, `Q_z|S_z = w|S_z`, `|S_z| = a`, `Q_z ≡ zB (mod E)`; the `z` are pairwise distinct in `K_line`; pairwise `|S_z ∩ S_{z'}| ≤ k+t−1`; then compute `(k+σ)^2 − n(k+t−1)` and, if positive, assert `|Z_t| ≤ n(σ−t+1)/((k+σ)^2−n(k+t−1))`, else emit `SUPER_JOHNSON_UNCAPPED`. It must refuse to report a slope cap whenever the denominator is `≤ 0`, and must count slopes (not witnesses or supports). It must not substitute `q_code` or `q_chal` for `q_line` in any probability, and must record the locator-prefix entropy strictly against `q_gen`. The checker certifies an instance; it cannot establish the uniform exponent outside the Johnson-safe range, which is exactly the point of the cut.

## 5. Next exact lemma or construction

The list/packing toolkit is exhausted; progress requires the one thing packing cannot see — control of the residue image on the single ray `K·[B]_E`. The exact next lemma is:

`L-CYCLE110-RESIDUE-RAY-OCCUPANCY`: For an official intrinsic LOW datum with `(k+σ)^2 ≤ n(k+t−1)`, source `AP_corr`, and no paid charge, bound the number of distinct values of `[Q]_E / [B]_E` (the projection of the shifted list `L_t(w)` onto the one-dimensional `K`-subspace `K·[B]_E ⊂ K[X]/(E) ≅ K^t`) by `n^{C}` with `C` independent of `k, σ, t` — or charge the excess.

The missing structure is precisely the `(t−1)`-codimensional collinearity constraint that the difference-signature step (Role 03 Step 3) shows is satisfiable for a `q^{-(t−1)}` fraction. Concretely, the bridge must combine the second-moment support packing above with an evaluation-at-roots-of-`E` incidence count (the `t` evaluations `Q(β_i)` for `β_i` the roots of `E`, off `D`), since collinearity is a condition on those off-`D` evaluations, not on `D`-supports. Equivalently: prove a "supports pack on `D` AND evaluations collide off `D`" joint-incidence bound, or charge the configuration. This is the occupied-color/eliminant content of wall alternatives (1)/(2); no constant-weight, sunflower, Johnson, or shifted-list theorem supplies it.

A counterpacket along this route would require exhibiting the Role 03 prefix-fiber family with the difference-signature collinearity made simultaneous and above corrected reserve, with `q_gen^{σ−t} < C(n,a)`, while clearing quotient/action-rank (the Role 02 cut shows full-fiber inflation is rank-one charged, so the supports must NOT descend to fibers of a single map) — that remains the only uncut mechanism, and it is an algebraic, not a packing, object.

---

## Mandatory Self-Audit

1. Proved: (a) the unconditional Fisher cap `|Z_t| ≤ C(n,k+σ)/C(n−k−t,σ−t)`; (b) the conditional Johnson cap `|Z_t| ≤ n(σ−t+1)/((k+σ)^2−n(k+t−1))` valid iff `(k+σ)^2 > n(k+t−1)`, with corollary `|Z_t| ≤ n` under margin; (c) the exact super-Johnson insufficiency of all support-only methods; (d) the reserve identity `Γ_t = Γ_0 − t log₂ q_gen` with the matching list lower bound. Not proved: any polynomial `|Z_t|` cap in the super-Johnson / constant-rate regime; that is exactly what packing cannot deliver, and I did not prove the residue-ray occupancy lemma that would.

2. Official-prize-relevant. The caps are over the actual `K_line` slope set using only source-valid algebraic facts; the cut is a structural impossibility, not a finite-model observation. It is neither a prize proof nor a counterpacket.

3. First failure line: the implication "`uncharged LOW datum ⇒ |Z_t| ≤ n^C`" fails at the very first step in the super-Johnson regime, where `(k+σ)^2 ≤ n(k+t−1)` makes the second-moment denominator nonpositive and the first-moment ratio superpolynomial; the constructions confirm the failure is real, not an artifact of loose counting.

4. Field ledger: locator-prefix entropy and reserve use `q_gen` only (`Γ_t`, the `q_gen^{σ−t}` lower bound). Distinct slopes and the only probability denominator are `q_line`; the `2^-128` target `N_off ≤ ⌊q_line/2^128⌋` is untouched here and not claimed. `q_code` is not used. `q_chal` is not used (no protocol-transfer theorem is invoked). No collapse of the four fields.

5. Reductions to the numerator: the packing caps are upper bounds, so quotient/periodic, contained/delete-one, tangent, field-confinement, and affine-color structure can only lower the true count — they never invalidate the cap. Same-slope collisions are excluded by construction (one support per distinct slope). None of these mechanisms rescues the super-Johnson regime, because the lower-bound construction already produces distinct, noncontained, nontangent slopes; the only listed mechanism that could absorb that construction is quotient/action-rank (per the Role 02 cut), which is an algebraic charge outside the packing toolkit.

6. Not a PLAN. This is a route cut plus one banked conditional cap. Conversion to PROOF of the full LOW branch requires `L-CYCLE110-RESIDUE-RAY-OCCUPANCY` (§5); conversion to COUNTERPACKET requires the simultaneous-collinearity prefix-fiber family above corrected reserve that also clears the action-rank charge.