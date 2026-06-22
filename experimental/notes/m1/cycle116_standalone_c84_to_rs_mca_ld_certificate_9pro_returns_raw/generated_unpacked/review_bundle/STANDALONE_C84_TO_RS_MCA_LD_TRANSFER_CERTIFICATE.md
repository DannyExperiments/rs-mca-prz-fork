# V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE

**Status:** `PROOF` for the finite support-wise MCA / `LD_sw` theorem below; `ROUTE_CUT` for ordinary list decoding, undefined external line-decoding terminology, protocol soundness, and official Proximity Prize promotion.

## 1. Definitions and exact MCA identity

Let `C <= F^D` be a linear code, `|D|=n`, and let `a` be an integer. Define

\[
\operatorname{LD}_{\rm sw}(C,a)
=
\max_{f,g\in F^D}
\#\left\{
 z\in F:
 \begin{array}{l}
 \exists S\subseteq D,\ |S|\ge a,\ (f+zg)|_S\in C|_S,\\
 \nexists c_f,c_g\in C:\ f|_S=c_f|_S,\ g|_S=c_g|_S
 \end{array}
\right\}.
\]

This is the unnormalized numerator of the support-wise MCA definition in `slackMCA_v3.tex` and `RS_disproof_v3.tex`. Since support sizes are integral,

\[
\varepsilon_{\rm mca}(C,\delta)
=
\frac{\operatorname{LD}_{\rm sw}
\left(C,\left\lceil(1-\delta)n\right\rceil\right)}{|F|}.
\]

No ordinary list size occurs in this identity.

## 2. Fixed-jet locator-to-MCA lemma

Let `D subset F`, `|D|=n`, `beta notin D`. Let `J` range over a family `mathcal J` of `j`-subsets of `D`, and put

\[
P_J(X)=\prod_{x\in J}(X-x),\qquad
V_D(X)=\prod_{x\in D}(X-x).
\]

Assume

\[
\deg(P_J-P_{J'})\le j-\sigma
\quad\text{for all }J,J',
\]

where `sigma>=1`, and put

\[
k=n-j-\sigma\ge1,
\qquad C=\operatorname{RS}[F,D,k].
\]

Write

\[
L_J(X)=\frac{V_D(X)}{P_J(X)}
      =\prod_{x\in D\setminus J}(X-x).
\]

Polynomial division at infinity shows that the terms of `L_J` of degrees greater than `k` are independent of `J`; call their common sum `U(X)`. Thus

\[
Q_J(X):=U(X)-L_J(X),\qquad \deg Q_J\le k.
\]

Set

\[
E=X-\beta,
\qquad
f(x)=\frac{U(x)}{x-\beta},
\qquad
g(x)=-\frac1{x-\beta}
\quad(x\in D),
\]

and

\[
z_J=Q_J(\beta)
=U(\beta)-\frac{V_D(\beta)}{P_J(\beta)}
=\alpha+\frac{\lambda}{P_J(\beta)},
\]

where

\[
\alpha=U(\beta),\qquad \lambda=-V_D(\beta)\ne0.
\]

For `S_J=D\setminus J`, define

\[
c_J(X)=\frac{Q_J(X)-z_J}{X-\beta}.
\]

The numerator vanishes at `beta`, and `deg Q_J<=k`, hence `deg c_J<k`. On `S_J`, `L_J=0`, so

\[
c_J=f+z_Jg.
\]

Moreover, `g|_{S_J}` has no degree-`<k` explanation. Otherwise a polynomial `G` of degree `<k` would make

\[
(X-\beta)G(X)+1
\]

a polynomial of degree at most `k` with `|S_J|=k+sigma>k` roots, while its value at `beta` is `1`. This is impossible. Therefore `z_J` is support-wise MCA-bad on the single line `f+zg`, with witness `S_J` and explaining codeword `c_J`.

Since `P_J(beta)` is nonzero and `p mapsto alpha+lambda/p` is injective on `F^*`,

\[
\operatorname{LD}_{\rm sw}(C,k+\sigma)
\ge
\#\{P_J(\beta):J\in\mathcal J\},
\]

and, because `ceil((1-j/n)n)=n-j=k+sigma`,

\[
\varepsilon_{\rm mca}(C,j/n)
\ge
\frac{\#\{P_J(\beta):J\in\mathcal J\}}{|F|}.
\]

This is also a degree-one noncontained residue-line datum with

\[
E=X-\beta,\qquad B=1,\qquad w=U|_D,
\]

because `Q_J congruent z_J (mod E)` and `Q_J=w` on `S_J`.

## 3. Cycle84 native instantiation

Let

\[
F_0=\mathbb F_{17}[X]/(X^{16}+X^8+3),
\qquad
\eta=6X^9,
\qquad
\beta=X+2,
\qquad
D_0=\langle\eta\rangle.
\]

The supplied finite checker verifies `ord(eta)=256`, so `|D_0|=256`.

For each Cycle84 seven-slot tuple `omega`, let `J_omega` be its 113-point co-support. Its seven 16-point slot locators satisfy

\[
L_{t,i,a}(X)=X^{16}+O(X^{10}),
\]

and there is one additional fixed point `1`. Hence

\[
P_\omega(X)
=(X-1)\prod_{t=1}^7L_{t,i_t,a_t}(X)
=X^{113}-X^{112}+O(X^{107}).
\]

The all-336 slot evaluation identities are

\[
L_{t,i,a}(\beta)=3^t u_t(i,a).
\]

Therefore

\[
P_\omega(\beta)
=(\beta-1)3^{1+\cdots+7}\prod_{t=1}^7u_t(i_t,a_t)
=\kappa\Phi(\omega),
\]

where

\[
\kappa=(\beta-1)3^{28}\ne0.
\]

The Cycle84 certificate gives

\[
\#\operatorname{im}\Phi=52{,}747{,}567{,}092.
\]

With

\[
(n,j,\sigma,k)=(256,113,6,137),
\]

the fixed-jet lemma yields

\[
\operatorname{LD}_{\rm sw}
\left(\operatorname{RS}[F_0,D_0,137],143\right)
\ge52{,}747{,}567{,}092,
\]

and

\[
\varepsilon_{\rm mca}
\left(\operatorname{RS}[F_0,D_0,137],113/256\right)
\ge\frac{52{,}747{,}567{,}092}{17^{16}}.
\]

Here `V_D=X^256-1`, and the common high quotient part can be written explicitly as

\[
U=X^{143}+X^{142}+X^{141}+X^{140}+X^{139}+X^{138}.
\]

Thus the displayed affine line is fully explicit.

## 4. Smooth `[512,256]` lift

Since

\[
v_2(17^{16}-1)=8
\]

and `eta` has order `2^8`, it is nonsquare in `F_0`. Let

\[
K=F_0(\theta),\qquad \theta^2=\eta.
\]

Then

\[
K\cong\mathbb F_{17^{32}},
\qquad \operatorname{ord}(\theta)=512,
\qquad H=\langle\theta\rangle=D_0\sqcup\theta D_0.
\]

Choose

\[
R=\{\theta\eta^i:0\le i\le118\},\qquad |R|=119,
\]

and put

\[
A_R(X)=\prod_{r\in R}(X-r).
\]

Extend the native line to words on `H` by

\[
\widetilde f(x)=
\begin{cases}
A_R(x)f(x),&x\in D_0,\\
0,&x\in\theta D_0,
\end{cases}
\qquad
\widetilde g(x)=
\begin{cases}
A_R(x)g(x),&x\in D_0,\\
0,&x\in\theta D_0.
\end{cases}
\]

For every native bad slope `z_J`, the polynomial

\[
\widetilde c_J=A_Rc_J
\]

has degree at most `119+136=255<256` and explains
`widetilde f+z_J widetilde g` on

\[
\widetilde S_J=S_J\cup R,
\qquad |\widetilde S_J|=143+119=262.
\]

Noncontainment is preserved. If a polynomial `G` of degree `<256` explained `widetilde g` on `widetilde S_J`, then `G` would vanish on `R`, hence `G=A_RG_0` with `deg G_0<137`. Division by the nonzero values of `A_R` on `S_J` would make `G_0` explain `g` on `S_J`, contradicting the native noncontainment proof.

Consequently, for

\[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\qquad |H|=512,
\]

one has

\[
\boxed{
\operatorname{LD}_{\rm sw}(C,262)
\ge52{,}747{,}567{,}092
}
\]

and, since

\[
\left\lceil\left(1-\frac{125}{256}\right)512\right\rceil=262,
\]

\[
\boxed{
\varepsilon_{\rm mca}(C,125/256)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}
>2^{-128}.
}
\]

The final inequality is exact because

\[
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6
<52{,}747{,}567{,}092.
\]

## 5. Field ledger

For the lifted row,

\[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}.
\]

The domain `H` generates `K`: `ord_256(17)=16`, so `eta` generates `F_0` over `F_17`, and adjoining `theta` is quadratic. The MCA denominator is `q_line=17^32`, because the source definition ranges `z` over the line field `K`.

`q_chal` is **unset**. No protocol challenge-field identification or protocol reduction is proved or needed for this finite code theorem.

## 6. Scope and route cuts

This certificate proves a finite support-wise MCA bad-slope lower bound and the exactly equivalent `LD_sw` numerator lower bound. It also exhibits one non-code-contained affine line with at least the same number of code-close points.

It does **not** prove an ordinary list-decoding lower bound for the displayed code: the witnesses concern many different received words `f+zg`, not many codewords around one fixed received word. It does **not** prove failure of an external `(delta,a_LD,n+1)` line-decoding predicate, because the attached source states only an implication and leaves the exact line-decoding formulation as an open alignment problem. Any line-decoding notion satisfying

\[
(\delta,a_{\rm LD},n+1)\text{-line-decodable}
\Longrightarrow
\operatorname{LD}_{\rm sw}
\left(C,\left\lceil(1-\delta)n\right\rceil\right)
\le a_{\rm LD}
\]

is ruled out here for every integer `a_LD<52,747,567,092`, but that adapter must be source-pinned separately.

No protocol soundness failure, asymptotic theorem, official Proximity Prize counterpacket, or accepted/deployed prime-field theorem is asserted.

## 7. Verifier

Run:

```bash
python3 verify_c84_to_rs_mca_ld_transfer.py \
  --packet-root /path/to/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro
```

Expected decision:

```text
CYCLE116_C84_TO_RS_MCA_LD_TRANSFER_ANTECEDENTS_VERIFIED
```

The verifier checks the finite Cycle84 receipt, all 336 slot identities, the fixed jet, the scalar `kappa`, the explicit native line constants, nonsquareness and the quadratic extension, the order-512 subgroup and padding partition, and the exact field/radius/target arithmetic. The universal fixed-jet and padding implications are proved above.
