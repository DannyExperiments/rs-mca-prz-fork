**Verdict:** both active walls are resolved for the restricted (t=2,j=4) branch.

The Subcase A failure is a false negative caused by applying a non-invariant good-reduction test to an unsaturated Cramer model. On the original line (z_1=z_0), the A-cover is smooth and tamely ramified, with one genuine (e=3) branch point at (s=1). It has good reduction at (p=7). Subcase B has good reduction at (p=31). Both characteristic-zero line covers have geometric monodromy (S_4), and both surface families consequently have split-slope density

[
\frac1{24}+O(p^{-1/2})
]

relative to (q_{\rm line}=p^2), outside explicit finite exclusion sets.

Confidence: **high**. The displayed bad-prime sets are certified sufficient sets; minimality is not asserted.

The ledgers remain:

[
q_{\rm gen}=p,\qquad
B=\mathbb F_p,\qquad
F=\mathbb F_{p^2}=B(\alpha),\quad \alpha^2=-1,
]
[
q_{\rm line}=p^2,\qquad q_{\rm chal}\text{ unused},\qquad
D=\mathbb F_p.
]

## AUDIT

### The two Cycle 41 repairs

Both local repairs are mathematically correct.

1. In (K[X]/E), with (K=\mathbb Q(i)), the scalar (i) must be represented as the residue pair
   [
   (i,0),
   ]
   not as a bare Gaussian scalar supplied where a residue element (c_0+c_1X) is expected.

2. After flattening an equation in
   [
   K[X]/E\simeq \mathbb Q^4
   ]
   into rational real/imaginary coordinates, a rational entry (r) must be embedded as the Gaussian scalar
   [
   (r,0)
   ]
   before passing it to the Gaussian determinant routine.

These repairs fix the checker’s types. They do **not** repair its mathematical good-reduction criterion.

### The substantive checker error

Cycle 41 used the Cramer determinant (D(s)) and

[
D(s)^6\operatorname{disc}*X L*{\tau(s)}
]

as two separate branch polynomials, and demanded that each be squarefree and that they be disjoint.

That is not invariant under:

* multiplying the binary quartic by a scalar polynomial;
* saturating a cleared-denominator equation by its coefficient content;
* changing from a monic affine root chart to the projective root line.

A zero of (D) can merely mean that one root moves to (X=\infty). It need not be a branch point or a singularity. Moreover, a tame (e=3) branch has discriminant multiplicity (e-1=2); squarefreeness of the weighted discriminant would incorrectly reject it.

The correct object is the **primitive projective binary quartic**

[
H(s;Y,Z)
]

obtained after removing the common content of the five Cramer coefficients. Good reduction is then checked on its projective curve, its reduced branch divisor, and its tame inertia indices.

Thus:

* the two Codex repairs are **correct**;
* the patched checker is **insufficient as a good-reduction checker**;
* its conclusion that Subcase A fails is **wrong**;
* its Subcase B conclusion happens to be true, but requires the independent primitive/projective audit below.

---

## PROOF

### 1. Independent characteristic-zero derivation

Work over

[
K=\mathbb Q(i),\qquad
A_K=K[X]/(X^2+iX+1).
]

In (A_K),

[
X^2=-1-iX,\qquad
X^3=i-2X,\qquad
X^4=2+3iX.
]

Let

[
L_\tau=X^4-\tau_1X^3+\tau_2X^2-\tau_3X+\tau_4.
]

Then

[
[L_\tau]_E
==========

\bigl(2-i\tau_1-\tau_2+\tau_4\bigr)
+
\bigl(3i+2\tau_1-i\tau_2-\tau_3\bigr)X.
]

Using the Cycle 29 quotient formula with

[
W_{n-1},W_{n-2},W_{n-3},W_{n-4}
===============================

1,i,1+i,1,
]

one obtains

[
\begin{aligned}
Q_\tau={}&X^3+(i-\tau_1)X^2
+(1+i-i\tau_1+\tau_2)X\
&+1-(1+i)\tau_1+i\tau_2-\tau_3,
\end{aligned}
]

and therefore

[
[Q_\tau]_E
==========

\bigl(1-i\tau_1+i\tau_2-\tau_3\bigr)
+
(i+\tau_2)X.
]

Write

[
z=z_0+iz_1,\qquad
u=1+X,\qquad b=X.
]

The source graph equation is exactly

[
(1+(1-z)X)[L_\tau]*E-\ell[Q*\tau]_E=0.
]

Flattening in the basis (1,i,X,iX) gives (M_\bullet(z)\tau=-c_\bullet(z)).

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
2-3z_1\
3z_0-4\
6-5z_0\
3-5z_1
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
2-3z_1\
3z_0-5\
9-5z_0\
3-5z_1
\end{pmatrix}.
]

The two surface Cramer determinants are

[
\begin{aligned}
\Delta_A={}&-z_0^4+3z_0^3-2z_0^2z_1^2+2z_0^2
+3z_0z_1^2+3z_0z_1\
&-11z_0-z_1^4+4z_1^2-9z_1+9,
\end{aligned}
]

and

[
\begin{aligned}
\Delta_B={}&-z_0^4+6z_0^3-2z_0^2z_1^2-4z_0^2z_1-19z_0^2\
&+6z_0z_1^2+4z_0z_1+30z_0-z_1^4-4z_1^3\
&+5z_1^2+2z_1-19.
\end{aligned}
]

This derivation reproduces the Cycle 40 finite models after reduction. There is no reconstruction error in the characteristic-zero matrices.

---

### 2. Subcase A on (z_1=z_0=s)

Put

[
h=s-1,\qquad q_A(s)=4s^2+2s-9.
]

Cramer’s rule gives

[
D_A=-h^2q_A
]

and

[
\begin{aligned}
N_1&=-12h^3,\
N_2&=-h^2(12s^2-2s-13),\
N_3&=-h(28s^2-60s+35),\
N_4&=-h^2(4s^2-18s+17).
\end{aligned}
]

Thus

[
\begin{aligned}
\tau_1&=\frac{12h}{q_A},\
\tau_2&=\frac{12s^2-2s-13}{q_A},\
\tau_3&=\frac{28s^2-60s+35}{h q_A},\
\tau_4&=\frac{4s^2-18s+17}{q_A}.
\end{aligned}
]

The cleared Cramer binary form is

[
H_{\rm raw}
===========

D_AY^4-N_1Y^3Z+N_2Y^2Z^2-N_3YZ^3+N_4Z^4.
]

Its five coefficients have common content (h). After saturation and a harmless sign normalization, the primitive binary quartic is

[
\boxed{
\begin{aligned}
H_A(s;Y,Z)={}&
h q_A,Y^4
-12h^2Y^3Z\
&+h(12s^2-2s-13)Y^2Z^2\
&-(28s^2-60s+35)YZ^3\
&+h(4s^2-18s+17)Z^4 .
\end{aligned}}
]

Its intrinsic discriminant is

[
\operatorname{Disc}_{Y,Z}(H_A)=h^2P_A(s),
]

where

```text
P_A(s) =
  1638400 s^16 - 4587520 s^15 - 34881536 s^14
+ 73072640 s^13 + 358903808 s^12 - 641441792 s^11
- 2127262720 s^10 + 2484816896 s^9 + 17489308160 s^8
- 39769366016 s^7 - 20116857792 s^6 + 194165722432 s^5
- 347849758128 s^4 + 331010951712 s^3 - 184759775360 s^2
+ 57468880452 s - 7749383319.
```

By contrast, the Cycle 41 raw numerator is

[
D_A^6\operatorname{disc}(L_\tau)
================================

# \operatorname{Disc}(H_{\rm raw})

h^8P_A(s).
]

Therefore the Cycle 41 failures were forced in characteristic zero:

[
D_A=-h^2q_A,\qquad
D_{\rm disc,raw}=h^8P_A.
]

Both are non-squarefree, and they share (h), before any reduction is taken.

#### The point (s=1)

At (h=0),

[
H_A(1;Y,Z)=-3YZ^3.
]

The point ([Y:Z]=[0:1]) is a simple unramified point. The other point is the root at infinity ([1:0]), of multiplicity three.

In the chart (Y=1), (w=Z/Y), the local equation is

[
\begin{aligned}
F(h,w)={}&
h q_A(s)-12h^2w
+h(12s^2-2s-13)w^2\
&-(28s^2-60s+35)w^3
+h(4s^2-18s+17)w^4.
\end{aligned}
]

At ((h,w)=(0,0)),

[
F_h(0,0)=q_A(1)=-3\ne0,
]

while the first nonzero (w)-term is

[
-3w^3.
]

Consequently the total curve is smooth there and

[
h=-w^3+\text{higher terms}.
]

This is one tame ramification point of index

[
e=3.
]

The factor (h^2) in the intrinsic discriminant is exactly the expected exponent (e-1=2). It is neither a collision nor a non-étale degeneration of the total curve.

The reduced branch support is

[
hP_A(s),
]

not (D_A\cdot h^8P_A).

At (p=7),

[
\operatorname{lc}(P_A)\equiv1,\qquad
P_A(1)\equiv1,\qquad
\operatorname{Res}(P_A,P_A')\equiv3\pmod7,
]

and the local coefficients satisfy

[
q_A(1)\equiv4,\qquad
28-60+35\equiv3\pmod7.
]

Thus the (e=3) branch survives tamely and is disjoint from the sixteen simple roots of (P_A).

An independent four-chart projective Jacobian computation gives the unit Gröbner basis in all four charts:

[
\begin{array}{c}
\text{base finite/fiber finite},\quad
\text{base finite/fiber infinity},\
\text{base infinity/fiber finite},\quad
\text{base infinity/fiber infinity}.
\end{array}
]

Hence the reduction of (H_A=0) at (p=7) is a smooth projective curve.

The finite factorization witnesses are:

[
s=0,\quad
\tau=(6,3,0,2),\quad \text{type }13,
]

and

[
s=3,\quad
\tau=(2,1,3,4),\quad \text{type }4.
]

Therefore the (p=7) line cover has

[
G_{\rm arith}=G_{\rm geom}=S_4.
]

### Classification of the A-side obstruction

The answer to the four alternatives is:

* **not** a branch collision or non-étale obstruction;
* **not** a bug in the reconstructed characteristic-zero equations;
* **not** a route cut;
* primarily a **bug in the good-reduction criterion**;
* with a genuine but harmless line-specific feature: a tame (e=3) branch at infinity.

A different line is unnecessary.

---

### 3. Subcase B on (z_1=z_0=s)

Put

[
Q_B=4s^4-4s^3+10s^2-32s+19,
]

and

[
\begin{aligned}
b_1&=2s^3-13s^2+14s-1,\
b_2&=12s^4-4s^3+38s^2-120s+99,\
b_3&=16s^3-60s^2+76s-31,\
b_4&=4s^4+20s^3+62s^2-244s+205.
\end{aligned}
]

Cramer’s rule gives (D_B=-Q_B) and

[
\tau_1=-\frac{4b_1}{Q_B},\qquad
\tau_2=\frac{b_2}{Q_B},\qquad
\tau_3=-\frac{2b_3}{Q_B},\qquad
\tau_4=\frac{b_4}{Q_B}.
]

The primitive projective quartic is

[
\boxed{
H_B=
Q_BY^4+4b_1Y^3Z+b_2Y^2Z^2+2b_3YZ^3+b_4Z^4 .
}
]

There is no coefficient content. Its discriminant is

[
\operatorname{Disc}_{Y,Z}(H_B)=16P_B(s),
]

where

```text
P_B(s) =
  102400 s^24 - 491520 s^23 + 1859584 s^22 - 3764224 s^21
+ 51914752 s^20 - 192626688 s^19 + 477325312 s^18
- 2008282112 s^17 + 7446446592 s^16 - 20807045120 s^15
+ 59079347712 s^14 - 185639798528 s^13 + 512758278912 s^12
- 1116174999552 s^11 + 2298634344064 s^10
- 5753999742784 s^9 + 14592594673376 s^8
- 28990435945600 s^7 + 41864795175328 s^6
- 43894177136944 s^5 + 33781948075336 s^4
- 19154923131744 s^3 + 7820247111000 s^2
- 2096953679988 s + 276965239259.
```

At (p=31),

[
\operatorname{lc}(P_B)\equiv7,\qquad
\operatorname{Res}(P_B,P_B')\equiv2\pmod{31}.
]

The same four-chart projective Jacobian test proves smoothness.

The finite witnesses are

[
s=0,\quad
\tau=(10,15,0,1),\quad \text{type }4,
]

and

[
s=4,\quad
\tau=(22,29,3,13),\quad \text{type }13.
]

Hence

[
G_{\rm arith}=G_{\rm geom}=S_4
]

at (p=31).

---

## BANKABLE_LEMMA

### Primitive line-cover good reduction

Let (C_A\to\mathbb P^1) and (C_B\to\mathbb P^1) be the projective covers defined by (H_A=0) and (H_B=0).

For A, outside the finite set defined by

[
N_A=
6,\operatorname{lc}(P_A),P_A(1),\operatorname{Disc}(P_A),
]

the branch data are:

[
1\text{ branch point of index }3,
\qquad
16\text{ branch points of index }2.
]

For B, outside the finite set defined by

[
N_B=
6,\operatorname{lc}(P_B),\operatorname{Disc}(P_B),
]

there are twenty-four distinct branch points, all of index (2).

The absence of branch at base infinity follows from the full discriminant degrees:

[
\deg(h^2P_A)=18=6\deg_s(H_A),
]

and

[
\deg(P_B)=24=6\deg_s(H_B).
]

At a simple zero of (P_A) or (P_B), the standard local discriminant criterion gives one smooth (e=2) ramification point. The unique A-point over (h=0) was checked explicitly and has smooth tame index (3).

Thus these are tame covers over the corresponding localizations of (\mathbb Z[i]). Tame specialization preserves the geometric monodromy representation.

Since the (p=7) A-fiber and (p=31) B-fiber have geometric group (S_4),

[
G_{\rm geom}
\bigl(C_A/\overline{\mathbb Q(i)}(s)\bigr)
==========================================

G_{\rm geom}
\bigl(C_B/\overline{\mathbb Q(i)}(s)\bigr)
==========================================

S_4.
]

Moreover, every good reduction of either line cover has geometric group (S_4).

### Certified finite exclusion sets over (\mathbb Z[i])

A sufficient rational-prime support for A is

[
\boxed{
S_A=
{2,3,5,1031,136189,
169114662857729621,
29920018492819343403247709}.
}
]

Indeed,

[
\begin{aligned}
\operatorname{Disc}(P_A)=
-&2^{288}3^{88}5^4
1031^2,136189^2\
&\cdot169114662857729621^3\
&\cdot29920018492819343403247709.
\end{aligned}
]

Also

[
\operatorname{lc}(P_A)=2^{16}5^2,\qquad
P_A(1)=-3^9.
]

A sufficient support for B is

[
\boxed{
\begin{aligned}
S_B={&
2,3,5,11,29,41,2063,234007,1149593,4711367,\
&429182827,986904239,6003144422654343011,\
&87979847046285199339509999686219951947
}.
\end{aligned}}
]

Here

[
\begin{aligned}
\operatorname{Disc}(P_B)=
-&2^{384}3^{99}5^4,11^3,29,41^3,2063^{30}
,234007^2\
&\cdot1149593\cdot4711367\cdot429182827^2
\cdot986904239^3\
&\cdot6003144422654343011^3\
&\cdot87979847046285199339509999686219951947.
\end{aligned}
]

For complete ideal-theoretic precision, the bad set over (\mathbb Z[i]) is the set of Gaussian prime ideals dividing ((N_A)) or ((N_B)). The displayed rational lists give their rational support.

For the source congruence classes:

[
\text{A: }p\equiv3,7\pmod{20},
\qquad
\text{B: }p\equiv11,19\pmod{20}.
]

The intersections with the certified exclusion sets are

[
S_A\cap{p\equiv3,7\pmod{20}}={3},
]

and

[
S_B\cap{p\equiv11,19\pmod{20}}
==============================

{11,\ 986904239,\ 6003144422654343011}.
]

Consequently:

* every A-source prime (p\ge7) is good for this certificate;
* every B-source prime outside the three displayed exceptions is good.

These are sufficient exclusions, not claimed minimal.

---

## PROOF

### Surface (S_4) and global split density

For every certified good source prime (p), the corresponding line pullback has geometric group (S_4). A line-pullback monodromy group is a subgroup of the two-dimensional surface monodromy group. Since the latter is itself a subgroup of (S_4),

[
S_4
\subseteq G_{\rm geom,surface}
\subseteq S_4.
]

Therefore

[
G_{\rm geom,surface}=S_4.
]

Let (U_p\subset\mathbb A^2_{\mathbb F_p}) be the fixed dense open obtained by removing:

* the Cramer determinant locus;
* the quartic discriminant locus;
* the remaining fixed Cycle 29/34 denominator loci.

Let

[
\widetilde V_p\longrightarrow U_p
]

be the (S_4)-Galois closure. Since the geometric monodromy is (S_4), (\widetilde V_p) is geometrically irreducible of dimension two.

Lang–Weil gives

[
#\widetilde V_p(\mathbb F_p)
============================

p^2+O(p^{3/2}),
]

with an implied constant depending only on the fixed subcase model.

For (z\in U_p(\mathbb F_p)), the fiber is an (S_4)-torsor. It has an (\mathbb F_p)-point precisely when Frobenius is the identity; in that case all (24) torsor points are rational. Identity Frobenius is equivalent to (L_{\tau(z)}) splitting into four distinct linear factors over (\mathbb F_p).

Hence

[
24N_{\rm split}(p)
==================

p^2+O(p^{3/2}),
]

so

[
\boxed{
N_{\rm split}(p)
================

# \frac{p^2}{24}+O(p^{3/2})

\frac{q_{\rm line}}{24}
+O(q_{\rm line}^{3/4}).
}
]

The removal of the fixed divisor complement costs only (O(p)), already absorbed by the error term.

This closes

[
\texttt{W-F1-AA-RES-T2J4-A2B-S4-BSIDE-GLOBAL-DENSITY},
]

and in fact gives the same conclusion for Subcase A.

### Source landing and noncontainment

For a split point (z), let (T\subset\mathbb F_p) be the four distinct roots of (L_{\tau(z)}), and put

[
S=D\setminus T.
]

Then

[
|S|=p-4.
]

Set

[
n=p,\qquad k=p-6,\qquad t=\sigma=2,\qquad j=4,
]

so

[
|S|=k+t.
]

Choose

[
W_{\rm top}
===========

X^{p-1}+\alpha X^{p-2}+(1+\alpha)X^{p-3}+X^{p-4},
]

and let (R\in F[X]_{<2}) be the unique residue correction satisfying

[
[W_{\rm top}+R]_E=1+X.
]

Then

[
W=W_{\rm top}+R
]

has exactly the required top coefficients and (u=[W]_E=1+X).

Divide

[
W=L_SQ_S+I_S,\qquad \deg I_S<|S|.
]

The graph equation and the fact that ([L_T]_E) is a unit give

[
[I_S]_E=zX.
]

Thus (I_S) is a degree-(<k+t) residue-line witness for slope (z).

Noncontainment is automatic. If (G\in F[X]_{<k}) agreed with (-X/E) on (S), then

[
EG+X
]

would have degree (<k+t=|S|) and at least (|S|) roots, hence would vanish identically. That would imply (E\mid X), impossible.

Therefore

[
\Lambda^{\rm NC}_{2,,4/p}
(\mathbb F_p,p-6)
\ge
\frac{p^2}{24}+O(p^{3/2}).
]

The exact normal-form theorem applies: (r=n-k=6), and for example

[
(X-\alpha)^6
]

is a degree-six polynomial nonzero on (D=\mathbb F_p). Consequently the explicit words

[
f=\frac{w}{E},\qquad
g=-\frac{X}{E}
]

satisfy

[
\boxed{
\epsilon_{\rm mca}
\left(
\operatorname{RS}[\mathbb F_{p^2},\mathbb F_p,p-6],
\frac4p
\right)
\ge
\frac1{24}-O(p^{-1/2}).
}
]

This is a source-valid restricted extension-line MCA lower bound. It does not merge (q_{\rm gen}=p) with (q_{\rm line}=p^2).

---

## ROUTE_CUT

The following routes are cut:

1. **“Subcase A cannot globalize because every tested prime fails good reduction.”**
   False. The failure is built into the raw Cramer factors (h^2) and (h^8). The primitive projective cover has good reduction at (p=7).

2. **“The Cramer determinant must be a reduced branch divisor disjoint from the quartic discriminant.”**
   False. Its zeros can be affine-chart failures, including ramification at a root at infinity.

3. **“A repeated discriminant factor is automatically bad reduction.”**
   False. The A-factor (h^2) records one smooth tame (e=3) point.

There is no route cut for Subcase A itself.

---

## COUNTERPACKET

No corrected-reserve, generated-field, smooth-domain, protocol, SNARK, or prize `COUNTERPACKET` is established.

The proven family has

[
\rho_p=\frac{p-6}{p}\longrightarrow1,
\qquad
\sigma=2,
\qquad
\frac{\sigma}{n}=\frac2p,
]

whereas the final corrected reserve requires fixed (\rho) and

[
\sigma\ge C\frac n{\log n}.
]

Furthermore,

[
D=\mathbb F_p,\qquad
q_{\rm gen}=p,\qquad
q_{\rm line}=p^2,
]

so the evaluation domain does not generate the line field. The current theorem is therefore a restricted extension-line result, not a disproof of the final generated-field conjecture.

---

## EXPERIMENTAL

A different A-line is not needed, but there is a redundant simple-branch certificate on

[
z_1=0.
]

Its Cramer denominator is

[
D_{A,0}=-s^4+3s^3+2s^2-11s+9,
]

and, writing

[
Q_{A,0}=s^4-3s^3-2s^2+11s-9,
]

the parameters are

[
\begin{aligned}
\tau_1&=\frac{3(s-1)(2s^2-5s+4)}{Q_{A,0}},\
\tau_2&=\frac{3s^4-10s^3+5s^2+12s-13}{Q_{A,0}},\
\tau_3&=\frac{15s^3-55s^2+73s-35}{Q_{A,0}},\
\tau_4&=\frac{s^4-4s^3+15s^2-25s+17}{Q_{A,0}}.
\end{aligned}
]

At (p=7), for its degree-24 discriminant factor (P_{A,0}),

[
\operatorname{Res}(Q_{A,0},Q_{A,0}')\equiv3,
]

[
\operatorname{Res}(P_{A,0},P_{A,0}')\equiv4,
]

[
\operatorname{Res}(Q_{A,0},P_{A,0})\equiv4
\pmod7.
]

There are no Cramer-singular (s)-values. The witnesses

[
s=0,\quad \tau=(6,3,0,2)
]

and

[
s=1,\quad \tau=(0,5,1,5)
]

have types (13) and (4), respectively. Thus this line also gives good reduction and (S_4), using only simple branch points.

The independent derivation and all exact assertions are in:

* [Corrected characteristic-zero/good-reduction checker](sandbox:/mnt/data/cycle42_corrected_goodred_checker.py)
* [Machine-readable certificate](sandbox:/mnt/data/cycle42_corrected_goodred_certificate.json)

---

## EXACT_NEW_WALL

The current (t=2,j=4) branch is complete. The next theorem required to move toward the full corrected-reserve problem is:

[
\boxed{
\texttt{W-F1-AA-RES-RESERVE-SCALED-GENERATED-FIELD-QUARTIC-CORE-LIFT}.
}
]

An exact useful formulation is:

For fixed (\rho\in(0,1)) and

[
\sigma_n=t_n\ge C\frac n{\log n},\qquad
j_n=n-k_n-t_n,
]

construct source-valid data

[
(D_n,F_n,E_n,B_{{\rm num},n},W_n)
]

and a fixed co-support

[
T_{0,n}\subset D_n,\qquad |T_{0,n}|=j_n-4,
]

such that, for

[
T=T_{0,n}\sqcup T_4,\qquad |T_4|=4,
]

the full landing equation modulo the genuinely degree-(t_n) denominator (E_n) reduces to the proven A or B quartic surface in the four moving roots (T_4), with:

[
#{\text{split slopes}}\ge c,q_{\rm line};
]

no effective reduction to a lower-degree denominator;

no quotient-periodic or residual-slack explanation;

noncontainment preserved;

and, for the final prize target, (D_n) a smooth multiplicative domain generating (F_n), so that (q_{\rm gen}=q_{\rm line}).

The hard algebra is to arrange that all residue coordinates introduced by the large denominator and the frozen (j_n-4) roots vanish or become identities, leaving exactly the already-proved quartic-core equation.

**Do you see a route to a full solve?**
Yes for the current branch: it is now solved through global density. For the full corrected-reserve/proximity problem, the route is the reserve-scaled generated-field quartic-core lift above. Proving or refuting that exact construction is the next decisive lemma.
