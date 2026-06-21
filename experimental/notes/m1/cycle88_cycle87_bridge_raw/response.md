I'll start by reading the file index, then the key project files and certificate context.The index is huge. Let me read the key Cycle87 and bridge files directly.This is the core proof. Let me read the master certificate, audit, and pass JSONs.Arithmetic checks out so far. Let me read the audit note and the relevant project state docs.Let me read the pass JSON, census result, and the route board / banked lemmas for the MCA definition.Let me check the active walls, banked lemmas, and instance registry for the official MCA definition.Let me look at the banked lemmas, instance registry, and director state for the MCA failure-row definition.Let me check the banked lemmas and cuts for the official MCA failure-row definition and the prize structure.Let me search the agents log and cuts file for the official MCA failure-row definition.Let me search the agents log for the official MCA failure-row definition and prize structure.My understanding of the certificate is now solid. Let me check the agents log for the official MCA / prize failure-row definition, to confirm what the bridge target requires.I have now read the certificate proof, master JSON, pass JSON, census result, audit note, and the surrounding route-board/director state. I have enough to decide the bridge. I do not have the official `slackMCA_v3.tex` / `proximity_blueprint_v3.tex` definitions in the attachments, which matters for one specific clause, and I flag that precisely below.

# BANKABLE_LEMMA

## 1. Executive verdict and confidence

The bridge `L-CYCLE87-464-U-OFFICIAL-MCA-FAIL-ROW` is **conditionally valid**, not false and not unconditionally theorem-valid. The internal reduction (slope formula → collision bound → transversality → field ledger → numerator > target) is mathematically sound and the decisive arithmetic checks out exactly. It is conditional on three things, two of which the bridge already names ("if its finite replay is trusted") and one of which is a definitional dependency I cannot close from the supplied package.

Confidence: high (~0.9) that the reduction is valid given the finite facts; the residual ~0.1 is concentrated entirely in the official-definition clause (item 4 below), not in the algebra.

I verified the load-bearing arithmetic independently:
- `q0 = 17^16 = 48,661,191,875,666,868,481` ✓
- `Q = q0^2+q0+1 = 2,367,911,594,760,467,245,892,767,489,196,618,115,843`, and `R·M = Q` with `R = 48,661,191,868,691,111,041`, `M = 48,661,191,882,642,625,923`, `gcd(R,M)=1` ✓
- `T_line = floor(17^48/2^128) = 338,617,018,271,848,945,628` (order check: `1.152e59 / 3.403e38 ≈ 3.386e20`) ✓
- `N·P = 2,782,305,834,758,012,141,568`; `N·P/2 = 1,391,152,917,379,006,070,784` ✓
- `margin = N·P/2 − T_line = 1,052,535,899,107,157,125,156` ✓
- Smooth histogram consistency: `84 = 2·(P − occupancy) = 2·(52,747,567,104 − 52,747,567,062) = 2·42` ✓, giving `m1=P−42`, `m2=42`, `m≥3=0`.

## 2. Exact theorem (conditional implication) proved

> **Lemma (Cycle87 bridge).** Assume the banked finite facts: (C84) the Cycle84 circuit yields `P = 52,747,567,104` distinct admissible 113-point supports `T ∈ P0` with `beta`-product occupancy `N = Occ(beta) = 52,747,567,092`; (C85) every such support has the fixed six-jet `J_T(t) ≡ 1−t (mod t^6)` and support size 113; and (C87) the executed smooth-quotient census is correct, i.e. the map `T ↦ pi(P_T(U))` into the order-`M` quotient has maximum fibre `mu_M(U) ≤ 2`. Then the explicit `[464,232]` GRS code over `L = F0[U]/(U^3−(X+2))` with the single affine syndrome line of §9.2 admits at least
> `N·P / 2 = 1,391,152,917,379,006,070,784`
> distinct transverse bad slopes, all with `q_gen=q_code=q_line=q_chal=17^48`, profile `(n,k,sigma,j,t)=(464,232,6,226,1)`, rate `rho=k/n=1/2`, and this count exceeds `floor(q_line/2^128) = 338,617,018,271,848,945,628`.

This is exactly the bridge target, so under (C84)+(C85)+(C87) the bridge holds.

## 3. Proof of the reduction; obstruction analysis

The four reduction steps are each individually correct:

**Slope identity (exact).** With `c = beta − U`, for any second-block point `x` one has `beta−(c+x) = U−x`, so `prod_{x∈T}(beta−(c+x)) = P_T(U)`. Hence for `S(v,T)=T_v ∪ (c+T)`, `P_S(beta) = P_{T_v}(beta)·P_T(U) = v·P_T(U)`, and the line's free coordinate is `z_{v,T} = 1/(v·P_T(U))`. This is exact and the inversion/affine normalization are bijections, preserving cardinality.

**Collision divisor (the crux).** `v ∈ Omega ⊂ F0^x` is a base scalar; `P_T(U) ∈ L`. Fix a target `w`. For each `T`, `v` is forced to `w·P_T(U)^{-1}`, and this lies in `Omega ⊂ F0^x` only if `[w]=[P_T(U)]` in `L^x/F0^x`. So the fibre over `w` has size `≤ #{T : [P_T(U)]=[w]} = mu_proj(U)`. The census proves `mu_M(U)≤2`; since `[z]=[w] ⟹ pi(z)=pi(w)` (because `pi(z)=z^{(q−1)R}` factors through `L^x/F0^x` onto the order-`M` quotient), every exact projective class is contained in one `pi`-fibre, so `mu_proj(U) ≤ mu_M(U) ≤ 2`. The smooth projection can only **merge** exact classes, never **split** them — this one-sidedness is what makes the upper bound sound. With `N·P` input pairs and every fibre `≤ 2`, the number of distinct slopes is `≥ N·P/2`.

**Transversality / noncontainment.** If the line direction lay in the span of the 226 support columns, projecting to the first 231 Vandermonde rows would force a dependence among 226 distinct columns of a `231×226` Vandermonde matrix, which has full column rank — contradiction with the nonzero last coordinate. So every counted incidence is transverse. Each `a_x = 1/P_S'(x)` is nonzero (squarefree support). ✓

**Field ledger.** The domain contains `eta` (degree 16 → generates `F0`), and `1, c+1` (→ generates `c`, hence `U = beta−c`), so it generates `L`; `q_gen = 17^48`. The matrix and line are over `L`; `q_code = q_line = 17^48`. Only `q_line` enters the target `floor(q_line/2^128)`; no spurious `q_chal` factor is inserted into numerator or denominator. ✓

**Where it cannot fail internally:** every reduction-attacker named in the prompt is closed — quotient/periodic structure is paid for through projective classes (and the *coarser* smooth quotient still has max 2); contained incidences are excluded by the Vandermonde rank argument; same-slope collisions are exactly the `mu_proj ≤ 2` divisor; affine/colour normalization is a bijection; the numerator is `N·P` (one representative per occupied `beta`-fibre in block one, all `P` in block two), not an unjustified `P^2`.

**The one obstruction I cannot discharge from the package (see §4).**

## 4. Required self-audit (exact answers)

**1. What I proved vs did not prove.** I proved the conditional implication of §2: that, *granting* (C84)+(C85)+(C87), the construction yields ≥ `N·P/2` distinct transverse bad slopes on one affine syndrome line of one `[464,232]` GRS code over `17^48`, exceeding `floor(q_line/2^128)`. I did **not** prove (C84)/(C85)/(C87) themselves — in particular I did not, and Codex did not, independently rerun the 52,747,567,104-record census; `mu_proj(U)≤2` remains certificate-level. I also did not verify that the constructed object meets the **official** MCA failure-row definition (the `def:residue`/`thm:normalform`/proximity-target spec), because that spec is referenced in the route board but is not present in this attachment set.

**2. Official-prize relevance.** It is official-*profile*-relevant: a genuine MCA numerator **lower counterpacket** with the correct field ledger, rate `1/2`, and a numerator beating the `2^-128` target by ~4.1×. It is more than a finite-model certificate but is **not** the full prize theorem; promoting it to prize status needs the separate splice lemma `L-CYCLE87-OFFICIAL-MCA-COUNTERPACKET-TO-FULL-PRIZE-REDUCTION`.

**3. First line where it could fail.** The first external dependency is (C84): that the tuple circuit gives exactly `P` distinct 113-point supports with the fixed six-jet and `beta`-occupancy exactly `N`. Inside the new work, the first failure point is (C87): a census result other than `mu_M(U)≤2` (e.g. a smooth class of size ≥ 9 that does not split under exact projective equality). Both are explicitly inside the bridge's "if its finite replay is trusted" antecedent. The first failure point *outside* that antecedent — the only one not covered by trusting the replay — is the definitional match in answer 4 below.

**4. Are `q_gen/q_line/q_code/q_chal` and `2^-128` used correctly?** Internally, yes: all four equal `17^48`, the four roles are justified separately (generation, code, line, declared challenge), and only `q_line` enters `floor(q_line/2^128)`; no ledger merge, no extra `q_chal` factor. The residual is that I cannot confirm from this package that `floor(q_line/2^128)` is *the* official target for the `(t=1, sigma=6, rho=1/2)` row in the prize spec, nor that `sigma=6, j=226, t=1` is an admissible official profile — these depend on `slackMCA_v3.tex`/`proximity_blueprint_v3.tex`, which are not attached. The bridge statement itself fixes the target as `floor(q_line/2^128)`, so the implication holds *on the bridge's own terms*; the open question is only whether those terms equal the official spec.

**5. Could structure reduce the numerator?** No, for the reasons in §3: projectivization/periodicity is paid through the (coarser) smooth quotient with max 2; contained incidences excluded by Vandermonde full rank; same-slope collisions are the divisor itself; affine colour normalization is bijective; support duplication excluded by disjoint blocks plus banked support-circuit injectivity. The conservative `÷2` already beats the target, and the actual histogram (only 42 multiplicity-2 classes) implies the true count is far higher.

**6. What converts this to PROOF or COUNTERPACKET.** Two items, in order:
   - **(census replay)** Independently rerun `cycle87_u_smooth_census` from source on a ≥66 GB-RAM or ~0.5–0.85 TB-scratch surface and reproduce `records=52,747,567,104`, `occupancy=52,747,567,062`, `smooth_max=2`. Also re-derive (C84) `P`, `N`, `m_max(beta)=2` via `W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION`. This discharges (C84)+(C87).
   - **(definitional checker)** A `verify_official_mca_row` that loads the official `def:residue`/proximity-target definitions and confirms: (i) the bad-slope numerator there equals the distinct-`z` count here; (ii) `(t,n,k,sigma,j,q_line)=(1,464,232,6,226,17^48)` is an admissible official row; (iii) the official rate-`1/2` target is exactly `floor(q_line/2^128)`. This discharges item 4's residual. Both passing → promote to PROOF/COUNTERPACKET.

## 5. Certificate / replay requirements (exact condition)

The bridge is valid **conditional on**: (a) independent full replay of the 52.7B-record smooth census reproducing `mu_M(U)≤2`; (b) the banked Cycle84 census (`P, N, m_max(beta)=2`) and Cycle85 six-jet/`rho` transfer; and (c) confirmation that the official MCA failure-row definition and rate-`1/2` target coincide with `floor(q_line/2^128)` for this profile. Under (a)+(b)+(c), the implication is theorem-valid. The package supplies (with verified checksums and lightweight verifiers passing) everything for (a) and (b) at certificate level but no independent re-execution; it supplies nothing decisive for (c).

## 6. Next exact lemma / construction

Bank `L-CYCLE87-464-U-OFFICIAL-MCA-FAIL-ROW` as **BANKABLE_LEMMA / CONDITIONAL** with the §2 statement and conditions (a)–(c). The next exact construction is the definitional checker of self-audit item 6(ii): a machine-checkable statement

```
THM (official-row identification):
  distinct_bad_slopes_official( GRS[464,232]/17^48, ell, def:residue )
    = #{ z in L : exists noncontained S, P_S(beta)^{-1} = z }
    >= N*P/2 > floor(q_line/2^128),
  with (t,n,k,sigma,j) = (1,464,232,6,226) an admissible official profile.
```

paired with the independent census replay. Proving that identity against the official spec, plus the replay, is exactly what upgrades this conditional lemma to an unconditional official MCA failure row and unlocks the subsequent `L-CYCLE88-...-PROXIMITY-PRIZE-BRIDGE`.