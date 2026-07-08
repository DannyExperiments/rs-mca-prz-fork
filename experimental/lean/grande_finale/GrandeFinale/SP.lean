import Mathlib
import GrandeFinale

/-!
# The SP program: primitive shift-pair control (`grande_finale.tex`, `\S`"Proved Prefix and Split-Pencil Reductions")

This file formalizes the *theorem-level*, self-contained parts of the SP program
of the manuscript — the proved reductions that surround the open conjecture SP
(`conj:SP`, "primitive shift-pair control").  SP itself is a genuinely open
research conjecture: it is an asymptotic `e^{o(n)}` statement about a primitive
shift-pair census, together with finite constants at four deployed rows resting on
external certificate packets, and it is *not* a self-contained theorem.  What is
proved here are the surrounding reductions that the manuscript records as already
theorem-level:

* the exact quotient-pullback depth transformation (`prop:sp-pullback`,
  `thm:coeff-quotient-extract`);
* the coefficient-scale gcd detection of quotient support (`lem:coeff-scale`) and
  the primitive-exclusion criterion for the binomial prototypes
  (`cor:primitive-coeff-exclusion`);
* the top-stratum quotient sieve depth collapse (`prop:top-stratum-quotient-sieve`);
* the locator factorization `ℓ_M - ℓ_{M'} = ℓ_R·(A - B)` and the prefix-collision
  rigidity `|M∖M'| ≥ w+1` (`prop:prefix-rigidity`), the structural fact that makes
  the primitive shift-pair census sharply structured;
* the abstract `Γ₂` ledger split into diagonal, quotient, and primitive parts
  (`prop:gamma2-ledger`).

Each declaration references the `\label{...}` of the manuscript statement it
formalizes.
-/

open scoped BigOperators
open scoped Classical
open Polynomial

namespace GrandeFinale.SP

/-! ## Quotient-pullback depth (`prop:sp-pullback`, `thm:coeff-quotient-extract`)

For a shift pair `A(X) = A₀(Xᶜ)`, `B(X) = B₀(Xᶜ)` of degree `e = c·e₀`, the
difference `A - B = (A₀ - B₀)(Xᶜ)` has degree `c·deg(A₀ - B₀)`.  Writing
`D = deg(A₀ - B₀)`, the upstairs depth-`w` condition `deg(A - B) ≤ e - w - 1`
becomes `c·D ≤ c·e₀ - (w+1)`, and the downstairs depth is
`w_c = ⌈(w+1)/c⌉ - 1`, whose condition is `D ≤ e₀ - ⌈(w+1)/c⌉`.  The following
is the exact integer equivalence between the two (stated without truncated
subtraction). -/

/-- The descended depth `w_c = ⌈(w+1)/c⌉ - 1` of the quotient pullback. -/
def descendedDepth (w c : ℕ) : ℕ := (w + 1) ⌈/⌉ c - 1

/--
Quotient-pullback depth equivalence (`prop:sp-pullback`).  With `D = deg(A₀-B₀)`
and `e = c·e₀`, the upstairs depth-`w` shift-pair condition
`c·D + (w+1) ≤ c·e₀` is equivalent to the downstairs condition
`D + ⌈(w+1)/c⌉ ≤ e₀` at depth `w_c = ⌈(w+1)/c⌉ - 1`.
-/
theorem sp_pullback_depth (c e0 w D : ℕ) (hc : 0 < c) :
    c * D + (w + 1) ≤ c * e0 ↔ D + (w + 1) ⌈/⌉ c ≤ e0 := by
  constructor <;> intro h <;> rw [ Nat.ceilDiv_eq_add_pred_div ] at *;
  · nlinarith [ Nat.div_mul_le_self ( w + 1 + c - 1 ) c, Nat.sub_add_cancel ( by linarith : 1 ≤ w + 1 + c ) ];
  · nlinarith [ Nat.div_add_mod ( w + 1 + c - 1 ) c, Nat.mod_lt ( w + 1 + c - 1 ) hc, Nat.sub_add_cancel ( by linarith : 1 ≤ w + 1 + c ) ]

/-! ## Coefficient scale and quotient detection (`def:coefficient-scale`, `lem:coeff-scale`)

For a monic degree-`e` split locator `L(X) = X^e + ∑_j λ_j X^{e-j}`, the
coefficient scale is `s(L) = gcd(n, e, {j : λ_j ≠ 0})`, where `n` is the coset
length.  We model the nonzero coefficient gaps by a finite set `S ⊆ ℕ`. -/

/-- The coefficient scale `s(L) = gcd(n, e, {j : λ_j ≠ 0})`, with the nonzero
coefficient gaps recorded as a finite set `S`. (`def:coefficient-scale`.) -/
def coeffScale (n e : ℕ) (S : Finset ℕ) : ℕ := Nat.gcd (Nat.gcd n e) (S.gcd id)

/-- The pair coefficient scale `s(A,B) = gcd(s(A), s(B))`. (`def:coefficient-scale`.) -/
def coeffScalePair (n e : ℕ) (SA SB : Finset ℕ) : ℕ :=
  Nat.gcd (coeffScale n e SA) (coeffScale n e SB)

/--
Coefficient scale detects quotient support (`lem:coeff-scale`, arithmetic
kernel): `c ∣ s(L)` iff `c ∣ n`, `c ∣ e`, and `c` divides every nonzero
coefficient gap.  This is the gcd characterization behind the statement that
`c ∣ s(L)` iff `L(X) = L_c(Xᶜ)`, i.e. the support is a union of `x ↦ xᶜ` fibers.
-/
theorem dvd_coeffScale (c n e : ℕ) (S : Finset ℕ) :
    c ∣ coeffScale n e S ↔ c ∣ n ∧ c ∣ e ∧ ∀ j ∈ S, c ∣ j := by
  simp +decide only [coeffScale, Nat.dvd_gcd_iff, Finset.dvd_gcd_iff];
  tauto

/--
Divisibility of the pair scale: `c ∣ s(A,B)` iff `c` divides both single scales.
-/
theorem dvd_coeffScalePair (c n e : ℕ) (SA SB : Finset ℕ) :
    c ∣ coeffScalePair n e SA SB ↔ c ∣ coeffScale n e SA ∧ c ∣ coeffScale n e SB := by
  exact Nat.dvd_gcd_iff

/--
Primitive exclusion of the binomial prototype (`cor:primitive-coeff-exclusion`).
The top-stratum binomial prototype `A = X^{w+1} - β` has its only nonzero
coefficient gap at `w+1 = e`, so when it splits over the order-`n` coset
(forcing `(w+1) ∣ n`) its coefficient scale is exactly `w+1`.  Hence for
`w ≥ 1` the prototype is quotient-borne (`s > 1`), never primitive.
-/
theorem binomial_coeffScale (n w : ℕ) (h : (w + 1) ∣ n) :
    coeffScale n (w + 1) {w + 1} = w + 1 := by
  obtain ⟨ k, rfl ⟩ := h;
  unfold coeffScale; simp +decide ;

/-! ## Top-stratum quotient sieve (`prop:top-stratum-quotient-sieve`) -/

/--
When `c ∣ (w+1)`, the ceiling `⌈(w+1)/c⌉` is the exact quotient `(w+1)/c`.
-/
theorem ceilDiv_of_dvd {c w : ℕ} (hc : 0 < c) (h : c ∣ (w + 1)) :
    (w + 1) ⌈/⌉ c = (w + 1) / c := by
  rw [ Nat.ceilDiv_eq_add_pred_div, Nat.add_sub_assoc hc ];
  · obtain ⟨ k, hk ⟩ := h; simp +arith +decide [ *, Nat.add_div ] ;

/--
Top-stratum quotient sieve depth collapse (`prop:top-stratum-quotient-sieve`).
At the top stratum `e = w+1`, if `c ∣ (w+1)` with `c > 0`, the descended degree
`e_c = (w+1)/c` and descended depth `w_c = (w+1)/c - 1` satisfy
`e_c ≤ w_c + 1`, i.e. the descended difference has degree `≤ 0` — the pair is
paid by a top-stratum constant-shift cell on the quotient coset.
-/
theorem top_stratum_depth {c w : ℕ} (hc : 0 < c) (h : c ∣ (w + 1)) :
    (w + 1) / c ≤ descendedDepth w c + 1 := by
  rw [ descendedDepth, ceilDiv_of_dvd hc h ];
  omega

/-! ## Locator factorization and prefix-collision rigidity (`prop:prefix-rigidity`, `prop:second-moment`)

The locator `ℓ_S(X) = ∏_{x∈S}(X - x)` is monic of degree `|S|`.  For two supports
`M, M'` with common part `R = M∩M'`, `A = ℓ_{M∖M'}`, `B = ℓ_{M'∖M}`, one has
`ℓ_M - ℓ_{M'} = ℓ_R·(A - B)`, the encoding of off-diagonal prefix collisions used
in the exact second moment. -/

variable {F : Type*} [Field F]

/-- The locator polynomial `ℓ_S(X) = ∏_{x∈S}(X - x)`. -/
noncomputable def locator (S : Finset F) : F[X] := ∏ x ∈ S, (X - C x)

/--
The locator is monic.
-/
theorem locator_monic (S : Finset F) : (locator S).Monic := by
  exact Polynomial.monic_prod_of_monic _ _ fun x hx => Polynomial.monic_X_sub_C x

/--
The locator has degree `|S|`.
-/
theorem locator_natDegree (S : Finset F) : (locator S).natDegree = S.card := by
  rw [ locator, Polynomial.natDegree_prod_of_monic ];
  · simp +decide [ Polynomial.natDegree_sub_eq_left_of_natDegree_lt ];
  · exact fun x hx => Polynomial.monic_X_sub_C x

/--
The locator is injective on finsets: `ℓ_M = ℓ_{M'}` iff `M = M'`.
-/
theorem locator_injective : Function.Injective (locator (F := F)) := by
  intro S T h_eq
  have h_roots : S.val = T.val := by
    unfold locator at h_eq;
    apply_fun Polynomial.roots at h_eq ; simp_all +decide [ Polynomial.roots_prod_X_sub_C ]
  exact Finset.val_inj.mp h_roots

/--
Locator factorization (`prop:second-moment`, `prop:prefix-rigidity`):
`ℓ_M - ℓ_{M'} = ℓ_{M∩M'}·(ℓ_{M∖M'} - ℓ_{M'∖M})`.  This is the bijective encoding
of an off-diagonal prefix-collision pair by its common part together with a
disjoint-root shift pair.
-/
theorem locator_diff_factor (M M' : Finset F) :
    locator M - locator M'
      = locator (M ∩ M') * (locator (M \ M') - locator (M' \ M)) := by
  -- Unfold `locator`.
  have hM : locator M = locator (M ∩ M') * locator (M \ M') := by
    unfold locator; rw [ ← Finset.prod_union ( Finset.disjoint_right.mpr fun x hx => by aesop ) ] ; congr; ext; by_cases h : ‹F› ∈ M' <;> simp +decide [ h ] ;
  have hM' : locator M' = locator (M ∩ M') * locator (M' \ M) := by
    unfold locator;
    rw [ ← Finset.prod_union ];
    · congr with x ; by_cases hx : x ∈ M <;> simp +decide [ hx ];
    · exact Finset.disjoint_left.mpr fun x hx₁ hx₂ => Finset.mem_sdiff.mp hx₂ |>.2 ( Finset.mem_inter.mp hx₁ |>.1 );
  rw [ hM, hM', mul_sub ]

/--
Prefix-collision rigidity (`prop:prefix-rigidity`).  If `M ≠ M'` and `M` is an
`m`-subset carrying the same identity prefix as `M'` — encoded as
`deg(ℓ_M - ℓ_{M'}) ≤ m - w - 1`, i.e. `(ℓ_M - ℓ_{M'}).natDegree + (w+1) ≤ m` —
then the symmetric difference satisfies `|M∖M'| ≥ w+1`.  This is the structural
fact that makes the primitive shift-pair census sharply structured.  (The
manuscript states this for two `m`-subsets; the hypothesis `M'.card = m` turns
out to be unnecessary for the conclusion and is omitted.)
-/
theorem prefix_rigidity (m w : ℕ) (M M' : Finset F)
    (hM : M.card = m) (hne : M ≠ M')
    (hdeg : (locator M - locator M').natDegree + (w + 1) ≤ m) :
    w + 1 ≤ (M \ M').card := by
  -- By `locator_diff_factor`, we have `locator M - locator M' = locator (M ∩ M') * (locator (M \ M') - locator (M' \ M))`.
  have h_diff : locator M - locator M' = locator (M ∩ M') * (locator (M \ M') - locator (M' \ M)) :=
    locator_diff_factor M M'
  rw [ h_diff, Polynomial.natDegree_mul' ] at hdeg;
  · grind +suggestions;
  · by_cases h : ( locator ( M \ M' ) - locator ( M' \ M ) ) = 0 <;> simp_all +decide [ locator_monic ];
    simp_all +decide [ sub_eq_zero, locator_injective.eq_iff ]

/-! ## SP from Q: prefix flatness controls the primitive shift-pair census (`conj:Q` ⟹ `conj:SP`)

The manuscript records that SP "controls the primitive part of the collision
ledger needed to make Q worst-case rather than average-case" and that in the
asymptotic closure "the prefix boundary cell is paid by Q ... and the primitive
second-moment cell by SP" (`conj:SP`, `thm:asymptotic`).  We make the precise
implication **Q ⟹ SP** into a proved theorem.

Recall the exact second-moment ledger (`prop:second-moment`, `prop:gamma2-ledger`):
with `f z = |Φ_w⁻¹(z)|` the primitive-fiber sizes over the prefix values `z`, the
total is `∑_z f z = binom(n,m)` and the *primitive shift-pair census* is the
off-diagonal second moment
`∑_z f z (f z - 1)`.
Conjecture Q is the maximum-fiber (prefix-flatness) bound
`f z ≤ R_Q · binom(n,m) · |B|⁻ʷ`, and the quotient-normalized density prediction
for the pair census is `binom(n,m)² · |B|⁻ʷ`.  The theorems below show that the
maximum-fiber bound forces the census to be at most the density prediction times
the *same* factor, i.e. `R_SP = R_Q`. -/

/-
Pair-census engine (`ℕ` form).  If every fiber `f z` is bounded by `B`, then the
primitive shift-pair census `∑_z f z (f z - 1)` is at most `(∑_z f z)·(B - 1)`.
This is the elementary counting core of `Q ⟹ SP`: a uniform max-fiber cap turns
into a linear bound on the off-diagonal second moment.
-/
theorem pair_census_le_of_max_fiber {ι : Type*} (s : Finset ι) (f : ι → ℕ) (B : ℕ)
    (hB : ∀ z ∈ s, f z ≤ B) :
    ∑ z ∈ s, f z * (f z - 1) ≤ (∑ z ∈ s, f z) * (B - 1) := by
  rw [ Finset.sum_mul _ _ _ ];
  exact Finset.sum_le_sum fun x hx => Nat.mul_le_mul_left _ ( Nat.sub_le_sub_right ( hB x hx ) _ )

/-
**Q ⟹ SP** (density form).  Let `f z ≥ 0` be the primitive-fiber sizes over the
prefix values `s`, with total `∑_z f z = Nsub` (the number of primitive
`m`-subsets, `binom(n,m)`) and `Bw > 0` the number of prefix values (`|B|ʷ`).
The prefix-flatness bound Q, `f z ≤ R_Q · Nsub / Bw` for all `z`, implies the SP
bound: the primitive shift-pair census `∑_z f z (f z - 1)` is at most the
quotient-normalized density prediction `Nsub² / Bw` times `R_SP = R_Q`.
(The positivity of `Bw = |B|ʷ` is not needed for this inequality and is omitted.)
-/
theorem sp_from_q {ι : Type*} (s : Finset ι) (f : ι → ℝ)
    (Nsub Bw RQ : ℝ) (hf : ∀ z ∈ s, 0 ≤ f z)
    (hsum : ∑ z ∈ s, f z = Nsub)
    (hQ : ∀ z ∈ s, f z ≤ RQ * Nsub / Bw) :
    ∑ z ∈ s, f z * (f z - 1) ≤ RQ * (Nsub ^ 2 / Bw) := by
  have h_sum : ∑ z ∈ s, f z * (f z - 1) ≤ ∑ z ∈ s, f z * (RQ * Nsub / Bw - 1) :=
    Finset.sum_le_sum fun z hz => mul_le_mul_of_nonneg_left (sub_le_sub_right (hQ z hz) _) (hf z hz)
  have hNsub : 0 ≤ Nsub := hsum ▸ Finset.sum_nonneg hf
  rw [← Finset.sum_mul, hsum] at h_sum
  have key : Nsub * (RQ * Nsub / Bw - 1) = RQ * (Nsub ^ 2 / Bw) - Nsub := by ring
  linarith [h_sum, key.le, hNsub]

/--
**Q ⟹ SP** (normalized `Γ₂` form).  In the normalization of `prop:gamma2-ledger`,
the primitive shift-pair contribution to `Γ₂`, namely
`Bw · (∑_z f z (f z - 1)) / Nsub²`, is at most `R_SP = R_Q`.  This is exactly the
statement that the primitive shift-pair strata contribute no more than the
quotient-normalized density prediction times `R_SP` (`conj:SP`), with the SP
factor equal to the Q factor.
-/
theorem sp_from_q_normalized {ι : Type*} (s : Finset ι) (f : ι → ℝ)
    (Nsub Bw RQ : ℝ) (hf : ∀ z ∈ s, 0 ≤ f z)
    (hBw : 0 < Bw) (hN : 0 < Nsub) (hsum : ∑ z ∈ s, f z = Nsub)
    (hQ : ∀ z ∈ s, f z ≤ RQ * Nsub / Bw) :
    Bw * ((∑ z ∈ s, f z * (f z - 1)) / Nsub ^ 2) ≤ RQ := by
  have h := sp_from_q s f Nsub Bw RQ hf hsum hQ
  have hpos : (0 : ℝ) < Nsub ^ 2 := by positivity
  have hstep : Bw * ((∑ z ∈ s, f z * (f z - 1)) / Nsub ^ 2)
      ≤ Bw * (RQ * (Nsub ^ 2 / Bw) / Nsub ^ 2) :=
    mul_le_mul_of_nonneg_left (by gcongr) hBw.le
  have heq : Bw * (RQ * (Nsub ^ 2 / Bw) / Nsub ^ 2) = RQ := by
    field_simp
  linarith [hstep, heq.ge]

/-! ## The primitive `L²` ledger split (`prop:gamma2-ledger`) -/

/--
Exact primitive `L²` ledger (`prop:gamma2-ledger`, arithmetic kernel).  Dividing
the exact second-moment identity `T = diagonal + ∑ (P_quot + P_prim)` by the
normalization `nrm` splits `Γ₂` into a diagonal term, a quotient term, and a
primitive term; SP is exactly the task of bounding the last summand.  Here we
record the underlying algebraic split for arbitrary real weights.
-/
theorem gamma2_ledger_split {ι : Type*} (s : Finset ι)
    (diagonal : ℝ) (Pquot Pprim : ι → ℝ) (nrm : ℝ) :
    (diagonal + ∑ e ∈ s, (Pquot e + Pprim e)) / nrm
      = diagonal / nrm + (∑ e ∈ s, Pquot e) / nrm + (∑ e ∈ s, Pprim e) / nrm := by
  simp +decide only [Finset.sum_add_distrib, add_div] ; ring

end GrandeFinale.SP