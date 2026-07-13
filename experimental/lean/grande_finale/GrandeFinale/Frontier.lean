import Mathlib

/-!
# Frontier kernels for the remaining missing inputs of `grande_finale.tex`

This file formalizes the self-contained, theorem-level kernels surrounding the
four residual pieces that the earlier partial formalization did *not* yet cover,
as recorded in the manuscript(s) `grande_finale.tex` /
`grande_finale_bc_attempt.tex`:

1. the **composite-prefix `gcd(e,N)` repair** — the generating-function
   factorization of `prop:composite-descend`, showing a Fourier direction whose
   active indices share a divisor `e` is a quotient-scale object;
2. the **row-sharp Q atom** motivation — the exact finite fiber census of
   `prop:mode-null-false` (the mode of the first prefix is *not* the null fiber),
   together with the elementary max-fiber → cell-ledger conversion that a
   row-sharp Q atom theorem (`prob:row-sharp-q`) would feed into;
3. the **finite BC chart-decomposition audit** — the disjoint chart-cover
   counting kernel of `prob:saturated-bc`: once every residual balanced-core
   chart is either explicitly paid or reduced to a one-parameter moving-root
   pencil (each contributing at most two slopes by `cor:bc-one-pencil`), the
   total slope count is bounded by the paid caps plus twice the number of
   pencils;
4. the **adjacent deployed safe rows** — the extension-cell dimension dichotomy
   of `prop:extension-cell-target`: a positive-dimensional extension chart cannot
   fit inside the prefix-normalized adjacent headroom, so only zero-dimensional
   charts survive, and then must satisfy `Δ ≤ H_ext`; plus the four printed
   `p > H_ext` numeric comparisons.

Honest scope: as the manuscript states, the row-sharp Q atom theorem
(`prob:row-sharp-q`) and the full finite BC chart-decomposition audit
(`prob:saturated-bc`) are genuinely open *problems* — these declarations
formalize the reusable self-contained reductions and finite facts around them,
not a discharge of the open problems themselves. The astronomically large
binomial `H_ext` values (`binom(2^21, 1116048)` etc.) are not re-derived; only
the arithmetic dichotomy and the printed integer comparisons are verified.

Each declaration references the manuscript `\label{...}` it corresponds to.
-/

open scoped BigOperators
open Finset

namespace Frontier

/-! ## 1. Composite-prefix `gcd(e,N)` repair (`prop:composite-descend`) -/

/-
Composite-prefix descent, abstract product form (`prop:composite-descend`).

If a finite index set `s` maps by `g` onto a target `t` with every fiber of the
same size `e`, and the multiplicand `F` is constant on fibers of `g`
(`F x = G (g x)`), then the product over `s` factors as the product over the
quotient `t` with each factor raised to the fiber size `e`:
`∏_{x∈s} F x = ∏_{y∈t} (G y)^e`.

This is the exact reason a Fourier direction whose active indices share the
divisor `e` (so that `g(x) = h(x^e)` is constant on the `e`-element fibers of
`x ↦ x^e`) descends to a quotient-scale object rather than carrying primitive
mass.
-/
theorem composite_prefix_descend
    {S β R : Type*} [CommMonoid R] [DecidableEq β]
    (s : Finset S) (t : Finset β) (g : S → β) (F : S → R) (G : β → R) (e : ℕ)
    (hmap : ∀ x ∈ s, g x ∈ t)
    (hconst : ∀ x ∈ s, F x = G (g x))
    (hfib : ∀ y ∈ t, (s.filter (fun x => g x = y)).card = e) :
    ∏ x ∈ s, F x = ∏ y ∈ t, (G y) ^ e := by
  simp +decide only [← Finset.prod_fiberwise_of_maps_to (by tauto) F];
  refine' Finset.prod_congr rfl fun y hy => _;
  rw [ Finset.prod_congr rfl fun x hx => hconst x ( Finset.mem_filter.mp hx |>.1 ), Finset.prod_congr rfl fun x hx => by rw [ Finset.mem_filter.mp hx |>.2 ], Finset.prod_const, hfib y hy ]

/-
Composite-prefix descent, generating-function form (`prop:composite-descend`).

The manuscript's identity
`∏_{a∈S} (1 + T·ψ(g(a))) = ∏_{b∈S_e} (1 + T·ψ(h(b)))^e`,
where `g(a) = h(a^e)` is constant on the `e`-element fibers of the `e`-th power
map `a ↦ a^e` (here abstracted as `g : S → β` with all fibers of size `e`, and
the fiber value carried by `hval : β → R`). Taking `[T^m]` of both sides then
shows every such coefficient sum is a quotient-scale object.
-/
theorem composite_prefix_gen_series
    {S β R : Type*} [CommRing R] [DecidableEq β]
    (s : Finset S) (t : Finset β) (g : S → β) (hval : β → R) (e : ℕ) (T : R)
    (hmap : ∀ x ∈ s, g x ∈ t)
    (hfib : ∀ y ∈ t, (s.filter (fun x => g x = y)).card = e) :
    ∏ x ∈ s, (1 + T * hval (g x)) = ∏ y ∈ t, (1 + T * hval y) ^ e := by
  convert composite_prefix_descend s t g ( fun x => 1 + T * hval ( g x ) ) ( fun y => 1 + T * hval y ) e hmap ( fun x hx => rfl ) hfib using 1

/-! ## 2. Row-sharp Q atom: mode census and the atom→ledger reduction -/

/--
The first-prefix fiber census on `D = 𝔽₁₇ˣ` at subset size `m = 9`, `w = 1`:
`N₉(s) = #{ M ⊆ D : |M| = 9, ∑_{x∈M} x = s }`, encoded via `Fin 16 ↪ 𝔽₁₇ˣ`
by `i ↦ i+1`.
-/
def mode17Fiber (s : ZMod 17) : ℕ :=
  (Finset.univ.filter (fun A : Finset (Fin 16) =>
      A.card = 9 ∧ (A.sum (fun i => ((i : ℕ) + 1 : ZMod 17))) = s)).card

/-- Null-fiber count `N₉(0) = 672` (`prop:mode-null-false`). -/
theorem mode17_null : mode17Fiber 0 = 672 := by native_decide

/-- A nonzero fiber count `N₉(1) = 673` (`prop:mode-null-false`). -/
theorem mode17_nonnull : mode17Fiber 1 = 673 := by native_decide

/--
The mode of the first prefix is **not** the null fiber (`prop:mode-null-false`):
`N₉(0) < N₉(1)`. This is why the raw mode-at-null shortcut is not the row-sharp
Q target — the extremal atom is a nonzero (primitive twist orbit) fiber.
-/
theorem mode17_null_not_max : mode17Fiber 0 < mode17Fiber 1 := by native_decide

/-
Atom → cell-ledger conversion (`prob:row-sharp-q`).

A row-sharp Q atom theorem provides a uniform max-fiber cap `f z ≤ R` over the
contributing prefix atoms `z ∈ Z`. Summed over the cell this gives the total cell
census bound `∑_{z∈Z} f z ≤ |Z|·R`, the elementary step by which a per-atom Q
bound feeds the first-match upper ledger.
-/
theorem q_atom_cell_ledger
    {ι : Type*} (Z : Finset ι) (f : ι → ℕ) (R : ℕ)
    (hmax : ∀ z ∈ Z, f z ≤ R) :
    ∑ z ∈ Z, f z ≤ Z.card * R := by
  simpa using Finset.sum_le_sum hmax

/-! ## 3. Finite BC chart-decomposition audit (`prob:saturated-bc`) -/

/-
BC chart-decomposition audit, disjoint-cover counting kernel (`prob:saturated-bc`).

Suppose the residual balanced-core charts `charts` split disjointly into a
`paid` family (each chart `c` contributing at most `cap c` slopes) and a `pencil`
family of one-parameter moving-root locator pencils (each contributing at most
`2` slopes by `cor:bc-one-pencil`). Then the total slope count is bounded by the
paid caps plus twice the number of pencils. This is the finite audit that turns a
complete chart classification into an upper ledger.
-/
theorem bc_chart_audit
    {ι : Type*} [DecidableEq ι]
    (paid pencil : Finset ι) (cap slopes : ι → ℕ)
    (hdisj : Disjoint paid pencil)
    (hpaid : ∀ c ∈ paid, slopes c ≤ cap c)
    (hpencil : ∀ c ∈ pencil, slopes c ≤ 2) :
    ∑ c ∈ (paid ∪ pencil), slopes c ≤ (∑ c ∈ paid, cap c) + 2 * pencil.card := by
  convert Nat.add_le_add ( Finset.sum_le_sum hpaid ) ( Finset.sum_le_sum hpencil ) using 1 ; simp +decide [ Finset.sum_union hdisj ];
  simp +decide [ mul_comm ]

/-! ## 4. Adjacent deployed safe rows: extension-cell target (`prop:extension-cell-target`) -/

/-
Positive-dimensional extension charts exceed the adjacent headroom
(`prop:extension-cell-target`).

If the prefix-normalized headroom `H` satisfies `H < p` (true at all four
deployed rows, where `p > 2^30` while `H_ext` is far smaller), then any extension
chart contributing a dimension-degree term `Δ·p^e` with `Δ ≥ 1` and positive
dimension `e ≥ 1` already exceeds the headroom: `H < Δ·p^e`.
-/
theorem extension_chart_pos_dim_exceeds
    {Δ p e H : ℕ} (hΔ : 1 ≤ Δ) (he : 1 ≤ e) (hpH : H < p) :
    H < Δ * p ^ e := by
  nlinarith [ Nat.pow_le_pow_right ( by linarith : 1 ≤ p ) he ]

/-
Extension-cell dichotomy (`prop:extension-cell-target`).

With headroom `H < p`, an extension chart `Δ·p^e` with `Δ ≥ 1` that fits inside
the headroom (`Δ·p^e ≤ H`) must be zero-dimensional (`e = 0`), and then satisfies
`Δ ≤ H`. Thus only zero-dimensional charts survive, and their degree ceiling is
exactly `H_ext`.
-/
theorem extension_chart_zero_dim
    {Δ p e H : ℕ} (hΔ : 1 ≤ Δ) (hpH : H < p) (hfit : Δ * p ^ e ≤ H) :
    e = 0 ∧ Δ ≤ H := by
  rcases e with ( _ | e ) <;> simp_all +decide;
  nlinarith [ Nat.pow_le_pow_right ( by linarith : 1 ≤ p ) ( by linarith : e + 1 ≥ 1 ) ]

/-- KoalaBear MCA adjacent row: `p > H_ext` (`prop:extension-cell-target`). -/
theorem koalabear_mca_p_gt_Hext : (4807520 : ℕ) < 2 ^ 31 - 2 ^ 24 + 1 := by
  norm_num

/-- KoalaBear list adjacent row: `p > H_ext` (`prop:extension-cell-target`). -/
theorem koalabear_list_p_gt_Hext : (4226236 : ℕ) < 2 ^ 31 - 2 ^ 24 + 1 := by
  norm_num

/-- Mersenne-31 MCA adjacent row: `p > H_ext` (`prop:extension-cell-target`). -/
theorem mersenne31_mca_p_gt_Hext : (9 : ℕ) < 2 ^ 31 - 1 := by
  norm_num

/-- Mersenne-31 list adjacent row: `p > H_ext` (`prop:extension-cell-target`). -/
theorem mersenne31_list_p_gt_Hext : (8 : ℕ) < 2 ^ 31 - 1 := by
  norm_num

end Frontier