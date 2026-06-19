## VERDICT

**Repository status: COUNTEREXAMPLE**

**Confidence: high.**

The requested literal compression

[
t>\sigma,\ \text{many slopes}
\quad\Longrightarrow\quad
\text{an equivalent residue datum of degree }t'\le \sigma
]

is false without substantially stronger safe-side hypotheses. There is, however, an exact compression to a (\sigma)-dimensional quotient, canonically identified with the Reed–Solomon syndrome quotient. That is the maximal unconditional compression.

Two conclusions follow.

1. **PROOF:** high-denominator thick residues introduce no new invariant incidence object: support by support, they are exactly the syndrome transverse-secant problem in codimension (\sigma).

2. **COUNTERPACKET:** they do introduce genuinely minimal denominator directions with (t>\sigma), including reduced, aperiodic, official-rate data with very large slope clouds. Thus one cannot replace the syndrome theorem by a theorem proved only for denominators (t\le \sigma).

The final corrected-reserve asymptotic upper theorem is not refuted. The counterpackets either lie below the asymptotic entropy boundary, or above raw entropy but below the required finite/local-limit reserve.

---

## THICK_RESIDUE_NORMAL_FORM

### BANKABLE_LEMMA — exact thick-residue quotient compression

Let

[
C=\operatorname{RS}[F,D,k],\qquad |D|=n,
]
[
a=k+\sigma,\qquad r=n-k,\qquad j=r-\sigma,
]
and let (E\in F[X]) have degree

[
t=\sigma+d\le r,\qquad d>0,
]

with (E(x)\ne0) for every (x\in D). Write (B_{\rm num}) for the residue numerator, to distinguish it from any base field.

For (S\subseteq D), (|S|=a), let

[
L_S(X)=\prod_{x\in S}(X-x)
]

and let (I_S(w)) be the unique degree-(<a) interpolant of (w|_S).

Set

[
A_E=F[X]/(E),\qquad
W_d={[H]_E:\deg H<d}.
]

Then:

[
Q|_S=w,\qquad \deg Q<k+t
]

holds exactly when

[
Q=I_S(w)+L_SH,\qquad \deg H<d.
]

Consequently, with

[
u_S=[I_S(w)]*E,\qquad b=[B*{\rm num}]_E,
]
[
V_S=[L_S]_E,W_d,
]

the support (S) witnesses slope (z) exactly when

[
zb\in u_S+V_S. \tag{1}
]

Because (E) has no roots in (S), ([L_S]_E) is a unit in (A_E). Hence

[
\dim_F V_S=d,\qquad
\dim_F(A_E/V_S)=t-d=\sigma. \tag{2}
]

Moreover, at a witnessed slope, noncontainment is exactly

[
b\notin V_S. \tag{3}
]

#### Proof of noncontainment

Suppose (b\in V_S). Then for some (\deg H<d),

[
B_{\rm num}-L_SH=ER
]

with (\deg R<k). On (S),

[
-\frac{B_{\rm num}}E=-R.
]

Thus the direction word (g=-B_{\rm num}/E) has a degree-(<k) explanation on (S). If (P=(Q-zB_{\rm num})/E), then (P=f+zg) on (S), so (P-z(-R)) also explains the anchor (f=w/E). The witness is contained.

Conversely, if (G\in F[X]_{<k}) explains (g) on (S), then

[
EG+B_{\rm num}
]

vanishes on (S). Its degree is (<k+t=a+d), so

[
EG+B_{\rm num}=L_SH,\qquad \deg H<d.
]

Therefore (b\in V_S). This proves (3).

### PROOF — fixed (\sigma)-dimensional quotient

Let

[
\pi_d:A_E\longrightarrow A_E/W_d
]

be the quotient map. Multiplying (1) by ([L_S]_E^{-1}) gives

[
\alpha_S=z\beta_S, \tag{4}
]
where

[
\alpha_S=
\pi_d!\left([L_S]_E^{-1}[I_S(w)]_E\right),
]
[
\beta_S=
\pi_d!\left([L_S]*E^{-1}[B*{\rm num}]_E\right).
]

The target (A_E/W_d) has dimension exactly (\sigma), independent of (t). Furthermore,

[
\beta_S\ne0
]

is exactly transversality/noncontainment. Hence every support contributes either no slope or one uniquely determined slope.

This is the correct unconditional thick-residue compression:

[
\boxed{
\text{degree }t=\sigma+d
\quad\rightsquigarrow\quad
\text{a support-dependent collinearity test in one fixed }\sigma
\text{-space}.
}
]

What does **not** follow is the existence of one fixed denominator (E') of degree (\le\sigma). The twisting multiplier ([L_S]_E^{-1}) depends on (S), and removing that cocycle is precisely an inverse problem, not a formal reduction.

---

### PROOF — canonical identification with syndrome transverse secants

Let

[
\mathcal V=F^D/C
]

be the syndrome space, of dimension (r=n-k). For (x\in D), let (h_x) be the syndrome class of the coordinate unit vector at (x). For (T\subseteq D), define

[
U_T=\operatorname{span}_F{h_x:x\in T}.
]

Since Reed–Solomon codes are MDS, any at most (r) of the (h_x)'s are linearly independent. Thus, for (|T|=j),

[
\dim U_T=j,\qquad \dim(\mathcal V/U_T)=\sigma.
]

Define

[
\theta_E:A_E\longrightarrow\mathcal V,
\qquad
\theta_E([R]_E)=\left[\frac{R}{E}\right].
]

This is injective. Indeed, if (R/E) equals a polynomial (P) of degree (<k) on all of (D), then (R-EP) has (n) roots and degree (<k+t\le n), hence is zero. Since (\deg R<t), this forces (R=0).

For (T=D\setminus S),

[
\theta_E(V_S)=\theta_E(A_E)\cap U_T. \tag{5}
]

To see this, if (R\equiv L_SH\pmod E), then (R/E), modulo a codeword, is represented by (L_SH/E), which vanishes on (S) and is supported on (T). The converse follows by reversing the argument.

The dimensions are

[
\dim\theta_E(A_E)=t,\qquad
\dim(\theta_E(A_E)\cap U_T)=d,
]

and therefore

[
\dim(\theta_E(A_E)+U_T)
=t+j-d
=(\sigma+d)+(r-\sigma)-d
=r.
]

Hence the induced map is an isomorphism

[
A_E/V_S\ \cong\ \mathcal V/U_T. \tag{6}
]

For the line

[
f=\frac wE,\qquad
g=-\frac{B_{\rm num}}E,
]

put

[
u=[f],\qquad v=[g]\in\mathcal V.
]

Then the thick-residue landing equation is exactly

[
u+zv\in U_T, \tag{7}
]

and noncontainment is exactly

[
v\notin U_T. \tag{8}
]

Thus the high-denominator branch is not merely analogous to the syndrome formulation. It is canonically the same incidence problem.

---

## COMPRESSION_THEOREM_OR_COUNTERPACKET

### ROUTE_CUT — high denominator is a universal chart

On a multiplicative domain (D\subseteq F^\times), every affine syndrome line has a degree-(r=n-k) residue representation.

Take (E=X^r), which is nonzero on (D). For any direction word (g), interpolate (Eg) by a polynomial (U) of degree (<n=k+r). Divide

[
U=ER+C,\qquad \deg R<k,\quad \deg C<r.
]

Then on (D),

[
g=R+\frac CE.
]

After subtracting the codeword direction (R), this is a residue direction with denominator degree (r). Therefore, whenever (\sigma<r),

[
\boxed{\text{the stratum }t>\sigma\text{ already contains every affine syndrome line}.}
]

A balanced (t=\sigma) theorem cannot be promoted to the full theorem merely by “ignoring” larger denominators.

There is also a parameter-count obstruction. The number of syndrome directions admitting some denominator of degree at most (\sigma) is at most

[
\sum_{s\le\sigma}q^{2s}
=O(\sigma q^{2\sigma}),
]

whereas the syndrome space has (q^r) vectors. When (r>2\sigma+O(\log_q\sigma)), most directions have no such representation.

Parameter counting alone does not refute a safe-side high-cloud inverse theorem, but it shows that such a theorem would be a genuine global inverse theorem, not denominator bookkeeping.

---

### COUNTERPACKET — general reduced overbalanced lower construction

Assume here that

[
q=q_{\rm gen}=q_{\rm line}=|F|.
]

Let (t=\sigma+1), and assume

[
k+2t\le n.
]

Choose an irreducible polynomial (E\in F[X]) of degree (t). Then

[
A_E=F[X]/(E)\cong F_{q^t}.
]

For every (a)-support (S),

[
V_S=[L_S]_E F
]

is a one-dimensional subspace.

For (B\in A_E^\times), let

[
c(B)=#{S: B\in V_S},
\qquad
M(B)=\binom na-c(B).
]

Counting pairs ((B,S)) gives

[
\sum_{B\in A_E^\times}c(B)
=\binom na(q-1).
]

Therefore some (B\ne0) satisfies

[
c(B)\le
\binom na\frac{q-1}{q^t-1},
]

and hence

[
M(B)\ge
\binom na
\left(1-\frac{q-1}{q^{\sigma+1}-1}\right). \tag{9}
]

All these (M(B)) supports are transverse.

Let

[
N=\binom na=\binom nj,
\qquad
\lambda_\perp=\frac{M(B)}{q^\sigma},
]

and define the Bessel shell

[
J_\sigma
========

\sum_{h=0}^{\sigma-1}
\binom jh\binom ahq^{-h}. \tag{10}
]

Then there exists an anchor (w) for which the number of distinct noncontained bad slopes is at least

[
\boxed{
q,\frac{\lambda_\perp}{\lambda_\perp+J_\sigma}.
} \tag{11}
]

If

[
\lambda_\perp>qJ_\sigma, \tag{12}
]

there is an anchor for which **every** slope is noncontained-bad.

#### PROOF of (11)

In syndrome space, fix the direction (v=[-B/E]), and retain the (M(B)) transverse secant spaces (U_T). For uniform (x\in\mathcal V), define

[
\nu(x)=#{T:x\in U_T,\ v\notin U_T}.
]

Then

[
\mathbb E\nu=\lambda_\perp.
]

For two (j)-sets (T,T'), put

[
h=|T\setminus T'|.
]

The MDS property gives

[
\Pr(x\in U_T\cap U_{T'})
========================

\begin{cases}
q^{-\sigma-h},&h<\sigma,\
q^{-2\sigma},&h\ge\sigma.
\end{cases}
]

For each (T), there are

[
\binom jh\binom ah
]

sets (T') at exchange distance (h). Consequently,

[
\mathbb E\nu^2
\le
\lambda_\perp^2+\lambda_\perp J_\sigma.
]

Paley–Zygmund yields

[
\Pr(\nu(x)>0)
\ge
\frac{\lambda_\perp}{\lambda_\perp+J_\sigma}.
]

For a uniform syndrome anchor (u), each (u+zv) is uniform in (\mathcal V). Summing over (z\in F) proves (11).

The variance estimate also gives

[
\Pr(\nu(x)=0)\le\frac{J_\sigma}{\lambda_\perp}.
]

Thus the expected number of missed slopes is at most (qJ_\sigma/\lambda_\perp), proving the all-slope assertion under (12).

---

### Reducedness and aperiodicity

The preceding direction has minimal denominator exactly (t).

Suppose it admitted a representation of degree (t'<t):

[
-\frac{B_{\rm num}}E
====================

R-\frac{B'}{E'}
\quad\text{on }D,
]

where (\deg R<k), (\deg E'=t'), and (\deg B'<t'). Cross-multiplication gives a polynomial vanishing on all (n) points of (D), of degree at most

[
k+t+t'-1<n.
]

It is therefore identically zero. Reducing the identity modulo (E) gives

[
BE'\equiv0\pmod E.
]

Since (E) is irreducible and (B\ne0) in (A_E), this forces (E\mid E'), impossible because (t'<t).

The same argument proves uniqueness among degree-(t) denominators.

At the official dyadic rates, (\gcd(n,k)) is a power of two. Taking (\sigma) even makes (t=\sigma+1) odd, so a degree-(t) denominator cannot be a pullback (E_0(X^M)) for any proper quotient degree (M\mid\gcd(n,k)), (M>1). The datum is therefore reduced and aperiodic in the source sense.

---

### Official-rate asymptotic counterpacket below entropy

Fix any

[
\rho\in\left{\frac12,\frac14,\frac18,\frac1{16}\right}.
]

Suppose

[
k/n\to\rho,\qquad
\sigma=(c+o(1))\frac{n}{\log_2q},
\qquad
c<H_2(\rho),
\qquad
\log q=o(n),
]

with (\sigma) even. Then

[
\log_2\frac{\binom n{k+\sigma}}{q^\sigma}
=========================================

(H_2(\rho)-c+o(1))n.
]

Also,

[
J_\sigma
\le
\exp!\left(2\sqrt{\frac{aj}{q}}\right)
\le
\exp!\left(\frac n{\sqrt q}\right)
==================================

2^{o(n)}.
]

Hence (12) holds, and a (1-o(1)) fraction of syndrome anchors produce **all (q) slopes**, with a minimal, growing, aperiodic denominator

[
t=\sigma+1>\sigma.
]

This refutes any unconditional “high cloud implies (t'\le\sigma)” theorem. It does not refute the safe branch because it lies below the entropy boundary.

---

### COUNTERPACKET — official-rate finite packet above raw entropy

There is also a theorem-level finite packet above the raw entropy inequality.

Take

[
F=\mathbb F_{65537},\qquad
n=32,\qquad
k=16,\qquad
\sigma=2,\qquad
a=18,\qquad
j=14,\qquad
t=3.
]

Let (D\le F^\times) be the subgroup of order (32), and choose any irreducible cubic (E). Since

[
N=\binom{32}{18}=471{,}435{,}600
<
65537^2=4{,}295{,}098{,}369,
]

the union of the (N) one-dimensional spaces (V_S\subset F_{q^3}) cannot cover (F_{q^3}^\times). Thus one may choose (B_{\rm num}) transverse to every support.

Here

[
\lambda=\frac{N}{q^2},
\qquad
J_2=1+\frac{14\cdot18}{q}
=1+\frac{252}{65537}.
]

Formula (11) gives

[
#{\text{distinct noncontained bad slopes}}
\ge
\left\lceil
\frac{Nq}{N+q^2+252q}
\right\rceil
============

6460. \tag{13}
      ]

This is an official-rate packet at

[
\rho=\frac12,\qquad
\delta=\frac jn=\frac7{16},
]

with

[
t=3>\sigma=2,
]

minimal denominator, no quotient pullback, and transverse landing at every witnessing support.

It also satisfies the raw entropy inequality with a genuine numerical margin:

[
2\log_2(65537)
==============

32.000044\ldots

>

# \log_2\binom{32}{18}

28.812485\ldots.
]

It is not a counterexample to the final corrected asymptotic theorem: (\sigma=2) is below the local-limit/quotient reserve (Cn/\log n).

A fully explicit smaller packet over (\mathbb F_{97}), including the anchor and exhaustive support verification, is available here:

[Finite (t=3,\sigma=2) counterpacket checker](sandbox:/mnt/data/lane06_t3_sigma2_counterpacket_verify.py)

That checker verifies

[
n=16,\quad k=8,\quad \sigma=2,\quad t=3,
]
[
E=X^3+X+1,\quad B_{\rm num}=1,
]
[
\binom{16}{10}=8008<97^2=9409,
]

together with 97 transverse witness incidences producing 67 distinct bad slopes.

---

## SOURCE_VALIDITY

**AUDIT**

The constructions respect the source distinctions.

* In both finite packets,

  [
  q_{\rm gen}=q_{\rm line}=|F|.
  ]

  No (q_{\rm line})-to-(q_{\rm gen}) transfer is being assumed.

* (q_{\rm chal}) is not used.

* There is no proper base field (B) in the prime-field examples. The symbol (B_{\rm num}) denotes only the residue numerator.

* Every witness has exact agreement support size

  [
  a=k+\sigma.
  ]

* Every counted landing is transverse:

  [
  v\notin U_T,
  ]

  equivalently

  [
  [B_{\rm num}]*E
  \notin
  [L_SF[X]*{<t-\sigma}]_E.
  ]

* Reducedness and absence of a degree-(\le\sigma) equivalent datum follow by the root-count argument above.

* For the dyadic official rates, the odd minimal denominator (t=\sigma+1) is not a quotient pullback.

* The asymptotic construction works for (1-o(1)) of all anchors when (\lambda_\perp\gg qJ_\sigma). It is therefore not confined to any predeclared template family occupying (o(1)) of syndrome-anchor space. An undefined catch-all “other template” is not auditable; it must be stated as an explicit algebraic class with a quantitative size bound.

---

## EXACT_NEW_WALL

### BANKABLE_LEMMA — finite entropy surplus is necessary

Assume the same-field setting

[
q=q_{\rm gen}=q_{\rm line},
]

and suppose (N<q^\sigma), so that a degree-(\sigma+1) direction can be chosen transverse to every (j)-secant.

If a universal upper theorem claims at most (L<q) bad slopes, then (11) forces

[
q\frac{\lambda}{\lambda+J_\sigma}\le L,
\qquad
\lambda=\frac N{q^\sigma}.
]

Equivalently,

[
\lambda\le\frac{LJ_\sigma}{q-L},
]

or

[
\boxed{
\sigma\log_2q-\log_2N
\ge
\log_2\frac{q-L}{LJ_\sigma}.
} \tag{14}
]

Thus a merely positive entropy surplus is insufficient for a finite (L=n^{1+o(1)}) numerator. When (q=n^C) and (J_\sigma=n^{o(1)}), one needs at least

[
\sigma\log_2q-\log_2N
\ge
(C-1-o(1))\log_2n
]

to rule out this generic high-denominator packet.

A fixed multiplicative entropy margin

[
\sigma\log_2q\ge(1+\varepsilon)\log_2N
]

pays much more than (14) asymptotically, but a finite checker must print the additive surplus.

---

### EXACT_NEW_WALL — denominator-free final statement

The remaining theorem should be stated directly in syndrome space.

Let

[
\mathcal V=F^D/\operatorname{RS}[F,D,k],
\qquad
U_T=\operatorname{span}{h_x:x\in T},
\qquad
|T|=j=n-k-\sigma.
]

For every affine line

[
\ell(z)=u+zv
]

define

[
Z_{\rm tr}(u,v)
===============

\left{
z\in F:
\exists T,\ |T|=j,\
u+zv\in U_T,\
v\notin U_T
\right}.
]

The exact unresolved theorem is:

[
\boxed{
|Z_{\rm tr}(u,v)|
\le n^{1+o(1)}
}
]

above the generated-field entropy reserve, the finite surplus (14), and the quotient reserve, unless the line belongs to an explicitly quantified quotient, tangent/common-envelope, or other declared template class.

This is precisely

[
\texttt{W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE}.
]

High denominator can therefore be ignored **as a separate coordinate index** once the proof is written in syndrome space. It cannot be ignored as a class of lines: the (t=r) chart contains every affine line, and a theorem restricted to (t\le\sigma) does not address the prize challenge.

The next exact lemma is not another denominator manipulation. It is a fixed-prime inverse theorem for affine lines meeting too many (j)-column secant spaces transversely, with the additive entropy surplus and all template classes stated quantitatively.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
