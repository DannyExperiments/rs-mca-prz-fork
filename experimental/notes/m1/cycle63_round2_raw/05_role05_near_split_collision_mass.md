COUNTERPACKET

## 1. Executive verdict and confidence

The hoped block-scale residual bound is false after nontrivial full-block trades are removed.

There is an exact characteristic-(17) model fiber with

[
52{,}747{,}567{,}104>2^{32}
]

product-conditioned supports, although every support contains no full coset of any subgroup of order at least (\sigma=6). Its normalized collision entropy is therefore strictly greater than one bit per least eligible block.

The construction tensors to a fixed-(\sigma=6) family of size

[
52{,}747{,}567{,}104^R
]

on (32R) least eligible blocks. It grows faster than both the Role-03 block residual and the effective-group baseline.

**Confidence: high, (0.99).**

---

## 2. Formal counterpacket statement

Call (T\subseteq H) **(\sigma)-block-free** if no coset (cK\subseteq T) exists for any subgroup (K\le H) with (|K|\ge \sigma).

### Theorem

Let

[
F_0=\mathbb F_{17^{16}},\qquad
H_0=\mu_{256}\subset F_0^\times,\qquad
\sigma=6,\qquad j=113.
]

There is a model target

[
b_0=\left(\prod T,e_1(T),\ldots,e_5(T)\right)
=(1,1,0,0,0,0)
]

such that its fiber contains exactly the explicitly constructed packet

[
\mathcal P_0,\qquad
|\mathcal P_0|=52{,}747{,}567{,}104,
]

and every (T\in\mathcal P_0) satisfies:

1. (T) is (6)-block-free;
2. (T) has trivial multiplicative stabilizer in (H_0);
3. every eligible full-block trade class meets (\mathcal P_0) in at most one support.

Moreover,

[
52{,}747{,}567{,}104
=393\cdot 2^{27}

> ;2^{32}
> \binom{32}{16}=601{,}080{,}390.
> ]

Here (32=|H_0|/M_0), where

[
M_0=2^{\lceil\log_2 6\rceil}=8.
]

Thus

[
\frac{\log_2|\mathcal P_0|}{|H_0|/M_0}>1.
]

For every power of two (R\ge1), the packet tensors to a single model fiber over

[
F_R=\mathbb F_{17^{16R}},\qquad
|H_R|=256R,\qquad
j_R=113R,
]

containing at least

[
|\mathcal P_R|=|\mathcal P_0|^R
]

block-free supports.

The same packet is realized in the minimal scalar CI stratum with

[
I_s=(XZ^6,B),\qquad
\deg(XZ^6)=7=\sigma+1,\qquad
\deg B=113R=j_R,
]

for the Reed–Solomon parameters

[
n=256R,\qquad r=113R+6,\qquad k=143R-6.
]

---

## 3. Full construction and proof

### 3.1 The 48-state characteristic-(17) jet gadget

Put (\zeta=3\in\mathbb F_{17}), which has order (16). Define exponent sets

[
\begin{aligned}
E_1&={0,1,2,3,5,11,12,13},\
E_2&={0,1,2,3,4,8,9,14},\
E_3&={0,1,2,4,5,7,11,14}.
\end{aligned}
]

Let

[
A_i={\zeta^e:e\in E_i}\subseteq\mu_{16}.
]

Direct multiplication in (\mathbb F_{17}[X]) gives

[
\prod_{x\in A_1}(X-x)
=====================

X^8+4X^5+5X^4+10X^3+4X^2+4X+6,
]

[
\prod_{x\in A_2}(X-x)
=====================

X^8+9X^5+5X^4+12X^3+14X^2+13X+14,
]

[
\prod_{x\in A_3}(X-x)
=====================

X^8+11X^5+5X^3+X^2+12X+4.
]

The (X^7) and (X^6) coefficients vanish in all three cases. Hence

[
e_1(A_i)=e_2(A_i)=0.
]

For (a\in\mathbb Z/16\mathbb Z), put

[
A_{i,a}:=\zeta^aA_i.
]

Scaling preserves (e_1=e_2=0), so all (48) sets (A_{i,a}) lie in one jet fiber.

They are distinct. Each (E_i) has trivial translation stabilizer because it is not invariant under addition by (8), and their cyclic gap words are respectively

[
(1,1,1,2,6,1,1,3),
]

[
(1,1,1,1,4,1,5,2),
]

[
(1,1,2,1,2,4,3,2),
]

which are inequivalent under cyclic rotation.

Their product colors are also explicit. The three seed products are

[
\prod A_1=\zeta^{15},\qquad
\prod A_2=\zeta^9,\qquad
\prod A_3=\zeta^{12}.
]

Since (|A_i|=8),

[
\prod A_{i,a}=\zeta^{8a}\prod A_i.
]

Thus the product exponent multiset of the (48) states is

[
8\cdot{1,4,7,9,12,15}\subset\mathbb Z/16\mathbb Z.
\tag{3.1}
]

Finally, relative to the four (\mu_4)-cosets in (\mu_{16}), the three occupancy vectors are

[
(2,3,1,2),\qquad
(3,2,2,1),\qquad
(2,2,2,2).
\tag{3.2}
]

Translation only cyclically permutes these coordinates. Consequently every (A_{i,a}) occupies each (\mu_4)-coset in between (1) and (3) points.

### 3.2 Quadratic lifting kills the first five jets

Choose (\eta\in F_0^\times) of order (256) with

[
\eta^{16}=\zeta=3.
]

Such an (\eta) exists because (F_0^\times) is cyclic and

[
v_2(17^{16}-1)=8.
]

Let

[
K=\langle\eta^8\rangle,\qquad |K|=32.
]

For every base state (A=A_{i,a}), define

[
\widetilde A
============

{x\in K:x^2\in A}.
]

The squaring map (K\to\mu_{16}) has kernel ({\pm1}), so

[
|\widetilde A|=16.
]

Writing

[
E_A(w)=\prod_{y\in A}(1-yw),
]

we have

[
\begin{aligned}
E_{\widetilde A}(z)
&=\prod_{y\in A}\prod_{x^2=y}(1-xz)\
&=\prod_{y\in A}(1-yz^2)\
&=E_A(z^2).
\end{aligned}
]

Because (e_1(A)=e_2(A)=0),

[
E_A(w)\equiv1\pmod{w^3},
]

and therefore

[
E_{\widetilde A}(z)\equiv1\pmod{z^6}.
\tag{3.3}
]

The product is preserved:

[
\prod_{x\in\widetilde A}x
=========================

# \prod_{y\in A}(-y)

\prod_{y\in A}y,
\tag{3.4}
]

because (|A|=8).

### 3.3 The finite product-conditioned packet

Reserve the coset (K), placing only the marker (1) in it. Use the other seven (K)-cosets as independent orientation blocks.

For (t=1,\ldots,7), choose one of the (48) lifted states (\widetilde A_t), and set

[
T={1}\cup\bigcup_{t=1}^7\eta^t\widetilde A_t.
\tag{3.5}
]

Then

[
|T|=1+7\cdot16=113.
]

By (3.3),

[
E_{\eta^t\widetilde A_t}(z)
===========================

E_{\widetilde A_t}(\eta^tz)
\equiv1\pmod{z^6}.
]

Hence

[
E_T(z)
\equiv1-z\pmod{z^6},
]

so every such support satisfies

[
e_1(T)=1,\qquad
e_2(T)=e_3(T)=e_4(T)=e_5(T)=0.
\tag{3.6}
]

If the product exponent of (A_t) is (r_t), then by (3.4),

[
\prod_{x\in\eta^t\widetilde A_t}x
=================================

# \eta^{16t}\zeta^{r_t}

\zeta^{t+r_t}.
]

Since

[
1+2+\cdots+7=28\equiv12\pmod{16},
]

the total product is (1) exactly when

[
r_1+\cdots+r_7\equiv4\pmod{16}.
\tag{3.7}
]

Let

[
S={1,4,7,9,12,15}.
]

Define the exact recurrence

[
c_0(0)=1,\qquad c_0(r)=0\ (r\ne0),
]

[
c_{\ell+1}(r)=\sum_{u\in S}c_\ell(r-u)
\quad\text{in }\mathbb Z/16\mathbb Z.
]

Seven iterations give

[
c_7(4)=25{,}152.
]

For every prescribed color exponent there are exactly (8) underlying base states by (3.1). Consequently the number of supports satisfying (3.7) is

[
\begin{aligned}
|\mathcal P_0|
&=c_7(4),8^7\
&=25{,}152\cdot2{,}097{,}152\
&=52{,}747{,}567{,}104.
\end{aligned}
\tag{3.8}
]

Thus every member of (\mathcal P_0) has the same product and the same five jet coordinates.

### 3.4 No eligible block trade survives

The least dyadic subgroup order at least (\sigma=6) is

[
M_0=8.
]

Inside an oriented (K)-coset, a (\mu_8)-coset corresponds under squaring to a (\mu_4)-coset in (\mu_{16}). By (3.2), its occupancy is therefore one of

[
2,\ 4,\ 6,
]

strictly between (0) and (8).

Inside the reserved (K)-coset, one (\mu_8)-coset contains the marker (1), and the other three are empty. No (\mu_8)-coset is full.

Every subgroup of (H_0) with order at least (6) has dyadic order at least (8) and contains (\mu_8). Every coset of such a subgroup is a union of (\mu_8)-cosets. It therefore cannot be contained in a support from (\mathcal P_0).

Hence every packet support is (6)-block-free.

More strongly, if two packet supports belonged to one fixed-defect full-(K')-block family with (|K'|\ge6), then a nontrivial change between them would fill a complete (K')-coset in one support and empty it in the other. That is impossible because neither support has a full eligible coset. Thus every nontrivial eligible block-trade class meets (\mathcal P_0) in at most one support.

The stabilizer is also trivial. The marker (1) belongs to every support, while (-1), which lies in the reserved (K)-coset, does not. Therefore

[
-T\ne T.
]

Every nontrivial subgroup of the dyadic group (H_0) contains (-1), so no nontrivial subgroup stabilizes (T).

### 3.5 Exact entropy comparison

There are

[
\frac{|H_0|}{M_0}=\frac{256}{8}=32
]

least eligible blocks. But

[
|\mathcal P_0|
=52{,}747{,}567{,}104
=393\cdot2^{27}
=\frac{393}{32},2^{32}

> 2^{32}.
> \tag{3.9}
> ]

Thus its normalized product-conditioned entropy is strictly greater than one bit per eligible block.

The Role-03 residual is even smaller:

[
\binom{32}{16}=601{,}080{,}390
<2^{32}
<|\mathcal P_0|.
\tag{3.10}
]

### 3.6 Tensor replication

Let (R) be a power of two and put

[
F_R=\mathbb F_{17^{16R}}.
]

By LTE,

[
v_2(17^{16R}-1)=8+v_2(R),
]

so (F_R^\times) contains a subgroup

[
H_R=\langle\theta\rangle
]

of order (256R). Choose (\theta) so that

[
\theta^{16R}=3.
]

Let

[
J=\langle\theta^R\rangle,\qquad |J|=256.
]

The packet (\mathcal P_0) is available inside (J). For independently chosen (T_u\in\mathcal P_0), define

[
T=\bigcup_{u=0}^{R-1}\theta^uT_u.
\tag{3.11}
]

The (J)-cosets are disjoint, so

[
|T|=113R,\qquad
|\mathcal P_R|=|\mathcal P_0|^R.
]

For every (T_u\in\mathcal P_0),

[
E_{T_u}(z)\equiv1-z\pmod{z^6},
\qquad
\prod T_u=1.
]

Consequently

[
E_{\theta^uT_u}(z)
\equiv1-\theta^uz\pmod{z^6},
]

and

[
\prod(\theta^uT_u)=\theta^{113u}.
]

Therefore every support in (3.11) has the same model boundary:

[
E_T(z)
\equiv
\prod_{u=0}^{R-1}(1-\theta^uz)
\pmod{z^6},
]

[
\prod T
=======

\theta^{113R(R-1)/2}.
]

Every (\mu_8)-coset lies inside one (J)-coset, so block-freeness and the trivial-stabilizer argument persist.

Thus

[
N_\Delta(b_R)\ge
52{,}747{,}567{,}104^R.
\tag{3.12}
]

The structural block residual has only (32R) blocks and satisfies

[
\binom{32R}{16R}<2^{32R}.
]

Since

[
52{,}747{,}567{,}104>2^{32},
]

the ratio between the collision packet and the block residual grows geometrically as

[
\left(\frac{393}{32}\right)^R.
\tag{3.13}
]

### 3.7 This lies in the stated hard regime

Here (p=17>s=5). The (17)-cyclotomic orbits meeting (1,\ldots,5) modulo (256R) have lengths

[
16R,\quad8R,\quad16R,\quad4R,\quad16R.
]

They are disjoint, so

[
D_5(17,256R)=60R.
\tag{3.14}
]

Therefore

[
|G_{\rm eff}|
=============

256R\cdot17^{60R}.
\tag{3.15}
]

The unconditional rank cap is

[
2^{,256R-60R}=2^{196R},
]

far above the block scale (2^{32R}), so the cyclotomic-rank theorem does not close this case.

Norm rigidity fails already at the dyadic test value (M=4). Indeed,

[
N_M=64R,\qquad
t_M=1,\qquad
A_M=1,\qquad
f_M=4R,
]

while

[
17^{4R}
<
(64R)^{32R}
===========

N_M^{\varphi(N_M)}.
\tag{3.16}
]

Thus this is genuinely outside both prior safe regimes.

The baseline term cannot absorb the tensor family. Since

[
\binom{256R}{113R}\le2^{256R}
]

and (17^4>2^{16}),

[
\frac{\binom{256R}{113R}}{|G_{\rm eff}|}
\le
\frac{2^{256R}}{256R,17^{60R}}
<
\frac{2^{16R}}{256R}.
\tag{3.17}
]

For every fixed (C_6), the term

[
C_6\frac{\binom{256R}{113R}}{|G_{\rm eff}|}
]

has exponential base at most (2^{16}) per tensor copy, while the packet has base (52{,}747{,}567{,}104>2^{32}).

Consequently any inequality of the target form must have

[
\operatorname{collision_residual}(256R,17,6)
\ge
52{,}747{,}567{,}104^R
----------------------

C_6\frac{2^{16R}}{256R}
\tag{3.18}
]

after removing nontrivial full-block trades.

A block-scale, polynomial, or (2^{32R})-scale collision residual is impossible.

### 3.8 Minimal-CI realization

Fix one support (T_0\in\mathcal P_R), and let

[
B=P_{T_0}(X,Z)
==============

\prod_{x\in T_0}(X-xZ).
]

Put

[
A_0=XZ^6.
]

All packet locators have equal product and equal (e_1,\ldots,e_5). Hence for every (T\in\mathcal P_R),

[
P_T-P_{T_0}
]

is divisible by (Z^6), from equality of the infinity jets, and by (X), from equality at (0). Therefore

[
P_T=B+A_0U_T.
\tag{3.19}
]

Moreover,

[
\gcd(A_0,B)=1,
]

because every root of (B) is a finite nonzero point of (H_R).

The complete intersection

[
I=(A_0,B)
]

has degrees

[
7,\quad113R
]

and socle degree

[
7+113R-2=113R+5.
]

Choose a nonzero socle functional of (S/I). The perfect complete-intersection pairing gives a syndrome functional (s) with exact apolar ideal (I_s=I).

Since

[
113R+5<256R,
]

evaluation on (H_R) is injective in this degree, so its evaluation columns span the full dual space and (s) is an actual Reed–Solomon syndrome.

For every packet locator, the coefficient of (B) in (3.19) is (1). Thus the representation is full-coordinate. Equivalently, if one coordinate vanished, deleting its locator factor would give a degree-((113R-1)) form in

[
I_{113R-1}=A_0S_{113R-8},
]

forcing divisibility by (XZ^6), impossible for a locator whose roots are distinct nonzero finite points.

The same argument excludes every (H_R)-supported locator of degree below (113R). Thus the packet lies in the minimal listed stratum.

---

## 4. Parameter ledger

| Quantity                             |                                   Finite packet |              Tensor family |
| ------------------------------------ | ----------------------------------------------: | -------------------------: |
| Characteristic                       |                                            (17) |                       (17) |
| Field                                |                           (\mathbb F_{17^{16}}) |     (\mathbb F_{17^{16R}}) |
| Field size at (R=1)                  | (48{,}661{,}191{,}875{,}666{,}868{,}481<2^{66}) |                          — |
| Domain size                          |                                           (256) |                     (256R) |
| Slack (\sigma)                       |                                             (6) |                        (6) |
| Jet depth                            |                                             (5) |                        (5) |
| Support weight (j)                   |                                           (113) |                     (113R) |
| Redundancy (r)                       |                                           (119) |                   (113R+6) |
| Code dimension (k)                   |                                           (137) |                   (143R-6) |
| CI degrees                           |                                       ((7,113)) |                 ((7,113R)) |
| Least eligible block (M_0)           |                                             (8) |                        (8) |
| Number of (M_0)-blocks               |                                            (32) |                      (32R) |
| Packet size                          |                          (52{,}747{,}567{,}104) |   (52{,}747{,}567{,}104^R) |
| Block residual                       |                (\binom{32}{16}=601{,}080{,}390) | (\binom{32R}{16R}<2^{32R}) |
| (D_5(17,n))                          |                                            (60) |                      (60R) |
| Effective group                      |                               (256\cdot17^{60}) |        (256R\cdot17^{60R}) |
| Rank cap                             |                                       (2^{196}) |                 (2^{196R}) |
| Nontrivial eligible block-trade mass |                           (0) inside the packet |      (0) inside the packet |

For the finite packet,

[
\frac{\binom{256}{113}}{256\cdot17^{60}}<\frac1{17}.
]

The exact verifier is [available here](sandbox:/mnt/data/verify_cycle63_role05_near_split_counterpacket.py).

---

## 5. Bankable versus conditional

### Bankable

* The 48 explicit (\mu_{16}) states and their locator expansions.
* Their common (e_1=e_2=0) jet.
* The exact product-color enumerator
  [
  8\bigl(Y+Y^4+Y^7+Y^9+Y^{12}+Y^{15}\bigr)
  \quad\text{in }\mathbb Z[\mathbb Z/16].
  ]
* The quadratic lifting identity and annihilation of jet degrees (1,\ldots,5).
* The exact count (52{,}747{,}567{,}104).
* Eligible block-freeness and trivial stabilizers.
* The tensor family of size (52{,}747{,}567{,}104^R).
* The hard-regime checks (D_5=60R) and failure of norm rigidity.
* The minimal-CI Reed–Solomon realization.

### Conditional only on terminology

If `block_trade_charge` is defined to charge singleton profiles having no movable full block, it can tautologically charge every support one at a time. Such a definition is not a structural block-trade charge and makes the target inequality vacuous.

Under the nonvacuous interpretation—charging mass compressed into nontrivial full-block families—the packet has zero block-trade mass.

The construction does not rule out an inequality whose collision residual is itself at least (52{,}747{,}567{,}104^R). It proves that such a residual must be exponentially larger than the proposed block scale.

---

## 6. Exact failure point

Full subgroup blocks are not the only tensorable configuration relations.

The missing relation is a **partial-pattern jet collision**:

* each local state partially occupies all four (\mu_4)-cosets;
* all 48 states have the same first two jets;
* quadratic lifting suppresses their differences through jet degree (5);
* no eligible (\mu_8)-block is ever full;
* the six product colors permit a large exact product-conditioned tensor fiber.

Thus a canonical maximal ((K,D)) assignment based only on full (K)-blocks cannot absorb the residual. It leaves exponentially many singleton block profiles inside one model fiber.

---

## 7. Next exact lemma or construction

There is still a route to a full solve, but the charge must be enlarged beyond full blocks.

The next exact wall should be

```text
L-MODEL-GJ-MAXIMAL-PREFIX-COLLISION-GADGET-CHARGE
```

For every divisor subgroup (J\le H), define the finite local equivalence

[
A\equiv_\sigma B
\iff
|A|=|B|
\quad\text{and}\quad
E_A(z)\equiv E_B(z)\pmod{z^\sigma}.
]

Attach to each equivalence class (\mathcal C) its exact product-color enumerator

[
W_{\mathcal C}
==============

\sum_{A\in\mathcal C}
Y^{\log_J(\prod A)}
\in\mathbb Z[J].
]

The next theorem must give a canonical maximal tensor-factor assignment of supports to such local classes, charge the relevant coefficient of the product of their (W_{\mathcal C}), and prove bounded overlap between competing subgroup scales.

Full (K)-block trades are then the simplest special case. The present counterpacket forces the theory to include partial-pattern classes such as the 48-state characteristic-(17) gadget above.
