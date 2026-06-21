BANKABLE_LEMMA

## 1. Executive verdict

**Confidence: high.**

The Cycle84 occupancy transfers with **zero additional multiplicity loss** to a transverse MCA slope packet. The exact normalized slope is not (\rho_\beta(T)) itself but

[
\chi_T=-\rho_\beta(T)^{-1},
]

up to a common affine bijection (z\mapsto az+b), (a\ne0). Hence

[
M_C(6)\ge 52{,}747{,}567{,}092
]

for an explicit research GRS/RS instance.

This does **not** prove equality for the whole MCA numerator, a scalar-list lower bound, frontier movement, or the full prize theorem.

## 2. Exact theorem

### (L)-CYCLE85-EXACT-ROLE05-TRANSVERSE-RECIPROCAL-TRANSFER

Let

[
F_0=\mathbf F_{17}[X]/(X^{16}+X^8+3),\qquad
\eta=6X^9,\qquad
D_0=\langle\eta\rangle=\mu_{256},
]

and let

[
\beta=X+2\notin D_0.
]

For every (T\in\mathcal P_0), write

[
P_T(Y)=\prod_{x\in T}(Y-x),\qquad
\rho_\beta(T)=P_T(\beta).
]

The banked Role05 packet has

[
|T|=j=113,\qquad
e_1(T)=1,\qquad e_2(T)=e_3(T)=e_4(T)=e_5(T)=0.
]

Put

[
\sigma=6,\qquad R=j+\sigma-1=118,\qquad k=256-j-\sigma=137.
]

Define parity-check columns

[
\widehat h_x=
\begin{pmatrix}
1\x\ \vdots\x^{117}\(\beta-x)^{-1}
\end{pmatrix}\in F_0^{119}.
]

Let

[
s=(\underbrace{0,\ldots,0}_{112},
1,1,1,1,1,1)\in F_0^{118},
]

and define the affine syndrome line

[
\ell(z)=u+zv,\qquad
u=(s,0),\qquad
v=(0,\ldots,0,-1).
]

Then, for every (T\in\mathcal P_0),

[
\chi_T=-\rho_\beta(T)^{-1}
]

is a transverse bad parameter of (\ell), witnessed by (T). Moreover,

[
\chi_T=\chi_{T'}
\iff
\rho_\beta(T)=\rho_\beta(T').
]

Consequently,

[
\left|
{\chi_T:T\in\mathcal P_0}
\right|
=======

# \operatorname{Occ}(\beta)

52{,}747{,}567{,}092.
]

Thus the MCA numerator of this code satisfies

[
\boxed{M_C(6)\ge 52{,}747{,}567{,}092.}
]

The exact packet spectrum is inherited unchanged:

[
\begin{aligned}
\text{packet supports}&=52{,}747{,}567{,}104,\
\text{distinct packet slopes}&=52{,}747{,}567{,}092,\
\text{singleton packet-slope fibers}&=52{,}747{,}567{,}080,\
\text{double packet-slope fibers}&=12,\
\text{fibers of size }\ge3&=0,\
D_{\rm offdiag}&=24.
\end{aligned}
]

## 3. Proof

### Common syndrome

For (T\in\mathcal P_0), set

[
c_{T,x}=\frac1{P_T'(x)},\qquad x\in T.
]

Since (T) has distinct elements, every (c_{T,x}\ne0).

Partial fractions give

[
\frac1{P_T(Y)}
==============

\sum_{x\in T}
\frac{1}{P_T'(x)(Y-x)}.
]

Expanding at infinity and comparing coefficients yields

[
\sum_{x\in T}\frac{x^m}{P_T'(x)}
================================

\begin{cases}
0,&0\le m\le111,\
h_{m-112}(T),&m\ge112,
\end{cases}
]

where (h_r(T)) is the (r)-th complete homogeneous symmetric function.

Because

[
e_1(T)=1,\qquad e_2(T)=\cdots=e_5(T)=0,
]

the standard recurrence gives

[
h_0(T)=h_1(T)=\cdots=h_5(T)=1.
]

Therefore, for every (T\in\mathcal P_0),

[
\sum_{x\in T}c_{T,x}(1,x,\ldots,x^{117})^{\mathsf T}=s.
]

All packet supports are thus full-coordinate representations of the same nonzero (t=1) residue syndrome.

### Exact slope

Evaluating the same partial-fraction identity at (Y=\beta) gives

[
\sum_{x\in T}\frac{c_{T,x}}{\beta-x}
====================================

# \frac1{P_T(\beta)}

\rho_\beta(T)^{-1}.
]

Hence

[
\sum_{x\in T}c_{T,x}\widehat h_x
================================

# (s,\rho_\beta(T)^{-1})

\ell!\left(-\rho_\beta(T)^{-1}\right).
]

Thus the reduced Role05 color is exactly

[
\chi_T=-\rho_\beta(T)^{-1}.
]

If the Cycle84 implementation counts normalized products
(\widehat\rho_T) satisfying (\rho_\beta(T)=C\widehat\rho_T) for one fixed
(C\ne0), then

[
\chi_T=-C^{-1}\widehat\rho_T^{-1}.
]

Multiplication by (C), inversion, and nonzero affine rescaling are all bijections, so the public occupancy is preserved exactly.

### The matrix defines a GRS/RS instance

Let (D_\beta=\operatorname{diag}(\beta-x)_{x\in D_0}). Then the rows of

[
\widehat H D_\beta
]

are evaluations of

[
1,\quad (\beta-Y),\quad (\beta-Y)Y,\quad\ldots,\quad
(\beta-Y)Y^{117}.
]

These (119) polynomials form a basis of (F_0[Y]_{\le118}): if

[
a+(\beta-Y)Q(Y)=0,\qquad \deg Q\le117,
]

then evaluation at (Y=\beta) gives (a=0), followed by (Q=0).

Thus (\widehat H) is row- and nonzero-column-equivalent to a degree-(118) Vandermonde parity-check matrix. It therefore defines a GRS code of parameters

[
[256,137].
]

Nonzero column scalings leave every support span (V_T) unchanged; invertible row transformations carry lines and support spans bijectively. Therefore the MCA numerator is the same for the corresponding ordinary RS normalization.

### Transversality and noncontainment

Suppose (v\in V_T). Then for some vector (a=(a_x)_{x\in T}),

[
v=\sum_{x\in T}a_x\widehat h_x.
]

Looking at the first (118) coordinates gives

[
\sum_{x\in T}a_x(1,x,\ldots,x^{117})^{\mathsf T}=0.
]

The (118\times113) Vandermonde submatrix on (T) has full column rank, so (a=0), contradicting (v\ne0). Hence

[
v\notin V_T
]

for every packet support. Every incidence above is transverse and is counted by the official MCA definition.

### No further collapse

For a fixed (T), the vector (c_T) is unique because the Vandermonde submatrix has full column rank. Thus one witness cannot generate multiple line parameters.

For two supports,

[
\chi_T=\chi_{T'}
\iff
-\rho_\beta(T)^{-1}=-\rho_\beta(T')^{-1}
\iff
\rho_\beta(T)=\rho_\beta(T').
]

Thus the only same-slope collisions are exactly the twelve double product fibers already recorded by Cycle84.

If two support spans coincide, a transverse affine line can meet that common span at only one parameter. Therefore coincident spans cannot identify two distinct occupied products.

Changing the augmented parity row by

[
\lambda\longmapsto a\lambda+\varphi H,\qquad a\ne0,
]

changes the packet parameter by

[
\chi_T\longmapsto a\chi_T-\varphi(s),
]

a common affine bijection. Affine color normalization causes no loss.

Quotient or periodic structure can classify these witnesses inside an upper-bound decomposition, but it cannot identify two distinct elements of the literal bad-parameter set in (F_{\rm line}).

## 4. Field and frontier interpretation

For the original model,

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481.
]

Therefore

[
T_{\rm line}
============

\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor
=0.
]

So

[
\operatorname{Occ}(\beta)>2^{32}
]

is **not** the native prize comparison. It is only a research benchmark. The native original-field comparison is merely (M_C(6)>0).

Also,

[
\frac{k}{n}=\frac{137}{256},
]

which is not one of the official rates listed in `RS-PRIZE-FRONTIER-V1`. Thus the original instance is a finite/model MCA certificate, not an official ledger packet.

### Exact rate-(\tfrac12) shortening

There is nevertheless an exact profile-compatible shortening.

Let

[
K=\langle\eta^8\rangle,\qquad |K|=32.
]

Every Role05 support has the form

[
T={1}\cup\bigcup_{t=1}^7\eta^t\widetilde A_t,
\qquad \widetilde A_t\subseteq K.
]

Hence every (T\in\mathcal P_0) avoids (K\setminus{1}). Choose

[
S={\eta^{8a}:1\le a\le18}\subset K\setminus{1},
\qquad
D_*=D_0\setminus S.
]

Then

[
|D_*|=238
]

and every packet support survives. Restricting the parity-check matrix to (D_*) gives a code of dimension

[
k_*=238-119=119,
]

so

[
\frac{k_*}{n_*}=\frac{119}{238}=\frac12,
\qquad
j=113,\qquad
\sigma=119-113=6.
]

Scalar-extending to

[
F_{\rm code}=F_{\rm line}=\mathbf F_{17^{32}}
]

preserves all distinct products and all rank/transversality statements. Here

[
T_{\rm line}
============

\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor
=6,
]

so the packet gives

[
M_C(6)\ge52{,}747{,}567{,}092>6.
]

This is an exact official-profile-compatible `FAIL` row under the attached v1 rules, but it is **frontier-redundant**: the core tangent bound already gives

[
M_C(6)\ge j=113>6.
]

It therefore does not move the failure frontier.

### Exact one-copy scalar-extension route cut

Every finite field containing (F_0=\mathbf F_{17^{16}}) has order (17^{16m}). Under the official strict cap (q_{\rm line}<2^{256}), only

[
m=1,2,3
]

are possible. Their targets are

[
\begin{array}{c|c}
q_{\rm line}&T_{\rm line}\ \hline
17^{16}&0\
17^{32}&6\
17^{48}&338{,}617{,}018{,}271{,}848{,}945{,}628.
\end{array}
]

For degrees (16) and (32), the tangent lower bound (j\ge113) already dominates. For degree (48),

[
52{,}747{,}567{,}092
<
338{,}617{,}018{,}271{,}848{,}945{,}628,
]

so one copy does not cross the target.

Therefore:

[
\boxed{\text{No direct one-copy scalar extension of this packet can move the official MCA frontier.}}
]

## 5. Verification requirements

The exact finite producer should be:

```text
V-CYCLE85-ROLE05-TRANSVERSE-RECIPROCAL-PACKET
```

It must bind the Cycle84 product certificate to the same support family and verify:

1. every enumerated state is a (113)-subset of (\mu_{256});
2. every support has (e_1=1) and (e_2=\cdots=e_5=0);
3. (\beta\notin\mu_{256});
4. the product counted by Cycle84 differs from (P_T(\beta)) only by the declared fixed nonzero scalar;
5. all supports avoid (K\setminus{1});
6. the syndrome is (s=(0^{112},1^6));
7. the slope transform is (z=-1/\rho);
8. transversality is certified by the (118\times113) Vandermonde rank argument;
9. the field, shortening, embedding, domain digest, code fingerprint, reserve and denominator are bound to the lower term.

The resulting lower-term entry should have the form

```text
theorem_id: L-CYCLE85-EXACT-ROLE05-TRANSVERSE-RECIPROCAL-TRANSFER
term_type: packet.explicit_mca_slope_set
objective: mca
direction: lower
sigma: 6
bound: 52747567092
q_gen: 17^16
q_line: 17^32
q_code: 17^32
T_line: 6
transversality: VERIFIED
contained_incidences: 0
slope_map: z = -1/rho
```

Its expected leave-one-out classification is:

```text
SUBFRONTIER_REDUNDANT
```

not `MOVES_FAILURE_FRONTIER`.

## 6. Next exact lemma

The arithmetic shows why two copies are the first plausible nonredundant scale:

[
\operatorname{Occ}(\beta)^2
===========================

2{,}782{,}305{,}834{,}125{,}041{,}336{,}464

>

# T_{17^{48}}

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

The next mathematical target is therefore:

```text
L-CYCLE86-TWO-COPY-RS-TRANSVERSE-SLOPE-PACKING
```

Exact required statement:

There exist an ([476,238]) GRS/RS code over (F_{17^{48}}), a syndrome line (\ell), two disjoint embeddings of the shortened Role05 support packet, and an element (\theta\in F_{17^{48}}\setminus F_{17^{16}}), such that every ordered pair ((T_1,T_2)\in\mathcal P_0^2) gives a transverse witness of support size (226) at slope

[
z(T_1,T_2)
==========

-\rho_\beta(T_1)^{-1}
-\theta\rho_\beta(T_2)^{-1}.
]

Because (1,\theta) are linearly independent over (F_{17^{16}}), this slope map is injective on occupied-product pairs. The consequence would be

[
M_C(12)\ge\operatorname{Occ}(\beta)^2>T_{17^{48}},
]

with

[
n=476,\quad k=238,\quad \sigma=12,\quad j=226,\quad k/n=1/2.
]

The naive disjoint-union construction does not already prove this: a (j=226,\sigma=12) barycentric packet needs eleven common leading elementary coefficients, while each Role05 copy fixes only five. The first uncontrolled coefficient is the sixth. A valid proof must provide a jet-separating RS realization; a valid counterpacket should exhibit why such a realization is impossible.

## Self-audit

1. **Exact implication proved:** distinct occupied (P_T(\beta)) values give exactly the same number of distinct transverse MCA parameters via (z=-P_T(\beta)^{-1}). Hence (M_C(6)\ge52{,}747{,}567{,}092).

   **Not proved:** (M_C(6)=52{,}747{,}567{,}092), any scalar-list numerator statement, frontier movement, or the full prize theorem.

2. The original (n=256) result is a finite/model MCA certificate. The shortened (n=238), (F_{17^{32}}) construction is official-profile-compatible under the attached v1 rules, but it is tangent-redundant and still needs a registry/checker artifact.

3. The first line where the certified reduction can fail is the binding assertion that the exact (\mathcal P_0) enumerated in Cycle84 is the same support family with
   [
   e_1=1,\quad e_2=\cdots=e_5=0
   ]
   and the stated coset support realization. Once that line is certified, the slope transfer is formal.

4. `q_line`, not `q_code`, is the native MCA denominator. In the original field (T_{\rm line}=0); in the quadratic extension it is (6); in degree (48) it is (338{,}617{,}018{,}271{,}848{,}945{,}628). `q_gen` is (17^{16}). `q_chal` pays none of these bills. The comparison with (2^{32}) is not a native (2^{-128}) comparison.

5. Quotient/periodic structure cannot reduce the literal slope set. Contained incidences are absent. Same-slope collisions are exactly the twelve Cycle84 double product fibers. Affine color normalization is bijective. No further numerator loss occurs.

6. This is not merely a plan. Promotion to a certified ledger term requires the exact checker `V-CYCLE85-ROLE05-TRANSVERSE-RECIPROCAL-PACKET`. The next unresolved mathematical theorem is the two-copy RS slope-packing lemma stated above.
