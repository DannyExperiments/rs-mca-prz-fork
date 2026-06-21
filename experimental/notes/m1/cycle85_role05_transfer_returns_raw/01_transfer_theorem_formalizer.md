BANKABLE_LEMMA

## 1. Executive verdict and confidence

`L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER` is **true after one precise correction**:

> Raw locator occupancy (#{P_T(\beta)}) transfers to distinct MCA slopes only when the supports have a common **exactly normalized** restriction to (\Delta).
> In general the relevant coordinate is (\gamma_T/P_T(\beta)), where
> [
> P_T|*\Delta=\gamma_T B|*\Delta.
> ]

For the Cycle65–84 packet, the required normalization holds with (\gamma_T=1), because all locators have the same six highest homogeneous coefficients. Therefore there is an explicit (t=1) MCA syndrome line whose Cycle84 subpacket contributes exactly

[
52,747,567,092
]

distinct transverse bad slopes.

Thus the bankable mathematical conclusion is

[
\boxed{M_{\operatorname{RS}[F,D,137]}(6)\ge 52,747,567,092.}
]

This is a **finite model/research MCA lower certificate**, not presently a frontier-moving prize certificate. The original (n=256) instance has inadmissible official rate (137/256), and its native target is (T_{\rm line}=0). Even after an exact rate-padding repair and every permitted scalar extension under the strict (q_{\rm line}<2^{256}) cap, the single Cycle84 block is either dominated by the core tangent lower bound or lies below the native target.

**Confidence:** high, (0.98), for the transfer theorem and explicit model corollary; high for the field-normalization and single-block relevance cut.

---

## 2. Exact corrected theorem

### `L-CYCLE85-FIXED-JET-LOCATOR-EVALUATION-TO-MCA-SLOPE`

Let (F) be a finite field, (D\subset F) an (n)-point evaluation domain, and (\beta\in F\setminus D). Let

[
j=n-k-\sigma,\qquad j>\sigma\ge1,
]

and let (\mathcal P\subseteq\binom Dj). For (T\in\mathcal P), write

[
P_T(X)=\prod_{x\in T}(X-x)
]

and homogenize it to a degree-(j) binary form.

Assume there is (T_\star\in\mathcal P) such that

[
X_0^\sigma\mid P_T-P_{T_\star}
\qquad\text{for every }T\in\mathcal P.
\tag{2.1}
]

Equivalently, all (P_T) have the same exact (\sigma)-jet at infinity, not merely the same projective class. Put

[
A=X_0^\sigma,\qquad B=P_{T_\star},\qquad
\Delta=\sigma[\infty],\qquad
\Delta^+=\Delta+[\beta].
]

Then:

1. There is a nonzero syndrome (s) for the extension code
   [
   C^+=\operatorname{RS}[F,D,k+1]
   ]
   whose apolar ideal is
   [
   I_s=(A,B).
   ]

2. Every (T\in\mathcal P) is a full-coordinate degree-(j) representation of (s).

3. For the shifted (t=1) code
   [
   C_\beta
   =======

   \operatorname{ev}*D\bigl((X-\beta)F[X]*{<k}\bigr),
   \qquad
   C^+=C_\beta\oplus F\mathbf1,
   \tag{2.2}
   ]
   there is an affine syndrome line
   [
   \ell(z)=u+zv,\qquad v\ne0,
   ]
   and constants (z_0\in F), (\kappa\in F^\times), such that the incidence supplied by (T) occurs at
   [
   \boxed{
   z_T=z_0+\frac{\kappa}{P_T(\beta)}.
   }
   \tag{2.3}
   ]

4. Every such incidence is transverse:
   [
   v\notin V_T.
   ]

5. Consequently,
   [
   z_T=z_{T'}
   \iff
   P_T(\beta)=P_{T'}(\beta),
   \tag{2.4}
   ]
   and therefore
   [
   \boxed{
   M_{C_\beta}(\sigma)
   \ge
   #{P_T(\beta):T\in\mathcal P}.
   }
   \tag{2.5}
   ]

Since (C_\beta) is diagonally equivalent to the ordinary Reed–Solomon code (\operatorname{RS}[F,D,k]), the same lower bound holds for that RS code.

### Necessary correction in the non-normalized case

If only

[
P_T|*\Delta=\gamma_T B|*\Delta
]

is known, with varying (\gamma_T\in F^\times), then the theorem becomes

[
z_T=z_0+\kappa\frac{\gamma_T}{P_T(\beta)}.
\tag{2.6}
]

Thus raw (P_T(\beta))-occupancy is not sufficient unless (\gamma_T) is constant or the normalized ratios are separately shown to be distinct. This is the first possible transfer failure.

---

## 3. Explicit Cycle84 instantiation and proof

### 3.1 Field, domain and parameters

Let

[
F=\mathbf F_{17}[\theta]/(\theta^{16}+\theta^8+3),
]

[
\eta=6\theta^9,\qquad
D=\langle\eta\rangle=\mu_{256},
\qquad
\beta=\theta+2.
]

The replay certificates establish that (\eta) has order (256) and that (\beta\notin D). Hence

[
|D|=256.
]

Take

[
n=256,\qquad k=137,\qquad \sigma=6,\qquad j=113,
]

so that

[
R=n-k-1=118=j+\sigma-1.
]

The shifted normal form is

[
E=X-\beta,\qquad B_0=1,
]

[
C_\beta=\operatorname{ev}*D(EF[X]*{<137}),
\qquad
C^+=C_\beta\oplus F\mathbf1
=\operatorname{RS}[F,D,138].
]

### 3.2 Exact support packet and its shell color

Define

[
\begin{aligned}
E_1&={0,1,2,3,5,11,12,13},\
E_2&={0,1,2,3,4,8,9,14},\
E_3&={0,1,2,4,5,7,11,14}
\end{aligned}
]

inside (\mathbf Z/16\mathbf Z). For (i\in{1,2,3}) and (a\in\mathbf Z/16\mathbf Z), put

[
B(i,a)=a+E_i
]

and

[
S_t(i,a)=
\left{
\eta^{t+8b},-\eta^{t+8b}:b\in B(i,a)
\right},
\qquad 1\le t\le7.
]

The packet-shell color is

[
r(i,a)=s_i+8(a\bmod2)\pmod{16},
\qquad
(s_1,s_2,s_3)=(15,9,12).
]

For a seven-tuple (\omega=((i_t,a_t))_{t=1}^7), define

[
T_\omega
========

{1}\cup\bigcup_{t=1}^7 S_t(i_t,a_t).
]

The seven slot residue classes are disjoint, so (|T_\omega|=113). Define

[
\mathcal P_0
============

\left{
T_\omega:
\sum_{t=1}^7 r(i_t,a_t)=4\pmod{16}
\right}.
]

Then

[
|\mathcal P_0|
==============

52,747,567,104.
]

This (\mathbf Z/16)-valued shell color is not the MCA color. It is the finite filter defining the product packet. In particular, it fixes the scalar product:

[
\prod_{x\in T}x
===============

# \eta^{16(1+\cdots+7+\sum_t r_t)}

# \eta^{16(28+4)}

1.

]

### 3.3 The common (\Delta)-fiber

Cycle67 proves that every (T\in\mathcal P_0) satisfies

[
e_1(T)=1,
\qquad
e_2(T)=e_3(T)=e_4(T)=e_5(T)=0.
]

Therefore all degree-(113) locators have the same six highest homogeneous coefficients. Hence, for any fixed (T_\star\in\mathcal P_0),

[
X_0^6\mid P_T-P_{T_\star}.
]

Set

[
A=X_0^6,\qquad B=P_{T_\star}.
]

Since (B) is monic at infinity,

[
\gcd(A,B)=1.
]

Also,

[
\deg A+\deg B=6+113=119=R+1.
]

Thus ((A,B)) is an Artinian binary complete intersection with socle degree (117=R-1). Macaulay duality supplies a nonzero functional, equivalently a nonzero extension-code syndrome (s), satisfying

[
I_s=(A,B).
]

For every (T\in\mathcal P_0),

[
P_T=A U_T+B.
\tag{3.1}
]

The coefficient of (B) is exactly (1). Since (j>\sigma), Cycle62’s full-coordinate criterion says precisely that this nonzero coefficient makes (T) a full-coordinate representation.

The lower generator (A=X_0^6) is nonreduced, supported at infinity, and is not a squarefree (D)-locator. Therefore

[
\varepsilon_A=0.
]

### 3.4 Locator evaluation is exactly the thickened lift

Put

[
\rho_\beta(T)=P_T(\beta)=\prod_{x\in T}(\beta-x).
]

Because (\beta\notin D),

[
\rho_\beta(T)\ne0.
]

Let

[
g_T=
\left[
\left.\frac{P_T}{L_*^{113}}\right|*{\Delta^+}
\right]
\in G*{\Delta^+},
]

where (L_*) is nonvanishing on (\Delta^+).

For (T,T'\in\mathcal P_0), suppose (g_T=g_{T'}). Equality in the quotient by (F^\times) means

[
P_T|*{\Delta^+}=cP*{T'}|_{\Delta^+}
]

for some (c\in F^\times). Restricting to (\Delta), where both restrictions equal (B|_\Delta), gives (c=1). Restricting to ([\beta]) then gives

[
P_T(\beta)=P_{T'}(\beta).
]

The converse is immediate: common restriction on (\Delta) together with equal evaluation at (\beta) gives equal restrictions on the disjoint scheme

[
\Delta^+=\Delta\sqcup[\beta].
]

Hence

[
\boxed{
g_T=g_{T'}
\iff
\rho_\beta(T)=\rho_\beta(T').
}
\tag{3.2}
]

Cycle62, equation (4.4), gives

[
T,T'\text{ have the same MCA slope}
\iff
g_T=g_{T'}.
]

Combining this with (3.2) proves exact slope/evaluation equivalence.

For the explicit affine formula, make the projective substitution

[
Y=(X-\beta)^{-1}.
]

The transformed monic locator is

[
Q_T(Y)
======

\frac{Y^{113}P_T(\beta+Y^{-1})}{P_T(\beta)}.
]

The numerator modulo (Y^6) is independent of (T), because it depends only on the six highest coefficients of (P_T). Thus the old scalar lift after transformation is a fixed nonzero multiple of (1/\rho_\beta(T)). Cycle62 equation (3.8) then gives

[
z_T=z_0+\frac{\kappa}{\rho_\beta(T)},
\qquad
\kappa\ne0.
]

### 3.5 Nonzero direction and transversality

The direction is the class of (\mathbf1) modulo

[
C_\beta=\operatorname{ev}*D((X-\beta)F[X]*{<137}).
]

It is nonzero. Otherwise there would be (f), (\deg f<137), such that

[
1=(x-\beta)f(x)
]

on all (256) points of (D). The polynomial (1-(X-\beta)f(X)), of degree at most (137), would have (256) roots and hence vanish identically, contradicting its value (1) at (X=\beta).

Now fix (T\in\mathcal P_0). If the direction lay in (V_T), some error vector supported on (T) would have the same syndrome as (\mathbf1). Thus, for some (f) of degree (<137),

[
1=(x-\beta)f(x)
]

on the agreement set (D\setminus T), whose size is

[
256-113=143=k+\sigma.
]

Again (1-(X-\beta)f(X)) has degree at most (137) but (143) roots, and evaluation at (\beta) supplies the contradiction. Therefore

[
v\notin V_T
]

for every packet support.

No occupied value is lost to contained incidences.

### 3.6 Exact transferred count

Cycle84 proves

[
#{\rho_\beta(T):T\in\mathcal P_0}
=================================

52,747,567,092,
]

with (52,747,567,080) singleton fibers and (12) double fibers.

Therefore, on the explicitly constructed line,

[
\boxed{
#{z_T:T\in\mathcal P_0}
=======================

52,747,567,092.
}
]

Consequently,

[
\boxed{
M_{\operatorname{RS}[F,D,137]}(6)
\ge
52,747,567,092.
}
\tag{3.3}
]

This is a lower bound, not an equality for the full MCA numerator: supports outside (\mathcal P_0) may add further slopes.

---

## 4. Exact ledger status and verification requirements

### 4.1 Raw Cycle84 research entry

The correct raw entry is:

```text
theorem_id: L-CYCLE85-FIXED-JET-LOCATOR-EVALUATION-TO-MCA-SLOPE
term_type: packet.explicit_mca_slope_set
objective: mca
direction: lower
scope: whole_numerator
profile: research

n:       256
k:       137
r:       119
sigma:   6
j:       113

q_gen:   17^16 = 48,661,191,875,666,868,481
q_code:  17^16
q_line:  17^16
q_chal:  unused / externally unspecified

T_code:  floor(17^16 / 2^128) = 0
T_line:  floor(17^16 / 2^128) = 0

lower_bound_at_sigma_6: 52,747,567,092
row_status: RESEARCH_MODEL_FAIL
```

The domain generates all of (\mathbf F_{17^{16}}): the order of (17) modulo (256) is (16), so a primitive (256)-th root cannot lie in a proper subfield.

The comparison

[
52,747,567,092>2^{32}
]

is not the native prize comparison. The native integer comparison is

[
52,747,567,092>T_{\rm line}=0.
]

Because (T_{\rm line}=0), the core unit lower bound already makes every reserve fail. Thus the Cycle84 term is leave-one-out **subfrontier redundant** in this raw research ledger.

The current instance also fails official profile validation because

[
\frac{k}{n}=\frac{137}{256}
\notin
\left{\frac12,\frac14,\frac18,\frac1{16}\right}.
]

### 4.2 Separate scalar-list statement

The scalar-list object is different. The same complete-intersection construction gives at least

[
|\mathcal P_0|=52,747,567,104
]

errors of weight (113) in one syndrome fiber of the extension code

[
\operatorname{RS}[F,D,138]
]

at scalar reserve

[
256-138-113=5.
]

That statement uses the support count (|\mathcal P_0|), not the occupancy count. Cycle84’s (m_{\max}=2) computation does not strengthen that scalar numerator.

### 4.3 Exact rate-padding lemma

Rate mismatch alone can be repaired without losing occupancy.

Choose any set

[
S\subset F\setminus(D\cup{\beta}),
\qquad |S|=18,
]

and put

[
D'=D\cup S,\qquad
\mathcal P_0'={T\cup S:T\in\mathcal P_0}.
]

Then

[
n'=274,\qquad
j'=131,\qquad
k'=n'-j'-6=137,
]

so

[
\frac{k'}{n'}=\frac12.
]

Writing (Q_S(X)=\prod_{s\in S}(X-s)),

[
P_{T\cup S}=Q_SP_T,
]

so the common six-jet remains fixed and

[
P_{T\cup S}(\beta)=Q_S(\beta)P_T(\beta).
]

Because (Q_S(\beta)\ne0), occupancy is unchanged:

[
#{P_{T\cup S}(\beta)}
=====================

52,747,567,092.
]

This is an exact rate-padding construction, but it does not make the single block frontier-relevant.

### 4.4 Single-block field-normalization route cut

Any finite line field containing (D) must contain (\mathbf F_{17^{16}}). Hence

[
q_{\rm line}=17^d,\qquad 16\mid d.
]

Under the strict official cap (q_{\rm line}<2^{256}), only

[
d\in{16,32,48}
]

are possible.

| (q_{\rm line}) | (T_{\rm line}=\lfloor q_{\rm line}/2^{128}\rfloor) | Single-block status                      |
| -------------: | -------------------------------------------------: | ---------------------------------------- |
|      (17^{16}) |                                                (0) | core unit lower already dominates        |
|      (17^{32}) |                                                (6) | core tangent lower (j\ge113>6) dominates |
|      (17^{48}) |                      (338,617,018,271,848,945,628) | (52,747,567,092<T_{\rm line})            |

Therefore:

[
\boxed{
\text{No permitted scalar extension makes the single Cycle84 block
leave-one-out frontier-relevant.}
}
]

Changing (q_{\rm chal}) cannot alter this conclusion.

### 4.5 Required transfer checker

The exact repository artifact should be:

```text
V-CYCLE85-FIXED-JET-RHO-TO-MCA-SLOPE
```

with output decision

```text
CYCLE85_FIXED_JET_OCCUPANCY_TRANSFER_VERIFIED
```

It must verify, without rerunning the Cycle84 census:

1. irreducibility of (X^{16}+X^8+3);
2. order (256) of (\eta) and (\beta\notin D);
3. the 336 slot definitions and disjoint support structure;
4. (|T|=113) and the shell-color condition;
5. the exact identities (e_1=1), (e_2=\cdots=e_5=0);
6. (A=X_0^6), (B=P_{T_\star}), (\gcd(A,B)=1);
7. the complete-intersection degree identity (6+113=119);
8. full-coordinate status;
9. (\rho_\beta(T)\ne0);
10. the exact slope formula or the equivalent (G_{\Delta^+})-class equivalence;
11. nonzero direction and transversality;
12. the Cycle84 certificate hashes and exact occupancy;
13. separate `q_gen`, `q_code`, `q_line`, and `q_chal`;
14. research versus official profile status and leave-one-out relevance.

No new MITM enumeration is required.

---

## 5. Next exact lemma or construction

The full model transfer is solved. The first plausible frontier-moving construction is not another single-block normalization; that route is cut by the field-degree table above.

The next exact target is:

```text
L-CYCLE85-TWO-BLOCK-Q48-DELTA-PLUS-OCCUPANCY
```

Construct over

[
K=\mathbf F_{17^{48}}
]

two disjoint embedded Cycle84 blocks whose combined degree-(226) locators retain a common six-jet and whose combined locator-evaluation map has maximum fiber at most (8). After adding (48) fixed support/domain points, the parameters become

[
n=560,\qquad k=280,\qquad \sigma=6,\qquad j=274,
\qquad \frac kn=\frac12.
]

The exact native target is

[
T_{48}
======

338,617,018,271,848,945,628.
]

A two-block packet has

[
|\mathcal P_0|^2
================

2,782,305,835,390,982,946,816
]

support pairs. Therefore the exact sufficient multiplicity theorem is

[
\boxed{m_{\max}^{(2)}\le8,}
]

because

[
\frac{|\mathcal P_0|^2}{8}
==========================

347,788,229,423,872,868,352

>

T_{48}.
]

At these parameters the tangent lower (j=274) is far below (T_{48}), so such a packet would genuinely move the certified failure frontier. The checker must either emit this (\le8) certificate or a concrete (9)-fold collision for the proposed two-block embedding.

---

## 6. Self-audit

### 1. What exact implication did I prove, and what did I not prove?

Proved:

[
\operatorname{Occ}(\beta)=52,747,567,092
\Longrightarrow
M_{\operatorname{RS}[F,D,137]}(6)
\ge52,747,567,092
]

for the explicit Cycle84 field/domain, via one constructed transverse (t=1) syndrome line.

Not proved:

* equality with the full MCA numerator;
* an MCA upper theorem;
* an official frontier value;
* a scalar-list conclusion derived from occupancy;
* tensor multiplicativity;
* a frontier-moving official counterpacket.

### 2. Is the result official-prize-relevant?

The raw (n=256) result is only a finite/model/research MCA certificate. It fails the official rate profile and has (T_{\rm line}=0).

Rate padding can produce a locally official-rate candidate, but the single block remains leave-one-out irrelevant for every permitted scalar extension under the strict field cap.

### 3. What is the first line where the theorem could fail?

The first mathematical failure point is

[
P_T|*\Delta=\gamma_TB|*\Delta
\quad\Longrightarrow\quad
\text{raw }P_T(\beta)\text{ determines color}.
]

That implication is false when (\gamma_T) varies. The correct coordinate is

[
\frac{\gamma_T}{P_T(\beta)}.
]

For (\mathcal P_0), the exact shared jet gives (\gamma_T=1), so the failure does not occur.

The first prize-promotion failure for the raw instance is official rate validation.

### 4. Are the four fields and the (2^{-128}) target used correctly?

Yes.

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}
]

for the native model; (q_{\rm chal}) is unused. MCA uses

[
T_{\rm line}=\left\lfloor q_{\rm line}/2^{128}\right\rfloor,
]

not (q_{\rm code}), (q_{\rm gen}), (q_{\rm chal}), or (2^{32}). Here (T_{\rm line}=0).

### 5. Can quotient structure, containment, collisions or affine normalization reduce the numerator?

No further reduction occurs.

* Quotient by (F^\times): neutralized by the common exact (\Delta)-restriction.
* Periodic/configuration quotients: may classify the packet for upper-bound accounting, but do not identify actual slopes.
* Containment: impossible by the (143)-zero polynomial argument.
* Same-slope collisions: exactly the twelve Cycle84 double fibers; they are already deducted in (\operatorname{Occ}(\beta)).
* Affine color normalization: a bijection, so it preserves collision classes.
* Nonreduced (\Delta): explicitly allowed by Cycle62.
* Denominators: (P_T(\beta)\ne0).

### 6. What converts this into repository-level PROOF?

This answer is not a PLAN. The mathematics is complete subject to the banked Cycle67 shared-jet identities. The exact remaining artifact is the deterministic bridge checker

```text
V-CYCLE85-FIXED-JET-RHO-TO-MCA-SLOPE
```

and its trusted-registry entry for

```text
L-CYCLE85-FIXED-JET-LOCATOR-EVALUATION-TO-MCA-SLOPE.
```

The next mathematical construction required for a frontier-moving result is the two-block (q_{\rm line}=17^{48}), maximum-fiber-(8) theorem stated above.
