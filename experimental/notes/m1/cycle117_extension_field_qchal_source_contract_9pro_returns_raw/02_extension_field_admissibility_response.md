## 1. LABEL

**PROOF**

**Scope:** source-level extension-field admissibility and promotion into the attached manuscripts’ raw support-wise line-MCA definition. This is not, by itself, an authority-pinned external Proximity Prize or protocol counterpacket.

**Confidence:** high.

## 2. EXECUTIVE VERDICT

The source text explicitly admits

[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\qquad H=\langle\theta\rangle,\quad |H|=512,
]

as a smooth multiplicative Reed–Solomon row.

Indeed, the row is an exact specialization of the source’s proved extension-tower theorem with

[
p=17,\qquad m=16,\qquad d=32,\qquad n=md=512,\qquad \rho=\frac12.
]

The order-(512) subgroup generates (\mathbb F_{17^{32}}), so there is no proper-subfield correction. The code field and line-parameter field are both (\mathbb F_{17^{32}}), and the MCA denominator is exactly (17^{32}). No separate (q_{\rm chal}) is defined.

“Not a deployed prime-field row” is therefore a limitation on deployment or external prize interpretation, not a rejection by the mathematical MCA definition. `RS_disproof_v3.tex` expressly distinguishes deployed prime-field examples from “generated extension-field examples” and includes the latter among its refuted cases.

## 3. SOURCE-PINNED ADMISSIBILITY LEMMA

### Lemma — admissibility of the Cycle116 extension row

Let

[
K=\mathbb F_{17^{32}},
\qquad
\theta\in K^\times,\quad \operatorname{ord}(\theta)=512,
\qquad
H=\langle\theta\rangle,
]

and let

[
C=\operatorname{RS}[K,H,256].
]

Then, under the source definitions in `RS_disproof_v3.tex` and `slackMCA_v3.tex`:

1. (H\le K^\times) is a smooth multiplicative domain because (|H|=512=2^9).
2. (H) generates (K) over (\mathbb F_{17}):
   [
   \mathbb F_{17}(H)=\mathbb F_{17}(\theta)=K.
   ]
3. (C) is an admitted smooth-domain Reed–Solomon code over a general prime-power field.
4. The line parameter is (z\in K), and
   [
   \epsilon_{\rm mca}(C,\delta)
   ============================

   \max_{f,g\in K^H}
   \frac{#{z\in K:z\text{ is support-wise MCA-bad}}}{|K|}.
   ]
   Hence
   [
   q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},
   \qquad q_{\rm chal}\text{ is unset}.
   ]
5. Consequently, the Cycle116 finite theorem promotes directly to the source’s raw MCA object:
   [
   \operatorname{LD}*{\rm sw}(C,262)
   \ge 52{,}747{,}567{,}092
   ]
   and
   [
   \epsilon*{\rm mca}!\left(C,\frac{125}{256}\right)
   \ge
   \frac{52{,}747{,}567{,}092}{17^{32}}.
   ]
6. Independently of Cycle116, the source’s own extension-tower theorem gives
   [
   \epsilon_{\rm mca}!\left(C,\frac{255}{512}\right)=1.
   ]

The last statement is at the weaker radius (255/512); it does not replace Cycle116’s stronger-radius result at (125/256=250/512).

## 4. PROOF DETAILS

### A. (H=\langle\theta\rangle) is exactly a source-valid smooth domain

`slackMCA_v3.tex:153–154` sets the vocabulary:

> (q) may be a general prime power; (D) or (H\le\mathbb F_q^\times) is a multiplicative subgroup, and “smooth” means its order is a power of two.

Thus (|H|=512=2^9) already satisfies the source definition of smoothness.

More decisively, `RS_disproof_v3.tex:373–383`, Lemma `lem:ext-coset-subgroup`, states that if

[
\operatorname{ord}_{md}(p)=d,
]

then an order-(md) subgroup of (\mathbb F_{p^d}^{\times}) exists and its generator has degree (d) over (\mathbb F_p).

`RS_disproof_v3.tex:394–413`, Lemma `lem:ext-tower-criterion`, proves that for

[
p\equiv1\pmod4,\qquad
m=2^{v_2(p-1)},\qquad
d\text{ a power of two},
]

one has (\operatorname{ord}_{md}(p)=d).

Substitute

[
p=17,\qquad
m=2^{v_2(16)}=16,\qquad
d=32.
]

Therefore

[
\operatorname{ord}_{512}(17)=32.
]

Equivalently, using the (2)-adic valuation,

[
v_2(17^e-1)=4+v_2(e)
]

for even (e). The divisibility (512=2^9\mid17^e-1) first occurs when (v_2(e)=5), namely at (e=32).

Hence an element of order (512) lies in no proper subfield of (\mathbb F_{17^{32}}), and

[
[\mathbb F_{17}(\theta):\mathbb F_{17}]=32.
]

Thus (\mathbb F_{17}(\theta)=\mathbb F_{17^{32}}).

Because (K^\times) is cyclic, it has a unique subgroup of order (512). The Cycle116 subgroup (\langle\theta\rangle) is therefore exactly the order-(512) subgroup supplied by the source tower lemma.

### B. The source extension theorem contains this exact row

`RS_disproof_v3.tex:416–425`, Theorem `thm:ext-smooth-towers`, considers

[
D\le\mathbb F_{p^d}^{\times},
\qquad |D|=n=md,
\qquad k=\rho n,
]

and proves

[
\epsilon_{\rm mca}
\left(
\operatorname{RS}[\mathbb F_{p^d},D,k],
1-\rho-\frac1n
\right)=1
]

provided

[
\rho(1-\rho)m^2\ge p.
]

For the target row,

[
\rho=\frac12,\qquad
n=16\cdot32=512,\qquad
k=256,
]

and

[
\rho(1-\rho)m^2
===============

# \frac14\cdot16^2

64
\ge17.
]

Therefore the theorem specializes exactly to

[
\epsilon_{\rm mca}
\left(
\operatorname{RS}[\mathbb F_{17^{32}},H,256],
\frac12-\frac1{512}
\right)
=======

1.

]

The proof at `RS_disproof_v3.tex:428–442` explicitly concludes that every

[
z\in\mathbb F_{17^{32}}
]

is bad for the line (x^{257}+zx^{256}). Thus both the extension-field code and the extension-field line parameter are directly present in a proved source theorem.

### C. Using (\mathbb F_{17^{32}}) as both code and line field is allowed

The source definitions use one field for the code alphabet, words, and line parameter.

`RS_disproof_v3.tex:110–114` defines, for (C\subseteq\mathbb F^D),

[
u_z=f+zg,\qquad z\in\mathbb F,
]

and normalizes the number of bad parameters by (|\mathbb F|).

Likewise, `slackMCA_v3.tex:643–647` defines

[
\epsilon_{\rm mca}(C,\delta)
============================

\max_{f,g\in\mathbb F^D}
\frac{1}{|\mathbb F|}
#{z:z\text{ is support-wise MCA-bad}}.
]

For

[
C=\operatorname{RS}[\mathbb F_{17^{32}},H,256],
]

the source therefore fixes

[
q_{\rm code}=q_{\rm line}=17^{32}.
]

The definition maximizes over arbitrary words (f,g\in K^H); it does not require the Cycle116 lifted line to be a monomial line or to consist of polynomial codewords.

### D. “Not deployed prime-field” is not a mathematical exclusion

`RS_disproof_v3.tex:371` says:

> “The prime-field quotient ladder already gives the deployed-field disproof. The following scalar-coset construction gives generated extension-field examples…”

The distinction is explicitly between deployment classes, not admissible mathematical rows.

More conclusively, the scope paragraph at `RS_disproof_v3.tex:505–509` includes among the refuted cases:

> “generated extension-field smooth towers.”

Thus the Cycle116 warning “not an accepted/deployed prime-field theorem” remains correct as a deployment and prize-scope warning, but it does not cut source-level MCA admissibility.

### E. The subfield correction produces no smaller field here

`slackMCA_v3.tex:600–601`, Remark `rem:subfield`, says that if the domain lies in a proper subfield (\mathbb F_{q_0}\subsetneq\mathbb F_q), locator coefficients and list-side entropy pigeonholes are governed by (q_0), not by the larger ambient alphabet.

That hypothesis fails here. Every proper subfield of (\mathbb F_{17^{32}}) is (\mathbb F_{17^e}) for a proper divisor (e\mid32), so (e\in{1,2,4,8,16}). But

[
v_2(17^e-1)\le8
]

for those (e), so none of their multiplicative groups contains an element of order (512). Therefore

[
H\nsubseteq\mathbb F_{17^e}
\quad\text{for every }e<32.
]

There is no hidden (q_0).

The related subfield-confinement theorem in `slackMCA_v3.tex:1533–1539` requires (D\subseteq B) for a proper subfield (B). No such (B) exists for this domain.

A conceptual distinction remains:

* (q_{\rm gen}) controls the field of definition and generated-field corrections.
* (q_{\rm line}) is the actual denominator in raw MCA.

Here both happen to equal (17^{32}); they are not separate denominator factors.

### F. Promotion of the Cycle116 finite theorem

Cycle116 proves a finite theorem for this exact row:

[
\operatorname{LD}_{\rm sw}(C,262)\ge N,
\qquad N=52{,}747{,}567{,}092.
]

Since

[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil
============

262,
]

the source definition gives

[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
=================================================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{17^{32}}
\ge
\frac{N}{17^{32}}.
]

This is source promotion of the finite support-wise MCA theorem. It is not promotion to ordinary list decoding or to a protocol-soundness claim.

## 5. FIELD AND PARAMETER LEDGER

| Quantity                   |             Value | Reason                                                                                  |   |       |
| -------------------------- | ----------------: | --------------------------------------------------------------------------------------- | - | ----- |
| (q_{\rm gen})              |         (17^{32}) | (\operatorname{ord}_{512}(17)=32), so (H) generates the full field                      |   |       |
| (q_{\rm code})             |         (17^{32}) | The row is (\operatorname{RS}[\mathbb F_{17^{32}},H,256])                               |   |       |
| (q_{\rm line})             |         (17^{32}) | The source samples (z) from the same field (\mathbb F) used in (C\subseteq\mathbb F^D)  |   |       |
| (q_{\rm chal})             |      unset / null | Neither source defines a distinct verifier or protocol challenge field for this theorem |   |       |
| (n)                        |             (512) | (                                                                                       | H | =512) |
| (k)                        |             (256) | Target row dimension                                                                    |   |       |
| (\rho)                     |             (1/2) | (k/n)                                                                                   |   |       |
| Cycle116 agreement         |             (262) | Six symbols beyond (k)                                                                  |   |       |
| Cycle116 radius            | (125/256=250/512) | (1-262/512)                                                                             |   |       |
| Direct source-tower radius |         (255/512) | (1-\rho-1/n)                                                                            |   |       |

The three equal field sizes are conceptually distinct ledger entries. They are not multiplied or charged more than once.

## 6. EVENT RETENTION / CHARGE AUDIT

| Possible loss          | Source status                                                                                                                                                           | Effect on Cycle116 numerator                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint               | No slope-endpoint deletion exists. The source counts all finite (z\in K).                                                                                               | None. Cycle116 slopes are finite and nonzero because (P_T(\beta)\ne0).                                                                                         |
| Periodic               | No periodic exclusion occurs in the raw MCA definition. `slackMCA_v3.tex:1043–1045` distinguishes raw counts from a possible future protocol-dependent aperiodic count. | None under the source definition.                                                                                                                              |
| Quotient               | Quotient-periodic lines are separated only in later positive conjectural packing normalizations; raw (\epsilon_{\rm mca}) retains their contribution.                   | None. No proof that the lifted Cycle116 line is quotient-periodic is needed.                                                                                   |
| Tangent                | Tangent behavior is an included lower-bound floor, not a rejection rule (`slackMCA_v3.tex:667–674`, `1210–1218`).                                                       | None. Moreover, Cycle116 proves the direction (g) is not code-explainable on each witness support, so its witnesses are not tangent in that normal-form sense. |
| Contained line/support | This is the genuine source exclusion: condition (ii) requires no simultaneous explanations of (f) and (g).                                                              | Paid. Cycle116’s Vandermonde argument proves (g) is not explainable on every witness support.                                                                  |
| Affine-color           | No affine-color predicate or quotient appears in either source MCA definition.                                                                                          | None. The Cycle84 color shell was already imposed before the certified distinct-slope count.                                                                   |
| Retained-event map     | Absent from the source. The source event is simply a distinct bad field element (z).                                                                                    | None.                                                                                                                                                          |
| Charge registry        | Absent from the source.                                                                                                                                                 | None; no charge may be invented.                                                                                                                               |

The numerator (N) already counts distinct slope values after same-slope collisions. It does not count witness-support multiplicity as additional events.

## 7. LINE-DECODING VS. (\operatorname{LD}_{\rm sw}) ADAPTER

The exact adapter in `m2_line_decoding_mca_bridge.md:43–53` is

[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{
\operatorname{LD}_{\rm sw}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)
}{|\mathbb F|}.
]

For this row,

[
\left\lceil
\left(1-\frac{125}{256}\right)512
\right\rceil=262,
]

hence

[
\epsilon_{\rm mca}
!\left(C,\frac{125}{256}\right)
===============================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{17^{32}}.
]

This is support-wise line decoding: one affine line has many distinct noncontained slopes, possibly with different witness supports and explaining codewords.

It does **not** prove that a single received word has (N) nearby codewords. Therefore it is not an ordinary Reed–Solomon list-decoding lower bound of size (N).

## 8. VERIFIER / REVIEWER CHECKLIST

* The Cycle116 verifier certifies (\operatorname{ord}(\theta)=512), (|H|=512), and (H) generates (K=\mathbb F_{17^{32}}).
* The source tower criterion independently gives (\operatorname{ord}_{512}(17)=32).
* The extension-tower theorem applies with (p=17,m=16,d=32,\rho=1/2).
* The source’s code field and line field are both (K).
* The only source-level event rejection—simultaneous explanation of (f) and (g)—is excluded by the Cycle116 Vandermonde proof.
* No source endpoint, retained-event, affine-color, or charge map exists.
* The exact security arithmetic is
  [
  \left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
  ]
  Thus any integer numerator at least (7) crosses (2^{-128}); the important mathematical content is the construction of (52{,}747{,}567{,}092) distinct support-wise bad slopes at agreement (262), not the final threshold comparison.
* The executable Cycle116 slot-log gauge is (\beta=X+2). Older display prose uses the primitive gauge (X+1). The gauges must not be conflated when quoting logarithms; the occupancy and field-admissibility conclusions are invariant under the consistently verified gauge change.

## 9. SELF-AUDIT

1. **Finite versus official:** Cycle116 is used only as a finite (\operatorname{LD}_{\rm sw})/support-wise MCA theorem. The new conclusion is source-manuscript admissibility, not an external official-prize contract.
2. **Exact source clause:** Acceptance is pinned to `RS_disproof_v3.tex:373–425`, especially Theorem `thm:ext-smooth-towers`, and to the MCA definitions at `RS_disproof_v3.tex:110–114` and `slackMCA_v3.tex:643–647`.
3. **Field ledger:** (q_{\rm gen},q_{\rm code},q_{\rm line}) are distinguished and each equals (17^{32}); (q_{\rm chal}) remains unset.
4. **Extension admissibility:** Proven through (\operatorname{ord}_{512}(17)=32) and the source tower theorem.
5. **Event retention:** All named loss mechanisms were audited; only containedness is a source predicate, and it is paid.
6. **MCA versus ordinary list decoding:** No ordinary list-decoding claim is made.
7. **Line adapter:** The exact ceiling formula is supplied and evaluates to (262).
8. **(2^{-128}):** The floor is (6); threshold crossing is noted as secondary.
9. **Primitive-log gauge:** Executable (\beta=X+2) is preserved; (X+1) is identified only as the older display gauge.
10. **Terminal discipline:** `PROOF` is justified because the attached source itself expressly admits—and proves a theorem for—the exact extension-field row.

## 10. NEXT EXACT STEP

No accepted-field compiler is needed for the source vocabulary. The only remaining wall, if an external official-prize or protocol claim is sought, is an authority-pinned wrapper specifying that those external rules adopt the attached raw support-wise MCA definition without additional protocol-specific exclusions.
