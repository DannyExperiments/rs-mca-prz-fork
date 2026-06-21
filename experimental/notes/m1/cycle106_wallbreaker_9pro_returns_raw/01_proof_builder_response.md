BANKABLE_LEMMA

Let (d=\sigma+1) and (\Theta_s={\theta:\Gamma(\theta)\in M_s}). I do not obtain the full polynomial bound, but I obtain a strict distinct-(\theta) reduction and the uniform bound
[
|\Theta_s|\le d(d+1)^{n/d}=n^{O(\log n)}
]
at corrected reserve. The exact remaining lemma is an aperiodic (d)-fold profile-entropy inverse theorem.

### 1. Exact activity identity

For each (\theta\in\Theta_s), choose one witness (S_\theta\subset H), (|S_\theta|=s). In
[
R_d=\mathbb F_p[X]/(X^{d+1}),
]
the Cycle105 identity is
[
(1-\theta X)g_{S_\theta}(X)=\widehat U(X),\qquad
g_S(X)=\prod_{x\in S}(1-xX). \tag{1}
]
This is the banked (k)-free collapse; Cycle105 did not bound the resulting incidence uniformly in (k). 

Also,
[
g_1(\theta)=u_1+\theta,
]
so (\Gamma) is injectively parametrized by (\theta). Hence all bounds below are genuinely on distinct active parameters, not on weighted witnesses.

## 2. Pairwise rainbow-prefix rigidity

Take distinct active (\theta,\phi\notin H), with witnesses (S_\theta,S_\phi). Put
[
C=S_\theta\cap S_\phi,\qquad
A=S_\theta\setminus S_\phi,\qquad
B=S_\phi\setminus S_\theta,
]
and (r=|A|=|B|). Cancelling the unit (g_C) from (1) gives
[
(1-\theta X)g_A(X)
\equiv
(1-\phi X)g_B(X)
\pmod{X^{d+1}}. \tag{2}
]

If (r<d), both sides have degree at most (r+1\le d), so (2) is an exact polynomial equality. Unique factorization then gives
[
A\sqcup{\theta}=B\sqcup{\phi}
]
as multisets of linear factors. This is impossible for distinct (\theta,\phi\notin H), since (A,B\subset H) are disjoint. The cases where one parameter is zero are also impossible by degree comparison.

Therefore
[
\boxed{|S_\theta\setminus S_\phi|\ge d},
\qquad
\boxed{|S_\theta\triangle S_\phi|\ge2d}. \tag{3}
]

Consequently, whenever
[
\min(s,n-s)<d,
]
there is at most one external active parameter, and hence
[
|\Theta_s|\le n+1.
]
Thus only the central regime (d\le s,n-s) remains.

Equivalently, after reversing the polynomials, every pair gives an exact defect identity
[
(Z-\theta)P_A(Z)-(Z-\phi)P_B(Z)=R_{\theta,\phi}(Z),
\qquad
\deg R_{\theta,\phi}\le r-d. \tag{4}
]
At minimum distance (r=d), the defect is constant. This is the precise Prouhet–Tarry–Escott-type rigidity forced by distinct active parameters.

## 3. (h)-fold profile injectivity

Fix (1\le h\le d). For an unordered (h)-multiset
[
\boldsymbol\theta={\theta_1,\ldots,\theta_h}\subseteq\Theta_s,
]
define its occupancy profile
[
z_{\boldsymbol\theta}(x)
========================

#{i:x\in S_{\theta_i}},
\qquad x\in H,
]
and its truncated profile polynomial
[
P_{\boldsymbol\theta}(X)
========================

\prod_{x\in H}(1-xX)^{z_{\boldsymbol\theta}(x)}
\pmod{X^{d+1}}.
]

Multiplying (1) over (i=1,\ldots,h) gives
[
Q_{\boldsymbol\theta}(X)P_{\boldsymbol\theta}(X)
================================================

\widehat U(X)^h
\quad\text{in }R_d, \tag{5}
]
where
[
Q_{\boldsymbol\theta}(X)=\prod_{i=1}^h(1-\theta_iX).
]

Suppose two (h)-multisets have the same truncated profile polynomial. It is a unit because its constant term is (1), so cancelling it in (5) gives
[
Q_{\boldsymbol\theta}\equiv Q_{\boldsymbol\phi}\pmod{X^{d+1}}.
]
Both polynomials have degree at most (h\le d); hence the equality is exact. Unique factorization recovers the multisets of nonzero parameters. Since (h) is known, the multiplicity of the parameter (0) is also recovered from the degree.

Thus:

[
\boxed{
\boldsymbol\theta\longmapsto P_{\boldsymbol\theta}
\text{ is injective on unordered (h)-multisets.}
} \tag{6}
]

This completely eliminates witness multiplicity from the counting problem.

Let (L=|\Theta_s|). There are (\binom{L+h-1}{h}) unordered (h)-multisets. Every occupancy vector has coordinates in ({0,\ldots,h}) and total weight (hs). Therefore
[
\boxed{
\binom{L+h-1}{h}
\le
[Y^{hs}](1+Y+\cdots+Y^h)^n.
} \tag{7}
]

In particular,
[
\frac{L^h}{h!}
\le
\binom{L+h-1}{h}
\le
(h+1)^n,
]
so
[
L\le (h!)^{1/h}(h+1)^{n/h}
\le h(h+1)^{n/h}. \tag{8}
]

Taking (h=d) proves the unconditional, (s)- and (k)-uniform bound
[
\boxed{
|\Gamma\cap M_s|
\le d(d+1)^{n/d}.
} \tag{9}
]

At (d\asymp n/\log n), this is
[
|\Gamma\cap M_s|\le \exp(O((\log n)^2))=n^{O(\log n)}.
]
It is quasi-polynomial, not polynomial.

## 4. Exact next lemma that closes the proof

Define the actual (d)-fold profile image
[
\mathscr P_d(\widehat U,s)
==========================

\left{
\prod_{x\in H}(1-xX)^{z_{\boldsymbol\theta}(x)}
\bmod X^{d+1}:
\boldsymbol\theta\in\operatorname{MSet}_d(\Theta_s)
\right}.
]
By (6),
[
\boxed{
|\mathscr P_d(\widehat U,s)|
============================

\binom{|\Theta_s|+d-1}{d}.
} \tag{10}
]

The precise missing theorem is:

[
\boxed{\texttt{L-CYCLE107-APERIODIC-D-FOLD-PROFILE-ENTROPY-INVERSE}}
]

There must be an explicit constant (A_{\rm ap}<\infty), independent of (n,s,k), such that every source-valid above-reserve datum satisfies the following dichotomy:

[
|\mathscr P_d(\widehat U,s)|\le A_{\rm ap}^{,n}, \tag{11}
]
or the checker outputs one of the source-forbidden structures:

1. a tangent, common-core, or common-envelope certificate; or
2. an active quotient scale
   [
   M_0\mid\gcd(n,k),\qquad M_0>\deg E,
   ]
   and a nonzero polynomial (m(Y)) with
   [
   \deg m<\deg E,\qquad E(X)\mid m(X^{M_0}). \tag{12}
   ]

Condition (12) is exactly
[
d_{M_0}(E)<\deg E,
]
or equivalently
[
\mathbb F[,[X^{M_0}],]
\subsetneq
\mathbb F[X]/(E).
]
The repaired denominator-level aperiodicity condition found in the adjacent source is precisely (d_M(E)=\deg E) for every active (M). 

This theorem closes Cycle106 immediately. Indeed, if the forbidden alternatives are excluded, then by (10)–(11),
[
\frac{|\Theta_s|^d}{d!}\le A_{\rm ap}^{,n},
]
and hence
[
|\Theta_s|
\le (d!)^{1/d}A_{\rm ap}^{n/d}
\le dA_{\rm ap}^{n/d}. \tag{13}
]
If the corrected reserve gives
[
d\ge C,\frac{n}{\log_2 n},
]
then
[
A_{\rm ap}^{n/d}
\le n^{(\log_2 A_{\rm ap})/C},
]
so
[
\boxed{
|\Gamma\cap M_s|
\le n^{,1+(\log_2 A_{\rm ap})/C},
} \tag{14}
]
uniformly in (s) and (k).

This visibly uses both required hypotheses:

* **above reserve** converts an exponential-in-(n) profile bound into a polynomial distinct-(\theta) bound;
* **aperiodicity** rules out the low-action-rank output (12).

## 5. Why the inverse theorem is the first real obstruction

It is not enough to prove that individual characters or literal coset swaps are nonperiodic. The adjacent model work constructs finite-characteristic prefix collisions that tensor while remaining outside the ordinary block-equivalence class. It explicitly concludes that a support/configuration entropy bound is needed, not merely a character-periodic quotient.

Therefore the exact theorem must prove one of these two statements:

[
\text{large (d)-fold profile entropy}
\Longrightarrow
\text{low source action rank}, \tag{15}
]
or
[
\text{large (d)-fold profile entropy}
\Longrightarrow
\text{a finite-characteristic collision-class certificate}
]
which can then be tensorized into a genuine aperiodic counterpacket.

A theorem that only detects full subgroup blocks is too weak.

The corresponding finite stress checker should be named

[
\boxed{\texttt{cycle107_profile_action_rank_descent_check.py}}.
]

Its exact outputs should be:

* `PROFILE_ENTROPY_CAP`, with the computed value of (|\mathscr P_d|);
* `ACTION_RANK_DESCENT(M,m)`, verifying (E\mid m(X^M)) and (\deg m<\deg E);
* `SOURCE_EXCLUDED_STRUCTURE`;
* `APERIODIC_PROFILE_COUNTERPACKET_CANDIDATE`, containing all distinct (\theta), their selected witnesses, the full (d_M(E)) table, and the profile hashes.

The existing weighted-closure checker is useful as a second backend: a relation (F\in I(M_s)) whose restriction to (\Gamma) is nonzero gives the immediate incidence bound (|\Gamma\cap M_s|\le\deg_\theta F(\Gamma)), but it is currently only an exponential finite/model checker. 

## Self-audit

**Exact implication proved.**
I proved pairwise external-support distance at least (2d), exact (h)-fold profile injectivity for every (h\le d), and
[
|\Gamma\cap M_s|\le d(d+1)^{n/d}.
]
I also proved that the explicit entropy bound (11) implies the desired polynomial incidence bound via (14).

**Exact implication not proved.**
I did not prove (11), nor that every violation produces the source action-rank certificate (12). Therefore I did not prove the Cycle106 wall.

**Prize relevance.**
This is an upper-side structural research lemma, not an official prize certificate. The full reduction from this wall through the M1 numerator, field denominators, frontier accounting, and the official statement has not been verified here.

**First possible failure line.**
The first unproved line is
[
|\mathscr P_d|>A_{\rm ap}^{,n}
\Longrightarrow
d_M(E)<\deg E
\quad\text{or another formally excluded source structure}.
]
Moreover, the compact Cycle106 packet never states the formal bridge from the (Uhat)-level word to the repaired denominator-level component-aperiodicity predicate. That bridge must be included in the theorem.

**Field ledgers.**
(q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and the (2^{-128}) target are not used. That is correct: this is a single-field numerator wall, before any normalization by a line field or frontier comparison.

**Possible numerator reductions.**

* Periodic or quotient swaps preserving the truncated subset polynomial preserve (g_1), hence preserve (\theta); they increase witness multiplicity but not the distinct numerator.
* Contained incidences can only reduce the source-relevant noncontained numerator; the bound above conservatively includes them.
* Same-slope collisions are removed by selecting one witness for each distinct (\theta).
* Affine color normalization cannot merge parameters because (g_1(\theta)=u_1+\theta) is injective.

**Confidence.**
High for (3), (6), (7), and (9). Unknown for the profile-entropy/action-rank inverse theorem.
