# VERDICT

**Repository status: AUDIT**

**Confidence: high.**

The Cycle 45–57 packet is not a proof of the Proximity Prize. It contains a theorem-grade lower/failure result for same-field support-wise scalar MCA, several exact structural reductions, and useful route cuts. It does not contain the all-line safe-side inverse theorem, an extension-line theorem, an actual-list local limit, or finite constants sufficient to determine any official (\delta_C^*(2^{-128})).

There is also a provenance problem: the uploaded archive ends at Cycle 47 plus earlier experimental material. No Cycle 49–57 proof files, theorem statements, calculations, or verifiers are present. Consequently, Cycle 49–57 claims can be audited logically from the supplied summary, but cannot be certified as repository theorems.

The strongest defensible classification is:

* Cycle 47 lower branch: **PROVED under the internal support-wise definition and explicit same-field assumptions**.
* Cycle 49 syndrome reformulation: **BANKABLE_LEMMA**, once written as below.
* Cycles 50–53: **ROUTE_CUTS**, not upper theorems.
* Cycles 54–55: **PROOF_CANDIDATE / EXPERIMENTAL**.
* Cycle 56: **ROUTE_CUT**.
* Cycle 57: **EXACT_NEW_WALL / EXPERIMENTAL**.
* Grand MCA theorem: **CONJECTURAL**.
* Grand interleaved-list theorem: **CONJECTURAL**.

# WHAT_IS_PROVED

## PROOF — finite domain-uniform Bessel–Paley lower theorem

Let

[
F=\mathbb F_Q,\qquad D\subseteq F^\times,\qquad |D|=n,
]

and let (C=\operatorname{RS}[F,D,k]). Fix (1\le t\le n-k), and put

[
a=k+t,\qquad j=n-a,\qquad N=\binom{n}{a}.
]

Let (E\in F[X]) have degree (t) and no root on (D). For an (a)-set (S\subseteq D), let (I_S(w)) be the degree-(<a) interpolant of (w|_S), and define

[
R_S(w)=[I_S(w)]_E\in A:=F[X]/(E).
]

For supports (S,S') at exchange distance

[
d=|S\setminus S'|=|S'\setminus S|,
]

one has the exact image formula

[
\operatorname{Im}(R_S,R_{S'})
=============================

\left{(u,v)\in A^2:
u-v\in [L_{S\cap S'}F[X]_{<d}]_E
\right}.
]

Because ([L_{S\cap S'}]_E) is a unit,

[
\operatorname{rank}*F(R_S,R*{S'})
=================================

t+\min(t,d).
]

Now fix a residue-line direction (B_{\rm num}=1), and set

[
\nu_w(z)
========

#{S\in\tbinom Da:R_S(w)=z[1]_E},
\qquad
\lambda=\frac{N}{Q^t}.
]

Writing

[
K_d=\binom ad\binom jd,
]

the exact second moment is

[
\mathbb E_w\nu_w(z)^2
=====================

\lambda^2+\lambda V,
]

where

[
V
=

\sum_{0\le d<t}
K_d\bigl(Q^{-d}-Q^{-t}\bigr).
]

In particular, with

[
J=\sum_{0\le d<t}K_dQ^{-d},
]

one has (0<V\le J) and

[
J
\le
\sum_{d\ge0}\frac{(aj/Q)^d}{(d!)^2}
\le
\exp!\left(2\sqrt{aj/Q}\right)
\le
\exp(n/\sqrt Q).
]

Two separate probabilistic arguments now give two finite lower bounds.

First, Paley–Zygmund gives

[
\Pr_w(\nu_w(z)>0)
\ge
\frac{\lambda^2}{\lambda^2+\lambda V}
=====================================

\frac{\lambda}{\lambda+V}.
]

Summing over (z\in F), some anchor (w) therefore occupies at least

[
Q\frac{\lambda}{\lambda+V}
]

distinct slopes.

Second,

[
\mathbb E_w
\sum_{z\in F}(\nu_w(z)-\lambda)^2
=================================

Q\lambda V.
]

Hence some anchor has at most (QV/\lambda) missed slopes, and therefore occupies at least

[
Q\left(1-\frac V\lambda\right)
]

slopes. If

[
\lambda>QV,
]

then every slope is occupied. The packet’s condition (\lambda>QJ) is a slightly weaker but convenient sufficient condition.

For every occupied slope (z), set

[
P_z=\frac{I_S(w)-z}{E}.
]

Then (\deg P_z<k) and (P_z=(w-z)/E) on (S). Noncontainment is automatic: if (G\in F[X]_{<k}) agreed with (-1/E) on (S), then (EG+1) would have (a=k+t) roots but degree at most (a-1), forcing (EG+1=0), which is impossible.

Thus, under the packet’s support-wise definition,

[
\boxed{
\epsilon_{\rm mca}!\left(C,\frac jn\right)
\ge
\max\left{
\frac{\lambda}{\lambda+V},
\left(1-\frac V\lambda\right)_+
\right}.
}
]

Moreover,

[
\lambda>QV
\quad\Longrightarrow\quad
\epsilon_{\rm mca}!\left(C,\frac jn\right)=1.
]

This Paley form is stronger than the stated Cycle 47 theorem in the sparse critical window.

### Asymptotic corollary

Assume (k/n\to\rho\in(0,1)),

[
t=(c+o(1))\frac{n}{\log_2Q},
\qquad
\log Q=o(n).
]

Since (Q\ge n+1) on a multiplicative domain,

[
\log_2J=o(n),
]

while

[
\log_2\lambda
=============

\bigl(H_2(\rho)-c+o(1)\bigr)n.
]

Consequently,

[
0<c<H_2(\rho)
\quad\Longrightarrow\quad
\epsilon_{\rm mca}=1
]

for all sufficiently large (n).

This is the strongest theorem actually proved by Cycles 45–47.

It is a theorem over the field used for the anchor, denominator, code, and slopes. To read its entropy boundary as a (q_{\rm gen})-boundary with error normalized by (q_{\rm line}), one needs

[
q_{\rm gen}=q_{\rm line}=Q.
]

No extension-field transfer is implicit.

---

## BANKABLE_LEMMA — exact syndrome/transverse-secant equivalence

Let

[
\mathsf H:F^D\longrightarrow F^{r},
\qquad r=n-k,
]

be a parity-check/syndrome map for the Reed–Solomon code, and write (h_x=\mathsf H(e_x)) for its columns. For (T\subseteq D), define

[
V_T=\operatorname{span}{h_x:x\in T}.
]

For a line (u_z=f+zg), let

[
\ell(z)=\mathsf H(f)+z\mathsf H(g).
]

Then, with (j=\lfloor\delta n\rfloor),

[
\boxed{
z\text{ is support-wise MCA-bad}
\iff
\exists T\subseteq D,\ |T|\le j:
\ell(z)\in V_T
\ \text{and}\
\ell\not\subseteq V_T.
}
]

Indeed:

[
u_z|*{D\setminus T}\in C|*{D\setminus T}
\iff
\ell(z)\in V_T,
]

and

[
f|*{D\setminus T},g|*{D\setminus T}\in C|_{D\setminus T}
\iff
\mathsf H(f),\mathsf H(g)\in V_T
\iff
\ell\subseteq V_T.
]

For an RS parity-check matrix, the column matroid is uniform up to rank (r). Since (j<r), every transverse witness with (|T|<j) can be extended to an exact (j)-set while preserving transversality. Thus exact (j)-column spans may be used, but this padding lemma must be stated; it is not automatic for an arbitrary linear code.

MCA counts the number of distinct (z), not the number of pairs ((z,T)). This distinction is load-bearing.

---

## BANKABLE_LEMMA — exact denominator-regime trichotomy

Fix agreement size

[
a=k+\sigma
]

and an exact (a)-set (S). Let (I_S(w)) be the degree-(<a) interpolant.

For a degree-(t) datum ((E,B_{\rm num},w)), assume ([B_{\rm num}]_E\ne0).

### (t<\sigma)

Any witness polynomial (Q) has degree (<k+t<a), so it is uniquely determined by its values on (S). Distinct slopes give distinct (Q)’s. Hence

[
#{\text{bad slopes}}
\le
\left|\operatorname{List}
\bigl(
\operatorname{RS}[F,D,k+t],
w,
1-a/n
\bigr)\right|.
]

The residual slack is exactly

[
a-(k+t)=\sigma-t.
]

This is an injection into the actual RS list. It is not an injection into a usefully bounded raw locator fiber.

### (t=\sigma)

The witness is uniquely

[
Q=I_S(w),
]

and the landing condition is

[
[I_S(w)]*E\in F[B*{\rm num}]_E.
]

If (B_{\rm num}\ne0), noncontainment is automatic by the same root-count argument. This is the balanced residue-cloud problem.

### (t>\sigma)

All polynomials of degree (<k+t) agreeing with (w) on (S) form

[
I_S(w)+L_SF[X]_{<t-\sigma}.
]

Modulo (E), define the support-dependent direction space

[
U_S=[L_SF[X]_{<t-\sigma}]_E.
]

Then slope (z) lands exactly when

[
z[B_{\rm num}]_E
\in
[I_S(w)]_E+U_S.
]

For an active support,

[
\boxed{
\text{the witness is noncontained}
\iff
[B_{\rm num}]_E\notin U_S.
}
]

If ([B_{\rm num}]*E\in U_S), the landing condition also forces ([I_S(w)]*E\in U_S), and both (w/E) and (-B*{\rm num}/E) are explained on (S). If ([B*{\rm num}]_E\notin U_S), the affine plane intersects the scalar line in at most one slope.

Thus the (t>\sigma) statement in the current summary is a valid exact reduction. It is not an upper bound.

---

## BANKABLE_LEMMA — close-support geometry with its missing hypothesis

Let (T,T') be (j)-sets in syndrome space, and put

[
d=|T\setminus T'|,
\qquad
C=T\cap T',
\qquad
r=j+\sigma.
]

If (d\le\sigma), then (|T\cup T'|\le r), and MDS independence gives

[
V_T\cap V_{T'}=V_C,
\qquad
V_T+V_{T'}=V_{T\cup T'}.
]

Therefore:

* If the same point of (\ell) lies in both spans, it lies in the common core (V_C).
* If two distinct points of (\ell) lie respectively in (V_T,V_{T'}), then

  [
  \ell\subseteq V_{T\cup T'}.
  ]

For (d>\sigma), this conclusion fails: (T\cup T') already spans the whole syndrome space, and (V_T\cap V_{T'}) can be strictly larger than (V_C).

So “close support collisions produce common-core structure” is theorem-grade only with the exchange condition (d\le\sigma).

# WHAT_IS_NOT_PROVED

## Strongest missing theorem

The missing theorem remains

[
\boxed{\texttt{W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE}.}
]

A defensible same-field asymptotic formulation is:

Let (\rho) be fixed, let (D_n\subseteq\mathbb F_{Q_n}^{\times}) be generated-field smooth domains, and assume

[
\operatorname{poly}(n)\le Q_n\le 2^{o(n)},
]

[
k_n=\rho n+O(1),
\qquad
a_n=k_n+\sigma_n,
\qquad
j_n=n-a_n,
]

[
\sigma_n\ge C\frac n{\log n},
]

and

[
\sigma_n\log_2Q_n
\ge
(1+\varepsilon)\log_2\binom n{a_n}.
]

For every affine syndrome line (\ell), prove

[
#\left{
z:
\exists T,\ |T|\le j_n,
\ell(z)\in V_T,
\ell\not\subseteq V_T
\right}
\le
n^{1+o(1)}
+
2^{(\beta(\rho)/H_2(\rho))\mathcal Q_D(\sigma_n/n)(1+o(1))}.
]

No proof is supplied for this assertion, even when:

* (q_{\rm gen}=q_{\rm line});
* quotient-pullback denominators are removed;
* (t=\sigma);
* the denominator is squarefree and generic;
* the anchor is arbitrary;
* the line is not contained in a proper secant envelope.

The following are also unproved:

1. The corresponding finite theorem with explicit constants sufficient for (\epsilon^*=2^{-128}).
2. Any formula for the four official (\delta_C^*(2^{-128})).
3. The extension-valued version when (B\subsetneq F), hence (q_{\rm gen}\ne q_{\rm line}).
4. A repaired actual-list local limit for the (t<\sigma) reduction.
5. An integration theorem handling all (t>\sigma) data through the syndrome formulation.
6. The grand interleaved-list upper theorem.
7. A non-diagonal correlated-anchor construction beating the exponent (H_2(\rho)-mc), or a diagonalization theorem proving that this is impossible.
8. Line-by-line equivalence with the survey’s official MCA Definition 4.3.
9. Independent verification of the imported list-to-agreement theorem used by the universal-cap branch.

# OVERCLAIMS

1. **“Cycle 47 closes the smooth-domain lower branch” is missing the field ledger.**
   It closes the same-field branch under the packet’s support-wise definition. If (D\subseteq B\subsetneq F), the random-anchor proof over (F) pays (q_{\rm line}^t), not (q_{\rm gen}^t). Restricting the construction to (B) gives at most (|B|) bad slopes normalized by (|F|), not error one.

2. **“Below the entropy boundary” is only a leading-order asymptotic statement.**
   The exact entropy gap solves

   [
   \tau\log_2Q=H_2(\rho+\tau),
   ]

   not (c=H_2(\rho)). The latter is obtained only because (t=o(n)).

3. **There is no single finite entropy boundary.**
   Writing (\lambda=N/Q^t):

   * the sparse bad-slope fraction is already at least approximately (\lambda);
   * the expected bad-slope numerator is approximately (Q\lambda=N/Q^{t-1});
   * all slopes require roughly (\lambda\gg QV).

   These are separated by one or two factors of (Q). The sign of

   [
   \log N-t\log Q
   ]

   alone does not distinguish safe, polynomially rich, and all-slope behavior.

4. **An (n^{1+o(1)}) numerator needs more than the literal inequality (Q^\sigma>N).**
   A one-dimensional residue line has (Q) points. In the sparse regime the Bessel–Paley theorem forces approximately

   [
   \frac{N}{Q^{\sigma-1}}
   ]

   bad slopes. To expect (O(n)), one needs at least the finite line-reserve condition

   [
   \sigma\log_2Q-\log_2N
   \gtrsim
   \log_2(Q/n),
   ]

   or a fixed multiplicative entropy margin together with (Q=2^{o(n)}).

5. **COUNTERPACKET — entropy-only finite upper.**
   Take

   [
   F=\mathbb F_{5^{64}},
   \quad
   n=256,
   \quad
   k=128,
   \quad
   t=\sigma=2,
   \quad
   a=130.
   ]

   Let (D) be the subgroup of order (256). Since

   [
   \operatorname{ord}_{256}(5)=64,
   ]

   (D) generates (F), so

   [
   q_{\rm gen}=q_{\rm line}=5^{64}<2^{256}.
   ]

   Choose an irreducible quadratic (E) with nonzero linear coefficient and (B_{\rm num}=1). Such (E) is not a pullback through (X\mapsto X^2).

   Here

   [
   \log_2\binom{256}{130}=251.6279\ldots,
   \qquad
   2\log_2|F|=297.2068\ldots,
   ]

   so the literal entropy inequality (Q^2>N) is cleared by about (45.58) bits. Nevertheless

   [
   \lambda=2^{-45.5788\ldots},
   \qquad
   V<2,
   ]

   and the Bessel–Paley theorem gives

   [
   \epsilon_{\rm mca}
   \left(
   C,\frac{126}{256}
   \right)

   >

   2^{-48}.
   ]

   Equivalently, some aperiodic degree-two datum has more than (2^{100}) bad slopes.

   This is an official-rate, source-valid counterpacket to any finite theorem saying “entropy cleared plus non-quotient denominator implies (O(n)) slopes.” It does **not** refute the full corrected-reserve conjecture, because (\sigma=2) does not clear the (n/\log n) or quotient reserve.

6. **“Balanced exact witnesses are automatically noncontained” omits hypotheses.**
   The valid statement requires ([B_{\rm num}]_E\ne0), (t\le\sigma), and support size at least (k+\sigma). It is not valid without the nonzero reduced numerator. It actually holds for every (t\le\sigma), not only (t=\sigma).

7. **The residual-list reduction needs an actual list theorem.**
   It does not reduce to the raw object (\operatorname{Fib}_U(a)). The repository’s literal conjectures `conj:arbitrary-local` and `conj:final-locator` are false: if (U) is itself a degree-(<k) codeword, then every (a)-set lies in (\operatorname{Fib}_U(a)), although the actual list has size one.

8. **The syndrome formulation must count distinct slopes, not support incidences.**
   One syndrome point can lie in exponentially many (j)-column spans. Bounding

   [
   #{(z,T):\ell(z)\in V_T}
   ]

   is not equivalent to bounding MCA.

9. **“(j)-column secants” is ambiguous.**
   The exact equivalence naturally uses (|T|\le j). Replacing this by exactly (j) requires the MDS padding lemma. It is false as a purely formal step for an arbitrary linear code.

10. **“Close collisions imply common core” needs (d\le\sigma).**
    For (d>\sigma), the union already spans the full syndrome space and the common-core conclusion is false.

11. **“A fixed tangent/core template contributes linearly many slopes” is only justified for a codimension-one star.**
    If supports have the form (C\cup{x}), there are at most (n-|C|) petals. For exchange width (d), the raw template contains

    [
    \binom{n-|C|}{d}
    ]

    supports, potentially (n^d). No theorem in the packet collapses all (d\ge2) templates to a linear number of slopes.

12. **“Quotient/tangent/common-envelope/template” is not yet a classification.**
    The terms are not defined in one theorem, their overlaps are not resolved, and no total slope budget is proved. As written, the exception clause can absorb every rich line and make the inverse statement vacuous.

13. **Cycle 54’s determinant/quadric normal form is not a counting theorem.**
    A normal form does not bound split points, slope multiplicities, or noncontained witnesses. The (j=1) stratum is also asymptotically rate-one when (t=\sigma=2).

14. **Cycle 55’s (O(\sqrt Q)) fluctuation is not automatically a COUNTERPACKET.**
    A Weil-type (O(\sqrt Q)) upper error only cuts an attempted (O(1)) proof. To refute an (O(1)) theorem, one needs a family attaining (\Omega(\sqrt Q)). One must also prove that the counted split pairs yield distinct slopes rather than many supports for the same slope.

15. **The conic argument requires missing hypotheses.**
    At minimum: odd characteristic, nonsquare discriminant polynomial, geometric irreducibility, exclusion of diagonal/repeated-root pairs, and control of restriction to the actual smooth domain rather than all of (F_Q).

16. **Cycle 56 identifies only one obstruction to promotion.**
    The fact that (t=2,j=2) forces (k=n-4) is decisive, but not exhaustive. Promotion would also require the official field cap, generated-field condition, entropy and quotient reserves, distinct slopes, noncontainment, and exclusion from every named template.

17. **Cycle 57’s high-(j), (t=2) target is not the safe-side theorem.**
    In the balanced interpretation it has (\sigma=2), hence is sub-reserve in the live (Q=2^{o(n)}) regime. In the unbalanced interpretation (t=2<\sigma), it belongs to the residual actual-list branch. It may yield an official finite counterpacket or a useful algebraic model, but it cannot by itself prove the corrected-reserve upper theorem.

18. **External-model agreement is not a proof-status criterion.**
    “Five answers call it PROOF” has no evidentiary value. The Cycle 47 result is bankable because its algebra checks, not because models agreed.

19. **The (m)-anchor list construction does not solve the list challenge.**
    The exponent

    [
    H_2(\rho)-mc
    ]

    is a lower-bound/volume calculation. There is no matching upper theorem, no proof of correlated-rank diagonalization, and no determination of the official threshold against (\epsilon^*q_{\rm line}).

20. **No (q_{\rm chal}) theorem appears.**
    The code-theoretic denominator is (q_{\rm line}). Any use of a distinct verifier challenge field requires a protocol reduction proving that it is the actual slope field.

21. **An asymptotic (n^{1+o(1)}) statement does not determine the finite prize threshold.**
    The official constraints (k\le2^{40}), (|F|<2^{256}), and (\epsilon^*=2^{-128}) require explicit constants and rounding. None are supplied.

22. **The lower theorem does not give the matching “every (\delta>\delta^*)” branch.**
    It gives explicit bad radii and monotonic propagation upward. Without the safe theorem below those radii, no threshold is determined.

# ROUTE_CUTS

## ROUTE_CUT — entropy-only upper

A finite upper theorem based only on

[
Q^\sigma>\binom n{k+\sigma}
]

is false, even with an aperiodic denominator. The unavoidable critical-window term is of order

[
Q\lambda=\frac{\binom n{k+\sigma}}{Q^{\sigma-1}}.
]

## ROUTE_CUT — raw locator fibers

The (t<\sigma) branch cannot be closed by bounding every raw (\operatorname{Fib}_U(a)). That object can be (\binom na) for a one-element actual list.

## ROUTE_CUT — (q_{\rm line}) pays (q_{\rm gen})

No argument may use extension-field slope entropy to pay a base/generated-field locator bill. The exact extension-coordinate theorem only converts an (F)-line into a multiplication-matrix slice inside an interleaved (B)-code; it gives no positive bound.

## ROUTE_CUT — balanced-only integration

A theorem for (t=\sigma) does not cover (t>\sigma). The latter is a support-dependent affine-plane incidence problem. Any claimed full assembly omitting this branch is incomplete.

## ROUTE_CUT — conic counting alone

A split-pair estimate counts algebraic points or support pairs. MCA counts distinct noncontained slopes. A multiplicity theorem is indispensable.

## ROUTE_CUT — (t=2,j=2) promotion

This toy stratum has (n-k=4), hence (\rho\to1). It cannot be an official fixed-rate asymptotic counterpacket.

## ROUTE_CUT — (t=2) high-(j) as the main upper route

It is useful as a finite obstruction scanner, but it does not address the corrected-reserve regime where (\sigma\to\infty).

# NEXT_EXACT_LEMMA

## EXACT_NEW_WALL

The bare (n^{1+o(1)}) inverse should be replaced by a finite occupancy-calibrated statement:

[
\boxed{
\texttt{W-MCA-SYNDROME-TRANSVERSE-SECANT-FINITE-OCCUPANCY-INVERSE}.
}
]

For the same-field generated case (q_{\rm gen}=q_{\rm line}=Q), let

[
\lambda
= ======

\frac{\binom n{k+\sigma}}{Q^\sigma}.
]

Prove, uniformly for every affine syndrome line (\ell),

[
\boxed{
|\operatorname{Bad}_j(\ell)|
\le
n^{1+o(1)}
+
Q\lambda,n^{o(1)}
+
2^{(\beta(\rho)/H_2(\rho))
\mathcal Q_D(\sigma/n)(1+o(1))}.
}
]

Equivalently,

[
\epsilon_{\rm mca}
\le
\frac{n^{1+o(1)}}{Q}
+
\lambda n^{o(1)}
+
\frac{
2^{(\beta/H_2)\mathcal Q_D(1+o(1))}
}{Q}.
]

The three terms have separate meanings:

* (n^{1+o(1)}): tangent/common-envelope/template floor;
* (Q\lambda=N/Q^{\sigma-1}): unavoidable finite entropy occupancy, forced by the Bessel–Paley COUNTERPACKET;
* quotient term: the already known quotient profile.

This formulation has four advantages.

1. It is not contradicted in the finite critical window.
2. It specializes to the desired (n^{1+o(1)}) numerator when

   [
   \sigma\log Q
   \ge
   (1+\varepsilon)\log\binom n{k+\sigma},
   \qquad
   Q=2^{o(n)},
   ]

   because then (Q\lambda=2^{-\Omega(n)}).
3. It gives the correct finite security condition: to make the entropy term at most (2^{-128}), require approximately

   [
   \sigma\log_2Q-\log_2\binom n{k+\sigma}
   \ge128
   ]

   before adding structural terms.
4. It matches the proved lower theorem to within subpolynomial/shell factors.

The first attackable sublemma should be the quotient-free, envelope-free case:

> Let (\mathcal Q_D(\sigma/n)=-\infty), and suppose (\ell) is not contained in any proper column envelope (V_U) with (|U|<r). Under the corrected reserve, prove
> [
> |\operatorname{Bad}_j(\ell)|
> \le
> n^{1+o(1)}+Q\lambda n^{o(1)}.
> ]

Close support pairs with exchange (d<\sigma) force a proper envelope by the bankable close-support lemma. Thus the remaining case has a support selector with pairwise exchange at least (\sigma). The missing mathematical input is a fixed-line local limit for this far-support family. That is the irreducible core; the (t=2) conic calculations are only low-dimensional models of it.

A counterexample construction that would be equally decisive must satisfy all of:

[
\rho\in{1/2,1/4,1/8,1/16},
]

[
\sigma\ge Cn/\log n,
]

the generated-field entropy margin, controlled quotient profile, an aperiodic denominator or envelope-free syndrome line, and

[
|\operatorname{Bad}_j(\ell)|
\gg
n^{1+o(1)}+Q\lambda n^{o(1)}.
]

No such construction is currently present.

# FULL_SOLVE_DISTANCE

There is a credible route, but the project is not one routine lemma from completion.

For same-field scalar MCA:

1. The lower/failure theorem is closed.
2. The exact syndrome reformulation is closed.
3. The denominator-regime decomposition is closed.
4. The central fixed-line transverse-secant local limit is completely open.
5. Common-envelope and quotient templates still need a quantitative, nonvacuous total budget.
6. A finite (2^{-128}) version still needs explicit constants.

For the complete prize:

* extension-valued lines require an F1 theorem;
* the (t<\sigma) branch requires a repaired actual-list theorem;
* the interleaved-list threshold remains open;
* the official definition and protocol field ledger remain unaudited;
* no official-rate (\delta_C^*) values are justified.

The next productive move is therefore not another (t=2) case split. It is a proof or counterpacket for the calibrated quotient-free, envelope-free syndrome-line bound above.

Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
