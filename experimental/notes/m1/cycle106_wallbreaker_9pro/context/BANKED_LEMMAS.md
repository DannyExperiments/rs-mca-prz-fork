# Current Banked Lemma - 2026-06-21 Cycle 105

```text
L-CYCLE105-KFREE-COLLAPSE-AND-COMPLEMENT-DUALITY
```

For `s=sigma+k`, bandwidth-`k` activity is exactly:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s,
M_s = {((-1)^l e_l(Sbar))_{l=1}^{sigma+1}: |Sbar|=s}.
```

Therefore all bandwidths share the same fixed rational curve `Gamma`; `k` only
changes the subset-size layer `M_s`.

The complement identity `g_Sbar g_{H\Sbar}=1-X^n` gives a fixed triangular
automorphism identifying `M_s` and `M_{n-s}`.

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle105_kfree_collapse_check.py
```

with `PASS`.

# Current Banked Lemma - 2026-06-21 Cycle 104

```text
L-CYCLE104-FIXED-BANDWIDTH-DIVISOR-INCIDENCE
```

For every fixed bandwidth `k`, Cycle104 proves:

```text
|Theta_U| <= binom(n,k)(sigma+1).
```

The reverse co-locator form is:

```text
theta active
<=> exists psi, deg psi <= k-2, such that
    B_theta(X)+psi(X) is a degree-s divisor of X^n-1.
```

For `k=2`, active theta forces a pair collision of `B_theta` on `mu_n`.
For fixed `k`, active theta forces a zero order-`k-1` divided difference on
some `k`-subset. Each obstruction is monic of degree `sigma+1` in theta.

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle104_fixed_k_divisor_incidence_check.py
```

with `PASS`.

The next wall is `W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE`.

# Previous Banked Lemma - 2026-06-21 Cycle 103

```text
L-CYCLE103-B1-E1-IMAGE-BOUND
```

For bandwidth `k=1`, so `s=sigma+1`, Cycle103 proves:

```text
|Theta_U| = |e_1(V)| <= (n-sigma+1)(sigma+1) = O(n^2).
```

The exact equivalence is:

```text
G(theta,X) = [(1-theta X)^(-1) Uhat(X)]_{deg_X <= sigma+1},
theta active <=> G(theta,X) | 1-X^n.
```

The proof pseudo-divides `1-X^n` by `G(theta,X)` over `F_p[theta]`. The
pseudo-remainder cannot vanish identically because the reverse of `G` would be a
theta-dependent monic divisor of the split polynomial `X^n-1`, impossible since
`n|p-1`.

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle103_b1_divisor_bound_check.py
```

with `PASS`.

The next wall is `W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE`.

# Previous Banked Lemma - 2026-06-21 Cycle 102

```text
L-CYCLE102-UHAT-FLATNESS-LINEAR-READOUT
```

Cycle102 banks the exact identity:

```text
g_{S'}(X) Uhat(X) == 1 - theta X  (mod X^{sigma+2}),
```

so after the theta-free flatness constraints

```text
[X^i](g_{S'} Uhat)=0,  i=2,...,sigma+1,
```

theta is forced by the linear readout:

```text
theta = e_1(S') - Uhat_1.
```

Therefore:

```text
|Theta_U| =
#{ distinct e_1(S') :
   S' subset mu_n, |S'| = m,
   [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

Cycle102 also banks a route cut:

```text
L-CYCLE102-PADE-SHORT-WINDOW-DIVISOR-FALSIFIER
```

The short-window Padé/BM denominator of `(theta^j-P_j)_{j=1}^{sigma+1}` need
not divide or be compatible with `X^n-1`, even in an aperiodic prime-`n` case.
Codex verified the finite falsifier with:

```text
current_repo_snapshot/experimental/scripts/cycle102_pade_falsifier_check.py
```

The next wall is `L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY`.

# Previous Banked Lemma - 2026-06-21 Cycle 101

```text
L-CYCLE101-DFT-INDICATOR-LINE-INCIDENCE-REFORMULATION
```

External active roots are equivalently feasible Fourier windows of
weight-`m` subgroup indicators:

```text
theta active
<=> exists c in {0,1}^H with chat(0)=m
    and chat(j)=theta^j-P_j for j=1,...,sigma+1.
```

This keeps the prize-relevant count at:

```text
|Theta_U| = #{theta : F(theta)>0},
```

not the weighted count:

```text
N=sum_theta F(theta).
```

Cycle101 also banks the threshold calibration:

```text
main <= 2^n / p^sigma = 2^(n - sigma log_2 p),
```

so the live corrected-reserve problem is error/concentration on the aperiodic
line, not the first moment.

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle101_dft_line_incidence_check.py
```

with:

```text
cases_checked = 20
total_active_hits = 21
max_distinct_theta = 1
cases_with_multiple_theta = 0
PASS
```

The next wall is Padé/uncertainty line-incidence. The raw Cycle101 response is
truncated in section 6 and the unfinished BKR discussion should not be used as
evidence.

# Previous Banked Lemma - 2026-06-21 Cycle 100

```text
L-CYCLE100-WEIGHTED-COUNT-SPLIT
```

The character-sum route counts the weighted active pair count:

```text
N = sum_theta F(theta),
```

whereas the prize-relevant numerator is:

```text
|Theta_U| = #{theta : F(theta)>0}.
```

Thus `N<=poly` requires both distinct support control and multiplicity control:

```text
|Theta_U| <= poly
F_max <= poly.
```

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle100_support_fiber_split_check.py
```

with:

```text
cases_checked = 26
total_support = 14
total_N = 15
max_F_max = 2
PASS
```

The next wall is the distinct reciprocal affine-line incidence, with subgroup
PTE multiplicity as a separate secondary target.

# Previous Banked Lemma - 2026-06-21 Cycle 99

```text
L-CYCLE99-DIVISOR-LINE-CHARACTER-SUM-REDUCTION
```

Active external roots are equivalently degree-`s` divisors `f | X^n - 1` with
`deg(U-(X-theta)f)<k`, reciprocal affine-line incidences against elementary
subsets of `H`, and an exact additive-character count `N=main+error`.

Cycle99 also cuts the generic agreement-only route below Johnson.

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle99_divisor_line_incidence_check.py
```

with:

```text
cases_checked = 20
constructed_cases_checked = 10
constructed_external_pairs = 11
PASS
```

The next wall is cancellation in the nonzero-frequency subgroup
elementary-symmetric transform.

# Previous Banked Lemma - 2026-06-21 Cycle 98

```text
L-CYCLE98-MOMENT-CURVE-INCIDENCE
```

After the corrected Cycle97 bandwidth-`1` split, the active external roots are
exactly:

```text
Theta_U = { theta in F_p \ H : v(theta) in P - M_s },
v(theta) = (theta, theta^2, ..., theta^{sigma+1}),
M_s = { (p_1(S), ..., p_{sigma+1}(S)) : S subset H, |S| = s }.
```

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle98_moment_curve_incidence_check.py
```

with:

```text
cases_checked = 40
total_external_theta = 2
total_external_pairs = 2
PASS
```

This is a reduction and finite sanity check, not a proof of the polynomial
incidence bound. The next wall is the aperiodic moment-curve incidence bound.

# Previous Banked Lemma - 2026-06-20 Cycle 82

```text
L-CYCLE82-FOUR-SLOT-PRODUCT-INJECTIVITY
L-CYCLE82-PRODUCT-FIBER-MINDIST-GE-5
```

Cycle 82 itself returned an unrun checker and a MITM plan. Codex locally
implemented and ran:

```text
current_repo_snapshot/experimental/scripts/cycle82_four_slot_product_checker.py
current_repo_snapshot/experimental/notes/m1/cycle82_four_slot_product_certificate.json
```

The exact certificate decision is:

```text
ALL_4_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 5
self_test = scalar_pair_12_matches_vectorized
```

For every four-slot subset of `{1,...,7}`, the packed-product map is injective
on `48^4` tuples. Combined with the Cycle 77 singleton/pair certificate and the
Cycle 81 three-slot certificate, every product fiber has Hamming distance at
least `5`.

This still does not prove `m_max(beta)<=12`; it makes the next wall the exact
color-filtered MITM maximum-fiber threshold census.

# Previous Banked Lemma - 2026-06-20 Cycle 81

```text
L-CYCLE81-THREE-SLOT-PRODUCT-INJECTIVITY
L-CYCLE81-PRODUCT-FIBER-MINDIST-GE-4
```

Codex locally ran:

```text
current_repo_snapshot/experimental/scripts/cycle81_vectorized_three_slot_checker.py
current_repo_snapshot/experimental/notes/m1/cycle81_three_slot_injectivity_certificate.json
```

The exact certificate decision is:

```text
ALL_3_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 4
self_test = scalar_pair_12_matches_vectorized
```

Thus every three-slot product map is injective on `48^3` tuples. Combined
with the Cycle 77 singleton/pair injectivity certificate, every product fiber
has Hamming distance at least `4`.

# Previous Banked Lemma - 2026-06-20 Cycle 80

```text
L-CYCLE80-WEIGHT-3-STRUCTURE
L-CYCLE80-RATIO-TRIPLE-REFORMULATION
```

Cycle 80 banks the exact three-slot reduction:

```text
Any three-slot product collision differs in all three slots.
```

Otherwise one slot cancels and yields a forbidden two-slot product collision.

For each slot, define

```text
R_t = {u_t(k)/u_t(k') : k != k'}.
```

Then a slot triple `(t1,t2,t3)` is product-injective exactly when:

```text
(R_t1 R_t2) cap R_t3 = empty.
```

Equivalently, no ratios `r_i in R_ti` satisfy:

```text
r_1 r_2 r_3 = 1.
```

Codex preserved the exact checker spec as:

```text
current_repo_snapshot/experimental/scripts/cycle80_three_slot_injectivity_checker.py
```

but the first pure-Python run was interrupted as too slow for a heartbeat-local
bounded follow-up. No all-triples certificate is banked yet.

# Previous Banked Lemma - 2026-06-20 Cycle 79

```text
L-CYCLE79-COMPLEMENT-INVOLUTION
```

Cycle 79 banks the exact complement involution on the 48 admissible
8-subsets:

```text
tau(1,a) = (2,a+6)
tau(2,a) = (1,a+10)
tau(3,a) = (3,a+8)
```

with all indices modulo `16`. For each slot:

```text
u_t(k) u_t(tau(k)) = 3^(-2t)(beta^32 - 9^t).
```

Thus globally:

```text
Phi(tau(T)) = K / Phi(T),
tau(P_0)=P_0,
m(v)=m(K/v).
```

Codex locally added and ran:

```text
current_repo_snapshot/experimental/scripts/cycle79_involution_verifier.py
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
```

with decision:

```text
CYCLE79_INVOLUTION_OK
```

Cycle 79 also cuts the coherent common-ratio formulation alone as equivalent
to the original product-fiber count. The live wall is now exact
minimum-distance or a tau-symmetric energy bound.

# Previous Banked Lemma - 2026-06-20 Cycle 78

```text
L-CYCLE78-LR-INCIDENCE-REDUCTION
```

Cycle 78 banks the exact left-right incidence formula. With

```text
L(k_1,k_2,k_3)=u_1u_2u_3,
R(k_4,k_5,k_6,k_7)=u_4u_5u_6u_7,
```

and both maps product-injective by Cycles 75 and 76, each fiber value satisfies:

```text
m(v)=#{ l in L_img :
        v l^{-1} in R_img
        and colorL(l)+colorR(v l^{-1})=4 mod 16 }.
```

Codex locally added:

```text
current_repo_snapshot/experimental/scripts/cycle78_lr_incidence_sanity.py
current_repo_snapshot/experimental/notes/m1/cycle78_lr_incidence_sanity_certificate.json
```

as a bounded sanity certificate for the product/color decomposition. It is not
a proof of `m_max<=12`.

The live wall is now the coherent common-ratio bound or exact census.

# Previous Banked Lemma - 2026-06-20 Cycle 77

```text
L-CYCLE77-CONFIG-EVALUATION-REDUCTION
L-CYCLE77-FIBER-IS-A-CODE
L-CYCLE77-PAIR-SUBSET-PRODUCT-INJECTIVITY
```

Cycle 77 banks that the seven-slot product map is equivalently a configuration
evaluation:

```text
Phi(T)=3^{-28} prod_{c in S(T)} (beta^2-c),
```

where `S(T)` chooses one admissible 8-subset from each of seven disjoint
eta-cosets. It also banks the fiber-as-code principle: if two tuples in one
product fiber differ exactly on slot set `D`, then the product map on `D` is
non-injective.

Codex locally added and ran:

```text
current_repo_snapshot/experimental/scripts/cycle77_subset_injectivity_check.py
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
```

which certifies all single-slot and two-slot product maps are injective:

```text
28 subsets checked, all product-injective, fiber distance >= 3.
```

This is not enough for `m_max(beta)<=12`; the live route now needs exact
compiled/sharded max-fiber census or the next subset-injectivity frontier.

# Previous Banked Lemma - 2026-06-20 Cycle 76

```text
L-CYCLE76-ONE-SIDED-INJECTIVE-FIBER-REDUCTION
L-CYCLE76-RIGHT-HALF-PRODUCT-INJECTIVITY
```

Cycle 76 banks the reduction:

```text
m_max(beta) <= max_v |A cap v B^{-1}|,
```

where

```text
A = {products on slots {1,2,3}},
B = {products on slots {4,5,6,7}}.
```

Cycle 75 had already locally certified:

```text
|A| = 48^3 = 110592, product map injective.
```

Codex locally added and ran:

```text
current_repo_snapshot/experimental/scripts/cycle76_fast_right_half_check.py
current_repo_snapshot/experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
```

which certifies:

```text
|B| = 48^4 = 5308416, product map injective.
```

The full `m_max(beta)<=12` target remains open. The live wall is now the
`A*B` max-fiber / max-intersection problem, not another injectivity-ladder rung.

# Previous Banked Lemma - 2026-06-20 Cycle 75

```text
L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS
W-CYCLE75-CONSTRAINED-ENERGY-IS-THE-RIGHT-SCALE
W-CYCLE75-LADDER-CANNOT-FINISH
```

Cycle 75 banks a direct max-fiber census design:

```text
split slots as {1,2,3} and {4,5,6,7};
use packed field product as equality key;
use color sum as the P_0 domain filter;
use a subfield norm, preferably N_{F/F_{17^8}}, as a lossless product shard.
```

Codex locally certified the left half:

```text
current_repo_snapshot/experimental/scripts/cycle75_mitm_half_rung_check.py
current_repo_snapshot/experimental/notes/m1/cycle75_mitm_half_rung_certificate.json
```

with `110592` distinct products on `110592` tuples for slots `{1,2,3}`.
The right half and full `m_max<=12` census remain open.

# Previous Banked Lemma - 2026-06-20 Cycle 73

```text
L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL
L-CYCLE73-SOUND-NORM-BUCKET
L-CYCLE73-UNCONSTRAINED-D-DOMINATES
```

For the explicit Cycle 66/68 field model:

```text
eta^16 = 3,
y_t = beta^2 eta^(-2t),
u_t(i,a)=prod_{c in S_{i,a}}(y_t-c),
S_{i,a} subset F_17^*.
```

Codex locally checked this identity against all 336 banked Cycle 68 slot
values:

```text
current_repo_snapshot/experimental/scripts/cycle73_prime_slot_norm_check.py
current_repo_snapshot/experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
```

Cycle 73 also banks that norm bucketing is sound because `N(prod u_t)` is a
function of the product itself, unlike the cut color key. Finally, the
unconstrained collision energy dominates the constrained color-zero energy, so
`D_unconstrained<=155` is sufficient for the existing occupancy gate.

# Previous Banked Lemma - 2026-06-20 Cycle 72

```text
L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION
```

For the seven-slot product map, with ordered off-diagonal collision count

```text
D = #{(T,T') : T != T', prod_t u_t(T_t)=prod_t u_t(T'_t)},
```

define `E_S` as the ordered fully displaced collision energy on a slot subset
`S`. Cycle 72 banks the exact decomposition:

```text
D = sum_{S subset {1,...,7}} 48^(7-|S|) E_S.
```

If every `s`-slot product map is injective, then `E_S=0` for `|S|<=s`.
Therefore a `k=4` ladder pass would reduce the `D<=155` target to the
`|S|=5,6,7` fully displaced energies, and a single five-slot collision would
already kill the `D<=155` route.

Source:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle72_product_only_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/cycle72_product_only_ladder_raw/response.md
```

# Previous Banked Lemma / Route Cut - 2026-06-20 Cycle 71

Cycle 71 banks:

```text
L-CYCLE71-FULL-DISPLACEMENT
```

If every `(k-1)`-subset of slots is product-injective, then any `k`-subset
collision must differ in every one of the `k` slots. This follows by canceling
any shared slot value and invoking `(k-1)`-subset injectivity.

Cycle 71 also cuts the returned Python verifier's `(color, product)` duplicate
key as insufficient for product-injectivity. The corrected local reference
script keys by packed field product only:

```text
current_repo_snapshot/experimental/scripts/cycle71_product_ladder_checker.py
current_repo_snapshot/experimental/notes/m1/cycle71_product_ladder_certificate.json
```

# Route Cut / Corrected Identity - 2026-06-20 Cycle 70

Cycle 70's t-independent slot-value collapse is false:

```text
u_t(i,a) = prod_{c in 3^a D_i}(beta^2-c)
```

fails already at `(t,i,a)=(1,1,0)`. The surviving checked identity is the
t-dependent Cycle 68 formula:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

Codex checked all 336 entries with:

```text
current_repo_snapshot/experimental/scripts/cycle70_slot_normalization_checker.py
current_repo_snapshot/experimental/notes/m1/cycle70_slot_normalization_certificate.json
```

# Current Banked Lemma - 2026-06-20 Cycle 69

```text
L-CYCLE69-ENERGY-TO-MULTIPLICITY
L-CYCLE69-INJECTIVITY-LADDER
L-CYCLE69-SLOT-COMPLEMENT-ORACLE
```

For the explicit Cycle 66/Cycle 68 seven-slot model, let

```text
m_v = #{T in P_0 : prod_t u_t(B_t)=v},
m_max = max_v m_v,
E = sum_v m_v^2,
D = E - |P_0| = sum_v m_v(m_v-1).
```

Cycle 69 banks the exact threshold gate:

```text
m_max(m_max - 1) <= D,
D <= 155 => m_max <= 12 => Occ(beta) >= |P_0|/12 > 2^32.
```

It also banks the injectivity ladder: if every `k`-subset of slots is
product-injective, then every full collision has slot support at least `k+1`.
Codex locally verified the complement oracle and product-injectivity through
`k=2`:

```text
current_repo_snapshot/experimental/scripts/cycle69_ladder_probe.py
current_repo_snapshot/experimental/notes/m1/cycle69_ladder_probe_certificate.json
```

# Current Banked Lemma - 2026-06-20 Cycle 68

```text
L-CYCLE68-DISJOINT-COSET-FACTORIZATION
```

For the explicit Cycle 66 model,

```text
rho_beta(T) = (beta - 1) * prod_{t=1}^7 prod_{b in B_t}
  (beta^2 - eta^(2t + 16b)).
```

Cycle 68 also banks slot disjointness, color-as-set-sum mod 16, and the
bijection from admissible tuples to valid seven-slot set-tuples. Codex locally
verified the reduction with:

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/notes/m1/cycle68_slot_factorization_certificate.json
```

# Current Banked Lemma - 2026-06-20 Cycle 67

```text
L-CYCLE67-COLLISION-MULTIPLICITY-REDUCTION
```

Cycle 67 banks the exact inequalities:

```text
Occ(beta) * m_max(beta) >= |P_0|,
Occ(beta) >= |P_0|^2 / E,
```

where `E=#{(T,T') : P_T(beta)=P_T'(beta)}`. It also banks the shared-jet
collision reduction `deg(P_T-P_T')<=107` for distinct locators in `P_0`.
The decision threshold is sharp at this scale:

```text
m_max(beta) <= 12 => Occ(beta)>2^32,
|P_0|/13 < 2^32.
```

Source:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle67_cross_color_injectivity_audit.md
current_repo_snapshot/experimental/notes/m1/cycle67_cross_color_injectivity_raw/response.md
```

# Current Banked Lemma - 2026-06-20 Cycle 66

```text
L-CYCLE66-OCCUPANCY-LOCATOR-EVALUATION-REFORMULATION
```

Cycle 66 corrects the Role 05 finite-field admissibility condition:

```text
v_2(17^16 - 1) = 8,
mu_512(F_{17^16}) = mu_256(F_{17^16}),
beta admissible iff beta notin mu_256.
```

It also banks the exact reformulation:

```text
Occ(beta) = #{ rho_beta(T) : T in P_0 },
rho_beta(T)=prod_{x in T}(beta-x),
```

up to the global nonzero factor `(beta-1)3^12`. Codex locally verified the
setup with `experimental/scripts/cycle66_occupancy_selfcheck.py`.

Source:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle66_sevenfold_product_occupancy_audit.md
current_repo_snapshot/experimental/notes/m1/cycle66_sevenfold_product_occupancy_raw/response.md
```

---

# Banked Lemma - 2026-06-20 Cycle 65

```text
L-MODEL-GJ-THICKENED-FACTORIZATION
```

For the Role 05 characteristic-17 model, Cycle 65 proves the exact local
factorization

```text
v_{t,A_{i,a}}
= prod_{x in eta^t A~}(beta - x)
= (-1)^a 3^t P_i(beta^2 zeta^{-a} eta^{-2t}),
```

and reduces occupied thickened colors to a constrained sevenfold product-set
count.

Source:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle65_thickened_gadget_color_audit.md
current_repo_snapshot/experimental/notes/m1/cycle65_thickened_gadget_color_raw/response.md
```

---

# Current Banked Lemma - 2026-06-20 Cycle 64

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-CONVOLUTION
```

For fixed subgroup scale `J <= H`, the model generalized-Jacobian fiber
`Phi_sigma^{-1}(b)` is exactly the coefficient of a per-coset
prefix-collision gadget convolution. The Role 05 characteristic-17 packet is
absorbed as seven gadget-class enumerators plus one marker.

Source:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle64_prefix_collision_gadget_audit.md
current_repo_snapshot/experimental/notes/m1/cycle64_prefix_collision_gadget_raw/response.md
```

---

# Banked Lemmas

## F1 Cosupport Moment Identity / Landing Orthogonality Reduction

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

Cycle 44 banks the following restricted full-base-domain identity:

```text
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
A = F[X]/E,
deg E = t = sigma,
j = |T| = n-a.
```

For `T=D\S`, `I_S=interp_S(w)`, `xi=[X]_E`, `ell=[X^p-X]_E`,
`Lambda(T)=[L_T]_E`, and source-valid `E` with no roots on `D`,

```text
rho(T)=[I_S]_E = -ell * Lambda(T)^(-1) * N(T),
N(T)=sum_{d in D} w(d)L_T(d)(xi-d)^(-1).
```

Writing

```text
L_T(X)=sum_{m=0}^j (-1)^m e_m(T)X^(j-m),
```

gives both `N(T)` and `Lambda(T)` as affine-linear functions of
`e_1(T),...,e_j(T)` with `T`-independent coefficients.

Cycle 44 also banks the exact additive-orthogonality landing formula

```text
#Land = binom(p,j)/p^(2(t-1)) + E_error,
```

where `E_error` is an explicit nonzero-character sum over elementary
symmetric functions of `T`.

This is not a reserve lift. It sharpens the live wall to

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION
```

with preferred subwall
`W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260619_CYCLE44_COSUPPORT_MOMENT_IDENTITY_AUDIT.md`

## F1 Reserve-Scale Cosupport Landing Reduction

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

Cycle 43 banks the route-level reduction:

```text
N_split <= #Land(j,t),
#Land(j,t) heuristically ~ C(p,j)/p^{2(t-1)},
N_split heuristically ~ min(q_line, C(p,j)/p^{2(t-1)}).
```

The rigorous part is the upper bound from the cosupport landing count. The
asymptotic is not proved; it is a route-organizing skeleton because it matches
the banked fixed regimes:

```text
j=2,t=2 -> O(1);
j=3,t=2 -> O(p);
j=4,t=2 -> p^2/24 + lower terms.
```

Cycle 43 also banks a route cut: the literal fixed quartic/S4 mechanism does
not reserve-scale. Reserve scale has `j=Theta(n) >> 2t=Theta(n/log n)`, so the
square Cramer/quartic object disappears. Along `j=2t -> infinity`, totally
split monodromy density is at most `1/j -> 0`.

The next exact wall is

```text
W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`

## F1 T2J4 Restricted Good-Reduction / Split-Density Closure

Status: BANKABLE_LEMMA / ROUTE_CUT / EXPERIMENTAL / AUDIT.

Cycle 42 external 5.5 Pro round banks, conservatively, an external-machine
certificate for the fixed restricted branch

```text
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
t = sigma = 2,
j = 4.
```

The four external answers agree:

1. Cycle 41's type repairs were correct.
2. The Cycle 41 raw affine/Cramer good-reduction gate was sufficient for one
   simple affine chart, but not necessary for tame/projective good reduction.
3. The A-side `G2/G3` failure is a false negative, not a source-valid route
   cut.
4. Subcase A has a corrected good-reduction/geometric-`S_4` certificate at
   `p=7`.
5. Subcase B has a corrected good-reduction/geometric-`S_4` certificate at
   `p=19` or `p=31`.
6. The fixed restricted branch has split-slope density

```text
N_split(p) = p^2/24 + O(p^(3/2))
           = q_line/24 + O(q_line^(3/4)).
```

Codex did not locally rerun the symbolic SymPy computations because `sympy` is
absent from the available Python environments, and no dependency was fetched.
The result is banked as external-machine certificate / PRZ-review material,
not as a promoted main-paper proof.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`

## F1 T2J4 Subcase Finite-Place Geometric S4 Certificates

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Cycle 40 banks the finite-place histogram criterion:

```text
off-singular factorization types "4" and "13"
  => G_arith = G_geom = S_4
```

at a tested finite prime. The reason is that `"4"` gives a 4-cycle and
`"13"` gives a 3-cycle, forcing arithmetic `S_4`; the two types have opposite
parity, so the quartic discriminant takes both square and nonsquare values and
the geometric group is not contained in `A_4`.

Codex extracted and ran the parametrized Cycle 40 checker. It reports
`all_pass=true`:

```text
Subcase A, ell=alpha: p=7,23,43,47 pass.
Subcase B, ell=-2X:  p=11,19,31,59 pass.
```

This is finite-place evidence and a bankable restricted certificate packet. It
does not prove characteristic-zero good reduction or a growing-prime theorem.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_result.json`

## F1 T2J4 Locator-Collapse Lemma

Status: PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, explicit family

```text
alpha^2=-1,
E=X^2+alpha X+1,
b=[Bnum]_E=X,
u=[W]_E=1+X,
W_{n-1..n-4}=1,alpha,1+alpha,1,
ell=[X^p-X]_E,
```

Cycle 39 proves:

```text
ell = alpha*1_A    if (-5/p)=+1,
ell = -2*b         if (-5/p)=-1.
```

Equivalently, for `p=3 mod4`, Subcase A has `p=2,3 mod5` and `ell=alpha`,
while Subcase B has `p=1,4 mod5` and `ell=-2X`.

This removes the false impression that the quartic surface family changes
freely with `p`; inside each subcase it is a fixed model. The Cycle 38
`p=31` finite-place certificate is Subcase B only. Subcase A and the
good-reduction bridge remain open.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify_result.json`

## F1 T2J4 A2_B Explicit Uniform-Family Candidate

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, off-`R0` branch, Cycle 36 banks the
explicit denominator family for primes `p = 3 mod 4`:

```text
alpha^2=-1,
E=X^2+alpha X+1,
b=[Bnum]_E=X.
```

For `a in F_p`, `E(a)=(a^2+1)+alpha*a`; the imaginary part vanishes only at
`a=0`, where `E(0)=1`. Thus `E` has no roots on `D=F_p`. Also
`E-E^tau=2 alpha X`, and a common root would force `X=0`, again impossible.
So the denominator is source-valid and separated for all odd primes
`p = 3 mod 4`.

The remaining free data hypotheses, including `kappa != 0`, are finite
nonvanishing conditions. This does not yet give a counterpacket.

Cycle 36 also banks the reduction of uniform S4 to a corrected finite
certificate: quartic transitivity/geometric irreducibility, resolvent
irreducibility, and discriminant nonsquareness must all be certified at a
good prime and then propagated by good reduction.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`

## F1 T2J4 A2_B Finite-Place S4 Certificate

Status: BANKABLE_LEMMA / ROUTE_CUT / EXPERIMENTAL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated branch,
Cycle 35 banks the following per-instance finite-place monodromy certificate.

For a fixed source-valid instance, suppose the off-`Delta` squarefree
specializations of the substituted quartic `L_tau` over `F_p` contain
factorization types:

```text
"4"   and   "13".
```

Then the arithmetic monodromy group is `S_4`: a 4-cycle and a 3-cycle cannot
lie together in any proper transitive subgroup of `S_4`. The type `"13"` is
even, so it also cuts the only possible nontrivial constant-field quotient of
`S_4`, namely the sign quotient. Hence the certified instance has

```text
G_geom = G_arith = S_4.
```

This is a finite-place certificate, not a uniform theorem. It does not by
itself prove a growing-prime `Theta(q_line)` counterpacket and does not promote
to corrected-reserve, MCA, list-decoding, line-decoding, CA, curve-MCA,
protocol, SNARK, or prize status.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`

## F1 T2J4 A2_B Dominance Lemma

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated branch,
Cycle 34 banks the off-curve dominance lemma on the stated dense open:

```text
psi: A^2_B --> A^4_B,
z |-> tau(z)=M(z)^(-1)(-C_0(z)).
```

Using the graph equation

```text
G(z,tau)=(u-zb)lambda(tau)-ell[Q_S(tau)]_E=0 in A=F[X]/E,
```

one can solve in the opposite direction for `z` as a rational collinearity
scalar whenever `b lambda(tau) != 0`. Thus the rational map `chi` satisfies
`chi o psi = id` generically. Cotangent functoriality gives
`D chi * D psi = I_2`, so the `B`-Jacobian of `psi` has generic rank two.

Therefore the off-curve image is surface-sized and birational onto the Cycle
30 quadric image. This cuts the hidden rank-one / curve-collapse route for
`O(p)` in this branch. It does not prove geometric monodromy, positive split
density, a `Theta(q_line)` counterpacket, corrected-reserve, MCA,
list-decoding, line-decoding, CA, curve-MCA, protocol, SNARK, or prize status.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`

## F1 T2J4 A2_B Singular Determinant Bound

Status: BANKABLE_LEMMA / CONDITIONAL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated branch,
Cycle 33 banks the singular determinant curve bound under the Cycle 29
top-symbol nonzero hypotheses.

Write

```text
z=z_0+alpha z_1,     z_0,z_1 in B.
```

Since multiplication by `z` on `A=F[X]/E` is

```text
m_z=z_0 I_4+z_1 A_alpha,
```

the Cycle 29 matrix `M(z)` has entries of total degree at most one in
`(z_0,z_1)`. Therefore

```text
Delta(z_0,z_1)=det_B M(z)
```

has total degree at most four. Cycle 29's top symbol

```text
TopSym(Delta)=-N(kappa)N(z)^2Q_4
```

is nonzero on the source-valid branch, so `Delta` is not identically zero.
Thus `Delta=0` has at most `4p` points in `F_p^2`, and the singular locus
contributes at most `4p=O(p)` split slopes.

This does not prove off-curve positive density, `S_4`, a
`Theta(q_line)` counterpacket, corrected-reserve, MCA, list-decoding,
line-decoding, CA, curve-MCA, protocol, SNARK, or prize status.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`

## F1 T2J4 Split-Quadric Gate Reduction

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`,
`q_line=p^2`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated window,
Cycle 30 reduces the distinct split-quartic gate to one `F`-quadric in
co-support elementary-symmetric coordinates `tau=e(T)`.

The reduction is:

```text
Phi(tau)=iota wedge_F mu,
iota = u*lambda - ell*[Q_S]_E,
mu = b*lambda,
lambda=[L_T]_E.
```

Equivalently,

```text
Phi(tau)
  = kappa*N_{A/F}(lambda)
    - (ell*[Q_S]_E) wedge_F (b*lambda).
```

Since `Q_S` is independent of `tau_4` and `lambda=lambda'+tau_4`, this is
quadratic in `tau_4`:

```text
Phi = kappa*tau_4^2
    + tau_4*(kappa*Tr_{A/F}(lambda') - (ell[Q_S]_E) wedge_F b)
    + (kappa*N_{A/F}(lambda') - (ell[Q_S]_E) wedge_F (b lambda')).
```

This banks the source-correct gate formulation only. It does not prove `O(p)`,
does not produce a `Theta(q_line)` counterpacket, and does not promote to MCA,
list-decoding, line-decoding, CA, curve-MCA, protocol, SNARK, or prize status.

Codex finite scans are EXPERIMENTAL and lean toward `O(p)`-scale slope counts,
making the next live wall `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md`

## F1 T2J4 Square Determinant And Top Symbol

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=4`,
off-`R0`, source-valid separated window, Cycle 29 banks the structural
transition from the `j=3` incidence determinant to a `j=4` square system.

The quotient has closed form

```text
Q_S = W_{n-1} X^3
    + (W_{n-2} - W_{n-1} tau_1) X^2
    + (W_{n-3} - W_{n-2} tau_1 + W_{n-1} tau_2) X
    + (W_{n-4} - W_{n-3} tau_1 + W_{n-2} tau_2 - W_{n-1} tau_3).
```

The affine bad-line system is

```text
M(z)tau=-C_0(z),     M(z)=[C_1(z)|C_2(z)|C_3(z)|C_4(z)]
```

in `A=F[X]/E`, a four-dimensional `B`-space. Thus off `det_B M(z)=0`, the
system has a unique affine preimage `tau(z)` for each slope `z`.

The top symbol of the square determinant is

```text
TopSym(det_B M(z)) = -N(kappa) * N(z)^2 * Q_4,
```

where `Q_4` is the Cycle 28 locator quantity

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

This is source-validly nonzero under Cycle 28 hypotheses. It does not imply an
`O(p)` slope bound for `j=4`; affine consistency is generically automatic.
The remaining gate is whether `tau(z)` is the elementary-symmetric tuple of a
distinct 4-subset of `F_p`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`

## F1 T2J3 Q4 Restricted Proof

Status: PROOF / ROUTE_CUT / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0`, `c_b!=0`, source-valid separated window, Cycle 28 proves that the
Cycle 16 determinant consistency polynomial `Q` is not identically zero.

The top coefficient is

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

For `c notin B`,

```text
Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

Thus `Q_4=0` iff `E` has an `F_p` root, excluded by source-validity. For
`c in B`, `Q_4=N(c_b)*Im(d)^2`, and separatedness excludes `d in B`.
Therefore `Q_4!=0`, hence `Q` is nonzero and the Cycle 16 safe-side bound
applies:

```text
C2 <= 4p = O(p).
```

This is a local residue-line incidence proof only. It is not a corrected
reserve theorem, not an MCA theorem, and not a protocol statement.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md`

## F1 T2J3 Q4 Locator-Norm Obstruction

Status: ROUTE_CUT / superseded by Cycle 28 restricted proof.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 27 gives a candidate closure of the last `Q==0`
branch.

Subject to independent confirmation of the Cycle 15/16/20/25 column
conventions, the degree-4 coefficient of the determinant consistency
polynomial `Q(z_0,z_1)` is

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

Equivalently, if `c=c_0+alpha c_1` and `d=d_0+alpha d_1`,

```text
Q_4 = N(c_b) * (c_1^2 d_0 - c_0 c_1 d_1 + d_1^2).
```

For `c notin B`,

```text
Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

Therefore `Q_4=0` iff `E` has an `F_p` root iff
`prod_{a in F_p}E(a)=0`, the locator norm already banked in Cycle 24.
Source-validity excludes roots on `F_p`.

For `c in B`, `Q_4=N(c_b)*Im(d)^2`; separatedness excludes `d in B`.
Thus `Q_4!=0` on the separated source-valid branches, pending the independent
source audit.

Consequence if confirmed: `Q` is not identically zero, so Cycle 16 gives
`O(p)` affine-consistent slopes; the distinct split-cubic gate only shrinks the
set. This remains a local residue-line incidence result only.

Audit caveat: do not promote to `PROOF` until Cycle 28 or another independent
source audit rederives the `Q_4` formula and the `q2` closed form directly.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE27_Q4_SPLIT_GATE_AUDIT.md`

## F1 T2J3 Q-Zero Rank Dichotomy

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 26 banks the rank dichotomy for the affine consistency
system.

Let

```text
C(z)=[c_1(z)|c_2(z)|c_3(z)] in Mat_{4 x 3}(B).
```

If some `3 x 3` minor of `C(z)` is not identically zero (NONDEP), then
`rank_B C(z)<=2` occurs on only `O(p)` values of `z`. Away from that locus,
`rank_B C(z)=3`, so `Q(z)=0` is necessary and sufficient for

```text
c_0(z) in span_B(c_1(z),c_2(z),c_3(z)).
```

Therefore:

```text
NONDEP and Q not identically zero => O(p) affine-consistent slopes.
```

In the `c notin B`, `c_b != 0` branch, the leading symbols of columns `1` and
`2` are `-c_b c` and `-c_b`, which are `B`-independent; hence that branch is
NONDEP.

DEP does not create slopes. It forces additional augmented-rank conditions for
`[C(z)|c_0(z)]`, and remains a separate degenerate wall.

Audit caveat: this is an affine `tau in B^3` statement. Actual line-incidence
still requires retaining distinct `D`-split cubics. The proposed `Q_4` formula
from Cycle 26 remains audit-only until independently verified.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md`

## F1 T2J3 Q Determinant Plucker Expansion

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 25 banks the multilinear determinant expansion behind
the Cycle 15/16 consistency polynomial.

If

```text
c_i(z)=s_i(z)u+t_i(z)b
```

and `<x,y>` is the alternating `B`-area form on `F`, then

```text
Q = <s_1,s_2><t_3,t_0> - <s_1,s_3><t_2,t_0>
  + <s_1,s_0><t_2,t_3> + <s_2,s_3><t_1,t_0>
  - <s_2,s_0><t_1,t_3> + <s_3,s_0><t_1,t_2>.
```

This verifies the Plucker/Laplace shape of `Q`, but not the specific Cycle 16
trace/Gram criterion.

Audit correction: `Q(z)=0` is only necessary in general. It is sufficient for
realizability only when `rank[c_1(z)|c_2(z)|c_3(z)]=3`; rank-drop strata need
augmented-rank minors. Do not bank `Q==0` as a counterpacket or as
`C2=p^2`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`

## F1 T2J3 D-Kernel Norm Factorization

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 24 closes the source-valid `D=0` branch.

Let

```text
E=X^2+cX+d,
A=F[X]/E,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[X^p-X]_E,
kappa=u wedge b.
```

Put

```text
w=c^2/4-d,
mu=w^((p-1)/2)-1,
delta_c=(c-c^p)/2.
```

Then

```text
ell=mu*(xi+c/2)+delta_c.
```

Under the Cycle 21/22 conventions

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell),
```

one has

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a)=delta_c^2-mu^2(c^2/4-d).
```

Since a source-valid residue-line denominator is nonzero on `D=F_p`,
`N(ell)!=0`. Off `R0`, `kappa!=0`, hence `D!=0`.

Therefore the source-valid `D=0`, off-`R0` branch is empty in this restricted
window. Do not bank any corrected-reserve, `q_gen`, protocol, list-decoding,
line-decoding, CA, MCA, curve-MCA, or SNARK consequence.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`

## F1 T2J3 c-in-B D-Kernel Emptiness

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 23 closes the `c in B`, `d notin B` part of the
`D=0` branch.

Let

```text
E=X^2+cX+d,
A=F[X]/E,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[X^p-X]_E,
kappa=u wedge b.
```

If `c in B`, put `sigma=xi+c/2`. Then

```text
sigma^2=c^2/4-d,
ell=mu sigma,
mu=(c^2/4-d)^((p-1)/2)-1.
```

For `d notin B`, both `mu` and `c^2/4-d` are nonzero. Under the Cycle 21/22
conventions

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell),
```

one has

```text
D=-mu^2(c^2/4-d)kappa.
```

Therefore `D != 0` whenever `kappa != 0`. The stratum

```text
c in B,
d notin B,
D=0,
off R0
```

is empty; the Cycle 22 `c in B`, `d notin B` nonemptiness/split-count wall is
cut.

Cycle 24 supersedes this as a corollary of `D=N(ell)kappa` and
`N(ell)=prod_{a in F_p}E(a)`. Do not bank any full `C2` bound, any
`Theta(q_line)` counterpacket, or any protocol/list/CA/MCA/line-decoding/
curve-MCA/SNARK consequence.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE23_CINB_DKERNEL_EMPTINESS_AUDIT.md`

## F1 T2J3 D-Kernel Decoupling Identity

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 22 banks the following exact identity below the
`D`-kernel alignment wall.

On `Delta1==0`, write

```text
p1+q2=f_0+f_1 tau_1+f_2 tau_2,
f_i in B.
```

Then

```text
Delta1==0
  iff
Im_alpha(p1+q2)=0 and Im_alpha(detP)=0.
```

On `D=0`, alignment is equivalent to the single scalar gate

```text
J_A=0,
```

where

```text
J_A=L(A/kappa),
L=partial_{tau_1}-c partial_{tau_2}.
```

Cycle 22 banks the decoupling identity

```text
Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2.
```

Consequently, on the stratum `c in B`, `d notin B` in odd characteristic,
alignment is impossible at any source-valid point of

```text
Delta1==0,
D=0.
```

Do not bank nonemptiness of that stratum, a slope lower bound, or a
`Theta(q_line)` counterpacket.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`

## F1 T2J3 D-Kernel Collapse Gates

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 21 banks the following slope-collapse gates on the
`Delta1==0` branch. Let

```text
L(f)=partial_{tau_1} f - c partial_{tau_2} f,
J_A=L(A/kappa),
J_Aprime=L(A'/kappa),
A=(ell Q) wedge b,
A'=u wedge (ell Q).
```

Away from discriminant ramification, simultaneous collapse of both slope
branches is equivalent to

```text
J_A=0,
J_Aprime=0.
```

Writing

```text
m=W_{n-2}+c W_{n-1},
w_1=W_{n-1},
```

the two gates are

```text
kappa J_A      = -(ell wedge b)m + P_E(b,ell)w_1,
kappa J_Aprime = -(u wedge ell)m - P_E(u,ell)w_1.
```

Their resultant is the Cycle 20 gate

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

Thus `D != 0` blocks simultaneous branch collapse. On `D=0`, collapse further
requires the leading-data ratio

```text
(W_{n-2}+cW_{n-1}:W_{n-1})
```

to lie on the corresponding kernel line.

Do not bank the stronger claim that the base-descent equations are independent
of this collapse gate; no elimination proof or source-valid off-kernel family
has been supplied.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`

## F1 T2J3 Rank-One Gate Lemma

Status: BANKABLE_LEMMA / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, with `E=X^2+cX+d`, `u=[W]_E`, `b=[Bnum]_E`,
`ell=[L_D]_E`, and `kappa=u wedge b`, Cycle 20 banks:

```text
q1 = -(Q_E(b)/kappa) eta,
eta=(c^2-d)+c tau_1+tau_2.
```

Thus the leading coefficient of the slope quadratic is rank-one in
`(tau_1,tau_2)`.

Cycle 20 also banks the quadric-branch normal form on `Delta1==0`:

```text
delta_z=(p1-q2)^2+4q1p2=(p1+q2)^2-4detP in B[tau_1,tau_2],
w^+-=(+-sqrt(delta_z)-A/kappa)/(2c_b eta),
A=(ell Q) wedge b,
c_b=-Q_E(b)/kappa.
```

Finally, the `P^2(F)` coefficient-image gate is

```text
det M=(c_b/kappa^2)D,
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

Do not bank slope collapse, non-collapse, or a `Theta(q_line)` counterpacket
from this lemma.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`

## F1 T2J3 Monicity In The Resonance Determinant

Status: BANKABLE_LEMMA / AUDIT.

In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
off-`R0` window, Cycle 14 gives an `F`-basis `{[W]_E,b}` of `A=F[X]/E`,
where `b=[Bnum]_E`, and

```text
iota=A0(tau_1,tau_2)-tau_3[W]_E,
mu=B0(tau_1,tau_2)-tau_3 b,
A0=p1[W]_E+p2 b,
B0=q1[W]_E+q2 b.
```

Thus the landing determinant in this basis is

```text
Delta=(p1-tau_3)(q2-tau_3)-p2 q1,
```

monic quadratic in `tau_3`. Splitting `Delta=Delta0+alpha Delta1` over
`F=B+alpha B` gives

```text
deg_{tau_3} Delta0 = 2, leading coefficient 1,
deg_{tau_3} Delta1 <= 1.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`

## F1 Fixed-Rate Sigma-1 Counterpacket

Status: COUNTERPACKET.

For `B=F_p`, `F=F_{p^2}`, `H=F_p^*`, `k=floor(rho(p-1))`, `a=k+1`, and `E=X-alpha` with `alpha notin B`, the same-numerator extension-line MCA lift has fixed-rate bad-slope density bounded below by a positive constant. This kills unrestricted `ass:extension-mca-lift`.

## F1 Residual Slack Reduction

Status: BANKABLE_LEMMA.

Unbalanced degree `t < sigma` residue-line data reduce to a residual list object with residual slack `sigma-t`; the remaining hard case is balanced `t approx sigma`.

## F1 Monic-Anchor Hat-E Reduction

Status: BANKABLE_LEMMA with open arbitrary-anchor caveat.

For balanced monic-anchor / locator data, equal slopes from supports `S,S'` imply `hat E | (L_S-L_S')`, where `hat E=lcm(E,E^tau) in B[X]` and `deg(hat E)<=2sigma`. This reduces that stratum to a base-field per-fiber readout at effective prefix `<=2sigma`.

## Raw L1 Arbitrary Fiber Overcount

Status: COUNTERPACKET.

The raw arbitrary `Fib_U(s)` statement is false as written: if `U` is already a codeword, every `s`-subset can be feasible while the list size is 1.

## F1 Arbitrary-Anchor Paired Base Readout

Status: BANKABLE_LEMMA with endpoint caveat.

In the quadratic setting `B=F_p`, `F=F_{p^2}`, `D subset B`, balanced `t=sigma`, and arbitrary `w:D->F`, write `w=w0+alpha*w1` over a `B`-basis. Since support interpolation over `D` has base-field Lagrange coefficients,

```text
interp_S(w)=interp_S(w0)+alpha*interp_S(w1).
```

The slope condition modulo `E` factors through

```text
S -> (interp_S(w0) mod Ehat, interp_S(w1) mod Ehat),
Ehat=lcm(E,E^tau) in B[X].
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE1_F1_ARBITRARY_ANCHOR_AUDIT.md`

## F1 Paired Readout Slope-Uniqueness And Dimension Caveats

Status: BANKABLE_LEMMA / AUDIT.

For the same quadratic balanced arbitrary-anchor setup, Cycle 2 records these reusable caveats:

- `Ehat=lcm(E,E^tau)` must be taken for the full denominator `E` in the residue-line datum.
- If `[Bnum]_E` is nonzero in `F[X]/(E)`, then the scalar slope `z` is unique even when `[Bnum]_E` is a zero divisor.
- Passing from a larger support to an `a=k+t` subset preserves the forced interpolant and residue equation, but may lose noncontainment.
- The quadratic paired readout has `B`-dimension `2 deg(Ehat) <= 4t`; in extension degree `e`, the analogous component readout has dimension `e deg(Ehat)`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_PAIRED_BASE_READOUT_AUDIT.md`

## F1 Balanced Noncontainment Subset Lemma

Status: BANKABLE_LEMMA / AUDIT.

For a degree-`t` residue-line datum with nonzero numerator `Bnum`, put `a=k+t`. On any support `S` with `|S|>=a`, there is no `G in F_{<k}[X]` satisfying `G=-Bnum/E` on `S`. Therefore every such support is automatically noncontained in the sense of `def:residue`.

This removes the support-shrinking noncontainment concern from the balanced nonzero-numerator case. Cycle 4 then cuts the balanced high-agreement sub-wall by `a=s_delta`; the remaining obstruction is value-count / slope-image packing, not noncontainment.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_AUDIT.md`

## F1 W-F1-AA-RES Wall Sharpening

Status: EXACT_NEW_WALL / AUDIT.

Restored `W-F1-AA` is a faithful arbitrary-anchor extension-denominator instance
of `Lambda^{NC}_{t,delta}` / `prob:perfiber`, not a smaller proved object.
The tangent/zero-numerator and quotient-periodic separations are necessary but
non-binding: the banked `sigma=1` fixed-rate counterpacket has nonzero numerator,
is aperiodic, and still gives `Theta(q_line)` slopes.

The correct active wall is reserve-indexed. Balanced `t=sigma` has hidden
reserve `eta=sigma/n`; fixed `sigma` is sub-reserve. Above corrected reserve,
the missing invariant is a rigidity/value-count law for the paired readout
`rho` on the bad line and the generated-field ledger controlling when the count
is governed by `q_gen` rather than `q_line`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE5_W_F1_AA_RES_EXACT_WALL_AUDIT.md`

## F1 W-F1-AA-RES Kernel Is Not The Wall

Status: EXACT_NEW_WALL / AUDIT.

Cycle 6B was malformed in the VS Code terminal artifact, but the structured
Claude CLI session log was recovered and then source-audited locally. The
source-valid content is only a wall sharpening:

- For `a=k+t` supports, equal slopes imply
  `interp_S(w)-interp_S'(w) in E*F_{<k}[X]`, by residue equality and degree
  count.
- The residue `[interp_S(w)]_E` is determined by the paired base readout
  modulo `Ehat`.
- These facts describe the kernel and descent of the slope map; they do not
  count distinct slope values.

The active missing invariant is therefore not the same-slope kernel. It is a
slope value-count / collision law for the paired base readout on the bad line
`F*[Bnum]_E`, after tangent and quotient-periodic separation, with the
`q_gen`/`q_line` ledger explicit.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RECOVERED_AUDIT.md`

## F1 Twisted Readout Transfer Boundary

Status: ROUTE_CUT / EXACT_NEW_WALL / AUDIT.

Cycle 7 produced a clean structured Claude answer that claimed a
`BANKABLE_LEMMA`, but source audit rejects the claimed exact transfer.

Bank only the boundary:

- The slope remains a function of the paired base readout, so
  `#slopes <= #paired-readout-values`; this is a safe but non-closing
  consequence of the paired-readout reduction.
- For `z in B`, the CRT equation can be written in the quotient as
  `[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat = z b_hat`.
- This is a twisted readout with nonconstant `theta in B[X]/Ehat`; it is not, in
  general, the ordinary residue of the interpolant of `w0+theta*w1`.
- Therefore `thm:exactcount` and `thm:rigidcyclo` do not transfer verbatim to
  this stratum.

The live wall is sharpened to:

```text
W-F1-AA-RES-TWISTED-READOUT:
prove or refute a value-count/collision law for
[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat with nonconstant theta.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE7_W_F1_AA_RES_VALUECOUNT_TWISTED_READOUT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle7_theta_multiplier_check.py`

## F1 Twisted Readout Isomorphism

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Cycle 8 resolves the twisted readout formulation in the separated quadratic
case.

Let `Ehat=E E^tau in B[X]` with `gcd(E,E^tau)=1`, and let
`theta in B[X]/Ehat` be the CRT class satisfying `theta=alpha mod E` and
`theta=alpha^tau mod E^tau`. Then:

```text
pi: B[X]/Ehat -> F[X]/E, [g] -> [g]_E
```

is a ring isomorphism, `pi(theta)=alpha`, and

```text
pi([interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat)
  = [interp_S(w0)+alpha interp_S(w1)]_E.
```

Consequently the twisted readout has exactly the same value count as the
original extension residue map. The twist is not a new obstruction and does not
create a `q_gen` saving.

The Cycle 7 non-absorption failure is explained by the commutator:

```text
theta interp_S(w1) - interp_S(theta w1) = L_S R_S,
deg R_S <= 2t-2.
```

The live wall is sharpened to:

```text
W-F1-AA-RES-RESIDUE-COUNT:
above corrected reserve eta=sigma/n, bound the F-residue value count
S -> [interp_S(w0)+alpha interp_S(w1)]_E
by n^{1+o(1)}, for arbitrary base anchors w0,w1 and aperiodic separated E.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE8_W_F1_AA_RES_TWISTED_READOUT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle8_twisted_readout_verify.py`

## F1 Locator-Quotient Line-Incidence Reduction

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Cycle 9 corrects the target after Cycle 8. The raw extension residue value count
is not the source MCA object; the source object is the number of scalar slopes
whose residues land on the bad line.

Let `W=interp_D(w)`, `L_S=prod_{d in S}(X-d)`, `|S|=a=k+t`, and
`I_S=interp_S(w)`. Euclidean division gives

```text
W = L_S Q_S + I_S,
deg Q_S <= n-a-1 = j-1, where j=n-a=r-t.
```

Therefore

```text
[I_S]_E = [W]_E - [L_S Q_S]_E in F[X]/E.
```

For nonzero numerator `Bnum`, the source-relevant count is

```text
#{ z in F : exists S, [I_S]_E = z[Bnum]_E },
```

equivalently the incidence/landing count of `[L_S Q_S]_E` in the affine line
`[W]_E - F[Bnum]_E`. Since `dim_F F[X]/E=t` and `dim_F F[Bnum]_E=1`, the line
has codimension `t-1`. The `sigma=1` fixed-rate counterpacket is the
codimension-zero endpoint where raw residues and slopes coincide.

The live wall is sharpened to:

```text
W-F1-AA-RES-LINE-INCIDENCE:
prove or refute the reserve-indexed incidence bound for
[L_S Q_S]_E in [W]_E - F[Bnum]_E
under balanced t=sigma, separated aperiodic E, arbitrary base anchors, and
field ledgers q_gen/q_line/q_chal kept separate.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE9_W_F1_AA_RES_RESIDUE_COUNT_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle9_locator_quotient_incidence_check.py`

## F1 t=2, j=2 Line-Incidence Lemma

Status: BANKABLE_LEMMA / AUDIT.

Cycle 11 closes the first finite bad-line incidence regime:

```text
t=sigma=2,     j=n-a=r-t=2,     a=n-2,     k=n-4.
```

For `W=interp_D(w)` and co-support `T=D\S={d1,d2}`, put
`s_T=d1+d2`, `p_T=d1d2`. Euclidean division

```text
W=L_S Q_S+I_S,       I_S=interp_S(w),       deg Q_S<=1
```

has the closed form

```text
Q_S = C(X-s_T)+C1,
C=[W]_{n-1},     C1=[W]_{n-2}+C sigma_1(D).
```

Thus `Q_S` depends on the co-support only through the sum `s_T`.

The bad-line landing condition

```text
[I_S]_E = z [Bnum]_E
```

is equivalent to one determinant equation

```text
det(s_T,p_T)=0,
det(s,p)=wedge([W]_E[L_T]_E-[L_D]_E[Q_S]_E, [Bnum]_E[L_T]_E).
```

Here `deg det<=2` and the coefficient of `p^2` is
`wedge([W]_E,[Bnum]_E)`. Hence `det identically zero` forces the
global/tangent endpoint. If `det` is not identically zero, the slope count is
`C2=O(n)`, with the conservative bound `C2<=6n`; generically `C2<=4` when the
base components have no common component. For `D=F_p`, `p>=7`, and
`deg W=n-1`, the repeated-sum argument excludes the identically-zero
determinant resonance.

This is not a proof of `conj:B` and gives no protocol or `q_gen` collapse.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE11_T2_J2_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle11_t2_j2_line_incidence_verify.py`

## F1 t=2, j=3 Quotient And Quadric Lemma

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Cycle 12 gives the next finite structural calculation:

```text
t=sigma=2,     j=n-a=r-t=3,     a=n-3,     k=n-5.
```

For co-support `T=D\S` of size `3`, with `tau_i=e_i(T)` and `E_i=e_i(D)`,
the quotient in

```text
W=L_S Q_S+I_S
```

is

```text
Q_S =
  W_{n-1} X^2
  + (W_{n-2}+W_{n-1}E_1) X
  + (W_{n-3}+W_{n-2}E_1+W_{n-1}(E_1^2-E_2))
  - tau_1 (W_{n-1}X+W_{n-2}+W_{n-1}E_1)
  + tau_2 W_{n-1}.
```

For `D=F_p`, this simplifies to

```text
Q_S=W_{n-1}(X^2-tau_1 X+tau_2)+W_{n-2}(X-tau_1)+W_{n-3}.
```

Thus `Q_S` is independent of `tau_3=e3(T)`.

The bad-line landing condition is the quadric

```text
Delta(T)=( [W]_E [L_T]_E - [L_D]_E [Q_S]_E )
          wedge ( [Bnum]_E [L_T]_E ) = 0,
```

with

```text
[tau_3^2]Delta = wedge([W]_E,[Bnum]_E).
```

This is not a slope-count theorem. It identifies the next wall:
`W-F1-AA-RES-T2J3-FIBER-COLLAPSE`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE12_T2_J3_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle12_t2_j3_line_incidence_scan.py`

## F1 t=2, j=3 Base-Component Complete Intersection

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Cycle 13 banks the generic/off-resonance completion of the Cycle 12
alternative lens.

Keep ledgers separate:

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`.
- `t=sigma=2`.
- `j=n-a=3`, so `a=n-3`, `k=n-5`.

Let `A=F[X]/E`, `L_T=X^3-tau_1 X^2+tau_2 X-tau_3`, and
`W=L_S Q_S+I_S`, `L_D=L_S L_T`. The Cycle 12 determinant satisfies

```text
Delta=( [W]_E[L_T]_E-[L_D]_E[Q_S]_E )
       wedge( [Bnum]_E[L_T]_E )
     = Res(L_T,E) * ( [I_S]_E wedge [Bnum]_E ).
```

Because `E` is nonzero on `D` and `T subset D`, `Res(L_T,E) != 0` for every
valid co-support. Thus `Delta=0` is exactly the landing condition; the
resultant factor adds no forced common component.

Writing `F=B+alpha B`,

```text
Delta=Delta_0+alpha Delta_1,
Delta_i in B[tau_1,tau_2,tau_3].
```

Off the resonance strata

```text
R0 = { [W]_E wedge [Bnum]_E = 0 },
Ra = { Delta in F^* \bar B[tau] },
Rb = { Delta has a \bar B-linear factor },
```

the base quadrics `Delta_0,Delta_1` have no common surface component. Hence
their zero set in `B^3` is a bounded-degree curve and has `O(p)` points. For
`D=F_p`, this gives

```text
C2 <= #landings = O(p)=O(n)
```

in the `t=sigma=2`, `j=3` regime off `R0 union Ra union Rb`.

This is not unconditional. The residual wall is the resonance locus:

```text
W-F1-AA-RES-T2J3-BASE-COMPONENT-RESONANCE.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE13_BASE_COMPONENT_COMPLETE_INTERSECTION_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle12_base_component_rank_scan.py`

## F1 t=2, j=3 Resonance Slope-Map Reduction

Status: EXACT_NEW_WALL / AUDIT.

Cycle 14 analyzes the residual resonance strata left by Cycle 13:

```text
Ra = { Delta in F^* \bar B[tau] },
Rb = { Delta has a \bar B-linear factor }.
```

It does not prove slope collapse and does not produce a counterpacket. It
reduces the resonance question to an explicit slope-map fiber problem.

Keep ledgers separate:

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`.
- `t=sigma=2`, `j=3`.

Off `R0={ [W]_E wedge [Bnum]_E = 0 }`, put

```text
A=F[X]/E,        b=[Bnum]_E,
m=[L_T]_E.
```

The landing determinant can be written

```text
Delta = iota wedge mu,
iota(tau)=m[I_S]_E=[W]_E m-[L_D]_E[Q_S]_E,
mu(tau)=m b.
```

Both are `A`-valued affine-linear forms:

```text
iota(tau)=A0(tau_1,tau_2)-tau_3[W]_E,
mu(tau)=B0(tau_1,tau_2)-tau_3 b.
```

Expanding `A0,B0` in the `F`-basis `{[W]_E,b}` gives

```text
A0=p1[W]_E+p2 b,
B0=q1[W]_E+q2 b,
```

and landing `[I_S]_E=z b` gives

```text
q1 z^2-(p1-q2)z-p2=0,
tau_3=p1-zq1 in B.
```

The new exact wall is:

```text
W-F1-AA-RES-T2J3-SURFACE-SLOPE-FIBER.
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`

## F1 t=2, j=3 Surface Slope-Fiber Rank/Determinant Wall

Status: EXACT_NEW_WALL / AUDIT.

Cycle 15 does not prove the slope bound and does not construct a
`Theta(q_line)` counterpacket. It gives the next bankable reduction.

On the Cycle 14 resonance surface, landing `[I_S]_E=z b` is equivalent to

```text
L_z(tau)=iota(tau)-z mu(tau)=0 in A=F[X]/E.
```

The `B`-linear part of `L_z:B^3 -> A ~= B^4` has explicit columns
`c1(z),c2(z),c3(z)`, and affine consistency is measured by

```text
Q(z_0,z_1)=det_{4x4}[c1(z) | c2(z) | c3(z) | c0(z)].
```

The safe wall is the rank/determinant pair:

- rank `3` with `Q!=0` gives a curve-sized slope set;
- rank `3` with `Q==0` identically is the possible `Theta(q_line)` regime.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle15_forced_ra_slope_scan_certificate.md`

## F1 t=2, j=3 Q-Nonzero Slope Bound

Status: BANKABLE_LEMMA / AUDIT.

Cycle 16 banks the safe side of the rank/determinant wall. In the
`D=F_p`, `t=sigma=2`, `j=3` regime, off
`R0={wedge([W]_E,[Bnum]_E)=0}`, the determinant consistency polynomial

```text
Q(z_0,z_1)=det_{4x4}[c1(z)|c2(z)|c3(z)|c0(z)]
```

has degree `<=4`. If `Q` is not identically zero, every landing slope lies on
the nonzero curve `Q=0`, so

```text
C2 <= 4p = O(p)=O(n).
```

The residual wall is only the `Q==0` branch, with the distinct `D`-split cubic
condition retained.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`

## F1 t=2, j=4 Cycle 37 Hand Gates For Explicit Family

Status: BANKABLE_LEMMA / EXPERIMENTAL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`

In the restricted family

```text
p = 3 mod 4
B = F_p
F = F_{p^2} = B(alpha)
alpha^2 = -1
E = X^2 + alpha X + 1
b = X
D = F_p
```

Cycle 37 banks only these hand checks:

- `E` has no root on `D=F_p`.
- `E` and `E^tau` are separated on `D`.
- The branch `c notin B`, `c_b != 0` is active.
- The remaining free data can be normalized so `kappa=1`.
- The top-symbol quantity is nonzero in the checked normalization, so the
  determinant curve is not identically zero.

This is not a geometric `S4` proof, not a uniform theorem, and not a
counterpacket.

## F1 t=2, j=4 Cycle 38 Repaired Single-Prime S4 Checker

Status: BANKABLE_LEMMA / EXPERIMENTAL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`

Cycle 38 repairs the Cycle 37 checker type error by replacing residue-pair
top coefficients with actual `F`-elements:

```text
W_{n-1..n-4}=1, alpha, 1+alpha, 1.
```

Codex ran the patched checker locally at `p=31`. The result is

```text
PASS_S4_finite_place=true
hist={"1111":1,"112":5,"13":11,"22":6,"4":6,"nonsquarefree":2}
witness_4cycle=[0,0]
witness_13=[4,4]
```

This banks a repaired checker and finite-place monodromy evidence only. It is
not a uniform `S_4` theorem, not geometric `S_4` over `B(z_0,z_1)`, not a
`COUNTERPACKET`, and not an MCA/protocol/prize theorem.
