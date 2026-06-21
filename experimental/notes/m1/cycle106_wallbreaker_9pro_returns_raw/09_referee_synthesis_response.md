BANKABLE_LEMMA

**Selected route: 3. Eliminant/subresultant/Wronskian reduction**, with a mandatory source-audit gate for the missing aperiodicity definition.

## Exact bankable reduction

Let
[
r=\sigma+2,\qquad m=n-s=n-\sigma-k,\qquad
R_r=\mathbf F_p[X]/(X^r),
]
and for (T\subseteq H=\mu_n) put
[
h_T(X)=\prod_{x\in T}(1-xX).
]

For (k\ge2), Cycle105’s complement form is
[
\theta\in\Theta_{\widehat U}
\iff
\exists T\in\binom Hm:
\quad h_T(X)\widehat U(X)=1-\theta X\quad\text{in }R_r.
\tag{1}
]

If (\Theta_{\widehat U}=\varnothing), the desired bound is trivial. Otherwise fix one active pair ((\theta_0,T_0)). Then
[
\widehat U=(1-\theta_0X)h_{T_0}^{-1}\quad\text{in }R_r.
\tag{2}
]

For every (T\in\binom Hm), define
[
B_T(X):=(1-\theta_0X)h_T(X)-h_{T_0}(X)
=\sum_{j=1}^{r-1}b_j(T)X^j
\quad\text{in }R_r,
]
and write
[
c_j=[X^j]h_{T_0},\qquad c_0=1.
]

Define the determinantal equations
[
\Delta_j(T):=b_j(T)-b_1(T)c_{j-1},
\qquad 2\le j\le r-1.
\tag{3}
]

Equivalently, require the matrix
[
\mathcal R_T=
\begin{pmatrix}
1&c_1&c_2&\cdots&c_{r-2}\
b_1(T)&b_2(T)&b_3(T)&\cdots&b_{r-1}(T)
\end{pmatrix}
\tag{4}
]
to have rank one.

### Lemma — dephased Möbius-jet rank-one reduction

[
\boxed{
\Theta_{\widehat U}
===================

\left{
-b_1(T):
T\in\binom Hm,\
\Delta_j(T)=0\ \text{for all }2\le j\le r-1
\right}.
}
\tag{5}
]

Thus the entire Cycle106 incidence problem is exactly the distinct first-coordinate image of a (k)-independent rank-one determinantal locus.

### Proof

Suppose (T) witnesses (\theta). Equations (1) and (2) give
[
(1-\theta_0X)h_T=(1-\theta X)h_{T_0}
\quad\text{in }R_r.
\tag{6}
]
Therefore
[
B_T=-\theta Xh_{T_0}.
]
Its (X)-coefficient is (b_1(T)=-\theta), and for (j\ge2),
[
b_j(T)=-\theta c_{j-1}=b_1(T)c_{j-1}.
]
Hence all (\Delta_j(T)) vanish.

Conversely, suppose all (\Delta_j(T)) vanish. Since (B_T) has zero constant coefficient,
[
B_T=b_1(T)Xh_{T_0}\quad\text{in }R_r.
]
Set (\theta=-b_1(T)). Then
[
(1-\theta_0X)h_T=(1-\theta X)h_{T_0}.
]
Multiplying by (h_{T_0}^{-1}) and using (2) gives
[
h_T\widehat U=1-\theta X.
]
Thus (T) witnesses (\theta). This also proves that the readout (-b_1(T)) is exact, not merely necessary. ∎

This removes simultaneously:

* the bandwidth (k) from the defining equations;
* the original curve (\Gamma);
* the existentially quantified (\theta);
* support multiplicity from the numerator;
* any need to union-bound over (k)-subsets.

I would bank this as

[
\boxed{\texttt{L-CYCLE107-DEPHASED-MOBIUS-JET-RANKONE-REDUCTION}}.
]

## Further exact consequence: short-petal rigidity

Take two active pairs ((\theta_i,T_i)) and ((\theta_j,T_j)). Write
[
C=T_i\cap T_j,\qquad
P=T_i\setminus T_j,\qquad
Q=T_j\setminus T_i,
]
so (|P|=|Q|=d).

Cancelling the unit (h_C) from the cross-multiplied form of (1) gives
[
(1-\theta_jX)h_P(X)
\equiv
(1-\theta_iX)h_Q(X)
\pmod {X^r}.
\tag{7}
]

If (d\le r-2=\sigma), both sides have degree at most (r-1), so (7) is an ordinary polynomial identity. Unique factorization then gives the complete classification:

[
\theta_i\ne\theta_j,\ d\le\sigma
\Longrightarrow
\theta_i,\theta_j\in H,\quad
P={\theta_i},\quad Q={\theta_j}.
\tag{8}
]

In particular, for two distinct external values
[
\theta_i,\theta_j\notin H,
]
one necessarily has
[
\boxed{|T_i\setminus T_j|\ge\sigma+1.}
\tag{9}
]

For equal slopes, cancellation of the unit (1-\theta X) in (7) gives
[
h_P\equiv h_Q\pmod{X^r}.
]
If (d<r), this is exact equality and hence (P=Q). Therefore distinct supports having the same slope satisfy
[
\boxed{|T_i\setminus T_j|\ge\sigma+2.}
\tag{10}
]

There is also an equivalent Prouhet–Tarry–Escott formulation. Since (r\le n<p), formal logarithms are legitimate, and active pairs satisfy
[
\sum_{x\in T_i}x^\ell-\sum_{x\in T_j}x^\ell
===========================================

\theta_i^\ell-\theta_j^\ell,
\qquad 1\le\ell\le\sigma+1.
\tag{11}
]
Thus
[
P\sqcup{\theta_j}
\quad\text{and}\quad
Q\sqcup{\theta_i}
]
have equal first (\sigma+1) power sums. When (d\le\sigma), Newton identities recover the entire multisets and yield (8).

## Two exact packing bounds

Let
[
L_{\rm ext}=|\Theta_{\widehat U}\setminus H|.
]
Choose one witness (T_\theta) for each distinct external (\theta). By (9), these supports have pairwise half-distance at least (\sigma+1).

Put
[
S_\theta=H\setminus T_\theta,\qquad |S_\theta|=s=\sigma+k.
]
Then
[
|S_\theta\cap S_{\theta'}|\le k-1.
]
Consequently no (k)-subset of (H) lies in two different (S_\theta), and
[
\boxed{
L_{\rm ext}\binom{s}{k}\le\binom nk.
}
\tag{12}
]

Equivalently,
[
L_{\rm ext}\le \frac{\binom nk}{\binom sk}.
\tag{13}
]

There is a dual bound directly on the (T_\theta). If (m\le\sigma), (9) gives
[
L_{\rm ext}\le1.
\tag{14}
]
If (m>\sigma), their pairwise intersections have size at most
[
m-\sigma-1.
]
Hence no ((m-\sigma))-subset lies in two different (T_\theta), and
[
\boxed{
L_{\rm ext}\binom{m}{m-\sigma}
\le
\binom{n}{m-\sigma}.
}
\tag{15}
]

Therefore
[
|\Theta_{\widehat U}|
\le
n+
\begin{cases}
1,&m\le\sigma,[2mm]
\displaystyle
\min\left{
\frac{\binom nk}{\binom{\sigma+k}{k}},
\frac{\binom n{m-\sigma}}{\binom m{m-\sigma}}
\right},
&m>\sigma.
\end{cases}
\tag{16}
]

The term (n) pays for all internal values (\theta\in H).

This proves the desired polynomial bound whenever either (k) or
[
m-\sigma=n-k-2\sigma
]
is bounded. The genuinely unresolved range is now the central range in which both quantities grow.

Packing alone cannot close that range: constant-weight codes with distance (2(\sigma+1)) may still be exponentially large. The rank-one/PTE identities, together with source aperiodicity, are the remaining information that must be exploited.

## Conservative verdict on Cycle106

Cycle106 itself contributed no mathematical evidence. Its Fable run failed before receiving the source snapshot.

The proposed Cycle106 wall is genuine, but the best current reduction is now strictly smaller:

> Count the distinct (b_1)-readouts of the rank-one locus (3), after one active base divisor has been fixed.

This is stronger than merely rewriting (\Gamma\cap M_s). It converts the problem to explicit (2\times2) minors and gives exact treatment of external values, internal one-point swaps, and same-slope multiplicity.

Confidence:

* algebraic reduction and packing consequences: **high**;
* choice of the next route: **moderate**;
* truth of the remaining aperiodic inverse theorem: **unknown**.

## Missing source hypothesis

The supplied compact packet repeatedly invokes

[
\text{“aperiodic }\widehat U\text{ above corrected reserve”}
]

but does not contain its exact definition or its negation certificate. In particular, it does not specify whether aperiodicity:

1. is a property of the truncated jet (\widehat U\bmod X^r); or
2. depends on a fuller source datum invisible to Cycle105’s incidence equations.

That is the first exact source-audit gate. Since the active set depends only on the (r)-jet, a proof based solely on (3) can consume source aperiodicity only if one proves one of the following:

[
\boxed{
\text{aperiodicity is determined by the }r\text{-jet},
}
\tag{17}
]
or the stronger implication
[
\boxed{
\text{any superpolynomial rank-one family forces an
aperiodicity violation for every source lift of that jet.}
}
\tag{18}
]

If two source-valid objects can share the same (r)-jet while one is periodic and the other aperiodic, then Cycle106 is missing a necessary hypothesis: its incidence set cannot distinguish those objects.

The exact gate should be named

[
\boxed{\texttt{L-CYCLE107-APERIODICITY-JET-VISIBILITY}}.
]

## Exact next theorem

[
\boxed{\texttt{W-CYCLE107-CENTRAL-APERIODIC-MOBIUS-JET-RANKONE-INVERSE}}
]

### Inputs

* (p) prime, (n\mid p-1), (H=\mu_n);
* (r=\sigma+2\le n);
* (m=n-\sigma-k);
* a source-valid datum satisfying the exact corrected-reserve condition;
* an active base pair ((\theta_0,T_0));
* the actual source-defined aperiodicity predicate;
* (B_T,b_j(T),\Delta_j(T)) as in (3);
* the central regime (k\to\infty) and (m-\sigma\to\infty).

Define
[
\Lambda(T_0,\theta_0)
=====================

\left{
-b_1(T):
T\in\binom Hm,\
\Delta_2(T)=\cdots=\Delta_{r-1}(T)=0
\right}.
]

### Required output

Prove that there is an absolute (C), depending only on the fixed reserve constants and not on (k,m,s,p), such that
[
\boxed{
|\Lambda(T_0,\theta_0)\setminus H|\le n^C.
}
\tag{19}
]

The preferred inverse form is stronger and more useful:

> If (|\Lambda\setminus H|>n^C), output the exact tuple appearing in the negation of the source aperiodicity definition—such as its quotient scale, coset decomposition, pullback polynomial, dephasing datum, or other required certificate.

A conclusion merely saying “the family looks periodic” is insufficient.

## Copy-ready next prompt

```text
Required label: PROOF, COUNTERPACKET, BANKABLE_LEMMA, ROUTE_CUT,
EXACT_NEW_WALL, AUDIT, or PLAN.

Attack:

W-CYCLE107-CENTRAL-APERIODIC-MOBIUS-JET-RANKONE-INVERSE

No Internet. Read every listed source file before reasoning.

MANDATORY GATE 0

Locate and quote verbatim the exact source definitions of:

1. “aperiodic Uhat”;
2. “above corrected reserve”;
3. the exact certificate witnessing failure of aperiodicity.

Prove L-CYCLE107-APERIODICITY-JET-VISIBILITY: explain exactly how that
source hypothesis constrains the r-jet Uhat mod X^(sigma+2). If the
aperiodicity predicate is not jet-visible, either carry the full source
datum through the theorem or return AUDIT/ROUTE_CUT with two admissible
lifts having the same jet but opposite aperiodicity status.

BANKED REDUCTION

Let r=sigma+2, H=mu_n, m=n-s, and

    h_T(X)=prod_{x in T}(1-xX).

Cycle105 gives

    theta active
    iff exists T subset H, |T|=m, with
        h_T Uhat = 1-theta X mod X^r.

If there is an active pair (theta0,T0), then

    Uhat=(1-theta0 X)h_T0^(-1) mod X^r.

For every m-subset T define

    B_T=(1-theta0 X)h_T-h_T0 mod X^r
       =sum_{j=1}^{r-1} b_j(T)X^j,

and

    Delta_j(T)
      =b_j(T)-b_1(T)[X^(j-1)]h_T0,
      2<=j<=r-1.

Then exactly

    Theta_Uhat
      ={-b_1(T):
         |T|=m and Delta_j(T)=0 for every 2<=j<=r-1}.

Do not replace this distinct b_1-image by the number of supports.

SHORT-PETAL FACT

For distinct external active theta values, chosen witnesses satisfy

    |T_theta \ T_theta'| >= sigma+1.

For equal slopes and distinct supports the bound is sigma+2.
The only distinct-slope case with petal size <=sigma is the internal
one-point swap:

    theta,theta' in H,
    T\T'={theta},
    T'\T={theta'}.

TARGET

Prove that, for source-aperiodic data above corrected reserve,

    #{-b_1(T) outside H:
       |T|=m and Delta_2(T)=...=Delta_(r-1)(T)=0}
      <= n^C

for an absolute exponent C independent of m,s,k and p.

Prefer an inverse theorem:

    more than n^C distinct readouts
    => exact source-valid certificate violating aperiodicity.

The result must use the above-reserve aperiodicity hypothesis. A generic
RS list bound, Johnson-radius argument, weighted Fourier count,
constant-weight packing bound, or unconditional divided-difference
argument is not accepted.

COUNTERPACKET STANDARD

A counterpacket must give a parameterized sequence containing:

- p_n, n, sigma_n, k_n, m_n;
- the full source datum, not only its truncated jet;
- a corrected-reserve certificate;
- an aperiodicity certificate in the exact source syntax;
- an active base pair (theta0,T0);
- more than n^A distinct external readouts for every fixed A along a
  subsequence;
- one explicit support T_theta for each readout;
- proof that quotient/coset-swap structure has not merely been renamed.

FINITE COMPUTATION

Finite searches may identify a base gadget, but a finite instance alone is
not a counterpacket. A successful counterpacket requires an inflation,
tensorization, or replication theorem preserving distinct theta values,
corrected reserve, and source aperiodicity.

STOP

Return PROOF only after verifying the exact source aperiodicity bridge.
Return COUNTERPACKET only with a growing distinct-theta family.
Return ROUTE_CUT if aperiodicity is not jet-visible.
Return EXACT_NEW_WALL only after a further strict, explicitly stated
reduction.
```

## Required context files

The next prompt must receive:

```text
context/CURRENT_CYCLE106_BRIEF.md
context/CURRENT_CYCLE105_BRIEF.md
context/m1_cycle105_uniform_bandwidth_divisor_incidence_audit.md
context/m1_cycle106_kfree_aperiodic_moment_curve_incidence_audit.md
context/cycle106_kfree_aperiodic_moment_curve_incidence_prompt.md
context/cycle105_kfree_collapse_check.py
context/ROUTE_BOARD_CURRENT.md
context/ACTIVE_WALLS.md
context/BANKED_LEMMAS.md
context/CUTS_AND_FALSE_ROUTES.md
```

It must additionally receive the actual source file or paper section containing the full definition of aperiodicity, the corrected-reserve inequality, and the negation certificate referred to as `rem:aper`. That material is absent from the compact packet. Any Cycle100/101 dephasing theorem invoked must also be supplied in its audited source form, not only as a route-board summary.

## Stop conditions

The route is **proved** when both jet visibility and (19) are established.

The route is **killed** by a source-valid sequence with
[
\frac{\log|\Lambda\setminus H|}{\log n}\longrightarrow\infty
]
while satisfying the exact corrected-reserve and aperiodicity predicates.

The wall must be **reformulated** if two admissible full source data have the same (r)-jet, and hence the same rank-one locus and active values, but opposite aperiodicity status. Then the corrected target must retain additional full-source information.

A finite checker failure would indicate an implementation or transcription error in the reduction, not evidence about the asymptotic inverse theorem.

The finite replay of the exact equivalence, petal-distance bound, and both packing inequalities passed on 144 small basepoints:

[Cycle107 Möbius-jet reduction checker](sandbox:/mnt/data/cycle107_mobius_jet_reduction_check.py)

## Self-audit

**Exact implication proved:** Cycle105 activity plus one active basepoint is equivalent to the rank-one equations (3), with active value exactly (-b_1(T)). Distinct external readouts satisfy the petal-distance bound and the two packing inequalities.

**Not proved:** No central (n^{O(1)}) incidence bound, no aperiodicity inverse, and no aperiodic growing-(k) counterpacket.

**Prize relevance:** This is a bankable structural reduction for the canonical M1 upper-side numerator. It is not an official Proximity Prize proof. No link has been verified from this balanced canonical wall through all-denominator MCA, protocol normalization, finite frontier accounting, or the official prize statement.

**First possible failure line:**
[
\text{superpolynomial rank-one readout family}
\Longrightarrow
\text{exact source aperiodicity violation}.
]
Before even attempting that implication, jet visibility of the source aperiodicity predicate must be established.

**Field ledger:** (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and (2^{-128}) are not used. The symbol (p) is only the ambient field characteristic. No field identification or entropy transfer is being assumed.

**Structural reductions:** Quotient-periodic structure may produce large rank-one families and must be classified using the exact source predicate. Internal/contained values contribute at most (n), with the only short-petal exception being a one-point internal swap. Same-slope support multiplicity does not enlarge the distinct numerator. The basepoint dephasing above is exact and preserves (H); a Möbius coordinate change normalizing (\theta_0) would generally move (H) away from a multiplicative subgroup and therefore cannot be used without re-verifying aperiodicity and quotient structure.
