BANKABLE_LEMMA

## 1. Executive verdict and confidence

The exact Cycle62→Cycle84 bridge is valid, with one correction:

[
\rho_\beta(T)=P_T(\beta)
]

is not literally the numerical reduced color in the original affine gauge. It is an exact coordinate on the relevant (\Delta^+)-lift fiber. After normalizing coordinates so that (\beta) is the external point at infinity, the reduced color has the form

[
\chi_T=a+\frac{b}{\rho_\beta(T)},\qquad b\ne0.
]

Consequently,

[
\rho_\beta(T)=\rho_\beta(T')
\iff
\Delta^+\text{-lift}(T)=\Delta^+\text{-lift}(T')
\iff
\chi_T=\chi_{T'}
\iff
z_T=z_{T'}.
]

Thus Cycle84 proves the exact finite MCA lower certificate

[
M_{C_0}(6)\ge 52,747,567,092
]

for an explicit (n=256,k=137) RS model.

More strongly, a two-copy generic-translation construction amplifies this to

[
52,747,567,092^2
================

2,782,305,834,125,041,336,464
]

distinct transverse slopes in an official-rate (1/2) instance over
(\mathbf F_{17^{48}}). This exceeds the correct native MCA target

[
\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor
================================================

338,617,018,271,848,945,628.
]

Therefore there is an official-profile existential counterpacket theorem, although a concrete good-translation/domain digest has not yet been materialized into a public checker certificate.

**Confidence:** high for the exact bridge and the two-copy existence proof; moderate-high for immediate registry integration because the final finite witness has not been serialized.

---

## 2. Exact theorem and checker statements

### Theorem 1 — exact Cycle85 occupancy transfer

Put

[
F_0=\mathbf F_{17}[X]/(X^{16}+X^8+3),
\quad
\eta=6X^9,
\quad
D=\langle\eta\rangle=\mu_{256},
\quad
\beta=X+2.
]

Let (\mathcal P_0\subseteq\binom D{113}) be the Cycle65–68 support packet. Define

[
\rho_\beta(T)=\prod_{x\in T}(\beta-x)=P_T(\beta).
]

Then there is a nonzero syndrome for

[
C_0=\operatorname{RS}[F_0,D,137]
]

and a shifted (t=1) affine syndrome line (\ell) at reserve

[
n=256,\quad k=137,\quad r=119,\quad \sigma=6,\quad j=113
]

such that:

1. every (T\in\mathcal P_0) is a full-coordinate degree-(113) representation;
2. every resulting incidence is transverse/noncontained;
3. for (T,T'\in\mathcal P_0),
   [
   z_T=z_{T'}
   \iff
   \rho_\beta(T)=\rho_\beta(T');
   ]
4. hence the explicit subpacket has exactly
   [
   52,747,567,092
   ]
   distinct bad slopes.

Therefore

[
\boxed{
M_{C_0}(6)\ge52,747,567,092.
}
]

This is a lower bound on the whole MCA numerator, not an equality for the whole numerator.

---

### Theorem 2 — two-copy official-rate amplification

Let

[
N=52,747,567,092.
]

There exists an explicit-in-principle field

[
E=\mathbf F_{17^{48}},
]

an affine domain (L\subset E) of size (560), and a code

[
C=\operatorname{RS}[E,L,280]
]

with official rate

[
\frac{k}{n}=\frac{280}{560}=\frac12,
]

such that at

[
r=280,\qquad \sigma=6,\qquad j=274
]

one shifted (t=1) syndrome line has at least (N^2) distinct transverse bad slopes:

[
\boxed{
M_C(6)\ge N^2
=============

2,782,305,834,125,041,336,464.
}
]

Since

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_{\rm chal}=17^{48}
]

may be used, the native target is

[
T_{\rm line}
============

# \left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor

338,617,018,271,848,945,628,
]

and therefore

[
M_C(6)>T_{\rm line}.
]

Within `RS-PRIZE-FRONTIER-V1`, this gives `FAIL` at reserve (6), conditional only on materializing the concrete translation and domain certificate.

A corresponding lower-term entry is:

```json
{
  "theorem_id": "L-CYCLE85-TWO-COPY-GENERIC-TRANSLATE-OCCUPANCY",
  "objective": "mca",
  "direction": "lower",
  "scope": "whole_numerator",
  "profile": "proximity-prize-2026-v1",
  "official": true,
  "n": "560",
  "k": "280",
  "sigma": "6",
  "j": "274",
  "q_gen": "115225400457255426923013053222916919834651165519677685328641",
  "q_code": "115225400457255426923013053222916919834651165519677685328641",
  "q_line": "115225400457255426923013053222916919834651165519677685328641",
  "q_chal": "115225400457255426923013053222916919834651165519677685328641",
  "T_line": "338617018271848945628",
  "lower_bound": "2782305834125041336464",
  "term_type": "packet.explicit_mca_slope_set",
  "expected_decision": "FAIL",
  "registry_state": "PENDING_CONCRETE_DOMAIN_CERTIFICATE"
}
```

No scalar-list conclusion follows, even though (q_{\rm code}=q_{\rm line}) in this amplified instance.

---

## 3. Proof and construction

### 3.1 The Cycle65 packet is one exact (\Delta)-support fiber

Use homogeneous coordinates in which finite (x\in F_0) is ([1:x]), infinity is ([0:1]), and

[
P_T^h(X_0,X_1)
==============

\prod_{x\in T}(X_1-xX_0).
]

Cycle67 proves that every (T\in\mathcal P_0) has

[
e_1(T)=1,
\qquad
e_2(T)=e_3(T)=e_4(T)=e_5(T)=0.
]

Hence

[
P_T^h
=====

X_1^{113}-X_0X_1^{112}
+X_0^6(\cdots),
]

so all (P_T^h) have the same restriction to

[
\Delta=6[\infty]=V(X_0^6).
]

Set

[
A=X_0^6.
]

Choose one (T_*\in\mathcal P_0) and set

[
B=P_{T_*}^h.
]

Because (B(0,1)=1),

[
\gcd(A,B)=1.
]

For every (T\in\mathcal P_0),

[
P_T^h-B
]

is divisible by (X_0^6), and therefore

[
P_T^h=A,U_T+B.
]

Thus the Cycle62 decomposition scalar is (\gamma_T=1) in this original coordinate system. Since (\gamma_T\ne0), every support is full-coordinate.

To construct the syndrome rigorously, let

[
S=F_0[X_0,X_1],
\qquad
Q=S/(A,B).
]

This is an Artinian complete intersection with socle degree

[
6+113-2=117.
]

Choose a nonzero functional on (Q_{117}). The perfect complete-intersection pairing gives an apolar functional whose annihilator is exactly

[
I_s=(A,B).
]

Its values on the degree-(117) monomial basis give a nonzero syndrome of length (118), as required by

[
R=j+\sigma-1=118.
]

This closes the first vulnerable implication:

[
\text{Cycle62 Role05 theorem}
\longrightarrow
\text{Cycle65 support packet}.
]

---

### 3.2 (\rho_\beta) is exactly the (\Delta^+)-lift coordinate

Cycle84 verifies

[
\beta^{256}\ne1,
]

so

[
\beta\notin D=\mu_{256}.
]

It is also finite and distinct from infinity. Hence

[
\Delta^+
========

6[\infty]+[\beta]
]

is a disjoint thickening.

Take (L_*=X_1), which is nonzero both at infinity and at (\beta=X+2). At infinity, with local parameter (t=X_0/X_1),

[
\frac{P_T^h}{X_1^{113}}
=======================

\prod_{x\in T}(1-xt)
\equiv
1-t
\pmod{t^6}.
]

At the external point,

[
\left.\frac{P_T^h}{X_1^{113}}\right|_\beta
==========================================

# \frac{P_T(\beta)}{\beta^{113}}

\frac{\rho_\beta(T)}{\beta^{113}}.
]

Thus the lift class is represented under Chinese remaindering by

[
g_T=
\left[
\left(
1-t,,
\frac{\rho_\beta(T)}{\beta^{113}}
\right)
\right]
\in
G_{\Delta^+}.
]

If (g_T=g_{T'}), there is a diagonal scalar (c\in F_0^\times) relating the two representatives. Comparing the constant term of the infinity jet gives (c=1). Therefore

[
g_T=g_{T'}
\iff
\rho_\beta(T)=\rho_\beta(T').
]

So Cycle84 counted actual occupied (\Delta^+)-lift classes, not a quotient or proxy for them.

---

### 3.3 Same (\rho_\beta) means exactly the same slope

Cycle62 Theorem C gives a bijection

[
\chi\longmapsto b_\chi^+
]

between admissible reduced colors and the lift fiber above the fixed (\Delta)-support class. Hence

[
g_T=g_{T'}
\iff
\chi_T=\chi_{T'}.
]

Actual slopes are

[
z_T=\lambda(w)+\chi_T,
]

so translation by the common (\lambda(w)) preserves equality:

[
z_T=z_{T'}
\iff
\chi_T=\chi_{T'}.
]

The raw value (\rho_\beta(T)) is not generally identical to (\chi_T). To see the exact relationship, perform the projective change

[
Y_0=X_1-\beta X_0,
\qquad
Y_1=X_0,
]

which sends (\beta) to infinity. The coefficient of (Y_1^{113}) in the transformed locator is (P_T(\beta)=\rho_\beta(T)), so monic normalization divides the transformed locator by (\rho_\beta(T)).

If (\rho_*=\rho_\beta(T_*)), the transformed Cycle62 scalar is therefore

[
\gamma_T'=\frac{\rho_*}{\rho_\beta(T)}.
]

Since the transformed external point is outside the transformed support modulus, Cycle62 Theorem B gives

[
\chi_T
======

# \chi_A+\kappa\gamma_T'

\chi_A+\kappa\frac{\rho_*}{\rho_\beta(T)},
\qquad \kappa\ne0.
]

Thus (\rho_\beta\mapsto\chi) is inverse-affine and injective on (F_0^\times). An augmented-row gauge change merely composes this with another common affine bijection.

---

### 3.4 Full-coordinate admissibility and noncontainment

All supports have exactly (113) distinct points:

* the seven slot cosets are disjoint;
* their (112) roots are distinct;
* the anchor (1) is outside those (112) roots;
* Cycle68 proves tuple-to-support injectivity.

Also

[
T\cap\operatorname{Supp}\Delta=\varnothing
]

because (\operatorname{Supp}\Delta={\infty}) and (D\subset F_0^\times).

Noncontainment is automatic. In the shifted presentation, write the full parity check as the (118)-row matrix (H) plus one augmented row. The line direction is the last coordinate vector. If that direction lay in the span of the augmented columns indexed by (T), some coefficient vector (d) would satisfy

[
H_Td=0.
]

But

[
|T|=113\le118,
]

and every (113)-column submatrix of the RS parity check is independent. Hence (d=0), contradicting that the resulting vector is the nonzero line direction.

Therefore every counted slope is transverse. Each support span meets the line in at most one parameter, so there is no same-witness or common-envelope multiplicity loss.

---

### 3.5 Direct Cycle84 consequence

The public replay proves

[
#{\rho_\beta(T):T\in\mathcal P_0}
=================================

52,747,567,092.
]

Sections 3.1–3.4 prove that this is exactly the number of distinct slopes furnished by the explicit subpacket. Therefore

[
M_{C_0}(6)\ge52,747,567,092.
]

The (12) double fibers are already accounted for. No quotient, affine gauge, containment condition, or support duplication causes a further loss.

---

### 3.6 Why one unamplified copy does not move the official frontier

The original rate is

[
\frac{137}{256},
]

which is outside the official set.

There is a simple fixed-support padding operation. Add (m) new domain points and put every one of them into every support. If (Q) is their fixed locator, replace

[
P_T\mapsto QP_T,\qquad B\mapsto QB.
]

Then (n) and (j) both increase by (m), while (k), (\sigma), full-coordinate status, and lift occupancy are unchanged.

Taking (m=18) gives

[
n=274,\quad k=137,\quad j=131,\quad \sigma=6,
\quad \frac{k}{n}=\frac12.
]

However, any line field containing (F_0) has degree divisible by (16). Under the strict condition (q_{\rm line}<2^{256}), the only possibilities are

[
q_{\rm line}=17^{16},\quad17^{32},\quad17^{48}.
]

Their targets are respectively

[
0,\qquad6,\qquad338,617,018,271,848,945,628.
]

For the first two fields, the core tangent lower bound

[
M_C(6)\ge j=131
]

already exceeds the target; the Cycle84 occupancy term is leave-one-out redundant. For the third field,

[
52,747,567,092
<
338,617,018,271,848,945,628.
]

Thus one copy can be made official-rate, but cannot be both threshold-decisive and frontier-moving.

This proves that the informal comparison

[
\operatorname{Occ}(\beta)>2^{32}
]

is only a research/tensor-block benchmark. It is not a native prize comparison for any admissible line field containing (F_0) under the strict cap.

---

### 3.7 Exact two-copy amplification

Let

[
\mathcal V
==========

{\rho_\beta(T):T\in\mathcal P_0},
\qquad |\mathcal V|=N.
]

For each (v\in\mathcal V), choose one support (T_v) satisfying

[
P_{T_v}(\beta)=v.
]

Work in

[
E=\mathbf F_{17^{48}},
]

viewed as a cubic extension of (F_0). One explicit field model is

[
E=F_0[\theta]/(\theta^3-\beta):
]

exact arithmetic gives

[
\beta^{(17^{16}-1)/3}=2+5X^8\ne1,
]

so (\beta) is not a cube in (F_0), and (\theta^3-\beta) is irreducible.

Consider the (N^2) polynomials

[
F_{v,w}(Y)=vP_{T_w}(Y),
\qquad (v,w)\in\mathcal V^2.
]

They are pairwise distinct. Indeed, if

[
vP_{T_w}=v'P_{T_{w'}}
]

as polynomials, comparison of leading coefficients gives (v=v'); monicity then gives (P_{T_w}=P_{T_{w'}}), hence (w=w').

Every difference has degree at most (113). Therefore the number of (y\in E) at which two values collide is at most

[
113\binom{N^2}{2}.
]

Also exclude:

* (y\in D), to keep every evaluation nonzero;
* (y\in\beta-(D-D)), so that (D) and ((\beta-y)+D) are disjoint;
* every proper subfield of (E), so that the resulting domain generates (E).

The exact inequality

[
113\binom{N^2}{2}
+256+65536
+\sum_{\substack{d\mid48\d<48}}17^d
<
17^{48}
]

holds. The dominant collision term is approximately (4.374\times10^{44}), while

[
17^{48}\approx1.152\times10^{59}.
]

Hence a good (y\in E) exists.

Put

[
c=\beta-y,
\qquad
D_1=D,
\qquad
D_2=c+D.
]

For a pair ((v,w)), use the support

[
T_v\cup(c+T_w).
]

Its locator evaluation at (\beta) is

[
P_{T_v}(\beta),P_{c+T_w}(\beta)
===============================

vP_{T_w}(y).
]

By construction these values are pairwise distinct, giving (N^2) occupied evaluations.

The common-jet property survives translation. If

[
J_T(t)=\prod_{x\in T}(1-xt)\equiv1-t\pmod{t^6},
]

then

[
J_{c+T}(t)
==========

(1-ct)^{113}
J_T!\left(\frac{t}{1-ct}\right)
\pmod{t^6},
]

which is independent of (T) modulo (t^6). Therefore every two-block locator has the same restriction to (6[\infty]).

Finally add (48) fixed domain points to every support. Then

[
n=512+48=560,
\qquad
j=226+48=274,
\qquad
k=n-j-\sigma=280.
]

The fixed locator multiplies every evaluation by the same nonzero scalar, so the (N^2) occupancy is unchanged.

Choosing (y) outside all proper subfields ensures that the generated domain field is (E). All official rate, field-cap, reserve, external-point, full-coordinate, and transversality hypotheses now hold.

---

## 4. Verification requirements

The direct transfer can be registered after a checker verifies:

1. the field modulus and the order-(256) element;
2. (\beta^{256}\ne1);
3. support size, disjoint slot cosets, and tuple-to-support injectivity;
4. the common identities (e_1=1,e_2=\cdots=e_5=0);
5. the divisibility
   [
   X_0^6\mid P_T-P_{T_*};
   ]
6. the exact Cycle84 occupancy certificate;
7. the equality of lift classes iff locator evaluations agree;
8. the inverse-affine color relation;
9. full-coordinate status and transversality.

For the official amplified packet, the checker additionally needs:

1. a field certificate for (E/F_0);
2. a concrete good (y), or acceptance of the generic-translation existence theorem;
3. the two-copy domain and fixed-padding domain digest;
4. verification that (y) has full degree (48);
5. the code fingerprint ((n,k)=(560,280));
6. native target calculation from (q_{\rm line}=17^{48});
7. registration of the new lower theorem.

The Cycle84 MITM computation does not need to be rerun.

---

## 5. Next exact construction

The transfer theorem itself is closed. The next exact task is:

```text
V-CYCLE85-TWO-COPY-GOOD-TRANSLATE-AND-LEDGER
```

It must materialize one (y\in\mathbf F_{17^{48}}), the (48) fixed padding points, and the resulting ordered-domain digest, then emit the official lower-term entry above.

Its decisive checks are exactly:

[
\begin{aligned}
&[F_{17}(y):F_{17}]=48,\
&y\notin D,\
&\beta-y\notin D-D,\
&vP_{T_w}(y)\ne v'P_{T_{w'}}(y)
\quad\text{for all distinct }(v,w),(v',w'),\
&M_C(6)\ge N^2>T_{\rm line}.
\end{aligned}
]

A theorem-registry implementation may replace the enormous final universal check by the proved nonzero-polynomial/root-union argument.

---

## Self-audit

### 1. Exact implication proved and not proved

Proved:

[
\operatorname{Occ}(\beta)=52,747,567,092
\Longrightarrow
M_{C_0}(6)\ge52,747,567,092.
]

Also proved existentially:

[
M_C(6)\ge
52,747,567,092^2

>

\left\lfloor17^{48}/2^{128}\right\rfloor
]

for an official-rate (1/2) code over (\mathbf F_{17^{48}}).

Not proved:

* equality for the whole MCA numerator;
* any scalar or interleaved-list numerator bound;
* an MCA upper theorem;
* the exact first safe reserve or full prize frontier;
* a public serialized certificate for the amplified good translation.

### 2. Official-prize relevance

The original (n=256,k=137) statement is only a finite/model/research certificate.

One-copy rate padding is official-profile admissible but frontier-redundant.

The two-copy generic-translation theorem is official-profile and threshold-relevant, but is not yet a public checker-certified counterpacket.

### 3. First possible failure line

Before this audit, the first vulnerable line was

[
\text{Cycle62 Role05}
\longrightarrow
\text{Cycle65 packet},
]

specifically the claim that the packet lies in one (\Delta)-support fiber and that (\rho_\beta) supplies the added (\Delta^+) coordinate. The choice

[
A=X_0^6
]

and the shared locator jet prove both facts.

The first remaining implementation failure is now the passage from the existential good translation to a concrete domain fingerprint.

### 4. Use of (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal})

For the original packet,

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16},
\qquad
T_{\rm line}=0.
]

The domain generates all of (F_0) because an element of order (256) over (\mathbf F_{17}) has degree

[
\operatorname{ord}_{256}(17)=16.
]

The challenge field is unused and cannot pay any denominator.

For the amplified official packet,

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_{\rm chal}=17^{48},
]

and the comparison is correctly made against

[
T_{\rm line}
============

\left\lfloor17^{48}/2^{128}\right\rfloor.
]

The comparison (\operatorname{Occ}>2^{32}) is not used as a prize target.

### 5. Possible numerator reductions

* **Quotient/periodic structure:** cannot identify distinct actual lift classes; it can only classify or charge them in an upper-bound program.
* **Contained incidences:** absent by MDS independence/noncontainment.
* **Same-slope collisions:** exactly the Cycle84 (\rho)-fibers; all are already counted.
* **Affine normalization:** bijective and causes no loss.
* **Projective scalar quotient:** the fixed infinity jet forces the scalar to be (1).
* **Fixed padding:** multiplies every lift value by one common nonzero factor.
* **Two-copy collisions:** excluded by the generic-translation root argument.

### 6. Conversion to public PROOF or COUNTERPACKET

This answer is not a PLAN. The exact remaining conversion task is the checker

```text
V-CYCLE85-TWO-COPY-GOOD-TRANSLATE-AND-LEDGER
```

with a concrete full-degree translation (y), domain hash, field/embedding certificate, and registered dependency on the Cycle84 public occupancy certificate.
