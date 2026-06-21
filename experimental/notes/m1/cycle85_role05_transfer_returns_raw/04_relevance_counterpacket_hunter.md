COUNTERPACKET

## 1. Executive verdict and confidence

**Cycle84 does not materially advance the official prize frontier. Confidence: high.**

The count does transfer, subject to the banked Cycle62–68 bridge, to a genuine finite (t=1) MCA lower certificate:

[
M_C(\sigma)\ge 52{,}747{,}567{,}092.
]

It does **not** prove equality with the whole MCA numerator.

The direct model has

[
n=256,\qquad \sigma=6,\qquad j=113,
\qquad k=n-j-\sigma=137,
]

so its rate (137/256) is outside the official rate set. More decisively, every possible one-copy line-field normalization under the official (q_{\rm line}<2^{256}) cap is either already defeated much farther along the reserve lattice by the core tangent bound, or has a native target larger than the Cycle84 count.

Thus

[
\operatorname{Occ}(\beta)>2^{32}
]

is only a research benchmark. It is not any native (T_{\rm line}) available to this characteristic-(17) model.

---

## 2. Exact counterpacket statement

### `C-CYCLE85-ONE-COPY-OCCUPANCY-NONMOVEMENT`

Let

[
F_0=\mathbf F_{17^{16}},\qquad
D=\mu_{256}\subset F_0,\qquad
\beta=X+2,
]

and let (\mathcal P_0) be the Cycle65–84 support family. Put

[
O:=#{\rho_\beta(T):T\in\mathcal P_0}
=52{,}747{,}567{,}092.
]

Assume a one-copy Role05 transfer realizes this family in a native MCA instance at reserve (\sigma_0), with support budget (j_0\ge113), and line field (F_{\rm line}) containing (F_0).

Under the official strict field cap (q_{\rm line}<2^{256}), the resulting lower term can never be classified

```text
MOVES_FAILURE_FRONTIER
```

by `RS-PRIZE-FRONTIER-V1`.

More exactly:

[
q_{\rm line}\in
{17^{16},17^{32},17^{48}}.
]

The corresponding native thresholds are

[
\begin{array}{c|c}
q_{\rm line}&T_{\rm line}=\lfloor q_{\rm line}/2^{128}\rfloor\
\hline
17^{16}&0\
17^{32}&6\
17^{48}&338{,}617{,}018{,}271{,}848{,}945{,}628.
\end{array}
]

The Cycle84 lower term is then respectively:

[
\begin{array}{c|c}
q_{\rm line}&\text{exact relevance classification}\
\hline
17^{16}&\texttt{SUBFRONTIER_REDUNDANT}\
17^{32}&\texttt{SUBFRONTIER_REDUNDANT}\
17^{48}&\texttt{NUMERICALLY_INACTIVE}.
\end{array}
]

Consequently, the informal comparison (O>2^{32}) supplies no official native-threshold or frontier-movement statement.

---

## 3. Proof and construction

### 3.1 What the finite count genuinely transfers to

Cycle65–68 identify, up to a fixed nonzero scalar,

[
\rho_\beta(T)=P_T(\beta)=\prod_{x\in T}(\beta-x)
]

with the thickened (\Delta^+)-lift coordinate of the support (T).

Cycle62 Role05 proves that, on a fixed (t=1) syndrome line,

[
T,T'\text{ give the same slope}
\iff
\text{their }\Delta^+\text{-lift classes agree}.
]

It also proves that changing the augmented parity-check row only applies a common affine bijection

[
\chi\longmapsto a\chi+b,\qquad a\ne0,
]

so it cannot merge distinct colors.

Therefore the Cycle84 product fibers are exactly the same-slope fibers for this subfamily. The twelve double fibers and no larger fibers are already incorporated into

[
O=52{,}747{,}567{,}092.
]

Cycle62 Role05 §6.6 proves automatic noncontainment for the shifted (t=1) slice. Hence these are transverse bad slopes, not contained incidences. Thus, for the associated line (\ell),

[
|\operatorname{Bad}_{\le113}(\ell)|\ge O,
]

and consequently

[
M_C(6)\ge O.
]

This is a whole-numerator **lower bound** because (M_C) maximizes over syndrome lines.

It is not an exact whole-numerator evaluation: supports outside (\mathcal P_0), and possibly the lower-weight (A)-support, can contribute additional slopes.

### 3.2 The direct model is not an official instance

The Role05 relation is

[
j=n-k-\sigma.
]

Substituting the Cycle84 values gives

[
k=256-113-6=137.
]

The official profile permits

[
\frac kn\in
\left{\frac12,\frac14,\frac18,\frac1{16}\right},
]

whereas (137/256) is none of these. Therefore the unmodified Cycle84 model is `VALID_RESEARCH`, not `VALID_OFFICIAL`.

This is the first failure in the direct official registration chain.

### 3.3 The rate defect can be repaired, but relevance still fails

The rate defect is not the fundamental obstruction.

Write the original apolar ideal as

[
I_s=(A,B),\qquad \deg A=6,\quad \deg B=113.
]

The support family has the form

[
T={1}\cup\bigcup_{t=1}^7\eta^t\widetilde A_t,
]

with (\widetilde A_t\subset K=\langle\eta^8\rangle). Hence every support avoids

[
K\setminus{1},
]

which has (31) points.

At most six points of (D) lie in (\operatorname{Supp}A). Choose a fixed set

[
S\subset (K\setminus{1})\setminus\operatorname{Supp}A,
\qquad |S|=9,
]

and let (Q=P_S).

Then

[
(A,BQ)
]

is a coprime complete intersection of degrees (6) and (122), and hence is the apolar ideal of a corresponding syndrome. For every (T\in\mathcal P_0),

[
P_{T\cup S}
=QP_T
=A(QU_T)+\gamma_T(BQ).
]

Thus (T\cup S) is a full-coordinate support of size (122). The new parameters are

[
n=256,\qquad k=128,\qquad \sigma=6,\qquad j=122,
]

so the rate is officially allowed.

In the thickened generalized Jacobian,

[
g_{T\cup S}=g_Sg_T.
]

Multiplication by the fixed unit (g_S) is bijective, so the number and multiplicities of occupied lift classes are unchanged. The padded official-rate packet still has exactly (O) occupied slopes within the constructed subfamily.

This padding lemma requires an explicit (S), new syndrome, and code fingerprint before registry promotion, but it shows that merely citing the raw (137/256) rate would not be a satisfactory final route cut.

### 3.4 Exhaustive line-field normalization

Because (\eta) has order (256), it cannot lie in any proper subfield of (F_0). Indeed, for (d\mid16),

[
v_2(17^d-1)=4+v_2(d),
]

and this is at most (7) for (d<16). Hence

[
q_{\rm gen}=17^{16}.
]

Any code or line field containing the domain therefore has characteristic (17), and an embedding

[
\mathbf F_{17^{16}}\hookrightarrow\mathbf F_{17^d}
]

requires (16\mid d).

The strict official cap excludes (d\ge64), since

[
17^{64}>2^{256}.
]

Thus the only possible line-field degrees are

[
d=16,32,48.
]

Their exact values and thresholds are:

[
17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481,
\qquad T_{\rm line}=0;
]

[
17^{32}
=2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361,
\qquad T_{\rm line}=6;
]

[
17^{48}
=115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641,
]

[
T_{\rm line}
=338{,}617{,}018{,}271{,}848{,}945{,}628.
]

No admissible line field has (T_{\rm line}=2^{32}).

### 3.5 Exact leave-one-out relevance

#### Case (q_{\rm line}=17^{16})

Here (T_{\rm line}=0).

The core unit lower bound is

[
M_C(\sigma)\ge1
]

at every reserve, including zero radius. Therefore every reserve already fails and the frontier has (f=r). Removing or adding the Cycle84 term changes nothing.

#### Case (q_{\rm line}=17^{32})

Here (T_{\rm line}=6).

The core tangent theorem gives

[
M_C(\sigma)\ge j_\sigma.
]

Suppose the Cycle84 packet is registered at reserve (\sigma_0) with support budget (j_0\ge113). Since (r=\sigma_0+j_0), at reserve

[
\tau=r-7=\sigma_0+j_0-7
]

the tangent bound is

[
M_C(\tau)\ge7>6.
]

Moreover,

[
\tau-\sigma_0=j_0-7\ge106.
]

Thus a core certificate already proves failure at a reserve at least (106) steps beyond the Cycle84 packet. A lower certificate at (\sigma_0) propagates only to reserves (\sigma\le\sigma_0), so Cycle84 cannot move (f).

For the concrete (9)-point padded code,

[
r=128,\qquad \sigma_0=6,\qquad j_0=122,
]

and the tangent frontier reaches

[
f_{\rm tan}=121,
]

whereas the Cycle84 term reaches only reserve (6).

#### Case (q_{\rm line}=17^{48})

Here

[
O=52{,}747{,}567{,}092
<
338{,}617{,}018{,}271{,}848{,}945{,}628
=T_{\rm line}.
]

The lower term does not certify failure at any reserve. It is numerically inactive.

This exhausts all one-copy official field normalizations.

---

## 4. Verification requirements

A registry-grade transfer should verify the following without rerunning the Cycle84 census:

1. **Bridge binding.** Bind the exact Cycle84 (\mathcal P_0), (\beta), field model, and product key to the exact Role05 syndrome, (A,B,\Delta,\Delta^+), and code fingerprint. The public replay currently certifies the product model, not this final code-fingerprint bridge.

2. **Support validity.** Verify that every (T\in\mathcal P_0) is squarefree, (D)-split, disjoint from (\operatorname{Supp}\Delta), and has (\gamma_T\ne0).

3. **Slope interpretation.** Verify the fixed-scalar or affine normalization connecting (\rho_\beta(T)) to the Role05 reduced color. Transversality then follows from the existing Role05 noncontainment theorem.

4. **Official padding, if used.** Emit an explicit (S), (Q=P_S), new syndrome (s_S), and certificate that its apolar ideal is ((A,BQ)). Check (S\cap T=\varnothing), (S\cap\operatorname{Supp}A=\varnothing), and (Q(\beta)\ne0).

5. **Field ledger.** Certify (q_{\rm gen}=17^{16}), all embeddings, (q_{\rm code}), (q_{\rm line}), and the exact target. Set the challenge debit to `unused`.

6. **Relevance.** Run leave-one-out relevance. A row marked `FAIL` is not evidence that a packet moved the frontier.

Quotient or periodic structure does not reduce the raw slope count. It may determine which upper-program component charges the packet, but the definition of (\operatorname{Bad}) contains no quotient exclusion.

---

## 5. Next exact lemma or construction

The one-copy route is cut. The exact amplification target is:

```text
L-CYCLE86-TWO-COPY-ROLE05-T1-TENSOR-AT-17^48
```

Construct a native MCA instance with

[
F_{\rm code}=F_0,\qquad
F_{\rm line}=\mathbf F_{17^{48}},
]

[
n=512,\qquad k=256,\qquad \sigma=12,\qquad j=244,
]

and an injection from pairs of padded Cycle84 supports into full-coordinate transverse supports such that, for some

[
\theta\in F_{\rm line}\setminus F_0,
]

the slopes have the form

[
z(T_1,T_2)=z_0+\chi(T_1)+\theta\chi(T_2).
]

This would make the slope map injective on the product of the two occupied sets and give

[
M_C(12)\ge O^2
=2{,}782{,}305{,}834{,}125{,}041{,}336{,}464,
]

while

[
T_{\rm line}
=338{,}617{,}018{,}271{,}848{,}945{,}628.
]

Thus

[
O^2>T_{\rm line}.
]

Unlike the one-copy packet, this is not dominated by the tangent bound, since (244\ll T_{\rm line}).

The exact current obstruction is that naïve locator multiplication does not preserve the two-generator (t=1) apolar condition. If

[
P_i=A_iU_i+\gamma_iB_i,
]

then

[
\begin{aligned}
P_1P_2
={}&A_1A_2U_1U_2
+\gamma_1A_2B_1U_2\
&+\gamma_2A_1B_2U_1
+\gamma_1\gamma_2B_1B_2.
\end{aligned}
]

The two middle terms are generally neither divisible by (A_1A_2) nor scalar multiples of (B_1B_2). Therefore “occupied colors multiply” is not presently a theorem. The next construction must explicitly eliminate or absorb these cross terms while preserving one common syndrome line.

---

## Self-audit

1. **Exact implication proved:** the Cycle84 count gives a finite one-copy MCA lower certificate (M_C(\sigma)\ge O), and no one-copy official normalization can move the failure frontier.
   **Not proved:** (M_C(\sigma)=O), a full prize theorem, a safe-side upper bound, or tensor multiplicativity.

2. **Prize status:** the present artifact is a finite/model certificate. With an added fixed-padding and transfer certificate it can become an official lower packet, but it remains subfrontier-redundant for (q_{\rm line}=17^{16},17^{32}) and inactive for (17^{48}).

3. **First failure line:** for the artifact as supplied, official validation fails at (k=137). After rate repair, the first decisive failure is field-target/leave-one-out relevance. The first still-needed registry bridge is the code-fingerprint-bound identification of (\rho_\beta) with the Role05 (\Delta^+)-color.

4. **Field use:** (q_{\rm gen}=17^{16}); native MCA uses (q_{\rm line}); scalar-list comparisons use (q_{\rm code}); (q_{\rm chal}) is unused. The (2^{-128}) test is implemented as lower (>T_{\rm line}). The (2^{32}) comparison is not native.

5. **Possible numerator reductions:** contained incidences do not reduce it; affine normalization is bijective; same-slope collisions are exactly the Cycle84 product collisions; quotient/periodic structure may classify the packet but cannot erase actual distinct slopes.

6. **Exact theorem needed next:** `L-CYCLE86-TWO-COPY-ROLE05-T1-TENSOR-AT-17^48`, including a common-syndrome construction, cross-term cancellation, full-coordinate verification, transversality, and injective color combination.
