# Executive verdict

**AUDIT**

The full prize problem is **not close**. The current route still lacks hard global inverse theorems, not merely constant optimization or formal cleanup.

* **MCA:** plausibly solvable after a substantial reorganization around a canonical line-level structure extractor. Confidence: **moderate**.
* **Interleaved list decoding:** materially farther away. The projection to scalar lists is banked, but the scalar circuit-transversal theorem is an independent hard inverse problem. Confidence that the present route alone closes it: **low-to-moderate**.
* Confidence that the current state is “one theorem away”: **low**.
* Confidence that (t>\sigma) should cease to be a separate research branch: **high**.
* Confidence that the current primitive ledger is incomplete: **high**.
* Confidence that the two Lattès finite constructions are arithmetically valid, modulo certificate and constant-field formalities: **high**.

The route has broadened every time a supposedly primitive remainder was isolated:

[
\text{monomial quotient}
\to \text{split-rational quotient}
\to \text{Lattès quotient}
\to \text{configuration character}
\to \text{module-level apolar structure}.
]

That is evidence against continuing to enumerate exceptional families one at a time. The next central object must be a **canonical low-complexity representation of the split locator/configuration algebra**, with a bounded-overlap theorem on one affine syndrome line.

A genus-by-genus classifier, by itself, is the wrong wall. A fixed-map Hasse–Weil bound does not control the sum over all maps realized by one syndrome line.

---

# AUDIT

## 1. Repository integrity and principal checks

The supplied archive matches its SHA-256 digest.

Independent arithmetic checks support the following conclusions.

### Degree-31 Lattès packet

For the construction in `01_lattes_degree31_counterpacket.md`:

* (p=8191), (F=\mathbb F_{p^{18}}), (n=8192), (k=2048), (\sigma=31).
* The claimed elliptic-curve order and the order-(31) kernel data check.
* The Vélu (x)-map on (\mathbf P^1(\mathbb F_{8191})) has fiber histogram
  [
  {31:131,\ 16:1,\ 1:4115}.
  ]
* The finite combinatorial and collision counts check.
* The domain is an allowed dyadic coset and generates the full field.
* The denominator degree, transversality and proper-envelope exclusion arguments are structurally sound.

What is still missing before promotion:

1. an explicit irreducible degree-(18) polynomial and reproducible field embedding;
2. emitted rational-map coefficients rather than existence-only construction;
3. careful arithmetic-versus-geometric Galois-closure and constant-field wording.

Status: **LIKELY / not yet banked**.

### Degree-113 Lattès packet

For `02_lattes_degree113_counterpacket.md`:

* (p=65537), (F=\mathbb F_{p^{15}}), (n=65536), (k=4096), (\sigma=113).
* The two elliptic-curve orders, the degree-(113) endomorphism kernel, the image size (580), the (144) free (C_4)-orbits and the (113)-point fibers check.
* The field-size, support-count and collision inequalities have very large margins.
* The official rate (1/16) and field restrictions are satisfied.

One statement should be weakened: the construction proves **at least**
(\binom{144}{37}) bad slopes, not necessarily exactly that many.

Status: **LIKELY / not yet banked**.

## 2. The divisor-norm packet is not at an official exact rate

The finite packet in `05_divisor_norm_character_counterpacket.md` uses

[
k=2{,}143{,}399{,}963,
]

whereas

[
\frac n8=2{,}147{,}483{,}648.
]

Thus that packet is not itself an exact rate-(1/8) prize instance.

It remains a valid counterexample to a general primitive completion theorem. Its prime choices are important: they exclude the listed pure and reserve-fixed equal-fiber templates. Those prime exclusions disappear after specializing to exact official dimensions.

Consequently:

* it kills the unrestricted primitive theorem;
* it does **not yet** prove that configuration characters are an independent official-rate ledger term after every possible split-rational/module container has been removed.

That official-rate independence question needs an explicit tagging audit.

---

# PROOF

## BANKABLE_LEMMA after a mechanical certificate: exact-rate product-character failure packets

The general product-character construction can nevertheless be specialized to all four official rates.

Take

[
p=2^{31}-1,\qquad
F=\mathbb F_{p^8},\qquad
q=p^8,\qquad
n=2^{34}.
]

Since

[
\operatorname{ord}_{2^{34}}(p)=8,
]

an order-(n) subgroup (H\leq F^\times) generates (F). Hence this is a same-field allowed domain with

[
k\leq 2^{40},\qquad q<2^{248}<2^{256}.
]

Put

[
T_q=\left\lfloor q/2^{128}\right\rfloor,
\qquad
\log_2T_q=119.9999999946\ldots .
]

For an exact dimension (K=\rho n), the product-character theorem gives

[
|Z|
\ge
\frac23
\min\left{
\left\lfloor
\frac{\binom n{K+\sigma}}
{nq^{\sigma-2}}
\right\rfloor,
\left\lfloor\frac{q-n}{2K}\right\rfloor
\right}.
]

The following are the largest reserves certified by this particular lower bound.

| Rate (\rho) | MCA reserve (\sigma) | Unsafe radius (1-\rho-\sigma/n) | (\log_2) occupancy | (\log_2) constructed slopes, lower bound |
| ----------: | -------------------: | ------------------------------: | -----------------: | ---------------------------------------: |
|       (1/2) |     (69{,}270{,}417) |            (0.4959679310559295) |          (91.9255) |                               (213.4150) |
|       (1/4) |     (56{,}558{,}797) |            (0.7467078447225504) |         (-69.6265) |                               (143.7886) |
|       (1/8) |     (38{,}083{,}574) |            (0.8727832442382351) |          (33.4628) |                               (215.4150) |
|      (1/16) |     (23{,}737{,}657) |            (0.9361182865104638) |         (-90.9905) |                               (122.4245) |

Every final column exceeds (\log_2T_q). In particular, even the weakest case gives normalized MCA error above approximately

[
2^{122.4245-248}>2^{-126}>2^{-128}.
]

At the next reserve, the pre-color bucket logarithms are respectively

[
57.90,\quad -102.07,\quad 2.24,\quad -121.12,
]

so this simple certificate no longer reaches (T_q).

The MCA construction initially uses

[
C_0=\operatorname{ev}_H((X-\beta)\mathcal P_K).
]

This is diagonally monomial-equivalent to the standard code
(\operatorname{RS}[F,H,K]). Coordinatewise multiplication by the nonzero
vector ((x-\beta)_{x\in H}) preserves agreement supports, affine lines and
slope counts. Thus the packet transfers to standard RS.

### Scalar list specialization

Set the theorem’s polynomial parameter to (k=K-1) and its reserve to
(\sigma=\tau+1). Then every (Q_T) has degree at most (K-1), so all
constructed objects are actual codewords in the standard
(\operatorname{RS}[F,H,K]), around one received word, with agreement
(K+\tau).

| Rate (\rho) | Extra agreement (\tau) | Unsafe radius (1-\rho-\tau/n) | (\log_2) actual scalar list, lower bound |
| ----------: | ---------------------: | ----------------------------: | ---------------------------------------: |
|       (1/2) |       (69{,}270{,}416) |          (0.4959679311141372) |                               (305.9487) |
|       (1/4) |       (56{,}558{,}796) |          (0.7467078447807580) |                               (142.8138) |
|       (1/8) |       (38{,}083{,}573) |          (0.8727832442964427) |                               (244.6845) |
|      (1/16) |       (23{,}737{,}655) |          (0.9361182866268791) |                               (363.2630) |

The next-reserve lower logarithms are

[
57.9255,\quad -103.6265,\quad -0.5372,\quad 119.1363,
]

all below (\log_2T_q).

These are genuine official-rate scalar-list counterpackets. They strengthen the failure side. They do **not** prove that the packet is outside every official-rate quotient or low-rank module container.

Confidence: **high**, subject to producing an exact-integer Robbins certificate and an independent monomial-equivalence audit.

---

# COUNTERPACKET

The product-character result creates an immediate cross-worker conflict.

The proposed critical-seed estimate

[
|\mathcal H(B)|
\le
\left\lceil
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
\right\rceil+2r
\tag{H2-19}
]

cannot be true after removing only the previously listed point-fiber and
envelope classes. The nonofficial prime packet has approximately (2^{215})
slopes, versus occupancy below (2^{29}) and (2r<2^{36}).

There are only two possible repairs:

1. configuration-character packets are removed before applying the estimate; or
2. a broader module/split-rational container is defined that demonstrably
   contains the product-character packet.

Calling the packet “primitive” and then applying (H2-19) is false.

For the exact official rates, the same construction gives large failure
packets, but the loss of the prime divisibility exclusions means that its
classification remains open.

---

# ROUTE_CUT

## 1. End the separate (t>\sigma) thick-residue program

The Cycle-59 universal-chart result shows that denominator degree is not an
intrinsic obstruction:

* every syndrome line has a degree-(r) presentation;
* arbitrary displayed denominator degrees can be introduced;
* action rank depends on presentation;
* the explicit
  [
  F=\mathbb F_{97},\quad n=16,\quad k=8,\quad
  \sigma=2,\quad t=3
  ]
  packet has (67) envelope-free slopes, minimal displayed denominator
  (3), and full monomial action ranks.

Any proposed theorem whose conclusion depends intrinsically on the displayed
(t) is already dead. The correct object is the denominator-free syndrome
line.

No theorem worker should be allocated to (t>\sigma) compression except to
run a regression test against new claims.

## 2. Do not make low-genus classification the main route

The Lattès packets kill genus-zero-only classification. They do not imply that
the project must classify every genus-one quotient before proving a safe
theorem.

A support-theoretic theorem can charge a realized block system without knowing
whether it arose from:

* a cyclic/dihedral map;
* a (PGL_2) subgroup chain;
* a Lattès map;
* another low-genus cover.

The actual unsolved issue is aggregation across all realized systems on one
line.

## 3. Cut the raw (n^{o(1)}) registry target

For a cyclic domain (H), the degree-two maps

[
R_a(X)=X+\frac aX,\qquad a\in H,
]

have fibers equal to the orbits of

[
x\longmapsto a/x.
]

For nonsquare (a), this gives a perfect pair partition of (H). Distinct
(a)'s give (\Theta(n)) distinct pair partitions.

Thus any argument of the form

[
\text{“there are only }n^{o(1)}
\text{ split-rational fiber systems”}
]

is false. Only a **line-level co-occurrence or core-residue entropy theorem**
could rescue equation (8).

## 4. Cut the constant-one primitive occupancy target

Worst-case maximum over all affine syndrome lines is not the same as the mean
occupancy of one random line. Even after algebraic structures are removed,
uniformity may require:

* an extreme-value term;
* a square-root/discrepancy term;
* a logarithmic factor;
* a finite exceptional floor.

The coefficient (C_{\mathrm{occ}}=1) plus (2r) is a conjectural sharp target,
not a safe intermediate theorem.

---

# EXACT_NEW_WALL

The central MCA wall should be renamed:

[
\boxed{
\texttt{W-MCA-CANONICAL-CONFIGURATION-STRUCTURE-EXTRACTOR}
}
]

Given all transverse (j)-support witnesses on one envelope-free affine
syndrome line, the theorem must assign each nonprimitive packet canonically to
one of:

1. a hereditary coordinate-envelope node;
2. a realized point-fiber/block system;
3. a low-complexity configuration module, including divisor norms;
4. a primitive residue.

It must then bound the **total line-level registry weight**, not the number of
syntactic maps.

The corresponding primitive theorem is:

[
\boxed{
\texttt{W-MCA-POST-STRUCTURE-PRIMITIVE-LOCAL-LIMIT}
}
]

The H2-core theorem and the (t=1) apolar theorem are inputs to the extractor.
They are not themselves charges.

For lists, the corrected wall is:

[
\boxed{
\texttt{W-LIST-GLOBAL-CIRCUIT-HITTING-WITH-CONFIGURATION-MODULES}
}
]

The current quotient/core/envelope trichotomy is probably incomplete unless
configuration-space packets are either added explicitly or shown to be a
special case of the low-affine-rank module branch.

---

# Minimal theorem package

## MCA challenge

### Logical minimum

Only two new code-specific results are logically needed.

**MCA-UPPER.** For every reserve (\sigma), give an explicit integer
(B_C(\sigma)) such that

[
M_C(\sigma)
:=
\max_{\ell}
|\operatorname{Bad}_\sigma(\ell)|
\le B_C(\sigma).
]

**MCA-LOWER.** At the preceding reserve, construct one line satisfying

[
|\operatorname{Bad}_{\sigma-1}(\ell)|>T_q.
]

The finite threshold-extraction lemma is already banked.

### Realistic decomposition of MCA-UPPER

The smallest credible decomposition is:

1. **Canonical structure extraction.**
   Assign all nonprimitive witnesses to canonical envelope, block-system or
   configuration-module containers.

2. **Global registry charge.**
   Bound the total weight of all containers occurring on one line:
   [
   Q_C(\sigma)+X_C(\sigma)+E_C(\sigma).
   ]

3. **Primitive local limit.**
   After all canonical structure is removed,
   [
   P_C(\sigma)
   \le
   C_{\mathrm{occ}}
   \frac{\binom n{k+\sigma}}{q^{\sigma-1}}
   +D_C(n,\sigma,q),
   ]
   with explicit (C_{\mathrm{occ}}) and discrepancy (D_C).

4. **Hereditary termination.**
   Prove that recursive shortening/envelope descent has a finite globally
   chargeable tree.

The final bound would have the form

[
M_C(\sigma)
\le
O_C(\sigma)
+Q_C(\sigma)
+X_C(\sigma)
+E_C(\sigma)
+P_C(\sigma).
]

### Asymptotic versus finite MCA requirements

An asymptotic theorem may tolerate:

* (n^{o(1)}) multiplicative losses;
* unspecified sufficiently large (q);
* (O(n)) floors;
* constants depending on fixed degree or rate.

The official (2^{-128}) certificate may not. It needs:

* a computable integer for every term;
* canonical deduplication across overlapping containers;
* exact field-generation accounting;
* the field cap (|F|<2^{256});
* exact comparison to (\lfloor q/2^{128}\rfloor);
* a failure witness at the previous integer reserve;
* the endpoint convention
  [
  \delta<
  1-\rho-\frac{\sigma^*-1}{n}
  ]
  for arbitrary real radii.

An (n^{o(1)}) factor is not a certificate. At (n=2^{34}), even one factor
of (n) costs (34) bits.

## Grand list decoding challenge

### Logical minimum

Because the same-field projection theorem is banked, the genuinely missing
theorem is scalar:

**LIST-UPPER.** For every scalar syndrome (s), construct a hitting set
(Z_s) meeting every low-arity full-support circuit and prove

[
|Z_s|
\le
T_q-\left\lfloor\frac{r-1}{\sigma}\right\rfloor.
]

The banked circuit theorem then gives

[
L_1(k+\sigma)\le T_q.
]

The projection theorem gives

[
L_m(k+\sigma)\le T_q
]

for every constant—or indeed arbitrary—interleaving arity (m), since
(\binom{T_q+1}{2}<q).

**LIST-LOWER.** At the preceding reserve, exhibit more than (T_q) actual
scalar codewords. The product-character specialization supplies such witnesses
for particular official codes.

### Realistic decomposition of LIST-UPPER

1. exact common-core descent — **banked**;
2. fixed split-rational support profile — **banked**;
3. low-affine-rank envelope charge — **unknown**;
4. bounded-overlap registry across all rational maps and defects — **unknown**;
5. configuration-module circuit branch — **currently missing**;
6. primitive circuit-transversal discrepancy — **unknown**.

The list problem will not follow automatically from the MCA safe theorem.
They share algebra, but the global objects differ: line intersections versus
circuit hitting.

---

# Dependency DAG

Status key:

* **BANKED**
* **LIKELY**
* **UNKNOWN**
* **DOUBTFUL**
* **FALSE**

## MCA DAG

```text
MCA-PRIZE-THRESHOLD
├── Finite reserve/endpoint extraction                         [BANKED]
├── Failure witness at previous reserve                       [BANKED in broad branches]
│   ├── Random-anchor/Bessel construction                     [BANKED]
│   └── Exact-rate product-character specializations          [LIKELY/BANKABLE]
└── MCA-FINITE-MASTER-UPPER                                   [UNKNOWN]
    ├── Denominator-free syndrome transverse-secant identity  [BANKED]
    ├── Canonical configuration structure extractor           [UNKNOWN]
    │   ├── Fixed-partition QAR packing                       [BANKED]
    │   ├── Fixed-core petal theorem                          [BANKED]
    │   ├── Monomial quotient registry                        [BANKED locally]
    │   ├── Lattès packet arithmetic                          [LIKELY]
    │   ├── Genus-0/1 classification                          [OPTIONAL/UNKNOWN]
    │   ├── Split-rational core-registry equation (8)          [DOUBTFUL]
    │   ├── Divisor-norm character branch                     [PROVED AS COUNTERPACKET]
    │   ├── Complete configuration-character ledger           [UNKNOWN]
    │   └── Multi-character/module iteration                  [UNKNOWN]
    ├── Hereditary envelope recursion                         [UNKNOWN]
    │   ├── Leaf peeling                                      [BANKED, audit needed]
    │   └── MDS-3-core extraction                             [BANKED, audit needed]
    └── Post-structure primitive local limit                  [UNKNOWN]
        ├── t=1 apolar complete-intersection normal form       [BANKED, audit needed]
        ├── Corank-one norm-character trichotomy               [UNKNOWN/likely incomplete]
        ├── Critical-seed H2 estimate (19), current form       [FALSE generally]
        └── Higher-genus Frobenius discrepancy, current form  [DOUBTFUL]
```

The discarded branch is:

```text
t > sigma intrinsic denominator compression                  [FALSE]
```

## List DAG

```text
INTERLEAVED-LIST-PRIZE
├── Same-field scalar projection theorem                      [BANKED]
├── Finite projection inequality at T_q                       [BANKED]
├── Scalar full-support identity                              [BANKED]
├── Full-support circuit reduction                            [BANKED]
├── Common-core hereditary descent                            [BANKED]
├── Scalar global circuit-hitting theorem                     [UNKNOWN]
│   ├── Low-arity reduction                                   [BANKED]
│   ├── Fixed split-rational packet profile                   [BANKED]
│   ├── Global split-rational bounded-overlap cover           [DOUBTFUL/UNKNOWN]
│   ├── Low-affine-rank envelope cover                        [UNKNOWN]
│   ├── Configuration-module circuit branch                  [MISSING]
│   └── Primitive circuit discrepancy                         [UNKNOWN]
└── Actual scalar list at previous reserve                    [PARTLY BANKED]
    └── Exact-rate product-character witnesses                [LIKELY/BANKABLE]
```

---

# Ranked kill tests

## 0. Already killed: intrinsic (t>\sigma) compression

**Claim:** high denominator degree implies additional compression or a smaller
intrinsic parameter space.

**Regression parameters:**

[
F=\mathbb F_{97},\quad n=16,\quad k=8,\quad
\sigma=2,\quad t=3.
]

**Refuting output:** the known (67)-slope packet with minimal denominator
(3), full action ranks and no proper envelope.

**Action:** retain one regression script; allocate no theorem worker.

---

## 1. Critical-seed H2 estimate (19)

**Fragility:** very high.

**Claim to test:**

[
|\mathcal H(B)|
\le
\left\lceil
\binom n{k+\sigma}/q^{\sigma-1}
\right\rceil+2r
]

after quotient and envelope removal.

**Toy parameters:**

1. exhaustive:
   [
   F=\mathbb F_{17},\quad n=8,\quad k=4,\quad \sigma=2,3;
   ]
2. medium:
   [
   F=\mathbb F_{97},\quad n=16,\quad k=8,\quad \sigma=2,3;
   ]
3. scaling:
   [
   F=\mathbb F_{193},\quad n=32,\quad k=16,8,4,2.
   ]

For (F_{17},n=8,k=4,\sigma=2),

[
\left\lceil\frac{\binom 86}{17}\right\rceil+2r
=2+8=10,
]

so a primitive (11)-slope line is already a counterexample.

**Checker:** `scan_h2_critical_seed.py`

* enumerate exact transverse support spans;
* canonicalize affine lines;
* compute minimal H2-defective subpackets;
* tag proper envelopes;
* enumerate degree-(\leq3) split-rational partitions;
* tag product and low-image configuration characters;
* report the residual completion count.

**Refuting output:** a seed assigned to the current primitive branch with count
strictly above the proposed bound.

**Confidence-increasing output:** every violation before character removal is
absorbed by an explicit configuration tag, and no violation remains afterward.

A clean tiny-case pass would not prove the theorem, but it would justify
working on the revised post-configuration statement.

---

## 2. Split-rational core-registry equation (8)

**Fragility:** high.

The exact adversarial family is

[
R_a(X)=X+a/X.
]

**Toy parameters:**

* (F=\mathbb F_{97}), (H) of order (16);
* (F=\mathbb F_{193}), (H) of order (32);
* (F=\mathbb F_{257}), (H) of order (64).

For nonsquare (a\in H), (R_a) gives a perfect pair partition. There are
(n/2) such partitions.

**Checker:** `split_rational_registry_kill.py`

1. canonicalize partitions up to target Möbius transformations and domain
   stabilizers;
2. enumerate or sample syndrome lines;
3. identify all partitions supporting a packet above the declared “rich”
   threshold;
4. compute
   [
   \frac{
   \sum_{\Pi\in\mathfrak P(\ell)}
   \binom{N_\Pi}{b_\Pi}}
   {\max_{\Pi}
   \binom{N_\Pi-1}{b_\Pi}}.
   ]

**Refuting output:** one envelope-free line with (n^\varepsilon) pairwise
nonrefining rich systems and ratio (n^{\Omega(1)}).

**Confidence-increasing output:** all systems rich on one line collapse to
(O(\operatorname{polylog}n)) core-residue families or share a proper
hereditary refinement.

If “rich” and “maximal inequivalent” cannot be made canonical before the
experiment, equation (8) is not a theorem statement and should be retired.

---

## 3. Corank-one divisor-norm trichotomy

**Fragility:** high.

The proposed three outcomes

[
\text{envelope}
\quad\text{or}\quad
\text{point-fiber quotient}
\quad\text{or}\quad
\chi_R(T)=\prod_{x\in T}R(x)
]

may omit additive or higher determinantal invariants of the configuration
algebra.

**Toy parameters:**

[
F_{17},\ n=8,\ j=2,3,4;
\qquad
F_{97},\ n=16,\ j=3,\ldots,8;
\qquad
\sigma=2,3.
]

**Checker:** `search_configuration_invariants.sage`

For every separated split-locator family:

* form the (t=1) apolar critical matrix;
* compute its rank-defect ideal;
* eliminate support variables;
* test whether the resulting invariant factors through:

  * a common envelope;
  * a point partition;
  * products (\prod R(x)) for rational (R) of bounded degree;
  * traces (\sum R(x));
  * two or more independent symmetric coefficients.

**Refuting output:** persistent rank defect with no current trichotomy tag.

**Confidence-increasing output:** for (\sigma=2), every irreducible
rank-defect component is one of the three proposed types, with an explicit
degree bound on (R).

The first serious theorem target should be (\sigma=2), not arbitrary
(\sigma).

---

## 4. Primitive occupancy/discrepancy with constant one

**Fragility:** high.

**Toy parameters:**

[
F_{17},\quad n=8,\quad k=4,\quad \sigma=2,3.
]

This is small enough to enumerate all syndrome points and all candidate affine
lines by deduplicating pairs of incidence points.

Medium random/extreme-value scan:

[
F_{97},\quad n=16,\quad k=8,\quad \sigma=3,4.
]

**Checker:** `enumerate_primitive_mca_lines.cpp`

* precompute all support spans;
* enumerate affine lines containing at least two incidence points;
* remove contained/envelope lines;
* tag all degree-(\leq3) block systems and low-image configuration
  characters;
* record the maximum remaining line count;
* compare against:
  [
  \left\lceil\binom n{k+\sigma}/q^{\sigma-1}\right\rceil+D
  ]
  for proposed floors (D=2r,4r,n).

**Refuting output:** a post-tagging line above the proposed finite bound.

**Confidence-increasing output:** the maximum residual tracks occupancy plus a
stable linear or square-root discrepancy across (q=17,97,193).

The experiment should estimate the right finite discrepancy shape before any
worker tries to prove (C_{\mathrm{occ}}=1).

---

## 5. Scalar circuit-cover trichotomy

**Fragility:** medium-high.

**Exact exhaustive parameters:**

[
F=\mathbb F_{17},\quad n=8,\quad k=4,\quad \sigma=1,2.
]

For (\sigma=2), enumerate every nonzero error vector of weight at most (2);
for (\sigma=1), weight at most (3). Bucket them by syndrome.

**Checker:** `enumerate_scalar_circuit_transversals.py`

For each syndrome:

1. construct every actual full-support list element;
2. construct the subspaces (W_P);
3. enumerate support-minimal circuits;
4. compute the exact minimum circuit hitting set by integer programming or
   exhaustive search;
5. classify every circuit by:

   * common core;
   * degree-(\leq3) split-rational profile;
   * low-affine-rank polynomial envelope;
   * product/configuration character.

**Refuting output:** a positive-excess circuit or a large minimum transversal
that has no current cover tag.

**Confidence-increasing output:** all unexplained circuits are configuration
character circuits and adding that branch produces the exact minimum hitting
number.

A second-stage sampled test should use

[
F_{97},\quad n=16,\quad k=8,\quad \sigma=2,3.
]

---

## 6. Lattès arithmetic and admissibility

**Fragility:** low-to-medium, but consequences are large.

### Degree (31)

Required checker output:

* (#E(\mathbb F_{8191})=8153=31\cdot263);
* order of the stated generator;
* the exact (31)-kernel polynomial;
* emitted Vélu map coefficients;
* fiber histogram
  [
  {31:131,16:1,1:4115};
  ]
* explicit degree-(18) field polynomial;
* explicit domain generator;
* denominator nonvanishing;
* final slope and collision count.

### Degree (113)

Required checker output:

* both curve orders;
* the degree-(113) kernel;
* image size (580);
* (144) free (C_4)-orbits;
* (113) distinct preimages per chosen value;
* emitted map and denominator coefficients;
* explicit degree-(15) field polynomial.

**Refuting output:** any mismatch in curve order, kernel size, fiber count,
pole avoidance, field generation, official rate, or collision exclusion.

**Confidence-increasing output:** agreement between a Sage implementation and
an independent finite-field implementation, both emitting the same certificate
hashes.

---

# PLAN: best next theorem-worker prompts

## Prompt 1 — exact official-rate product-character theorem

```text
Using experimental/notes/m1/cycle60_find_the_theorem_raw/
05_divisor_norm_character_counterpacket.md, prove or refute the following
official-rate specialization.

Let p=2^31-1, q=p^8, n=2^34, F=F_q, and let H<=F^* have
order n. For K in {n/2,n/4,n/8,n/16}, prove exact MCA and scalar-list
failure certificates at the reserves in the supplied Cycle-61 planning table.

Required proof components:
1. ord_n(p)=8 and H generates F;
2. exact product/high-coefficient bucketing;
3. exact full-support identity and support separation;
4. external-color extraction for MCA;
5. diagonal monomial equivalence from ev((X-beta)P_K) to standard RS[K];
6. direct standard-RS interpretation for the scalar list specialization;
7. exact integer comparison with floor(q/2^128);
8. proof that the listed reserve is maximal for this particular lower-bound
   formula.

Do not use floating-point numerics as the final certificate. Produce:
- a TeX theorem and proof;
- a standalone exact-integer or Robbins-bound script;
- a JSON certificate containing every parameter and inequality.

Acceptance:
all four rates certify >floor(q/2^128), and the next reserve fails the same
lower-bound test.

Failure:
identify the first incorrect algebraic, field-generation, floor, radius, or
code-equivalence step and give corrected parameters.
```

## Prompt 2 — kill equation (8) in degree two

```text
Prove or refute W-MCA-SPLIT-RATIONAL-CORE-REGISTRY, equation (8), already in
the degree-two involution family R_a(X)=X+a/X.

Work over:
- F_97 with an order-16 subgroup;
- F_193 with an order-32 subgroup;
- F_257 with an order-64 subgroup.

First prove that nonsquare a in H gives an exact pair partition by the
involution x -> a/x, and canonicalize these partitions modulo all allowed
domain and target equivalences.

Then search for one envelope-free affine syndrome line supporting rich
packets from many pairwise nonrefining R_a partitions.

Acceptance, counterexample route:
give one explicit code, line, support families and canonical partitions for
which the left/right ratio in equation (8) is n^{Omega(1)}.

Acceptance, proof route:
prove for this entire degree-two family that all partitions rich on one line
merge into O(polylog n) canonical core-residue systems or force a proper
hereditary envelope.

Failure:
if “rich,” “maximal” or “inequivalent” cannot be defined canonically, report
equation (8) as ill-posed and replace it with an exact statement.
```

## Prompt 3 — H2 defect versus configuration characters

```text
Audit and attempt to kill the Critical-seed H2-defect inverse, equation (19).

Part A: apply the general divisor-product packet symbolically and determine
exactly which hypothesis of equation (19) it violates. Do not accept
“split-rational” as an explanation unless an explicit map, partition or module
containing the packet is exhibited.

Part B: exhaustively test:
F_17, n=8, k=4, sigma=2 and 3;
F_97, n=16, k=8, sigma=2 and 3.

For every envelope-free line:
- compute minimal H2-defective subpackets;
- remove all degree-at-most-3 point-fiber packets;
- remove product and other low-image configuration-character packets;
- count residual critical-seed completions.

Acceptance, counterexample:
produce an explicit residual seed above
ceil(binomial(n,k+sigma)/q^(sigma-1))+2r.

Acceptance, theorem repair:
prove a sigma=2 statement in which every H2-defective seed is canonically
assigned to an envelope, a realized block system, a configuration character,
or an occupancy/discrepancy residue with a verified finite bound.

Failure:
a merely descriptive classification without a canonical assignment and total
line-level charge is not accepted.
```

## Prompt 4 — independent Lattès certificate

```text
Independently verify both Cycle-60 Lattès packets without reusing their
arithmetic assertions as assumptions.

For the degree-31 packet, emit:
- an explicit F_{8191^18} polynomial;
- curve orders and point orders;
- kernel and Velu map coefficients;
- the complete P^1(F_8191) fiber histogram;
- denominator, domain and collision certificates.

For the degree-113 packet, emit:
- an explicit F_{65537^15} polynomial;
- both curve orders;
- the CM endomorphism and kernel certificate;
- all 144 selected fiber values;
- the rational map and denominator;
- exact collision and field-generation checks.

Separately formalize:
1. three full subline fibers imply descent after target Mobius transformation;
2. the arithmetic Galois-closure split-fiber budget, with all constant-field
   and ramification hypotheses stated correctly.

Acceptance:
two independent implementations agree and the TeX theorem uses “at least,”
not “exactly,” where only a constructed subfamily is counted.

Failure:
give the smallest failed arithmetic or geometric claim and whether the packet
can be repaired.
```

## Prompt 5 — exhaustive scalar circuit transversal

```text
Solve the scalar full-support circuit-transversal problem completely for
F_17, n=8, k=4, at reserves sigma=1 and sigma=2.

Enumerate all actual nonzero-error representations, grouped by syndrome.
For each syndrome:
- construct W_P and the full-support circuit matroid;
- enumerate every support-minimal circuit;
- compute the exact minimum hitting number;
- perform exact common-core descent;
- tag degree-at-most-3 split-rational profiles;
- tag low-affine-rank envelopes;
- tag product/configuration-character profiles.

Deliver either:
A. an explicit untagged positive-excess circuit, disproving the proposed
   quotient/core/envelope cover; or
B. a complete machine-verifiable classification for this toy model and the
   exact hitting numbers.

Acceptance:
every reported circuit includes its supports, locator polynomials, syzygy
coefficients and classification certificate.

Failure:
raw padded-support multiplicities or nonminimal relations are not accepted.
```

## Prompt 6 — (\sigma=2), (t=1) apolar inverse theorem

```text
Work only on the first nontrivial case of
W-JR-T1-PRIMITIVE-APOLAR-SPLIT-NUMERATOR-INVERSE:
t=1 and sigma=2.

Using the apolar complete-intersection normal form I=(A,B), classify persistent
corank-one degeneracy on a separated full-coordinate split-locator family.

Desired conclusion:
after canonical common-envelope removal, either
1. the locators realize a point-fiber block system;
2. a nonconstant low-image configuration invariant is forced, with explicit
   form and degree bound; or
3. the family satisfies an explicit finite primitive second-moment bound.

Search explicitly for invariants not of norm form prod R(x), including traces,
other elementary symmetric coefficients and two-character combinations.

Acceptance, proof:
an exact algebraic theorem with canonical output, not a heuristic factorization.

Acceptance, counterexample:
an explicit finite family whose determinant vanishes persistently but has no
listed output.

Failure:
do not generalize to arbitrary sigma until the sigma=2 statement survives the
finite symbolic search.
```

---

# Verification and formalization plan

## Claims to verify first

The order should be:

1. **Exact-rate product-character specialization.**
   It can immediately strengthen the official failure ledger and may expose a
   missing scalar-list container.

2. **Cross-worker consistency between the divisor packet and H2 equation
   (19).**
   No H2 result should be promoted while this conflict remains unresolved.

3. **Lattès arithmetic and arithmetic Galois-closure wording.**
   The base arithmetic looks correct; the remaining risk is formal geometry
   and reproducibility.

4. **Fixed-partition and fixed-core injections.**
   These are likely bankable and form useful unconditional infrastructure.

5. **Hereditary MDS-3-core dependencies.**
   Independently check leaf peeling, Macaulay dimension counts, support
   thinning and the codimension-one seed construction.

6. **(t=1) apolar complete-intersection theorem.**
   Check degree conventions, direct-sum slices and the
   (\gcd(U,V)=1) full-coordinate criterion.

7. **Scalar circuit and projection theorems.**
   These appear sound, but should receive an independent proof before being
   used as the permanent list foundation.

## Scripts/checkers

| Script                                     | Purpose                                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------- |
| `cert_product_character_official.py`       | Exact four-rate MCA/list certificate and maximality under the construction |
| `verify_lattes31.sage`                     | Degree-31 field, curve, kernel, map, fibers and packet                     |
| `verify_lattes113.sage`                    | Degree-113 CM, kernel, fibers and packet                                   |
| `split_rational_registry_kill.py`          | (R_a=X+a/X) partition canonicalization and line co-occurrence              |
| `enumerate_primitive_mca_lines.cpp`        | Exhaustive (F_{17},n=8) MCA line scan                                      |
| `scan_h2_critical_seed.py`                 | H2 extraction, registry tagging and equation-(19) violations               |
| `search_configuration_invariants.sage`     | Elimination search for non-norm configuration invariants                   |
| `enumerate_scalar_circuit_transversals.py` | Exact toy scalar lists, circuits and hitting sets                          |
| `verify_t_gt_sigma_regression.py`          | Permanent regression against denominator-dependent claims                  |
| `finite_threshold_ledger.py`               | Integer safe/unsafe reserve and endpoint certificate                       |

Each certificate script should emit deterministic JSON and be checked by a
second implementation. Floating-point logarithms may be displayed but may not
be the proof object.

## TeX promotion policy

Promote only after independent review:

* denominator-free syndrome formulation;
* finite threshold and endpoint lemma;
* (t>\sigma) universal-chart route cut;
* fixed-partition QAR packing;
* fixed-core petal theorem;
* scalar circuit and projection theorems;
* (t=1) apolar normal form;
* exact-rate product-character theorem;
* Lattès packets after explicit field/map certificates.

Do **not** promote as theorems:

* equation (8);
* equation (19);
* the genus-(\geq2) discrepancy branch;
* the full divisor-norm trichotomy;
* a constant-one primitive occupancy bound;
* the global scalar circuit cover;
* claims that a Lattès construction gives exactly the constructed number of
  slopes.

---

# Resource allocation

## Round 1: verification and killing

Allocate the nine theorem workers as follows.

| Worker | Assignment                                                                                  |
| -----: | ------------------------------------------------------------------------------------------- |
|      1 | Exact-rate product-character theorem and finite certificate                                 |
|      2 | Degree-31 Lattès independent certificate                                                    |
|      3 | Degree-113 Lattès independent certificate                                                   |
|      4 | Degree-two split-rational registry kill test                                                |
|      5 | H2 equation-(19) versus configuration characters                                            |
|      6 | Exhaustive primitive MCA scan over (F_{17},n=8)                                             |
|      7 | Exhaustive scalar circuit-transversal scan                                                  |
|      8 | (t=1,\sigma=2) apolar/configuration symbolic classification                                 |
|      9 | Referee/integrator: dependency checks, finite floors, GRS invariance and certificate review |

The local Fable/Codex loop should:

* generate the finite-field implementations;
* run property-based checks;
* compare independent implementations;
* minimize counterexamples;
* emit exact JSON witnesses;
* reject any result lacking reproducible parameters.

It should not adjudicate the algebraic classification by itself.

## Human/PRZ priority

The first human checks should be:

1. the exact-rate product-character specialization;
2. whether the official-rate packets are absorbed by an existing block/module
   ledger;
3. the direct conflict between configuration characters and H2 equation (19);
4. the standard-RS/GRS invariance step;
5. the Lattès arithmetic-versus-geometric closure language.

These checks can materially alter the route board before another broad theorem
round.

## Round 2: default allocation after the kill round

Assuming the likely outcome—Lattès survives, equation (19) needs repair, and
equation (8) is at least underspecified—allocate:

| Workers | Assignment                                               |
| ------: | -------------------------------------------------------- |
|       2 | Configuration-character algebra and multi-character rank |
|       2 | Canonical line-level split-rational/block registry       |
|       1 | Post-structure H2/primitive discrepancy                  |
|       1 | Hereditary envelope termination and global charge        |
|       2 | Configuration-aware scalar circuit cover                 |
|       1 | Finite ledger, formalization and adversarial referee     |

Do not allocate workers to:

* standalone (t>\sigma) compression;
* a complete classification of all Lattès maps;
* generic high-genus Hasse–Weil estimates without a line-level registry;
* another seed-local completion lemma equivalent to the original full problem.

---

# CONDITIONAL

If the exact-rate product-character packets remain large after exhaustive
low-degree quotient, common-core and low-rank-module tagging, then
configuration characters are an **official-rate mandatory ledger term**.

If they are completely absorbed by a canonical existing module container,
then divisor norms should be treated as examples of that module theory rather
than as a separate additive ledger.

Either outcome is useful. What is not acceptable is leaving the classification
ambiguous while applying a primitive occupancy bound.

Likewise, if the Lattès certificates survive, the safe theorem must cover
their realized block systems. It does not necessarily need a complete
classification of genus-one rational maps.

---

# Route to a full solve

The full prize problem is not currently derivable from the existing named
walls. Two missing theories block it.

## MCA blocker

A canonical, bounded-overlap structure extractor for a whole affine syndrome
line is missing. It must unify:

* point-fiber block systems;
* Lattès and other split-rational systems;
* configuration-space determinant/norm characters;
* hereditary envelopes;
* module-level apolar degeneracies.

Only after that extractor exists is a “primitive discrepancy” theorem a
well-defined target.

The next exact safe-side lemma should be the restricted

[
\boxed{
\texttt{W-JR-T1-SIGMA2-CONFIGURATION-ALGEBRA-EXTRACTOR}.
}
]

Attempting the all-(\sigma) version now is too broad.

## List blocker

The scalar list problem needs a global hitting set for all low-arity
full-support circuits. A local classification of one circuit is insufficient;
overlap across cores, rational maps, envelopes and configuration modules is
the central difficulty.

That theorem is at least as hard as the MCA structure extractor and is not
automatically implied by it.

## Bottom line

The project is **plausibly solvable**, but the present route is medium-to-long
range and still missing hard inverse theorems. The immediate highest-value
result is the exact-rate product-character certificate. The immediate
highest-value safe-side work is the (\sigma=2,t=1) configuration-algebra
extractor plus the degree-two registry kill test. The separate
(t>\sigma), genus-classification-first and constant-one H2 routes should be
stopped.
