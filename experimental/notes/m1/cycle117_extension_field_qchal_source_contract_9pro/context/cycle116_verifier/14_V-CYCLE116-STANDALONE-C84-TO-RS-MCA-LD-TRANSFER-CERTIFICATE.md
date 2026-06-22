# V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE

## LABEL

**AUDIT / PROOF**

## EXECUTIVE VERDICT

There is no fatal algebraic gap in the proposed finite transfer.  From the accepted Cycle84 finite product certificate and the explicit slot-factorization data in the packet, one obtains a single affine Reed--Solomon line with at least

\[
N=52{,}747{,}567{,}092
\]

distinct support-wise MCA-bad slopes.  The native row is

\[
\operatorname{RS}[\mathbb F_{17^{16}},\langle\eta\rangle,137]
\]

at agreement size \(143\).  A common agreement-padding construction then gives the smooth row

\[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\qquad H=\langle\theta\rangle,
\qquad |H|=512,
\]

at agreement size \(262\), with

\[
\operatorname{LD}_{\rm sw}(C,262)\ge N,
\qquad
\epsilon_{\rm mca}\!\left(C,\frac{125}{256}\right)
\ge \frac{N}{17^{32}}>2^{-128}.
\]

This is a finite support-wise MCA / \(\operatorname{LD}_{\rm sw}\) theorem.  It is not an ordinary list-decoding lower bound with numerator \(N\), not a protocol soundness failure, not an asymptotic theorem, not an official Proximity Prize counterpacket, and not an accepted/deployed prime-field theorem.

The accompanying script `verify_cycle116_transfer_hypotheses.py` is a reviewer-facing wrapper for the finite and algebraic hypotheses.  It fail-closes on `REVIEW_MANIFEST.sha256`, replays the existing Cycle84 verifier, checks all 336 bridge identities, and verifies the smooth lift and security arithmetic.  The generic fixed-jet and padding implications are the symbolic lemmas proved below.

## STANDALONE CERTIFICATE SECTION

### 1. Support-wise numerator

For a linear code \(C\subseteq F^D\), \(|D|=n\), define \(\operatorname{LD}_{\rm sw}(C,a)\) as the maximum over affine lines \(f+zg\), \(z\in F\), of the number of slopes for which there exists \(S\subseteq D\), \(|S|\ge a\), such that

\[
(f+zg)|_S\in C|_S
\]

but no pair \(c_f,c_g\in C\) simultaneously satisfies

\[
f|_S=c_f|_S,
\qquad
g|_S=c_g|_S.
\]

By the source definition,

\[
\epsilon_{\rm mca}(C,\delta)
=\frac{\operatorname{LD}_{\rm sw}(C,\lceil(1-\delta)n\rceil)}{|F|}.
\]

This identity is definitional.  \(\operatorname{LD}_{\rm sw}\) is not the ordinary worst-case Reed--Solomon list size.

### 2. Fixed-jet locator-to-MCA theorem

Let \(F\) be a finite field, \(D\subset F\) a set of \(n\) distinct points, and \(\beta\in F\setminus D\).  Let \(\mathcal J\) be a nonempty family of \(j\)-subsets of \(D\), with monic locators

\[
P_J(X)=\prod_{a\in J}(X-a).
\]

Let \(\sigma\ge1\), assume \(j+\sigma\le n\), and suppose

\[
\deg(P_J-P_{J'})\le j-\sigma
\qquad(J,J'\in\mathcal J).
\]

Put

\[
r=j+\sigma,
\qquad k=n-r,
\qquad C=\operatorname{RS}[F,D,k].
\]

Then there is one affine line \(u_z=f+zg\) such that, for every \(J\in\mathcal J\),

\[
z_J=-\frac1{P_J(\beta)}
\]

is support-wise MCA-bad with witness support

\[
S_J=D\setminus J,
\qquad |S_J|=n-j=k+\sigma.
\]

Equivalently, the slope has the required common reciprocal-affine form

\[
z_J=\alpha+\frac{\lambda}{P_J(\beta)}
\]

with \(\alpha=0\) and \(\lambda=-1\).  A common invertible affine reparameterization gives any other common pair \((\alpha,\lambda)\) with \(\lambda\ne0\).

Consequently,

\[
\operatorname{LD}_{\rm sw}(C,k+\sigma)
\ge \#\{P_J(\beta):J\in\mathcal J\},
\]

and

\[
\epsilon_{\rm mca}\!\left(C,\frac jn\right)
\ge
\frac{\#\{P_J(\beta):J\in\mathcal J\}}{|F|}.
\]

The same construction has one degree-one residue datum

\[
E=X-\beta,
\qquad B=V_D(\beta),
\qquad V_D(X)=\prod_{a\in D}(X-a).
\]

### 3. Cycle84 native instantiation

Let

\[
F_0=\mathbb F_{17}[X]/(X^{16}+X^8+3),
\qquad \eta=6X^9,
\qquad \beta=X+2,
\qquad D_0=\langle\eta\rangle.
\]

The packet verifies

\[
|D_0|=256,
\qquad \beta\notin D_0.
\]

Use

\[
\begin{aligned}
E_1&=\{0,1,2,3,5,11,12,13\},\\
E_2&=\{0,1,2,3,4,8,9,14\},\\
E_3&=\{0,1,2,4,5,7,11,14\},
\end{aligned}
\]

and \(B_{i,a}=a+E_i\pmod {16}\).  Put

\[
Y_{i,a}=\{y\in\langle\eta^8\rangle:
 y^2\in\{3^b:b\in B_{i,a}\}\}.
\]

For a seven-state tuple \(\tau=((i_t,a_t))_{t=1}^7\), define

\[
T_\tau=\{1\}\cup\bigcup_{t=1}^7\eta^tY_{i_t,a_t}.
\]

The eight cosets \(\eta^t\langle\eta^8\rangle\), \(0\le t\le7\), are disjoint; \(|Y_{i,a}|=16\); and the 48 sets \(B_{i,a}\) are distinct.  Hence

\[
|T_\tau|=113,
\]

and the tuple-to-support map is injective.

For each block set

\[
R_{t,i,a}(Z)
=\prod_{b\in B_{i,a}}(Z^2-\eta^{2t}3^b).
\]

The three root polynomials \(\prod_{e\in E_i}(Y-3^e)\) have zero coefficients at \(Y^7\) and \(Y^6\).  Therefore every block locator satisfies

\[
R_{t,i,a}(Z)=Z^{16}+O(Z^{10}).
\]

It follows that the full locator

\[
P_\tau(Z)=\prod_{x\in T_\tau}(Z-x)
\]

satisfies the exact degree statement

\[
\boxed{
P_\tau(Z)=Z^{113}-Z^{112}+R_\tau(Z),
\qquad \deg R_\tau\le107.
}
\]

Thus the common-jet theorem applies with

\[
(n,j,\sigma,k)=(256,113,6,137).
\]

The packet's 336 exact slot identities give

\[
R_{t,i,a}(\beta)=3^t u_t(i,a).
\]

Hence, with \(\Phi(\tau)=\prod_{t=1}^7u_t(i_t,a_t)\),

\[
\begin{aligned}
P_\tau(\beta)
&=(\beta-1)\prod_{t=1}^7R_{t,i_t,a_t}(\beta)\\
&=(\beta-1)3^{1+\cdots+7}\Phi(\tau)\\
&=(\beta-1)3^{28}\Phi(\tau)\\
&=4(\beta-1)\Phi(\tau).
\end{aligned}
\]

Thus

\[
\boxed{
P_\tau(\beta)=\kappa\Phi(\tau),
\qquad \kappa=4(\beta-1)\ne0.
}
\]

The Cycle84 shell is precisely the family on which the finite census was performed.  Its color condition has already been paid by that restriction; it is not an additional MCA quotient or denominator.

The accepted finite receipt gives

\[
\#\Phi(\mathcal P_0)=52{,}747{,}567{,}092.
\]

Since multiplication by \(\kappa\ne0\) and inversion are bijections on \(F_0^\times\), the fixed-jet theorem yields

\[
\boxed{
\operatorname{LD}_{\rm sw}
\bigl(\operatorname{RS}[F_0,D_0,137],143\bigr)
\ge52{,}747{,}567{,}092
}
\]

and

\[
\boxed{
\epsilon_{\rm mca}
\left(\operatorname{RS}[F_0,D_0,137],\frac{113}{256}\right)
\ge\frac{52{,}747{,}567{,}092}{17^{16}}.
}
\]

The packet-indexed slope fibers have 12 double fibers and no packet fiber of size at least three.  This does not assert that no outside support produces an additional witness for one of those slopes.

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

First extend the native line and code from \(F_0\) to \(K\).  Noncontainment does not disappear: if a degree-\(<137\) polynomial over \(K\) agreed with an \(F_0\)-valued native word on 137 points of \(F_0\), interpolation on those points would force all its coefficients into \(F_0\).

Let

\[
L_A(X)=\prod_{a\in A}(X-a).
\]

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
\]

## PROOF DETAILS

### A. Construction of one common affine line

Let \(V_D(X)=\prod_{a\in D}(X-a)\), and let \(H_C\) be the \(r\times n\) parity-check matrix whose column at \(a\in D\) is

\[
h_a=V_D'(a)^{-1}v(a),
\qquad
v(a)=(1,a,\ldots,a^{r-1})^{\mathsf T}.
\]

Its kernel is \(C=\operatorname{RS}[F,D,k]\).  For \(J\in\mathcal J\), put

\[
W_J=\operatorname{span}\{h_a:a\in J\}.
\]

Identifying coefficient vectors with polynomials of degree \(<r\),

\[
W_J^\perp=P_JF[X]_{<\sigma}.
\]

Let \(\operatorname{top}_\sigma(Q)\) denote the top \(\sigma\) coefficients of \(Q\in F[X]_{<r}\).  The map

\[
M_J:A\longmapsto\operatorname{top}_\sigma(P_JA),
\qquad A\in F[X]_{<\sigma},
\]

is independent of \(J\) by the common-jet hypothesis, and is invertible because \(P_J\) is monic.  Call the common map \(M\).  Define

\[
\ell(Q)=\bigl(M^{-1}(\operatorname{top}_\sigma Q)\bigr)(\beta).
\]

Choose \(y_0\in F^r\) representing \(\ell\) under coefficient pairing, and let

\[
y_1=v(\beta).
\]

For \(Q=P_JA\in W_J^\perp\),

\[
\langle Q,y_0+zy_1\rangle
=A(\beta)(1+zP_J(\beta)).
\]

At \(z_J=-P_J(\beta)^{-1}\), this vanishes for every \(A\), so

\[
y_0+z_Jy_1\in W_J.
\]

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

## VERIFIER / CHECKER REQUIREMENTS

The supplied checker `verify_cycle116_transfer_hypotheses.py` performs the following deterministic checks using only the packet:

1. Verifies all 25 files pinned by `REVIEW_MANIFEST.sha256` before importing packet code.  The older inner `MANIFEST.sha256` is not the review root because it includes a mutable `__pycache__` entry and stale pre-review hashes.
2. Runs the existing Cycle84 verifier and checks
   \(m_{\max}=2\), occupancy \(N\), \(D=24\), and 12 double fibers.
3. Checks irreducibility of \(X^{16}+X^8+3\), \(\eta^{16}=3\), \(\operatorname{ord}(\eta)=256\), \(\beta\notin D_0\), and that \(\eta\) is nonsquare.
4. Recomputes the three \(E_i\) root polynomials and their zero \(Y^7,Y^6\) coefficients.
5. Checks all 336 block locators satisfy both the degree gap and
   \(R_{t,i,a}(\beta)=3^tu_t(i,a)\).
6. Checks the 48 state sets are distinct and their colors equal their exponent sums.
7. Checks the symbolic degree support that yields
   \(P_T=X^{113}-X^{112}+O(X^{107})\).
8. Constructs \(K=F_0[\theta]/(\theta^2-\eta)\), checks \(\operatorname{ord}(\theta)=512\), and enumerates the 512 distinct points of \(H\).
9. Checks the \(D_0\sqcup A\sqcup R\) partition and all dimension/agreement arithmetic.
10. Checks \(\lfloor17^{32}/2^{128}\rfloor=6\) and the strict numerator inequality.

The checker intentionally reports that the finite bundle uses two primitive-log gauges: the prose/master explicit witness uses \(X+1\), while `slot_logs.json` and the compact/full census use \(X+2=\beta\).  It verifies that both are primitive and that the two based logarithms

\[
\log_{X+1}(v)=814{,}364{,}899{,}710{,}808{,}391,
\qquad
\log_{X+2}(v)=10{,}842{,}140{,}456{,}386{,}731{,}719
\]

exponentiate to the same displayed double-fiber field product \(v\).  Product equality and occupancy are invariant under this consistent gauge change, so this is not a theorem failure.  The prose line claiming one undifferentiated generator must nevertheless be corrected; no numerical logarithm should be quoted without its base.

The exact missing checker clause in the original packet is the bridge assertion, for every one of the 336 states,

\[
R_{t,i,a}(Z)=\prod_{b\in a+E_i}(Z^2-\eta^{2t}3^b),
\quad
\deg(R_{t,i,a}-Z^{16})\le10,
\quad
R_{t,i,a}(\beta)=3^tu_t(i,a).
\]

Once this clause is combined with the generic fixed-jet lemma above, no enumeration of all \(48^7\) locators is required.

## FIELD AND PARAMETER LEDGER

| Quantity | Native row | Smooth lifted row |
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

## NEXT EXACT STEP

Package the theorem note and checker together and correct the stale prose generator line.  The checker already fail-closes on the 25-file `REVIEW_MANIFEST.sha256` root and explicitly verifies both based logarithms.  For official-prize promotion, the next lemma is not algebraic: it is an authority-pinned admission/source/challenge-field contract specifying whether this extension-field row is admitted and what, if any, endpoint, periodic, affine-color, or retained-event processing applies.
