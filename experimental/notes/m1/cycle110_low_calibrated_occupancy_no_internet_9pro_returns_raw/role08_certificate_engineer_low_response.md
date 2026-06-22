I'll start by reading the file index, then the project state files and the packet context.I'll read the key context files: the current cycle state, the prior referee synthesis, and the canonical tracker.Let me read the referee synthesis, the canonical tracker, and the project state files in parallel.Now the prior-cycle role responses and the canonical tracker. Let me read the most load-bearing ones in parallel.This is a deep, multi-cycle research problem. Let me read the canonical tracker plus the counterpacket-hunter, AP_corr, and q-ledger role responses to anchor the exact definitions.Let me read the AP_corr/charge role, the q-ledger role, the role01 prover, and the canonical tracker to anchor the exact definitions and prior caps.Let me read the q-ledger closer, the role01 prover, and the canonical tracker. These anchor the exact budget and prior caps.Let me read the role01 full prover and the canonical tracker to anchor the LOW-specific state and definitions.Let me read the canonical tracker, the interior stratified cover audit, and the certificate engineer response together.I have a strong picture. Let me read the two remaining technical roles (balanced, high), the interior cover audit, and the Role 08 certificate engineer materials to ground the harness deliverable and avoid contradicting banked results.BANKABLE_LEMMA

(Embedded: one EXACT_NEW_WALL, one conditional ROUTE_CUT, plus the Role‑08 checker spec and Role‑09 referee synthesis the fused prompt asks for. No PROOF, no COUNTERPACKET — and I will say exactly why neither is justified.)

I read the Cycle110 state, the Cycle109 roles 01/02/03/06/07/09, the interior‑cover audit, and the canonical tracker. Everything below is pure reasoning on the attached packet; no external sources.

## 1. Executive verdict and confidence

There is a route to a full solve of the LOW branch, but it does not close in this round. The correct next step is not "bound the shifted list." It is to recognize that the LOW count is **exactly** a line‑intersection of a residue image, and that the only remaining freedom an adversary has is a single, namable codimension. I prove the exact occupancy identity, show that linear algebra alone is circular (so the bound must come from reserve or charge), and reduce the surviving counterpacket space to exactly two mechanisms.

- Occupancy identity (Lemma A) and explained‑support form (Lemma B): confidence very high — elementary algebra, each step checked.
- Circularity route‑cut (Obs. C): high.
- Reserve‑absorption arithmetic (D) and the localization of the surviving counterpacket: arithmetic certain; applicability conditional on the calibrated upper bound, which I flag explicitly as unproved.
- This is official‑route relevant (it is stated over `K_line` on the official residue datum), not a finite/model certificate. It is not a prize proof and not a counterpacket.

## 2. Exact statements

Fix `K = K_line`, `q = q_line = |K|`, `D ⊂ K` with `|D| = n`, code `C = RS[K,D,k]`, `σ ≥ 1`, `a = k+σ ≤ n`, and `1 ≤ t < σ`. Let `(E,B,w)` be the official intrinsic LOW datum: `deg E = t`, `E(x) ≠ 0 ∀x∈D`, `B ≢ 0 (mod E)`. Write

```
A_E := K[X]/(E)         (dim_K A_E = t)
Bbar := B mod E ≠ 0
ℓ := K·Bbar = { z·Bbar : z ∈ K }   (the slope line: a 1-dim K-subspace, q points)
L_t(w) := { Q ∈ K[X], deg Q < k+t : agr_D(Q,w) ≥ k+σ }       (shifted list)
R_t(w) := { [Q]_E : Q ∈ L_t(w) } ⊆ A_E                        (residue image)
```

**Lemma A (exact LOW occupancy identity).** The map `z ↦ z·Bbar` is a bijection `Z_t(E,B,w) → R_t(w) ∩ ℓ`. Hence
```
|Z_t(E,B,w)| = | R_t(w) ∩ ℓ |.
```
The LOW distinct‑slope count is exactly the number of occupied points of the residue image lying on the fixed slope line `ℓ ⊂ A_E`. This is option‑(1) "residual‑image" made into an equality, with same‑slope collisions already collapsed (the count is of points in `A_E`, not of supports or witnesses).

**Lemma B (explained‑support form).** Let `E_t := { S ⊆ D : |S| = a, w|_S is interpolated by some deg < k+t polynomial }`. For `S ∈ E_t` that polynomial `Q_S` is unique. Then `R_t(w) = { [Q_S]_E : S ∈ E_t }`, so
```
|Z_t| = #{ distinct values [Q_S]_E , S ∈ E_t , that lie on ℓ }.
```
Every occupied slope comes from an `a`‑support whose `w`‑values lie on a degree‑`<k+t` curve (`σ−t` linear conditions) and whose residue then lands on `ℓ` (a further `t−1` conditions inside the `t`‑dimensional `A_E`). Total deficiency `(σ−t)+(t−1) = σ−1`. This is the exact source of the "occupied‑color scale `~ C(n,a)/q^{σ−1}`" that Role 03 hit from below.

**Observation C (linear‑algebra is circular — a route‑cut on "more identities").** Fix any `z_0 ∈ Z_t` with witness `Q_0`, and a lift `β` of `Bbar` with `deg β < t`. Every witness satisfies `Q_i = Q_0 + (z_i−z_0)β + E·R_i` with `deg R_i < k`. Putting `φ := (w−Q_0)/E`, `ψ := β/E` on `D`, agreement of `Q_i` with `w` on `S_i` is equivalent to
```
R_i agrees with  φ − (z_i−z_0)·ψ  on S_i, |S_i| = a, deg R_i < k.
```
So `Z_t` is, verbatim, the bad‑slope set of the line `(φ, −ψ)` for the **same** code `RS[K,D,k]` at the **same** agreement `a`, with `ψ` of intrinsic degree `t`. The LOW problem maps to itself under an affine reparametrization. Consequence: no purely linear/interpolation manipulation can lower the count; the bound must come from the reserve (entropy) or from an official charge. This cuts the family of "rearrange the witnesses" attacks.

**Arithmetic D (reserve absorption of the occupancy main term).** As reals, for any `M ≥ 0`,
```
M ≤ q^σ · 2^{-128}   ⇒   M / q^{σ−1} ≤ q · 2^{-128}.
```
Apply with `M = C(n, k+σ)`: a corrected reserve carrying a ≥128‑bit margin, `C(n,k+σ) ≤ q_gen^{σ}·2^{-128}`, in the typed same‑field regime `q_gen = q_line = q`, forces the occupancy main term `C(n,a)/q^{σ−1} ≤ q_line·2^{-128}`.

**EXACT_NEW_WALL — `L-CYCLE111-LOW-COLLINEARITY-CODIMENSION-OR-FIELD-TRANSFER`.** Prove one of:
- (calibrated upper bound) absolute `C_low` with `|Z_t| ≤ C_low·( C(n,a)/q_line^{σ−1} ) + n^{C_low}`, constants independent of `k,σ,t`; equivalently, the `t−1` collinearity conditions of Lemma B are non‑degenerate unless a quotient/periodic/field charge is present; or
- (collinearity‑codimension charge) `|Z_t| > C_low·C(n,a)/q_line^{σ−1} + n^{C_low}` produces a mechanically stated quotient/periodic, field‑confinement, or affine‑color charge; or
- (cross‑field transfer) when `q_gen < q_line`, an explicit predicate transferring the `q_gen`‑reserve to the `q_line`‑denominator (see §5), without which Arithmetic D does not apply.

## 3. Proofs

**Lemma A.** Injectivity of `z ↦ z·Bbar`: if `z·Bbar = z′·Bbar` in `A_E` then `(z−z′)Bbar = 0`; `z−z′ ∈ K` is a scalar and `Bbar ≠ 0` as a vector of the `K`‑space `A_E`, so `z = z′`. (Note: `E` need not be squarefree and `Bbar` need not be a unit; only `Bbar ≠ 0` is used.) Membership: `z ∈ Z_t` iff some `Q ∈ L_t(w)` has `Q ≡ zB (mod E)`, i.e. `[Q]_E = z·Bbar`, i.e. `z·Bbar ∈ R_t(w) ∩ ℓ`. The bijection follows, giving the cardinality equality. ∎

**Lemma B.** If `Q ∈ L_t(w)` with agreement set `T`, `|T| ≥ a`, pick any `a`‑subset `S ⊆ T`; then `Q|_S = w|_S`, so `S ∈ E_t`. Uniqueness: two degree‑`<k+t` polynomials matching `w` on `S` agree on `|S| = a ≥ k+t` points, hence are equal; so `Q_S = Q` and `[Q]_E = [Q_S]_E`. Conversely `S ∈ E_t ⇒ Q_S ∈ L_t(w)` (agreement `≥ a`). Thus `R_t(w) = {[Q_S]_E}`, and intersect with `ℓ` by Lemma A. The deficiency count: "`w|_S` on a degree‑`<k+t` curve" is `a−(k+t) = σ−t` conditions; "`[Q_S]_E ∈ ℓ`" is `t−1` conditions in `A_E ≅ K^t`. ∎

**Observation C.** Modulo `V_0 := {E·R : deg R < k}` (which is `ker([·]_E` on `V_{<k+t})`), `A_E ≅ V_{<k+t}/V_0`, and each `Q_i ↦ z_i·Bbar` lies on the line `ℓ`. So `Q_i − Q_0 − (z_i−z_0)β ∈ V_0`, giving `Q_i = Q_0 + (z_i−z_0)β + E R_i`. Dividing the agreement equation `Q_i = w` on `S_i` by `E` (nonzero on `D`) yields `R_i = φ − (z_i−z_0)ψ` on `S_i`. Since `deg R_i < k`, this is exactly badness of slope `z_i−z_0` for the line `(φ,−ψ)` over `RS[K,D,k]` at agreement `a`. `ψ = β/E` has intrinsic denominator degree `t` when `gcd(β,E)=1`. ∎

**Arithmetic D.** Divide `M ≤ q^σ 2^{-128}` by `q^{σ−1} > 0`. ∎

**Why this localizes the counterpacket (conditional).** Role 03's lower bound realizes `|Z_t| ≳ C(n,a)/q^{σ−1}` in the same field. Its mechanism is capped above by the prefix‑fiber size `C(n,a)/q^{σ−t}` and, after the collinearity reduction (which costs the `q^{t−1}` of Lemma B's `t−1` conditions), by the scale `C(n,a)/q^{σ−1}`. By Arithmetic D, in the same‑field regime with ≥128‑bit reserve margin this scale is `≤ q_line·2^{-128}` — i.e. **the locator‑prefix/residue‑collinearity family cannot be a same‑field counterpacket against the `q_line` budget unless it beats its own collinearity codimension `q^{t−1}`**. Hence the surviving counterpacket space is exactly: (a) a cross‑field family `q_gen ≪ q_line` riding an unproven transfer; or (b) a family realizing more than `C(n,a)/q^{σ−1}` distinct collinear residues, i.e. beating the `t−1` codimension. This is a precise narrowing, not a closure: the matching **upper** bound `|Z_t| ≤ C·C(n,a)/q^{σ−1}` is unproved, because degenerate alignment (many supports forced onto `ℓ`) is precisely the quotient/periodic/field charge.

## 4. Verification requirements (and Role‑08 LOW checker spec)

A sound finite LOW checker `CHECK-CYCLE110-LOW-OCCUPANCY.v1` must, for a finite official instance:

1. Field ledger: record `q_gen,q_code,q_line,q_chal` with explicit embeddings; verify every slope and every normalization coefficient is in `K_line`; refuse `q_chal` as a denominator absent a transfer receipt.
2. Datum: verify `deg E = t`, `E(x)≠0 ∀x∈D`, `Bbar = B mod E ≠ 0`; certify intrinsic degree `t` (not a padded presentation, e.g. via `n > k+2t−2` as in Role 03 Step 4), not merely `deg E = t`.
3. Exact `Z_t` extraction: build `A_E`, the line `ℓ = K·Bbar`; enumerate explained supports `E_t`, form `[Q_S]_E`, intersect with `ℓ`; emit `Z_t` as **canonical `K_line` representatives, globally deduplicated** (Lemma A guarantees `|Z_t| = |R_t ∩ ℓ|`).
4. Same‑slope dedup: confirm distinct supports with equal `[Q_S]_E` contribute one slope.
5. Charge classification where checkable: endpoint (`c_end ≤ 1`); contained (a degree‑`<k` explanation on the active support — degree argument shows LOW witnesses with `Bbar≠0` are noncontained, so this should be empty); quotient/periodic and field/affine‑color via the collinearity‑degeneracy test of Lemma B; retain every support‑dependent normalization tag.
6. Numerator accounting: compute the integer `|Z_t|` and the candidate cap; do **not** sum LOW over `t` blindly — the q‑ledger needs `⋃_t L_t`, and `max_t` only if strata are exclusive.
7. Terminal labels (cannot overclaim):

```
LOW_CERTIFIED_FOR_INSTANCE       -- |Z_t| extracted, all charges classified, |Z_t| ≤ stated cap
UNPAID_LOW_RESIDUAL              -- occupied collinear residues with no separator and no valid charge
FIELD_LEDGER_MISMATCH           -- a slope/coeff/denominator uses the wrong field
MODEL_ONLY_STRESS_FAMILY        -- growing finite family; reserve/AP_corr not source-certified
SOURCE_VALID_LOW_COUNTERPACKET  -- requires the external receipts below
```

Promotion receipts to lift `MODEL_ONLY_STRESS_FAMILY → SOURCE_VALID_LOW_COUNTERPACKET`: (i) a formal source `AP_corr` predicate evaluated true (not "non‑pullback denominator," not a density test); (ii) the corrected‑reserve inequality with its explicit margin and `q_gen` value; (iii) negative certificates for endpoint, quotient/periodic, contained/delete‑one, tangent, field, affine‑color, hidden‑action‑rank, normalization charges, each at `K_line` slope level; (iv) for cross‑field, the §5 transfer theorem; (v) the integer witness `|Z_t| > ⌊q_line/2^128⌋` or `> n^C` for the targeted `C`. A finite pass certifies an instance only; it cannot establish the uniform `C_low`.

## 5. Next exact lemma / construction (and Role‑09 referee synthesis)

Strongest source‑valid theorem actually proved this round: **Lemma A + Lemma B** (exact LOW occupancy = line‑intersection of the residue image; option‑(1) target reduced to an exact finite geometry). Strongest route cut: **Observation C** (LOW is closed under affine self‑reduction, so no further linear‑algebra identity can produce the cap). No source‑valid counterpacket exists; the locator‑prefix family is *not* promotable, because Arithmetic D shows it is within the `q_line` budget in the same‑field reserve regime, and cross‑field it lacks the transfer.

Exact next constructions for Cycle111, in order:

1. `L-CYCLE111-LOW-COLLINEARITY-NONDEGENERACY`: prove the `t−1` collinearity conditions of Lemma B cut the explained‑support set by a factor `≥ q^{t−1}/n^{C}` unless the residue map `S ↦ [Q_S]_E` factors through a proper quotient algebra of `A_E` (the hidden‑action‑rank / field‑confinement charge of Role 02/06). This is the matching upper bound; combined with a `σ−t` slack bound on `|E_t|` it gives `|Z_t| ≤ C(n,a)/q^{σ−1}·n^{C}`, then Arithmetic D closes same‑field.
2. `L-CYCLE111-FIELD-TRANSFER-PREDICATE` (predicate, state visibility): define `AP_corr^{xfer}` = "the explained‑support residue map and the reserve both descend to `K_gen`, and `ℓ ∩ R_t` injects into a set already counted over `K_gen`." State it as a **new strengthened hypothesis** (it is not source‑visible today). Without it, the mixed scale `q_gen^{σ−t}·q_line^{t−1}` flagged by Role 03 is the natural — but unproved — denominator.
3. Counterpacket attempt to falsify (1): build a family beating collinearity codimension, i.e. `> C(n,a)/q^{σ−1}` distinct collinear residues with full action rank `d_R(E)=t` (Role 02's "non‑fibered, full‑action‑rank, bounded‑overlap locator trade"), corrected reserve with margin, and all charges absent. If it exists, it is the genuine LOW counterpacket; if every such attempt collapses to `d_R(E)<t`, lemma (1) is true.

Referee strictness notes honored: distinct slopes counted in `K_line` (Lemma A); support multiplicity collapsed; quotient/periodic and affine‑color enter only as the collinearity‑degeneracy charge; tangent/contained excluded by the degree argument for `Bbar≠0`; support‑dependent normalization keeps its tag; this is a **calibrated occupied‑color cap**, never a pure `n^C` LOW cap. `q_chal` is untouched. The target as stated in the common prompt is correct; I have only made its option (1) exact and named the precise missing inequality.

## Mandatory self‑audit

1. **Proved vs not.** Proved: `|Z_t| = |R_t(w) ∩ ℓ|` (Lemma A); `R_t(w) = {[Q_S]_E : S∈E_t}` with `Q_S` unique (Lemma B); the affine self‑reduction (Obs. C); the absorption arithmetic (D). Not proved: the calibrated upper bound `|Z_t| ≤ C·C(n,a)/q^{σ−1}+n^C`; the collinearity‑nondegeneracy charge; the cross‑field transfer; any final `N_off ≤ ⌊q_line/2^128⌋`.
2. **Relevance.** Official‑prize relevant (stated over `K_line` on the official residue datum, distinct slopes in `K_line`). Not a prize proof; not a counterpacket; not a finite/model‑only certificate (Lemmas A/B are uniform algebra).
3. **First failure line.** The reduction first becomes non‑rigorous at "the `t−1` collinearity conditions are non‑degenerate," i.e. the step from Lemma B's deficiency count `σ−1` to an actual upper bound. Degenerate alignment is exactly the uncharged danger; this is the `L-CYCLE111` wall, and it is where Arithmetic D's applicability is currently assumed rather than proved.
4. **Field / `2^-128` use.** `q_line` is the sole slope denominator and the count field; `q_gen` carries only the reserve; `q_code` plays no denominator role; `q_chal` is unused (no transfer invoked). Arithmetic D is stated in the **typed same‑field** regime `q_gen=q_line=q` (an identified equality, not a collapse); cross‑field is explicitly deferred to predicate (2). The `2^-128` target enters only through the comparison `C(n,a) ≤ q^σ 2^{-128} ⇒ main term ≤ q_line 2^{-128}`.
5. **Could the named structures reduce the numerator?** Yes, and only at the `K_line` slope level: same‑slope support collisions are already collapsed by Lemma A; contained/tangent are absent for `Bbar≠0` (degree argument); quotient/periodic, field‑confinement, and affine‑color enter precisely as degeneracy of the `t−1` collinearity conditions (the `L-CYCLE111` charge) and must be charged there, not silently dropped; LOW/BAL/HIGH combine by `max` over exclusive intrinsic strata, with paid branches union‑bounded.
6. **PLAN→PROOF/COUNTERPACKET converter.** This is a BANKABLE_LEMMA plus an EXACT_NEW_WALL, not a PLAN. It becomes PROOF on proving `L-CYCLE111-LOW-COLLINEARITY-NONDEGENERACY` (matching upper bound) and, where `q_gen<q_line`, `L-CYCLE111-FIELD-TRANSFER-PREDICATE`, then discharging Arithmetic D into the official `q_line`‑ledger. It becomes COUNTERPACKET on a growing official LOW family with full action rank `d_R(E)=t`, corrected reserve margin, all charges absent, and `>C(n,a)/q^{σ−1}` distinct collinear residues — i.e. one that provably beats the `q^{t−1}` collinearity codimension.