# Executive verdict

**No—the full prize problem is not close.** The repository has strong failure mechanisms, exact reformulations, and several useful local lemmas, but neither grand challenge has its safe-side inverse theorem.

| Assessment                                         |              Verdict |     Confidence |
| -------------------------------------------------- | -------------------: | -------------: |
| Full solution from the presently banked statements |        Not available |     High, 0.98 |
| Full solution within the next two worker rounds    |             Unlikely |     High, 0.85 |
| Broad syndrome/circuit route eventually succeeding |            Plausible | Moderate, 0.55 |
| Continuing by merely adding more quotient families | Unlikely to converge |     High, 0.85 |
| Building a reliable finite certificate layer now   |      Straightforward |     High, 0.95 |

The state is best described as **still missing hard inverse theorems**, not “one lemma away.” The MCA and list challenges end at different upper-side walls:

* MCA needs a uniform, maximum-over-lines support-factor/container theorem.
* List decoding needs a global circuit-transversal theorem.
* The interleaving projection is no longer a wall.
* The failure side is much closer to completion than the safe side.

There is also no credible rate-only answer consisting of four constants. The exact threshold depends on (n), the relevant fields, the domain (L), divisibility, and its realized quotient/configuration profiles.

**CONDITIONAL.** Paper D currently gives only an upper cap, and it depends on an imported Crites–Stewart theorem not independently available in the archive:

[
\delta_C^*\le 1-\rho-2^{-9}
\quad
(\rho=1/2,1/4,1/8),
]

and

[
\delta_C^*\le 1-\rho-2^{-10}
\quad
(\rho=1/16),
]

under its stated divisibility hypotheses. This does not determine the threshold and should not be promoted as an unconditional repository theorem until the import is checked line by line.

---

# AUDIT — exact finite objects

Put

[
C=\operatorname{RS}[F,L,k],\qquad
n=|L|,\qquad
r=n-k,
]

and at reserve (\sigma\ge1),

[
a=k+\sigma,\qquad j=r-\sigma=n-a.
]

Let (H) be an (r\times n) RS parity-check matrix, with column (h_x) at (x\in L), and write

[
V_T=\operatorname{span}_F{h_x:x\in T}.
]

For an affine syndrome line (\ell(z)=u+zv), the exact MCA numerator is

[
M_C(\sigma)=
\max_{u,v\in F^r}
\left|
\left{
z\in F:
\exists T\in\binom Lj,\
u+zv\in V_T,\
v\notin V_T
\right}
\right|.
]

There should be **no additional global noncontainment condition in this definition**. A line contained in one proper secant envelope can still have transverse witnesses against other supports. Envelope-freeness is an upper-proof branch, not part of the MCA event.

For scalar lists, define

[
\nu_e^\circ(s)=
#\left{
(E,c):
|E|=e,\
c\in(F^\times)^E,\
H_Ec=s
\right}.
]

Since (e<r), the MDS property makes (H_E) injective. Thus the exact scalar numerator is

[
L_C(\sigma)=
\max_{s\in F^r}
\sum_{e=0}^{j}\nu_e^\circ(s).
]

The relevant targets are

[
T_{\rm MCA}=\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor,
\qquad
T_{\rm list}=\left\lfloor\frac{q_{\rm code}}{2^{128}}\right\rfloor.
]

In the ordinary same-field problem (q_{\rm line}=q_{\rm code}=|F|), but the proof ledger should not silently identify all fields.

| Field          | Permitted role                                                    |
| -------------- | ----------------------------------------------------------------- |
| (q_{\rm gen})  | Generated-domain entropy, base-field pigeonhole, domain structure |
| (q_{\rm line}) | MCA slope probability and MCA target numerator                    |
| (q_{\rm code}) | Scalar/interleaved alphabet and list target                       |
| (q_{\rm chal}) | External protocol challenge accounting only                       |

A larger (q_{\rm chal}) cannot pay an MCA or list bill over a smaller line/code field. Similarly, a generated-field entropy estimate cannot be paid with (q_{\rm line}) without a transfer theorem.

The threshold is a staircase. If (\sigma_*) is the minimal safe reserve and (\sigma_*-1) is unsafe, then

[
\delta_{\rm grid}
=================

# 1-\rho-\frac{\sigma_*}{n}

\frac{r-\sigma_*}{n}
]

is the largest safe grid radius, while the challenge threshold defined as a supremum is

[
\boxed{
\delta_C^*
==========

# 1-\rho-\frac{\sigma_*-1}{n}

\frac{r-\sigma_*+1}{n}.
}
]

The supremal endpoint itself is unsafe. A certificate must report both quantities.

---

# PROOF — exact syndrome padding

Suppose (z) is MCA-bad on a support (S) with (|S|\ge a), and put (E=L\setminus S), (e=|E|\le j). Then

[
u+zv\in V_E.
]

The failure of simultaneous explanation on the same (S) means that (u,v) are not both in (V_E). Since (u+zv\in V_E), membership (v\in V_E) would also imply (u\in V_E). Hence

[
v\notin V_E.
]

It remains to enlarge (E) to a (j)-set while preserving transversality. Extend the independent RS columns indexed by (E) to a basis

[
E\sqcup B,\qquad |B|=r-e.
]

Modulo (V_E), express the nonzero vector (v) in the basis indexed by (B). Choose one basis column (b_0) carrying a nonzero coefficient. Since

[
j-e=(r-e)-\sigma\le r-e-1,
]

choose (j-e) elements of (B\setminus{b_0}). Their union with (E) is a (j)-set (T) satisfying

[
u+zv\in V_T,\qquad v\notin V_T.
]

Conversely, such a (T) gives an agreement support (L\setminus T) of size (a), and (v\notin V_T) rules out simultaneous explanation there.

**BANKABLE_LEMMA.** The denominator-free (j)-span formula is exact, including overagreement.

---

# PROOF — arbitrary-defect partial-block packing

This closes a genuine gap in the Cycle 60 fixed-partition theorem.

Let

[
\mathcal B={B_1,\ldots,B_N}
]

be any family of pairwise disjoint blocks in (L), each of size (M). The blocks need not cover (L), and no assumption (M\mid k) is required.

Fix integers (b,d\ge0) satisfying

[
d+Mb=a=k+\sigma.
]

Let (Z) be a set of slopes on a proper-envelope-free syndrome line. For every (z\in Z), suppose an exact (a)-point witness has been selected in the form

[
S_z=D_z\sqcup\bigcup_{i\in A_z}B_i,
\qquad
|D_z|=d,\quad |A_z|=b,
]

where (D_z) is disjoint from the selected blocks. Put (J_z=L\setminus S_z), so (|J_z|=j), and assume

[
\ell(z)\in V_{J_z}.
]

For every integer (h) satisfying

[
0\le h\le d,
\qquad
d-h\le\sigma-1,
]

one has

[
\boxed{
|Z|\binom dh
\le
\binom Nb\binom{j+d}{h}.
}
]

Therefore

[
\boxed{
|Z|
\le
\min\left{
q_{\rm line},
\min_{\max(0,d-\sigma+1)\le h\le d}
\left\lfloor
\frac{\binom Nb\binom{j+d}{h}}{\binom dh}
\right\rfloor
\right}.
}
\tag{PB}
]

### Proof

Consider incidences ((z,C)) with (C\in\binom{D_z}{h}), and map

[
(z,C)\longmapsto (A_z,C).
]

There are (\binom dh) incidences per slope. For fixed (A), the subset (C) lies outside its (Mb) selected block points, leaving

[
n-Mb=n-(a-d)=j+d
]

possible points. Hence the target has size at most

[
\binom Nb\binom{j+d}{h}.
]

The map is injective. If two distinct slopes (z,z') had the same (A) and (C), then

[
|D_z\setminus D_{z'}|\le d-h\le\sigma-1.
]

Consequently,

[
|J_z\cup J_{z'}|
================

j+|D_z\setminus D_{z'}|
\le
j+\sigma-1
==========

r-1.
]

The two distinct line points lie in (V_{J_z}) and (V_{J_{z'}}), so

[
\operatorname{span}{u,v}
\subseteq
V_{J_z\cup J_{z'}},
]

a proper envelope, contradiction.

### Consequences

* If (d<\sigma), choose (h=0):

  [
  |Z|\le\binom Nb.
  ]

  Thus varying defects add no multiplicative penalty.

* If (d=\sigma), choose (h=1). For a full partition with (M\mid k), this recovers

  [
  |Z|\le\frac n\sigma\binom{N-1}{k/M}.
  ]

* It handles both Lattès packets directly:

  * degree (31): (N=131,b=67,d=2<31), giving (\binom{131}{67});
  * degree (113): (N=144,b=37,d=28<113), giving (\binom{144}{37}).

**BANKABLE_LEMMA.** The old fixed-defect/fixed-partition wall is substantially narrower now. The unsolved quotient wall is no longer per-partition packing; it is aggregation across inequivalent block systems and configuration factors.

---

# BANKABLE_LEMMA — interleaving is exactly scalar

If the worst scalar list has size at most (U) and

[
\binom{U+1}{2}<q_{\rm code},
]

then every interleaved list, of any arity, has size at most (U). A linear projection outside the union of pair-collision hyperplanes makes (U+1) interleaved codewords distinct while preserving every column agreement.

Conversely, a scalar list embeds as

[
P\longmapsto(P,0,\ldots,0).
]

At

[
T_q=\left\lfloor\frac q{2^{128}}\right\rfloor
]

and (q\le2^{256}),

[
\binom{T_q+1}{2}<q.
]

Hence, in the same-field official regime,

[
\boxed{
L_m(\sigma)\le T_q
\iff
L_1(\sigma)\le T_q
}
]

for every interleaving arity (m). The phrase “constant arity” is no longer mathematically relevant at the official threshold.

---

# COUNTERPACKET

The Cycle 58–60 counterpackets rule out several formerly plausible theorem shapes.

| Packet                            | What it proves                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| Degree-31 Lattès, rate (1/4)      | Genus-zero/PGL(_2), monomial, and toric-dihedral registries are incomplete           |
| Degree-113 CM-Lattès, rate (1/16) | The genus-one branch is not a sporadic low-degree anomaly                            |
| Divisor-norm character packet     | Point-fiber quotient templates do not exhaust the (t=1) configuration-space branch   |
| Star/Sidon scalar list packet     | Split-rational quotients plus common cores do not give a general scalar list theorem |
| High-denominator examples         | No general compression from (t>\sigma) to (t\le\sigma)                               |
| (t=2), high-(j) examples          | A pure (n^{1+o(1)}) MCA upper bound is false without occupancy                       |

**AUDIT.** I independently checked the finite arithmetic in both Lattès packets.

For the degree-31 packet:

[
#E(\mathbf F_{8191})=8153=31\cdot263,
]

the stated kernel coordinates and orders agree, and the rational fiber distribution is

[
31^{131},\quad16^1,\quad1^{4115}.
]

The exact threshold is

[
T_q=
80,951,559,894,234,747,884,481,262,824,352,
]

while the surviving packet has more than (2^{127}) distinct slopes.

For the degree-113 packet:

[
#E(\mathbf F_{65537})=65540,
]

the (113)-kernel and (580)-point image counts agree, and the image has exactly (144) free (C_4)-orbits. The exact target is

[
T_q=
5,193,485,407,918,146,305,910,242,003,458,339,
]

while

[
\binom{144}{37}
===============

32,877,924,651,615,125,350,719,849,588,315,840.
]

The remaining Lattès work is geometric proof review: arithmetic versus geometric Galois closure, constant fields, separability, ramification, and the exact monodromy/genus argument.

The divisor-norm packet is not at an exact official rate: (k/n\approx0.124762), not (1/8). It kills the broad primitive-completion lemma, but it does not by itself prove that an exact-rate official theorem must contain precisely that term.

---

# ROUTE_CUT

1. **The genus-zero/genus-one taxonomy is not the prize theorem.** It classifies individual maps. It does not bound the number of induced block systems, their overlaps, or their aggregate weight on one affine line.

2. **“Genus at least two implies discrepancy” is not currently a theorem.** Hasse–Weil bounds the number of split fibers of one fixed cover. It does not control the number of covers, growing genus, growing Galois group, or repeated support realizations.

3. **The exact divisor-norm trichotomy is probably false.** Product is only the first obvious configuration character. Other elementary symmetric functions, additive traces, multiple characters, and higher-codimension factors are natural counterexample sources.

4. **The raw three-term LIST-CONT theorem is incomplete.** The star/Sidon packet requires a low-affine-rank or polynomial-envelope branch, unless official smooth domains are separately proved to exclude that phenomenon.

5. **The (H_2)-defective “occupancy plus (2r)” charge is unsupported and likely false.** The 3-core extraction may be correct; the proposed global charge is not banked.

6. **Do not return to denominator-by-denominator analysis.** The universal (t=r) chart shows why high denominator degree is not an intrinsic class. Syndrome space is the correct global object.

7. **Do not promote a rate-only threshold formula.** Two codes at the same rate can have different quotient/Lattès/configuration profiles and therefore different finite transitions.

---

# EXACT_NEW_WALL

The MCA wall should now be renamed

[
\boxed{
\texttt{W-MCA-MULTIPLE-SUPPORT-FACTOR-AGGREGATION}.
}
]

Per fixed block system and profile, the packing problem is now controlled by ((\mathrm{PB})). What remains is to prove that all *heavy* realized support factors on one envelope-free line can be canonically clustered and charged without summing an uncontrolled number of profiles.

The other MCA walls are

[
\texttt{W-MCA-HEREDITARY-ENVELOPE-POTENTIAL},
]

and

[
\texttt{W-MCA-PRIMITIVE-SUPPORT-DISCREPANCY}.
]

For lists, the exact wall is

[
\boxed{
\texttt{W-LIST-LOW-ARITY-GLOBAL-CIRCUIT-TRANSVERSAL}.
}
]

It must output one global hitting set for all low-arity circuits of a syndrome, not a separate classification certificate for each circuit.

---

# Minimal theorem package

## MCA challenge

### Logical minimum

Only two new mathematical theorems are logically necessary:

1. A global finite upper theorem producing an explicit integer (U_{\rm MCA}(C,\sigma)) with

   [
   M_C(\sigma)\le U_{\rm MCA}(C,\sigma).
   ]

2. A previous-reserve lower theorem producing (B_{\rm MCA}(C,\sigma-1)) with

   [
   M_C(\sigma-1)\ge B_{\rm MCA}(C,\sigma-1).
   ]

Together with

[
U_{\rm MCA}(C,\sigma)\le T_{\rm MCA}
<
B_{\rm MCA}(C,\sigma-1),
]

the exact staircase is determined.

### Smallest realistic upper decomposition

For an envelope-free line, the theorem must prove an assigned decomposition of the form

[
|\operatorname{Bad}*\sigma(\ell)|
\le
U*{\rm block}
+
U_{\rm cfg}
+
\left\lceil
C_{\rm occ}
\frac{\binom nj}{q_{\rm line}^{\sigma-1}}
\right\rceil
+
D_{\rm prim}.
]

Here:

* (U_{\rm block}) aggregates realized partial block systems, including PGL(_2), Lattès, and any other point-fiber quotient;
* (U_{\rm cfg}) handles low-complexity configuration-space factors such as divisor norms;
* the occupancy term is unavoidable;
* (D_{\rm prim}) is the residual one-line discrepancy term.

For an enveloped line, a separate hereditary theorem must give (E_{\rm her}). The correct overall aggregation is

[
\boxed{
U_{\rm MCA}(\sigma)
===================

\max\left{
E_{\rm her},
,
U_{\rm block}+U_{\rm cfg}
+
\left\lceil
C_{\rm occ}
\frac{\binom nj}{q_{\rm line}^{\sigma-1}}
\right\rceil
+
D_{\rm prim}
\right}.
}
]

It is not a six-term sum across mutually exclusive line branches.

### Asymptotic requirement

For reserves above the corrected boundary, it is enough asymptotically to prove

[
\frac{
U_{\rm block}+U_{\rm cfg}+E_{\rm her}+D_{\rm prim}
}{q_{\rm line}}
\to0
]

and

[
\frac{\binom nj}{q_{\rm line}^{\sigma}}\to0.
]

Below the boundary, the Bessel/random-anchor branch should give a limiting error (>2^{-128}), preferably error one.

### Finite (2^{-128}) requirement

The asymptotic theorem is not a prize certificate. The finite version needs:

* explicit integer constants;
* exact profile weights;
* exact field attribution;
* exact envelope-tree recurrence;
* strict comparison with (\lfloor q_{\rm line}/2^{128}\rfloor);
* a lower certificate at the immediately preceding reserve.

The same-field Bessel–Paley lower bound is a viable previous-reserve certificate where its exact rational inequality clears the target. Otherwise an explicit line packet is needed.

---

## List challenge

The following objects are already banked:

[
L_C(\sigma)
===========

\max_s\sum_{e=0}^{j}\nu_e^\circ(s),
]

and, for a listed polynomial (P) of actual reserve

[
\tau(P)=|A(P)|-k\ge\sigma,
]

the space

[
W_P=p_PF[X]_{<\tau(P)}
\subseteq s^\perp.
]

If a set (Z_s) meets every full-support circuit, then

[
\sum_{P\notin Z_s}\tau(P)\le r-1,
]

and therefore

[
\boxed{
|\mathcal L_s|
\le
|Z_s|+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor.
}
]

It suffices to hit circuits of arity at most

[
\ell_\sigma=\left\lceil\frac r\sigma\right\rceil.
]

Thus the smallest missing upper theorem is:

> For every scalar syndrome (s), construct a canonical set (Z_s) hitting every support-minimal full-support circuit of arity at most (\ell_\sigma), with
> [
> |Z_s|
> \le
> U_{\rm block}
> +U_{\rm core}^{\rm her}
> +U_{\rm affine}^{\rm her}
> +U_{\rm prim}.
> ]

The finite safety condition is

[
\boxed{
U_{\rm block}
+U_{\rm core}^{\rm her}
+U_{\rm affine}^{\rm her}
+U_{\rm prim}
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor
\le T_{\rm list}.
}
]

A matching scalar lower list at (\sigma-1) then determines the exact threshold. Projection gives every interleaving arity for free.

The available previous-reserve list lower certificates include

[
B_{\rm ent}(\tau)
=================

\left\lceil
\frac{\binom n{k+\tau}}{q_{\rm gen}^{\tau}}
\right\rceil,
]

base-field lists that persist over extensions,

[
B_{\rm quot}(\tau)
==================

\max_{\substack{M\mid\gcd(n,k)\M>\tau}}
\binom{n/M-1}{k/M},
]

and explicit split-rational or configuration packets.

---

# Dependency DAG

```text
MCA-PRIZE-SOLVE                                             [UNKNOWN]
├── Exact syndrome numerator and reserve staircase          [ALREADY BANKED]
├── MCA finite safe upper                                   [UNKNOWN]
│   ├── Arbitrary-defect one-block-system packing            [ALREADY BANKED]
│   ├── Multiple block-system aggregation                    [UNKNOWN]
│   │   ├── Three-fiber descent / genus-zero registry        [LIKELY]
│   │   ├── Lattès/isogeny geometric registry                [LIKELY]
│   │   └── Genus≥2 aggregate Hasse-discrepancy claim        [DOUBTFUL]
│   ├── Configuration-factor hierarchy                       [UNKNOWN]
│   │   └── Envelope / point fiber / one norm trichotomy     [DOUBTFUL]
│   ├── Hereditary envelope recurrence                       [UNKNOWN]
│   │   ├── Internal envelope and petal floors               [ALREADY BANKED]
│   │   ├── Exact shortening step                            [LIKELY]
│   │   └── Bounded branching potential                      [UNKNOWN]
│   └── Primitive discrepancy                               [UNKNOWN]
│       ├── Hereditary MDS-3-core extraction                 [LIKELY]
│       ├── Occupancy + 2r H2-defect charge                  [DOUBTFUL]
│       ├── t=1 shifted-code reduction                       [ALREADY BANKED]
│       ├── t=1 apolar complete-intersection details         [LIKELY]
│       └── t=1 primitive inverse                            [UNKNOWN]
├── Previous-reserve MCA failure                            [LIKELY]
│   ├── Same-field Bessel–Paley theorem                      [ALREADY BANKED]
│   └── Explicit quotient/Lattès packets                     [LIKELY]
└── Exact finite certificate checker                        [LIKELY]

LIST-PRIZE-SOLVE                                            [UNKNOWN]
├── Exact scalar full-support identity                       [ALREADY BANKED]
├── Circuit reduction and reserve-weighted remainder         [ALREADY BANKED]
├── Global low-arity circuit hitting theorem                 [UNKNOWN]
│   ├── Exact common-core descent                            [ALREADY BANKED]
│   ├── Fixed split-rational profile charge                  [ALREADY BANKED]
│   ├── Low-affine-rank envelope branch                      [UNKNOWN]
│   ├── Primitive positive-splitting-excess branch           [UNKNOWN]
│   └── Bounded-overlap global hitting set                   [UNKNOWN]
├── Previous-reserve scalar lower list                      [LIKELY]
├── Scalar-to-all-interleavings projection                   [ALREADY BANKED]
└── Exact finite certificate checker                        [LIKELY]

Pure n^(1+o(1)) MCA upper                                   [FALSE]
General t>sigma compression                                 [FALSE]
Monomial/action-rank-only quotient registry                 [FALSE]
Point-fiber-only JR registry                                [FALSE]
Quotient-plus-common-core general list theorem              [FALSE]
Raw three-term LIST-CONT for general domains                [FALSE]
```

---

# PLAN — best next six theorem-worker prompts

## Prompt 1 — independently formalize the new packing theorem

```text
THEOREM-WORKER: W-MCA-ARBITRARY-DEFECT-PARTIAL-BLOCK-PACKING

Let C=RS[F,L,k], r=n-k, a=k+sigma, j=r-sigma. Let B_1,...,B_N
be pairwise disjoint M-subsets of L. On a proper-envelope-free affine
syndrome line, suppose every retained slope z has a selected exact witness

S_z = D_z disjoint-union union_{i in A_z} B_i,

with |D_z|=d, |A_z|=b, and d+Mb=a.

Prove or refute that for every h with
max(0,d-sigma+1) <= h <= d,

|Z| binom(d,h) <= binom(N,b) binom(j+d,h).

Give the optimized finite bound, including the field-size cap.

Acceptance criteria:
1. A complete injectivity proof using only MDS column spans.
2. Correct handling of d=0, d<sigma, d=sigma, and d>sigma.
3. No assumptions M|k or that the blocks cover L.
4. Recovery of the old fixed-partition theorem when d=sigma.
5. Explicit substitution of the degree-31 and degree-113 Lattes profiles.

Failure criterion:
An explicit prime-field RS instance with a proper-envelope-free line
violating the displayed inequality, verified directly from parity-check spans.
```

## Prompt 2 — the actual quotient wall

```text
THEOREM-WORKER: W-MCA-TWO-BLOCK-SYSTEM-OVERLAP

Let R_1,R_2 be separable rational maps inducing two families of disjoint
full blocks on the same smooth RS domain. Fix support profiles
(d_i,M_i,b_i) at agreement k+sigma. Study slopes on one proper-envelope-free
syndrome line admitting witnesses from both block systems.

Prove one of the following, or provide a finite counterexample:

(A) an explicit upper bound B_cross(n,k,sigma,M_1,M_2,deg R_1,deg R_2)
for the number of such slopes when R_1 and R_2 have no common right factor
and their block systems have no nontrivial common refinement;

(B) a structural theorem showing that a large overlap forces a common
right factor, a common configuration-space factor, or a proper syndrome
envelope.

Acceptance criteria:
1. The theorem is stated on induced support systems, not on one formula
   for a denominator.
2. It covers PGL2 and Lattes systems.
3. It yields a clustering/aggregation corollary bounding the total profile
   weight of all heavy systems on one line.
4. All constants are finite integers.

Failure criterion:
An official-cap, envelope-free line carrying many pairwise incompatible
heavy block systems whose aggregate exceeds every proposed bound.
```

## Prompt 3 — hereditary envelope potential

```text
THEOREM-WORKER: W-MCA-HEREDITARY-ENVELOPE-POTENTIAL

For an affine syndrome line with a minimal envelope R of size j+d<r,
separate internal witnesses from external witnesses using the exact Cycle 59
shortening data. Define a canonical child instance for every external class.

Prove or refute the existence of an integer-valued potential Phi such that:
1. every child has strictly smaller Phi;
2. internal slopes have the stated exact linear cap;
3. the sum or maximum of all child bounds is controlled by an explicit
   E_her(n,k,sigma), not by the raw number of subsets;
4. every slope is assigned to exactly one node.

Acceptance criteria:
A complete recurrence with base cases, exact floors, and a proof that the
total tree weight fits the maximum-over-lines MCA ledger.

Failure criterion:
A small explicit RS family whose canonical shortening tree has necessarily
superpolynomial total assigned weight despite every node satisfying the
local internal cap.
```

## Prompt 4 — (t=1) configuration inverse

```text
THEOREM-WORKER: W-JR-T1-CONFIGURATION-FACTOR-INVERSE

Work in the t=1 apolar complete-intersection normal form. After common-core
removal, every full-coordinate split locator has
P_T = A U_T + B V_T with gcd(U_T,V_T)=1 and pair intersection at most
j-sigma.

Do not assume the exact three-way trichotomy
'envelope / point-fiber quotient / one norm character'.

Prove either:
1. a finite hierarchy theorem saying that every large envelope-free packet
   factors through a bounded-codimension algebraic map on Sym^j(L), with
   an explicit profile charge and bounded overlap; or
2. a primitive discrepancy bound after all such factors of degree/codimension
   at most the stated cutoff are removed.

Acceptance criteria:
The product-character packet is recovered as one case; all factors and
charges are canonical and finite; the theorem bounds distinct colors/slopes,
not raw supports.

Failure criterion:
An explicit family outside the proposed hierarchy exceeding the primitive
bound, together with exact support and color counts.
```

## Prompt 5 — scalar list base case

```text
THEOREM-WORKER: W-LIST-M3-FULL-SUPPORT-CIRCUIT-COVER

Classify support-minimal three-term relations

U_1/G_1 + U_2/G_2 + U_3/G_3 = 0,
deg U_i < tau_i,

arising from actual full-support scalar RS list elements on an official
smooth domain. First remove the exact common agreement core.

Prove that every such circuit belongs to one of:
1. a certified split-rational block packet;
2. a bounded low-affine-rank polynomial envelope;
3. a primitive family having an explicit finite global hitting-set charge.

Acceptance criteria:
1. The result produces a hitting set for all m=3 circuits of one syndrome,
   not one classification witness per circuit.
2. Overagreement is charged by tau_i.
3. The constants and overlap convention are explicit.
4. The theorem is tested against the star/Sidon construction.

Failure criterion:
An exact smooth-domain circuit family with no listed structure and hitting
number exceeding the proposed primitive allowance.
```

## Prompt 6 — finite verifier

```text
THEOREM-WORKER / CODEX: W-FINITE-RS-PRIZE-CERTIFICATE-V1

Implement a deterministic verifier for supplied MCA/list theorem certificates.

It must:
1. use no binary floating-point decisions;
2. maintain q_gen, q_line, q_code, and q_chal separately;
3. compute T=floor(q/2^128) exactly;
4. verify maximum-versus-sum branch aggregation;
5. support exact small binomials and rigorous interval certificates for
   large binomials;
6. verify the arbitrary-defect partial-block formula;
7. verify circuit-free list remainders and projection collisions;
8. emit the safe grid radius and unsafe supremal endpoint separately;
9. return PASS, FAIL, INCONCLUSIVE, or INVALID_CERTIFICATE;
10. include regression certificates for both Lattes packets.

Acceptance criterion:
All comparisons affecting PASS/FAIL are exact integer or rigorous directed
interval comparisons, with canonical JSON and SHA-256 theorem manifests.

Failure criterion:
Any decision depends on math.log, lgamma, a decimal estimate, an unverified
field substitution, or an ambiguous overlap sum.
```

---

# Kill tests and counterexample searches

| Proposed lemma                    | Fast adversarial test                                                                                                                                                                                                |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exact syndrome formula            | For (q=7,17), (n\le8), enumerate direct support-wise MCA from words and compare with all (j)-span incidences. Any mismatch is fatal.                                                                                 |
| Partial-block packing             | Over (\mathbf F_{17}), enumerate all lines and partial (2)- and (3)-block systems for (n=8). Test every (d,h) in ((\mathrm{PB})).                                                                                    |
| Multiple-system overlap           | Enumerate all degree-2 and degree-3 rational maps over (\mathbf F_{17}) and (\mathbf F_{97}), deduplicate induced partitions, and find lines supporting many incompatible systems. Add small degree-3/5 Lattès maps. |
| Envelope potential                | For (q=7,n=6,k=1) and (q=17,n=8), enumerate minimal envelopes and every shortening child. Search for exponential branching or repeated slope assignment.                                                             |
| One-character JR trichotomy       | On cyclic groups of orders (8) and (16), bucket locators by product, (e_1), (e_2), trace, and pairs of characters. Search for large packets outside point fibers plus one product character.                         |
| H2-defect charge                  | Enumerate only set systems actually realized on one affine syndrome line. Random abstract 3-cores are irrelevant and can produce false counterexamples.                                                              |
| (m=3) list circuit classification | For (q=17,n=8,k=4), enumerate all scalar syndrome fibers, extract support-minimal circuits, and solve the minimum circuit hitting set exactly by brute force or ILP.                                                 |
| Affine-envelope omission          | Reproduce small star/Sidon analogues and test whether smooth multiplicative-domain constraints truly eliminate them.                                                                                                 |
| Base-to-extension MCA transfer    | Over small (B\subset F), compare (B)-valued and genuinely (F)-valued lines. This should quickly kill any attempted general MCA transfer.                                                                             |
| Threshold accounting              | Synthetic tests at (q<2^{128}), (q=2^{128}), and near (2^{256}); test strict failure (B>T), safe (U\le T), and endpoint rounding.                                                                                    |

The most likely false targets are:

* a single divisor-norm-character trichotomy;
* a universal (O(r)) H2-defect charge;
* a polynomial bound on all nonempty quotient packets without a heaviness condition;
* automatic high-genus discrepancy from Hasse–Weil alone;
* a simple additive envelope-tree recurrence;
* the assertion that solving (m=3) circuits automatically solves all critical arities.

---

# Verification and formalization plan

## Claims to verify first

1. **Exact MCA semantics and padding.** The proof above should be inserted into the formal source before any more container work.

2. **Arbitrary-defect partial-block packing.** This should replace the narrower (d=\sigma), (M\mid k), full-partition statement.

3. **Bessel–Paley lower theorem.** Independently recheck:

   * the joint-rank formula;
   * the exact second moment;
   * ceilings in the integer slope count;
   * the correction that (\lambda>QJ) is stronger, not weaker, than (\lambda>QV);
   * same-field assumptions.

4. **Projection and field expansion.** Promote after a short independent proof audit. For (B\subset F), expansion in a (B)-basis identifies scalar RS over (F) with an interleaving over (B), but the collision inequality must be paid over (B).

5. **Lattès geometry.** Arithmetic is now checked. Review:

   * field of definition and constant field of the Galois closure;
   * full-fiber simplicity;
   * monodromy and genus;
   * denominator nonvanishing;
   * envelope-freeness;
   * collision-exclusion argument.

6. **(t=1) apolar package.** Check every degree shift, Hilbert function, uniqueness of (P_T=AU+BV), the gcd criterion, and pair-intersection bound.

7. **Hereditary MDS-3-core.** Verify the syzygy and leaf-peeling extraction, but do not promote the unproved H2-defect charge.

8. **Configuration-character packet.** Verify the finite construction, while stating prominently that its rate is not exactly official.

9. **Scalar circuit theorem.** Check the syndrome pairing and Birkhoff–Grothendieck excess formula. The elementary circuit-hitting inequality itself is ready for promotion.

10. **Paper D import.** The exact CS25 theorem, code dimension shift (k\leftrightarrow k+1), integer-radius condition, and constants must be checked against the primary source before the cap is called unconditional.

## TeX promotion policy

Promote after one independent proof review and one regression test:

* exact syndrome equivalence;
* reserve staircase;
* scalar full-support identity;
* scalar circuit reduction;
* projection theorem;
* fixed-core petal theorem;
* arbitrary-defect partial-block packing.

Do not yet promote as final theorems:

* the global low-genus quotient classifier;
* genus-(\ge2) discrepancy;
* H2-defect finite charge;
* one-character JR trichotomy;
* raw LIST-CONT;
* unconditional Paper D cap.

The repository’s existing verification layer is not certificate-grade:

* `entropy_margin.py` and `interleaved_budget.py` use floating logarithms and encode obsolete ledgers;
* `certificate_emit.py` formats JSON but proves nothing;
* the reproducibility audit checks 81 scripts and flags 30 for review;
* `tex_reference_integrity_audit.py` currently resolves the TeX root incorrectly and fails from the documented repository root.

---

# PLAN — first finite certificate script specification

The first verifier should be named

```text
experimental/scripts/rs_prize_certificate_v1.py
```

and should verify supplied certificates rather than attempt theorem discovery.

## Input contract

```json
{
  "schema": "rs-prize-certificate-v1",
  "instance": {
    "characteristic": "...",
    "q_gen": "...",
    "q_line": "...",
    "q_code": "...",
    "q_chal": "...",
    "n": "...",
    "k": "...",
    "rate_numerator": "...",
    "rate_denominator": "...",
    "domain_type": "multiplicative_coset",
    "domain_order_factorization": {},
    "field_embedding_evidence": {}
  },
  "candidate": {
    "sigma_safe": "...",
    "sigma_previous": "..."
  },
  "mca": {
    "upper": {},
    "previous_reserve_lower": {}
  },
  "list": {
    "upper": {},
    "previous_reserve_lower": {}
  },
  "theorem_manifest": []
}
```

All proof-relevant integers should be canonical decimal strings. Every theorem entry should carry an identifier, version, source-file digest, hypotheses, and aggregation role.

## Supported upper terms

The first version should understand only explicit, audited term types:

* `occupancy_upper`;
* `fixed_defect_block_profile`;
* `varying_defect_partial_block_profile` using ((\mathrm{PB}));
* `configuration_profile`;
* `envelope_tree_node`;
* `primitive_integer_allowance`;
* `circuit_hitting_allowance`;
* `circuit_free_remainder`.

No arbitrary executable formula should be accepted.

## Supported lower terms

* exact or bounded Bessel–Paley;
* entropy pigeonhole;
* quotient-core binomial;
* explicit split-rational packet;
* explicit configuration packet;
* explicit list/slope enumeration for toy cases.

## Arithmetic requirements

* Exact `floor`, `ceil`, and rational comparisons.
* No `float`, `math.log`, `lgamma`, or decimal estimates in decisions.
* Small binomials via exact integers under a configurable bit budget.
* Large binomials through rigorous ball intervals, preferably Arb/FLINT, using:

  * entropy bounds first;
  * Robbins/Stirling refinement if necessary;
  * `INCONCLUSIVE` if the interval still straddles the threshold.
* Do not materialize (\binom n a) when (n) may be (2^{44}).
* Verify prime-power and field-inclusion evidence, or require a supplied Pocklington/Pratt-style certificate.
* Verify domain divisibility such as (n\mid q_{\rm code}-1).
* Verify (k\le2^{40}), (q<2^{256}), and exact rate.
* Verify all strict versus non-strict comparisons.

## Aggregation rules

The certificate expression must distinguish:

* `max`: mutually exclusive line classes, such as enveloped versus envelope-free;
* `sum`: disjoint or canonically assigned slope/list classes;
* `min(q,...)`: field-size cap;
* recursion: hereditary child theorem.

The verifier must reject a sum if the theorem manifest does not state a disjoint assignment or a justified union bound.

## Required outputs

```text
MCA_SAFE / MCA_UNSAFE / MCA_UNDECIDED
LIST_SAFE / LIST_UNSAFE / LIST_UNDECIDED
sigma_star, if bracketed exactly
safe_grid_radius as a reduced rational
supremal_transition as a reduced rational
endpoint_safe = false/unknown
exact target numerators
exact or rigorous upper/lower slacks
field ledger used by every term
projection collision result
theorem manifest SHA-256
```

Exit codes should distinguish invalid certificates from mathematically inconclusive certificates.

## Mandatory regression tests

* Degree-31 Lattès threshold and profile.
* Degree-113 Lattès threshold and profile.
* (d<\sigma), (d=\sigma), and (d>\sigma) block profiles.
* (q<2^{128}), where (T=0); in particular, list safety is impossible because the worst list is at least one.
* (q=2^{128}) and near-(2^{256}) projection checks.
* Safe-at-(\sigma), unsafe-at-(\sigma-1) endpoint staircase.
* Artificial example where replacing `max` by `sum` changes the result.
* Rejection of a certificate using (q_{\rm chal}) in place of (q_{\rm code}) or (q_{\rm line}).

A separate companion program,

```text
rs_prize_small_oracle.py
```

should compute exact (M_C(\sigma)), exact scalar lists, support-minimal circuits, and minimum hitting sets for tiny prime-field instances. It is a conjecture killer, not an official-size verifier.

---

# Resource allocation

## Round 1 — verification and route narrowing

| Worker | Assignment                                                                             |
| -----: | -------------------------------------------------------------------------------------- |
|      1 | Formalize exact syndrome equivalence and arbitrary-defect partial-block packing        |
|      2 | Two-block-system overlap theorem or counterpacket                                      |
|      3 | Hereditary envelope potential and exhaustive small-case search                         |
|      4 | (t=1) apolar/configuration-factor inverse                                              |
|      5 | H2-core realizability and adversarial test of the proposed finite charge               |
|      6 | Scalar (m=3) circuit classification                                                    |
|      7 | Scalar low-affine-rank envelope detector and smooth-domain exclusion test              |
|      8 | Exact certificate verifier and small oracle                                            |
|      9 | Meta-referee: Lattès geometry, Paper D import, theorem-manifest and field-ledger audit |

The local Fable/Codex loop should handle finite-field enumeration, ILP circuit hitting sets, exact arithmetic, conjecture mutation, and regression generation. It should not be used to promote theorem statements merely because small cases pass.

The human/PRZ review should first check:

1. the exact MCA support semantics and padding proof;
2. the Crites–Stewart import and off-by-one conditions;
3. the Lattès Galois-closure arguments;
4. the (t=1) apolar degree bookkeeping.

Those are higher leverage than reviewing more numerical packet tables.

## Round 2 — contingent allocation

If the two-block-system overlap theorem survives:

* 3 workers on global block/configuration aggregation;
* 2 workers on primitive MCA discrepancy;
* 2 workers on list circuits (m=3\to4) and global hitting;
* 1 worker on envelope recurrence;
* 1 worker on certificate integration/adversarial review.

If it fails by a new configuration factor:

* 3 workers formalize the counterfactor and define the minimal enlarged factor object;
* 2 workers test whether the enlarged hierarchy stabilizes in (t=1);
* 2 workers remain on scalar list circuits;
* 1 worker maintains the finite verifier;
* 1 worker independently attempts to kill the revised theorem.

If a second qualitatively new factor appears after that enlargement, stop expanding the named-template registry. That would be evidence that the route needs a general algebraic regularity/local-limit theorem on configuration space rather than another taxonomy cycle.

---

# Route to a full solve

The next load-bearing theorem is **not another genus classifier**. The per-block-system support count is now under control. The next exact lemma is:

[
\boxed{
\texttt{W-MCA-TWO-BLOCK-SYSTEM-OVERLAP}
}
]

followed by its global heavy-factor aggregation corollary.

That theorem determines whether “quotient contribution” is a finite, chargeable object or an open-ended list of unrelated maps. Without it, the primitive complement is not well-defined: a slope declared primitive today may become a new quotient packet tomorrow.

In parallel, the best tractable list target is the (m=3) full-support circuit cover. Success there would reveal whether the scalar wall admits an induction on circuit arity or whether genuinely new structures appear immediately at (m=4).

The route remains plausible only under the following sequence:

1. Formalize the exact reductions and the new arbitrary-defect packing theorem.
2. Prove heavy support factors aggregate on one line.
3. Bound the hereditary envelope tree.
4. Prove a primitive support-discrepancy theorem, beginning with (t=1).
5. Prove the scalar low-arity global circuit transversal.
6. Insert exact constants into the finite verifier.
7. Certify safety at (\sigma_*) and failure at (\sigma_*-1), code by code.

At present, steps 2–5 are open. Steps 2 and 5 are hard inverse theorems, not bookkeeping. That is the precise obstruction to a full prize solution.
