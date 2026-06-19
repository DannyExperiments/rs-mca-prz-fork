# ROUTE_CUT

**Confidence: high.**

The (t>\sigma) branch does not admit a genuine denominator-compression theorem. Its maximal unconditional compression is supportwise and syndrome-theoretic. In fact, (t=r=n-k) is a universal chart for every affine syndrome line, so a theorem classifying high-denominator clouds is essentially the full syndrome transverse-secant inverse theorem.

I also found an explicit strengthened counterpacket to literal compression. It has minimal denominator (t=3>\sigma=2), full quotient-action rank, no proper common envelope, and (67) distinct noncontained slopes. It is not a counterexample to the corrected theorem, because (67) lies below the codimension-(\sigma) occupancy term (8008/97).

## 1. Exact theorem and counterpacket

### Theorem A — canonical supportwise compression

Let

[
C=\operatorname{RS}[F,D,k],\qquad |D|=n,\qquad r=n-k,
]

and fix

[
a=k+\sigma,\qquad j=n-a=r-\sigma.
]

Suppose a residue presentation has denominator degree

[
t=\sigma+d,\qquad d>0,
]

with (E(x)\ne0) on (D). Put

[
A_E=F[X]/(E),\qquad
W_d=[F[X]_{<d}]_E.
]

For an (a)-set (S\subset D), let

[
L_S(X)=\prod_{x\in S}(X-x),\qquad T=D\setminus S,
]

and define

[
V_{E,S}=[L_S]*E W_d
=[L_SF[X]*{<d}]_E.
]

Then:

1. Every (Q\in F[X]_{<k+t}) agreeing with (w) on (S) is uniquely of the form
   [
   Q=I_S(w)+L_SH,\qquad \deg H<d.
   ]

2. Writing
   [
   i_S=[I_S(w)]*E,\qquad b=[B*{\rm num}]*E,
   ]
   the support (S) witnesses slope (z) exactly when
   [
   zb\in i_S+V*{E,S}.
   ]

3. The incidence is noncontained exactly when
   [
   b\notin V_{E,S}.
   ]

4. The quotient has dimension
   [
   \dim_F A_E/V_{E,S}=t-d=\sigma.
   ]

More importantly, this quotient is canonically the syndrome quotient.

Let

[
\mathcal V=F^D/C,\qquad
U_T=\operatorname{span}{h_x:x\in T},
]

where (h_x) is the syndrome column at (x). Define

[
\Theta_E:A_E\longrightarrow\mathcal V,
\qquad
[R]*E\longmapsto \left[\left(\frac{R(x)}{E(x)}\right)*{x\in D}\right].
]

Then (\Theta_E) is injective and

[
\Theta_E(V_{E,S})=\Theta_E(A_E)\cap U_T.
]

Consequently, the induced map

[
\boxed{
\overline\Theta_{E,S}:
A_E/V_{E,S}\overset{\sim}{\longrightarrow}\mathcal V/U_T
}
]

is an isomorphism of (\sigma)-dimensional vector spaces.

If

[
u=\operatorname{syn}(w/E),
\qquad
v=\operatorname{syn}(-B_{\rm num}/E),
]

then under this isomorphism,

[
zb\in i_S+V_{E,S}
\iff
u+zv\in U_T,
]

and

[
b\notin V_{E,S}
\iff
v\notin U_T.
]

Thus

[
\boxed{
Z_{\rm NC}(E,B_{\rm num},w)
===========================

\left{
z:\exists T,\ |T|=j,\
u+zv\in U_T,\ v\notin U_T
\right}.
}
]

This is equality, not merely a comparison.

---

### Theorem B — degree (r) is a universal chart

Assume (D\subset F^\times). Let (E) be any monic degree-(r) polynomial with no roots on (D).

For any word (g:D\to F), interpolate (E(x)g(x)) by a polynomial (U_g) of degree (<n). Euclidean division gives

[
U_g=ER_g+C_g,
\qquad
\deg R_g<k,\quad \deg C_g<r.
]

Hence on (D),

[
g=R_g+\frac{C_g}{E}.
]

Modulo the codeword (R_g), the direction is represented by (C_g/E). For an arbitrary anchor (f), take (w(x)=E(x)f(x)).

Therefore every affine syndrome line has a residue presentation with

[
t=r>\sigma.
]

In particular,

[
\boxed{
\max_{\sigma<t\le r}\Lambda_t^{\rm NC}
======================================

\max_{\text{affine syndrome lines }\ell}
|Z_{\rm tr}(\ell)|.
}
]

The displayed denominator is not intrinsic. Neither is its displayed action rank. At degree (r), one may choose (E) to be a primitive irreducible polynomial. If (\xi) is its root and (M\le n\le q-1), then (\xi^M) cannot lie in a proper subfield, so

[
d_M(E)=r.
]

Thus even a quotient-structured syndrome line can be put into a high-denominator chart whose displayed (d_M(E)) is maximal. Quotient structure in the (t>\sigma) branch must therefore be defined either:

* through a genuinely minimal presentation in a range where minimal presentations are unique; or
* directly in syndrome/support language.

It cannot be read from an arbitrary overbalanced denominator.

---

### Theorem C — an envelope-free occupancy packet for (\sigma=1)

Let (D\subset\mathbb F_q^\times), (|D|=n), and let (r=n-k\ge4). Set

[
\sigma=1,\qquad j=r-1,\qquad t=2,
\qquad
N=\binom{n}{r-1}.
]

Assume (q>N). Then there exists a residue-line datum such that:

[
\tau(v)=2>\sigma,
]

[
d_M(E)=2
\quad\text{for every }M\mid\gcd(n,k),\ M>1,
]

the syndrome line lies in no proper column envelope, every support incidence is transverse, and

[
\boxed{
|Z_{\rm NC}|
\ge
\left\lceil
\frac{qN}{q+N-1}
\right\rceil.
}
]

#### Construction

Choose a primitive irreducible quadratic (E). Then

[
A_E\simeq\mathbb F_{q^2}.
]

For every (a=k+1) support (S),

[
V_{E,S}=F[L_S]_E
]

is a one-dimensional (F)-subspace of (A_E). There are at most (N) such lines, whereas (A_E) has (q+1) projective lines. Since (N<q+1), choose

[
b\notin \bigcup_S V_{E,S}.
]

The corresponding syndrome direction (v) is outside every (j=r-1) column span. Every smaller proper column span extends to an ((r-1))-column span, so (v) is outside every proper column envelope.

For a uniformly random syndrome point (x), let

[
\nu(x)=#{T:|T|=r-1,\ x\in U_T}.
]

Distinct (U_T)'s are distinct hyperplanes, so

[
\mathbb E\nu=\frac Nq
]

and

[
\mathbb E\nu^2
==============

\frac Nq+\frac{N(N-1)}{q^2}.
]

Paley–Zygmund gives

[
\Pr(\nu(x)>0)
\ge
\frac{N}{q+N-1}.
]

Averaging over the (q) points of (u+Fv) produces the claimed anchor.

Because there are only (N) supports,

[
|Z_{\rm NC}|\le N.
]

Hence this packet is exactly an occupancy packet:

[
|Z_{\rm NC}|=\Theta(N)
======================

\Theta!\left(\frac{\binom nj}{q^{\sigma-1}}\right).
]

It clears low denominator, action-rank, tangent, and common-envelope explanations. Only the occupancy alternative remains.

---

### Explicit (\sigma=2), (t=3) packet

The following finite packet strengthens the archived (q=97) example.

[
F=\mathbb F_{97},\quad
n=16,\quad
k=8,\quad
r=8,
]

[
\sigma=2,\quad
a=10,\quad
j=6,\quad
t=3.
]

Use the order-(16) subgroup

[
D=\langle8\rangle
=================

(1,8,64,27,22,79,50,12,96,89,33,70,75,18,47,85).
]

Take

[
E=X^3+X+1,\qquad B_{\rm num}=1,
]

and, in the displayed ordering of (D),

[
w=
(50,42,9,48,46,39,45,91,78,57,85,6,53,92,70,5).
]

Exact exhaustive calculation gives:

[
88
\quad\text{transverse support incidences},
]

and

[
\boxed{67\text{ distinct noncontained slopes}.}
]

The slope set is

[
\begin{aligned}
{&
0,1,2,3,4,5,8,9,10,11,12,14,15,16,17,18,20,21,22,23,25,29,31,\
&35,36,37,38,39,41,42,43,44,46,48,49,51,54,56,57,58,59,61,64,\
&65,66,67,68,69,70,71,72,75,76,77,78,80,81,82,83,85,86,87,90,\
&91,92,95,96}.
\end{aligned}
]

It satisfies all of the following.

* **Minimal and unique denominator.** If
  [
  -\frac1E=R-\frac{B'}{E'}
  ]
  on (D), with (\deg R<8) and (\deg E'\le3), cross-multiplication gives a polynomial of degree at most
  [
  (k-1)+3+3=13<16.
  ]
  It is therefore identically zero. Reduction modulo (E) forces (E\mid E'). Thus no degree-(\le2) presentation exists, and a degree-(3) presentation has (E') proportional to (E).

* **Full action rank.** A root (\xi) of (E) has multiplicative order (6338=2\cdot3169). The active quotient scales are (M=2,4,8), and
  [
  \operatorname{ord}(\xi^M)=3169>96.
  ]
  Since degree (3) is prime, the only proper subfield is (\mathbb F_{97}). Hence
  [
  d_2(E)=d_4(E)=d_8(E)=3.
  ]

* **Every active support is transverse.**
  For all (8008) ten-element supports,
  [
  [1]_E\notin [L_SF]_E.
  ]

* **No proper common envelope.**
  In the (8)-dimensional syndrome space, exactly (109) seven-column hyperplanes contain (v), and none contains (u). Every smaller column envelope extends to a seven-column hyperplane, so
  [
  \operatorname{span}(u,v)\not\subseteq U_R
  \quad\text{for every }|R|<8.
  ]

* **Above raw entropy.**
  [
  N=\binom{16}{10}=8008<97^2=9409,
  ]
  with additive surplus
  [
  2\log_2 97-\log_2 8008
  ======================

  0.232599426\ldots\text{ bits}.
  ]

* **Calibrated occupancy absorbs it.**
  The relevant codimension is (\sigma=2), not the displayed denominator degree (t=3):
  [
  R_{\rm occ}
  ===========

  # \frac{\binom{16}{10}}{97^{,2-1}}

  # \frac{8008}{97}

  82.556701\ldots.
  ]
  Thus
  [
  67<R_{\rm occ}.
  ]

The exact verifier is here:

[Role 05 (t=3,\sigma=2) exhaustive packet verifier](sandbox:/mnt/data/role05_t3_sigma2_packet_verify.py)

## 2. Proof consequences

The most important numerical conclusion is that the occupancy exponent is controlled by the syndrome codimension (\sigma), not by the residue denominator degree (t).

For fixed agreement (a=k+\sigma),

[
N=\binom{n}{a}=\binom nj,
]

and the unstructured line-occupancy numerator is

[
\boxed{
R_{\rm occ}
===========

\frac{N}{q^{\sigma-1}}.
}
]

The normalized contribution is

[
\frac{N}{q^\sigma}.
]

Using (t) instead would be wrong. In the explicit packet, a hypothetical high-denominator term

[
\frac{\binom{16}{k+t}}{97^{t-1}}
================================

# \frac{\binom{16}{11}}{97^2}

0.464\ldots
]

would predict essentially no slopes, while the actual count is (67). The reason is precisely that the affine thick-residue planes have codimension (\sigma), irrespective of their ambient dimension (t).

## 3. Parameter ledger

| Parameter                    |    Explicit packet |
| ---------------------------- | -----------------: |
| (q_{\rm gen})                |               (97) |
| (q_{\rm line})               |               (97) |
| (q_{\rm chal})               |             unused |
| (n)                          |               (16) |
| (k)                          |                (8) |
| (\rho)                       |              (1/2) |
| (r=n-k)                      |                (8) |
| (\sigma)                     |                (2) |
| (a=k+\sigma)                 |               (10) |
| (j=r-\sigma)                 |                (6) |
| residue (t)                  |                (3) |
| thick dimension (d=t-\sigma) |                (1) |
| (N=\binom nj)                |             (8008) |
| (\lambda=N/q^\sigma)         |     (0.8511000106) |
| (q\lambda=N/q^{\sigma-1})    |      (82.55670103) |
| distinct bad slopes          |               (67) |
| normalized MCA contribution  | (67/97=0.69072165) |
| entropy surplus              | (0.232599426) bits |
| active (M)                   |            (2,4,8) |
| (d_M(E))                     |            (3,3,3) |
| proper common envelopes      |                (0) |

## 4. Route-board impact

1. **Cut literal denominator compression.**
   “Many (t>\sigma) slopes imply an equivalent denominator of degree (\le\sigma)” is false, even after minimality, quotient-action rank, transversality, and common-envelope tests.

2. **Close Role 05 as a coordinate reduction.**
   The (t>\sigma) case introduces no separate invariant incidence geometry. It is exactly the syndrome transverse-secant problem through the canonical quotients
   [
   A_E/V_{E,S}\simeq\mathcal V/U_T.
   ]

3. **Do not classify overbalanced packets using a displayed (E).**
   At degree (r), every syndrome line admits essentially arbitrary denominators. Any quotient classification must be presentation-invariant.

4. **The occupancy term is unavoidable after structural exclusions.**
   The explicit packet is minimal, full action-rank, fully transverse, and envelope-free, yet has (67>n) slopes. The corrected main term absorbs it:
   [
   67<8008/97.
   ]

5. **The correct global theorem contains no residue (t).**
   Its same-field shape must be

   [
   \boxed{
   |Z_{\rm tr}(u,v)|
   \le
   n^{1+o(1)}
   +
   \frac{\binom nj}{q^{\sigma-1}},n^{o(1)}
   +
   \mathrm{Quotient}(u,v)
   +
   \mathrm{Envelope}(u,v).
   }
   ]

## 5. What remains open

The explicit packet does not refute the calibrated safe-side theorem. It has only (\sigma=2), a (0.233)-bit entropy surplus, and its slope count is below occupancy.

The unresolved problem is now cleanly denominator-free:

> Above the finite entropy surplus and quotient reserves, prove that every quotient-free, proper-envelope-free affine syndrome line has at most
> [
> n^{1+o(1)}
> +
> \frac{\binom nj}{q^{\sigma-1}}n^{o(1)}
> ]
> transverse secant slopes.

No further manipulation of (Q=I_S(w)+L_SH) will solve that problem, because the degree-(r) chart contains every affine syndrome line.

## Do you see a route to a full solve? ROLE 05 - High-Denominator t > sigma Thick-Residue Branch

**Yes for eliminating Role 05 as an independent branch; not yet for the complete MCA upper theorem.**

The next exact lemma is:

[
\boxed{\texttt{W-MCA-FAR-SUPPORT-CALIBRATED-RATIO-IMAGE}}
]

Let

[
c_T(s)
======

\bigl(
\langle s,L_TX^m\rangle
\bigr)_{0\le m<\sigma}.
]

For an affine syndrome line (u+zv), define the partial ratio map

[
\zeta_{u,v}(T)=z
]

on split locators satisfying

[
c_T(u)+z,c_T(v)=0,
\qquad
c_T(v)\ne0.
]

After deleting explicitly quantified quotient packets and proper-envelope slopes, prove

[
\boxed{
|\operatorname{im}\zeta_{u,v}|
\le
n^{1+o(1)}
+
\frac{\binom nj}{q^{\sigma-1}},n^{o(1)}.
}
]

In the proper-envelope-free branch, any two selected witnesses for distinct slopes satisfy

[
|T\setminus T'|\ge\sigma.
]

Therefore the exact missing input is a fixed-line local limit for this (\sigma)-separated split-locator ratio image. That is the next theorem; there is no remaining high-denominator compression lemma before it.
