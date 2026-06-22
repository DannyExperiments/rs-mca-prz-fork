I'll start by reading the file index and key project files to understand the current state.I'll read the key context files for this LOW calibrated occupancy branch, prioritizing the Role 03 lineage and current state.Let me read the synthesis, q-ledger, and canonical tracker to understand the calibration and the exact ledger constraints.Let me read the counterpacket hunter, AP_corr descent, and the interior stratified cover audit to pin down the exact open arrow.BANKABLE_LEMMA

I read the Cycle110 state, the Cycle109 Role 03 / Role 06 / Role 07 / Role 09 responses, and the counterpacket-hunter cut. The right move on this branch is not to defend `|Z_t| <= n^C`; it is to identify the correct inverse object and prove the bound that object actually obeys. The central new content is an exact reduction of the LOW slope count to an augmented Reed–Solomon list count, which makes the calibration, the `q^{t-1}` gap, the dedup, and the ledger fit all explicit.

## 1. Executive verdict and confidence

The correct LOW occupancy object is not the shifted list `L_t(w)` and not a naive `n^C`. It is the agreement list of a single `(k+1)`-dimensional augmented RS code at reserve `sigma-1`. I prove:

- **Reduction (exact, unconditional).** `|Z_t|` equals the number of distinct codewords of `C^+ = RS[D,k] + K·v` (with `v = B/E` on `D`) that agree with `u = w/E` on at least `k+sigma` points. This is reserve `sigma-1`, not `sigma-t`, and it explains the previously-banked `q^{t-1}` gap as the codimension of the line `K·[B]_E` inside `K[X]/(E)`.
- **Johnson occupancy cap (exact, unconditional, `q`-free).** If `(k+sigma)^2 > (k+t-1)n` then `|Z_t| <= floor( (k+sigma)n / ((k+sigma)^2 - (k+t-1)n) )`.
- **Calibration verdict.** Outside the Johnson regime no `(k,sigma,t)`-uniform polynomial-in-`n` cap can exist (the Cycle109 lower bound already forces `~ binom(n,k+sigma)/q^{sigma-1}` slopes), so the correct main term is the reserve term `binom(n,k+sigma)/q^{sigma-1}`, which is **paid by corrected reserve into the `q_line` ledger**, not bounded by `n`.

Confidence: high on the reduction and the Johnson cap (elementary, checkable); high that this is the correct calibration; the sub-Johnson upper bound itself is **not proved** and is the exact remaining wall (residue equidistribution vs. alignment charge).

This is official-route-relevant structural progress over `K_line`, not a prize proof and not a counterpacket.

## 2. Exact statements

Throughout `K = K_line`, `q = q_line`, `D ⊂ K`, `|D| = n`, `a = k + sigma`, `1 <= t < sigma`. WLOG reduce `B` mod `E`, so `deg B < t = deg E`, `B != 0`. Set `u(x) = w(x)/E(x)`, `v(x) = B(x)/E(x)` for `x ∈ D` (well-defined since `E(x) != 0`). Let `C^+ := RS[D,k] ⊕ K·v` as a space of functions `D -> K`.

**Theorem A — L-CYCLE110-LOW-AUGMENTED-CODE-REDUCTION.**
The map sending a slope `z` to the function `phi = M + z·v` (where `Q = zB + EM`, `deg M < k`, is any witness) is a bijection
```
Z_t(E,B,w)  <->  { distinct z-components of phi in C^+ : agr_D(phi, u) >= a }.
```
Consequently `|Z_t| = #{ z : exists phi in C^+ with v-coordinate z and agr_D(phi,u) >= a }`, an agreement-list count for the dimension-`(k+1)` code `C^+` at reserve `a-(k+1) = sigma-1`. Moreover `C^+` has minimum distance `>= n-(k+t-1)`: two distinct slopes have witness supports meeting in `<= k+t-1` points.

**Theorem B — L-CYCLE110-LOW-JOHNSON-OCCUPANCY-CAP.**
If `(k+sigma)^2 > (k+t-1)·n` then
```
|Z_t| <= floor( (k+sigma)·n / ((k+sigma)^2 - (k+t-1)·n) ).
```
The bound is explicit, independent of `q`, `sigma-t`, the field, and the witness multiplicity. It is `O(n)` whenever `(k+sigma)^2 >= (1+eps)(k+t-1)n`.

**Calibration (replacement for `|Z_t| <= n^C`).** The correct uniform statement is the dichotomy
```
|Z_t| <= max( JohnsonCap ,  ceil( binom(n,k+sigma) / q^{sigma-1} ) ) + N_low^charge,
```
where the first term is active in the Johnson regime and the second is the reserve main term paid by the ledger; `N_low^charge` collects explicitly capped LOW charges (endpoint <=1, quotient/periodic, field-confinement, affine-color, contained/tangent). The genuinely open arrow is the sub-Johnson upper bound, stated in §5.

**Checker target — CHECK-CYCLE110-LOW-AUGMENTED-OCCUPANCY.v1.** Accepts `(K,D,k,sigma,t,E,B,w)` and a claimed slope list with one witness `(z_i, M_i, S_i)` each; verifies `deg E = t`, `E|_D != 0`, `B != 0 mod E`, `deg M_i < k`, `|S_i| >= a`, `M_i + z_i v = u` on `S_i`, pairwise `|S_i ∩ S_j| <= k+t-1`, all `z_i` distinct in `K`; then checks the regime `(k+sigma)^2 > (k+t-1)n` and the Johnson integer cap, or else routes to the sub-Johnson reserve/charge ledger of §5.

## 3. Proofs

**Theorem A.** `z ∈ Z_t` gives `Q`, `deg Q < k+t`, `Q ≡ zB (mod E)`, `agr_D(Q,w) >= a`. Then `Q - zB = E·M` with `M = (Q-zB)/E`; since `deg(Q-zB) <= max(deg Q, deg B) < k+t` and we divide by `deg E = t`, we get `deg M < k`. On the agreement support `S` (`|S| >= a`), `Q(x)=w(x)` and `E(x) != 0` give `M(x) + z·v(x) = u(x)`. So `phi := M + z v ∈ C^+` agrees with `u` on `S`.

*Well-defined `z`-component / injectivity.* `v ∉ RS[D,k]`: if `v` agreed with some `deg<k` poly `N` on all of `D`, then `B - E N` vanishes on `D`, but `deg(B-EN) < k+t <= n` (as `t<sigma` gives `k+t < k+sigma <= n`), forcing `B = EN`, i.e. `B ≡ 0 (mod E)` — contradiction. Hence `RS[D,k] ⊕ K v` is a direct sum of functions on `D`, and each `phi` has a unique `z`-coordinate. So `Z_t` maps onto exactly the set of distinct `z`-coordinates of agreeing codewords. Surjectivity is the reverse of the above computation (`phi = M + zv` agreeing with `u` on `S` gives `Q = EM + zB`, `deg<k+t`, agreeing with `w` on `S`, `Q ≡ zB mod E`).

*Pairwise support bound.* For distinct slopes `z != z'`, pick witnesses; on `S_z ∩ S_{z'}` we have `phi_z - phi_{z'} = 0`, i.e. `(M_z - M_{z'}) + (z-z')v = 0`; multiply by `E`: the polynomial `P := E(M_z-M_{z'}) + (z-z')B` vanishes on `S_z ∩ S_{z'}`, `deg P < k+t`. `P != 0`: else `E(M_z-M_{z'}) = -(z-z')B`, and reducing mod `E` gives `(z-z')B ≡ 0`, impossible since `z != z'`, `B != 0 mod E`. A nonzero `deg<k+t` polynomial has `< k+t` roots, so `|S_z ∩ S_{z'}| <= k+t-1`. ∎

This also recovers and sharpens the banked injection: the residue-line image lives in a dimension-`(k+1)` code (reserve `sigma-1`), whereas `L_t(w)` is the dimension-`(k+t)` list (reserve `sigma-t`). The exact main-term ratio is `q^{(sigma-1)-(sigma-t)} = q^{t-1}`, i.e. the line `K[B]_E` is codimension `t-1` in `K[X]/(E) = K^t`. The `t-1` "extra coordinates" of Cycle109 are now an honest dimension count.

**Theorem B (Johnson / double count).** Let `m = |Z_t|`, supports `S_1,...,S_m`, `|S_i| >= a`, pairwise `|S_i ∩ S_j| <= I := k+t-1`. With `d_x = #{i : x ∈ S_i}`:
```
sum_x C(d_x,2) = sum_{i<j} |S_i ∩ S_j| <= C(m,2)·I,    sum_x d_x = sum_i |S_i| >= m·a.
```
Convexity of `C(·,2)` over `n` points with mean `d_bar = (sum d_x)/n >= ma/n`:
```
n·C(ma/n, 2) <= sum_x C(d_x,2) <= C(m,2)·I
=> (ma/n)(ma - n) <= m(m-1) I
=> a(ma - n) <= (m-1) I n < m I n
=> m(a^2 - I n) < a n.
```
When `a^2 > I n` this gives `m < a n /(a^2 - I n)`, hence `|Z_t| <= floor(a n /(a^2 - I n))`. Substituting `a=k+sigma`, `I=k+t-1`. ∎

**Why no uniform `n^C` below the regime.** The Cycle109 same-field construction produces `~ binom(n,a)/q^{sigma-1}` distinct slopes (already dedup'd at the `K`-slope level). Choosing `q` so that `q^{sigma-1} <~ binom(n,a) < q^{sigma}` (compatible with reserve `q^sigma > binom(n,a)`) makes this superpolynomial in `n` while staying below `a^2 <= (k+t-1)n`. So in the sub-Johnson regime there is provably no `(k,sigma,t)`-uniform polynomial-in-`n` cap; the reserve term is mandatory. This is the precise sense in which `|Z_t| <= n^C` is miscalibrated.

## 4. Verification requirements

- **Algebraic (Theorems A,B):** the checker of §2 is purely polynomial-arithmetic over `K_line`; no field transfer, no `q_gen`/`q_code`/`q_chal`. Same-slope supports collapse automatically because the count is over distinct `z`-coordinates of `C^+` (one codeword per slope). All slopes are in `K_line` by construction.
- **Regime gate:** Theorem B is valid only inside `(k+sigma)^2 > (k+t-1)n`; the checker must verify this strictly before emitting the cap, else route to §5.
- **For official promotion (not done here):** the sub-Johnson upper bound, the residue-alignment charge cap, the corrected-reserve inequality with the `2^128` factor, and the same-field/transfer certificate. The packet still exposes no formally checkable `AP_corr` + corrected-reserve adapter, so no source-valid conclusion attaches to the sub-Johnson branch yet.

## 5. Next exact lemma / construction, and ledger fit

**Q-ledger fit of the main term (so the wall is correctly scoped).** Using the line-level mutual exclusion of LOW/BALANCED/HIGH (Role 09: the ledger uses `max`, not sum), the LOW branch may use the whole `floor(q_line/2^128)` budget. Define the **corrected LOW reserve** as the two explicit inequalities
```
(R1)  q^{sigma} >= 2^{129} · binom(n, k+sigma);
(R2)  q        >= 2^{129} · n^{C_low}.
```
Then `binom(n,a)/q^{sigma-1} = binom(n,a)·q/q^{sigma} <= q/2^{129}` by (R1), and `N_low^charge <= n^{C_low} <= q/2^{129}` by (R2), so the calibrated bound of §2 gives `|Z_t| + N_low^charge <= q/2^{128} = floor-budget`. The main term is therefore **payable, not fatal** — provided the sub-Johnson upper bound holds.

**Exact next wall — L-CYCLE110-LOW-RESIDUE-EQUIDISTRIBUTION-OR-ALIGNMENT-CHARGE.**
In the augmented-code picture, prove: for every official intrinsic LOW datum with corrected reserve and source `AP_corr`, EITHER
```
|Z_t| = #{phi in C^+ : agr_D(phi,u) >= k+sigma}  <=  ceil( binom(n,k+sigma)/q^{sigma-1} ) + n^{C_low},
```
OR there is a charge witnessing residue alignment: the agreeing codewords of the dimension-`(k+t)` list `L_t(w)` have residues mod `E` concentrated on the line `K·[B]_E` beyond the equidistribution fraction `q^{1-t}` — equivalently `v = B/E` is code-aligned mod the residue — which is an explicit quotient / field-confinement / affine-color charge with its own `K_line`-slope cap.

This is the only missing arrow. Its content is: the residue map `res: L_t(w) -> K[X]/(E) = K^t` does not over-concentrate preimages on the single line `K[B]_E` unless `(E,B,w)` carries source-visible quotient/field structure. The Cycle109 lower bound shows the bound is tight (cannot be improved below `binom(n,a)/q^{sigma-1}`), and the counterpacket-hunter cut shows fixed-defect / full-fiber alignment is exactly the charged side (action rank 1).

**Exact counterpacket mechanism (the opposing target).** A growing official LOW family with `t < sigma` intrinsic, corrected reserve (R1)–(R2), source `AP_corr`, all listed charges absent or below cap, and a locator-prefix/residue-collinearity fiber whose distinct-slope count exceeds both `binom(n,k+sigma)/q^{sigma-1} + n^{C_low}` and `floor(q_line/2^128)` — i.e. residue over-concentration on `K[B]_E` that is provably NOT any source-visible quotient/field/affine charge. That is precisely the equidistribution failure my wall forbids; producing it (or proving it impossible) closes the branch.

**Suggested attack order for the wall:** (i) a second-moment/character bound on `res` over `L_t(w)` controlling line-concentration by a quotient-rank invariant `d_R(E)`; (ii) identify the failure locus of (i) with the Role-06 hidden-action / Role-02 action-rank charge so that over-concentration is always charged; (iii) discharge into (R1)–(R2).

## 6. Mandatory self-audit

1. **Proved vs not proved.** Proved (unconditional, over `K_line`): the exact reduction `|Z_t| = ` augmented-`C^+` agreement count at reserve `sigma-1` (Theorem A), the distinct-slope/support pairwise bound `<= k+t-1`, and the Johnson occupancy cap (Theorem B) in regime `(k+sigma)^2 > (k+t-1)n`. Not proved: the sub-Johnson upper bound `binom(n,a)/q^{sigma-1} + n^{C_low}`, the residue-equidistribution-or-charge dichotomy, the charge caps, `AP_corr` descent, field transfer, and the final integer ledger inequality.
2. **Relevance.** Official-route-relevant: stated and proved over the actual line field `K_line`, on official reduced residue-line data; it corrects the calibration and supplies a genuine `q`-free occupancy cap in a delimited regime. It is neither a prize proof nor a counterpacket nor a finite/model certificate.
3. **First failure line.** The first unproved arrow is: *uncharged intrinsic LOW datum with `(k+sigma)^2 <= (k+t-1)n` ⟹ residues of `L_t(w)` are not over-concentrated on `K[B]_E`* (equivalently the §5 dichotomy). Everything before it (reduction, dedup, Johnson cap) is unconditional.
4. **Field / `2^-128` use.** Slopes counted in `K_line`; sole denominator `q_line`; target `floor(q_line/2^128)`. `q_gen` enters only via the corrected reserve (R1); `q_code` not used; `q_chal` not used (no protocol-transfer theorem invoked). The `q^{t-1}` gap is a `K_line`-internal codimension, not a cross-field substitution. The main term fits the budget only under the explicit (R1)–(R2); I did not prove (R1)–(R2) hold for official instances.
5. **Numerator reductions.** Same-slope support collisions: collapsed by construction (one `C^+` codeword per slope), contribute once. Contained/tangent: excluded for these witnesses by the degree argument (`EG+B`, `deg<k+t<a`), so they cannot inflate the count and are not the reducing mechanism. Quotient/periodic/field-confinement/affine-color: these are exactly the *alignment* side of the §5 dichotomy and must be charged at the `K_line`-slope level with retained chart tags; they reduce the free count only when explicitly capped. Affine normalization is cardinality-preserving and may not drop its tag.
6. **PLAN conversion.** Not a PLAN. To PROOF: prove L-CYCLE110-LOW-RESIDUE-EQUIDISTRIBUTION-OR-ALIGNMENT-CHARGE, the LOW charge caps, (R1)–(R2) for official data, and the §5 ledger arithmetic. To COUNTERPACKET: the growing residue-over-concentration family of §5 that evades every source-visible quotient/field/affine charge while exceeding `floor(q_line/2^128)`.