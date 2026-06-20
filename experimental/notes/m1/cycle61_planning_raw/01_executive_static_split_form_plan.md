# Executive verdict

The full prize problem is **not close**. The repository has theorem-grade lower bounds, exact reformulations, and several useful structural reductions. It does not have either safe-side master theorem.

My assessment:

| Question                                                                     | Verdict                                                                                                                                   | Confidence   |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| Is the grand list challenge plausibly solvable from this program?            | Yes, but only after replacing the broad circuit taxonomy by a canonical static split-form inverse theorem. Medium-range.                  | Moderate     |
| Is the grand MCA challenge plausibly solvable from this program?             | Plausible, but it remains a harder dynamic inverse problem with an additional hereditary-envelope obstruction.                            | Moderate-low |
| Is the current Cycle 60 route close to a solution?                           | No. It is still missing hard inverse theorems.                                                                                            | High         |
| Will a genus-zero/genus-one/higher-genus quotient catalogue close the route? | Very unlikely. That is the wrong organizing wall.                                                                                         | High         |
| Can the exact answers be four constants depending only on the four rates?    | No. The finite answer is code-specific: it depends on (n,q,L,k), generated and line fields, divisibility, and realized support structure. | High         |

The route has expanded horizontally after every counterpacket:

[
\text{monomial}
\to \text{Möbius/split-rational}
\to \text{Lattès}
\to \text{configuration characters}
\to \text{H2 cores}.
]

That is evidence that the exception taxonomy is not converging. The project should narrow to two canonical inverse problems:

1. a **static split-form linear-section theorem** for scalar lists;
2. a **dynamic catalecticant-pencil theorem** for MCA lines.

Everything else should be treated as proof technology or as a falsification test for those two theorems.

---

# AUDIT

The archive checksum matches the supplied SHA-256 value. I inspected the Cycle 58–61 audits, all nine Cycle 60 returns, the route-state documents, and the relevant parts of the main TeX files.

The following claims are genuinely banked or very close to bankable:

* exact syndrome/transverse-secant formulation of MCA;
* exact full-support syndrome formulation of scalar lists;
* same-field Bessel–Paley MCA failure theorem;
* interleaved-to-scalar projection at the official (2^{-128}|F|) scale;
* information-set petal bound;
* H2-core extraction as a structural certificate;
* (t=1) apolar complete-intersection normal form;
* scalar full-support circuit-transversal reduction;
* exact integer reserve-to-radius extraction.

The following audit corrections are important.

1. The Cycle 60 fixed-partition packing theorem does **not** cover either Lattès packet as written. It assumes an equipartition, (M\mid k), and defect (d=\sigma). The degree-31 packet has
   [
   2079=2+67\cdot31,
   ]
   and the degree-113 packet has
   [
   4209=28+37\cdot113.
   ]
   Their full fibers also cover only part of the domain. A residual, partial-block packing lemma is required.

2. The scalar list problem has a canonical graded apolar identity that is stronger and cleaner than the present route board suggests. It reduces the entire scalar list—including overagreement—to counting completely split forms in the graded slices of one binary complete intersection.

3. The Cycle 60 divisor-norm phenomenon is not an arbitrary new exception family. In the minimal apolar slice, the relevant norm character is forced by an exact resultant identity. This gives a much narrower route than “classify (\chi_R) for arbitrary rational functions (R).”

4. I independently checked the core arithmetic in both Lattès notes:

   * for the degree-31 example, the curve order (8153=31\cdot263), the displayed multiples of (G), the kernel (x)-coordinates, and the discriminant/character sum are correct;
   * for the degree-113 example, (9^{16384}=-1\bmod65537), the curve order is (65540), and the Gaussian factorization producing norm (113) is correct.

   The explicit Vélu/Lattès maps, complete fiber distributions, finite-field choices, and all collision exclusions still require Sage verification. The packets are not yet publication-grade.

---

# PROOF

## BANKABLE_LEMMA — residual partial-block packing

Let (C=\operatorname{RS}[F,L,k]), (r=n-k), and (j=r-\sigma). Let

[
\mathcal B={B_y:y\in\Omega}
]

be (N) pairwise disjoint (M)-subsets of (L); they need not cover (L).

Suppose an envelope-free affine syndrome line has a set (Z) of distinct transverse bad slopes with selected witnesses

[
S_z=D_z\sqcup\bigcup_{y\in A_z}B_y,
]

where

[
|D_z|=d,\qquad |A_z|=b,\qquad d+Mb=k+\sigma,
]

and (D_z) is disjoint from the selected blocks.

For (d\ge1), set

[
h=\max{1,d-\sigma+1}.
]

For (X\subseteq L), let (m(X)) be the number of blocks in (\mathcal B) meeting (X). Then

[
\boxed{
|Z|
\le
\frac1{\binom dh}
\sum_{X\in\binom Lh}
\binom{N-m(X)}b
\le
\frac{\binom nh}{\binom dh}\binom Nb.
}
]

If the blocks equipartition (L), this sharpens to

[
\boxed{
|Z|
\le
\frac{\binom nh}{\binom dh}\binom{N-1}b.
}
]

For (d=0),

[
\boxed{|Z|\le\binom Nb.}
]

### Proof

Count pairs ((z,X)) with (X\in\binom{D_z}{h}), and map

[
(z,X)\longmapsto (X,A_z).
]

If two distinct slopes (z,z') have the same image, their supports share the same selected blocks and satisfy

[
|D_z\setminus D_{z'}|
\le d-h\le \sigma-1.
]

Their complementary error supports therefore have union of size at most

[
j+\sigma-1=r-1.
]

The two distinct points of the syndrome line lie in the corresponding two column spans, so the entire syndrome plane lies in the span of their union, a proper envelope. This contradicts envelope-freeness. The map is injective.

For fixed (X), the selected blocks must avoid every block meeting (X), giving at most (\binom{N-m(X)}b) choices. The result follows.

For (d=0), each chosen block set determines one error support. A transverse affine line meets its column span in at most one point.

This repairs the Cycle 60 packing statement and covers both residual Lattès profiles. It does not solve the weighted sum over many inequivalent block systems.

---

## BANKABLE_LEMMA — scalar graded-apolar list identity

Let

[
C=\operatorname{RS}[F,L,k],\qquad r=n-k,
]

and let (s\ne0) be a syndrome. After standard nonzero GRS column rescaling, use moment-curve parity-check columns. Let (S=F[X_0,X_1]), identify (s) with a functional on (S_{r-1}), and define its apolar ideal (I_s).

Then

[
I_s=(A,B),
]

where (A,B) are coprime homogeneous forms with

[
\deg A=d,\qquad \deg B=b,\qquad d\le b,\qquad d+b=r+1.
]

For an error support (E\subseteq L), (|E|=e<r), let (P_E) be its homogeneous locator. Then

[
s\in V_E
\quad\Longleftrightarrow\quad
P_E\in (I_s)_e.
]

Every such locator has a unique representation

[
P_E=A,U+B,V,
]

with

[
\deg U=e-d,\qquad \deg V=e-b,
]

where negative-degree spaces are zero.

The syndrome representation on (E) has every coordinate nonzero if and only if

[
\boxed{\gcd(U,V)=1,}
]

using the convention (\gcd(U,0)=U).

Consequently, for target error radius

[
j=r-\sigma,
]

the exact scalar list for syndrome (s) is the number of monic, squarefree, completely (L)-split forms

[
A,U+B,V\in (I_s)_e,\qquad 0\le e\le j,
]

with (\gcd(U,V)=1).

In particular:

* if (e<b), a full-support representation is possible only when (e=d) and (P_E) is a scalar multiple of (A);
* if (d\le\sigma), then (b\ge j+1), so the list has size at most one;
* the first nontrivial primitive stratum is
  [
  d=\sigma+1,\qquad b=j.
  ]

In that first stratum, apart from the possible minimal locator (A), every listed boundary locator is

[
\boxed{P_E=A,U+cB,\qquad c\in F^\times.}
]

### Proof of the full-coordinate criterion

The coefficient at (x\in E) vanishes exactly when (s\in V_{E\setminus{x}}), equivalently

[
P_E/\ell_x\in I_s,
]

where (\ell_x) is the corresponding linear factor.

If

[
P_E/\ell_x=A,U'+B,V',
]

then multiplying by (\ell_x) and using uniqueness of the degree-(e) decomposition gives

[
U=\ell_xU',\qquad V=\ell_xV'.
]

Thus the coefficient at (x) vanishes exactly when (\ell_x\mid\gcd(U,V)). Since (P_E) is completely split, every nonconstant common factor of (U,V) supplies such a root.

This theorem should replace the scalar circuit cover as the **minimal logical formulation** of the list challenge. The circuit machinery remains potentially useful for proving the resulting split-form bound.

---

## BANKABLE_LEMMA — the configuration character is a canonical resultant

In the minimal primitive stratum, assume (A,B,P_E) are monic and

[
P_E=A,U+cB,\qquad
\deg A=d,\quad \deg B=\deg P_E=e,\quad c\ne0.
]

If (E) is the root set of (P_E), then

[
\boxed{
\prod_{x\in E}A(x)
==================

(-1)^{de}c^d\operatorname{Res}(A,B).
}
]

Indeed,

[
\operatorname{Res}(P_E,A)
=========================

(-1)^{de}\operatorname{Res}(A,P_E),
]

and modulo (A),

[
P_E\equiv cB.
]

Hence

[
\operatorname{Res}(A,P_E)=c^d\operatorname{Res}(A,B).
]

For the general slice (P_E=AU+BV),

[
\operatorname{Res}(P_E,A)
]

is, up to the fixed (A,B) factor, the norm/resultant of (V) modulo (A). If (A) and (V) share a root, this is precisely the fixed-defect branch.

This is the correct narrowing of the Cycle 60 configuration-character ledger:

[
\boxed{
\text{canonical apolar resultants/subresultants},
\quad\text{not arbitrary }\chi_R\text{ for arbitrary }R.
}
]

Without a complexity restriction of this kind, allowing arbitrary divisor-norm characters is vacuous: interpolation permits essentially arbitrary functions on (L).

---

# COUNTERPACKET

## Official-rate strengthening of the Cycle 60 product-character packet

The divisor-norm obstruction can be placed at an exact official rate without the nonofficial value of (k) used in Cycle 60.

Take

[
p=2^{31}-1,\qquad F=\mathbb F_{p^8},\qquad q=p^8,
]

and let (H\le F^\times) be the subgroup of order

[
n=2^{34}.
]

The congruences

[
p^2\equiv1-2^{32},\qquad
p^4\equiv1-2^{33}\ne1,\qquad
p^8\equiv1\pmod{2^{34}}
]

show that (H) generates (F).

Use the exact official rate

[
k=n/8=2^{31}
]

and set

[
\sigma=38,083,574.
]

Then

[
a=k+\sigma=2,185,567,222.
]

Writing (x=a/n), direct interval evaluation gives

[
nH_2(x)-(\sigma-1)\log_2q<51.
]

Thus the boundary occupancy term satisfies

[
\boxed{
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}<2^{51}.
}
]

The standard type lower bound

[
\binom na\ge \frac{2^{nH_2(a/n)}}{n+1}
]

gives

[
\boxed{
\frac{\binom n{k+\sigma}}{nq^{\sigma-2}}>2^{230}.
}
]

Moreover,

[
q-n>3\cdot2^{246},
\qquad
2k=2^{32},
]

so the external-color extraction term satisfies

[
\left\lfloor\frac{q-n}{2k}\right\rfloor
\ge3\cdot2^{214}.
]

The Cycle 60 product-character construction therefore gives at least

[
\boxed{|Z|\ge2^{215}}
]

distinct envelope-free (t=1) MCA slopes.

But

[
q<2^{248},
\qquad
T_q=\left\lfloor q/2^{128}\right\rfloor<2^{120}.
]

Hence this exact rate-(1/8) instance is unsafe by at least (95) bits while its occupancy term is below (2^{51}).

This establishes, in the official finite regime:

[
\boxed{
\text{occupancy alone is false even at an exact prize rate.}
}
]

It does not establish that this packet evades every possible support-theoretic block container. Its value is narrower and decisive: the configuration/resultant term is genuinely load-bearing, not an artifact of the nonofficial rate in the Cycle 60 example.

A short interval-arithmetic certificate should be written before promotion.

---

# ROUTE_CUT

1. **Stop treating low-genus classification as the main quotient theorem.**
   The split-fiber estimate
   [
   s_R|G_R|\le q_0+1+2g_R\sqrt{q_0}
   ]
   has a main term (q_0/|G_R|) for every genus. Genus (g\ge2) does not make a map a small “finite discrepancy” exception. Higher-genus maps can still have many full split fibers. Genus is useful metadata, not the container definition.

2. **One verified Lattès packet is enough.**
   Its purpose is to kill a genus-zero-only classifier. Building an exhaustive Lattès registry before proving a weighted support-partition theorem is low expected value.

3. **The Cycle 60 split-rational registry is still too syntactic.**
   What matters is the total support-profile weight required by one line, not the number or classification of rational maps producing the same blocks.

4. **The current divisor-norm proposal is too broad.**
   “Allow (\chi_R(T)=\prod_{x\in T}R(x))” for unrestricted (R) can encode essentially arbitrary support statistics. The route needs a theorem proving that only bounded-complexity canonical apolar resultants or subresultants arise.

5. **H2-defect is not an upper-bound term.**
   H2 extraction is a real structural lemma. But both random occupancy packets and algebraically structured packets can be H2-defective. Calling the remainder “H2-defective” does not charge it.

6. **Critical-seed completion is not a smaller theorem.**
   Once coefficients are included, a seed fixes the syndrome and its completions are the original colored fiber minus the seed.

7. **Do not make the circuit cover and the apolar inverse simultaneous mandatory walls.**
   The scalar challenge logically reduces to the static graded-apolar split-form count. Circuit transversals are one possible proof mechanism or independent counterexample scanner.

8. **No more denominator-stratum assembly.**
   A theorem proved only for (t=\sigma), or only for (t\le\sigma), cannot solve MCA. The denominator-free syndrome/catalecticant pencil must remain the global object.

9. **An (n^{1+o(1)}) statement is not a finite certificate.**
   At the official rates, (n\le2^{44}). Even (n^3) can exceed (2^{128}), while the actual target can be much smaller than (2^{128}). Every polynomial floor needs its degree and constant.

---

# EXACT_NEW_WALL

The route should be reduced to the following three walls.

## 1. Static split-form inverse — the list wall

For a smooth domain (L), a binary complete intersection

[
I=(A,B),\qquad \deg A+\deg B=r+1,
]

and (j=r-\sigma), bound

[
\mathfrak L_L(A,B;j)
====================

\sum_{e=0}^j
#\left{
\begin{array}{l}
P=AU+BV\text{ monic, squarefree and completely }L\text{-split},\
\gcd(U,V)=1
\end{array}
\right}.
]

This is exactly the scalar list problem. The first nontrivial case is

[
\deg A=\sigma+1,\qquad \deg B=j,
]

where the boundary forms are

[
P=AU+cB.
]

The resultant identity shows exactly which configuration character must be handled.

## 2. Dynamic split-form pencil inverse — the MCA wall

For an affine syndrome pencil

[
s_z=u+zv,
]

let (I_{s_z}) be its apolar/catalecticant ideal. Count the values (z) for which the degree-(j) slice contains a full-support (L)-split locator, excluding contained incidences.

After removing proper envelopes, the desired theorem must prove

[
|\operatorname{Bad}*\sigma(\ell)|
\le
\left\lceil
C*{\rm occ}\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
\right\rceil
+
Q_{\rm stat}
+
D_{\rm prim},
]

where (Q_{\rm stat}) is a bounded-complexity support-statistic term incorporating:

* realized partial block systems;
* canonical apolar resultant/norm fibers;
* their hereditary restrictions.

The theorem must bound the **total mass on one line**, not classify one packet at a time.

## 3. Hereditary potential theorem

The exact shortening operation is banked. What is missing is a potential function proving that all children of an enveloped line have bounded total charge.

A termination proof is insufficient. The theorem must control total weight under branching.

These are the real hard inverse theorems. The eight Cycle 61 wall names are subcases or attempted proof mechanisms for these three.

---

# CONDITIONAL — minimal theorem package

## Grand MCA challenge

### Logical minimum

For each allowed (C) and reserve (\sigma):

1. **MCA-UPPER**
   [
   M_C(\sigma)\le U_C^{\rm MCA}(\sigma)
   ]
   with an explicit integer (U_C^{\rm MCA}(\sigma)).

2. **MCA-LOWER at the previous reserve**
   [
   M_C(\sigma-1)>T_F,
   \qquad
   T_F=\left\lfloor |F|/2^{128}\right\rfloor.
   ]

3. Exact monotonicity and integer threshold extraction.

### Realistic asymptotic package

The smallest credible decomposition of MCA-UPPER is:

* **MCA-STAT:** bounded total weight of all realized block and canonical resultant/norm structures on one envelope-free line;
* **MCA-PRIM:** conditional local limit for the remainder;
* **MCA-HER:** bounded hereditary shortening potential.

The Bessel–Paley lower theorem is already sufficient whenever it exceeds the target. Explicit quotient, Lattès, or configuration packets cover reserves where it does not.

### Finite (2^{-128}) package

One needs exact integers

[
Q_{\rm stat},\quad D_{\rm prim},\quad E_{\rm her},\quad C_{\rm occ}
]

such that

[
\boxed{
U_C^{\rm MCA}(\sigma)
=====================

\max\left{
E_{\rm her},
\left\lceil
C_{\rm occ}\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
\right\rceil
+
Q_{\rm stat}
+
D_{\rm prim}
\right}
\le T_F.
}
]

The current `Q_split` is too narrow; it must be replaced by (Q_{\rm stat}).

---

## Grand list challenge

### Logical minimum

1. Exact scalar full-support identity — banked.
2. Interleaved projection theorem — banked.
3. One uniform static split-form upper theorem:
   [
   \mathfrak L_L(A,B;j)\le U_C^{\rm list}(\sigma)
   ]
   for every apolar complete intersection.
4. A matching list larger than (T_F) at the previous reserve.
5. Exact threshold extraction.

No independent interleaving theorem remains in the same-field official regime.

### Realistic asymptotic package

A static inverse theorem should bound

[
\mathfrak L_L(A,B;j)
]

by:

* the random/coset-volume main term
  [
  \frac1{q^r}
  \sum_{e=0}^j\binom ne(q-1)^e;
  ]
* explicit canonical resultant/block structures;
* a finite primitive discrepancy term.

Common-core descent and circuit transversals can be used internally, but they are not additional logical inputs.

### Finite (2^{-128}) package

The theorem must produce an explicit integer

[
U_C^{\rm list}(\sigma)\le T_F.
]

If (q<2^{128}), then (T_F=0), while a worst-case scalar list always has at least one codeword. Thus the list challenge is meaningful only once the field is large enough that (T_F\ge1).

At (q\le2^{256}),

[
\binom{T_F+1}{2}<q,
]

so

[
L_m(\sigma)\le T_F
\quad\Longleftrightarrow\quad
L_1(\sigma)\le T_F
]

for every interleaving arity (m).

---

## Exact radius extraction

Let (\widehat\sigma) be the smallest integer reserve for which the relevant numerator is at most (T_F). Then the largest safe grid radius is

[
1-\rho-\frac{\widehat\sigma}{n}.
]

The supremal real transition is

[
\boxed{
\delta_C^*
==========

1-\rho-\frac{\widehat\sigma-1}{n},
}
]

with that endpoint itself unsafe when (\widehat\sigma) is minimal.

This must be done code by code. A rate-only asymptotic reserve does not determine the prize answer.

---

# Dependency DAG

```text
MCA-EXACT-THRESHOLD                                              [unknown]
├── integer threshold extraction                                [already banked]
├── previous-reserve failure
│   ├── Bessel–Paley same-field theorem                          [already banked]
│   └── explicit quotient/configuration packet when BP is weak  [likely/instance-dependent]
└── MCA-UPPER                                                    [unknown]
    ├── syndrome transverse-secant equivalence                   [already banked]
    ├── envelope-free/enveloped dichotomy                        [already banked]
    ├── structured support-statistic mass theorem                [unknown]
    │   ├── equipartition fixed-defect packing                    [already banked]
    │   ├── residual partial-block packing                        [likely]
    │   ├── global weighted partition registry                   [unknown]
    │   ├── canonical apolar resultant ledger                    [likely]
    │   ├── arbitrary divisor-norm registry                      [false/vacuous]
    │   ├── genus-zero-only registry                             [false]
    │   ├── genus-zero-plus-genus-one registry as complete       [false]
    │   └── higher-genus = small discrepancy                     [false as stated]
    ├── hereditary shortening total-weight theorem               [unknown, doubtful]
    └── primitive catalecticant-pencil local limit               [unknown, hard]
        ├── H2-core extraction                                   [already banked]
        ├── H2-defect automatically chargeable                   [false]
        ├── critical seed gives a smaller completion problem     [false]
        └── conditional support-statistic local limit            [unknown]

LIST-EXACT-THRESHOLD                                             [unknown]
├── scalar full-support syndrome identity                        [already banked]
├── scalar graded-apolar identity                                [likely]
├── interleaved projection at prize scale                        [already banked]
├── static split-form inverse                                    [unknown, hard]
│   ├── minimal generator slice d = sigma + 1                    [unknown]
│   ├── canonical resultant character                            [likely]
│   ├── higher V-degree induction/subresultants                  [unknown]
│   ├── common-factor descent                                    [already banked in equivalent forms]
│   └── circuit-transversal route
│       ├── circuit hitting reduction                            [already banked]
│       └── global low-arity circuit cover                       [unknown]
├── previous-reserve list lower bound
│   ├── generated-field entropy                                  [already banked in stated regimes]
│   ├── quotient packets                                         [already banked in stated regimes]
│   └── exact matching at every candidate reserve                [unknown]
└── finite integer certificate                                   [likely once upper theorem exists]

UNIVERSAL MCA CAP
└── imported Crites–Stewart conversion                           [unknown until independent audit]
```

---

# PLAN — best next theorem-worker prompts

## Prompt 1 — minimal apolar split-form inverse

```text
TITLE: W-LIST-APOLAR-MINIMAL-GENERATOR-INVERSE

Work only from the repository and the following exact reduction.

Let C=RS[F,L,k], r=n-k, j=r-sigma. Let a nonzero scalar
syndrome have apolar ideal I=(A,B), with

deg A = sigma+1,
deg B = j,
gcd(A,B)=1.

Apart from a possible minimal locator A, every full-support boundary
error locator is uniquely

P = A U + c B,

where deg U=j-sigma-1 and c in F^×, and P must be monic,
squarefree, and split completely over L.

Prove a uniform finite upper theorem for the number of such P on
official smooth domains, or construct an official-rate counterpacket.

The desired proof may use the exact resultant identity

prod_{x in roots(P)} A(x)
  = (-1)^((sigma+1)j) c^(sigma+1) Res(A,B).

A successful structural theorem must give a global count, with explicit
integer constants, after separating:
(1) common/fixed factors;
(2) realized partial-block pullbacks;
(3) canonical low-image resultant/norm fibers;
(4) a primitive discrepancy term.

ACCEPTANCE:
- An explicit bound uniform in the syndrome and valid for all full-support
  forms in this stratum; or
- an explicit counterpacket with an official rate, q<2^256, k<=2^40,
  exact full support, and size > floor(q/2^128).

FAILURE:
- Merely restating the apolar normal form;
- bounding raw split supports without the full-coordinate condition;
- classifying one packet without a total bound;
- introducing arbitrary norm characters with no degree/complexity bound.
```

## Prompt 2 — canonical resultant-character completeness

```text
TITLE: W-APOLAR-RESULTANT-CHARACTER-COMPLETENESS

Let I=(A,B) be a binary apolar complete intersection and let

P_i = A U_i + B V_i

be a family of monic squarefree L-split forms with gcd(U_i,V_i)=1.
Assume deg V_i=h is fixed and small relative to sigma.

Prove or refute the following exact inverse statement:

After stratifying by G_i=gcd(A,V_i), every family larger than the
occupancy scale has a large subfamily for which either

(a) the residual supports are unions of blocks of one realized
    split-rational partial block system; or
(b) the canonical norm map
      V -> Res(A,V)
    or a bounded list of canonical subresultants has image smaller
    than the generic q^(h+1) scale.

The theorem must bound the number and total entropy of the canonical
statistics it outputs. Arbitrary rational functions R are disallowed.

ACCEPTANCE:
- A proved trichotomy with bounded description complexity and a finite
  profile charge; or
- a concrete fourth mechanism, preferably already for h=0 or h=1,
  with exact finite data.

FAILURE:
- Calling every rich family a configuration-character packet;
- outputting a statistic chosen after seeing the family without a
  complexity bound;
- a per-character estimate with no global aggregation theorem.
```

## Prompt 3 — weighted partial-block registry

```text
TITLE: W-MCA-WEIGHTED-PARTIAL-BLOCK-REGISTRY

Use the residual partial-block packing theorem:

For one partial block system B={B_y}, witnesses
S_z=D_z disjoint-union union_{y in A_z} B_y,
and h=max(1,d-sigma+1),

|Z_B| <= binom(n,h)/binom(d,h) * binom(N,b).

Prove or refute a one-line weighted registry theorem.

For every envelope-free affine syndrome line, let P(line) be a
canonical minimal collection of inequivalent realized partial block
systems needed to cover all rich block-structured slopes. Prove

sum_{Pi in P(line)} weight(Pi)
 <= n^O(1) * max_Pi weight(Pi),

with a polynomial degree and constant small enough for the finite
2^-128 ledger.

The definition must identify block systems by their actual full blocks,
not by a rational-map formula or monodromy label.

ACCEPTANCE:
- A global weighted bound with an explicit canonicalization/refinement rule;
  or
- one envelope-free official or scalable line whose minimum weighted
  cover violates every proposed polynomial factor.

FAILURE:
- Classifying maps one at a time;
- counting syntactically distinct maps that induce the same blocks;
- assuming M divides k or that the full blocks cover L;
- treating genus >=2 as automatically negligible.
```

## Prompt 4 — hereditary envelope potential

```text
TITLE: W-MCA-HEREDITARY-ENVELOPE-POTENTIAL

Start from the exact Cycle 59/60 shortening operation for a minimal
proper syndrome envelope. Construct a numerical potential Phi(n,k,sigma)
such that:

1. every child has the same reserve sigma;
2. internal slopes are charged by the exact linear cap;
3. the sum of Phi over all children is at most Phi of the parent;
4. Phi is small enough to fit floor(q/2^128) at official parameters.

Prove the resulting total shortening-tree bound, or construct a finite
family whose canonical minimal-envelope tree has superpolynomial total
weight.

ACCEPTANCE:
- An explicit recurrence and closed-form finite bound;
- no counting of duplicate slopes across children;
- field and reserve ledgers preserved exactly.

FAILURE:
- Termination without total-weight control;
- a bound on one branch only;
- choosing a different noncanonical envelope to make each local estimate work.
```

## Prompt 5 — primitive catalecticant-pencil local limit

```text
TITLE: W-MCA-PRIMITIVE-CATALECTICANT-PENCIL

Let s_z=u+zv be an envelope-free affine syndrome pencil for an
official smooth RS code. For each z, form the apolar/catalecticant
ideal I_{s_z}. Select one exact full-support degree-j locator for each
bad slope.

Remove all slopes assigned to:
(1) a realized partial block system;
(2) a canonical apolar resultant/subresultant packet;
(3) a hereditary envelope descendant.

Prove

#remaining slopes
 <= ceil(C * binom(n,j)/q^(sigma-1)) + P(n,sigma),

with explicit C and P, or construct an official counterpacket.

Begin with the smallest constant-Kronecker-index/corank-one pencil
stratum. Count distinct slopes, not locator incidences.

ACCEPTANCE:
- A finite maximum-over-lines theorem;
- explicit treatment of support multiplicity and full-coordinate witnesses;
- a nonvacuous definition of the removed structures.

FAILURE:
- an average-over-lines estimate;
- a bound on support incidences rather than slopes;
- simply renaming the remainder H2-defective;
- a denominator-only theorem.
```

## Prompt 6 — arity-three scalar circuit kill test

```text
TITLE: W-LIST-ARITY-3-FULL-SUPPORT-CIRCUIT-COVER

Independently test the circuit route on the first nontrivial arity.

Classify support-minimal identities

U_1/G_1 + U_2/G_2 + U_3/G_3 = 0,

where the G_i are actual full agreement locators on a smooth
multiplicative domain and deg U_i is below the actual reserve tau_i.

After exact common-factor descent, prove that every such circuit lies in
one of:
(1) a bounded low-affine-rank polynomial envelope;
(2) one realized partial block system;
(3) one canonical apolar resultant packet;
(4) a primitive family with a uniformly bounded global hitting number.

Alternatively, produce an official smooth-domain arity-three circuit
family refuting that list.

ACCEPTANCE:
- A global circuit transversal bound, not merely classification of one
  circuit; or
- a full-support official counterpacket with list size above the prize target.

FAILURE:
- quotient plus common-core only;
- arbitrary-domain counterexamples without attempting the official smooth case;
- treating each circuit as a separate container.
```

---

# COUNTERPACKET — kill tests and likely false lemmas

| Proposed statement                                                        | Assessment        | Fast falsification test                                                                                                                                                                                |   |                                                   |
| ------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | - | ------------------------------------------------- |
| Genus (0/1) registry plus “higher-genus discrepancy” is complete          | Likely false      | Construct degree-(M) maps with genus-(\ge2) Galois closure over small (q), enumerate full split fibers, and compare (q/                                                                                | G | ) main term with the proposed discrepancy budget. |
| Corank-one degeneracy has only envelope/point-fiber/divisor-norm outcomes | Doubtful          | For (q=17,97), (n=8,16), enumerate locator families and test elementary-symmetric, trace, resultant, discriminant, and pair-product statistics. Search for a rich fiber invisible to the product norm. |   |                                                   |
| One line needs only (n^{o(1)}) inequivalent block systems                 | Unknown, doubtful | Enumerate all pole-free degree (2,3,4) maps on (n=8,16) smooth domains; compute induced full-block systems and solve the minimum weighted set-cover problem for each rich line.                        |   |                                                   |
| Canonical hereditary shortening trees have polynomial total weight        | Unknown           | Exhaust all syndrome lines for (q=7,13,17), (n\le12); generate all minimal-envelope children and record maximum leaves, duplicate slopes, and total exact charge.                                      |   |                                                   |
| Primitive occupancy after only point-block and envelope removal           | False             | The official rate-(1/8) product-character packet above already falsifies it.                                                                                                                           |   |                                                   |
| H2-defect is a bounded exceptional template                               | False             | Run the H2 extractor on random-anchor occupancy packets; large generic packets must also enter the H2-defective branch.                                                                                |   |                                                   |
| Quotient plus common-core covers scalar circuits                          | False generally   | The Cycle 60 Sidon/star packet already kills the arbitrary-domain version. Repeat enumeration on (F_{17}), (n=16), and (F_{257}) smooth domains for arity (3,4).                                       |   |                                                   |
| Residual partial-block packing                                            | Likely true       | Exhaust all abstract support systems for (n\le12) and verify the injection bound. Any failure should produce two slopes whose union is allegedly not a proper envelope.                                |   |                                                   |
| Scalar graded-apolar identity                                             | Likely true       | Enumerate all words/syndromes for (F_5,n=4,k=2) and (F_7,n=6,k=3); compare actual lists, full-support syndromes, and split elements of all graded apolar slices.                                       |   |                                                   |
| Pure boundary-layer list control implies full list control                | False             | Quotient and tangent overagreement packets already supply lower-layer lists with no boundary elements.                                                                                                 |   |                                                   |

The most likely false proposed theorem is the unrestricted divisor-norm trichotomy. The second most likely is a polynomial weighted registry across all split-rational partitions. Both should be attacked adversarially before anyone invests in classification.

---

# AUDIT — verification and formalization plan

## Claims requiring independent review first

1. **Official definition and threshold rounding**

   * exact support-wise MCA definition;
   * actual slope/code/challenge fields;
   * (|T|\le j) versus exact-(j) padding;
   * minimal safe reserve and the (+1/n) supremum correction.

2. **Cycle 47 Bessel–Paley theorem**

   * rank formula;
   * second moment;
   * Paley and missed-slope bounds;
   * same-field assumptions;
   * integer ceiling used in the prior-reserve certificate.

3. **Scalar graded-apolar identity**

   * GRS rescaling;
   * complete-intersection generator degrees;
   * full-coordinate iff (\gcd(U,V)=1);
   * all overagreement layers.

4. **Residual partial-block packing**

   * partial block systems rather than equipartitions;
   * arbitrary residual defect (d);
   * the (d>\sigma) subset parameter (h=d-\sigma+1).

5. **Official rate-(1/8) product-character packet**

   * modular order;
   * entropy interval;
   * color extraction;
   * exact MCA line and envelope exclusion.

6. **One Lattès packet**

   * verify degree 113 first because it is exact rate (1/16) and has a cleaner same-subfield construction;
   * retain degree 31 as an independent cross-check.

7. **H2 extraction**

   * leaf-peeling loss;
   * exact Macaulay dimension formula;
   * the implication from nonzero syndrome plane to positive splitting excess.

8. **Imported Crites–Stewart conversion**

   * exact radius;
   * normalization;
   * augmented code;
   * field in which the random parameter is sampled;
   * constants used by Paper D.

## Scripts/checkers to write

* `verify_lattes113.sage`

  * construct (E/\mathbb F_{65537});
  * verify Frobenius/CM factorization;
  * construct the degree-113 endomorphism;
  * derive the induced (t=x^2) map;
  * enumerate all 144 full fibers;
  * verify the transported domain and all slope-collision exclusions.

* `verify_lattes31.sage`

  * verify curve order, point order, kernel, Vélu map, 131 full fibers, action ranks and exact slope counts.

* `verify_official_product_character.py`

  * exact rate-(1/8) parameters;
  * interval arithmetic for both entropy bounds;
  * exact target and color floor;
  * machine-readable certificate.

* `scalar_apolar_enum.py`

  * enumerate actual scalar lists;
  * compute syndromes and apolar ideals;
  * enumerate graded split forms;
  * verify the (\gcd(U,V)) full-support criterion.

* `partial_block_packing_check.py`

  * property-based testing of the new residual packing lemma.

* `syndrome_line_container_scan.py`

  * enumerate bad slopes exactly;
  * deduplicate support incidences;
  * detect envelopes;
  * attach partial-block, norm/resultant, and H2 tags.

* `partition_registry_ilp.py`

  * enumerate small rational maps/block systems;
  * calculate minimum weighted block-system cover for each line.

* `envelope_tree_enum.py`

  * generate canonical shortening trees;
  * report duplicate slopes, depth, leaf count and total charge.

* `scalar_circuit_scan.py`

  * enumerate full-support circuits and minimum circuit transversals.

* `finite_threshold_certificate.py`

  * exact (T_F);
  * exact upper and lower ledgers;
  * field separation;
  * output (\widehat\sigma), safe grid radius and supremal transition.

## TeX promotion order

Promote only after two independent reviews:

1. exact syndrome/full-support/projection statements;
2. scalar graded-apolar identity;
3. residual partial-block packing;
4. official product-character packet;
5. one fully executable Lattès packet.

Do not promote as theorems:

* the complete genus-(0/1/\ge2) registry;
* the divisor-norm trichotomy;
* the H2-defect charge;
* the hereditary total-weight claim;
* either grand upper theorem;
* the universal cap until the imported conversion is checked.

---

# PLAN — resource allocation

Nine workers should not be given nine unrelated wall names. Use independent adversarial duplication on the highest-value claims.

## Round 1

| Instances | Assignment                                                                      |
| --------: | ------------------------------------------------------------------------------- |
|         2 | Prompt 1: one proof-first, one counterpacket-first                              |
|         1 | Prompt 2: resultant-character completeness                                      |
|         1 | Prompt 3: weighted partial-block registry                                       |
|         1 | Prompt 4: hereditary envelope potential                                         |
|         1 | Prompt 5: primitive catalecticant pencil                                        |
|         1 | Prompt 6: arity-three scalar circuit route                                      |
|         1 | Independent arithmetic verifier for Lattès 113 and the official product packet  |
|         1 | Meta-referee: definitions, finite ledger, Bessel theorem, Crites–Stewart import |

The local Fable/Codex loop should support them with:

* exact small-field enumeration;
* Sage finite-field and isogeny calculations;
* symbolic resultants/subresultants;
* property-based tests;
* ILP minimum-cover calculations;
* interval-arithmetic certificates.

## Round 1 stop/go criteria

* If Prompt 1 produces a valid structural theorem, make the apolar route primary.
* If Prompt 1 produces an official new counterpacket, identify the invariant it exploits before attempting a repaired theorem.
* If Prompt 3 finds superpolynomial minimum block-system cover, stop building quotient registries.
* If Prompt 4 finds exponential hereditary branching, replace tree summation by a max/energy argument.
* If Prompt 2 finds a fourth low-image invariant, do not append it casually to the ledger; first seek a general resultant/subresultant formulation.

## Round 2 if the apolar base case survives

| Instances | Assignment                                                                    |
| --------: | ----------------------------------------------------------------------------- |
|         3 | Extend minimal (V)-degree (0) to (1,2,\ldots), including fixed-defect descent |
|         1 | Sum all overagreement layers and produce finite scalar constants              |
|         1 | Independent scalar counterexample hunter                                      |
|         2 | Transfer the static theorem into (t=1) and low-(t) MCA strata                 |
|         1 | Dynamic catalecticant-pencil primitive theorem                                |
|         1 | Formalization and finite threshold certificate                                |

If the apolar base case fails, Round 2 should instead place three workers on the new invariant, two on theorem repair, two on independent official counterpackets, one on finite consequences, and one as referee.

## Human/PRZ order

The human/PRZ review should examine, in this order:

1. the scalar graded-apolar identity and minimal-generator reduction;
2. the residual partial-block correction, because it changes the claimed scope of two Cycle 60 lemmas;
3. the official rate-(1/8) product-character packet;
4. one executable Lattès packet;
5. the imported Crites–Stewart theorem.

The first item can reorient the entire project. The Lattès classification cannot.

---

# ROUTE TO FULL SOLVE

The answer is **no** for the current route as written. The blocker is not one missing estimate. It is the absence of a uniform inverse theorem separating random split-form occupancy from bounded-complexity support statistics.

The precise missing theory is:

[
\boxed{
\begin{array}{l}
\text{Static: large intersections of an apolar linear section with the}\
\text{finite split-form locus force canonical low-complexity resultants,}\
\text{partial block systems, or bounded primitive discrepancy;}[2mm]
\text{Dynamic: the same statement uniformly for a one-parameter}\
\text{catalecticant pencil, with distinct-slope and envelope control.}
\end{array}
}
]

The next exact lemma should be

[
\boxed{\texttt{W-LIST-APOLAR-MINIMAL-GENERATOR-INVERSE}.}
]

It is the correct first target because:

* it is the first nontrivial scalar list stratum;
* it is canonical and two-generated;
* the configuration character is forced by an exact resultant;
* its extension would solve the scalar challenge;
* scalar projection would then solve every interleaving arity;
* the same theorem controls the (t=1) MCA branch;
* it gives a disciplined route for higher (V)-degree through fixed defects and subresultants.

The proposed solve sequence is:

1. Prove or kill the minimal apolar slice.
2. Extend by induction on (\deg V), with exact resultant/subresultant accounting.
3. Sum all error-weight layers and produce a finite scalar certificate.
4. Apply projection to finish the interleaved list challenge.
5. Formulate the corresponding catalecticant-pencil theorem for MCA.
6. Prove the hereditary envelope potential.
7. Combine primitive, structural and hereditary bounds into an exact integer MCA certificate.
8. At each candidate reserve, pair the upper certificate with Bessel–Paley or an explicit prior-reserve counterpacket.
9. Extract the code-specific (\delta_C^*) with the (1/n) endpoint correction.

Anything less—another quotient family, another normal form, another structural tag, or another one-sided lower bound—is route repair, not a prize solve.
