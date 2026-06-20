COUNTERPACKET

## 1. Executive verdict and confidence

The scalar block-collapse identity does **not** transfer unchanged to (t=1) MCA color occupancy.

A full (K)-block always kills the appropriate lower jets, but:

* when the added point (\beta) is a new reduced component, the toric block label (c^M) becomes the surviving multiplicative MCA color;
* when (\beta) thickens an existing point, blocks of order (M\ge \sigma) are color-neutral, but the critical support-collapse scale (M=\sigma-1) retains an additive top-jet color (c^M).

Consequently, a fixed ((K,D)) support packet can split into many MCA slopes. The correct charge is the pushforward of block configurations to the thickened group, equivalently:

[
\text{product occupancy}
]

in the multiplicative-color branch, and

[
\text{sum occupancy conditioned on product}
]

at the critical additive-color scale.

**Confidence:** high, (0.99), for the block formulas, charge object, and counterpacket families; moderate, (0.80), for the proposed remaining route because it still depends on canonical maximal ((K,D)) assignment and residual non-double-counting.

---

## 2. Formal block-color transfer theorem

Let (F=\mathbf F_q), let (H\le F^\times) be cyclic of order (n), and let

[
\Gamma=[0]+\sigma[\infty].
]

This is the colored modulus (\Delta+[\beta]). With (z) the local coordinate at infinity, normalize the one-atom map as

[
\alpha_\Gamma(x)=(-x,1-xz)
\in F^\times\times
\left(1+zF[z]/(z^\sigma)\right).
]

Thus a subset (T\subset H) maps to

[
\Phi_\Gamma(T)=
\left(
(-1)^{|T|}\prod_{x\in T}x,,
\prod_{x\in T}(1-xz)\bmod z^\sigma
\right).
]

Let (K\le H) have order (M), let (C=cK), and define its intrinsic block label

[
y(C):=c^M.
]

This is independent of the representative (c).

### Theorem 2.1 — exact thickened block product

For every (K)-coset (C=cK),

[
\prod_{x\in C}(X-xZ)=X^M-y(C)Z^M,
]

and

[
\boxed{
\beta_K^+(C):=
\prod_{x\in C}\alpha_\Gamma(x)
==============================

\left(-y(C),,1-y(C)z^M\bmod z^\sigma\right).
}
]

Hence:

1. all jet coordinates of degrees (1,\ldots,M-1) vanish;
2. if (M\ge \sigma), every jet coordinate in (G_\Gamma) vanishes, but the toric coordinate (-y(C)) remains;
3. if (M=\sigma-1), the unique surviving jet is
   [
   -y(C)z^{\sigma-1}.
   ]

The toric block color therefore never disappears intrinsically from (G_\Gamma). Whether it is support data or MCA color depends on the restriction map (G_\Gamma\to G_\Delta).

---

## 3. The two (t=1) color branches

There are two ways to remove the external layer from the model colored modulus.

### 3.1 Multiplicative-color branch: (\beta\notin\operatorname{Supp}\Delta)

Take

[
\Delta_\times=\sigma[\infty],
\qquad \beta=0,
]

so that

[
\Gamma=\Delta_\times+[0].
]

The restriction map is

[
\pi_\times:
F^\times\times U_{\sigma-1}\longrightarrow U_{\sigma-1},
\qquad
(a,u)\longmapsto u,
]

with

[
\ker\pi_\times\simeq F^\times.
]

For every (M\ge\sigma),

[
\pi_\times(\beta_K^+(C))=1,
]

but

[
\beta_K^+(C)=(-y(C),1)
]

is generally nontrivial in the color kernel.

Thus:

[
\boxed{
\text{a full (K)-block is support-invisible but carries multiplicative color }y(C).
}
]

This already kills the naive assertion that a scalar block packet contributes only one MCA slope.

### 3.2 Additive-color branch: (\beta\in\operatorname{Supp}\Delta)

Assume (\sigma\ge2), and take

[
\Delta_+= [0]+(\sigma-1)[\infty],
\qquad
\beta=\infty.
]

Restriction truncates the last infinity jet:

[
\pi_+:
F^\times\times U_{\sigma-1}
\longrightarrow
F^\times\times U_{\sigma-2}.
]

Its kernel is

[
\ker\pi_+
=========

{(1,1+t z^{\sigma-1}):t\in F}
\simeq(F,+).
]

There are now two scales.

If (M\ge\sigma), then

[
\beta_K^+(C)=(-y(C),1).
]

The toric label is already visible in (G_{\Delta_+}), and the added color coordinate is zero. Therefore:

[
\boxed{
M\ge\sigma:
\text{ a fixed old support target contains all such block trades at one slope.}
}
]

At the critical scale (M=\sigma-1),

[
\beta_K^+(C)
============

(-y(C),1-y(C)z^{\sigma-1}).
]

The projection remembers only ((-y(C),1)), while the new additive color is (-y(C)). Therefore:

[
\boxed{
M=\sigma-1:
\text{ support collapse occurs, but the added top-jet color survives.}
}
]

For dyadic (H), this critical obstruction exists exactly when (\sigma-1) is a power of two dividing (n).

---

## 4. Exact ((K,D,\mathrm{color})) charge

Fix a defect set (D\subset H). Let

[
\mathcal B_{K,D}
================

{C=cK:C\cap D=\varnothing}
]

be the available full (K)-blocks. For

[
S\in\binom{\mathcal B_{K,D}}{\ell},
]

put

[
T(D,S)
======

D\sqcup\bigcup_{C\in S}C,
]

and define

[
P(S):=\prod_{C\in S}y(C),
\qquad
\Sigma(S):=\sum_{C\in S}y(C).
]

Let (g_D=\Phi_\Gamma(D)).

### Exact block formulas

If (M\ge\sigma),

[
\boxed{
\Phi_\Gamma(T(D,S))
===================

g_D\left((-1)^\ell P(S),1\right).
}
]

If (M=\sigma-1),

[
\boxed{
\Phi_\Gamma(T(D,S))
===================

g_D
\left(
(-1)^\ell P(S),,
1-\Sigma(S)z^{\sigma-1}
\right).
}
]

The second formula follows because

[
\prod_{C\in S}(1-y(C)z^{\sigma-1})
\equiv
1-\Sigma(S)z^{\sigma-1}
\pmod {z^\sigma}.
]

### Intrinsic charge measure

The correct charge object is not the pair ((K,D)) alone. It is the counting measure on the thickened group

[
\boxed{
\mu^+_{K,D,\ell}(g)
===================

#\left{
S\in\binom{\mathcal B_{K,D}}{\ell}:
\Phi_\Gamma(T(D,S))=g
\right}.
}
]

For an old support target (b\in G_\Delta), the corresponding MCA occupancy charge is

[
\boxed{
\operatorname{Occ}_{K,D,\ell}(b)
================================

#\left{
g\in\pi^{-1}(b):
\mu^+_{K,D,\ell}(g)>0
\right}.
}
]

This is the exact shear-invariant and gauge-invariant ((K,D,\mathrm{color})) object.

In coordinates, define

[
A^\times_{K,D,\ell}(p)
======================

#\left{
S:
|S|=\ell,\ P(S)=p
\right},
]

and

[
A^{\times,+}_{K,D,\ell}(p,\tau)
===============================

#\left{
S:
|S|=\ell,\ P(S)=p,\ \Sigma(S)=\tau
\right}.
]

Then:

* in the multiplicative branch,
  [
  \operatorname{Occ}_{K,D,\ell}
  =============================

  #{p:A^\times_{K,D,\ell}(p)>0};
  ]
* in the additive branch with (M\ge\sigma), a fixed support target fixes (p), and the occupancy is at most one;
* in the critical additive branch (M=\sigma-1), a fixed support target fixes (p), and
  [
  \boxed{
  \operatorname{Occ}_{K,D,\ell}(b)
  ================================

  #{\tau:A^{\times,+}_{K,D,\ell}(p_b,\tau)>0}.
  }
  ]

Thus the critical arithmetic object is a restricted sum image conditioned on a restricted product.

---

## 5. Counterpacket I: multiplicative block color gives many slopes

Let

[
M>\sigma,\qquad N\ge2,
\qquad n=MN,
]

and choose (F) with (n\mid q-1). Let (H\le F^\times) have order (n), and let (K\le H) have order (M). Put

[
j=M,\qquad k=n-j-\sigma=MN-M-\sigma.
]

Work in the Role-05 normalization with (\beta=\infty), and set

[
A(X,Z)=X^\sigma,
\qquad
B(X,Z)=X^M-Z^M.
]

Thus

[
\Delta=\sigma[0],
\qquad
\Delta^+=\sigma[0]+[\infty].
]

For a (K)-coset (C=cK), write (y=c^M). Its locator is

[
P_C=X^M-yZ^M.
]

It satisfies

[
\boxed{
P_C
===

A(1-y)X^{M-\sigma}
+yB.
}
]

Therefore every (K)-coset is a full-coordinate degree-(j) representation in one old (G_\Delta)-fiber: the coefficient of (B) is the nonzero scalar (y).

An explicit syndrome is obtained by taking the moment vector of length

[
R=M+\sigma-1
]

with

[
s_{\sigma-1}=1,
\qquad
s_i=0\quad(i\ne\sigma-1).
]

Indeed:

* (A=X^\sigma) annihilates it because all moments (s_{\sigma+m}) vanish;
* (B=X^M-1) annihilates it because
  [
  s_{M+m}-s_m=0
  \quad(0\le m\le\sigma-2);
  ]
* (\deg A+\deg B=R+1), so the apolar ideal is exactly ((A,B)).

The color matrix has

[
a_\sigma=b_M=1,
\qquad
\eta_A=0,
\qquad
\eta_B=-1.
]

Hence the reduced color of the coset with label (y) is

[
\boxed{\chi_C=-y.}
]

The map

[
H/K\longrightarrow H^M,\qquad cK\longmapsto c^M
]

is a bijection, so there are exactly

[
\boxed{N=n/M}
]

distinct supports and exactly (N) distinct MCA slopes.

There is no lower (H)-supported representation: the only possible lower locator is (A=X^\sigma), which is nonreduced and supported at (0\notin H).

This is a parameterized counterpacket to any transfer theorem charging the entire support-block family as one MCA color.

---

## 6. Counterpacket II: the critical additive block scale

Let

[
M\ge2,\qquad N\ge4\text{ even},
\qquad n=MN,
]

and choose (F,H,K) as above. Set

[
\sigma=M+1,
\qquad
j=2M,
\qquad
k=n-j-\sigma=M(N-3)-1.
]

Let

[
Y:=H^M,
\qquad |Y|=N.
]

Choose a nonsquare (\varpi\in Y); for cyclic even (Y), a generator is such a choice.

For (y\in Y), define

[
r_y:=y+\frac{\varpi}{y}.
]

The involution

[
y\longmapsto \frac{\varpi}{y}
]

has no fixed points because (\varpi) is nonsquare. For each orbit, form the support

[
T_y=C_y\sqcup C_{\varpi/y},
]

where (C_y) denotes the unique (K)-coset with block label (y).

Its locator is

[
P_y(X,Z)
========

(X^M-yZ^M)
\left(X^M-\frac{\varpi}{y}Z^M\right)
]

or

[
P_y
===

X^{2M}-r_yX^MZ^M+\varpi Z^{2M}.
]

Choose one orbit (y_0), put (r_0=r_{y_0}), and define

[
A=XZ^M,
\qquad
B=X^{2M}-r_0X^MZ^M+\varpi Z^{2M}.
]

Then

[
\Delta=[0]+M[\infty],
\qquad
\Delta^+=[0]+(M+1)[\infty],
]

and

[
\boxed{
P_y
===

B+(r_0-r_y)X^{M-1}A.
}
]

Thus all (T_y) lie in one old generalized-Jacobian support fiber, with constant (B)-coefficient (\gamma_y=1).

An explicit syndrome of length (R=3M) is

[
s_0=1,
\qquad
s_{2M}=-\varpi,
\qquad
s_i=0\quad(i\notin{0,2M}).
]

Indeed:

* (A(X)=X), regarded as a homogeneous form of degree (M+1), annihilates (s) because
  [
  s_1,\ldots,s_{2M-1}=0;
  ]
* (B(X)=X^{2M}-r_0X^M+\varpi) annihilates (s), since at shift zero
  [
  \varpi s_0-r_0s_M+s_{2M}
  =\varpi-\varpi=0,
  ]
  and every other required shift is zero;
* the generator degrees sum to
  [
  (M+1)+2M=3M+1=R+1.
  ]

For the color matrix,

[
a_\sigma=0,\qquad b_j=1,
\qquad
\eta_A=-\varpi,
\qquad
\eta_B=\varpi r_0.
]

The leading cofactor coordinate is

[
u_y=r_0-r_y.
]

Hence

[
\boxed{
\chi_y
======

# -\varpi u_y+\varpi r_0

# \varpi r_y

\varpi\left(y+\frac{\varpi}{y}\right).
}
]

Finally,

[
r_y=r_{y'}
]

implies

[
(y-y')(yy'-\varpi)=0.
]

Therefore either (y=y') or (y'=\varpi/y), which is the same involution orbit. Distinct supports in the packet consequently have distinct slopes.

There are exactly

[
\boxed{\frac N2}
]

supports and exactly (N/2) distinct MCA slopes, although all supports occupy one old (G_\Delta)-fiber.

This is the precise critical additive-color obstruction.

---

## 7. Small exact finite specializations

Both obstructions already occur over (\mathbf F_{17}).

### Multiplicative branch

Take

[
H=\langle2\rangle,\quad |H|=8,
\quad K=\langle4\rangle,\quad |K|=4,
]

[
\sigma=2,\quad j=4,\quad k=2,
]

[
A=X^2,\qquad B=X^4-Z^4.
]

The syndrome is

[
s=(0,1,0,0,0).
]

The two (K)-cosets have labels (1) and (-1=16), and reduced colors

[
16,\qquad1.
]

### Additive branch

Take

[
H=\langle2\rangle,\quad |H|=8,
\quad K={1,-1},\quad |K|=2,
]

[
\sigma=3,\quad j=4,\quad k=1.
]

Let

[
A=XZ^2,
]

[
B=(X^2-Z^2)(X^2-4Z^2).
]

The syndrome is

[
s=(1,0,0,0,13,0).
]

The supports

[
T_1={1,16,2,15},
\qquad
T_2={4,13,8,9}
]

have equal product (4) and equal (e_1=0), hence the same old support class. Their (e_2)-coordinates are respectively

[
12,\qquad5,
]

and their reduced colors are

[
3,\qquad14.
]

All representation coefficients are nonzero; one choice of ordering gives

[
c_{T_1}=c_{T_2}=(12,12,14,14).
]

These examples are structural certificates, not by themselves official finite-prize certificates.

---

## 8. Invariance and edge cases

1. **Coset representative.** Replacing (c) by (cu), (u\in K), leaves
   [
   (cu)^M=c^M.
   ]

2. **Auxiliary form (L_*).** Changing (L_*) multiplies every degree-(j) target by one common group element. It translates the charge measure but preserves its multiplicities and occupied-support cardinality.

3. **Generator shear.** The charge is defined from the actual thickened product (\Phi_\Gamma(T)), so it is unchanged under
   [
   B\mapsto rB+AC,\qquad r\ne0.
   ]

4. **Domain scaling.** Scaling (H) by (a) sends every block label to (a^My). Product and sum labels undergo bijective rescaling, preserving occupancy cardinalities.

5. **Characteristic.** Since (K\le F^\times), (M\mid(q-1)), so the block polynomial is separable. No logarithm, factorial, or characteristic-size hypothesis is used.

6. **Extension fields.** The identity
   [
   \prod_{u\in K}(X-cuZ)=X^M-c^MZ^M
   ]
   is algebraic and survives scalar extension. If the coset divisor is defined over the base field, the block formula descends.

7. **(\sigma=1).** The additive thickening branch has no critical (M=\sigma-1) subgroup. The multiplicative-color obstruction remains valid.

8. **Critical scale.** The additive obstruction occurs only at (M=\sigma-1). For (M\ge\sigma), the added top jet is zero.

9. **Defect normalization.** For a canonical profile, (D) should contain no complete selected (K)-coset; otherwise that coset must be absorbed into the block set. The formulas remain true before canonicalization.

---

## 9. Parameter ledger and finite relevance

| Object                                    | Exact value                                |   |   |
| ----------------------------------------- | ------------------------------------------ | - | - |
| Colored model modulus                     | (\Gamma=[0]+\sigma[\infty])                |   |   |
| Thickened group                           | (F^\times\times(1+zF[z]/z^\sigma))         |   |   |
| Block order                               | (M=                                        | K | ) |
| Quotient block count                      | (N=n/M)                                    |   |   |
| Block label                               | (y(cK)=c^M\in H^M)                         |   |   |
| Block product                             | ((-y,1-yz^M))                              |   |   |
| Multiplicative support-collapse threshold | (M\ge\sigma)                               |   |   |
| Multiplicative surviving color            | (y)                                        |   |   |
| Additive neutral threshold                | (M\ge\sigma)                               |   |   |
| Additive critical scale                   | (M=\sigma-1)                               |   |   |
| Additive surviving color                  | (y), accumulated as (\sum y)               |   |   |
| Multiplicative charge                     | product-image occupancy                    |   |   |
| Critical additive charge                  | sum-image occupancy conditioned on product |   |   |
| Multiplicative counterpacket slopes       | (N)                                        |   |   |
| Critical additive counterpacket slopes    | (N/2)                                      |   |   |

These counterpackets do not kill the scalar support-mass charge: the number of slopes never exceeds the number of support representations. They kill only the claim that one scalar ((K,D)) packet can automatically be charged as one MCA color.

---

## 10. Bankable versus conditional

### Bankable

* The exact thickened block product.
* The multiplicative/additive projection dichotomy.
* The fact that multiplicative-color blocks remain color-active for every (M\ge\sigma).
* The color-neutrality of additive-branch blocks for (M\ge\sigma).
* The critical additive obstruction at (M=\sigma-1).
* The intrinsic pushforward charge (\mu^+_{K,D,\ell}).
* The product and joint product-sum coordinate formulas.
* Both parameterized counterpacket families.
* The conclusion that block packets can produce many distinct slopes.

### Conditional

* A canonical maximal ((K,D)) assignment.
* Finite non-double-counting across different block scales.
* A prize-compatible bound for the critical restricted sum-product image.
* A residual local limit after all block-color profiles have been removed.

---

## 11. Exact failure point

The false implication is

[
\text{block collapses in }G_\Delta
\quad\Longrightarrow\quad
\text{block has one fixed lift in }G_{\Delta+[\beta]}.
]

Its kernel-valued failures are explicit:

[
(-y,1)\in\ker\pi_\times
]

in the multiplicative branch, and

[
(1,1-yz^{\sigma-1})\in\ker\pi_+
]

at the critical additive scale.

Thus scalar support charge and MCA color occupancy are different pushforwards of the same block configurations.

---

## 12. Next exact lemma and route to a full solve

A route remains, but it requires a colored block charge.

The next exact structural lemma should be

```text
L-JR-T1-MAXIMAL-KD-COLOR-PUSHFORWARD-NONOVERLAP
```

It should combine a canonical maximal ((K,D)) assignment with the finite inequality

[
\begin{aligned}
\operatorname{Occ}*{\mathrm{MCA}}(b)
\le;&
\sum*{\text{multiplicative profiles}}
#{p:A^\times_{K,D,\ell}(p)>0}\
&+
\sum_{\text{critical additive profiles}}
#{\tau:A^{\times,+}*{K,D,\ell}(p_b,\tau)>0}\
&+
\sum*{\text{neutral additive profiles}}1
+
N_{\mathrm{residual}}(b).
\end{aligned}
]

The exact new arithmetic wall is

```text
L-JR-T1-CRITICAL-BLOCK-SUM-PRODUCT-OCCUPANCY
```

for

[
\boxed{
V_{Y,E}(\ell,p)
===============

#\left{
\sum_{y\in S}y:
S\in\binom{Y\setminus E}{\ell},
\ \prod_{y\in S}y=p
\right}.
}
]

Here (Y=H^M), and (E) is the set of block labels made unavailable by the defect.

**Do I see a route to a full solve?** Yes, conditionally. First establish canonical maximal ((K,D)) assignment and overlap control. Then replace scalar block mass by the colored pushforward charge above. The only new MCA-specific block obstruction is the finite restricted sum-product occupancy at (M=\sigma-1); outside that scale, the multiplicative product image or a single neutral color gives the exact transfer.
