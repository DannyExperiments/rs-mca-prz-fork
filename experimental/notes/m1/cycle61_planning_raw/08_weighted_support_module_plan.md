# Executive verdict

**AUDIT**

The full prize problem is not close to solved. The repository has a strong lower/failure theory, several exact reductions, and materially better normal forms, but it still lacks the inverse/container theorems that would produce a safe-side result.

| Question                                                                        | Verdict                                                                            |         Confidence |
| ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -----------------: |
| Is the current mathematical language basically right?                           | Yes: syndrome transverse secants for MCA; full-support circuits for lists          |         High, 0.90 |
| Is the MCA challenge plausibly solvable along a narrowed version of this route? | Yes, but only with new inverse theory                                              |     Moderate, 0.55 |
| Is the scalar/list challenge plausibly solvable from the current circuit route? | Possibly, but the global hitting theorem may be as hard as the MCA inverse theorem | Moderate-low, 0.35 |
| Is either challenge one or two lemmas from completion?                          | No                                                                                 |         High, 0.95 |
| Can the four rates have four universal numerical radii?                         | No. The finite answer is code- and domain-specific                                 |         High, 0.98 |

The exact answer must depend on (n,q,k), the generated and line fields, the actual smooth domain, divisibility data, active block systems, configuration-space packets, and finite rounding. A rate-only table cannot solve the official finite problem.

**ROUTE_CUT**

The expanding genus-zero/genus-one/higher-genus quotient ledger is not a viable primary organization of the upper theorem. It classifies possible maps, not the total number or overlap of support families realized on one syndrome line. It also does not cover configuration-space characters.

Genus should be certificate metadata for a support container, not the definition of the master container theorem.

**ROUTE_CUT**

The proposed corank-one trichotomy

[
\text{envelope}\quad\text{or}\quad
\text{point-fiber quotient}\quad\text{or}\quad
\text{one divisor-norm character}
]

is probably false or at least badly under-specified. Multiple independent symmetric invariants, additive configuration invariants, determinantal or Plücker-type invariants, and higher-rank split-numerator modules can save conditions. Building an ever-growing explicit exception ledger is unlikely to terminate.

**EXACT_NEW_WALL**

The correct central MCA wall is:

[
\boxed{
\text{a puncture-hereditary, line-intrinsic,
weighted support-module cover theorem}
}
]

together with a primitive discrepancy theorem for the complement.

This has two genuinely hard components:

1. A global weighted registry theorem that bounds the total support-profile weight across all structured containers on one line, rather than proving a bound separately for each map.
2. A primitive inverse theorem for the residual split-locator family after that registry and all proper envelopes have been removed.

There is an additional load-bearing issue not sufficiently isolated in the route board:

**EXACT_NEW_WALL — hereditary puncture closure.** Envelope shortening and list common-core descent produce arbitrary punctured domains. A theorem proved only for multiplicative cosets or other original smooth domains cannot simply be invoked recursively on those children. Either the master theorem must hold for the full descendant class, or the descendants must be charged without reapplying the smooth-domain theorem. Without this, the hereditary induction is circular.

# A bankable aggregation lemma

**PROOF — BANKABLE_LEMMA**

The information-set petal argument gives a slightly stronger and cleaner aggregation statement than summing separately over rational maps.

### Structured-core registry lemma

Let (C=\operatorname{RS}[F,L,k]), (r=n-k), and let (\ell(z)=u+zv) be an affine syndrome line contained in no proper column envelope. Let

[
\mathfrak U\subseteq \binom{L}{k}
]

be any finite family of certified (k)-point cores. Suppose that, for every (z) in a set (Z), there is a selected core (U_z\in\mathfrak U) and a codeword agreeing with the corresponding word on (U_z) and on at least (s) further coordinates.

Then

[
\boxed{
|Z|
\le
\min\left{
|F|,
\left\lfloor\frac r s\right\rfloor |\mathfrak U|
\right}.
}
]

### Proof

Assign each slope to one selected core. For a fixed (U), the extra-agreement petals for distinct slopes are pairwise disjoint on an envelope-free line, so at most (\lfloor r/s\rfloor) slopes can be assigned to (U). Sum over the distinct cores in (\mathfrak U).

### Consequence

For point-fiber structures, one should deduplicate rational maps by the actual (k)-cores or block partitions they induce:

[
\left|
\bigcup_{\Pi} Z_\Pi
\right|
\le
\left\lfloor\frac r s\right\rfloor
\left|
\bigcup_{\Pi}\mathfrak U_\Pi
\right|.
]

The correct structural quantity is therefore the entropy of the union of realized core families, not the number of formulas for rational maps. Lattès maps matter only when they create genuinely new support systems.

This does not solve the quotient wall: the union of admissible cores may still be enormous. It does identify the quantity that a global registry theorem must bound.

# Minimal theorem package

## MCA challenge

There is a distinction between the smallest logically sufficient black box and the smallest realistic proof package.

### Logical black-box minimum

One finite theorem giving an explicit upper bound for every affine syndrome line, one adjacent-reserve failure certificate, and the exact threshold-extraction lemma would suffice.

That formulation hides all the hard mathematics. The smallest realistic package has three open upper-side modules.

### Banked spine

Let

[
r=n-k,\qquad a=k+\sigma,\qquad j=r-\sigma,
\qquad T_q=\left\lfloor\frac q{2^{128}}\right\rfloor .
]

Define

[
M_C(\sigma)=
\max_{\ell(z)=u+zv}
\left|
\left{
z:
\exists T\in\binom Lj,\
\ell(z)\in V_T,\
v\notin V_T
\right}
\right|.
]

The following infrastructure is already banked or very close to banked:

1. Syndrome/transverse-secant equivalence.
2. Exact-(j) padding for RS parity-check columns.
3. Monotonicity in the radius.
4. The same-field Bessel–Paley lower theorem.
5. Exact common-envelope shortening identities.
6. Fixed-core petal bounds.
7. The reserve-sized-defect fixed-partition packing argument.

### Open MCA theorem A: weighted support-module registry

For every envelope-free syndrome line, construct a canonical registry of structured support families with total weight

[
W_{\mathrm{mod}}(C,\sigma,\ell)
]

and prove an explicit uniform bound

[
W_{\mathrm{mod}}(C,\sigma,\ell)
\le Q_{\mathrm{mod}}(C,\sigma).
]

The registry must be defined on support families or split-numerator modules, not on one chosen denominator or one chosen rational ratio. It must include, without separate ad hoc theorem statements:

* equal-fiber block systems induced by split-rational maps;
* projective and subgroup-chain block systems;
* Lattès/isogeny block systems;
* fixed-defect and mixed-profile block systems;
* configuration-space or divisor-character modules;
* generator changes in apolar complete intersections;
* low-affine-rank support modules.

The theorem must bound the total registry weight on one line. Per-map Hasse–Weil estimates do not suffice.

### Open MCA theorem B: primitive transverse-secant discrepancy

After removing the fixed registry and all proper envelopes, prove

[
\boxed{
|\operatorname{Bad}^{\mathrm{prim}}*\sigma(\ell)|
\le
\left\lceil
C*{\mathrm{occ}}
\frac{\binom nj}{q^{\sigma-1}}
\right\rceil
+
D_{\mathrm{prim}}(n,k,\sigma)
}
]

with explicit constants.

This theorem must cover every denominator presentation because it is stated in syndrome space. The (t=1) apolar theorem and the hereditary three-core theorem are normal forms feeding this inverse theorem; neither is presently a bound on the primitive complement.

### Open MCA theorem C: hereditary envelope induction

For an enveloped line, prove a finite recurrence for the canonical shortening tree and bound its total contribution by

[
E_{\mathrm{her}}(C,\sigma).
]

The theorem must be uniform over every punctured descendant produced by the recurrence. Termination alone is not enough; total branching and child weights must be controlled.

### Resulting finite upper bound

The three modules should imply

[
\boxed{
M_C(\sigma)
\le
U_{\mathrm{MCA}}(C,\sigma)
:=
\max\left{
E_{\mathrm{her}},
\left\lceil
C_{\mathrm{occ}}
\frac{\binom nj}{q^{\sigma-1}}
\right\rceil
+
Q_{\mathrm{mod}}
+
D_{\mathrm{prim}}
\right}.
}
]

Safety is certified by

[
U_{\mathrm{MCA}}(C,\sigma)\le T_q.
]

### Matching lower/failure package

At the preceding reserve (\sigma-1), one needs a verified witness or lower theorem giving more than (T_q) slopes. The finite lower certificate may be

[
B_{\mathrm{prev}}
=================

\max{
B_{\mathrm{BP}},
B_{\mathrm{quot}},
B_{\mathrm{proj}},
B_{\mathrm{Latt\grave es}},
B_{\mathrm{config}},
B_{\mathrm{explicit}}
}>T_q.
]

The Bessel–Paley theorem is strong in the entropy branch but does not automatically match every structural floor. Exact determination is therefore necessarily certificate-based unless a new lower-completeness theorem is proved.

## List challenge

The interleaved part is essentially closed at the official same-field scale. The remaining problem is scalar.

Define

[
L_C(\sigma)
===========

\max_{s\in F^r}
\sum_{e=0}^{r-\sigma}\nu_e^\circ(s).
]

The banked reductions give:

[
L_C(\sigma)
\le
U_{\mathrm{hit}}(C,\sigma)
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor ,
]

where (U_{\mathrm{hit}}) is the size of a set meeting every full-support circuit of arity at most

[
\ell_\sigma=\left\lceil\frac r\sigma\right\rceil .
]

### Open list theorem: hereditary low-arity circuit hitting

For every scalar syndrome (s), construct a canonical hitting set (Z_s) meeting all full-support circuits of arity at most (\ell_\sigma), with

[
\boxed{
|Z_s|
\le
T_q-\left\lfloor\frac{r-1}{\sigma}\right\rfloor .
}
]

The hitting set must charge circuits through:

* exact common-core descent;
* split-rational block systems and their full support profiles;
* low-affine-rank polynomial envelopes;
* configuration or split-numerator modules;
* a bounded primitive circuit registry.

A classification of each circuit separately is insufficient. The theorem must output one globally bounded hitting set.

The same puncture-heredity issue appears here: removing a common agreement core replaces the original smooth domain by an arbitrary puncture.

### Matching list failure

At (\sigma-1), one needs an actual scalar list of more than (T_q) codewords. Entropy and quotient-core bounds supply many cases, but an adjacent-reserve witness is still a code-specific obligation.

## Asymptotic versus finite requirements

| Requirement         | Asymptotic theorem                          | Finite (2^{-128}) certificate                           |
| ------------------- | ------------------------------------------- | ------------------------------------------------------- |
| Occupancy           | Correct exponent and uniform (o(q)) control | Exact binomial and field-power integer bounds           |
| Structured families | Subexponential or (o(q)) total profile      | Exact registry and exact profile sum                    |
| Primitive remainder | (o(q)), uniformly over lines                | Explicit (C_{\mathrm{occ}}) and (D_{\mathrm{prim}})     |
| Heredity            | Uniform closure under descendants           | Explicit branching recurrence and total                 |
| List circuits       | (U_{\mathrm{hit}}=o(q))                     | (U_{\mathrm{hit}}\le T_q-\lfloor(r-1)/\sigma\rfloor)    |
| Failure             | Correct reserve scale                       | More than (T_q) explicit slopes/codewords at (\sigma-1) |
| Radius              | Leading-order reserve                       | Floors, endpoint, and monotonicity                      |

An (n^{o(1)}) statement is not a finite prize certificate. Under the official caps, a hidden constant or a factor of (n) can consume the entire 128-bit margin.

# Threshold convention

**BANKABLE_LEMMA**

Let

[
\widehat\sigma_{\mathrm{MCA}}
=============================

\min{\sigma:M_C(\sigma)\le T_q},
]

and similarly for lists. If safety holds at (\widehat\sigma) and failure is proved at (\widehat\sigma-1), then:

* the largest safe grid radius is

[
\delta_{\mathrm{grid}}
======================

# \frac{r-\widehat\sigma}{n}

1-\rho-\frac{\widehat\sigma}{n};
]

* the supremal real transition is

[
\boxed{
\delta_C^*
==========

1-\rho-\frac{\widehat\sigma-1}{n},
}
]

with the endpoint itself unsafe under the standard (\lfloor n\delta\rfloor) convention.

The papers must not call the latter an attained “largest radius” unless the endpoint convention has been changed.

# Dependency DAG

Status meanings:

* **already banked**: theorem-grade or previously audited exact infrastructure;
* **likely**: self-contained proof appears sound but has not passed independent line review;
* **doubtful**: plausible formulation is probably incomplete or false;
* **false**: killed by a known route cut or counterpacket;
* **unknown**: no proof or counterexample.

```text
MCA-PRIZE-THRESHOLD [unknown]
├── MCA-EXACT-REDUCTION-AND-MONOTONICITY [already banked]
│   ├── syndrome/transverse-secant equivalence [already banked]
│   ├── exact-j padding lemma [already banked]
│   └── grid/supremal threshold extraction [likely]
│
├── MCA-SAFE-UPPER [unknown]
│   ├── ENVELOPE-FREE-MASTER [unknown]
│   │   ├── WEIGHTED-SUPPORT-MODULE-REGISTRY [unknown]
│   │   │   ├── fixed-core petal theorem [likely]
│   │   │   ├── reserve-defect fixed-partition packing [likely]
│   │   │   ├── exact fixed-container profile charge [likely]
│   │   │   ├── projective/split-rational block recognition [likely]
│   │   │   ├── Lattès-113 packet and registry entry [unknown]
│   │   │   ├── divisor/configuration packet and registry entry [unknown]
│   │   │   ├── total-weight/overlap theorem [unknown]
│   │   │   └── genus taxonomy alone implies global cover [false]
│   │   │
│   │   └── PRIMITIVE-DISCREPANCY [unknown]
│   │       ├── split-locator syzygy-excess formula [likely]
│   │       ├── hereditary MDS three-core extraction [likely, wording repair]
│   │       ├── t=1 apolar complete-intersection normal form [likely]
│   │       ├── H2-defect charge theorem [unknown]
│   │       ├── t=1 split-numerator inverse [unknown]
│   │       ├── general 1<t<sigma level-algebra inverse [unknown]
│   │       └── exact three-outcome configuration trichotomy [doubtful]
│   │
│   └── HEREDITARY-ENVELOPE-INDUCTION [unknown]
│       ├── exact shortening identity [already banked]
│       ├── tree termination [already banked]
│       ├── closure over arbitrary punctures [unknown]
│       └── total branching/weight bound [unknown]
│
├── MCA-PREVIOUS-RESERVE-FAILURE [conditional]
│   ├── same-field Bessel–Paley lower theorem [already banked]
│   ├── monomial/projective quotient packets [already banked or likely]
│   ├── Lattès-113 finite packet [unknown pending verification]
│   ├── divisor-norm finite packet [unknown pending verification]
│   └── adjacent-reserve completeness [unknown]
│
└── MCA-FINITE-CERTIFICATE-COMPILER [likely engineering]
    ├── exact integer arithmetic [likely]
    ├── field-ledger validation [likely]
    ├── endpoint checker [likely]
    └── proof/certificate hash verification [likely]
```

```text
LIST-PRIZE-THRESHOLD [unknown]
├── scalar full-support identity [likely]
├── prize-scale interleaving projection [likely]
├── full-support circuit reduction [likely]
│
├── GLOBAL-LOW-ARITY-CIRCUIT-HITTING [unknown]
│   ├── common-core shortening identity [likely]
│   ├── fixed split-rational support-profile charge [likely]
│   ├── low-affine-rank envelope classification [unknown]
│   ├── primitive circuit inverse theorem [unknown]
│   ├── global overlap/hitting-set theorem [unknown]
│   └── puncture-hereditary closure [unknown]
│
├── previous-reserve actual-list witness [conditional]
└── finite threshold compiler [likely engineering]
```

Known false nodes should remain explicitly recorded:

```text
pure n^{1+o(1)} upper bound without occupancy                 [false]
balanced t=sigma theorem suffices for full MCA               [false]
general t>sigma compression to t<=sigma                      [false]
monomial action rank is a complete quotient ledger           [false]
point-fiber quotients are a complete JR ledger               [false]
critical-seed completion is a weaker problem                 [false]
d_R(E) is a canonical denominator-free container             [false]
quotient plus common core suffices for general scalar lists  [false]
per-map Hasse–Weil bounds imply a global line cover           [false]
```

# Best next six theorem-worker prompts

## Prompt 1 — exact finite spine formalization

```text
W-FOUNDATION-EXACT-SPINE-FORMALIZATION

No Internet. Work only from the attached RS-MCA repository.

Produce a standalone TeX proof note containing exact, fully quantified
statements and proofs of the following:

1. syndrome/transverse-secant equivalence for RS MCA;
2. exact-j padding while preserving transversality;
3. monotonicity and grid-versus-supremal threshold extraction;
4. the information-set petal theorem;
5. the fixed-partition packing theorem, explicitly restricted to the
   reserve-sized-defect hypotheses under which its injection is valid;
6. the scalar full-support identity;
7. the full-support circuit transversal theorem, carefully distinguishing
   an all-circuit transversal from a low-arity transversal;
8. the prize-scale interleaving projection theorem.

Do not import any Cycle 60 claim as proved merely because it is labelled
BANKABLE_LEMMA. State every field, support-size, transversality, full-support,
and zero-syndrome exception.

Acceptance criteria:
- a compilable standalone TeX file;
- no dependence on an unproved structural theorem;
- exact floor/ceiling formulas;
- a dependency table;
- exhaustive small checks over F_7 or F_11 for the linear-algebra statements.

Failure criteria:
- give a concrete counterexample;
- or identify the weakest corrected hypothesis and restate the theorem.
```

## Prompt 2 — independent Lattès-113 certificate

```text
W-VERIFY-LATTES-113

Independently verify or kill
cycle60_find_the_theorem_raw/02_lattes_degree113_counterpacket.md.

The target instance is:
p=65537, K=F_{p^15}, n=65536, k=4096, sigma=113,
E: y^2=x^3-9x, and the CM endomorphism [7]+epsilon[8]iota.

Required checks:
1. the twist, Frobenius, and exact point count 65540;
2. the factorization of Frobenius-minus-one and rational cyclic kernel of
   order 113;
3. construction of the induced degree-113 rational map R=A/B, preferably
   with explicit coefficients or a machine-checkable straight-line program;
4. exactly 144 disjoint simple full fibers of size 113;
5. transport to the coset L=alpha F_p^* over K;
6. construction of the denominator, word line, fixed 28-point defect, and
   all binom(144,37) supports;
7. distinct slopes, exact agreement size, transversality, and absence of a
   proper envelope;
8. the claimed full monomial action ranks;
9. all inequalities against floor(q/2^128).

Acceptance criteria:
- a machine-readable certificate;
- one independent verifier not sharing the construction code;
- a short TeX theorem whose hypotheses exactly match the certificate.

Failure criteria:
- report the first false arithmetic or geometric assertion;
- determine whether the packet can be repaired;
- do not retain the genus-one route claim if the actual support packet fails.
```

## Prompt 3 — divisor-norm packet and trichotomy red team

```text
W-VERIFY-DIVISOR-NORM-AND-KILL-TRICHOTOMY

Independently verify or refute
cycle60_find_the_theorem_raw/05_divisor_norm_character_counterpacket.md.

First prove or disprove symbolically:
- the locator bucketing bound;
- the exact support identity W-Q_T=-gamma x^{-1}L_S on H;
- sigma-separation from the coefficient constraints;
- distinct-color extraction;
- full-coordinate and proper-envelope claims.

Then verify the proposed finite instance over
p=2^31-1, F=F_{p^8}, n=2^34, with the stated k and sigma:
- order and generated-field claims;
- primality/Pocklington certificates;
- entropy and bucket logarithm intervals;
- critical arity and tangent bound;
- final |Z|>=2^215 inequality.

Finally attack the proposed exact three-way corank-one trichotomy.
Search for families preserving two independent symmetric or norm characters,
or an additive/determinantal configuration invariant not representable by one
point-fiber quotient or one norm character.

Acceptance criteria:
- either a complete certified counterpacket with a precisely stated killed
  theorem;
- or a concrete failed step and corrected maximum claim.

Failure criterion for the trichotomy:
- one explicit finite split-locator family exhibiting a fourth mechanism.
```

## Prompt 4 — global structured-core registry

```text
W-MCA-WEIGHTED-STRUCTURED-CORE-REGISTRY

Let ell be one envelope-free affine syndrome line. Define structured
containers by their realized support families, identifying rational maps that
induce the same block system or the same certified k-core family.

Prove or refute the following form of global theorem:

There is a canonical family U_struct of distinct k-point cores such that every
point-fiber/split-rational structured slope can be assigned to a core in
U_struct, and

  |U_struct|
  <= B_struct(C,sigma)

for an explicit finite bound depending on the actual domain registry, not on
the number of formulas for rational maps. Consequently,

  |Z_struct|
  <= floor(r/sigma) B_struct(C,sigma).

The theorem must handle Möbius/projective and verified Lattès block systems.
It must prove a bound on the union of cores or on a canonical antichain of
containers. A separate Hasse-Weil estimate for each map is not accepted.

Acceptance criteria:
- a line-intrinsic canonical assignment;
- a global union/overlap bound;
- exact finite profile weights;
- closure under equivalent maps and common refinements.

Failure criteria:
- construct an allowed code and one envelope-free line for which the minimum
  possible weighted core registry exceeds the proposed target;
- identify whether the obstruction is a new pointwise block system or a
  configuration-space module.
```

## Prompt 5 — (t=1) edge-slice inverse

```text
W-JR-T1-EDGE-SLICE-INVERSE

Work in the exact t=1 apolar normal form. Let
I_s=(A,B) be envelope-free with deg A=sigma, so that

  (I_s)_j = A S_{j-sigma} direct-sum F B.

Count monic, squarefree, fully D-split forms

  P_i=A U_i+c_i B

whose corresponding representations are full-coordinate and whose external
colors are distinct.

Prove an explicit occupancy-plus-structure bound, or construct an official
counterpacket. The structure alternatives may include:
- a common split factor;
- a fixed defect;
- a split-rational block system;
- a verified configuration-space module.

Do not assume the point-fiber/divisor-norm trichotomy is complete.

Acceptance criteria:
- a finite bound with explicit constants;
- or an allowed-field counterpacket above both occupancy and the 2^-128
  target after all stated containers are removed.

Failure criteria:
- identify the additional invariant or module needed;
- provide a minimal finite example and symbolic mechanism.

This restricted deg A=sigma case must be settled before claiming the general
t=1 split-numerator inverse.
```

## Prompt 6 — scalar three- and four-circuit theorem

```text
W-LIST-ARITY-3-4-CIRCUIT-HITTING

For a scalar RS syndrome, classify support-minimal full-support relations

  sum_{i=1}^m U_i p_i = 0,
  deg U_i < tau_i,

for m=3 and then m=4, after exact common-error-core and common-agreement-core
stripping.

The objective is not merely to list possible circuits. Construct a globally
bounded set of codewords meeting every such circuit, or give a counterpacket
showing that quotient/core/envelope containers are insufficient.

Required alternatives to test:
1. low-affine-rank polynomial envelope;
2. split-rational block system with exact full-support profile;
3. configuration/split-numerator module;
4. genuinely primitive circuit.

Acceptance criteria:
- an explicit uniform hitting-number bound for all arity-3 circuits, and
  preferably arity 4;
- proof that the construction is hereditary under the relevant punctures;
- exhaustive verification for small cases such as
  (q,n,k)=(7,6,2) and selected F_11 examples.

Failure criteria:
- an explicit syndrome, full-support list, minimal circuit, and proof that it
  evades every declared container.
```

# Kill tests and counterexample searches

| Proposed lemma                                                         | Risk                    | Fast falsification test                                                                                                                                                                                                |
| ---------------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exact envelope/point-fiber/one-norm trichotomy                         | Very high               | Over (F_7,F_{11},F_{17}), bucket split locators by two independent elementary symmetric coefficients or two multiplicative characters. Test whether the resulting degeneration is representable by one norm character. |
| Genus (0/1/\ge2) taxonomy gives a global cover                         | High                    | Enumerate low-degree rational maps on (F_{17}^\times), deduplicate induced partitions, and count maximal incomparable block systems. Per-map fiber bounds do not control this number.                                  |
| H2-defective packets are automatically structured                      | High                    | Enumerate syndrome-line packets for (q=17,n=16,k=8,\sigma=2,3). Compute H2 defects and test quotient, envelope, and configuration tags. Random occupancy-scale packets are expected to be H2-defective.                |
| A puncture recursion has polynomial total branching                    | High                    | Enumerate all minimal envelopes and exact child data for (q=11) or (17). Track the number of distinct descendants and total profile weight; an exponential antichain kills the naive recurrence.                       |
| The general fixed-partition injection works for arbitrary defect size  | High                    | Repeat the collision argument with defect (d>\sigma). A shared defect point only gives exchange distance (d-1), which need not create a proper envelope. The current theorem must remain restricted.                   |
| The (t=1) primitive count after point-fiber removal is occupancy-sized | Moderate-high           | Enumerate apolar ideals for (q=7,11,17), compute all fully split degree-(j) forms in ((I_s)_j), and remove common factors and block partitions. Record residual maxima.                                                |
| Quotient plus common core hits all scalar circuits                     | Already false generally | Reproduce the star/Sidon packet, then search for a multiplicative-domain analogue before asserting relevance to the official domain class.                                                                             |
| Heavy-rectangle rigidity in the fixed-core return                      | Moderate                | Verify every unit, residue, and pencil hypothesis over (F_{17}); search for a (K_{2,2}) configuration satisfying the stated hypotheses but not the conclusion.                                                         |
| The H2 theorem always extracts (d<\sigma)                              | False as worded         | Formula (2) gives (d<\sigma) only once (m_0) exceeds the explicit threshold. Repair the prose and theorem corollary.                                                                                                   |
| Degree-31 Lattès packet arithmetic                                     | Moderate                | Redo the good-parameter averaging. In particular, check whether the collision exclusion and bad-(\theta) estimates lose a factor of two. Treat degree 113 as the primary packet.                                       |
| Real threshold formula and endpoint                                    | Moderate formal risk    | Exhaustively compare (\lfloor n\delta\rfloor), grid reserves, and safety for small (n). Include the case (q<2^{128}), where (T_q=0).                                                                                   |
| Same/generated-field transfer                                          | High                    | For small (B\subset F), enumerate extension-valued syndrome lines. Never allow (q_{\rm line}) to pay a (q_{\rm gen}) structural bill without an explicit theorem.                                                      |

The best small-case scalar-list enumerator should group pairs

[
(E,c),\qquad c\in(F^\times)^E,
]

by their exact syndrome, rather than enumerate received words. It can then construct the spaces (W_P), find support-minimal circuits, and solve the minimum hitting-set problem exactly by brute force or integer programming.

# Verification and formalization plan

## Repository audit

**AUDIT**

The uploaded archive checksum matches the supplied checksum.

Current mechanical status:

* The existing test suite reports 19 passes and 2 skips.
* Those tests do not independently verify the Cycle 60 Lattès, divisor-norm, apolar, or H2 packages.
* All five main TeX files compile, but unresolved references or citations remain in every file.
* Several audit scripts compute the repository root with the wrong parent index and fail under their documented invocation.
* The script reproducibility audit marks 30 of 81 scripts for review.
* Raw Cycle 60 returns are model outputs and evidence, not source-level proofs.

The root-path bug should be repaired before relying on any repository-wide audit. Scripts should accept an explicit `--root` argument rather than infer fragile relative paths.

## Cycle 58–60 claim triage

### Ready for immediate line-by-line proof review

These should be moved into standalone formal notes, not directly into the main papers:

1. Same-field Bessel–Paley lower theorem.
2. Syndrome/transverse-secant equivalence.
3. Exact-(j) padding.
4. Denominator-regime trichotomy as a route reduction.
5. Information-set petal theorem.
6. Fixed-partition packing under its exact reserve-sized-defect hypotheses.
7. Exact scalar full-support identity.
8. Full-support circuit transversal.
9. Prize-scale projection theorem.
10. Exact common-core shortening.

Mathematical confidence is high, but “ready for review” is not the same as promoted.

### Specialist review before promotion

1. Split-locator syzygy-excess formula.
2. Hereditary MDS three-core extraction, after correcting the unconditional (d<\sigma) sentence.
3. (t=1) apolar complete-intersection theorem.
4. Full-coordinate criterion (\gcd(U,V)=1), including generator-change invariance.
5. Jet-residue exact sequence and its field/GRS rescalings.
6. Galois-closure split-fiber point budget, with constant-field and ramification hypotheses.

The H2 proof needs explicit verification of:

* leaf peeling and common-root stripping;
* rank two at every point of (\mathbf P^1), including infinity;
* the bundle splitting degree sum;
* the Macaulay/cohomology identity;
* the implication from a realized nonzero syndrome packet to positive excess;
* all threshold inequalities.

The apolar proof needs explicit verification of:

* the (\sigma\ge2) boundary;
* GRS column rescaling;
* characteristic-independent complete-intersection arguments;
* equal-degree generator ambiguity;
* the envelope interpretation;
* exact-weight layers (e<j).

### Experimental or counterpacket-only

These remain in `experimental/` until independently certified:

* degree-31 and degree-113 Lattès packets;
* divisor-norm finite packet;
* projective-subline official-cap packet;
* general-domain star/Sidon circuit packet;
* the heavy-rectangle claim;
* genus-zero/genus-one taxonomy as a complete classifier;
* H2-defect charging;
* the global finite container package.

**COUNTERPACKET policy:** a packet may be promoted only after the exact theorem it kills is written first. “This suggests the route is incomplete” is not an adequate formal scope statement.

## Required checker suite

The following scripts should be added:

```text
check_theorem_registry.py
check_dependency_acyclicity.py
check_field_ledger.py
check_threshold_rounding.py
verify_syndrome_padding_small.py
verify_petal_and_partition_small.py
verify_scalar_circuit_small.py
verify_apolar_slice_small.py
verify_h2_syzygy_small.py
verify_lattes113_certificate.py
verify_divisor_norm_certificate.py
enumerate_split_partition_registry.py
enumerate_scalar_circuit_hitting.py
enumerate_envelope_descendants.py
verify_prize_certificate.py
```

Finite packets should emit JSON certificates. The verifier, not the constructor, should recompute:

* field orders and irreducibility;
* polynomial identities;
* support sizes and disjointness;
* exact slope counts;
* transversality;
* action ranks;
* integer inequalities against (T_q);
* source-file and code hashes.

Lean or another proof assistant is appropriate first for the linear and combinatorial spine: padding, petals, partition injection, circuits, and projection. It is not the first tool for Lattès geometry or Hilbert–Burch/apolar algebra.

# Paper and notes organization

## What remains in `experimental/`

Everything conjectural, machine-dependent, or awaiting independent proof review:

```text
experimental/formal/
  00_status_registry.yaml
  01_notation_and_thresholds.tex
  02_exact_linear_algebra_spine.tex
  03_support_packing_lemmas.tex
  04_algebraic_normal_forms.tex
  05_master_theorem_contracts.tex
  06_finite_certificate_spec.md

experimental/counterpackets/
  projective_subline/
  lattes_31/
  lattes_113/
  divisor_norm/
  scalar_star/

experimental/certificates/
experimental/reviews/
experimental/failed_lemmas/
```

`00_status_registry.yaml` should be authoritative. Every item should contain:

```text
id
title
status
exact_quantifiers
field_hypotheses
domain_class
dependencies
counterexamples
proof_file
certificate_files
reviewers
last_review_date
source_hash
```

The raw Cycle 58–60 directories remain immutable provenance.

## What should become a formal companion note

The exact spine is strong enough to justify a separate technical note before the safe-side theorem is solved.

### Formal Note I: Exact finite reductions for RS proximity

1. Field and domain conventions.
2. Reserve, grid radius, and real threshold.
3. Syndrome transverse-secant identity.
4. Exact-support padding.
5. Bessel–Paley lower theorem.
6. Information-set petals and reserve-defect partition packing.
7. Scalar full-support syndrome identity.
8. Circuit transversal theorem.
9. Interleaving projection.
10. Finite certificate interface.

This note should contain no conjectural global container theorem.

### Formal Note II: Algebraic normal forms for the unsolved inverse problem

1. Split-locator syzygy matrix.
2. Bundle splitting and excess.
3. Corrected hereditary three-core extraction.
4. (t=1) reduction to dimension (k+1).
5. Binary apolar complete-intersection normal form.
6. Generator invariance and full-coordinate criterion.
7. Precisely stated open inverse theorems.

This note can be publishable even if the grand challenges remain open, provided proof status is exact.

### Counterpacket atlas

A separate note should contain, after verification:

1. Occupancy packets.
2. Möbius/projective block systems.
3. Lattès/isogeny block systems.
4. Divisor-norm/configuration packets.
5. General-domain circuit packets.
6. A table mapping each packet to the exact theorem it kills.

This material should not be mixed into the safe-side proof as informal “exception examples.”

## Eventual main safe-side paper

Only after the upper theorem is genuinely closed:

1. Exact finite theorem statement.
2. Canonical support-module registry.
3. Global structured-weight theorem.
4. Primitive discrepancy theorem.
5. Puncture-hereditary envelope induction.
6. Scalar circuit-hitting theorem.
7. Finite certificate algorithm.
8. Matching adjacent-reserve lower certificates.
9. Exact four-rate code-family outputs.

The existing `slackMCA_v3.tex` should not absorb the Cycle 60 route wholesale. It already contains now-superseded pure aperiodic (n^{1+o(1)}) targets. Those statements should be marked historical or replaced only after the new theorem contract has stabilized.

Paper A and Paper D should remain lower/failure papers. Paper C should consume a verified certificate and should not reproduce the upper proof.

# Notation unification

The present notes overload several symbols. The formal notes should use:

| Object                | Required notation                 |   |   |
| --------------------- | --------------------------------- | - | - |
| Evaluation domain     | (L)                               |   |   |
| Ambient field         | (F), (q=                          | F | ) |
| Generated/base field  | (B), (q_{\rm gen}=                | B | ) |
| Redundancy            | (r=n-k)                           |   |   |
| Reserve               | (\sigma)                          |   |   |
| Agreement size        | (a=k+\sigma)                      |   |   |
| Error size            | (j=r-\sigma)                      |   |   |
| Agreement support     | (S)                               |   |   |
| Error support         | (T) or (J), choose one globally   |   |   |
| Fixed defect          | (\Delta)                          |   |   |
| Residue denominator   | (E(X))                            |   |   |
| Syndrome line         | (\ell(z)=u+zv)                    |   |   |
| Word line             | (w(z)=f+zg)                       |   |   |
| Column span           | (V_T)                             |   |   |
| Syndrome plane        | (U_\ell=\operatorname{span}(u,v)) |   |   |
| Rational map          | (R=P/Q)                           |   |   |
| Induced block system  | (\Pi_R)                           |   |   |
| Block size/number     | (M,N)                             |   |   |
| Interleaving arity    | (m) only                          |   |   |
| Packet size           | (h) or (s_{\rm pkt}), not (m)     |   |   |
| Actual list reserve   | (\tau(P))                         |   |   |
| MCA numerator         | (M_C(\sigma))                     |   |   |
| Scalar list numerator | (L_C(\sigma))                     |   |   |
| Prize target          | (T_q=\lfloor q/2^{128}\rfloor)    |   |   |
| Container weight      | (\omega(\mathcal K))              |   |   |

In the (t=1) note, use (r_1=r-1) for the redundancy of the dimension-(k+1) code. Do not reuse (R), which is already needed for rational maps.

The default domain convention should be a multiplicative coset (L=\alpha H), with subgroup statements identified as special cases.

# Exact theorem names

Recommended stable names:

```text
Theorem: Syndrome-Line Transverse-Secant Identity
Lemma: Exact-Support Transverse Padding
Theorem: Same-Field Bessel–Paley MCA Lower Bound
Lemma: Information-Set Petal Bound
Lemma: Reserve-Defect Partition Packing
Lemma: Structured-Core Registry Bound
Theorem: Scalar Full-Support Syndrome Identity
Lemma: Full-Support Circuit Transversal
Theorem: Prize-Scale Interleaving Projection
Lemma: Common-Core Shortening Identity
Proposition: Split-Locator Syzygy-Excess Formula
Lemma: Hereditary Three-Core Extraction
Theorem: Binary Apolar Locator-Slice Normal Form
```

Open statements should be visibly named as conjectures or theorem contracts:

```text
Conjecture: Weighted Support-Module Registry
Conjecture: Primitive Transverse-Secant Discrepancy
Conjecture: Puncture-Hereditary Envelope Induction
Conjecture: Low-Arity Full-Support Circuit Hitting
```

Do not call a conjectural master statement a “container theorem” in prose before it is proved.

# Proof order avoiding circularity

**PLAN**

1. Freeze field, domain, radius, and support conventions.
2. Prove the exact syndrome and scalar-list identities.
3. Prove padding, monotonicity, projection, petals, and circuit reduction.
4. Prove exact shortening identities, but do not yet invoke induction.
5. Prove the apolar and syzygy normal forms independently of any quotient classifier.
6. Verify all counterpackets.
7. Freeze a canonical registry definition in response to the verified packets.
8. Define “primitive” as the exact complement of that frozen registry and proper envelopes.
9. Prove the envelope-free weighted registry theorem.
10. Prove the primitive discrepancy theorem.
11. Prove that both theorems are uniform over the complete descendant class.
12. Perform hereditary induction.
13. Compile exact finite upper certificates.
14. Produce an explicit adjacent-reserve lower certificate.
15. Extract the grid radius and supremal real threshold.

Circular patterns to prohibit:

* defining “primitive” by whatever the primitive theorem later fails to count;
* using a quotient classifier whose definition depends on a selected denominator;
* invoking the smooth-domain theorem on an arbitrary punctured child;
* using a per-container bound and silently assuming few containers;
* using H2-defect as a charged exception before proving its charge;
* proving an upper theorem with one field and normalizing by another;
* using a boundary-support count as an actual-list count.

# Promotion policy

**PLAN**

Use a six-stage policy:

| Stage           | Meaning                                                   |
| --------------- | --------------------------------------------------------- |
| E0 RAW          | Model return, informal calculation, or conjectural sketch |
| E1 REPRODUCED   | Independent symbolic or finite checks pass                |
| E2 PROOF NOTE   | Standalone exact theorem and proof with all hypotheses    |
| E3 RED TEAMED   | Independent counterexample search and second proof review |
| E4 PRZ ACCEPTED | Human line-by-line review and dependency approval         |
| E5 MAIN TEX     | Eligible for inclusion in the paper                       |

Additional rules:

1. `BANKABLE_LEMMA` is a queue label, not a proof status.
2. No global theorem may depend on an E0 or E1 item except under an explicit `CONDITIONAL` heading.
3. A finite counterpacket requires two independent implementations or one implementation plus a compact independently checkable certificate.
4. Every theorem must declare its field ledger.
5. Every recursive theorem must state the descendant domain class.
6. Every asymptotic statement must have a separate finite corollary before being used for (2^{-128}).
7. Every counterpacket must state exactly which quantifier or alternative it refutes.
8. The main TeX files must have zero undefined references and citations before new material is merged.
9. Raw model language such as “confidence: high” is not copied into mathematical prose.
10. All generated tables in a prize certificate must be reproducible from the certificate script.

# Referee checklist

A PRZ or external referee should be able to answer yes to all of the following:

1. Is the exact code, domain, rate, field, and field of definition stated?
2. Are (q_{\rm gen}), (q_{\rm line}), and (q_{\rm chal}) kept separate?
3. Is the radius converted to an integer support size with an explicit endpoint convention?
4. Does every MCA witness include transversality?
5. Does every scalar-list count use full supports and nonzero error coefficients?
6. Is exact-(j) padding proved rather than assumed?
7. Is the structured registry defined before the primitive complement?
8. Are equivalent maps deduplicated by their realized support systems?
9. Is the total number or total weight of containers bounded globally?
10. Does any use of Hasse–Weil control more than one fixed map? If not, is that limitation explicit?
11. Is hereditary induction valid on every punctured descendant?
12. Are overagreement layers weighted by the actual reserve (\tau(P))?
13. Are all finite constants compared as integers to (T_q)?
14. Is there an explicit failure witness at the preceding reserve?
15. Is the final real threshold attained or merely a supremum?
16. Are all computational claims linked to independent certificates?
17. Does each counterpacket kill only the theorem actually stated?
18. Is the dependency graph acyclic and free of unpromoted claims?

# Resource allocation

## Round 1: theorem-statement stabilization and verification

| Worker | Assignment                                                                               |
| -----: | ---------------------------------------------------------------------------------------- |
|      1 | Exact finite spine: syndrome, padding, petals, circuits, projection, thresholds          |
|      2 | Lattès-113 arithmetic and machine certificate                                            |
|      3 | Divisor-norm packet and trichotomy red team                                              |
|      4 | Syzygy-excess and H2 theorem audit                                                       |
|      5 | (t=1) apolar theorem audit and edge-slice attack                                         |
|      6 | Envelope/common-core shortening and puncture-heredity analysis                           |
|      7 | Global structured-core registry and block-system overlap                                 |
|      8 | Scalar arity-3/4 circuit hitting and small enumeration                                   |
|      9 | Meta-referee: field ledgers, finite endpoint, status registry, certificate specification |

The local Fable/Codex loop should:

* repair repository audit scripts;
* maintain the theorem/dependency registry;
* compile all formal notes;
* generate exhaustive small cases;
* emit and check JSON certificates;
* compare theorem statements against known counterpackets;
* refuse automatic promotion.

## Human/PRZ review order

1. Definitions, field ledgers, support sizes, and threshold endpoint.
2. Exact linear/combinatorial spine.
3. Lattès and divisor-norm packets, because they determine the correct theorem statement.
4. Apolar and H2 normal forms.
5. Hereditary descendant closure.
6. Only then the broad registry or primitive theorem.

Reviewing a broad inverse theorem before the counterpackets and descendant class are fixed risks proving the wrong statement again.

## Round 2

Assuming both major counterpackets verify:

| Workers | Assignment                                                                             |
| ------: | -------------------------------------------------------------------------------------- |
|       3 | Weighted support-module registry: block systems, configuration modules, global overlap |
|       2 | Primitive theory: (t=1) split slice and H2-defect charge                               |
|       2 | Scalar circuits: higher arity and global hitting                                       |
|       1 | Hereditary recurrence and finite branching                                             |
|       1 | Adversarial referee and finite certificate compiler                                    |

If the Lattès packet fails, do not spend a round classifying genus-one maps. Repair or withdraw it and shift that worker to support-partition overlap. If the divisor-norm packet fails, do not build a configuration-character taxonomy until the exact surviving mechanism is known.

# Route to a full solve

**CONDITIONAL**

The route is viable only if a canonical weighted support-module inverse theorem exists. There is currently no evidence strong enough to assert that it does.

The best next exact mathematical target is not a complete genus registry and not the critical-seed completion theorem. It is:

[
\boxed{
\texttt{W-JR-T1-DENSITY-TO-WEIGHTED-SUPPORT-MODULE-CONTAINER}
}
]

Start with the edge slice (\deg A=\sigma). Prove that every unusually large family of full-coordinate, completely split forms

[
P_i=A U_i+c_iB
]

in one envelope-free apolar degree slice either:

1. has a certified support-module container with an exact finite profile charge; or
2. is bounded by occupancy plus an explicit finite term.

A counterexample is equally valuable: it would expose the next missing lower-floor mechanism before the project commits to another incomplete upper theorem.

After that base case:

1. Extend from the edge slice to the full (t=1) apolar slice.
2. Relate the resulting module containers to the global H2/syzygy formulation.
3. Prove total weighted overlap on one syndrome line.
4. Establish puncture-hereditary closure and envelope induction.
5. Solve the scalar low-arity circuit hitting theorem in parallel.
6. Run the finite compiler and supply adjacent-reserve witnesses.

**Final verdict:** the project has reached a credible formulation phase, not a closing phase. The old wall was too narrow. The present blocker is a genuine finite-field inverse theorem for dense families of completely split forms in line-intrinsic modules, plus a global weighted-overlap theorem and hereditary closure. Without those, the grand challenges remain open regardless of how complete the quotient taxonomy becomes.
