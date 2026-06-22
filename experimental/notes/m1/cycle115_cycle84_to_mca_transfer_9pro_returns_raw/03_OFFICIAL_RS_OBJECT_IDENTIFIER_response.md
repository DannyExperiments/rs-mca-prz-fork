LABEL: **PROOF**

EXECUTIVE VERDICT:

Cycle84 admits an exact transfer to an ordinary Reed–Solomon MCA and support-wise line-decoding statement.

The key theorem is a **fixed-jet reciprocal-locator transfer**. Applied natively, it gives

[
C_0=\operatorname{RS}!\left[\mathbb F_{17^{16}},\langle\eta\rangle,137\right],
\qquad n=256,\quad |S|=143,\quad \delta=\frac{113}{256},
]

with at least

[
N=52{,}747{,}567{,}092
]

distinct support-wise MCA-bad slopes on one explicit affine line.

More significantly, a fixed-support padding construction gives an exact smooth, official-rate row under the family stated in `proximity_blueprint_v3.tex`:

[
C_1=\operatorname{RS}!\left[\mathbb F_{17^{32}},H_{512},256\right],
\qquad |H_{512}|=512,\quad \rho=\frac12,
]

at

[
|S|=257,\qquad \delta=\frac{255}{512},
]

again with at least (N) distinct bad slopes. Here

[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6,
]

so (N>6). Thus this is a genuine smooth power-of-two, rate-(1/2), same-field RS-MCA lower row under the packet’s stated definition.

This is **not** a solution of the Proximity Prize frontier. The row is only one symbol below capacity, hence below the corrected reserve and in the already-expected failure region. It also does not produce a significant list-decoding lower bound: the explicit double fibers yield list size at least (2), not a large list.

The Cycle88–89 ([464,232]) row over (\mathbb F_{17^{48}}) remains only a conditional arbitrary-domain RS/GRS row. Its first prize-family failure is (464\neq 2^m).

Confidence: **high** for the algebraic transfer and all finite field/parameter ledgers; **moderate** for calling extension fields “official” outside the packet’s own survey restatement, because Cycle92 records that external source-scope question as unresolved.

EXACT THEOREM OR OBSTRUCTION:

### Fixed-jet reciprocal-locator transfer theorem

Let (F) be a finite field, (D\subset F), (|D|=n), and let

[
C=\operatorname{RS}[F,D,k].
]

Let (\mathcal S) be a family of supports (S\subset D), all of size

[
|S|=a=k+\sigma,\qquad \sigma\ge1.
]

For (S\in\mathcal S), define

[
L_S(X)=\prod_{x\in S}(X-x),\qquad
P_S(X)=\prod_{x\in D\setminus S}(X-x),
]

so that

[
L_S(X)P_S(X)=M_D(X):=\prod_{x\in D}(X-x).
]

Assume that all (L_S) have the same coefficients in degrees

[
a,a-1,\ldots,k+1.
]

Let (W(X)) be this common degree-(\ge k+1) truncation. Then

[
Q_S(X):=W(X)-L_S(X)
]

has degree at most (k).

Choose (\beta\notin D), and define the fixed line

[
f(x)=\frac{W(x)}{x-\beta},
\qquad
g(x)=-\frac1{x-\beta},
\qquad x\in D.
]

For each (S), put

[
z_S=Q_S(\beta)
=W(\beta)-\frac{M_D(\beta)}{P_S(\beta)}.
]

Then (z_S) is support-wise MCA-bad on (S). Indeed,

[
c_S(X)=\frac{Q_S(X)-z_S}{X-\beta}
]

has degree (<k), and on (S),

[
c_S(x)=\frac{W(x)-z_S}{x-\beta}=f(x)+z_Sg(x).
]

Noncontainment is automatic: if a polynomial (G) of degree (<k) agreed with (g) on (S), then

[
(X-\beta)G(X)+1
]

would have degree at most (k), at least (k+1) roots, and value (1) at (X=\beta), a contradiction.

Finally, because (M_D(\beta)\ne0), the map

[
u\longmapsto W(\beta)-\frac{M_D(\beta)}u
]

is injective on (F^\times). Hence the slope fibers are exactly the fibers of (P_S(\beta)). Therefore

[
\operatorname{LD}_{\rm sw}(C,a)
\ge
#{P_S(\beta):S\in\mathcal S},
]

and

[
\epsilon_{\rm mca}!\left(C,1-\frac an\right)
\ge
\frac{#{P_S(\beta):S\in\mathcal S}}{|F|}.
]

This is the exact transfer theorem requested by PRZ.

PROOF / DISPROOF / ROUTE CUT:

### 1. Native Cycle84 row over (\mathbb F_{17^{16}}): PROOF

Set

[
F_0=\mathbb F_{17}[X]/(X^{16}+X^8+3),
\qquad D_0=\langle\eta\rangle,
\qquad |D_0|=256.
]

For a packet tuple (T=((i_t,a_t))_{t=1}^7), Cycle84 defines a co-support

[
E_T={1}\cup\bigcup_{t=1}^7\eta^tA(i_t,a_t)
]

of size (1+7\cdot16=113), and hence

[
S_T=D_0\setminus E_T,\qquad |S_T|=143.
]

Let

[
P_T(X)=\prod_{x\in E_T}(X-x),\qquad
L_T(X)=\frac{X^{256}-1}{P_T(X)}.
]

The paired-root slot construction and the two zero top coefficients of the packet’s degree-eight templates imply that every sixteen-point slot locator has no terms in degrees (15,14,13,12,11). Consequently,

[
P_T(X)
=X^{113}-X^{112}
+0X^{111}+0X^{110}+0X^{109}+0X^{108}
+O(X^{107}).
]

Division into (X^{256}-1) gives

[
L_T(X)
=X^{143}+X^{142}+X^{141}+X^{140}+X^{139}+X^{138}
+O(X^{137}).
]

Thus the common jet is

[
W_0(X)=X^{143}+X^{142}+X^{141}+X^{140}+X^{139}+X^{138}.
]

The transfer theorem therefore applies to

[
C_0=\operatorname{RS}[F_0,D_0,137].
]

The exact line is

[
f_0(x)=\frac{W_0(x)}{x-\beta},
\qquad
g_0(x)=-\frac1{x-\beta}.
]

The bad slope attached to (T) is

[
z_T
=W_0(\beta)-\frac{\beta^{256}-1}{P_T(\beta)}.
]

The Cycle84 slot-factorization identities give the exact bridge

[
P_T(\beta)
=(\beta-1),3^{1+\cdots+7}\Phi(T)
=(\beta-1)3^{28}\Phi(T).
]

Both scalar factors are nonzero. Hence the map from (\Phi(T)) to (z_T) is reciprocal-affine and injective on distinct product values. The complete packet slope spectrum is therefore:

[
\begin{aligned}
\text{distinct packet slopes}&=52{,}747{,}567{,}092,\
\text{double slope fibers}&=12,\
\text{fibers of size }\ge3&=0.
\end{aligned}
]

Thus

[
\operatorname{LD}_{\rm sw}(C_0,143)
\ge52{,}747{,}567{,}092
]

and

[
\epsilon_{\rm mca}!\left(C_0,\frac{113}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{16}}
\approx 2^{-29.781}.
]

The native row is smooth but has rate (137/256), not a prize rate.

A precision point: (m_{\max}=2) alone, together with the packet size (P), gives only

[
\operatorname{Occ}\ge \frac P2
=26{,}373{,}783{,}552.
]

The stronger numerator (52{,}747{,}567{,}092) uses the supplied exact occupancy certificate.

### 2. Smooth rate-(1/2) padding row over (\mathbb F_{17^{32}}): PROOF

Define

[
F_1=F_0[V]/(V^2-\eta).
]

Because (v_2(|F_0^\times|)=8) and (\eta) has order (256), (\eta) is not a square in (F_0). Thus (V^2-\eta) is irreducible and

[
F_1\cong\mathbb F_{17^{32}}.
]

Put

[
\omega=V,\qquad \omega^2=\eta.
]

Then (\omega) has order (512), and

[
H_{512}=\langle\omega\rangle
]

is a smooth multiplicative subgroup containing

[
D_0=\langle\omega^2\rangle.
]

Choose the explicit fixed set

[
A={\omega^{2r+1}:0\le r\le113}
\subset H_{512}\setminus D_0,
\qquad |A|=114.
]

For every Cycle84 support (S_T), define

[
S'_T=S_T\cup A.
]

Then

[
|S'_T|=143+114=257.
]

Take

[
C_1=\operatorname{RS}[F_1,H_{512},256].
]

Let

[
A_0(X)=\prod_{a\in A}(X-a).
]

The support locator is

[
L'_T(X)=A_0(X)L_T(X),
]

which is monic of degree (257=k+1). Thus the fixed-jet theorem applies with the automatic one-coefficient jet

[
W_1(X)=X^{257}.
]

The exact line is

[
f_1(x)=\frac{x^{257}}{x-\beta},
\qquad
g_1(x)=-\frac1{x-\beta},
\qquad x\in H_{512},
]

and the packet slope is

[
z'_T
=\beta^{257}
-\frac{A_0(\beta)(\beta^{256}-1)}{P_T(\beta)}.
]

Since (\beta\notin H_{512}), the numerator multiplying (P_T(\beta)^{-1}) is nonzero. Hence the Cycle84 product fibers transfer without additional collision loss.

Therefore

[
\operatorname{LD}_{\rm sw}(C_1,257)
\ge52{,}747{,}567{,}092
]

and

[
\epsilon_{\rm mca}!\left(C_1,\frac{255}{512}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}
\approx2^{-95.1804}

> 2^{-128}.
> ]

This gives

[
\delta^*_{C_1}(2^{-128})\le\frac{255}{512}.
]

It is an exact ordinary RS row, not merely GRS-isometric.

### 3. List-decoding consequence: only weak

A double product fiber gives two distinct supports with the same line slope. The corresponding codewords are distinct: equality of codewords would imply equality of (Q_T), hence equality of the support locators and supports.

Thus the explicit double witness proves

[
L_{C_0}!\left(\frac{113}{256}\right)\ge2
]

and

[
L_{C_1}!\left(\frac{255}{512}\right)\ge2.
]

Nothing in Cycle84 proves that the full RS list has size at most (2), nor does it produce a superpolynomial or threshold-crossing fixed-word list. Occupancy is an MCA/line numerator; fiber multiplicity is the relevant packet-list quantity.

### 4. Cycle88–89 two-copy row: conditional finite proof, prize route cut

Accepting the Cycle87 certificate chain gives a GRS row diagonally equivalent to RS with

[
(n,k,\sigma,j,t)=(464,232,6,226,1)
]

over

[
F_2=F_0[U]/(U^3-\beta)\cong\mathbb F_{17^{48}}.
]

Its audited slope form is

[
z_{v,T}=\frac1{vP_T(U)}
]

and its conservative bad-slope numerator is

[
B=\frac{NP}{2}
=1{,}391{,}152{,}917{,}379{,}006{,}070{,}784.
]

This exceeds

[
\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor
=338{,}617{,}018{,}271{,}848{,}945{,}628
]

by

[
1{,}052{,}535{,}899{,}107{,}157{,}125{,}156.
]

Cycle89 correctly identifies these as support-wise MCA slopes under the packet-local definition. Nevertheless,

[
464=2^4\cdot29
]

is not a power of two. Cycle90 therefore cuts every literal padding, shortening, subgroup-inclusion, or quotient-pullback port of that domain into a pure (2)-group domain.

The exact (464)-point domain list, GRS multipliers, and coefficient-level (f,g) vectors are also absent from the current compact packet. The row is therefore conditional on the audited Cycle87 certificate package.

FIELD AND PARAMETER LEDGER:

### Native one-copy row

```text
field F =
  F_0 = F_17[X]/(X^16 + X^8 + 3) = F_{17^16}

evaluation domain D =
  <eta>, eta = 6X^9, |<eta>| = 256

smooth multiplicative subgroup/coset? =
  yes; power-of-two multiplicative subgroup

code type RS or GRS =
  ordinary RS

n =
  256

k =
  137

rate rho =
  137/256

agreement/support size =
  143 = k + 6

radius delta =
  1 - 143/256 = 113/256

line family f + z g =
  f(x) = (x^143+x^142+x^141+x^140+x^139+x^138)/(x-beta)
  g(x) = -1/(x-beta)

bad-slope numerator =
  at least 52,747,567,092

q_gen =
  17^16
  (ord_256(17)=16, so eta generates the full field)

q_code =
  17^16

q_line =
  17^16

q_chal =
  not intrinsic to the code row;
  equals 17^16 under a same-field protocol instantiation

floor(q_line / 2^128) =
  0

numerator > target? =
  yes, but the target is arithmetically vacuous at this field size

first unsupported official-definition condition =
  rate 137/256 is not in {1/2,1/4,1/8,1/16}
```

### Smooth padded rate-(1/2) row

```text
field F =
  F_1 = F_0[V]/(V^2-eta) = F_{17^32}

evaluation domain D =
  H_512 = <V>, with V^2=eta and |H_512|=512

smooth multiplicative subgroup/coset? =
  yes; power-of-two multiplicative subgroup

code type RS or GRS =
  ordinary RS

n =
  512

k =
  256

rate rho =
  1/2

agreement/support size =
  257 = k + 1

radius delta =
  1 - 257/512 = 255/512

line family f + z g =
  f(x)=x^257/(x-beta)
  g(x)=-1/(x-beta)

bad-slope numerator =
  at least 52,747,567,092

q_gen =
  17^32

q_code =
  17^32

q_line =
  17^32

q_chal =
  17^32 under the explicit same-field experiment;
  no separate extension-challenge credit is used

floor(q_line / 2^128) =
  6

numerator > target? =
  yes; 52,747,567,092 > 6

first unsupported official-definition condition =
  none under the family stated in proximity_blueprint_v3.tex;
  external authority-pinned admissibility of extension fields remains
  the Cycle92 source-scope caveat
```

### Two-copy Cycle87–89 row

```text
field F =
  F_0[U]/(U^3-beta) = F_{17^48}

evaluation domain D =
  the Cycle87 464-point two-block domain;
  its element-level list/digest is absent from this compact packet

smooth multiplicative subgroup/coset? =
  no; n=464 is not a power of two

code type RS or GRS =
  certified as GRS; diagonally isometric to ordinary RS for
  support-wise MCA purposes

n =
  464

k =
  232

rate rho =
  1/2

agreement/support size =
  238 = k + 6

radius delta =
  1 - 238/464 = 226/464 = 113/232

line family f + z g =
  one t=1 affine residue/syndrome line;
  audited slopes z_{v,T}=1/(v P_T(U));
  explicit coefficient vectors f,g are not in this packet

bad-slope numerator =
  1,391,152,917,379,006,070,784, conditional on Cycle87

q_gen =
  17^48 as asserted by the Cycle87 generated-domain certificate

q_code =
  17^48

q_line =
  17^48

q_chal =
  17^48 only under a same-field protocol instantiation;
  it is not an additional denominator

floor(q_line / 2^128) =
  338,617,018,271,848,945,628

numerator > target? =
  yes, conditionally

first unsupported official-definition condition =
  evaluation domain is not a smooth power-of-two subgroup/coset
```

SELF-AUDIT:

1. **Exact implication proved and not proved.**
   Proved: Cycle84’s product occupancy transfers exactly to bad slopes on an explicit ordinary RS line, first on ([256,137]) over (\mathbb F_{17^{16}}), and after fixed padding on the smooth ([512,256]) row over (\mathbb F_{17^{32}}). Consequently the corresponding support-wise line-decoding numerators and MCA lower bounds follow.
   Not proved: an above-reserve prize-frontier counterexample, an exact MCA threshold, a substantial fixed-word list lower bound, an interleaved-list statement, or an unconditional reconstruction of the Cycle87 (464)-point certificate.

2. **Claim level.**
   The native row is a paper-facing finite smooth RS-MCA/line-decoding proof but has a non-prize rate. The padded ([512,256]) row lies in the packet’s stated smooth, official-rate family and clears the exact (2^{-128}) same-field numerator target. It is nevertheless below the corrected reserve and is not a solution of the Proximity Prize frontier. The (464)-point row is finite arbitrary-domain evidence only.

3. **First possible failure line.**
   For the algebraic transfer itself, the first possible failure would have been the fixed-jet identity or the reciprocal-locator identity. Both are proved above. For external prize promotion, the first remaining line is the authority-pinned source ruling on extension-field admissibility. For Cycle87, the first failure is earlier: its domain is not power-of-two smooth.

4. **Field ledger.**
   The only MCA denominator used is (q_{\rm line}). In the new row,

   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}.
   ]

   Setting (q_{\rm chal}=17^{32}) is a same-field experiment, not extra credit. Neither (q_{\rm gen}) nor (q_{\rm code}) is used a second time as a denominator. The exact target is (6), not (0), (N), or a (17^{48}) threshold.

5. **Possible numerator losses.**
   None of the named mechanisms reduces the proved native or padded numerator:

   * quotient or periodic structure is not excluded by `def:mca`;
   * contained incidences are ruled out by the polynomial root-count argument for (g);
   * same-slope collisions are exactly the Cycle84 fibers, including the twelve doubles;
   * the affine normalization is injective because its reciprocal coefficient is nonzero;
   * all slopes are finite field elements, so no projective endpoint is counted;
   * tangent or source-charge terminology does not subtract valid bad slopes under the canonical support-wise definition.

   For the conditional (464)-row, projective/same-slope loss is already paid by the factor (1/2); the remaining issue is certificate availability and domain admissibility.

6. **What would constitute a frontier solve.**
   The exact next theorem is not another Cycle84 census. It is:

   [
   \boxed{\text{L-CYCLE115-SMOOTH-PAIR-COMPOSITION-ABOVE-RESERVE}}
   ]

   Over (K=\mathbb F_{17^{48}}), (D=\langle\eta\rangle) of order (256), and

   [
   C=\operatorname{RS}[K,D,128],
   ]

   construct one fixed line and supports of size (143), indexed by a two-copy Cycle84 packet, whose final slope multiplicity is at most (8). This would give

   [
   \left\lfloor\frac{N^2}{8}\right\rfloor
   =347{,}788{,}229{,}265{,}630{,}167{,}058

   >

   # 338{,}617{,}018{,}271{,}848{,}945{,}628

   \left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor.
   ]

   The checker must emit the actual support map, a single RS-compatible (f+zg), coefficient-level noncontainment, final slope fibers, and the typed (q_{\rm gen}/q_{\rm code}/q_{\rm line}/q_{\rm chal}) ledger. Naive tensoring or an unproved additive color formula is insufficient.

NEXT EXACT STEP:

Bank the fixed-jet reciprocal-locator theorem and the explicit ([512,256]) smooth padding row.

For external prize use, obtain the exact authority-pinned source contract deciding whether (\mathbb F_{17^{32}}) and (\mathbb F_{17^{48}}) are admitted prize fields. For genuine frontier progress, attack `L-CYCLE115-SMOOTH-PAIR-COMPOSITION-ABOVE-RESERVE`; it is the first missing mathematical line after the present proof.

OFFICIAL_ROW_IDENTIFIED
