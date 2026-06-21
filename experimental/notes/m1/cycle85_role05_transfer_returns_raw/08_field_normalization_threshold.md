AUDIT

## 1. Executive verdict and confidence

**Verdict:** the Cycle84 count yields a bankable finite/model MCA numerator lower certificate, but the comparison with (2^{32}) is not the native prize comparison.

For the explicit packet,

[
q_{\mathrm{gen}}=q_{\mathrm{code}}=q_{\mathrm{line}}
=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481,
]

so

[
T_{\mathrm{line}}
=T_{\mathrm{code}}
=\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor
=0.
]

Consequently, the corrected comparison is

[
M_C(6)\ge 52{,}747{,}567{,}092>0=T_{\mathrm{line}},
]

not (M_C(6)>2^{32}=T_{\mathrm{line}}).

Thus:

* (52{,}747{,}567{,}092>2^{32}) is a **research/tensor-block benchmark**.
* It is a **wrong-denominator statement** if described as the native threshold of this field.
* The native research ledger row is `FAIL`, but it is zero-target redundant: the core lower bound (M_C(\sigma)\ge1) already makes every reserve fail.
* The current instance is not accepted by the official profile because
  [
  n=256,\qquad k=256-113-6=137,\qquad \frac{k}{n}=\frac{137}{256},
  ]
  which is not one of (1/2,1/4,1/8,1/16).

**Confidence:** high on the field and denominator audit; high on the finite MCA lower implication conditional on the banked Cycle62/65–68 transfer; unknown on the required tensor construction.

---

## 2. Exact theorem and checker statement

### Theorem `L-CYCLE85-FIELD-NORMALIZED-ROLE05-OCCUPANCY-TRANSFER`

Let

[
F_0=\mathbf F_{17}[X]/(X^{16}+X^8+3),
\qquad
D=\mu_{256}\subset F_0,
\qquad
\beta=X+2\notin D.
]

Consider the explicit Role05 packet with

[
(n,k,\sigma,j)=(256,137,6,113),
\qquad j=n-k-\sigma,
]

and support family (\mathcal P_0). Assume the banked Cycle62 thickened-modulus theorem and the Cycle65–68 locator-evaluation reduction. Then the explicit (t=1) syndrome line has at least

[
\operatorname{Occ}(\beta)
=========================

# #\left{\prod_{x\in T}(\beta-x):T\in\mathcal P_0\right}

52{,}747{,}567{,}092
]

distinct transverse bad slopes. Hence

[
\boxed{M_C(6)\ge52{,}747{,}567{,}092.}
]

The native fields are

[
q_{\mathrm{gen}}=q_{\mathrm{code}}=q_{\mathrm{line}}=17^{16}.
]

The value of (q_{\mathrm{chal}}) is not determined by the packet and has no effect on this comparison.

Therefore

[
\boxed{T_{\mathrm{line}}=T_{\mathrm{code}}=0}
]

and the corrected native comparison is

[
\boxed{52{,}747{,}567{,}092>0.}
]

This theorem does **not** identify the scalar-list numerator, does not establish an official-profile packet, and does not determine the full MCA numerator.

### Correct ledger entry

```text
objective.kind             = mca
profile.mode               = research
n                          = 256
k                          = 137
sigma                      = 6
j                          = 113
q_gen                      = 48661191875666868481
q_code                     = 48661191875666868481
q_line                     = 48661191875666868481
q_chal                     = separately declared; no denominator debit
T_code                     = 0
T_line                     = 0
T_decision                 = 0
lower_term.type            = packet.explicit_mca_slope_set
lower_term.reserve         = 6
lower_term.value           = 52747567092
row_verdict                = FAIL
term_relevance             = ZERO_TARGET_CORE_REDUNDANT
official_profile_result    = REJECT_INVALID_RATE_137_OVER_256
```

Since (T_{\mathrm{line}}=0), the checker’s global research result is

```text
r = n-k = 119
f = 119
c = null
s = null
no_safe_reserve = true
```

independently of the Cycle84 packet.

---

## 3. Proof and construction

### 3.1 Product field and generated field

The polynomial (X^{16}+X^8+3) is irreducible over (\mathbf F_{17}), so the quotient has order (17^{16}).

The element (\eta=6X^9) has order (256). Moreover,

[
17^2\equiv33,\quad
17^4\equiv65,\quad
17^8\equiv129,\quad
17^{16}\equiv1
\pmod{256},
]

and no earlier displayed power is (1). Therefore

[
\operatorname{ord}_{256}(17)=16.
]

Any field containing a primitive (256)-th root of unity must therefore contain (\mathbf F_{17^{16}}). Consequently the multiplicative-subgroup domain already generates the full field:

[
q_{\mathrm{gen}}=17^{16}.
]

The explicit RS code is over that same field, so (q_{\mathrm{code}}=17^{16}).

### 3.2 Slope-line field

In the Cycle62 (t=1) normalization, both the reduced color and actual line parameter lie in the ambient field:

[
\chi(T,c)\in F_0,
\qquad
z(T,c)=\lambda(w)+\chi(T,c)\in F_0.
]

Thus the corresponding MCA parameter field is

[
q_{\mathrm{line}}=|F_0|=17^{16}.
]

The product values also lie in (F_0^\times):

[
\rho_\beta(T)=\prod_{x\in T}(\beta-x).
]

Cycle65 identifies the occupied thickened colors with these values up to multiplication by a fixed nonzero constant. The augmented-row normalization then applies a fixed affine bijection to colors. Neither operation changes cardinality.

Therefore distinct occupied (\rho_\beta(T)) values yield distinct slopes.

### 3.3 Exact arithmetic

[
17^{16}
=======

48{,}661{,}191{,}875{,}666{,}868{,}481.
]

[
2^{128}
=======

340{,}282{,}366{,}920{,}938{,}463{,}463{,}374{,}607{,}431{,}768{,}211{,}456.
]

Hence

[
\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor=0.
]

Also,

[
2^{32}=4{,}294{,}967{,}296,
]

[
\operatorname{Occ}(\beta)=52{,}747{,}567{,}092,
]

and

[
\operatorname{Occ}(\beta)-2^{32}
================================

48{,}452{,}599{,}796.
]

The (2^{32}) comparison is arithmetically true but is not the native threshold.

### 3.4 Why (2^{32}) is not obtainable by compatible scalar extension

For a native target to equal (2^{32}), the line-field order would have to satisfy

[
2^{160}
\le q_{\mathrm{line}}
<
2^{160}+2^{128}.
]

Any finite field containing (F_0=\mathbf F_{17^{16}}) has order

[
q_{\mathrm{line}}=17^{16e}
]

for some positive integer (e). The first compatible possibilities are (e=1,2,3,\ldots), and none lies in the interval above. Therefore no scalar extension compatible with this packet makes (2^{32}) the exact native threshold.

A field such as (\mathbf F_{2^{160}}) would have the desired target, but it has the wrong characteristic and cannot contain or scalar-extend the Cycle84 model.

### 3.5 Complete compatible-extension audit

Under the official strict cap (q_{\mathrm{line}}<2^{256}), only (e=1,2,3) are possible:

| Extension     |                                                                                                     (q_{\mathrm{line}}) |                       (T_{\mathrm{line}}) | Fixed Cycle84 packet                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------: | ----------------------------------------: | ------------------------------------------ |
| (F_{17^{16}}) |                                                                                (48{,}661{,}191{,}875{,}666{,}868{,}481) |                                       (0) | clears trivially                           |
| (F_{17^{32}}) |                                       (2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361) |                                       (6) | clears, but tangent (113>6) already clears |
| (F_{17^{48}}) | (115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641) | (338{,}617{,}018{,}271{,}848{,}945{,}628) | does not clear                             |
| (F_{17^{64}}) |                                                                                                        bit length (262) |                                         — | violates (q_{\mathrm{line}}<2^{256})       |

Thus scalar extension alone has no useful regime:

* degree (1): zero-target degeneracy;
* degree (2): the packet is dominated by the elementary tangent bound;
* degree (3): the denominator is nontrivial, but the fixed occupancy is too small;
* degree (4): outside the field cap.

This is an exact route cut for pure field extension.

### 3.6 Correct interpretation of the (2^{32}) benchmark

Under the strict field cap,

[
T_{\mathrm{line}}<2^{128}.
]

Therefore, if an exact fourfold tensor theorem gave

[
M_{\mathrm{tensor}}\ge\operatorname{Occ}(\beta)^4,
]

then

[
\operatorname{Occ}(\beta)>2^{32}
\quad\Longrightarrow\quad
M_{\mathrm{tensor}}>2^{128}>T_{\mathrm{line}}.
]

That is the only clean prize-scale interpretation of the (2^{32}) line: it is a sufficient **per-block benchmark for a fourfold multiplicative tensor**. No such tensor theorem is currently banked.

Using the exact occupancy rather than only (>2^{32}), a smaller amplification could work over (F_{17^{48}}):

[
\operatorname{Occ}(\beta)^2
===========================

2{,}782{,}305{,}834{,}125{,}041{,}336{,}464

>

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

Even product multiplicity eight would suffice:

[
\frac{\operatorname{Occ}(\beta)^2}{8}
=====================================

347{,}788{,}229{,}265{,}630{,}167{,}058

>

T_{\mathrm{line}},
]

with margin

[
9{,}171{,}210{,}993{,}781{,}221{,}430.
]

Multiplicity nine is not sufficient under this crude bound:

[
\frac{\operatorname{Occ}(\beta)^2}{9}
=====================================

309{,}145{,}092{,}680{,}560{,}148{,}496
<
T_{\mathrm{line}}.
]

A mere second copy inside (F_0), or inside a multiplicative scalar coset of (F_0), cannot work: its product set has size at most

[
|F_0^\times|
============

48{,}661{,}191{,}875{,}666{,}868{,}480
<
T_{\mathrm{line}}(F_{17^{48}}).
]

The second packet must therefore have genuinely extension-valued colors.

### 3.7 Fixed-support rate padding is algebraically available

There is a clean way to repair the nonofficial rate without changing occupied-color cardinality.

Suppose a (t=1) packet has apolar generators

[
(A,B),\qquad \deg A=\sigma,\quad \deg B=j,
]

and locators

[
P_T=A U_T+\gamma_TB.
]

Choose (m) fixed new domain points (U), disjoint from the old domain, (\operatorname{Supp}A), and (\beta), and let

[
Q(X)=\prod_{u\in U}(X-u).
]

Then

[
QP_T=A(QU_T)+\gamma_T(BQ).
]

The new apolar pair is ((A,BQ)), the new supports are (T\cup U), and

[
\rho_\beta(T\cup U)=Q(\beta)\rho_\beta(T).
]

Because (Q(\beta)\ne0), occupied colors and slopes are multiplied by one fixed unit; their cardinality is unchanged. Parameters transform as

[
n\mapsto n+m,\qquad
j\mapsto j+m,\qquad
k\mapsto k,\qquad
\sigma\mapsto\sigma.
]

For one Cycle84 packet, (m=18) gives

[
(n,k,\sigma,j)=(274,137,6,131),
\qquad
\frac{k}{n}=\frac12.
]

This repairs the official rate, but not the denominator relevance: over (F_{17^{32}}) the tangent bound still dominates, while over (F_{17^{48}}) the unamplified occupancy is below target.

---

## 4. Verification requirements

A promoted certificate must verify all of the following:

1. **Finite transfer registry:** exact dependencies from the Cycle62 thickened-color theorem through the Cycle84 exact occupancy certificate.
2. **Field ledger:** irreducibility, (\eta) order (256), generated-field minimality, and all embeddings (q_{\mathrm{gen}}\to q_{\mathrm{code}}\to q_{\mathrm{line}}).
3. **MCA witness:** explicit nonconstant syndrome line, support witnesses, full-coordinate status, and the equality between product collisions and slope collisions.
4. **Transversality:** the shifted (t=1) noncontainment theorem must be registered against the exact code fingerprint.
5. **Profile:** exact (n,k,\sigma,j), allowed rate, field caps, and domain digest.
6. **Tensor case:** exact occupied product-set count, or a deterministic certificate that its pair-product multiplicity is at most eight.
7. **Padding case:** explicit new points, the polynomial (Q), coprimality with (A), and the new apolar/syndrome certificate.
8. **No challenge-field substitution:** (q_{\mathrm{chal}}) cannot pay the MCA denominator.

---

## 5. Next exact lemma or construction

The next substantive target is:

### `L-CYCLE86-EXTENSION-VALUED-TWO-PACKET-TENSOR-AND-RATE-PADDING`

Construct over

[
K=\mathbf F_{17^{48}}
]

two disjoint (t=1) Role05 packets with:

[
|D_1|=|D_2|=256,\qquad
|S_1|=|S_2|=52{,}747{,}567{,}092,
]

a common degree-six apolar generator (A), degree-113 generators (B_1,B_2), and locators

[
P_{i,T}=A U_{i,T}+\gamma_{i,T}B_i,
]

such that

[
m_\times:=
\max_y
#{(s_1,s_2)\in S_1\times S_2:s_1s_2=y}
\le8.
]

Then

[
P_{1,T_1}P_{2,T_2}
==================

A\left(
A U_{1,T_1}U_{2,T_2}
+\gamma_{2,T_2}U_{1,T_1}B_2
+\gamma_{1,T_1}U_{2,T_2}B_1
\right)
+\gamma_{1,T_1}\gamma_{2,T_2}B_1B_2,
]

so the combined supports form one degree-226 Role05 packet with at least

[
347{,}788{,}229{,}265{,}630{,}167{,}058
]

distinct slopes.

Add 48 fixed support points using the padding lemma. The resulting parameters are

[
(n,k,\sigma,j)=(560,280,6,274),
\qquad
\frac{k}{n}=\frac12,
]

with

[
q_{\mathrm{gen}}=q_{\mathrm{code}}=q_{\mathrm{line}}=17^{48}<2^{256}.
]

Its lower numerator would exceed the exact native target

[
338{,}617{,}018{,}271{,}848{,}945{,}628,
]

giving an official-profile MCA counterpacket.

The exact unsolved construction requirement is therefore not “count more products.” It is:

> Build a second disjoint packet sharing the same degree-six support modulus, whose occupied thickened colors genuinely leave the base subfield, and certify pair-product multiplicity at most eight.

---

## Self-audit

### 1. Exact implication proved and not proved

Proved:

[
\operatorname{Occ}(\beta)=52{,}747{,}567{,}092
\Longrightarrow
M_C(6)\ge52{,}747{,}567{,}092
]

for the explicit model, subject to the banked transfer theorem chain.

Also proved:

[
T_{\mathrm{line}}=T_{\mathrm{code}}=0
]

for the native model, and that no compatible scalar extension makes (2^{32}) the native threshold.

Not proved:

* an official-profile instance for the current packet;
* a frontier-moving lower term;
* tensor multiplicativity;
* the two-packet extension-valued construction;
* any scalar-list numerator conclusion;
* a full prize theorem.

### 2. Official-prize relevance

The present result is a **finite/model/research MCA certificate**. In research mode it is a zero-target-redundant failure. The attached instance is rejected in official mode because (137/256) is not an allowed rate.

### 3. First line where the reduction can fail

The first false normalization is

[
T_{\mathrm{line}}\stackrel{\text{wrong}}{=}2^{32}.
]

The actual value is (0). After that, official profile validation fails at the rate check.

For the proposed amplified route, the first genuine construction wall is existence of a second extension-valued packet sharing the same (A) and having pair-product multiplicity at most eight.

### 4. Correct use of the four fields and (2^{-128})

* (q_{\mathrm{gen}}=17^{16}): domain-generated field.
* (q_{\mathrm{code}}=17^{16}): native code alphabet.
* (q_{\mathrm{line}}=17^{16}): actual MCA slope field.
* (q_{\mathrm{chal}}): separate and irrelevant to the numerator threshold.
* (T_{\mathrm{line}}=\lfloor q_{\mathrm{line}}/2^{128}\rfloor=0).
* (T_{\mathrm{code}}=0), but the current object is not a scalar-list numerator.
* (2^{32}) is not either native target.

### 5. Possible numerator reductions

For the finite transferred packet:

* **Quotient/periodic structure:** no cardinality loss; Cycle84 lifted its quotient census back to exact equality in (F_0^\times). It may affect exception classification, not the actual slope count.
* **Contained incidences:** excluded by the banked shifted-(t=1) noncontainment theorem.
* **Same-slope collisions:** exactly the product collisions already removed in (\operatorname{Occ}(\beta)).
* **Affine color normalization:** a bijection, hence no loss.
* **Scalar multiplication by the fixed factor:** also a bijection.

These issues reappear in a future tensor packet and must be reverified there.

### 6. Exact theorem converting the result into an official counterpacket

`L-CYCLE86-EXTENSION-VALUED-TWO-PACKET-TENSOR-AND-RATE-PADDING`, stated above, is the exact conversion theorem. Its decisive finite checker target is

[
m_\times\le8
]

for the two occupied color sets over (\mathbf F_{17^{48}}), followed by the explicit 48-point fixed-support padding certificate.
