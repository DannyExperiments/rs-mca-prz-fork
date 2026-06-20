# Executive verdict

**AUDIT**

No exact prize radii can currently be certified from the repository.

| Branch                                                                              | Verdict                                                                                        |        Confidence |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------: |
| Scalar/interleaved list challenge                                                   | **Medium-range.** The reductions are strong, but one hard inverse/local-limit theorem remains. |              High |
| MCA challenge                                                                       | **Not close.** At least three genuinely different upper-side theories remain missing.          |              High |
| Full two-prize solve from the broad route                                           | Plausible as a research program, but not plausibly one or two theorem rounds away.             |              High |
| Current `W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER` as the primary list wall | Wrong level of abstraction and quantitatively over-strong.                                     |              High |
| Apolar recasting below                                                              | Likely bankable after independent formal review.                                               | High, about (0.9) |

The list problem is considerably healthier than the MCA problem. Projection, actual full-support counting, common-core descent, exact reserve weighting, and circuit extraction are essentially settled. But the circuit formulation has been mistaken for the final theorem. A global circuit transversal bound is almost as hard as bounding the list itself, and its additive (\lfloor(r-1)/\sigma\rfloor) loss is unacceptable when the finite target (T_q=\lfloor q/2^{128}\rfloor) is small.

The sharper scalar object is:

[
\boxed{\text{all completely (L)-split, full-coordinate divisors in one binary apolar complete intersection.}}
]

That formulation simultaneously handles every overagreement layer and gives a canonical, gauge-invariant determinantal language for circuits.

The exact remaining list obstruction is therefore not “classify every low-arity denominator relation.” It is:

[
\boxed{\text{prove a finite one-sided local limit for split divisors in one apolar CI,
modulo canonical block systems, cores, and envelopes.}}
]

---

# A new exact reduction

**PROOF**

## All-layer scalar apolar complete-intersection theorem

Let

[
C=\operatorname{RS}[F,L,k],\qquad q=|F|,\qquad n=|L|,\qquad r=n-k,
]

and fix reserve (\sigma\ge 1), with

[
j=r-\sigma.
]

After the standard nonzero GRS column scaling, identify the parity-check columns with the rational-normal-curve points and identify a nonzero syndrome (s\in F^r) with a functional

[
\Lambda_s:S_{r-1}\longrightarrow F,\qquad S=F[X_0,X_1].
]

Define the apolar ideal by

[
(I_s)_e
=======

{P\in S_e:\Lambda_s(PQ)=0\text{ for every }Q\in S_{r-1-e}}.
]

For (E\subseteq L), let (p_E\in S_{|E|}) be its homogeneous locator.

### 1. Exact all-layer locator criterion

For every (e\le j),

[
s\in \operatorname{span}{h_x:x\in E}
\quad\Longleftrightarrow\quad
p_E\in (I_s)_e.
]

Hence the actual scalar list fiber is exactly

[
N_s(\sigma)
===========

#\left{
\begin{array}{c}
\text{monic squarefree }p\mid \Lambda_L,\quad \deg p\le j,\
p\in I_s,\quad\text{the unique syndrome representation is full-coordinate}
\end{array}
\right}.
]

The worst scalar list is

[
L_C(\sigma)=\max_s N_s(\sigma).
]

The case (s=0) has (N_0(\sigma)=1).

### 2. One complete intersection governs every error weight

For (s\ne0), the quotient (S/I_s) is an Artinian Gorenstein algebra of codimension two and socle degree (r-1). Therefore

[
I_s=(A,B),
]

where (A,B) are coprime homogeneous forms of degrees

[
d\le b,\qquad d+b=r+1.
]

For every (e\le j<r+1),

[
(I_s)*e=A S*{e-d}\oplus B S_{e-b},
]

with (S_t=0) for (t<0). Thus every listed locator has a unique expression

[
p_E=A U_E+B V_E.
]

The representation of (s) on (E) has every coefficient nonzero exactly when

[
\gcd(U_E,V_E)=1,
]

interpreted as the absence of a common projective factor.

This condition is invariant under all admissible changes of CI generators. In particular, when (d<b),

[
B\mapsto cB+AC
]

induces

[
(U,V)\mapsto \left(U-\frac CcV,\frac1cV\right),
]

which preserves the ideal ((U,V)).

### 3. Exact low-generator collapse and layer gap

If (e<b), then (V_E=0). Full-coordinate support then forces (U_E) to be constant. Consequently,

[
e<b
\quad\Longrightarrow\quad
e=d\text{ and }p_E\sim A.
]

Therefore:

[
\boxed{N_s(\sigma)\ge2\Longrightarrow b\le j\Longrightarrow d\ge\sigma+1.}
]

If (d<b), at most one listed locator occurs below degree (b), namely (A) itself when (A) is squarefree and (L)-split. Every other listed locator satisfies

[
e\ge b,\qquad
\tau=r-e\le d-1.
]

Thus a large scalar list automatically lies in the two-generator regime. The (d\le\sigma) branch is not a hard primitive branch: its list size is at most one.

### 4. Exact apolar normal form for the full-support circuit blocks

For a listed error support (E), put

[
e_E=|E|,\qquad \tau_E=r-e_E.
]

The banked circuit block is

[
W_E=p_ES_{\tau_E-1}\subseteq (I_s)_{r-1}.
]

Since

[
(I_s)_{r-1}
===========

A S_{b-2}\oplus B S_{d-2},
]

the coefficient-pair isomorphism

[
A R+B T\longleftrightarrow(R,T)
]

sends (W_E) to

[
\widetilde W_E
==============

{(Q U_E,Q V_E):Q\in S_{\tau_E-1}}.
]

Hence a circuit relation

[
\sum_i Q_i p_{E_i}=0,\qquad Q_i\in S_{\tau_i-1},
]

is exactly the simultaneous polynomial syzygy

[
\sum_i Q_iU_i=0,\qquad
\sum_i Q_iV_i=0.
]

So every scalar circuit is a bounded-degree syzygy of the (2\times N_s) polynomial matrix

[
M_s=
\begin{pmatrix}
U_1&\cdots&U_{N_s}\
V_1&\cdots&V_{N_s}
\end{pmatrix}.
]

This matrix is canonical up to graded row operations of constant determinant.

### 5. Pair determinant and absence of two-element circuits

For distinct listed locators (i,h), define

[
\Delta_{ih}=U_iV_h-U_hV_i.
]

Then (\Delta_{ih}\ne0), and

[
\deg \Delta_{ih}
================

# e_i+e_h-r-1

r-\tau_i-\tau_h-1.
]

Every common root of (p_{E_i}) and (p_{E_h}) is a root of (\Delta_{ih}). Indeed,

[
V_hp_{E_i}-V_ip_{E_h}=A\Delta_{ih},
]

and

[
U_hp_{E_i}-U_ip_{E_h}=-B\Delta_{ih}.
]

Since (A,B) are coprime,

[
|E_i\cap E_h|
\le \deg\Delta_{ih}.
]

Equivalently, (\deg\operatorname{lcm}(p_{E_i},p_{E_h})\ge r+1). Thus

[
W_{E_i}\cap W_{E_h}=0.
]

There are no two-element full-support circuits.

### 6. Exact three-circuit criterion

For three distinct listed locators, let

[
g=\gcd(\Delta_{12},\Delta_{23},\Delta_{31}),\qquad
\gamma=\deg g.
]

The kernel of the (2\times3) matrix is generated by the primitive minor vector

[
\left(
\frac{\Delta_{23}}g,,
-\frac{\Delta_{13}}g,,
\frac{\Delta_{12}}g
\right).
]

A degree-budgeted full-support three-circuit exists exactly when

[
\boxed{\tau_1+\tau_2+\tau_3+\gamma\ge r.}
]

If (\tau_1+\tau_2+\tau_3<r), the precise missing reserve must be supplied by the common determinantal divisor:

[
\gamma\ge r-(\tau_1+\tau_2+\tau_3).
]

Because pair circuits do not exist, every such three-term relation is automatically support-minimal.

This is a canonical definition of a three-way polynomial envelope: the columns become rank one along the divisor (g).

### 7. General apolar circuit bundle

For a subfamily (I) of size (m\ge3), consider

[
\phi_I:
\bigoplus_{i\in I}\mathcal O_{\mathbf P^1}(-e_i)
\longrightarrow
\mathcal O_{\mathbf P^1}(-d)\oplus
\mathcal O_{\mathbf P^1}(-b),
]

whose (i)-th column is ((U_i,V_i)).

Let (\Gamma_I) be the common degeneracy divisor of all (2\times2) minors, with degree (\gamma_I). Write

[
\ker\phi_I
\simeq
\bigoplus_{\nu=1}^{m-2}\mathcal O_{\mathbf P^1}(-\delta_\nu).
]

Then

[
\boxed{
\sum_{\nu=1}^{m-2}\delta_\nu
============================

\sum_{i\in I}e_i-r-1-\gamma_I.
}
]

Moreover, the exact circuit-space dimension at the actual reserve budgets is

[
\boxed{
\dim\operatorname{Circ}(I)
==========================

# h^0(\ker\phi_I(r-1))

\sum_{\nu=1}^{m-2}(r-\delta_\nu)_+.
}
]

Thus every deficient-reserve circuit has one of two algebraically precise causes:

1. a large common determinantal divisor (\Gamma_I); or
2. an anomalously unbalanced splitting of (\ker\phi_I).

That is the correct primitive diagnostic.

---

**BANKABLE_LEMMA**

The repository’s Cycle 60 (t=1) apolar theorem and scalar circuit theorem therefore combine into a stronger scalar theorem:

[
\boxed{
\text{one syndrome}
\Longleftrightarrow
\text{one binary CI}
\Longleftrightarrow
\text{one shifted (2\times N) syzygy problem across all layers}.
}
]

This should be independently formalized before being treated as paper-grade, especially the sheaf-degree formula, generator-gauge invariance, and edge cases (d=b), (d=1), and (s=0).

---

# The circuit route needs to be demoted

**ROUTE_CUT**

Let (h_s) be the minimum number of listed codewords meeting every circuit, and let (\alpha_s) be the maximum cardinality of a circuit-free subfamily. Then

[
h_s=N_s-\alpha_s.
]

The circuit theorem gives

[
\sum_{P\in I}\tau(P)\le r-1
]

for every circuit-free (I), hence

[
1\le\alpha_s\le
R_\sigma:=\left\lfloor\frac{r-1}{\sigma}\right\rfloor
]

whenever (N_s>0). Consequently,

[
N_s-R_\sigma\le h_s\le N_s-1.
]

The Cycle 60 target

[
h_s\le T_q-R_\sigma
]

is sufficient for (N_s\le T_q), but it is not a minimal equivalent wall. It can lose the entire finite certificate when (T_q<R_\sigma), even though the actual list may be tiny.

More fundamentally, (h_s) differs from (N_s) by at most (R_\sigma). Bounding the global transversal is therefore already almost the original list problem. Merely classifying individual circuits does not control (h_s); one still needs a bounded-overlap assignment or a density-increment argument.

The proper role of circuits is:

[
\boxed{\text{structural extraction and falsification, not the final list theorem.}}
]

The final upper theorem should count the split divisors directly. Circuits and their apolar bundles should be used to detect quotient, envelope, and primitive concentration.

Other route cuts remain valid:

* Raw feasible or padded supports are not actual lists.
* A boundary-only theorem does not control overagreement.
* A single ratio (B/A) is not canonical because of polynomial shear.
* Monomial quotient tests are not domain-uniform.
* Quotient packets plus common agreement cores are not exhaustive: the star/Sidon packet forces a polynomial-envelope term.
* Fixing a full-coordinate critical seed merely fixes the syndrome; its completion problem is essentially the original fiber problem.

---

# The correct new list wall

**EXACT_NEW_WALL**

[
\boxed{\texttt{W-LIST-APOLAR-CI-SPLIT-DIVISOR-LOCAL-LIMIT}}
]

For every official smooth subgroup or coset (L), every reserve (\sigma\ge1), and every nonzero syndrome with apolar CI

[
I_s=(A,B),\qquad d+b=r+1,\qquad d\ge\sigma+1,
]

let

[
\mathcal D_s^\circ(\sigma)
==========================

\left{
p\mid\Lambda_L:
\begin{array}{l}
p\text{ monic, squarefree},\
\deg p\le r-\sigma,\
p=AU+BV,\quad \gcd(U,V)=1
\end{array}
\right}.
]

Prove a canonical decomposition tree assigning every member exactly once to:

1. **Hereditary core containers:** a subfamily with a common agreement core, followed by exact shortening.
2. **Realized block-system containers:** full supports equal a fixed defect plus selected blocks of a realized equal-fiber partition. The charge is the exact support profile, not the number of rational formulas.
3. **Determinantal/polynomial envelopes:** families detected by common minor divisors, low-rank incidence, or a quantitatively unbalanced apolar kernel bundle.
4. **Primitive remainder:** the complement after the first three assignments.

The primitive bound should be stated using the exact all-layer occupancy

[
\mu_{\le j}
===========

\frac1{q^r}
\sum_{e=0}^{j}\binom ne(q-1)^e,
]

not merely the boundary approximation. A finite version should prove

[
|\mathcal D_{s,\mathrm{prim}}^\circ|
\le
\left\lceil C_{\mathrm{prim}}\mu_{\le j}\right\rceil
+
D_{\mathrm{prim}},
]

with explicit constants, and a global certificate

[
E_{\mathrm{core}}
+
Q_{\mathrm{block}}
+
E_{\mathrm{env}}
+
\left\lceil C_{\mathrm{prim}}\mu_{\le j}\right\rceil
+
D_{\mathrm{prim}}
\le T_q.
]

The theorem must include a deterministic priority rule or bounded-overlap argument. A statement of the form “every large subfamily resembles some quotient” is insufficient.

---

# Minimal theorem package

## Grand MCA challenge

### Asymptotic package

The smallest honest package is not the full current taxonomy. It is:

1. **Syndrome transverse-secant identity — banked.**

   [
   M_C(\sigma)
   ===========

   \max_\ell
   |\operatorname{Bad}_\sigma(\ell)|.
   ]

2. **Support-theoretic structural cover — unknown.**

   On an envelope-free line, canonically remove realized block systems. This theorem must absorb genus-zero, Lattes/genus-one, and any other realized low-complexity quotient without counting syntactic rational functions.

3. **Hereditary envelope theorem — unknown.**

   Bound the total charge of the canonical shortening tree, not merely each child.

4. **Primitive discrepancy theorem — unknown.**

   After structural removal, prove the occupancy/main-term bound plus explicit discrepancy. Configuration-space characters and divisor-norm effects must either be classified or absorbed by this theorem.

5. **Matching failure theorem — strong but not fully code-specific.**

   The random-anchor/Bessel branch is theorem-grade in its audited range. Codes not covered by that finite inequality still need explicit previous-reserve witnesses.

The Lattes registry, (t=1) apolar theorem, H2 extraction, and divisor-norm trichotomy are dependencies or possible methods. They are not logically separate requirements if a denominator-free theorem proves items 2–4 directly.

### Finite (2^{-128}) package

For each code and reserve, produce explicit integers

[
Q_{\mathrm{block}},\quad
E_{\mathrm{her}},\quad
D_{\mathrm{prim}},\quad
C_{\mathrm{occ}}
]

such that

[
M_C(\sigma)
\le
\max\left{
E_{\mathrm{her}},
Q_{\mathrm{block}}+
D_{\mathrm{prim}}+
\left\lceil
C_{\mathrm{occ}}\frac{\binom nj}{q^{\sigma-1}}
\right\rceil
\right}
\le T_q.
]

Then produce an actual line with more than (T_q) slopes at (\sigma-1), or invoke a verified lower theorem that supplies it.

## Grand list challenge

### Asymptotic package

1. **Interleaved-to-scalar projection — banked.**
2. **Exact scalar full-support identity — banked.**
3. **All-layer apolar CI and circuit-bundle normal form — proved above, pending review.**
4. **Apolar split-divisor local limit/container theorem — hard unknown.**
5. **Matching previous-reserve lower theorem — partly banked.**

No separate circuit-transversal theorem is logically required in the minimal package. It is an internal extraction tool for item 4.

### Finite (2^{-128}) package

Let

[
T_q=\left\lfloor\frac q{2^{128}}\right\rfloor.
]

One needs:

1. an explicit direct bound (L_C(\sigma)\le T_q);

2. an actual list (>T_q) at (\sigma-1);

3. the projection inequality

   [
   \binom{T_q+1}{2}<q_{\mathrm{proj}};
   ]

4. exact field bookkeeping;

5. exact threshold rounding.

The correct entropy lower certificate is

[
\max_s N_s(\sigma)
\ge
\left\lceil
\frac1{q^r}
\sum_{e=0}^{r-\sigma}
\binom ne(q-1)^e
\right\rceil.
]

At a single boundary layer it is

[
\left\lceil
\frac{\binom nj(q-1)^j}{q^r}
\right\rceil,
]

not unconditionally (\lceil\binom nj/q^\sigma\rceil). The simplified Cycle 60 finite lower ledger needs this correction before promotion.

Quotient and split-rational constructions may give stronger lower certificates.

For either challenge define

[
\sigma_C^*
==========

\min{\sigma:N_C(\sigma)\le T_q},
]

where (N_C) is the relevant exact numerator. Then

[
\delta_{\max}^{\mathrm{grid}}
=============================

1-\rho-\frac{\sigma_C^*}{n}.
]

The supremal real transition is

[
1-\rho-\frac{\sigma_C^*-1}{n},
]

with the endpoint unsafe when (\sigma_C^*) is minimal.

There is no rate-only finite formula.

---

# Dependency DAG

Status legend: **banked**, **likely**, **unknown**, **doubtful**, **false**.

```text
FULL TWO-PRIZE SOLVE [unknown]
|
+-- MCA-EXACT-THRESHOLD [unknown]
|   |
|   +-- syndrome transverse-secant formulation [banked]
|   +-- lower/failure branch [banked in audited range; finite gaps unknown]
|   +-- MCA-CONT upper theorem [unknown, hard]
|   |   |
|   |   +-- fixed realized-partition profile bounds [banked]
|   |   +-- global support-system cover / bounded overlap [unknown]
|   |   |   +-- genus-zero registry [likely]
|   |   |   +-- Lattes/genus-one packets [doubtful until arithmetic audit]
|   |   |   +-- high-genus discrepancy branch [unknown]
|   |   +-- exact shortening operation [banked]
|   |   +-- bounded hereditary-envelope tree [unknown]
|   |   |   +-- H2/MDS-3-core extraction [banked]
|   |   |   +-- H2-defect global charge [unknown]
|   |   +-- primitive occupancy/discrepancy [unknown]
|   |       +-- t=1 apolar normal form [banked]
|   |       +-- divisor-norm/configuration effect [counterpacket; ledger needed]
|   |       +-- primitive inverse theorem [unknown, hard]
|   +-- exact finite constants and field ledger [unknown]
|
+-- LIST-EXACT-THRESHOLD [unknown]
    |
    +-- interleaved projection [banked]
    +-- exact threshold rounding [banked]
    +-- scalar full-support syndrome identity [banked]
    +-- all-layer apolar CI locator normal form [likely/bankable]
    |   +-- codimension-two AG complete intersection [banked ingredient]
    |   +-- full-coordinate gcd criterion [likely/bankable]
    |   +-- low-generator collapse [likely/bankable]
    |   +-- apolar block/circuit matrix [likely/bankable]
    |   +-- pair and three-circuit criteria [likely/bankable]
    |   +-- general kernel-bundle formula [likely/bankable]
    |
    +-- W-LIST-APOLAR-CI-SPLIT-DIVISOR-LOCAL-LIMIT [unknown, hard]
    |   +-- common agreement-core shortening [banked]
    |   +-- fixed block-system profile count [banked]
    |   +-- global block-system registry / overlap control [unknown]
    |   +-- determinantal envelope definition [partly likely]
    |   +-- determinantal envelope global charge [unknown]
    |   +-- primitive apolar discrepancy [unknown, hard]
    |
    +-- previous-reserve failure [partly banked]
        +-- exact all-layer average lower bound [banked]
        +-- quotient-core actual lists [banked]
        +-- split-rational packets [partly banked]
        +-- code-specific finite witness selection [unknown]
```

**FALSE or cut nodes**

```text
pure n^{1+o(1)} safe-side theorem without occupancy/floors
raw feasible supports = actual scalar list
boundary padding substitutes for lower error weights
monomial quotient registry is domain-uniformly complete
point-fiber quotients exhaust JR degeneracy
quotient + common agreement core exhaust scalar lists
one selected ratio B/A is canonical
high-denominator MCA compresses to t <= sigma
full-coordinate seed completion is a weaker problem
per-circuit classification automatically yields a global hitting set
h_s <= T_q - floor((r-1)/sigma) is the minimal list wall
```

---

# Best next theorem-worker prompts

## Prompt 1 — Formalize the new apolar theorem

```text
PROVE OR DISPROVE: L-SCALAR-APOLAR-CI-ALL-LAYERS-AND-CIRCUIT-BUNDLE.

Let C=RS[F,L,k], r=n-k, sigma>=1, j=r-sigma, and let s!=0 be a
scalar syndrome. Define its binary apolar ideal I_s from the functional on
S_{r-1}.

Prove, over an arbitrary finite field and after arbitrary nonzero GRS column
scaling:

1. I_s=(A,B), with coprime generators of degrees d<=b and d+b=r+1.
2. For every e<=j, an error locator p_E represents s iff p_E in (I_s)_e.
3. Writing p_E=A U_E+B V_E uniquely, the syndrome representation is
   full-coordinate iff gcd(U_E,V_E)=1.
4. If e<b, full-coordinate forces e=d and p_E proportional to A.
   Hence a fiber of size >=2 has d>=sigma+1.
5. Under (I_s)_{r-1}=A S_{b-2} direct-sum B S_{d-2}, the circuit block
   p_E S_{r-e-1} becomes {(Q U_E,Q V_E)}.
6. Pair determinants are nonzero and have degree
   e_i+e_h-r-1; no two-element circuits exist.
7. For triples, with gamma=deg gcd(Delta_12,Delta_23,Delta_31), a
   full-support circuit exists iff tau_1+tau_2+tau_3+gamma>=r.
8. For m columns, prove the kernel-bundle degree and circuit-dimension
   formulas.

Check invariance under B -> cB+AC and GL_2 changes when d=b.

ACCEPTANCE:
A complete proof covering s=0 separately, d=b, missing coefficient spaces,
homogenization, roots at infinity, and all characteristic issues; plus small
finite-field tests.

FAILURE:
An explicit F,L,s and listed supports violating any clause, with complete
machine-checkable data.
```

## Prompt 2 — Attack the actual list wall

```text
PROVE OR BUILD A COUNTERPACKET:
W-LIST-APOLAR-CI-SPLIT-DIVISOR-LOCAL-LIMIT.

Work on an official domain L=alpha*mu_n, with n a power of two and
k/n in {1/2,1/4,1/8,1/16}. For one nonzero syndrome let
I_s=(A,B), d+b=r+1, d>=sigma+1.

Count every monic squarefree divisor p|Lambda_L of degree <=r-sigma
having a coprime representation p=AU+BV.

Construct a canonical, nonovercounting decomposition into:
(a) common-agreement-core descendants;
(b) realized equal-fiber block-system packets, charged by exact support
    profiles rather than rational-map count;
(c) determinantal or low-affine-rank envelope packets;
(d) a primitive remainder.

Desired primitive bound:
    |primitive| <= ceil(C*mu_{<=j}) + D,
where
    mu_{<=j}=q^{-r} sum_{e<=j} binom(n,e)(q-1)^e,
and C,D are explicit enough for comparison with floor(q/2^128).

ACCEPTANCE:
Either a complete finite theorem with a deterministic assignment rule and
explicit constants, or a genuine reduction to one clearly narrower named
lemma.

FAILURE:
An official-domain family above the proposed bound that has no large common
core, no realized block-system container under the stated definition, no
charged determinant envelope, and no overlap loophole.
```

## Prompt 3 — Global realized-block-system registry

```text
PROVE OR KILL:
W-LIST-REALIZED-BLOCK-SYSTEM-PROFILE-COVER.

Given all full agreement supports in one scalar syndrome fiber, consider every
equal-size partition of a subset of L that is realized as full fibers of some
separable rational map. Identify maps that induce the same block system.

Prove that the supports assigned to maximal block systems admit a canonical
cover whose total charge is bounded by the sum of their exact binomial support
profiles, with bounded overlap or a potential-decrease argument. Show that
large overlap between nonrefining block systems forces either:
1. a common agreement core;
2. a low-affine-rank/determinantal envelope; or
3. a coarser realized block system.

Do not count formulas for rational functions.

ACCEPTANCE:
A global syndrome-wise inequality suitable for the finite list certificate.

FAILURE:
One explicit CI/list fiber supporting many nonrefining realized partitions
whose total profile charge is super-budget and which triggers none of the
three structural conclusions.
```

## Prompt 4 — Deficient-circuit inverse theorem

```text
PROVE OR DISPROVE:
W-LIST-APOLAR-BUNDLE-DEFICIENT-CIRCUIT-INVERSE.

For a support-minimal apolar circuit I of arity
m<=ceil(r/sigma), put T_I=sum_i tau_i and assume T_I<r.
Let Gamma_I be the gcd divisor of all 2x2 minors of the coefficient matrix,
and let ker(phi_I)=direct-sum O(-delta_nu).

Use the exact identities
    sum delta_nu = sum e_i-r-1-deg Gamma_I
and
    dim Circ(I)=sum (r-delta_nu)_+
to prove a quantitative alternative:

A. deg Gamma_I supplies a fixed positive fraction of r-T_I; or
B. a subcircuit has a canonical common-core, realized block-system, or
   low-affine-rank envelope certificate; or
C. the circuit belongs to an explicitly defined primitive splitting-imbalance
   class whose total incidence in one syndrome fiber has an occupancy-scale
   bound.

The conclusion must support global charging, not only classify one circuit.

ACCEPTANCE:
A proved quantitative trichotomy with a monotone potential for recursive
removal.

FAILURE:
An explicit official-domain family of many deficient circuits with small
minor gcds, no core/block/envelope certificate, and unbounded primitive
overlap.
```

## Prompt 5 — Exhaustive falsifier

```text
BUILD: scalar_apolar_ci_scan.py.

For small multiplicative subgroup/coset instances, compute exactly:

- every actual full-support scalar list fiber;
- its apolar CI generator degrees;
- every split locator and coprime coefficient pair;
- all pair minors and common minor divisors;
- all circuits up to ceil(r/sigma);
- minimum circuit transversal and maximum circuit-free subfamily;
- common agreement cores;
- realized equal-fiber partitions up to a chosen rational-map degree;
- residual primitive counts versus the exact occupancy mean.

Primary cases:
F_17 with n=8 and rates 1/2,1/4,1/8;
F_17 with n=16 for structured/random syndromes;
F_97 and F_257 with n=16;
selected quotient-core, star/Sidon, additive, and random packets.

ACCEPTANCE:
Reproducible JSON plus automatic extraction of the smallest counterexample to
each proposed lemma. Cross-check all banked scalar identities.

Do not interpret q<2^128 examples as prize certificates; they are structural
kill tests only.
```

## Prompt 6 — Finite certificate and lower-ledger audit

```text
AUDIT AND FORMALIZE: L-LIST-FINITE-2^-128-CERTIFICATE.

Produce an exact integer certificate for a supplied code C and reserve sigma:

1. q, n, k, r, j, T_q=floor(q/2^128);
2. same-field or base-field projection inequality;
3. exact all-layer occupancy mean;
4. core, block-system, envelope, and primitive upper charges;
5. direct proof that their assigned union is the full scalar list;
6. previous-reserve lower certificate;
7. grid radius and real-radius endpoint convention.

Explicitly audit the Cycle 60 simplified entropy lower
ceil(binomial(n,j)/q^sigma). Replace it by the exact full-support expression
unless an additional argument proves the simplification.

ACCEPTANCE:
A machine-checkable certificate schema plus proof that a passing certificate
implies the scalar and every constant-arity interleaved prize statement.

FAILURE:
A concrete field-transfer, rounding, or full-coordinate counterexample to any
certificate implication.
```

---

# Kill tests and counterexample searches

**COUNTERPACKET**

| Proposed claim                                                         | Risk                                    | Fast falsification                                                                                                              |
| ---------------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| A selected (B/A) classifies quotient structure                         | Already false as a canonical claim      | Apply (B\mapsto B+AC); look for changed action rank with unchanged split slice                                                  |
| Every envelope is detected by a large gcd of minors                    | Doubtful                                | Compute (\Gamma_I) for the star/Sidon packet and low-affine-rank packets; (\Gamma_I=1) with a large envelope kills the claim    |
| Every individual circuit has a quotient/core/envelope tag              | Likely false without density hypotheses | Replay mixed Kronecker-scroll examples and search small official groups                                                         |
| A bounded number of rational maps controls the quotient charge         | Likely false                            | Enumerate low-degree maps on (\mu_{16}), deduplicate induced partitions, and count nonrefining systems                          |
| The global hitting-set target is equivalent to the list target         | False                                   | Compute (N_s,\alpha_s,h_s); find fibers with (h_s>T-R_\sigma) after setting a comparison threshold (T\ge N_s)                   |
| Primitive residual is (O(\mu_{\le j})) with a universal small constant | Unknown and high-risk                   | Remove all currently recognized structures in (n=8,16) subgroup cases and maximize residual/mean                                |
| Common-core recursion has automatically bounded branching              | Doubtful                                | Construct overlapping sunflower/star sublists with many competing cores                                                         |
| Boundary layer controls all layers                                     | False                                   | Search syndromes where most list mass occurs at (e<j)                                                                           |
| (\binom nj/q^\sigma) is an exact actual-list average lower bound       | False without correction                | Compare with (\binom nj(q-1)^j/q^r) symbolically or in any small field                                                          |
| Lattes packets are already theorem-grade                               | Unverified                              | Recompute curve orders, subgroup sizes, separability, full fibers, collision exclusions, and domain admissibility independently |

The most important computational target is not raw maximum list size. It is the residual profile after canonical structural removal:

[
\frac{
N_s-
N_{\rm core}-
N_{\rm block}-
N_{\rm env}
}{
\mu_{\le j}
}.
]

A persistent large ratio on official subgroup toy cases is either the missing container or a counterexample to the intended local limit.

---

# Verification and formalization plan

**AUDIT**

## Claims to verify first

1. Interleaved projection, including the actual projection field.
2. Exact scalar full-support syndrome identity.
3. Circuit-hitting theorem and actual-reserve weighting.
4. Cycle 60 syzygy-bundle twists and dimension formulas.
5. (t=1) apolar CI theorem, especially the gcd criterion and generator gauge.
6. The all-layer apolar theorem and three-circuit criterion above.
7. Common agreement-core shortening.
8. Fixed-partition support-profile counts.
9. Star/Sidon and additive quotient counterpackets.
10. Only then: Lattes and divisor-norm arithmetic.

The existing finite audits currently pass:

* `verify_l2_interleaved_constants.py`
* `verify_l2_quotient_core_count.py`
* `verify_l1_syndrome_catalecticant_shells.py`
* `verify_l1_determinantal_support_criterion.py`

The latter two pass all four default toy cases. They are finite consistency checks, not upper theorems.

## New scripts

```text
verify_scalar_apolar_ci_all_layers.py
verify_apolar_circuit_bundle.py
enumerate_scalar_full_support_fibers.py
solve_min_circuit_transversal.py
classify_realized_block_systems.py
scan_apolar_primitive_residual.py
replay_cycle58_60_counterpackets.py
emit_finite_list_prize_certificate.py
```

The apolar verifier should test invariance under random admissible generator shears, not merely one chosen generator pair.

## TeX promotion

Promote only after independent proof review and computational audit:

* projection theorem;
* scalar full-support identity;
* common-core descent;
* all-layer apolar CI theorem;
* pair and three-circuit criteria;
* general apolar kernel-bundle formula.

Do not yet promote as theorems:

* Lattes packet claims;
* a complete genus-zero/genus-one registry;
* any global block-system overlap bound;
* any primitive (n^{1+o(1)}) or occupancy theorem;
* any finite (2^{-128}) constants;
* the simplified entropy lower ledger;
* the current global circuit-cover wall.

---

# Resource allocation

**PLAN**

## Round 1: verification and route narrowing

| Worker | Assignment                                                                                 |
| -----: | ------------------------------------------------------------------------------------------ |
|      1 | Formal proof of the all-layer apolar CI theorem                                            |
|      2 | Independent adversarial referee for that theorem; search edge cases and gauge failures     |
|      3 | Exhaustive scalar/apolar/circuit scanner                                                   |
|      4 | Realized block-system registry and overlap theorem                                         |
|      5 | Determinantal envelope and deficient-circuit inverse                                       |
|      6 | Primitive apolar local limit, harmonic/finite-field approach                               |
|      7 | Exact finite list certificate and previous-reserve lower ledger                            |
|      8 | MCA-only verification of Lattes and configuration-character packets                        |
|      9 | Meta-referee: dependency audit, false-wall detection, and proof-to-certificate consistency |

This allocates six primary workers to the list theorem, two to cross-branch/MCA verification, and one to adversarial integration.

The human/PRZ should check, in this order:

1. the all-layer apolar theorem;
2. the demotion of the global hitting-set wall;
3. the exact full-support lower mean and field ledger;
4. scanner output;
5. only afterward the Lattes taxonomy.

## Round 2 if the apolar theorem survives

* Three workers attack primitive local limit by deliberately different methods:

  * subgroup/Hayes/Fourier estimates;
  * algebraic geometry of split divisors in a pencil;
  * inverse Littlewood–Offord/additive combinatorics.
* Two workers attack global block-system overlap.
* One worker handles determinant-envelope/hereditary charging.
* One worker produces exact finite constants and lower witnesses.
* One worker continues MCA structural verification.
* One worker serves as formal referee and attempts counterexamples.

## Round 2 if a counterpacket appears

* Three workers generalize it toward an official domain and official rate.
* Two identify the missing invariant/container.
* Two repair the decomposition and overlap ledger.
* One recomputes threshold consequences.
* One independently referees the claimed counterexample.

The local Fable/Codex loop should handle exhaustive algebra, finite-field enumeration, Fitting ideals, minor gcds, splitting computations, proof lint, and certificate generation. It should not be trusted to infer the primitive inverse theorem from finite samples.

---

# Route to a full solve

**CONDITIONAL**

For the list challenge, the route is now precise:

1. Bank the all-layer apolar CI and circuit-bundle theorem.
2. Prove or kill `W-LIST-APOLAR-CI-SPLIT-DIVISOR-LOCAL-LIMIT`.
3. Obtain explicit structural and primitive charges at each reserve.
4. Find the least (\sigma) whose direct list bound is at most (T_q).
5. Produce an actual list larger than (T_q) at (\sigma-1).
6. Invoke projection to obtain the same threshold for every constant interleaving arity.

The exact blocker is:

[
\boxed{
\text{a finite one-sided local limit for fully (L)-split divisors in a
binary apolar complete intersection, modulo canonical structural containers.}
}
]

For MCA, no analogous single narrowed wall is yet available. It remains blocked by:

[
\boxed{
\text{global support-system cover}
+
\text{bounded hereditary-envelope charge}
+
\text{primitive all-line discrepancy}.
}
]

The scalar list problem is medium-range. The combined prize problem is still missing hard inverse theorems. The correct immediate move is to formalize the apolar reduction and attack the split-divisor local limit—not to launch another broad circuit-by-circuit quotient classification.
