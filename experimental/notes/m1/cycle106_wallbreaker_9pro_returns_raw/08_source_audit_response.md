AUDIT

**Verdict:** Cycle106 is not presently a well-formed theorem, and even a proof of its intended incidence statement would certify only the aperiodic component of one subgroup/same-field M1 reduction. It would not, by itself, certify the complete M1 numerator or an official prize result.

```text
first_missing_hypothesis =
an exact predicate AP_{n,sigma}(Uhat), an exact corrected-reserve threshold,
and a source theorem proving that every residual official bad slope produces a
normalized Uhat satisfying that predicate.

first_unsafe_promotion =
“Cycle106 proved” => “the M1 upper-side numerator is bounded.”
Cycle106 addresses only the putative aperiodic incidence leaf; no exhaustive
official-bad-slope cover and normalization theorem is present.

exact theorem needed next =
L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER,
followed by an explicit finite Cycle106 incidence bound B_ap(n,sigma), and then
a certified whole-numerator upper program whose value is at most
floor(q_line/2^128).
```

## 1. Cycle103 bandwidth-one claim

The algebraic claim is coherent under the implicit hypotheses

[
p\ \text{prime},\qquad n\mid p-1,\qquad H=\mu_n,\qquad
\widehat U(0)=u_0=1,\qquad 0\le \sigma\le n-1.
]

For (k=1), activity gives a degree-(\sigma+1) polynomial

[
G_\theta(X)=
\left[\frac{\widehat U(X)}{1-\theta X}\right]_{\le \sigma+1}
]

equal to (g_{\bar S}(X)) for a ((\sigma+1))-subset (\bar S\subset H). Hence it divides (1-X^n). If the pseudo-remainder vanished identically, the reverse of (G_\theta) would be a monic divisor of the split polynomial (X^n-1) over (\mathbf F_p(\theta)); all such monic divisors are products of fixed linear factors (X-x), (x\in H), and therefore have (\theta)-independent coefficients. This contradicts

[
g_1(\theta)=u_1+\theta.
]

Thus the stated bound

[
|\Theta_U|\le (n-\sigma+1)(\sigma+1)
]

is consistent with the supplied proof summary.

Two qualifications are mandatory:

1. This is a bound on distinct parameters, not on weighted subset witnesses.
2. It is not an official constant-rate result: (k=1) is not the asymptotic official-rate regime.

**Source status:** the compact packet contains the Cycle103 audit, but not the referenced raw response or `cycle103_b1_divisor_bound_check.py`. Consequently, I can audit the mathematical skeleton but cannot independently replay its exact pseudo-remainder degree calculation from this packet alone. Since the prompt declares Cycle103 banked, I treat it as an accepted dependency rather than newly source-verified evidence.

## 2. Cycle104 fixed-(k) claim

The finite inequality

[
|\Theta_U|\le \binom nk(\sigma+1)
]

is not logically restricted to fixed (k). The described divided-difference union bound is a finite statement for every admissible (k). “Fixed (k)” is relevant only when interpreting the right side as polynomial in (n).

The claimed mechanism is:

* an active divisor has an (s=k+\sigma) element root set;
* on that set, (B_\theta) agrees with a polynomial of degree at most (k-2);
* therefore every chosen (k)-subset has vanishing divided difference of order (k-1);
* for a fixed (k)-subset, this obstruction is a nonzero degree-(\sigma+1) polynomial in (\theta);
* union over the (\binom nk) choices.

This gives a valid fixed-bandwidth upper stratum, but for (k=\rho n),

[
\binom nk
]

is generally exponential. It therefore contributes no uniform M1 upper theorem.

**Source status:** as for Cycle103, the compact packet omits the referenced Cycle104 raw answer and checker. The audit summary alone is not a replayable proof certificate.

## 3. Cycle105 collapse: valid, but two corrections are required

### 3.1 The (k)-free collapse

With (d=\sigma+1), (s=k+\sigma), and (u_0=1),

[
g_\ell(\theta)=\sum_{i=0}^{\ell}u_{\ell-i}\theta^i
]

gives

[
\theta\text{ active}
\iff
\exists,\bar S\subset H,\ |\bar S|=s,\quad
g_{\bar S}(X)\equiv G_\theta(X)\pmod{X^{d+1}}.
]

Hence

[
\theta\text{ active}
\iff
\Gamma_{\widehat U,\sigma}(\theta)\in M_s.
]

This is the genuine (k)-free reduction: for fixed ((\widehat U,\sigma)), the curve is independent of (k), while (k) selects the layer (s=k+\sigma).

The phrase “one fixed curve” must not be read as uniform over (\sigma). Its ambient dimension and coefficients change with (\sigma).

The distinction between parameter count and image-point count is harmless only because

[
g_1(\theta)=u_1+u_0\theta=u_1+\theta
]

is injective. Therefore

[
#{\theta:\Gamma(\theta)\in M_s}=|\Gamma\cap M_s|.
]

The normalization (u_0=1), or at least (u_0\ne0), must be included in the theorem statement. It is implicit in the preceding reciprocal-locator derivation but absent from the abbreviated Cycle106 wall.

Also, the source numerator concerns external parameters (\theta\in\mathbf F_p\setminus H). Bounding all (\theta\in\mathbf F_p) is a safe stronger upper bound, but equality with the source numerator requires the external restriction.

### 3.2 The stated complement map fails at one admissible endpoint

Cycle105 writes

[
g_{\bar S}(X)g_{H\setminus\bar S}(X)
=1-X^n\equiv1\pmod{X^{\sigma+2}}.
]

The final congruence requires

[
\sigma+1<n.
]

At the admissible endpoint (k=1,\sigma=n-1,s=n), it is false.

A concrete countercheck is

[
p=5,\qquad n=4,\qquad \sigma=3,\qquad H=\mathbf F_5^\times.
]

Then

[
g_H(X)=1-X^4,
]

so the prefix point in (M_4) is

[
(0,0,0,-1)=(0,0,0,4).
]

The checker’s ordinary truncated-inverse map sends this to

[
(0,0,0,1),
]

whereas (M_0={(0,0,0,0)}). Thus the implemented `iota` does not map (M_4) to (M_0). The six supplied checker cases all have (\sigma+1<n), so their `PASS` does not test this endpoint.

The exact repair is simple. In

[
R_d=\mathbf F_p[X]/(X^{d+1}),\qquad d=\sigma+1,
]

define

[
\iota_{n,d}(A)=(1-X^n)A^{-1}.
]

Then

[
\iota_{n,d}(g_{\bar S})=g_{H\setminus\bar S}
]

for every admissible (d\le n). This is a triangular affine involution. For (d<n), it reduces to ordinary truncated inversion. If (A=1+\sum_{t=1}^d a_tX^t) and
(\iota_{n,d}(A)=1+\sum_{t=1}^d b_tX^t), the exact recurrence is

[
b_t=-\mathbf1_{t=n}-a_t-\sum_{i=1}^{t-1}a_i b_{t-i}.
]

Thus Cycle105 complement duality is repairable, but its displayed congruence and its supplied checker are not valid at the zero-radius (k=1) endpoint.

## 4. Cycle106 is not currently a mathematically closed statement

The phrase

```text
aperiodic Uhat above corrected reserve
```

is never defined in the supplied packet. There is no:

* predicate (\operatorname{AP}_{n,\sigma}(\widehat U));
* corrected-reserve function or inequality;
* quantifier range for (p,n,\sigma,k,s);
* normalization hypothesis on (\widehat U);
* source lemma saying which quotient or periodic configurations violate the predicate;
* theorem proving that every residual official M1 line produces such a (\widehat U).

This is not a cosmetic omission. Until the predicate is fixed, both a proof and a counterpacket can be rejected after the fact by changing what “aperiodic” means.

The properly quantified local theorem must have the form:

> There exist explicit absolute constants (C,A) and an exact decidable predicate (\operatorname{AP}*{n,\sigma}) such that, for every prime (p), every (n\mid p-1), every admissible (1\le k\le n-\sigma), (s=k+\sigma), and every normalized (\widehat U) satisfying the exact reserve condition and (\operatorname{AP}*{n,\sigma}(\widehat U)),
> [
> #\left{\theta\in\mathbf F_p\setminus H:
> \Gamma_{\widehat U,\sigma}(\theta)\in M_s\right}
> \le Cn^A.
> ]

The constants must be uniform in

[
p,n,\sigma,k,s,\widehat U.
]

An unspecified (n^{O(1)}) is sufficient for a research asymptotic theorem only if the uniformity is explicit. It is not a finite prize certificate.

## 5. Proving corrected Cycle106 would not yet prove the M1 numerator bound

The official MCA numerator is a maximum over affine syndrome lines of the number of distinct line parameters admitting a transverse support witness:

[
M_C(\sigma)=
\max_{u,v\ne0}
\left|
\left{
z:\exists T,\ |T|\le j_\sigma,\
u+zv\in V_T,\ v\notin V_T
\right}
\right|.
]

Exact-(j) padding is available only for (\sigma\ge1), not at (\sigma=0). 

Cycle106 would bound an object of the form

[
U_{\rm ap}
==========

#{\theta:\Gamma_{\widehat U,\sigma}(\theta)\in M_s}.
]

To make this a bound on a component of (M_C(\sigma)), one still needs a theorem converting every relevant slope (z) into a Cycle105 parameter (\theta). The exact missing bridge is:

### `L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER`

For every official same-field subgroup instance, reserve (\sigma\ge1), and affine syndrome line (\ell(z)=u+zv), there must be:

1. an exhaustive, source-valid branch assignment of every
   (z\in\operatorname{Bad}*{\le j*\sigma}(u,v));
2. certified residual, high-denominator, occupancy, tangent/contained, quotient-periodic, and aperiodic branches;
3. on the aperiodic branch, an affine map
   [
   \phi(z)=az+b,\qquad a\ne0,
   ]
   a normalized (\widehat U), and (s=k+\sigma), such that
   [
   \phi(B_{\rm ap})
   \subseteq
   {\theta\in\mathbf F_p\setminus H:
   \Gamma_{\widehat U,\sigma}(\theta)\in M_s};
   ]
4. a proof that (\operatorname{AP}_{n,\sigma}(\widehat U)) holds;
5. exact branch coverage and aggregation certificates.

The current prize checker treats `mca.aperiodic_upper` as one component leaf, not a whole-numerator theorem. A component becomes a valid upper certificate only after an exhaustive coverage program consumes it. The documented sharp form is

[
\max!\left{
U_{\rm res},,
U_{\rm high},,
N_{\rm occ}+U_{\rm tan}+U_{\rm quot}+U_{\rm ap}
\right},
]

with certified justification for each `max` and `sum`. 

Therefore:

[
\boxed{\text{Cycle106 alone does not bound }M_C(\sigma).}
]

It bounds at most (U_{\rm ap}), after the missing normalization theorem is proved.

## 6. Even a complete M1 numerator bound would not automatically be prize-level

Suppose the preceding coverage theorem and Cycle106 together produce an explicit whole-numerator bound (U_{\rm M1}(\sigma)). Official safety requires the finite inequality

[
U_{\rm M1}(\sigma)
\le
T_{\rm line}
:=
\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor.
]

A statement such as

[
U_{\rm M1}(\sigma)\le n^{O(1)}
]

does not establish this inequality. The exponent, constant, field size, reserve and other branch costs must be explicit.

The remaining official checks include:

* valid code/domain/rate profile;
* field embeddings;
* correct reserve and support-budget conversion;
* whole-line maximization;
* exact branch aggregation;
* exact integer comparison with the native denominator;
* theorem-registry and producer fingerprints.

Thus the promotion

[
\text{polynomial M1 numerator}
\Longrightarrow
\text{official prize result}
]

is invalid without an explicit field-versus-bound inequality and a complete certified profile.

## Field-ledger audit

At Cycle106 itself, the four (q)-roles and the (2^{-128}) threshold should not appear. The wall is a single-field structural incidence theorem over (\mathbf F_p); it seeks a bound depending on (n), not a probability comparison.

At the official splice:

* `q_line` is the actual MCA line-parameter field and the native denominator.
* `q_code` is the code alphabet and the list-decoding denominator.
* MCA may use `q_code` only when (q_{\rm line}=q_{\rm code}) or an exact normalization bridge is registered.
* `q_gen` may pay generated-domain entropy, locator or projection costs only where a theorem explicitly permits it.
* `q_chal` is an external protocol challenge field and cannot pay any MCA, code, generated-field or projection cost.
* The relevant M1 threshold is
  [
  T_{\rm line}=\left\lfloor q_{\rm line}/2^{128}\right\rfloor,
  ]
  not (q_{\rm chal}/2^{128}), and not generally (q_{\rm code}/2^{128}). 

## Collision and overcount audit

**Quotient/periodic structure.** It cannot simply be discarded. It must be either excluded by the exact aperiodicity predicate or covered by a separately bounded branch. A slope appearing in several branches must still be counted only once or controlled by a valid union bound.

**Contained incidences.** The official bad-slope definition requires transversality (v\notin V_T). A divisor or subset incidence model that includes contained supports is an overcount. Such an overcount is safe for an upper bound only if official bad slopes inject into it; it is not an equality.

**Same-slope collisions.** Cycle105 already passes to distinct (\theta) values. Multiple subsets producing the same (\theta) do not enlarge the numerator. No further multiplicity division is justified.

**Affine normalization.** A change (z\mapsto\theta=az+b) preserves cardinality exactly only when (a\ne0) in the actual line field. The external restriction (\theta\notin H) and all exceptional values must also be tracked. No such source certificate is included in the packet.

## Self-audit

**Exact implication proved here:** the ordinary Cycle105 truncated-inverse complement map requires (\sigma+1<n); the corrected all-endpoint map is

[
A\longmapsto(1-X^n)A^{-1}
\pmod{X^{\sigma+2}}.
]

I also established the exact logical placement of a corrected Cycle106 theorem: it can supply only the (U_{\rm ap}) component until an official bad-slope cover theorem is supplied.

**Not proved:** the aperiodic incidence bound, the missing official normalization/coverage theorem, a complete M1 numerator bound, or an official prize-level inequality.

**Status:** this is a source-chain audit plus an exact correction to complement duality. It is not an official prize certificate.

**First literal mathematical failure in the banked chain:** Cycle105’s line

[
1-X^n\equiv1\pmod{X^{\sigma+2}}
]

at (\sigma+1=n).

**First consequential failure on the Cycle106-to-prize chain:** the undefined phrase “aperiodic above corrected reserve,” followed immediately by the absent official bad-slope-to-(\Gamma) coverage theorem.

**Route to a full solution:** prove the explicitly quantified incidence theorem with an exact integer (B_{\rm ap}(n,\sigma)); prove `L-M1-OFFICIAL-BAD-SLOPE-TO-APERIODIC-GAMMA-COVER`; then verify

[
\max{U_{\rm res},U_{\rm high},
N_{\rm occ}+U_{\rm tan}+U_{\rm quot}+B_{\rm ap}}
\le
\left\lfloor q_{\rm line}/2^{128}\right\rfloor.
]

Without all three links, promotion past Cycle106 is unsafe.
