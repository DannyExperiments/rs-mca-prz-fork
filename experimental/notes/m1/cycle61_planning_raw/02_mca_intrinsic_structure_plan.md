# AUDIT — Executive verdict

The MCA safe-side problem is **not close**. The route is plausible only after substantial narrowing, and it is still missing three hard inverse theorems:

1. an intrinsic structured-extraction theorem for large envelope-free syndrome-line packets;
2. a worst-case primitive occupancy/discrepancy theorem;
3. a hereditary-envelope theorem controlling non-occupancy charges after shortening.

**Assessment**

| Question                                                                                  | Verdict           |             Confidence |
| ----------------------------------------------------------------------------------------- | ----------------- | ---------------------: |
| Is the denominator-free syndrome formulation correct?                                     | Yes               |          High, (>0.99) |
| Are all denominator degrees, including (t>\sigma), represented by it?                     | Yes               |                   High |
| Is the current quotient taxonomy sufficient?                                              | No                |                   High |
| Is the MCA safe side one lemma away?                                                      | No                |                   High |
| Is a solve plausible after route narrowing?                                               | Yes, medium-range | Moderate, about (0.55) |
| Is the current expanding “list every quotient mechanism” route likely to close by itself? | No                |                   High |
| Can the next two worker rounds plausibly finish the prize?                                | Unlikely          |                   High |

The central strategic problem is that every counterpacket currently enlarges the exception ledger: monomial quotients became split-rational quotients, then Lattès quotients, then divisor/configuration characters. Unless this is replaced by a single **structure-or-discrepancy theorem**, the taxonomy can expand indefinitely.

The genus-zero/genus-one classification is not the primary wall. It classifies a rational map **after a common map has been extracted**. The missing theorem is the extraction of a common intrinsic structure from a large packet on one syndrome line.

The scalar list branch is not addressed here beyond noting that nothing in this package supplies its missing scalar full-support theorem.

---

# PROOF — Exact finite MCA object

Let
[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,\qquad q=|F|,\qquad r=n-k,
]
and fix a reserve
[
\sigma\ge 1,\qquad a=k+\sigma,\qquad j=r-\sigma=n-a.
]

Choose an RS parity-check matrix (H\in F^{r\times n}), with column (h_x) at (x\in L), and write
[
V_T=\operatorname{span}_F{h_x:x\in T}.
]

For an affine syndrome line (\ell(z)=u+zv), define
[
\operatorname{Bad}_{\sigma}(\ell)
=================================

\left{
z\in F:
\exists T\in\binom Lj,\quad
u+zv\in V_T,\quad v\notin V_T
\right}.
]

Then the exact MCA numerator is
[
\boxed{
M_C(\sigma)=\max_{u,v\in F^r}
|\operatorname{Bad}_{\sigma}(u+Fv)|.
}
]

The support-wise MCA error at the grid radius
[
\delta_\sigma=\frac jn
=1-\frac{k+\sigma}{n}
]
is exactly
[
\boxed{
\epsilon_{\mathrm{mca}}(C,\delta_\sigma)=\frac{M_C(\sigma)}q.
}
]

The proof is the banked syndrome equivalence:

* agreement off (T) is equivalent to (u+zv\in V_T);
* simultaneous explainability of the whole word line on the same coordinates is equivalent to (v\in V_T);
* an error set of size (<j) can be padded to size exactly (j) while preserving (v\notin V_T), using the RS full-spark property.

Consequently, no denominator degree occurs in the exact theorem.

The exact target integer is
[
T_q=\left\lfloor \frac q{2^{128}}\right\rfloor,
]
and
[
\boxed{
\epsilon_{\mathrm{mca}}(C,\delta_\sigma)\le 2^{-128}
\iff
M_C(\sigma)\le T_q.
}
]

Moreover, (M_C(\sigma)) is nonincreasing in (\sigma).

Define
[
\sigma_C^*=\min{\sigma:M_C(\sigma)\le T_q}.
]

Then the largest safe **grid radius** is
[
\delta_{\mathrm{grid}}
======================

1-\frac{k+\sigma_C^*}{n}.
]

Under the paper’s definition
[
\delta_C^*=\sup{\delta:\epsilon_{\mathrm{mca}}(C,\delta)\le2^{-128}},
]
the exact supremum is
[
\boxed{
\delta_C^*
==========

1-\frac{k+\sigma_C^*-1}{n}.
}
]

That supremum is generally not attained: at the endpoint the integer agreement threshold drops from (k+\sigma_C^*) to (k+\sigma_C^*-1), which is unsafe by minimality. Thus “largest radius” and “supremal radius” must not be conflated.

Two field-regime facts also have to be frozen:

* If (q<2^{128}), then (T_q=0), while (M_C(r)=1); no radius is safe.
* If (q) is exponentially too large, for example (q\ge 2^{n+128}), the crude support union bound trivializes the challenge.

A rate alone therefore does not determine the finite threshold. The actual allowed sequence (q(n)), domain (L_n), and actual slope field must be part of the theorem.

---

# ROUTE_CUT — Do not create a separate (t>\sigma) theorem

The proposed universal compression
[
t>\sigma\quad\Longrightarrow\quad t'\le \sigma
]
is false.

Every syndrome line has noncanonical high-degree residue charts, and the Cycle 59 (t=3>\sigma=2) packet already kills simple compression. Denominator degree is therefore a chart variable, not a line-intrinsic stratum.

The safe-side theorem should be proved directly for (M_C(\sigma)). A result proved only for (t\le\sigma), or only for the balanced (t=\sigma) cloud, does not cover MCA.

The (t=1) apolar problem remains important because it is a necessary special case and a useful test laboratory. It is not currently a reduction of the general syndrome problem.

---

# BANKABLE_LEMMA — Arbitrary-defect packing for partial equal-fiber systems

This corrects the scope gap in the Cycle 60 fixed-partition theorem.

The result handles:

* arbitrary defect size (d);
* (M\nmid k);
* partial full-fiber systems with exceptional fibers or uncovered points;
* Lattès-style packets.

Let
[
\Pi={B_y:y\in\Omega}
]
be (N=|\Omega|) pairwise disjoint (M)-subsets of (L). They need not cover (L).

Let (Z_{\Pi,d,b}) be a set of distinct bad slopes on an envelope-free line. Suppose each (z\in Z_{\Pi,d,b}) has a selected agreement support
[
S_z=D_z\sqcup \bigcup_{y\in A_z}B_y,
]
where
[
|D_z|=d,\qquad A_z\in\binom{\Omega}{b},\qquad
D_z\cap\bigcup_{y\in A_z}B_y=\varnothing,
]
and
[
d+Mb=k+\sigma.
]

Put
[
h_0=\max{0,d-\sigma+1}.
]

Then, for every integer (h) with (h_0\le h\le d),
[
\boxed{
|Z_{\Pi,d,b}|\binom dh
\le
\binom Nb\binom{n-Mb}{h}.
}
]

Therefore
[
\boxed{
|Z_{\Pi,d,b}|
\le
W_\Pi(d,b)
:=
\min\left{
q,;
\min_{h_0\le h\le d}
\left\lfloor
\binom Nb
\frac{\binom{n-Mb}{h}}{\binom dh}
\right\rfloor
\right}.
}
]

## PROOF

For each (z), mark an (h)-subset (C\subseteq D_z) and consider
[
(z,C)\longmapsto (C,A_z).
]

Suppose two distinct slopes (z,z') map to the same ((C,A)). Their full-block portions are identical, while (C\subseteq D_z\cap D_{z'}). Hence
[
|S_z\setminus S_{z'}|
=====================

|D_z\setminus D_{z'}|
\le d-h
<\sigma.
]

Passing to complementary error supports (T_z=L\setminus S_z),
[
|T_z\cup T_{z'}|
================

j+|S_z\setminus S_{z'}|
<j+\sigma=r.
]

Because
[
u+zv\in V_{T_z},\qquad
u+z'v\in V_{T_{z'}},
]
the two distinct points span the syndrome plane:
[
\operatorname{span}(u,v)\subseteq V_{T_z\cup T_{z'}}.
]
This is a proper envelope, contradicting envelope-freeness. The map is therefore injective.

For each (A\in\binom{\Omega}{b}), the marked set (C) must lie outside the (Mb) selected block points, giving (\binom{n-Mb}{h}) possibilities. Counting both sides proves the inequality.

## Consequences

If (d<\sigma), take (h=0):
[
|Z_{\Pi,d,b}|\le \min\left{q,\binom Nb\right}.
]

Thus the degree-31 Lattès profile with a two-point defect is charged directly by its full-fiber profile (\binom{131}{67}), even though (31\nmid k) and most evaluation points lie in exceptional or non-full fibers.

If (d=\sigma), take (h=1):
[
|Z_{\Pi,\sigma,b}|
\le
\binom Nb\frac{n-Mb}{\sigma}.
]

When the blocks partition all of (L), this is exactly
[
\frac n\sigma\binom{N-1}{b},
]
recovering the Cycle 60 theorem.

This lemma solves the **per-fixed-block-system charge**. It does not solve how many incompatible block systems a single syndrome line can realize.

---

# BANKABLE_LEMMA — Occupancy is conserved under envelope shortening

Let a minimal envelope have domain (R\subseteq L), with
[
s=|R|=j+d<r.
]

The external-envelope shortening theorem sends a child descriptor to a code
[
\operatorname{RS}[F,R,h]
]
at the same reserve (\sigma). Its agreement size is (h+\sigma), and its external zero set (A\subseteq L\setminus R) has size (k-h).

The exact support counts satisfy
[
\boxed{
\sum_{h\in\mathbb Z}
\binom{n-s}{k-h}\binom{s}{h+\sigma}
===================================

\binom n{k+\sigma}.
}
]

This is just Vandermonde’s identity, or equivalently the partition of every ((k+\sigma))-point agreement support according to its intersection with (R).

External children have (h\ge1), so their sum is at most the right-hand side.

Consequently, if each child had a pure primitive estimate
[
C_{\mathrm{occ}}
\frac{\binom{s}{h+\sigma}}{q^{\sigma-1}},
]
then summing over every external descriptor (A) would cost at most
[
C_{\mathrm{occ}}
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}.
]

Thus the occupancy term itself is already hereditarily compatible.

## EXACT_NEW_WALL

The hereditary obstruction is entirely in the other terms:

* a polynomial or linear floor repeated once per child;
* quotient/configuration registry terms generated inside arbitrary punctures;
* H2-defective or tangent terms charged independently at every node.

A theorem of the form
[
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}+O(n)
]
cannot simply be applied to every child: the (O(n)) term explodes under branching.

This is why the Cycle 60 H2 bound is an extraction theorem, not a prize-solving hereditary estimate.

---

# EXACT_NEW_WALL — Minimal MCA theorem package

The logically smallest unknown ingredient is one uniform upper theorem for (M_C(\sigma)). The smallest modular package that appears realistically provable has three unknown modules.

Put
[
N_\sigma=\binom n{k+\sigma}=\binom nj.
]

## Theorem MCA-HER — Hereditary-envelope bound

Prove an explicit integer (E_C(\sigma)) such that every line contained in a proper column envelope satisfies
[
|\operatorname{Bad}_\sigma(\ell)|\le E_C(\sigma).
]

The theorem must include:

* the banked internal minimal-envelope cap;
* exact external shortening;
* occupancy amortization by the Vandermonde identity;
* a global, nonrepeated charge for tangent, leaf-peel, H2-defective and structured descendants.

The acceptance criterion is not merely termination of the shortening tree. It is an explicit bound on the **total tree weight with no hidden factor equal to the number of children**.

There are two viable formulations:

1. a direct parent-domain potential theorem, preferred because it preserves smooth-domain structure;
2. a uniform theorem over every arbitrary punctured RS descendant and every descendant rate.

The second is much stronger than the official four-rate problem because shortening leaves both the smooth-domain class and the set of official rates.

## Theorem MCA-STR — Intrinsic structured-registry theorem

For every envelope-free syndrome line, construct a canonical weighted cover of all structurally exceptional slopes by:

* partial split-rational block systems, including PGL(_2), subgroup-chain and Lattès/isogeny systems;
* bounded-complexity configuration-space fibers, including divisor norms;
* any further low-image invariant forced by the proof.

The total cover weight must satisfy
[
Q_C(\sigma)\le Q_{\mathrm{blk}}(\sigma)+Q_{\mathrm{cfg}}(\sigma)
]
for explicit integers.

For a fixed block system, the weight should use (W_\Pi(d,b)) above, not a count of rational-function formulas.

The required theorem is not “classify all rational maps.” It is:

> A large packet on one syndrome line either has a common intrinsic low-complexity structure whose weighted profile can be charged, or it passes to the primitive discrepancy theorem.

Necessary properties:

* invariant under postcomposition by (\operatorname{PGL}_2);
* invariant under changes of denominator chart;
* invariant under apolar generator shear in the (t=1) normal form;
* duplicate maps defining the same block system counted only once;
* no enumeration of all rational interpolants on (L).

## Theorem MCA-PRIM — Primitive occupancy/discrepancy theorem

After removing envelopes and the canonical structured cover, prove
[
\boxed{
|\operatorname{Bad}^{\mathrm{prim}}*\sigma(\ell)|
\le
\left\lceil
C*{\mathrm{occ}}
\frac{N_\sigma}{q^{\sigma-1}}
\right\rceil
+
D_C(\sigma),
}
]
with explicit (C_{\mathrm{occ}}) and (D_C(\sigma)).

The essential requirements are:

* worst-case over every affine syndrome line;
* counts distinct slopes, not support incidences;
* applies directly in syndrome space;
* (D_C(\sigma)) is globally chargeable under the hereditary theorem;
* no undefined “generic”, “primitive-looking”, or “random-like” hypothesis.

The H2 theorem and the (t=1) apolar theorem are inputs to this theorem, not substitutes for it.

## Combined finite bound

If the three theorems hold, then
[
\boxed{
M_C(\sigma)
\le
U_C(\sigma)
:=
\max\left{
E_C(\sigma),,
Q_C(\sigma)
+
\left\lceil
C_{\mathrm{occ}}
\frac{N_\sigma}{q^{\sigma-1}}
\right\rceil
+
D_C(\sigma)
\right}.
}
]

The exact finite safety certificate is
[
\boxed{
U_C(\sigma)\le
\left\lfloor\frac q{2^{128}}\right\rfloor.
}
]

No other denominator branch is needed.

---

# CONDITIONAL — Asymptotic versus finite requirements

## Asymptotic safe side

The asymptotic theorem only needs, at the proposed first safe reserve,
[
E_C(\sigma)+Q_C(\sigma)+D_C(\sigma)=o(q)
]
with enough quantitative decay to be below (2^{-128}q), and
[
C_{\mathrm{occ}}
\frac{N_\sigma}{q^\sigma}\le 2^{-128}-o(1).
]

Equivalently, define the occupancy reserve
[
\mathcal R_{\mathrm{occ}}(C,\sigma)
===================================

\sigma\log_2 q-\log_2\binom n{k+\sigma}.
]

The occupancy requirement is
[
\mathcal R_{\mathrm{occ}}(C,\sigma)
\ge
128+\log_2 C_{\mathrm{occ}}+o(1).
]

A matching lower theorem at (\sigma-1) then identifies the transition.

## Finite (2^{-128}) certificate

The finite theorem needs substantially more:

* exact (q), not a generated field or challenge field unless a transfer theorem is proved;
* exact ceilings and floors;
* an explicit canonical block/configuration registry;
* exact profile weights, including exceptional fibers and arbitrary defects;
* an exact hereditary potential;
* exact rational or integer (C_{\mathrm{occ}});
* a verified lower/failure inequality at the previous reserve.

No (n^{o(1)}), (O(n)), “bounded multiplicity”, or unquantified registry term is sufficient.

---

# Dependency DAG

```text
MCA PRIZE THRESHOLD
│
├── Exact threshold arithmetic                         [ALREADY BANKED]
│   ├── M_C(sigma) syndrome identity                   [ALREADY BANKED]
│   ├── exact-j padding                                [ALREADY BANKED]
│   ├── monotonicity in sigma                          [ALREADY BANKED]
│   └── floor(q/2^128) and endpoint convention         [ALREADY BANKED]
│
├── Failure at sigma*-1                                [BANKED/CONDITIONAL]
│   └── Bessel/random-anchor lower construction        [STRONG; field scope audit needed]
│
└── Safe side at sigma*
    │
    ├── MCA-HER hereditary-envelope theorem            [UNKNOWN]
    │   ├── close supports force envelope              [ALREADY BANKED]
    │   ├── minimal-envelope internal cap              [ALREADY BANKED]
    │   ├── external-envelope shortening               [LIKELY/BANKED PENDING REFEREE]
    │   ├── Vandermonde occupancy conservation         [BANKABLE_LEMMA HERE]
    │   └── non-occupancy hereditary potential         [UNKNOWN, HARD]
    │
    └── Envelope-free theorem                          [UNKNOWN]
        │
        ├── MCA-STR structured registry                [UNKNOWN, HARD]
        │   ├── fixed partial-block charge             [BANKABLE_LEMMA HERE]
        │   ├── fixed-core petal bound                 [LIKELY; special scope]
        │   ├── Lattès branch is necessary             [LIKELY; final verification pending]
        │   ├── intrinsic rich-structure extraction    [UNKNOWN, CENTRAL]
        │   ├── genus-0/1 classification after extract [LIKELY]
        │   ├── high-genus discrepancy                 [UNKNOWN]
        │   └── configuration-character cover          [UNKNOWN]
        │       └── corank-one norm trichotomy          [DOUBTFUL]
        │
        └── MCA-PRIM primitive discrepancy             [UNKNOWN, CENTRAL]
            ├── hereditary MDS-3-core extraction       [LIKELY; independent audit needed]
            ├── t=1 apolar CI normal form              [LIKELY; independent audit needed]
            ├── t=1 primitive color-image theorem      [UNKNOWN, HARD]
            └── global syndrome primitive theorem      [UNKNOWN, HARD]
```

## False nodes that should be deleted

```text
pure n^{1+o(1)} bound without occupancy                [FALSE]
pairwise sigma-separation implies a small packet       [FALSE]
point-fiber quotients are a complete ledger            [FALSE/TOO NARROW]
genus-zero quotient systems are a complete ledger      [FALSE]
universal t>sigma compression                          [FALSE]
critical-seed completion is a weaker t=1 theorem       [FALSE]
fixed-core QAR theorem covers arbitrary Lattès packets [FALSE]
all split-rational maps have n^{o(1)} total registry   [LIKELY FALSE AS STATED]
```

---

# COUNTERPACKET — What the existing examples actually prove

### Degree-31 Lattès packet

The core arithmetic is strongly supported:

* (p=8191);
* the proposed elliptic curve has (8153=31\cdot263) points;
* the degree-31 map has full-fiber distribution
  [
  31^{131},\quad16^1,\quad1^{4115};
  ]
* the packet uses (67) full fibers and a two-point defect;
* (\log_2\binom{131}{67}\approx127.11);
* the target numerator has about (106) bits;
* occupancy is negligible.

This kills a genus-zero-only or (M>\sigma)-only ledger if the remaining action-rank, no-envelope and admissibility checks pass. The degree-113 example is not needed to establish the logical route cut.

### Divisor-norm packet

The product character
[
T\longmapsto (-1)^j\prod_{x\in T}x
]
can save one syndrome condition and create a bucket a factor roughly (q/n) above raw occupancy.

This kills point-fiber-only primitive statements.

It does **not yet** establish that a divisor-character term is independently necessary at each official exact rate: the displayed finite instance is near, but not exactly, rate (1/8). An exact-rate adaptation or an official-rate counterpacket is still required.

### High-denominator packet

The (t=3>\sigma=2) packet kills universal compression but does not threaten the denominator-free formulation.

---

# EXACT_NEW_WALL — Best next exact research lemma

The decisive next wall is

```text
W-JR-T1-INTRINSIC-STRUCTURE-OR-OCCUPANCY
```

In the (t=1) apolar normal form, let
[
I_s=(A,B)
]
be the apolar complete intersection. In the envelope-free case, the lower generator degree satisfies (d\ge\sigma), and every relevant split locator lies in
[
(I_s)_j
=======

A,S_{j-d}\oplus B,S_{d-\sigma}.
]

The next theorem should classify the external-color image of the full-coordinate, (L)-split forms in this module.

A successful theorem must say:

> If the set of distinct external colors exceeds an explicit occupancy-plus-linear bound, then a quantitatively large subfamily is captured by one intrinsic split-rational block system or one bounded-complexity configuration-space low-image invariant, with an explicit profile charge.

The statement must be invariant under replacing the complete-intersection generators by
[
(A,B)\longmapsto (A,B+HA).
]

This is the best next target because:

* it is a necessary special case of the global theorem;
* it already contains point-fiber, Lattès-compatible and divisor-character phenomena;
* it is finite enough for exhaustive small-field testing;
* a counterexample would expose the next missing invariant before resources are spent on a global registry;
* a proof would supply the first genuine primitive inverse theorem in the project.

The global syndrome theorem and hereditary envelope theorem would still remain afterward.

---

# PLAN — Copy-ready theorem-worker prompts

## Prompt 1 — Referee and generalize the new block-packing lemma

```text
PROBLEM: W-MCA-PARTIAL-BLOCK-ARBITRARY-DEFECT-PACKING

Let C=RS[F,L,k], reserve sigma, and let ell be an envelope-free affine
syndrome line. Let Pi={B_y:y in Omega} be N pairwise disjoint M-subsets of L,
not necessarily covering L. Suppose each retained bad slope z has an agreement
support

S_z = D_z disjoint-union (union_{y in A_z} B_y),

with |D_z|=d, |A_z|=b, D_z disjoint from the selected blocks, and
d+Mb=k+sigma.

Prove or disprove that for every
h >= max(0,d-sigma+1),

|Z| binom(d,h) <= binom(N,b) binom(n-Mb,h).

Derive the optimized finite weight and all equality cases. Check that it
recovers the Cycle 60 fixed-partition theorem and applies to partial Lattes
full-fiber systems.

ACCEPTANCE:
- a complete proof using only transversality and envelope-freeness;
- partial block systems and exceptional points are handled;
- no M|k assumption;
- exact integer floors are stated;
- an exhaustive checker verifies all q<=11 feasible cases.

FAILURE:
- an explicit RS line and support packet violating the inequality, including
  full field/domain/line/support data.
```

## Prompt 2 — Hereditary non-occupancy potential

```text
PROBLEM: W-MCA-HEREDITARY-NONOCCUPANCY-POTENTIAL

Use the exact external-envelope shortening theorem. For a minimal envelope
R of size s, external children are indexed by h>=1 and A subset L\R with
|A|=k-h, and the child is RS[F,R,h] at reserve sigma.

The occupancy terms satisfy the exact Vandermonde conservation law

sum_h binom(n-s,k-h) binom(s,h+sigma) = binom(n,k+sigma).

Construct an explicit nonnegative potential Phi on the original line and all
shortening nodes such that:

internal_cap(node) + sum_children Phi(child) <= Phi(node),

and Phi(root) is o(q), or give a counterexample showing that no potential
depending only on node parameters and the known H2/quotient charges can work.

ACCEPTANCE:
- no multiplication by the number of nonempty children;
- arbitrary punctured descendants are covered;
- tangent/leaf/H2 and structured charges are included;
- exact finite constants are given;
- the recurrence terminates and proves an explicit E_C(sigma).

FAILURE:
- an explicit finite shortening tree whose minimum canonical charge exceeds
  every proposed parameter-only potential by a superpolynomial factor.
```

## Prompt 3 — (t=1) apolar primitive inverse

```text
PROBLEM: W-JR-T1-INTRINSIC-STRUCTURE-OR-OCCUPANCY

Assume the Cycle 60 t=1 apolar complete-intersection normal form. Work with an
envelope-free syndrome, so the lower generator degree d satisfies d>=sigma.
The split locators are full-coordinate degree-j forms

P = A U + B V

in A*S_{j-d} + B*S_{d-sigma}, with the external evaluation color at beta.

Prove an explicit finite structure-or-discrepancy theorem for the set of
distinct colors, or construct a counterpacket.

A positive theorem must show that a color set larger than

ceil(C_occ binom(n,j)/q^(sigma-1)) + P(n,sigma)

contains a quantitatively large subfamily captured by either:
(1) one intrinsic split-rational full-block system, or
(2) one bounded-complexity low-image function on the split-locator
    configuration space.

The theorem must be invariant under complete-intersection generator shear.

ACCEPTANCE:
- explicit C_occ and P;
- exact definitions of both structure alternatives;
- a finite weighted charge for the extracted container;
- no genericity assumptions;
- counts distinct colors, not locators or supports.

FAILURE:
- an explicit field, domain, apolar CI, split locators and distinct colors
  beating the bound while clearing common factors, known block systems,
  known divisor norms and the H2-primitive test.
```

## Prompt 4 — Intrinsic rich split-rational extraction

```text
PROBLEM: W-MCA-RICH-SPLIT-RATIONAL-EXTRACTION

Let an envelope-free syndrome line have a large selected family of agreement
supports. Prove or disprove that if many supports admit representations by
full fibers of degree-M rational maps, then a positive fraction of those
supports use one common block system intrinsically determined by the locator
module.

The extracted object must be the block system, not a rational-function
formula or denominator action rank.

ACCEPTANCE:
- invariance under postcomposition by PGL2 and change of denominator chart;
- a quantitative richness threshold;
- a bound on the minimum weighted cover by distinct block systems;
- Lattes systems at M=sigma are included;
- high-degree interpolation maps cannot make the conclusion vacuous.

FAILURE:
- a single envelope-free line realizing many pairwise incompatible rich block
  systems whose minimum weighted cover exceeds the proposed bound.
```

## Prompt 5 — Corank-one configuration classification

```text
PROBLEM: W-JR-CORANK-ONE-CONFIGURATION-INVARIANT-CLASSIFICATION

In the t=1 apolar normal form, classify all corank-one degeneracies that save
one independent syndrome condition on a large family of L-split locators.

Test the proposed alternatives:
- common split factor/envelope;
- point-fiber quotient;
- divisor-norm/configuration character.

Prove the trichotomy with exact hypotheses, or produce a fourth mechanism.

ACCEPTANCE:
- classification is invariant under apolar generator shear;
- every determinant/minor degeneracy is accounted for;
- each alternative yields an explicit finite container weight;
- no use of a chosen denominator chart.

FAILURE:
- an explicit low-image invariant or packet not equivalent to any of the three
  alternatives.
```

## Prompt 6 — Complete verification of the degree-31 Lattès packet

```text
PROBLEM: VERIFY-MCA-LATTES31-Counterpacket

Independently reconstruct the entire degree-31 packet from raw finite-field
data.

Verify:
1. field and domain admissibility;
2. elliptic curve order and subgroup;
3. the Velu isogeny and induced rational map;
4. exact full-fiber histogram;
5. every selected agreement support;
6. distinct slope colors;
7. transversality;
8. absence of a proper common envelope;
9. claimed denominator/action-rank exclusions;
10. exact comparison with floor(q/2^128) and the occupancy term.

ACCEPTANCE:
- a deterministic script emitting a machine-readable certificate and a short
  formal proof of each algebraic implication.

FAILURE:
- identify the first incorrect arithmetic, admissibility, transversality,
  envelope or exclusion claim.
```

---

# COUNTERPACKET — Kill tests

| Proposed statement                                             | Fast falsification test                                                                                                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Every H2-defective packet is quotient/configuration structured | Enumerate (q\le13), (n\le8); find H2-defective packets with no degree-(\le4) block system or norm character                                 |
| Corank-one degeneracy has only three mechanisms                | Enumerate small apolar complete intersections and compute all low-image minors under generator shear                                        |
| Primitive occupancy holds with (C_{\mathrm{occ}}=1)            | Compute exact color images after known-container removal and maximize the ratio to (N_\sigma/q^{\sigma-1})                                  |
| A parameter-only hereditary potential is polynomial            | Build all minimal-envelope shortening trees for (q\le11); optimize canonical child assignments and measure charge growth                    |
| Split-rational registries have (n^{o(1)}) total weight         | Enumerate degree-2 and degree-3 maps on (\mathbf P^1(F_q)), quotient by identical block systems, and solve the minimum weighted set cover   |
| Divisor norms are required at exact rate (1/8)                 | Redo the restricted-product DP with (k=n/8) exactly and test all official domain constraints                                                |
| The fixed-core theorem handles Lattès packets                  | Check (M\mid k), full-domain equipartition, and existence of a (k)-point union of full fibers; the degree-31 packet fails these assumptions |
| (t=1) solves all denominator degrees                           | Run the known (F_{17}), (t=3,\sigma=2) packet through any proposed reduction                                                                |

Recommended toy regimes:

[
F_7,F_{11},F_{13},F_{17},\qquad n\le 8,
]
with exact rates where possible. The (F_7,n=6,k=1,j=3) envelope configuration is a useful first hereditary stress case.

---

# AUDIT — Verification and formalization order

## Verify first

1. Exact syndrome equivalence, exact-(j) padding, monotonicity and the real-radius endpoint convention.
2. External-envelope shortening in both directions, including transversality.
3. The arbitrary-defect partial-block lemma above.
4. The Vandermonde occupancy conservation identity and its use in the shortening ledger.
5. The degree-31 Lattès packet.
6. The H2 theorem:

   * leaf peel loses at most (n) slopes;
   * common-root stripping preserves the correct packet;
   * the locator matrix is basepoint-free;
   * the bundle splitting and Macaulay excess formula have the claimed shifts.
7. The (t=1) apolar theorem:

   * generator degrees;
   * envelope dichotomy;
   * direct-sum slice;
   * full-coordinate criterion (\gcd(U,V)=1);
   * invariance under generator shear.
8. The divisor-character packet, especially exact-rate relevance.

## Scripts to write

```text
verify_mca_exact_object.py
enumerate_mca_lines.py
verify_envelope_shortening.py
verify_partial_block_packing.py
verify_envelope_vandermonde.py
verify_h2_core.py
verify_t1_apolar.py
verify_lattes31.py
search_configuration_characters.py
registry_weighted_set_cover.py
mca_finite_certificate.py
```

The finite certificate script should use integer arithmetic only and emit:

* (q,n,k,\sigma,j);
* (T_q);
* exact binomial values;
* every block/configuration profile weight;
* hereditary potential;
* primitive numerator bound;
* the final comparison (U_C(\sigma)\le T_q);
* the lower comparison at (\sigma-1).

## Promote to TeX after review

Promotable now or after one referee pass:

* exact denominator-free (M_C(\sigma));
* exact-(j) padding;
* monotonicity and the threshold convention;
* close-support envelope lemma;
* arbitrary-defect partial-block packing;
* occupancy conservation under shortening.

Promote only after independent algebraic review:

* external-envelope shortening;
* fixed-core petal theorem, with its divisibility scope explicit;
* H2 extraction;
* (t=1) apolar normal form;
* degree-31 Lattès counterpacket.

Do not promote as theorems:

* the degree-113 packet before independent reconstruction;
* the corank-one trichotomy;
* a global split-rational registry bound;
* higher-genus discrepancy;
* any implication from (t=1) to all denominator degrees;
* official-rate necessity of divisor characters before an exact-rate packet.

---

# PLAN — Resource allocation

## Round 1: verification and decisive kill tests

| Worker | Assignment                                                                    |
| -----: | ----------------------------------------------------------------------------- |
|      1 | Exact finite object, endpoint convention, integer certificate skeleton        |
|      2 | Referee/formalize partial-block arbitrary-defect packing                      |
|      3 | Full degree-31 Lattès reconstruction                                          |
|      4 | Independent referee of H2 extraction                                          |
|      5 | Independent referee and computational atlas for (t=1) apolar form             |
|      6 | Search for (t=1) primitive counterpackets                                     |
|      7 | Hereditary-envelope potential: proof or explicit branching obstruction        |
|      8 | Exact-rate divisor-character adaptation and corank-one kill search            |
|      9 | Rich split-rational extraction and small-field registry set-cover experiments |

The local Fable/Codex loop should maintain one shared exact-arithmetic data format for:

* fields and domains;
* parity-check matrices;
* canonical affine lines;
* support witnesses;
* envelope certificates;
* block systems;
* configuration invariants;
* apolar ideals;
* machine-readable theorem certificates.

## Round 2 if the (t=1) target survives

* Three workers: independent proof attacks on the (t=1) structure-or-occupancy theorem:

  * apolar/commutative algebra;
  * additive-combinatorial/Fourier;
  * algebraic-geometric incidence.
* Two workers: intrinsic block/configuration extraction.
* One worker: hereditary potential.
* One worker: translation back to the global syndrome formulation.
* One worker: exact constants and finite ledger.
* One worker: adversarial referee and counterexample search.

## Round 2 if a new (t=1) counterpacket appears

* Three workers: isolate and classify the new invariant.
* Two workers: determine whether it is a block system, configuration character or genuinely new mechanism.
* Two workers: redesign and stress-test the primitive definition.
* One worker: preserve the hereditary-envelope lane.
* One worker: update the finite ledger and route board.

## Human/PRZ priority

The human review should check, in this order:

1. the exact allowed field/domain growth regime;
2. the supremum-versus-attained-radius convention;
3. the complete degree-31 Lattès certificate;
4. the H2 bundle/Macaulay argument;
5. the (t=1) apolar normal form;
6. the definition of “intrinsic structured container” before any broad registry proof begins.

The degree-113 packet and a general genus taxonomy should not be the first human priority.

---

# PLAN — Route to a full MCA solve

1. Freeze the exact syndrome object and finite threshold convention.
2. Bank the partial-block arbitrary-defect theorem and occupancy-conservation identity.
3. Verify H2, (t=1) apolar and degree-31 Lattès claims.
4. Resolve the (t=1) structure-or-occupancy wall.
5. Use what survives to formulate the intrinsic global structured-extraction theorem.
6. Prove the denominator-free primitive discrepancy theorem.
7. Prove a hereditary potential that amortizes every non-occupancy term over arbitrary shortening.
8. Build the exact integer ledger at each reserve.
9. Find the first (\sigma) with (U_C(\sigma)\le T_q).
10. Combine with the lower/failure theorem at (\sigma-1) to certify the exact transition.

The route is blocked not by denominator bookkeeping, and not by incomplete genus classification. It is blocked by the absence of a theorem converting a **large finite split-locator packet on one syndrome line** into either a bounded-weight intrinsic structure or a sharp occupancy estimate.
