# Current Active Wall - 2026-06-21 After Cycle 105

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Cycle105 banks the k-free collapse:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s.
```

The active wall is:

```text
For aperiodic Uhat above corrected reserve and every s,
|Gamma cap M_s| <= n^{O(1)}
```

with exponent independent of `s` and `k`.

Generic RS list-size, Johnson-radius, and unconditional divided-difference
routes are cut. The proof must use above-reserve aperiodicity of `Uhat`.

# Current Active Wall - 2026-06-21 After Cycle 104

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE
```

Cycle104 proves the fixed-bandwidth bound:

```text
|Theta_U| <= binom(n,k)(sigma+1).
```

This closes `k=2` and every fixed `k`, but it is not enough for growing
bandwidth. The active wall is to prove:

```text
|Theta_U| <= n^{O(1)}
```

with exponent independent of `k`, after quotient/periodic branches are charged,
or produce a source-valid aperiodic growing-`k` counterpacket.

# Previous Active Wall - 2026-06-21 After Cycle 103

```text
W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE
```

Cycle103 closes bandwidth `k=1`:

```text
|Theta_U| = |e_1(V)| <= (n-sigma+1)(sigma+1) = O(n^2).
```

The remaining upper-side wall starts at `k=2`. For `k>=2`:

```text
theta active
<=> exists rho in F_p[X], deg rho <= k-2, such that
    G(theta,X) + X^(sigma+2) rho(X) divides 1-X^n.
```

The next task is to prove a polynomial distinct-theta bound for this affine
divisor family after quotient/periodic branches are charged, or produce a
source-valid aperiodic counterpacket.

# Previous Active Wall - 2026-06-21 After Cycle 102

```text
L-CYCLE103-E1-IMAGE-ON-FLAT-VARIETY
```

Cycle102 kills the short-window Padé/Berlekamp-Massey denominator route. The
surviving exact upper-side wall is:

```text
|e_1(V)| <= n^{O(1)}
```

where

```text
V = { S' subset mu_n :
      |S'| = m,
      [X^i](g_{S'} Uhat)=0 for i=2,...,sigma+1 }.
```

The numerator remains the distinct support:

```text
|Theta_U| = |e_1(V)|.
```

Do not use the false short-window Padé divisor implication and do not substitute
the weighted count `N=sum_theta F(theta)`.

# Previous Active Wall - 2026-06-21 After Cycle 101

```text
L-CYCLE102-PADE-UNCERTAINTY-LINE-INCIDENCE
```

Cycle101 reframed the distinct-root target as a Fourier-window feasibility
problem for subgroup indicators:

```text
chat(j)=theta^j-P_j, j=1,...,sigma+1.
```

The active incidence form remains:

```text
|Theta_U| = |ell cap E_m|_distinct <= n^{O(1)}.
```

Do not replace this by the weighted count `N=sum_theta F(theta)`. Do not rely
on min-distance/packing alone; Cycle101 cut that route.

Cycle102 should verify or kill the first Padé implication:

```text
theta active
=> Q_theta is divisor-compatible with X^n-1
```

where `Q_theta` is the corrected Padé / Berlekamp-Massey denominator attached
to `(theta^j-P_j)_{j=1}^{sigma+1}`. If false, the answer must give the corrected
lemma or a concrete finite/source-valid counterpacket.

# Previous Active Wall - 2026-06-21 After Cycle 100

```text
L-CYCLE101-DISTINCT-LINE-INCIDENCE-OR-PTE-FIBER-SPLIT
```

Cycle100 shows the weighted character-sum target is stronger than needed:
`N=sum_theta F(theta)` can be large from a single large fiber even when the
distinct root count is small.

Primary target:

```text
|Theta_U| = |line cap E_m|_distinct <= n^{O(1)}.
```

Secondary target:

```text
F_max <= n^{O(1)}
```

for subgroup PTE fibers, including overlapping patterns after
quotient-periodic branches are charged.

# Previous Active Wall - 2026-06-21 After Cycle 99

```text
W-CYCLE100-SUBGROUP-ELEMSYM-MOMENT-CHARACTER-SUM
```

Cycle99 reduced the B1 aperiodic external-root count to the exact
nonzero-frequency error term:

```text
sum_{t != 0} psi(-<t,P>)
  e_s({psi(L_t(x))}_{x in H})
  sum_{theta in F_p \ H} psi(L_t(theta)).
```

The active wall is to prove the aperiodic cancellation bound:

```text
|error numerator| <= p^(sigma+1) n^{O(1)}.
```

If the full sum is too broad, reduce to a smaller monomial or low-rank
elementary-symmetric transform theorem, or produce a nonperiodic prefix with
superpolynomial error.

# Previous Active Wall - 2026-06-21 After Cycle 98

```text
L-CYCLE99-B1-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Cycle98 banked the exact normal form:

```text
Theta_U = v(F_p \ H) cap (P - M_s).
```

The current upper-side wall is to prove or kill:

```text
|v(F_p \ H) cap (P - M_s)_aper| <= n^{O(1)}
```

for the corrected reserve range after quotient-periodic cores are charged.

This is not a direct consequence of the `b=0` prefix local limit. The `b=0`
input controls vertical fibers of the subgroup power-sum image `M_s`; Cycle99
needs a transverse incidence theorem for the moment curve against `M_s`.

The next exact prompt is:

```text
current_repo_snapshot/experimental/notes/m1/cycle99_b1_aperiodic_moment_curve_incidence_prompt.md
```

# Previous Active Wall - 2026-06-20 After Cycle 83

```text
W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION
```

Cycle 83 did not prove `m_max(beta)<=12` and did not find a 13-fold packet.
It returned `EXACT_NEW_WALL / PLAN` in a read-only environment.

The mathematical target remains:

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

but the immediate blocker is execution resources. Cycle 83's proposed resource
tiers are:

```text
Bloom duplicate detector + exact recount: about 66GB RAM.
Deterministic shard/reduce: about 0.5-0.85TB scratch.
Low-disk recompute sharding: around one to several days of repeated passes.
```

The local Mac was effectively full during banking. Codex removed only six
no-token RS-MCA `*-preview-*` staging directories to preserve the raw answer
and write the audit; paid/completed run artifacts were not deleted.

Do not launch another broad theorem prompt before deciding the execution
surface for the threshold census or packet search.

# Previous Active Wall - 2026-06-20 Cycle 83

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

Cycle 82 locally certified:

```text
ALL_4_SUBSETS_PRODUCT_INJECTIVE
fiber_min_distance_lower_bound = 5
```

The injectivity ladder is now a guardrail, not the live target. The next finite
target is the direct color-filtered MITM threshold census:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

Use the banked L/R incidence formula:

```text
m(v)=#{ l in L_img :
        v l^{-1} in R_img
        colorL(l)+colorR(v l^{-1})=4 mod 16 }.
```

The desired next artifact is either a threshold certificate proving no value
reaches count `13`, or an explicit 13-fold colored packet.

# Previous Active Wall - 2026-06-20 Cycle 82

```text
V-CYCLE82-FOUR-SLOT-OR-MITM-MMAX-CERTIFICATE
L-CYCLE82-FOUR-SLOT-PRODUCT-INJECTIVITY
W-CYCLE82-COLOR-FILTERED-MITM-MMAX-CENSUS
```

Cycle 82 answered the four-slot branch with a local Codex certificate. The
MITM `m_max(beta)<=12` branch remains open and is carried into Cycle 83.

# Previous Active Wall - 2026-06-20 Cycle 81

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE81-COMPILED-THREE-SLOT-CERTIFICATE
L-CYCLE80-MINDIST-CERTIFICATE
W-CYCLE80-COMPILED-MITM-MMAX-CENSUS
```

Cycle 80 banks the exact reduction:

```text
three-slot injectivity for (t1,t2,t3)
iff (R_t1 R_t2) cap R_t3 = empty.
```

It does not execute the finite certificate. Codex preserved a pure-Python
checker, but the first run was too slow for a heartbeat-local bounded follow-up.
The next target is therefore executable/certificate-focused: compiled or
vectorized all-triples product-injectivity, or an explicit three-slot collision
packet.

# Previous Active Wall - 2026-06-20 Cycle 80

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE80-MINDIST-OR-SYMMETRIC-ENERGY
L-CYCLE79-MINDIST-EXACT
W-CYCLE79-SYMMETRIC-ENERGY-BOUND
```

Cycle 79 did not prove `m_max(beta)<=12` and did not find a `13`-fold packet.
It banks the complement involution:

```text
Phi(tau(T)) = K / Phi(T),  tau(P_0)=P_0,  m(v)=m(K/v).
```

It also cuts the coherent common-ratio formulation alone as merely another
view of the same fiber count. The next finite target is to decide exact
three-slot product-injectivity:

```text
Is every three-slot product map injective?
```

or to use the tau symmetry to prove a multiplicity/energy bound approaching
`m_max(beta)<=12`.

# Previous Active Wall - 2026-06-20 Cycle 79

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE79-COMMON-RATIO-BOUND-OR-CENSUS
W-CYCLE79-COHERENT-RATIO-SET-SIZE
```

Cycle 78 did not prove `m_max(beta)<=12` and did not find a `13`-fold packet.
It banks the exact left-right incidence formula and cuts another broad census
planning round. The next non-computational theorem target is the coherent
common-ratio set:

```text
Delta subset Ratios(L_img) cap Ratios(R_img)
```

arising from one product fiber. Prove `|Delta|<=12`, find a coherent size-13
set, or reduce to a theorem-grade exact census.

# Previous Active Wall - 2026-06-20 Cycle 78

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE78-EXACT-MMAX-CENSUS
W-CYCLE78-FULL-PRODUCT-INJECTIVITY-OR-13FOLD
```

Cycle 77 did not prove `m_max(beta)<=12` and did not find a `13`-fold packet.
It banks the configuration-evaluation reduction and the fiber-as-code lemma.
Codex locally certified:

```text
all slot subsets of sizes 1 and 2 are product-injective;
fiber minimum distance >= 3.
```

The next target is execution-focused: compute exact `m_max`, find a `13`-fold
packet, or compile/execute the next subset-injectivity frontier beginning with
all 3-subsets.

# Previous Active Wall - 2026-06-20 Cycle 77

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE77-AB-PRODUCT-MAXFIBER
W-CYCLE77-MAX-INTERSECTION-A-B-INVERSE
```

Cycle 76 locally certified the right MITM half:

```text
slots {4,5,6,7}: 48^4 = 5308416 tuples, 5308416 distinct products.
```

Together with the Cycle 75 left-half certificate:

```text
slots {1,2,3}: 48^3 = 110592 tuples, 110592 distinct products.
```

both sides of the MITM split are product-injective. The remaining finite model
object is:

```text
max_v |A cap v B^{-1}| <= 12,
```

or an explicit `13`-fold collision packet in the original constrained domain
`P_0`.

Compiled/sharded census code is useful only if it returns a theorem-grade
certificate. Unrun code is not a proof.

# Previous Active Wall - 2026-06-20 Cycle 76

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE76-RIGHT-HALF-AND-MMAX-CENSUS
W-CYCLE74-DIRECT-MMAX-BUCKET-BOUND
```

Cycle 75 banked a meet-in-the-middle, subfield-norm-sharded max-fiber census
design and corrected the energy heuristic to the constrained-domain scale.
Codex locally certified product-only injectivity for the MITM left half:

```text
slots {1,2,3}: 48^3 = 110592 tuples, 110592 distinct products.
```

Cycle 76's Fable worker could not execute code, but Codex locally added and ran
the optimized right-half checker. The right half is now certified. The remaining
target is the `A*B` max-intersection wall recorded above.

# Previous Active Wall - 2026-06-20 Cycle 75

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE75-DIRECT-MMAX-FIBER-CENSUS
W-CYCLE74-DIRECT-MMAX-BUCKET-BOUND
```

Cycle 74 did not execute the ladder, but it cut the total-energy gate
`D<=155` as likely too strong. Codex checked:

```text
(48^7)^2 / (17^16 - 1) ~= 7082.63.
```

So total off-diagonal collision energy may be much larger than 155 even when
the maximum fiber is below 13. The actual target should be certified directly:

```text
m_max(beta) = max_v #{T in P_0 : product(T)=v} <= 12.
```

The next exact target is a norm-sharded/color-filtered direct max-fiber census,
or an explicit 13-fold collision packet.

# Previous Active Wall - 2026-06-20 Cycle 74

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE74-NORM-BUCKET-COMPILED-LADDER-RUN
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 73 did not execute the expensive ladder. It banks:

```text
L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL
L-CYCLE73-SOUND-NORM-BUCKET
L-CYCLE73-UNCONSTRAINED-D-DOMINATES
```

Codex locally checked the prime-field slot identity on all 336 entries and
verified `eta^16=3` with:

```text
current_repo_snapshot/experimental/scripts/cycle73_prime_slot_norm_check.py
current_repo_snapshot/experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
```

The next exact target is now execution-focused: use the norm bucket, which is a
function of the product and therefore lossless, to produce a real
product-only `k=3/k=4` certificate, preferably `k=5`, or an explicit
collision.

# Previous Active Wall - 2026-06-20 Cycle 73

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE72-COMPILED-PRODUCT-ONLY-LADDER-AND-ENERGY
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 72 did not execute or certify `k=3/k=4`. It is banked as
`AUDIT / BANKABLE_LEMMA / PLAN` because it supplied the exact
displacement-energy decomposition:

```text
D = sum_S 48^(7-|S|) E_S.
```

If the product-only ladder passes through `k=4`, only fully displaced
`|S|=5,6,7` collision energies remain. A single five-slot collision gives
`D>=2304>155`, so `k=5` product-injectivity is mandatory for the current
`D<=155` route.

The next exact target is a real compiled/product-only verifier or structural
proof for `k=3/k=4` (and preferably `k=5`), or an explicit product collision.
No unrun pass should be accepted.

Read:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle72_product_only_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/cycle72_product_only_ladder_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle73_compiled_product_ladder_packet/CYCLE73_COMPILED_PRODUCT_LADDER_PROMPT.md
```

before relying on the Cycle 72 raw response.

# Previous Active Wall - 2026-06-20 Cycle 72

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE71-PRODUCT-ONLY-K3-K4-LADDER-RUN
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 71 did not execute the `k=3/k=4` rungs. It banks the
full-displacement lemma, but its Python verifier used `(color, product)` as the
duplicate key. That is not a valid product-injectivity proof unless product
equality is already known to force color equality. Codex added a corrected
product-only reference script and locally rechecked only `k<=2`.

The next exact target is a real product-only optimized/compiled run for
`k=3/k=4`, or a proof that product equality forces color equality, or an
explicit partial collision.

Read:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle71_optimized_ladder_audit.md
current_repo_snapshot/experimental/scripts/cycle71_product_ladder_checker.py
current_repo_snapshot/experimental/notes/m1/cycle71_product_ladder_certificate.json
```

before relying on the Cycle 71 raw response.

# Previous Active Wall - 2026-06-20 Cycle 71

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE70-K3-K4-OPTIMIZED-LADDER-RUN
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 70 cut the tempting t-independent slot collapse

```text
u_t(i,a) = prod_{c in 3^a D_i}(beta^2-c),
```

with a local counterexample at `(t,i,a)=(1,1,0)`. The surviving exact identity
is the original t-dependent Cycle 68 formula:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

The next task is an executable optimized verifier or structural proof for the
`k=3` and `k=4` product-injectivity rungs, or an explicit partial collision.
Read:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle70_k3_k4_ladder_audit.md
current_repo_snapshot/experimental/scripts/cycle70_slot_normalization_checker.py
current_repo_snapshot/experimental/notes/m1/cycle70_slot_normalization_certificate.json
```

before relying on the Cycle 70 raw response.

# Previous Active Wall - 2026-06-20 Cycle 70

The live model-level M1/scalar-apolar target is now:

```text
V-CYCLE69-K3-K4-INJECTIVITY-LADDER
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 69 banks the energy gate

```text
D <= 155 => m_max(beta) <= 12 => Occ(beta) >= |P_0|/12 > 2^32,
```

where `D=sum_v m_v(m_v-1)` is the ordered off-diagonal collision count.
Codex locally verified the complement oracle and the product-injectivity
ladder through `k=2`; a pure-Python `k=3` run was interrupted for performance,
not for mathematical failure. The next exact task is to prove/kill the `k=3`
and `k=4` ladder rungs by optimized verifier or structural proof, then either
bound `D` or exhibit a 13-fold collision.

Read:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle69_slot_log_independence_audit.md
current_repo_snapshot/experimental/scripts/cycle69_ladder_probe.py
current_repo_snapshot/experimental/notes/m1/cycle69_ladder_probe_certificate.json
```

before older Cycle 68 notes.

# Previous Active Wall - 2026-06-20 Cycle 69

The live model-level M1/scalar-apolar target is now:

```text
L-CYCLE68-SLOT-LOG-INDEPENDENCE
W-CYCLE68-SLOT-SUMSET-MULTIPLICITY
```

Cycle 68 banks the disjoint-coset factorization below the previous
`m_max(beta)<=12` wall. The remaining object is a short-relation / seven-slot
sumset multiplicity problem for the 112 elements
`beta^2-eta^(2t+16b)`. Read
`current_repo_snapshot/experimental/notes/m1/m1_cycle68_collision_multiplicity_audit.md`
and the local checker before older notes.

# Current Active Wall - 2026-06-20 Cycle 68

The live M1/scalar-apolar target is now:

```text
W-CYCLE67-COLLISION-MULTIPLICITY
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

Cycle 67 cuts the pure cross-color shortcut and replaces it with the exact
multiplicity target:

```text
m_max(beta) <= 12,
m_max(beta)=max_v #{T in P_0 : P_T(beta)=v}.
```

Because `|P_0|=52,747,567,104`, this implies
`Occ(beta)>=|P_0|/12>2^32`. Read
`current_repo_snapshot/experimental/notes/m1/m1_cycle67_cross_color_injectivity_audit.md`
before the older Cycle 66 audit.

# Current Active Wall - 2026-06-20 Cycle 67

The live M1/scalar-apolar target is now:

```text
L-CYCLE66-CROSS-COLOR-INJECTIVITY-LOWER-BOUND
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

Cycle 66 made the sevenfold occupancy verifier precise but did not compute
`Occ(beta)` or prove `Occ(beta) >= 2^32`. The next symbolic attempt is the
cross-color injectivity/lower-bound shortcut:

```text
Occ(beta) >= 8^7 * (# independent color classes),
```

or a concrete collision mechanism killing that shortcut. Read
`current_repo_snapshot/experimental/notes/m1/m1_cycle66_sevenfold_product_occupancy_audit.md`
before the older Cycle 65 audit.

---

# Previous Active Wall - 2026-06-20 Cycle 66

The live M1/scalar-apolar verifier target is:

```text
V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

Cycle 65 reduces thickened color occupancy to a constrained sevenfold
product-set in `F_{17^16}^*`. Read
`current_repo_snapshot/experimental/notes/m1/m1_cycle65_thickened_gadget_color_audit.md`
before older wall entries.

Cycle 66 answered this as `AUDIT / BANKABLE_LEMMA / EXACT_NEW_WALL`: it
corrected admissibility to `beta notin mu_256`, reformulated occupancy as
distinct locator evaluations, and supplied a self-checkable finite setup. It
did not solve the full occupancy count.

---

# Current Active Wall - 2026-06-20 Cycle 65

The live M1/scalar-apolar wall is:

```text
W-MODEL-GJ-THICKENED-GADGET-COLOR-OCCUPANCY
```

Cycle 64 closed the exact prefix-gadget convolution but cut gadget charge as a
scalar smallness certificate. The next task is to prove/kill the Role 05
thickened color occupancy calculation. Read
`current_repo_snapshot/experimental/notes/m1/m1_cycle64_prefix_collision_gadget_audit.md`
before older wall entries.

---

# Active Walls

## W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

Cycle 44 refines the Cycle 43 cosupport subset-product wall to an exact
moment/cancellation object. In the restricted full-base-domain branch

```text
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
deg E = t = sigma,
A = F[X]/E,
j = |T| = n-a,
```

for `T=D\S`, `I_S=interp_S(w)`, `xi=[X]_E`,
`ell=[X^p-X]_E`, `Lambda(T)=[L_T]_E`, Cycle 44 banks

```text
rho(T) = [I_S]_E = -ell * Lambda(T)^(-1) * N(T),
N(T)=sum_{d in D} w(d)L_T(d)(xi-d)^(-1).
```

Writing `L_T(X)=sum_m (-1)^m e_m(T)X^(j-m)`, both `N(T)` and
`Lambda(T)` are affine-linear in the elementary symmetric functions `e_m(T)`.
The landing condition `rho(T) in F*b` is therefore reduced to elementary
symmetric exponential sums over `j`-subsets of `F_p`.

Banked exact landing formula:

```text
#Land = binom(p,j)/p^(2(t-1)) + E_error,
```

where `E_error` is an explicit nonzero-character sum over the structured cone
`c(eta,z)`.

Preferred live subwall:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

Prove

```text
M_2 = sum_z nu(z)^2 <= #Land + (1+o(1)) #Land^2/q_line,
```

where `nu(z)=#{T: rho(T)=z b}`. Or falsify it by producing a source-valid
growing family with a high-multiplicity slope

```text
max_z nu(z) >= #Land/p^(1+epsilon).
```

Do not promote this to a reserve lift, generated-field theorem, MCA/list/
line/curve-MCA consequence, protocol, SNARK, prize result, or final
counterpacket. Cycle 44 banks the exact identity and the exact wall only.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260619_CYCLE44_COSUPPORT_MOMENT_IDENTITY_AUDIT.md`

## W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION

Status: EXACT_NEW_WALL / BANKABLE_LEMMA / AUDIT / EXPERIMENTAL / answered by
Cycle 44 and superseded by
`W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION`.

Cycle 43 cuts the literal route of directly amplifying the fixed `t=2,j=4`
quartic/S4 mechanism to reserve scale. The fixed branch is the square point
`j=2t`; reserve scale instead has

```text
t = sigma = Theta(n/log n),
j = Theta(n),
j >> 2t.
```

So the square Cramer / single quartic monodromy object is not the reserve-scale
object. Along the balanced diagonal `j=2t -> infinity`, totally split
monodromy density is at most `1/j -> 0`, so the fixed `1/24` density cannot
survive as a literal monodromy amplification.

Cycle 43 redirects the reserve wall to cosupport-residue equidistribution:

```text
rho(T) = [I_{D\T}]_E,
Land = {T : rho(T) in F*b},
Slopes = {z in F : exists T, rho(T)=z b}.
```

Useful heuristic skeleton:

```text
N_split ~ min(q_line, C(p,j)/p^{2(t-1)}),
```

which matches the banked fixed `j=2`, `j=3`, and `j=4` regimes but is not
proved in reserve scale. The next theorem-sized object is cancellation /
decoupling / anticollision for subset-product moments

```text
e_j({chi(xi-d)}_{d in F_p}),   xi=[X]_E, chi nontrivial on (F[X]/E)^*.
```

Subtargets:

1. prove cancellation in the elementary-symmetric character sums;
2. prove quotient decoupling for `[I_{D\T}]_E`;
3. bound landing multiplicities `max_z #{T in Land : rho(T)=z b}`;
4. exhibit explicit separated growing-degree denominators
   `deg E = sigma = Theta(n/log n)` with no roots on `D=F_p`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`

## W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT /
answered by Cycle 43 and superseded by
`W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`.

Cycle 42 external 5.5 Pro round cuts the prior A-side good-reduction
obstruction for the fixed restricted `t=2,j=4` branch. Four external answers
and returned checker/certificate artifacts agree that Cycle 41's raw
affine/Cramer `(G1,G2,G3)` gate was overstrong: its A-side failure is a false
negative caused by unsaturated/projective/common-factor behavior, not a
source-valid obstruction. Conservatively banked result:

```text
restricted fixed branch:
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
t = sigma = 2,
j = 4,
N_split(p) = p^2/24 + O(p^(3/2))
           = q_line/24 + O(q_line^(3/4)).
```

This is a restricted local closure only. It is not a corrected-reserve,
fixed-rate, generated-field, MCA/list/line-decoding/curve-MCA, protocol,
SNARK, prize, or final `COUNTERPACKET` result.

The live wall is now reserve scaling:

1. Construct a source-valid family lifting the closed fixed `t=2,j=4`
   mechanism to growing `t=sigma >= C n/log n`, `j=Theta(n)`, separated
   denominator/cosupport data, and positive noncontained split-slope density.
2. Or prove a theorem-sized obstruction showing that the quartic local
   monodromy mechanism cannot be reserve-scaled.
3. Keep `q_gen`, `q_line`, `q_chal`, `B`, and `F` separate. Do not merge the
   fixed restricted ledger into a prize-level generated-field statement.

Aliases:

```text
W-F1-AA-RES-T2J4-TO-CORRECTED-RESERVE-SLOPE-PRESERVING-LIFT
W-F1-AA-RES-RESERVE-SCALED-GENERATED-FIELD-QUARTIC-CORE-LIFT
```

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`

## W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT /
answered by Cycle 42 and superseded by
`W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT`.

Cycle 40 banks finite-place geometric `S_4` evidence in both locator-collapse
subcases. The off-singular histogram criterion `"4"` plus `"13"` gives
`G_arith=G_geom=S_4` at the tested finite prime. Codex ran the parametrized
checker locally and got `all_pass=true`:

```text
Subcase A, ell=alpha: p=7,23,43,47 pass.
Subcase B, ell=-2X:  p=11,19,31,59 pass.
```

The remaining bridge is not more finite-place `S_4`; it is the
characteristic-zero branch data and good-reduction certificate. Separately for
`ell=alpha` and `ell=-2X`, compute or certify:

1. the characteristic-zero determinant/branch polynomial `Delta(z_0,z_1)`;
2. the numerator of `disc_X L_tau` over `Q(i)(z_0,z_1)`;
3. a finite prime from the passing list that is actually a good-reduction
   prime for that characteristic-zero cover;
4. the tame-specialization step from characteristic zero to the finite-place
   geometric `S_4` certificate;
5. the Chebotarev/Lang-Weil density step only after the good-reduction bridge
   is source-valid.

Do not promote this to `COUNTERPACKET`, corrected-reserve, MCA, CA, list,
line-decoding, curve-MCA, protocol, SNARK, or prize status without the missing
source hypotheses.

## W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE

Status: PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / answered by Cycle
40 and superseded by `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA`.

Cycle 39 banks the restricted locator-collapse lemma for the explicit family

```text
p = 3 mod 4,
B=F_p,
F=F_{p^2}=B(alpha),
alpha^2=-1,
E=X^2+alpha X+1,
b=X,
D=F_p,
u=[W]_E=1+X,
W_{n-1..n-4}=1,alpha,1+alpha,1,
ell=[X^p-X]_E.
```

The collapse is:

```text
Subcase A: (-5/p)=+1, equivalently p=2,3 mod5, ell=alpha.
Subcase B: (-5/p)=-1, equivalently p=1,4 mod5, ell=-2X.
```

The existing Cycle 38 finite-place certificate at `p=31` lies only in
Subcase B. It does not certify Subcase A, and it does not by itself prove good
reduction.

Former tasks:

1. Produce a finite-place `S_4` certificate for Subcase A, preferably at
   `p=7`, `23`, `43`, or `47`.
2. Certify the good-reduction bridge in each subcase: degree of `Delta`,
   separability of the quartic cover, etaleness away from the branch divisor,
   cubic-resolvent irreducibility, and nonconstant squarefree discriminant.
3. Or prove a `ROUTE_CUT`: one subcase is reducible, trapped in `A_4`, has a
   constant-field obstruction, or otherwise cannot yield the restricted seed.
4. Do not promote this to `COUNTERPACKET`, corrected-reserve, MCA, CA, list,
   line-decoding, curve-MCA, protocol, SNARK, or prize status without the
   missing source hypotheses.

## W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED

Status: PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / answered by
Cycle 39 and superseded by `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE`.

Cycle 38 repaired the Cycle 37 checker and produced a local finite-place
certificate at `p=31`. Cycle 39 removes the apparent free `p`-dependence by
proving the locator-collapse lemma and splitting the branch into Subcase A
and Subcase B.

## W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT / answered at
finite-place level by Cycle 38 and superseded by
`W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED`.

Cycle 36 banks the explicit source-valid family

```text
p = 3 mod 4,
B=F_p,
F=F_{p^2}=B(alpha),
alpha^2=-1,
E=X^2+alpha X+1,
b=X.
```

The denominator has no roots on `D=F_p` and is separated from `E^tau`.
The remaining free data must be chosen with `kappa != 0`.

Tasks:

1. Choose fixed remaining data `(u,W_{n-1},...,W_{n-4})` with `kappa != 0`.
2. Build the Cycle 29/30/32 system `M(z)tau=-C_0(z)` for
   `z=z_0+alpha z_1`.
3. Restrict to a generic line `z_1=m z_0+e` at one good prime `p0=3 mod 4`.
4. Certify `Delta=det_B M(z)` is nonzero with the expected source-valid
   top-symbol behavior.
5. Certify quartic transitivity/geometric irreducibility, preferably with a
   finite-place factorization type `"4"`.
6. Certify cubic-resolvent absolute irreducibility and discriminant
   nonsquareness/nonconstant squarefree part.
7. If successful, state only the restricted local counterpacket seed; do not
   promote to corrected-reserve, MCA, CA, list-decoding, line-decoding,
   curve-MCA, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-A2B-UNIFORM-S4

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT / answered by
Cycle 36 and superseded by `W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT`.

Cycle 35 banks a finite-place monodromy certificate in the restricted
`D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_gen=p`, `q_line=p^2`, `t=sigma=2`,
`j=4` branch:

```text
off-Delta squarefree types "4" and "13"
  => G_arith=S_4,
and the even type "13" cuts the sign constant-field obstruction,
  => G_geom=G_arith=S_4
```

This applies per fixed tested instance. It upgrades the Cycle 32 finite
histograms to serious `EXPERIMENTAL / AUDIT` evidence, but it is not a
uniform-in-`p` theorem.

Tasks:

1. Construct explicit source-valid parameters
   `(E, b, W_{n-1},...,W_{n-4})` for infinitely many primes, keeping
   `q_gen=p`, `B=F_p`, `F=F_{p^2}`, and `q_line=p^2` separate.
2. Prove `G_geom(L_tau / \bar B(z_0,z_1))=S_4` uniformly, ideally by an
   explicit slice, irreducible resolvent, and nonsquare discriminant
   certificate.
3. Prove arithmetic/geometric equality, or state the exact constant-field
   obstruction.
4. If the uniform route works, state only the restricted local
   `Theta(q_line)` counterpacket seed with all hypotheses; do not promote it
   to corrected-reserve, MCA, CA, list-decoding, line-decoding, curve-MCA,
   protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / answered by
Cycle 35 and superseded by `W-F1-AA-RES-T2J4-A2B-UNIFORM-S4`.

Cycle 34 banks the off-curve dominance side of the `A^2_B` monodromy wall.
In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=4`
branch, on the stated source-valid dense open,

```text
psi: z |-> tau(z)=M(z)^(-1)(-C_0(z))
```

has generic `B`-Jacobian rank two and is birational onto the Cycle 30
quadric image. Therefore the off-curve family is genuinely surface-sized.
The rank-one / hidden curve-collapse explanation for `O(p)` is cut.

The finite-place version of the geometric monodromy and constant-field gate for

```text
L_tau=X^4-tau_1 X^3+tau_2 X^2-tau_3 X+tau_4
```

over `B(z_0,z_1)`, with splitting over `B=F_p`, is now certified per
instance by Cycle 35 when types `"4"` and `"13"` occur off `Delta`.

Former tasks:

1. Prove geometric transitivity, ideally `G_geom=S_4`, for the substituted
   quartic family.
2. Prove arithmetic/geometric equality, i.e. no constant-field obstruction.
3. Or produce the exact obstruction: reducible resolvent, square
   discriminant, constant-field extension, or a source-valid counterpacket.
4. Produce an explicit symbolic checker/certificate for `disc_num`, the cubic
   resolvent, and the constant-field tests.

Keep this as a local residue-line problem only. Do not promote it to list, CA,
MCA, line-decoding, curve-MCA, `q_gen`, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / answered by
Cycle 34 and superseded by the geometric-S4 wall.

Cycle 33 banks the singular-bound side of the `A^2_B` monodromy wall. Under
the Cycle 29 top-symbol nonzero hypotheses, the determinant curve

```text
Delta(z_0,z_1)=det_B M(z)=0
```

has degree at most four and is not the zero polynomial. Therefore it has at
most `4p` points over `B=F_p`, so the singular determinant curve contributes
only `O(p)` split slopes in the restricted `t=2,j=4` branch.

The live problem is now the off-curve family:

```text
tau(z_0,z_1)=M(z)^(-1)(-C_0(z)),
L_tau=X^4-tau_1 X^3+tau_2 X^2-tau_3 X+tau_4.
```

Tasks:

1. Decide whether `tau:A^2_B -> A^4_B` has generic `B`-Jacobian rank two.
   Rank two preserves the `p^2`-scale image; rank at most one would be the
   hidden `O(p)` collapse.
2. Compute/source-audit the cubic resolvent and square class of
   `disc_X L_tau` after substituting `tau(z_0,z_1)`.
3. Identify the geometric/arithmetic monodromy group or a constant-field
   obstruction.

Keep this as a local residue-line problem only. Do not promote it to list, CA,
MCA, line-decoding, curve-MCA, `q_gen`, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE

Status: BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL / AUDIT / superseded
by the dominance-resolvent wall.

Cycle 32 cuts the one-variable `B(z)` / `F(z)` framing. The `t=2,j=4`
quartic family must be treated as a two-dimensional `B`-surface family over
`A^2_B`, with coordinates

```text
z = z_0 + alpha z_1,     z_0,z_1 in B=F_p,
F=F_{p^2},               q_line=p^2.
```

Off the determinant curve

```text
Delta(z_0,z_1)=det_B M(z)=0,
```

the Cycle 29/30 Cramer system gives a unique quartic

```text
L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4.
```

Codex added a local histogram checker implementing

```text
(u - z b) * [L_tau]_E - ell * [Q_tau]_E = 0 in A=F[X]/E.
```

It matches direct support enumeration away from `Delta=0`; mismatches are
tracked as `singular_split_C2` and remain boundary/audit material.

Cycle 33 answers the first part of the wall: `Delta=0` contributes at most
`4p` split slopes under the Cycle 29 top-symbol nonzero hypotheses. The
off-curve dominance/resolvent problem remains live.

Keep this as a local residue-line problem only. Do not promote it to list, CA,
MCA, line-decoding, curve-MCA, `q_gen`, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4

Status: EXACT_NEW_WALL / superseded by `A^2_B` monodromy-certificate audit.

Cycle 31 turns the split-quadric-collapse question into an exact quartic
monodromy wall. It does not prove that `O(p)` collapse is impossible and does
not bank a `Theta(q_line)` counterpacket. It identifies the next invariant:

```text
disc_X L_{tau(z)}, resolvent cubic, and geometric monodromy of L_{tau(z)}.
```

The base-field issue is part of the wall: `z` ranges over `F=F_{p^2}`, while
the quartic must split into roots in `B=F_p`. A correct proof must decide
whether the family lives over `B(z_0,z_1)`, over `F(z)`, or as a
two-dimensional `B`-parameter family with an `F_p`-splitting condition.

Live problem:

1. Compute/source-audit `disc_X L_{tau(z)}` and the resolvent cubic from the
   Cycle 29 square-system columns.
2. Certify `G=S_4` or identify the actual transitive subgroup.
3. Apply the correct function-field Chebotarev/Weil or equivalent finite-field
   splitting statement, if applicable.
4. If monodromy degenerates, identify the exact invariant forcing possible
   sub-`Theta(q_line)` behavior.

Keep this as a local residue-line problem only. Do not promote it to list, CA,
MCA, line-decoding, curve-MCA, `q_gen`, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE

Status: EXACT_NEW_WALL / superseded by quartic monodromy audit.

Cycle 30 reduces the `t=2,j=4` split-quartic gate to one `F`-quadric, i.e.
two `B`-quadrics, in elementary-symmetric co-support coordinates
`tau=e(T)`.

Ledger:

```text
D=F_p,
B=F_p,
F=F_{p^2},
q_gen=p,
q_line=p^2,
t=sigma=2,
j=4,
off R0,
source-valid separated E=X^2+cX+d,
c_b != 0.
```

The gate is:

```text
Phi(tau)=iota wedge_F mu
        = kappa*N_{A/F}(lambda)
          - (ell*[Q_S]_E) wedge_F (b*lambda) = 0,
lambda=[L_T]_E.
```

Because `Q_S` is independent of `tau_4` and `lambda=lambda'+tau_4`,

```text
Phi = kappa*tau_4^2
    + tau_4*(kappa*Tr_{A/F}(lambda') - (ell[Q_S]_E) wedge_F b)
    + (kappa*N_{A/F}(lambda') - (ell[Q_S]_E) wedge_F (b lambda')).
```

Codex finite scans over random small source-valid instances count distinct
bad slopes by direct division and `line_scalar` tests. The data lean toward
`O(p)`, not the naive positive-density `Theta(p^2)` heuristic:

```text
p=17 avg_C2/p=0.482, avg_C2/p^2=0.0284
p=19 avg_C2/p=0.618, avg_C2/p^2=0.0325
p=23 avg_C2/p=0.739, avg_C2/p^2=0.0321
p=29 avg_C2/p=1.078, avg_C2/p^2=0.0372
```

Live problem:

1. Prove a hidden rational-root, discriminant, trace/norm, Frobenius, or
   factorization collapse that cuts the totally split distinct locus down to
   `O(p)`.
2. Or construct a source-valid growing-prime family realizing
   `Theta(q_line)` slopes and explain why the random finite scan missed it.
3. Or isolate the exact next invariant: resultant, discriminant, rational-root
   criterion over `F_p(V)`, Galois group condition, or refined checker.

Keep this as a local residue-line problem only. Do not promote it to list,
CA, MCA, line-decoding, curve-MCA, `q_gen`, protocol, SNARK, or prize status.

## W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / superseded by split-quadric collapse.

Cycle 30 answers the first split-quartic-gate formulation by deriving the
explicit split-quadric equation above. The remaining wall is not the existence
of the gate, but whether its totally split distinct locus collapses to `O(p)`
or admits a `Theta(q_line)` source-valid family.

## W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / superseded by split-quartic gate.

Cycle 29 answers this wall: the top-symbol mechanism persists at the level of
the square determinant, but the determinant no longer bounds slopes because it
is an invertibility determinant.

Banked content:

```text
TopSym(det_B M(z))=-N(kappa)N(z)^2Q_4,
```

where `Q_4` is the Cycle 28 locator quantity and is source-validly nonzero.

Current wall: `W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE`.

## W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT

Status: PROOF / ROUTE_CUT / superseded by Cycle 28.

Cycle 27 appears to cut the remaining `Q==0` obstruction in the restricted
`D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0` window by
identifying

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

The locator identity is

```text
c notin B:
  Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

So `Q_4=0` iff `E` has an `F_p` root iff the Cycle 24 locator norm
`prod_{a in F_p}E(a)` vanishes. Source-validity should exclude this. For
`c in B`, separatedness should force `d notin B`, making
`Q_4=N(c_b)*Im(d)^2` nonzero.

Live task:

1. Reconstruct the Cycle 15/16 columns and Cycle 25 Plucker/Laplace
   determinant.
2. Recompute `Q_4` directly.
3. Verify or refute the `P`-cancellation and the locator identity.
4. Decide whether the restricted `t=2,j=3` branch can be promoted from
   `BANKABLE_LEMMA / AUDIT` to local `PROOF`.

Do not promote anything to corrected-reserve MCA, protocol, list-decoding,
line-decoding, CA, curve-MCA, SNARK, or prize status.

## W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE

Status: ROUTE_CUT / superseded by
`W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT`, pending independent source audit.

Cycle 26 sharpens the rank-consistency wall. In the NONDEP case for
`C(z)=[c_1(z)|c_2(z)|c_3(z)]`, rank-drop costs only `O(p)` slopes; away from
rank-drop, `Q(z)=0` is necessary and sufficient for affine consistency.
Moreover, in the `c notin B`, `c_b != 0` branch, the leading symbols
`-c_b c` and `-c_b` are `B`-independent, so that branch is NONDEP.

Thus the remaining NONDEP obstruction is:

```text
Q(z_0,z_1) == 0 identically,
source-valid,
D != 0,
det M=(c_b/kappa^2)D != 0,
distinct D-split cubics retained.
```

Cycle 26 proposes an audit-only top-degree obstruction:

```text
Q_4 = N(c_b) *
      ( Im_alpha(c) Im_alpha(q2^0)
      + Im_alpha(conj(c) w) Im_alpha(q2^2)
      - Im_alpha(w) Im_alpha(q2^1) )

w=c^2-d,
q2^2=P,
q2^1=d+Pc,
q2^0=cd+P w.
```

Live problem:

1. Verify or refute this `Q_4` formula from the Cycle 15/16 column definitions.
2. If correct, prove or refute source-valid `Q_4 != 0` on the NONDEP
   `c notin B` branch.
3. If `Q_4=0` can occur, decide whether all lower coefficients of `Q` can
   vanish while the distinct `D`-split cubic gate is retained.
4. Keep affine `tau in B^3` consistency separate from actual line-incidence by
   distinct split cubics.

Do not bank the `Q_4` formula, `Q_4 != 0`, or any `Theta(q_line)`
counterpacket until source-checked.

## W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY

Status: EXACT_NEW_WALL / superseded by
`W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE`.

Cycle 25 corrects the determinant-only wall. For fixed `z`, the affine system

```text
c_1(z)tau_1+c_2(z)tau_2+c_3(z)tau_3+c_0(z)=0 in B^4
```

realizes a slope iff

```text
c_0(z) in span_B(c_1(z),c_2(z),c_3(z)).
```

The determinant

```text
Q(z)=det_B[c_1(z)|c_2(z)|c_3(z)|c_0(z)]
```

is necessary but sufficient only on the rank-three stratum of
`C(z)=[c_1(z)|c_2(z)|c_3(z)]`. On rank-drop strata, augmented-rank minors are
needed.

Live problem:

```text
source-valid E nonzero on D=F_p,
off R0,
c_b != 0,
D != 0,
det M=(c_b/kappa^2)D != 0,
Q(z_0,z_1)==0 identically,
rank-stratified consistency conditions,
distinct D-split cubics retained.
```

Decide whether the realized slope set is always `O(p)` or whether there is a
source-valid growing-prime family with `Theta(p^2)=Theta(q_line)` realized
slopes.

This remains sub-reserve (`eta_reserve=2/n`) and must not be promoted to a
corrected-reserve, `q_gen`, protocol, list-decoding, line-decoding, CA, MCA, or
SNARK statement.

## W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT

Status: EXACT_NEW_WALL / superseded by
`W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`.

Cycle 24 cuts the entire source-valid `D=0`, off-`R0` branch in the restricted
`D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3` window:

```text
ell=[X^p-X]_E=mu*(xi+c/2)+delta_c,
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a).
```

Since source-valid denominators are nonzero on `D=F_p`, `N(ell)!=0`; off
`R0`, `kappa!=0`; hence `D!=0`.

The live branch returns to Cycle 16's determinant-split wall. On source-valid
`Ra/Rb` resonance data, distinct `D`-split cubics, and off `R0`, decide the
remaining case:

```text
Q(z_0,z_1)==0 identically,
D!=0,
det M=(c_b/kappa^2)D != 0.
```

Questions:

1. Does `Q==0` with `det M!=0` force the split-cubic slope image to be `O(p)`?
2. Or is there a source-valid growing-prime family with
   `C2=Theta(p^2)=Theta(q_line)`?
3. If neither can be proved immediately, isolate the exact invariant,
   elimination ideal, or finite checker schema deciding the branch.

Cycle 25 sharpens this: `Q==0` alone is not enough to realize slopes because
rank-drop strata require augmented-rank conditions.

## W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C

Status: ROUTE_CUT / superseded by
`W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT`.

Cycle 24 proves the stronger norm factorization

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a).
```

For source-valid denominators nonzero on `D=F_p`, `N(ell)!=0`; off `R0`,
`kappa!=0`; so this `D=0` branch is empty. Do not keep prompting this wall.

Historical statement before cut:

Cycle 23 cuts the previous `c in B`, `d notin B` nonemptiness target. In the
restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0`
window, it proves

```text
if c in B, d notin B, and kappa != 0, then D != 0.
```

The exact closed form is

```text
ell=[X^p-X]_E=mu*(xi+c/2),
D=-mu^2(c^2/4-d)kappa.
```

Therefore the only surviving separated `D=0`, off-`R0` lane is

```text
D=0
off R0
E separated
c notin B.
```

The live wall is to decide the nonsplit-`c` branch:

```text
c notin B,
E separated,
Delta1==0,
D=0,
off R0,
c_b=-Q_E(b)/kappa != 0,
W_{n-1} != 0.
```

Questions:

1. Compute `ell=[X^p-X]_E` in usable closed form for `c notin B`.
2. Re-derive `D` as an explicit bilinear form in `(u,b)` with coefficients
   from `(c,d)` and Frobenius.
3. Decide whether `D=0`, `Delta1==0`, and off-`R0` are jointly empty,
   curve-sized, or surface-sized.
4. If nonempty, decide whether the split-cubic slope set is `O(p)` or
   `Omega(p^2)=Omega(q_line)` over growing primes.

## W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS

Status: ROUTE_CUT / superseded by
`W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C`, then cut by Cycle 24.

Cycle 23 proves the `c in B`, `d notin B`, `D=0`, off-`R0` stratum is empty by
the closed form `D=-mu^2(c^2/4-d)kappa`. The live wall is now the
complementary `c notin B` lane above.

## W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT

Status: EXACT_NEW_WALL / superseded by
`W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS`.

Cycle 21 banks differential collapse gates for the restricted
`D=F_p`, `t=sigma=2`, `j=3`, off-`R0` branch. On `Delta1==0`, with

```text
L(f)=partial_{tau_1} f - c partial_{tau_2} f,
J_A=L(A/kappa),
J_Aprime=L(A'/kappa),
```

simultaneous slope-branch collapse is governed by

```text
J_A=0,
J_Aprime=0.
```

With

```text
m=W_{n-2}+c W_{n-1},
w_1=W_{n-1},
```

the gates are

```text
kappa J_A      = -(ell wedge b)m + P_E(b,ell)w_1,
kappa J_Aprime = -(u wedge ell)m - P_E(u,ell)w_1,
```

and their resultant is the Cycle 20 gate

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

The live wall is now the `D=0` compatibility condition. Decide whether

```text
Delta1==0,
D==0,
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0
```

force the leading-data ratio

```text
(W_{n-2}+cW_{n-1}:W_{n-1})
```

onto the kernel line of

```text
[(ell wedge b), -P_E(b,ell);
 (u wedge ell),  P_E(u,ell)].
```

If yes, the `D=0` branch collapses by the banked gates. If no, an off-kernel
source-valid family is the first serious seed for a `Theta(q_line)`
counterpacket in this sub-reserve toy window.

This remains sub-reserve (`eta_reserve=2/n`) and must not be promoted to a
corrected-reserve, `q_gen`, protocol, list-decoding, line-decoding, CA, MCA, or
SNARK statement.

## W-F1-AA-RES-T2J3-B-RANKONE-DESCENT

Status: EXACT_NEW_WALL / superseded by `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`.

Cycle 20 banks the rank-one/gate structure in the restricted
`D=F_p`, `t=sigma=2`, `j=3`, off-`R0` window:

```text
q1=c_b eta,
eta=(c^2-d)+c tau_1+tau_2,
w^+-=(+-sqrt(delta_z)-A/kappa)/(2c_b eta)
```

on the `Delta1==0` quadric branch, where `delta_z in B[tau_1,tau_2]`.

The `P^2(F)` coefficient-image gate is

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell),
det M=(c_b/kappa^2)D.
```

The open wall is finer than `D=0`: decide whether the base-descent equations

```text
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0
```

force

```text
dw wedge d eta == 0,
```

hence `dim_B Im(w)=1` and `C2=O(p)`, or whether there is source-valid data with
`dw wedge d eta != 0`, giving a seed for `C2=Theta(p^2)=Theta(q_line)` over
growing primes.

This remains sub-reserve (`eta_reserve=2/n`) and must not be promoted to a
corrected-reserve, `q_gen`, protocol, list-decoding, line-decoding, CA, MCA, or
SNARK statement.

## W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE

Status: EXACT_NEW_WALL.

Cycle 18 banks a restricted monicity lemma in the `D=F_p`,
`t=sigma=2`, `j=3`, off-`R0` window. In the `{[W]_E,b}` basis,

```text
Delta(tau)=wedge_{W,b}(iota,mu)
          =(p1-tau_3)(q2-tau_3)-p2 q1
```

is monic quadratic in `tau_3`. Splitting `Delta=Delta0+alpha Delta1` over
`F=B+alpha B` gives `Delta0` monic degree `2` in `tau_3` and
`deg_{tau_3} Delta1<=1`.

The safe side remains: if `Delta0,Delta1` have no common component over the
algebraic closure of `B`, then `C2=O(p)`.

The active wall is the non-coprime resonance branch. Since
`deg_{tau_3} Delta1<=1`, the branch is either `Delta1==0` or a graph
`tau_3=-h/s`. In the graph case, the slope map reduces to

```text
z(tau_1,tau_2)=(p1+h/s)/q1,
```

equivalently to the coefficient map

```text
mu_coef : (tau_1,tau_2) -> [q1 : (p1-q2) : p2] in P^2(F).
```

The next task is to prove this rational map has one-dimensional image on every
source-valid non-coprime stratum, forcing `C2=O(p)`, or construct a
growing-prime source-valid family with `C2=Theta(p^2)=Theta(q_line)`.

Do not promote this sub-reserve toy-window wall to a corrected-reserve theorem,
`q_gen` statement, protocol claim, list-decoding statement, CA, MCA, or
line-decoding statement.

## W-F1-AA-RES-T2J3: Next Finite Extension Bad-Line Incidence Wall

Status: EXACT_NEW_WALL.

Cycle 11 closes the first finite bad-line incidence regime `t=sigma=2`,
`j=n-a=r-t=2`: in that regime

```text
Q_S = C(X-s_T)+C1
```

depends only on the co-support sum, and bad-line landing is one conic
`det(s_T,p_T)=0`, giving `C2=O(n)` under the stated nonresonance hypotheses.

The next target is:

```text
W-F1-AA-RES-T2J3:
prove or refute the bad-line incidence law for t=2, j=3.
```

Reason: at `j=3`, `deg Q_S<=2`, so the quotient should acquire dependence on
both elementary co-support parameters and the special Cycle 11 sum-only
rigidity is expected to fail. The task is to determine whether a replacement
low-degree incidence invariant still bounds slopes, or whether a finite
counterpacket appears.

Secondary target:

```text
W-F1-AA-RES-T3J2:
analyze t=3, j=2, where the bad line has codimension two in F[X]/E.
```

Do not treat the solved `t=2,j=2` calculation as evidence for the full
corrected-reserve conjecture.

## W-F1-AA-RES-LINE-INCIDENCE: Reserve-Indexed Extension Bad-Line Incidence

Status: EXACT_NEW_WALL.

Question:

After Cycles 1-5, in quadratic extensions with `D subset B`, arbitrary anchors reduce to the paired base interpolation-residue readout

```text
S -> (interp_S(w0) mod Ehat, interp_S(w1) mod Ehat).
```

Cycle 4 verifies the source ledger:

```text
a=ceil((1-delta)n), sigma=a-k, balanced t=sigma, hence k+t=a=s_delta.
```

Thus high agreement is automatic on the `a`-subset in the balanced regime. Can one prove a slope-image/bad-locus packing theorem for this paired readout, or produce a finite balanced arbitrary-anchor counterpacket?

Cycle 5 sharpens the live wall:

- Restored `W-F1-AA` is a faithful arbitrary-anchor extension-denominator instance of `Lambda^{NC}_{t,delta}` / `prob:perfiber`.
- Tangent/zero-numerator and quotient-periodic separation are necessary but non-binding.
- The banked `sigma=1` fixed-rate counterpacket survives both and yields `Theta(q_line)` slopes.
- Therefore the missing axis is reserve `eta=sigma/n`, and the first missing invariant is a rigidity/value-count law for the paired readout on the bad line, analogous to `thm:rigidcyclo` / `thm:exactcount` for the monic prefix object.

Cycle 6B sharpens this again:

- The same-slope kernel is not the wall. On `a=k+t` supports,
  equal slopes only says `interp_S(w)-interp_S'(w) in E*F_{<k}[X]`.
- The paired base readout already determines `[interp_S(w)]_E`.
- These facts describe the slope map's kernel/descent, not the number of
  distinct slope values.
- The actual wall is a value-count / collision law for the image of the paired
  readout on the bad line `F*[Bnum]_E`.

Cycle 7 cuts a tempting but false transfer:

- A clean structured Claude answer claimed a `BANKABLE_LEMMA` by transferring
  the `z in B` stratum to a base residue-line datum
  `(Ehat,b_hat,w0+theta*w1)`.
- Source audit rejects that transfer. The CRT class
  `theta in B[X]/Ehat` is generally nonconstant, and multiplication by
  `theta` does not commute with support interpolation:
  `theta * interp_S(w1)` is not generally `interp_S(theta*w1)` modulo `Ehat`.
- Therefore `thm:exactcount` / `thm:rigidcyclo` cannot be imported verbatim
  through the claimed base datum.
- The live object is a twisted readout:

```text
S -> [interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat.
```

Cycle 8 resolves the twist:

- In the separated case `gcd(E,E^tau)=1`, reduction modulo `E` gives a ring
  isomorphism `B[X]/Ehat ~= F[X]/E`.
- Under this isomorphism, the twisted readout is exactly the original extension
  residue `[interp_S(w0)+alpha interp_S(w1)]_E`.
- The non-absorption commutator is real but locator-divisible:
  `theta interp_S(w1)-interp_S(theta w1)=L_S R_S`,
  `deg R_S<=2t-2`.
- Thus the twist is inert for value counting. The hard object is the extension
  residue count itself.

Cycle 9 corrects the count being asked for:

- The raw residue set
  `C1=#{[interp_S(w0)+alpha interp_S(w1)]_E}` is not the source object in
  `def:residue` / `thm:normalform`.
- The source object is the slope set
  `C2=#{z in F : exists S, [interp_S(w)]_E = z[Bnum]_E}`.
- Equivalently, it is a landing/incidence count into the bad line
  `F[Bnum]_E subset F[X]/E`.
- Since `dim_F F[X]/E=t` and `dim_F F[Bnum]_E=1` for nonzero numerator, the
  reserve mechanism is a codimension-`(t-1)` incidence problem. The
  `sigma=1` counterpacket is exactly the codimension-zero endpoint where raw
  residues and slopes coincide.
- The locator-quotient identity
  `W=L_S Q_S+interp_S(w)`, `deg Q_S<=n-a-1`, gives
  `[interp_S(w)]_E=[W]_E-[L_S Q_S]_E`.

Current target:

```text
bound the number of slopes z in F for which some a-subset S satisfies
[interp_S(w0)+alpha interp_S(w1)]_E = z[Bnum]_E.
```

Equivalently:

```text
[L_S Q_S]_E lands in [W]_E - F[Bnum]_E,
where W=interp_D(w), W=L_S Q_S+interp_S(w), deg Q_S<=j-1, j=n-a=r-t.
```

Parameters to keep separate:

- `B=F_p`, generated/entropy field, `q_gen=p`.
- `F=F_{p^2}`, line/extension field, `q_line=p^2`.
- `q_chal` is protocol challenge field only after a protocol theorem.
- `sigma=t=2` is the first finite balanced test case.

Success outputs:

- BANKABLE_LEMMA: prove a source-valid incidence/collision lemma for landings
  of `[L_S Q_S]_E` in the affine bad line `[W]_E-F[Bnum]_E`, even in a
  restricted but meaningful regime.
- COUNTERPACKET: explicit finite or symbolic data showing that the reserve-indexed wall is false above corrected reserve, with field ledgers separated.
- ROUTE_CUT: show `W-F1-AA-RES-LINE-INCIDENCE` is not source-valid and identify
  the false reduction.
- EXACT_NEW_WALL: identify the first missing invariant sharper than the current
  bad-line incidence law.

Non-goals:

- Do not attempt a raw uniform fiber bound over all arbitrary `w0,w1`; low-degree anchors make that statement false.
- Do not reopen the balanced nonzero-numerator support-shrinking noncontainment issue; it is handled by the Cycle 3 lemma.
- Do not reintroduce `W-F1-AA-AGR` as a balanced wall; Cycle 4 cuts it by `a=s_delta`.
- Do not ask another worker to prove only the same-slope kernel
  `E*F_{<k}[X]`; Cycle 6B shows that is a tautological restatement, not a
  value-count theorem.
- Do not absorb the nonconstant CRT multiplier `theta` into the base word as
  `w0+theta*w1` without a theorem; Cycle 7 gives a concrete local check showing
  this commutation fails in general.
- Do not reopen `W-F1-AA-RES-TWISTED-READOUT` as the live wall; Cycle 8 shows
  the twist is isomorphic to the original extension residue count.
- Do not treat the raw residue value count `C1` as the MCA slope count; Cycle 9
  shows the source-relevant count is the bad-line incidence/slope count `C2`.
- Do not use the sub-reserve `sigma=1` counterpacket as a corrected-reserve refutation.
- Do not claim `ass:extension-mca-lift`, a protocol denominator saving, or a line-decoding theorem from the paired-readout reduction alone.

Cycle 11 status update:

- The restricted case `t=sigma=2`, `j=n-a=2` is now BANKABLE_LEMMA / AUDIT.
- The general line-incidence wall remains open.
- The immediate next finite wall is `t=2,j=3`.

Cycle 12 status update:

- The `t=sigma=2`, `j=n-a=3` quotient algebra is now BANKABLE_LEMMA / AUDIT.
- For co-support `T` of size `3`, `Q_S` depends on `e1(T),e2(T)` and not
  `e3(T)`.
- Bad-line landing is a quadric `Delta(e1,e2,e3)=0` with leading coefficient
  `[e3^2]Delta=wedge([W]_E,[Bnum]_E)`.
- Cycle 11's solution-counting mechanism dies at `j=3`; the quadric may have
  `Theta(n^2)` split triples when `D=F_p`, `n=p`.
- The active wall is therefore not the existence of a low-degree incidence
  equation. It is slope-fiber collapse on that quadric:

```text
W-F1-AA-RES-T2J3-FIBER-COLLAPSE.
```

Concrete question:

For fixed slope `z`, the equation `[I_S]_E=z[Bnum]_E` cuts a line `ell_z` in
the elementary-symmetric `(e1,e2,e3)` space. How many `D`-split cubics

```text
X^3-e1 X^2+e2 X-e3
```

can lie on `ell_z`? If the average fiber is `Theta(n)`, then `C2=Theta(n)`;
if the average fiber is `O(1)`, then sub-reserve `C2` can grow like
`Theta(n^2)=Theta(q_line)`.

Codex's first finite scanner observed `max_C2=5` over random `p=7,11,17`
instances, but this is EXPERIMENTAL and not a theorem.

Cycle 12 alternative-lens update:

- The `Delta=0` equation is `F`-valued while
  `(e1,e2,e3) in B^3`.
- In the quadratic field ledger `F=B+alpha B`, this is generally two
  `B`-quadrics

```text
Delta=Delta_0+alpha Delta_1,
Delta_i in B[e1,e2,e3].
```

- Therefore the generic landing locus is a complete-intersection curve of
  size `O(p)`, not a surface of size `Theta(p^2)`.
- A Codex local scanner observed `coeff_component_rank=2` and
  `zeros_all_B3=O(p)` across random `p=7,11,17` cases.

Refined immediate wall:

```text
W-F1-AA-RES-T2J3-BASE-COMPONENT-COMPLETE-INTERSECTION.
```

Prove or refute that `Delta_0` and `Delta_1` have no common surface component
outside classified resonance strata. If true for `D=F_p`, then
`C2<=#landings=O(p)=O(n)` without proving small fixed-slope fibers.

Cycle 13 status update:

- The base-component complete-intersection route is now BANKABLE_LEMMA / AUDIT
  off the resonance strata.
- Banked identity:

```text
Delta = Res(L_T,E) * ( [I_S]_E wedge [Bnum]_E ),
```

with `Res(L_T,E) != 0` on valid co-supports.

- Off

```text
R0 = { [W]_E wedge [Bnum]_E = 0 },
Ra = { Delta in F^* \bar B[e1,e2,e3] },
Rb = { Delta has a \bar B-linear factor },
```

the base quadrics `Delta_0,Delta_1` are coprime, so `#landings=O(p)` and
`C2=O(n)` for `D=F_p`, `t=sigma=2`, `j=3`.

Current exact wall:

```text
W-F1-AA-RES-T2J3-BASE-COMPONENT-RESONANCE.
```

Question: on `Ra` and `Rb`, do many split cubics land with many distinct
slopes, or does the slope map collapse? This is the only remaining place where
the old fixed-slope fiber-collapse wall is still needed in the `D=F_p`,
`t=2,j=3` test regime.

Cycle 14 status update:

- `Ra/Rb` are not source-excluded by the currently banked hypotheses.
- On `Ra/Rb`, the landing locus can be a base surface, so Cycle 13's
  complete-intersection `#landings=O(p)` argument does not apply.
- The remaining obstruction is the slope map on that surface.

Current exact wall:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT.
```

Cycle 15 sharpens the Cycle 14 surface slope-fiber problem. On a resonance
surface `Sigma subset B^3`, with

```text
iota=A0(tau_1,tau_2)-tau_3[W]_E,
mu=B0(tau_1,tau_2)-tau_3 b,
L_z(tau)=iota(tau)-z mu(tau),
```

landing `[I_S]_E=z b` is equivalent to `L_z(tau)=0` in `A=F[X]/E`.
Writing the `B`-linear part of `L_z` as columns

```text
c1(z), c2(z), c3(z) in A ~= B^4,
```

the consistency determinant is

```text
Q(z_0,z_1)=det_{4x4}[c1(z) | c2(z) | c3(z) | c0(z)].
```

Rank alone is not the invariant. For fixed `z`, rank `3` gives an affine
consistency determinant; if `Q!=0`, the slope set is curve-sized `O(p)`, while
rank `3` with `Q==0` identically is the possible `Theta(q_line)` slope regime.

The immediate target is:

- prove `Q!=0` or equivalent curve-sized image control on every source-valid
  `Ra/Rb` resonance stratum; or
- construct source-valid data with `Q==0` identically, enough split-distinct
  co-supports, and `C2=Theta(p^2)=Theta(q_line)`.

The split-cubic condition remains:

```text
X^3-tau_1 X^2+tau_2 X-tau_3
```

must split with distinct roots in `D=F_p`.

Codex local evidence:

- `20260618_cycle15_forced_ra_slope_scan.py` forced the `Ra` coefficient-line
  condition over `p=7` and found only `C2<=6` in 12 smoke seeds. This is
  EXPERIMENTAL / AUDIT evidence only.

Cycle 16 status update:

- Off `R0`, if the determinant consistency polynomial `Q(z_0,z_1)` is not
  identically zero, then `C2<=4p=O(p)=O(n)`.
- Therefore the remaining `t=2,j=3` resonance wall is the `Q==0` branch.
- `Q==0` alone is not a counterpacket because it ignores the distinct
  `D`-split cubic condition.
- The live question is whether the slope map restricted to distinct split
  cubics on the `Q==0` resonance branch realizes `Theta(p^2)=Theta(q_line)`
  slopes or collapses to `O(p)`.

Current target:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT:
on source-valid Ra/Rb resonance data with Q==0 identically, count the image of
the slope map on distinct D-split cubics T subset F_p, |T|=3.
```

## F1 t=2, j=4 Homerun / Single-Prime S4 Certificate Wall

Status: EXACT_NEW_WALL / AUDIT.

Current prompt target:

```text
Cycle 38 homerun full-solve / big-leap attempt
```

Narrow wall inside the prompt:

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

Known source-valid explicit family:

```text
p = 3 mod 4
B = F_p
F = F_{p^2} = B(alpha)
alpha^2 = -1
E = X^2 + alpha X + 1
b = X
D = F_p
q_gen = p
q_line = p^2
q_chal = unused
```

Cycle 37 confirms the hand gates but does not produce a working checker or
finite `S4` certificate. A successful attack may repair the checker, replace
the route with a source-valid obstruction/counterpacket seed, or identify a
more valuable global route.
