I'll start by reading the file index and the key project files to understand the current state.Let me read the most relevant recent files.Now let me read the Cycle98 brief and the active external root audit, plus the Cycle99 prompt.Now let me read the Cycle98 audit details and the Cycle99 prompt for exact setup.Now let me read the Cycle98 audit and the Cycle99 prompt for the precise setup.Let me read the Cycle98 audit and the Cycle99 prompt for the precise mathematical setup.Let me check the run directory structure to see what stage this is at.I have enough context now. I'm the Cycle 99 worker on the RS-MCA / Proximity Prize research, attacking `L-CYCLE99-B1-APERIODIC-MOMENT-CURVE-INCIDENCE`. Let me work through the mathematics and write the response.

My analysis of the target: bound `|v(F_p\H) ∩ (P - M_s)_aper|` by `n^{O(1)}`. Let me record the key derivations, then write the deliverable.

The condition `v(θ) ∈ P − M_s` means `∃ S⊆H, |S|=s` with `p_j({θ}⊔S)=P_j` for `j=1..σ+1`. Via Newton's identities (valid since `p>s+1`), this is equivalent to `(X−θ)f_S(X) ≡ U(X) (mod deg<k)`, where `f_S=∏_{x∈S}(X−x)` is a degree-`s` divisor of `X^n−1`. This unlocks three equivalent forms and identifies the problem as RS list-decoding over a subgroup at agreement `s=k+σ`, below the Johnson radius.

Let me write the response file.This gives me the exact toy model. Let me write a verifier for the new divisor/list-decoding equivalence and run it, then write the response. Let me check the writable layout first.I now have the full picture. I'm the Cycle 99 worker attacking `L-CYCLE99-B1-APERIODIC-MOMENT-CURVE-INCIDENCE`. I've worked through the mathematics. Note: in this run only the `Read` tool is wired up, so I cannot write `response.md` to disk or execute a verifier — I'll deliver the complete worked answer here (and give an exact, runnable checker spec for Codex to execute locally, matching the established cycle workflow).

---

# Cycle 99 — B1 Aperiodic Moment-Curve Incidence

Classification: **BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.**

I do **not** prove the polynomial bound in the live corrected-reserve range, and I do **not** produce a counterpacket. I bank an exact three-way reformulation, identify the object as sub-Johnson subgroup-RS list-decoding (route-cut), prove the easy regimes unconditionally, and — the main new content — reduce the target to a single explicit character-sum bound via an *exact* identity `|Θ_U| ≤ N = main + error` with `main ≤ 1`.

## Setup and notation

`p` prime, `p ≡ 1 mod n`, `H ≤ F_p^*` cyclic of order `n`, so `∏_{x∈H}(X−x) = X^n − 1`. `U` monic of degree `s+1`, `s = k+σ`, `k = ρn`, `σ ≥ Cn/log n`. `P=(P_1,…,P_{σ+1})` is the power-sum prefix of `U`; `v(θ)=(θ,…,θ^{σ+1})`; `M_s={(p_1(S),…,p_{σ+1}(S)):S⊆H,|S|=s}`; `Θ_U = {θ∈F_p∖H : v(θ)∈P−M_s}`.

## Lemma A (power-sum ⇔ divisor-remainder ⇔ codeword forms)

For `θ∈F_p∖H` the following are equivalent:

1. `v(θ) ∈ P − M_s`.
2. `∃` monic `f | X^n−1`, `deg f = s`, with `deg(U − (X−θ)f) < k`.
3. `∃ r∈F_p[X]`, `deg r<k`, with `U − r = (X−θ)f`, `f|X^n−1`, `deg f=s`, `θ∉H`.

Proof. `T = S⊔{θ}` has `|T|=s+1` and `p_j(T)=p_j(S)+θ^j`, so (1) ⟺ `p_j(T)=P_j` for `j≤σ+1`. Since `p>s+1`, Newton's identities make `(p_1,…,p_{σ+1})` and `(e_1,…,e_{σ+1})` mutually determined; the monic polynomial with root multiset `T` is `(X−θ)f_S` with `f_S=∏_{x∈S}(X−x)`. Matching `e_1,…,e_{σ+1}` of `T` and `U` ⟺ the top `σ+1` coefficients (degrees `s…k`) of `(X−θ)f_S` and `U` agree ⟺ `deg(U−(X−θ)f_S)<k`. `f_S` is a degree-`s` divisor of `X^n−1`. Setting `r=U−(X−θ)f` gives (3). ∎

**Injectivity `θ↦r`.** If `(X−θ)f = U−r = (X−θ′)f′`, unique factorization forces the unique non-`H` linear factor to coincide: `θ=θ′`. Hence

> `|Θ_U| ≤ #{deg-<k codewords r whose agreement with u:=U|_H is exactly s}`,

i.e. `Θ_U` injects into the list of the `[n,k]` Reed–Solomon code on evaluation set `H` at agreement `s=k+σ` (error weight `m=n−k−σ`). This is the precise list-decoding identification.

## Lemma B (reciprocal / affine-line-incidence form)

Let `Ũ(X)=X^{s+1}U(1/X)` (so `Ũ(0)=1`), `W=Ũ^{-1}∈F_p[[X]]`, and for `S′=H∖S`, `|S′|=m`, set `g_{S′}(X)=∏_{x∈S′}(1−xX)`. Using `∏_{x∈H}(1−xX)=1−X^n` and `σ+2≤n`, reversal of Lemma A(2) gives

```text
g_{S′}(X) ≡ (1 − θX)·W(X)   (mod X^{σ+2}).
```

Writing `g_{S′}=∑_i(−1)^i e_i(S′)X^i` and `W=∑W_jX^j` (`W_0=1`), this is

```text
e_i(S′) = (−1)^i ( W_i − θ W_{i−1} ),   i = 1,…,σ+1,
```

an affine-linear image of `θ`. Therefore `|Θ_U| ≤ |ℓ ∩ E_m|`, where `ℓ⊂F_p^{σ+1}` is the explicit affine line above and `E_m={e(S′):|S′|=m}` is the elementary-symmetric image of `m`-subsets of `H`. (`θ` is recovered as `θ = e_1(S′)+W_1`.) ∎

This is exactly the "moment curve against `M_s`" wall from Cycle 98, now in dual elementary-symmetric coordinates where the moment curve straightens to a line and the subgroup data sits in `E_m`.

## Route-cut (Johnson radius)

The list of codewords at agreement `≥ s` is `n^{O(1)}` **iff** `s > √(kn)` (Johnson). With `s=ρn+σ`, `√(kn)=√ρ·n`, this needs

```text
σ > (√ρ − ρ) n = √ρ(1−√ρ) n = Θ(n).
```

Since `σ=Θ(n/log n)=o(n)`, the live range is **strictly below Johnson** for all large `n`. Consequence: the bound cannot follow from agreement/Johnson alone; any proof must use (a) the multiplicative-subgroup structure of `H` and (b) aperiodicity of `P`. Generic RS lists below Johnson can be exponential, so the "many codewords from one fixed `U`" structure plus subgroup arithmetic is essential. This formally cuts the agreement-only route.

## Unconditional partial results

- **Small field:** `|Θ_U| ≤ p−n`. If `p = n^{O(1)}` the target holds trivially. The content is entirely the large-`p` (prize-scale `q_line`) regime.
- **Above-Johnson reserve:** if `σ ≥ (√ρ−ρ)n + 1`, then `|Θ_U| ≤ n(n−k)/(s²−kn) = n^{O(1)}` unconditionally (Johnson count). This pins the hardness exactly at `σ=o(n)`.

## Main new reduction (exact identity, `main ≤ 1`)

Let `N = ∑_{θ∉H} #{S⊆H,|S|=s : p_j(S)=P_j−θ^j, j≤σ+1} ≥ |Θ_U|`. Expanding each constraint with the additive character `ψ` and using `∑_{|S|=s}ψ(∑_{x∈S}L_t(x)) = e_s({ψ(L_t(x))}_{x∈H})` where `L_t(X)=∑_{j=1}^{σ+1} t_jX^j`:

```text
N = (1/p^{σ+1}) ∑_{t∈F_p^{σ+1}} ψ(−⟨t,P⟩) · e_s({ψ(L_t(x))}_{x∈H}) · S(t),
S(t) = ∑_{θ∉H} ψ(L_t(θ)).
```

The `t=0` term is the exact main term

```text
main = C(n,s)·(p−n) / p^{σ+1} ≤ C(n,s)/p^σ ≤ 2^n / n^σ = 2^{n − σ log n} = 2^{n − Cn} ≤ 1
```

for `C ≥ ln 2` (using `p≥n+1`, `n^{n/log n}=e^n`). Since `N` is a nonnegative integer count and the expansion is exact,

```text
|Θ_U| ≤ N = main + error ≤ 1 + |error|.
```

**Therefore the target `|Θ_U| ≤ n^{O(1)}` is equivalent (up to the trivial small-`p` case) to**

```text
|error| = | (1/p^{σ+1}) ∑_{t≠0} ψ(−⟨t,P⟩) e_s({ψ(L_t(x))}_{x∈H}) S(t) | ≤ n^{O(1)}.
```

For `S(t)` Weil gives `|S(t)| ≤ σ√p + n` (complete sum of `ψ∘L_t`, `deg L_t ≤ σ+1 < p`). The genuinely open factor is the **elementary-symmetric transform** `e_s({ψ(L_t(x))}_{x∈H})`, for which only the trivial `|·|≤C(n,s)` is known; the `p^{σ+1}` terms then overwhelm. Cancellation must come from averaging over the moment pencil `t↦L_t`, and the resonant `t` (supported on indices `≡0 mod M`, paired with `μ_M`-periodic `P`) are exactly the ones with no cancellation — which is why **aperiodicity of `P` is the hypothesis that kills them** (and why the periodic core is charged separately).

## Exact next wall

```text
W-CYCLE99-SUBGROUP-ELEMSYM-MOMENT-CHARACTER-SUM  (alias L-CYCLE100):

For H ≤ F_p^* of order n, aperiodic prefix P (P not μ_M-invariant, M|n, M>1),
  | ∑_{t≠0} ψ(−⟨t,P⟩) · e_s({ψ(L_t(x))}_{x∈H}) · ∑_{θ∉H}ψ(L_t(θ)) |  ≤  p^{σ+1} · n^{O(1)}.
```

This is strictly smaller and fully explicit. Proving it ⟹ PROOF of `L-CYCLE99`. A nonperiodic `P` forcing `|error|` superpolynomial ⟹ COUNTERPACKET (the only known large-error mechanisms are periodic, so this would require a new aperiodic resonance — a precise target for the falsifier).

A first sub-step worth isolating: bound the *single-frequency* moment slices `e_s({ψ(c·x^j)}_{x∈H})` for one monomial `L_t = c x^j`, which is a Gauss-sum-symmetric-function object; controlling these and their products is the natural ladder toward the full pencil bound.

## Checker spec (for Codex to run locally; not executed in this run)

Extend `cycle98_moment_curve_incidence_check.py` to `cycle99_divisor_line_incidence_check.py`, asserting on small `(p,n,k,σ)`:

1. Lemma A: `Θ_U` (power-sum form) `==` `{θ∉H : deg(U − (X−θ)f) < k for some degree-s divisor f of X^n−1}` `==` codeword-agreement-exactly-`s` set; and `θ↦r` injective.
2. Lemma B: for each active `θ`, `g_{S′} ≡ (1−θX)W mod X^{σ+2}` and `e(S′)∈ℓ`; report `|ℓ∩E_m|`.
3. Identity: recompute `N` two ways — direct pair count vs. the character expansion — assert equality; print `main`, `|error|`, and confirm `main ≤ 1` for `C≥ln2` cases.
Certificate fields: `{p,n,k,sigma,s,seed, external_theta, N, main, error_abs, aperiodic, johnson_gap=s^2−k n, status}`. Counterpacket trigger: aperiodic family with `error_abs/n^c` growing.

## Self-audit

1. **Proved:** Lemmas A, B (exact equivalences + injective embedding into subgroup-RS list at agreement `s`); the sub-Johnson route-cut; the two unconditional regimes; the exact identity `|Θ_U| ≤ N = main+error` with `main ≤ 1`, reducing the target to `|error| ≤ n^{O(1)}`. **Not proved:** the elementary-symmetric/moment character-sum bound itself — hence **not** the polynomial bound in the live range.
2. **Research/model + bankable reduction**, not an official-prize theorem.
3. **First failure line:** `W-CYCLE99-SUBGROUP-ELEMSYM-MOMENT-CHARACTER-SUM` (no proven cancellation in `e_s` along the pencil below Johnson). Minor side-conditions: `main≤1` needs `C≥ln2`, `p≥n` (both hold).
4. **Ledgers:** `p=q_line=q_code=q_gen=q_chal` here (single field), `n|p−1`, `k=ρn`, `σ` reserve; `2^{-128}` target ↔ requiring poly list size; used consistently and not conflated.
5. **Yes:** quotient/periodic structure produces exactly the resonant `t` (supported on multiples of `M`) with no cancellation — the periodic counterpacket — so aperiodicity is required and is precisely what the error-bound must exploit. `θ∈H` (contained) is separated upstream; same-slope collapse is handled since `θ↦r` is injective. Affine color normalization does not further reduce the numerator here.
6. **PLAN→PROOF:** prove the boxed character-sum lemma for aperiodic `P`. **PLAN→COUNTERPACKET:** exhibit aperiodic `P` with superpolynomial `|error|` (must beat the periodic-only known resonances).

**Route to a full solve:** yes, conditional on the boxed lemma. Next exact object: bound the subgroup elementary-symmetric transform `e_s({ψ(L_t(x))}_{x∈H})` along the moment pencil, starting from single-monomial `L_t=c x^j` slices (Gauss-sum symmetric functions) and building to the full `(σ+1)`-frequency pencil, with aperiodicity removing the resonant frequency support.