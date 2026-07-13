import Mathlib
import GrandeFinale.QFourierTao

/-!
# The entropy-inverse route to Q: the two rigorous atoms

This file formalizes the two *rigorous, self-contained* pieces of the
entropy-inverse-Littlewood–Offord route to the prefix-flatness input `Q`
(`conj:Q` of `grande_finale.tex`), namely:

1. **The exact logarithmic-moment equivalence** (§1 of the route).
   Together with the forward inequality already proved in
   `GrandeFinale.QFourierTao` (`QFourierTao.log_moment_to_max_gamma`,
   `QFourierTao.q_flatness_from_collision`), the reverse inequality proved here
   (`collision_moment_le_of_max`) establishes the two-sided equivalence

   `Γ_q^{prim} ≤ exp(o(n)·q)  ⇔  M_{prim} ≤ exp(o(n))`  (primitive asymptotic Q),

   for any moment order `q → ∞` with `w·log|B|/q = o(n)`.

2. **The Vandermonde rank rigidity** (§4 of the route).
   The half-moment-curve columns `v_y = (ρ(y), ρ(y)y, …, ρ(y)y^{r-1})` with
   `ρ(y) ≠ 0` and the `y`'s distinct are linearly independent
   (`halfMoment_linearIndependent`), because the scaled Vandermonde determinant
   is a unit (`halfMoment_det`).  Consequently any submodule (e.g. the affine
   span of a low-rank generalized arithmetic progression) containing a set `T`
   of such columns has `finrank ≥ |T|` (`halfMoment_subset_rank`).  This is the
   obstruction that turns a positive-rate low-rank structure into a
   contradiction once `r = Θ(n)`.

## Honest scope

The genuinely deep step of the route — the **entropy-scale inverse
Littlewood–Offord / Balog–Szemerédi–Gowers theorem** that, from
`Γ_q^{prim} ≥ exp(η·n·q)`, extracts a positive-rate subset `U` of columns lying
in a rank-`o(n)` generalized/coset progression — is *not* discharged here.  As
the manuscript and the summary record, that is a genuinely open ingredient
requiring a Rényi-entropy strengthening of Tao–Vu / Green–Ruzsa that does not
follow as a black box from the standard polynomial-concentration or
small-doubling theorems.  What is machine-checked below are exactly the two
rigorous atoms that the open theorem feeds into and out of: the moment
equivalence (both directions) and the Vandermonde rank rigidity that closes the
argument once the inverse theorem produces low rank.
-/

open scoped BigOperators
open Matrix

namespace QEntropyInverse

/-! ## 1. The reverse direction of the logarithmic-moment equivalence -/

/--
**Reverse direction of the log-moment equivalence** (§1, "Q implies moment bound").

Let `R : ι → ℝ` be nonnegative normalized fiber ratios over a finite prefix set
`S`, with total mass `∑_s R(s) ≤ Bw` (here `Bw = |B|^w`, and the mass bound is
the exact count identity `∑_s N^{prim}(s) ≤ binom(n,m)`).  If every ratio is
bounded by the maximum `M` (primitive asymptotic Q, `M = M_{prim}`), then the
normalized `q`-collision moment obeys

`Γ_q = |B|^{-w}·∑_s R(s)^q ≤ M^{q-1}`.

Combined with the forward inequality `QFourierTao.log_moment_to_max_gamma`, this
gives the exact two-sided equivalence `Γ_q ≤ exp(o(n)·q) ⇔ M ≤ exp(o(n))`.
-/
theorem collision_moment_le_of_max {ι : Type*} (S : Finset ι) (R : ι → ℝ)
    (hR : ∀ s ∈ S, 0 ≤ R s) (Bw : ℝ) (hBw : 0 < Bw)
    (hmass : ∑ s ∈ S, R s ≤ Bw)
    (M : ℝ) (hM0 : 0 ≤ M) (hM : ∀ s ∈ S, R s ≤ M) (q : ℕ) (hq : 1 ≤ q) :
    QFourierTao.collisionMoment S R Bw q ≤ M ^ (q - 1) := by
  have hsum : ∑ s ∈ S, R s ^ q ≤ M ^ (q - 1) * Bw := by
    calc
      ∑ s ∈ S, R s ^ q ≤ ∑ s ∈ S, M ^ (q - 1) * R s := by
            apply Finset.sum_le_sum
            intro s hs
            have hsplit : R s ^ q = R s ^ (q - 1) * R s := by
              rw [← pow_succ]; congr 1; omega
            rw [hsplit]
            exact mul_le_mul_of_nonneg_right
              (pow_le_pow_left₀ (hR s hs) (hM s hs) (q - 1)) (hR s hs)
      _ = M ^ (q - 1) * ∑ s ∈ S, R s := by rw [Finset.mul_sum]
      _ ≤ M ^ (q - 1) * Bw := mul_le_mul_of_nonneg_left hmass (by positivity)
  unfold QFourierTao.collisionMoment
  rw [inv_mul_le_iff₀ hBw, mul_comm]
  exact hsum

/-! ## 2. The Vandermonde rank rigidity of the half-moment columns -/

/--
The half-moment-curve matrix `M i j = ρ i · (y i)^j` factors as
`diagonal ρ · vandermonde y`.
-/
theorem halfMoment_eq_diagonal_mul_vandermonde {F : Type*} [CommRing F] {r : ℕ}
    (ρ y : Fin r → F) :
    (Matrix.of (fun (i j : Fin r) => ρ i * (y i) ^ (j : ℕ)))
      = Matrix.diagonal ρ * Matrix.vandermonde y := by
  ext i j
  simp [Matrix.diagonal_mul, Matrix.vandermonde_apply]

/--
**Scaled Vandermonde determinant** (§4).  The determinant of the half-moment
matrix `M i j = ρ i · (y i)^j` is `(∏ ρ i)·∏_{i<j}(y j − y i)`.
-/
theorem halfMoment_det {F : Type*} [CommRing F] {r : ℕ} (ρ y : Fin r → F) :
    (Matrix.of (fun (i j : Fin r) => ρ i * (y i) ^ (j : ℕ))).det
      = (∏ i, ρ i) * ∏ i, ∏ j ∈ Finset.Ioi i, (y j - y i) := by
  rw [halfMoment_eq_diagonal_mul_vandermonde, Matrix.det_mul, Matrix.det_diagonal,
    Matrix.det_vandermonde]

/--
**Vandermonde independence of the half-moment columns** (§4).  With `ρ` nowhere
zero and the base points `y` distinct, the moment-curve columns
`v_y = (ρ(y), ρ(y)y, …, ρ(y)y^{r-1})` are linearly independent: multiplying the
`y`-column by `ρ(y)^{-1}` yields `(1, y, …, y^{r-1})`, and the Vandermonde
determinant is nonzero for distinct `y`.
-/
theorem halfMoment_linearIndependent {F : Type*} [Field F] {r : ℕ}
    (ρ y : Fin r → F) (hρ : ∀ i, ρ i ≠ 0) (hy : Function.Injective y) :
    LinearIndependent F
      (fun (i : Fin r) => (fun (j : Fin r) => ρ i * (y i) ^ (j : ℕ))) := by
  have hrow :
      (Matrix.of (fun (i j : Fin r) => ρ i * (y i) ^ (j : ℕ))).row =
        (fun (i : Fin r) => (fun (j : Fin r) => ρ i * (y i) ^ (j : ℕ))) := rfl
  rw [← hrow]
  apply Matrix.linearIndependent_rows_of_isUnit
  rw [Matrix.isUnit_iff_isUnit_det, halfMoment_det]
  refine IsUnit.mul ?_ ?_
  · exact isUnit_iff_ne_zero.mpr (Finset.prod_ne_zero_iff.mpr (fun i _ => hρ i))
  · refine isUnit_iff_ne_zero.mpr (Finset.prod_ne_zero_iff.mpr (fun i _ => ?_))
    refine Finset.prod_ne_zero_iff.mpr (fun j hj => ?_)
    rw [Finset.mem_Ioi] at hj
    refine sub_ne_zero.mpr (fun h => ?_)
    exact absurd (hy h.symm) (by intro hh; rw [hh] at hj; exact lt_irrefl _ hj)

/--
**Rank rigidity** (§4).  If a set `T` of half-moment columns all lie in a
submodule `W` of `Fin r → F` (e.g. the affine span of a low-rank generalized
arithmetic progression), then `|T| ≤ finrank W`.  Hence a positive-rate set of
primitive columns (`|T| ≥ c·n`) cannot lie in a rank-`o(n)` structure once
`r = Θ(n)`, which is the contradiction that closes the entropy-inverse route.
-/
theorem halfMoment_subset_rank {F : Type*} [Field F] {r : ℕ}
    (ρ y : Fin r → F) (hρ : ∀ i, ρ i ≠ 0) (hy : Function.Injective y)
    (T : Finset (Fin r)) (W : Submodule F (Fin r → F))
    (hW : ∀ i ∈ T, (fun (j : Fin r) => ρ i * (y i) ^ (j : ℕ)) ∈ W) :
    T.card ≤ Module.finrank F W := by
  set v : Fin r → (Fin r → F) :=
    fun (i : Fin r) => (fun (j : Fin r) => ρ i * (y i) ^ (j : ℕ)) with hv
  have hvli : LinearIndependent F v := halfMoment_linearIndependent ρ y hρ hy
  have hsub : LinearIndependent F (fun i : T => v i.1) :=
    hvli.comp _ (by intro a b h; exact Subtype.ext h)
  have hW' : LinearIndependent F (fun i : T => (⟨v i.1, hW i.1 i.2⟩ : W)) := by
    apply LinearIndependent.of_comp W.subtype
    simpa using hsub
  have hcard := hW'.fintype_card_le_finrank
  simpa using hcard

end QEntropyInverse
