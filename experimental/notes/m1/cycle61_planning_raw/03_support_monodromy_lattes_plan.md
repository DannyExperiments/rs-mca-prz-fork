# Executive verdict

**The prize problems are not close.** The route is plausible, but it still lacks hard inverse/container theorems rather than merely arithmetic cleanup.

* **Grand MCA:** medium-range. The lower/failure side and exact syndrome formulation are strong, but the upper side still needs two major results: a line-local weighted support-container theorem and a primitive remainder theorem.
  **Confidence that the present architecture can eventually solve it: moderate, about 55%.**
* **Grand list decoding:** harder and more independent than the route board sometimes suggests. Projection to scalar lists is banked; the scalar full-support circuit transversal theorem is not.
  **Confidence that the current route can solve it without a substantial new idea: low-to-moderate, about 35%.**
* **Quotient/Lattès branch:** the two proposed Lattès packets are substantially correct. The quotient taxonomy must change again, however: genus (g\ge2) is not automatically a discrepancy-only remainder.
  **Confidence in this route correction: high, above 90%.**

The correct quotient invariant is **not** any one of Galois-closure genus, monodromy, action rank, or fiber count. The primary object is the realized support block system on (L). Monodromy data certify and constrain it; the actual support profile charges it; action rank only recognizes it inside a chosen denominator chart.

---

# AUDIT — Degree-31 and degree-113 Lattès packets

I independently reproduced the finite arithmetic.

## Degree 31

For
[
p=8191,\qquad E:y^2=x^3+x+459,
]
the checks give:

[
#E(\mathbf F_p)=8153=31\cdot263.
]

The stated point (G=(0,7904)) has order (8153), and the order-31 kernel has exactly the stated fifteen nonzero (x)-coordinates. The induced degree-31 Lattès map has rational fiber distribution

[
31^{131},\qquad 16^1,\qquad 1^{4115}.
]

For (F=\mathbf F_{8191^{18}}),

[
\log_2|F|=233.9968298\ldots,
]
and
[
\log_2\binom{131}{67}=127.1056011\ldots.
]

After the stated collision deletion, the exact lower bound is

[
183062151498210163887302260440015706432>2^{127},
]
whereas
[
\left\lfloor |F|/2^{128}\right\rfloor
=====================================

80951559894234747884481262824352
<2^{106}.
]

**Verdict:** admissible and route-changing. Confidence **high, about 98%**.

Remaining theorem-grade review items:

1. Reproduce the Vélu rational function in Sage or Magma, not only its fibers.
2. Verify regularity and constant field of the (D_{62}) Galois closure.
3. Audit every excluded-(\theta) locus, especially the simultaneous monomial/dihedral action-rank exclusions.
4. Translate the projective-subline Cayley transport and target Möbius normalization into a single explicit rational function over the code field.

## Degree 113

For
[
p=65537,\qquad E:y^2=x^3-9x,
]
the checks give

[
9^{(p-1)/4}=-1,\qquad #E(\mathbf F_p)=65540=113\cdot580.
]

With
[
\iota(x,y)=(-x,256y),
]
the correct sign for the stated choice of (\iota) is

[
\phi=[7]-[8]\iota.
]

Its kernel has size (113), its image has size (580), and (\phi) is the identity on the four rational 2-torsion points. On the cyclic kernel, (\iota) acts as multiplication by (15\bmod113), with

[
15^2=-1,\qquad 15^4=1\pmod{113},
]
confirming the faithful (C_4)-action.

The image has (144) free (C_4)-orbits, and each corresponding (t=x^2) value has a full fiber of (113) distinct rational (t)-values. For (F=\mathbf F_{65537^{15}}),

[
\log_2|F|=240.0003302\ldots,
]
[
\log_2\binom{144}{37}=114.6626745\ldots,
]
while
[
\log_2\left\lfloor |F|/2^{128}\right\rfloor
=112.0003302\ldots.
]

Thus the packet exceeds the exact target by a factor of approximately (6.3).

**Verdict:** admissible after one presentational repair. Confidence **high, about 95%**.

The repair is that the raw construction does not explicitly prove that its initial representative (A_0/B_0) is pole-free on the whole evaluation domain. This is harmless but must be written: choose (c\notin R(L)) and postcompose by a Möbius map whose unique pole is (c). That preserves degree, block system, monodromy, and full fibers.

The exact audit is reproducible here:

* [Audit script](sandbox:/mnt/data/cycle61_quotient_packet_audit.py)
* [Audit output](sandbox:/mnt/data/cycle61_quotient_packet_audit.txt)

---

# ROUTE_CUT

The wall

```text
W-SRQ-HIGH-GENUS-FROBENIUS-DISCREPANCY-CONTAINER
```

is incorrectly formulated.

A fully split regular fiber has identity Frobenius. Consequently its count has a Chebotarev main term of order

[
\frac{q_0}{|G|},
]

not merely a square-root discrepancy. Genus (g\ge2) does not imply that the full-fiber profile is negligible.

## COUNTERPACKET — a genus-4 split-rational packet

Over (\mathbf F_{257}), consider

[
R_0(x)=x^4-x^2+112x.
]

Its derivative has exactly three simple rational roots,

[
64,\quad75,\quad118,
]

with distinct critical values. The polynomial is rationally indecomposable: after removing the cubic term, a quadratic-of-quadratic decomposition in characteristic not two would force the linear coefficient to vanish.

Therefore the geometric monodromy is (S_4): it is primitive and contains both a 4-cycle from infinity and simple transpositions from the finite critical points. The Galois-closure branch types are

[
(4),(2),(2),(2),
]
so Riemann–Hurwitz gives

[
2g-2
====

24\left(-2+\frac34+3\cdot\frac12\right)
=6,
\qquad g=4.
]

Nevertheless, (R_0) has fourteen full 4-point fibers in (\mathbf F_{257}^{\times}).

Transport to

[
F=\mathbf F_{257^{17}},\qquad
L=\alpha\mathbf F_{257}^{\times},\qquad
n=256,\quad k=16,\quad \sigma=4.
]

Selecting five of the fourteen full fibers gives

[
\binom{14}{5}=2002
]

transverse, envelope-free bad slopes after choosing the generic denominator parameter. The exact prize numerator is

[
\left\lfloor |F|/2^{128}\right\rfloor=273.
]

Moreover,

[
\log_2\frac{\binom{256}{20}}{|F|^3}
=-310.463\ldots,
]
while the normalized packet size has logarithm

[
\log_2(2002/|F|)
=-125.128\ldots>-128.
]

This is an occupancy-clean high-genus main-term packet.

It does **not** by itself prove that no unrelated low-genus support system can cover some of the same slope supports. It does prove that any theorem treating every (g\ge2) full-split profile as a discrepancy term is false.

## EXACT_NEW_WALL

```text
W-SRQ-ALL-GENUS-FULL-FIBER-PROFILE-REGISTRY
W-MCA-SUPPORT-MONODROMY-WEIGHTED-OVERLAP-COVER
```

The corrected split is not (g=0,1) versus (g\ge2). It is:

1. **Profile-capable covers:** enough full blocks to assemble a (k)-point core; these require explicit main-term profile charges, in every genus.
2. **Profile-light covers:** unable to assemble such a core; these may pass into the primitive/occupancy theorem.
3. **Hereditary/envelope covers:** overlapping systems force shortening or a common envelope.

---

# The correct registry invariant

The registry should have five levels.

### 1. Primary invariant: support block system

For a separable rational map (R) of degree (M), define

[
\Pi_R(L)=
\left{
R^{-1}(y)\cap L:
|R^{-1}(y)\cap L|=M
\right}.
]

Two maps are registry-equivalent when they induce the same collection of full blocks on (L).

This is invariant under target Möbius transformations, formula changes, and relabeling of quotient values.

### 2. Refinement and common-right-factor closure

If
[
R=R_0\circ W,
]
then the (W)-blocks refine the (R)-blocks. Systems related by a common right factor must be merged into a refinement lattice rather than charged independently.

### 3. Algebraic certificate

A support class should carry a certificate of the form

[
\mathfrak c(\Pi)=
(K_0,;X_R,;G_R,;H_R,;g_R,;\mathbf e_R,;
\operatorname{Prof}_L(R)).
]

Here:

* (K_0) is the minimal descent field relevant to the domain;
* (X_R) is the regular Galois closure;
* (G_R) is geometric monodromy;
* (H_R) is a point stabilizer, so (M=[G_R:H_R]);
* (g_R) is Galois-closure genus;
* (\mathbf e_R) is branch-cycle/inertia data;
* (\operatorname{Prof}_L(R)) is the actual full-fiber profile on (L).

The descent field is load-bearing. Applying Hasse–Weil over the enormous code field instead of the small field on which the map and domain descend loses all useful information.

### 4. Finite support charge

For a defect (D\subseteq L), write

[
\Pi_D={B\in\Pi:B\cap D=\varnothing}.
]

For supports made from (D) and (b) full blocks, the exact raw profile is

[
\omega(\Pi,D,b)
===============

\min\left{
q,\binom{|\Pi_D|}{b}
\right}.
]

But this should be sharpened by (k)-core coverage.

For a support family (\mathscr A), define

[
\kappa_k(\mathscr A)
====================

\min\left{
|\mathcal U|:
\mathcal U\subseteq\binom Lk,\
\forall S\in\mathscr A\ \exists U\in\mathcal U,\ U\subseteq S
\right}.
]

The correct line-local charge is

[
W_\sigma(\mathscr A)
====================

\min\left{
|\mathscr A|,
\left\lfloor\frac r\sigma\right\rfloor
\kappa_k(\mathscr A)
\right}.
]

### 5. Local metadata: action rank

The quantity (d_R(E)) remains useful for recognizing that a particular denominator lies over a particular rational action. It is not a canonical registry key.

The Lattès packets explicitly demonstrate this:

[
d_R(E)=1
]

while every tested fixed-coordinate monomial action has full rank.

---

# PROOF — common-full-block rigidity

## BANKABLE_LEMMA

Let (R,S:\mathbf P^1\to\mathbf P^1) be separable rational maps of degrees (M,N). Assume they have no nonconstant common right factor.

If (t) simple full (M)-point fibers of (R) are each contained in a fiber of (S), then

[
\boxed{
t\le
\left\lfloor\frac{2(N-1)}M\right\rfloor.
}
]

In particular, two same-degree full blocks shared by two degree-(M) maps force a common right factor. If both maps are indecomposable, they are target-Möbius equivalent.

### Proof

Let (\Gamma_R) be the off-diagonal correspondence

[
R(x)=R(y),\qquad x\ne y.
]

As a divisor on (\mathbf P^1\times\mathbf P^1), it has bidegree

[
(M-1,M-1).
]

Similarly, (\Gamma_S) has bidegree ((N-1,N-1)).

If the two correspondences had a common irreducible component, then the map

[
x\longmapsto (R(x),S(x))
]

would not be generically injective. Hence

[
[\overline K(x):\overline K(R,S)]>1.
]

By Lüroth, (\overline K(R,S)=\overline K(W)) for a nonconstant (W), so (R) and (S) would have a common right factor. Therefore (\Gamma_R) and (\Gamma_S) have no common component.

Their intersection number is

[
(M-1,N-1)\cdot(N-1,N-1)
=======================

2(M-1)(N-1).
]

Every common simple full (R)-block contributes all (M(M-1)) ordered off-diagonal pairs. Thus

[
tM(M-1)\le2(M-1)(N-1),
]

which gives the claim.

This lemma should be promoted immediately after a separability and homogenization review. It supplies the missing deduplication rule for the support registry.

---

# BANKABLE_LEMMA — profile-capability cutoff

Let (R) have a regular Galois closure (X_R/K_0), with group (G_R), genus (g_R), and constant field (K_0=\mathbf F_{q_0}). Let (s_R) be the number of unramified fully split (K_0)-rational fibers.

Then

[
\boxed{
s_R|G_R|
\le
#X_R(K_0)
\le
q_0+1+2g_R\sqrt{q_0}.
}
]

If a witness support contains (b) full degree-(M) fibers and

[
bM\ge k,
]
then, writing
[
h_R=|H_R|=\frac{|G_R|}{M},
]
one obtains

[
\boxed{
h_R
\le
\frac{q_0+1+2g_R\sqrt{q_0}}{k}.
}
]

For (q_0\sim n) and controlled genus, this is asymptotically

[
h_R\le\frac1\rho+o(1).
]

Thus the relevant asymptotic stabilizer scales at the four rates are approximately

[
2,\ 4,\ 8,\ 16.
]

This is the correct narrowing device. It does not justify a genus cutoff. The genus-4 quartic has (h_R=6), and is therefore profile-capable at rate (1/16).

---

# CONDITIONAL — theorem replacing the old quotient ledger

## Support–monodromy weighted cover theorem

Let (C=\operatorname{RS}[F,L,k]), let (r=n-k), and fix reserve (\sigma). Let (\ell) be an envelope-free affine syndrome line.

Let (Z_{\mathrm{SR}}(\ell)) be the transverse bad slopes admitting a witness support that is a defect plus full fibers of some separable rational map.

The desired theorem should assert the existence of a line-local collection of maximal support block-system classes

[
\mathfrak R(\ell)
]

with the following properties.

### A. Support-level assignment

Every (z\in Z_{\mathrm{SR}}(\ell)) is assigned one full agreement support

[
S_z\in\mathscr A_\ell(\Pi)
]

for one (\Pi\in\mathfrak R(\ell)).

### B. Right-factor deduplication

Systems sharing sufficiently many full blocks are merged through their common-right-factor/refinement closure. Algebraically different formulae inducing the same full blocks are counted once.

### C. Profile-capable completeness

Every retained system either:

1. has a regular algebraic certificate
   [
   (K_0,X_R,G_R,H_R,g_R,\mathbf e_R,\operatorname{Prof}_L(R))
   ]
   satisfying the point-budget capability test; or
2. cannot place (k) agreement points in full blocks and is transferred to the primitive theorem.

This branch must include:

* genus-zero subgroup-chain covers;
* genus-one Lattès/isogeny covers;
* all profile-capable higher-genus covers.

### D. Weighted line bound

One has

[
\boxed{
|Z_{\mathrm{SR}}(\ell)|
\le
\sum_{\Pi\in\mathfrak R(\ell)}
W_\sigma\bigl(\mathscr A_\ell(\Pi)\bigr)
\le
Q_{\mathrm{SR}}(C,\sigma),
}
]

where (Q_{\mathrm{SR}}(C,\sigma)) is an explicit, machine-checkable integer.

The first inequality follows from the fixed-core petal theorem. The hard content is the second inequality: bounding the collective (k)-core complexity of all systems realized on one syndrome line.

This is the clean theorem replacing the old formula/action-rank ledger.

**Current status:** unknown. This is a hard inverse theorem. A classification of genus-zero and genus-one covers alone does not prove it.

---

# Minimal theorem package

## Grand MCA challenge

### Smallest asymptotic package

1. **SR-COVER:** the support–monodromy weighted cover theorem above.
2. **HERED-ENV:** a finite hereditary common-envelope/shortening theorem.
3. **PRIM-MCA:** after removing split-rational systems and envelopes,
   [
   |\operatorname{Bad}^{\rm prim}_\sigma(\ell)|
   \le
   (1+o(1))
   \frac{\binom nj}{q^{\sigma-1}}
   +o(q),
   \qquad j=r-\sigma.
   ]
   This theorem must absorb the jet-residue, configuration-character, high-denominator, and MDS-3-core branches.
4. **MCA-FAIL:** a matching lower theorem at the preceding reserve, either Bessel–Paley/random-anchor or an explicit packet.

The divisor-norm trichotomy and (t=1) apolar inverse theorem are not logically separate members of the minimal package. They are likely necessary subtheorems for PRIM-MCA.

### Exact finite (2^{-128}) package

For every candidate reserve (\sigma), produce explicit integers satisfying

[
M_C(\sigma)
\le
U_{\rm MCA}(\sigma)
===================

\max\left{
E_{\rm her},
\left\lceil
C_{\rm occ}\frac{\binom nj}{q^{\sigma-1}}
\right\rceil
+D_{\rm prim}
+Q_{\rm SR}
\right}.
]

Safety requires

[
U_{\rm MCA}(\sigma)
\le
T_q:=\left\lfloor\frac q{2^{128}}\right\rfloor.
]

At the previous reserve (\sigma-1), one needs an exact lower certificate exceeding (T_q).

If (\widehat\sigma) is the minimal safe reserve, then

[
\delta_{\max}^{\rm grid}
========================

1-\rho-\frac{\widehat\sigma}{n},
]

while the supremal real transition is

[
\delta_C^*
==========

1-\rho-\frac{\widehat\sigma-1}{n},
]

with the transition endpoint itself unsafe.

## Grand list decoding challenge

### Smallest asymptotic package

1. The exact scalar full-support identity and circuit reduction — already banked.
2. **LIST-CIRCUIT-COVER:** every low-arity positive-excess full-support circuit is covered by:

   * common-core containers;
   * split-rational/full-block containers;
   * low-affine-rank envelopes;
   * a primitive discrepancy remainder.
3. The same-field scalar-to-interleaved projection theorem — already banked.
4. A matching previous-reserve scalar lower construction.

### Exact finite (2^{-128}|F|) package

Prove

[
L_C(\sigma)
\le
E_{\rm core}+Q_{\rm list}+D_{\rm list}
+
\left\lceil
C_{\rm list}q^{-r}
\sum_{e=0}^{j}\binom ne(q-1)^e
\right\rceil
\le T_q.
]

The projection theorem then handles every constant interleaving arity because, at the official scale and (q<2^{256}),

[
\binom{T_q+1}{2}<q.
]

The scalar circuit cover remains the central unknown theorem.

---

# Dependency DAG

```text
GRAND-MCA-SOLVE [unknown]
├── exact syndrome transverse-secant formulation [already banked]
├── MCA-UPPER [unknown]
│   ├── SR-COVER [unknown]
│   │   ├── support-block-system definition [already banked]
│   │   ├── fixed-partition packing [already banked]
│   │   ├── fixed-core petal theorem [already banked]
│   │   ├── common-full-block rigidity [likely; bankable now]
│   │   ├── three-full-fiber descent [likely; needs audit]
│   │   ├── genus-zero subgroup-chain classification [likely, tame case]
│   │   ├── genus-one Lattès classification [likely, tame case]
│   │   ├── degree-31/113 packet arithmetic [likely; audit passed]
│   │   ├── profile-capable all-genus registry [unknown]
│   │   └── weighted overlap on one line [unknown]
│   ├── HERED-ENV [unknown]
│   │   └── hereditary MDS-3-core extraction [already banked]
│   └── PRIM-MCA [unknown]
│       ├── t=1 apolar normal form [already banked]
│       ├── t=1 primitive inverse [unknown]
│       ├── divisor-norm/configuration trichotomy [unknown]
│       └── primitive occupancy/discrepancy [unknown]
├── previous-reserve MCA failure [already banked in restricted branches;
│                                 unknown uniformly code-by-code]
└── exact integer threshold scanner [likely]

OLD: g>=2 = discrepancy-only [false]
OLD: action rank as canonical quotient key [false]
OLD: pure n^(1+o(1)) safe-side target [false or too narrow]

GRAND-LIST-SOLVE [unknown]
├── scalar full-support identity [already banked]
├── full-support circuit reduction [already banked]
├── low-arity circuit transversal cover [unknown]
│   ├── common-core reduction [already banked]
│   ├── quotient/full-block circuit cover [unknown]
│   ├── low-affine-rank envelope cover [unknown]
│   └── primitive positive-excess circuit bound [unknown]
├── scalar-to-interleaved projection [already banked]
├── previous-reserve list failure [likely/code-specific]
└── exact integer threshold scanner [likely]
```

---

# PLAN — Best next theorem-worker prompts

## Prompt 1 — highest priority

```text
W-MCA-SUPPORT-MONODROMY-WEIGHTED-OVERLAP-COVER

Let C=RS[F,L,k], r=n-k, and let ell be an envelope-free affine
syndrome line. For every transverse split-rational bad slope choose one
full agreement support S_z and one realized full-block system Pi_z.

Prove or refute the following statement:

After merging systems through common-right-factor refinement, the selected
support families admit k-core covers K_i satisfying

  sum_i min{|A_i|, floor(r/sigma)|K_i|}
  <= Q_SR(C,sigma),

where Q_SR is an explicit expression depending only on actual full-fiber
profiles and the smooth-domain registry, not on the number of rational
formulae representing those profiles.

The proof must allow varying map degree, varying defect, incomplete
partitions, Lattes systems, and higher-genus profile-capable systems.

Acceptance:
- a fully quantified theorem with an explicit finite Q_SR;
- a proof of the line-local overlap step;
- exact treatment of refinement and duplicate support systems.

Failure criterion:
- an explicit envelope-free syndrome line carrying support systems whose
  weighted k-core complexity violates every proposed registry bound.
```

## Prompt 2 — all-genus profile-capable classification

```text
W-SRQ-SMALL-STABILIZER-HURWITZ-REGISTRY

Let R:P1->P1 be separable with regular Galois closure X/K0, group G,
point stabilizer H, and h=|H|. Assume R has enough full K0-rational
fibers to place at least k evaluation points in full blocks on an official
smooth domain.

For the four rates, use the split-fiber point budget to reduce to the
profile-capable range h approximately <= 2,4,8,16. Classify, parameterize,
or refute the possibility of a finite Hurwitz registry for these covers.
Do not assume g(X)<=1.

Acceptance:
- a branch-cycle/Hurwitz-space description sufficient for finite profile
  charging, including positive-dimensional families; or
- a structural theorem showing such covers refine genus-zero/Lattes
  systems; or
- an explicit infinite higher-genus family proving that taxonomy-first
  classification cannot yield a bounded registry.

Failure criterion:
- merely listing finite transitive groups or quoting genus-zero/genus-one
  classifications without handling higher genus and support profiles.
```

## Prompt 3 — formal Lattès certification

```text
VERIFY-LATTES-31-113

Independently certify the degree-31 and degree-113 Lattes MCA packets in
Sage and, where practical, Magma.

For degree 31 verify:
curve order, generator order, kernel, Velu map, reduced degree, complete
fiber distribution, target-Mobius pole removal, Galois closure/signature,
theta-exclusion count, action ranks, support identities, transversality,
envelope exclusion, denominator uniqueness, and exact threshold inequality.

For degree 113 verify:
the CM Frobenius sign, phi=[7]-[8]iota for the stated iota, kernel and image,
iota action on the kernel, induced rational map in t=x^2, 144 full fibers,
pole-free target normalization, monodromy C113 semidirect C4, theta
exclusions, support identities, and exact threshold inequality.

Acceptance:
machine-readable certificates plus a TeX-ready proof with no unchecked
finite arithmetic.

Failure criterion:
any incorrect fiber count, field-generation claim, pole condition,
constant-field claim, or exclusion-locus bound.
```

## Prompt 4 — high-genus main-term kill test

```text
W-SRQ-HIGH-GENUS-MAIN-TERM-COUNTERPACKET

Independently verify the proposed map

  R(x)=x^4-x^2+112x over F_257.

Prove or disprove:
- indecomposability over the algebraic closure;
- geometric monodromy S4;
- Galois-closure genus 4;
- the fourteen full 4-point fibers;
- the rate-1/16, n=256, sigma=4 MCA construction with 2002 distinct
  transverse envelope-free slopes over F_(257^17);
- target floor(q/2^128)=273 and the occupancy bound.

Then determine whether those support families are already covered by an
unrelated genus-zero or genus-one block system. Use common-full-block
rigidity and exhaustive finite searches.

Acceptance:
either a theorem-grade high-genus packet genuinely requiring an all-genus
registry, or an explicit alternative support container explaining it.

Failure criterion:
verification of arithmetic alone without testing alternative block-system
coverage.
```

## Prompt 5 — primitive MCA complement

```text
W-MCA-PRIMITIVE-AFTER-SUPPORT-QUOTIENT-REMOVAL

Work in the denominator-free syndrome transverse-secant formulation.
Assume all support families admitting a profile-capable split-rational
block system and all hereditary envelopes have been removed.

Prove or refute a finite primitive bound

  |Bad_prim(ell)|
  <= ceil(C_occ binom(n,j)/q^(sigma-1)) + D_prim,

with explicit C_occ and D_prim small enough for the official 2^-128
certificate.

The theorem must explicitly handle:
- the t=1 apolar complete-intersection chart;
- divisor-norm/configuration-space characters;
- hereditary MDS-3 critical cores;
- all denominator degrees through the syndrome formulation.

Acceptance:
an exact theorem or a finite counterpacket outside every registered
quotient, configuration-character, and envelope branch.

Failure criterion:
a statement restricted to one denominator stratum or one fixed seed.
```

## Prompt 6 — scalar circuit cover

```text
W-LIST-LOW-ARITY-FULL-SUPPORT-CIRCUIT-COVER

For an RS syndrome s, consider support-minimal relations

  sum_i U_i p_{E_i}=0,
  deg U_i < tau_i,

among actual full-support error representations, with circuit arity at most
ceil(r/sigma).

Prove that a transversal meeting every such circuit has size bounded by an
explicit sum of:
- common-core hereditary charges;
- split-rational full-block charges;
- low-affine-rank envelope charges;
- a primitive discrepancy term.

The theorem must retain every overagreement layer through the actual
reserves tau_i.

Acceptance:
an exact finite transversal bound which, together with
floor((r-1)/sigma), is <= floor(q/2^128).

Failure criterion:
an explicit same-field smooth-domain circuit family escaping all proposed
containers and exceeding the target.
```

---

# Kill tests and counterexample searches

| Proposed statement                                                                 | Assessment                                  | Fast falsification test                                            |
| ---------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------ |
| Every (g\ge2) cover contributes only discrepancy                                   | **False**                                   | The genus-4 quartic over (\mathbf F_{257})                         |
| Every profile-capable cover has (g\le1)                                            | **False**                                   | Same quartic; (S_4), (g=4), stabilizer size (6)                    |
| Genus and abstract monodromy determine the quotient template                       | **False**                                   | Compare toric and elliptic dihedral signatures; branch data differ |
| Action rank determines the support block system                                    | **False**                                   | Degree-31 and degree-113 Lattès packets                            |
| There are only (n^{o(1)}) rational-map formulae to charge                          | **Likely false**                            | Enumerate positive-dimensional degree-4 (S_4) Hurwitz families     |
| Low-genus classification alone gives a line bound                                  | **Doubtful**                                | Search one line carrying many inequivalent low-genus systems       |
| Two same-degree indecomposable maps may share many full blocks without equivalence | **False under separability**                | Common-full-block rigidity lemma                                   |
| A fixed-defect packet count can simply be multiplied over all defects              | **Too expensive/usually false as a target** | Compare with fixed-core and fixed-partition packing                |

Recommended finite searches:

1. Over (\mathbf F_{17},\mathbf F_{29},\mathbf F_{97},\mathbf F_{257}), enumerate normalized separable maps of degrees (2)–(6).
2. Record full blocks, refinement relations, branch signatures, and point-stabilizer sizes.
3. Build the block-system intersection graph: join two maps when they share two or more full blocks.
4. Verify that each joined same-degree indecomposable pair is target-equivalent.
5. For small RS instances (n=8,16), enumerate affine syndrome lines and measure how many inequivalent block systems one envelope-free line can realize.
6. Search specifically for many systems with no shared full block but highly overlapping (k)-core families. That is the most dangerous obstruction to the proposed cover theorem.

---

# AUDIT — verification and formalization plan

The Cycle 58–60 claims should be reviewed in this order.

1. **Lattès arithmetic and admissibility.** These change the registry.
2. **Fixed-partition packing and fixed-core petal theorem.** These are short, central, and likely fully bankable.
3. **Common-full-block rigidity.** This should become the registry deduplication lemma.
4. **High-genus quartic kill test.** PRZ should decide immediately whether the old high-genus wall is retired.
5. **Scalar full-support identity, circuit reduction, and projection.** These delimit the list problem exactly.
6. **Divisor-norm/configuration-character counterpacket.**
7. **Hereditary MDS-3-core extraction.**
8. **(t=1) apolar normal form.**

Scripts/checkers to write:

```text
verify_lattes31.sage
verify_lattes113.sage
verify_high_genus_quartic.sage
split_block_registry.py
common_right_factor_bezout.sage
small_field_line_overlap.py
verify_mca_packet_witness.sage
verify_scalar_full_support.py
finite_threshold_ledger.py
```

A result should enter the main TeX only after:

* two independent arithmetic implementations agree;
* the map’s constant field and regularity are explicit;
* pole removal on the entire evaluation domain is checked;
* all generic-parameter exclusions are numerically below the field size;
* the support identity is verified symbolically;
* transversality, envelope exclusion, and canonical denominator claims are checked separately;
* exact integer comparison uses (\lfloor q/2^{128}\rfloor), not floating-point approximations.

---

# PLAN — resource allocation

## Round 1

| Worker | Assignment                                                                      |
| ------ | ------------------------------------------------------------------------------- |
| 1      | Degree-31 Sage/Magma certification                                              |
| 2      | Degree-113 CM/Lattès certification                                              |
| 3      | High-genus quartic verification and search for further small-stabilizer packets |
| 4      | Formal proof and extensions of common-full-block rigidity                       |
| 5      | Small-stabilizer branch-cycle/Hurwitz registry                                  |
| 6      | Line-local weighted (k)-core overlap theorem                                    |
| 7      | Primitive MCA: (t=1), divisor norm, MDS-3 remainder                             |
| 8      | Scalar full-support circuit cover                                               |
| 9      | Adversarial referee, exact ledger, and TeX formalization                        |

The local Fable/Codex loop should handle exhaustive small-field enumeration, exact integer ledgers, property tests, resultant/common-factor checks, and automatic witness verification. It should not be used to conjecture the global cover theorem from numerical data without a human-readable invariant.

## Round 2

If the small-stabilizer registry appears finite or structurally tractable:

* three workers on all-genus profile-capable classification;
* two on weighted line overlap;
* one on primitive MCA;
* one on hereditary envelopes;
* one on scalar circuits;
* one as independent referee.

If positive-dimensional higher-genus families proliferate:

* stop taxonomy-first work;
* allocate four workers to direct support-hypergraph/(k)-core overlap;
* two to primitive MCA;
* two to scalar circuits;
* one to verification.

## Human/PRZ priority

PRZ should check, in this order:

1. the genus-4 quartic route cut;
2. the degree-113 CM sign and pole-free normalization;
3. the common-full-block rigidity proof;
4. the decision to make support block systems—not algebraic formula classes—the canonical registry object.

Do not spend another full round enumerating Lattès formulae before the line-local overlap theorem has a credible statement. A perfect taxonomy with no collective line bound does not advance the prize.

---

# Route to a full solve

The next exact lemma is:

```text
W-MCA-SUPPORT-MONODROMY-WEIGHTED-OVERLAP-COVER
```

Specifically, prove that after common-right-factor merging, the total (k)-core cover complexity of all split-rational support systems realized on one envelope-free syndrome line is bounded by an explicit finite profile ledger.

That is the quotient-side bottleneck. It is not the classification of Lattès maps by itself.

Even after that lemma, the MCA challenge still needs the primitive complement theorem. The list challenge independently needs the low-arity full-support circuit cover.

Therefore the exact conclusion is:

* **The route remains plausible.**
* **It is not close.**
* **The old high-genus discrepancy wall is wrong.**
* **The route must narrow from formula taxonomy to support-level weighted overlap.**
* **The two genuinely hard missing theories are the MCA primitive inverse theorem and the scalar circuit transversal theorem.**
