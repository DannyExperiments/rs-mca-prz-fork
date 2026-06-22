LABEL: **BANKABLE_LEMMA — PRIZE_FAMILY_EMBEDDING_PROVED at finite-row level; ROUTE_CUT for the Cycle88/89 (q=17^{48}) frontier transfer**

EXECUTIVE VERDICT:

The Cycle85 one-copy construction already uses a genuine smooth multiplicative domain:
[
D_0=\langle \eta\rangle\le \mathbb F_{17^{16}}^\times,\qquad |D_0|=256.
]
Its defect is not the domain. Its defects are the non-prize rate (137/256), the small line field (17^{16}), and dependence on the separate Cycle84-to-Cycle85 fixed-jet transfer.

There is, however, an exact code-theoretic lift of the Cycle85 row to
[
\operatorname{RS}!\left[\mathbb F_{17^{32}},H,256\right],
\qquad |H|=512,
]
where (H) is a power-of-two multiplicative subgroup and the rate is exactly (1/2). The lifted line has at least
[
52,747,567,092
]
support-wise noncontained bad slopes at agreement size (262), hence
[
\operatorname{LD}*{\rm sw}(C,262)\ge 52,747,567,092
]
and
[
\epsilon*{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{52,747,567,092}{17^{32}}

> 2^{-128}.
> ]

This is an official-family, paper-facing finite RS-MCA/line-decoding row. It is not a Proximity Prize frontier advance: at (q_{\rm line}=17^{32}), the target numerator is only (6), while the generic tangent floor already gives (250) bad slopes.

By contrast, the Cycle88/89 ([464,232]) row over (\mathbb F_{17^{48}}) is an arbitrary-domain RS/GRS row. It cannot be literally embedded into a smooth multiplicative domain over the same field: every power-of-two subgroup of (\mathbb F_{17^{48}}^\times) has order at most (256). The (17^{48}) numerator therefore remains non-prize-facing unless a new smooth-domain re-realization theorem is proved.

Confidence: **high** for the lifting theorem, GRS invariance, and (17^{48}) field obstruction; **moderate-high** for the final Cycle84 corollary because the packet supplies the Cycle85 bridge as an audited banked claim rather than its complete raw proof.

EXACT THEOREM OR OBSTRUCTION:

### Smooth agreement-padding transfer theorem

Let (F\subseteq K), let (D\subseteq F), and suppose a line in
[
C_0=\operatorname{GRS}_{v}[F,D,k_0]
]
has a set (\Gamma\subseteq F) of distinct support-wise MCA-bad slopes. Suppose that for every (z\in\Gamma) there is a witness support (S_z\subseteq D), (|S_z|\ge a_0).

Let (A,R\subseteq K) be disjoint from each other and from (D), with (|A|=h). Put
[
L_A(X)=\prod_{\alpha\in A}(X-\alpha).
]

After diagonal GRS-to-RS normalization, write the original line as (f+zg) and let (p_z\in K[X]_{<k_0}) explain it on (S_z). On
[
D'=D\sqcup A\sqcup R
]
define
[
\widetilde f(x)=
\begin{cases}
L_A(x)f(x),&x\in D,\
0,&x\in A\cup R,
\end{cases}
\qquad
\widetilde g(x)=
\begin{cases}
L_A(x)g(x),&x\in D,\
0,&x\in A\cup R.
\end{cases}
]

Then every (z\in\Gamma) is support-wise MCA-bad for the single line
[
\widetilde f+z\widetilde g
]
in
[
C'=\operatorname{RS}[K,D',k_0+h],
]
with witness support
[
S'_z=S_z\cup A,\qquad |S'_z|\ge a_0+h.
]

Consequently,
[
\operatorname{LD}_{\rm sw}(C',a_0+h)\ge |\Gamma|.
]

### Cycle85 instantiation

Use the banked Cycle85 row:
[
F_0=\mathbb F_{17^{16}},\quad
D_0=\langle\eta\rangle,\quad
(n_0,k_0,\sigma_0)=(256,137,6),
]
with
[
a_0=k_0+\sigma_0=143,\qquad
|\Gamma|=52,747,567,092.
]

The packet’s finite model identifies (\eta=6X^9) as an element of order (256). Let
[
K=F_0(\theta),\qquad \theta^2=\eta.
]
Because (\eta) generates the (2)-Sylow subgroup of (F_0^\times), it is not a square in (F_0), so
[
K\cong\mathbb F_{17^{32}},
\qquad \operatorname{ord}(\theta)=512.
]
Set
[
H=\langle\theta\rangle
=D_0\sqcup\theta D_0.
]

Choose, explicitly,
[
A={\theta\eta^i:0\le i\le118},\qquad |A|=119,
]
and
[
R={\theta\eta^i:119\le i\le255},\qquad |R|=137.
]

Then
[
D_0\sqcup A\sqcup R=H,
]
and the transfer theorem gives
[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
]
with
[
n=512,\quad k=256,\quad \rho=\frac12,
]
and agreement size
[
a=143+119=262=k+6.
]
Thus
[
\delta=1-\frac{262}{512}=\frac{125}{256}.
]

The exact conclusion is
[
\boxed{
\operatorname{LD}*{\rm sw}(C,262)
\ge 52,747,567,092
}
]
and
[
\boxed{
\epsilon*{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{52,747,567,092}{17^{32}}

> 2^{-128}.
> }
> ]

No ordinary list-size lower bound follows: the construction gives many close points on one line, not many codewords close to one fixed received word.

PROOF / DISPROOF / ROUTE CUT:

### Proof of the smooth lift

1. **Cycle85’s domain is smooth.**
   The packet checker constructs all Cycle84 complement supports inside (\langle\eta\rangle). Its construction of (\eta) forces (\eta^{256}=1) and (\eta^{128}\ne1), so (\operatorname{ord}(\eta)=256). Hence the one-copy evaluation domain is a power-of-two multiplicative subgroup.

2. **GRS causes no loss.**
   For nonzero coordinate multipliers (v_x), the map
   [
   (u_x)*{x\in D}\longmapsto (v_x^{-1}u_x)*{x\in D}
   ]
   maps (\operatorname{GRS}_v(D,k)) to (\operatorname{RS}(D,k)). It preserves every support, Hamming equality, simultaneous explainability, and the line parameter (z). Therefore list sizes, support-wise line-decoding numerators, and MCA bad-slope sets are unchanged exactly.

3. **Scalar extension causes no loss.**
   A word and evaluation set defined over (F_0) cannot acquire a new degree-(<137) explanation merely by passing to (K). If a (K)-polynomial explains the word on at least (137) points of (F_0), interpolation on any (137) of those points gives the same polynomial with coefficients in (F_0).

4. **Agreement padding preserves noncontainment.**
   For each original explaining polynomial (p_z), use
   [
   \widetilde p_z=L_Ap_z.
   ]
   Since (\deg L_A=119) and (\deg p_z<137),
   [
   \deg\widetilde p_z<256.
   ]
   It agrees with the lifted line on (S_z), and both sides vanish on (A).

   If degree-(<256) polynomials (F,G) simultaneously explained (\widetilde f,\widetilde g) on (S_z\cup A), then both (F) and (G) would vanish on all (119) points of (A). Hence
   [
   F=L_AF_0,\qquad G=L_AG_0,
   ]
   with (\deg F_0,\deg G_0<137). Dividing on (S_z) would give simultaneous explanations of the original (f,g), contradicting Cycle85 noncontainment.

5. **The added set (R) is harmless.**
   No witness support uses (R). Adding those coordinates changes the ambient domain and radius but neither agreement nor noncontainment on (S_z\cup A).

### Route cut for Cycle88/89

Let
[
L=\mathbb F_{17^{48}}.
]
By LTE,
[
v_2(17^{48}-1)=v_2(17-1)+v_2(48)=4+4=8.
]
Therefore every power-of-two subgroup or coset in (L^\times) has order at most
[
2^8=256.
]

Hence the ([464,232]) Cycle88/89 row cannot itself be a smooth multiplicative subgroup/coset row over (L).

There is also no proper extension of (L) inside the prize cap that could contain the same field data. Any finite field containing (L) has size (17^d) with (48\mid d). But
[
17^d<2^{256}
\quad\Longrightarrow\quad
d<63,
]
so the only admissible multiple of (48) is (d=48) itself. The next containing field, (\mathbb F_{17^{96}}), exceeds (2^{256}).

Thus a literal field-preserving embedding of the (464)-point row into a larger smooth subgroup is impossible within the stated field cap. A different-field or compressed-domain construction would be a new theorem, not an embedding of the existing row.

FIELD AND PARAMETER LEDGER:

| Row             | Domain and code                             |                         Parameters | Field ledger                                                                                              |                   Bad numerator |                 (2^{-128}) target | Status                                     |
| --------------- | ------------------------------------------- | ---------------------------------: | --------------------------------------------------------------------------------------------------------- | ------------------------------: | --------------------------------: | ------------------------------------------ |
| Cycle85 native  | (D_0=\langle\eta\rangle), RS/GRS            | (n=256,k=137,a=143,\delta=113/256) | (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}); (q_{\rm chal}=17^{16}) only in the same-field experiment |              (N=52,747,567,092) | (\lfloor17^{16}/2^{128}\rfloor=0) | Smooth domain, non-prize rate              |
| New smooth lift | (H=\langle\theta\rangle), ordinary RS       | (n=512,k=256,a=262,\delta=125/256) | (q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_{\rm chal}=17^{32})                                              |              (N=52,747,567,092) | (\lfloor17^{32}/2^{128}\rfloor=6) | Official-family finite MCA/LD row          |
| Cycle88/89      | arbitrary 464-point domain, GRS (\simeq) RS | (n=464,k=232,a=238,\delta=113/232) | Conditionally all (=17^{48})                                                                              | (1,391,152,917,379,006,070,784) |     (338,617,018,271,848,945,628) | Arbitrary-domain only; no smooth embedding |

For the new lift,
[
17^{32}
=======

2,367,911,594,760,467,245,844,106,297,320,951,247,361,
]
and
[
\frac{52,747,567,092}{17^{32}}
\approx 2^{-95.18}.
]

The target is being divided by (q_{\rm line}), not by an unrelated larger verifier field. If a protocol sampled the line parameter from (17^{48}), the (17^{32}) numerator would have to be divided by (17^{48}); the displayed (2^{-128}) conclusion would no longer follow.

SELF-AUDIT:

1. **Exact implication proved and not proved.**
   Proved:
   [
   \text{Cycle85 one-copy RS/GRS MCA row}
   \Longrightarrow
   \text{smooth }[512,256]\text{ RS MCA/LD row over }\mathbb F_{17^{32}}.
   ]
   Not proved directly from the standalone Cycle84 certificate:
   [
   \text{Cycle84 product occupancy}
   \Longrightarrow
   \text{Cycle85 one common support-wise MCA line}.
   ]
   That arrow still relies on the audited fixed-six-jet, (\gamma_T=1), reciprocal-affine slope contract.

2. **Claim level.**
   The new result is an official-family, paper-facing finite RS-MCA/support-wise-line-decoding theorem, conditional on the supplied Cycle85 banked transfer. It is not a prize-frontier proof. The generic tangent floor at this row is already
   [
   \frac{\lfloor\delta n\rfloor}{q}
   =\frac{250}{17^{32}}

   > 2^{-128},
   > ]
   > so the target was already lost without Cycle84.

3. **First possible failure line.**
   Starting from the standalone Cycle84 file, the first unsupported line is the Cycle84-to-Cycle85 identification:
   [
   T\mapsto
   \bigl(S_T,p_T,z_T=a+b/P_T(\beta)\bigr)
   ]
   on one common line, with (b\ne0), fixed (\gamma_T=1), correct support size, and noncontainment. Once that contract holds, the smooth lift above has no further gap.

4. **Use of the fields and target.**
   The new row uses
   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=q_{\rm chal}=17^{32}.
   ]
   The (2^{-128}) denominator is therefore correct. For Cycle88/89, the audited equality of all four fields with (17^{48}) is correct only for the arbitrary-domain row. The base field (17^{16}) must not be used as its MCA denominator.

5. **Possible numerator losses.**
   In the new lift there is no new quotient, projective, same-slope, endpoint, tangent, or affine-normalization loss:

   * slopes are unchanged rather than remapped;
   * scalar extension preserves distinct field elements;
   * noncontainment is proved by divisibility by (L_A);
   * support size is exactly (262);
   * no endpoint is removed;
   * tangent slopes are not included in the claimed (N);
   * GRS scaling is an exact isometry.

   Quotient-periodic structure may classify the row as belonging to a known lower/failure branch. It does not remove slopes from the raw support-wise MCA definition. No claim about the aperiodic packing number is made.

   For any attempted transplant of the Cycle88/89 numerator to a smooth domain, all these losses must be rechecked from zero. The arbitrary-domain audit does not protect the numerator after changing the domain.

6. **What converts this to full proof or frontier proof.**
   Full proof of the displayed ([512,256]) row requires the exact Cycle85 source contract below. A frontier-relevant (17^{48}) result requires a new compressed smooth-domain construction; the (464)-point row cannot simply be embedded.

NEXT EXACT STEP:

First, close the one remaining dependency:

```text
V-CYCLE115-C84-TO-C85-FIXED-JET-LINE-CONTRACT
```

It must emit and verify, for the Cycle84 packet:

```text
D0 = <eta>, |D0| = 256
GRS multiplier vector v
one line f + z g
S_T = D0 \ T, |S_T| = 143
p_T in F0[X]_<137 with f + z_T g = p_T on S_T
z_T = a + b / P_T(beta), with common a,b and b != 0
gamma_T = 1 for every packet support
no simultaneous degree-<137 explanations of f and g on S_T
exact projected slope count = 52,747,567,092
```

Once this contract replays, the smooth ([512,256]) theorem above becomes an unconditional finite `PROOF`.

For a genuinely frontier-active result at (q_{\rm line}=17^{48}), the exact missing theorem is:

```text
L-CYCLE115-F17^48-H256-TWO-COPY-COMPRESSION
```

Required contract:

[
H=\langle\eta\rangle\le\mathbb F_{17^{48}}^\times,\quad |H|=256,\quad k=128,
]
together with one residue-line datum and a map from two Cycle84 occupied coordinates to supports of a named exact size, such that:

```text
every retained slope is support-wise noncontained;
all slopes lie on one affine line/residue datum;
q_gen=q_code=q_line=q_chal=17^48;
the final slope map has fiber size at most 8;
no quotient/periodic/contained/endpoint/affine charge is double-counted.
```

The numerical reason for the fiber-(8) target is exact:
[
\left\lfloor\frac{N^2}{8}\right\rfloor
======================================

347,788,229,265,630,167,058

>

# 338,617,018,271,848,945,628

\left\lfloor\frac{17^{48}}{2^{128}}\right\rfloor.
]

That compressed (H_{256}) theorem—not a (464)-to-power-of-two padding argument—is the exact missing smooth-domain frontier bridge.
