# Summary of changes for run bd890afe-b644-4f9c-87fe-39c668dbde5e
I formalized part (c) of the main theorem — the number-theoretic (cyclotomic sieve) density statement — in `RS_disproof_v3.lean`, extending the existing `RSLocator` development. Aristotle reported that the file builds cleanly with no `sorry` and no added axioms (`thm_main_c` depends only on `propext`, `Classical.choice`, `Quot.sound`).

Added declarations:

- `epsMca_ge_restrictedSumset_full`: the full-domain (`a = 1`, `Q = D`) form of the quotient-locator lower bound, `ε_mca(RS[F,D,k], δ) ≥ |ℓ^∧D| / q` for every radius `δ ≥ 1 − ρ − 1/n`.
- `epsMca_ge_density_full`: the density reduction — if the restricted sumset satisfies `|ℓ^∧D| ≥ q / C`, then `ε_mca(RS[F,D,k], δ) ≥ 1/C`. This is exactly the step "the MCA statement follows from the quotient-locator lemma with `D = Q`, `a = 1`" in the sieve proof.
- `thm_main_c` (Theorem 2.1(c)): from the density conclusion of the cyclotomic sieve theorem, there are infinitely many primes `p` (i.e. for every bound `X` a prime `p > X`) carrying an order-`N` subgroup `Q ≤ 𝔽_p^×` for which the MCA error at radius `1 − ρ − 1/N` is at least `(log₂ p)^{-6}`, an inverse-polynomial (non-negligible) function of the security parameter.

Scope decision (matching the file's existing precedent for part (a)'s Dias da Silva–Hamidoune coverage): the sieve's sole genuinely-external analytic input, the Siegel–Walfisz theorem, is not in Mathlib. I therefore take the sieve's restricted-sumset density conclusion as the explicit hypothesis `hsieve` — precisely how the paper *imports* Siegel–Walfisz — and the content proved here is the (non-trivial) reduction from that density to the MCA obstruction, carried out over the prime fields `ZMod p`. The concrete numeric verification records (Appendix V1–V5) were, as requested, not formalized.

In this repository, verify the package locally before treating the build claim
as checked.

# Summary of changes for run 6bd7afbd-40c4-4c5a-82ae-cac0908d39f0
I formalized the self-contained algebraic core of the paper "Capacity-Edge Obstructions to Reed–Solomon Mutual Correlated Agreement over Smooth Multiplicative Domains" (`RS_disproof_v3.tex`) into a single Lean file, `RS_disproof_v3.lean`. Aristotle reported that the project builds cleanly with no warnings, no `sorry`, and no added axioms; the main theorems depend only on the standard `propext`, `Classical.choice`, `Quot.sound`.

What is formalized (all proofs complete):

- The **quotient locator polynomial** `locator A a = ∏_{b∈A}(X^a - b)` and its two basic facts (`locator_eq_expand`, `locator_eval_zero`).
- The **locator decomposition** `locator_decomp` (the heart of the paper's "Quotient locator" lemma): for `a ≥ 1` and `k = a·(|A|−1)`, the locator equals `X^{k+a} + (−∑A)·X^k + R` with `deg R < k`.
- A faithful **MCA framework**: `RSagrees` (agreement with a degree-`<k` Reed–Solomon codeword on a support set), `badAt`/`badSet` (the "bad slope" condition of the paper's MCA definition), and `epsMca` (the support-wise line-MCA error as a max over line pairs). Includes the "no low-degree explanation" step `not_RSagrees_pow`.
- **Monotonicity** of `epsMca` in the radius (`epsMca_mono`), plus `epsMca_le_one`.
- The **quotient locator lemma** `locator_bad` and its lower bound `epsMca_ge_restrictedSumset`: `ε_mca(RS[F,D,k], δ) ≥ |ℓ^∧Q|/q` for every radius `δ ≥ 1−ρ−1/N`.
- **Theorem 2.1(a)** `epsMca_eq_one_of_cover`: under full restricted-sumset coverage the MCA error is exactly `1` on the whole radius interval.
- **Theorem 2.1(d)** `list_lower_bound`: a worst-case list lower bound — some slope `z` yields at least `C(N,ℓ)/q` Reed–Solomon codewords agreeing with `x^{k+a}+z·x^k` on the fiber `S_A`, via a pigeonhole argument.
- `a = 1` **full-domain specializations** (`epsMca_eq_one_of_cover_full`, `list_lower_bound_full`) matching the paper's deployed multiplicative-domain setting (Theorem 2.1(b,c,d)). These also confirm the abstract quotient-configuration hypotheses are non-vacuously satisfiable (they hold for any finite domain with `a = 1`).

Scope decisions: the deep external inputs the paper imports but does not prove (Dias da Silva–Hamidoune coverage; Siegel–Walfisz for the sieve) are not in Mathlib, so I encoded them as explicit hypotheses of the theorems that consume them (e.g. the coverage hypothesis `restrictedSumset Q ℓ = univ` in Theorem (a)), rather than introducing any axioms. The multiplicative-subgroup structure of a smooth domain enters only through the fiber-size hypothesis `hfib` (each fiber of `x ↦ x^a` has size `a`), which is a faithful and satisfiable abstraction. The number-theoretic sieve density statement (part c) and the concrete numeric verification records (Appendix V1–V5) were not formalized; the reusable locator/MCA/list machinery above is the mathematical engine underlying all four parts of the main theorem.

In this repository, verify the package locally before treating the build claim
as checked.
