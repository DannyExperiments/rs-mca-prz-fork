import Mathlib

/-!
# The Fourier–Tao closing patch for the asymptotic Q input
(`q_fourier_tao_finish_patch.tex`)

This file formalizes the *self-contained, theorem-level* content of the
Fourier–Tao finish patch for the prefix-flatness input `Q` (`conj:Q` of
`grande_finale.tex`).  The patch replaces the naive triangle-inequality /
uniform-character route by a **logarithmic collision moment** argument:

* `lem:log-moment-to-q` — moment-to-max with logarithmic order: the maximum
  normalized fiber ratio `max_s R(s)` is controlled by the `q`-collision moment
  `Γ_q` via `log max_s R(s) ≤ (w log|B| + log Γ_q)/q`.

* `cor:asymp-q-fourier-tao` — asymptotic (and finite-row) `Q` follows once the
  *primitive* collision moment `Γ_q^{prim}` is bounded (`thm:primitive-log-collision`).

## Honest scope

The deep input `thm:primitive-log-collision` — that the primitive `q`-collision
moment is `≤ exp(o(n)·q)` after the quotient / planted / tangent / extension /
saturated first-match cells are removed — is stated in the manuscript only as a
*proof blueprint* resting on an inverse Littlewood–Offord / Balog–Szemerédi–Gowers
large-spectrum step.  It is a genuinely open ingredient and is **not** discharged
here.  What is machine-checked below is exactly the reusable reduction the patch
provides: the elementary log-moment inequality, and the derivation of the `Q`
prefix-flatness bound (with the explicit constant `R_Q = (|B|^w · Γ_q)^{1/q}`)
from *any* collision-moment bound.  Feeding `thm:primitive-log-collision` into
these lemmas yields `Q`; the collision-moment hypothesis is left as an explicit
input, matching the conditional-reduction style used elsewhere in this project.
-/

open scoped BigOperators

namespace QFourierTao

/-
**Core log-moment inequality** (`lem:log-moment-to-q`).

For nonnegative weights `R : ι → ℝ` on a finite set `S`, any integer order
`q ≥ 1`, and any element `s₀ ∈ S` with `R s₀ > 0`,
`q · log (R s₀) ≤ log (∑_{s∈S} R s ^ q)`, i.e.
`log (R s₀) ≤ log (∑_{s∈S} R s ^ q) / q`.

This is the deterministic step behind the patch: since
`max_s R(s)^q ≤ ∑_s R(s)^q`, the log of the maximum is at most the log of the
`q`-th moment divided by `q`.
-/
theorem log_moment_to_max {ι : Type*} (S : Finset ι) (R : ι → ℝ)
    (hR : ∀ s ∈ S, 0 ≤ R s) (q : ℕ) (hq : 1 ≤ q)
    {s₀ : ι} (hs₀ : s₀ ∈ S) (hpos : 0 < R s₀) :
    Real.log (R s₀) ≤ Real.log (∑ s ∈ S, R s ^ q) / q := by
  rw [ le_div_iff₀ ( by positivity ) ];
  rw [ mul_comm, ← Real.log_pow ] ; exact Real.log_le_log ( pow_pos hpos q ) ( hpos.le |> fun h => Finset.single_le_sum ( fun s _ => pow_nonneg ( hR s ‹_› ) q ) hs₀ ) ;

/--
The normalized `q`-collision moment `Γ_q = |B|^{-w} · ∑_s R(s)^q` of the patch,
where `Bw = |B|^w` and `R(s) = N(s)/N̄` is the normalized fiber ratio.
-/
noncomputable def collisionMoment {ι : Type*} (S : Finset ι) (R : ι → ℝ)
    (Bw : ℝ) (q : ℕ) : ℝ :=
  Bw⁻¹ * ∑ s ∈ S, R s ^ q

/-
**Log-moment-to-max in `Γ_q` form** (`lem:log-moment-to-q`).

With `Bw = |B|^w > 0` and `Γ_q = collisionMoment S R Bw q`, the log of any
positive normalized ratio `R s₀` is bounded by `(log Bw + log Γ_q)/q`.  This is
the displayed inequality `log max_s R(s) ≤ (w log|B| + log Γ_q)/q` of the patch.
-/
theorem log_moment_to_max_gamma {ι : Type*} (S : Finset ι) (R : ι → ℝ)
    (hR : ∀ s ∈ S, 0 ≤ R s) (Bw : ℝ) (hBw : 0 < Bw) (q : ℕ) (hq : 1 ≤ q)
    {s₀ : ι} (hs₀ : s₀ ∈ S) (hpos : 0 < R s₀) :
    Real.log (R s₀) ≤
      (Real.log Bw + Real.log (collisionMoment S R Bw q)) / q := by
  rw [ collisionMoment ];
  convert log_moment_to_max S R hR q hq hs₀ hpos using 1 ; rw [ Real.log_mul ( by positivity ) ( by exact ne_of_gt <| lt_of_lt_of_le ( pow_pos hpos q ) <| Finset.single_le_sum ( fun x hx => pow_nonneg ( hR x hx ) q ) hs₀ ), Real.log_inv ] ; ring;

/-
**Asymptotic / quantitative Q from the collision moment**
(`cor:asymp-q-fourier-tao`).

Let `N : ι → ℝ` be nonnegative fiber counts over prefix values `S`, `N̄ > 0` the
mean, `Bw = |B|^w > 0`, and `q ≥ 1`.  If the normalized `q`-collision moment is
bounded by `G` (this is `thm:primitive-log-collision` after paying the quotient
and first-match cells), then every fiber satisfies the prefix-flatness bound
`N s₀ ≤ (Bw · G)^{1/q} · N̄`.

This is exactly conjecture `Q` with the explicit constant
`R_Q = (|B|^w · Γ_q)^{1/q}`; choosing `q = ⌈log n⌉` and the primitive-collision
bound `G = exp(o(n))` gives `R_Q = e^{o(n)}`, the asymptotic Q input.
-/
theorem q_flatness_from_collision {ι : Type*} (S : Finset ι) (N : ι → ℝ)
    (hN : ∀ s ∈ S, 0 ≤ N s) (Nbar : ℝ) (hNbar : 0 < Nbar)
    (Bw : ℝ) (hBw : 0 < Bw) (q : ℕ) (hq : 1 ≤ q)
    (G : ℝ) (hG : collisionMoment S (fun s => N s / Nbar) Bw q ≤ G)
    {s₀ : ι} (hs₀ : s₀ ∈ S) :
    N s₀ ≤ (Bw * G) ^ ((q : ℝ)⁻¹) * Nbar := by
  -- By definition of collisionMoment, we have that N s₀ ^ q ≤ Bw * G * Nbar ^ q.
  have h_ineq : (N s₀ / Nbar) ^ q ≤ Bw * G := by
    unfold collisionMoment at hG;
    rw [ inv_mul_le_iff₀ ( by positivity ) ] at hG ; nlinarith [ Finset.single_le_sum ( fun s _ => pow_nonneg ( div_nonneg ( hN s ‹_› ) hNbar.le ) q ) hs₀ ] ;
  convert mul_le_mul_of_nonneg_right ( Real.rpow_le_rpow ( pow_nonneg ( div_nonneg ( hN s₀ hs₀ ) hNbar.le ) _ ) h_ineq ( inv_nonneg.mpr ( Nat.cast_nonneg q ) ) ) hNbar.le using 1;
  rw [ ← Real.rpow_natCast, ← Real.rpow_mul ( div_nonneg ( hN s₀ hs₀ ) hNbar.le ), mul_inv_cancel₀ ( by positivity ), Real.rpow_one, div_mul_cancel₀ _ hNbar.ne' ]

/-
**Finite-row bit certificate** (`lem:log-moment-to-q`, finite form).

For nonnegative ratios `R`, base `|B| = base > 1`, depth `w`, order `q ≥ 1`, and
bit margin `Δ`, if `(w log₂|B| + log₂ Γ_q)/q ≤ Δ` then every positive ratio
`R s₀ ≤ 2^Δ`.  This is the finite-row certificate the patch requires: it is valid
only when the moment order `q` is large enough that the numerator fits the margin.
-/
theorem q_flatness_bit_certificate {ι : Type*} (S : Finset ι) (R : ι → ℝ)
    (hR : ∀ s ∈ S, 0 ≤ R s) (base : ℝ) (hbase : 1 < base) (w q : ℕ) (hq : 1 ≤ q)
    (Δ : ℝ) {s₀ : ι} (hs₀ : s₀ ∈ S) (hpos : 0 < R s₀)
    (hcert :
      ((w : ℝ) * Real.logb 2 base +
          Real.logb 2 (collisionMoment S R (base ^ w) q)) / q ≤ Δ) :
    R s₀ ≤ (2 : ℝ) ^ Δ := by
  refine' le_trans _ ( Real.rpow_le_rpow_of_exponent_le ( by norm_num ) hcert );
  rw [ ← Real.log_le_log_iff ( by positivity ) ( by positivity ), Real.log_rpow zero_lt_two ];
  convert log_moment_to_max_gamma S R hR ( base ^ w ) ( by positivity ) q hq hs₀ hpos using 1 ; norm_num [ Real.logb, mul_div_assoc ];
  field_simp

end QFourierTao