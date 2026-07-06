# b2_modp_giant_extras — first move: frame validated, analytic handle built, bound scoped

- **Status:** SCOPING + TOY-VERIFICATION (no bound proved yet). 2026-07-06.
- **DAG node:** `b2_modp_giant_extras` [TARGET] — a verified single point of failure into the MCA-safe
  grand challenge (`b2 --req--> u2c_boundary_scale_column --req--> x4b_moment_trade_exclusion --> ... -->
  mca_safe --> mca_grand`). Its char-0 sibling `b1_char0_giant_coset_theorem` is [PROVED] but enters
  `u2c` only as `ev` (support), NOT as an `alt` — the mod-p case has no Galois analogue, so **there is no
  bypass around b2** (verified against `prize_dag.json` edges).
- **Scripts (reproducible):** `../scripts/b2_toy_n16.py`, `b2_toy_sweep.py`, `b2_charsum_crosscheck.py`.
- **Lane check:** non-overlapping — disjoint from holmbuar (E_3/max-fiber), LegaSage (conj_f/XR),
  DannyExperiments (CAP25 Q-fin), and the M1 rank-2 slope terminal (scouted 2026-07-06).

## The object, re-derived (the reframing `b2` states but did not re-derive)

A **t-null block** is a subset `B ⊆ μ_n` (n = 2^s; `q ≡ 1 mod n` so `μ_n ⊆ F_q`) with vanishing power
sums `Σ_{x∈B} x^r = 0` in `F_q` for `r = 1..t`. By **Newton's identities**, vanishing power sums
`p_1..p_t` ⟺ vanishing elementary symmetric `e_1..e_t` ⟺ the monic divisor `L_B(X) = Π_{x∈B}(X−x)` of
`X^n − 1` has its **top t coefficients zero** (a "coefficient gap"). Hence:

> **b2's count = the number of monic degree-b divisors of `X^n − 1` over `F_q` with a top-t coefficient
> gap that are NOT coset-unions** — a Hayes/Carlitz "divisors with prescribed leading coefficients"
> count.

**Validated numerically** (`b2_toy_n16.py`): the Newton equivalence holds on every mod-p t-null block at
`(n,t,q) = (16,4,17)`.

## The Frobenius gap, made concrete

- **char 0 (b1):** `f_B` has integer coefficients, so `B̂(ζ^r)=0` propagates along Galois orbits ⟹ every
  0/1 t-null vector is a union of `μ_M`-cosets with `M > t`. **Confirmed:** at `(16,4)` the char-0 t-null
  blocks are *exactly* the 4 `μ_8`-coset unions (`b2_toy_n16.py`, exact `ℤ^8` arithmetic via `Φ_16=X^8+1`).
- **mod p (`q ≡ 1 mod n`):** Frobenius fixes `μ_n` pointwise, the forcing dies, and **"extras"
  (non-coset-union t-null blocks) genuinely appear** — e.g. **3600 extras** at `(16,1,17)` vs only 256
  structured (`b2_toy_sweep.py`). They vanish as the constraint cost approaches the entropy (t=3,4 at
  n=16 → 0 extras) and as `q` grows (`q=97` → 0 extras) — the char-0/finite-field gap is fundamental,
  not technical, exactly as the node states.

## The analytic handle (the concrete first move), cross-checked on two engines

Additive-character orthogonality gives the **exact first-moment identity**
```
N_t(n,q) = #{ B ⊆ μ_n : Σ_{x∈B} x^r = 0, r=1..t }
         = q^{-t} · Σ_{c ∈ F_q^t}  Π_{x∈μ_n} ( 1 + e_q( Σ_r c_r x^r ) ),   e_q(u)=exp(2πi u/q).
```
The `c=0` term is `2^n`; the giant-regime bound must control the rest. **`b2_charsum_crosscheck.py`
confirms `N_t` (character sum) equals the brute enumeration EXACTLY** on all of
`(8,1),(8,2),(16,1),(16,2),(16,3),(16,4),(16,2@q=97)` — the two-engine check (nt-stack rule) on the
Hayes/Carlitz handle we will bound.

## Scoping the `n^3` cushion (what the bound is, and is NOT)

The `n^3 = 2^123` bound is **giant-regime-specific**, about the *extras* (deviation from the structured
coset-unions), NOT the total t-null count. At small t the total count follows the first moment
`N_t ≈ 2^n/q^t` and **vastly exceeds `n^3`** (verified by character sum, no enumeration needed):

| n | t | q | `N_t` (exact) | `2^n/q^t` | `n^3` | verdict |
|---|---|---|---|---|---|---|
| 16 | 1 | 17 | 3856 | 3855 | 4096 | `≤ n^3` (coincidence: `2^16/17 ≈ 2^12`) |
| 32 | 1 | 97 | 44,278,048 | 4.4e7 | 32,768 | `≫ n^3` (small-t, NOT a prize row) |
| 64 | 1 | 193 | 9.56e16 | 9.56e16 | 262,144 | `≫ n^3` (small-t, NOT a prize row) |

So the node's point (ii) is confirmed: **"pure counting can never close it"** — the *total* first moment
is enormous near the prize balance (`t log2 q ≈ n`), and the content of b2 is that the first moment is
almost entirely **structured** (coset unions, per b1) with only `≤ n^3` genuine extras. Full enumeration
lives in the wrong (small-t) regime to test this; the giant regime is analytic-only.

## Phase 0 — structural go/no-go (2026-07-06): the coset-union dichotomy FAILS below balance

Tested whether the extras confine to a coset scale (u2c's dichotomy conjecture: every t-null block is a
union of μ_M-cosets with `M ≥ t`), by classifying every t-null block by its symmetry scale `M_sym` =
largest power-of-2 `M | n` with `B` a union of μ_M-cosets (`../scripts/b2_phase0_dichotomy.py`;
meet-in-the-middle enumeration; **Codex-reviewed to GREEN over 2 rounds** — one float-precision bug in the
character count was fixed to an exact integer DP; MITM completeness, `M_sym`, Newton, and the char-0 `ℤ^8`
arithmetic were all independently re-verified).

**Result: the dichotomy FAILS below balance.** The extras are genuinely *unstructured* (`M_sym = 1`, not
even closed under `x → −x`), and their appearance is governed by the balance point `cost = t·log2 q`
vs `entropy ≈ log2 C(n, n/2)`:

| n=32, q=97 (entropy ≈ 29.2) | t=2 | t=3 | t=4 | t=5 | t=6 |
|---|---|---|---|---|---|
| cost = t·log2 q | 13.2 | 19.8 | 26.4 | 33.0 | 39.6 |
| extras | 455488 | 6336 | 160 | 0 | 0 |
| dichotomy | FAILS | FAILS | FAILS | HOLDS | HOLDS |

Codex-confirmed witness: at (16,2,17), block `{1,2,3,13,15}` (exponents `[0,1,4,6,14]`) has `Σx = Σx² = 0`
yet is not closed under `x → −x` — a genuine unstructured 2-null block.

**Consequence (route pruned).** The prize regime sits ~2% *below* balance, so unstructured extras
genuinely exist there — **b2's `≤ n^3` bound CANNOT rest on a coset-union dichotomy** (that route, the u2c
hope, is false below balance). This is *not* a refutation of u2c: their coset-only scans were at/above
balance or a narrower construction. Encouragingly, near balance the extras are modest (160 at t=4,
`≪ n^3`) and only balloon far below balance; the prize is *just* below balance.

## Step 2 (revised after Phase 0): the analytic route, not a coset dichotomy

Bound the count of the genuinely-unstructured extras directly — the node's own `attack_surface` calls this
"most promising" (the Hayes/Carlitz divisor frame), and Phase 0 confirms it is the *only* viable route.
Two prongs, both avoiding the cancellation floor (extras `≪ N_t`, so no subtracting two `~2^{4e10}` counts):
1. **Hayes/Carlitz divisor count.** Bound `#{monic deg-b divisors of X^n−1 with a top-t coefficient gap
   that are ∉ 𝔽_q[X^M]}` via the leading-coefficient (Hayes) character group over `𝔽_q[X]`: the
   structured mass sits on characters trivial on the μ_M-substructure, the extras on the complementary
   characters — bounded by Weil **directly, no subtraction**.
2. **Pair-correlation of the defect.** Second moment of the *non-coset defect* (not the total count) —
   genuinely `~n^3`-size because the obstruction rarely fires; uses the same cyclotomic-index structure
   as the L1 directions bridge.
Tools: PARI/GP (Hayes char sums, `factormod`), python-flint/Arb (rigorous enclosures), Sage cross-check,
Oscar (monodromy of the coincidence variety for prong 2), Aristotle for an isolated rigidity sub-lemma;
empirical extras-vs-n scaling near balance → the research CPU box (MITM to n≈48–56).

## Honest scope

First move + Phase 0: reframing **re-derived and numerically validated**, b1 **confirmed**, Frobenius-gap
extras **exhibited**, character-sum handle **built and two-engine cross-checked**, and the coset-union
dichotomy **tested and refuted below balance** — all scripts **Codex-green**. **No bound on the extras is
proved yet** — that is Step 2 (the analytic route), the open crux of the node. Nothing here is a prize
threshold.
