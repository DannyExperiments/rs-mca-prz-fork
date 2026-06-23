# LABEL

**BANKABLE_LEMMA**

## EXECUTIVE VERDICT

The Cycle116 ledger is correct for the finite code and for the attached manuscript’s raw support-wise line-MCA definition:

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},\qquad
q_{\rm chal}=\text{null}.
]

Here `null` means **no additional challenge field is instantiated**. The only sampling field in the source definition is already the line-parameter field (F), so the unique MCA denominator is

[
q_{\rm line}=|F|=17^{32}.
]

Consequently,

[
\varepsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
\ge \frac{52{,}747{,}567{,}092}{17^{32}}

> 2^{-128}.
> ]

This is bankable as a finite/source q-ledger theorem. It is not yet an authority-pinned official-prize ledger because the packet contains no official clause defining a separate (q_{\rm chal}), challenge sampling set, or postprocessing/retained-event predicate.

**Confidence:** high for the finite and attached-source theorem; unknown for an external official-prize wrapper.

---

# SOURCE-PINNED THEOREM

### Exact no-extra-denominator q-ledger lemma

Let

[
K=\mathbb F_{17^{32}},\qquad
H=\langle\theta\rangle\le K^\times,\qquad
|H|=512,
]

where (H) generates (K) over (\mathbb F_{17}), and let

[
C=\operatorname{RS}[K,H,256].
]

Assume the Cycle116 finite certificate

[
\operatorname{LD}_{\rm sw}(C,262)\ge
N,\qquad N=52{,}747{,}567{,}092.
]

Then, under the support-wise line-MCA definition in the attached source,

[
\boxed{
\varepsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
====================================================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{|K|}
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}

> 2^{-128}.
> }
> ]

The corresponding field ledger is

[
\boxed{
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32},
\qquad q_{\rm chal}=\text{null}.
}
]

No factor (q_{\rm gen}), (q_{\rm code}), or (q_{\rm chal}) is to be multiplied into the denominator.

---

# PROOF DETAILS

## 1. The source accepts the extension-field row

The general RS object is defined in `context/source/RS_disproof_v3.tex`, lines 91–95:

[
\operatorname{RS}[F,D,k]
========================

{(P(x))_{x\in D}:\deg P<k},
]

with the stated counterexamples using multiplicative subgroups (D\le F^\times) of power-of-two order. Thus the basic definition is not restricted to prime fields.

The extension-field acceptance is also explicit, not merely implicit:

* `RS_disproof_v3.tex`, lines 369–371, introduces “generated extension-field examples”.
* Lines 373–383 give the scalar-coset subgroup lemma over (\mathbb F_{p^d}).
* Lines 416–425 state the smooth extension-tower theorem for
  (\operatorname{RS}[\mathbb F_{p^d},D,k]).

For the Cycle116 row, set

[
p=17,\qquad m=16,\qquad d=32,\qquad n=md=512,\qquad \rho=\frac12.
]

The source hypotheses hold:

[
\operatorname{ord}_{512}(17)=32,
]

and

[
\rho(1-\rho)m^2
===============

# \frac14\cdot 16^2

64
\ge 17.
]

Hence the source’s explicit extension theorem itself applies to the same unique order-(512) subgroup of (\mathbb F_{17^{32}}^\times).

That source theorem gives error one at radius (255/512). It is not being used to infer the Cycle116 bound at the smaller radius

[
\frac{125}{256}=\frac{250}{512};
]

its role here is to make extension-field and smooth-domain admissibility unambiguous.

## 2. (q_{\rm gen}=17^{32})

The symbol (q_{\rm gen}) is reviewer-ledger notation, not literal source notation. Its meaning here is

[
q_{\rm gen}
===========

\left|\mathbb F_{17}(H)\right|.
]

Since (H=\langle\theta\rangle) and (\theta) has order (512=2^9), the degree of (\theta) over (\mathbb F_{17}) is the multiplicative order of (17) modulo (512).

For every (e\ge1),

[
v_2(17^e-1)=v_2(17-1)+v_2(e)=4+v_2(e).
]

Thus (512\mid17^e-1) exactly when (4+v_2(e)\ge9), whose least solution is (e=32). Therefore

[
[\mathbb F_{17}(\theta):\mathbb F_{17}]=32
]

and

[
\mathbb F_{17}(H)=\mathbb F_{17}(\theta)=\mathbb F_{17^{32}}.
]

Hence

[
q_{\rm gen}=17^{32}.
]

This agrees with the generated-field/Frobenius receipt in the Cycle116 verifier.

## 3. (q_{\rm code}=17^{32})

The symbol (q_{\rm code}) is also reviewer-ledger notation. The attached source writes the code as

[
C=\operatorname{RS}[F,D,k]\subseteq F^D.
]

For the Cycle116 row, (F=K=\mathbb F_{17^{32}}). Therefore the code alphabet has cardinality

[
q_{\rm code}=|K|=17^{32}.
]

## 4. (q_{\rm line}=17^{32}) is the exact denominator

The controlling source clause is `RS_disproof_v3.tex`, lines 110–114:

> For a line (u_z=f+zg), the bad parameters are (z\in F), and
> [
> \varepsilon_{\rm mca}(C,\delta)
> ===============================
>
> \max_{f,g}
> \frac{#{z\in F:z\text{ bad}}}{|F|}.
> ]

The same definition appears in `slackMCA_v3.tex`, lines 643–650, with denominator (1/|F|).

Thus the line sample space is exactly (K), and

[
q_{\rm line}=|K|=17^{32}.
]

There is no freedom to normalize this particular (\varepsilon_{\rm mca}) by (q_{\rm gen}), by the subgroup order (512), by (2^{128}), or by an additional field.

## 5. Radius-to-agreement conversion

The exact bridge in `context/source/m2_line_decoding_mca_bridge.md`, lines 31–53, defines

[
\operatorname{LD}_{\rm sw}(C,a)
===============================

\max_{f,g}
#{z\in F:z\text{ has a support-wise noncontained witness of size }\ge a}
]

and proves

[
\varepsilon_{\rm mca}(C,\delta)
===============================

\frac{
\operatorname{LD}_{\rm sw}
\bigl(C,\lceil(1-\delta)n\rceil\bigr)
}{|F|}.
]

Here

[
\left(1-\frac{125}{256}\right)512
=================================

# \frac{131}{256}\cdot512

262,
]

so there is no ceiling ambiguity:

[
\varepsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
====================================================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{17^{32}}.
]

## 6. (q_{\rm chal}) is not a second denominator

No symbol (q_{\rm chal}), and no separate challenge-field denominator, is defined anywhere in the three primary source files.

The attached manuscripts sometimes use the word “challenge”, but their challenge-parameter statements continue to write

[
C=\operatorname{RS}[\mathbb F_q,H,k]
]

and normalize MCA by the same (q=|\mathbb F_q|). For example, `slackMCA_v3.tex`, lines 1464–1482 and 1505–1510, treats “challenge parameters” while retaining the single field (q).

Therefore:

[
q_{\rm chal}=\text{null}
]

is the correct finite-code metadata status. It means:

* the line challenge (z) already ranges over the (q_{\rm line})-element field;
* no additional protocol challenge field has been instantiated;
* no extra denominator is available.

If a later official wrapper defines (q_{\rm chal}=q_{\rm line}), that is merely an alias for the same sampling space and cannot justify division by (q_{\rm line}q_{\rm chal}). If it defines a different challenge set (Z), the required quantity becomes

[
\frac{|\operatorname{Bad}\cap Z|}{|Z|},
]

which requires a new intersection/retention theorem.

---

# FIELD AND PARAMETER LEDGER

| Symbol         | Source status                                                            | Meaning in this theorem                     |     Value | Ledger use                                              |
| -------------- | ------------------------------------------------------------------------ | ------------------------------------------- | --------: | ------------------------------------------------------- |
| (q_{\rm gen})  | Reviewer alias; source uses generated-field/field-of-definition language | Size of (\mathbb F_{17}(H))                 | (17^{32}) | Certifies that (H) is not confined to a proper subfield |
| (q_{\rm code}) | Reviewer alias; source writes (F_q)                                      | Alphabet size of (C\subseteq K^H)           | (17^{32}) | Describes the RS code                                   |
| (q_{\rm line}) | Reviewer alias pinned by `def:mca`                                       | Number of affine parameters (z\in K)        | (17^{32}) | **The sole MCA denominator**                            |
| (q_{\rm chal}) | Not source-defined                                                       | Additional protocol challenge field, if any |      null | No denominator and no entropy factor                    |

The three equal numerical values do not represent three independent random choices. They are three semantic roles played by the same field in this generated-field row.

---

# EXACT ARITHMETIC

## Field size

[
\boxed{
17^{32}
=======

2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361.
}
]

Also,

[
2^{128}
=======

340{,}282{,}366{,}920{,}938{,}463{,}463{,}374{,}607{,}431{,}768{,}211{,}456.
]

The exact Euclidean decomposition is

[
17^{32}
=======

6\cdot2^{128}
+
326{,}217{,}393{,}234{,}836{,}465{,}063{,}858{,}652{,}730{,}341{,}978{,}625,
]

with the remainder strictly between (0) and (2^{128}). Hence

[
\boxed{\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.}
]

## Strict threshold comparison

For an integral numerator (N),

[
\frac N{17^{32}}>2^{-128}
\iff
N>\frac{17^{32}}{2^{128}}
\iff
N\ge7.
]

Since

[
N=52{,}747{,}567{,}092,
]

the inequality is strict. Equivalently,

[
2^{128}N-17^{32}
================

17{,}949{,}066{,}977{,}018{,}851{,}466{,}377{,}275{,}544{,}392{,}249{,}248{,}647{,}251{,}758{,}591

> 0.
> ]

Numerically,

[
\frac{N}{17^{32}}
\approx2.22759866579\times10^{-29},
\qquad
2^{-128}\approx2.93873587706\times10^{-39}.
]

The lower bound exceeds (2^{-128}) by a factor of approximately

[
7.580125465\times10^9.
]

Thus the floor-(6) comparison is correct but is not the substantive mathematical achievement. The substantive content is the certified numerator of more than (52) billion distinct bad slopes.

---

# EVENT RETENTION / CHARGE AUDIT

The raw source definition sends the bad set directly to the numerator. Its only substantive tests are agreement on a sufficiently large common support and failure of simultaneous explanation.

| Possible loss  | Attached-source status                                                                                                                                               | Effect on the Cycle116 numerator       |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Endpoint       | No projective (z=\infty) event appears. Parameters are (z\in F). Also (125/256<1/2), so this is not the capacity endpoint.                                           | No loss                                |
| Periodic       | Not excluded by `def:mca`. Later periodic classifications concern structure or proposed corrected bounds.                                                            | No loss in raw (\varepsilon_{\rm mca}) |
| Quotient       | Raw quotient-periodic slopes remain bad slopes. `slackMCA_v3.tex`, lines 1043–1045, explicitly distinguishes raw counts from possible protocol-dependent absorption. | No loss in raw (\varepsilon_{\rm mca}) |
| Tangent        | The source treats the tangent floor as an unavoidable contribution, not as an exclusion.                                                                             | No denominator or subtraction          |
| Contained line | Already handled by the source’s simultaneous-explanation condition. Cycle116’s Vandermonde argument proves its witnesses noncontained.                               | All certified events pass              |
| Affine-color   | No such rule occurs in the source MCA definition. The finite color restriction was already paid inside the Cycle84 census.                                           | No second color quotient               |
| Retained-event | No retained-event map is defined in the attached source.                                                                                                             | Absent                                 |
| Charge         | No charge map subtracting Cycle116 events is defined. Tangent and quotient terms appear as contributions in corrected conjectures, not post-count denominators.      | Absent                                 |

Therefore the attached source retains all (N) certified events in its **raw** support-wise MCA numerator.

This does not prove that an external protocol or official prize formulation lacks a different event-retention map. The source itself warns in `slackMCA_v3.tex`, lines 1043–1045, that which raw or aperiodic number is operational depends on the protocol definition.

---

# LINE-DECODING VS `LD_SW` ADAPTER

The exact source adapter is

[
\boxed{
\varepsilon_{\rm mca}(C,\delta)
===============================

\frac{
\operatorname{LD}_{\rm sw}
\bigl(C,\lceil(1-\delta)n\rceil\bigr)
}{|F|}.
}
]

For the present parameters,

[
\boxed{
\varepsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
====================================================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{17^{32}}.
}
]

The theorem therefore establishes a support-wise noncontained line-decoding numerator lower bound.

It does **not** establish an ordinary RS list-size lower bound of (N). Ordinary list decoding asks for one fixed received word having many nearby codewords; Cycle116 instead gives one affine line having many slopes, generally with slope-dependent supports and explaining codewords. The separate list-decoding analogue in `RS_disproof_v3.tex`, line 103, is not obtained from this certificate.

---

# VERIFIER / REVIEWER CHECKLIST

* Packet checksums in `SHA256SUMS.txt`: verified.
* `cycle116_role08_verifier/run_verifier.sh`: locally replayed with exit code (0).
* Terminal decision: `CYCLE116_TRANSFER_CERTIFICATE_VERIFIED`.
* Generated-field check: passed.
* (\theta) order: (512).
* (H) generates (\mathbb F_{17^{32}}): passed.
* Numerator: (52{,}747{,}567{,}092).
* Denominator label: `q_line`.
* `q_chal`: `null`.
* Strict integer comparison: `2^128*N > 17^32`.
* Scope flags for ordinary list decoding, protocol soundness, asymptotics, and official-prize status: all false.

The primitive-log metadata warning must be preserved: older display prose uses an (X+1) primitive-log gauge, while executable slot logs and the verified algebra use

[
\beta=X+2.
]

Both are primitive, but the publication-facing receipt should use or explicitly reindex to the executable (\beta=X+2) gauge.

---

# SELF-AUDIT

1. **Finite versus official:** only the finite/source support-wise theorem is claimed.
2. **Exact source clause:** extension fields are accepted by `RS_disproof_v3.tex`, lines 91–95 and 369–425; normalization is fixed by lines 110–114.
3. **Field ledger:** all four ledger roles are separated.
4. **Extension admissibility:** proved via (\operatorname{ord}_{512}(17)=32) and the explicit extension theorem.
5. **Event retention:** every requested category was checked; absent rules were stated absent.
6. **MCA versus list decoding:** no ordinary list-size claim is made.
7. **Line adapter:** the exact (LD_{\rm sw}) equality and agreement conversion are supplied.
8. **(2^{-128}) comparison:** floor (=6) is recorded as correct but mathematically secondary.
9. **Primitive-log gauge:** executable (\beta=X+2) warning retained.
10. **Terminal discipline:** `BANKABLE_LEMMA` is used because official-prize challenge and retention clauses remain unpinned.

---

# NEXT EXACT STEP

The smallest missing official-wrapper theorem is:

> **Authority-pinned challenge-sampling and retention identification.**
> Prove that the official challenge sample space is (Z=K=\mathbb F_{17^{32}}), that the official bad-event predicate agrees with the source support-wise MCA predicate, and that no endpoint, periodic, quotient, affine-color, retained-event, or charge postprocessing removes the Cycle116 slopes.

Under that clause, any official (q_{\rm chal}) would either be absent or merely the alias

[
q_{\rm chal}=q_{\rm line}=17^{32},
]

and the denominator theorem above would promote unchanged.
