# Cycle 45 random-anchor reserve-lift certificate

This note records the exact source-level statements proved in the accompanying answer. It does not promote them to generated-field, MCA, protocol, SNARK, prize, or final COUNTERPACKET status.

## Ledger

\[
q_{\rm gen}=p,\quad B=\mathbb F_p,\quad F=\mathbb F_{p^2},\quad q_{\rm line}=Q=p^2,
\]
\[
D=\mathbb F_p,\quad A=F[X]/(E),\quad \deg E=t=\sigma,\quad a=k+t,\quad j=p-a.
\]

Let \(b=[B_{\rm num}]_E\ne0\), and for \(T\in\binom Dj\), \(S=D\setminus T\), put
\(R_T(w)=[\operatorname{interp}_S(w)]_E\). Define
\[
L(w)=\#\{T:R_T(w)\in Fb\},\qquad
\nu_w(z)=\#\{T:R_T(w)=zb\},\qquad
M_2(w)=\sum_{z\in F}\nu_w(z)^2.
\]

## Pair-rank lemma

If \(T,T'\) have exchange distance
\(h=|T\setminus T'|=|S\setminus S'|\), then for uniform \(w\in F^D\),
\((R_T(w),R_{T'}(w))\) is uniform on an \(F\)-linear subspace of \(A^2\) of dimension
\[
t+\min(h,t).
\]
Indeed, with \(C=S\cap S'\), the image is
\[
\{(x,y):x-y\in [L_C]_E\,[F[X]_{<h}]_E\}.
\]
The factor \([L_C]_E\) is a unit because \(E\) has no roots on \(D\).

## Exact and bounded moments

Write
\[
N=\binom pj,\qquad c_h=\binom jh\binom ah,\qquad
\Theta=\frac{N}{Q^t},\qquad \mu=\frac{N}{Q^{t-1}}=Q\Theta.
\]
Then
\[
\mathbb E_w L=\mu,
\]
\[
\mathbb E_w M_2
=N\sum_{h=0}^{\min(a,j)}c_h Q^{1-t-\min(h,t)}.
\]
Since \(ja\le p^2/4=Q/4\),
\[
\sum_{h\ge1}c_hQ^{-h}
\le \sum_{h\ge1}\frac{4^{-h}}{(h!)^2}=:C_*<\infty.
\]
Consequently
\[
\mathbb E M_2\le \frac{\mu^2}{Q}+(1+C_*)\mu,
\]
and
\[
\operatorname{Var}(L)\le \mu+C_*Q\mu.
\]
If \(\Theta\to\infty\), then \(L=(1+o(1))\mu\) with probability \(1-o(1)\). Moreover, since
\(M_2-L^2/Q\ge0\),
\[
\mathbb E\left(M_2-\frac{L^2}{Q}\right)
\le (1+C_*)\mu
=o\left(\frac{\mu^2}{Q}\right).
\]
Thus with probability \(1-o(1)\),
\[
M_2\le (1+o(1))\frac{L^2}{Q},
\]
and hence
\[
\#\{z:\nu_w(z)>0\}\ge \frac{L^2}{M_2}=(1-o(1))Q.
\]

## Explicit reserve-scale family

Fix \(\rho\in(0,1)\) and \(0<C<H_2(\rho)/2\). For each sufficiently large odd prime \(p\), let
\[
k=\lfloor\rho p\rfloor,\qquad
t=\frac{Cp}{\log_2p}+o\left(\frac p{\log p}\right),\qquad
j=p-k-t.
\]
Choose \(\alpha\in F\setminus\mathbb F_p\),
\[
E=X^t-\alpha,\qquad B_{\rm num}=1.
\]
Then \(E(d)\ne0\) for every \(d\in\mathbb F_p\), and
\[
\log_2\Theta=(H_2(\rho)-2C+o(1))p\to+\infty.
\]
Choose any anchor in the probability-one asymptotic good set above (equivalently, the lexicographically first such anchor). It satisfies
\[
\#\mathrm{Land}=(1+o(1))\frac{\binom pj}{p^{2(t-1)}},
\]
\[
M_2\le \#\mathrm{Land}+(1+o(1))\frac{\#\mathrm{Land}^2}{p^2},
\]
\[
\#\mathrm{Slopes}=(1-o(1))p^2.
\]
Every landing support is noncontained because \(|S|=k+t\) and \(B_{\rm num}\ne0\): if \(G\in F[X]_{<k}\) agreed with \(-B_{\rm num}/E\) on \(S\), then \(EG+B_{\rm num}\) would have at least \(k+t\) roots but degree at most \(k+t-1\).

## Uniform-L2 falsifiers

1. For \(w\equiv0\), every cosupport lands at slope zero:
\[
\#\mathrm{Land}=N,\quad \nu(0)=N,\quad M_2=N^2,\quad \#\mathrm{Slopes}=1.
\]

2. Let \(w(0)=1\), \(w(d)=0\) for \(d\ne0\). Every \(T\ni0\) has \(R_T(w)=0\), hence
\[
\nu(0)\ge\binom{p-1}{j-1}\ge \frac jp\,#\mathrm{Land}.
\]
If \(t\nmid p-1\), the full-domain interpolant \(W=1-X^{p-1}\) satisfies
\([W]_E\notin F[1]_E\), so this concentration remains off the earlier \(R_0\) locus.
