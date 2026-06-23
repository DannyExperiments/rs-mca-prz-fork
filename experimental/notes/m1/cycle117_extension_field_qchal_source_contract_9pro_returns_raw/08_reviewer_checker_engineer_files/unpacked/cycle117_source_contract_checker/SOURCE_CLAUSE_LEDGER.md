# Source Clause Ledger

Every clause is bound both by the whole-file SHA-256 in the checker and by the line-slice SHA-256 below. Line numbers are valid only for the pinned bytes.

## RS_GENERAL_SMOOTH_ROW

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `91-95`
- Slice SHA-256: `cb78d937dd5dd59e79119f3bf4e04ba9926a625a39bba8aed2940e89b1f8d37b`
- Use: General RS row over a field; smooth power-of-two subgroup domain.

```text
The Proximity Prize \cite{ProximityPrize,ABF26,BonehKeynote} concerns Reed--Solomon codes
\[
        \RS[\F,D,k]=\{(P(x))_{x\in D}:\deg P<k\},\qquad n=|D|,\ \rho=k/n,
\]
over \emph{smooth} multiplicative domains.  In this paper all stated counterexamples use multiplicative subgroups $D\le\F^\times$ of power-of-two order; the same locator calculation also applies to multiplicative cosets after the evident rescaling, but no coset generality is needed below.  Correlated-agreement theorems control, for a random $z$, whether closeness of $f+zg$ to the code forces closeness of $f$ and $g$ individually; the \emph{mutual} (support-wise) version asks this on the same agreement set, which is what FRI/WHIR-style extractors consume \cite{FRI,WHIR}.  Proximity gaps and (M)CA are known throughout the Johnson regime $\delta<1-\sqrt\rho$ \cite{BCIKS23}, and the prize challenge is the region between Johnson and capacity $1-\rho$.  The optimistic endpoint --- conjectured in various forms since proximity gaps were introduced \cite{BCIKS23}, and the natural reading of the grand challenge --- is:
```

## RS_CAPACITY_TRANSCRIPTION_SCOPE

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `97-107`
- Slice SHA-256: `2359254ed1a211638b59758f50cda02b50c506130c63ec5eb5df36f3a24e5956`
- Use: No-slack support-wise line form and explicit statement that it is a manuscript transcription of the challenge.

```text
\begin{conjecture}[Up-to-capacity MCA; no-slack support-wise line form]\label{conj:capacity}
Let $C=\RS[\F,D,\rho n]$ be a smooth-domain Reed--Solomon code, $\rho\in\{1/2,1/4,1/8,1/16\}$.  For every $\delta<1-\rho$,
\[
        \eps_{\rm mca}(C,\delta)\ \le\ \mathrm{negl}(q)
        \qquad\big(\text{concretely: }\le2^{-128}\text{ for the prize fields}\big),
\]
where $\eps_{\rm mca}$ is the support-wise line-MCA error of \cref{def:mca} below.  List-decoding analogue: for every $\delta<1-\rho$, every received word has at most $\mathrm{poly}(q)$ codewords within relative distance $\delta$.
\end{conjecture}

\begin{remark}[What exactly is being refuted]\label{rem:formulation}
The prize materials phrase the challenge as determining the largest $\delta$ with negligible MCA/list error \cite{ProximityPrize,ABF26}; \cref{conj:capacity} is the assertion that this $\delta$ reaches capacity, transcribed in the minimal no-slack, same-support, two-word (line) form.  Everything below refutes \emph{this} form, quantitatively and with explicit witnesses.  If a formulation includes a slack parameter $\tau$, a curve variant, or a different agreement notion, our results convert into necessary conditions on that formulation (\cref{sec:scope}): in particular any slack $\tau\le2^{-18}$ is insufficient on BabyBear/KoalaBear domains with $2^{18}\mid n$, and $\tau\le c_\rho/\log p$ is insufficient on infinitely many smooth prime fields.  We do not claim anything about slacked formulations above these floors.
```

## RS_SUPPORTWISE_MCA_DEFINITION

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `110-115`
- Slice SHA-256: `e65dbc3b34be54e4e6c3a45c48da32a2adf519047ec7a006d60e6201e28572d9`
- Use: Bad-slope predicate and denominator |F|.

```text
\begin{definition}[Support-wise line-MCA error]\label{def:mca}
For a linear code $C\subseteq\F^D$ and a line $u_z=f+zg$, the parameter $z$ is \emph{bad at radius $\delta$} if there is $S\subseteq D$, $|S|\ge(1-\delta)n$, and $c\in C$ with $u_z|_S=c|_S$, while no pair $c_f,c_g\in C$ has $f|_S=c_f|_S$ and $g|_S=c_g|_S$.  Then
\[
        \eps_{\rm mca}(C,\delta)=\max_{f,g}\ \frac{\#\{z\in\F:\ z\ \text{bad}\}}{|\F|}.
\]
\end{definition}
```

## RS_EXTENSION_FIELD_CONSTRUCTION

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `369-383`
- Slice SHA-256: `8c102986da07b6d90fa8935639c836aa95e0490817cc1c7e47e5b7711a38dcb3`
- Use: Generated extension-field subgroup construction.

```text
\section{Extension-field towers and density variants}\label{sec:extension-towers}

The prime-field quotient ladder already gives the deployed-field disproof.  The following scalar-coset construction gives generated extension-field examples with error one at one symbol below capacity and explains why borderline fields such as Goldilocks still have large bad-slope density even when full restricted-sum coverage fails.

\begin{lemma}[Scalar-coset subgroup]\label{lem:ext-coset-subgroup}
Let $p$ be an odd prime, let $m\mid p-1$, put $n=md$, and assume
\[
        \ord_{md}(p)=d.
\]
Then $\F_{p^d}^{\times}$ contains an element $\zeta$ of order $n$.  If $H\le\F_p^\times$ is the subgroup of order $m$ and $D=\langle\zeta\rangle\le\F_{p^d}^{\times}$, then
\[
        D=\bigsqcup_{i=0}^{d-1}\zeta^iH,
\]
and $1,\zeta,\ldots,\zeta^{d-1}$ is an $\F_p$-basis of $\F_{p^d}$.  Conversely, an element of order $n$ and degree $d$ over $\F_p$ has $\ord_n(p)=d$.
\end{lemma}
```

## RS_EXTENSION_FIELD_THEOREM

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `416-426`
- Slice SHA-256: `599e4870896dc62efe427b0154ba84aab9888d5ba4c61237223e3d9f3abac139`
- Use: Smooth extension towers theorem over F_{p^d}.

```text
\begin{theorem}[Smooth extension towers: full density]\label{thm:ext-smooth-towers}
Let $p\equiv1\pmod4$ be prime, let $m=2^{\vtwo(p-1)}$, let $d$ be a power of two, and let $D\le\F_{p^d}^{\times}$ be the subgroup of order $n=md$ supplied by \cref{lem:ext-coset-subgroup,lem:ext-tower-criterion}.  Fix $0<\rho\le1/2$ with $r:=\rho m\in\Z$, and assume
\[
        \rho(1-\rho)m^2\ge p.
\]
Then, for $k=\rho n$,
\[
        \eps_{\rm mca}\left(\RS[\F_{p^d},D,k],\,1-\rho-\frac1n\right)=1.
\]
In particular, if $m^2\ge18p$, this holds simultaneously for all four prize rates.
\end{theorem}
```

## RS_PROTOCOL_SCOPE_CUT

- File: `inputs/source/RS_disproof_v3.tex`
- Lines: `505-511`
- Slice SHA-256: `1631cbc8c19d631c6790f12130bb633c5be03df2b5140ee71f4255be1b3bf556`
- Use: Protocol-specific constraints are absent; protocol soundness is untouched.

```text
\section{Scope: what is refuted, what survives}\label{sec:scope}

\paragraph{Refuted.}  \Cref{conj:capacity} in its stated form, at every prize rate, for every target $\eps^*<1$, on the deployed FFT fields (error one, on an interval), on linear-size Fermat fields (error $1-1/p$, verified), on generated extension-field smooth towers (error one at one symbol below capacity when the scalar-coset coverage condition holds), and even on borderline Goldilocks-type towers at non-negligible density.  In the negligibility sense, with non-negligible meaning inverse-polynomial in $\lambda=\log_2q$, the conjecture also fails on infinitely many smooth prime fields at radius $1-\rho-O(1/\log p)$.  The polynomial-list analogue fails unconditionally at the prize rates on every power-of-two subgroup domain with $n\ge(\log_2q)^{1+\eps}$ for any fixed $\eps>0$; the divisor-level version of \cref{thm:main}(d) is valid for arbitrary rates whenever the chosen divisor $N$ satisfies $\rho N\in\Z$.

\paragraph{Not refuted, and turned into floors.}  Any formulation with explicit slack $\tau$: our results show such a formulation \emph{must} take $\tau>1/\hat N\asymp\sqrt{\rho(1-\rho)/p}$ on fields where the $2$-part of $p-1$ reaches $\hat N$ (including BabyBear, KoalaBear, and $3\cdot2^{30}+1$), $\tau>c_\rho/\log p$ on the sieve fields, and $\tau>(\log_2q)^{-1-\eps}$ for the prize-rate list version whenever the domain has the corresponding dyadic divisors; above these floors the present no-slack arguments make no negative claim.  The restricted-sum mechanism itself cannot certify arbitrary depths: certifying error $\eta$ at $1-\rho-1/N$ through a quotient $Q$ needs $\binom{N}{\rho N+1}\ge\eta q$ (the construction's bad set has size at most $|(\rho N{+}1)^{\wedge}Q|\le\binom{N}{\rho N+1}\le2^{\HH(\rho)N(1+o(1))}$), i.e.\ $N\ge\log_2(\eta q)/\HH(\rho)\,(1-o(1))$ --- a radius gap $O(\HH(\rho)/\log_2(\eta q))$ at best.  Curve-MCA and exact slacked threshold formulations require additional constraints and analysis beyond the no-slack model studied here; protocol-level soundness of FRI/WHIR-type systems is untouched, because deployed analyses operate in the Johnson regime with margins and include protocol-specific constraints absent from this minimal no-slack definition.

\paragraph{Companion manuscripts.}  The corrected slack/entropy theory and failure-ladder calculus built on these floors are developed in \cite{SlackTheory}.  The divisor-level list bound of \cref{thm:main}(d), sharpened to slack two and pigeonholed over the field of definition, composes with the Crites--Stewart list-to-agreement conversion \cite{CS25} into a field-size-universal challenge cap in \cite{UniversalCap}, which also places the list mass directly against the survey's $\eps^*|\F|$ budget.
```

## SLACK_GENERAL_PRIME_POWER_NOTATION

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `153-160`
- Slice SHA-256: `d4cec43b03dff8ea013aa7dbb5f554008b67294e73a0d3a9accb0e9a3632c279`
- Use: General prime-power notation and smooth subgroup RS code.

```text
\paragraph{Setting and notation.}
$p$ is prime ($q$ a general prime power where stated); $D$ or $H\le\F_q^\times$ is a multiplicative subgroup of order $n$, \emph{smooth} meaning $n$ is a power of two; $C=\RS[\F_q,D,k]=\{(P(x))_{x\in D}:\deg P<k\}$ with $k=\rho n$, $\rho\in(0,1)$ fixed.  For a finite set $A$ in a field, $L_A(X)=\prod_{a\in A}(X-a)=X^{|A|}+\sum_{j\ge1}(-1)^je_j(A)X^{|A|-j}$ and $p_j(A)=\sum_{a\in A}a^j$; for $h\ge0$, $h^{\wedge}A$ is the set of sums of $h$ distinct elements of $A$.  $\HH$ is binary entropy.  Divisibility hypotheses ($\rho N\in\Z$, $t\mid N$, $t\mid\rho N$, $\sigma\mid k$, and the like) are stated where they are used.

\part{List entropy, quotient cores, and Route 1}

\section{List decoding as a locator-fiber problem}\label{sec:fiber}

Every received word $y:H\to\F_q$ has a unique interpolant $U\in\F_q[X]$ of degree $<n$ on $H$.  Write $\List(y,\delta)$ for the list of codewords within relative radius $\delta$ of $y$, and $\Lst(C,\delta)=\max_y|\List(y,\delta)|$ for the worst-case list size.  A codeword $P$ agrees with $y$ on a set $S\subseteq H$ if and only if
```

## SLACK_SUBFIELD_CORRECTION

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `600-602`
- Slice SHA-256: `4f5874dcd18643064fe140c266037776315a7f9e272650a2ddb7d7d3f777e4fd`
- Use: Generated-field or field-of-definition correction.

```text
\begin{remark}[Subfield correction]\label{rem:subfield}
If $H$ is contained in a proper subfield $\F_{q_0}\subsetneq\F_q$, then the entropy scale is governed by the field of definition $q_0$, not the ambient alphabet size $q$.  Indeed, locator coefficients of subsets of $H$ lie in $\F_{q_0}$, and the pigeonhole denominator in \Cref{thm:pigeonhole} is $q_0^\sigma$.  Thus any ambient-$q$ formulation over extension fields is false unless a generated-field hypothesis or a field-of-definition parameter is included.
\end{remark}
```

## SLACK_SUPPORTWISE_MCA_DEFINITION

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `639-653`
- Slice SHA-256: `197663dd490be2970fc80a78116acf6a937f1922cf67de91adb6e146477bf046`
- Use: Support-wise line-MCA definition and |F| denominator.

```text
\begin{definition}[Support-wise agreement]\label{def:sclose}
For $C\subseteq\F^D$, $|D|=n$, $\delta\in[0,1]$: a word $u\in\F^D$ is \emph{$S$-close} to $C$ at radius $\delta$ if $S\subseteq D$, $|S|\ge(1-\delta)n$, and $u|_S=c|_S$ for some $c\in C$.
\end{definition}

\begin{definition}[Bad parameter and line-MCA error]\label{def:mca}
For a line $u_z=f+zg$, $z\in\F$: the parameter $z$ is \emph{support-wise MCA-bad} at radius $\delta$ if there is $S\subseteq D$ with (i) $u_z$ $S$-close to $C$ at radius $\delta$, and (ii) no pair $c_f,c_g\in C$ satisfying $f|_S=c_f|_S$ and $g|_S=c_g|_S$.  Then
\[
        \emca(C,\delta)\ =\ \max_{f,g\in\F^D}\ \frac1{|\F|}\,\#\{z:\ z\text{ support-wise MCA-bad for }f+zg\},
\]
and the threshold is
\[
        \delta^*_C(\eps^*)=\sup\{\delta:\emca(C,\delta)\le\eps^*\}.
\]
A witness at radius $\delta$ is one at every larger radius (neither condition mentions $\delta$ otherwise), so $\emca(C,\cdot)$ is nondecreasing and error one propagates upward; this is the monotonicity lemma of \cite{NoSlack}.
\end{definition}
```

## SLACK_TANGENT_FLOOR

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `667-674`
- Slice SHA-256: `4a10260c3ceba3115243f8989477eabe5ca432d22de1f4b8800158827be661bf`
- Use: Tangent floor is a lower bound, not an exclusion.

```text
\begin{proposition}[Tangent floor]\label{prop:floor}
For $C=\RS[\F,D,k]$ and $\delta\in(0,1-\rho)$ with $m=\lfloor\delta n\rfloor\le q$:
$\emca(C,\delta)\ \ge\ m/q$.
\end{proposition}

\begin{proof}
Fix $E\subseteq D$, $|E|=m$, codewords $P_1,P_2$, and $f=P_1+e_f$, $g=P_2+e_g$ with errors supported on $E$, $e_g\equiv1$ there and $e_f$ injective there.  For $x\in E$ put $z_x=-e_f(x)$ and $S_x=(D\setminus E)\cup\{x\}$: the error of $u_{z_x}$ against the codeword $P_1+z_xP_2$ vanishes at $x$ and off $E$, so condition (i) holds; a codeword explaining $g$ on $S_x$ would agree with $P_2$ on $n-m>k$ points, hence equal $P_2$, contradicting $g(x)\ne P_2(x)$: condition (ii).  The $m$ slopes $z_x$ are distinct and bad.
\end{proof}
```

## SLACK_SUBFIELD_CONFINEMENT

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `1529-1540`
- Slice SHA-256: `1a42660bdfe8982699c63707361967b245820aa6c1b062eb0956c00fb61ed6c3`
- Use: Subfield confinement condition D subset B and B-valued line.

```text
\section{Subfield confinement over extension fields}\label{sec:subfield}

Deployed instantiations sample the slope from an extension field $\F=B^{\,d}$ of the base field $B$ containing the domain.  The following confinement theorem shows the entire prime-field witness theory deflates by a factor $|B|/|\F|$ in that setting, while the list-side obstructions persist --- so the two grand challenges genuinely decouple over extensions.  A two-radius refinement of \cref{thm:subfield}, covering the proximity-loss form of correlated agreement, is proved in \cite[Lem.\ ``subfield confinement'']{UniversalCap}.

\begin{theorem}[Subfield confinement]\label{thm:subfield}
Let $B\le\F$ be a subfield, $D\subseteq B$, $C=\RS[\F,D,k]$, and let $f,g\in B^D$ be $B$-valued words.  Then every support-wise MCA-bad parameter of the line $f+zg$, at every radius, lies in $B$.
\end{theorem}

\begin{proof}
Fix a $B$-basis $e_1=1,e_2,\dots,e_d$ of $\F$ and the $B$-linear coordinate projections $\pi_i:\F\to B$.  For $P\in\F[X]_{<k}$ and $x\in D\subseteq B$ we have $\pi_i(P(x))=(\pi_iP)(x)$, where $\pi_iP$ applies $\pi_i$ to coefficients; each $\pi_iP$ is a codeword.  Let $z\notin B$, so $z=\sum_iz_ie_i$ with $z_{i_0}\ne0$ for some $i_0\ge2$, and let $S$ be any set on which $f+zg$ agrees with a codeword $P$.  Comparing coordinates on $S$: the $i_0$-th coordinate of $(f+zg)(x)=f(x)+zg(x)$ is $z_{i_0}g(x)$, so $g|_S=(z_{i_0}^{-1}\pi_{i_0}P)|_S$, and the first coordinate is $f(x)+z_1g(x)$, so $f|_S=(\pi_1P-z_1z_{i_0}^{-1}\pi_{i_0}P)|_S$.  Both explaining polynomials have degree $<k$, so $f$ and $g$ are simultaneously explained on $S$ itself, and $z$ fails condition (ii) of \cref{def:mca} for every candidate $S$.
\end{proof}
```

## M2_LDSW_EXACT_BRIDGE

- File: `inputs/source/m2_line_decoding_mca_bridge.md`
- Lines: `12-68`
- Slice SHA-256: `28a631bd5a52c92f79df653f121f9d77153980968a433c8927c82d182e4e83f1`
- Use: Definition of LD_sw and exact equality with epsilon_mca.

```text
## Setup

Let `C <= F^D` be a linear code over a finite field `F`, with `|D|=n`.
For `S subset D`, write `C|S` for the punctured code on `S`.  Let

```text
a(delta) = ceil((1-delta)n).
```

For a line `ell_z = f + z g`, with `f,g in F^D`, call a slope `z`
support-wise noncontained at agreement size `a` if there is a support
`S subset D` such that

```text
|S| >= a,
(f + z g)|S in C|S,
and there do not exist c_f,c_g in C with f|S=c_f|S and g|S=c_g|S.
```

Define the support-wise line-decoding numerator

```text
LD_sw(C,a) =
  max_{f,g in F^D} #{z in F : z is support-wise noncontained for f+z g
                    at agreement size a}.
```

This is the line-decoding numerator that the MCA ledger can consume directly.

## Exact Bridge

For every linear code `C <= F^D` and every `delta in [0,1]`,

```text
eps_mca(C,delta) = LD_sw(C,ceil((1-delta)n)) / |F|.
```

This is an equality, not only an implication.  The support-wise MCA definition
maximizes over the same pairs `(f,g)` and counts the same slopes `z`: a large
support explaining the line point but not simultaneously explaining `(f,g)`.
The only conversion is from radius to agreement size by
`a=ceil((1-delta)n)`.

Consequently, any theorem proving

```text
LD_sw(C,a(delta)) <= a_LD
```

immediately gives

```text
eps_mca(C,delta) <= a_LD / |F|.
```

This is the precise finite-length content behind the manuscript phrase
`(delta,a_LD,n+1) line-decodable => eps_mca <= a_LD/|F|`.
```

## M2_CLOSE_POINT_LINE_DECODING_SUFFICIENT_ONLY

- File: `inputs/source/m2_line_decoding_mca_bridge.md`
- Lines: `249-266`
- Slice SHA-256: `f5defc6ca1906b90dfd4c8a4c4772b0db80899c0cea5714cc4b73efc1fe88dc2`
- Use: Close-point line decoding is a sufficient stronger predicate, not equivalent.

```text
## What an External Line-Decoding Theorem Must Prove

A close-point line-decoding bound with a contained-line exception,

```text
either f+F g is contained in C, or #{z : dist(f+z g,C) <= delta} <= a_LD,
```

is sufficient, since support-wise noncontained slopes are a subset of close
line points, and a line contained in `C` has no support-wise noncontained
slopes.  This sufficient condition is usually stronger than necessary.

## Close-Point Line-Decoding Is Strictly Stronger

The sufficient close-point predicate above is not equivalent to the
support-wise numerator.  This matters when importing external line-decoding
theorems: a theorem that bounds all close line points with only a "line
contained in the code" exception may be much stronger than what MCA needs.
```

## M2_EXTERNAL_DEFINITION_STILL_TO_MATCH

- File: `inputs/source/m2_line_decoding_mca_bridge.md`
- Lines: `406-414`
- Slice SHA-256: `5d9a59a8fd9698e1c6fe6e64e40c47e3a0f382afd79f78c42d0884b3873deb30`
- Use: External (delta,a_LD,n+1) definition remains an explicit follow-up check.

```text
## Follow-Up Checks

- Match the external `(delta,a_LD,n+1)` line-decoding definition used in
  protocol papers against `LD_sw(C,a)`.
- Decide whether the `n+1` parameter is only a codeword-uniqueness threshold or
  whether it hides an additional proximity-loss convention.
- Check whether protocol line-decoding imports have a common-support or
  code-line-proximity exception strong enough to avoid the spike-line
  close-point separation.
```

## C116_SMOOTH_ROW_AND_CANONICAL_AR

- File: `inputs/cycle116/CYCLE116_CERTIFICATE.md`
- Lines: `276-325`
- Slice SHA-256: `759154e4d984ab4e78f445da558f91480cf2dcdc77d631a7c60a3a0f1b3aa373`
- Use: F_17^32 lift, order-512 H, and canonical A/R partition.

```text
### 4. Smooth \([512,256]\) agreement-padding lift

Let \(q_0=17^{16}\).  By the 2-adic lifting formula,

\[
v_2(q_0-1)
=v_2(17-1)+v_2(17+1)+v_2(16)-1
=8.
\]

Thus the 2-Sylow subgroup of \(F_0^\times\) has order \(256\).  Since \(\eta\) has exact order \(256\), it is not a square in \(F_0\).  Therefore

\[
K=F_0(\theta),
\qquad \theta^2=\eta,
\]

is a quadratic field extension, so

\[
K\cong\mathbb F_{17^{32}}.
\]

Moreover, \(\operatorname{ord}(\theta)=512\), because \(\theta^2\) has order \(256\).  Put

\[
H=\langle\theta\rangle
=D_0\sqcup\theta D_0,
\qquad |H|=512.
\]

Take

\[
A=\{\theta\eta^i:0\le i\le118\},
\qquad |A|=119,
\]

and

\[
R=\{\theta\eta^i:119\le i\le255\},
\qquad |R|=137.
\]

Then \(D_0,A,R\) are pairwise disjoint and

\[
H=D_0\sqcup A\sqcup R.
\]
```

## C116_PADDING_RETENTION_AND_THRESHOLD

- File: `inputs/cycle116/CYCLE116_CERTIFICATE.md`
- Lines: `335-419`
- Slice SHA-256: `78b87b9c3780ce24af03bbec8d0885ff01703df8933c2b12d9e8b545a6ba83ab`
- Use: Padding preserves noncontainment; LD_sw/MCA theorem and threshold arithmetic.

```text
For the native line \(f+zg\), define words on \(H\) by

\[
\widetilde f(x)=
\begin{cases}
L_A(x)f(x),&x\in D_0,\\
0,&x\in A\cup R,
\end{cases}
\qquad
\widetilde g(x)=
\begin{cases}
L_A(x)g(x),&x\in D_0,\\
0,&x\in A\cup R.
\end{cases}
\]

For a native bad slope \(z\), let \(p_z\in F_0[X]_{<137}\) be the explaining polynomial on \(S_z\subseteq D_0\), \(|S_z|=143\).  Then

\[
\widetilde p_z=L_Ap_z
\]

has degree \(<256\) and explains \(\widetilde f+z\widetilde g\) on

\[
S'_z=S_z\cup A,
\qquad |S'_z|=143+119=262.
\]

If degree-\(<256\) polynomials \(F,G\in K[X]\) simultaneously explained \(\widetilde f,\widetilde g\) on \(S'_z\), both would vanish on all 119 points of \(A\).  Hence

\[
F=L_AF_0,
\qquad G=L_AG_0,
\qquad \deg F_0,\deg G_0<137.
\]

Dividing on \(S_z\), where \(L_A\ne0\), would give simultaneous native explanations over \(K\), hence over \(F_0\), contradicting native noncontainment.  Thus every native bad slope remains bad after the lift.

Consequently, for

\[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\]

one has

\[
\boxed{
\operatorname{LD}_{\rm sw}(C,262)
\ge52{,}747{,}567{,}092.
}
\]

Since

\[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil=262,
\]

the exact MCA bridge gives

\[
\boxed{
\epsilon_{\rm mca}\!\left(C,\frac{125}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}.
}
\]

Finally,

\[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6
<52{,}747{,}567{,}092,
\]

so

\[
\boxed{
\epsilon_{\rm mca}\!\left(C,\frac{125}{256}\right)>2^{-128}.
}
```

## C116_NONCONTAINMENT_PROOF

- File: `inputs/cycle116/CYCLE116_CERTIFICATE.md`
- Lines: `478-540`
- Slice SHA-256: `0d1cd82a4bbb3ae070511c84b84152dbef10805bf4bc8e5bb9fae8979a6795f0`
- Use: One affine line and support-wise noncontainment proof.

```text
The parity-check matrix has rank \(r\).  Choose \(g\) explicitly by

\[
g(a)=\frac{V_D(\beta)}{\beta-a};
\]

Lagrange interpolation gives \(H_Cg=y_1\).  Choose \(f\) with \(H_Cf=y_0\); for example, invert any weighted Vandermonde \(r\times r\) column minor and take \(f\) supported on those \(r\) coordinates.

Since \(H_C(f+z_Jg)\in W_J\), there is an error word \(e_J\) supported on \(J\) with

\[
H_Ce_J=H_C(f+z_Jg).
\]

Thus

\[
c_J=f+z_Jg-e_J\in C,
\]

and \(c_J=f+z_Jg\) on \(S_J=D\setminus J\).

### B. Support-wise noncontainment

If \(g|_{S_J}\) were explained by a codeword \(c_g\in C\), then \(g-c_g\) would be supported on \(J\), and therefore

\[
y_1=H_Cg\in W_J.
\]

But \(W_J\) has the same span as \(\{v(a):a\in J\}\), while the \(j+1\) Vandermonde columns

\[
\{v(a):a\in J\}\cup\{v(\beta)\}
\]

are linearly independent because \(j+1\le r\) and \(\beta\notin D\).  Hence \(y_1=v(\beta)\notin W_J\), a contradiction.  Thus \(g\) is not code-explainable on \(S_J\), which is stronger than the required failure of simultaneous explanation.

### C. Degree-one residue datum

Set

\[
E=X-\beta,
\qquad B=V_D(\beta),
\qquad w=E f
\]

as words on \(D\).  Since \(g=-B/E\) on \(D\), if \(C_J(X)\) is the degree-\(<k\) polynomial representing \(c_J\), then

\[
Q_J=EC_J+z_JB
\]

satisfies

\[
\deg Q_J<k+1,
\qquad Q_J\equiv z_JB\pmod E,
\qquad Q_J=w\text{ on }S_J.
\]

The preceding Vandermonde argument proves the residue witness is noncontained.  Thus the theorem genuinely constructs one affine line, explaining codewords, witness supports, a common degree-one denominator, and noncontainment.
```

## C116_Q_LEDGER_AND_SCOPE

- File: `inputs/cycle116/CYCLE116_CERTIFICATE.md`
- Lines: `585-608`
- Slice SHA-256: `0ed7a9580d9e1d76ab8d6c1ccef548076fef80b23bee289e30a922eac062e1fd`
- Use: q_gen/q_code/q_line/q_chal ledger and finite-only scope.

```text
|---|---:|---:|
| Base/code field | \(\mathbb F_{17^{16}}\) | \(K=\mathbb F_{17^{32}}\) |
| \(q_{\rm gen}\) | \(17^{16}\) | \(17^{32}\) |
| \(q_{\rm code}\) | \(17^{16}\) | \(17^{32}\) |
| \(q_{\rm line}\) | \(17^{16}\) | \(17^{32}\) |
| \(q_{\rm chal}\) | uninstantiated | uninstantiated |
| Domain | \(D_0=\langle\eta\rangle\) | \(H=\langle\theta\rangle\) |
| Length \(n\) | 256 | 512 |
| Dimension \(k\) | 137 | 256 |
| Agreement | 143 | 262 |
| Radius \(\delta\) | \(113/256\) | \(125/256\) |
| Certified numerator | \(N\) | \(N\) |

For the lifted row, \(q_{\rm gen}=17^{32}\) because \(H\) contains \(\theta\), \(\eta=\theta^2\) generates \(F_0\) over \(\mathbb F_{17}\), and \(F_0(\theta)=K\).  Only \(q_{\rm line}=|K|\) appears in the MCA denominator.  No verifier challenge field is used.

## SELF-AUDIT

1. **Exact theorem proved.**  A finite smooth-domain \([512,256]\) Reed--Solomon code over \(\mathbb F_{17^{32}}\) has a single affine line with at least \(N\) support-wise noncontained slopes at agreement 262.  Therefore the stated \(\operatorname{LD}_{\rm sw}\) and MCA lower bounds hold.
2. **Not proved.**  No ordinary list-decoding lower bound of size \(N\); no protocol soundness failure; no asymptotic theorem; no official Proximity Prize admission; no accepted prime-field realization; no \([464,232]\) smooth lift.
3. **Common-line issue.**  Closed by the parity-check/fixed-top-coefficient construction.  The line, direction, reciprocal slope gauge, explaining codewords, supports, and noncontainment are common or explicitly identified.
4. **Cycle84 identities.**  Closed by the 336 block identities and the two zero subleading coefficients.  The exact statements are \(P_T=X^{113}-X^{112}+\deg\le107\) and \(P_T(\beta)=4(\beta-1)\Phi(T)\).
5. **Smooth lift.**  Agreement and noncontainment survive by the fixed vanishing factor \(L_A\); scalar extension is controlled by interpolation.
6. **Loss audit.**  Reciprocal/scalar normalization is bijective; same-slope collisions are already reflected in occupancy; all slopes are finite because \(P_T(\beta)\ne0\); contained/tangent witnesses are excluded by the Vandermonde argument; no additional color division is allowed; quotient/periodic classifications do not alter the raw source definition.  Any official retained-event normalization would require a separate theorem.
7. **Residue stratum after lifting.**  The native row is explicitly degree-one residue-line.  The padding proof certifies the lifted row directly through support-wise MCA; it does not claim that the lifted line remains in the same degree-one residue coordinate.
```

## C116_OFFICIAL_CONTRACT_WALL

- File: `inputs/cycle116/CYCLE116_CERTIFICATE.md`
- Lines: `610-612`
- Slice SHA-256: `05e27dde42c84846a478e4f9ff936671f0b34a8171bcfaa30453e84d1952729d`
- Use: Authority-pinned admission/source/challenge-field contract remains the next step.

```text
## NEXT EXACT STEP

Package the theorem note and checker together and correct the stale prose generator line.  The checker already fail-closes on the 25-file `REVIEW_MANIFEST.sha256` root and explicitly verifies both based logarithms.  For official-prize promotion, the next lemma is not algebraic: it is an authority-pinned admission/source/challenge-field contract specifying whether this extension-field row is admitted and what, if any, endpoint, periodic, affine-color, or retained-event processing applies.
```

## SLACK_QUOTIENT_PERIODIC_ANALYTIC_ROLE

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `1693-1699`
- Slice SHA-256: `4aebef764b6cbfaa1480eb8416d220e305ba654f3321a30b2a67e79b66bd7edd`
- Use: Quotient-periodic structure appears in a corrected analytic positive-side ledger, not in the raw bad-parameter definition.

```text
On the MCA side, the same two-scale shape is now matched by proved statements in Part~II: the quotient-exact floor (\cref{prop:qfloor}) shows the closed-form quotient count survives at every prime above the quotient norm threshold, the necessity theorem (\cref{thm:qnecessity}) shows the quotient profile of \cref{def:qprofile} is genuinely necessary for polynomial MCA slope bounds at large primes, and the deployed-rate challenge cap (\cref{prop:prize}) translates the floor into concrete prime-field parameter statements.

The proved positive side currently reaches two important but not final regimes.  In characteristic zero, prefix fibers are exactly quotient-periodic and therefore polynomial at $\sigma\ge Cn/\log n$.  In prime fields $p\equiv1\pmod n$, the Galois-amplified no-collision theorem transfers this to finite fields once
\[
        p>\exp\!\left(C\frac{n\log n}{\sigma}\right).
\]
At the corrected reserve $\sigma\asymp n/\log n$, this is the quasi-polynomial split-prime range $p>\exp(O((\log n)^2))$.
```

## SLACK_QUOTIENT_PERIODIC_FLOOR_SEPARATION

- File: `inputs/source/slackMCA_v3.tex`
- Lines: `1724-1730`
- Slice SHA-256: `0b900d0ec73235b091867709ec6fddeed76f5742b26af466d82e4061932b0867`
- Use: The later conjectural bound explicitly separates tangent and quotient-periodic floors on the bound side.

```text
and put $\eta_n=\sigma_n/n$ and $C_n=\RS[\F_{q_n},H_n,k_n]$.  Then, with the unavoidable tangent floor and the separated quotient-periodic floor included on the right,
\[
        \emca\big(C_n,1-\rho-\eta_n\big)
        \le
        \frac{n^{1+o(1)}+2^{(\beta(\rho)/\HH(\rho))\mathcal Q_{H_n}(\eta_n)(1+o(1))}}{q_n}.
\]
In packing form (\cref{rem:aper}), the conjectural aperiodic noncontained residue-line packing has size $n^{1+o(1)}$, while the separated quotient-periodic contribution is bounded at the displayed quotient-profile scale.  In particular, if
```
