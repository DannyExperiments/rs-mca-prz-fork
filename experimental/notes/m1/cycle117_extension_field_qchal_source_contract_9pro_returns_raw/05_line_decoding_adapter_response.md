## 1. LABEL

**ROUTE_CUT**

**Confidence: high.**

## 2. EXECUTIVE VERDICT

The exact finite adapter is proved:

[
\boxed{
\epsilon_{\mathrm{mca}}(C,\delta)
=================================

\frac{\operatorname{LD}_{\mathrm{sw}}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)}
{|\mathbb F|}
}
]

under the attached support-wise MCA definitions.

For Cycle116,

[
n=512,\qquad \delta=\frac{125}{256},\qquad
\left\lceil(1-\delta)n\right\rceil
=\left\lceil\frac{131}{256}\cdot512\right\rceil
=262.
]

Consequently,

[
\operatorname{LD}_{\mathrm{sw}}(C,262)\ge 52{,}747{,}567{,}092
]

implies

[
\epsilon_{\mathrm{mca}}!\left(C,\frac{125}{256}\right)
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}.
]

The route to an official `(δ,a_LD,n+1)-line-decodable` conclusion is nevertheless cut. No attached source file formally defines that notation. The only source occurrence calls it a “manuscript phrase,” while the same file explicitly leaves matching it to an external definition as future work: `context/source/m2_line_decoding_mca_bridge.md:67–68,408–414`. The canonical tracker likewise says the exact parameter statement is open: `context/RS_MCA_CANONICAL_TRACKER.md:68`.

This omission is mathematically consequential. A closed-ball convention gives agreement (262), whereas a strict-ball convention gives agreement (263):

[
\frac{d_H(u,C)}n\le\frac{125}{256}
\iff \operatorname{agr}(u,C)\ge262,
]

but

[
\frac{d_H(u,C)}n<\frac{125}{256}
\iff \operatorname{agr}(u,C)\ge263.
]

Cycle116 proves the lower bound at (262), not at (263).

## 3. SOURCE-PINNED THEOREM OR ROUTE CUT

### Source-pinned support-wise theorem

The controlling definition is in:

* `context/source/RS_disproof_v3.tex:110–114`;
* equivalently, `context/source/slackMCA_v3.tex:639–652`.

For a line (u_z=f+zg), a parameter (z\in\mathbb F) is bad if there is one support (S\subseteq D) such that:

[
|S|\ge(1-\delta)n,
\qquad
u_z|_S=c|_S\quad\text{for some }c\in C,
]

while no (c_f,c_g\in C) simultaneously satisfy

[
f|_S=c_f|_S,
\qquad
g|_S=c_g|_S.
]

The error is the maximum number of such finite slopes (z), divided by (|\mathbb F|).

The attached bridge note then defines (\operatorname{LD}_{\rm sw}) in exactly these terms and states the equality above: `context/source/m2_line_decoding_mca_bridge.md:14–53`.

### Exact route cut

The packet contains no formal definition specifying what

[
(\delta,a_{\mathrm{LD}},n+1)\text{-line-decodable}
]

means. In particular, it does not specify:

1. whether the distance ball is closed or strict;
2. whether (a_{\rm LD}) counts slopes, line points, codewords, or pairs ((z,c));
3. whether slopes range over (\mathbb F) or a projective line (\mathbb F\cup{\infty});
4. what the third parameter (n+1) controls;
5. whether the exceptional alternative is exact containment in (C), proximity to a code-line, or some weaker explanation;
6. whether any common-support, tangent, endpoint, or proximity-loss condition is included.

Therefore the literal implication

[
(\delta,a_{\rm LD},n+1)\text{-line-decodable}
\Longrightarrow
\operatorname{LD}*{\rm sw}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)
\le a*{\rm LD}
]

cannot be attributed to the source until that definition is supplied.

## 4. PROOF DETAILS

Let (C\le\mathbb F^D), where (|D|=n). For (f,g\in\mathbb F^D) and an integer (a), define

[
\begin{aligned}
B_a(f,g)={z\in\mathbb F:;&
\exists S\subseteq D,\ |S|\ge a,\ \exists c\in C,\
&(f+zg)|_S=c|_S,\
&\nexists(c_f,c_g)\in C^2:
f|_S=c_f|_S\ \text{and}\ g|_S=c_g|_S
}.
\end{aligned}
]

Define

[
\boxed{
\operatorname{LD}_{\rm sw}(C,a)
===============================

\max_{f,g\in\mathbb F^D}|B_a(f,g)|.
}
]

This is exactly the definition in `m2_line_decoding_mca_bridge.md:21–39`.

Now put

[
a_\delta=\left\lceil(1-\delta)n\right\rceil.
]

Because (|S|) is an integer,

[
|S|\ge(1-\delta)n
\iff
|S|\ge a_\delta.
]

Hence, for every fixed (f,g), the set of slopes called bad by the source MCA definition is exactly (B_{a_\delta}(f,g)). Therefore

[
\begin{aligned}
\epsilon_{\rm mca}(C,\delta)
&=
\max_{f,g}
\frac{|B_{a_\delta}(f,g)|}{|\mathbb F|}\
&=
\frac1{|\mathbb F|}
\max_{f,g}|B_{a_\delta}(f,g)|\
&=
\frac{\operatorname{LD}*{\rm sw}(C,a*\delta)}
{|\mathbb F|}.
\end{aligned}
]

This is equality, not merely an inequality.

The equivalent distance-coordinate formula is

[
a_\delta
========

n-\lfloor\delta n\rfloor,
]

since

[
\left\lceil n-\delta n\right\rceil
==================================

n-\lfloor\delta n\rfloor.
]

For Cycle116,

[
\delta n=\frac{125}{256}\cdot512=250,
]

so

[
a_\delta=512-250=262.
]

Thus the Cycle116 lower bound gives

[
\epsilon_{\rm mca}!\left(C,\frac{125}{256}\right)
=================================================

\frac{\operatorname{LD}_{\rm sw}(C,262)}{17^{32}}
\ge
\frac{52{,}747{,}567{,}092}{17^{32}}.
]

### Why this is not ordinary list decoding

Ordinary list size fixes one received word (y) and counts

[
#{c\in C:d_H(y,c)\le\delta n}.
]

Cycle116 instead fixes one affine line and produces many distinct slopes (z), hence many generally different received words (f+zg). Each slope can have its own explaining codeword and support. No single received word with (52{,}747{,}567{,}092) close codewords is constructed.

Therefore no ordinary list-decoding lower bound follows.

## 5. FIELD AND PARAMETER LEDGER

| Quantity       | Meaning                                    | Cycle116 value | Status                                                   |           |   |
| -------------- | ------------------------------------------ | -------------: | -------------------------------------------------------- | --------- | - |
| (q_{\rm gen})  | Field generated by the evaluation subgroup |      (17^{32}) | (H=\langle\theta\rangle) generates (\mathbb F_{17^{32}}) |           |   |
| (q_{\rm code}) | Alphabet/coefficient field of (C)          |      (17^{32}) | (C=\operatorname{RS}[\mathbb F_{17^{32}},H,256])         |           |   |
| (q_{\rm line}) | Field from which (z) is sampled            |      (17^{32}) | Source has (z\in\mathbb F) and denominator (             | \mathbb F | ) |
| (q_{\rm chal}) | Separate protocol challenge field          |      **unset** | No attached source clause defines one                    |           |   |

Only (q_{\rm line}) is used in the MCA denominator:

[
\epsilon_{\rm mca}
==================

\frac{#{\text{bad finite slopes}}}{q_{\rm line}}.
]

There is no additional division by (q_{\rm gen}), (q_{\rm code}), or (q_{\rm chal}).

The extension-field row is admissible for the attached manuscript’s raw support-wise MCA definition. The manuscript allows finite fields and smooth multiplicative subgroups, and it explicitly develops generated extension-field rows in `context/source/RS_disproof_v3.tex:369–424`. Taking (p=17), (m=16), and (d=32) gives subgroup order (md=512) in (\mathbb F_{17^{32}}), matching the Cycle116 structural row.

The field-of-definition warning in `context/source/slackMCA_v3.tex:600–601` does not shrink (q_{\rm gen}) here because (H) generates the full field.

This establishes compatibility with the attached raw MCA source. It does not supply an external protocol or official line-decodability contract.

## 6. EVENT RETENTION / CHARGE AUDIT

| Rule           | Raw source status                                                | Cycle116 consequence                                                                        |                 |                              |
| -------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------- | ---------------------------- |
| Endpoint       | Retained: source uses (                                          | S                                                                                           | \ge(1-\delta)n) | Exact agreement (262) counts |
| Periodic       | No exclusion in `def:mca`                                        | No slopes removed                                                                           |                 |                              |
| Quotient       | No exclusion in `def:mca`                                        | No slopes removed; quotient separation elsewhere concerns corrected upper-bound bookkeeping |                 |                              |
| Tangent        | Not an exclusion; the source even proves a tangent lower floor   | Cycle116 additionally proves its direction is not code-explainable on each witness support  |                 |                              |
| Contained line | Paid through the definition’s simultaneous-explanation condition | Cycle116’s Vandermonde argument proves support-wise noncontainment                          |                 |                              |
| Affine color   | No source rule                                                   | (N) already counts distinct slopes; no further color division                               |                 |                              |
| Retained event | No such map in the raw definition                                | All definition-valid slopes are retained                                                    |                 |                              |
| Charge         | No charge registry in the raw definition                         | No charge subtraction is authorized                                                         |                 |                              |

The endpoint issue reappears only when attempting to import the undefined external line-decodability notion. A strict-distance definition would require (263) agreements and would not automatically retain Cycle116’s exact-(262) witnesses.

## 7. LINE-DECODING VS `LD_SW` ADAPTER

### Closed-ball adapter theorem

Define

[
\operatorname{Close}_{\le\delta}(f,g)
=====================================

\left{
z\in\mathbb F:
\min_{c\in C}\frac{d_H(f+zg,c)}n\le\delta
\right}.
]

Suppose an external theorem proves that for every (f,g),

[
f+\mathbb Fg\subseteq C
\quad\text{or}\quad
|\operatorname{Close}*{\le\delta}(f,g)|\le a*{\rm LD}.
\tag{LD(_{\le})}
]

Then

[
\boxed{
\operatorname{LD}*{\rm sw}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)
\le a*{\rm LD}.
}
]

#### Proof

If (f+\mathbb Fg\not\subseteq C), every support-wise bad slope has a codeword agreement on at least

[
\left\lceil(1-\delta)n\right\rceil
]

coordinates. Its distance to (C) is therefore at most (\delta), so

[
B_{a_\delta}(f,g)
\subseteq
\operatorname{Close}_{\le\delta}(f,g).
]

Hence (|B_{a_\delta}(f,g)|\le a_{\rm LD}).

If (f+\mathbb Fg\subseteq C), then (f\in C) by taking (z=0), and (g\in C) because (f+g\in C) and (C) is linear. Thus (f) and (g) themselves simultaneously explain every support, so there are no support-wise bad slopes. Therefore the same bound holds in the exceptional case. Maximizing over (f,g) proves the result.

Combining this with the exact bridge gives

[
\epsilon_{\rm mca}(C,\delta)
\le
\frac{a_{\rm LD}}{|\mathbb F|}.
]

This is the sufficient adapter described informally in `m2_line_decoding_mca_bridge.md:249–259`.

### Strict-ball variant

If the external predicate bounds slopes satisfying

[
\frac{d_H(f+zg,C)}n<\delta,
]

then the correct agreement threshold is

[
a_\delta^{<}
============

# n-\lceil\delta n\rceil+1

\lfloor(1-\delta)n\rfloor+1.
]

The resulting implication is

[
\boxed{
\operatorname{LD}*{\rm sw}
!\left(C,n-\lceil\delta n\rceil+1\right)
\le a*{\rm LD}.
}
]

At Cycle116 parameters,

[
a_\delta^{<}=512-\lceil250\rceil+1=263.
]

Thus the strict variant does not consume the banked lower bound at agreement (262).

### Conditional Cycle116 consequence

If the missing source definition is exactly the closed-ball predicate ((\mathrm{LD}*{\le})), then Cycle116 proves that the code cannot be ((125/256,a*{\rm LD},n+1))-line-decodable for any

[
a_{\rm LD}<52{,}747{,}567{,}092.
]

That conclusion remains conditional on adopting the missing definition.

A broader exception such as “the received line is close to a code-line” is not automatically harmless. It requires a common-support guarantee or a separate residual bound; this issue is analyzed in `m2_line_decoding_mca_bridge.md:320–384`.

## 8. VERIFIER / REVIEWER CHECKLIST

1. **Definition match:** Confirm the external line-decodability source uses a closed Hamming ball, not a strict ball.
2. **Counted object:** Confirm (a_{\rm LD}) bounds distinct finite slopes, or at least an object that surjects onto those slopes.
3. **Slope universe:** Confirm whether the line has (|\mathbb F|) affine parameters or (|\mathbb F|+1) projective points.
4. **Exception:** Confirm that the only zero-cost exception is exact containment in (C), or supply a support-wise residual bound.
5. **Third parameter:** Define the role of (n+1); do not assume it is inert.
6. **Denominator:** Use (q_{\rm line}=17^{32}) exactly once. Leave (q_{\rm chal}) unset.
7. **Claim scope:** State support-wise MCA / `LD_sw`, not ordinary list decoding.
8. **Integrity:** All entries in the packet’s `SHA256SUMS.txt` verified successfully.
9. **Cycle116 gauge:** Preserve the distinction between old display logs based at (X+1) and executable slot logs based at (\beta=X+2).

## 9. SELF-AUDIT

* **Finite versus official:** Cycle116 is used as a finite support-wise MCA / `LD_sw` theorem. No official external line-decodability claim is made.
* **Exact source clause:** Raw MCA is pinned to `RS_disproof_v3.tex:110–114` and `slackMCA_v3.tex:639–652`. The missing line-decodability definition is pinned to the unresolved language in `m2_line_decoding_mca_bridge.md:67–68,408–414`.
* **Field ledger:** (q_{\rm gen}), (q_{\rm code}), and (q_{\rm line}) are distinguished despite having the same value. (q_{\rm chal}) is not invented.
* **Extension field:** The row is accepted by the attached raw MCA manuscript formulation, but this is not an external protocol contract.
* **Event retention:** Endpoint and noncontainment are paid; periodic, quotient, affine-color, retained-event, and charge filters are absent from the raw definition.
* **Ordinary list decoding:** Not claimed.
* **Line adapter:** Closed- and strict-ball variants are separately proved.
* **(2^{-128}):**

  [
  \left\lfloor\frac{17^{32}}{2^{128}}\right\rfloor=6.
  ]

  Hence any integer numerator at least (7) crosses the threshold. The threshold comparison is true but not the main content; constructing (52{,}747{,}567{,}092) distinct support-wise slopes is.
* **Primitive-log gauge:** The (X+1) versus (\beta=X+2) warning is preserved.
* **Terminal label:** `ROUTE_CUT` is conservative and forced by the missing formal definition.

## 10. NEXT EXACT STEP

Add an authority-pinned definition equivalent to the following:

> **Definition.** Let (C\le\mathbb F^D), (|D|=n). The code is closed-ball ((\delta,a_{\rm LD}))-affine-line-decodable if, for every (f,g\in\mathbb F^D), either (f+\mathbb Fg\subseteq C), or
> [
> #\left{z\in\mathbb F:
> d_H(f+zg,C)/n\le\delta\right}
> \le a_{\rm LD}.
> ]
> The parameter set is (\mathbb F); the count is over distinct slopes; the contained-line exception has no additional proximity alternative.

Then record the adapter theorem:

[
(\delta,a_{\rm LD})\text{-affine-line-decodable}
\Longrightarrow
\operatorname{LD}*{\rm sw}
!\left(C,\left\lceil(1-\delta)n\right\rceil\right)
\le a*{\rm LD}
\Longrightarrow
\epsilon_{\rm mca}(C,\delta)
\le\frac{a_{\rm LD}}{|\mathbb F|}.
]

The source must separately define what its existing third parameter (n+1) means. Until that sentence exists, the Cycle116 conclusion stops exactly at manuscript-compatible support-wise MCA / `LD_sw`.
