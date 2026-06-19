# VERDICT

**Repository status: AUDIT**

No rate-only finite value of (\delta_C^*(2^{-128})) is justified for either challenge.

Three exact pieces can nevertheless be banked:

1. **PROOF:** both thresholds admit an exact integer-reserve formula with rounding error exactly (+1/n).
2. **BANKABLE_LEMMA:** MCA and interleaved lists have exact syndrome-space formulations that give exhaustive finite checkers and automatically cover all denominator degrees.
3. **PROOF:** the official list challenge has a strong finite quotient-core ceiling, uniformly over (q_{\rm line}<2^{256}), assuming the relevant dyadic quotient divides (n).

The remaining obstruction is not lower-bound arithmetic. It is the absence of:

* an explicit finite all-secants MCA inverse bound;
* an actual scalar-list local limit, as opposed to the false raw-support-fiber statement;
* an interleaved common-support completion or diagonalization theorem.

Confidence is high for the exact reductions and quotient-core bounds below. The MCA universal cap remains conditional on the imported list-to-agreement conversion and its normalization audit.

# FINITE_LEDGER

Let
[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,\qquad k=\rho n,\qquad
r=n-k,
]
where (L\subseteq B\subseteq F), with
[
|B|=q_{\rm gen},\qquad |F|=q_{\rm line}.
]
The verifier challenge field (q_{\rm chal}) does not enter either mathematical threshold unless a separate theorem identifies it with (q_{\rm line}) or transfers the relevant numerator.

Set the exact target numerator
[
T:=\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor.
]

Thus MCA is safe precisely when its number of bad slopes is at most (T), and the list challenge is safe precisely when its worst list has at most (T) elements.

If (q_{\rm line}<2^{128}), then (T=0). Both challenges already fail at radius (0):

* every proper linear code has MCA numerator exactly (1) at radius (0);
* every code has worst-case list size exactly (1) at radius (0).

Hence (q_{\rm line}\ge 2^{128}) is a baseline requirement. A larger (q_{\rm chal}) does not repair this.

## PROOF — exact integer threshold formula

For (X\in{\mathrm{MCA},\mathrm{list},m}), let (N_X(a)) denote the relevant worst-case integer numerator when agreement on at least (a) positions is required. Define
[
a_X^*:=\min{a:N_X(a)\le T},
\qquad
\sigma_X^*:=a_X^*-k.
]

Because
[
a(\delta)=\left\lceil(1-\delta)n\right\rceil
]
and (N_X(a)) is nonincreasing in (a),
[
\boxed{
\delta_{X,C}^*(2^{-128})
========================

# 1-\frac{a_X^*-1}{n}

1-\rho-\frac{\sigma_X^*}{n}+\frac1n.
}
]

Thus the finite rounding term is not merely (O(1/n)); it is exactly (+1/n), provided (\sigma_X^*>0). The known failure floors ensure that positivity in the official large-(n) regimes.

## BANKABLE_LEMMA — exact syndrome formulation for MCA

Choose a parity-check matrix (H) for (C), with syndrome space (F^r). Write (h_x) for the column indexed by (x\in L), and for (T\subseteq L) put
[
V_T:=\operatorname{span}_F{h_x:x\in T}.
]

At agreement (a=k+\sigma), let
[
j=n-a=r-\sigma.
]

A word (u) agrees with a codeword outside an error set (T), (|T|\le j), exactly when
[
\operatorname{syn}(u)\in V_T.
]

Consequently, for the affine syndrome line
[
\ell(z)=s_f+zs_g,
]
the parameter (z) is support-wise MCA-bad exactly when there is some (T), (|T|\le j), such that
[
\ell(z)\in V_T
\qquad\text{but}\qquad
\ell\not\subseteq V_T.
]

Therefore the exact MCA numerator is
[
\boxed{
M_C(k+\sigma)=
\max_{\ell\subseteq F^r\ {\rm affine\ line}}
\left|
\left{
z:
\exists,T,\ |T|\le r-\sigma,\
\ell(z)\in V_T,\
\ell\not\subseteq V_T
\right}
\right|.
}
]

This is the precise transverse-secant formulation. It covers every residue denominator degree (t) simultaneously.

For small parameters, an exhaustive checker can:

1. enumerate and deduplicate (V_T) for (|T|\le j);
2. enumerate affine lines in (F^r);
3. test containment and unique transverse intersection by linear algebra;
4. count distinct parameters (z).

There are
[
q_{\rm line}^{,r-1}\frac{q_{\rm line}^r-1}{q_{\rm line}-1}
]
affine lines, so this is exact but infeasible at challenge size.

## BANKABLE_LEMMA — exact syndrome formulation for interleaved lists

For (m) rows, let (\mathcal E_{m,j}) be the set of (m\times n) error arrays having at most (j) nonzero columns. Define
[
\Psi_m(E)
=========

\bigl(H e_1^{\mathsf T},\ldots,H e_m^{\mathsf T}\bigr)
\in(F^r)^m.
]

Then the actual worst-case column-distance list size is exactly
[
\boxed{
L_{C,m}(k+\sigma)
=================

\max_{s\in(F^r)^m}
\left|
\Psi_m^{-1}(s)\cap\mathcal E_{m,r-\sigma}
\right|.
}
]

This is the correct finite local-limit object. It does not suffer from raw-support overcounting.

# MCA_THRESHOLD_STATUS

**Status: CONDITIONAL**

## Exact theorem-backed lower floors

### 1. Tangent floor and the (q/n) floor

At exact reserve (\sigma),
[
\delta_\sigma=1-\frac{k+\sigma}{n},
\qquad
\delta_\sigma n=n-k-\sigma.
]

The tangent construction gives
[
M_C(k+\sigma)\ge n-k-\sigma.
]

Together with the radius-zero numerator (1), safety requires
[
\boxed{
\max{1,n-k-\sigma}\le T.
}
]

Equivalently,
[
\sigma\ge \sigma_{\rm tan}:=\max{0,n-k-T},
]
and, away from rounding,
[
\frac{q_{\rm line}}n
\gtrsim
2^{128}(1-\rho-\eta).
]

This can dominate every algebraic reserve when (q_{\rm line}/n) is too small. It is completely independent of (q_{\rm gen}).

### 2. Exact finite Bessel entropy checker

For the balanced scalar construction, put
[
a=k+\sigma,\qquad j=n-a,\qquad Q=q_{\rm line},
\qquad N_\sigma=\binom n a,
]
and define the integer
[
K_\sigma
:=
\sum_{d=0}^{\sigma-1}
\binom jd\binom ad Q^{\sigma+1-d}.
]

Cycle 47 implies that some line has at least
[
\boxed{
B_{\rm Bes}(\sigma)
===================

\max\left{
0,,
Q-\left\lfloor\frac{K_\sigma}{N_\sigma}\right\rfloor
\right}
}
]
bad slopes.

Thus every (\sigma) satisfying
[
B_{\rm Bes}(\sigma)>T
]
is definitely unsafe.

The all-slope criterion is the especially clean condition
[
\binom n{k+\sigma}>K_\sigma.
]

This is a same-field scalar MCA theorem using (q_{\rm line}). It is not permission to replace (q_{\rm gen}) by (q_{\rm line}) in locator-list or residual-slack estimates.

Asymptotically, its boundary is
[
\eta_{\rm ent,MCA}
\sim
\frac{H_2(\rho)}{\log_2q_{\rm line}}.
]

For the official rates:
[
\begin{array}{c|c|c|c}
\rho&H_2(\rho)&H_2(\rho)/256&g_{\rm universal}\
\hline
1/2&1&0.00390625&2^{-9}=0.001953125\
1/4&0.811278&0.003169&2^{-9}\
1/8&0.543564&0.002123&2^{-9}\
1/16&0.337290&0.001318&2^{-10}=0.0009765625
\end{array}
]

Hence, whenever the finite Bessel theorem is in its asymptotic regime, its entropy floor is stronger than the universal cap throughout the entire (q_{\rm line}<2^{256}) envelope. The universal cap remains important for small finite (n), for extension ledgers where the Bessel criterion has not been checked, and as a field-uniform theorem.

### 3. Universal cap

Subject to the imported list-to-agreement conversion and its exact normalization, the repository gives
[
\delta_{\rm MCA,C}^*(2^{-128})
\le
1-\rho-g_\rho,
]
where
[
g_\rho=
\begin{cases}
2^{-9},&\rho\in{1/2,1/4,1/8},\
2^{-10},&\rho=1/16.
\end{cases}
]

The corresponding integer statement is
[
\sigma_{\rm MCA}^*\ge \lfloor ng_\rho\rfloor+1.
]

The stated divisibility requirements are (2^{10}\mid n) for the first three rates and (2^{11}\mid n) for rate (1/16).

### 4. The (1-n/q) factor does not weaken the cap below (2^{-128})

The imported conversion produces the lower bound
[
\frac1{2k}\left(1-\frac n{q_{\rm line}}\right).
]

Because (n\mid q_{\rm line}-1), write (q_{\rm line}-1=hn).

* If (h\ge2), then (1-n/q_{\rm line}>1/2), giving at least (1/(4k)\ge2^{-42}).
* If (h=1), then (q_{\rm line}=n+1). Since (k\le2^{40}) and (\rho\ge1/16), (n\le2^{44}), so
  [
  \frac1{2k(n+1)}>2^{-86}.
  ]

Thus the cap’s error is always above (2^{-86}), hence far above (2^{-128}). The (q/n) issue is real for the positive theorem and tangent floor, but it does not invalidate this negative cap.

## Exact unconditional bracket

Define
[
\underline\sigma_{\rm MCA}
:=
1+\max\left{
\sigma:
\text{some certified MCA lower bound at }\sigma\text{ exceeds }T
\right}.
]

This includes the Bessel checker, tangent floor, quotient-value-set certificates and, conditionally, the universal cap.

A crude but exact safe-side certificate follows from one bad parameter per support:
[
M_C(k+\sigma)
\le
\sum_{s=k+\sigma}^n\binom ns.
]

Define
[
\overline\sigma_{\rm MCA}
:=
\min\left{
\sigma:
\sum_{s=k+\sigma}^n\binom ns\le T
\right}.
]

Then
[
\boxed{
1-\rho-\frac{\overline\sigma_{\rm MCA}-1}{n}
\le
\delta_{\rm MCA,C}^*(2^{-128})
\le
1-\rho-\frac{\underline\sigma_{\rm MCA}-1}{n}.
}
]

The interval is presently enormous because the all-line upper inverse is missing.

## All-denominator obstruction

The residue-degree decomposition has three genuinely different regimes:

[
\begin{array}{c|l}
t<\sigma&
\text{bad slopes inject into an actual list for dimension }k+t,\
&\text{with residual slack }\sigma-t;[1mm]
t=\sigma&
\text{balanced transverse-secants/residue-cloud problem};[1mm]
t>\sigma&
\text{support-dependent affine-plane incidence in the residue quotient.}
\end{array}
]

A balanced theorem alone does not prove the upper branch.

The (t<\sigma) reduction is useful only where (\sigma-t) clears an actual finite scalar-list theorem. It gives no control for (t=\sigma-1) unless a one-unit residual-slack theorem exists. The (t>\sigma) branch is not a list problem at all.

This is why the syndrome formulation is the correct global wall.

# LIST_THRESHOLD_STATUS

**Status: CONDITIONAL, with a strong unconditional quotient-core ceiling**

## Exact entropy lower bound

At reserve (\sigma), generated-field coefficient pigeonholing gives a scalar list of size at least
[
\boxed{
E_{\rm ent}(\sigma)
===================

\left\lceil
\frac{\binom n{k+\sigma}}{q_{\rm gen}^{,\sigma}}
\right\rceil.
}
]

Repeated-row diagonalization transfers this unchanged to every constant interleaving arity (m). Therefore
[
E_{\rm ent}(\sigma)>T
\quad\Longrightarrow\quad
\text{the official interleaved list challenge fails at }\sigma.
]

The finite entropy inequality that must be cleared is
[
\log_2\binom n{k+\sigma}
------------------------

\sigma\log_2q_{\rm gen}
\le
\log_2T.
]

This is a (q_{\rm gen}) bill. It cannot be paid using (q_{\rm line}) merely because the final list is divided by (q_{\rm line}).

## PROOF — finite quotient-core threshold ceiling

Let (M\mid\gcd(n,k)), put (N=n/M), and suppose (1\le\sigma<M). The quotient-core theorem gives an actual scalar list of size
[
Q_M=\binom{N-1}{k/M}.
]

Thus every safe reserve must satisfy
[
\sigma\ge M
\qquad
\text{for every }M\text{ with }Q_M>T.
]

Equivalently, define
[
\sigma_{\rm quot,list}
:=
\max_{\substack{
M\mid\gcd(n,k)\
k/M\le n/M-1\
\binom{n/M-1}{k/M}>T
}}
M.
]
Then
[
\sigma_{\rm list}^*\ge\sigma_{\rm quot,list}.
]

For the worst allowed line field, (q_{\rm line}<2^{256}), one has (T<2^{128}). At the four official rates, the following quotient packets already exceed the target:

[
\begin{array}{c|c|c|c|c}
\rho&N&\binom{N-1}{\rho N}&\log_2(\text{packet})&
\text{threshold ceiling}\
\hline
1/2&256&\binom{255}{128}&250.673&
1-\rho-2^{-8}+1/n\
1/4&256&\binom{255}{64}&203.152&
1-\rho-2^{-8}+1/n\
1/8&256&\binom{255}{32}&135.227&
1-\rho-2^{-8}+1/n\
1/16&512&\binom{511}{32}&168.816&
1-\rho-2^{-9}+1/n
\end{array}
]

The hypotheses are that (N\mid n) and (M=n/N\ge2), equivalently (2N\mid n) in the dyadic setting.

For example, at the first three rates, take (M=n/256) and (\sigma=M-1). The list challenge fails at
[
\delta
======

# 1-\rho-\frac{M-1}{n}

1-\rho-\frac1{256}+\frac1n.
]

Repeated rows give the identical lower bound for every interleaving arity.

The preceding dyadic quotient orders are minimal for a field-uniform (2^{128}) packet: at (N=128), the corresponding logarithms are respectively (123.17), (99.81), and (66.15); at rate (1/16), (N=256) gives only (82.97) bits.

## COUNTERPACKET — raw arbitrary support fibers cannot be used

The raw conjecture
[
|\operatorname{Fib}_U(k+\sigma)|\le n^B
\quad\text{for every }U
]
is false.

If (U) is itself a degree-(<k) codeword, then every ((k+\sigma))-subset is feasible:
[
|\operatorname{Fib}_U(k+\sigma)|
================================

\binom n{k+\sigma},
]
while the actual list has size exactly (1).

Therefore a finite threshold checker must use one of:

* actual scalar lists;
* full agreement supports;
* maximal supports;
* sparse syndrome fibers.

It may not use raw feasible (a)-subsets as a list-size surrogate without an explicit overcount factor.

## BANKABLE_LEMMA — exact interleaved support formula

For a received row (U_i), let
[
\mathcal A_i
============

\left{
A_{U_i}(c):
c\in C,\ |A_{U_i}(c)|\ge a
\right},
\qquad
A_{U_i}(c)={x:c(x)=U_i(x)}.
]

For (a\ge k),
[
\boxed{
|\Lambda(\operatorname{Int}(C,m),1-a/n,U)|
==========================================

#\left{
(A_1,\ldots,A_m):
A_i\in\mathcal A_i,
\left|\bigcap_iA_i\right|\ge a
\right}.
}
]

In particular,
[
|\Lambda(\operatorname{Int}(C,m),1-a/n,(V,\ldots,V))|
=====================================================

|\Lambda(C,1-a/n,V)|.
]

Hence every scalar lower bound transfers without an (m)-loss.

The reverse direction does not follow: a scalar upper bound (L_1) gives only the conservative estimate
[
L_m\le L_1^m
]
unless common-intersection codegrees are controlled.

## ROUTE_CUT — the MCA universal cap is not automatically a list cap

The slack-two packet used by the MCA universal cap naturally produces a list in an augmented dimension.

If (h=n/N), (|A|=\rho N+2), and (S_A) is the pullback of (A), then
[
L_{S_A}(X)
==========

X^{k+2h}
-e_1(A)X^{k+h}
+e_2(A)X^k+\cdots.
]

After fixing (e_1(A)), subtracting (L_{S_A}) from the received polynomial generally leaves a degree-(k) term. Thus the resulting codeword lies in dimension (k+1), not necessarily in the official dimension-(k) code.

This packet is tailored to the augmented-code list-to-agreement conversion. It cannot be booked directly as an official list-challenge lower bound.

The ordinary quotient-core theorem above is the correct direct list floor.

## Exact unconditional bracket

Let
[
\underline\sigma_{\rm list}
===========================

\max\left{
1+\max{\sigma:E_{\rm ent}(\sigma)>T},
,
\sigma_{\rm quot,list}
\right}.
]

The interleaved code has the same column minimum distance
[
d=n-k+1.
]
Unique decoding therefore gives list size at most (1) whenever
[
2(n-k-\sigma)<n-k+1,
]
equivalently
[
\sigma\ge\overline\sigma_{\rm list}:=
\left\lceil\frac{n-k}{2}\right\rceil.
]

Provided (q_{\rm line}\ge2^{128}),
[
\boxed{
1-\rho-\frac{\overline\sigma_{\rm list}-1}{n}
\le
\delta_{\rm list,C,m}^*(2^{-128})
\le
1-\rho-\frac{\underline\sigma_{\rm list}-1}{n}.
}
]

Closing this interval requires both the actual scalar local limit and the interleaved completion theorem.

# DOMINANT_FLOORS

## MCA

The dominance order is parameter-dependent:

1. **Baseline field floor:** if (q_{\rm line}<2^{128}), no radius meets the target.
2. **Tangent/(q/n) floor:** dominates whenever
   [
   T<n(1-\rho-\eta).
   ]
3. **Balanced entropy floor:** in same-field scalar MCA and sufficiently large (n), this is asymptotically (H_2(\rho)/\log_2q_{\rm line}). It exceeds the universal-cap reserve at every official rate for every (q_{\rm line}<2^{256}).
4. **Quotient profile:** may dominate code-specifically if a large quotient packet remains active.
5. **Universal cap:** gives a robust finite extension-safe ceiling, but is not the asymptotically dominant lower floor after Cycle 47.
6. **All-denominator inverse:** dominates the safe-side status. Until it is proved, none of the preceding floors identifies the threshold.

A statement such as
[
M_C(k+\sigma)\le n^{1+o(1)}
]
is insufficient for (2^{-128}). One needs the explicit finite comparison
[
M_C(k+\sigma)\le T.
]

For example, if (n=2^{44}):

* at (q_{\rm line}=2^{256}), (T=2^{128});
* at (q_{\rm line}=2^{186}), (T=2^{58}).

Thus an upper numerator (n(\log_2n)^C) could tolerate roughly (C\le15.4) in the first case but only (C\le2.6) in the second. An unspecified (o(1)) exponent cannot be used in a finite certificate.

## List challenge

The lower floor is
[
\max{\text{generated-field entropy},\text{quotient profile}}.
]

The asymptotic entropy reserve is approximately (H_2(\rho)/b_{\rm gen}), where (b_{\rm gen}=\log_2q_{\rm gen}). Comparing it with the field-uniform quotient floors above gives the crossover bitlengths:

[
\begin{array}{c|c}
\rho&\text{entropy dominates quotient when }b_{\rm gen}\lesssim\
\hline
1/2&256.0\
1/4&207.7\
1/8&139.2\
1/16&172.7
\end{array}
]

Thus for a 31-bit generated FFT field, entropy is decisively dominant:
[
\begin{array}{c|c}
\rho&H_2(\rho)/31\
\hline
1/2&0.03226\
1/4&0.02617\
1/8&0.01753\
1/16&0.01088
\end{array}
]

For generated fields near 256 bits, the quotient-core floor dominates at rates (1/4,1/8,1/16), and is essentially tied with entropy at rate (1/2).

On the positive side, the dominant missing constraint is the **actual scalar list local limit**. Even if a theorem gives
[
L_1\le n^B,
]
the finite field budget requires
[
B\log_2n\le\log_2q_{\rm line}-128.
]

At (n=2^{44}):

* (q_{\rm line}=2^{256}) permits only (B\le2.91);
* (q_{\rm line}=2^{186}) permits only (B\le1.32).

Using the product bound for (m) rows replaces (B) by (mB). This is why projection/diagonalization is a finite-threshold issue, not merely an asymptotic refinement.

# CONDITIONAL_FORMULA

No evaluated rate-only formula is justified.

For either challenge (X), suppose one has:

1. a finite lower checker proving every reserve below (\widehat\sigma_X) unsafe;
2. a finite upper theorem proving the numerator at reserve (\widehat\sigma_X) is at most (T);
3. all quotient, tangent, field-transfer, interleaving and integer conditions checked at the actual ((n,k,q_{\rm gen},q_{\rm line})).

Then monotonicity gives the exact formula
[
\boxed{
\delta_{X,C}^*(2^{-128})
========================

1-\rho-\frac{\widehat\sigma_X}{n}+\frac1n.
}
]

For MCA, the finite upper theorem must bound
[
I^\pitchfork_{r-\widehat\sigma_{\rm MCA}}(\ell)
\le T
]
for every affine syndrome line (\ell).

For the (m)-interleaved list challenge, it must bound
[
\max_s
\left|
\Psi_m^{-1}(s)\cap\mathcal E_{m,r-\widehat\sigma_{\rm list}}
\right|
\le T.
]

At present neither (\widehat\sigma_{\rm MCA}) nor (\widehat\sigma_{\rm list}) can be evaluated from the repository’s proved upper results.

# EXACT_NEW_WALL

## EXACT_NEW_WALL — MCA

`W-MCA-FINITE-SYNDROME-TRANSVERSE-SECANT-TARGET-INVERSE`

For every official finite code and every reserve (\sigma) clearing the exact tangent, entropy and quotient lower checkers, prove that every affine line (\ell\subseteq F^{n-k}) satisfies
[
\left|
\left{
z:
\exists T,\ |T|\le n-k-\sigma,
\ell(z)\in V_T,
\ell\not\subseteq V_T
\right}
\right|
\le
\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor,
]
unless the line has an explicit certificate of:

* quotient descent;
* tangent/common-core descent;
* a residual-list obstruction already counted at dimension (k+t);
* another finite template whose exact slope contribution is included in the numerator.

The theorem must include lower secants, (t<\sigma), (t=\sigma), and (t>\sigma). The staged
`W-MCA-T2-HIGH-J-DETERMINANTAL-QUADRIC-SPLIT-COUNT`
is a useful subwall but cannot determine the prize threshold by itself.

## EXACT_NEW_WALL — list

`W-LIST-FINITE-COLUMN-SPARSE-SYNDROME-FIBER-DIAGONALIZATION`

For every official finite code and constant (m), prove that every column-sparse syndrome fiber satisfies
[
\left|
\Psi_m^{-1}(s)\cap\mathcal E_{m,n-k-\sigma}
\right|
\le
\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor
]
once generated-field entropy and the exact quotient profile clear, or else classify every larger fiber as one of:

* a repeated-row or lower-arity diagonalization;
* an aligned quotient-core packet;
* a bounded near-exact-support completion neighborhood;
* a genuinely non-diagonal rank-compression construction.

The scalar (m=1) theorem must be stated for actual lists, full supports, or sparse syndrome fibers—not raw feasible support sets.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
