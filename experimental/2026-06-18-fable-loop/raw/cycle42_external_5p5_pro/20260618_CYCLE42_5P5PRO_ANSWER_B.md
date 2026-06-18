The two current walls are resolved.

**Subcase A does globalize.** The failure on (z_1=z_0) is the combination of a nonprimitive Cramer presentation and a nongeneric tame cubic branch point. It is not a structural obstruction and not a Subcase-A route cut. The clean replacement line is
[
z_0=s,\qquad z_1=0,
]
with good reduction at (p_0=7).

**Subcase B’s certificate is source-valid.** The original line (z_1=z_0) has good reduction at (p_0=19).

For each subcase, outside an explicit finite bad-prime set, the surface quartic has geometric monodromy (S_4), and the number of off-branch slopes whose quartic splits completely over (B=\mathbf F_p) is
[
\frac{p^2}{24}+O(p^{3/2})
=\frac{q_{\rm line}}{24}+O(q_{\rm line}^{3/4}).
]

This also gives a source-valid **restricted, sub-reserve MCA lower bound** at radius (4/p). It is not a corrected-reserve result or a prize counterpacket.

## AUDIT

### Ledger

Throughout:
[
q_{\rm gen}=p,\qquad B=\mathbf F_p,
]
[
F=\mathbf F_{p^2}=B(\alpha),\qquad q_{\rm line}=p^2,
]
[
\alpha^2=-1,\qquad D=\mathbf F_p,
]
and (q_{\rm chal}) is unused.

The branch is
[
t=\sigma=2,\qquad j=4,\qquad r=6,\qquad k=p-6,\qquad a=p-4.
]

No identification of (q_{\rm gen}) with (q_{\rm line}) is made.

### Independent reconstruction of the characteristic-zero model

Work first in
[
K=\mathbf Q(i),\qquad
A=K[X]/(X^2+iX+1).
]
In (A),
[
X^2=-1-iX,\qquad X^3=i-2X,\qquad X^4=2+3iX.
]

Put
[
L_\tau=X^4-\tau_1X^3+\tau_2X^2-\tau_3X+\tau_4.
]
Then
[
[L_\tau]_E=\lambda_0+\lambda_1X
]
with
[
\lambda_0=2-i\tau_1-\tau_2+\tau_4,
\qquad
\lambda_1=3i+2\tau_1-i\tau_2-\tau_3.
]

Using the source-defined Cycle-29 quotient and the top coefficients
[
W_{p-1},W_{p-2},W_{p-3},W_{p-4}
=1,i,1+i,1,
]
one obtains
[
Q_\tau=
X^3+(i-\tau_1)X^2
+(1+i-i\tau_1+\tau_2)X
+1-(1+i)\tau_1+i\tau_2-\tau_3.
]
Reduction modulo (E) gives
[
[Q_\tau]_E=q_0+q_1X,
]
where
[
q_0=1-i\tau_1+i\tau_2-\tau_3,
\qquad
q_1=i+\tau_2.
]

Since (u=1+X), (b=X), the exact graph equation is
[
\bigl(1+(1-z)X\bigr)(\lambda_0+\lambda_1X)
=\ell(q_0+q_1X)
\quad\text{in }A.
]

For (c=1-z),
[
(1+cX)(a+bX)
=(a-cb)+\bigl(ca+(1-ic)b\bigr)X.
]

Writing
[
z=z_0+iz_1
]
and equating the four rational coordinates gives
[
M_\bullet(z_0,z_1)\tau+C_\bullet(z_0,z_1)=0.
]

For Subcase A, (\ell=i):
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
C_A=
\begin{pmatrix}
2-3z_1\
3z_0-4\
6-5z_0\
3-5z_1
\end{pmatrix}.
]

Its surface determinant is
[
\begin{aligned}
\det M_A={}&-z_0^4+3z_0^3-2z_0^2z_1^2+2z_0^2
+3z_0z_1^2+3z_0z_1-11z_0\
&-z_1^4+4z_1^2-9z_1+9.
\end{aligned}
]

For Subcase B, (\ell=-2X):
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
C_B=
\begin{pmatrix}
2-3z_1\
3z_0-5\
9-5z_0\
3-5z_1
\end{pmatrix}.
]

Its surface determinant is
[
\begin{aligned}
\det M_B={}&-z_0^4+6z_0^3-2z_0^2z_1^2-4z_0^2z_1-19z_0^2\
&+6z_0z_1^2+4z_0z_1+30z_0
-z_1^4-4z_1^3+5z_1^2+2z_1-19.
\end{aligned}
]

Thus the source equations actually descend from (K=\mathbf Q(i)) to a model over (\mathbf Q). The use of Gaussian arithmetic in Cycle 41 is an implementation choice, not the intrinsic field of definition of the resulting coordinate cover.

### The two Cycle-41 repairs

The first repair is **mathematically correct**:

* In the pair representation (a+bX\in K[X]/E), the element (\ell=i) is the pair
  [
  (i,0),
  ]
  not a bare Gaussian scalar supplied where a residue pair is expected.

The second repair is also **mathematically correct**, but only as an implementation adaptation:

* After taking real and imaginary parts, all matrix entries are rational scalars.
* Embedding each rational (r) as the Gaussian scalar ((r,0)) before applying the Gaussian determinant code leaves the determinant unchanged.

The repairs are nevertheless **insufficient as a certificate**. They do not address:

1. common polynomial factors shared by the Cramer determinant and every Cramer numerator;
2. the distinction between the discriminant of a primitive integral quartic and (D^6\operatorname{disc}) formed from an unreduced rational presentation;
3. legitimate higher tame ramification, for which the discriminant polynomial is not squarefree.

Thus the patched checker reconstructs the equations correctly, but its A-side interpretation is wrong.

## PROOF

### Resolution of the Subcase-A obstruction on (z_1=z_0)

Put (z_0=z_1=s). The raw Cycle-41 Cramer data are
[
D_{\rm raw}=-(s-1)^2(4s^2+2s-9),
]
and
[
\begin{aligned}
N_{1,\rm raw}&=-12(s-1)^3,\
N_{2,\rm raw}&=-(s-1)^2(12s^2-2s-13),\
N_{3,\rm raw}&=-(s-1)(28s^2-60s+35),\
N_{4,\rm raw}&=-(s-1)^2(4s^2-18s+17).
\end{aligned}
]

Hence
[
\gcd(D_{\rm raw},N_{1,\rm raw},\ldots,N_{4,\rm raw})=s-1.
]

The primitive Cramer data are therefore
[
D=-(s-1)(4s^2+2s-9),
]
[
\begin{aligned}
N_1&=-12(s-1)^2,\
N_2&=-(s-1)(12s^2-2s-13),\
N_3&=-(28s^2-60s+35),\
N_4&=-(s-1)(4s^2-18s+17).
\end{aligned}
]

For
[
P(s,x)=Dx^4-N_1x^3+N_2x^2-N_3x+N_4,
]
the primitive discriminant factors as
[
\operatorname{disc}*xP=(s-1)^2H*{16}(s),
]
with (H_{16}) squarefree and (H_{16}(1)\ne0).

The Cycle-41 checker instead formed
[
D_{\rm raw}^6\operatorname{disc}*x
\left(
x^4-\frac{N*{1,\rm raw}}{D_{\rm raw}}x^3+\cdots
\right),
]
which equals
[
(s-1)^8H_{16}(s).
]

Exactly six powers of (s-1) are presentation artifacts:
[
(s-1)^8=(s-1)^6\cdot(s-1)^2.
]

The remaining square is genuine ramification. Set
[
u=s-1,\qquad y=x^{-1},
]
and form
[
R(u,y)=y^4P(1+u,y^{-1}).
]
The exact expansion begins
[
R(u,y)=3u+3y^3-10u^2+3uy^2+12u^2y-4u^3+\cdots.
]
The lower Newton polygon has the segment
[
(0,1)\longrightarrow(3,0),
]
of slope (-1/3). Consequently three branches have (y)-valuation (1/3), so the local inertia contains a 3-cycle. This is tame away from (p=3), and its discriminant contribution is (3-1=2), exactly the residual factor ((s-1)^2).

Therefore:

* the factor ((s-1)^6) is a Cramer-normalization bug;
* the remaining ((s-1)^2) is a real tame cubic branch point;
* the line (z_1=z_0) is nongeneric for Subcase A;
* it does **not** show that the Subcase-A surface is non-etale generically or cannot globalize.

### Exact clean-line search criterion

For an affine line
[
z_0=s,\qquad z_1=ms+e,
]
the correct test is:

1. derive (D,N_1,\ldots,N_4) from (M\tau=-C);
2. divide all five polynomials by their common gcd;
3. form the primitive quartic
   [
   P=Dx^4-N_1x^3+N_2x^2-N_3x+N_4;
   ]
4. take the primitive part
   [
   d(s)=\operatorname{prim}\bigl(\operatorname{disc}_xP\bigr);
   ]
5. require
   [
   \operatorname{disc}_sD\ne0,\quad
   \operatorname{disc}_sd\ne0,\quad
   \operatorname{Res}_s(D,d)\ne0;
   ]
6. at a finite prime in the correct locator subcase, require preservation of degrees and factorization types (4) and (13).

The line (m=e=0), namely (z_1=0), passes immediately for Subcase A.

### Subcase A: clean line (z_1=0)

Put (z_0=s,z_1=0). The determinant and Cramer numerators are
[
D_A=-s^4+3s^3+2s^2-11s+9,
]
[
\begin{aligned}
N_{A,1}&=-3(s-1)(2s^2-5s+4),\
N_{A,2}&=-3s^4+10s^3-5s^2-12s+13,\
N_{A,3}&=-15s^3+55s^2-73s+35,\
N_{A,4}&=-s^4+4s^3-15s^2+25s-17.
\end{aligned}
]

Define
[
P_A(s,x)
=D_Ax^4-N_{A,1}x^3+N_{A,2}x^2-N_{A,3}x+N_{A,4}.
]

Its primitive branch polynomial is

```text
400*s^24 - 7920*s^23 + 69508*s^22 - 348316*s^21
+ 953209*s^20 + 258700*s^19 - 17489392*s^18
+ 97454182*s^17 - 313359736*s^16 + 733669438*s^15
- 2386040179*s^14 + 13728496688*s^13
- 70131665278*s^12 + 262090357400*s^11
- 731156131013*s^10 + 1571547336796*s^9
- 2655337076864*s^8 + 3560143325766*s^7
- 3789620525240*s^6 + 3177050813106*s^5
- 2060269324668*s^4 + 1000550914720*s^3
- 343644635244*s^2 + 74682091848*s - 7749383319
```

At (p_0=7),
[
(\operatorname{lc}D_A,\operatorname{lc}d_A,
\operatorname{Res}(D_A,D_A'),
\operatorname{Res}(d_A,d_A'),
\operatorname{Res}(D_A,d_A))
\equiv
(1,1,3,4,4)\pmod7.
]
All entries are nonzero.

The exact finite histogram is
[
{,112:1,;13:4,;4:2,}.
]

Explicit Frobenius witnesses are:

* At (s=0),
  [
  \tau=(6,3,0,2),
  ]
  and
  [
  L_\tau=(x-1)(x^3+2x^2-2x-2)
  \quad\text{over }\mathbf F_7,
  ]
  with the cubic irreducible. This is type (13).

* At (s=1),
  [
  \tau=(0,5,1,5),
  ]
  and
  [
  L_\tau=x^4-2x^2-x-2
  ]
  is irreducible over (\mathbf F_7). This is type (4).

A transitive subgroup of (S_4) containing a 4-cycle and a 3-cycle is (S_4). Since type (4) is odd and type (13) is even, the rational-point Frobenius elements do not all lie in one parity coset. Hence
[
G_{\rm arith}=G_{\rm geom}=S_4
]
on this finite line.

Because (7\equiv3\pmod4) and (7\equiv2\pmod5), this is genuinely a Subcase-A prime.

### Subcase B: line (z_1=z_0)

Put (z_0=z_1=s). There is no common Cramer factor. The determinant and numerators are
[
D_B=-4s^4+4s^3-10s^2+32s-19,
]
[
\begin{aligned}
N_{B,1}&=4(2s^3-13s^2+14s-1),\
N_{B,2}&=-12s^4+4s^3-38s^2+120s-99,\
N_{B,3}&=2(16s^3-60s^2+76s-31),\
N_{B,4}&=-4s^4-20s^3-62s^2+244s-205.
\end{aligned}
]

The primitive branch polynomial is

```text
102400*s^24 - 491520*s^23 + 1859584*s^22 - 3764224*s^21
+ 51914752*s^20 - 192626688*s^19 + 477325312*s^18
- 2008282112*s^17 + 7446446592*s^16 - 20807045120*s^15
+ 59079347712*s^14 - 185639798528*s^13
+ 512758278912*s^12 - 1116174999552*s^11
+ 2298634344064*s^10 - 5753999742784*s^9
+ 14592594673376*s^8 - 28990435945600*s^7
+ 41864795175328*s^6 - 43894177136944*s^5
+ 33781948075336*s^4 - 19154923131744*s^3
+ 7820247111000*s^2 - 2096953679988*s + 276965239259
```

At (p_0=19),
[
(\operatorname{lc}D_B,\operatorname{lc}d_B,
\operatorname{Res}(D_B,D_B'),
\operatorname{Res}(d_B,d_B'),
\operatorname{Res}(D_B,d_B))
\equiv
(4,9,8,13,17)\pmod{19}.
]
Again all entries are nonzero.

The finite histogram is
[
{,1111:1,;112:3,;13:4,;22:5,;4:4,;
\text{singular}:2,}.
]

Explicit witnesses are:

* (s=2):
  [
  \tau=(14,0,12,7),
  ]
  [
  L_\tau=(x-5)(x^3-9x^2-7x-9),
  ]
  with irreducible cubic, giving type (13).

* (s=6):
  [
  \tau=(10,16,4,2),
  ]
  [
  L_\tau=x^4+9x^3-3x^2-4x+2,
  ]
  irreducible over (\mathbf F_{19}), giving type (4).

Thus the finite geometric group is (S_4). Since
[
19\equiv3\pmod4,\qquad 19\equiv4\pmod5,
]
this is genuinely a Subcase-B certificate.

### Good reduction and the bad-prime set

For either clean line, let (D_\bullet(s)) be the primitive determinant and
[
d_\bullet(s)=\operatorname{prim}
\bigl(\operatorname{disc}*xP*\bullet(s,x)\bigr).
]

A sufficient, effective bad-prime integer is
[
N_\bullet
=========

30\left|
\operatorname{lc}(D_\bullet)
\operatorname{lc}(d_\bullet)
\operatorname{disc}*s(D*\bullet)
\operatorname{disc}*s(d*\bullet)
\operatorname{Res}*s(D*\bullet,d_\bullet)
\right|.
]

This is not claimed minimal.

For A:
[
\operatorname{lc}D_A=1,\qquad
\operatorname{lc}d_A=400,
]
[
\operatorname{disc}D_A=-25288=-2^3\cdot29\cdot109,
]
[
\operatorname{Res}(D_A,d_A)
=43304901709787942111597952.
]

For B:
[
\operatorname{lc}D_B=4,\qquad
\operatorname{lc}d_B=102400,
]
[
\operatorname{disc}D_B=-73559296,
]
[
\operatorname{Res}(D_B,d_B)
=117595767882696202767106970591341305306207654843031519280234496.
]

The exact integers (\operatorname{disc}d_A), (\operatorname{disc}d_B), (N_A), and (N_B) are in the attached exact certificate.

For every rational prime (p\nmid N_\bullet):

* the degrees of (D_\bullet,d_\bullet) are preserved;
* both remain squarefree;
* they remain disjoint;
* infinity remains outside the branch and pole divisors;
* (p\nmid24), so all inertia is tame.

The marked tame fundamental group of the line complement therefore specializes without changing the monodromy representation. The (p_0=7) and (p_0=19) fibers prove that the characteristic-zero geometric groups are (S_4), and every other good reduction has the same geometric group.

Over (\mathbf Z[i]), a sufficient bad-prime set is
[
\mathcal S_\bullet
==================

{\mathfrak p\subset\mathbf Z[i]:
\mathfrak p\mid N_\bullet\mathbf Z[i]}.
]
For the relevant primes (p\equiv3\pmod4), ((p)) is inert in (\mathbf Z[i]), so the condition is simply (p\nmid N_\bullet).

The congruence split is:
[
\begin{array}{c|c|c}
p\bmod20&\text{subcase}&\ell\ \hline
3,7&A&i\
11,19&B&-2X.
\end{array}
]

### Global split density on the surface

For a fixed good prime in its appropriate subcase, let
[
U_p\subset\mathbf A^2_{\mathbf F_p}
]
be the open locus where (\det M_\bullet\ne0) and the resulting quartic is squarefree.

Over (U_p), consider the ordered-root cover
[
Y_p\longrightarrow U_p,
]
whose points are
[
(z_0,z_1,x_1,x_2,x_3,x_4)
]
such that the elementary-symmetric tuple (e(x_1,\ldots,x_4)) satisfies
[
M_\bullet(z_0,z_1)e(x_1,\ldots,x_4)
+C_\bullet(z_0,z_1)=0
]
and
[
\prod_{r<s}(x_r-x_s)\ne0.
]

This is finite etale of degree (4!=24).

The restriction to the certified line already has geometric monodromy (S_4). The line monodromy is a subgroup of the surface monodromy, so the surface geometric monodromy is also (S_4). Hence the ordered-root cover is geometrically connected.

Lang–Weil gives
[
#Y_p(\mathbf F_p)=p^2+O_\bullet(p^{3/2}),
]
where the constant is effective and depends only on the fixed integral equations of the subcase.

A point (z\in U_p(\mathbf F_p)) contributes 24 ordered roots precisely when its quartic splits into four distinct linear factors over (\mathbf F_p), and otherwise contributes zero. Therefore
[
#\left{
z\in U_p(\mathbf F_p):
L_{\tau(z)}\text{ splits completely and distinctly}
\right}
=======

\frac{p^2}{24}+O_\bullet(p^{3/2}).
]

Equivalently,
[
N_{\rm split}(p)
================

\frac{q_{\rm line}}{24}
+O_\bullet(q_{\rm line}^{3/4}).
]

This resolves
[
\texttt{W-F1-AA-RES-T2J4-A2B-S4-BSIDE-GLOBAL-DENSITY}
]
and proves the analogous A-side statement.

## BANKABLE_LEMMA

### Two-subcase uniform (S_4) and density theorem

For every sufficiently large prime (p\equiv3\pmod4):

* use Subcase A when (p\equiv3,7\pmod{20}), excluding (p\mid N_A);
* use Subcase B when (p\equiv11,19\pmod{20}), excluding (p\mid N_B).

Then the source-defined (t=2,j=4) surface family has
[
G_{\rm geom}=G_{\rm arith}=S_4
]
and
[
N_{\rm split}(p)
================

\frac{p^2}{24}+O(p^{3/2}).
]

Confidence: **high**.

### Source-valid restricted MCA consequence

This consequence can now be promoted because all required source hypotheses can be checked directly.

Define
[
H_p=
X^{p-1}+\alpha X^{p-2}
+(1+\alpha)X^{p-3}+X^{p-4}.
]
Let (R_p) be the unique polynomial of degree (<2) such that
[
[R_p]_E=(1+X)-[H_p]_E,
]
and put
[
W_p=H_p+R_p.
]

Then:

* (\deg W_p<p);
* ([W_p]_E=1+X);
* its top four coefficients are (1,\alpha,1+\alpha,1);
* (E) is nonzero on (D=\mathbf F_p), since
  [
  E(a)=(a^2+1)+\alpha a
  ]
  cannot vanish;
* (E) and its conjugate are separated;
* (B_{\rm num}=X\ne0);
* (\kappa=(1+X)\wedge X=1).

For every split slope (z), let (T\subset\mathbf F_p) be the four distinct roots of (L_{\tau(z)}), and set
[
S=\mathbf F_p\setminus T,\qquad |S|=p-4.
]
Let (I_S) be the degree-(<p-4) interpolant of (W_p|_S). The exact graph equation gives
[
[I_S]_E=zX.
]
Hence
[
P_z=\frac{I_S-zX}{E}
]
is a polynomial of degree (<p-6=k), and on (S)
[
P_z=\frac{W_p-zX}{E}.
]

The residue line is therefore
[
f=\frac{W_p}{E},\qquad g=-\frac{X}{E}.
]

Noncontainment is automatic. If (G\in F[X]), (\deg G<k), agreed with (-X/E) on (S), then
[
EG+X
]
would have at least (p-4) roots but degree (<p-4), forcing (EG+X=0), impossible because (E\nmid X).

Thus
[
\Lambda^{\rm NC}_{2,,4/p}(D,k)
\ge
\frac{p^2}{24}+O(p^{3/2}).
]

The exact-normal-form auxiliary condition is also satisfied: because (p>3), the sixth-power map on (\mathbf F_p^\times) is not surjective, so one can choose (c) outside its image and (X^6-c) is a degree-6 polynomial nonzero on all of (D).

Therefore, for
[
C_p=\operatorname{RS}
[\mathbf F_{p^2},\mathbf F_p,p-6],
]
[
\operatorname{emca}!\left(C_p,\frac4p\right)
\ge
\frac1{24}-O(p^{-1/2}).
]

This is a genuine MCA statement, but only in the restricted sub-reserve regime
[
\sigma=2,\qquad \eta=\frac2p,
]
with rate (1-6/p).

## ROUTE_CUT

The following routes are cut:

1. **“Subcase A cannot globalize.”** False.
2. **“Failure of G2/G3 on (z_1=z_0) proves a non-etale obstruction.”** False.
3. **“The raw Cycle-41 discriminant numerator is intrinsic.”** False; it contains a spurious sixth power caused by a common Cramer factor.
4. **“Every good-reduction certificate must have squarefree quartic discriminant.”** False as a necessity; tame inertia of order (3) legitimately gives discriminant multiplicity (2).

The only route cut is narrower:

> The line (z_1=z_0) should not be used as a simple-branch good-reduction certificate for Subcase A.

## COUNTERPACKET

None.

The result is not above corrected reserve. It has
[
\eta=\frac2p=o!\left(\frac1{\log p}\right),
]
uses (D=\mathbf F_p), and has rate tending to (1). It therefore does not contradict the fixed-rate corrected-reserve conjecture and does not imply CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.

## EXACT_NEW_WALL

The characteristic-zero and global-density walls for the fixed (t=2,j=4) branch are closed.

The next exact construction needed for a full corrected-reserve solve is:

> **Reserve-growing source-valid split-cover construction.**
> For a fixed rate (\rho\in(0,1)), construct a family with
> [
> t_n=\sigma_n\ge C\frac{n}{\log n},
> \qquad
> k_n=\rho n+O(1),
> \qquad
> j_n=n-k_n-t_n,
> ]
> on the required generated-field or smooth domain, together with separated, aperiodic residue-line data
> [
> (E_n,B_n,W_n)
> ]
> such that the noncontained slope image contains (c,q_{\rm line}) slopes for some fixed (c>0). Equivalently, construct a geometrically connected ordered-root cover for the degree-(j_n) co-support locator, with uniform Lang–Weil or Chebotarev estimates strong enough when (j_n) grows.

The fixed quartic argument does not itself provide this. At fixed rate, (j_n) grows linearly with (n), so both monodromy degree and error constants must be controlled uniformly. That is the real scaling wall.

## EXPERIMENTAL

No random or heuristic computation is needed for the conclusions above. The supplied checker:

* derives both matrices directly from the residue equation;
* primitive-reduces the Cramer presentation;
* computes exact discriminants and resultants over (\mathbf Z);
* verifies the (p=7) and (p=19) finite factorization certificates.

Artifacts:

* [Independent exact checker](sandbox:/mnt/data/cycle42_external_model_certificate.py)
* [Exact JSON certificate](sandbox:/mnt/data/cycle42_external_model_certificate.json)
* [Readable certificate](sandbox:/mnt/data/cycle42_external_model_certificate.md)

**Do you see a route to a full solve?** Yes, but not by further work on the fixed (t=2,j=4) monodromy wall; that branch is now complete. The next exact construction is the reserve-growing, fixed-rate split-cover family above—or, on the positive side, a theorem proving that no such family can have (\Theta(q_{\rm line})) slope image once (t=\sigma\gtrsim n/\log n).
