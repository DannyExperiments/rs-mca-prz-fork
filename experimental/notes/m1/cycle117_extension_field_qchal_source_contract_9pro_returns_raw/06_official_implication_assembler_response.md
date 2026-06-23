# LABEL

**PROOF**

**Final status:** `SOURCE_ACCEPTED_MCA_COUNTERPACKET`
**Official-prize promotion:** `ROUTE_CUT — SOURCE_CONTRACT_MISSING`
**Confidence:** high

Here “source accepted” means accepted by the attached mathematical manuscripts. It does not mean accepted by an authority-pinned Proximity Prize contract.

## Strongest proved theorem

**Theorem.** Let
[
K=\mathbb F_{17^{32}},\qquad H=\langle\theta\rangle\le K^\times,
\qquad |H|=512,\qquad C=\operatorname{RS}[K,H,256].
]
Assume (H) generates (K). Then there exist (f,g\in K^H) and a set
[
Z\subseteq K,\qquad |Z|\ge N:=52{,}747{,}567{,}092,
]
such that for every (z\in Z) there is a support (S_z\subseteq H) of size (262) and a codeword (c_z\in C) satisfying
[
(f+zg)|*{S_z}=c_z|*{S_z},
]
while no pair (c_f,c_g\in C) simultaneously satisfies
[
f|*{S_z}=c_f|*{S_z},\qquad g|*{S_z}=c_g|*{S_z}.
]

Consequently,
[
\operatorname{LD}*{\rm sw}(C,262)\ge 52{,}747{,}567{,}092,
]
and, since
[
\left\lceil\left(1-\frac{125}{256}\right)512\right\rceil=262,
]
[
\epsilon*{\rm mca}!\left(C,\frac{125}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}

> 2^{-128}.
> ]

This is a source-valid support-wise line-MCA/(\operatorname{LD}_{\rm sw}) counterpacket. It is not ordinary list decoding or an official prize counterpacket.

## Source acceptance of the extension-field row

The row is admitted explicitly, not merely by inference.

* `context/source/slackMCA_v3.tex:153-154` defines smooth multiplicative RS rows as subgroups of (\mathbb F_q^\times) of power-of-two order.
* More decisively, `context/source/RS_disproof_v3.tex:394-425` proves a smooth extension-tower theorem.

Instantiate that theorem with
[
p=17,\qquad m=2^{\nu_2(17-1)}=16,\qquad d=32,\qquad \rho=\frac12.
]
Its 2-adic criterion gives
[
\operatorname{ord}*{md}(p)=\operatorname{ord}*{512}(17)=32.
]
Thus an element of order (512) has degree (32) over (\mathbb F_{17}), so
[
\mathbb F_{17}(\theta)=\mathbb F_{17^{32}}.
]
Moreover,
[
\rho(1-\rho)m^2=\frac14\cdot16^2=64\ge17,
]
and (k=\rho md=256). Since (K^\times) is cyclic, its subgroup of order (512) is unique, so the theorem’s domain is precisely (H).

The source theorem independently gives
[
\epsilon_{\rm mca}(C,255/512)=1.
]
Cycle116 supplies the distinct, deeper-radius result at
[
125/256=250/512,
]
equivalently agreement (262) rather than (257).

## Exact source definition and field ledger

The governing definition is `context/source/RS_disproof_v3.tex:110-115`, equivalently `slackMCA_v3.tex:639-653`: (z) ranges over the same field (\mathbb F) as the line, and the number of bad parameters is divided by (|\mathbb F|).

| Ledger field   |     Value | Role                                                     |
| -------------- | --------: | -------------------------------------------------------- |
| (q_{\rm gen})  | (17^{32}) | Generated field; source notation corresponds to (q_D)    |
| (q_{\rm code}) | (17^{32}) | RS alphabet/coefficient field (K)                        |
| (q_{\rm line}) | (17^{32}) | Parameter field (z\in K); the sole MCA denominator       |
| (q_{\rm chal}) |    `null` | Not defined or used by the attached code/line-MCA source |

Although the first three values coincide, they are logically distinct. No generated-field, alphabet-field, or line-field factor is counted twice.

## Event-retention and charge audit

Under the raw source definition, all (N) designated Cycle116 slopes remain bad parameters.

| Possible loss                      | Status                     | Reason                                                                                                                                |
| ---------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Endpoint deletion                  | `ABSENT_FROM_SOURCE`       | The definition counts finite (z\in K); Cycle116 has (P_T(\beta)\ne0), so every slope is finite                                        |
| Periodic quotienting               | `PRESENT_BUT_IRRELEVANT`   | Periodicity appears in structural/positive-conjecture bookkeeping, not as a quotient of raw (\epsilon_{\rm mca})                      |
| Quotient-profile/core charge       | `PRESENT_BUT_IRRELEVANT`   | The profile separates mechanisms but does not delete raw bad slopes                                                                   |
| Tangent exclusion                  | `PRESENT_AND_PAID`         | The source tangent floor is a lower bound; Cycle116 additionally proves the direction is not code-explainable on its witness supports |
| Contained-line/support exclusion   | `PRESENT_AND_PAID`         | This is exactly condition (ii) of the source definition, and Cycle116 proves noncontainment                                           |
| Same-slope collision               | `PRESENT_AND_PAID`         | (N) is already the number of distinct locator values/slopes after fiber collisions                                                    |
| Affine-color normalization         | `ABSENT_FROM_SOURCE`       | No such rule occurs in the MCA definition                                                                                             |
| Retained-event map                 | `ABSENT_FROM_SOURCE`       | No secondary retained-event projection is defined                                                                                     |
| Charge registry or (AP_{\rm corr}) | `ABSENT_FROM_SOURCE`       | No charge/removal mechanism is supplied                                                                                               |
| Protocol challenge filtering       | `UNKNOWN_MISSING_CONTRACT` | Relevant only to a later official-protocol promotion                                                                                  |

The source itself distinguishes raw bad-slope counts from conjectural aperiodic normalization in `slackMCA_v3.tex:1044` and `1255-1256`; that normalization is not part of Definitions `def:mca`.

## Line decoding versus ordinary list decoding

`context/source/m2_line_decoding_mca_bridge.md:14-53` defines
[
\operatorname{LD}_{\rm sw}(C,a)
===============================

\max_{f,g}#{z:\text{(z) has a support-wise noncontained witness of size }\ge a}
]
and proves the exact adapter
[
\epsilon_{\rm mca}(C,\delta)
============================

\frac{\operatorname{LD}_{\rm sw}
!\left(C,\lceil(1-\delta)n\rceil\right)}
{|\mathbb F|}.
]

Thus Cycle116 obstructs any line-decoding assertion whose exact conclusion is
[
\operatorname{LD}_{\rm sw}(C,262)<N.
]

It does **not** establish the broader external predicate
((\delta,a_{\rm LD},n+1))-line-decodable: the note leaves matching that external definition as an audit item at lines `408-414`. It also does not prove that one received word has (N) nearby codewords. Therefore neither ordinary list decoding nor general close-point line decoding may be claimed.

## Exact official-prize ROUTE_CUT

The first broken implication is
[
\boxed{
\text{attached-manuscript MCA counterpacket}
;\not\Rightarrow;
\text{official Proximity Prize counterpacket}.
}
]

`context/source/RS_disproof_v3.tex:106-108` expressly describes its conjecture as a transcription of a “natural reading” into a minimal no-slack, same-support, two-word line formulation. Lines `86` and `505-509` exclude slacked, curve-constrained, and protocol-specific formulations from the claim.

The packet contains no authority/version-pinned official clause declaring that:

1. generated extension-field rows such as (RS[\mathbb F_{17^{32}},H,256]) are official challenge rows;
2. the official challenge samples (z) over (K);
3. (q_{\rm chal}=q_{\rm line}), or even defines (q_{\rm chal});
4. no endpoint, retained-event, quotient, affine-color, or charge processing applies.

Hence `OFFICIAL_PRIZE_COUNTERPACKET` is not proved. The official branch remains `SOURCE_CONTRACT_MISSING`, not `SOURCE_REJECTED`.

## PRZ-facing theorem statement — 123 words

> **Theorem (source-scoped finite MCA counterpacket).** Let (K=\mathbb F_{17^{32}}), let (H=\langle\theta\rangle\le K^\times) have order (512) and generate (K), and let (C=RS[K,H,256]). The attached manuscripts admit this as a smooth generated extension-field Reed–Solomon row. There exist (f,g\in K^H) and (Z\subseteq K), (|Z|\ge52{,}747{,}567{,}092), such that every (z\in Z) has a 262-point support explaining (f+zg) by a codeword, but not simultaneously explaining (f) and (g). Therefore
> [
> LD_{\rm sw}(C,262)\ge52{,}747{,}567{,}092,\qquad
> \epsilon_{\rm mca}(C,125/256)\ge\frac{52{,}747{,}567{,}092}{17^{32}}>2^{-128}.
> ]
> Here (q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{32}) and (q_{\rm chal}) is undefined. This is not ordinary list decoding or an official prize counterpacket.

## Final self-audit

[
17^{32}
=======

2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361,
\qquad
\left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
]
Thus the (2^{-128}) crossing is correct but not the main content; the content is the explicit one-line packet of (52{,}747{,}567{,}092) distinct noncontained slopes.

The primitive-log warning remains: old display prose uses an (X+1) gauge, while executable slot logs and the locator evaluation use (\beta=X+2). Numerical logarithms must retain their base. The packet hashes pass, and the bundled self-contained verifier terminates with `CYCLE116_TRANSFER_CERTIFICATE_VERIFIED`.
