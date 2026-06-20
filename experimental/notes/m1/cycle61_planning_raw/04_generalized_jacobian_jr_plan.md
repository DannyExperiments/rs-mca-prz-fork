## Executive verdict

The full prize problem is **not close**. It remains a medium-range program blocked by several genuinely hard inverse theorems, not by bookkeeping or one missing estimate.

* **MCA challenge:** plausibly solvable along a corrected version of this route, but only after replacing the vague divisor-norm ledger by a generalized-Jacobian subset-product formulation and separately solving the (d>\sigma) rational-pair inverse problem. **Confidence: moderate, about 60%.**
* **Grand list challenge:** structurally reduced to a clean scalar circuit problem, but that scalar cover theorem is independent and still hard. **Confidence: low-to-moderate, about 40%.**
* **A full solve in the next two theorem-worker rounds:** unlikely. **Confidence: high, about 85%.**
* **The current `critical-seed completion` wall is the wrong wall:** high confidence, above 95%.
* **The old pure (n^{1+o(1)}) primitive bound is false or incorrectly normalized:** high confidence.
* **No numerical values of (\delta_C^*) at rates (1/2,1/4,1/8,1/16) are presently justified.**

The exact finite answer, once the missing upper theorem is proved, is

[
\delta_{X,C}^*(2^{-128})
========================

1-\rho-\frac{\sigma_X^*}{n}+\frac1n,
]

where (\sigma_X^*) is the least reserve whose exact numerator is at most

[
T_F=\left\lfloor\frac{|F|}{2^{128}}\right\rfloor .
]

The lower/failure machinery is close to sufficient for locating (\sigma_X^*) from below. The missing part is proving safety at the first candidate reserve.

---

## AUDIT

The repository’s strongest conclusions are consistent:

1. The MCA object is the denominator-free transverse-secant problem

   [
   \operatorname{Bad}_\sigma(\ell)=
   \left{
   z:\exists |T|\le r-\sigma,\
   \ell(z)\in V_T,\
   \ell\not\subseteq V_T
   \right}.
   ]

2. A correct upper bound must contain:

   * an occupancy/main term;
   * split-rational and Lattes quotient profiles;
   * hereditary envelope terms;
   * configuration-space quotient terms;
   * a genuine primitive discrepancy remainder.

3. The `t=1` branch is ordinary (\operatorname{RS}[F,D,k+1]) decoding with an external evaluation color. It is therefore a mandatory base case, not a harmless special stratum.

4. Fixing a full-coordinate critical seed merely fixes the syndrome. Its completion set is the original colored syndrome fiber minus the seed. It does not reduce the inverse problem.

5. H2-defect is an inverse certificate, not a payable exception. Generic occupancy packets can have dense three-cores.

6. Point-fiber quotients do not account for the Cycle 60 product packet.

The principal correction I would make to the Cycle 60 route board is that the product/divisor-norm packet is not an isolated new species of exception. At minimal apolar degree, all such characters live in one canonical generalized Jacobian. That gives a substantially narrower and cleaner first theorem.

---

# PROOF

## Minimal-apolar-degree generalized-Jacobian fiber theorem

Consider the `t=1` apolar complete intersection

[
I_s=(A,B)\subset F[X_0,X_1],
]

with

[
\deg A=d,\qquad \deg B=j+\sigma-d.
]

Assume the envelope-free minimal-degree case

[
d=\sigma.
]

Then

[
\deg B=j,\qquad
(I_s)*j=A,S*{j-\sigma}\oplus FB.
]

Let

[
\Delta=V(A)
]

be the degree-(\sigma) effective divisor on (\mathbf P^1). Remove any evaluation points lying in (\operatorname{Supp}\Delta):

[
D^\circ=D\setminus\operatorname{Supp}\Delta.
]

Choose a linear form (L_*) nonvanishing on (\Delta). For (x\in D^\circ), let

[
L_x=X_1-xX_0
]

and define

[
\alpha_\Delta(x)
================

\left[
\left.\frac{L_x}{L_*}\right|_\Delta
\right].
]

The target group is

[
G_\Delta
:=
H^0(\Delta,\mathcal O_\Delta)^\times/F^\times,
]

the (F)-points of the generalized Jacobian of (\mathbf P^1) with modulus (\Delta). Define

[
b_\Delta
========

\left[
\left.\frac{B}{L_*^j}\right|*\Delta
\right]
\in G*\Delta.
]

Then, except for the possible singleton edge case (j=\sigma) and (P_T\sim A),

[
\boxed{
\begin{aligned}
&T\in\binom{D}{j}
\text{ gives a full-coordinate representation of }s\
&\qquad\Longleftrightarrow\qquad
T\subseteq D^\circ
\quad\text{and}\quad
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta
\text{ in }G_\Delta.
\end{aligned}}
]

### Proof

A degree-(j) locator is

[
P_T=\prod_{x\in T}L_x.
]

Since

[
(I_s)*j=A,S*{j-\sigma}\oplus FB,
]

we have

[
P_T\in(I_s)_j
\iff
P_T=AU+cB
]

for some (U\in S_{j-\sigma}) and (c\in F).

For a full-coordinate representation, the Cycle 60 gcd criterion gives

[
\gcd(U,c)=1.
]

Unless (j=\sigma) and (U) is a unit, this forces (c\ne0).

Restricting to (\Delta) kills the (AU) term:

[
P_T|*\Delta=cB|*\Delta .
]

After division by (L_*^j) and quotienting by (F^\times), this becomes

[
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta.
]

Conversely, equality in (G_\Delta) means that for some (c\in F^\times),

[
P_T|*\Delta=cB|*\Delta.
]

Hence (A\mid P_T-cB), so

[
P_T=AU+cB.
]

Since (c\ne0), the representation is full-coordinate.

If (x\in T\cap\operatorname{Supp}\Delta), then at (x),

[
0=P_T(x)=cB(x),
]

contradicting (c\ne0) and (\gcd(A,B)=1). Thus (T\subseteq D^\circ).

### Exact group size

Write

[
\Delta=\sum_i m_iP_i,
]

where (P_i) has residue degree (d_i). Then

[
\boxed{
|G_\Delta|
==========

# \frac{\prod_i (q^{d_i}-1),q^{d_i(m_i-1)}}{q-1}

q^{\sigma-1}
\frac{\prod_i(1-q^{-d_i})}{1-q^{-1}}.
}
]

This shows that the ambient (q^{\sigma-1}) occupancy denominator is only an approximation. More importantly, it may still be the wrong denominator because the point images can generate a much smaller subgroup.

---

## PROOF

### Exact Fourier and quotient charging

Let

[
N_{\Delta,j}(b)
===============

#\left{
T\in\binom{D^\circ}{j}:
\prod_{x\in T}\alpha_\Delta(x)=b
\right}.
]

Finite Fourier inversion gives

[
\boxed{
N_{\Delta,j}(b)
===============

\frac1{|G_\Delta|}
\sum_{\chi\in\widehat G_\Delta}
\chi(b)^{-1}
e_j!\left(
\chi(\alpha_\Delta(x)):x\in D^\circ
\right).
}
]

The trivial character is not necessarily the entire main term.

Fix (x_0\in D^\circ), and let

[
G_{\rm eff}
===========

\left\langle
\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1}:
x\in D^\circ
\right\rangle.
]

All (j)-fold products lie in one coset of (G_{\rm eff}). Characters annihilating (G_{\rm eff}) therefore contribute coherently. The correct baseline occupancy is

[
\boxed{
\frac{\binom{|D^\circ|}{j}}{|G_{\rm eff}|},
}
]

not automatically (\binom nj/q^{\sigma-1}).

More generally, let (\mathcal S\le\widehat G_\Delta), put

[
K=\mathcal S^\perp,\qquad Q=G_\Delta/K,
]

and let (N_Q(y)) count subset products after projection to (Q). Then the total Fourier contribution of all characters in (\mathcal S) is exactly

[
\boxed{
\frac{N_Q(\pi b)}{|K|}.
}
]

This is how divisor-norm and jet characters must be charged: **jointly through a quotient-conditioned main term**, not one character at a time.

---

## COUNTERPACKET

### Conceptual interpretation of the Cycle 60 product packet

Take

[
\Delta=[0]+(\sigma-1)[\infty].
]

Then

[
|G_\Delta|=(q-1)q^{\sigma-2}.
]

It has one toric coordinate and a local-unit filtration of total size (q^{\sigma-2}). On a multiplicative subgroup (H\le F^\times) of order (n), the toric image has size at most (n). Hence

[
|G_{\rm eff}|\le nq^{\sigma-2}.
]

Therefore some boundary fiber has size at least

[
\boxed{
\frac{\binom nj}{nq^{\sigma-2}}.
}
]

This is exactly the support scale of the Cycle 60 divisor-product packet.

Thus that packet is not anomalous discrepancy relative to the correct effective-group occupancy. It is a counterexample to using the ambient denominator (q^{\sigma-1}).

In monic locator coordinates, this generalized-Jacobian boundary condition fixes:

[
c_0(P_T)
]

and the first (\sigma-2) jets at infinity, equivalently the highest (\sigma-2) nonleading coefficients. This is the product-plus-high-coefficient bucket from Cycle 60.

---

## BANKABLE_LEMMA

### H2 syzygies split componentwise in apolar coordinates

Now let the apolar generator degree be

[
d>\sigma
]

and write every locator as

[
P_i=AU_i+BV_i,
]

with

[
\deg U_i=j-d,\qquad
\deg V_i=d-\sigma,
]

and (\gcd(A,B)=1).

Suppose H2 extraction produces coefficient forms (C_i) of degree

[
e<\sigma
]

such that

[
\sum_i C_iP_i=0,
\qquad
\sum_i z_iC_iP_i=0.
]

Then

[
\boxed{
\sum_i C_iU_i=
\sum_i C_iV_i=
\sum_i z_iC_iU_i=
\sum_i z_iC_iV_i=0.
}
]

### Proof

From

[
A\sum_iC_iU_i+B\sum_iC_iV_i=0
]

and (\gcd(A,B)=1),

[
A\mid \sum_iC_iV_i,\qquad
B\mid \sum_iC_iU_i.
]

But

[
\deg\sum_iC_iV_i
\le e+d-\sigma<d=\deg A,
]

so the first sum is zero. Similarly,

[
\deg\sum_iC_iU_i
\le e+j-d
<
j+\sigma-d
==========

\deg B.
]

Hence the second sum is zero. The (z_i)-weighted identity is identical.

This is the correct algebraic object in the (d>\sigma) branch: a family of rational pairs ((U_i,V_i)) admitting two simultaneous low-degree syzygies.

---

## ROUTE_CUT

The wall

```text
W-JR-CORANK-ONE-DIVISOR-NORM-CHARACTER-TRICHOTOMY
```

is too atomized and probably false as stated.

At (d=\sigma), divisor norms, products, residue-field norms and fat-point jet characters are all characters of the single group (G_\Delta). The correct question is not:

> Which one exceptional character occurred?

It is:

> What quotient of the generalized Jacobian captures the coherent character subgroup, and how large is the remaining subset-product discrepancy?

Replace that wall by:

```text
W-JR-T1-GJ-QUOTIENT-CONDITIONED-SUBSET-PRODUCT-LOCAL-LIMIT
```

The critical-seed wall should also be cut. A critical seed remains useful only for:

* choosing a canonical coordinate chart;
* reducing exhaustive search dimension;
* identifying a codimension-one span;
* avoiding noncanonical witness choices.

It is not a counting theorem.

---

## EXACT_NEW_WALL

### First hard wall: minimal apolar degree

Let (H) be an official smooth domain, let (\Delta) be any degree-(\sigma) modulus, and let

[
\alpha_\Delta:H^\circ\to G_{\rm eff}
]

be the boundary map above.

Prove a canonical quotient (\pi:G_{\rm eff}\to Q_{\rm str}) capturing all certified structured characters such that

[
\boxed{
N_{\Delta,j}(b)
\le
\frac{N_{Q_{\rm str},j}(\pi b)}
{|\ker\pi|}
+
C_{\rm prim}
\frac{\binom{|H^\circ|}{j}}{|G_{\rm eff}|}
+
P_{\rm fin}(n,\sigma),
}
]

with explicit finite constants.

The first instance must be

[
\Delta=[0]+(\sigma-1)[\infty],
]

because that instance already contains the known counterpacket.

### Second hard wall: nonminimal apolar degree

```text
W-JR-T1-H2-RATIONAL-PAIR-INVERSE
```

Given coprime (A,B), fully split forms

[
P_i=AU_i+BV_i,
]

and simultaneous low-degree H2 syzygies among the (U_i) and (V_i), prove that a large family forces one of:

1. a common split factor or fixed agreement core;
2. a proper hereditary envelope;
3. a split-rational or Lattes pullback;
4. a degree-(\sigma) generalized-Jacobian quotient on a large subfamily;
5. a quantitatively bounded primitive discrepancy family.

No existing theorem in the repository proves this.

---

## Is (t=1) the correct base case?

Yes, with an important qualification.

* It is the correct **mandatory base case** because it already contains ordinary scalar RS decoding, configuration characters and the product packet.
* Within (t=1), (d=\sigma) is the correct first subcase because it has an exact finite abelian-group formulation.
* It is **not** a sufficient induction base. There is no proved reduction from arbitrary (1<t<\sigma), arbitrary apolar (d>\sigma), or the denominator-free all-line problem to (d=\sigma).
* A proof restricted to (t=1,d=\sigma) would be meaningful but would not solve the MCA challenge.

---

# Minimal theorem package

## MCA challenge

### Asymptotic missing package

The smallest credible missing package is:

**MCA-A — Canonical cover theorem.**
Every excessive affine syndrome line admits a bounded-overlap decomposition into:

* hereditary envelope descendants;
* genus-zero split-rational block systems;
* genus-one Lattes/isogeny systems;
* generalized-Jacobian configuration quotients;
* a primitive residue.

**MCA-B — Primitive local-limit theorem.**
The primitive residue obeys occupancy plus explicit finite discrepancy. Its indispensable subcases are:

1. (t=1,d=\sigma): generalized-Jacobian subset-product local limit;
2. (t=1,d>\sigma): H2 rational-pair inverse;
3. all-denominator assembly in the syndrome formulation.

**MCA-C — Lower/failure matching.**
The current random-anchor/Bessel and quotient lower checkers must be shown to fail every reserve below the proposed (\sigma_{\rm MCA}^*). Most of this is already banked in restricted regimes.

### Additional finite (2^{-128}) package

The asymptotic theorem is insufficient. A finite certificate must give:

[
\begin{aligned}
&\text{occupancy contribution}\
+{}&\text{all quotient-profile contributions}\
+{}&\text{hereditary envelope contribution}\
+{}&\text{primitive discrepancy}\
+{}&\text{tangent and lower-weight contributions}
\le
\left\lfloor q/2^{128}\right\rfloor .
\end{aligned}
]

It must include:

* exact constants, not (n^{o(1)});
* every support weight (e\le j);
* exact field-of-definition and field-transfer conditions;
* exact integer rounding;
* no double charging between character quotients and point-fiber quotients.

## Grand list challenge

### Asymptotic missing package

Only one major new theorem is logically necessary after the banked projection:

**LIST-A — Scalar full-support circuit cover.**
Every low-arity positive-excess circuit is covered by a bounded-overlap union of:

* common-core descendants;
* split-rational/Lattes quotient circuits;
* low-affine-rank polynomial envelopes;
* a primitive circuit discrepancy class.

The banked circuit-hitting theorem then gives

[
L_{\rm sc}
\le
U_{\rm circuit}
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor.
]

The same-field projection theorem transfers this exact threshold to every constant interleaving arity.

### Additional finite package

One must prove

[
U_{\rm circuit}
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor
\le
\left\lfloor q/2^{128}\right\rfloor
]

at the first candidate reserve, with all quotient and field-transfer ledgers evaluated exactly.

---

# Dependency DAG

Legend:

* `[BANKED]` repository theorem-grade or nearly so;
* `[LIKELY]` precise and plausible, but requires independent checking;
* `[UNKNOWN]` genuine open theorem;
* `[DOUBTFUL]` current formulation probably wrong;
* `[FALSE]` explicitly cut by a counterpacket or exact reduction.

```text
GRAND MCA THRESHOLD                                      [UNKNOWN]
├── Exact integer reserve/radius formula                 [BANKED]
├── Lower/failure checker below candidate reserve        [BANKED, restricted]
└── Finite all-line safe-side theorem                    [UNKNOWN]
    ├── Exact syndrome transverse-secant formulation     [BANKED]
    ├── Canonical quotient cover                         [UNKNOWN]
    │   ├── Fixed-partition QAR packing                  [BANKED]
    │   ├── Fixed-core petal bound                       [BANKED]
    │   ├── Genus-zero PGL2 registry                     [LIKELY/partial]
    │   ├── Lattes/isogeny registry                      [UNKNOWN; arithmetic unverified]
    │   └── Bounded total profile weight                 [UNKNOWN]
    ├── Hereditary envelope total-weight theorem         [UNKNOWN]
    ├── Primitive occupancy/discrepancy theorem          [UNKNOWN]
    │   ├── t=1 apolar CI normal form                    [BANKED, audit needed]
    │   ├── d=σ generalized-Jacobian fiber theorem       [PROVED HERE]
    │   ├── Effective-subgroup occupancy correction      [PROVED HERE]
    │   ├── Joint quotient-character charging identity   [PROVED HERE]
    │   ├── Model jet-modulus local limit                [UNKNOWN]
    │   ├── H2/MDS-3-core extraction                     [BANKED, audit needed]
    │   ├── H2 componentwise apolar splitting            [PROVED HERE]
    │   ├── d>σ rational-pair inverse                    [UNKNOWN]
    │   └── all-denominator primitive assembly           [UNKNOWN]
    └── Explicit finite 2^-128 ledger                    [CONDITIONAL]

GRAND INTERLEAVED LIST THRESHOLD                          [UNKNOWN]
├── Exact scalar full-support identity                   [BANKED]
├── Same-field projection at official scale              [BANKED]
├── Full-support circuit-hitting theorem                 [BANKED]
├── Low-arity circuit structural cover                   [UNKNOWN]
│   ├── Common-core shortening                           [BANKED]
│   ├── Quotient circuit charge                          [UNKNOWN]
│   ├── Low-affine-rank envelope charge                  [UNKNOWN]
│   └── Primitive circuit local limit                    [UNKNOWN]
└── Explicit finite 2^-128 ledger                        [CONDITIONAL]

CUT OR FALSE NODES
├── Pure n^(1+o(1)) all-line safe-side target            [FALSE/too narrow]
├── Point-fiber quotient ledger is complete              [FALSE]
├── Critical-seed completion is a weaker theorem         [FALSE]
├── General t>σ compression to low t                     [FALSE]
├── H2-defect itself is a payable structural class       [FALSE]
├── Charge each divisor character separately             [DOUBTFUL]
└── Image size alone controls maximum fiber              [FALSE]
```

---

# Best next theorem-worker prompts

## Prompt 1 — generalized-Jacobian theorem audit

```text
Prove or refute the following exact theorem, including all edge cases.

Let I_s=(A,B) be the apolar complete intersection for a t=1 RS syndrome,
with deg A=sigma and deg B=j. Let Delta=V(A), let
G_Delta=H^0(Delta,O_Delta)^*/F^*, and define the boundary map
alpha_Delta(x)=[(L_x/L_*)|Delta].

Claim: except for the possible singleton j=sigma locator A, the
full-coordinate j-support representations of s are exactly the subsets T
avoiding Supp(Delta) satisfying

    product_{x in T} alpha_Delta(x)=[B/L_*^j].

Also prove the group-order formula and the finite Fourier formula.

Acceptance criteria:
1. Handle nonreduced A and irreducible closed points.
2. Handle evaluation points lying on Delta.
3. Prove independence of the auxiliary form L_*.
4. Handle generator changes B -> cB+AC.
5. State the j=sigma exceptional case exactly.
6. Verify exhaustively over F_7, F_11 and F_17.

Failure criterion:
Produce an explicit apolar CI and split locator for which the claimed
boundary equivalence or full-coordinate implication fails.
```

## Prompt 2 — model jet-modulus local limit

```text
Attack the exact model primitive theorem.

Let n=2^m, H<=F_q^* have order n, and define for j-subsets T

    Phi_sigma(T)
      = (product(T), first sigma-2 high locator coefficients)

equivalently the generalized-Jacobian boundary map for
Delta=[0]+(sigma-1)[infinity].

After charging all quotient-periodic classes at subgroup scales M>sigma-2,
prove an explicit finite bound

    max_b #Phi_sigma^{-1}(b)
      <= C_occ * binom(n,j)/(n q^(sigma-2))
         + P_fin(n,sigma).

First prove the characteristic-zero and stable split-prime versions using
the repository's inverse quotient and Galois-amplification theorems. Then
determine whether the same statement is plausible for polynomial fields.

Acceptance criteria:
1. C_occ and P_fin are explicit.
2. The q/n product packet is included in the main term, not called an error.
3. Quotient classes are assigned disjointly or with a proved overlap bound.
4. The proof covers arbitrary targets b and fixed-density j.
5. The finite statement can be inserted into the 2^-128 ledger.

Failure criterion:
Give an infinite or parameterized family of non-quotient fibers larger than
the displayed scale, with exact fiber cardinality and field/domain data.
```

## Prompt 3 — generalized-Jacobian character classifier

```text
For a degree-sigma modulus Delta on P^1 over F_q and a cyclic evaluation
domain H, classify the pullbacks

    x -> chi(alpha_Delta(x))

for chi in the character group of J_Delta(F_q).

Desired theorem:
Every character belongs to exactly one certified class:
(a) annihilator/effective-image main term;
(b) genus-zero split-rational quotient;
(c) genus-one Lattes/isogeny quotient;
(d) conductor-degenerate toric or local-unit character;
(e) primitive character with an explicit subset-product discrepancy bound.

Do not classify characters separately if they generate one quotient. Produce
the canonical quotient generated by every structured character subgroup.

Acceptance criteria:
1. Treat reduced, nonreduced and nonsplit Delta.
2. State conductors and exceptional triviality conditions exactly.
3. Explain how norms from nonrational closed points enter.
4. Give a finite bound for the total quotient-conditioned contribution.
5. Test every divisor partition of sigma<=5 over fields q<=101.

Failure criterion:
Produce a character whose pullback creates a large fiber but belongs to none
of the proposed structural classes.
```

## Prompt 4 — (d>\sigma) H2 rational-pair inverse

```text
Let I_s=(A,B) be an envelope-free t=1 apolar CI with deg A=d>sigma.
Let P_i=A U_i+B V_i be distinct, squarefree, D-split, full-coordinate
locators. Assume an H2 extraction gives degree-e coefficients C_i, e<sigma,
with

    sum C_i P_i = sum z_i C_i P_i = 0.

First independently prove that these identities split into simultaneous
syzygies on U_i and V_i.

Then prove or refute:

A sufficiently large family forces a large subfamily with one of:
1. a common factor/fixed agreement core;
2. a hereditary envelope;
3. a split-rational or Lattes pullback;
4. a degree-sigma generalized-Jacobian boundary quotient;
5. occupancy-sized residual.

Acceptance criteria:
- quantitative family-size threshold;
- explicit finite charge for every outcome;
- invariant under CI generator shear B -> cB+AC;
- no use of H2-defect as an uncharged exception.

Failure criterion:
Construct a parameterized family of coprime rational pairs with the
simultaneous syzygies, no listed structure, and super-occupancy many split
numerators.
```

## Prompt 5 — computational primitive counterpacket hunter

```text
Write an exhaustive Sage/Python search for t=1 apolar packets over
q<=101, n<=16.

For every nonzero syndrome:
1. compute the apolar CI degrees;
2. enumerate full-coordinate split degree-j locators;
3. calculate external colors;
4. construct the generalized-Jacobian boundary map when d=sigma;
5. compute effective subgroup, complete fiber histogram and Fourier spectrum;
6. when d>sigma, search for minimal H2 syzygies and classify rational-pair
   relations.

Test moduli:
3*infinity, 0+2*infinity, 0+1+infinity,
an irreducible quadratic plus a rational point,
and an irreducible cubic.

Output any packet exceeding
    C * binom(n,j)/|G_eff| + 3n
for C=1,2,4, after all known quotient/core tags.

Acceptance:
Reproducible JSON plus a human-readable certificate for every extremal case.

Failure of the conjectured theorem:
One explicit quotient-free, envelope-free, color-distinct packet above the
target, including all polynomial and support data.
```

## Prompt 6 — scalar list circuit cover

```text
Prove or refute W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER.

For scalar RS lists at reserve sigma, every circuit of arity at most
ceil(r/sigma) should admit a canonical assignment to:
1. common-core shortening;
2. split-rational/Lattes quotient;
3. low-affine-rank polynomial envelope;
4. primitive discrepancy.

Prove an explicit bound U_circuit on a transversal hitting every circuit,
sufficient to make

    U_circuit + floor((r-1)/sigma) <= floor(q/2^128).

Acceptance:
All overagreement layers are handled through actual reserve tau(P), and
the theorem is stated for actual full-support codewords, not padded supports.

Failure:
An official-domain circuit family avoiding every container and exceeding the
finite target.
```

---

# Kill tests and counterexample searches

## Immediate numerical regression tests

### Test A: ambient occupancy is false

Take

[
q=17,\qquad H=\langle9\rangle,\qquad |H|=8,\qquad j=4,\qquad \sigma=2.
]

The product-fiber sizes are

[
8,8,8,8,9,9,10,10.
]

Thus:

* ambient generalized-Jacobian average:

  [
  \binom84/(q-1)=70/16=4.375;
  ]

* effective-subgroup average:

  [
  \binom84/|H|=70/8=8.75;
  ]

* maximum fiber: (10).

Any theorem retaining (q^{\sigma-1}) rather than (|G_{\rm eff}|) is already dead in this toy case.

### Test B: product-plus-jet occupancy

Take

[
q=97,\qquad H=\langle8\rangle,\qquad |H|=16,
]

with

[
j=6,\quad \sigma=3,\quad a=10,\quad k=7.
]

Bucket by:

* the product of (T);
* the coefficient (d_9) of the complementary locator.

There are exactly

[
16\cdot97=1552
]

possible buckets, all occupied. Their average size is

[
8008/1552\approx5.1598,
]

and the maximum is (9).

This should be a permanent regression test for the model local-limit theorem.

## Most likely false proposed statements

1. **“Every generalized-Jacobian fiber is within a constant of its average.”**
   Likely false without quotient extraction.

2. **“Low image size of one character bounds the corresponding fiber by its average.”**
   False. Image size gives only an average over quotient targets, not a maximum.

3. **“Every H2-defective family is quotient structured.”**
   False in random occupancy models.

4. **“The (d>\sigma) branch compresses to (d=\sigma).”**
   Very doubtful. The variable rational pairs carry information absent at (d=\sigma).

5. **“Point quotients plus one product character are enough.”**
   Likely false. Mixed toric/local-unit character subgroups and nonsplit divisor norms must be tested.

6. **“A bounded number of critical seeds pays the packet.”**
   False unless a separate bounded-overlap theorem is proved.

## Symbolic checks

For every small-field CI:

* verify (P_T\in(I_s)_j\iff s\in V_T);
* verify full support (\iff\gcd(U_T,V_T)=1);
* check the generalized-Jacobian product equation;
* compare the support fiber to the distinct-color fiber;
* test invariance under (B\mapsto cB+AC);
* calculate (G_{\rm eff}), not merely (G_\Delta);
* search for Fourier spikes outside the known structured character subgroup.

For (d>\sigma):

* enumerate simultaneous syzygies of the (U_i,V_i);
* reject any proposed inverse statement if a family survives with no common factor, no fixed core, no rational pullback and no degree-(\sigma) boundary quotient.

---

# Verification and formalization plan

## Claims to verify first

1. **Cycle 60 product/divisor packet.**

   * locator bucket size;
   * triangular coefficient relation;
   * exact full agreement support;
   * (\sigma)-separation;
   * external-color extraction;
   * envelope noncontainment;
   * giant finite arithmetic.

2. **Cycle 60 (t=1) apolar theorem.**

   * Artinian Gorenstein/CI derivation;
   * locator criterion;
   * envelope dichotomy;
   * direct-sum slice;
   * full-coordinate gcd criterion;
   * pairwise separation;
   * generator-gauge invariance.

3. **Cycle 60 H2 theorem.**

   * basepoint-free rank claim after peeling;
   * splitting-degree sum;
   * Macaulay excess formula;
   * existence of a nontrivial high-degree summand;
   * exact (3)-core local argument;
   * the “at most (n) peeled slopes” accounting.

4. **Cycle 60 Lattes packets.**
   These should not enter a theorem statement until the curve orders, isogeny fibers, field admissibility and transverse slope counts are independently reproduced.

5. **Scalar projection and circuit-hitting theorem.**
   They are simpler but foundational for the list branch.

## Scripts/checkers

```text
verify_apolar_ci.sage
verify_generalized_jacobian_fiber.sage
scan_gj_subset_fibers.py
verify_divisor_norm_packet.sage
verify_h2_core.sage
search_rational_pair_packets.sage
verify_fixed_partition_qar.py
verify_scalar_circuits.sage
verify_lattes_31.m
verify_lattes_113.m
finite_prize_ledger.py
```

`finite_prize_ledger.py` should accept

[
(n,k,q_{\rm gen},q_{\rm line},\sigma)
]

and return:

* (T_F=\lfloor q_{\rm line}/2^{128}\rfloor);
* tangent floor;
* Bessel/entropy lower certificate;
* every quotient-profile contribution;
* occupancy using (|G_{\rm eff}|);
* envelope and primitive finite floors;
* final pass/fail comparison.

## TeX promotion policy

Promote now, after independent review:

* exact generalized-Jacobian fiber theorem;
* group-order formula;
* Fourier formula;
* joint quotient-character charging identity;
* H2 componentwise apolar splitting.

Promote only after computational and human review:

* Cycle 60 product packet;
* apolar full-coordinate criterion;
* H2 excess formula;
* fixed-partition QAR bounds.

Do not promote as theorems:

* the full primitive local limit;
* the Lattes packets before arithmetic verification;
* any character trichotomy without a complete nonsplit/nonreduced audit;
* any H2-defect “container” that lacks a finite charge.

---

# Resource allocation

## Round 1: nine theorem workers

| Worker | Assignment                                                                                                       |
| ------ | ---------------------------------------------------------------------------------------------------------------- |
| 1      | Independently prove and TeX the generalized-Jacobian fiber theorem                                               |
| 2      | Prove the stable-field model theorem for ([0]+(\sigma-1)\infty) using the banked dyadic inverse quotient theorem |
| 3      | Exhaustive generalized-Jacobian fiber and Fourier counterexample search                                          |
| 4      | Classify characters for arbitrary reduced/nonreduced degree-(\sigma) moduli                                      |
| 5      | Attack the (d>\sigma) H2 rational-pair inverse                                                                   |
| 6      | Independently audit Cycle 60 apolar, H2 and product-packet proofs                                                |
| 7      | Verify the Lattes packets and construct the genus (0/1) quotient registry                                        |
| 8      | Work on the scalar full-support circuit cover                                                                    |
| 9      | Maintain the exact finite ledger and act as adversarial referee                                                  |

The local Fable/Codex loop should:

* formalize finite abelian Fourier identities;
* check the divisor exact sequence and polynomial divisibility arguments;
* generate exhaustive Sage cases;
* lint every proposed theorem against the finite ledger;
* reject any upper theorem whose “exception” has no exact charge.

## Round 2 allocation

If the model generalized-Jacobian theorem survives:

* 3 workers on the polynomial-field model local limit;
* 2 workers on arbitrary moduli and mixed toric/local-unit characters;
* 2 workers on the (d>\sigma) rational-pair inverse;
* 1 worker on scalar circuits;
* 1 worker on finite assembly and formalization.

If the model theorem fails:

* stop attempting the broad primitive theorem;
* assign 4 workers to classify the new packet;
* assign 2 to expand the generalized-Jacobian quotient ledger;
* assign 1 to recompute candidate reserves;
* retain 1 on scalar circuits and 1 as meta-referee.

## Human/PRZ priority

The human check should proceed in this order:

1. generalized-Jacobian equivalence and the effective-subgroup correction;
2. Cycle 60 product-packet proof and finite arithmetic;
3. apolar CI and H2 proofs;
4. model-modulus stable-field corollary;
5. Lattes arithmetic;
6. only then a broad primitive inverse theorem.

Do not spend human time polishing a general trichotomy before the model modulus has survived the finite kill tests.

---

# CONDITIONAL

For the model modulus

[
\Delta=[0]+(\sigma-1)[\infty],
]

the repository’s characteristic-zero dyadic inverse quotient theorem already gives a partial positive result.

Two locators in the same generalized-Jacobian fiber have equal:

* first (\sigma-2) nonleading high coefficients;
* product.

Equality of the first (\sigma-2) elementary symmetric functions alone implies quotient periodicity over characteristic zero. Therefore, if (M_0) is the least power of two exceeding (\sigma-2), every characteristic-zero model fiber has size at most

[
2^{n/M_0}.
]

The same conclusion holds in the repository’s stable split-prime range

[
p>
\exp!\left(
C\frac{n\log(2n)}{\sigma-2}
\right).
]

This is a real base-case theorem, but it does not reach the polynomial-field regime relevant to the sharp corrected reserve. Generic Weil bounds are unlikely to close that gap: when the evaluation subgroup is much smaller than (\sqrt q), full-field character-sum bounds are too weak.

---

# PLAN

The shortest realistic primitive route is:

1. **Bank the generalized-Jacobian theorem.**
2. **Replace ambient occupancy by effective-subgroup occupancy.**
3. **Solve the model modulus**
   [
   [0]+(\sigma-1)[\infty]
   ]
   first, with the known product packet built into the main term.
4. **Classify structured character subgroups jointly**, not character by character.
5. **Use H2 only in the (d>\sigma) branch.**
6. **Exploit the componentwise rational-pair syzygies.**
7. **Attempt an all-(t) assembly only after both (t=1) subbranches are controlled.**
8. In parallel, keep the scalar list circuit branch independent.

The next genuinely hard lemma is therefore:

```text
W-JR-T1-GJ-QUOTIENT-CONDITIONED-SUBSET-PRODUCT-LOCAL-LIMIT
```

for

[
\Delta=[0]+(\sigma-1)[\infty].
]

The precise missing theory blocking the full route is not “more algebraic manipulation.” It is a finite-field local-limit/inverse theorem for large fixed-weight subset-product fibers on generalized Jacobians of low conductor, followed by a simultaneous rational-pair inverse theorem for (d>\sigma). Until both exist, the primitive MCA branch is not solved; until the scalar circuit cover also exists, neither grand challenge is solved.
