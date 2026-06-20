AUDIT

## 1. Executive verdict and confidence

The scalar-apolar route remains plausible, but Cycle 63 cannot count as successful merely by defining a “maximal” ((K,D)). A canonical assignment is set-theoretically easy on a cyclic (2)-group; the difficult theorem is an **exact, target-compatible total charge** after assignment.

There is also a mandatory wording correction:

[
\text{“a full block has zero jets”}
]

is false for an arbitrary auxiliary form (L_*). The invariant statement is that all (K)-block images lie in one fixed coset of the toric subgroup, while their pairwise ratios have zero jets and color (c^M/d^M).

**Confidence:** high for this route board and correction; moderate that block trades close the model minimal stratum; low-to-moderate that this alone leads quickly to the full scalar theorem, because arbitrary moduli and higher CI strata remain.

---

## 2. Corrected formal block-collapse statement

Let

[
\Delta=[0]+\sigma[\infty],\qquad H\le F^\times
]

be cyclic, let (K\le H) have order (M\ge \sigma), and let (C=cK). With monic locators,

[
P_C(X,Z)=\prod_{u\in K}(X-cuZ)=X^M-c^MZ^M.
]

For an admissible (L_*), define

[
\beta_{K,L_*}(C)=
\left[
\left.\frac{P_C}{L_*^M}\right|*\Delta
\right]\in G*\Delta.
]

Fix another coset (C_0=dK). Then the invariant relative block color is

[
\Gamma_{K,C_0}(C)
:=
\beta_{K,L_*}(C)\beta_{K,L_*}(C_0)^{-1}.
]

### Corrected block-collapse lemma

Under

[
G_\Delta\cong F^\times\times
\left(1+zF[z]/z^\sigma\right),
]

one has

[
\boxed{
\Gamma_{K,C_0}(cK)
==================

\left(\frac{c^M}{d^M},1\right).
}
]

Consequently:

1. Every relative block image has zero jet coordinates of degrees (1,\ldots,\sigma-1).
2. It depends only on the coset (cK), equivalently on (c^M).
3. It is independent of (L_*).
4. Replacing (c) by (cu), (u\in K), changes nothing.
5. The absolute block images form a fixed coset
   [
   \beta_{K,L_*}(C_0),T_K
   ]
   of the toric block-color subgroup (T_K\cong H/K).
6. For a fixed number (\ell) of blocks, changing (L_*) only translates every block-subset target by the same element. All subset-product counts are unchanged.

### Proof

At infinity, with (z=Z/X),

[
\frac{P_C}{P_{C_0}}
===================

\frac{1-c^Mz^M}{1-d^Mz^M}
\equiv1\pmod {z^\sigma},
]

because (M\ge\sigma). At (0=[0:1]),

[
\frac{P_C(0,1)}{P_{C_0}(0,1)}
=============================

# \frac{-c^M}{-d^M}

\frac{c^M}{d^M}.
]

The denominators (L_*^M) cancel in the ratio. Also ((cu)^M=c^M) for (u\in K). The argument remains valid over an extension or for a Galois-stable coset divisor whenever (c^M) lies in the base field.

### Why the absolute zero-jet formulation is false

Take (F=\mathbf F_5), (\sigma=M=2), (K={\pm1}), and (L_*=X+Z). Then

[
\frac{P_K}{L_*^2}
=================

\frac{X^2-Z^2}{(X+Z)^2}.
]

At infinity,

[
\frac{1-z^2}{(1+z)^2}
=====================

\frac{1-z}{1+z}
\equiv1-2z\pmod {z^2},
]

so the absolute block image has a nonzero first jet. This does not damage the route: the jet is fixed independently of the block coset and disappears in relative colors or fixed-cardinality target translation.

This corrected relative formulation must replace the literal version in `L-MODEL-GJ-BLOCK-COLLAPSE-LEMMA`.

---

## 3. Exact block-charge object

For fixed (K), define the canonical full-coset decomposition of a support (T\subseteq H) by

[
\mathcal S_K(T)={C\in H/K:C\subseteq T},
]

[
D_K(T)=T\setminus\bigcup_{C\in\mathcal S_K(T)}C.
]

Then (D_K(T)) contains no full (K)-coset, and this representation is unique at the fixed scale (K).

For a prospective defect (D), put

[
\Omega_K(D)={C\in H/K:C\cap D=\varnothing}.
]

Let

[
\ell=\frac{j-|D|}{M}.
]

If (\ell\notin\mathbf Z_{\ge0}), the associated charge is zero. Otherwise, fixing a reference coset (C_0), define

[
\mathsf B_{K,D}(b)
==================

#\left{
S\in\binom{\Omega_K(D)}{\ell}:
\prod_{C\in S}\Gamma_{K,C_0}(C)
===============================

b\bigl(\Phi_\sigma(D)\beta_K(C_0)^\ell\bigr)^{-1}
\right}.
]

This is an exact finite subset-product count on (H/K), and

[
\Phi_\sigma\left(D\cup\bigcup_{C\in S}C\right)
==============================================

\Phi_\sigma(D)\beta_K(C_0)^\ell
\prod_{C\in S}\Gamma_{K,C_0}(C).
]

Thus every fixed ((K,D)) profile has an exact, (L_*)-invariant block charge.

What remains open is not this identity. It is the following complete package.

### Exact central theorem required

`L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE` must supply an explicitly defined partition

[
\Phi_\sigma^{-1}(b)
===================

\left(\bigsqcup_{(K,D)\in\mathcal I_b}
\mathcal A_{K,D}(b)\right)
\sqcup
\mathcal R_b
]

such that:

[
\mathcal A_{K,D}(b)
\subseteq
\left{
D\cup\bigcup_{C\in S}C:
S\text{ counted by }\mathsf B_{K,D}(b)
\right};
]

the assignment to ((K,D)) is deterministic and depends only on the support occupancy vector; and there is an explicit integer bound

[
\boxed{
\sum_{(K,D)\in\mathcal I_b}
|\mathcal A_{K,D}(b)|
\le
\mathsf{BT}_\sigma(n,j,p;b).
}
]

The theorem must also define the residual (\mathcal R_b) exactly. Words such as “non-block,” “primitive,” or “maximal defect” are not sufficient definitions.

A lexicographic or maximal-(K) assignment by itself proves nothing quantitative. Because the subgroup lattice of dyadic (H) is a chain, one can always choose a canonical scale. The substantive issue is whether the resulting sum of block-profile charges is small enough for the finite ledger.

---

## 4. Dependency DAG after Cycle 62

```text
L-LIST-APOLAR-ALL-LAYER-CI
        |
        v
L-LIST-MINIMAL-CI-GJ-FIBER
        |
        +------------------------------+
        |                              |
        v                              v
model boundary/Fourier             t=1 MCA support fiber
cyclotomic-rank cap                and Delta+[beta] color
norm-rigidity                             |
        |                                  v
        v                         thickened block/color transfer
Role-04 block counterpacket                 |
        |                                  v
        v                         occupied-lift local limit
corrected relative block collapse           |
        |                                  v
        v                         d>sigma and all-line assembly
canonical block-profile partition
        |
        v
finite non-double-counting / total block charge
        |
        v
near-split residual collision-class mass
        |
        v
MODEL MINIMAL-STRATUM LOCAL LIMIT
        |
        +-------------------------------+
        |                               |
        v                               v
arbitrary degree-(sigma+1) Delta     finite checker registration
        |
        v
equal-degree and higher CI strata
        |
        v
full all-layer scalar list upper
        |
        v
scalar-to-interleaved transfer
        |
        v
official finite reserve certificate
```

The old one-atom (Q_{\rm per}) theorem is removed from the critical path. Its exact Fourier contribution may remain as an optional nonnegative subcharge, but it cannot organize the exceptional mass.

---

## 5. Exact theorem package needed for scalar list

Let

[
r=n-k,\qquad j=r-\sigma,\qquad
T_{\rm code}=\left\lfloor\frac{q_{\rm code}}{2^{128}}\right\rfloor.
]

The final scalar numerator is

[
L_C(\sigma)
===========

\max_s
#\left{
E\subseteq L:
|E|\le j,\
p_E\in I_s,\
\gcd(U_E,V_E)=1
\right}.
]

A scalar prize theorem at reserve (\widehat\sigma) requires

[
L_C(\widehat\sigma)\le T_{\rm code}
]

and, for an exact threshold,

[
L_C(\widehat\sigma-1)>T_{\rm code}.
]

The required package is:

| Gate                      | Exact requirement                                                                                                                                                   |   |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| S0                        | Independent red-team acceptance of Roles 01 and 02, including zero syndrome, infinity, nonreduced and nonsplit (\Delta), small characteristic, and generator shear. |   |
| S1                        | Corrected relative block-collapse theorem above.                                                                                                                    |   |
| S2                        | Canonical block-profile partition and an explicit total charge (\mathsf{BT}_\sigma), not merely a canonical name for each support.                                  |   |
| S3                        | In the regime not already covered by the cyclotomic-rank cap or norm rigidity, prove                                                                                |   |
|                           | [                                                                                                                                                                   |   |
| \mathcal R_b              |                                                                                                                                                                     |   |
| \le                       |                                                                                                                                                                     |   |
| \left\lceil               |                                                                                                                                                                     |   |
| C_\sigma\frac{\binom nj}{ | G_{\rm eff}                                                                                                                                                         | } |
| \right\rceil              |                                                                                                                                                                     |   |

*

R_{\rm coll}(n,p,\sigma)
]
with explicit integers (C_\sigma,R_{\rm coll}). |
| S4 | Extend the model theorem from ([0]+\sigma[\infty]) to every degree-(\sigma+1) divisor (\Delta=V(A)) arising in Role 02, or prove an exact worst-case reduction from arbitrary (\Delta) to finitely many model types. |
| S5 | Close the remaining CI strata. When (r<2\sigma+1), Role 01 already forces list size at most one. When (r=2\sigma+1), the equal-degree pencil (\mathbf P\langle A,B\rangle) requires a finite split-member bound. When (r>2\sigma+1), every stratum (d>\sigma+1), (b=r+1-d<j), requires control of all layers (e=b,\ldots,j) with (\gcd(U,V)=1). |
| S6 | Assemble a complete whole-numerator upper program, register it in the finite checker, and apply the scalar-to-interleaved projection theorem over the actual code field. |

The model block-trade theorem therefore does not itself solve scalar list decoding. It closes only Gate S2, and with the residual theorem, Gate S3.

---

## 6. Exact theorem package needed for MCA transfer

Role 05 identifies the correct object:

[
\text{supports in }G_\Delta,\qquad
\text{colors in }G_{\Delta^+},
\qquad
\Delta^+=\Delta+[\beta].
]

The MCA numerator counts occupied lifts, not support multiplicity:

[
M_{t=1}(s)
==========

\varepsilon_A+
#\left{
g\in\pi^{-1}(b_\Delta):
N^+_{\Delta^+,j}(g)>0
\right}.
]

Accordingly, scalar block charges transfer only after proving:

1. **Thickened relative block classification.** For each (K), determine the exact subgroup or coset containing
   [
   \prod_{u\in K}\alpha_{\Delta^+}(cu).
   ]
   If a color coordinate survives, identify it explicitly as a function of (c^M) and the geometry of (\Delta^+).

2. **Canonical colored charge.** Define exact ((K,D,\kappa)) classes, where (\kappa) is the surviving lift/color datum in (K_{\rm col}).

3. **Occupied-lift bound.** Prove
   [
   #{g\text{ occupied}}
   \le
   \mathsf{BT}^{\rm occ}*{\sigma}(b*\Delta)
   +
   U^{\rm occ}_{\rm res}.
   ]
   A bound on the sum of support multiplicities is not an MCA theorem.

4. **Color residual local limit.** Bound the residual occupied lift set in the near-split finite-characteristic regime.

5. **All-line assembly.** Close the (d>\sigma) rational-pair branch and prove that the (t=1) normal form controls every relevant syndrome line, over the actual line field.

The final finite target is

[
T_{\rm line}
============

\left\lfloor\frac{q_{\rm line}}{2^{128}}\right\rfloor,
]

not (T_{\rm code}) unless an exact normalization bridge is registered.

---

## 7. Cycle 63 decision board

| Cycle 63 output                                                                                                                 | Referee consequence                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Counterexample to Role 01 or Role 02                                                                                            | `ROUTE_CUT` for the scalar-apolar route.                                                       |
| Corrected block collapse only                                                                                                   | Useful bankable lemma, but the central wall remains open.                                      |
| A maximal or canonical ((K,D)) assignment without an explicit summed charge                                                     | `PLAN`, not a theorem-level success. Canonical naming is insufficient.                         |
| Canonical partition plus exact finite overlap/charge bound                                                                      | Structural Cycle 63 success. The exact remaining wall is collision-class mass.                 |
| Partition/charge plus near-split residual theorem                                                                               | Strong Cycle 63 success: the model minimal-stratum local limit closes.                         |
| Overlap counterpacket that collapses after passing to a common dyadic refinement or common color                                | Repair the assignment; this does not kill the route.                                           |
| Residual base gadget with (B) structural (M_0)-blocks and more than (2^B) product-conditioned, pairwise residual configurations | Kills the one-bit-per-(M_0)-block residual. Tensorization gives a parameterized counterpacket. |
| Official-scale residual counterpacket with no charged block profile and size exceeding every proposed explicit residual         | Cuts the present block-trade continuation, though not the apolar identities themselves.        |
| Exact computable charge/residual formulas whose finite relevance is unknown                                                     | Implement the frontier checker before proving broader generalizations.                         |

Here

[
M_0=2^{\lceil\log_2\sigma\rceil}.
]

The normalized-entropy kill test must apply after the canonical block charge has been removed. Theorem 7.1 of Role 03 approaches one bit per (M_0)-block from below and therefore does not yet kill the structural residual.

### What actually kills the scalar-apolar route

A failure of the block-trade repair does not invalidate apolar CI or the generalized-Jacobian fiber identity. It kills only the current positive continuation.

The scalar-apolar spine itself is killed only by an explicit failure of Role 01 or Role 02. The present block-trade route is killed by a parameterized residual family that survives every precisely defined block charge and violates any target-compatible finite residual.

---

## 8. When the finite checker must come first

Switch to checker implementation before another general theorem round when all of the following hold:

[
\mathsf{BT}*\sigma,\quad
C*\sigma,\quad
R_{\rm coll}
]

are explicit integer functions or exact certificate-producing algorithms, and the only unresolved question is whether

[
1+\mathsf{BT}*\sigma+
\left\lceil
C*\sigma\frac{\binom nj}{|G_{\rm eff}|}
\right\rceil+
R_{\rm coll}
\le T_{\rm code}
]

at the first candidate reserve.

The checker should then determine

[
c=f+1,
]

the first reserve not already killed by lower packets, and identify which of the following is actually frontier-relevant:

* model minimal stratum;
* arbitrary-(\Delta) transfer;
* equal-degree pencil;
* higher CI strata;
* extension/interleaving transfer;
* MCA color occupancy.

This prevents proving a broad arbitrary-(\Delta) theorem when the model charge already fails at the candidate reserve, or proving an elaborate residual theorem at a reserve already killed by the Role 04 packet.

---

## 9. PRZ review packet

The immediate PRZ submission should contain two separately labeled results:

1. **Positive algebraic package**
   [
   \texttt{L-LIST-APOLAR-ALL-LAYER-CI}
   +
   \texttt{L-LIST-MINIMAL-CI-GJ-FIBER},
   ]
   after the Cycle 63 red-team audit, with the strict hypothesis (j>d) and equal-degree edge stated explicitly.

2. **Negative route-cut package**
   the exact Role 04 same-field counterpacket, together with the statement that it cuts the one-atom (Q_{\rm per}) local-limit theorem but not the GJ fiber theorem.

If Cycle 63 proves the canonical partition and quantitative charge theorem, submit it as a third result with the corrected relative block-collapse formulation. Do not send an assignment theorem lacking a total finite charge, and do not send the old Role 03 all-field local-limit claim.

---

## 10. Next two-round plan

### If Cycle 63 strongly succeeds

**Cycle 64**

1. Prove arbitrary-(\Delta) transfer for degree (\sigma+1).
2. Implement and run `rs_prize_frontier_v1.py` with the new block charge.
3. Attack the equal-degree pencil and (d>\sigma+1) CI strata.
4. Prove the thickened ((K,D,\kappa)) MCA transfer.

**Cycle 65**

1. Assemble the complete all-layer scalar upper.
2. Register exact finite programs and determine the first safe reserve.
3. Apply the scalar-to-interleaved projection theorem.
4. Attempt the (t=1) occupied-color theorem and all-line MCA assembly.

### If Cycle 63 partially succeeds

**Cycle 64**

1. Finish the exact summed block charge or the near-split residual, whichever is missing.
2. Implement the checker in parallel.
3. Run a targeted residual gadget search using the exact canonical assignment.

**Cycle 65**

Proceed to arbitrary (\Delta) only if the model theorem clears the checker’s candidate reserve. Otherwise formalize the counterpacket and revise the structural invariant.

### If Cycle 63 fails quantitatively

**Cycle 64**

1. Formalize the residual counterpacket.
2. Determine whether common-color closure, a collision module, or a bounded-degree subresultant invariant absorbs it.
3. Implement the checker to identify the surviving finite reserves.
4. Preserve Role 05 as an independent MCA backup rather than assuming scalar transfer.

**Cycle 65**

Either test the replacement invariant in the model minimal stratum or switch to finite-instance certification at the first unresolved official reserve.

---

## 11. Bankable versus conditional

**Bankable now, subject to independent review:** the all-layer apolar CI structure, the minimal unequal-degree GJ fiber identity, Role 03’s exact model coordinates and safe-range caps, the Role 04 counterpacket, and Role 05’s (\Delta+[\beta]) color correction.

**Bankable from this audit:** the corrected relative block-collapse lemma and the fact that fixed-(K) block-plus-defect descriptions are unique once the defect contains no full (K)-coset.

**Conditional:** every quantitative maximal-scale assignment, total block charge, near-split residual estimate, arbitrary-(\Delta) transfer, higher-stratum upper, and MCA occupied-color transfer.

The exact failure point is the absence of an explicit admissibility predicate, disjoint or bounded-overlap charge, and target-compatible sum. “Choose a maximal ((K,D))” does not close that gap.

## Final answer

Yes, there is a route to a full solve, but Cycle 63 can at most close the model minimal-stratum structural wall.

The next exact lemma should be the corrected form

```text
L-MODEL-GJ-CANONICAL-BLOCK-TRADE-PARTITION-AND-BUDGET
```

comprising:

[
\text{relative toric block collapse}
+
\text{exact profile assignment}
+
\text{finite summed charge}
+
\text{precisely defined residual}.
]

After it, the next exact theorem is

```text
L-MODEL-GJ-NEAR-SPLIT-RESIDUAL-MASS-AFTER-BLOCK-CHARGE.
```
