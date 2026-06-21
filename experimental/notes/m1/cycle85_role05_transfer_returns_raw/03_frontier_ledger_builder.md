ROUTE_CUT

## 1. Executive verdict — confidence: high

Cycle84 supports the corrected finite implication

[
M_{C_0}(6)\ge 52{,}747{,}567{,}092
]

for the Role05 (t=1) MCA model, provided the banked Cycle62 and Cycle65–68 transfer statements are accepted. It does **not** give a scalar-list numerator, and it does not identify the complete MCA numerator.

The native model has

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481,
]

so

[
T_{\rm line}=T_{\rm code}
=\left\lfloor\frac{17^{16}}{2^{128}}\right\rfloor=0.
]

Therefore the comparison with (2^{32}) is not an RS-PRIZE-FRONTIER-V1 comparison. It is only an internal research benchmark.

As supplied, the row is not an official row because

[
(n,k)=(256,137),\qquad \frac{k}{n}=\frac{137}{256},
]

which violates the official rate set
({1/2,1/4,1/8,1/16}). The correct current classification is:

```text
RESEARCH_MODEL_FAIL
```

not official `FAIL`, and not `UNKNOWN`.

There is, however, an exact shortening construction that repairs the rate: remove 18 coordinates never used by any Cycle84 support. This produces a rate-(1/2) ([238,119]) GRS/RS instance with the same reserve, syndrome dimension, witnesses, colors, and lower bound. Even after this repair, the Cycle84 term never moves the certified frontier for any permitted scalar extension of (F_{17^{16}}): at small line fields the core tangent bound already proves failure, while at the next line-field size the Cycle84 numerator is below the native target.

---

## 2. Exact theorem and ledger statement

### Corrected transfer theorem

Define

[
F_0=\mathbf F_{17}[X]/(X^{16}+X^8+3),\qquad
D=\mu_{256}=\langle\eta\rangle,\qquad
\eta=6X^9,
]

and let

[
\beta=X+2\notin D.
]

The native MCA code parameter is

[
C_0=\operatorname{RS}[F_0,D,137].
]

Its Role05 parameters are

[
n=256,\quad k=137,\quad r=n-k=119,
]
[
\sigma=6,\quad a=k+\sigma=143,\quad
j=r-\sigma=113.
]

The quotient code used internally by the shifted (t=1) normal form has dimension (k+1=138) and parity-check dimension

[
R=n-k-1=118=j+\sigma-1.
]

Do not enter (k=138) in the MCA ledger; that is the auxiliary extension-code dimension.

Let (\mathcal P_0) be the Cycle65–84 support family and

[
\rho_\beta(T)=\prod_{x\in T}(\beta-x).
]

Then the corrected theorem is:

> **`L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER`.**
> Assume:
>
> 1. every (T\in\mathcal P_0) is a size-(113), full-coordinate representation on one fixed nonconstant Role05 (t=1) syndrome line;
> 2. (\rho_\beta(T)) is the exact coordinate of the corresponding (\Delta^+)-lift, not merely a quotient of that coordinate;
> 3. the Cycle62 equivalence between occupied (\Delta^+)-lifts and distinct reduced MCA colors holds;
> 4. the Role05 noncontainment hypothesis holds.
>
> Then
>
> [
> \left|\operatorname{Bad}*{\le113}(u,v)\right|
> \ge
> #{\rho*\beta(T):T\in\mathcal P_0}.
> ]
>
> Consequently, using the Cycle84 public replay,
>
> [
> \boxed{
> M_{C_0}(6)\ge52{,}747{,}567{,}092.
> }
> ]

This is a lower certificate. It is not the assertion

[
M_{C_0}(6)=52{,}747{,}567{,}092.
]

Other supports, other Role05 fibers, and any lower-weight (A)-support may add slopes.

### Objective identification

```text
objective: MCA lower numerator
not: scalar-list numerator
not: exact whole MCA numerator
```

Cycle84 alone certifies a model-level thickened-color occupancy. The MCA interpretation additionally depends on the Cycle62/Cycle65 transfer.

### Native parameter ledger

| Quantity                        |            Exact value |   |                        |
| ------------------------------- | ---------------------: | - | ---------------------- |
| (n)                             |                  (256) |   |                        |
| (k)                             |                  (137) |   |                        |
| redundancy (r=n-k)              |                  (119) |   |                        |
| reserve (\sigma)                |                    (6) |   |                        |
| agreement (a=k+\sigma)          |                  (143) |   |                        |
| support budget (j=r-\sigma)     |                  (113) |   |                        |
| support size in (\mathcal P_0)  |                  (113) |   |                        |
| grid radius                     |              (113/256) |   |                        |
| (t)                             |                    (1) |   |                        |
| (\deg\Delta)                    |                    (6) |   |                        |
| (\deg\Delta^+)                  |                    (7) |   |                        |
| (                               |           \mathcal P_0 | ) | (52{,}747{,}567{,}104) |
| occupancy                       | (52{,}747{,}567{,}092) |   |                        |
| (m_{\max})                      |                    (2) |   |                        |
| ordered off-diagonal energy (D) |                   (24) |   |                        |

### Field ledger

[
q_{\rm gen}=q_{\rm code}=q_{\rm line}=17^{16}
=48{,}661{,}191{,}875{,}666{,}868{,}481.
]

The equality (q_{\rm gen}=17^{16}) is forced: (\eta) has order (256), and

[
\operatorname{ord}_{256}(17)=16,
]

so no proper subfield of (F_0) contains (\eta).

```text
q_chal: not specified by the Cycle84/Role05 packet
field debit: unused
```

A concrete checker input must supply (q_{\rm chal}) and its field certificate. Its value cannot change either (T_{\rm line}) or (T_{\rm code}).

### Promotion-ready lower-term payload

The currently honest registry status is `PENDING_REVIEW`, because no combined transfer producer, code fingerprint, domain certificate, or (q_{\rm chal}) ledger is supplied.

```json
{
  "id": "cycle85.role05.occupancy.mca.lower.sigma6",
  "status": "PENDING_REVIEW",
  "objective": "mca",
  "direction": "lower",
  "term_type": "packet.explicit_mca_slope_set",
  "scope": {
    "kind": "whole_numerator",
    "id": "M_C"
  },
  "aggregation_role": "standalone",
  "reserve_data": {
    "kind": "table",
    "entries": [
      {
        "sigma": "6",
        "bound": "52747567092"
      }
    ]
  },
  "field_debits": {
    "entropy": "unused",
    "line": "q_line",
    "code": "q_code",
    "challenge": "unused"
  },
  "theorem_id": "L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER",
  "dependencies": [
    "L-JR-T1-GJ-FIBER-AND-COLOR",
    "L-MODEL-GJ-THICKENED-FACTORIZATION",
    "L-CYCLE66-LOCATOR-EVALUATION-OCCUPANCY",
    "L-CYCLE68-DISJOINT-COSET-FACTORIZATION",
    "L-CYCLE84-EXACT-COLOR-FILTERED-MMAX",
    "V-CYCLE84-GITHUB-PUBLIC-REPLAY",
    "RS-PRIZE-FRONTIER-V1-SOUNDNESS"
  ],
  "hypothesis_evidence": [
    "n=256",
    "k=137",
    "sigma=6",
    "j=113",
    "all packet supports have size 113",
    "beta=X+2 is outside mu_256",
    "rho_beta is the full Delta-plus lift coordinate",
    "distinct rho_beta values give distinct affine slope parameters",
    "all packet incidences are noncontained and transverse"
  ],
  "producer_certificate": {
    "producer_id": "V-CYCLE85-ROLE05-OCCUPANCY-TRANSFER-CHECKER",
    "certificate_sha256": null,
    "cycle84_exact_certificate_sha256": "cfee92099c54e2f4d746f7f887d95610000d6c0985e25acf459bc9f9f2257c29",
    "cycle84_local_result_sha256": "2afa5a166e7df598ef94eb3b1ee767089ecb172f2a11040fed49cb10619022e7",
    "cycle84_public_receipt_sha256": "99a2c618803dd1f4b143e6872d10bd76833c2fddceaaf2d706b04fd3ff6d0759"
  },
  "notes": "Promote to PROVED_FINITE only after the combined transfer checker, code fingerprint, domain certificate, field ledger, and q_chal value verify."
}
```

### Current row classification

For the native model,

[
T_{\rm line}=0.
]

Hence the mathematical research row at (\sigma=6) is `FAIL`. Indeed the core unit lower bound (M_C(\sigma)\ge1) already makes every reserve fail when (T_{\rm line}=0).

But the official checker rejects the unmodified instance before assigning a row status because (137/256) is not an allowed official rate. Therefore:

```text
mathematical research row: FAIL
official unmodified input: INVALID_PROFILE_RATE
required external label: RESEARCH_MODEL_FAIL
Cycle84 term relevance: NO_FRONTIER_MOTION
```

---

## 3. Proof and exact normalization construction

### 3.1 Occupancy gives distinct MCA slopes

The Cycle62 Role05 theorem states that, for one fixed old support target (b_\Delta), the MCA colors are exactly the occupied points in its (\Delta^+)-lift fiber. It also states

[
T,T'\text{ have the same slope}
\iff
[T]*{\Delta^+}=[T']*{\Delta^+}.
]

Cycle65 identifies the finite coordinate on this lift fiber with

[
\rho_\beta(T)=P_T(\beta)
=\prod_{x\in T}(\beta-x),
]

up to a fixed nonzero scalar and an affine color relabeling. Fixed nonzero scaling and affine relabeling are bijections, so they preserve cardinality and collisions.

Therefore

[
#{\text{slopes supplied by }\mathcal P_0}
=========================================

#{\rho_\beta(T):T\in\mathcal P_0}.
]

Cycle84 proves the right side is exactly (52{,}747{,}567{,}092).

The Role05 noncontainment argument proves that these are genuine transverse bad parameters, not contained incidences. Thus they lie in one (\operatorname{Bad}_{\le113}(u,v)), and maximizing over lines gives the stated MCA lower bound.

### 3.2 Exact unused-coordinate shortening lemma

Cycle68’s factorization shows that the squared slot roots range over

[
\mu_{128}\setminus\mu_{16}.
]

Taking both square roots inside (\mu_{256}), their full preimage is

[
\mu_{256}\setminus\mu_{32}.
]

Every packet support consequently lies in

[
\Omega={1}\cup(\mu_{256}\setminus\mu_{32}).
]

Hence no packet support uses any point of

[
\mu_{32}\setminus{1},
]

which contains (31) points.

Choose explicitly

[
Z={\eta^{8b}:1\le b\le18}
\subseteq\mu_{32}\setminus{1},
]

and put

[
D'=D\setminus Z.
]

Then

[
|D'|=238,
]

and every (T\in\mathcal P_0) remains a subset of (D').

Shorten (C_0=\operatorname{RS}[D,137]) on the coordinates (Z). A polynomial (f) of degree (<137) vanishing on all (Z) has the unique form

[
f=P_Zg,\qquad
P_Z(X)=\prod_{z\in Z}(X-z),\qquad
\deg g<119.
]

Therefore the shortened code is

[
\operatorname{GRS}[F_0,D',119]
]

with multipliers (P_Z(x)). Coordinate-wise rescaling by (P_Z(x)^{-1}) identifies it with the standard code

[
C'=\operatorname{RS}[F_0,D',119].
]

Nonzero column rescaling does not change support spans, bad-line parameters, or transversality. Equivalently, a parity-check matrix for the shortened code is obtained by deleting the (Z)-columns from the original parity-check matrix. Since all packet supports avoid (Z), every Cycle84 witness and every slope survives unchanged.

The normalized parameters are therefore

[
n'=238,\qquad k'=119,\qquad r'=119,
]
[
\sigma'=6,\qquad j'=113,\qquad a'=125,
]
[
\delta_{\rm grid}'=\frac{113}{238},
\qquad \frac{k'}{n'}=\frac12.
]

The quotient (t=1) parity-check dimension remains exactly

[
n'-k'-1=118=j'+\sigma'-1.
]

Thus:

[
\boxed{
M_{C'}(6)\ge52{,}747{,}567{,}092.
}
]

This removes the visible official-rate defect without tensoring.

### 3.3 Why (2^{32}) is not a native target

For the native field,

[
T_{\rm line}
============

\left\lfloor
\frac{48{,}661{,}191{,}875{,}666{,}868{,}481}
{340{,}282{,}366{,}920{,}938{,}463{,}463{,}374{,}607{,}431{,}768{,}211{,}456}
\right\rfloor
=0.
]

To have (T_{\rm line}=2^{32}), one would need

[
2^{160}\le q_{\rm line}<(2^{32}+1)2^{128}.
]

But every finite line field containing (F_{17^{16}}) has order

[
q_{\rm line}=17^{16m}.
]

Under the official strict cap (q_{\rm line}<2^{256}), only (m=1,2,3) are possible:

| (m) |                                                                                                 (q_{\rm line}=17^{16m}) |                            (T_{\rm line}) | Cycle84 consequence                |
| --: | ----------------------------------------------------------------------------------------------------------------------: | ----------------------------------------: | ---------------------------------- |
|   1 |                                                                                (48{,}661{,}191{,}875{,}666{,}868{,}481) |                                       (0) | `FAIL`, already by unit lower      |
|   2 |                                       (2{,}367{,}911{,}594{,}760{,}467{,}245{,}844{,}106{,}297{,}320{,}951{,}247{,}361) |                                       (6) | `FAIL`, already by tangent (j=113) |
|   3 | (115{,}225{,}400{,}457{,}255{,}426{,}923{,}013{,}053{,}222{,}916{,}919{,}834{,}651{,}165{,}519{,}677{,}685{,}328{,}641) | (338{,}617{,}018{,}271{,}848{,}945{,}628) | Cycle84 lower term is below target |

For (m=4),

[
17^{64}>2^{256},
]

so the official field cap fails.

Thus there is no permissible line-field extension for which

[
113\le T_{\rm line}
<
52{,}747{,}567{,}092.
]

That interval is the exact condition under which Cycle84 could beat the target at reserve (6) after the core tangent lower bound has stopped doing so.

Therefore the one-copy Cycle84 term is never a leave-one-out frontier mover:

* for (m=1,2), a core lower term already proves failure;
* for (m=3), Cycle84 does not exceed the target.

---

## 4. Verification requirements

Before changing the lower term to `PROVED_FINITE`, RS-PRIZE-FRONTIER-V1 must receive:

1. A deterministic certificate binding every (T\in\mathcal P_0) to one fixed nonzero (t=1) syndrome line, including full-coordinate status and support size (113).

2. A transfer certificate proving that (\rho_\beta(T)) is the full (\Delta^+)-lift coordinate used by the Cycle62 theorem, not a quotient, norm, or periodic projection of it.

3. A transversality certificate invoking the exact Role05 noncontainment hypotheses for this line.

4. For the shortened normalization, a certificate of
   [
   \mathcal P_0\subseteq{1}\cup(\mu_{256}\setminus\mu_{32}),
   ]
   the explicit set (Z), and the shortening/GRS equivalence.

5. The ordered-domain digest, domain certificate, field certificates, embedding certificates, and generated-field minimality certificate.

6. A concrete (q_{\rm chal}). It remains an unused debit but is mandatory in a conforming input.

7. A combined producer hash and code fingerprint binding
   [
   (\text{code ID},\text{objective},n,k,D,q_{\rm gen},q_{\rm line},
   q_{\rm code},q_{\rm chal})
   ]
   to the Cycle84 replay certificate.

The Cycle84 public replay verifies the finite occupancy calculation. It does not itself verify Items 1–7.

---

## 5. Next exact lemma or construction

The immediate construction that closes the current transfer wall is:

```text
V-CYCLE85-ROLE05-OCCUPANCY-TRANSFER-AND-SHORTENING-CHECKER
```

It must emit:

```text
CYCLE85_ROLE05_MCA_PACKET_VERIFIED
native_model_M_C_sigma6_lower = 52747567092
shortened_model_n = 238
shortened_model_k = 119
shortened_model_sigma = 6
shortened_model_j = 113
shortened_model_rate = 1/2
transversality = true
rho_to_slope_injective = true
domain_shortening_verified = true
```

and the promotion-ready `packet.explicit_mca_slope_set` term with a complete code fingerprint.

For an actual frontier-moving construction, the exact next mathematical target is:

```text
L-CYCLE86-RS-TWO-BLOCK-ROLE05-SLOPE-INJECTION
```

Target statement:

> Construct a rate-(1/2) ([476,238]) GRS/RS instance over the Cycle84 code field, with reserve (\sigma=12), support budget (j=226), and a line over (F_{17^{48}}), together with an injection
>
> [
> S_{\rm occ}\times S_{\rm occ}
> \hookrightarrow
> \operatorname{Bad}_{\le226}(u,v).
> ]

Numerically this would give

[
|S_{\rm occ}|^2
===============

2{,}782{,}305{,}834{,}125{,}041{,}336{,}464

>

# 338{,}617{,}018{,}271{,}848{,}945{,}628

T_{\rm line}(17^{48}).
]

The unresolved part is not the arithmetic. It is the existence of one RS-compatible affine syndrome line realizing the two independent occupied coordinates injectively.

---

## Self-audit

### 1. What exact implication did I prove, and what did I not prove?

Proved, subject to the banked Role05 transfer dependencies:

[
\operatorname{Occ}(\beta)=52{,}747{,}567{,}092
\Longrightarrow
M_C(6)\ge52{,}747{,}567{,}092.
]

I also proved that shortening on 18 explicitly unused coordinates preserves this lower packet and converts ((256,137)) into the rate-(1/2) parameters ((238,119)).

I did not prove equality with the entire MCA numerator, a scalar-list numerator statement, a frontier-moving result, a tensor amplification theorem, or a currently registry-admissible official certificate.

### 2. Is the result official-prize-relevant?

The unmodified result is only a finite/model research certificate because its rate is invalid.

The shortened result is compatible with the visible official rate and field-cap conditions, but is not yet an accepted official packet because the registry binding, (q_{\rm chal}), domain fingerprint, and combined transfer certificate are absent. Moreover, even after promotion it is leave-one-out redundant for every permissible line-field extension.

### 3. What is the first line where the reduction could fail?

Without treating the Markdown audits as trusted registry entries, the first line is:

```text
Every T in P_0 is a full-coordinate witness on one fixed t=1 line,
and rho_beta(T) is the full Delta-plus lift coordinate for that line.
```

That is the Cycle65-to-Cycle62 bridge. The Cycle84 count begins only after this identification.

For the unmodified official instance, the first unconditional checker failure is earlier and simpler:

```text
137/256 is not in {1/2,1/4,1/8,1/16}.
```

### 4. Are the fields and the (2^{-128}) target used correctly?

Yes:

```text
q_gen  = 17^16
q_code = 17^16
q_line = 17^16 in the native model
q_chal = unspecified and unused
T_line = 0
T_code = 0
```

Neither (q_{\rm chal}) nor (2^{32}) is a valid substitute for the native MCA denominator. No compatible official-cap scalar extension makes (2^{32}) the native target.

### 5. Can quotient structure, contained incidences, same-slope collisions, or affine normalization reduce the numerator?

Once the corrected transfer theorem is certified, no:

* same-slope collisions are already removed by taking distinct (\rho_\beta)-values;
* affine color normalization is bijective;
* Role05 noncontainment makes the incidences transverse;
* shortening preserves all relevant support spans;
* quotient/periodic structure may affect an upper-bound decomposition or exception label, but cannot identify two already-distinct actual line parameters.

The only live danger is that (\rho_\beta) might have been certified merely as a quotient coordinate rather than the full (\Delta^+)-lift coordinate. That is exactly what the missing transfer checker must exclude.

### 6. What converts this into a checker-certified proof?

`V-CYCLE85-ROLE05-OCCUPANCY-TRANSFER-AND-SHORTENING-CHECKER`, with the seven verification items above.
