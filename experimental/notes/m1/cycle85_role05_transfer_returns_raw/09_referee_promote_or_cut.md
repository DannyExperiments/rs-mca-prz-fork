BANKABLE_LEMMA

## 1. Executive verdict

**Confidence: high.**

`L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER` is **true only after correction**:

[
\boxed{\text{packet distinct-slope count}=52{,}747{,}567{,}092}
]

and therefore

[
\boxed{M_C(6)\ge 52{,}747{,}567{,}092}
]

for the explicit Role05 research model.

It is **not** an exact evaluation of the whole MCA numerator, and it is **not** presently an official prize-frontier counterpacket. Its correct classification is:

[
\boxed{\text{finite-model obstruction certificate}}
]

It can also be registered as a research MCA lower term, but direct field normalization makes it either tangent-redundant or numerically inactive. The comparison with (2^{32}) has no native prize meaning.

---

## 2. Exact bankable theorem

### `L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY`

Let

[
F_0=\mathbf F_{17}[X]/(X^{16}+X^8+3),\qquad q_0=17^{16},
]

[
D=\mu_{256}=\langle\eta\rangle,\qquad
\eta=6X^9,\qquad
\beta=X+2\notin D.
]

Let (\mathcal P_0) be the Cycle65–68 admissible seven-slot support family. Every (T\in\mathcal P_0) has

[
|T|=113
]

and monic locator

[
P_T(Y)=\prod_{x\in T}(Y-x).
]

The banked shared-jet identities are

[
e_1(T)=1,\qquad e_2(T)=\cdots=e_5(T)=0,
]

so for all (T,T'\in\mathcal P_0),

[
\deg(P_T-P_{T'})\le 107.
]

Define

[
\rho_\beta(T)=P_T(\beta)=\prod_{x\in T}(\beta-x).
]

Then there is a nonconstant (t=1) affine syndrome line for the GRS-normalized code

[
C_0=\operatorname{RS}[F_0,D,137]
]

at reserve

[
\sigma=6,\qquad j=256-137-6=113,
]

such that:

1. every (T\in\mathcal P_0) gives a full-coordinate bad incidence on this line;
2. every such incidence is transverse/noncontained;
3. for (T,T'\in\mathcal P_0),

[
z_T=z_{T'}
\iff
\rho_\beta(T)=\rho_\beta(T');
]

4. consequently, the packet contribution to the distinct-slope set is exactly

[
|{z_T:T\in\mathcal P_0}|
========================

|{\rho_\beta(T):T\in\mathcal P_0}|.
]

Using the Cycle84 public certificate,

[
\boxed{
|{z_T:T\in\mathcal P_0}|=52{,}747{,}567{,}092
}
]

with packet slope-fiber spectrum

[
\begin{aligned}
\text{singleton slopes}&=52{,}747{,}567{,}080,\
\text{double slopes}&=12,\
\text{slopes of multiplicity }\ge3&=0,\
D_{\mathrm{ordered,offdiag}}&=24.
\end{aligned}
]

Therefore

[
\boxed{
M_{C_0}(6)\ge52{,}747{,}567{,}092.
}
]

The equality applies to the **packet contribution**, not to the whole MCA numerator.

---

## 3. Proof

Choose a reference (T_*\in\mathcal P_0). Homogenize the locators as

[
P_T^h(X_0,X_1)=\prod_{x\in T}(X_1-xX_0).
]

Let

[
A=X_0^6,\qquad B=P_{T_*}^h.
]

The shared six leading coefficients imply

[
P_T^h-P_{T_*}^h
]

is divisible by (X_0^6). Hence uniquely

[
P_T^h=A,U_T+B.
]

Moreover,

[
B(0,1)=1,
]

so (\gcd(A,B)=1). The binary complete-intersection/apolar correspondence therefore supplies a nonzero syndrome (s) whose apolar ideal is

[
I_s=(A,B),\qquad \deg A=6,\quad \deg B=113.
]

The coefficient of (B) in every packet locator is exactly (1), hence nonzero. Cycle62 Theorem A then gives a unique full-coordinate representation for every (T\in\mathcal P_0).

Now put

[
\Delta=6[\infty],\qquad \Delta^+=\Delta+[\beta].
]

All packet locators have the same **normalized restriction** to (\Delta), not merely the same projective class. Suppose two lifted classes in (G_{\Delta^+}) agree. Then for some (c\in F_0^\times),

[
P_T^h|*{\Delta^+}=cP*{T'}^h|_{\Delta^+}.
]

Restricting to (\Delta) gives (c=1), because both restrictions equal the same unit (B|_\Delta). Equality of the lifted classes is therefore equivalent to equality at the added point:

[
P_T(\beta)=P_{T'}(\beta).
]

Thus

[
[P_T|*{\Delta^+}]=[P*{T'}|*{\Delta^+}]
\iff
\rho*\beta(T)=\rho_\beta(T').
]

Cycle62 Theorem C and formula (4.4) identify equality of these lifted classes exactly with equality of MCA slopes. Any augmented-row or color normalization is a common affine bijection and cannot change collisions.

Cycle62 §6.6 proves automatic noncontainment in the shifted (t=1) slice. Hence every occupied packet color is an actual transverse MCA bad slope.

Finally Cycle84 supplies the exact occupancy and fiber histogram.

---

## 4. Exact correction to the proposed Cycle85 statement

The proposed statement should be replaced by:

> **Corrected Cycle85 transfer statement.**
> For the explicit Role05 packet, Cycle84 computes the exact number of distinct packet slopes on one transverse (t=1) MCA syndrome line:
> [
> M_{\mathcal P_0}^{\mathrm{line}}
> =52{,}747{,}567{,}092.
> ]
> Consequently the whole MCA numerator satisfies
> [
> M_{C_0}(6)\ge52{,}747{,}567{,}092.
> ]
> No equality for the whole numerator and no official-prize conclusion follow without a validated field/profile ledger.

The phrase “exact MCA numerator with value (\operatorname{Occ}(\beta))” is too strong.

---

## 5. Field and threshold adjudication

The native model field has exact order

[
q_0=17^{16}=48{,}661{,}191{,}875{,}666{,}868{,}481.
]

Because

[
\operatorname{ord}_{256}(17)=16,
]

the subgroup (D=\mu_{256}) generates all of (F_0). Thus, in the native model,

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}.
]

The value of (q_{\rm chal}) is not supplied and is irrelevant to both the numerator and its target.

The native targets are

[
T_{\rm line}=T_{\rm code}
=========================

\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor
=0.
]

Therefore

[
\operatorname{Occ}(\beta)>2^{32}
]

is **not** the native comparison. At the native field, even one bad slope already exceeds the (2^{-128}) target.

For an MCA line-field extension (F_0\subseteq \mathbf F_{17^d}), finite-field embedding forces (16\mid d). Under the official strict cap (q_{\rm line}<2^{256}), the only possibilities are:

| (q_{\rm line}) |                            (T_{\rm line}) | Effect of Cycle84 term                           |
| -------------- | ----------------------------------------: | ------------------------------------------------ |
| (17^{16})      |                                       (0) | trivial; no safe reserve                         |
| (17^{32})      |                                       (6) | fails, but tangent lower bound already dominates |
| (17^{48})      | (338{,}617{,}018{,}271{,}848{,}945{,}628) | (52{,}747{,}567{,}092) is inactive               |

There is no direct line-field extension containing (F_0) whose native target is near (2^{32}).

### Exact direct-normalization route cut

The original model has

[
\frac{k}{n}=\frac{137}{256},
]

which is outside the official rate set.

This rate defect can itself be repaired without changing occupancy: add a fixed set (S) of 18 new evaluation points to the domain and include all 18 in every packet support. Then

[
n'=274,\quad k'=137,\quad \sigma'=6,\quad j'=131,
]

and

[
\frac{k'}{n'}=\frac12.
]

If (Q_S) is the fixed marker locator, then

[
P_{T\cup S}(\beta)=Q_S(\beta)P_T(\beta),
]

so packet occupancy remains exactly (52{,}747{,}567{,}092).

Nevertheless:

* for (q_{\rm line}=17^{32}), the tangent lower bound (j'=131) already exceeds (T_{\rm line}=6), so Cycle84 is `SUBFRONTIER_REDUNDANT`;
* for (q_{\rm line}=17^{48}), the Cycle84 term is `NUMERICALLY_INACTIVE`.

Thus a **single directly normalized copy cannot move the official certified frontier**.

---

## 6. Objective separation

| Object                                        |                      Exact certified quantity |
| --------------------------------------------- | --------------------------------------------: |
| finite seven-slot input mass                  |                        (52{,}747{,}567{,}104) |
| packet distinct MCA slopes                    |                        (52{,}747{,}567{,}092) |
| whole MCA numerator                           |               at least (52{,}747{,}567{,}092) |
| scalar-list fiber of the (k+1) extension code | separate support count (52{,}747{,}567{,}104) |
| native MCA target over (F_{17^{16}})          |                                           (0) |
| informal benchmark                            |                  (2^{32}=4{,}294{,}967{,}296) |

The scalar-list support mass and MCA slope occupancy belong to different codes/reserves and different denominator rules.

---

## 7. Referee decisions

### 1. Strongest theorem-level statement now bankable

The exact packet-slope theorem above:

[
|\operatorname{Bad}*{\mathcal P_0}(\ell)|
=52{,}747{,}567{,}092,
\qquad
M*{C_0}(6)\ge52{,}747{,}567{,}092.
]

### 2. Status of `L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER`

**True only with corrections.**

It gives exact packet occupancy and a whole-numerator lower bound. It does not give an exact whole MCA numerator or an official frontier failure.

### 3. Classification

Primary classification:

[
\boxed{\text{finite-model obstruction certificate}}
]

Secondary checker classification:

* registerable as a `VALID_RESEARCH` lower term;
* directly normalized official-rate version is either subfrontier-redundant or inactive.

It is not an official prize-frontier counterpacket, but it is also not mathematically irrelevant.

### 4. What should be promoted into `tex/`

Promote:

1. `L-CYCLE85-EXACT-ROLE05-PACKET-SLOPE-OCCUPANCY`;
2. the exact packet slope-fiber histogram;
3. the fixed-marker padding lemma;
4. the direct field-normalization gap corollary.

Label the Cycle84 count explicitly as computer-assisted and finite-model.

### 5. What should remain experimental

Keep experimental:

* `Occ(beta)>2^32` as a purported prize comparison;
* whole-numerator equality;
* tensor or product amplification;
* any `Occ^2` claim;
* official-frontier movement;
* quotient-conditioned amplification;
* use of (q_{\rm code}) as the MCA denominator without a registered bridge.

### 6. Exact next lemma

```text
L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION
```

Let

[
\Omega={\rho_\beta(T):T\in\mathcal P_0}\subset F_0,
\qquad |\Omega|=52{,}747{,}567{,}092.
]

Over

[
L=\mathbf F_{17^{48}},
]

choose (\alpha\in L\setminus F_0). Construct one official-rate (t=1) RS instance and an injective support map

[
\Psi:\mathcal P_0\times\mathcal P_0\longrightarrow
\binom{D^{(2)}}{j^{(2)}}
]

on one affine syndrome line such that, after one common affine normalization,

[
z_{\Psi(T_1,T_2)}
=================

\rho_\beta(T_1)+\alpha\rho_\beta(T_2).
]

Because (1,\alpha) are (F_0)-linearly independent, this slope map is injective on (\Omega^2). It would give

[
M_{C^{(2)}}(\sigma^{(2)})
\ge |\Omega|^2
==============

2{,}782{,}305{,}834{,}125{,}041{,}336{,}464,
]

whereas

[
T_{\rm line}(17^{48})
=====================

338{,}617{,}018{,}271{,}848{,}945{,}628.
]

Hence

[
|\Omega|^2>T_{\rm line}(17^{48})
]

by a factor exceeding (8).

This exact composition theorem would convert the model certificate into an official-scale counterpacket, subject to the emitted rate, domain, reserve, field, and noncontainment certificate.

### 7. What PRZ should check first

PRZ should run the **profile-and-field normalization gate before quotient analysis**:

1. derive (k=137), reject the unpadded (137/256) official rate;
2. test the 18-marker rate-(1/2) normalization;
3. certify (q_{\rm gen}=17^{16});
4. enumerate the only admissible direct line degrees (16,32,48);
5. classify the packet as redundant at degree (32) and inactive at degree (48).

No further one-copy threshold work is warranted after that result.

---

## 8. Verification requirements

Add a deterministic bridge checker:

```text
V-CYCLE85-ROLE05-PACKET-TO-MCA-BRIDGE
```

It should verify:

* the finite-field and subgroup certificates;
* (\beta\notin D);
* tuple-to-support bijectivity and (|T|=113);
* (\deg(P_T-P_{T_*})\le107) from the local slot identities;
* (P_T=A U_T+B) with common nonzero (B)-coefficient;
* full-coordinate status;
* normalized (\Delta^+)-lift equivalence with (P_T(\beta));
* noncontainment;
* the code/reserve fingerprint;
* the Cycle84 artifact hashes and public replay receipt;
* native and extension targets.

Expected terminal certificate fields:

```text
decision = CYCLE85_ROLE05_PACKET_SLOPE_TRANSFER_VERIFIED
packet_supports = 52747567104
packet_distinct_slopes = 52747567092
packet_singleton_slopes = 52747567080
packet_double_slopes = 12
packet_m_max = 2
n = 256
k = 137
sigma = 6
j = 113
native_q_line = 48661191875666868481
native_T_line = 0
official_unpadded_rate_valid = false
```

The bridge checker must not rerun the Cycle84 MITM census.

---

## 9. Two-step execution plan with stop conditions

### Step 1 — close and promote Cycle85

Implement `V-CYCLE85-ROLE05-PACKET-TO-MCA-BRIDGE`, including the fixed-marker and field-gap checks.

**Promote** only if it verifies exact lift equality, full-coordinate status, and transversality.

**Stop and cut the transfer** if distinct (\rho_\beta)-values fail to give distinct (\Delta^+)-classes or if the packet cannot be bound to the stated code fingerprint.

### Step 2 — run exactly one amplification construction

Attempt `L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION` over (F_{17^{48}}).

**Positive stop:** an official checker instance validates and emits

[
M>T_{\rm line}.
]

**Negative stop:** prove that every admissible two-copy composition has color image contained in an affine (F_0)-coset, or otherwise cannot realize an (F_0)-linearly independent pair encoding on one transverse line. That would cut this amplification route.

---

## 10. Self-audit

1. **Proved:** exact packet slope occupancy and the lower bound
   [
   M_{C_0}(6)\ge52{,}747{,}567{,}092.
   ]
   **Not proved:** equality for the whole MCA numerator, an official frontier move, or a prize solution.

2. The result is a **finite/model certificate**, registerable as a research lower term. It is not presently official-prize-relevant.

3. The first potentially failing mathematical line is the identification of raw (P_T(\beta)) with normalized (\Delta^+)-lift classes. The shared exact (\Delta)-restriction repairs this. The first actual failure in the official chain is the profile/field normalization arrow.

4. (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}) are not conflated. Native MCA uses (T_{\rm line}), scalar lists use (T_{\rm code}), and (q_{\rm chal}) is unused. The (2^{-128}) target is applied by exact flooring. The (2^{32}) comparison is not native.

5. Quotient or periodic structure does not reduce the actual slope set once equality is tested in (G_{\Delta^+}). Contained incidences are excluded by the (t=1) theorem. Same-slope collisions are exactly the twelve double fibers already deducted in (\operatorname{Occ}). Affine color normalization is bijective.

6. The exact construction converting this result into a prize-level counterpacket is `L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION`; its required output and numerical threshold are stated above.
