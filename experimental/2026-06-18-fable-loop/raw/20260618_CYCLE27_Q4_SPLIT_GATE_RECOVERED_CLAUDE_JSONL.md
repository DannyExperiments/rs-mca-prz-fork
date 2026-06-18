Verified all required files. I have the column definitions (Cycle 15/25), the six-term Plücker expansion (Cycle 25, banked), the rank-one form `q1=c_b·η` (Cycle 20, banked), the `q2` closed form (Cycle 25), and the norm factorization `D=N(ℓ)κ=κ·∏_{a∈F_p}E(a)` (Cycle 24, banked). I worked the top coefficient directly.

---

# Cycle 27 — `W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE`

Ledger respected: `B=F_p` (`q_gen=p`), `F=F_{p^2}` (`q_line=p^2`), `q_chal` unused, `D=F_p` (`n=p`), `t=σ=2`, `j=3`, `η_reserve=2/n` sub-reserve, off `R0` (`κ=u∧b≠0`). Restricted line-incidence/residue calculation only. No `q_gen`/protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK claim.

Convention (odd `p`): write `F=B(α)`, `α²=θ∈B` a non-square, so `τ`-conjugation is `ᾱ=−α`. For `f=f_0+αf_1` set `Im(f):=f_1`. Area form `⟨x,y⟩:=Im(x̄y)=x_0y_1−x_1y_0`: `B`-bilinear, alternating, `⟨1,f⟩=Im(f)`, and crucially `⟨λx,λy⟩=N(λ)⟨x,y⟩` (multiply-by-`λ` scales area by its determinant `N(λ)`).

## 1. The `Q_4` formula is CORRECT — and its `P`-dependence cancels

Top-degree extraction. Write each column coordinate as `s_i=σ_i−zβ_i`, `t_i=γ_i−zδ_i` (`β_i,δ_i∈F`). From the banked columns:

```text
β_1=q1^1, β_2=q1^2, β_0=q1^0, β_3=0      (c_3=−u+zb has s_3=−1, z-free)
δ_1=q2^1, δ_2=q2^2, δ_0=q2^0, δ_3=−1     (t_3=z)
```

Since `⟨s_i,s_j⟩` has `z²`-part `N(z)⟨β_i,β_j⟩` and `⟨t_k,t_l⟩` has `z²`-part `N(z)⟨δ_k,δ_l⟩`, the degree-4 part of the banked six-term `Q` is `N(z)²·Q_4`. With `β_3=0`, three of the six terms vanish, leaving exactly

```text
Q_4 = ⟨β_1,β_2⟩⟨δ_3,δ_0⟩ + ⟨β_1,β_0⟩⟨δ_2,δ_3⟩ − ⟨β_2,β_0⟩⟨δ_1,δ_3⟩.
```

Now `q1=c_b·η`, `η=w+cτ_1+τ_2` (`w=c²−d`), so `(β_1,β_2,β_0)=c_b·(c,1,w)`. By the scaling law `⟨β_i,β_j⟩=N(c_b)⟨x_i,x_j⟩` with `(x_1,x_2,x_0)=(c,1,w)`. Using `δ_3=−1` (so `⟨·,δ_3⟩=±Im`):

```text
Q_4 = N(c_b)·[ Im(c)·Im(q2^0) + Im(c̄w)·Im(q2^2) − Im(w)·Im(q2^1) ].
```

**This reproduces the displayed Cycle 26 formula exactly.** Question 1: the formula is verified from the Cycle 15/25 column definitions.

But it is not in lowest terms. With `q2^2=P, q2^1=d+Pc, q2^0=cd+Pw`, split off the `P`-part. The bracket's `P`-linear piece is

```text
φ(P) = Im(c)·Im(Pw) + Im(c̄w)·Im(P) − Im(w)·Im(Pc),
```

a `B`-linear functional of `P`. Evaluate on the basis `{1,α}`: `φ(1)=Im(c)Im(w)−Im(w)Im(c)=0`; `φ(α)=Im(c)w_0+(c_0w_1−c_1w_0)−Im(w)c_0=0`. So `φ≡0`: **every `P`-term cancels.** The cancellation is structural — `q2`'s `P`-part is `P·η` and `q1=c_b·η`, i.e. the same rank-one direction `η`.

What survives is the `P`-free part `Im(c)Im(cd)−Im(w)Im(d)`. Substituting `w=c²−d` and simplifying (`Im(c²)=2c_0c_1`):

```text
corrected top coefficient:
Q_4 = N(c_b)·( Im(d)² − Im(c)·Im(c̄d) )
    = N(c_b)·( c_1² d_0 − c_0 c_1 d_1 + d_1² ),    c=c_0+αc_1, d=d_0+αd_1.
```

## 2. Source-valid `⟹ Q_4 ≠ 0` (on every separated branch) — Question 2 PROVED

The decisive identity. For `a∈F_p⊂B`, `Im(E(a))=Im(a²+ca+d)=c_1 a + d_1`. When `c∉B` (`c_1≠0`) this is a bijection `F_p→F_p`, so `E` has a root in `F_p` iff `E(a^*)=0` at the unique `a^*=−d_1/c_1∈F_p`, where `E(a^*)=(a^*)²+c_0a^*+d_0∈B`. Clearing denominators,

```text
c_1²·E(a^*) = c_1² d_0 − c_0 c_1 d_1 + d_1²  =  Q_4 / N(c_b).
```

Hence, for `c∉B`:

```text
Q_4 = N(c_b)·Im(c)²·E(−Im(d)/Im(c)),   and   Q_4 = 0  ⟺  E has a root in F_p  ⟺  N(ℓ)=∏_{a∈F_p}E(a)=0.
```

This is the **same** `N(ℓ)=∏_aE(a)` that Cycle 24 attached to `D`. Two independent routes (`D=N(ℓ)κ` and the slope-determinant top symbol) land on the identical Frobenius-locator norm — strong corroboration of the banked column forms.

Now run the two source-valid branches (`c_b≠0`, off `R0`, separated `gcd(E,E^τ)=1`):

- **`c∉B`** (NONDEP, per Cycle 26): source-valid means `E` nonzero on `F_p`, i.e. `N(ℓ)≠0`, so `E(a^*)≠0`, so `Q_4≠0`.
- **`c∈B`** (the residual / possibly-DEP locus): `Q_4=N(c_b)·Im(d)²`. Separatedness forbids `d∈B` (else `E∈B[X]`, `E^τ=E`, `gcd≠1`), so `Im(d)≠0`, so `Q_4≠0`. (Also `c∈B,d∉B` makes `Im(E(a))=Im(d)≠0`, so `E` is automatically nonzero on `F_p`.)

```text
separated + source-valid + off R0 + c_b≠0  ⟹  Q_4 ≠ 0   (all branches).
```

The only zeros of `Q_4` (with `c_b≠0`) are `E` having an `F_p`-root (`c∉B`) or `d∈B` (`c∈B`) — both excluded by source-validity/separatedness. The hypothesis `det M=(c_b/κ²)D≠0` is automatic here and independent of `Q_4`.

## 3. Consequence — the `Q≡0` live branch is empty; `C2=O(p)` (Question 3 moot)

`N(z)²` is the square of the anisotropic norm form, `≢0` and with no `B`-linear factor. So `Q_4≠0 ⟹ deg Q=4`, `Q≢0`, and the leading form carries no spurious line. By the banked Cycle 16 lemma, off `R0`,

```text
Q ≢ 0  ⟹  C2 ≤ #{z∈F : Q(z)=0} ≤ 4p = O(p)=O(n).
```

Since `Q_4≠0` holds for all separated source-valid off-`R0` data with `c_b≠0`, **the `Q≡0` branch is empty source-validly across the whole `t=2,j=3` window** — both the `c∉B` NONDEP branch and the `c∈B,d∉B` residual DEP-candidate. Question 3's premise ("`Q_4=0` source-validly") never occurs, so no lower-coefficient analysis is needed: `Q` is never identically zero. The candidate `Θ(q_line)` seed is removed.

## 4. Distinct split-cubic gate (Question 4)

I am proving an **upper** bound, so the gate only helps. The realized line-incidence slope set (slopes for which a witnessing co-support `τ(z)` yields `X³−τ_1X²+τ_2X−τ_3` split with distinct roots in `F_p`) is a **subset** of the affine-`τ∈B³`-consistent set counted by `{Q(z)=0}`. Therefore

```text
#{distinct-split-cubic slopes} ≤ #{affine-consistent slopes} = O(p).
```

No conflation occurs: affine consistency gives `O(p)`; the gate cannot enlarge it. (The gate would matter only for a lower-bound/counterpacket attempt, which is now foreclosed.)

## Primary label

```text
BANKABLE_LEMMA
```

Banked (restricted `D=F_p`, `t=σ=2`, `j=3`, off `R0`, source-valid, separated):

1. **Corrected top coefficient.** The degree-4 part of `Q` is `N(z)²·Q_4` with
   `Q_4 = N(c_b)·(Im(d)² − Im(c)·Im(c̄d))`. The displayed Cycle 26 `Q_4` is correct; its `P`-dependence cancels identically (rank-one `η`-collinearity of `q1` and `q2`'s `P`-part).
2. **Locator identity.** For `c∉B`, `Q_4 = N(c_b)·Im(c)²·E(−Im(d)/Im(c))`, so `Q_4=0 ⟺ N(ℓ)=∏_{a∈F_p}E(a)=0` — the same norm as Cycle 24's `D`.
3. **Source-valid `Q_4≠0` on every branch**, hence `Q≢0`, hence (Cycle 16) `C2=O(p)`; the distinct-split-cubic gate only shrinks this.

This constitutes a **PROOF that the `Q≡0` live branch is empty and `C2=O(p)` for the entire source-valid separated `t=2,j=3` off-`R0` window**, conditional only on the one mechanical confirmation of the banked `q2=(cd+dτ_1)+Pη` closed form against the raw Cycle 14/15 column definitions. I keep the conservative `BANKABLE_LEMMA` label (not `PROOF`) pending that check, per the Cycle 26 audit's standing requirement that `Q_4` be independently verified before promotion.

Not banked: any corrected-reserve, `q_gen`, protocol, list/CA/MCA/line-decoding/curve-MCA/SNARK consequence; any prize claim; any finite scan as proof.

Residual `EXACT_NEW_WALL`: `W-F1-AA-RES-T2J4` (and `T3J2`) — does the slope-consistency top symbol remain a nonzero power of `N(ℓ)=∏_aE(a)` for higher `j`?

Deterministic checker to bank the upgrade to PROOF (no `q_gen` merge):

```text
checker(p):  # p≥7 odd
  for E=X^2+cX+d, c,d∈F_{p^2}:
    filter: gcd(E,E^τ)=1 ; ∏_{a∈F_p}E(a)≠0 ; κ=u∧b≠0 ; c_b=−Q_E(b)/κ≠0
    build  : columns c_0..c_3 from RAW Cycle14/15 defs (NOT from banked q_i)
    Q      : 4×4 B-determinant in (z_0,z_1) ; extract deg-4 part ; divide by N(z)^2 → Q4_actual
    assert : Q4_actual == N(c_b)*(Im(d)^2 − Im(c)*Im(conj(c)*d))
    assert : (Q4_actual==0) == (E has a root in F_p)
    assert : Q not identically zero      # predicted for all source-valid separated E
  report : any source-valid separated (c,d) with Q≡0   # predicted: NONE
```

If this passes over `p=7,11,13`, the banked `q2` form is confirmed and the lemma is a full PROOF of `C2=O(p)` in this window. (Checker output is confirmation, never the proof.)

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Yes, for this restricted line-incidence sub-problem. The `t=2,j=3` wall is now closed (modulo the mechanical `q2` check): the `Q≡0` counterpacket branch is empty because the top slope-consistency coefficient is `N(c_b)·Im(c)²·E(a^*)`, governed by the locator norm `N(ℓ)=∏_{a∈F_p}E(a)` that source-validity forces nonzero. Next exact lemma: **prove the leading-coefficient-equals-`N(ℓ)`-power phenomenon for general `j`** — that the top-degree coefficient of the slope-consistency determinant `Q` in the `t=2`, arbitrary-`j` regime is a nonzero `B`-multiple of a power of `N(ℓ)=∏_{a∈F_p}E(a)` (the quotient `Q_S` has degree `j−1`, so the columns and the Plücker expansion scale accordingly). If so, source-validity kills `Q≡0` for the entire `t=2` family in the toy window, giving `C2=O(p)` uniformly there. This remains strictly sub-reserve (`η=2/n`) and yields no protocol, `q_gen`, MCA, or reserve consequence.
