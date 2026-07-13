# Signed local-minority fixed-composition fibers

## Status and scope

**PROVED / EXACT ARITHMETIC CERTIFICATE / EXPERIMENTAL.**  This note records a
profilewise theorem for the power-sum map on a fixed equal-block occupancy
profile.  It gives a product-Johnson distance, product-shadow and
block-centered Plotkin fiber caps, a hereditary realized-image consequence,
and two zero-target exclusions.  The first source consumer is an exact labeled
occupancy refinement of the corrected `#714` partial-occupancy cells.

The result is deliberately local.  It neither exhausts all profiles nor edits
or promotes any stable-paper theorem.  In the deployed nine-partial profile it
proves a fiber upper bound of `153`.  The number `441080640` below is only the
sum of those profilewise upper bounds over a displayed permutation orbit; it
is not asserted to be attained.

## 1. Exact profile and signed minority normal form

Let \(F\) be a field of characteristic \(\ell>w\), let
\(D\subset F^\times\), and fix a partition

\[
D=C_1\sqcup\cdots\sqcup C_N,\qquad |C_i|=q.
\]

Write \(n=Nq\), \(\delta=w+1\), and

\[
\Phi_w(S)=(P_1(S),\ldots,P_w(S)),\qquad
P_j(S)=\sum_{a\in S}a^j.
\]

For an exact labeled occupancy vector
\(r=(r_1,\ldots,r_N)\in\{0,\ldots,q\}^N\), put

\[
\Omega_r=\{S\subseteq D:|S\cap C_i|=r_i\text{ for every }i\},
\qquad I=\{i:0<r_i<q\}.
\]

For \(i\in I\), define

\[
t_i=\min(r_i,q-r_i),\qquad
\epsilon_i=
\begin{cases}
+1,&2r_i\le q,\\
-1,&2r_i>q,
\end{cases}
\]

and, for \(S\in\Omega_r\),

\[
U_i(S)=
\begin{cases}
S\cap C_i,&\epsilon_i=+1,\\
C_i\setminus S,&\epsilon_i=-1.
\end{cases}
\qquad |U_i(S)|=t_i.
\]

The profile constants used below are

\[
\begin{aligned}
c_r&=\sum_{i:r_i>q/2}\Phi_w(C_i),\\
T&=\sum_{i\in I}t_i,
&T_+&=\sum_{\epsilon_i=+1}t_i,
&T_-&=\sum_{\epsilon_i=-1}t_i,\\
B_r&=\sum_{i\in I}t_i(q-t_i)
=\sum_{i=1}^N r_i(q-r_i),\\
M_r&=|\Omega_r|=\prod_{i\in I}\binom q{t_i}.
\end{aligned}
\]

Empty sums and products have their usual values.  Dense local complementation
gives the exact affine identity

\[
\boxed{\quad
\Phi_w(S)=c_r+\sum_{i\in I}\epsilon_i\Phi_w(U_i(S)).
\quad} \tag{SLM1}
\]

Equivalently, for every unitary additive character \(\chi\) of the additive
group \(F^w\),

\[
\chi(\Phi_w(S))
=\chi(c_r)\prod_{i\in I}\chi(\Phi_w(U_i(S)))^{\epsilon_i}. \tag{SLM2}
\]

The fixed offset matters when complete-block moments do not vanish.  No
assumption \(q>w\) is needed for (SLM1).

## 2. Fiber theorem

For integers \(0\le u_i\le t_i\), set

\[
C_{\rm sh}(u)=
\left\lfloor
\frac{\prod_{i\in I}\binom q{u_i}}
     {\prod_{i\in I}\binom {t_i}{u_i}}
\right\rfloor,
\qquad
C_{\rm sh}=
\min_{\sum_i(t_i-u_i)\le w}C_{\rm sh}(u). \tag{SLM3}
\]

The admissible set is nonempty because \(u_i=t_i\) is always allowed.  Define
the block-Plotkin cap by

\[
C_{\rm Pl}=
\begin{cases}
\displaystyle
\left\lfloor\frac{\delta q}{\delta q-B_r}\right\rfloor,
&B_r<\delta q,\\[1.1ex]
2|I|(q-1),&B_r=\delta q,\\
+\infty,&B_r>\delta q,
\end{cases}
\qquad
C_r=\min(C_{\rm sh},C_{\rm Pl}). \tag{SLM4}
\]

The strict formula in (SLM4) is exactly
\(\lfloor\delta q/(\delta q-B_r)\rfloor\).  Its numerator and denominator
must not be interchanged.

**Theorem 2.1 (signed local-minority fixed-composition cap).**  Every target
fiber on the exact profile satisfies

\[
\max_{v\in F^w}|\Omega_r\cap\Phi_w^{-1}(v)|\le C_r. \tag{SLM5}
\]

Consequently, if \(L_r=|\Phi_w(\Omega_r)|\), then

\[
L_r\ge\left\lceil\frac{M_r}{C_r}\right\rceil. \tag{SLM6}
\]

If \(T\le w\), then \(C_{\rm sh}=1\), so \(\Phi_w\) is injective on
\(\Omega_r\).

### Proof

Take two supports \(S,S'\in\Omega_r\) in one fiber and abbreviate their
minority tuples by \(U=(U_i)\) and \(V=(V_i)\).  Cancelling \(c_r\) in (SLM1)
gives

\[
\sum_i\epsilon_i\Phi_w(U_i)=\sum_i\epsilon_i\Phi_w(V_i).
\]

Form ordinary \(T\)-subsets of the disjoint block union,

\[
\begin{aligned}
A(U,V)&=\bigcup_{\epsilon_i=+1}U_i
       \ \cup\!\!\bigcup_{\epsilon_i=-1}V_i,\\
B(U,V)&=\bigcup_{\epsilon_i=+1}V_i
       \ \cup\!\!\bigcup_{\epsilon_i=-1}U_i.
\end{aligned}
\]

They have equal power sums through degree \(w\).  Moreover,

\[
d_J(A,B)=\sum_{i\in I}|U_i\setminus V_i|. \tag{1}
\]

Remove the common core of \(A\) and \(B\), leaving disjoint \(d\)-sets \(X,Y\)
with equal first \(w\) power sums.  If \(d\le w\), Newton identities are
invertible because \(\operatorname{char}F>w\).  The monic root polynomials of
\(X\) and \(Y\) are equal, hence \(X=Y\).  Disjointness then forces \(d=0\).
Thus distinct tuples in one fiber obey the product-Johnson distance

\[
\sum_i|U_i\setminus V_i|\ge\delta=w+1. \tag{2}
\]

For an admissible \(u\), a tuple \(W_i\subseteq U_i\), \(|W_i|=u_i\), cannot
belong to two same-fiber codewords.  Otherwise both words contain \(W_i\) in
each block and their distance is at most
\(\sum_i(t_i-u_i)\le w\), contradicting (2).  Each codeword contains
\(\prod_i\binom{t_i}{u_i}\) such subshadow tuples, while the ambient product
contains \(\prod_i\binom q{u_i}\).  Double counting proves (SLM3).  If
\(T\le w\), the choice \(u_i=0\) gives cap one.

For Plotkin, center each minority tuple block by block:

\[
x_U=\bigoplus_{i\in I}
\left(\mathbf 1_{U_i}-\frac{t_i}{q}\mathbf 1_{C_i}\right).
\]

Then

\[
\|x_U\|^2=\frac{B_r}{q},\qquad
\langle x_U,x_V\rangle
=\frac{B_r}{q}-\sum_i|U_i\setminus V_i|
\le\frac{B_r}{q}-\delta. \tag{3}
\]

If a fiber has \(A\) members and \(B_r<\delta q\), summing (3) gives

\[
0\le\left\|\sum_Ux_U\right\|^2
\le A\frac{B_r}{q}
 +A(A-1)\left(\frac{B_r}{q}-\delta\right).
\]

After division by \(A>0\), this is

\[
A(\delta q-B_r)\le\delta q,
\]

which proves the strict branch

\[
A\le\left\lfloor\frac{\delta q}{\delta q-B_r}\right\rfloor.
\]

At equality \(B_r=\delta q\), the normalized \(x_U\) have pairwise
nonpositive inner products and lie in dimension \(|I|(q-1)\).  The standard
obtuse-code bound gives at most twice that dimension.  For completeness, pick
one unit vector \(y\); all other vectors have nonpositive \(y\)-coordinate,
and their nonzero projections to \(y^\perp\) remain pairwise nonpositive.
At most one projection is zero, namely that of \(-y\), so induction on the
dimension gives \(2|I|(q-1)\).  This proves (SLM4)-(SLM5), and counting the
\(M_r\) supports by fibers gives (SLM6).  QED.

## 3. Hereditary realized-image consequence

Let \(\Omega_r^0\subseteq\Omega_r\) be any nonempty subset, including an actual
support set left after arbitrary first-match deletion.  Define

\[
f_v=|\Omega_r^0\cap\Phi_w^{-1}(v)|,
\qquad L_0=|\Phi_w(\Omega_r^0)|.
\]

Deletion cannot enlarge a target fiber, while
\(|\Omega_r^0|/L_0\ge1\).  Therefore

\[
\boxed{\quad
\max_v f_v\le C_r
\le C_r\frac{|\Omega_r^0|}{L_0}.
\quad} \tag{SLM7}
\]

This is a direct residual-own-image Q certificate whenever
\(\log C_r=o(n)\); no ambient \( |F|^w\) denominator is substituted.  It also
gives, for every integer \(s\ge2\),

\[
\sum_v f_v^s\le C_r^{s-1}|\Omega_r^0|. \tag{SLM8}
\]

In particular the order-two SP bound is inherited by every first-match
residual subset of a paid exact profile.

## 4. Zero-target exclusions

### 4.1 Split-sign exclusion

**Corollary 4.1.**  Assume \(c_r=0\), \(I\ne\varnothing\), and

\[
T_+\le w,\qquad T_-\le w. \tag{4}
\]

Then

\[
\Omega_r\cap\Phi_w^{-1}(0)=\varnothing. \tag{SLM9}
\]

Indeed, a zero support would give equal power sums for

\[
A_+=\bigcup_{\epsilon_i=+1}U_i(S),\qquad
A_-=\bigcup_{\epsilon_i=-1}U_i(S).
\]

Both sets have size at most \(w\).  Newton identities make their elementary
symmetric coefficients through degree \(w\) equal.  Since every element of
\(D\) is nonzero, the top coefficient of a nonempty root polynomial is
nonzero, so the degrees and then the root sets agree.  The two sets occupy
disjoint sign-block unions, hence both would be empty, contrary to
\(I\ne\varnothing\).

The conditions \(c_r=0\), \(D\subset F^\times\), and both inequalities in
(4) are genuine hypotheses.  The verifier contains counterfixtures for
dropping the offset or one side-mass condition.

### 4.2 Cyclic zero saturation

Now let \(D=\mu_n\subset F^\times\), let \(H\le\mu_n\) have order \(q\), and
let the blocks be the labeled \(H\)-cosets.  Put

\[
g_r=\gcd(q,r_1,\ldots,r_N).
\]

**Corollary 4.2.**  If \(S\in\Omega_r\) has \(\Phi_w(S)=0\), let
\(K=\{h\in H:hS=S\}\) and \(k=|K|\).  Then

\[
k\mid g_r,\qquad
B_r\ge(q-k)\delta,\qquad
\frac qk\le C_r. \tag{SLM10}
\]

Consequently,

\[
\boxed{\quad
B_r<(q-g_r)\delta
\quad\text{or}\quad
C_r<\frac q{g_r}
\quad\Longrightarrow\quad
\Omega_r\cap\Phi_w^{-1}(0)=\varnothing.
\quad} \tag{SLM11}
\]

To prove this, multiplication by \(H\) preserves each labeled block and the
zero target.  The stabilizer acts freely inside every coset, so \(k\mid r_i\)
for all \(i\).  Also

\[
\sum_{h\in H}d_J(S,hS)
=q|S|-\sum_i r_i^2
=\sum_i r_i(q-r_i)=B_r. \tag{5}
\]

There are \(q/k-1\) nontrivial orbit supports, each represented by \(k\)
multipliers and each at distance at least \(\delta\), proving the middle
inequality in (SLM10).  The orbit has \(q/k\) members in one fiber, proving
the last inequality.  Since \(k\le g_r\), either strict inequality in
(SLM11) is impossible for a zero support.

This is a zero-target support-stabilizer statement.  It is not a ray owner.

## 5. Exact-profile compiler

For one fixed equal-block partition there are at most

\[
(q+1)^N=(q+1)^{n/q} \tag{6}
\]

labeled occupancy vectors.  If \(q=q_n\to\infty\), then

\[
\log (q+1)^{n/q}=\frac nq\log(q+1)=o(n). \tag{7}
\]

If \({\cal R}\) is any family of exact profiles and
\(\Omega^0\subseteq\bigcup_{r\in{\cal R}}\Omega_r\), then targetwise summation
gives

\[
\max_v|\Omega^0\cap\Phi_w^{-1}(v)|
\le\sum_{r\in{\cal R}}C_r. \tag{8}
\]

Thus the exact refinement pays every profile with \(B_r\le\delta q\) at
polynomial loss in the source regime: in the strict case
\(C_{\rm Pl}\le\delta q\), and at equality
\(C_{\rm Pl}\le2n\).  The product-shadow branch additionally pays any profile
with \(\log C_{\rm sh}=o(n)\).  An `exp(o(n))` family of such exact profiles
adds back with `exp(o(n))` total loss.

For the corrected `#714` decomposition, the compiler refines a coarse
partial-occupancy cell by recording each labeled block's exact occupancy.
The theorem is then applied before or after support-level first-match deletion
using (SLM7).  This consumes the corrected support partition and its add-back;
it does not repeat `#714`'s image theorem.

## 6. Deployed exact certificates

Use

\[
\begin{aligned}
p&=2130706433,& n&=2097152,& m&=981104,\\
w&=67471,&\delta&=67472,&q&=2^{17}=131072,&N&=16.
\end{aligned}
\]

Here \(p-1=1016n\), so the order-\(n\) multiplicative domain and its
order-\(q\) subgroup exist.  Also \(q>w\); hence every complete \(H\)-coset
has zero moments through degree \(w\), and \(c_r=0\) for these profiles.

### 6.1 Nine-partial strict profile

Take the labeled occupancy multiset

\[
(129214,\ 129215^{\times6},\ 38300^{\times2},\ 0^{\times7}).
\]

It has support size \(m\), nine partial blocks, seven dense blocks, and two
sparse blocks.  Its signed minority multiset is

\[
(1858,\ 1857^{\times6};\ 38300^{\times2}),
\]

where the semicolon separates negative and positive sign blocks.  Exact
arithmetic gives

\[
\begin{aligned}
T_-&=13000,&T_+&=76600,&T&=89600>w,\\
B_r&=8786128342,&
\delta q&=8843689984,&
\delta q-B_r&=57561642.
\end{aligned}
\]

Therefore the repaired strict cap is

\[
C_r\le C_{\rm Pl}
=\left\lfloor\frac{8843689984}{57561642}\right\rfloor
=153. \tag{9}
\]

Every raw or first-match residual fiber in this one exact nine-partial profile
is therefore **at most 153**, and

\[
|\Phi_w(\Omega_r)|\ge
\left\lceil
\frac{
\binom q{1858}\binom q{1857}^{6}\binom q{38300}^{2}}
{153}
\right\rceil. \tag{10}
\]

The local rotation gcd is \(g_r=1\).  Both cyclic exclusions are visible:

\[
(q-1)\delta-B_r=57494170>0,
\qquad 153<q/g_r=131072. \tag{11}
\]

Hence this exact profile has empty zero fiber.  Notice that split-sign
exclusion alone does not apply because \(T_+>w\).

This is genuinely local.  On the nine-block minority union,

\[
T(9q-T)=97668300800>\delta(9q)=79593209856,
\]

and globally

\[
m(n-m)=1094959156992>\delta n=141499039744.
\]

Thus the corresponding ambient Plotkin tests fail.  The ambient shadow ratio
is also exponentially large: with \(u=m-w=913633\),

\[
\left(\frac{n}{m}\right)^u
=\left(\frac{131072}{61319}\right)^{913633}>2^{1000000}. \tag{12}
\]

Permuting the occupancy multiset among the 16 labeled cosets gives exactly

\[
\frac{16!}{1!6!2!7!}=2882880
\]

profiles.  Summing the profilewise cap gives the union bound

\[
\max_v|\Omega_{\rm orbit}\cap\Phi_w^{-1}(v)|
\le2882880\cdot153=441080640. \tag{13}
\]

Equation (13) is an upper bound only.  No equality or attained maximum is
claimed.  The union's zero fiber is empty because it is empty profile by
profile.

### 6.2 Neighboring injective profile

Take

\[
(130800^{\times3},\ 130801^{\times4},\ 32750^{\times2},\ 0^{\times7}).
\]

Its negative minorities are \(272^{\times3},271^{\times4}\), and its positive
minorities are \(32750^{\times2}\).  Hence

\[
T_-=1900,\qquad T_+=65500,\qquad T=67400\le w.
\]

The exact-profile map is injective.  Both sign-side masses are at most \(w\),
so its zero fiber is empty.  Its realized image is exactly

\[
\binom q{272}^{3}\binom q{271}^{4}\binom q{32750}^{2}. \tag{14}
\]

### 6.3 Source-supported coarse full-coset multiplicity

Fix three partial cosets with occupancies

\[
(129172,32750,32750)
\]

and choose six full cosets among the remaining thirteen.  The partial
minorities have \(T_-=1900\), \(T_+=65500\), and \(T=67400\le w\), so the
partial map is injective and zero-empty.  Complete cosets have zero prefix
because \(q>w\).  Therefore each partial image point has exactly

\[
\binom{13}{6}=1716 \tag{15}
\]

raw supports, every residual fiber has size at most `1716`, and the coarse
zero fiber is empty.  Its exact image size is

\[
\binom q{1900}\binom q{32750}^{2}.
\]

This coarse multiplicity is recorded because it is explicitly supported by
the source profile.  It is not extrapolated to arbitrary coarse cells.

## 7. Exact remaining mixed-sign wall

At the same \(q\), arrange the 16 \(H\)-cosets in eight pairs.  In each pair
put occupancy

\[
q-60000=71072
\]

on one coset and occupancy \(51566\) on the other.  Then

\[
8\cdot71072+8\cdot51566=981104,
\]

while

\[
T_-=480000>w,\qquad T_+=412528>w,
\]

and

\[
B_r=66913011168>\delta q=8843689984. \tag{16}
\]

Thus neither block Plotkin nor split-sign zero exclusion applies.  Every
admissible product shadow must retain at least

\[
T-w=892528-67471=825057
\]

minority points.  Since every \(t_i\le60000\), its pre-floor ratio is at least

\[
\left(\frac{q}{60000}\right)^{825057}
=\left(\frac{4096}{1875}\right)^{825057}>2^{930000}. \tag{17}
\]

So the product-shadow cap is exponentially nonpaying as well.

The pairing keeps the coarser dyadic occupancies uniform:

\[
(q',N',r')\in\{
(262144,8,122638),
(524288,4,245276),
(1048576,2,490552),
(2097152,1,981104)
\}.
\]

At every one of these scales,

\[
\frac{N'r'(q'-r')}{q'}
=\frac{m(n-m)}n
=\frac{4277184207}{8192}>67472, \tag{18}
\]

so block Plotkin still fails.  The exact next object is therefore any
nonempty primitive first-match residual inside this balanced mixed-sign
profile.  It requires either a signed phase/Fourier/Sidon/Hankel max-fiber
estimate at its actual realized-image scale, or a fully rooted owner carrying
the source's received data, explaining data, first-match ownership, and slope
projection.

## 8. Nonclaims

- No all-profile Q theorem is proved.  Only exact profiles satisfying the
  displayed Plotkin or shadow conditions are paid.
- No global \(\nu(0)\le n^3\) theorem or complete finite numerator is proved.
- No RC theorem, distinct-ray bound, ray compiler, CAT ledger, or outer UNIF
  statement is proved.  Q/SP is not promoted to rays.
- No rooted owner is supplied for every profile left by the compiler.
- No finite threshold, adjacent-row threshold, Grand MCA prize solve, or Grand
  List improvement is claimed.
- The permutation-orbit number `441080640` is not an attained maximum claim.
- No stable paper TeX is changed or promoted by this note.

## 9. Verification

The stdlib-only verifier is

```text
experimental/scripts/verify_signed_local_minority_fixed_composition.py
```

It independently checks the deployed arithmetic, exact cap `153`, both
zero-empty inequalities, the neighboring injective row, the coarse
multiplicity `1716`, the nested remaining wall, exhaustive small-field
profiles, and explicit sign/shadow/Plotkin/zero-hypothesis tamper fixtures.
