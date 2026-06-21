BANKABLE_LEMMA

## L-CYCLE106-ONE-EXTERNAL-DEPHASING-TRANSVERSAL-PACKING

The intended implication

[
\text{many distinct active }\theta
\Longrightarrow
\text{forbidden periodicity of }\widehat U
]

does **not** follow from dephasing alone. What does follow is a strict reduction to a one-external-point fixed-jet transversal whose members satisfy strong Prouhet–Tarry–Escott identities and a constant-weight packing condition.

Set

[
d=\sigma+1,\qquad s=\sigma+k,
]

and write

[
g_S(X)=\prod_{x\in S}(1-xX),\qquad
\widehat U(X)=\sum_{j=0}^{d}u_jX^j.
]

If (u_0\ne1), there are no active parameters. Hence assume (u_0=1).

Cycle105 gives

[
\theta\text{ active}
\iff
\exists S\in\binom Hs:
g_S(X)\equiv G(\theta,X)\pmod {X^{d+1}},
]

and the triangular definition of (G) gives

[
(1-\theta X)G(\theta,X)\equiv\widehat U(X)
\pmod {X^{d+1}}.
]

Therefore

[
\boxed{
\theta\text{ active}
\iff
\exists S\in\binom Hs:
(1-\theta X)g_S(X)\equiv\widehat U(X)
\pmod {X^{d+1}}.
}
\tag{1}
]

No output from the failed Cycle106 Fable harness is used here.

## 1. The dephasing map

Restrict initially to

[
\theta\in\mathbf F_p^\times\setminus H.
]

For a witness ((\theta,S)), define

[
\mathfrak d(\theta,S)=A_{\theta,S}:=S\sqcup{\theta}.
\tag{2}
]

Because (\theta\notin H),

[
g_{A_{\theta,S}}(X)
=(1-\theta X)g_S(X).
]

Thus (1) becomes

[
g_{A_{\theta,S}}(X)
\equiv \widehat U(X)\pmod {X^{d+1}}.
\tag{3}
]

Define the one-external fixed-jet fiber

[
\mathcal D_s(\widehat U):=
\left{
A\subset\mathbf F_p^\times:
|A\cap H|=s,\ |A\setminus H|=1,
g_A\equiv\widehat U\pmod {X^{d+1}}
\right}.
\tag{4}
]

The unique external point gives a projection

[
c:\mathcal D_s(\widehat U)\to\mathbf F_p^\times\setminus H,
\qquad
c(A)=\text{the unique element of }A\setminus H.
\tag{5}
]

Then exactly

[
c(\mathcal D_s(\widehat U))
===========================

\left{\theta\in\mathbf F_p^\times\setminus H:
\Gamma(\theta)\in M_s
\right}.
\tag{6}
]

This is the required dephasing: multiplication by (1-\theta X) removes the geometric phase (1/(1-\theta X)) and turns activity into a fixed moment-jet condition.

## 2. Distinct support and witness multiplicity

For every distinct external active (\theta), choose one witness (S_\theta), for example the lexicographically least one, and put

[
A_\theta=S_\theta\sqcup{\theta}.
\tag{7}
]

Then

[
\theta\longmapsto A_\theta
\tag{8}
]

is injective, because (A_\theta\setminus H={\theta}). Consequently,

[
#{\text{distinct external active }\theta}
=========================================

#{A_\theta:\theta\text{ external active}}.
\tag{9}
]

Hence arbitrary witness multiplicity at one (\theta) cannot invalidate the distinct-support conclusion after passing to this canonical transversal.

There is also no hidden self-intersection of (\Gamma). Indeed,

[
g_1(\theta)=u_1+\theta
\tag{10}
]

because (u_0=1). Thus (\Gamma) is injective already in its first coordinate. Therefore

[
|\Gamma\cap M_s|
================

#{\theta:\theta\text{ active}}.
\tag{11}
]

The exceptional parameters satisfy

[
#(H\cup{0})\le n+1.
\tag{12}
]

It is therefore enough to bound the external transversal, then add (n+1).

## 3. Exact structure forced between two distinct colors

Take two distinct external active parameters (\theta\ne\phi), with selected witnesses (S=S_\theta) and (T=S_\phi). Let

[
C=S\cap T,
]

and define

[
L=(S\setminus C)\sqcup{\theta},\qquad
R=(T\setminus C)\sqcup{\phi}.
\tag{13}
]

The sets (L,R) are disjoint and have equal cardinality

[
r=|S\setminus T|+1=|T\setminus S|+1.
\tag{14}
]

From the common fixed jet,

[
g_Cg_L\equiv \widehat U\equiv g_Cg_R
\pmod {X^{d+1}}.
]

Since (g_C(0)=1), it is a unit in
(\mathbf F_p[X]/(X^{d+1})), so it cancels:

[
\boxed{
g_L(X)\equiv g_R(X)\pmod {X^{d+1}}.
}
\tag{15}
]

Equivalently,

[
\sum_{x\in L}x^j=\sum_{y\in R}y^j,
\qquad 1\le j\le d.
\tag{16}
]

One direct derivation is

[
-\frac{Xg_L'(X)}{g_L(X)}
========================

\sum_{j\ge1}\left(\sum_{x\in L}x^j\right)X^j,
]

and similarly for (R).

If (r\le d), then both (g_L) and (g_R) have degree at most (d), so congruence modulo (X^{d+1}) is equality as polynomials. Unique factorization would give (L=R), impossible because they are disjoint and contain the distinct external points (\theta,\phi). Hence

[
r\ge d+1.
]

Therefore

[
\boxed{|S_\theta\setminus S_\phi|\ge d=\sigma+1.}
\tag{17}
]

Since both supports have cardinality (s=\sigma+k),

[
\boxed{
|S_\theta\cap S_\phi|
\le s-d=k-1.
}
\tag{18}
]

Thus the selected witnesses form a (k)-packing: no (k)-subset of (H) is contained in two selected witnesses.

This gives the unconditional distinct-color bound

[
\boxed{
N_{\rm out}
\le
\frac{\binom nk}{\binom sk}
}
\qquad(k\ge1),
\tag{19}
]

where (N_{\rm out}) denotes the number of distinct external active parameters. If (k=0), (17) is impossible for two different witnesses because (s=d-1), so (N_{\rm out}\le1).

There is a complementary cap. Put

[
m=n-s,\qquad
k^\vee=m-d+1=n-k-2\sigma.
\tag{20}
]

The complements (H\setminus S_\theta), each of size (m), satisfy

[
|(H\setminus S_\theta)\cap(H\setminus S_\phi)|
\le m-d=k^\vee-1.
]

Hence, when (k^\vee\ge1),

[
\boxed{
N_{\rm out}
\le
\frac{\binom n{k^\vee}}{\binom m{k^\vee}}.
}
\tag{21}
]

When (k^\vee\le0), we have (m<d), while two distinct complements would have to differ in at least (d) places; therefore (N_{\rm out}\le1).

Combining everything,

[
\boxed{
|\Gamma\cap M_s|
\le
n+1+
\min\left{
\frac{\binom nk}{\binom{\sigma+k}k},
,
\frac{\binom n{k^\vee}}{\binom{n-\sigma-k}{k^\vee}}
\right},
}
\tag{22}
]

with either ratio replaced by (1) in its corresponding zero-or-negative boundary case.

This is stronger than merely converting a weighted incidence count into distinct support. It is a direct distinct-(\theta) packing theorem.

## 4. The exact reduced PTE/rational-contact wall

Fix one member ((\theta_0,S_0)) of the external transversal. For every other ((\theta,S_\theta)), put

[
P_\theta=S_\theta\setminus S_0,\qquad
Q_\theta=S_0\setminus S_\theta.
]

Then (P_\theta,Q_\theta\subset H) are disjoint,

[
|P_\theta|=|Q_\theta|\ge d,
\tag{23}
]

and cancellation of the common support gives

[
\boxed{
(1-\theta X)g_{P_\theta}(X)
\equiv
(1-\theta_0X)g_{Q_\theta}(X)
\pmod {X^{d+1}}.
}
\tag{24}
]

Equivalently,

[
\frac{(1-\theta X)g_{P_\theta}(X)}
{(1-\theta_0X)g_{Q_\theta}(X)}
\equiv1\pmod {X^{d+1}}.
\tag{25}
]

Thus every additional active color produces a disjoint equal-cardinality colored Prouhet–Tarry–Escott trade of depth (d), with all ordinary entries in (H) and one external entry on each side.

This is the strictly smaller residual theorem:

> **T-CYCLE107-APERIODIC-COLORED-PTE-TRANSVERSAL-INVERSE.**
> Under the literal source definition of above-reserve aperiodicity, uniformly bound by (n^C) the number of pairwise distinct external (\theta) for which there exist disjoint (P_\theta,Q_\theta\subset H), of equal size at least (d), satisfying (24), with the resulting supports (S_\theta) forming the packing (18).
> The exponent (C) must be independent of (s) and (k). Equivalently, any family larger than (n^C) must output a certificate rejected by the source aperiodicity verifier.

If this theorem holds, (12) immediately gives the Cycle106 target.

## 5. What periodicity is actually forced

There is one exact periodicity implication. For (\lambda\in H), define

[
\lambda A={\lambda a:a\in A}.
]

Then

[
g_{\lambda A}(X)=g_A(\lambda X).
\tag{26}
]

If both (A) and (\lambda A) lie in (\mathcal D_s(\widehat U)), then

[
\widehat U(\lambda X)
\equiv g_A(\lambda X)
=g_{\lambda A}(X)
\equiv\widehat U(X)
\pmod {X^{d+1}}.
\tag{27}
]

Therefore a scaling collision creates the explicit stabilizer certificate

[
u_j(\lambda^j-1)=0,\qquad 0\le j\le d.
\tag{28}
]

Define

[
K_{\widehat U}
==============

\left{
\lambda\in H:
\lambda^j=1
\text{ for every }j\le d\text{ with }u_j\ne0
\right}.
\tag{29}
]

Any same-orbit collision must use (\lambda\in K_{\widehat U}). In particular, if (u_1\ne0), then

[
K_{\widehat U}={1}.
\tag{30}
]

But a large transversal need not contain two elements in the same (H)-scaling orbit. The number of one-external scaling orbits is already on the order of

[
\frac{(p-1-n)\binom ns}{n},
]

which is exponential in the central subset-size range. Therefore

[
\text{many fixed-jet representations}
\not\Longrightarrow
\text{a scaling collision}
]

at any polynomial threshold.

The only automatic structure supplied by dephasing is (15)–(18), namely colored PTE trades and packing. A new inverse theorem is needed to convert a large collection of such trades into whatever stronger periodic/dephased structure the actual source aperiodicity condition forbids.

Moreover, the supplied Cycle105–106 packet uses the phrase “above-reserve aperiodicity” but does not include a formal predicate or a source theorem of the form

[
\text{large colored-PTE transversal}
\Longrightarrow
\text{aperiodicity-failure certificate}.
\tag{31}
]

Consequently I cannot verify the requested item “why that structure violates the actual aperiodicity hypothesis.” That implication is precisely the remaining theorem, not a consequence presently available in the packet.

## 6. Exact witness-multiplicity obstruction

Weighted witness counts cannot be substituted for distinct colors.

Let (K=\mu_M\le H), where

[
M>d.
]

For every (K)-coset (C=aK),

[
g_C(X)
=\prod_{x\in aK}(1-xX)
=1-(aX)^M
\equiv1\pmod {X^{d+1}}.
\tag{32}
]

Choose (2t) distinct (K)-cosets, grouped into pairs

[
(C_i^0,C_i^1),\qquad 1\le i\le t.
]

For every (\varepsilon\in{0,1}^t), let

[
S_\varepsilon
=============

\bigcup_{i=1}^t C_i^{\varepsilon_i}.
]

All these supports have cardinality (tM), and

[
g_{S_\varepsilon}(X)\equiv1\pmod {X^{d+1}}.
\tag{33}
]

Fix one external (\theta_0\ne0) and take

[
\widehat U(X)=1-\theta_0X.
]

Then for every (\varepsilon),

[
(1-\theta_0X)g_{S_\varepsilon}(X)
\equiv\widehat U(X)\pmod {X^{d+1}}.
\tag{34}
]

Thus one single active color (\theta_0) has at least

[
2^t
]

different witnesses.

At the same time (u_1=-\theta_0\ne0), so the simple coefficient-scaling stabilizer (29) is trivial. Hence even “trivial scaling stabilizer” does not control witness multiplicity.

This is **not** a counterpacket to Cycle106: it is an explicitly periodic coset-swap construction, and I have not shown it satisfies the actual above-reserve aperiodicity predicate. It is instead the exact mechanism proving that weighted-to-distinct transfer is invalid unless one first passes to a one-witness-per-color transversal.

## 7. Why the packing lemma alone cannot finish the proof

At corrected reserve,

[
d=\sigma+1=\Theta!\left(\frac n{\log n}\right),
]

and in the central regime (s=\Theta(n)). The distance condition

[
|S_\theta\setminus S_\phi|\ge d
]

still permits exponentially large constant-weight codes.

Indeed, the number of (s)-subsets within directed distance less than (d) of one fixed (s)-subset is at most

[
B=\sum_{i=0}^{d-1}\binom si\binom{n-s}i.
]

For central (s) and (d=\Theta(n/\log n)),

[
\log B
======

# O!\left(d\log\frac nd\right)

O!\left(\frac{n\log\log n}{\log n}\right)
=o(n).
]

A greedy packing therefore has at least

[
\frac{\binom ns}{B}=2^{\Theta(n)}
]

members. Thus no generic constant-weight-code or divided-difference argument can replace the missing colored-PTE inverse theorem.

## 8. Exact next checker

The finite checker should be

```text
cycle107_colored_dephasing_transversal_checker.py
```

with inputs

```text
(p,n,sigma,k,Uhat,VERIFY_ABOVE_RESERVE_APERIODICITY).
```

It should:

1. Set (d=\sigma+1), (s=\sigma+k), and construct (H=\mu_n).
2. For each (S\in\binom Hs), write
   [
   g_S(X)=1+a_1X+\cdots.
   ]
   The (X)-coefficient of (1) forces the unique candidate
   [
   \theta=a_1-u_1=-e_1(S)-u_1.
   ]
3. Verify exactly
   [
   a_j-\theta a_{j-1}=u_j,
   \qquad 2\le j\le d.
   ]
4. Hash witnesses by (\theta), recording both their multiplicity and the lexicographically least witness.
5. Separate (\theta=0), (\theta\in H), and external (\theta).
6. Form the canonical external transversal and verify for every pair:
   [
   g_L\equiv g_R\pmod {X^{d+1}},
   \qquad
   |S_\theta\setminus S_\phi|\ge d.
   ]
7. Verify the two packing bounds (19) and (21).
8. Run the literal source aperiodicity-certificate extractor on the **transversal**, never on the full witness multiset.

Its possible outputs should be:

```text
COLORED_TRANSVERSAL_CAP_PASS
APERIODICITY_FAILURE_CERTIFICATE
FINITE_COLORED_COUNTERPACKET_CANDIDATE
```

A finite candidate is only a research/model certificate. To become a `COUNTERPACKET`, it must be promoted to an unbounded family with superpolynomially many distinct external colors and must pass the actual above-reserve aperiodicity verifier for every family member.

## Route to a full solution

There is a precise conditional route:

[
\begin{aligned}
\text{Cycle105 activity}
&\xrightarrow{\text{proved}}
\text{one-external fixed-jet fiber},\
&\xrightarrow{\text{canonical section}}
\text{distinct-color transversal},\
&\xrightarrow{\text{proved}}
\text{disjoint colored PTE packing},\
&\xrightarrow{\boxed{\text{missing inverse theorem}}}
\text{source-valid aperiodicity failure}.
\end{aligned}
]

The exact missing implication is

[
\boxed{
|\mathcal T|>n^C
\Longrightarrow
\text{a certificate contradicting the literal above-reserve
aperiodicity predicate for }\widehat U.
}
\tag{35}
]

Without (35), there is no full Cycle106 proof. Conversely, a parameterized family violating (35) while passing the literal predicate would be the required counterpacket mechanism.

## Self-audit

**What exact implication did I prove?**
Distinct external active parameters inject into a fixed (d)-jet one-external support fiber. Any two selected witnesses yield a disjoint equal-size PTE trade of depth (d), their (H)-supports differ in at least (d) positions, and the resulting distinct-color count satisfies the exact packing bounds (19), (21), and (22).

**What exact implication did I not prove?**
I did not prove that a superpolynomial colored-PTE transversal forces any structure forbidden by the actual above-reserve aperiodicity hypothesis. I also did not prove that the coset-swap multiplicity example satisfies that hypothesis.

**Is this official-prize-relevant?**
It is directly relevant to the M1 upper-side structural wall, conditional on the banked Cycle105 equivalence. It is not an official Proximity Prize proof. I have not reverified every link from Cycle105 activity, through noncontainment and the all-denominator assembly, to the official statement.

**Where is the first possible failure?**
Within the new reduction, the first unproved line is exactly (35). In the inherited official chain, the first earlier line that would need independent checking is the claim that Cycle105’s fixed-prefix activity equation exactly represents the official noncontained bad-slope numerator in every required branch.

**Are the field ledgers and (2^{-128}) being used correctly?**
They are not used. No (q_{\rm gen}), (q_{\rm line}), (q_{\rm code}), (q_{\rm chal}), or (2^{-128}) arithmetic enters this single-field structural lemma. No field transfer or probability conclusion is claimed.

**Can quotient structure, contained incidences, same-slope collisions, or affine normalization reduce the numerator?**
Periodic/coset-swap structure can create exponentially many witnesses at one color, but cannot reduce the canonical distinct-color transversal. Same-slope multiplicity is removed by selecting one witness per (\theta). The curve itself has no collisions because (g_1(\theta)=u_1+\theta). Any legitimate affine color change with nonzero linear coefficient preserves cardinality. Contained-incidence and official-normal-form issues remain inherited Cycle105/assembly questions; this lemma counts every solution of the banked fixed-prefix equation.

**Confidence:** high for the dephasing bijection, injective transversal, PTE identity, minimum-distance conclusion, and packing bounds; unknown for the missing aperiodic colored-PTE inverse theorem.
