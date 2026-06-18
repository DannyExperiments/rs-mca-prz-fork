The ledgers remain separate throughout:

[
q_{\rm gen}=p,\qquad B=\mathbf F_p,\qquad
F=\mathbf F_{p^2}=B(\alpha),\qquad
q_{\rm line}=p^2,\qquad q_{\rm chal}\text{ unused}.
]

Also

[
D=\mathbf F_p,\quad n=p,\quad t=\sigma=2,\quad j=4,\quad
a=p-4,\quad k=p-6,\quad \delta=\frac4p.
]

**Verdict:** both named walls close. The Subcase A failure is a false negative caused by an affine Cramer chart and an overstrong good-reduction criterion. The same line (z_1=z_0) works. Subcase B admits the requested explicit finite bad-prime set and the global (1/24)-density argument. The same density conclusion also holds for Subcase A.

## AUDIT

### The two Codex repairs

Both repairs are mathematically correct.

1. In
   [
   A_K=K[X]/(E),\qquad K=\mathbf Q(i),\qquad E=X^2+iX+1,
   ]
   an element is a pair of Gaussian coefficients (c_0+c_1X). Hence
   [
   \ell=i\quad\longleftrightarrow\quad (i,0),
   \qquad
   \ell=-2X\quad\longleftrightarrow\quad(0,-2).
   ]
   Treating (i) as a bare scalar where a residue-pair was required was type-wrong.

2. After writing
   [
   z=z_0+iz_1,\qquad z_0,z_1,\tau_1,\dots,\tau_4\in\mathbf Q,
   ]
   the real and imaginary components of the two residue coefficients are four rational scalar equations. Embedding each rational scalar as (q+0i) before a Gaussian determinant operation is mathematically harmless.

The second repair is correct only under this fixed-field interpretation. The variables (\tau_i,z_0,z_1) are (\mathbf Q)-coordinates of a Weil-restricted model; they are not arbitrary (K)-variables.

### What remained wrong after those repairs

The patched Cycle 41 checker is not a valid necessary-and-sufficient good-reduction test.

It still:

* uses the unreduced determinant (\Delta_L) as a universal Cramer denominator;
* forms (\Delta_L^6\operatorname{disc}(L)) without first passing to a primitive projective binary quartic;
* demands squarefreeness of the discriminant polynomial, thereby excluding legitimate tame ramification of index (e>2);
* demands disjointness between a chart-pole divisor and the discriminant, even when the projective cover extends smoothly through that chart boundary;
* does not check the local model at (r=1) or at (r=\infty).

Thus:

* the two local type repairs are correct;
* the Subcase B positive result survives independent verification;
* the Subcase A negative result does not.

Cycle 41’s gates (G1,G2,G3) are sufficient for a simple-branch affine presentation. They are not necessary good-reduction conditions.

## PROOF

### 1. Independent source derivation over (K=\mathbf Q(i))

In (A_K),

[
X^2=-1-iX,\qquad
X^3=i-2X,\qquad
X^4=2+3iX.
]

For

[
L_\tau=X^4-\tau_1X^3+\tau_2X^2-\tau_3X+\tau_4,
]

one obtains

[
\lambda=[L_\tau]_E
=(2-i\tau_1-\tau_2+\tau_4)
+(2\tau_1-i\tau_2-\tau_3+3i)X.
]

Using the source quotient formula and

[
W_{n-1},W_{n-2},W_{n-3},W_{n-4}
=1,i,1+i,1,
]

gives

[
[Q_S]_E
=(1-i\tau_1+i\tau_2-\tau_3)+(\tau_2+i)X.
]

The source graph equation is

[
(u-zb)\lambda-\ell[Q_S]_E=0,
\qquad
u=1+X,\quad b=X,\quad z=z_0+iz_1.
]

Splitting the two residue coefficients into real and imaginary parts yields a rational system

[
M_s(z_0,z_1)\tau=c_s(z_0,z_1).
]

For Subcase A, (\ell=i),

[
M_A=
\begin{pmatrix}
2z_0-3&z_1&1-z_0&1\
2z_1-1&1-z_0&1-z_1&0\
2-3z_1&2z_0-2&z_1-1&1-z_0\
3z_0-3&2z_1-2&1-z_0&-z_1
\end{pmatrix},
]

[
c_A=
\begin{pmatrix}
3z_1-2\
4-3z_0\
5z_0-6\
5z_1-3
\end{pmatrix}.
]

For Subcase B, (\ell=-2X),

[
M_B=
\begin{pmatrix}
2z_0-2&z_1-3&1-z_0&1\
2z_1-1&1-z_0&-z_1&0\
2-3z_1&2z_0-2&z_1-3&1-z_0\
3z_0-5&2z_1-1&1-z_0&-z_1
\end{pmatrix},
]

[
c_B=
\begin{pmatrix}
3z_1-2\
5-3z_0\
5z_0-9\
5z_1-3
\end{pmatrix}.
]

The two surface determinants are therefore

[
\begin{aligned}
\Delta_A={}&-z_0^4+3z_0^3-2z_0^2z_1^2+2z_0^2
+3z_0z_1^2+3z_0z_1-11z_0\
&-z_1^4+4z_1^2-9z_1+9,
\end{aligned}
]

and

[
\begin{aligned}
\Delta_B={}&-z_0^4+6z_0^3-2z_0^2z_1^2-4z_0^2z_1-19z_0^2\
&+6z_0z_1^2+4z_0z_1+30z_0-z_1^4-4z_1^3
+5z_1^2+2z_1-19.
\end{aligned}
]

These equations have rational coefficients. The nominal (K=\mathbf Q(i)) model has descended to (\mathbf Q). Reduction modulo an inert (p\equiv3\pmod4) gives the required (B=\mathbf F_p) surface, and adjoining (i\mapsto\alpha) gives (F=\mathbf F_{p^2}). Directly treating the residue field of (\mathbf Z[i]/(p)) as the base field would incorrectly merge (B) and (F).

### 2. Subcase A on (z_1=z_0=r)

Put

[
h(r)=4r^2+2r-9.
]

Then

[
\Delta_{A,L}=-(r-1)^2h(r),
]

and cancellation of the Cramer factors gives

[
\begin{aligned}
\tau_1&=\frac{12(r-1)}h,\
\tau_2&=\frac{12r^2-2r-13}{h},\
\tau_3&=\frac{28r^2-60r+35}{(r-1)h},\
\tau_4&=\frac{4r^2-18r+17}{h}.
\end{aligned}
]

The correct primitive projective quartic in root coordinates ((U:V)) is

[
\begin{aligned}
F_A={}&(r-1)h,U^4-12(r-1)^2U^3V\
&+(r-1)(12r^2-2r-13)U^2V^2\
&-(28r^2-60r+35)UV^3\
&+(r-1)(4r^2-18r+17)V^4.
\end{aligned}
]

Its intrinsic discriminant is

[
\operatorname{Disc}_{U,V}(F_A)=(r-1)^2P_A(r),
]

where

[
\begin{aligned}
P_A(r)={}&1638400r^{16}-4587520r^{15}-34881536r^{14}
+73072640r^{13}\
&+358903808r^{12}-641441792r^{11}-2127262720r^{10}
+2484816896r^9\
&+17489308160r^8-39769366016r^7-20116857792r^6
+194165722432r^5\
&-347849758128r^4+331010951712r^3-184759775360r^2\
&+57468880452r-7749383319.
\end{aligned}
]

By contrast, the monic affine quartic has

[
\operatorname{Disc}(L_A)
=\frac{P_A(r)}{(r-1)^4h(r)^6},
]

so Cycle 41’s expression was

[
\Delta_{A,L}^{,6}\operatorname{Disc}(L_A)
=(r-1)^8P_A(r).
]

The exponent (8) decomposes as:

* intrinsic valuation (2), coming from genuine tame (e=3) ramification;
* artificial valuation (6), coming from the unreduced Cramer determinant.

### 3. The exact A-side local geometry

The determinant surface has a singular point at ((z_0,z_1)=(1,1)). Writing

[
z_0=1+u,\qquad z_1=1+v,
]

gives

[
\Delta_A
=3u^2+uv-v^2+\text{terms of degree at least }3.
]

Thus it is an ordinary node away from characteristic (13). The tested line (v=u) passes through the node, explaining the factor ((r-1)^2) in (\Delta_{A,L}).

This does not make the quartic cover singular. At the potentially problematic root-coordinate point, use

[
t=r-1,\qquad U=1,\qquad V=y.
]

Then

[
F_A(t,1,y)=-3t-3y^3+\text{higher-order terms},
]

so

[
\frac{\partial F_A}{\partial t}(0,0)=-3\neq0.
]

Consequently the total curve is smooth there and

[
t=-y^3+\cdots .
]

This is one tame ramification point of index (e=3). The discriminant valuation (2=e-1) is exactly correct.

The remaining (16) branch points are the roots of (P_A). When (P_A) is squarefree, they are simple (e=2) branches. The roots of (h) are merely changes of affine root chart; the projective fibers are unramified there. At (r=\infty), the fiber is

[
4(U^4+3U^2V^2+V^4),
]

which is separable outside characteristics (2,5).

Thus the A branch profile is

[
(e=3);+;16\text{ simple }(e=2)\text{ branches}.
]

There is no branch collision or non-étale good-reduction obstruction.

### 4. Subcase B on (z_1=z_0=r)

Put

[
H=4r^4-4r^3+10r^2-32r+19
]

and

[
\begin{aligned}
N_1&=-8r^3+52r^2-56r+4,\
N_2&=12r^4-4r^3+38r^2-120r+99,\
N_3&=-32r^3+120r^2-152r+62,\
N_4&=4r^4+20r^3+62r^2-244r+205.
\end{aligned}
]

Then

[
\Delta_{B,L}=-H,\qquad
\tau_i=N_i/H,
]

and the primitive projective quartic is

[
F_B=HU^4-N_1U^3V+N_2U^2V^2-N_3UV^3+N_4V^4.
]

Its discriminant is

[
\operatorname{Disc}(F_B)=16P_B(r),
]

where the coefficient vector of (P_B), descending from degree (24), is

```text
[102400, -491520, 1859584, -3764224, 51914752,
 -192626688, 477325312, -2008282112, 7446446592,
 -20807045120, 59079347712, -185639798528,
 512758278912, -1116174999552, 2298634344064,
 -5753999742784, 14592594673376, -28990435945600,
 41864795175328, -43894177136944, 33781948075336,
 -19154923131744, 7820247111000, -2096953679988,
 276965239259]
```

Here Cycle 41’s denominator clearing happens to be correct:

[
\Delta_{B,L}^{,6}\operatorname{Disc}(L_B)=16P_B.
]

When (P_B) is squarefree, the line cover has (24) simple (e=2) branch points. The roots of (H) are unramified projective fibers; at infinity the fiber is again (4(U^4+3U^2V^2+V^4)).

## ROUTE_CUT

The A-side alternatives are resolved as follows.

* **True branch-collision/non-étale obstruction:** no. There is one smooth tame (e=3) branch.
* **Artifact of the line (z_1=z_0):** partially yes. The line passes through the node ((1,1)) of the affine determinant surface, producing the doubled Cramer factor.
* **Bug in the reconstructed source equation:** no. The source graph equation and the independently derived matrices agree.
* **Bug in the good-reduction checker:** yes. It treats a simple-branch affine criterion as necessary and does not projectivize or cancel Cramer factors.
* **Genuine Subcase A route cut:** no.

A different line is unnecessary. The line (z_1=z_0) itself gives the required certificate after projective normalization.

This also cuts the naive full-reserve continuation “replace the quartic by a generic degree-(j) polynomial and repeat Chebotarev.” At fixed rate,

[
j=n-k-t=(1-\rho)n-t=\Theta(n)
]

when (t\asymp n/\log n). Generic (S_j) monodromy would give complete-splitting density (1/j!). With the present (q_{\rm line}=p^2=\operatorname{poly}(n)),

[
\frac{q_{\rm line}}{j!}\longrightarrow0.
]

Thus the present positive-density mechanism is inherently a bounded-(j), high-rate mechanism. It cannot be lifted to corrected reserve merely by increasing the cover degree.

## BANKABLE_LEMMA

### Explicit good-reduction sets

For A,

[
P_A(1)=-19683=-3^9,
]

[
\operatorname{Res}(P_A,h)
=2^{40}3^{16}\cdot71\cdot127\cdot137.
]

A sufficient excluded integer is

[
N_A=
30,\operatorname{lc}(P_A),
|P_A(1)|,|\operatorname{Disc}(P_A)|,
|\operatorname{Res}(P_A,h)|.
]

Its complete factorization is

[
\begin{aligned}
N_A={}&2^{345}3^{114}5^7\cdot71\cdot127\cdot137
\cdot1031^2\cdot136189^2\
&\cdot169114662857729621^3\
&\cdot29920018492819343403247709.
\end{aligned}
]

In particular (p=7) is good. Among relevant A primes
(p\equiv3,7\pmod{20}), (p\ge7), the displayed sufficient set excludes only (p=127).

For B,

[
\operatorname{Res}(P_B,H)
=2^{64}3^{14}29^2,2063^6,20558103118321,
]

[
\operatorname{Res}(H,N_1)=-2^{10}3^2\cdot29\cdot2063.
]

A sufficient excluded integer is

[
N_B=
30,\operatorname{lc}(P_B),
|\operatorname{Disc}(P_B)|,
|\operatorname{Res}(P_B,H)|,
|\operatorname{Res}(H,N_1)|.
]

Its complete factorization is

[
\begin{aligned}
N_B={}&2^{471}3^{116}5^7,11^3,29^4,41^3,2063^{37}
,234007^2,1149593,4711367\
&\cdot429182827^2\cdot986904239^3\
&\cdot6003144422654343011^3\
&\cdot87979847046285199339509999686219951947\
&\cdot20558103118321.
\end{aligned}
]

Thus (p=19,31,59) are good; (p=11) is excluded because (P_B\bmod11) is not squarefree. Among relevant B primes (p\equiv11,19\pmod{20}), the displayed sufficient set excludes

[
11,\quad986904239,\quad6003144422654343011.
]

These sets are explicit sufficient bad sets, not asserted to be minimal stable-reduction sets.

Over (\mathbf Z[i]), define

[
S_s={\mathfrak p\subset\mathbf Z[i]:\mathfrak p\mid N_s\mathbf Z[i]}.
]

For the relevant (p\equiv3\pmod4), ((p)) is the unique inert Gaussian prime above (p). The actual (B=\mathbf F_p) model is obtained from the rational descent, not by replacing (B) with the Gaussian residue field (\mathbf F_{p^2}).

### Uniform (S_4) monodromy

Outside (S_A), the A projective line cover has:

* one stable tame (e=3) branch at (r=1);
* a finite étale divisor of (16) simple branch points (P_A=0);
* no branch at the roots of (h) or at infinity.

Outside (S_B), the B cover has (24) simple branches and no branch at (H=0) or infinity.

Tame specialization therefore preserves geometric monodromy.

At (p=7), Cycle 40’s A line contains unramified factorization types (4) and (13). At (p=31), the B line contains the same two types. A transitive subgroup of (S_4) containing a (4)-cycle and a (3)-cycle is (S_4). The two degree-one Frobenius elements cannot lie in one coset of either (A_4) or (V_4), so the geometric group is also (S_4).

Consequently, for every allowed prime outside the corresponding finite set,

[
G_{\rm geom,line}=G_{\rm arith,line}=S_4.
]

The line monodromy embeds into the two-dimensional surface monodromy. Since the latter is a subgroup of (S_4), it follows that

[
G_{\rm geom,surface}=G_{\rm arith,surface}=S_4.
]

### Chebotarev/Lang–Weil density

Let (U_{s,p}\subset\mathbf A^2_{\mathbf F_p}) be the open locus where

[
\Delta_s(z_0,z_1)\neq0
]

and the substituted quartic (L_{s,z}(X)) is separable.

Let (Y_{s,p}\to U_{s,p}) be the ordered-root cover. It is finite étale of degree (4!=24). The surface (Y_{s,p}) is geometrically irreducible because the geometric monodromy is (S_4).

For (z\in U_{s,p}(\mathbf F_p)), (L_{s,z}) splits into four distinct linear factors over (\mathbf F_p) exactly when the fiber of (Y_{s,p}) contains (24) rational points. Therefore

[
N^{\rm off}*{\rm split}(p)
=\frac{#Y*{s,p}(\mathbf F_p)}{24}.
]

The equations have fixed complexity within each subcase, so Lang–Weil gives a uniform constant (C_s) such that

[
#Y_{s,p}(\mathbf F_p)
=p^2+O_s(p^{3/2}).
]

Hence

[
N^{\rm off}*{\rm split}(p)
=\frac{p^2}{24}+O_s(p^{3/2})
=\frac{q*{\rm line}}{24}+O_s(q_{\rm line}^{3/4}).
]

The determinant and branch curves contain only (O(p)) slopes, which is absorbed by this error.

This proves the requested B-side global density and, simultaneously, the A-side density.

### Exact source-level witness construction

For each allowed (p), define

[
H_p=X^{p-1}+\alpha X^{p-2}+(1+\alpha)X^{p-3}+X^{p-4}.
]

Let (R_p\in F[X]_{<2}) be the unique representative of

[
(1+X)-[H_p]_E,
]

and put

[
W_p=H_p+R_p,\qquad w_p=W_p|_D.
]

Then

[
[W_p]_E=1+X
]

and the required top four coefficients are unchanged.

For a split surface point (z), let (T\subset\mathbf F_p) be the four roots of (L_{\tau(z)}), and set (S=D\setminus T). Then

[
|S|=p-4=k+t.
]

Write

[
W_p=L_SQ_S+I_S,\qquad \deg I_S<|S|.
]

Since (L_D=L_SL_T), reduction modulo (E) gives

[
[W_p]_E[L_T]_E
=[L_D]_E[Q_S]_E+[I_S]_E[L_T]_E.
]

The graph equation gives

[
([I_S]_E-zX)[L_T]_E=0.
]

Because (E) has no root on (D), ([L_T]_E) is a unit. Hence

[
[I_S]_E=zX.
]

Thus (I_S) is a degree-(<k+t) witness agreeing with (w_p) on (S).

It is automatically noncontained. If (G\in F[X]_{<k}) agreed with (-X/E) on (S), then

[
EG+X
]

would have degree (<k+t=|S|) and at least (|S|) roots. It would therefore vanish identically, impossible because (E\nmid X).

Consequently,

[
\Lambda^{\rm NC}*{2,,4/p}
\bigl(D=\mathbf F_p,k=p-6;,F=\mathbf F*{p^2}\bigr)
\ge
\frac{p^2}{24}-C_sp^{3/2}.
]

The exact-normal-form hypothesis also holds: (r=n-k=6), and (E^3) is a degree-(6) polynomial nonzero everywhere on (D). Therefore the source theorem gives the restricted MCA consequence

[
\varepsilon_{\rm mca}
\left(
\operatorname{RS}[\mathbf F_{p^2},\mathbf F_p,p-6],
\frac4p
\right)
\ge
\frac1{24}-O_s(p^{-1/2}).
]

All source hypotheses used in this last implication have now been checked explicitly.

## COUNTERPACKET

This can be promoted only in the following narrow sense:

> For both congruence subcases, outside an explicit finite prime set, there is a source-valid, noncontained, sub-reserve (t=2,j=4) packing of size
> [
> \frac{q_{\rm line}}{24}+O(q_{\rm line}^{3/4}),
> ]
> and hence a constant-order MCA lower bound.

It is therefore a **restricted local, sub-reserve COUNTERPACKET** against any reserve-free (n^{1+o(1)}) all-line slope bound.

It is not:

* a corrected-reserve counterpacket;
* a fixed-rate counterpacket;
* a counterexample to the floor- and quotient-corrected MCA conjecture;
* a CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize solution.

The obstruction is quantitative and structural:

[
\rho=1-\frac6p\longrightarrow1,
\qquad
\eta=\frac{t}{n}=\frac2p\ll\frac1{\log p}.
]

## EXPERIMENTAL

The following artifacts reproduce the exact symbolic calculations. They are corroboration and reproducibility material; the proof above does not treat finite scans as substitutes for the projective argument.

* [Full Cycle 42 certificate](sandbox:/mnt/data/20260618_CYCLE42_EXTERNAL_CO_DIRECTOR_CERTIFICATE.md)
* [Corrected projective good-reduction checker](sandbox:/mnt/data/20260618_cycle42_corrected_projective_goodred_checker.py)
* [Checker result](sandbox:/mnt/data/20260618_cycle42_corrected_projective_goodred_checker_result.json)
* [Complete bad-prime factorizations](sandbox:/mnt/data/20260618_cycle42_bad_prime_factorizations.json)
* [Full bivariate A discriminant data](sandbox:/mnt/data/bivar_A.json)
* [Full bivariate B discriminant data](sandbox:/mnt/data/bivar_B.json)
* [Finite surface split scan](sandbox:/mnt/data/20260618_cycle42_surface_split_scan.json)

## EXACT_NEW_WALL

The two requested walls are closed:

```text
W-F1-AA-RES-T2J4-A2B-S4-SUBCASEA-GOODRED-OBSTRUCTION
```

and

```text
W-F1-AA-RES-T2J4-A2B-S4-BSIDE-GLOBAL-DENSITY
```

The next exact wall is not another quartic or good-prime computation. It is:

```text
W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT
```

A theorem-sized formulation is:

> For fixed (\rho\in(0,1)), construct—or rule out—source-valid data with
> [
> k=\rho n+O(1),\qquad
> t=\sigma\ge Cn/\log n,\qquad
> j=n-k-t=\Theta(n),
> ]
> with (E) separated, nonvanishing and quotient-aperiodic, together with a structured family
> [
> \mathcal T_n\subseteq\binom D j
> ]
> for which membership (T\subset D) is automatic and the induced slope map has more than
> [
> n^{1+o(1)}
> +2^{(\beta/\mathsf H)\mathcal Q_H(\eta)(1+o(1))}
> ]
> distinct noncontained slopes.

Equivalently, the positive-theorem direction is to prove a **reserve-scale small-monodromy/structure dichotomy**:

> Any above-reserve aperiodic incidence cover with monodromy small enough to yield many completely split fibers must be tangent, contained, or quotient-periodic.

Without such a structured-co-support or small-monodromy theorem, the present (S_4) method cannot reach fixed rate: the corresponding generic (S_j) identity density is (1/j!).

**Do I see a route to a full solve?** Not from the bounded-(j) branch alone. The current two walls are solved, but a full corrected-reserve or prize-level solve requires the structured-co-support reserve lift—or the complementary small-monodromy classification—stated above. Confidence in the algebraic obstruction resolution and the restricted density theorem is high.
