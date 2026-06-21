BANKABLE_LEMMA

### L-CYCLE106-BOOLEAN-FOURIER-SHELL-REDUCTION

Let (d=\sigma+1). There is an exact Fourier reduction that counts **distinct (\theta)** and exposes the precise point where above-reserve aperiodicity must act.

Assume the banked normalization (\widehat U(0)=1), and define the truncated logarithmic moments

[
P_j=-j[X^j]\log \widehat U(X),\qquad 1\le j\le d.
]

For an (s)-subset (S\subset H), write

[
p_j(S)=\sum_{x\in S}x^j,
\qquad
\mathcal P_s=
\left{(p_1(S),\ldots,p_d(S)):|S|=s\right},
]

where (\mathcal P_s) is a set of **distinct moment vectors**, not a multiset of witnesses.

Because (d\le n<p), Newton identities give a triangular bijection between (\mathcal P_s) and the elementary-symmetric layer (M_s).

The Cycle105 incidence condition is therefore exactly

[
\theta\text{ active}
\iff
P-v_d(\theta)\in\mathcal P_s,
\qquad
v_d(\theta)=(\theta,\theta^2,\ldots,\theta^d).
\tag{1}
]

Indeed,

[
-j[X^j]\log g_S(X)=p_j(S)
]

and

[
-j[X^j]\log \frac{\widehat U(X)}{1-\theta X}
=P_j-\theta^j.
]

Thus the desired distinct support is

[
I_s(P):=
|\Gamma\cap M_s|
================

\sum_{\theta\in\mathbb F_p}
1_{\mathcal P_s}\bigl(P-v_d(\theta)\bigr).
\tag{2}
]

This already removes witness multiplicity completely.

---

## 1. Exact Boolean Fourier formula

The group being Fourier-expanded is the additive group

[
A_d=(\mathbb F_p^d,+),
]

not the multiplicative group (H).

Fix a nontrivial additive character (\psi), and use

[
\widehat f(t)=\sum_{y\in A_d}f(y)\psi(-\langle t,y\rangle).
]

Then

[
I_s(P)
======

\frac1{p^d}
\sum_{t\in\mathbb F_p^d}
\widehat{1_{\mathcal P_s}}(t),
\psi(\langle t,P\rangle),
K_d(t),
\tag{3}
]

where

[
K_d(t)
======

\sum_{\theta\in\mathbb F_p}
\psi!\left(-\sum_{j=1}^d t_j\theta^j\right).
\tag{4}
]

The exact nonzero-frequency phase is therefore

[
\psi!\left(
\sum_{j=1}^d t_j(P_j-\theta^j)
\right).
\tag{5}
]

This formula counts distinct active (\theta), not active pairs.

The zero mode is

[
\frac{|\mathcal P_s|}{p^{d-1}}
==============================

\frac{|\mathcal P_s|}{p^\sigma}
\le
\frac{\binom ns}{p^\sigma}
\le
\frac{2^n}{p^\sigma}.
\tag{6}
]

Thus the only numerical reserve implication needed here is

[
\frac{2^n}{p^\sigma}\le n^{O(1)}.
\tag{7}
]

No (2^{-128}) arithmetic is required.

---

## 2. Where aperiodicity can enter—and where it cannot

Let

[
r(t)=\max{j:t_j\neq0}.
]

For (t\neq0):

[
K_d(t)=0\quad\text{if }r(t)=1,
]

and for (2\le r(t)<p),

[
|K_d(t)|\le (r(t)-1)\sqrt p.
\tag{8}
]

For quadratic modes (r(t)=2),

[
|K_d(t)|=\sqrt p
\tag{9}
]

exactly.

Crucially, (\widehat U) enters (3) only through the unit phase

[
\psi(\langle t,P\rangle).
]

Consequently:

* (|K_d(t)|) is independent of (\widehat U);
* (|\widehat{1_{\mathcal P_s}}(t)|) is independent of (\widehat U);
* every (L^q)-norm or modewise-magnitude estimate is identical for periodic and aperiodic (\widehat U).

Therefore aperiodicity cannot improve any individual character sum. It must create cancellation **between different frequencies (t)** through the dephasing factors (\psi(\langle t,P\rangle)).

This rigorously cuts every Fourier proof based only on

[
|\widehat{1_{\mathcal P_s}}(t)|,\qquad
|K_d(t)|,
]

or their norm estimates. Such an argument would be independent of (P) and would consequently also prove the bound for the banked periodic branch, where superpolynomial configurations are known to exist.

---

## 3. Exact distinct-support shell decomposition

For (1\le r\le d), define the extension-count function of the **distinct full moment image**

[
\nu_{r,s}(y_1,\ldots,y_r)
=========================

#\left{
z\in\mathcal P_s:
(z_1,\ldots,z_r)=(y_1,\ldots,y_r)
\right}.
\tag{10}
]

These are not subset-witness multiplicities. They count distinct full (d)-moment vectors extending a given (r)-prefix. In particular,

[
\nu_{d,s}=1_{\mathcal P_s}.
]

Set

[
J_{r,s}(P)
==========

\sum_{\theta\in\mathbb F_p}
\nu_{r,s}
\bigl(P_1-\theta,\ldots,P_r-\theta^r\bigr).
\tag{11}
]

Then

[
J_{d,s}(P)=I_s(P).
\tag{12}
]

Since (\theta\mapsto P_1-\theta) is bijective,

[
J_{1,s}(P)=|\mathcal P_s|.
\tag{13}
]

For (r\ge2), define the signed shell correlation

[
C_{r,s}(P)
==========

\sum_{\substack{t\in\mathbb F_p^r\t_r\neq0}}
\widehat{\nu_{r,s}}(t),
\psi(\langle t,P_{\le r}\rangle),
K_r(t).
\tag{14}
]

Fourier inversion, separating (t_r=0), gives the exact recurrence

[
J_{r,s}(P)
==========

\frac1pJ_{r-1,s}(P)
+
\frac1{p^r}C_{r,s}(P).
\tag{15}
]

Define

[
\Delta_{r,s}(P)
===============

# J_{r,s}(P)-\frac1pJ_{r-1,s}(P)

\frac{C_{r,s}(P)}{p^r}.
\tag{16}
]

Iterating (15) yields

[
I_s(P)
======

\frac{|\mathcal P_s|}{p^{d-1}}
+
\sum_{r=2}^d p^{,r-d}\Delta_{r,s}(P).
\tag{17}
]

This is the exact direct-support analogue of the Cycle99 weighted character-sum formula.

Since

[
\sum_{r=2}^d p^{r-d}<\frac{p}{p-1},
]

a large incidence forces one genuinely large positive shell:

[
\max_{2\le r\le d}\Delta_{r,s}(P)
\ge
\frac{p-1}{p}
\left(
I_s(P)-\frac{|\mathcal P_s|}{p^{d-1}}
\right).
\tag{18}
]

Thus a superpolynomial aperiodic counterpacket necessarily produces a specific (r) with superpolynomial one-step conditional concentration.

---

## 4. Exact next lemma that would prove Cycle106

The required theorem is:

### T-CYCLE107-APERIODIC-BOOLEAN-SHELL-INVERSE

There exists an absolute (C), independent of (s,k,r), such that for every above-reserve aperiodic (\widehat U),

[
\Delta_{r,s}(P)\le n^C
\qquad
\text{for every }s\text{ and every }2\le r\le d.
\tag{19}
]

Equivalently, in inverse form,

[
\Delta_{r,s}(P)>n^C
\Longrightarrow
\widehat U
\text{ admits a charged quotient/subgroup-periodic certificate}.
\tag{20}
]

If (19) holds, then (17) and the reserve bound give

[
|\Gamma\cap M_s|
\le
\frac{2^n}{p^\sigma}
+
\frac{p}{p-1}n^C
================

n^{O(1)}
\tag{21}
]

uniformly in (s) and (k).

This is the exact next lemma. It is phase-sensitive, counts distinct support, and has no hidden (\binom nk) loss.

The first substantive risk is that the project’s actual aperiodicity condition may not be hereditary under truncation from (P_{\le d}) to (P_{\le r}). In that case, (20) must prove that a periodic certificate detected at an intermediate shell lifts to a forbidden periodic certificate for the full (\widehat U).

---

## 5. Exact quotient-periodic resonance in the Fourier variables

There is a weighted (H)-action on frequencies:

[
h\star(t_1,\ldots,t_r)
======================

(h^{-1}t_1,h^{-2}t_2,\ldots,h^{-r}t_r).
\tag{22}
]

Because (S\mapsto hS) preserves (s)-subsets of (H),

[
\widehat{\nu_{r,s}}(h\star t)
=============================

\widehat{\nu_{r,s}}(t),
]

and changing (\theta\mapsto h\theta) gives

[
K_r(h\star t)=K_r(t).
]

Hence an orbit contributes through the dephasing sum

[
D_{t,P}
=======

\sum_{h\in H/\operatorname{Stab}(t)}
\psi!\left(
\sum_{j=1}^r h^{-j}t_jP_j
\right).
\tag{23}
]

Moreover,

[
|\operatorname{Stab}(t)|
========================

\gcd!\left(n,{j:t_j\neq0}\right).
\tag{24}
]

Thus nontrivial stabilizer is exactly a quotient-periodic frequency: the phase polynomial (L_t(x)) is constant on cosets of a nontrivial subgroup of (H).

This identifies the candidate mechanism precisely:

* nontrivial stabilizer modes are the charged quotient-periodic branch;
* full-orbit modes require genuine aperiodic cancellation in (D_{t,P}) and across different orbits.

A separate Weil estimate on each (D_{t,P}) is not enough. It gives at most a polynomial orbit-size saving, whereas the central layers carry superpolynomial Fourier mass.

---

## 6. Why the usual character-sum closure fails at central rate

Parseval gives, for (r\ge2),

[
\sum_{t\in\mathbb F_p^r}|K_r(t)|^2=p^{r+1},
]

and after removing (t_r=0),

[
\sum_{t_r\neq0}|K_r(t)|^2=p^r(p-1).
\tag{25}
]

Also,

[
\sum_t|\widehat{\nu_{r,s}}(t)|^2
================================

p^r\sum_y\nu_{r,s}(y)^2.
\tag{26}
]

Consequently the direct Cauchy closure is only

[
|\Delta_{r,s}(P)|
\le
\sqrt{(p-1)\sum_y\nu_{r,s}(y)^2}.
\tag{27}
]

At the final shell,

[
\sum_y\nu_{d,s}(y)^2=|\mathcal P_s|,
]

so

[
|\Delta_{d,s}(P)|
\le
\sqrt{(p-1)|\mathcal P_s|}.
\tag{28}
]

This is generally superpolynomial in the central regime.

Indeed, moment fibers themselves form constant-weight codes. If two distinct (s)-subsets (S,T) have the same first (d) power sums, put

[
r_0=|S\setminus T|=|T\setminus S|.
]

If (r_0\le d), Newton identities applied to (S\setminus T) and (T\setminus S) imply equality of those two multisets, a contradiction. Hence

[
r_0\ge d+1.
]

Thus every fiber has Johnson minimum distance at least (d+1). Sphere packing in (J(n,s)) gives

[
|\mathcal P_s|
\ge
\sum_{i=0}^{\lfloor d/2\rfloor}
\binom{s}{i}\binom{n-s}{i},
\tag{29}
]

with the upper limit truncated by (\min(s,n-s)) when necessary. For central (s) and growing (d), this is superpolynomial. Therefore Parseval, large sieve, absolute Fourier mass, and separate Weil estimates cannot close Cycle106.

---

## 7. Why the Cycle99 elementary-symmetric transform is not enough

Let

[
R_s(y)
======

#{S\subset H:|S|=s,\ p(S)=y}.
]

Its Fourier transform is explicitly computable:

[
\widehat R_s(t)
===============

e_s!\left(
{\psi(-L_t(x)):x\in H}
\right),
\qquad
L_t(X)=\sum_{j=1}^d t_jX^j.
\tag{30}
]

But

[
1_{\mathcal P_s}(y)=1_{{R_s(y)>0}}
]

is a nonlinear Booleanization. There is no linear conversion from (\widehat R_s) to (\widehat{1_{\mathcal P_s}}).

The weighted count

[
N_s(P)=
\sum_\theta R_s(P-v_d(\theta))
]

satisfies (I_s(P)\le N_s(P)), so a polynomial upper bound on (N_s) would suffice. However its standard Parseval closure is

[
\left|
N_s(P)-\frac{\binom ns}{p^{d-1}}
\right|
\le
\sqrt{pE_s},
\qquad
E_s=\sum_yR_s(y)^2\ge\binom ns.
\tag{31}
]

For central (s), this is exponential. Thus the computable weighted transform does not solve the distinct-support problem without a new phase-sensitive theorem.

---

## Self-audit

**Exact implication proved.**

[
\left[
\frac{2^n}{p^\sigma}\le n^{C_0}
\ \text{and}
\Delta_{r,s}(P)\le n^C\ \forall r,s
\right]
\Longrightarrow
|\Gamma\cap M_s|\le n^{O(1)}.
]

Also, any superpolynomial incidence forces a specific shell (r) with superpolynomial positive discrepancy by (18).

**Exact implication not proved.**

I did not prove that above-reserve aperiodicity implies the shell bound (19), nor that every anomalously large shell correlation yields a project-valid periodic certificate. That is now the first exact theorem.

**Status relative to the official prize.**

This is a single-field, upper-side research reduction. Proving the next shell-inverse theorem would close the current Cycle106 numerator wall, assuming Cycles103–105 and the precise aperiodic/periodic charging are valid. It would not by itself verify every link to the official Proximity Prize statement.

**First line where the theorem can fail.**

The first non-exact line is

[
\text{above-reserve aperiodicity of }\widehat U
\Longrightarrow
\Delta_{r,s}(P)\le n^{O(1)}.
]

More specifically, aperiodicity may fail to descend to intermediate logarithmic prefixes (P_{\le r}), or a genuinely aperiodic (P) may still align with the signed Boolean shell spectrum.

**Field ledgers.**

(q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}), and the (2^{-128}) target are not used. This is correct: the reduction is entirely over the single field (\mathbb F_p). Reserve is used only through (2^n/p^\sigma\le n^{O(1)}).

**Possible numerator reductions.**

Quotient-periodic structure appears exactly as nontrivial frequency stabilizers (24) and may be charged separately. Contained incidences remain real incidences and are not silently discarded. Same-slope collisions do not inflate the answer because (P_1-\theta) determines (\theta) injectively. Subset-witness multiplicity is removed by using (1_{\mathcal P_s}). Newton/logarithmic or affine color normalizations are invertible triangular changes of coordinates and do not alter the distinct numerator.

**Confidence:** high for the exact reduction and the phase-blind route cut; unknown for the aperiodic Boolean-shell inverse theorem.
