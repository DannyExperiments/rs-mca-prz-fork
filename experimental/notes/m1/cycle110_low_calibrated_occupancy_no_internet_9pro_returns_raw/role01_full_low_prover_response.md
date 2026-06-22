Copy answer
I'll start by reading the file index, then the core project state and the cycle-specific context before attempting the proof.Let me read the cycle110 state file and the most relevant context files directly from the attachment directory.Let me read the key Cycle109 role responses and the canonical tracker, which define the exact objects and prior progress.This role03 response is the core. Let me read the referee synthesis, the q-ledger closer, and the counterpacket hunter to understand the full board.Let me read the counterpacket hunter, the q-ledger closer, and the cycle109 full prover responses to complete my picture of the board.Let me read the q-ledger closer and the full stratified prover from cycle109, plus the canonical tracker definitions.Let me read the canonical tracker for the exact definitions of the field tower, AP_corr, and corrected reserve, plus the AP_corr descent role.Let me read the AP_corr descent role, the role01 prover, and role05/role04 to understand the exact AP_corr predicate and charge definitions.Let me read the remaining key roles: the full stratified prover (role01), the high transverse plane (role05), the balanced mobius jet (role04), and the interior cover audit.I have enough to work with. I've read the LOW residual-image role (03), the referee synthesis (09), the counterpacket hunter (02), the q-ledger closer (07), the full stratified prover (01), the AP_corr/charge role (06), and the canonical tracker. The core banked facts are: the injection `|Z_t| ≤ |L_t(w)|` into the shifted list, the support-packing cap, automatic noncontainment, and Cycle109's claim that the residual slack `σ−t` is a "real" lost margin. Let me work the mathematics directly.

---

BANKABLE_LEMMA

(with an embedded ROUTE_CUT on the "σ−t is a fundamental loss" reading, and an explicit conditional that upgrades to PROOF the moment the base correlated‑agreement bound is supplied)

## 1. Executive verdict and confidence

I did not produce an unconditional source-valid `PROOF`, and I did not produce a `COUNTERPACKET`. I proved an exact reduction that is, I believe, the strongest correct LOW statement and that materially re-bases the wall:

**The intrinsic LOW residue-line slope count is, exactly and over `K_line`, a base reserve‑σ correlated-agreement (MCA) bad‑slope count for a fixed rational word pair — not a residual-slack‑`(σ−t)` list problem.**

Concretely, `|Z_t(E,B,w)|` equals the number of `λ ∈ K_line` for which `φ − λψ` is `(k+σ)`-close to `RS[K_line,D,k]`, where `ψ = B/E` is the intrinsic line direction and `φ = (w−Q_0)/E`. The denominator code has dimension `k`, and the agreement surplus is the **full** reserve `σ`, with `t` appearing only in the choice of the word pair.

Consequences:
- The `σ−t` "lost margin" that Cycle109 (role03/role09) treated as a genuine obstruction is an artifact of the lossy injection `Z_t ↪ L_t(w)`. The slope **image** is governed by reserve `σ`, not slack `σ−t`. (ROUTE_CUT on that reading.)
- LOW is not downstream of a new "occupied-color" theorem. It is an **instance of the base M1 wall** (M1-C106), at reserve `σ`, with a structured low-complexity direction `ψ = B/E`. The "calibrated occupancy bound" of target (1) is exactly the base correlated-agreement count `≈ q_line/2^{Γ_0}`.
- Every official charge (endpoint/quotient/periodic/contained/tangent/field/affine-color/hidden-action/normalization) transfers between the two sides through a single affine-color tag `λ ↦ z_0+λ`, so no charge is created or destroyed.

Confidence: **high** on the exact equality and its proof (it is elementary polynomial division over `K_line`); **high** that this dissolves the `σ−t` framing; **high** that it does not by itself prove the prize numerator (the base bound is the prize core and remains open).

This is official-prize-relevant structural progress over `K_line`, not a finite/model certificate, and not a prize proof.

## 2. Exact theorem statement

Let `K = K_line`, `q = q_line = |K|`, `D ⊆ K` with `|D| = n`, `a := k+σ ≤ n`. Fix an intrinsic LOW residue datum `(E,B,w)`:
```
1 ≤ t < σ,   deg E = t,   E(x) ≠ 0 ∀ x∈D,   B ≢ 0 (mod E),   w : D → K.
```
WLOG replace `B` by `B mod E`, so `deg B < t` and `B ≠ 0` (this does not change any class `zB mod E`). Define
```
Z_t = { z ∈ K : ∃ Q ∈ K[X], deg Q < k+t, agr_D(Q,w) ≥ a, Q ≡ zB (mod E) }.
```
Introduce the per-coordinate **rational words** on `D` (well-defined since `E(x) ≠ 0`):
```
ψ(x) := B(x)/E(x),     and, after fixing one z_0 ∈ Z_t with witness Q_0,
φ(x) := (w(x) − Q_0(x))/E(x).
```
Define the **base reserve‑σ correlated-agreement bad-slope set** of the pair `(φ,ψ)` for the dimension-`k` code:
```
Λ_{k,σ}(φ,ψ) = { λ ∈ K : ∃ R ∈ K[X], deg R < k, agr_D(R, φ − λψ) ≥ a }.
```

**Theorem (LOW residue line = base correlated agreement).**
If `Z_t = ∅` the count is `0`. Otherwise, for any fixed `z_0 ∈ Z_t`,
```
Z_t(E,B,w) = z_0 + Λ_{k,σ}(φ,ψ),     hence   |Z_t(E,B,w)| = |Λ_{k,σ}(φ,ψ)|,
```
an exact equality of subsets of `K_line`. The code dimension is `k` and the agreement surplus is `σ` (not `σ−t`). The intrinsic denominator degree `t` enters only through the word pair `(φ,ψ)`; the direction `ψ = B/E` is the intrinsic line direction `−g`.

**Corollary (calibration).** The Cycle109 same-field lower construction `|Z_t| ≳ \binom{n}{a}/q^{σ−1}` is exactly the calibrated base count: with `Γ_0 := σ\log_2 q_gen − \log_2\binom{n}{a}` (the corrected-reserve entropy margin), `\binom{n}{a}/q^{σ−1} = q/2^{Γ_0}` in the same-field case `q_gen=q_line=q`. So target (1)'s "calibrated occupancy main term," with constants independent of `k,σ,t`, is precisely `|Λ_{k,σ}| ≈ q_line/2^{Γ_0}`, inherited verbatim from the base problem.

**Conditional PROOF statement.** If the base bound
```
(★)  for the pair (φ, ψ=B/E),  |Λ_{k,σ}(φ,ψ)| ≤ M(n)   [or ≤ ⌊q_line/2^128⌋ under corrected reserve]
```
is supplied with `M` independent of `k,σ,t` (this is exactly M1-C106 / `W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE` specialized to the rational direction `B/E`), then `|Z_t| ≤ M(n)` with the **same** constant and **no** `σ−t` penalty, closing the LOW branch and fitting the `q_line`-ledger.

## 3. Proof

Assume `Z_t ≠ ∅`; fix `z_0 ∈ Z_t` and a witness `Q_0` (`deg Q_0 < k+t`, `agr_D(Q_0,w) ≥ a`, `Q_0 ≡ z_0 B mod E`).

**Step 1 — normal form of every witness.** Let `z ∈ Z_t` with any witness `Q_z`. Put `λ = z − z_0`. Since `deg B < deg E = t`, the element `λB` is already reduced mod `E`, so
```
[Q_z − Q_0]_E = (z − z_0)[B]_E = [λB]_E   ⟹   E | (Q_z − Q_0 − λB).
```
Now `deg(Q_z − Q_0 − λB) < k+t` (each term has degree `< k+t`; `deg λB < t`). Dividing by `E` (degree `t`):
```
R_z := (Q_z − Q_0 − λB)/E ∈ K[X],   deg R_z < (k+t) − t = k.
```
Thus **every** LOW witness has the form `Q_z = Q_0 + λB + E·R_z` with `R_z ∈ RS[K,D,k]` (degree `< k`). This is where `t` is absorbed: the residue constraint plus the degree bound force the free part to be a genuine degree-`<k` codeword.

**Step 2 — agreement is preserved coordinatewise.** For `x ∈ D` (so `E(x) ≠ 0`):
```
Q_z(x) = w(x)
 ⟺ Q_0(x) + λB(x) + E(x)R_z(x) = w(x)
 ⟺ E(x)R_z(x) = (w(x) − Q_0(x)) − λB(x)
 ⟺ R_z(x) = φ(x) − λψ(x).
```
Hence `agr_D(Q_z, w) = agr_D(R_z, φ − λψ)`. Since `agr_D(Q_z,w) ≥ a`, the codeword `R_z` (degree `< k`) certifies `λ ∈ Λ_{k,σ}(φ,ψ)`. Therefore `z = z_0 + λ ∈ z_0 + Λ_{k,σ}`.

**Step 3 — converse.** Let `λ ∈ Λ_{k,σ}(φ,ψ)` with witness `R` (`deg R < k`, `agr_D(R, φ−λψ) ≥ a`). Set `z = z_0 + λ` and `Q = Q_0 + λB + E·R`. Then `deg Q < k+t` (terms have degrees `< k+t`, `< t`, `< k+t`); by Step 2 (read backwards) `agr_D(Q,w) ≥ a`; and `[Q]_E = [Q_0]_E + λ[B]_E = (z_0+λ)[B]_E = z[B]_E`. So `z ∈ Z_t`.

**Step 4 — bijection.** Steps 2–3 give `Z_t = z_0 + Λ_{k,σ}(φ,ψ)`. Translation by `z_0` is a bijection of `K_line`, so `|Z_t| = |Λ_{k,σ}(φ,ψ)|`. ∎

**Nondegeneracy (why `Λ` is a genuine M1 line, not all of `K`).** The banked noncontainment lemma says no `G` of degree `< k` agrees with `−B/E = −ψ` on `≥ a` points; i.e. `ψ` is itself `not` `(k+σ)`-close to `RS[K,D,k]`. Hence the family `{φ − λψ}` is a genuine affine line transverse to the code (not a constant coset), and `|Λ_{k,σ}|` is exactly the nondegenerate base proximity-gap count. Also `ψ ≢ 0` on `D` (else `D ⊆ roots(B)`, impossible since `deg B < t < n`).

**Charge transfer.** The map `Z_t → Λ` is the fixed affine bijection `z ↦ z − z_0`, a single retained-tag affine-color normalization (`a_τ = 1`). It preserves distinct-slope counts in `K_line` and collapses no collisions. Therefore every official charge stratum of the base pair `(φ,ψ)` pulls back to a LOW charge of the same `K_line` cardinality, and vice versa: endpoint, quotient/periodic, contained (`ψ` or `φ` code-close), tangent, field-confinement, affine-color, hidden-action-rank, normalization — all transfer one-to-one. No charge is created, destroyed, or inflated.

**Consistency checks against the banked board.**
- `t=1`, `E=X−β`, `B=b` constant: `z = Q(β)/b`, so `|Z_1| = #{Q(β) : Q ∈ L_1(w)}` = number of occupied evaluation colors at `β`. This matches role03's `t=1` generalized-Jacobian "occupied thickened color" numerator, and equals `|Λ|` by the theorem. ✓
- Role03's lower bound `\binom{n}{a}/q^{σ−1}` equals `q/2^{Γ_0}`, the calibrated base correlated-agreement scale. The construction is the main term, not a counterpacket — exactly what corrected reserve (`Γ_0 ≥ 128`) is designed to keep below `q/2^{128}`. ✓
- The injection `|Z_t| ≤ |L_t(w)|` (slack `σ−t`) is recovered as a weakening: `Λ_{k,σ}(φ,ψ) ↪ L_t(w)` by `λ ↦ Q_z`. The list is large (slack `σ−t`); its residue-line image `Λ` is governed by reserve `σ`. The `σ−t` loss lives in the injection, not in `Z_t`. ✓

## 4. Verification requirements

A deterministic checker accepting `(K_line, D, k, σ, t, E, B, w, z_0, Q_0, R)` must verify:
1. Field/typing: all of `E,B,w,Q_0,R, z_0` over `K_line`; distinct counts taken in `K_line`.
2. Datum validity: `deg E = t`, `E(x) ≠ 0 ∀x∈D`, `B := B mod E ≠ 0`, `deg B < t`, `1 ≤ t < σ`, `a = k+σ ≤ n`.
3. Base witness: `deg Q_0 < k+t`, `agr_D(Q_0,w) ≥ a`, `Q_0 ≡ z_0 B (mod E)`.
4. Reduction identity: define `φ(x)=(w(x)−Q_0(x))/E(x)`, `ψ(x)=B(x)/E(x)`; check `deg R < k` and `agr_D(R, φ−λψ) = agr_D(Q_0+λB+E·R, w)` for the tested `λ` (this is the per-coordinate identity of Step 2 — an algebraic check, not enumeration).
5. Bijection bookkeeping: emitted `z = z_0 + λ` are pairwise distinct iff the `λ` are; affine-color tag `(τ, a_τ=1, b_τ=z_0)` retained.
6. Nondegeneracy: noncontainment certificate for `ψ` (no degree-`<k` poly agrees with `−ψ` on `≥ a` points).

For official promotion the checker must additionally evaluate the base-side objects: the corrected-reserve inequality on `Γ_0` (using `q_gen`), the source `AP_corr` predicate on the pair `(φ, B/E)`, the base charge certificates, and finally the integer ledger `N_off ≤ ⌊q_line/2^128⌋`. The reduction itself supplies **none** of these; it only certifies that the LOW instance is identical to a base instance, so the base certificates suffice with no `σ−t` correction.

What this lemma does **not** verify: any upper bound on `|Λ_{k,σ}(φ,ψ)|`. That is `(★)`, the base wall.

## 5. Next exact lemma or construction

**`L-CYCLE110-BASE-CA-BOUND-FOR-RATIONAL-DIRECTION` (the converter to PROOF).**
There exists `M(n)`, independent of `k,σ,t`, such that for every official intrinsic LOW datum, the induced pair `(φ, ψ=B/E)` over `K_line` satisfies
```
|Λ_{k,σ}(φ,ψ)| ≤ M(n)         (calibrated form: ≤ ⌊q_line/2^128⌋ under corrected reserve Γ_0 ≥ 128 + O(log n)),
```
or its failure produces a base official charge. This is exactly the active M1 wall `W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE` specialized to the structured direction `ψ = B/E` (a degree-`(<t,t)` rational function — precisely the low-complexity input the M1 aperiodic-incidence/`Γ∩M_s` machinery targets). Proving `(★)` immediately closes LOW via §2's conditional, with the same constant and no `σ−t` penalty.

**Why this is the right next step rather than a new occupancy theorem.** My reduction shows the previously-posited "intrinsic LOW calibrated occupancy theorem" is **not a separate theorem**: it is the base correlated-agreement bound. So effort should fold LOW into M1-C106 (passing `ψ = B/E` as the direction word) instead of opening an independent occupancy track.

**Exact counterpacket mechanism (and why role02 already constrains it).** A LOW counterpacket exists iff a base counterpacket exists with a rational direction `ψ = B/E`, `deg B < deg E = t < σ`, above corrected reserve, all base charges absent, and `|Λ_{k,σ}| >` the permitted `q_line` budget. Role02 already cut the full-fiber/punctured-`X^M` realization of this as action-rank-one (a quotient charge). So any LOW counterpacket must be **non-fibered, full-action-rank** on the base side — the overlapping-locator-trade target role02 isolated — now with the extra constraint that its direction is the low-degree rational `B/E`.

---

# Mandatory Self-Audit Addendum

**1. What exact implication did I prove / not prove?**
Proved (exactly, over `K_line`): `Z_t(E,B,w) = z_0 + Λ_{k,σ}(φ, B/E)`, hence `|Z_t| = |Λ_{k,σ}|`, with surplus the full reserve `σ`, uniform in `t`, with one-to-one charge transfer. Not proved: any upper bound on `|Λ_{k,σ}|` (the base correlated-agreement numerator), the field transfer in the mixed-field reserve, or the final `q_line/2^128` inequality. So I proved "LOW ≡ base MCA," not "base MCA is small."

**2. Official-prize-relevant or only model/research?** Prize-relevant and source-level: the construction is over `K_line` with official residue-line/noncontainment objects, and it re-bases an active prize branch. It is not a finite/model certificate and not a prize proof.

**3. First line where it could fail.** Not in §3 (elementary division; airtight). The first place the *program* can fail is `(★)`: `|Λ_{k,σ}(φ, B/E)| ≤ M(n)` or charge. Equivalently, the base proximity-gap/correlated-agreement count for the rational direction `B/E` at reserve `σ` and precision `2^{-128}` — the prize core. Secondarily, in mixed fields, the reserve hypothesis `Γ_0` mixes `q_gen` (entropy) and `q_line` (count); the reduction is field-clean (an identity over `K_line`), but `(★)`'s reserve must be the base problem's own, not a silent `q_gen↔q_line` swap.

**4. Are `q_gen,q_line,q_code,q_chal,2^-128` used correctly?** Yes. The equality and the count `|Z_t|=|Λ|` are entirely in `K_line` (denominator `q_line`). `q_gen` enters only via the corrected-reserve margin `Γ_0` and the calibrated main term `q_line/2^{Γ_0}`. `q_code` plays no denominator role; `q_chal` is unused (no protocol transfer invoked). The target remains `N_off ≤ ⌊q_line/2^128⌋`, unchanged and unmet here.

**5. Could quotient/periodic, contained, same-slope, tangent, field, or affine-color reduce the numerator?** Yes, and they do so identically on both sides because the bijection is a single retained-tag affine map `λ↦z_0+λ` (`a_τ=1`): same-slope collisions collapse equally; contained = `ψ`/`φ` code-close (excluded for genuine LOW by noncontainment of `ψ`); quotient/periodic and hidden-action-rank pull back from the base pair (role02's action-rank-one full-fiber charge transfers directly); tangent/endpoint/field/affine-color caps transfer with equal `K_line` cardinality. The reduction neither manufactures nor hides any charge.

**6. If PLAN, what converts it?** This is not a PLAN; it is a proved exact reduction (BANKABLE_LEMMA) plus a ROUTE_CUT. It converts to `PROOF` exactly upon `(★)` = `L-CYCLE110-BASE-CA-BOUND-FOR-RATIONAL-DIRECTION` (M1-C106 with direction `B/E`) plus the existing q-ledger (role07 (3)). It converts to `COUNTERPACKET` exactly upon a non-fibered, full-action-rank base family with direction `B/E`, `deg B < deg E = t < σ`, above corrected reserve, all base charges absent, and `|Λ_{k,σ}|` exceeding the `q_line` budget — the role02 overlapping-locator-trade target, now specialized to a low-degree rational direction.