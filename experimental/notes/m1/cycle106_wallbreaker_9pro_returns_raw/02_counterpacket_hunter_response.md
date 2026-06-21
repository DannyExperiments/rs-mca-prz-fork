AUDIT

The packet does not define the formal aperiodicity predicate or the corrected reserve inequality, so no construction can presently be certified as a source-valid **aperiodic, above-reserve** counterpacket. The strongest exact attack is a **short locator-twist dephasing mechanism**: it preserves a polynomial fraction of distinct active values while hiding a periodic core from any aperiodicity test applied only to the displayed prefix (\widehat U).

Set (h=\sigma+1<n), (R_h=\mathbb F_p[X]/(X^{h+1})), (H=\mu_n), and (m=n-s).

## 1. Exact complement-line normal form

For (T=H\setminus\bar S), Cycle105 activity is equivalent to

[
\widehat U(X)g_T(X)=1-\theta X \qquad\text{in }R_h.
\tag{1}
]

Indeed,

[
g_{\bar S}g_T=1-X^n=1\quad\text{in }R_h,
]

while the banked condition says

[
g_{\bar S}=\frac{\widehat U}{1-\theta X}.
]

Thus the counterpacket problem is exactly to find one unit (U=\widehat U\bmod X^{h+1}) and many distinct (\theta) admitting equal-weight subsets (T_\theta\subseteq H) satisfying (1).

Also,

[
g_1(\theta)=u_1+\theta,
]

so (\theta\mapsto\Gamma(\theta)) is injective. Same-slope or affine-normalization collisions cannot merge distinct (\theta)'s unless the normalization is noninvertible, in which case it is not an equivalent reformulation of the numerator.

## 2. External witnesses are strongly separated

**Lemma.** If (\theta\ne\phi) are external active values, with witnesses (T_\theta,T_\phi) of size (m), then

[
|T_\theta\setminus T_\phi|
==========================

|T_\phi\setminus T_\theta|
\ge h.
\tag{2}
]

**Proof.** Put

[
A=T_\theta\setminus T_\phi,\qquad
B=T_\phi\setminus T_\theta,\qquad |A|=|B|=r.
]

Cross-multiplying (1) and cancelling the common locator gives

[
g_A(X)(1-\phi X)
\equiv
g_B(X)(1-\theta X)
\pmod {X^{h+1}}.
\tag{3}
]

If (r<h), both sides have degree at most (r+1\le h), so (3) is an equality in (\mathbb F_p[X]). Unique factorization then identifies the external factor (1-\phi X) with (1-\theta X), hence (\phi=\theta). The case where one parameter is (0) is excluded by the degree difference. Contradiction. ∎

Since (r\le \min(m,n-m)), this immediately gives

[
\min(m,n-m)<h
\quad\Longrightarrow\quad
#{\text{external active }\theta}\le1.
]

There are at most (n) internal values, so

[
|\Gamma\cap M_s|\le n+1
\qquad
\text{unless }h\le m\le n-h.
\tag{4}
]

Thus the unresolved incidence wall is strictly confined to the central layers.

## 3. Exact (h)-fold product-Sidon reduction

Choose one witness (T_\theta) for every distinct active value, and let (L) be their number.

For an (r)-multiset (A) of active values, (1\le r\le h), define its occupancy vector

[
z_A=\sum_{\theta\in A}\mathbf 1_{T_\theta}
\in{0,1,\ldots,r}^{H}.
]

**Lemma.** The map (A\mapsto z_A) is injective on (r)-multisets.

If (z_A=z_B), then the products of the corresponding locators are equal. Multiplying (1) over the two multisets gives

[
\prod_{\theta\in A}(1-\theta X)
\equiv
\prod_{\phi\in B}(1-\phi X)
\pmod {X^{h+1}}.
]

Both sides have degree at most (r\le h), so they are equal polynomials. Unique factorization recovers the nonzero parameters, while the fixed multiset cardinality recovers the number of zero parameters. Hence (A=B).

Consequently,

[
\binom{L+r-1}{r}
\le
[z^{rm}](1+z+\cdots+z^r)^n.
\tag{5}
]

Taking (r=h),

[
L
\le
\left(
h!,[z^{hm}](1+z+\cdots+z^h)^n
\right)^{1/h}
\le
h(h+1)^{n/h}.
\tag{6}
]

This is uniform in (s,k,p,U). It proves a polynomial bound when (h=\Omega(n)). At the reserve scale suggested in the packet, (h=\Theta(n/\log n)), it gives only

[
L\le \exp(O((\log n)^2))=n^{O(\log n)},
]

not (n^{O(1)}). This identifies the remaining quantitative gap exactly: aperiodicity must save a factor of roughly

[
\exp!\big(\Theta(n\log h)\big)
]

inside the occupancy count before taking the (h)-th root.

## 4. Strongest counterpacket mechanism: short locator-twist dephasing

Let (A,B\subseteq H) be disjoint, with

[
A\subseteq T_\theta,\qquad B\cap T_\theta=\varnothing.
]

Define

[
U_{A,B}=U,\frac{g_A}{g_B},
\qquad
T'*\theta=(T*\theta\setminus A)\cup B.
\tag{7}
]

Then exactly

[
U_{A,B}g_{T'_\theta}
====================

# U\frac{g_A}{g_B},g_{T_\theta\setminus A}g_B

# Ug_{T_\theta}

1-\theta X.
\tag{8}
]

Thus every retained (\theta) remains active and remains distinct.

Moreover, averaging over all disjoint (A,B) of prescribed sizes (a,b) gives some pair satisfying

[
#{\theta:A\subseteq T_\theta,\ B\cap T_\theta=\varnothing}
\ge
L,
\frac{\binom ma\binom{n-m}b}
{\binom na\binom{n-a}b}.
\tag{9}
]

For (m/n\in[\varepsilon,1-\varepsilon]) and (a+b\le\varepsilon n/2), the ratio is at least

[
(\varepsilon/2)^{a+b}.
\tag{10}
]

Hence a twist involving (O(n/h)) locator factors loses only a polynomial fraction of support when (h=\Theta(n/\log n)). A superpolynomial distinct-support packet would remain superpolynomial.

### One-point evasion of weak global periodicity tests

Suppose a periodic seed (U_0) lies in (\mathbb F_p[X^d]) for some (d>1), and choose (b\in H) avoided by many witnesses. Set

[
U'=\frac{U_0}{1-bX},
\qquad
T'*\theta=T*\theta\cup{b}.
]

Then all retained (\theta)'s remain active. But

[
[ X ]U'=b\ne0.
]

Therefore:

* (U'\notin\mathbb F_p[X^d]) for every (d>1);
* if (U'(\lambda X)=U'(X)), comparison of the (X)-coefficient forces (\lambda=1).

So (U') has trivial visible multiplier stabilizer and no visible coefficient period, although

[
(1-bX)U'=U_0
]

is periodic.

This rigorously kills any aperiodicity definition that tests only the displayed prefix (U) for a global stabilizer or missing coefficient classes. It does **not** kill an aperiodicity definition that searches for bounded locator twists exposing a periodic core.

## 5. Exact blocking condition

The locator-twist attack is blocked by the following strengthened predicate:

[
\operatorname{Aper}^{\mathrm{core}}*{t}(U):
\quad
U\frac{g_A}{g_B}\notin\operatorname{Per}*{H,h}
]

for every disjoint (A,B\subseteq H) with

[
|A|+|B|\le t,
\qquad
t\asymp \frac nh,
\tag{11}
]

where (\operatorname{Per}_{H,h}) must be the project’s actual quotient/subgroup-periodic class.

A global predicate (\operatorname{Aper}(U)) is insufficient. The necessary hypothesis is locator-core robustness at least through (O(n/h)) twists.

## 6. Other proposed mechanisms

### Same-slope or affine-color normalization

Killed exactly by

[
g_1(\theta)=u_1+\theta.
]

The curve is already injectively parametrized by its first coordinate. An invertible affine normalization preserves the numerator; a noninvertible one requires an additional fiber theorem and cannot be used as an equality.

### Contained incidences

Fix (C\subseteq H) and take

[
U=g_C^{-1},\qquad
T_\theta=C\cup{\theta},\qquad \theta\in H\setminus C.
]

Then

[
Ug_{T_\theta}=1-\theta X.
]

This can have trivial visible global periodicity while multiplication by (g_C) exposes the periodic core (1). But it yields only

[
n-|C|
]

distinct values, all internal. It is a diagnostic against weak aperiodicity, not a superpolynomial counterpacket.

More generally, a common witness core (C) can simply be cancelled by replacing (U) with (Ug_C). Containment does not itself amplify distinct support.

### Independent quotient/coset coordinates

If four witnesses form an exact multiplicative rectangle,

[
g_{T_{00}}g_{T_{11}}
====================

g_{T_{01}}g_{T_{10}},
]

then for (h\ge2),

[
(1-\theta_{00}X)(1-\theta_{11}X)
================================

(1-\theta_{01}X)(1-\theta_{10}X),
]

so

[
{\theta_{00},\theta_{11}}
=========================

{\theta_{01},\theta_{10}}.
]

Thus a full Cartesian product of independent coset-swap coordinates cannot multiplicatively generate four new distinct parameters. It may create enormous witness multiplicity, but not the required distinct support.

### Complement duality

Complement duality replaces (U) by (U^{-1}) and (m) by (n-m) in the line form. It preserves the same (\theta)-support bijectively. It can relocate a construction between the two sides of the central band, but it cannot amplify the numerator.

## 7. Exact next lemma

The proof-side theorem now needed is:

[
\boxed{\text{L-CYCLE107-SHORT-LOCATOR-CORE-INVERSE}}
]

There exist absolute constants (C_0,C_1) such that, whenever

[
h\le m\le n-h
]

and (L>n^{C_1}) distinct external values admit witnesses satisfying (1), there are disjoint (A,B\subseteq H) with

[
|A|+|B|\le C_0\frac nh
]

for which

[
U\frac{g_A}{g_B}\in\operatorname{Per}_{H,h},
\tag{12}
]

with (\operatorname{Per}_{H,h}) instantiated by the project’s actual charged quotient-periodic class.

Combined with the core-robust aperiodicity condition (11), this would prove the desired polynomial incidence bound. Conversely, a counterpacket would require:

1. an explicit above-reserve periodic seed having (n^{\omega(1)}) **distinct** active values, not merely many witnesses;
2. a short locator twist retaining (n^{\omega(1)}) of them via (9);
3. a proof that the resulting (U_{A,B}) nevertheless satisfies the project’s actual aperiodicity predicate.

The packet provides neither item 1 nor the formal predicate needed for item 3.

## Source defect preventing a stronger label

The uploaded compact source gives no exact:

* definition of (\operatorname{Aper}_{H,h}(U));
* definition of the charged periodic class (\operatorname{Per}_{H,h});
* corrected reserve inequality, including constants and dependence on (p);
* transfer theorem from the earlier “aperiodic separated (E)” condition to the truncated unit (\widehat U).

Therefore calling the locator-dephased construction “aperiodic above corrected reserve” would be unsupported.

The exact finite checker used for the algebraic normal form, distinct-support counting, pair separation, and bounded weak-periodicity twists is here:

* [Exact Cycle106 support/twist checker](sandbox:/mnt/data/cycle106_exact_support_checker.py)
* [(p=29,n=7,h=4,m=3) contained-twist certificate](sandbox:/mnt/data/cycle106_checker_p29_n7_s3_m3.json)
* [(p=31,n=10,h=3,m=5) external-pair certificate](sandbox:/mnt/data/cycle106_checker_p31_n10_s2_m5.json)

These were rerun exactly; they are finite/model certificates only.

## Self-audit

**Exact implication proved:** activity implies the complement-line equation; distinct external witnesses have half-distance at least (h); noncentral layers have at most (n+1) total active values; selected witnesses form an (h)-fold product-Sidon family; hence (L\le h(h+1)^{n/h}); short locator twists preserve activity and a quantified fraction of distinct support.

**Exact implication not proved:** neither (L\le n^{O(1)}) at (h=\Theta(n/\log n)) nor existence of an aperiodic, above-reserve family with (L=n^{\omega(1)}).

**Prize relevance:** these are upper-side structural research lemmas and finite certificates. They do not verify every link to the official Proximity Prize statement.

**First possible failure in the proposed full reduction:** the assertion that the source’s aperiodicity condition forbids every (O(n/h))-locator twist exposing a quotient-periodic core.

**Field/protocol ledgers:** (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and the (2^{-128}) target were not used. That is correct for this single-field structural wall; no protocol probability conclusion is claimed.

**Numerator reductions:** visible quotient periodicity can be hidden by a locator twist; common containment cancels; same-slope collision is impossible because (g_1) is injective; invertible affine normalization preserves cardinality; complement duality preserves rather than enlarges support.

**Confidence:** high for the displayed algebraic lemmas and the source-definition audit; unknown for the full polynomial incidence conjecture.
