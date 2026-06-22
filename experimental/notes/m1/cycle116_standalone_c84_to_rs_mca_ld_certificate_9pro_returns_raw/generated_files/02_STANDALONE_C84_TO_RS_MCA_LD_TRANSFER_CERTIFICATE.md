# V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE

**LABEL: PROOF**

## 1. Scope and imported finite clause

This note proves a finite Reed--Solomon support-wise MCA / support-wise line-decoding theorem from the supplied Cycle84 packet. It does not prove an ordinary list-decoding lower bound, a protocol soundness failure, an asymptotic theorem, an accepted/deployed prime-field theorem, or an official Proximity Prize counterpacket.

Write \(\xi\) for the residue class of the field indeterminate and reserve \(Y\) for locator polynomials. Put
\[
F_0=\mathbb F_{17}[\xi]/(\xi^{16}+\xi^8+3),\qquad
\eta=6\xi^9,\qquad \beta=\xi+2.
\]
The supplied finite certificate, verified by `context/cycle84_finite_certificate/verify_certificate.py`, gives for the Cycle84 color shell \(\mathcal P_0\):
\[
|\mathcal P_0|=52{,}747{,}567{,}104,
\quad |\{\Phi(T):T\in\mathcal P_0\}|=52{,}747{,}567{,}092,
\]
with maximum product-fiber size \(2\), exactly twelve double fibers, no fiber of size at least three, and ordered off-diagonal energy \(24\).

## 2. Definitions

For a linear code \(C\le F^D\) and integer \(a\), let \(\operatorname{LD}_{\rm sw}(C,a)\) be the maximum, over lines \(f+zg\), of the number of slopes \(z\in F\) for which there exists \(S\subseteq D\), \(|S|\ge a\), such that \((f+zg)|_S\in C|_S\), while no pair of codewords simultaneously explains \(f|_S\) and \(g|_S\). For \(a=\lceil(1-\delta)|D|\rceil\), the packet's exact bridge gives
\[
\epsilon_{\rm mca}(C,\delta)=\frac{\operatorname{LD}_{\rm sw}(C,a)}{|F|}.
\]

## 3. Fixed-jet locator-to-MCA transfer

### Lemma 1 (fixed-jet locator-to-MCA transfer)

Let \(D\subset F\), \(|D|=n\), let \(\beta\notin D\), and let \(\mathcal J\) be a family of \(j\)-subsets of \(D\). Define
\[
P_J(Y)=\prod_{a\in J}(Y-a),\qquad M_D(Y)=\prod_{a\in D}(Y-a).
\]
Assume \(\sigma\ge1\), \(k=n-j-\sigma\ge1\), and
\[
\deg(P_J-P_{J'})\le j-\sigma\qquad(J,J'\in\mathcal J).
\]
Then one affine line and one degree-one residue datum witness every value
\[
z_J=\alpha+\frac{\lambda}{P_J(\beta)},
\qquad \lambda\ne0,
\]
with support \(S_J=D\setminus J\), \(|S_J|=k+\sigma\). Consequently
\[
\operatorname{LD}_{\rm sw}(\operatorname{RS}[F,D,k],k+\sigma)
\ge |\{P_J(\beta):J\in\mathcal J\}|,
\]
\[
\epsilon_{\rm mca}(\operatorname{RS}[F,D,k],j/n)
\ge \frac{|\{P_J(\beta):J\in\mathcal J\}|}{|F|}.
\]

#### Proof

Put \(L_J=M_D/P_J\). It is monic of degree \(n-j=k+\sigma\). For a monic degree-\(d\) polynomial \(A\), write \(A^*(T)=T^dA(T^{-1})\). The hypothesis says that all \(P_J^*\) are congruent modulo \(T^\sigma\). Since their constant term is one,
\[
(P_J^*)^{-1}\equiv(P_{J'}^*)^{-1}\pmod{T^\sigma}.
\]
Thus \(L_J^*=M_D^*/P_J^*\) is independent of \(J\) modulo \(T^\sigma\), so
\[
\deg(L_J-L_{J'})\le (k+\sigma)-\sigma=k.
\]
Let \(W(Y)\) be the common sum of the terms of \(L_J\) in degrees \(k+1,\ldots,k+\sigma\), and put
\[
Q_J(Y)=W(Y)-L_J(Y),\qquad \deg Q_J\le k.
\]
Take the degree-one residue datum
\[
E(Y)=Y-\beta,\qquad B(Y)=1,
\qquad w=W|_D,
\]
and the single line
\[
f(x)=\frac{W(x)}{x-\beta},\qquad
 g(x)=-\frac1{x-\beta}\qquad(x\in D).
\]
Define
\[
z_J=Q_J(\beta),\qquad
c_J(Y)=\frac{Q_J(Y)-z_J}{Y-\beta}.
\]
Then \(\deg c_J<k\). On \(S_J=D\setminus J\), the support locator \(L_J\) vanishes, so \(Q_J=W\) and
\[
c_J(x)=\frac{W(x)-z_J}{x-\beta}=f(x)+z_Jg(x).
\]
Hence \(c_J\) explains the line point on \(S_J\).

The witness is noncontained. If a polynomial \(G\) of degree less than \(k\) explained \(g\) on \(S_J\), then
\[
(Y-\beta)G(Y)+1
\]
would have degree at most \(k\), at least \(|S_J|=k+\sigma\ge k+1\) roots, and value \(1\) at \(Y=\beta\), a contradiction. Thus no simultaneous explanation of \(f,g\) exists.

Finally,
\[
z_J=W(\beta)-L_J(\beta)
=W(\beta)-\frac{M_D(\beta)}{P_J(\beta)}.
\]
Therefore \(\alpha=W(\beta)\) and \(\lambda=-M_D(\beta)\ne0\). The map \(u\mapsto\alpha+\lambda/u\) is injective on \(F^\times\), proving the count. The residue conditions are also explicit: \(Q_J\equiv z_J\pmod E\), \(Q_J=w\) on \(S_J\), and \(\deg Q_J<k+1\). ∎

## 4. Cycle84 fixed-jet and product-scalar instantiation

### Lemma 2 (Cycle84 support locators)

The explicit model data in `model/cycle68_slot_factorization_checker.py` contain
\[
\begin{aligned}
E_1&=\{0,1,2,3,5,11,12,13\},\\
E_2&=\{0,1,2,3,4,8,9,14\},\\
E_3&=\{0,1,2,4,5,7,11,14\}.
\end{aligned}
\]
For \(i\in\{1,2,3\}\), let
\[
h_i(Z)=\prod_{e\in E_i}(Z-3^e).
\]
Direct multiplication in \(\mathbb F_{17}[Z]\) gives
\[
\begin{aligned}
h_1(Z)&=Z^8+4Z^5+5Z^4+10Z^3+4Z^2+4Z+6,\\
h_2(Z)&=Z^8+9Z^5+5Z^4+12Z^3+14Z^2+13Z+14,\\
h_3(Z)&=Z^8+11Z^5+5Z^3+Z^2+12Z+4.
\end{aligned}
\]
In particular, the \(Z^7\) and \(Z^6\) coefficients vanish in every template.

The packet verifies
\[
\operatorname{ord}(\eta)=256,
\qquad \eta^{16}=3,
\qquad \beta\notin\langle\eta\rangle.
\]
For a state \((i,a)\), put \(B(i,a)=a+E_i\subset\mathbb Z/16\mathbb Z\) and
\[
A(i,a)=\{\eta^{8m}:m\bmod16\in B(i,a)\}\subset\langle\eta^8\rangle.
\]
This set has sixteen elements. For a seven-tuple \(T=((i_t,a_t))_{t=1}^7\), define the Cycle84 co-support
\[
J_T=\{1\}\cup\bigcup_{t=1}^7\eta^tA(i_t,a_t)\subset D_0:=\langle\eta\rangle.
\]
The eight residue classes modulo eight are disjoint, so \(|J_T|=1+7\cdot16=113\). Let
\[
P_T(Y)=\prod_{x\in J_T}(Y-x).
\]
Then
\[
P_T(Y)=Y^{113}-Y^{112}+O(Y^{107}),
\]
where \(O(Y^{107})\) means a polynomial of degree at most \(107\). Moreover
\[
P_T(\beta)=\kappa\Phi(T),
\qquad \kappa=(\beta-1)3^{28}\ne0.
\]

#### Proof

For slot \(t\) and state \((i,a)\), pair the two roots above each \(b\in B(i,a)\):
\[
R_{t,i,a}(Y)
=\prod_{b\in B(i,a)}(Y^2-\eta^{2t}3^b).
\]
The shifted polynomial \(\prod_{b\in B(i,a)}(Z-3^b)\) is a scalar rescaling of \(h_i\), so its \(Z^7,Z^6\) coefficients vanish. Since \(R_{t,i,a}\) contains only even powers, it follows that
\[
R_{t,i,a}(Y)=Y^{16}+O(Y^{10});
\]
all coefficients in degrees \(15,14,13,12,11\) are zero. Hence
\[
\prod_{t=1}^7R_{t,i_t,a_t}(Y)=Y^{112}+O(Y^{106}),
\]
and multiplication by the fixed root \(Y-1\) yields
\[
P_T(Y)=(Y-1)\prod_{t=1}^7R_{t,i_t,a_t}(Y)
=Y^{113}-Y^{112}+O(Y^{107}).
\]

For evaluation at \(\beta\), the model's slot value is
\[
u_t(i,a)=(-1)^a h_i(\beta^2 3^{-a}\eta^{-2t}).
\]
Using \(\eta^{16}=3\) and \(3^8=-1\) in \(\mathbb F_{17}\),
\[
R_{t,i,a}(\beta)=3^t u_t(i,a).
\]
Therefore
\[
P_T(\beta)
=(\beta-1)\prod_{t=1}^7 3^tu_t(i_t,a_t)
=(\beta-1)3^{1+\cdots+7}\Phi(T)
=(\beta-1)3^{28}\Phi(T).
\]
The scalar is nonzero. ∎

### Corollary 2.1 (native row)

Let
\[
C_0=\operatorname{RS}[F_0,D_0,137].
\]
Here \(n=256,j=113,\sigma=6,k=137\), and \(S_T=D_0\setminus J_T\) has size \(143\). The common top part of \((Y^{256}-1)/P_T(Y)\) is
\[
W_0(Y)=Y^{143}+Y^{142}+Y^{141}+Y^{140}+Y^{139}+Y^{138}.
\]
Thus one explicit native line is
\[
f_0(x)=\frac{W_0(x)}{x-\beta},
\qquad g_0(x)=-\frac1{x-\beta},
\]
with slopes
\[
z_T=W_0(\beta)-\frac{\beta^{256}-1}{P_T(\beta)}
=W_0(\beta)-\frac{\beta^{256}-1}{\kappa\Phi(T)}.
\]
For each \(T\), if \(L_T=(Y^{256}-1)/P_T\), put
\[
Q_T=W_0-L_T,
\qquad c_T(Y)=\frac{Q_T(Y)-Q_T(\beta)}{Y-\beta}.
\]
Then \(\deg c_T<137\) and \(c_T=f_0+z_Tg_0\) on \(S_T\). The direction \(g_0\) has no degree-less-than-137 explanation on \(S_T\). Since the reciprocal-affine slope map has exactly the Cycle84 product fibers,
\[
\operatorname{LD}_{\rm sw}(C_0,143)\ge52{,}747{,}567{,}092,
\]
\[
\epsilon_{\rm mca}(C_0,113/256)
\ge\frac{52{,}747{,}567{,}092}{17^{16}}.
\]

## 5. GRS/RS normalization

### Lemma 3 (diagonal normalization)

For nonzero coordinate multipliers \(v_x\), the map \(u_x\mapsto v_x^{-1}u_x\) sends \(\operatorname{GRS}_v[F,D,k]\) to \(\operatorname{RS}[F,D,k]\), sends a line \(f+zg\) to a line with the same slope parameter, and preserves support equality and simultaneous explainability. Therefore it preserves \(\operatorname{LD}_{\rm sw}\) and the MCA bad-slope set exactly.

No normalization is needed in Corollary 2.1: the construction is already an ordinary RS construction.

## 6. Smooth agreement-padding lift

### Lemma 4 (agreement-padding lift)

Let \(F\subseteq K\), \(D\subset F\), and suppose a line \(f+zg\) for \(\operatorname{RS}[F,D,k_0]\) has a set \(\Gamma\subseteq F\) of bad slopes, with explaining polynomials \(p_z\in F[Y]_{<k_0}\) on supports \(S_z\). Let \(A,R\subset K\) be disjoint from each other and from \(D\), with \(|A|=h\), and put
\[
A_*(Y)=\prod_{a\in A}(Y-a).
\]
On \(D'=D\sqcup A\sqcup R\), define
\[
\widetilde f(x)=
\begin{cases}A_*(x)f(x),&x\in D,\\0,&x\in A\cup R,
\end{cases}
\qquad
\widetilde g(x)=
\begin{cases}A_*(x)g(x),&x\in D,\\0,&x\in A\cup R.
\end{cases}
\]
Then every \(z\in\Gamma\) is bad for \(\operatorname{RS}[K,D',k_0+h]\) on \(S_z\cup A\), provided the original noncontainment remains valid against \(K\)-polynomials. An explaining polynomial is \(A_*p_z\). If degree-less-than-\(k_0+h\) polynomials \(F_1,G_1\) simultaneously explained \(\widetilde f,\widetilde g\) on \(S_z\cup A\), both would vanish on \(A\), hence
\[
F_1=A_*F_0,\qquad G_1=A_*G_0,
\qquad \deg F_0,\deg G_0<k_0,
\]
and division on \(S_z\) would contradict native noncontainment. Thus agreement and noncontainment are preserved, and the slope set is unchanged.

### Corollary 4.1 (smooth \([512,256]\) row)

Since \(17^{16}-1\) has 2-adic valuation eight and \(\eta\) has order \(256\), \(\eta\) is a nonsquare in \(F_0\). Let
\[
K=F_0(\theta),\qquad \theta^2=\eta.
\]
Then \(K\cong\mathbb F_{17^{32}}\), \(\theta^{256}=-1\), \(\theta^{512}=1\), and \(\operatorname{ord}(\theta)=512\). Put
\[
H=\langle\theta\rangle=D_0\sqcup\theta D_0.
\]
Choose
\[
A=\{\theta\eta^i:0\le i\le118\},\qquad |A|=119,
\]
\[
R=\{\theta\eta^i:119\le i\le255\},\qquad |R|=137.
\]
Then \(D_0\sqcup A\sqcup R=H\). Applying Lemma 4 with \(k_0=137\) and \(h=119\) gives
\[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\qquad |H|=512,
\]
with the same \(52{,}747{,}567{,}092\) slopes bad on supports of size
\[
143+119=262.
\]
Native noncontainment remains valid over \(K\) by the same root-count proof for \(g_0=-1/(Y-\beta)\). Therefore
\[
\operatorname{LD}_{\rm sw}(C,262)\ge52{,}747{,}567{,}092,
\]
\[
\epsilon_{\rm mca}(C,125/256)
\ge\frac{52{,}747{,}567{,}092}{17^{32}}.
\]

There is also a direct fixed-root normalization of the smooth row. The complement of \(S_T\cup A\) in \(H\) is \(J_T\cup R\), with locator
\[
P'_T=P_RP_T,
\qquad \deg P'_T=250.
\]
Since \(\deg(P_T-P_{T'})\le107\),
\[
\deg(P'_T-P'_{T'})\le137+107=244=250-6,
\]
and
\[
P'_T(\beta)=P_R(\beta)\kappa\Phi(T),\qquad P_R(\beta)\ne0.
\]
Lemma 1 therefore also constructs a degree-one residue datum directly on \(H\), with \(n=512,j=250,\sigma=6,k=256\), the same support size \(262\), and the same number of slopes.

## 7. Field and target ledger

The order computations are
\[
\operatorname{ord}_{256}(17)=16,
\qquad \operatorname{ord}_{512}(17)=32.
\]
Thus the smallest fields generated by \(D_0\) and \(H\) are respectively \(F_0\) and \(K\). For the smooth row,
\[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}.
\]
No protocol challenge field is part of this theorem; under a same-field protocol instantiation one may additionally set \(q_{\rm chal}=17^{32}\), but \(q_{\rm chal}\) is not used as a second denominator.

Exactly,
\[
17^{32}=2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361,
\]
\[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
\]
Since \(52{,}747{,}567{,}092>6\),
\[
\frac{52{,}747{,}567{,}092}{17^{32}}>2^{-128}.
\]
Numerically the ratio is approximately \(2^{-95.1804}\).

## 8. Final theorem

There exists a smooth multiplicative-subgroup Reed--Solomon row
\[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],\qquad |H|=512,
\]
and one affine line over \(\mathbb F_{17^{32}}\) with at least \(52{,}747{,}567{,}092\) distinct support-wise noncontained slopes, each having an explaining degree-less-than-256 codeword on a support of size \(262\). Consequently
\[
\boxed{\operatorname{LD}_{\rm sw}(C,262)\ge52{,}747{,}567{,}092},
\]
\[
\boxed{\epsilon_{\rm mca}(C,125/256)
\ge\frac{52{,}747{,}567{,}092}{17^{32}}>2^{-128}}.
\]

This is a finite, paper-facing support-wise MCA / \(\operatorname{LD}_{\rm sw}\) theorem. It is not an ordinary list-decoding lower bound, a protocol soundness failure, an asymptotic theorem, an accepted/deployed prime-field theorem, or an official Proximity Prize counterpacket.

## 9. Verifier status

The companion script `verify_c84_to_rs_mca_ld_transfer.py` verifies every finite instantiation clause used above: the existing occupancy certificate, the three template factorizations, all 336 degree-16 slot locators and their missing top coefficients, all 336 slot evaluation scalars, the nonzero \(\kappa\), the order/nonsquare/quadratic-extension facts, the 512-element subgroup and its \(119+137\) partition, and the exact integer ledger. It deliberately does not pretend to machine-prove Lemmas 1, 3, or 4; those are the short symbolic proofs in this note.

One editorial inconsistency should be corrected when the packet is republished: `STANDALONE_FINITE_CERTIFICATE.md` says `gamma = X+1` is primitive, while `data/slot_logs.json` and `verify_certificate.py` use the primitive generator `(2,1)=X+2=beta`. The executed verifier confirms the latter. This naming typo does not affect the occupancy theorem or the transfer, but it should not remain in a reviewer-facing bundle.
