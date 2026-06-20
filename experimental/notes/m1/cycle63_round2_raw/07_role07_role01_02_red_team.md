AUDIT

## 1. Executive verdict and confidence

Both Cycle 62 algebraic lemmas survive red-team review.

* `L-LIST-APOLAR-ALL-LAYER-CI`: **bankable**.
* `L-LIST-MINIMAL-CI-GJ-FIBER`: **bankable only with the stated strict hypothesis (j>d=\sigma+1)**.
* Confidence: **high, 0.99**.

Necessary wording corrections:

1. Replace every projective use of “monic locator” by “proportional over (F^\times) to the chosen homogeneous locator.” Monicity is not intrinsic when infinity is allowed.
2. Define
   [
   D={x\in L:A(x)\neq0}
   ]
   rather than informally subtracting scheme-theoretic supports.
3. Define “squarefree” as “the divisor (V(A)) is reduced,” not via ordinary derivative tests in small characteristic.
4. Define (\widehat G=\operatorname{Hom}(G,\mathbf C^\times)) in the Fourier formula.
5. Retain (s\neq0) and (j>d) explicitly whenever Role 02 is cited. The equality case is a different pencil statement.
6. State the actual GRS parity-check normalization: the column at (x) is (w_x\operatorname{ev}_x) for a specific nonzero dual multiplier (w_x), not an unexplained unweighted evaluation column.

There is one packaging defect: Role 01 cites `verify_scalar_apolar_ci_all_layers.py` and a JSON report, but neither artifact is present in the supplied archive. This does not affect the proof, but the quoted computational counts are not independently bankable from this packet.

---

## 2. Formal audited theorem

Let (F) be a field, let (L\subset\mathbf P^1(F)) be a set of (n) distinct points, and let (C) be a projective GRS code of dimension (k). Put

[
r=n-k,\qquad N=r-1,\qquad
1\le \sigma\le r,\qquad j=r-\sigma.
]

Choose a parity-check basis in which

[
h_x=w_x\operatorname{ev}_x^{(N)},\qquad w_x\in F^\times.
]

For a syndrome (s), let (\Lambda_s\in S_N^*), (S=F[X_0,X_1]), be the corresponding functional, and define

[
(I_s)*e=
{P\in S_e:\Lambda_s(PQ)=0\ \forall Q\in S*{N-e}}
\quad(0\le e\le N),
]

with ((I_s)_e=S_e) for (e>N).

For (x\in L), choose a linear form (\ell_x) vanishing at (x), and for (E\subseteq L) put

[
p_E=\prod_{x\in E}\ell_x.
]

### Audited Role 01 statement

If (s\neq0), then

[
I_s=(A,B),\qquad \gcd(A,B)=1,
\qquad d:=\deg A\le b:=\deg B,
\qquad d+b=r+1.
]

For every (E\subseteq L), (e=|E|\le j),

[
s\in\operatorname{span}{h_x:x\in E}
\iff p_E\in(I_s)_e.
]

The representation on (E) is unique. Moreover,

[
(I_s)*e=A S*{e-d}\oplus B S_{e-b},
]

so there is a unique pair

[
p_E=AU_E+BV_E.
]

If

[
s=\sum_{x\in E}c_xh_x,\qquad
Z_E={x\in E:c_x=0},
]

then, with the convention (\gcd(U,0)=U),

[
\boxed{\gcd(U_E,V_E)\sim p_{Z_E}}.
]

Therefore (E) is the actual error support, rather than a padded support, exactly when

[
\gcd(U_E,V_E)=1.
]

If (E) is full-coordinate and (e<b), then

[
e=d,\qquad p_E\sim A.
]

If (s=0), then (I_s=S), and the only full-coordinate support of size at most (j) is (E=\varnothing).

### Audited Role 02 statement

Assume further that

[
d=\sigma+1,\qquad b=j>d.
]

Let

[
\Delta=V(A),\qquad
D={x\in L:A(x)\neq0}.
]

Choose a linear form (L_*) whose restriction to (\Delta) is a unit. Put

[
R_\Delta=H^0(\Delta,\mathcal O_\Delta),\qquad
G_\Delta=R_\Delta^\times/F^\times,
]

[
\alpha_\Delta(x)=
\left[\left.\frac{\ell_x}{L_*}\right|*\Delta\right],
\qquad
b*\Delta=
\left[\left.\frac{B}{L_*^j}\right|_\Delta\right].
]

Then, for (T\in\binom Lj),

[
\boxed{
T\text{ is full-coordinate}
\iff
T\subseteq D
\text{ and }
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta.
}
]

Consequently,

[
\boxed{
N_s(\sigma)=
\mathbf 1_{{\exists E\in\binom Ld:\ p_E\sim A}}
+
#\left{
T\in\binom Dj:
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta
\right}.
}
]

The indicator condition is equivalently that (V(A)) is reduced and all its closed points are distinct (F)-rational points belonging to (L).

If

[
\Delta=\sum_i m_iP_i,\qquad
f_i=[\kappa(P_i):F],
]

then

[
\boxed{
|G_\Delta|
==========

\frac1{q-1}
\prod_i q^{(m_i-1)f_i}(q^{f_i}-1).
}
]

For (x_0\in D), define

[
G_{\mathrm{eff}}
================

\left\langle
\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1}:x\in D
\right\rangle.
]

Writing

[
\beta_x=\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1},
\qquad
h_b=b\alpha_\Delta(x_0)^{-j},
]

the exact Fourier count is

[
N_{\Delta,j}(b)
===============

\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi\in\widehat{G_{\mathrm{eff}}}}
\chi(h_b^{-1})
[z^j]\prod_{x\in D}(1+z\chi(\beta_x))
]

when (h_b\in G_{\mathrm{eff}}), and is zero otherwise.

---

## 3. Full proof and edge-case audit

### 3.1 Compatibility with actual RS/GRS parity-check columns

Projective GRS duality gives

[
C^\perp=\operatorname{GRS}_r(L,u)
]

for nonzero dual multipliers (u_x). Hence, after choosing the monomial basis of (S_N), a parity-check matrix has columns

[
h_x=u_x\operatorname{ev}_x^{(N)}.
]

For affine (x=a=[1:a]),

[
h_a=u_a(1,a,\ldots,a^N)^{\mathsf T}.
]

With (\infty=[0:1]),

[
h_\infty=u_\infty(0,\ldots,0,1)^{\mathsf T}.
]

For an error vector (e),

[
s=He=\sum_x e_xh_x.
]

All (u_x) are nonzero, so passing between weighted and unweighted evaluation columns never changes which coefficients vanish. Thus “full-coordinate” in the apolar argument is exactly actual nonzero error support in RS/GRS coordinates.

### 3.2 Complete-intersection structure

Let (R_s=S/I_s). Multiplication followed by (\Lambda_s) gives

[
(R_s)*e\times(R_s)*{N-e}\longrightarrow F.
]

This pairing is perfect by the definition of (I_s). Since (s\neq0),

[
\dim_F(R_s)_N=1.
]

No nonzero class below degree (N) can lie in the socle: if (P\in(R_s)*e), (e<N), were killed by both degree-one variables, it would be killed by all of (S*{N-e}), contradicting perfectness.

Hence (R_s) is a standard graded Artinian Gorenstein quotient of the two-variable polynomial ring, with socle degree (N) and type one. By the Hilbert–Burch resolution, a height-two Artinian ideal with type one has exactly two minimal generators. Therefore

[
I_s=(A,B)
]

is a regular sequence.

The Koszul resolution gives socle degree

[
d+b-2=N,
]

hence

[
d+b=r+1.
]

No derivative, factorial, or characteristic restriction occurs here.

### 3.3 Locator criterion and uniqueness

For (E\subseteq L), (e=|E|\le j\le N), the degree-(N) forms vanishing on (E) are exactly

[
p_ES_{N-e}.
]

Indeed, each (\ell_x) divides such a form, and the distinct (\ell_x) are pairwise nonassociate.

The annihilator of this space is

[
(p_ES_{N-e})^\perp
==================

\operatorname{span}{\operatorname{ev}_x:x\in E}.
]

Its dimension is (e), and the evaluation functionals are independent because any (e\le N+1=r) points of the degree-(N) rational normal curve are independent. Nonzero GRS multipliers do not change their span. Therefore

[
p_E\in I_s
\iff
s\in\operatorname{span}{h_x:x\in E}.
]

The same independence gives uniqueness of the coefficient vector.

### 3.4 Unique CI decomposition

The map

[
S_{e-d}\oplus S_{e-b}\to(I_s)_e,
\qquad
(U,V)\mapsto AU+BV
]

is surjective. If (AU+BV=0), coprimality gives

[
U=BW,\qquad V=-AW
]

with (W\in S_{e-d-b}). But

[
e\le j\le r-1<r+1=d+b,
]

so (W=0). Thus the decomposition is unique through the endpoint (e=j).

### 3.5 Exact padding divisor

Let (Z_E={x:c_x=0}). Removing zero coordinates gives a representation on (E\setminus Z_E), hence

[
p_{E\setminus Z_E}\in I_s.
]

Writing

[
p_{E\setminus Z_E}=AU_0+BV_0
]

and multiplying by (p_{Z_E}), uniqueness gives

[
U_E=p_{Z_E}U_0,\qquad
V_E=p_{Z_E}V_0.
]

Thus (p_{Z_E}\mid\gcd(U_E,V_E)).

Conversely, every irreducible common divisor of (U_E,V_E) divides (p_E). Since (p_E) is a product of distinct (F)-linear factors, such a divisor is some (\ell_x), (x\in E). Dividing the coefficient pair by (\ell_x) shows

[
p_E/\ell_x\in I_s,
]

so (s) is represented on (E\setminus{x}). Uniqueness of the representation on (E) then forces (c_x=0).

Therefore

[
\gcd(U_E,V_E)\sim p_{Z_E}.
]

This completely handles non-full-coordinate padding.

### 3.6 Low-generator collapse

When (e<b),

[
p_E=AU_E,\qquad V_E=0.
]

If the support is full-coordinate, then (\gcd(U_E,0)=U_E) is a unit. Thus

[
e=d,\qquad p_E\sim A.
]

Such an (E) exists precisely when the divisor (V(A)) is reduced and equals

[
\sum_{x\in E}[x]
]

for some (E\subseteq L).

### 3.7 The degree-(j) generalized-Jacobian slice

Under (d=\sigma+1<j=b),

[
(I_s)*j=A S*{j-d}\oplus FB.
]

Therefore

[
p_T=AU+cB
]

uniquely. Since (j-d>0),

[
T\text{ full-coordinate}
\iff c\neq0.
]

If (c=0), then (p_T=AU) and (U) is a positive-degree common divisor of the coefficient pair; this is precisely padded use of the low support (V(A)).

Now (L_*) trivializes (\mathcal O_{\mathbf P^1}(1)|_\Delta). For degree-(j) forms (F_1,F_2),

[
F_1|*\Delta=F_2|*\Delta
\iff
F_1-F_2\in A S_{j-d}.
]

This remains true for nonreduced (\Delta), because (\Delta) is the Cartier divisor cut out by (A).

Moreover, (\gcd(A,B)=1) implies (B|_\Delta) is a unit. At every local Artin component, the residue of (B) is nonzero, so (B) is invertible there.

For (T\subseteq D),

[
\left.\frac{p_T}{L_*^j}\right|_\Delta
=====================================

\prod_{x\in T}
\left.\frac{\ell_x}{L_*}\right|_\Delta.
]

Equality of its class with (b_\Delta) means exactly that, for some (c\in F^\times),

[
p_T-cB\in A S_{j-d}.
]

Equivalently,

[
p_T=AU+cB,\qquad c\neq0,
]

which is exactly the full-coordinate condition.

If (T) contained a point of (\operatorname{Supp}\Delta), then one factor (\ell_x|*\Delta) would be a nonunit. Its product could not equal the unit (cB|*\Delta). Hence the disjointness condition is both necessary and sufficient.

### 3.8 Nonreduced and nonsplit (\Delta)

Write

[
\Delta=\sum_i m_iP_i.
]

Then

[
R_\Delta\cong\prod_iR_i,
\qquad
R_i=H^0(m_iP_i,\mathcal O_{m_iP_i}).
]

Each (R_i) is an Artin local ring with residue field (\mathbf F_{q^{f_i}}). Reduction gives

[
1\to1+\mathfrak m_i\to R_i^\times
\to\mathbf F_{q^{f_i}}^\times\to1.
]

The maximal ideal has (F)-dimension ((m_i-1)f_i), so

[
|1+\mathfrak m_i|=q^{(m_i-1)f_i}.
]

Thus

[
|R_i^\times|
=q^{(m_i-1)f_i}(q^{f_i}-1),
]

giving the claimed group order after quotienting by diagonal (F^\times).

This simultaneously handles:

* repeated rational roots;
* repeated nonsplit closed points;
* roots at infinity;
* arbitrary characteristic.

### 3.9 Effective group and Fourier inversion

Fix (x_0\in D) and put

[
a_0=\alpha_\Delta(x_0),\qquad
\beta_x=\alpha_\Delta(x)a_0^{-1}.
]

Every (j)-fold product lies in

[
a_0^jG_{\mathrm{eff}}.
]

Changing (x_0) replaces the generators by pairwise quotients and gives the same subgroup.

For (h_b=ba_0^{-j}), character orthogonality yields

[
\mathbf 1_{{\prod_{x\in T}\beta_x=h_b}}
=======================================

\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi\in\widehat{G_{\mathrm{eff}}}}
\chi(h_b^{-1})
\prod_{x\in T}\chi(\beta_x).
]

Summing over (j)-subsets gives the asserted coefficient formula. The trivial-character contribution is exactly

[
\frac{\binom{|D|}{j}}{|G_{\mathrm{eff}}|}.
]

### 3.10 Generator shear and auxiliary choices

For unequal degrees, every generator change is

[
A'=aA,\qquad
B'=cB+AC,
]

with (a,c\in F^\times). At the coefficient-pair level,

[
(U,V)\mapsto
\left(U-c^{-1}CV,;c^{-1}V\right).
]

This is a unimodular transformation over (S), so the ideal ((U,V)), and hence its gcd, is unchanged.

On (\Delta),

[
B'|*\Delta=cB|*\Delta,
]

so (b_\Delta) is unchanged in (R_\Delta^\times/F^\times).

Changing (L_*) multiplies every (\alpha_\Delta(x)) by the same class (u) and multiplies (b_\Delta) by (u^j). Therefore the product equation and normalized Fourier target are unchanged.

When (d=b), every generator change is in (\operatorname{GL}_2(F)); the coefficient pair transforms by its inverse, again preserving the generated ideal and gcd.

---

## 4. Required edge-case ledger and exact finite relevance

| Check                           | Audit result                                                                                                      |   |      |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- | - | ---- |
| Zero syndrome                   | (I_0=S); independence of at most (j<r) columns implies only the empty support is full.                            |   |      |
| Equal degrees (j=d)             | Role 01 survives; Role 02 must not be applied. The degree-(j) object is a projective pencil.                      |   |      |
| Roots at infinity               | Use homogeneous locators, e.g. (\ell_\infty=X_0) for (\infty=[0:1]). No affine degree is lost.                    |   |      |
| Repeated/nonreduced (\Delta)    | Fully covered by the Cartier-divisor restriction and local Artin-unit argument.                                   |   |      |
| Nonsplit closed points          | Fully covered by residue extensions (\kappa(P_i)=\mathbf F_{q^{f_i}}).                                            |   |      |
| Small characteristic            | Proof uses multiplication pairings, not ordinary differential apolarity.                                          |   |      |
| Generator shear                 | Gcd ideal and GJ target are invariant.                                                                            |   |      |
| Non-full padding                | Exactly measured by (p_{Z_E}).                                                                                    |   |      |
| (D) empty or too small          | In the strict RS stratum it is automatically large enough; see below. The formal formula also returns zero when ( | D | <j). |
| Endpoint (e=j)                  | Safe because (j<d+b); no syzygy ambiguity occurs.                                                                 |   |      |
| Projective/affine normalization | Statements must be up to (F^\times); “monic” is optional affine gauge only.                                       |   |      |
| Actual RS/GRS columns           | Dual multipliers are nonzero and preserve coefficient support.                                                    |   |      |

In the strict Role 02 stratum,

[
r=d+j-1,\qquad d<j.
]

Since (\operatorname{Supp}\Delta) contains at most (d) rational points,

[
|D|\ge n-d
=(k+r)-d
=k+j-1.
]

For the standard code range (k\ge1),

[
\boxed{|D|\ge j.}
]

Thus (D=\varnothing) and (|D|<j) cannot occur in the actual strict minimal RS stratum.

Likewise,

[
d<r\le n\le q+1,
]

so (\Delta) cannot contain every rational point of (\mathbf P^1(F_q)). A suitable (L_*) therefore exists automatically.

### Exact equality-edge packet

The strict inequality in Role 02 is genuinely necessary for its coefficient criterion.

Take

[
F=\mathbf F_3,\qquad
L=\mathbf P^1(\mathbf F_3),\qquad
n=4,\quad k=1,\quad r=3,\quad
\sigma=1,\quad j=d=2.
]

Let (\Lambda\in S_2^*) satisfy

[
\Lambda(X^2)=1,\qquad
\Lambda(XY)=0,\qquad
\Lambda(Y^2)=1.
]

Then

[
I_\Lambda=(XY,\ X^2-Y^2).
]

The locator

[
A=XY
]

has support ({0,\infty}), and

[
\Lambda=\operatorname{ev}*0+\operatorname{ev}*\infty
]

is full-coordinate on it. The second generator is proportional to the locator of ({1,2}), and

[
\Lambda=2\operatorname{ev}_1+2\operatorname{ev}_2
]

is also full-coordinate.

Thus at (j=d), the coefficient pair ((1,0)) is full-coordinate. The implication “full iff the (B)-coefficient is nonzero” would fail if Role 02 were extended to equality. The actual strict statement excludes this packet and is correct.

---

## 5. Bankable versus conditional

### Bankable

* Characteristic-free complete-intersection structure for nonzero syndromes.
* All-layer locator/span equivalence.
* Unique coefficient-pair decomposition through (e=j).
* Exact zero-coordinate divisor
  [
  \gcd(U_E,V_E)\sim p_{Z_E}.
  ]
* Low-generator collapse.
* Zero-syndrome count (N_0(\sigma)=1).
* Equal-degree pencil description and (\operatorname{GL}_2(F))-invariance.
* Strict minimal-stratum generalized-Jacobian equivalence.
* Nonreduced, nonsplit, and infinity cases.
* Exact (G_\Delta) order.
* Effective product coset and finite Fourier expansion.
* Independence of (L_*), locator scaling, basepoint, and generator shear.
* Compatibility with actual RS/GRS error supports.

### Conditional or requiring correction

* Role 02 cannot be quoted at (j=d) without adding the separate pencil member (A).
* “Monic (A)” is not projectively bankable; use (A\sim p_E).
* Ordinary derivative apolarity is not a valid substitute in small characteristic unless expressed with divided powers.
* The Role 01 computational audit counts are not reproducible from the supplied archive because its cited verifier and JSON are absent.
* No local-limit, collision-mass, or block-trade estimate follows from these algebraic lemmas alone.

---

## 6. Failure point

There is no mathematical failure inside the stated hypotheses.

The exact scope boundary is

[
s\neq0,\qquad
\deg A=\sigma+1,\qquad
\deg B=j>\sigma+1,\qquad
\gcd(A,B)=1
]

for the Role 02 theorem.

The proof does not address configuration-level multiplicity inside a fixed generalized-Jacobian fiber. That is the genuine remaining obstruction, not an apolar or generalized-Jacobian defect.

---

## 7. Next exact lemma or construction

A route to a full solve remains credible, with **moderate confidence**, because the scalar algebraic reduction survives intact.

The next exact construction is

```text
L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE
```

and, more specifically, its unresolved core:

```text
L-MODEL-GJ-CANONICAL-MAXIMAL-KD-ASSIGNMENT-AND-OVERLAP
```

It must assign every support profile

[
D\cup\bigcup_{cK\in S}cK
]

to one canonical maximal subgroup/defect pair ((K,D)), invariant under the allowed gauges, and prove an exact finite non-double-counting or bounded-overlap theorem for the resulting block charges.

The block-collapse identity itself is elementary:

[
\prod_{u\in K}(X-cuZ)
=====================

X^{|K|}-c^{|K|}Z^{|K|}
\equiv X^{|K|}
\pmod{Z^\sigma}
\quad(|K|\ge\sigma).
]

Thus the next obstruction is not the jet calculation. It is the canonical maximal block assignment and its overlap mass.
