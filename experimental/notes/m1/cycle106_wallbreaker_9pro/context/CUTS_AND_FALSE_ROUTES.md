# Current Route Cut - 2026-06-21 Cycle 105

Do not use generic RS list-size, Johnson-radius, characteristic-free, or
unconditional divided-difference arguments as the primary route for the uniform
central-rate upper bound.

Reason: in the prize reserve regime `sigma=o(n)` with `k=rho n`, the activity
radius is beyond Johnson. Superpolynomial subgroup-periodic list configurations
exist in the charged branch. A successful proof of the active aperiodic bound
must consume above-reserve aperiodicity of `Uhat`.

# Current Route Cut - 2026-06-20 Cycle 75

Do not treat the product-injectivity ladder as a complete proof of
`m_max<=12`.

Reason: even a pass through `k=5` only forces collisions to differ in at least
six of seven slots. A Singleton-style length-7 alphabet-48 distance-6 bound
gives at best:

```text
m_max <= 48^2 = 2304,
```

not `12`. The ladder is useful for support structure and acceleration, but
the active target is still direct max-fiber certification or a 13-fold
collision packet.

# Previous Route Cut - 2026-06-20 Cycle 74

Do not treat `D<=155` as the only viable route to the Role 05 model target.

Reason: `D<=155` is a valid sufficient condition for `m_max<=12`, but it is
probably too strong. A random-map heuristic gives total ordered collision
energy near:

```text
(48^7)^2/(17^16-1) ~= 7082.63.
```

This can coexist with small maximum fibers. The actual obstruction is a
13-fold fiber in the constrained domain `P_0`, so the live target is direct
max-fiber certification or an explicit 13-fold collision.

# Previous Route Cut - 2026-06-20 Cycle 73

Do not treat another unrun compiled-verifier sketch as progress on the ladder.

Reason: Cycles 72 and 73 both returned useful verifier architecture but had
read-only tools and explicitly did not execute code. The next model run should
either execute/certify product-only `k=3/k=4` or produce an explicit collision;
otherwise the ladder remains open.

# Previous Route Cut - 2026-06-20 Cycle 72

Do not treat unrun verifier code as a product-injectivity certificate.

Reason: Cycle 72's worker had read-only tools and explicitly marked the
returned Python/C verifier artifacts as `UNRUN`. The response is useful for
the next compiled-verifier prompt and banks the displacement-energy
decomposition, but it does not prove `k=3`, `k=4`, `k=5`, or `D<=155`.

The live target remains an actual product-only compiled run, structural proof,
or explicit collision.

# Previous Route Cut - 2026-06-20 Cycle 71

Do not use `(color, product)` as a duplicate key for product-injectivity unless
you have separately proved that product equality forces color equality.

Reason: the ladder condition is equality of field products. A verifier keyed by
`(color, product)` can miss a product collision whose two preimages have
different color. Cycle 71's returned Python sketch has this flaw. The corrected
reference key is packed field product only.

The live verifier target is product-only `k=3/k=4`, or a proof that the color
filter is lossless.

# Route Cut - 2026-06-20 Cycle 70

Do not use the Cycle 70 t-independent slot-value collapse.

False claim:

```text
u_t(i,a) = prod_{c in 3^a D_i}(beta^2-c).
```

Codex's local checker cuts this with a first counterexample at
`(t,i,a)=(1,1,0)`. The missing term is the t-dependent argument
`eta^(-2t)` after pulling out `(eta^(2t))^8=3^t`.

Surviving identity:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

The live wall remains an optimized `k=3/k=4` ladder run or collision-energy
count, not a symbolic collapse to prime-field shifts.

# Current Route Cut - 2026-06-20 Cycle 67

Do not use the pure color-class shortcut as a proof of `Occ(beta)>=2^32`.

Reason: Cycle 67 identifies color as only the coarse `Z/16` projection. The
within-class injectivity and cross-class disjointness needed for the shortcut
live in the full cyclic group of order `17^16-1`, i.e. in the relation lattice
of `{beta-x : x in mu_256}`. The shortcut may be true for the explicit model,
but it is not a theorem about color alone.

The repaired target is the exact finite multiplicity wall:

```text
W-CYCLE67-COLLISION-MULTIPLICITY: prove or kill m_max(beta)<=12.
```

# Current Route Cut - 2026-06-20 Cycle 66

Do not treat an implementation-ready occupancy verifier as a proof that
`Occ(beta) >= 2^32`.

Reason: Cycle 66 supplied a precise finite setup and useful corrections, but
the full occupancy count was not executed and the proposed projected-power
lower-bound backend was left as an ellipsis. The result is model-level verifier
progress, not an official counterpacket.

---

# Route Cut - 2026-06-20 Cycle 65

Do not try to collapse thickened color to product color or truncated jet.

Reason: Cycle 65 proves

```text
rho_beta(T)=beta^113 E_T(1/beta),
```

so the thickened coordinate sees full locator coefficients. The Role 05 packet
fixes only the first five elementary coefficients and the product; higher
coefficients vary.

The next live quantity is explicit occupied color count, not a symbolic
collapse identity.

---

# Current Route Cut - 2026-06-20 Cycle 64

Do not use exact prefix-gadget charge as a scalar support-mass smallness
certificate.

Reason: Cycle 64 proves that for fixed subgroup scale the total gadget charge
is exactly the scalar support mass `N_Delta(b)`. Role 05 already gives

```text
N_Delta(b_0) >= 52,747,567,104 > 2^32.
```

The remaining relevant quantity is thickened MCA color occupancy, not support
mass.

---

# Cuts And False Routes

## Do Not Directly Amplify The T2J4 Quartic/S4 Mechanism To Reserve Scale

Status: ROUTE_CUT / BANKABLE_LEMMA / AUDIT.

Cycle 43 cuts the literal route

```text
fixed t=2,j=4 quartic/S4 density 1/24
=> direct reserve-scale positive density by amplifying the same mechanism.
```

Reason:

- the fixed branch is the square point `j=2t`;
- reserve scale has `j=Theta(n) >> 2t=Theta(n/log n)`, so the square Cramer
  and single-quartic monodromy object is absent;
- balanced diagonal scaling `j=2t -> infinity` has totally split monodromy
  density at most `1/j -> 0`.

This does not cut the reserve-scale route. It redirects it to cosupport
landing / subset-product equidistribution.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`

## Do Not Treat Cycle 41 A-Side Raw G2/G3 Failure As A Route Cut

Status: ROUTE_CUT / BANKABLE_LEMMA / AUDIT.

Cycle 42 cuts the false route

```text
A fails G2/G3 on raw affine/Cramer data
=> Subcase A cannot globalize.
```

The raw Cycle 41 gate is a sufficient simple-affine-chart criterion, not an
intrinsic necessary good-reduction test. The returned Cycle 42 certificates
diagnose the A-side failure as unsaturated/projective/common-factor behavior,
and give corrected Subcase A good reduction at `p=7`.

Do not keep searching for an A-side obstruction unless a concrete flaw is
found in the Cycle 42 certificate package. The current wall is reserve scaling,
not another fixed `t=2,j=4` good-prime search.

Source:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`

## Do Not Use Resolvent Plus Discriminant Without Quartic Transitivity

Status: ROUTE_CUT / AUDIT.

Cycle 36 corrects a possible overclaim in the raw recovered answer. For a
quartic family, the shortcut

```text
resolvent absolutely irreducible + nonsquare discriminant ==> S_4
```

is not safe unless quartic transitivity/geometric irreducibility is also
certified. A quartic with a linear factor and irreducible cubic factor can have
an `S_3` subgroup behavior.

Future certificates must include a transitivity witness. A finite-place
factorization type `"4"` is a clean witness; types `"4"` and `"13"` are the
preferred certificate package.

## Do Not Promote A Finite S4 Histogram To A Uniform Counterpacket

Status: ROUTE_CUT / AUDIT.

Cycle 35 gives a useful finite-place `S_4` certificate: off-`Delta`
squarefree types `"4"` and `"13"` certify `G_geom=G_arith=S_4` for a fixed
tested source-valid instance. That is enough to interpret the Cycle 32
histogram as serious `EXPERIMENTAL / AUDIT` evidence.

It is not enough to bank a `COUNTERPACKET`. A counterpacket seed still needs:

- an explicit source-valid family for infinitely many primes;
- uniform geometric `S_4`;
- arithmetic/geometric equality over the family;
- a controlled finite-field splitting estimate;
- preservation of the Cycle 29/30/33/34 hypotheses.

Do not cite the Cycle 32/35 finite data as a full `Theta(q_line)` result or
as a prize-level disproof.

## Do Not Explain The T2J4 Off-Curve Count By Rank-One Collapse

Status: ROUTE_CUT / BANKABLE_LEMMA / AUDIT.

Cycle 34 cuts the hidden rank-one / curve-collapse explanation for the
off-curve `t=2,j=4` `A^2_B` family. On the source-valid dense open, the
rational map

```text
psi:z |-> tau(z)=M(z)^(-1)(-C_0(z))
```

has generic `B`-Jacobian rank two and is birational onto the Cycle 30 quadric
image. Thus the off-curve image is a surface, not a curve.

Future work should attack the geometric monodromy, transitivity, and
constant-field layer. Do not keep trying to force `O(p)` through generic
Jacobian rank collapse unless a concrete flaw is found in the Cycle 34
dominance argument.

## Do Not Treat The T2J4 Singular Curve As A Theta(q_line) Source

Status: ROUTE_CUT / BANKABLE_LEMMA / AUDIT.

Cycle 33 cuts the singular determinant curve as a possible `Theta(q_line)`
source in the restricted `t=2,j=4` branch. Under the Cycle 29 top-symbol
nonzero hypotheses, `Delta(z_0,z_1)=det_B M(z)` has total degree at most four
and is not identically zero, so `Delta=0` has at most `4p` points over
`B=F_p`.

Future work should attack the off-curve rational map and quartic
resolvent/monodromy. Do not keep treating boundary mismatches in the Cycle 32
checker as evidence for a surface-sized singular contribution.

## Do Not Use One-Variable B(z) Or F(z) For The T2J4 Quartic Family

Status: ROUTE_CUT / AUDIT.

Cycle 32 cuts the one-variable framing. Numerically `|F_{p^2}|=|A^2(F_p)|`,
but the algebraic object is not a one-variable function field. Write

```text
z=z_0+alpha z_1,     z_0,z_1 in B=F_p.
```

The Cycle 29 columns are affine-linear in `(z_0,z_1)`, so the determinant
`Delta=det_B M(z)` is a plane curve and the off-curve quartic family lives
over the surface `A^2_B`. Any Chebotarev/Lang-Weil/monodromy argument must be
made on this two-dimensional base with the `B=F_p` splitting condition.

Do not cite Cycle 31's one-variable framing as a proof of `1/24` density, and
do not use `F(z)` to merge `B`, `F`, `q_gen`, and `q_line`.

## Do Not Treat Cycle 31 As A T2J4 Counterpacket

Status: ROUTE_CUT / AUDIT.

Cycle 31 labels its answer `ROUTE_CUT` and claims the hidden `O(p)` collapse
"does not exist." That is not banked. No discriminant, resolvent, monodromy
group, or Chebotarev constant was computed.

Bank only the narrower conclusion:

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```

is the next exact wall. A `Theta(q_line)` counterpacket requires a
source-valid positive-density splitting theorem or an explicit growing-prime
family, not the generic `1/24` heuristic.

## Do Not Treat Generic Two-Quadric Dimension As A T2J4 Counterpacket

Status: ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL.

Cycle 30 rewrites the `t=2,j=4` split-quartic gate as one `F`-quadric, i.e.
two `B`-quadrics, in four elementary-symmetric variables. A naive dimension
count suggests a surface and possible `Theta(q_line)=Theta(p^2)` split
density, but that is not a source-valid counterpacket.

Reason:

- The variables are not arbitrary `B^4` points. They must be elementary
  symmetric tuples of four distinct roots in `F_p`.
- The finite direct scans count realized bad slopes and lean toward `O(p)`,
  not positive-density `p^2`, in random small source-valid instances.
- Thus the next question is the hidden split-locus collapse, not a generic
  algebraic-geometry dimension heuristic.

Future workers should prove the collapse, produce a genuine growing-prime
source-valid `Theta(q_line)` family, or isolate the exact invariant controlling
the discrepancy.

## Do Not Extend The T2J3 Determinant Obstruction To T2J4

Status: ROUTE_CUT / EXACT_NEW_WALL.

Cycle 29 shows why the Cycle 28 determinant proof does not automatically
extend from `j=3` to `j=4`. At `j=3`, three co-support parameters live in a
four-dimensional `B`-space, so affine consistency is controlled by an
augmented determinant. At `j=4`, four parameters live in the same
four-dimensional space, so the coefficient determinant is square:

```text
M(z)tau=-C_0(z).
```

When `det_B M(z) != 0`, this gives a unique affine preimage for each slope
rather than an obstruction to realizing the slope. The nonzero top symbol

```text
TopSym(det_B M(z))=-N(kappa)N(z)^2Q_4
```

only proves generic invertibility. It does not prove `C2=O(p)` at `j=4`.

Future prompts must attack the distinct split-quartic gate for `tau(z)`, not
ask for another top-symbol proof as if it would bound slopes.

## Do Not Search The Restricted T2J3 Q==0 Branch Further

Status: ROUTE_CUT / PROOF.

Cycle 28 proves, in the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`,
`t=sigma=2`, `j=3`, off-`R0`, `c_b!=0`, source-valid separated window, that
`Q_4!=0` and therefore `Q` is not identically zero. Hence Cycle 16 gives
`C2<=4p`.

Future workers should not search this branch for `Theta(q_line)`
counterpackets unless they first find a concrete flaw in the Cycle 28 proof
dependencies. The next wall is `t=2,j=4`, not another `t=2,j=3` retry.

## Do Not Re-Attack Source-Valid Q==0 In T2J3 Without First Auditing Q4

Status: ROUTE_CUT / superseded by Cycle 28 restricted proof.

Cycle 27 appears to cut the last source-valid `Q==0` branch in the restricted
`D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0` window:

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) * Im(conj(c) d) ).
```

For `c notin B`, `Q_4=0` is equivalent to `E` having an `F_p` root, hence to
the Cycle 24 locator norm `prod_{a in F_p}E(a)` vanishing. Source-validity
excludes this. For `c in B`, separatedness gives `d notin B`, so
`Q_4=N(c_b)*Im(d)^2 != 0`.

Until the Cycle 28 proof audit is done, do not treat this as a final proof.
But also do not keep searching for a `Theta(q_line)` counterpacket on this
branch without first finding a flaw in the `Q_4` derivation or source-validity
implication.

## Do Not Treat Q==0 Alone As A Counterpacket

Status: ROUTE_CUT / EXACT_NEW_WALL.

Cycle 25 rejects the determinant-only overclaim. For fixed `z`, the determinant

```text
Q(z)=det_B[c_1(z)|c_2(z)|c_3(z)|c_0(z)]
```

is a necessary consistency condition for the affine system

```text
c_1(z)tau_1+c_2(z)tau_2+c_3(z)tau_3+c_0(z)=0.
```

It is sufficient only when the first three columns have rank `3`. If their
rank drops, `Q(z)=0` may hold automatically while `c_0(z)` is not in their
span. Therefore future agents must not claim

```text
Q==0 identically => every z in F is realized
```

or a `Theta(q_line)` counterpacket without the rank-stratified consistency
conditions and a growing-prime source-valid family.

## Do Not Keep Searching The Source-Valid D=0 Off-R0 Branch In T2J3

Status: ROUTE_CUT / BANKABLE_LEMMA.

Cycle 24 proves, in the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`,
`t=sigma=2`, `j=3` window, that

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a).
```

Source-valid residue-line denominators are nonzero on `D=F_p`, so
`N(ell)!=0`; off `R0`, `kappa!=0`. Hence `D=0` off `R0` has no source-valid
points in this restricted window. The previous nonsplit-`c` wall is cut.

Future prompts should return to the non-`D=0` determinant-split branch
`W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT` rather than looking for a
`Theta(q_line)` seed on `D=0`.

## Do Not Use Unrestricted Extension-Line MCA Lift

Status: ROUTE_CUT / COUNTERPACKET.

The claim that a base MCA numerator can be divided by `q_chal=|F|` for arbitrary extension-valued lines is false. The finite and fixed-rate `E=X-alpha` witnesses show extension-valued bad slopes can occupy a positive fraction of `F`.

## Do Not Use Raw Arbitrary Locator Fibers

Status: ROUTE_CUT / COUNTERPACKET.

Raw support fibers count contained supports and can be huge even when actual list size is 1. Any L1 proof must repair the object before citation.

## Do Not Call Paper D Universal Cap Unconditional

Status: AUDIT / CONDITIONAL.

Paper D's arithmetic is internally coherent in the available audit, but its imported Crites-Stewart / ABF theorem remains unverified from primary source.

## Do Not Use W-F1-AA-AGR As A Balanced Wall

Status: ROUTE_CUT.

Cycle 4 verifies that source notation has `a=ceil((1-delta)n)` and `sigma=a-k`. In the balanced regime `t=sigma`, one has `k+t=a=s_delta`. Therefore the high-agreement condition `nu(S)>=s_delta` adds no condition on an `a`-subset and is not a separate balanced wall. High-agreement belongs only to unbalanced `t<sigma`, already routed through the residual-slack/list object.

## Do Not Absorb Nonconstant CRT Multipliers Into Words

Status: ROUTE_CUT.

Cycle 7 rejects the claimed transfer from

```text
[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat
```

to an ordinary base residue-line datum with pointwise word `w0+theta*w1`.
The CRT class `theta in B[X]/Ehat` is generally nonconstant, and multiplication
by `theta` does not commute with support interpolation. A local check over
`F_5` with `Ehat=X^2+1`, `theta=X`, and `S={0,1}` gives
`theta*interp_S(w1) = -1 mod Ehat` but `interp_S(theta*w1)=X mod Ehat`.

Therefore do not import `thm:exactcount` / `thm:rigidcyclo` to the `z in B`
stratum unless a new theorem proves the appropriate twisted-readout count.

## Do Not Treat The Twist As A Remaining Wall

Status: ROUTE_CUT / BANKABLE_LEMMA.

Cycle 8 proves that in the separated quadratic case the twisted quotient
readout is isomorphic to the original extension residue:

```text
B[X]/Ehat ~= F[X]/E,
[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat
  <-> [interp_S(w0)+alpha interp_S(w1)]_E.
```

So do not ask future workers to solve the twist itself. Cycle 9 further
sharpens the live problem to the bad-line incidence wall
`W-F1-AA-RES-LINE-INCIDENCE`.

## Do Not Treat Raw Residue Count As The MCA Slope Count

Status: ROUTE_CUT / EXACT_NEW_WALL.

Cycle 9 separates two objects:

```text
C1 = #{[interp_S(w)]_E}
C2 = #{z in F : exists S with [interp_S(w)]_E = z[Bnum]_E}
```

The source normal form counts slopes, so `C2` is the relevant object. A raw
residue count/counterexample for `C1` is not by itself an MCA/proximity
advance. The corrected wall is the bad-line incidence problem
`W-F1-AA-RES-LINE-INCIDENCE`.

The locator-quotient form is:

```text
W = L_S Q_S + interp_S(w),  deg Q_S<=n-a-1,
[interp_S(w)]_E = [W]_E - [L_S Q_S]_E.
```

Future prompts should ask for incidence into `[W]_E-F[Bnum]_E`, not a raw
cardinality bound for all extension residues.

## Keep Online Slope Count And Line Incidence Identified

Status: ROUTE_CUT / AUDIT.

Cycle 10 independently restates the corrected source object as
`W-F1-AA-RES-ONLINE-SLOPE-COUNT`. This is not a separate new wall from Cycle 9's
`W-F1-AA-RES-LINE-INCIDENCE`; it is the same object with the source qualifiers
spelled out:

- slope `z in F`;
- landing on the bad line `F[Bnum]_E`;
- noncontained witness;
- quotient-periodic denominators separated as in `rem:aper`.

Do not let future workers fork these into two targets. Use
`W-F1-AA-RES-LINE-INCIDENCE / ONLINE-SLOPE-COUNT` as one wall.

## Do Not Extend Cycle 11 Beyond t=2, j=2 Without A New Theorem

Status: AUDIT / ROUTE_CUT.

Cycle 11 proves a useful low-regime lemma, but only for

```text
t=sigma=2,     j=n-a=r-t=2.
```

The key rigidity is

```text
Q_S = C(X-s_T)+C1,
```

so `Q_S` depends only on the size-2 co-support sum. This is special to
`j=2`. At `j=3`, `deg Q_S<=2`, and dependence on additional co-support
elementary parameters is expected. At `t=3`, bad-line landing has codimension
two in `F[X]/E`.

Therefore do not cite Cycle 11 as:

- a proof of `conj:B`;
- an asymptotic corrected-reserve theorem;
- a result for `j>=3` or `t>=3`;
- a `q_gen` collapse;
- a protocol/MCA/CA/list-/line-decoding consequence.

Use it only as the closed base case for the next walls
`W-F1-AA-RES-T2J3` and `W-F1-AA-RES-T3J2`.

## Do Not Bank Cycle 12 As A t=2,j=3 Slope Bound

Status: AUDIT / ROUTE_CUT.

Cycle 12 proves useful structure for `t=2,j=3`, but it does not prove a
corrected slope-count bound. The banked algebra is:

- `Q_S` depends on `e1(T),e2(T)` and not `e3(T)`;
- bad-line landing is a quadric in `(e1,e2,e3)`;
- `[e3^2]Delta=wedge([W]_E,[Bnum]_E)`.

The false upgrade is:

```text
quadric bad locus => C2=O(n).
```

At `j=3`, solution counting on the quadric can be `Theta(n^2)` for
`D=F_p`, `n=p`; any useful bound must come from slope-fiber collapse, not from
low-degree incidence alone.

Also do not use large sub-reserve `C2` evidence at `eta=2/n` as a
counterpacket to the corrected-reserve conjecture.

## Do Not Use Rank Alone In Cycle 15

Status: AUDIT / ROUTE_CUT.

Cycle 15's useful output is the rank/determinant wall, not a rank-only
dichotomy. For fixed `z`, rank `3` of the columns

```text
c1(z), c2(z), c3(z) in A ~= B^4
```

means the affine equation `L_z(tau)=0` has one determinant consistency
condition

```text
Q(z_0,z_1)=det_{4x4}[c1(z) | c2(z) | c3(z) | c0(z)].
```

If `Q!=0`, the slope set is curve-sized `O(p)`, not `Theta(p^2)`. The possible
large-slope regime requires `Q==0` identically, plus enough split-distinct
co-supports and a finite slope map. Future prompts must ask for this
rank/determinant invariant, not a rank-only count.

## Do Not Treat Q Identically Zero As A Counterpacket

Status: AUDIT / ROUTE_CUT.

Cycle 16 cuts the next tempting overclaim. Even if the determinant consistency
polynomial `Q(z_0,z_1)` is identically zero, this is only a statement about the
ambient `B^3` resonance surface. It ignores the requirement that

```text
X^3-tau_1 X^2+tau_2 X-tau_3
```

split into three distinct roots in `D=F_p`.

Therefore `Q==0` alone is not a `Theta(q_line)` counterpacket. A counterpacket
requires a growing family where, on the distinct split-cubic locus, the slope
count `C2` satisfies `C2/p^2` bounded below. Single-prime examples are
EXPERIMENTAL only, and the whole `t=sigma=2` wall remains sub-reserve.

## Do Not Treat The Cycle 37 Checker As A Certificate

Status: AUDIT / ROUTE_CUT.

Cycle 37 supplied an inline Python checker for a proposed single-prime `S4`
certificate, but Codex extracted and ran it locally and it failed with a type
error caused by mixing `F`-elements with residue-pairs:

```text
TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
```

Therefore Cycle 37 does not bank:

- a working checker;
- a finite single-prime `S4` certificate;
- geometric `S4`;
- a `Theta(q_line)` counterpacket;
- any MCA, CA, list-decoding, line-decoding, protocol, SNARK, or prize claim.

Future work may repair the checker, but must preserve the field ledgers and
show quartic transitivity/geometric irreducibility, a 3-cycle/resolvent
witness, discriminant/sign control, and bad-place exclusions.

## Do Not Treat Cycle 38 Finite S4 As Uniform

Status: AUDIT / ROUTE_CUT.

Cycle 38 repairs the Cycle 37 checker and verifies a finite-place `p=31`
certificate for the explicit `t=2,j=4` family. This cuts only the false route
that the Cycle 37 checker failure was mathematical evidence against the
family.

Do not cite Cycle 38 as:

- a symbolic or uniform `S_4` proof;
- a good-reduction theorem;
- a `Theta(q_line)` counterpacket;
- a corrected-reserve theorem;
- an MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or
  prize result.

The live wall is the symbolic/good-reduction bridge:

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
```
# Current Route Cut - 2026-06-21 Cycle 102

```text
L-CYCLE102-PADE-SHORT-WINDOW-DIVISOR-FALSIFIER
```

False route:

```text
theta active
=> the short-window Padé/BM denominator of (theta^j-P_j)_{j=1}^{sigma+1}
   is compatible with a divisor of X^n - 1.
```

Cycle102 gives an explicit aperiodic finite falsifier over `F_29`, with
`n=7`, `sigma=3`, `S'={1,16,24}`, `theta=2`, and window `(12,21,28,13)`. The
short-window recurrence has characteristic polynomial `T^2-24T+1`, irreducible
over `F_29`, so it cannot divide `X^7-1`.

Correct replacement:

```text
g_{S'}(X) Uhat(X) == 1 - theta X  (mod X^{sigma+2})
```

and the next wall is the distinct `e_1` image on the `Uhat`-flat locus.
