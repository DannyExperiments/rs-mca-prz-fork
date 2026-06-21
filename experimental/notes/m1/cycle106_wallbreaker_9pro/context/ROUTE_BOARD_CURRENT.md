# Route Board

Labels are literal: PROOF, COUNTERPACKET, BANKABLE_LEMMA, ROUTE_CUT, EXACT_NEW_WALL.

## Cycle 105 k-Free Uniform Bandwidth Reduction

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL.

Source:

- `current_repo_snapshot/experimental/notes/m1/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md`
- `current_repo_snapshot/experimental/scripts/cycle105_kfree_collapse_check.py`
- `current_repo_snapshot/experimental/notes/m1/cycle105_uniform_bandwidth_divisor_incidence_raw/response.md`

Audit judgment:

- Cycle105 banks the k-free collapse:

```text
theta active
<=> (g_1(theta),...,g_{sigma+1}(theta)) in M_s.
```

- Thus all bandwidths share one fixed rational curve `Gamma`; the `binom(n,k)`
  factor in Cycle104 is a union-bound artifact.
- Cycle105 banks the fixed triangular complement duality `M_s ~= M_{n-s}`.
- Cycle105 cuts generic RS list-size, Johnson-radius, and unconditional
  divided-difference routes: any central-rate proof must consume above-reserve
  aperiodicity.
- Codex locally replayed the k-free collapse and complement duality in small
  finite cases, and the checker passed.

Current exact wall:

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

Prove or kill the aperiodic distinct-support incidence bound
`|Gamma cap M_s| <= n^{O(1)}` with exponent independent of `s` and `k`.

## Cycle 104 Fixed-Bandwidth Divisor Incidence

Status: PROOF / EXACT_NEW_WALL.

Source:

- `current_repo_snapshot/experimental/notes/m1/m1_cycle104_bandwidth_k_divisor_incidence_audit.md`
- `current_repo_snapshot/experimental/scripts/cycle104_fixed_k_divisor_incidence_check.py`
- `current_repo_snapshot/experimental/notes/m1/cycle104_bandwidth_k_divisor_incidence_raw/response.md`

Audit judgment:

- Cycle104 proves:

```text
|Theta_U| <= binom(n,k)(sigma+1)
```

for every fixed `k`, including the first open case `k=2`.
- The proof reverses the co-locator and uses pair collisions for `k=2` and
  divided-difference obstructions for fixed `k`.
- Codex locally replayed the fixed-`k` divisor-incidence predicate in small
  finite cases, and the checker passed.
- This is upper-side prize-relevant structure but not a full upper theorem,
  because the exponent depends on `k`.

Current exact wall:

```text
W-CYCLE105-UNIFORM-BANDWIDTH-DIVISOR-INCIDENCE
```

The next target is a bound with exponent independent of growing `k`, or a
source-valid aperiodic counterpacket.

## Cycle 103 B1 e1-Image Flat-Variety Bound

Status: PROOF / EXACT_NEW_WALL.

Source:

- `current_repo_snapshot/experimental/notes/m1/m1_cycle103_e1_image_flat_variety_audit.md`
- `current_repo_snapshot/experimental/scripts/cycle103_b1_divisor_bound_check.py`
- `current_repo_snapshot/experimental/notes/m1/cycle103_e1_image_flat_variety_raw/response.md`

Audit judgment:

- Cycle103 proves the bandwidth-`1` distinct-root numerator bound:

```text
|Theta_U| = |e_1(V)| <= (n-sigma+1)(sigma+1) = O(n^2).
```

- The proof uses the exact equivalence:

```text
G(theta,X) = [(1-theta X)^(-1) Uhat(X)]_{deg_X <= sigma+1},
theta active <=> G(theta,X) | 1-X^n.
```

- Codex locally replayed the B1 divisor equivalence and finite bound in small
  cases, including the Cycle102 `F_29` instance, and the checker passed.
- This is prize-relevant upper-side structure for the B1 stratum, but it is not
  the full RS-MCA upper theorem and does not merge the finite frontier ledger.

Current exact wall:

```text
W-CYCLE104-BANDWIDTH-K-DIVISOR-INCIDENCE
```

For `k>=2`, prove or kill the affine divisor-family bound:

```text
theta active
<=> exists rho, deg rho <= k-2, such that
    G(theta,X)+X^(sigma+2)rho(X) divides 1-X^n.
```

## Cycle 83 MITM Threshold Plan And Resource Wall

Status: EXACT_NEW_WALL / PLAN.

Source:

- `current_repo_snapshot/experimental/notes/m1/m1_cycle83_mitm_mmax_threshold_audit.md`
- `current_repo_snapshot/experimental/notes/m1/cycle83_mitm_mmax_threshold_raw/response.md`

Audit judgment:

- Cycle 83 ran in a read-only environment and explicitly marked its returned
  census code as `UNRUN`.
- It does not prove `m_max(beta)<=12`.
- It does not produce a 13-fold colored packet.
- It does sharpen the live wall to a color-filtered L/R threshold census:

```text
m(v)=#{ l in L_img :
        v l^{-1} in R_img
        colorL(l)+colorR(v l^{-1}) = 4 mod 16 }.
```

- The target is to prove no value reaches count `13`, or output a packet when
  one does.
- Cycle 83 estimates `|P_0| = 52,747,567,104` compatible products and proposes
  three execution tiers: about `66GB` RAM Bloom duplicate detection, about
  `0.5-0.85TB` deterministic scratch, or slow recompute sharding.
- During banking, local disk was effectively full; Codex removed only no-token
  RS-MCA preview staging directories to preserve raw artifacts and write the
  compact audit.

Current exact wall:

```text
W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION
```

Do not treat Cycle 83 as a proof. The next real progress is a reproducible
threshold census on a suitable execution surface, or an explicit 13-fold packet.

## Cycle 82 Four-Slot Product Injectivity And MITM Wall

Status: PROOF / BANKABLE_LEMMA / PLAN.

Source:

- `current_repo_snapshot/experimental/notes/m1/m1_cycle82_four_slot_or_mitm_mmax_audit.md`
- `current_repo_snapshot/experimental/scripts/cycle82_four_slot_product_checker.py`
- `current_repo_snapshot/experimental/notes/m1/cycle82_four_slot_product_certificate.json`

Audit judgment:

- Cycle 82's Fable answer was read-only and therefore not a proof by itself.
- Codex converted the returned four-slot checker into a local executable
  verifier and ran the full 35-subset certificate.
- The certificate proves:

```text
ALL_4_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 5
```

- Consequently every product fiber in the Cycle 68 finite model has Hamming
  distance at least `5`.
- This is not a proof of `m_max(beta)<=12`. The live wall is now the
  color-filtered L/R MITM threshold census.

Current exact wall:

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

The next target is a reproducible threshold certificate proving no product
value in `P_0` reaches multiplicity `13`, or an explicit 13-fold colored
collision packet.

## Cycle 42 Restricted Good-Reduction / Split-Density Closure And Reserve-Lift Wall

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`

Audit judgment:

- Four external 5.5 Pro answers plus returned checker/certificate artifacts
  agree that Cycle 41's A-side raw affine/Cramer `G2/G3` failure was a false
  negative, not a source-valid obstruction.
- The correct view is that the raw Cycle 41 gate was sufficient for one
  simple affine chart but not necessary for tame/projective good reduction.
- The fixed restricted branch

```text
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
t = sigma = 2,
j = 4
```

  has external-machine certificates for Subcase A at `p=7` and Subcase B at
  `p=19`/`p=31`, with geometric `S_4` witnesses.
- The resulting restricted split-slope density is

```text
N_split(p) = p^2/24 + O(p^(3/2))
           = q_line/24 + O(q_line^(3/4)).
```

- Codex syntax-checked and source-inspected the returned checkers but did not
  locally rerun the SymPy computations because `sympy` is absent and no
  dependency was fetched.
- This is a restricted local closure only. It is not a corrected-reserve,
  fixed-rate, generated-field, MCA/list/line-decoding/curve-MCA, protocol,
  SNARK, prize, or final `COUNTERPACKET` statement.

Current exact wall:

```text
W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT
```

The next target is a homerun/reserve-lift attempt: either lift the closed
fixed quartic mechanism to growing reserve `t=sigma >= C n/log n`,
`j=Theta(n)` with source-valid separated denominator/cosupport data and
positive noncontained split-slope density, or prove a theorem-sized
obstruction showing why the quartic branch cannot scale.

## Cycle 40 Subcase Finite-Place Geometric S4 And Char0Delta Wall

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT /
answered by Cycle 42 and superseded by
`W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT`.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_result.json`

Audit judgment:

- Cycle 40 banks the finite-place histogram criterion:

```text
off-singular factorization types "4" and "13"
  => G_arith = G_geom = S_4
```

- Codex extracted and ran the parametrized checker locally.
- The checker reports `all_pass=true`:

```text
Subcase A, ell=alpha: p=7,23,43,47 pass.
Subcase B, ell=-2X:  p=11,19,31,59 pass.
```

- This closes the Subcase A finite-place gap, but it does not prove
  characteristic-zero good reduction or a growing-prime theorem.
- This is not a `COUNTERPACKET`, corrected-reserve theorem, MCA, CA, list,
  line-decoding, curve-MCA, protocol, SNARK, or prize statement.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA
```

The next target is a homerun/full-solve attempt at the characteristic-zero
branch determinant, quartic discriminant, good-reduction prime, and tame
specialization bridge per subcase.

## Cycle 39 Locator Collapse And Subcase Good-Reduction Wall

Status: PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / answered by
Cycle 40.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify_result.json`

Audit judgment:

- Cycle 39 proves the restricted locator-collapse lemma for the explicit
  `t=2,j=4` family:

```text
ell=[X^p-X]_E = alpha   if (-5/p)=+1,
ell=[X^p-X]_E = -2X     if (-5/p)=-1.
```

- Thus the surface family is fixed within two congruence subcases, rather
  than varying freely with `p`.
- Cycle 38's `p=31` finite-place certificate belongs to Subcase B only.
- Subcase A and good reduction remain unproved.
- This is not a uniform theorem and not a `COUNTERPACKET`.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE
```

The next target is a subcase-separated `S_4` / good-reduction certificate, or
a precise obstruction showing that one subcase cannot globalize.

## Cycle 38 Repaired Finite-Place S4 Certificate And Symbolic Good-Reduction Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT / answered by
Cycle 39.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`

Audit judgment:

- Cycle 38 identifies the exact Cycle 37 checker bug: four top free
  coefficients were residue-pairs where the checker needed `F`-elements.
- The patched data are
  `W_{n-1..n-4}=1,alpha,1+alpha,1`, with `u=[W]_E=1+X` and `kappa=1`.
- Codex ran the patched checker locally at `p=31`; it reports
  `PASS_S4_finite_place=true`, with factorization types `"4"` and `"13"`,
  a nonsquare-discriminant witness, and no singular points on the tested line.
- This is finite-place `EXPERIMENTAL / AUDIT` evidence and a bankable checker
  repair. It is not a uniform theorem and not a `COUNTERPACKET`.

Former exact wall:

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
```

Cycle 39 answers this by proving locator collapse and sharpening the wall to
the subcase good-reduction certificate.

## Cycle 36 Explicit A2_B Family And Single-Prime S4 Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT / answered at
finite-place level by Cycle 38 and superseded by symbolic good reduction.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`

Audit judgment:

- Cycle 36 banks an explicit source-valid denominator family for primes
  `p = 3 mod 4`:

```text
B=F_p, F=F_{p^2}=B(alpha), alpha^2=-1,
E=X^2+alpha X+1, b=X, D=F_p.
```

- For `a in F_p`, `E(a)=(a^2+1)+alpha*a`, so `E` has no `F_p` root.
  Also `E-E^tau=2 alpha X` and `E(0)=1`, so the denominator is separated.
- The remaining free data are finite nonvanishing choices, notably
  `kappa != 0`.
- Uniform geometric S4 is reduced to a finite single-good-prime certificate
  plus good-reduction monotonicity.
- Correction: resolvent irreducibility plus nonsquare discriminant is not
  enough by itself. The certificate must also prove quartic
  transitivity/geometric irreducibility, for example by a finite-place
  factorization type `"4"`.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

For the explicit family, produce or specify a reproducible good-prime
certificate checking determinant/top-symbol gates, quartic transitivity,
resolvent irreducibility, and discriminant nonsquareness. Success would still
be only a restricted local `Theta(q_line)` counterpacket seed, not a
corrected-reserve, MCA, line-decoding, protocol, SNARK, or prize theorem.

## Cycle 35 A2_B Finite-Place S4 Certificate And Uniform-S4 Wall

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT /
answered by Cycle 36 and superseded by the single-prime certificate wall.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`

Audit judgment:

- Cycle 35 banks a finite-place monodromy certificate for a fixed
  source-valid restricted `t=2,j=4` `A^2_B` instance.
- If the off-`Delta` squarefree specializations of `L_tau` over `F_p` contain
  factorization types `"4"` and `"13"`, then arithmetic monodromy is `S_4`.
- Since `"13"` is an even degree-one Frobenius type, the sign constant-field
  obstruction is absent in that certified instance; hence
  `G_geom=G_arith=S_4`.
- The Cycle 32 `p=29` histogram contains `"4"`, `"13"`, and `"1111"`, so it is
  strong `EXPERIMENTAL / AUDIT` evidence for one tested instance.
- This is not a uniform-in-`p` theorem and not yet a `COUNTERPACKET`.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-UNIFORM-S4
```

Construct an explicit source-valid growing-prime family and prove geometric
`S_4` plus arithmetic/geometric equality uniformly, or find the exact
constant-field/resolvent/source-validity obstruction. A genuine uniform proof
would give a restricted local `Theta(q_line)` counterpacket seed; it would
still not be corrected-reserve, MCA, line-decoding, protocol, SNARK, or prize
status.

## Cycle 34 A2_B Dominance And Geometric-S4 Wall

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / superseded by
Cycle 35 finite-place certificate.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`

Audit judgment:

- Cycle 34 banks the restricted dominance lemma for the off-curve
  `t=2,j=4` `A^2_B` family.
- On the source-valid dense open, the rational map
  `psi:z |-> tau(z)=M(z)^(-1)(-C_0(z))` has generic `B`-Jacobian rank two.
- The map is birational onto the Cycle 30 quadric image, via the rational
  inverse coordinate recovered from
  `(u-zb)lambda(tau)-ell[Q_S(tau)]_E=0`.
- Therefore the rank-one / hidden curve-collapse route for `O(p)` off-curve
  counts is cut.
- This does not prove any positive split density, geometric `S_4`,
  arithmetic/geometric equality, or `Theta(q_line)` counterpacket.

Former exact wall:

```text
W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4
```

Cycle 35 gives a finite-place certificate for tested instances and moves the
live target to uniform `S_4` / growing-prime construction.

## Cycle 33 A2_B Singular Bound And Dominance-Resolvent Wall

Status: BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL / AUDIT / superseded
by Cycle 34 dominance audit.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`

Audit judgment:

- Cycle 33 banks the singular determinant curve bound in the restricted
  `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=4` branch.
- Under the Cycle 29 top-symbol nonzero hypotheses,
  `Delta(z_0,z_1)=det_B M(z)` has total degree at most four and is not
  identically zero.
- Therefore the singular determinant locus contributes at most `4p=O(p)`
  split slopes.
- This does not prove any off-curve split density, `S_4`, arithmetic/geometric
  monodromy equality, or `Theta(q_line)` counterpacket.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT
```

Decide generic `B`-Jacobian rank of `tau(z_0,z_1)=M(z)^(-1)(-C_0(z))`,
then compute/source-audit the quartic resolvent/discriminant and constant-field
test for the off-curve `A^2_B` family.

## Cycle 32 A2_B Monodromy Certificate Wall

Status: ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT / superseded by
Cycle 33 singular-bound audit.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`

Audit judgment:

- Cycle 32 cuts the one-variable `B(z)` / `F(z)` framing.
- The correct model is a two-dimensional `B`-surface over `A^2_B`, with
  `z=z_0+alpha z_1`, `z_0,z_1 in B=F_p`.
- The local Cramer-system checker matches direct support enumeration away from
  the determinant curve `Delta=det_B M(z)=0`; boundary discrepancies are
  recorded as `singular_split_C2`.
- This is not a proof of `S_4`, not a proof of positive density, and not a
  `Theta(q_line)` counterpacket.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE
```

Decide whether `Delta=0` contributes only `O(p)` split slopes and whether the
off-curve surface family has arithmetic/geometric monodromy with a positive
identity Frobenius class.

## Cycle 31 T2J4 Quartic Monodromy Wall

Status: EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle31_t2_j4_scaling_spotcheck_certificate.md`

Audit judgment:

- Cycle 31 argues that the `t=2,j=4` split locus is governed by quartic
  monodromy rather than hidden rational-root collapse.
- Do not bank its strongest claim that `O(p)` collapse is impossible.
- Do not bank a `Theta(q_line)` counterpacket.
- The bankable progress is the exact next invariant: compute the discriminant,
  resolvent, and geometric monodromy of
  `L_{tau(z)}=X^4-tau_1(z)X^3+tau_2(z)X^2-tau_3(z)X+tau_4(z)`.

Local spot-check:

```text
p=31 avg over 2 seeds: C2=28.00, C2/p=0.903, C2/p^2=0.0291
p=37 one seed:        C2=39,    C2/p=1.054, C2/p^2=0.0285
```

Interpretation:

- The earlier phrase "leans O(p)" is too strong.
- Cycle 31's proposed `1/24` density is also not established.
- Further random scans are lower value than the exact monodromy/resolvent
  computation.

Current exact wall:

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```

Decide the correct base-field model for `z in F_{p^2}` and splitting over
`B=F_p`, then certify or refute the monodromy/positive-density route.

## Cycle 30 T2J4 Split-Quadric Gate Reduction

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md`

Banked narrow reduction:

- In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `q_line=p^2`,
  `q_gen=p`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated window,
  the distinct split-quartic gate can be written in co-support coordinates
  `tau=e(T)` as one `F`-quadric, equivalently two `B`-quadrics:

```text
Phi(tau)=iota wedge_F mu = 0,
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

- Since `Q_S` is independent of `tau_4` and `lambda=lambda'+tau_4`,
  Cycle 30 gives the quadratic form

```text
Phi = kappa*tau_4^2
    + tau_4*(kappa*Tr_{A/F}(lambda') - (ell[Q_S]_E) wedge_F b)
    + (kappa*N_{A/F}(lambda') - (ell[Q_S]_E) wedge_F (b lambda')).
```

Codex local experimental scan:

```text
p=17 avg_C2/p=0.482, avg_C2/p^2=0.0284
p=19 avg_C2/p=0.618, avg_C2/p^2=0.0325
p=23 avg_C2/p=0.739, avg_C2/p^2=0.0321
p=29 avg_C2/p=1.078, avg_C2/p^2=0.0372
```

Interpretation:

- The two-quadric reduction alone does not prove `O(p)` and does not give a
  `Theta(q_line)` counterpacket.
- The finite scan leans toward a hidden `O(p)`-scale split-locus collapse,
  contrary to the naive positive-density `p^2` heuristic.

Current exact wall:

- `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE`: decide whether the split gate has
  a hidden rational-root, discriminant, trace/norm, or Frobenius collapse
  forcing `O(p)`, or construct a source-valid growing-prime family with
  `Theta(q_line)` slopes.

## Cycle 29 T2J4 Locator Top-Symbol Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`

Banked narrow lemma:

- In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=4`,
  off-`R0`, source-valid separated window, the quotient has the closed form

```text
Q_S = W_{n-1} X^3
    + (W_{n-2} - W_{n-1} tau_1) X^2
    + (W_{n-3} - W_{n-2} tau_1 + W_{n-1} tau_2) X
    + (W_{n-4} - W_{n-3} tau_1 + W_{n-2} tau_2 - W_{n-1} tau_3).
```

- The locator residue introduces `tau_4`, giving a square affine system

```text
M(z)tau=-C_0(z),     M(z)=[C_1(z)|C_2(z)|C_3(z)|C_4(z)]
```

  in the four-dimensional `B`-space `A=F[X]/E`.
- Hence the determinant at `j=4` is an invertibility/uniqueness determinant,
  not the Cycle 28 incidence obstruction. Generic slopes have a unique affine
  preimage `tau(z)=M(z)^(-1)(-C_0(z))`.
- The top symbol persists:

```text
TopSym(det_B M(z)) = -N(kappa) * N(z)^2 * Q_4,
```

  with the same source-valid nonzero Cycle 28 locator quantity

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

Route correction:

- This does not prove `C2=O(p)` for `j=4`. Once `M(z)` is invertible, affine
  consistency is automatic. The slope bound must come from the actual split
  quartic gate.

Current exact wall:

- `W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE`: bound or refute the number of slopes
  for which the rational preimage `tau(z)` is the elementary-symmetric tuple
  of a distinct 4-subset of `F_p`.

## Cycle 28 Restricted T2J3 Q4 Proof

Status: PROOF / ROUTE_CUT / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md`

Restricted theorem:

- In the `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0`,
  `c_b!=0`, source-valid separated window, the determinant consistency
  polynomial `Q(z_0,z_1)` is not identically zero.
- Therefore Cycle 16 gives

```text
C2 <= #{z in F : Q(z)=0} <= 4p = O(p).
```

- The distinct split-cubic gate only shrinks the realized slope set.

Proof mechanism:

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

For `c notin B`,

```text
Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)),
```

so vanishing is equivalent to an `F_p` root of `E`, excluded by source-validity.
For `c in B`, `Q_4=N(c_b)*Im(d)^2`, nonzero by separatedness.

Route cut:

- Do not keep searching for source-valid `Theta(q_line)` counterpackets in the
  restricted `t=2,j=3` branch. It is closed as a local residue-line incidence
  theorem.

Superseded exact wall:

- `W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL`: test whether the top-symbol
  mechanism persists at `t=2,j=4`, ideally as a nonzero scalar times a power
  of `prod_{a in F_p}E(a)`.

## Cycle 27 Q4 Locator-Norm Obstruction

Status: ROUTE_CUT / superseded by Cycle 28 restricted proof.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE27_Q4_SPLIT_GATE_AUDIT.md`

Banked narrow lemma:

- In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
  off-`R0`, source-valid separated window, Cycle 27 identifies the candidate
  degree-4 coefficient

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

- The apparent `P`-dependence in the Cycle 26 expression cancels because the
  `P`-part of `q2` is collinear with the rank-one direction of `q1`.
- For `c notin B`,

```text
Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

  Hence `Q_4=0` iff `E` has an `F_p` root iff
  `prod_{a in F_p}E(a)=0`, the same locator norm cut in Cycle 24.
- For `c in B`, `Q_4=N(c_b)*Im(d)^2`; separatedness excludes `d in B`.

Consequence:

- Subject to an independent source audit of the Cycle 15/16/20/25 column
  conventions, `Q_4!=0` is source-validly forced, so `Q` is not identically
  zero and Cycle 16 gives `O(p)` affine-consistent slopes. The distinct
  split-cubic gate can only shrink that set.

Superseded wall:

- `W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT`: independently rederive the `Q_4`
  formula and source-valid nonvanishing. If confirmed, promote the restricted
  `t=2,j=3` branch to a local proof; if not, isolate the exact flaw or
  counterpacket.

## Cycle 26 Q-Zero Rank Dichotomy

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md`

Banked narrow lemma:

- Let `C(z)=[c_1(z)|c_2(z)|c_3(z)] in Mat_{4 x 3}(B)`.
- If some `3 x 3` minor of `C(z)` is not identically zero (NONDEP), then
  the rank-drop locus `rank_B C(z)<=2` has size `O(p)`.
- Away from that rank-drop locus, `rank_B C(z)=3`, so `Q(z)=0` is necessary
  and sufficient for the affine consistency condition
  `c_0(z) in span_B(c_1(z),c_2(z),c_3(z))`.
- Therefore in NONDEP, `Q` not identically zero gives `O(p)` affine-consistent
  slopes.
- In the `c notin B`, `c_b != 0` branch, the leading symbols of columns `1`
  and `2` are `-c_b c` and `-c_b`, which are `B`-independent. Hence that
  branch is NONDEP.

Audit correction:

- The proposed top-degree `Q_4` obstruction is not yet banked as proved.
  It must be verified from the Cycle 15/16 column definitions before use.
- Affine consistency in `tau in B^3` is not yet actual line-incidence:
  distinct `D`-split cubics must still be retained.

Current exact wall:

- `W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE`: verify or refute the proposed
  `Q_4` formula; if correct, prove or refute source-valid `Q_4 != 0`; then
  carry the distinct split-cubic gate separately.

## Cycle 25 Q-Zero Rank-Consistency Correction

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`

Banked narrow lemma:

- In the Cycle 15/16 determinant setup, if
  `c_i(z)=s_i(z)u+t_i(z)b`, then

```text
Q = <s_1,s_2><t_3,t_0> - <s_1,s_3><t_2,t_0>
  + <s_1,s_0><t_2,t_3> + <s_2,s_3><t_1,t_0>
  - <s_2,s_0><t_1,t_3> + <s_3,s_0><t_1,t_2>.
```

- `det M=(c_b/kappa^2)D` is a `z`-free source invariant and does not by
  itself decide whether the slope-fiber determinant `Q(z)` vanishes.

Audit correction:

- `Q(z)=0` is necessary for a realized slope, but not sufficient unless
  `rank[c_1(z)|c_2(z)|c_3(z)]=3`.
- On rank-drop strata, the augmented rank conditions for
  `[c_1(z)|c_2(z)|c_3(z)|c_0(z)]` are required.
- Therefore do not bank the recovered answer's claim that `Q==0` identically
  gives all `p^2` slopes.

Current exact wall:

- `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`: decide the rank-stratified
  consistency locus on the source-valid `Q==0`, `D!=0`, `det M!=0` branch.

## Cycle 24 D-Kernel Norm Factorization

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`

Banked narrow lemma:

- In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
  off-`R0` window,
  `ell=[X^p-X]_E=mu*(xi+c/2)+delta_c`, with
  `mu=(c^2/4-d)^((p-1)/2)-1` and `delta_c=(c-c^p)/2`.
- With
  `D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)`, the gate factors as
  `D=N(ell)kappa`.
- The norm is the resultant
  `N(ell)=prod_{a in F_p}E(a)`.

Route cut:

- Source-valid residue-line denominators are nonzero on `D=F_p`, so
  `N(ell)!=0`.
- Off `R0`, `kappa!=0`.
- Therefore the whole source-valid `D=0`, off-`R0` branch is empty in this
  restricted `t=2,j=3` calculation. This cuts the nonsplit-`c` wall and
  subsumes Cycle 23.

Current exact wall:

- Superseded by Cycle 25: the determinant-only wall is sharpened to
  `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`.

## Cycle 23 c-in-B D-Kernel Emptiness

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE23_CINB_DKERNEL_EMPTINESS_AUDIT.md`

Banked narrow lemma:

- In the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`,
  off-`R0` window, if `c in B` and `d notin B`, then
  `ell=[X^p-X]_E=mu*(xi+c/2)`.
- With
  `D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)`, the gate factors as
  `D=-mu^2(c^2/4-d)kappa`.
- Since `d notin B` and `kappa != 0`, this forces `D != 0`.

Route cut:

- The explicit `c in B`, `d notin B`, `Delta1==0`, `D=0`, off-kernel
  stratum from Cycle 22 is empty. It cannot supply a `Theta(q_line)`
  counterpacket.

Current exact wall:

- Superseded by Cycle 24: the complementary nonsplit-`c` lane is also empty
  for source-valid denominators, because `D=N(ell)kappa` and
  `N(ell)=prod_{a in F_p}E(a)`.

## Cycle 22 D-Kernel Decoupling

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`

Banked narrow lemma:

- `Delta1==0` is equivalent to the two base-descent equations
  `Im_alpha(p1+q2)=0` and `Im_alpha(detP)=0`.
- On `D=0`, leading-data alignment reduces to the scalar gate `J_A=0`.
- On `Delta1==0`,
  `Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2`.
- Therefore on any source-valid point with `c in B`, `d notin B`,
  `Delta1==0`, and `D=0`, alignment is impossible in odd characteristic.

Rejected overclaim:

- Do not claim a counterpacket or non-collapse family without proving
  nonemptiness and a growing split-cubic slope lower bound.

Current exact wall:

- Superseded by Cycle 23: the `c in B`, `d notin B` nonemptiness wall is empty.
  Continue at `W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C`.

## Cycle 21 D-Kernel Alignment Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`

Banked narrow lemma:

- On the restricted `D=F_p`, `t=sigma=2`, `j=3`, off-`R0` branch, simultaneous
  slope-branch collapse on `Delta1==0` is equivalent, away from discriminant
  ramification, to two scalar gates `J_A=J_Aprime=0`.
- These gates are linear in
  `(m,w_1)=(W_{n-2}+cW_{n-1}, W_{n-1})`.
- Their resultant is the Cycle 20 gate
  `D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)`.

Rejected overclaim:

- Do not claim the base-descent equations fail to force collapse unless an
  elimination proof or source-valid off-kernel family is supplied.

Current exact wall:

- `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`: on `Delta1==0`, `D==0`, and the two
  base-descent equations, decide whether the leading-data ratio is forced onto
  the collapse-kernel line.

## F1 Extension-Line MCA Lift

Status: ROUTE_CUT / COUNTERPACKET for unrestricted same-numerator lift.

Source targets:

- `upstream_main_20260618/tex/snarks_v4.tex`, label `ass:extension-mca-lift`
- `upstream_main_20260618/tex/proximity_blueprint_v3.tex`, label `prob:F1`
- `upstream_main_20260618/tex/slackMCA_v3.tex`, labels `def:residue`, `thm:normalform`
- `upstream_main_20260618/experimental/pr-triage-2026-06-17.md`

Banked facts:

- Same-numerator lift is false for arbitrary extension-valued lines.
- Verified finite witnesses exist over `F_7 -> F_49` and `F_17 -> F_17^2`.
- Fixed-rate `sigma=1` asymptotic counterexample is banked: `E=X-alpha`, `alpha notin B`, bad-slope density stays positive over `q_line=|F|`.
- Unbalanced degree `t < sigma` residue-line data reduce to a residual list object with slack `sigma-t`.
- Balanced monic-anchor data admit a bankable algebraic reduction: equal slopes imply `hat E | (L_S-L_S')`, where `hat E=lcm(E,E^tau) in B[X]` and `deg(hat E)<=2sigma`.

Current exact wall:

- Cycle 1 reduced arbitrary anchors in the quadratic case to the paired base interpolation-residue readout
  `S -> (interp_S(w0) mod Ehat, interp_S(w1) mod Ehat)`.
- This kills the immediate extension-only invariant, but the packing endpoint remains open.
- The proposed raw generalized per-fiber endpoint is unsafe as stated for arbitrary low-degree/codeword anchors.
- Need a corrected slope-image/bad-locus packing theorem or a finite base-field arbitrary-anchor packing counterpacket.

## L1 Locator Fiber

Status: ROUTE_CUT for the raw arbitrary `Fib_U(s)` formulation; open for repaired objects.

Banked fact:

- If `U` is itself a codeword, every `s`-subset can be feasible while the actual list size is 1, so the raw support fiber overcounts.

Live route:

- Repair with exact-agreement, maximal-support, or codeword-indexed canonical support fibers.

## A0 Crites-Stewart / Paper D Import

Status: AUDIT / CONDITIONAL.

Banked fact:

- No internal arithmetic failure found in Paper D's universal cap calculation.
- Primary Crites-Stewart / ABF theorem import still not verified.

## Cycle 1 Fable Loop

Status: BANKABLE_LEMMA / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE1_F1_ARBITRARY_ANCHOR_AUDIT.md`

Banked narrow lemma:

- In quadratic extensions with `D subset B`, balanced arbitrary anchors split into base components and factor through `(B[X]/Ehat)^2`.

Rejected overclaim:

- Do not cite the raw answer as a full F1 proof.
- Do not cite the raw generalized per-fiber endpoint without repair.

## Cycle 2 Paired Base Readout Retry

Status: BANKABLE_LEMMA / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_PAIRED_BASE_READOUT_AUDIT.md`

Banked narrow lemma:

- For quadratic `B=F_p`, `F=F_{p^2}`, `D subset B`, balanced `t=sigma`, arbitrary anchors factor through
  `rho(S)=(interp_S(w0) mod Ehat, interp_S(w1) mod Ehat)` with `Ehat=lcm(E,E^tau) in B[X]`.
- The scalar slope `z` is unique whenever `[Bnum]_E` is nonzero, even if `[Bnum]_E` is a zero divisor.
- Shrinking a support to an `a=k+t` subset preserves the forced interpolant and residue equation, but not necessarily noncontainment.

Current exact wall:

- `W-F1-AA`: bound the slope image / distinct bad-locus readout classes for the paired base interpolation-residue object after tangent/contained and quotient-periodic cases are separated.
- Do not replace this by a raw uniform fiber bound over arbitrary `w0,w1`; codeword anchors make raw fibers huge while contributing at most one slope.

## Cycle 3 Noncontainment Audit

Status: BANKABLE_LEMMA / ROUTE_CUT for the proposed high-agreement wall.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_NONCONTAINMENT_SUBSET_LEMMA.md`

Banked narrow lemma:

- In a nonzero-numerator residue-line datum, every support of size at least `a=k+t` is automatically noncontained. No degree-`<k` polynomial can agree with `-Bnum/E` on `a` points, since `E G+Bnum` would have degree `<a` and too many roots.
- Thus shrinking a genuine balanced support to an `a`-subset does not lose noncontainment, provided `Bnum != 0`.

Current exact wall:

- Cycle 4 cuts `W-F1-AA-AGR` as a balanced-case wall. In the source ledger, `a=ceil((1-delta)n)` and `sigma=a-k`; balanced `t=sigma` gives `k+t=a=s_delta`.
- The live wall is restored to `W-F1-AA`: pure balanced slope-image / bad-locus packing for the paired base readout on `a=s_delta` subsets.

## Cycle 4 Balance-Notation Audit

Status: ROUTE_CUT / BANKABLE_LEMMA.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE4_BALANCE_NOTATION_ROUTE_CUT_AUDIT.md`

Banked correction:

- Keep the noncontainment lemma from Cycle 3.
- Cut the high-agreement wall `W-F1-AA-AGR` in the balanced regime, because `nu(S)>=s_delta` is automatic for `|S|=a=s_delta`.

Current exact wall:

- Cycle 5 sharpens `W-F1-AA` to `W-F1-AA-RES`: the reserve-indexed paired-readout rigidity/value-count wall.
- The tangent/zero-numerator and quotient-periodic separations are necessary but non-binding; the banked `sigma=1` fixed-rate counterpacket survives both with `Theta(q_line)` slopes.
- The missing invariant is a rigidity/value-count law for `rho(S)=(interp_S(w0) mod Ehat, interp_S(w1) mod Ehat)` on the bad line, plus the reserve threshold `eta=sigma/n` at which the count changes from `Theta(q_line)` sub-reserve to conjectural `n^{1+o(1)}` above corrected reserve.

## Cycle 5 Reserve-Indexed Wall Audit

Status: EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE5_W_F1_AA_RES_EXACT_WALL_AUDIT.md`

Banked conservative content:

- Restored `W-F1-AA` is a faithful arbitrary-anchor extension-denominator instance of `Lambda^{NC}_{t,delta}` / `prob:perfiber`.
- The two named separations in restored `W-F1-AA` do not bind: the `sigma=1` fixed-rate counterpacket has `Bnum=1`, `E=X-alpha`, is aperiodic, and still yields `Theta(q_line)` slopes.
- Balanced `t=sigma` hides the reserve parameter `eta=sigma/n`; fixed `sigma` is sub-reserve.

Current exact wall:

- `W-F1-AA-RES`: prove or refute the paired-readout rigidity/value-count law and reserve threshold for arbitrary anchors after field ledgers are separated.

## Cycle 7 Twisted Readout Audit

Status: ROUTE_CUT / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE7_W_F1_AA_RES_VALUECOUNT_TWISTED_READOUT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle7_theta_multiplier_check.py`

Cut:

- Cycle 7's claimed `BANKABLE_LEMMA` is rejected as stated.
- The CRT class `theta in B[X]/Ehat` is generally nonconstant.
- Therefore the quotient readout
  `[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat`
  is not, in general, the ordinary interpolation residue of the pointwise word
  `w0 + theta*w1`.
- Do not import `thm:exactcount` or `thm:rigidcyclo` to the `z in B` stratum by
  pretending this is an ordinary base residue-line datum.

Banked conservative content:

- Part A of the recovered answer is source-valid but mostly already present in
  the paired-readout bank: the slope is a function of the paired base readout,
  hence `#slopes <= #paired-readout-values`.
- The new useful information is the transfer boundary: a new theorem is needed
  for the nonconstant-multiplier/twisted readout.

Current exact wall:

- `W-F1-AA-RES-TWISTED-READOUT`: prove or refute a value-count/collision law for
  `[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat` with nonconstant
  `theta in B[X]/Ehat`, after reserve, tangent, and quotient-periodic
  separations.

## Cycle 8 Twisted Readout Isomorphism

Status: BANKABLE_LEMMA / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE8_W_F1_AA_RES_TWISTED_READOUT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle8_twisted_readout_verify.py`

Banked lemma:

- In the separated quadratic case, reduction modulo `E` gives a ring
  isomorphism `B[X]/Ehat ~= F[X]/E`.
- The twisted readout maps exactly to the original extension residue:

```text
[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat
  <-> [interp_S(w0)+alpha interp_S(w1)]_E.
```

- The Cycle 7 non-absorption failure is explained by
  `theta interp_S(w1)-interp_S(theta w1)=L_S R_S`, `deg R_S<=2t-2`.

Current exact wall:

- `W-F1-AA-RES-RESIDUE-COUNT`: prove or refute the reserve-indexed value count
  for `[interp_S(w0)+alpha interp_S(w1)]_E in F[X]/E` for arbitrary base
  anchors and aperiodic separated `E`. No `q_gen` collapse is known.

## Cycle 9 Locator-Quotient Line-Incidence Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE9_W_F1_AA_RES_RESIDUE_COUNT_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle9_locator_quotient_incidence_check.py`

Banked lemma:

- For `W=interp_D(w)`, `L_S=prod_{d in S}(X-d)`, `|S|=a=k+t`, and
  `I_S=interp_S(w)`, Euclidean division gives:

```text
W = L_S Q_S + I_S,
deg Q_S <= n-a-1 = j-1, where j=n-a=r-t.
```

- Hence:

```text
[I_S]_E = [W]_E - [L_S Q_S]_E in F[X]/E.
```

- The source-relevant object in `def:residue` / `thm:normalform` is not the raw
  residue count `#{[I_S]_E}`. It is the slope/bad-line incidence count:

```text
#{ z in F : exists S with [I_S]_E = z[Bnum]_E }.
```

- Since `dim_F F[X]/E=t` and `dim_F F[Bnum]_E=1`, this is an incidence problem
  into a codimension-`(t-1)` line. The `sigma=1` counterpacket is the
  codimension-zero endpoint where raw residues and slopes coincide.

Current exact wall:

- `W-F1-AA-RES-LINE-INCIDENCE`: prove or refute the reserve-indexed incidence
  bound for `[L_S Q_S]_E` landing in `[W]_E-F[Bnum]_E`, under balanced
  `t=sigma`, separated aperiodic `E`, arbitrary base anchors, and separated
  field ledgers.

## Cycle 10 Manual Route-Cut Reinforcement

Status: ROUTE_CUT / EXACT_NEW_WALL.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE10_MANUAL_RESIDUE_COUNT_ROUTE_CUT_AUDIT.md`

Banked alignment:

- Cycle 10 independently cuts raw residue cardinality as the wrong source
  object and restores the online slope count:

```text
#{ z in F : exists noncontained a-subset S with
   [interp_S(w0)+alpha interp_S(w1)]_E = z[Bnum]_E }.
```

- Its proposed name `W-F1-AA-RES-ONLINE-SLOPE-COUNT` is the same live wall as
  Cycle 9's `W-F1-AA-RES-LINE-INCIDENCE`, with noncontainment and aperiodicity
  made explicit.

Current exact wall:

- `W-F1-AA-RES-LINE-INCIDENCE / ONLINE-SLOPE-COUNT`.

## Cycle 11 t=2, j=2 Line-Incidence Audit

Status: BANKABLE_LEMMA / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE11_T2_J2_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle11_t2_j2_line_incidence_verify.py`

Banked lemma:

- In the first finite balanced incidence regime
  `t=sigma=2`, `j=n-a=r-t=2`, `a=n-2`, `k=n-4`, the locator quotient is rigid:

```text
Q_S = C(X-s_T)+C1.
```

- The bad-line landing condition is one conic:

```text
det(s_T,p_T)=0,
det(s,p)=wedge([W]_E[L_T]_E-[L_D]_E[Q_S]_E, [Bnum]_E[L_T]_E).
```

- The `p^2` coefficient of `det` is
  `wedge([W]_E,[Bnum]_E)`, so `det identically zero` forces the
  global/tangent endpoint.
- If `det` is not identically zero, `C2=O(n)`, conservatively `C2<=6n`;
  generically `C2<=4`.
- For `D=F_p`, `p>=7`, and `deg W=n-1`, the repeated-sum argument excludes the
  identically-zero resonance.

Local check:

- `20260618_cycle11_t2_j2_line_incidence_verify.py` passed over sampled
  `F_7`, `F_11`, and `F_17` quadratic extensions with `max_C2=2`.

Current exact wall:

- `W-F1-AA-RES-T2J3`: extend or refute the incidence law for `t=2,j=3`.
- Secondary wall: `W-F1-AA-RES-T3J2`.

Do not bank:

- any proof of `conj:B`;
- any extension to `j>=3` or `t>=3`;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 12 t=2, j=3 Line-Incidence Audit

Status: EXACT_NEW_WALL / BANKABLE_LEMMA / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE12_T2_J3_LINE_INCIDENCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle12_t2_j3_line_incidence_scan.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle12_t2_j3_codex_local_note.md`

Harness note:

- The original terminal scrape for Cycle 12 was visibly malformed. The clean
  structured Claude JSONL answer was recovered and promoted to `response.md`;
  the bad scrape is preserved separately.

Banked structural lemma:

- In the next finite balanced incidence regime
  `t=sigma=2`, `j=n-a=r-t=3`, `a=n-3`, `k=n-5`, the locator quotient has the
  closed form

```text
Q_S =
  W_{n-1} X^2
  + (W_{n-2}+W_{n-1}E_1) X
  + (W_{n-3}+W_{n-2}E_1+W_{n-1}(E_1^2-E_2))
  - tau_1 (W_{n-1}X+W_{n-2}+W_{n-1}E_1)
  + tau_2 W_{n-1},
```

where `tau_i=e_i(T)` and `E_i=e_i(D)`.

- For `D=F_p`, this becomes

```text
Q_S=W_{n-1}(X^2-tau_1 X+tau_2)+W_{n-2}(X-tau_1)+W_{n-3}.
```

- Thus `Q_S` depends on `e1(T),e2(T)` but not `e3(T)`.
- Bad-line landing is a quadric condition

```text
Delta(T)=( [W]_E [L_T]_E - [L_D]_E [Q_S]_E )
          wedge ( [Bnum]_E [L_T]_E ) = 0
```

in `(e1,e2,e3)`, with `[e3^2]Delta=wedge([W]_E,[Bnum]_E)`.

Current exact wall:

- `W-F1-AA-RES-T2J3-FIBER-COLLAPSE`: prove or refute slope-fiber collapse on
  the `t=2,j=3` quadric. Cycle 11's conic solution-counting mechanism is now
  vacuous because a quadric in three co-support variables can have
  `Theta(n^2)` split triples when `D=F_p`, `n=p`.
- Codex's random scanner over `p=7,11,17` found no easy counterpacket and
  observed `max_C2=5`, but this is EXPERIMENTAL only.

Refined attack lens:

- Since `Delta` is `F`-valued and `(tau_1,tau_2,tau_3) in B^3`, write
  `Delta=Delta_0+alpha Delta_1` with `Delta_i in B[tau_1,tau_2,tau_3]`.
- Generic landing is therefore two base-field quadratic equations, not one.
- A Codex local scanner
  `20260618_cycle12_base_component_rank_scan.py` observed
  `coeff_component_rank=2` and `zeros_all_B3=O(p)` across random
  `p=7,11,17` cases.
- New immediate wall:

```text
W-F1-AA-RES-T2J3-BASE-COMPONENT-COMPLETE-INTERSECTION.
```

- If `Delta_0` and `Delta_1` have no common surface component outside
  classified resonance strata, then `#landings=O(p)` for `D=F_p`, hence
  `C2=O(n)` without a fixed-slope fiber-collapse theorem.

Do not bank:

- any `C2` upper/lower bound for `t=2,j=3`;
- any proof of `conj:B`;
- any counterpacket to the corrected-reserve conjecture;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 13 Base-Component Complete-Intersection Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE13_BASE_COMPONENT_COMPLETE_INTERSECTION_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle12_base_component_rank_scan.py`

Harness note:

- The original terminal scrape for Cycle 13 was visibly malformed and was
  classified `HARNESS_MALFORMED_VISIBLE_TERMINAL`.
- The clean structured Claude JSONL recovery was present, promoted to
  `response.md`, and is the audited math artifact.

Banked lemma:

- In the `D=F_p`, `t=sigma=2`, `j=3` regime, the landing determinant satisfies

```text
Delta = Res(L_T,E) * ( [I_S]_E wedge [Bnum]_E ),
```

with `Res(L_T,E) != 0` for every valid co-support. Therefore `Delta=0`
faithfully detects landings and has no forced resultant common component.

- Splitting `Delta=Delta_0+alpha Delta_1` over `F=B+alpha B` gives two
  base-field quadrics in `(tau_1,tau_2,tau_3)`.
- Off the resonance strata

```text
R0 = { [W]_E wedge [Bnum]_E = 0 },
Ra = { Delta in F^* \bar B[tau] },
Rb = { Delta has a \bar B-linear factor },
```

the base quadrics have no common surface component. Thus their common zero set
in `B^3` is curve-sized, and

```text
C2 <= #landings = O(p)=O(n)
```

for `D=F_p`, `t=sigma=2`, `j=3`, off `R0 union Ra union Rb`.

Current exact wall:

```text
W-F1-AA-RES-T2J3-BASE-COMPONENT-RESONANCE.
```

On `Ra` and `Rb`, determine whether many `D`-split cubics land with many
distinct slopes, or whether the slope map collapses. This resonance wall is
where the older fixed-slope fiber-collapse analysis is still required.

Do not bank:

- an unconditional `t=2,j=3` bound;
- a proof of `conj:B`;
- any counterpacket;
- any result above corrected reserve;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 14 Base-Component Resonance Audit

Status: EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`

Harness note:

- Cycle 14 completed cleanly with `answerSource=claude_structured_jsonl` and
  `classification=EXACT_NEW_WALL`.

Banked reduction:

- On `Ra/Rb`, the source hypotheses do not exclude resonance.
- The landing locus can be a base surface, so the Cycle 13
  complete-intersection count does not apply there.
- Off `R0`, write

```text
iota=A0(tau_1,tau_2)-tau_3[W]_E,
mu=B0(tau_1,tau_2)-tau_3 b.
```

Landing `[I_S]_E=z b` gives the slope equations

```text
q1 z^2-(p1-q2)z-p2=0,
tau_3=p1-zq1 in B.
```

Current exact wall:

```text
W-F1-AA-RES-T2J3-SURFACE-SLOPE-FIBER.
```

On a resonance surface `Sigma subset B^3`, determine whether the slope map has
`O(p)` image or `Theta(p^2)` image on `D`-split cubics. This is a sub-reserve
`sigma=2` wall and is not a corrected-reserve counterpacket unless reserve
assumptions are separately changed.

Do not bank:

- slope collapse on `Ra/Rb`;
- a `Theta(q_line)` counterpacket;
- a proof of `conj:B`;
- any result above corrected reserve;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 15 Surface Slope-Fiber Rank/Determinant Audit

Status: EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle15_forced_ra_slope_scan.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle15_forced_ra_slope_scan_certificate.md`

Harness note:

- Cycle 15 completed with `answerSource=claude_structured_jsonl` and
  `classification=EXACT_NEW_WALL`.
- The clean `response.md` is the audited math artifact; terminal transcript is
  revenue/debug evidence only.

Banked reduction:

- On the Cycle 14 resonance surface, landing `[I_S]_E=z b` is equivalent to
  the affine equation

```text
L_z(tau)=iota(tau)-z mu(tau)=0 in A=F[X]/E.
```

- Writing the `B`-linear part of `L_z` as columns

```text
c1(z), c2(z), c3(z) in A ~= B^4,
```

gives a determinant consistency polynomial

```text
Q(z_0,z_1)=det_{4x4}[c1(z) | c2(z) | c3(z) | c0(z)].
```

Audit correction:

- Do not bank the raw rank-only dichotomy. Rank `3` alone does not imply a
  `Theta(q_line)` slope family.
- If rank is `3` and `Q!=0`, the possible slopes lie on a bounded-degree
  plane curve over `B`, hence are `O(p)`.
- The possible large-slope regime is rank `3` with `Q==0` identically, plus
  enough split-distinct co-supports and finite slope map.

Current exact wall:

```text
W-F1-AA-RES-T2J3-SURFACE-SLOPE-FIBER-RANK-DETERMINANT.
```

Next run should either prove `Q!=0` or equivalent curve-sized image control on
source-valid `Ra/Rb` resonance data, or construct source-valid data with
`Q==0` identically and `C2=Theta(p^2)=Theta(q_line)`.

Do not bank:

- a proof of slope collapse on all resonance strata;
- a `Theta(q_line)` counterpacket;
- the raw claim that rank `3` alone decides the slope count;
- a proof of `conj:B`;
- any result above corrected reserve;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 16 Rank/Determinant Resonance Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`

Harness note:

- The visible terminal scrape was classified
  `HARNESS_MALFORMED_VISIBLE_TERMINAL` and is not banked as math.
- A clean recovered Claude structured JSONL answer exists and is the audited
  math artifact.
- The run also exposed a source-mount bug: the Packy source snapshot omitted
  Cycle 15 audit/certificate files. Refresh `current_loop_20260618` before the
  next Fable run.

Banked safe-side lemma:

- In the `D=F_p`, `t=sigma=2`, `j=3` regime, off
  `R0={wedge([W]_E,[Bnum]_E)=0}`, if

```text
Q(z_0,z_1)=det_{4x4}[c1(z)|c2(z)|c3(z)|c0(z)]
```

is not identically zero, then every landing slope lies on the nonzero plane
curve `Q=0`, with `deg Q<=4`. Thus

```text
C2 <= 4p = O(p)=O(n).
```

Audit-only content:

- The recovered answer proposes a trace/Plucker formula and conjugate-skew
  Gram criterion for `Q==0`. Treat this as a verifier target, not yet as a
  proved banked lemma.

Current exact wall:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT.
```

On source-valid `Ra/Rb` resonance data with `Q==0` identically, determine
whether the slope map restricted to distinct `D`-split cubics has
`Theta(p^2)=Theta(q_line)` image or collapses to `O(p)=O(n)`.

Do not bank:

- `Q==0` alone as a counterpacket;
- slope collapse on the `Q==0` branch;
- the trace/Gram criterion until independently checked;
- any proof of `conj:B`;
- any result above corrected reserve;
- any protocol/MCA/CA/list-/line-decoding consequence;
- any `q_gen` collapse.

## Cycle 37 Single-Prime S4 Certificate Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_local_result.txt`

Banked content:

- The Cycle 36 explicit family remains source-valid in the hand gates:
  `B=F_p`, `F=F_{p^2}=B(alpha)`, `alpha^2=-1`, `p=3 mod 4`,
  `E=X^2+alpha X+1`, `b=X`, `D=F_p`.
- `E(a)=(a^2+1)+alpha*a` has no root on `D=F_p`.
- `E-E^tau=2 alpha X`; common roots force `X=0`, but `E(0)=1`.
- The active branch is `c notin B`, `c_b!=0`, and the remaining free data can
  be chosen with `kappa!=0`; the normalization `u=1+X` gives `kappa=1`.
- With `c=alpha`, `d=1`, the top symbol quantity is `Q4=N(c_b)!=0`, so
  `Delta=det_B M(z)` is not identically zero and the determinant curve
  contributes at most `4p` slopes in this restricted branch.

Rejected content:

- The model-proposed Python checker is not a working single-prime certificate.
  Codex ran it locally and it fails with
  `TypeError: unsupported operand type(s) for %: 'tuple' and 'int'`.
- Do not bank a geometric `S4` proof, a finite certificate, or a
  `COUNTERPACKET` from Cycle 37.

Current exact wall:

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

Cycle 38 deliberately uses a homerun prompt: try to solve or disprove the
route outright; if that fails, repair the checker, produce a source-valid
counterpacket seed, or reduce the obstruction to the next exact lemma.
