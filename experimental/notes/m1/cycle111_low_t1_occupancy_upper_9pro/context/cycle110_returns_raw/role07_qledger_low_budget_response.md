I'll start by reading the file index and key project files to understand the current state.I'll read the key context files to understand the current state of the LOW branch.Let me read the role-specific files most relevant to my task (q-ledger LOW budget) and the synthesis.Now let me read the cycle110 role prompt for my task, plus the LOW-specific role responses and synthesis.Let me read the LOW residual image (role03), AP_corr descent (role06), the synthesis (role09), and the counterpacket hunter (role02).Let me read the synthesis, counterpacket hunter, and AP_corr descent responses in parallel.Let me read the AP_corr descent, full prover, and certificate engineer responses in parallel.Let me read the remaining key responses: full stratified prover (role01), balanced Mobius (role04), high transverse (role05), certificate engineer (role08), and the canonical tracker.Let me read the remaining context: certificate engineer, the interior stratified cover audit, and the canonical tracker (key sections), plus the balanced/high responses.Let me read the canonical tracker (key sections) and the balanced/high responses to complete my picture.BANKABLE_LEMMA

## 1. Executive verdict and confidence

I can build the exact LOW q-ledger and derive the precise field inequality the LOW branch must satisfy. The result is a closed, two-sided budget statement, not a full prize proof: the lower side (necessity) is rigorously forced by the banked Role 03 residue-line slicing construction; the upper side (sufficiency) is conditional on the still-open calibrated-occupancy cap.

The key finding is that the LOW distinct-slope **main term is not the residual list size**. The shifted list at residual slack `σ−t` has scale `C(n,a)/q_gen^{σ−t}` (reserve does not transfer), but the *distinct-slope* image collapses by a further `t−1` collinearity coordinates counted in `q_line`, giving a main term whose budget condition is governed by the product `q_gen^{σ−t} q_line^{t}`. In the same-field case this product is `q^σ` for every `t`, so the LOW branch demands exactly the `2^128`-scaled σ-reserve — no more, no less. LOW is therefore a *calibrated main-term branch*, consistent with Role 03's correction that a bare `|Z_t| ≤ n^C` target is miscalibrated.

Confidence: high on the budget arithmetic and the field discipline; high that the binding constraint is the `t=1` end in the extension case; the fit-or-fail dichotomy is exact, conditional on whether Role 03's locator-prefix family is officially uncharged.

Official-prize-relevant as a source-level field-ledger reduction. Not a finite/model certificate; not a completed proof.

## 2. Exact ledger statement

`L-CYCLE110-LOW-QLEDGER-BUDGET`

Field roles (no collapse):
- `q_gen` = generated/entropy field, pays the locator-prefix coordinates `σ−t`;
- `q_code` = code alphabet; enters slope counting **only** through `D ⊆ K_code` and scalar-extension new-root effects (Role 07 Route cut 3); never a denominator;
- `q_line` = `|K_line|`, the field of distinct slopes and the **sole** security denominator;
- `q_chal` = challenge field; absent a protocol-transfer theorem it pays nothing.

Per official line instance the intrinsic degree `t = τ(g)` is fixed, but the bad-slope set partitions by degree, `B_off = ⊔_t B_off^{(t)}`, so the LOW count is a **sum**:
```text
N_LOW = sum_{t=1}^{sigma-1} |B_off^{(t)}|.
```

Banked LOW main term (mixed field), distinct in `K_line`, support-collisions already collapsed:
```text
M_LOW(t)  ~  C(n, k+sigma) / ( q_gen^{sigma-t} * q_line^{t-1} ).
```

Budget the prize imposes, `N_LOW <= floor(q_line / 2^128)`:
```text
2^128 * sum_{t=1}^{sigma-1} M_LOW(t)  <=  q_line.            (BUDGET)
```

Exact sufficient field lower bound (per-t form of (BUDGET)):
```text
for every 1 <= t < sigma:
    q_gen^{sigma-t} * q_line^{t}  >=  2^128 * (sigma-1) * C(n, k+sigma).   (LOW-FIT)
```

The binding constraint is the `t` minimising the product `q_gen^{σ−t} q_line^{t} = q_gen^σ (q_line/q_gen)^t`:
- same field `q_gen=q_code=q_line=q`: product `= q^σ` for all `t`, giving the clean budget
  ```text
  q^{sigma}  >=  2^128 * (sigma-1) * C(n, k+sigma);            (SAME-FIELD)
  ```
- extension `q_line >= q_gen` (the F1/line-decoding case): increasing in `t`, binding at `t=1`:
  ```text
  q_gen^{sigma-1} * q_line  >=  2^128 * (sigma-1) * C(n, k+sigma);   (EXT, t=1 binds)
  ```
- contracted `q_line <= q_gen`: binding at `t = σ−1`: `q_gen * q_line^{sigma-1} >= 2^128 (sigma-1) C(n,a)`.

Equivalent entropy-margin form. Define the LOW security margin
```text
Gamma_LOW := min_{1<=t<sigma} [ (sigma-t) log2 q_gen + t log2 q_line ]
             - log2 C(n,k+sigma) - log2(sigma-1).
```
Then (LOW-FIT) ⇔ `Gamma_LOW >= 128`.

Charge-cap alternative. If the official charges (quotient/action-rank, periodic, tangent, field-confinement, affine-color) absorb the locator-prefix family, the free residual obeys `|Z_t^free| <= n^{C_low}` and LOW fits under the far weaker polynomial field bound
```text
q_line  >=  2^128 * (sigma-1) * n^{C_low}.                   (CHARGED-FIT)
```

## 3. Proof of the ledger and derivation of the main term

Necessity (field lower bound) — proved modulo "construction is officially admissible." Role 03's `L-CYCLE109-LOW-RESIDUE-SLICING-RETAINS-OCCUPANCY` constructs, in the same field, an intrinsic degree-`t` datum `(E,1,w)` with
```text
|Z_t| >= ceil( L_0 / (1 + lambda_t (L_0 - 1)) ),   L_0 = ceil( C(n,a) / q^{sigma-t} ),
```
and for `t=1`, `|Z_1| >= (1/2) min{ L_0, (q-n)/k }`. The three cost layers are exact: the locator-prefix fiber spends `σ−t` coordinates (Step 1, buckets in `K_gen`), the vector-collision census deduplicates same-slope supports (Step 2, `c_same=0`), and forcing the `t`-dimensional residue onto one scalar line spends `t−1` coordinates counted in `K_line` (Step 3). Net codimension `(σ−t)+(t−1)=σ−1`, hence the mixed-field main term
```text
M_LOW(t) ~ C(n,a) / ( q_gen^{sigma-t} q_line^{t-1} ).
```
Above reserve `L_0 < (q−n)/k`, so the `t=1` capacity cap is inactive and `M_LOW(1)=L_0`. Therefore an admissible official LOW instance realises `|B_off^{(t)}| >= M_LOW(t)` distinct `K_line`-slopes, and `N_off >= M_LOW(t)`. The prize bound `N_off <= floor(q_line/2^128)` then **forces** `q_gen^{σ−t} q_line^{t} >= 2^128 C(n,a)` (drop the `(σ−1)` since this is a single `t`). So (LOW-FIT) is a *necessary* field lower bound whenever the family is uncharged. ∎ (conditional clause: admissibility under AP_corr / charges).

Sufficiency (budget closes LOW) — conditional on the calibrated cap. By the Role 01/09 injection `z ↦ Q_z` (`B≠0 mod E` ⇒ injective; automatic noncontainment), `|Z_t| <= |L_t(w)|`, but that is the *list*, not the calibrated cap. **Assume** the target cap `|Z_t^free| <= M_LOW(t) + n^{C_low}` with `C_low` absolute. Summing the partition and applying (LOW-FIT) per `t`,
```text
2^128 N_LOW <= 2^128 sum_t (M_LOW(t)+n^{C_low})
            <= 2^128 (sigma-1)(M_LOW(t*) + n^{C_low}) <= q_line,
```
where `t*` is the binding degree; the last step is exactly (LOW-FIT) together with (CHARGED-FIT). Since the official experiment samples `theta ~ Unif(K_line)`, `Pr[bad] = N_off/q_line <= 2^{-128}`. ∎ (conditional on the cap).

Why the (σ−1) factor and not a max. The intrinsic degree is a property of the *slope*, so distinct bad degrees contribute disjoint slope sets and `N_LOW` is a genuine sum over `1 ≤ t < σ` (this is the H4 "sum, not max" point from Role 07 — and it is unavoidable here because, unlike the LOW/BAL/HIGH stratification across the whole experiment, the LOW interior is itself stratified by `t`). The `(σ−1)` is therefore a real ledger cost, absorbed cleanly by demanding the per-`t` form of (LOW-FIT).

Field-discipline checks. The entropy exponent `σ−t` sits on `q_gen`; the slope/denominator exponent `t` and the final denominator sit on `q_line`; `q_code` never enters the count; `q_chal` is unused. No field is substituted into `floor(q_line/2^128)`.

## 4. Verification requirements

A source-valid LOW ledger certificate must:
1. record `q_gen, q_code, q_line, q_chal` with explicit embeddings, and verify every counted slope and every normalization coefficient lies in `K_line`;
2. confirm the experiment samples `Unif(K_line)`, denominator exactly `q_line`;
3. for the realised instance, certify the intrinsic degree `t = τ(g)` (not a padded presentation) and assign each bad slope to its degree class;
4. either (a) produce the calibrated occupancy cap `|Z_t^free| <= M_LOW(t)+n^{C_low}` with an explicit absolute `C_low`, or (b) emit, for every slope above that cap, a mechanically checkable charge (quotient/action-rank with full-rank test `d_R(E)=deg E`, periodic, tangent, field-confinement, affine-color) with its exact distinct-slope cap and retained chart tag;
5. compute the integer test literally: `2^128 * (sum_t (cap_t)) <= q_line`, using (LOW-FIT) at the binding `t*`;
6. confirm the corrected reserve actually *implies* (LOW-FIT); a reserve stated only as `q^σ >= C(n,a)` (no `2^128` and no `(σ−1)`) is insufficient and must be flagged.

A finite checker can validate a proposed instance, the per-`t` arithmetic, and the binding-`t` selection, but cannot establish `C_low` or the universal cap.

## 5. Next exact lemma / obstruction

Exact parameter obstruction (counterpacket window). LOW **cannot** fit, and Role 03's family is a genuine counterpacket, exactly when both hold:
```text
(i)  exists 1 <= t < sigma with
        C(n, k+sigma)  >  q_gen^{sigma-t} * q_line^{t} / 2^128      (reserve below LOW-FIT)
(ii) that t is realised by an official datum passing AP_corr with all
     charges (quotient/action-rank d_R(E)=deg E, periodic, tangent,
     field, affine-color) absent.
```
Equivalently `Gamma_LOW < 128` with the witnessing family uncharged. Because the binding term in the extension case is `t=1`, the sharpest counterpacket target is the `t=1` locator-prefix/residue-collinearity family at margin
```text
log2 C(n,k+sigma)  -  ( (sigma-1) log2 q_gen + log2 q_line )  >  -128.
```

The exact next lemma that converts this BANKABLE_LEMMA into PROOF or COUNTERPACKET:

`L-CYCLE110-LOW-PREFIX-FAMILY-CHARGE-OR-MAIN-TERM`
Decide whether the same-field locator-prefix/residue-collinearity datum of Role 03 (with `M_LOW(t)` distinct `K_line`-slopes, `t=1` first) carries a full-rank failure — i.e. a source-visible rational `R` with `d_R(E) < deg E` after an allowed gauge, or an affine-color/field-confinement cap — under the *frozen* `AP_corr`.
- If always charged: `|Z_t^free| <= n^{C_low}`, LOW closes under (CHARGED-FIT) `q_line >= 2^128 (σ−1) n^{C_low}`, prize-relevant for the calibrated-occupancy path.
- If some instance is uncharged: it is a source-valid LOW counterpacket whenever the official reserve sits in window (i)–(ii); the prize then **requires** the reserve be strengthened to (LOW-FIT)/`Gamma_LOW >= 128`.

Either outcome is decisive; the q-ledger is now reduced to this single algebraic charge test.

---

## Mandatory Self-Audit

1. **Proved vs not proved.** Proved: the exact LOW budget identity `2^128 Σ_t M_LOW(t) <= q_line`, its per-`t` field lower bound (LOW-FIT), the same-field/extension/contracted binding-`t` reductions, the entropy-margin form, and — modulo admissibility of Role 03's construction — the *necessity* of (LOW-FIT). Not proved: the calibrated upper cap `|Z_t^free| <= M_LOW(t)+n^{C_low}` (sufficiency leg), any mixed-field transfer formula beyond the `q_gen^{σ−t}q_line^{t-1}` constraint count (Role 03/09 flag it as unproved), and whether the corrected reserve implies (LOW-FIT).

2. **Relevance.** Official-prize-relevant: stated over `K_line`, denominator `q_line`, target `floor(q_line/2^128)`. Not a finite/model certificate (the main term is an asymptotic family bound), not a completed proof.

3. **First failure line.** `uncharged intrinsic LOW datum at degree t ⇒ |Z_t^free| <= M_LOW(t) + n^{C_low}`. If the locator-prefix family is uncharged and the reserve is below (LOW-FIT) at that `t`, the sufficiency leg fails and the bound becomes a counterpacket. The necessity leg's hidden assumption — that the construction passes AP_corr and dodges the `d_R(E)=1` quotient charge of Role 02 — is the second failure point.

4. **Field / 2^-128 usage.** `q_gen`: entropy only, carries `σ−t`. `q_code`: alphabet; no denominator role; enters only via `D ⊆ K_code` and scalar-extension roots. `q_line`: sole denominator and slope field; carries `t` and the final `/2^128`. `q_chal`: unused (no transfer theorem invoked). The `2^128` appears once, multiplying `N_LOW`, against `q_line`. No collapse.

5. **Numerator-reducing structures.** Same-slope collisions: already deduplicated in `M_LOW` (Role 03 `c_same=0`). Contained/tangent: excluded in the construction by the degree argument (noncontainment automatic). Quotient/periodic/action-rank: *can* remove the entire prefix family if `d_R(E) < deg E` — this is exactly the open charge test and the route to (CHARGED-FIT). Field confinement: caps a branch by a subfield size but leaves the `q_line` denominator unchanged. Affine-color normalization: cardinality-preserving unless support-dependent, in which case its chart tag must be retained (no silent merge). Each can only lower the numerator *with an explicit cap*.

6. **Not a PLAN.** This is a derived ledger lemma plus an exact obstruction window. It converts to PROOF via `L-CYCLE110-LOW-PREFIX-FAMILY-CHARGE-OR-MAIN-TERM` resolving "always charged" (then (CHARGED-FIT) closes LOW); it converts to COUNTERPACKET if that lemma exhibits one uncharged instance inside window (i)–(ii), giving `>= M_LOW(t) > floor(q_line/2^128)` distinct `K_line`-slopes above corrected reserve and AP_corr.