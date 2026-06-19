## VERDICT

**Repository status: AUDIT**

**Confidence: high.**

A balanced (t=\sigma) upper theorem does **not** by itself imply the full scalar MCA upper theorem.

There are two distinct interpretations of “balanced theorem”:

1. An **unrestricted numerical theorem** for every degree-(\sigma) datum, including data obtained by padding lower denominators, automatically controls all (t\le \sigma).
2. A theorem only for **primitive/reduced balanced data**, with low-denominator descent listed as an exceptional template, controls only the genuinely balanced stratum. The exceptional (t<\sigma) data still need a separate theorem.

Neither interpretation controls primitive (t>\sigma) data. Those data produce support-dependent positive-dimensional affine planes in the residue algebra, not the fixed point cloud occurring at (t=\sigma). Moreover, active high-degree directions of minimal denominator (\sigma+1) exist in the official fixed-rate regime and admit no compression to degree (\le\sigma).

Thus the proposed assembly

[
\text{balanced upper}+\text{residual list}\Longrightarrow\text{full scalar MCA upper}
]

is incomplete in two places:

[
\boxed{\text{residual-unsafe }t<\sigma}
\qquad\text{and}\qquad
\boxed{t>\sigma}.
]

The second is the fundamental missing branch.

---

## ALL_DENOMINATOR_LEDGER

Let

[
D\subset F,\qquad |D|=n,\qquad C=\operatorname{RS}[F,D,k],
]

and fix target agreement

[
a=k+\sigma,\qquad r=n-k,\qquad j=n-a=r-\sigma.
]

For a degree-(t) residue datum write

[
E\in F[X],\quad \deg E=t,\quad E|*D\ne0,
]
[
B*{\rm num}\in F[X]_{<t},\qquad w:D\to F.
]

Write

[
A_E:=F[X]/(E),\qquad \overline P=[P]_E.
]

A witness for slope (z) consists of (Q_z\in F[X]_{<k+t}) and a support of size at least (a) satisfying

[
Q_z=w\text{ on }S_z,\qquad \overline{Q_z}=z\overline{B_{\rm num}}.
]

The source normal form gives, when the scalar slope field is (F),

[
q_{\rm line},\varepsilon_{\rm MCA}(C,1-a/n)
===========================================

\max_{1\le t\le r}\Lambda^{\rm NC}*{t,1-a/n}(D,k),
\qquad q*{\rm line}=|F|.
]

No (q_{\rm gen}) entropy statement is involved in this identity. The generated field enters only when bounding particular strata.

### BANKABLE_LEMMA — exact-support reduction

Every noncontained witness on a support (T) of size at least (a) has a noncontained restriction to some (a)-subset (S\subseteq T).

### PROOF

Suppose instead that every (a)-subset (S\subseteq T) is contained. Thus for every such (S) there are (A_S,G_S\in F[X]*{<k}) explaining (w/E) and (-B*{\rm num}/E) on (S).

Adjacent (a)-subsets in the Johnson graph differ in one point and intersect in

[
a-1=k+\sigma-1\ge k
]

points. Hence (A_S-A_{S'}) and (G_S-G_{S'}), each of degree (<k), have at least (k) roots and are zero. Connectivity of the Johnson graph gives one common pair (A,G) explaining both words on all of (T), contradicting noncontainment. ∎

Consequently all three strata can be analyzed using supports of size exactly (a).

### BANKABLE_LEMMA — zero numerator contributes no noncontained witnesses

If (B_{\rm num}=0), then every witness is contained.

Indeed, (Q\equiv0\pmod E) gives (Q=EP) for some (P\in F[X]_{<k}). On the support,

[
P=w/E,
]

while (G=0) explains the direction. Hence one may assume

[
B_{\rm num}\ne0.
]

### AUDIT — raw denominator degree is not intrinsic

On a multiplicative domain, the raw degree (t) can always be padded upward.

Let (d\ge0), (t+d\le r), and take (H=X^d), which is nonzero on (D\subset F^\times). Define

[
E'=EH,\qquad B'*{\rm num}=B*{\rm num}H,\qquad w'=Hw,\qquad Q'_z=HQ_z.
]

Then

[
\deg E'=t+d,\qquad \deg Q'_z<k+t+d,
]
[
Q'*z\equiv zB'*{\rm num}\pmod{E'},
\qquad Q'_z=w'\text{ on }S_z.
]

Moreover,

[
\frac{w'}{E'}=\frac wE,\qquad
-\frac{B'*{\rm num}}{E'}=-\frac{B*{\rm num}}E,
]

so containment and noncontainment are unchanged. Therefore, for unrestricted data,

[
\Lambda_t^{\rm NC}\le \Lambda_{t+d}^{\rm NC}.
]

In particular,

[
\max_{t\le\sigma}\Lambda_t^{\rm NC}=\Lambda_\sigma^{\rm NC},
\qquad
\max_{t\le r}\Lambda_t^{\rm NC}=\Lambda_r^{\rm NC}.
]

Thus the three-stratum ledger is meaningful only after passing to a **minimal or descended denominator degree**, not merely the displayed degree of a padded datum.

Conversely, a common factor can be cancelled. If

[
E=HE_0,\qquad B_{\rm num}=HB_0,
]

then every witness (Q_z) is divisible by (H), because both (Q_z-zB_{\rm num}) and (zB_{\rm num}) are divisible by (H). Dividing (E,B_{\rm num},Q_z) by (H), and dividing (w) pointwise by (H|_D), preserves all witnessed slopes and noncontainment.

The intrinsic degree is more accurately

[
\tau(g):=
\min\left{
t:
g=R-\frac{B_{\rm num}}E\text{ on }D,\
\deg R<k,\ \deg E=t,\ \deg B_{\rm num}<t
\right},
]

where (g) is the line direction word. The three strata should be interpreted as (\tau(g)<\sigma), (\tau(g)=\sigma), and (\tau(g)>\sigma).

The exact interpolation ledger is then:

| Stratum             | Interpolation object on (S)                | Remaining problem                                     |
| ------------------- | ------------------------------------------ | ----------------------------------------------------- |
| (t<\sigma)          | one polynomial (Q=I_S(w)) of degree (<k+t) | actual shifted-dimension RS list or sliced-list bound |
| (t=\sigma)          | one residue point ([I_S(w)]_E)             | balanced fixed-line/point-cloud incidence             |
| (t=\sigma+h>\sigma) | an affine (h)-plane                        | support-dependent transverse line-plane incidence     |

---

## T_LESS_SIGMA

Let (t<\sigma). Put

[
s_t:=\sigma-t>0.
]

### BANKABLE_LEMMA — residual-list injection

For every degree-(t) datum with (B_{\rm num}\ne0),

[
#{\text{noncontained bad slopes}}
\le
\mathsf L_F(D;k+t,a),
]

where

[
\mathsf L_F(D;k+t,a)
:=
\max_{w:D\to F}
\left|
\left{
Q\in F[X]_{<k+t}:
|{x\in D:Q(x)=w(x)}|\ge a
\right}
\right|.
]

Thus the relevant code is

[
\operatorname{RS}[F,D,k+t]
]

and its residual agreement surplus is

[
a-(k+t)=\sigma-t=s_t.
]

### PROOF

Choose one witness polynomial (Q_z) for every bad slope (z). Every (Q_z) is a listed polynomial for the received word (w) in dimension (k+t).

If two slopes (z,z') had the same selected polynomial, then

[
(z-z')B_{\rm num}\equiv0\pmod E.
]

Since (\deg B_{\rm num}<\deg E) and (B_{\rm num}\ne0), its residue class is nonzero. Hence (z=z'). The map (z\mapsto Q_z) is injective. ∎

For (t\le\sigma), noncontainment is in fact automatic once (B_{\rm num}\ne0). If a degree-(<k) polynomial (G) explained the direction on a support of size (a), then

[
EG+B_{\rm num}
]

would have (a) roots but degree (<k+t\le a). It would therefore be zero, forcing (E\mid B_{\rm num}), impossible.

### The actual list theorem still needed

The sufficient theorem is a bound on **distinct listed polynomials**:

[
\mathsf L_F(D;k+t,a)\le N_t.
]

A raw support-fiber theorem is not the required object.

If (D\subset B_0\subseteq F), where (B_0) is the generated field of size (q_{\rm gen}), and (F/B_0) has extension degree (e), then the required statement is either:

* a direct list theorem for (\operatorname{RS}[F,D,k+t]), or
* an (e)-interleaved, common-support list theorem over (B_0).

A scalar base-field list theorem does not automatically control an arbitrary (F)-valued word.

The theorem must also be evaluated at the shifted dimension (k+t). In particular, the active quotient profile is the profile for

[
(D,k+t,a),
]

not necessarily the profile for ((D,k,a)).

### ROUTE_CUT — the original entropy reserve does not transfer

The residual list theorem has its own entropy bill:

[
(\sigma-t)\log_2q_{\rm gen}
\quad\text{versus}\quad
\log_2\binom na.
]

This is not paid by merely knowing

[
\sigma\log_2q_{\rm gen}

>

\log_2\binom na.
]

Indeed, define the original and residual entropy margins

[
\Gamma_0
:=
\sigma\log_2q_{\rm gen}-\log_2\binom na,
]

[
\Gamma_t
:=
(\sigma-t)\log_2q_{\rm gen}-\log_2\binom na.
]

Then exactly

[
\Gamma_t=\Gamma_0-t\log_2q_{\rm gen}.
]

Even a positive (\Gamma_0) can become strongly negative for modest (t).

This is not merely a weakness of existing techniques. There is an exact list lower bound

[
\mathsf L_F(D;k+t,a)
\ge
\left\lceil
\frac{\binom na}{q_{\rm gen}^{,\sigma-t}}
\right\rceil.
]

To prove it, map every (a)-subset (S) to the first (s_t=\sigma-t) nonleading coefficients of its locator (L_S). These coefficients lie in (B_0^{s_t}). A fiber has size at least (\binom na/q_{\rm gen}^{s_t}). Fixing its common prefix and subtracting each (L_S) from the corresponding monic degree-(a) polynomial produces distinct degree-(<k+t) codewords agreeing with one received word on (S).

Therefore, a polynomial-size list theorem requires at least

[
(\sigma-t)\log_2q_{\rm gen}
\ge
\log_2\binom na-(1+o(1))\log_2n.
]

The list route can control only the residual-safe range

[
\mathcal T_{\rm list}
=====================

\left{
t<\sigma:
\sigma-t
\text{ clears residual entropy, local-limit, and shifted quotient reserve}
\right}.
]

It cannot control all (t<\sigma) near the entropy boundary.

### COUNTERPACKET — raw support fibers are the wrong theorem

Take (w) itself to be a polynomial of degree (<k+t). Since (t<\sigma), any other degree-(<k+t) polynomial agreeing with (w) on (a>k+t) points must equal (w). Thus the actual list has size one.

Nevertheless every (a)-subset of (D) is a feasible agreement support, so the raw support fiber has size

[
\binom na.
]

Hence no uniform polynomial upper bound on raw feasible (a)-subsets can substitute for the actual list theorem.

### Exactly how balanced upper can cover (t<\sigma)

If the balanced theorem is a numerical theorem for **all** degree-(\sigma) data, lower denominators are already included by padding:

[
(E,B_{\rm num},w,Q)
\longmapsto
(EX^{\sigma-t},B_{\rm num}X^{\sigma-t},
X^{\sigma-t}w,X^{\sigma-t}Q).
]

Thus such an unrestricted balanced theorem would make the residual-list branch unnecessary for the MCA numerator.

But if the balanced theorem excludes common-factor or low-denominator descendants as a template, this padding lands exactly in the excluded branch. Then:

* residual-safe (t) can be handled by the actual list theorem;
* residual-unsafe (t<\sigma) still need a one-dimensional residue-sliced list theorem

[
\left|
\left{
z:
\exists Q\in F[X]_{<k+t},
\operatorname{agr}(Q,w)\ge a,
[Q]*E=z[B*{\rm num}]_E
\right}
\right|
\le n^{1+o(1)}+\text{template terms}.
]

A full list-size theorem is impossible in much of this range, but this sliced statement might still hold.

---

## T_EQUALS_SIGMA

Let (t=\sigma). For every (a)-subset (S), let (I_S(w)) be the unique polynomial of degree (<a) interpolating (w) on (S).

Since

[
k+t=k+\sigma=a,
]

any witness polynomial has degree (<a), and hence must be exactly

[
Q_z=I_S(w).
]

Therefore the support (S) witnesses slope (z) exactly when

[
[I_S(w)]*E=z[B*{\rm num}]_E.
]

Since (B_{\rm num}\ne0), the map (z\mapsto z[B_{\rm num}]_E) is injective.

### BANKABLE_LEMMA — balanced point-cloud identity

The balanced bad-slope set is precisely

[
Z_\sigma(E,B_{\rm num},w)
=========================

\left{
z\in F:
\exists S\in\binom Da,
[I_S(w)]*E=z[B*{\rm num}]_E
\right}.
]

Every such witness is automatically noncontained by the root-count argument above.

Thus a balanced upper theorem controls exactly the intersection of the fixed residue line

[
\ell_{B_{\rm num}}
==================

F[B_{\rm num}]_E
\subset A_E
]

with the arbitrary-anchor residue cloud

[
\mathcal C_E(w)
===============

\left{
[I_S(w)]_E:
S\in\binom Da
\right}.
]

It does **not** control any positive-dimensional interpolation freedom. That freedom begins immediately at (t=\sigma+1).

As noted above, an unrestricted numerical balanced theorem also controls all intrinsic degrees (t<\sigma) through padding. A primitive balanced theorem controls only the (\tau(g)=\sigma) stratum.

---

## T_GREATER_SIGMA

Write

[
t=\sigma+h,\qquad 1\le h\le j.
]

Fix an (a)-subset (S), its locator

[
L_S(X)=\prod_{x\in S}(X-x),
]

and its interpolation polynomial (I_S(w)\in F[X]_{<a}).

### BANKABLE_LEMMA — exact affine-plane normal form

The polynomials (Q\in F[X]_{<k+t}) agreeing with (w) on (S) are exactly

[
I_S(w)+L_SF[X]_{<h}.
]

Consequently (S) supports slope (z) exactly when

[
z[B_{\rm num}]_E
\in
[I_S(w)]*E+[L_SF[X]*{<h}]_E.
]

This is the requested affine-plane incidence

[
z[B_{\rm num}]_E
\in
[I_S(w)]*E+[L_SF[X]*{<t-\sigma}]_E.
]

### PROOF

If (Q=w=I_S(w)) on (S), then (L_S\mid Q-I_S(w)). Since

[
\deg Q<k+t=a+h,
]

the quotient has degree (<h). The converse is immediate. Reducing modulo (E) gives the incidence equation. ∎

Set

[
i_S=[I_S(w)]*E,\qquad
b=[B*{\rm num}]_E,
]

and

[
V_S:=[L_SF[X]_{<h}]_E\subset A_E.
]

Because (E) has no root in (S),

[
\gcd(E,L_S)=1,
]

so ([L_S]_E) is a unit. Multiplication by ([L_S]*E) is injective, and the natural map (F[X]*{<h}\to A_E) is injective because (h<t). Therefore

[
\dim_FV_S=h.
]

Thus (i_S+V_S) is an affine (h)-plane in the (t)-dimensional residue algebra (A_E), of codimension

[
t-h=\sigma.
]

### BANKABLE_LEMMA — contained is exactly nontransverse

For a fixed (S), the following are equivalent:

1. (S) is contained;
2. (i_S\in V_S) and (b\in V_S);
3. the entire line (Fb) is contained in the affine plane (i_S+V_S).

### PROOF

An anchor explanation (A\in F[X]_{<k}) satisfies

[
EA=I_S(w)\quad\text{on }S.
]

Hence

[
EA-I_S(w)=L_SR
]

for some (R\in F[X]_{<h}), which implies (i_S\in V_S). Conversely, if (i_S=[L_SR]_E), then

[
A=\frac{I_S(w)-L_SR}{E}
]

has degree (<k) and explains (w/E) on (S).

Similarly, a direction explanation (G\in F[X]_{<k}) satisfies

[
EG+B_{\rm num}=0\quad\text{on }S,
]

and hence (b\in V_S). Conversely, if (b=[L_SR]_E), then

[
G=\frac{L_SR-B_{\rm num}}E
]

has degree (<k) and explains (-B_{\rm num}/E) on (S).

The equivalence with line containment is now immediate. ∎

It follows that a noncontained incidence occurs exactly when

[
b\notin V_S
]

and

[
Fb\cap(i_S+V_S)\ne\varnothing.
]

In that case the intersection consists of exactly one point. Thus every support contributes at most one noncontained slope, and all noncontained intersections are transverse.

Equivalently, with the quotient map

[
\pi_S:A_E\to A_E/V_S,
]

whose target has dimension (\sigma), a noncontained slope satisfies

[
\pi_S(i_S)=z,\pi_S(b),
\qquad
\pi_S(b)\ne0.
]

This resembles the balanced equation, but the quotient (\pi_S) depends on (S).

### Fixed-quotient, moving-direction form

Multiplication by ([L_S]_E^{-1}) sends (V_S) to the fixed subspace

[
U_h=[F[X]_{<h}]_E.
]

Let

[
\pi_h:A_E\to A_E/U_h.
]

Then the incidence is equivalently

[
\pi_h!\left([L_S]_E^{-1}i_S\right)
==================================

z,
\pi_h!\left([L_S]_E^{-1}b\right),
]

with

[
\pi_h!\left([L_S]_E^{-1}b\right)\ne0.
]

The quotient now has fixed dimension (\sigma), but both the point and the line direction move with (S). Balanced (t=\sigma) controls a fixed direction (b); it gives no bound for this moving-direction family.

Choosing a basis (\lambda_{S,1},\ldots,\lambda_{S,\sigma}) of the annihilator of (V_S), the support condition is the determinantal system

[
\lambda_{S,p}(i_S)\lambda_{S,q}(b)
----------------------------------

\lambda_{S,q}(i_S)\lambda_{S,p}(b)
=0
]

for all (p,q), with at least one (\lambda_{S,p}(b)\ne0). This is the exact high-(t) determinantal incidence object.

### ROUTE_CUT — this is not a polynomial residue quotient

One might try to regard (A_E/V_S) as a degree-(\sigma) residue algebra and invoke the balanced theorem. This fails algebraically.

Since (h\ge1), (V_S) contains ([L_S]_E), which is a unit. But

[
\dim V_S=h<t,
]

so (V_S\ne A_E). A proper ideal cannot contain a unit. Hence (V_S) is not an ideal, and (A_E/V_S) is only a vector-space quotient, not a ring quotient (F[X]/(E')).

Thus there is no support-independent degree-(\sigma) denominator obtained by quotienting (E).

### ROUTE_CUT — ordinary list decoding is impossible here

For each fixed support (S), the affine family

[
I_S(w)+L_SF[X]_{<h}
]

contains exactly (q_{\rm line}^{,h}) distinct polynomials of degree (<k+t), all agreeing with (w) on (S). Therefore the ordinary shifted-dimension list size is at least

[
q_{\rm line}^{,t-\sigma}.
]

The high-(t) branch can only be controlled by transverse incidence geometry, not by ordinary list decoding.

### ROUTE_CUT — no general denominator compression

Take the official fixed-rate regime and suppose

[
2\sigma+1\le r=n-k.
]

This holds eventually at every official rate

[
\rho\in{1/2,1/4,1/8,1/16}
]

when (\sigma=O(n/\log n)).

Set

[
t=\sigma+1
]

and, on a multiplicative domain (D\subset F^\times), take

[
E=X^t,\qquad g(x)=-\frac1{E(x)}=-x^{-t}.
]

This direction has a degree-(t) representation with (B_{\rm num}=1).

Suppose it admitted a representation of degree (t'\le\sigma):

[
-\frac1E=R-\frac{B'}{E'}
\quad\text{on }D,
]

where

[
\deg R<k,\qquad \deg E'=t',\qquad \deg B'<t'.
]

Then

[
REE'-B'E+E'
]

vanishes on all (n) points of (D). Its degree is strictly less than

[
k+t+t'\le k+r=n,
]

so it is the zero polynomial. Reducing this identity modulo (E) gives

[
E'\equiv0\pmod E.
]

But (\deg E'<\deg E), a contradiction. Therefore

[
\tau(g)=\sigma+1>\sigma.
]

This direction is also active. It is not a codeword. Hence it cannot be explained on every (a)-subset: otherwise the explanations on adjacent (a)-subsets, whose intersections have size at least (k), would all coincide and give a global degree-(<k) explanation. Choose an (a)-subset (S) on which (g) is not explained. Then the line

[
f=0,\qquad g=-1/E
]

has a noncontained witness at (z=0), with

[
w=0,\qquad Q_0=0.
]

Thus even **active** (t>\sigma) data need not compress to (t'\le\sigma).

This refutes every blanket denominator-compression lemma. It does not refute a much stronger statement saying that **many** transverse slopes force descent; such a statement would itself be the required high-(t) inverse theorem.

---

## ASSEMBLY_OR_ROUTE_CUT

### PROOF — corrected conditional assembly

Let

[
N_{<}:=
\max_{1\le t<\sigma}
\sup_{(E,B_{\rm num},w)}
|Z_t(E,B_{\rm num},w)|,
]

[
N_{=}:=
\sup_{\deg E=\sigma}
|Z_\sigma(E,B_{\rm num},w)|,
]

and

[
N_{>}:=
\max_{\sigma<t\le r}
\sup_{(E,B_{\rm num},w)}
|Z_t(E,B_{\rm num},w)|.
]

Then the exact normal form gives

[
\varepsilon_{\rm MCA}(C,1-a/n)
==============================

\frac{\max{N_<,N_=,N_>}}{q_{\rm line}}.
]

Consequently a full theorem follows from:

[
N_<\le N_{\rm low},
\qquad
N_=\le N_{\rm bal},
\qquad
N_>\le N_{\rm high},
]

with conclusion

[
\varepsilon_{\rm MCA}(C,1-a/n)
\le
\frac{\max{N_{\rm low},N_{\rm bal},N_{\rm high}}}
{q_{\rm line}}.
]

Each (N_\bullet) must already include any allowed quotient, tangent, common-envelope, or other template term.

The corrected branch assembly is therefore:

1. **Residual-safe (t<\sigma):** use the actual list theorem for (\operatorname{RS}[F,D,k+t]), paying the (q_{\rm gen}) entropy and shifted quotient bills at residual slack (\sigma-t).
2. **Residual-unsafe (t<\sigma):** use an unrestricted balanced theorem through padding, or prove a separate low-denominator residue-sliced list theorem.
3. **(t=\sigma):** use the balanced arbitrary-anchor fixed-line/point-cloud inverse theorem.
4. **Primitive (t>\sigma):** use a uniform transverse affine-plane inverse theorem, or bypass denominators with the syndrome transverse-secant theorem.

If the balanced theorem is unrestricted and numerical, then

[
N_<\le N_=
]

by padding, so only the balanced and high branches remain.

If the balanced theorem excludes descended data, ordinary residual lists do not fill the resulting low-degree gap near (t=\sigma).

### ROUTE_CUT

The statement

[
\text{balanced theorem}+\text{residual list theorem}
\Longrightarrow
\text{full scalar MCA theorem}
]

is false as a theorem assembly unless it explicitly includes:

* a treatment of residual-unsafe (t<\sigma), and
* a primitive (t>\sigma) transverse incidence theorem.

The (t>\sigma) omission cannot be repaired by a formal denominator compression.

The field ledger remains separate:

[
q_{\rm gen}
\quad\text{pays locator/list entropy},
]

[
q_{\rm line}
\quad\text{divides the bad-slope numerator},
]

and (q_{\rm chal}) does not enter unless a protocol theorem identifies it with the actual line-sampling field. No (q_{\rm line})-to-(q_{\rm gen}) transfer has been proved here.

---

## EXACT_NEW_WALL

### EXACT_NEW_WALL — high-denominator transverse affine-plane inverse

For every official fixed rate, every corrected-reserve smooth domain, every

[
1\le h\le j,\qquad t=\sigma+h,
]

and every primitive degree-(t) datum, define

[
V_S=[L_SF[X]_{<h}]_E
]

and

[
\mathcal Z_h(E,B_{\rm num},w)
=============================

\left{
z\in F:
\exists S\in\binom Da,
[B_{\rm num}]_E\notin V_S,
[I_S(w)]*E-z[B*{\rm num}]_E\in V_S
\right}.
]

Prove, after quotient/tangent/common-envelope templates are separated,

[
|\mathcal Z_h(E,B_{\rm num},w)|
\le n^{1+o(1)}
]

uniformly over every (h\in[1,j]).

Equivalently, in the fixed quotient

[
W_h=A_E/[F[X]_{<h}]_E,
]

prove that the number of distinct scalars (z) for which

[
\pi_h([L_S]_E^{-1}[I_S(w)]_E)
=============================

z,
\pi_h([L_S]*E^{-1}[B*{\rm num}]_E)
\ne0
]

for some (S) is at most (n^{1+o(1)}), unless the moving projective directions and supports form an explicit template.

### Coordinate-free exact replacement

Let (H_{\rm RS}) be a parity-check matrix for (C), let (s(y)=H_{\rm RS}y) be the syndrome, and for (T\subseteq D), (|T|=j), let

[
W_T=\operatorname{span}{H_{\rm RS}(:,x):x\in T}.
]

A word (y) agrees with a codeword on (D\setminus T) exactly when

[
s(y)\in W_T.
]

For a line (f+zg), put

[
\ell(z)=s(f)+zs(g).
]

Then a noncontained bad slope is exactly a transverse incidence

[
\ell(z)\in W_T,
\qquad
\ell\not\subseteq W_T.
]

Therefore the single all-denominator theorem needed is precisely:

[
\boxed{
#\left{
z:
\exists T\in\binom Dj,
\ell(z)\in W_T,
\ell\not\subseteq W_T
\right}
\le
n^{1+o(1)}+\text{explicit template terms}.
}
]

This is the coordinate-free form of

[
\texttt{W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE}.
]

It genuinely covers all (t), unlike a balanced residue-cloud theorem.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction? **Yes. The next exact lemma is the uniform high-(t) transverse affine-plane inverse above—preferably proved directly in its syndrome (j)-column secant form. If the balanced theorem excludes descended data, it must be paired with the residual-unsafe low-denominator residue-sliced list bound as a second assembly lemma.**
