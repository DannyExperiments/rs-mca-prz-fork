COUNTERPACKET

The interleaved-to-scalar projection theorem is complete. The scalar theorem is **false in a domain-uniform form if the quotient reserve only recognizes multiplicative maps (X\mapsto X^M)**. There is an exact additive-quotient packet with actual codewords, canonical full supports, positive entropy margin, no common agreement coordinate, trivial multiplicative quotient profile, and list size above the official (2^{-128}) target.

This does not yet refute the narrower conjecture restricted to official power-of-two multiplicative domains.

## 1. Exact theorem, lemma, and counterpacket

### A. Exact projection theorem

Let (K=\mathbb F_q), let (C\subseteq K^n) be any linear code, and write (L_m(a)) for the worst (m)-interleaved list size at column agreement at least (a).

If
[
L_1(a)\le L
\qquad\text{and}\qquad
\binom{L+1}{2}<q,
]
then, for every (m\ge1),
[
L_m(a)\le L.
]

Consequently, if
[
T=\left\lfloor\frac{q_{\rm chal}}{2^{128}}\right\rfloor
\quad\text{and}\quad
\binom{T+1}{2}<q_{\rm code},
]
then at every agreement threshold (a),
[
L_m(a)\le T
\quad\Longleftrightarrow\quad
L_1(a)\le T.
]

In the official same-field normalization
[
q_{\rm chal}=q_{\rm code}=q\le2^{256},
]
the inequality always holds. Hence
[
\boxed{
\delta_{\rm list}^*(C,m,2^{-128})
=================================

\delta_{\rm list}^*(C,1,2^{-128})
}
]
for every interleaving arity (m).

### B. Critical full-support locator-syzygy lemma

Let (H) be a standard GRS parity-check matrix with syndrome dimension
[
r=n-k.
]
Suppose one nonzero syndrome (s) has full-support representations on error sets
[
E_1,\ldots,E_m,\qquad |E_i|=e_i<r.
]
Let
[
L_{E_i}(X)=\prod_{x\in E_i}(X-x).
]

Choose positive integers (b_i) satisfying
[
b_i\le r-e_i,
\qquad
\sum_{i=1}^m b_i=r.
]
Then there are polynomials (A_i), not all zero, such that
[
\boxed{
\sum_{i=1}^m A_i(X)L_{E_i}(X)=0,
\qquad
\deg A_i<b_i.
}
]

For a support-minimal such relation, every (A_i\neq0). If
[
A_i^{\rm agr}=D\setminus E_i,
]
then the agreement coordinates exclusive to codeword (i) inside that minimal subpacket satisfy
[
\boxed{
\left|
A_i^{\rm agr}\setminus
\bigcup_{h\ne i}A_h^{\rm agr}
\right|
\le b_i-1.
}
]

At the target (e_i\le r-\sigma), take
[
\ell=\left\lceil\frac r\sigma\right\rceil,\qquad
b_1=\cdots=b_{\ell-1}=\sigma,\qquad
b_\ell=r-(\ell-1)\sigma.
]
Thus any list of size at least (\ell) produces a support-minimal, low-degree, split-locator syzygy. This is the exact univariate dual of the Cycle 58 block-secant determinant.

### C. Additive-quotient full-support packet

Let (F=\mathbb F_{p^m}), and let (V\le F) be an (\mathbb F_p)-linear subspace of size
[
h=p^{m-s}.
]
Its subspace polynomial
[
\phi(X)=L_V(X)=\prod_{v\in V}(X-v)
]
is a (p)-linearized polynomial of degree (h), with kernel (V). Put
[
W=\phi(F),\qquad |W|=Q=p^s.
]
Every fiber of (\phi) is a coset of (V), hence has exactly (h) elements.

Take the evaluation domain
[
D=F^\times.
]
Fix (b\le Q-1) and suppose
[
(b-1)h<k<bh.
]
For every (b)-subset (A\subseteq W^\times), define
[
q_A(Z)=\prod_{\alpha\in A}(Z-\alpha),
]
[
Y(X)=\phi(X)^b,
]
and
[
P_A(X)=\phi(X)^b-q_A(\phi(X)).
]

Then:

1. Since (q_A) is monic of degree (b), the leading terms cancel:
   [
   \deg P_A\le(b-1)h<k.
   ]
   Thus (P_A) is an RS codeword.

2. On (D),
   [
   Y(x)-P_A(x)=q_A(\phi(x)).
   ]
   Therefore
   [
   A_Y(P_A)=\phi^{-1}(A),
   ]
   exactly.

3. Because (A\subseteq W^\times), all of its fibers avoid (0), and hence
   [
   |A_Y(P_A)|=bh.
   ]

4. Distinct (A)'s give distinct polynomials and distinct full agreement supports.

Consequently,
[
\boxed{
#{P\in RS[F,F^\times,k]:|A_Y(P)|=bh}
\ge
\binom{Q-1}{b}.
}
]

This is not a raw-support artifact. It is an actual list with exact, canonical full supports.

---

## 2. Proof details

### Projection proof

Suppose an (m)-interleaved list contains (L+1) distinct tuples
[
c^{(1)},\ldots,c^{(L+1)}\in C^m
]
around a received array (Y).

For (\lambda=(\lambda_1,\ldots,\lambda_m)\in K^m), define
[
\pi_\lambda(c_1,\ldots,c_m)=\sum_{u=1}^m\lambda_uc_u\in C
]
and project (Y) by the same linear functional.

For each pair (i\ne j), collision of the projected codewords means
[
\sum_u\lambda_u(c_u^{(i)}-c_u^{(j)})=0.
]
This is the kernel of a nonzero linear map (K^m\to K^n), so it has at most (q^{m-1}) elements.

The union of all collision kernels has size at most
[
\binom{L+1}{2}q^{m-1}<q^m.
]
Choose (\lambda) outside the union. All (L+1) projected codewords are distinct.

Every column on which an interleaved tuple agrees with (Y) remains an agreement after projection. Therefore the projection gives (L+1) distinct scalar codewords with agreement at least (a), contradicting (L_1(a)\le L).

The reverse inequality (L_m(a)\ge L_1(a)) follows by embedding
[
c\longmapsto(c,0,\ldots,0).
]

For the official target, put (x=q/2^{128}). Since (q\le2^{256}), one has (x\le2^{128}), and
[
\binom{T+1}{2}
\le
\frac{x(x+1)}2
<
2^{128}x
=q.
]

If (q_{\rm chal}\ne q_{\rm code}), the exact condition remains
[
T(T+1)<2q_{\rm code}.
]
A large challenge field cannot replace a small projection field.

If (B\subseteq F), (D\subseteq B), and ([F:B]=e), coordinate expansion gives
[
RS[F,D,k]\cong\operatorname{Int}(RS[B,D,k],e)
]
with exact preservation of column agreement. The projection condition must then be paid using (q_{\rm gen}=|B|), not (|F|).

### Locator-syzygy proof

After the usual nonzero GRS column rescaling, identify the parity-check columns with
[
h_x=(1,x,\ldots,x^{r-1})^{\mathsf T}.
]
Identify the dual of syndrome space with (F[X]_{<r}).

For an error set (E),
[
V_E^\perp
=========

L_E(X)F[X]_{<r-|E|}.
]
Indeed, a polynomial vector is orthogonal to every (h_x), (x\in E), precisely when it vanishes on (E).

Since (s\in V_{E_i}), every polynomial in
[
L_{E_i}F[X]*{<b_i}
]
lies in the hyperplane (s^\perp\subset F[X]*{<r}).

Consider
[
\Psi:\bigoplus_iF[X]*{<b_i}\longrightarrow F[X]*{<r},
\qquad
(A_i)*i\longmapsto\sum_iA_iL*{E_i}.
]
The source has dimension
[
\sum_i b_i=r,
]
while its image lies in the ((r-1))-dimensional hyperplane (s^\perp). Hence (\ker\Psi\ne0), proving the syzygy.

Now take a support-minimal relation. If (x) is agreed upon only by codeword (i) inside that subpacket, then
[
x\notin E_i,\qquad x\in E_h\quad(h\ne i).
]
Evaluating the syzygy at (x) kills every term except the (i)-th:
[
A_i(x)L_{E_i}(x)=0.
]
Since (L_{E_i}(x)\ne0), one has (A_i(x)=0). Hence all exclusive agreement points are roots of (A_i), giving the stated bound.

### Why the additive packet is a genuine quotient packet

The subspace-polynomial construction also gives the exact factorization
[
\boxed{
X^{q-1}-1
=========

\frac{\phi(X)}X
\prod_{\alpha\in W^\times}
\bigl(\phi(X)-\alpha\bigr).
}
]
Indeed,
[
\prod_{\alpha\in W}(\phi(X)-\alpha)
]
is monic of degree (q) and has every element of (F) as a root, so it equals (X^q-X).

Thus (F^\times) is partitioned into:

* one exceptional punctured fiber (V^\times) of size (h-1);
* (Q-1) full additive fibers of size (h).

This is structurally identical to the multiplicative quotient-core mechanism, except that the quotient map is the additive polynomial (\phi=L_V), not (X^M).

---

## 3. Parameter ledger

Specialize to
[
F=\mathbb F_{3^{103}},\qquad
D=F^\times.
]
Let
[
h=3^{99},\qquad Q=3^4=81.
]
Choose an (\mathbb F_3)-subspace (V) of dimension (99), and let (\phi=L_V).

Take the official rate
[
\rho=\frac12.
]

| Parameter                               |               Exact value |
| --------------------------------------- | ------------------------: |
| (q_{\rm gen}=q_{\rm line}=q_{\rm chal}) |               (q=3^{103}) |
| (n)                                     |               (81h-1=q-1) |
| (k)                                     |   ((81h-1)/2=40h+(h-1)/2) |
| (b)                                     |                      (41) |
| (a)                                     |                     (41h) |
| (\sigma=a-k)                            |                 ((h+1)/2) |
| (r=n-k)                                 |                       (k) |
| (j=n-a=r-\sigma)                        |                   (40h-1) |
| Actual scalar list                      | at least (\binom{80}{41}) |

The exact list size supplied by the construction is
[
\binom{80}{41}
==============

104885081691059684352800.
]

The official target numerator is
[
T
=

# \left\lfloor\frac{3^{103}}{2^{128}}\right\rfloor

40893077080.
]
Therefore
[
\boxed{
\binom{80}{41}>T.
}
]

### Entropy margin

Since
[
3^{103}>2^{163},
]
one has
[
\sigma\log_2q

>

\frac{h+1}{2},163.
]
Meanwhile
[
\frac{201}{200}n
================

\frac{201}{200}(81h-1).
]
Direct comparison gives
[
\frac{163(h+1)}2

>

\frac{201}{200}(81h-1).
]
Hence
[
\boxed{
\sigma\log_2q

>

\frac{201}{200}\log_2\binom{n}{a}.
}
]
The packet clears the generated-field entropy boundary with a fixed (0.5%) margin.

In occupancy notation,
[
\lambda=\frac{\binom{n}{a}}{q^\sigma}
<
2^{-n/200}.
]
Thus the packet is not an occupancy fluctuation.

### Multiplicative quotient profile

Here
[
\gcd(n,k)=k.
]
For an active multiplicative quotient (M\mid k), put
[
d=\frac{k}{M},\qquad N=\frac nM=2d.
]
If (M>\sigma), then
[
N<\frac n\sigma<162,
]
so (d<81).

But (k=(3^{103}-1)/2) has no prime divisor below (104). Indeed, if a prime (\ell\mid k), then
[
3^{103}\equiv1\pmod\ell.
]
Since (103) is prime and (\ell\ne2,3), the multiplicative order of (3\bmod\ell) is (103), forcing
[
103\mid\ell-1.
]
Thus no divisor (1<d<81) exists.

The only active multiplicative scale is therefore
[
M=k,\qquad N=2,\qquad \frac{k}{M}=1,
]
whose quotient packet has size
[
\binom{N-1}{k/M}=\binom11=1.
]

So the current multiplicative quotient profile contributes zero bits, while the actual list has more than (2^{76}) elements.

### Full-support and template checks

Every constructed codeword has exact agreement (a); there is no overagreement.

Moreover,
[
\bigcap_{A\in\binom{W^\times}{41}}\phi^{-1}(A)=\varnothing.
]
Thus there is no common agreement coordinate, much less a (k-1)-point tangent core.

The obstruction is instead the additive composition subcode
[
F[\phi]_{\le40}.
]

Repeated-row embedding transfers the same failure to every interleaving arity.

---

## 4. Route-board impact

The following can now be banked.

**Projection/L2:** complete. Under the exact finite projection inequality, the official interleaved threshold is exactly the scalar threshold. There is no independent correlated-interleaving theorem left in the same-field regime.

**Scalar syndrome reduction:** the critical block-secant certificate has a sharper univariate form:
[
\sum_iA_iL_{E_i}=0,\qquad \deg A_i<\sigma.
]
The primitive scalar problem can therefore be attacked as a low-arity split-locator syzygy inverse problem.

**Route cut:** the quotient reserve cannot be defined solely through
[
X\mapsto X^M,\qquad M\mid\gcd(n,k),
]
or through the corresponding multiplicative quotient profile. Additive subspace polynomials produce the same list mechanism.

The repaired structural ledger must recognize a broader invariant:
[
\phi:D\to W
]
where (\phi) has low degree, few image values, and large nearly uniform fibers, and where cancellation of leading quotient coefficients keeps the resulting codewords below degree (k).

A suitable generalized action-rank invariant is
[
d_\phi(E)=|\phi(R_E)|
]
for a split root set (R_E), with the existing (d_M(E)) recovered by (\phi(X)=X^M).

---

## 5. What remains open

The packet uses (D=F^\times) of order (3^{103}-1). It is cyclic but not a power-of-two FFT domain. Therefore it does not settle the strictly smooth/power-of-two multiplicative-domain prize instance.

Three walls remain there:

1. **Functional quotient rigidity.** Decide whether a low-degree map with many large fibers on a power-of-two multiplicative subgroup must factor through (X^M), possibly with a dihedral/inversion variant.

2. **Primitive split-locator syzygies.** After all functional quotients and core descents are removed, bound the number of completions of
   [
   \sum_iA_iL_{E_i}=0,\qquad \deg A_i<\sigma,
   ]
   that arise from one full-support syndrome.

3. **Field transfer.** If (q_{\rm gen}<q_{\rm line}), base-field projection requires
   [
   \binom{L_B+1}{2}<q_{\rm gen}.
   ]
   The official (q_{\rm chal}) budget alone does not establish this.

## Do you see a route to a full solve?

Not with the current multiplicative-only template statement: the theorem first needs the functional-quotient repair above.

For the official smooth cyclic case, the next exact lemma is:

[
\boxed{
\texttt{W-LIST-SMOOTH-CYCLIC-ONE-DEFECT-FUNCTIONAL-QUOTIENT-RIGIDITY}
}
]

Let (H=\mu_n\subset F^\times) have official smooth order, with (\operatorname{char}F\nmid n). Classify every factorization
[
X^n-1
=====

R(X)\prod_{\beta\in B}(\phi(X)-\beta)
]
satisfying
[
\deg\phi=M,\qquad
\deg R<M,
]
where every (\phi(X)-\beta) has exactly (M) simple roots in (H), and (R) contains the one defective fiber.

Prove that either:

[
\phi|_H
\text{ factors through }X\mapsto X^d
]
up to affine changes and the permitted inversion/dihedral symmetry, so the packet is charged by the multiplicative quotient profile; or the resulting family has size below the finite occupancy target.

If this rigidity lemma is false, the next construction to seek is precisely a nonmonomial one-defect factorization on a power-of-two subgroup. If it is true, the remaining scalar wall is the quotient-free critical split-locator syzygy inverse described above.
