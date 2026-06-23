LABEL:

**BANKABLE_LEMMA / ROUTE_CUT / SOURCE-SCOPED PROOF**

**L-CYCLE118-QCHAL-FIELD-THICKENING-OR-DENSITY-LOSS — CLOSED AS A DICHOTOMY**

Confidence: high.

EXECUTIVE VERDICT:

The attached MCA definition has only one sampled variable, (z\in\mathbb F). Thus, within the attached-source experiment, the sample-field cardinality is necessarily (q_{\rm line}=|\mathbb F|); there is no independent (q_{\rm chal}).

More strongly, let

[
K=\mathbb F_{17^{32}},\qquad
C_K=\operatorname{RS}[K,H,256].
]

For every extension (E/K), scalar extension of a (K)-valued line produces **no new bad slopes**:

[
\operatorname{Bad}_{E}(f,g;a)
=============================

\operatorname{Bad}_{K}(f,g;a)
\subseteq K.
]

Therefore the Cycle116 numerator does not thicken. For every proper extension (E/K),

[
\frac{#\operatorname{Bad}_{E}(f,g;a)}{|E|}
\le \frac{|K|}{|E|}
\le \frac1{|K|}
<2^{-128}.
]

So literal field thickening by replacing (z\in K) with (z\in E) decisively kills every (K)-valued Cycle116-type line, not merely the certified subset of (N) slopes.

There are exactly two possible no-loss escapes:

1. A separate challenge field may map to (K) by a balanced surjection. Then challenge density is preserved exactly.
2. The line must become genuinely (E)-valued. For fixed length (512), this is impossible for ([E:K]\ge5) by a universal support-count bound. Only extension degrees (2,3,4) remain mathematically open.

A source-valid replacement over (E=\mathbb F_{17^{32r}}) does exist if the row may change: for power-of-two (r), a generated power-of-two domain of length (512r) supports a line on which **every** (z\in E) is bad at agreement (256r+1). This is not a preservation of the Cycle116 radius (125/256).

THEOREM / COUNTERPACKET / ROUTE CUT:

### Theorem A — source MCA has no second challenge denominator

For a linear code (C\subseteq F^D), the attached definition is

[
\epsilon_{\rm mca}(C,\delta)
============================

\max_{f,g\in F^D}
\frac{
#{z\in F:z\text{ is support-wise MCA-bad for }f+zg}
}{|F|}.
]

Hence the unique source sample space is (F). In the Cycle116 row,

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},
\qquad q_{\rm chal}=\text{null}.
]

If one introduces a notation (q_{\rm sample}^{\rm MCA}) for the cardinality of the source experiment’s sampled parameter, then

[
q_{\rm sample}^{\rm MCA}=q_{\rm line}=17^{32}.
]

This does **not** define an official protocol (q_{\rm chal}).

---

### Theorem B — exact scalar-extension invariance

Let (K\subseteq E) be finite fields, (D\subseteq K), and

[
C_K=\operatorname{RS}[K,D,k],
\qquad
C_E=\operatorname{RS}[E,D,k].
]

For (f,g\in K^D) and agreement threshold (a), let
(\operatorname{Bad}_K(f,g;a)) and (\operatorname{Bad}_E(f,g;a)) denote their support-wise bad-slope sets over the respective codes.

Then

[
\boxed{
\operatorname{Bad}_E(f,g;a)
===========================

\operatorname{Bad}_K(f,g;a)
\subseteq K.
}
]

This holds for every (a), equivalently at every radius.

Consequently, scalar extension preserves the complete bad-slope numerator of a (K)-valued line exactly, but changes its density by

[
\frac{|K|}{|E|}.
]

For the Cycle116 line, its (N) certified slopes remain bad, but no new slopes outside (K) arise:

[
\frac{N}{|E|}
\le
\epsilon_{\text{that line over }E}
\le
\frac{|K|}{|E|}.
]

The exact full numerator of the Cycle116 line was not enumerated, so it need not equal (N); the theorem says whatever that numerator is, it is unchanged.

---

### Corollary B.1 — proper scalar extension destroys the (2^{-128}) violation

Write (E=\mathbb F_{17^{32r}}), so (|E|=|K|^r). For (r\ge2),

[
\epsilon_{\text{any (K)-valued line over }E}
\le |K|^{1-r}
\le |K|^{-1}.
]

The packet verifies

[
\left\lfloor\frac{|K|}{2^{128}}\right\rfloor=6,
]

so (|K|>2^{128}), and therefore

[
\boxed{
\epsilon_{\text{any (K)-valued line over a proper }E/K}
<2^{-128}.
}
]

Thus the direct implication

[
\text{Cycle116 line over }K
\Longrightarrow
\text{same line over a larger line field }E
]

fails at its first density step.

---

### Theorem C — universal fixed-([512,256]) extension cut

For every field (E) containing (K),

[
C_E=\operatorname{RS}[E,H,256]
]

satisfies

[
\boxed{
\operatorname{LD}_{\rm sw}(C_E,262)
\le \binom{512}{262}.
}
]

Therefore, if (E=\mathbb F_{17^{32r}}) and (r\ge5),

[
\epsilon_{\rm mca}!\left(C_E,\frac{125}{256}\right)
<
2^{-128}.
]

This upper bound holds for **all** (E)-valued lines, not only scalar extensions of Cycle116.

Hence:

[
\boxed{
\text{At fixed }(n,k,a)=(512,256,262),
\text{ only }[E:K]\in{2,3,4}
\text{ can remain open.}
}
]

---

### Theorem D — exact balanced-challenge no-loss compiler

Let (\Omega) be a finite official challenge space and let

[
\mu:\Omega\to K
]

be the official challenge-to-line-slope map. For a source bad-slope set (B\subseteq K), the challenge error is exactly

[
\Pr_{\omega\in\Omega}[\mu(\omega)\in B]
=======================================

\frac1{|\Omega|}
\sum_{z\in B}|\mu^{-1}(z)|.
]

If (\mu) is balanced, meaning every fiber has size (|\Omega|/|K|), then

[
\boxed{
\Pr[\mu(\omega)\in B]=\frac{|B|}{|K|}.
}
]

For every extension (E/K), a (K)-linear coordinate projection

[
\pi:E\to K
]

is a balanced surjection, with fibers of size (|E|/|K|). Thus the challenge family

[
u_c=f+\pi(c)g,\qquad c\in E,
]

has exactly the original Cycle116 bad-event density.

This is a conditional no-loss compiler. It applies only if the official contract explicitly permits a separate challenge field and explicitly defines the line parameter as such a balanced image. It is not the source affine line (f+cg) over (E).

---

### Theorem E — generated smooth replacement over power-of-two extensions

Let (r=2^s) and

[
E_r=\mathbb F_{17^{32r}}.
]

Then (E_r^\times) has a subgroup (D_r) of order

[
n=512r
]

which generates (E_r) over (\mathbb F_{17}). Put

[
k=\frac n2=256r.
]

For the line on (D_r)

[
u_z(x)=x^{k+1}+z x^k,
\qquad z\in E_r,
]

every parameter (z\in E_r) is support-wise MCA-bad at agreement (k+1). Therefore

[
\boxed{
\epsilon_{\rm mca}
\left(
\operatorname{RS}[E_r,D_r,256r],
\frac12-\frac1{512r}
\right)
=1.
}
]

This gives a complete numerator thickening:

[
\operatorname{LD}_{\rm sw}
\left(
\operatorname{RS}[E_r,D_r,256r],
256r+1
\right)
=|E_r|.
]

It is a replacement construction, not a scalar extension of the Cycle116 row. In particular,

[
\frac12-\frac1{512r}>\frac{125}{256},
]

so this theorem cannot be used to claim agreement (262r) or the Cycle116 radius.

---

### Route cut for non-power-of-two extension degrees

Write

[
r=2^s u,\qquad u\text{ odd}.
]

Every power-of-two subgroup of
(\mathbb F_{17^{32r}}^\times) lies in

[
\mathbb F_{17^{32\cdot2^s}}.
]

Therefore, when (u>1), no power-of-two multiplicative domain generates all of (E_r).

Thus a generated-field, power-of-two smooth thickening exists precisely along the power-of-two extension tower. Odd extension factors require either a non-power-of-two domain or a genuinely different compiler.

PROOF DETAILS:

### 1. Proof of exact scalar-extension invariance

Choose a (K)-basis

[
e_1=1,e_2,\ldots,e_r
]

of (E), and let (\pi_i:E\to K) be the corresponding coordinate projections. For every (P\in E[X]) and (x\in D\subseteq K),

[
\pi_i(P(x))=(\pi_iP)(x),
]

where (\pi_iP) means coefficientwise projection. Degrees do not increase.

First let (z\notin K). Write

[
z=z_1e_1+\cdots+z_re_r
]

and choose (i\ge2) with (z_i\ne0). Suppose that on some support (S),

[
P(x)=f(x)+zg(x)
]

for a polynomial (P\in E[X]_{<k}). Projecting to coordinate (i) gives

[
(\pi_iP)(x)=z_i g(x)
\qquad(x\in S),
]

so the degree-(<k) polynomial

[
G=z_i^{-1}\pi_iP
]

explains (g) on (S). The first coordinate gives

[
(\pi_1P)(x)=f(x)+z_1g(x),
]

so

[
A=\pi_1P-z_1G
]

explains (f) on the same (S). Thus every close witness for (z\notin K) is automatically contained, and (z) cannot be support-wise bad.

Now let (z\in K). Any (K)-codeword witness is also an (E)-codeword witness. Conversely, any (E)-polynomial explaining the (K)-valued word (f+zg) projects via (\pi_1) to a (K)-polynomial explaining the same word. Likewise, an (E)-polynomial explaining (f) or (g) projects to a (K)-polynomial explaining it. Therefore closeness and simultaneous containment are equivalent over (K) and (E), proving exact equality of bad sets.

This strengthens the packet’s subfield-confinement theorem from inclusion to complete base-change invariance.

### 2. Proof of the fixed-row support cap

At agreement (262\ge256+1), every bad witness can be reduced to an exact support of size (262).

Indeed, if a word fails to be degree-(<256) polynomial data on a larger support, that failure is already visible on a (257)-subset: choose 256 points and interpolate; if every additional point were compatible, the interpolant would explain the full support. Extend such a (257)-subset to 262 points.

For a fixed support (S), at most one slope is noncontained. If distinct (z,z') were both explained on (S) by codewords (P,P'), then

[
g|_S=\left(\frac{P-P'}{z-z'}\right)\Big|_S
]

and

[
f|_S=(P-zg)|_S
]

would simultaneously be code-explained, contradicting badness.

Assigning one exact witness support to each bad slope therefore gives an injection into the 262-subsets of (H):

[
#\operatorname{Bad}\le\binom{512}{262}.
]

For (r\ge5),

[
|E|=|K|^r>2^{128r}\ge2^{640},
]

while

[
\binom{512}{262}<2^{512}.
]

Hence

[
\frac{\binom{512}{262}}{|E|}
<
2^{-128}.
]

### 3. Proof of the power-of-two domain classification

Let (r=2^s u), (u) odd. By the 2-adic lifting formula,

[
\begin{aligned}
\nu_2(17^{32r}-1)
&=\nu_2(17-1)+\nu_2(17+1)+\nu_2(32r)-1\
&=4+1+(5+s)-1\
&=9+s.
\end{aligned}
]

Thus the largest power-of-two subgroup in (E_r^\times) has order (2^{9+s}).

For (t\ge5),

[
\operatorname{ord}_{2^t}(17)=2^{t-4},
]

because

[
\nu_2(17^{2^a}-1)=4+a
]

and (a=t-4) is minimal. An element of order (2^{9+s}) therefore has degree

[
2^{9+s-4}=2^{5+s}=32\cdot2^s
]

over (\mathbb F_{17}).

Hence the maximal power-of-two subgroup generates exactly

[
\mathbb F_{17^{32\cdot2^s}},
]

which equals (E_r) precisely when (u=1).

### 4. Proof of the smooth replacement construction

Assume (r=2^s), put (d=32r), and let (\zeta) have order

[
16d=512r.
]

The order computation above gives

[
\operatorname{ord}_{512r}(17)=d,
]

so (1,\zeta,\ldots,\zeta^{d-1}) is an (\mathbb F_{17})-basis of (E_r). Let

[
H_0=\mathbb F_{17}^{\times},
\qquad |H_0|=16.
]

Then

[
D_r=\bigsqcup_{i=0}^{d-1}\zeta^iH_0.
]

The restricted-sum bound in the packet gives

[
8^{\wedge}H_0=\mathbb F_{17},
\qquad
9^{\wedge}H_0=\mathbb F_{17},
]

since

[
8(16-8)+1=65\ge17,
\qquad
9(16-9)+1=64\ge17.
]

Given any (y=\sum_{i=0}^{d-1}c_i\zeta^i\in E_r), choose a 9-subset (T_0\subseteq H_0) summing to (c_0), and for (i\ge1) choose an 8-subset (T_i\subseteq H_0) summing to (c_i). Then

[
A=T_0\sqcup\zeta T_1\sqcup\cdots\sqcup\zeta^{d-1}T_{d-1}
]

has

[
|A|=9+8(d-1)=8d+1=k+1
]

and sum (y). Thus

[
(k+1)^{\wedge}D_r=E_r.
]

For a desired slope (z), choose (A) with sum (-z). Its locator is

[
L_A(X)
======

X^{k+1}+zX^k+R_A(X),
\qquad \deg R_A<k.
]

On (A),

[
x^{k+1}+zx^k=-R_A(x),
]

giving a degree-(<k) explanation. But (x^k) cannot agree with a degree-(<k) polynomial on (k+1) points. Thus every (z) is support-wise bad.

### 5. Unrestricted-domain fallback over every extension

For completeness, every (E=\mathbb F_{17^{32r}}), including non-power-of-two (r), admits a source-valid full-density construction on

[
D=E^\times,\qquad n=|E|-1,\qquad k=n/2.
]

Since (|E|\equiv1\pmod4), write (|E|=4m+1). Every (y\in E) is a sum of (2m+1=k+1) distinct nonzero elements:

* For (y\ne0), construct a set summing to (1) as ({1}) plus (m) disjoint pairs ({a,-a}), then multiply by (y).
* For (y=0), use ({1,2,-3}) plus (m-1) disjoint pairs ({a,-a}).

The same locator argument therefore gives

[
\epsilon_{\rm mca}
\left(
\operatorname{RS}[E,E^\times,(|E|-1)/2],
\frac12-\frac1{|E|-1}
\right)
=1.
]

This is not an FFT-size or power-of-two-domain compiler.

FIELD AND PARAMETER LEDGER:

| Branch                                | (q_{\rm gen}) | (q_{\rm code}) | (q_{\rm line}) |                  (q_{\rm chal}) | Result                                      |   |                                  |
| ------------------------------------- | ------------: | -------------: | -------------: | ------------------------------: | ------------------------------------------- | - | -------------------------------- |
| Cycle116 source row                   |   (K=17^{32}) |            (K) |            (K) |                            null | (N/K>2^{-128})                              |   |                                  |
| Same (H), scalar extension to (E=K^r) |           (K) |            (E) |            (E) |                            null | Bad set unchanged and contained in (K)      |   |                                  |
| Proper scalar extension, (r\ge2)      |           (K) |            (E) |            (E) |                            null | Every (K)-valued line has error (<2^{-128}) |   |                                  |
| Separate balanced challenge compiler  |           (K) |            (K) |            (K) | (E), only if officially defined | Exact no-loss density                       |   |                                  |
| Generated smooth replacement, (r=2^s) |           (E) |            (E) |            (E) |                            null | (n=512r,\ k=256r,\ a=k+1,\ \epsilon=1)      |   |                                  |
| Full multiplicative replacement       |           (E) |            (E) |            (E) |                            null | (n=                                         | E | -1,\ k=n/2,\ a=k+1,\ \epsilon=1) |

For Cycle116 itself:

[
\begin{aligned}
K&=\mathbb F_{17^{32}},\
|K|&=2367911594760467245844106297320951247361,\
n&=512,\quad k=256,\quad a=262,\quad \delta=125/256,\
N&=52{,}747{,}567{,}092.
\end{aligned}
]

SELF-AUDIT:

1. **Exact statement and scope.**
   I proved, under the attached finite/source support-wise MCA definitions, exact bad-set invariance under scalar extension, a fixed-row support cap, a conditional balanced-challenge no-loss theorem, and source-valid replacement constructions. No official/prize-adopted theorem was proved.

2. **Field ledger.**
   In the banked row, (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}) and (q_{\rm chal}=\mathrm{null}). With the same domain (H) and scalar-extended code (E), (q_{\rm gen}=|K|) while (q_{\rm code}=q_{\rm line}=|E|). A non-null (q_{\rm chal}) was used only in the explicitly conditional challenge-map theorem.

3. **Numerator losses.**
   No endpoint, quotient, periodic, tangent, contained-line, affine-color, or charge rule was introduced. Under scalar extension, the source bad set is unchanged; the failure is purely denominator dilution. The replacement constructions exclude containment by the degree-(k) root argument. Official retention rules remain unpinned.

4. **Decoding notion.**
   Every result concerns support-wise (\operatorname{LD}_{\rm sw}) and support-wise MCA. It is not ordinary fixed-word list decoding or generic close-point line decoding.

5. **First missing official clause.**
   The first q-field clause is now precise: the packet lacks the authority-pinned tuple

   [
   (\Omega_{\rm chal},\Pr_{\rm chal},
   \mu:\Omega_{\rm chal}\to F_{\rm line},
   \text{event pullback/filter rule}).
   ]

   Merely supplying (|\Omega_{\rm chal}|) is insufficient. Balanced projection gives no loss; direct scalar extension gives decisive loss.

6. **Next worker target.**
   The next checker must pin the challenge-to-line map. If it returns direct identity sampling over (E), the only fixed-([512,256]) unresolved extensions are degrees (2,3,4), and they require a genuinely (E)-valued line.

No agreement-263 upgrade was claimed. The scalar-extension obstruction holds at every agreement threshold, but the Cycle116 certified numerator remains an agreement-262 result.

NEXT EXACT STEP:

First produce:

```text
V-CYCLE118-QCHAL-SAMPLER-MAP-RECEIPT
```

with mandatory fields

```text
challenge_space
challenge_distribution
q_chal
line_field
challenge_to_line_parameter_map
bad_event_pullback_or_filter
duplicate/quotient/charge treatment
```

The checker should return exactly one of:

```text
DIRECT_K_SAMPLING_CYCLE116_DENSITY_RETAINED
BALANCED_CHALLENGE_PROJECTION_NO_LOSS
IDENTITY_E_SCALAR_EXTENSION_CYCLE116_LINE_KILLED
UNDEFINED_MAP_NO_OFFICIAL_CLAIM
```

If the receipt selects identity scalar extension (E=K^r), the exact remaining mathematical target is

[
\boxed{
\operatorname{RL}_{\rm NC}^{=}
(H,256,262;K^r)
\ge
\left\lfloor\frac{|K|^r}{2^{128}}\right\rfloor+1,
\qquad r\in{2,3,4},
}
]

using a genuinely (K^r)-valued residue-line datum. For (r\ge5), the support-count theorem proves this target impossible.

If row enlargement is permitted and the radius (125/256) must be preserved, the exact fixed-jet construction target is:

[
\mathcal J_r\subseteq\binom{D_r}{250r},
]

such that

[
\deg(P_J-P_{J'})\le244r
]

for all (J,J'\in\mathcal J_r), and for some (\beta\in E_r\setminus D_r),

[
#{P_J(\beta):J\in\mathcal J_r}

>

\frac{|E_r|}{2^{128}}.
]

That is precisely the missing (j=250r,\ \sigma=6r,\ a=262r) thickened fixed-jet occupancy lemma.
