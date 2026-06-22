LABEL: PROOF

EXECUTIVE VERDICT:

Cycle84 admits an exact, paper-facing transfer to a genuine **standard Reed–Solomon support-wise MCA and line-decoding lower bound**. The missing transfer theorem is a fixed-leading-jet locator theorem.

For the native Cycle84 parameters, it gives
[
C=\operatorname{RS}!\left[\mathbb F_{17^{16}},\langle\eta\rangle,137\right],
\qquad
\delta=\frac{113}{256},
]
and one affine (t=1) line containing at least
[
52{,}747{,}567{,}092
]
distinct support-wise MCA-bad slopes.

Moreover, fixed-root padding gives smooth power-of-two subgroup rows over (\mathbb F_{17^{32}}) at the prize rates (1/2) and (1/4), with the same numerator. These are mathematically valid finite RS-MCA rows, but the packet does **not** justify calling them official Proximity Prize counterpackets: Cycle92 leaves extension-field admissibility and the official source/challenge contract unresolved. If extension fields are rejected, a loss-preserving embedding into an accepted prize field remains missing.

Confidence: high.

EXACT THEOREM OR OBSTRUCTION:

### Fixed-jet locator-to-line-MCA theorem

Let (D\subseteq F) consist of (n) distinct points, let (\beta\notin D), and let (\mathcal J) be a family of (j)-subsets of (D). Write
[
P_J(X)=\prod_{a\in J}(X-a).
]

Assume that, for some (\sigma\ge 1),
[
\deg(P_J-P_{J'})\le j-\sigma
\qquad\text{for all }J,J'\in\mathcal J.
\tag{FJ}
]
Thus all locators have a common leading (\sigma)-jet. Put
[
k=n-j-\sigma,\qquad C=\operatorname{RS}[F,D,k].
]

Then there is one affine line
[
u_z=f+zg,\qquad z\in F,
]
such that every
[
z_J=P_J(\beta)^{-1}
]
is support-wise MCA-bad for (C) at radius
[
\delta=\frac jn,
]
with witness support
[
S_J=D\setminus J,\qquad |S_J|=n-j=k+\sigma.
]

Consequently,
[
\epsilon_{\rm mca}!\left(C,\frac jn\right)
\ge
\frac{\left|{P_J(\beta):J\in\mathcal J}\right|}{|F|},
\tag{1}
]
and
[
LD_{\rm sw}(C,n-j)
\ge
\left|{P_J(\beta):J\in\mathcal J}\right|.
\tag{2}
]

The indexed map (J\mapsto z_J) has exactly the same fiber histogram as (J\mapsto P_J(\beta)), because inversion is a bijection on (F^\times).

The line is a degree-(1) residue line with
[
E(X)=X-\beta.
]

### Cycle84 instantiation

For a Cycle84 tuple (T), let
[
J_T={1}\cup
\bigcup_{t=1}^7\eta^t\operatorname{lift}(i_t,a_t),
\qquad |J_T|=113,
]
and
[
P_T(X)=\prod_{x\in J_T}(X-x).
]

The three packet base polynomials
[
\prod_{e\in E_i}(Z-3^e)
]
have zero (Z^7) and (Z^6) coefficients. Hence each (16)-point slot locator has the form
[
X^{16}+O(X^{10}),
]
and therefore
[
P_T(X)=X^{113}-X^{112}+R_T(X),
\qquad \deg R_T\le107.
\tag{3}
]
Thus
[
\deg(P_T-P_{T'})\le107=113-6,
]
so the fixed-jet theorem applies with
[
(n,k,\sigma,j)=(256,137,6,113).
]

The packet slot factorization gives the exact evaluation identity
[
P_T(\beta)
==========

# (\beta-1)3^{1+\cdots+7}\Phi(T)

(\beta-1)3^{28}\Phi(T).
\tag{4}
]
The multiplier in (4) is fixed and nonzero. Therefore
[
z_T=P_T(\beta)^{-1}
===================

\bigl((\beta-1)3^{28}\bigr)^{-1}\Phi(T)^{-1}
\tag{5}
]
is a bijective reciprocal-scalar normalization of the Cycle84 product.

It follows that the designated slope family has exactly the Cycle84 spectrum:
[
\begin{aligned}
\text{packet incidences}&=52{,}747{,}567{,}104,\
\text{distinct designated bad slopes}&=52{,}747{,}567{,}092,\
\text{singleton packet fibers}&=52{,}747{,}567{,}080,\
\text{double packet fibers}&=12,\
\text{packet fibers of size }\ge3&=0.
\end{aligned}
\tag{6}
]

PROOF / DISPROOF / ROUTE CUT:

### 1. The RS parity-check realization

Let
[
L_D(X)=\prod_{x\in D}(X-x),\qquad r=n-k=j+\sigma.
]
Define
[
(Hw)_m
======

\sum_{x\in D}\frac{x^m w(x)}{L_D'(x)},
\qquad 0\le m<r.
\tag{7}
]

For every polynomial (p) of degree (<k),
[
\deg(X^mp)\le (r-1)+(k-1)=n-2.
]
The standard Lagrange coefficient identity gives
[
\sum_{x\in D}\frac{x^mp(x)}{L_D'(x)}=0.
]
The weighted Vandermonde matrix (H) has rank (r), so
[
\ker H=\operatorname{RS}[F,D,k].
\tag{8}
]

This is a standard RS code, not merely a GRS row up to an unverified scaling.

### 2. The fixed-jet syndrome line

For (J\in\mathcal J), define an error word supported exactly on (J):
[
e_J(x)=
\begin{cases}
\dfrac{L_D'(x)}
{(\beta-x)P_J'(x)},&x\in J,[1.2ex]
0,&x\notin J.
\end{cases}
\tag{9}
]

Divide
[
X^m=Q_{m,J}(X)P_J(X)+R_{m,J}(X),
\qquad \deg R_{m,J}<j.
\tag{10}
]
For (m<j+\sigma), the quotient (Q_{m,J}) depends only on the common leading (\sigma)-jet in (FJ). Hence it is independent of (J); denote it by (Q_m).

Lagrange interpolation on (J) gives
[
\begin{aligned}
(He_J)*m
&=
\sum*{x\in J}\frac{x^m}{(\beta-x)P_J'(x)}\
&=
\frac{R_{m,J}(\beta)}{P_J(\beta)}\
&=
\frac{\beta^m}{P_J(\beta)}-Q_m(\beta).
\end{aligned}
\tag{11}
]
Thus
[
He_J=A+z_JB,
\qquad
A_m=-Q_m(\beta),\quad B_m=\beta^m,
\quad z_J=P_J(\beta)^{-1}.
\tag{12}
]

Define
[
g(x)=\frac{L_D(\beta)}{\beta-x}.
\tag{13}
]
Full-domain Lagrange interpolation gives
[
Hg=(1,\beta,\ldots,\beta^{r-1})=B.
\tag{14}
]

Fix (J_0\in\mathcal J) and set
[
f=e_{J_0}-z_{J_0}g.
\tag{15}
]
Then (Hf=A). Therefore
[
H(f+z_Jg-e_J)=0.
]
Consequently,
[
c_J:=f+z_Jg-e_J\in C.
\tag{16}
]

On (S_J=D\setminus J), the error (e_J) vanishes, so
[
(f+z_Jg)|*{S_J}=c_J|*{S_J}.
\tag{17}
]
This proves the required agreement on (k+\sigma=n-j) coordinates.

### 3. Noncontainment

Suppose (g) were explained by a codeword (c_g\in C) on (S_J). Then
[
v=g-c_g
]
would be supported on (J) and would satisfy
[
Hv=Hg=B.
]

The syndrome of any word supported on (J) lies in the span of the weighted Vandermonde columns
[
\left{\frac{(1,x,\ldots,x^{r-1})}{L_D'(x)}:x\in J\right}.
]
But
[
B=(1,\beta,\ldots,\beta^{r-1})
]
is not in this span. Indeed, (J\cup{\beta}) consists of (j+1\le r) distinct points, and the corresponding Vandermonde columns are linearly independent.

Therefore (g) is not code-explainable on (S_J). In particular, no pair (c_f,c_g\in C) simultaneously explains (f,g) there. Each (z_J) is support-wise MCA-bad.

This also proves that these are not tangent incidences: failure already occurs in the direction word (g).

### 4. Exact (t=1) residue-line identification

Put
[
E(X)=X-\beta,\qquad B_0=L_D(\beta).
]
Then
[
g=-\frac{B_0}{E}
]
on (D). Let (w=Ef). If (p_J) is the degree-(<k) polynomial representing (c_J), define
[
Q_{z_J}=Ep_J+z_JB_0.
]
Then
[
\deg Q_{z_J}<k+1,\qquad
Q_{z_J}\equiv z_JB_0\pmod E,
]
and on (S_J),
[
Q_{z_J}=w.
]
The Vandermonde argument above is exactly the residue-line noncontainment condition.

Thus the construction is an official support-wise (t=1) residue-line/MCA object.

### 5. Native finite RS consequence

Let
[
F=\mathbb F_{17^{16}},\qquad D=\langle\eta\rangle,\qquad |D|=256.
]
Cycle84 has (\beta\notin D), since (\beta^{256}\ne1). Applying the theorem gives
[
\boxed{
\epsilon_{\rm mca}
\left(
\operatorname{RS}[F,D,137],
\frac{113}{256}
\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{16}}.
}
\tag{18}
]
Numerically,
[
\frac{52{,}747{,}567{,}092}{17^{16}}
\approx2^{-29.781}.
]

Equivalently,
[
\boxed{
LD_{\rm sw}
\left(
\operatorname{RS}[F,D,137],143
\right)
\ge52{,}747{,}567{,}092.
}
\tag{19}
]

The same line also satisfies
[
#\left{
z:\operatorname{dist}(f+zg,C)\le\frac{113}{256}
\right}
\ge52{,}747{,}567{,}092.
\tag{20}
]

### 6. What follows for list decoding

The tuple-to-support map is injective: the seven moving blocks lie in distinct cosets (\eta^t\langle\eta^8\rangle), and the packet’s 48 block sets are distinct. Each (e_T) is nonzero at every point of (J_T). Therefore distinct tuples in the same Cycle84 product fiber yield distinct codewords at the same line point.

Hence the 12 double fibers give 12 received words on the line with at least two explicitly designated codewords at exact distance (113).

However:

* “no packet fiber of size at least (3)” is only a statement about the designated Cycle84 codewords;
* it is not an upper bound on the full Reed–Solomon list;
* no large worst-case list at one received word follows from the large slope occupancy.

Thus the nontrivial consequence is MCA/line occupancy, not a full list-decoding theorem.

### 7. Fixed-root smooth-domain padding

There is also a clean prize-rate finite corollary.

Let
[
K=F(\zeta),\qquad \zeta^2=\eta.
]
Since (\eta) has order (256) and is nonsquare in (F), this is a quadratic extension:
[
K\cong\mathbb F_{17^{32}},
]
and (\zeta) has order (512). Put
[
H=\langle\zeta\rangle,\qquad |H|=512,
\qquad D=\langle\zeta^2\rangle.
]

The original packet never uses the 31 points of
[
\langle\eta^8\rangle\setminus{1},
]
and it uses no point of (H\setminus D). Thus there are
[
31+256=287
]
universally unused points available as fixed co-support roots.

If (R) is any fixed set of such points and
[
J_T^+=J_T\cup R,
\qquad
P_T^+=P_RP_T,
]
then
[
\deg(P_T^+-P_{T'}^+)\le\deg P_R+107
=(113+|R|)-6,
]
and
[
P_T^+(\beta)=P_R(\beta)(\beta-1)3^{28}\Phi(T).
]
Thus the fixed jet and the entire Cycle84 evaluation spectrum are preserved.

Two exact rows result:

[
\boxed{
\begin{aligned}
C_{1/2}&=\operatorname{RS}[K,H,256],\
(n,k,\sigma,j)&=(512,256,6,250),\
\delta&=\frac{250}{512}=\frac{125}{256},
\end{aligned}}
\tag{21}
]
using 137 fixed roots, and
[
\boxed{
\begin{aligned}
C_{1/4}&=\operatorname{RS}[K,H,128],\
(n,k,\sigma,j)&=(512,128,6,378),\
\delta&=\frac{378}{512}=\frac{189}{256},
\end{aligned}}
\tag{22}
]
using 265 fixed roots.

For both,
[
\epsilon_{\rm mca}(C_\rho,\delta)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}
\approx2^{-95.180}

> 2^{-128}.
> \tag{23}
> ]
> Here
> [
> \left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
> ]

These are smooth power-of-two subgroup rows at prize rates. Nevertheless, under the packet’s Cycle92 audit they remain **generated-extension-field research theorems**, not official-prize counterpackets, until the official field/source contract accepts such extension fields.

They are also not meaningful frontier advances in the raw no-slack ledger: at this field size the tangent floor already exceeds the integer target (6). The Cycle84 incidences are genuinely non-tangent, but the (2^{-128}) comparison itself is weak here.

### 8. Cycle88/89 route cut

The Cycle88/89 candidate says, conditionally,
[
(n,k,\sigma,j,t)=(464,232,6,226,1)
]
over (\mathbb F_{17^{48}}), with numerator
[
1{,}391{,}152{,}917{,}379{,}006{,}070{,}784
]
against
[
\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor
================================================

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

Cycle89 correctly identifies this, conditional on the Cycle87 census, as a finite support-wise RS/GRS MCA row. But Cycle90 cuts prize promotion:
[
464=2^4\cdot29
]
is not a power-of-two multiplicative subgroup order, and the factor (29) cannot be removed by literal padding, shortening, subgroup inclusion, or quotient pullback.

The supplied compact packet contains audit summaries rather than the raw Cycle87 replay bundle, so the ruthless referee status of this row remains conditional. It is not needed for the native fixed-jet theorem proved above.

FIELD AND PARAMETER LEDGER:

| Row                     | Parameters                                                              | Field ledger                                                                                                                      | Numerator and target                                              | Status                                                                                     |
| ----------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Native Cycle84 transfer | ((n,k,\sigma,j,t)=(256,137,6,113,1)), agreement (143), (\delta=113/256) | (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}). The domain already generates the full field. (q_{\rm chal}) is not invoked.      | (N=52{,}747{,}567{,}092); (\lfloor q_{\rm line}/2^{128}\rfloor=0) | Proved finite RS-MCA/line theorem; non-prize rate and denominator comparison is inactive   |
| Padded rate (1/2)       | ((512,256,6,250,1)), (\delta=125/256)                                   | (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}), since an order-512 domain generates (\mathbb F_{17^{32}}). (q_{\rm chal}) unset. | (N); target (6)                                                   | Proved smooth prize-rate extension-field finite theorem; official admissibility unresolved |
| Padded rate (1/4)       | ((512,128,6,378,1)), (\delta=189/256)                                   | Same (17^{32}) ledger                                                                                                             | (N); target (6)                                                   | Same                                                                                       |
| Cycle88/89 candidate    | ((464,232,6,226,1))                                                     | Audits claim (q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_{\rm chal}=17^{48})                                                         | (1.391\times10^{21}); target (3.386\times10^{20})                 | Conditional finite arbitrary-domain row; not smooth prize family                           |

The denominator in the mathematical MCA error is (q_{\rm line}), not (q_{\rm gen}) from a smaller base field and not (q_{\rm chal}). No (q_{\rm chal}) credit has been used in the proved rows.

SELF-AUDIT:

1. **Exact implication proved.**
   Cycle84’s locator family and finite spectrum imply a standard ([256,137]) RS support-wise MCA/line lower bound with at least (52{,}747{,}567{,}092) distinct bad slopes. Fixed-root padding also proves smooth ([512,256]) and ([512,128]) extension-field rows.

   **Not proved:** an official Proximity Prize counterpacket, a full list-size theorem, an upper bound on the total bad-slope set, or the Cycle88/89 two-copy census from first principles.

2. **Claim level.**
   The native result is a paper-facing finite RS-MCA/support-wise line-decoding theorem. The padded rows are paper-facing smooth-domain, prize-rate extension-field theorems. Under the supplied audits, none is yet an official-prize result.

3. **First unsupported prize implication.**
   For the padded rows:
   [
   \text{generated extension-field smooth RS row}
   \Longrightarrow
   \text{official admissible prize-field/source row}.
   ]
   This is the first unsupported line.

   If extension fields are rejected, the first missing theorem is a loss-preserving fixed-jet occupancy compiler into an accepted prime/deployed prize field.

   For the Cycle88/89 route, the earlier failure is:
   [
   \text{arbitrary }464\text{-point RS domain}
   \Longrightarrow
   \text{power-of-two smooth multiplicative prize domain}.
   ]

4. **(q)-ledger and (2^{-128}).**
   The proved denominator is always (q_{\rm line}=q_{\rm code}).
   (q_{\rm gen}) is not used as a substitute denominator.
   (q_{\rm chal}) is not silently identified with (q_{\rm line}).
   At (17^{16}), the integer threshold is zero, so the (2^{-128}) comparison has no frontier content.
   At (17^{32}), the target is six; it is exceeded, but the source admissibility and tangent-dominated regime prevent prize promotion.

5. **Possible numerator losses.**

   * **Same-slope collisions:** exactly accounted for by (5); the packet histogram remains 12 doubles and no packet triples.
   * **Affine/color normalization:** multiplication by a fixed nonzero scalar and inversion are bijections. No loss.
   * **Contained incidences:** ruled out by the (j+1)-column Vandermonde argument.
   * **Tangent loss:** these incidences are non-tangent because (g) itself is not explainable on the witness support.
   * **Endpoint loss:** all designated (z_T) are finite and nonzero in the raw affine MCA definition. A protocol-specific endpoint deletion still needs a source contract.
   * **Quotient/periodic structure:** it does not reduce the raw support-wise MCA numerator. An aperiodic or quotient-separated corrected formulation could discard or charge part of the family; no retained-numerator theorem has been proved for that formulation.
   * **Source/charge normalization:** absent from the raw mathematical definition and therefore not deducted here. It remains a live official-protocol wall.

6. **Minimal dependency ledger.**

   Already proved or supplied:

   * Cycle84 finite certificate and exact spectrum.
   * Cycle84 support/slot definitions.
   * The common six-jet identity (3).
   * The evaluation identity (4).
   * The fixed-jet locator-to-MCA theorem proved above.
   * The support-wise MCA definition and (LD_{\rm sw}) bridge.
   * The fixed-root padding corollary.

   Not supplied or not proved:

   * an authority-pinned extension-field prize-admissibility ruling;
   * a (q_{\rm chal})/verifier source contract;
   * a retained-slope theorem after official quotient, periodic, endpoint, affine, and charge processing;
   * an accepted-field smooth compiler if extension fields are rejected;
   * an independent Cycle87 full replay within this compact packet;
   * a full RS list-decoding bound.

NEXT EXACT STEP:

### Immediate checker

The light checker verifies the algebraic transfer premises without recomputing Cycle84:

[Fixed-jet transfer checker](sandbox:/mnt/data/cycle115_fixed_jet_transfer_checker.py)

[Checker output](sandbox:/mnt/data/cycle115_fixed_jet_transfer_checker_output.json)

### Next 9-Pro target

```text
V-CYCLE116-EXTENSION-FIELD-PRIZE-ADMISSIBILITY-AND-RETAINED-SLOPE-CONTRACT
```

It must consume the explicit (t=1) rows (21)–(22) and return exactly one of:

```text
OFFICIAL_ADMISSIBLE_RAW_MCA
SOURCE_REJECTED_AT_EXACT_CLAUSE
COLOR_COMPRESSED_OR_CHARGED_WITH_EXACT_RETAINED_NUMERATOR
QCHAL_QLINE_MISMATCH_WITH_EXACT_DENOMINATOR
```

The contract must pin:

* accepted field class;
* official RS domain class;
* support-wise MCA definition;
* (q_{\rm gen},q_{\rm code},q_{\rm line},q_{\rm chal});
* endpoint and projective normalization;
* quotient/periodic classification;
* exhaustive charge registry;
* final retained-slope map and integer numerator.

If the extension rows are rejected, the next theorem is:

```text
L-CYCLE117-ACCEPTED-FIELD-SMOOTH-FIXED-JET-OCCUPANCY-COMPILER
```

It must construct, in an accepted prize field, a power-of-two subgroup (H), a prize-rate (k), a family of (j=n-k-\sigma) co-supports with a common (\sigma)-jet, and an evaluation map retaining more than
[
\left\lfloor q_{\rm line}/2^{128}\right\rfloor
]
distinct slopes after every official source/charge/normalization loss.

### Shortest PRZ-facing response

> Cycle84 has an exact fixed-jet transfer: its locators satisfy (P_T=X^{113}-X^{112}+O(X^{107})) and (P_T(\beta)=\kappa\Phi(T)), yielding one (t=1) line for (\operatorname{RS}[\mathbb F_{17^{16}},\langle\eta\rangle,137]) with at least (52{,}747{,}567{,}092) support-wise bad slopes at (\delta=113/256). Fixed-root padding gives smooth prize-rate ([512,256]) and ([512,128]) rows over (\mathbb F_{17^{32}}). The remaining prize-facing wall is not the Cycle84 computation but the authority-pinned extension-field/source/charge contract—or, if extension fields are excluded, an accepted-field smooth fixed-jet embedding.
