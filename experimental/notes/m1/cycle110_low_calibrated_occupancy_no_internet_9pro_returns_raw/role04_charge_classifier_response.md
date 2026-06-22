I'll start by reading the file index and the core project files to understand the current state.I'll read the core state files and the canonical tracker first to understand the exact definitions and current board.Let me read the canonical tracker, the role prompts for my role (04 Charge Classifier), and the most relevant Cycle109 responses.Let me read my role prompt and the most relevant Cycle109 responses in parallel.The Role 03 response gives me the core construction. Let me read the counterpacket hunter, AP_corr/charge, q-ledger, and referee synthesis responses to understand both sides.This is very informative. Let me read the AP_corr/charge classifier (Role 06), q-ledger (Role 07), and the referee synthesis (Role 09) responses.Let me read the q-ledger closer (Role 07), referee synthesis (Role 09), and the full prover (Role 01).Let me read the full stratified prover (Role 01), the q-ledger closer (Role 07), and the Cycle109 audit in parallel.I have a strong understanding now. Let me read the q-ledger closer (Role 07) and the Cycle109 audit to confirm the budget facts before synthesizing.Let me read the remaining key context: the Cycle109 interior cover audit, the BALANCED Mobius-jet (Role 04), and the HIGH transverse (Role 05) responses.EXACT_NEW_WALL
(with three embedded BANKABLE_LEMMA results: LOW robust‑noncontainment vacuity, the residue‑image reduction, and the single‑mechanism collapse of the uncharged residual)

I read the Cycle110 state, the canonical tracker, and the Cycle109 returns from Roles 01, 02, 03, 06, 07, 09 plus the interior‑cover audit. No internet was used.

## 1. Executive verdict and confidence

There is a route to a full solve of the LOW branch, but it is conditional and the conditioning step is exactly the wall. The route is not a bare `|Z_t| ≤ n^C` cap — that target is false (Role 03's lower bound) and miscalibrated. The correct LOW alternative is a calibrated occupancy cap at scale `q_line · 2^{−Γ₀}`, where `Γ₀` is the entropy reserve. The next exact lemma is the matching residue‑collinearity upper bound, cleanest at `t = 1`.

What I prove here (bankable):
- the contained AND delete‑`j` charges are vacuous for all `j ≤ σ−t` in intrinsic LOW data, so for `t < σ` the delete‑one charge contributes zero;
- the LOW slope set is exactly an intersection of a residue image with one line: `|Z_t| = |Img ∩ K·[B]_E|`;
- after the structural charges are applied, the genuinely uncharged LOW residual collapses to exactly one mechanism — non‑fibered residue collinearity at the locator‑prefix scale — and its main term sits at the occupancy fraction `C(n,a)/q^σ = 2^{−Γ₀}`, not at any `n^{−C}`.

What I cannot prove (the wall): the upper bound matching Role 03's lower bound on that one surviving mechanism. AP_corr's power against the overlapping‑locator‑trade is unknown; this is precisely where a counterpacket can live.

Confidence: high on the vacuity lemma, the residue‑image reduction, and the calibration; high that the surviving mechanism is the unique uncharged one; moderate that the occupancy upper bound is true rather than refutable.

Notation throughout: `K = K_line`, `q = q_line`, `a = k+σ`, `A_E = K[X]/(E) ≅ K^t`, `[·]_E` reduction mod `E`, `deg B < t`, `[B]_E ≠ 0`. Entropy reserve `Γ₀ := σ·log₂ q_gen − log₂ C(n,a)`.

## 2. Charge classification — mechanical predicates for LOW

Each predicate is stated on a witnessed slope `z` with a chosen witness `(Q_z, S_z)`, `deg Q_z < k+t`, `Q_z|_{S_z} = w`, `|S_z| = a`, `Q_z ≡ z·B (mod E)`. Distinct slopes are counted in `K`; same‑slope collisions are pre‑collapsed.

1. Endpoint. `z ∈ Z_t^end` iff its canonical witness degree drops under the official endpoint‑first partition (a forced root at the distinguished boundary coordinate). Cap `c_end ≤ 1` (banked Cycle108).

2. Contained. `z ∈ Z_t^cont` iff `∃ G, deg G < k, EG + B ≡ 0 on S_z`. Predicate is decidable by one interpolation + degree test.

3. Delete‑`j`. `z ∈ Z_t^{del,j}` iff `∃ G, deg G < k, ∃ S' ⊆ S_z, |S'| ≥ a−j, EG+B ≡ 0 on S'`.

4. Tangent. `z ∈ Z_t^tan` iff the agreement of `Q_z` with `w` on `S_z` carries a Hasse‑derivative (higher‑order) coincidence, i.e. the CA‑visibility/MCA‑badness gap of X1. This is a CA→MCA bridge term, not a residue‑line slope event.

5. Quotient / periodic / hidden‑action‑rank. `z` is charged iff there is a source‑visible rational `R = P/Q` (`Q` invertible on `D` and mod `E`) with generalized action rank `d_R(E) := dim_K K[R(ξ)] < t` (`ξ = [X]_E`), and `B, w, {L_{S_z}}` lie in `U·K[R(ξ)]` after an allowed gauge; or there is a proper quotient `K ≤ H` with `K`‑periodic templates `Q_K` and `S_z = Q_ξ △ E_z`, `|E_z| ≤ A` absolute, the tag `(τ,K,ξ,E_z)` fixing `z` injectively with no free `K_line` label. Cap `Σ_K T_K·B_A(n)`, `B_A(n)=Σ_{j≤A}C(n,j) ≤ (A+1)n^A` (banked Roles 02, 06).

6. Field‑confinement. `z ∈ Z_t^field` iff `Z_t^free ⊆ a'·K' + b'` for a proper subfield `K' ⊊ K`, tag `(a',b',K')` retained. Empty when `K` is prime.

7. Affine‑color. `z ∈ Z_t^color` iff `z` lies in one of `c` support‑dependent affine classes `ν_τ(z)=a_τ z + b_τ`, `a_τ ≠ 0`, tag `τ` retained. A fixed affine bijection is cardinality‑preserving and reduces nothing; only a certified `c`‑color/coset union with bounded per‑class content reduces the count.

8. Normalization. `z ∈ Z_t^norm` iff `z` is removed by a vanishing denominator, degenerate Möbius/jet determinant, zero affine coefficient, normalization pole, or loss of same‑field injectivity. Tag retained.

9. Uncharged LOW residual `Z_t^free`: everything not assigned above.

## 3. Proofs

### 3.1 LOW robust‑noncontainment: contained and delete‑`j` are vacuous for `j ≤ σ−t` (BANKABLE_LEMMA)

Let `z ∈ Z_t`, witness `(Q_z,S_z)`. Suppose `G`, `deg G < k`, and `S' ⊆ S_z`, `|S'| ≥ a−j`, with `EG + B ≡ 0` on `S'`. Then
`deg(EG+B) ≤ max(t+(k−1), t−1) = k+t−1`,
while `EG+B` vanishes on `|S'| ≥ k+σ−j` points. A polynomial of degree `≤ k+t−1` vanishing on `≥ k+t` points is identically zero, and
`k+σ−j ≥ k+t ⟺ j ≤ σ−t`.
Hence for `j ≤ σ−t`, `EG+B ≡ 0`, i.e. `E | B`. But `0 ≠ B`, `deg B < t = deg E`, contradiction. So `Z_t^{del,j} = ∅` for every `j ≤ σ−t`; in particular `Z_t^cont = Z_t^{del,1} = ∅` whenever `t < σ`. ∎

Consequence: LOW data carry a noncontainment robustness radius `σ−t ≥ 1`. The contained/delete‑one ledger slots are provably zero in LOW and need no cap. Tangent (X1) is the only non‑quotient "incidence" term, and it is carried at the CA→MCA bridge with the floor `⌊δn⌋/q`, not in the residue‑line slope count, because LOW agreement is simple (multiplicity‑one) on distinct points of `D`.

### 3.2 Residue‑image reduction (BANKABLE_LEMMA)

Let `L_t(w) = {Q : deg Q < k+t, agr_D(Q,w) ≥ a}` (the shifted RS list of `RS[K,D,k+t]` at slack `σ−t`) and `Img = {[Q]_E : Q ∈ L_t(w)} ⊆ A_E`. Then
`z ∈ Z_t ⟺ z·[B]_E ∈ Img`,
and since `[B]_E ≠ 0` the map `z ↦ z[B]_E` is an injection `K ↪ K·[B]_E`. Therefore
`|Z_t| = |Img ∩ K·[B]_E|`.
LOW is exactly: how many residues of the slack‑`(σ−t)` list lie on the fixed line `K·[B]_E ⊆ A_E ≅ K^t`. (Injectivity `z ↦ Q_z` of Role 01/09 is the special case projecting to one witness.) ∎

### 3.3 Collapse of the uncharged residual to one mechanism

Run the general LOW datum through §2 using §3.1:
- contained, delete‑one: empty (§3.1);
- tangent: not a residue‑line slope event (§3.1 remark);
- endpoint: `≤ 1`;
- quotient/periodic/HAR: any family whose supports are a bounded‑defect perturbation of a single map's fibers, or descend to `d_R(E) < t`, is paid with a polynomial cap (Roles 02, 06). This includes every punctured `X^M`‑fiber and full‑fiber packet (`d_R(E)=1`);
- field‑confinement, affine‑color, normalization: tagged, cardinality‑honest.

What is left in `Img ∩ K·[B]_E` is exactly the part that is non‑fibered (full action rank `d_R(E)=t` for every source‑visible `R`) and not a bounded‑defect periodic perturbation. By Role 02 §3.8 the only construction that produces such residues is the overlapping locator trade: a locator‑prefix fiber whose `E`‑residues are forced collinear with `[B]_E` without descending to any bounded‑profile quotient algebra. Role 03 builds exactly this family and certifies the residues are noncontained, nontangent, intrinsic‑degree‑`t`, and same‑slope‑deduplicated. So the uncharged LOW residual equals the non‑fibered residue‑collinearity count, and nothing else survives. ∎

### 3.4 Calibration: the residual is at occupancy scale, not `n^{−C}` (route correction)

Role 03's prefix‑fiber + difference‑signature construction (codimension `(σ−t) + (t−1) = σ−1`, same‑field) yields, after collapsing same‑slope collisions,
`|Z_t^free| ≳ ½ · min( L₀ , (q−n)/(k+t−1) )`, `L₀ = ⌈C(n,a)/q^{σ−1}⌉`,
and `C(n,a)/q^{σ−1} = q·(C(n,a)/q^σ) = q·2^{−Γ₀}` (same field). Therefore:
- a `|Z_t| ≤ n^C` cap is false once `Γ₀ = O(log n)` and `q` is large (then `q·2^{−Γ₀} = q/poly(n) ≫ n^C`);
- the prize fraction `|Z_t|/q` lands at `2^{−Γ₀}`, so the LOW budget `q/2^128` is met iff the corrected reserve furnishes `Γ₀ ≳ 128`.

So the only admissible positive LOW statement is the calibrated occupancy form, with the reserve doing the work — exactly as the Role 03 audit demanded and the bare‑`n^C` audit forbade.

## 4. The exact new wall

`L-CYCLE110-LOW-RESIDUE-COLLINEARITY-OCCUPANCY-CAP`

Let `(E,B,w)` be intrinsic LOW over `K_line`, `1 ≤ t < σ`, above corrected reserve `Γ₀`, satisfying source AP_corr, with every source‑visible `R` of full action rank `d_R(E)=t` and no bounded‑defect periodic descent. Then there exist absolute `C, C₀` (independent of `k, σ, t`) with
`|Z_t| = |Img ∩ K·[B]_E| ≤ C · C(n,a) / (q_gen^{σ−t} · q_line^{t−1}) + n^{C₀}`,
i.e. as a fraction of `q_line`, `|Z_t|/q_line ≤ C · C(n,a)/(q_gen^{σ−t} q_line^{t}) + n^{C₀}/q_line`. Same field: `|Z_t| ≤ C·q_line·2^{−Γ₀} + n^{C₀}`.

The mixed denominator `q_gen^{σ−t} q_line^{t−1}` (prefix coordinates over `K_gen`, residue/collinearity coordinates over `K_line`) is the natural constraint count but is itself an unproved transfer; it must not be silently flattened to `q_gen^{σ−1}` or `q_line^{σ−1}`. This carries the q‑ledger separation: `q_gen` pays prefix entropy, `q_line` counts slopes, `q_chal` is absent.

Matching counterpacket target

A growing official LOW family `(D_i,k_i,σ_i,K_{line,i},E_i,B_i,w_i)`, `t_i < σ_i` intrinsic, above corrected reserve, source AP_corr passing, with all charges of §2 absent or below cap and full action rank, for which the non‑fibered collinear residue count satisfies
`|Img_i ∩ K·[B_i]_{E_i}| > C·C(n_i,a_i)/(q_{gen,i}^{σ_i−t_i} q_{line,i}^{t_i−1}) · ω(1)` and exceeds `⌊q_{line,i}/2^128⌋`.
By §3.4 the prefix‑fiber family already reaches the occupancy scale; a counterpacket must beat it — show the overlapping‑locator‑trade produces super‑occupancy collinearity while staying full‑rank and AP_corr‑clean.

## 5. Verification requirements

A Cycle110 LOW checker must:
- record `q_gen, q_code, q_line, q_chal` with explicit embeddings; count `Z_t` as distinct `K_line` scalars (collisions collapsed); reject any `q_chal`/`q_code` substitution for `q_line` absent a transfer theorem.
- certify the datum: `E(x)≠0` on `D`, `deg E = t` intrinsic (not padded), `0≠B`, `deg B < t`, `[B]_E ≠ 0`.
- verify §3.1 vacuity by checking `σ−t ≥ 1` (then contained/delete‑one slots forced to 0, not merely unfilled).
- compute `Img ∩ K·[B]_E` for any finite instance and emit it as the LOW object; verify each surviving residue is non‑fibered (`d_R(E)=t` for the source‑visible `R` list) and not bounded‑defect periodic (`|E_z| > A`), else route to the quotient/HAR cap.
- evaluate, not name, the §2 predicates; retain every support‑dependent tag.
- check the integer ledger `2^128 · M_led ≤ q_line` with the LOW term entered as `C·C(n,a)/(q_gen^{σ−t}q_line^{t−1}) + n^{C₀}`, never as `n^C` alone.

A finite checker can confirm an instance or finite cap; it cannot establish the uniform `C, C₀` or the field transfer.

## 6. Next exact lemma or construction

Attack `t = 1` first, where `A_E = K` and the line is all of `A_E`, so the wall is unobstructed by the collinearity coordinates:

`L-CYCLE110-T1-EXTERNAL-OCCUPANCY-LOCAL-LIMIT`. For `E=(X−β)`, `β ∉ D`, `Z_1 = {Q(β)/B(β) : Q ∈ L_1(w)}`, so `|Z_1| = |{Q(β) : Q ∈ L_1(w)}|`, the occupied‑color count at one external point of the slack‑`(σ−1)` list of `RS[K,D,k+1]`. Prove
`|{Q(β):Q∈L_1(w)}| ≤ C·C(n,a)/q_gen^{σ−1} + n^{C₀}`
with `C,C₀` absolute, for non‑fibered AP_corr data above corrected reserve. This is the generalized‑Jacobian thickened‑fiber occupancy estimate that Role 03/Role 05 flagged as unbanked; it is the minimal true statement that converts the LOW branch to PROOF at `t=1`.

Then for general `t`: bound `|Img ∩ K·[B]_E|` via the Roth–Ruckenstein bivariate list curve `P(X,Y)` (`deg_Y P = |L_t(w)|`) reduced mod `E` — the lemma is that the `Y`‑roots collinear with `[B]_E` are controlled by `deg_X P` and the action rank, capping collinear residues at the prefix scale `C(n,a)/(q_gen^{σ−t}q_line^{t−1})`. A refutation of this curve‑reduction bound is the counterpacket.

## Mandatory self‑audit

1. Proved: contained/delete‑`j` (`j ≤ σ−t`) vacuity for LOW; `|Z_t| = |Img ∩ K·[B]_E|`; the uncharged residual collapses to the single non‑fibered residue‑collinearity mechanism; its main term is `C(n,a)/q^{σ−1} = q·2^{−Γ₀}`, so `n^C` is false. Not proved: the matching upper bound on that mechanism (the cap in §4), the field‑transfer formula, the `t=1` occupancy local limit, and hence the LOW branch closure or its refutation.

2. Official‑prize‑relevant: yes. The objects are over the actual line field `K_line`, the residue datum is the official normal form, and the calibration is tied to the `q_line/2^128` budget via `Γ₀`. It is not a finite/model certificate and not a prize proof; the §4 wall and §6 lemma are research targets.

3. First failure line: "uncharged, full‑action‑rank, AP_corr LOW datum ⟹ `|Img ∩ K[B]_E| ≤ C·C(n,a)/(q_gen^{σ−t}q_line^{t−1}) + n^{C₀}`." Everything before it (vacuity, reduction, collapse, lower bound) holds; this upper bound is unproven and is exactly where the overlapping‑locator‑trade may break it.

4. Fields and `2^{−128}`: used correctly. `q_gen` carries prefix/reserve entropy (`Γ₀`, the `q_gen^{σ−t}` factor); `q_line` is the sole slope denominator and the only field in `⌊q_line/2^128⌋`; the residue/collinearity coordinates contribute `q_line^{t−1}`; `q_code` has no denominator role; `q_chal` is unused (no protocol transfer invoked). The mixed factor `q_gen^{σ−t}q_line^{t−1}` is explicitly flagged unproved, not collapsed.

5. Numerator reductions: contained/delete‑one removed by proof (zero, not capped); tangent moved to the X1 bridge term; quotient/periodic/HAR and fibered/full‑fiber packets paid with polynomial caps (Roles 02, 06); field‑confinement and affine‑color reduce only with retained tags and certified coset structure; same‑slope collisions pre‑collapsed in `|Z_t| = |Img ∩ K[B]_E|`. None silently discarded. The only term not reducible by any of these is the non‑fibered collinear residue count — the wall.

6. This is not a PLAN. To convert to PROOF: prove §6's `t=1` occupancy local limit, then the general curve‑reduction collinearity cap of §4, then enter the LOW term in the §5 ledger and verify `2^128·M_led ≤ q_line`. To convert to COUNTERPACKET: instantiate §4's matching target with a full‑rank, AP_corr‑clean, charge‑free family whose collinear residue count beats the occupancy scale and exceeds `⌊q_line/2^128⌋`.