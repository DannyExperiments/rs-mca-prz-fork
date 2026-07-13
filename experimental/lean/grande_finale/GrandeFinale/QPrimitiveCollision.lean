import Mathlib
import GrandeFinale.QFourierTao
import GrandeFinale.QEntropyInverse

/-!
# Developing the entropy-inverse route to the primitive collision theorem

This file develops the **primitive logarithmic collision route** to the
prefix-flatness input `Q` (`thm:primitive-log-collision` and its proof blueprint
in `q_fourier_tao_finish_patch.tex`).  The patch reduces asymptotic `Q` to a
bound on the primitive `q`-collision moment `Γ_q^{prim}`, and its proof blueprint
proceeds through four ingredients:

1. **The moment expansion into collision tuples.**  The `q`-collision moment is,
   up to the fixed normalisation, the number of collision tuples
   `(M_1,…,M_q)` with a common prefix.  This is the exact combinatorial identity
   `∑_s N(s)^q = #{(M_1,…,M_q) : H_w 1_{M_1} = ⋯ = H_w 1_{M_q}}`
   (`collision_count_identity`).

2. **The trade formulation.**  Relative to `M_1`, each collision tuple gives
   integer-valued trades `f_i = 1_{M_i} − 1_{M_1}` with vanishing power-sum
   moments `∑_x f_i(x) x^a = 0`, `0 ≤ a ≤ w`.

3. **The deterministic low-support exclusion** ("Tao's uncertainty principle /
   BCH argument").  No nonzero primitive trade can have support at most the active
   designed distance: a nonzero function killing the moments `0,…,w` has support
   `≥ w+2` (`trade_designed_distance`), because a Vandermonde system on its
   support would otherwise force it to vanish (`moment_poly_vanishing`).  In the
   prefix-collision language this is the rigidity `|M ∆ M'| ≥ w+2` for distinct
   supports with the same degree-`≤ w` prefix (`prefix_collision_rigidity`).

4. **The Vandermonde rank rigidity** that closes the argument once the inverse
   theorem produces a low-rank structure.  This is
   `QEntropyInverse.halfMoment_subset_rank`: a positive-rate set of moment-curve
   columns cannot lie in a submodule of rank below its cardinality.

## Honest scope

The single genuinely deep step of the route — the **entropy-scale inverse
Littlewood–Offord / Balog–Szemerédi–Gowers large-spectrum theorem** that turns a
positive-rate excess `Γ_q^{prim} ≥ exp(η·n·q)` into a positive-density subfamily
of trades whose active columns lie in a rank-`o(n)` generalized coset progression
— is a genuinely open ingredient and is **not** discharged here.  What is
machine-checked below are the deterministic, self-contained atoms of the route
(items 1–3 above, together with item 4 already in `QEntropyInverse`), which are
exactly the pieces the open inverse theorem consumes and produces.
-/

open scoped BigOperators
open Polynomial
open Classical

namespace QPrimitiveCollision

/-! ## 1. The moment expansion into collision tuples -/

/--
**Collision-count identity** (moment expansion, §"Expand the `q`-collision
moment").  For a prefix map `H : α → β` on a finite domain and an order `q ≥ 1`,
the number of `q`-tuples `t : Fin q → α` whose images `H (t i)` are all equal
(the collision tuples) equals `∑_s |fiber s|^q`, the sum of `q`-th powers of the
prefix-fiber sizes.  This is the exact identity behind
`Γ_q = |B|^{w(q-1)}/binom(n,m)^q · #{collision tuples}`.
-/
theorem collision_count_identity {α β : Type*} [Fintype α] [DecidableEq β]
    (H : α → β) (q : ℕ) (hq : 1 ≤ q) :
    (Finset.univ.filter (fun t : Fin q → α => ∀ i j, H (t i) = H (t j))).card
      = ∑ s ∈ Finset.univ.image H,
          (Finset.univ.filter (fun a => H a = s)).card ^ q := by
  classical
  rw [Finset.card_eq_sum_card_fiberwise
      (f := fun t : Fin q → α => H (t ⟨0, hq⟩)) (t := Finset.univ.image H)]
  · apply Finset.sum_congr rfl
    intro s _
    have hset :
        (Finset.univ.filter (fun t : Fin q → α => ∀ i j, H (t i) = H (t j))).filter
            (fun t => H (t ⟨0, hq⟩) = s)
          = Fintype.piFinset (fun _ : Fin q =>
              Finset.univ.filter (fun a => H a = s)) := by
      ext t
      simp only [Finset.mem_filter, Finset.mem_univ, true_and, Fintype.mem_piFinset]
      constructor
      · rintro ⟨hall, h0s⟩ i
        rw [hall i ⟨0, hq⟩, h0s]
      · intro hi
        exact ⟨fun i j => by rw [hi i, hi j], hi ⟨0, hq⟩⟩
    rw [hset, Fintype.card_piFinset]
    simp
  · intro t _
    exact Finset.mem_image_of_mem H (Finset.mem_univ _)

/-! ## 2–3. The deterministic low-support exclusion -/

/--
**Moment vanishing implies polynomial vanishing.**  If a weighting `f : ι → F`
kills every power-sum moment `∑_i f i (x i)^a` for `0 ≤ a ≤ w`, then it kills the
evaluation of *any* polynomial of degree `≤ w`: `∑_i f i · q(x i) = 0`.  This is
the linear-algebra core of the BCH/uncertainty-principle exclusion.
-/
theorem moment_poly_vanishing {F ι : Type*} [Field F] [Fintype ι] (x : ι → F)
    (f : ι → F) (w : ℕ) (hmom : ∀ a, a ≤ w → ∑ i, f i * (x i)^a = 0)
    (q : F[X]) (hq : q.natDegree ≤ w) :
    ∑ i, f i * q.eval (x i) = 0 := by
  have hev : ∀ i, q.eval (x i) = ∑ a ∈ Finset.range (w+1), q.coeff a * (x i)^a := by
    intro i; rw [Polynomial.eval_eq_sum_range' (Nat.lt_succ_of_le hq)]
  simp_rw [hev, Finset.mul_sum]
  rw [Finset.sum_comm]
  apply Finset.sum_eq_zero
  intro a ha
  rw [Finset.mem_range] at ha
  have hpull : ∑ i, f i * (q.coeff a * (x i)^a) = q.coeff a * ∑ i, f i * (x i)^a := by
    rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro i _; ring
  rw [hpull, hmom a (by omega), mul_zero]

/--
**Deterministic low-support exclusion / designed distance**
("Tao's uncertainty principle / BCH argument").  Let the base points `x` be
distinct.  A nonzero weighting `f : ι → F` that kills all power-sum moments
`∑_i f i (x i)^a`, `0 ≤ a ≤ w`, must have support of size at least `w + 2`.

Equivalently: no nonzero primitive trade can have support at most the active
designed distance `w + 1`.  The proof is the Vandermonde minimum-distance
argument — if the support `T` had `|T| ≤ w+1`, evaluating the degree-`(|T|-1)`
node polynomial `∏_{k∈T∖{j}}(X − x_k)` against the moments (via
`moment_poly_vanishing`) would force each `f j = 0`.
-/
theorem trade_designed_distance {F ι : Type*} [Field F] [Fintype ι] (x : ι → F)
    (hx : Function.Injective x) (f : ι → F) (w : ℕ)
    (hmom : ∀ a, a ≤ w → ∑ i, f i * (x i)^a = 0) (hf : f ≠ 0) :
    w + 2 ≤ (Finset.univ.filter (fun i => f i ≠ 0)).card := by
  classical
  set T := Finset.univ.filter (fun i => f i ≠ 0) with hT
  by_contra hcon
  push_neg at hcon
  have hTne : T.Nonempty := by
    rw [Finset.filter_nonempty_iff]
    by_contra h
    push_neg at h
    apply hf; funext i; simpa using h i (Finset.mem_univ i)
  obtain ⟨j, hjT⟩ := hTne
  have hjf : f j ≠ 0 := (Finset.mem_filter.mp hjT).2
  set p : F[X] := ∏ i ∈ (T.erase j), (X - C (x i)) with hp
  have hdeg : p.natDegree ≤ w := by
    rw [hp]
    refine le_trans (Polynomial.natDegree_prod_le (T.erase j) (fun i => (X - C (x i)))) ?_
    have hone : ∀ i ∈ T.erase j, (X - C (x i)).natDegree = 1 := by
      intro i _; rw [Polynomial.natDegree_X_sub_C]
    rw [Finset.sum_congr rfl hone]
    simp only [smul_eq_mul, mul_one, Finset.sum_const,
      Finset.card_erase_of_mem hjT]
    have hc := Finset.card_erase_add_one hjT
    omega
  have hvan := moment_poly_vanishing x f w hmom p hdeg
  have heval : ∀ i, p.eval (x i) = ∏ k ∈ (T.erase j), (x i - x k) := by
    intro i; rw [hp, Polynomial.eval_prod]; apply Finset.prod_congr rfl; intro k _; simp
  have hsum : ∑ i, f i * p.eval (x i) = f j * p.eval (x j) := by
    rw [Finset.sum_eq_single j]
    · intro i _ hij
      by_cases hi : i ∈ T
      · rw [heval, Finset.prod_eq_zero (Finset.mem_erase.mpr ⟨hij, hi⟩) (by simp)]; ring
      · rw [hT, Finset.mem_filter] at hi
        push_neg at hi
        rw [hi (Finset.mem_univ i)]; ring
    · intro h; exact absurd (Finset.mem_univ j) h
  rw [hsum] at hvan
  have hpj : p.eval (x j) ≠ 0 := by
    rw [heval]
    apply Finset.prod_ne_zero_iff.mpr
    intro k hk
    rw [Finset.mem_erase] at hk
    exact sub_ne_zero.mpr (fun h => hk.1 (hx h).symm)
  rcases mul_eq_zero.mp hvan with h | h
  · exact hjf h
  · exact hpj h

/--
**Prefix-collision rigidity** (moment form).  If two supports `M, M' ⊆ ι` carry
the same degree-`≤ w` prefix — i.e. `∑_{i∈M}(x i)^a = ∑_{i∈M'}(x i)^a` for
`0 ≤ a ≤ w` — and `M ≠ M'`, then their symmetric difference has size at least
`w + 2`.  This is the trade formulation (items 2–3): the difference indicator
`1_M − 1_{M'}` is a nonzero trade with vanishing moments and support `M ∆ M'`, so
`trade_designed_distance` applies.  It is the moment-based analogue (with the
sharper designed distance `w+2`) of the locator-degree rigidity
`SP.prefix_rigidity`.
-/
theorem prefix_collision_rigidity {F ι : Type*} [Field F] [Fintype ι] (x : ι → F)
    (hx : Function.Injective x) (w : ℕ) (M M' : Finset ι)
    (hpre : ∀ a, a ≤ w → ∑ i ∈ M, (x i)^a = ∑ i ∈ M', (x i)^a)
    (hne : M ≠ M') :
    w + 2 ≤ ((M \ M') ∪ (M' \ M)).card := by
  classical
  set f : ι → F :=
    fun i => (if i ∈ M then (1:F) else 0) - (if i ∈ M' then 1 else 0) with hf
  have hmom : ∀ a, a ≤ w → ∑ i, f i * (x i)^a = 0 := by
    intro a ha
    have hval : ∑ i, f i * (x i)^a = (∑ i ∈ M, (x i)^a) - (∑ i ∈ M', (x i)^a) := by
      simp only [hf, sub_mul, Finset.sum_sub_distrib, ite_mul, one_mul, zero_mul,
        Finset.sum_ite_mem, Finset.univ_inter]
    rw [hval, hpre a ha, sub_self]
  have hfne : f ≠ 0 := by
    intro h
    apply hne
    ext i
    have hi := congrFun h i
    simp only [hf] at hi
    by_cases hM : i ∈ M <;> by_cases hM' : i ∈ M' <;> simp_all
  have hcard := trade_designed_distance x hx f w hmom hfne
  have hset : (Finset.univ.filter (fun i => f i ≠ 0)) = (M \ M') ∪ (M' \ M) := by
    ext i
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, hf, Finset.mem_union,
      Finset.mem_sdiff]
    by_cases hM : i ∈ M <;> by_cases hM' : i ∈ M' <;> simp [hM, hM']
  rwa [hset] at hcard

/--
**Prefix injectivity on small supports.**  If two supports `M, M'` are small
enough that `|M| + |M'| ≤ w + 1`, then the degree-`≤ w` prefix map is injective
on them: sharing the same prefix forces `M = M'`.  This is the concrete form of
"no primitive positive-rate excess at low support": the number of distinct small
supports realising a given prefix is one.  It follows from
`prefix_collision_rigidity`, since `|M ∆ M'| ≤ |M| + |M'| ≤ w + 1 < w + 2`.
-/
theorem prefix_injective_on_small {F ι : Type*} [Field F] [Fintype ι] (x : ι → F)
    (hx : Function.Injective x) (w : ℕ) (M M' : Finset ι)
    (hsmall : M.card + M'.card ≤ w + 1)
    (hpre : ∀ a, a ≤ w → ∑ i ∈ M, (x i)^a = ∑ i ∈ M', (x i)^a) :
    M = M' := by
  classical
  by_contra hne
  have hrig := prefix_collision_rigidity x hx w M M' hpre hne
  have hle : ((M \ M') ∪ (M' \ M)).card ≤ M.card + M'.card := by
    refine le_trans (Finset.card_union_le _ _) ?_
    exact Nat.add_le_add (Finset.card_le_card (Finset.sdiff_subset))
      (Finset.card_le_card (Finset.sdiff_subset))
  omega

end QPrimitiveCollision
