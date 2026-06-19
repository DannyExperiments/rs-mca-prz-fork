# Cycle 59 5.5/5.6 Route-Repair Audit

## Claim

The Cycle 59 nine-lane theorem-worker run does **not** solve the Proximity
Prize. It is significant because it repairs the target again: the calibrated
syndrome transverse-secant theorem must be quotient-invariant in a stronger
functional sense than the Cycle 58 `X^M` action-rank ledger.

The most important new warning is:

```text
monomial quotient-action rank is not a canonical quotient ledger.
```

The quotient/template side must now recognize projective or split-rational
quotients, not only maps of the form `X -> X^M`.

## Status

AUDIT / EXPERIMENTAL, with COUNTERPACKET and BANKABLE_LEMMA subresults.

Conservative banking:

- **BANKABLE_LEMMA:** large transverse slope packets reduce to a deterministic
  split-locator syzygy-excess obstruction.
- **COUNTERPACKET:** pure Kronecker/minimal-basis section extraction is false;
  coefficient trajectories inside moving fibers require an additional inverse
  theorem.
- **BANKABLE_LEMMA:** quotient-action-rank classification is sharp for an
  individual fixed-defect packet, but the global cover theorem is missing.
- **COUNTERPACKET / ROUTE CUT:** monomial `d_M(E)` does not catch
  Mobius-conjugated or split-rational quotient packets.
- **ROUTE_CUT:** the high-denominator `t > sigma` branch does not genuinely
  compress to `t <= sigma`; syndrome space is the right global chart.
- **BANKABLE_LEMMA:** the `t < sigma` jet-residue bridge is exact and restores
  the correct entropy dimension using top jets plus residue.
- **COUNTERPACKET / ROUTE CUT:** scalar list templates must also include
  functional quotients, not only multiplicative quotients.
- **BANKABLE_LEMMA:** finite prize certification is an exact integer ledger,
  with branch maxima sharper than a naive six-term sum.
- **AUDIT:** the full problem is not one lemma away; MCA safe side and scalar
  list safe side remain separate major inverse/container problems.

## Parameters

The run concerns the official RS-MCA and list decoding challenges for

```text
C = RS[F,L,k]
n = |L|
rho = k/n in {1/2, 1/4, 1/8, 1/16}
a = k + sigma
j = n - a = n-k-sigma
epsilon* = 2^-128
```

The exact syndrome object remains:

```text
V_T = span{H_RS(:,x) : x in T},     |T| = j
ell(z) = u + z v
bad/transverse slope: ell(z) in V_T and v notin V_T.
```

Ledgers must remain separated:

```text
q_gen    entropy/generated-domain field
q_line   slope field
q_chal   challenge field
Q        same-field size when q_gen=q_line=q_chal
```

No answer in this round justifies letting `q_line` or `q_chal` pay a
`q_gen` entropy bill without an explicit transfer theorem.

## Existing Paper Dependency

Primary dependency: Paper B / M1, especially the corrected-reserve MCA normal
form and denominator-free syndrome transverse-secant formulation.

Companion dependency: scalar list/full-support local limit. The interleaved
list wall is mostly projection bookkeeping at the official same-field scale,
but the scalar theorem remains open.

## Lane Summary

Raw returns are preserved in:

```text
experimental/notes/m1/cycle59_5p6_raw/
```

| Lane | Raw file | Returned status | Conservative bank |
| --- | --- | --- | --- |
| 01 calibrated syndrome inverse | `01_calibrated_syndrome_inverse_syzygy_excess.md` | BANKABLE_LEMMA | exact split-locator Macaulay/syzygy-excess reduction; inverse still open |
| 02 locator scroll minimal basis | `02_locator_scroll_kronecker_counterpacket.md` | COUNTERPACKET | pure low-degree section extraction false; need mixed Kronecker coefficient-ratio inverse |
| 03 calibrated counterpacket | `03_mobius_split_rational_counterpacket.md` | COUNTERPACKET | monomial action-rank ledger misses Mobius/split-rational quotient packet |
| 04 quotient action rank | `04_quotient_action_rank_classifier.md` | BANKABLE_LEMMA | fixed-defect packet theorem; arbitrary-anchor quotient charge needs full profile and cover lemma |
| 05 high denominator | `05_high_denominator_thick_residue_route_cut.md` | ROUTE_CUT | no genuine high-denominator compression; `t=r` is a universal syndrome chart |
| 06 jet-residue bridge | `06_jet_residue_actual_list_bridge.md` | BANKABLE_LEMMA | exact sequence for top jets plus residue; identifies colored full-secant local-limit wall |
| 07 scalar list | `07_scalar_list_functional_quotient_counterpacket.md` | COUNTERPACKET | interleaved projection complete; scalar list quotient ledger must include functional quotients |
| 08 finite threshold | `08_finite_prize_threshold_ledger.md` | BANKABLE_LEMMA | exact finite certification ledger; no rate-only threshold |
| 09 referee formalizer | `09_referee_route_board_formalizer.md` | AUDIT | full problem still needs canonical hereditary container system and scalar list container theorem |

## Ledger Impact

### 1. MCA Upper Wall

The previous wall

```text
W-MCA-CALIBRATED-SYNDROME-TRANSVERSE-SECANT-INVERSE
```

should be refined to a finite, canonical, hereditary container theorem:

```text
W-MCA-FINITE-CANONICAL-HEREDITARY-AFFINE-SECANT-CONTAINER
```

The theorem must be line-intrinsic and must not depend on a noncanonical
choice of residue denominator.

### 2. Quotient Ledger

The monomial action-rank invariant

```text
d_M(E) = deg minpoly([X^M] mod E)
```

is not enough. A repaired quotient ledger must include split-rational maps

```text
R(X) = P(X)/Q(X)
```

with many equal-size split fibers inside the domain, and charge denominator
compression by

```text
d_R(E) = deg minpoly([R(X)] mod E).
```

The new quotient wall is:

```text
W-MCA-PROJECTIVE-SPLIT-RATIONAL-ACTION-RANK-INVERSE
```

At a minimum, quotient templates must be closed under projective RS
automorphisms, including dihedral/inversion and norm-one/projective-subline
symmetries when present.

### 3. Fixed-Defect Quotient Packets

For one fixed quotient scale and defect set, the sharp arbitrary-anchor charge
is the full quotient support profile:

```text
min{|F|, binom(n/M-c_T, k/M)}
```

not the smaller canonical-line exponent

```text
2^{(beta(rho)/H_2(rho)) Q_H(eta)}.
```

The missing global theorem is:

```text
W-MCA-QAR-FIXED-DEFECT-COVER
```

After tangent/common-envelope slopes are removed, quotient-structured slopes on
one affine syndrome line should be coverable by `n^{o(1)}` fixed-defect
quotient/action-rank packets. This is not proved.

### 4. Residual / Jet-Residue Branch

For `t < sigma`, the correct object is the exact jet-residue sequence:

```text
P |-> (Top_{sigma-t}(P), [P]_E).
```

The top jets contribute `sigma-t` constraints and the residue line contributes
`t-1`, recovering the same total `sigma-1` codimension as the balanced
occupancy term. The branch wall becomes:

```text
W-JR-PRIMITIVE-COLORED-FULL-SECANT-LOCAL-LIMIT
```

with a critical-kernel completion subwall:

```text
W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION
```

This is bankable infrastructure, but it does not close the high-denominator
branch.

### 5. High Denominator Branch

The `t > sigma` branch does not admit a useful general compression theorem.
The degree `t=r=n-k` presentation is a universal chart for any affine syndrome
line. Therefore high-denominator analysis should be absorbed by the canonical
syndrome theorem rather than treated as a separate denominator-compression
problem.

### 6. List Branch

The same-field official interleaved-to-scalar projection theorem is effectively
closed, subject to the finite collision inequality. The list wall is scalar:

```text
W-LIST-FINITE-FULL-SUPPORT-POINT-SECANT-KERNEL-CONTAINER
```

The scalar list quotient ledger must also recognize functional quotients. A
pure multiplicative quotient profile is too narrow outside the strict
power-of-two multiplicative-domain setting.

## Corrected Target

For MCA, the desired theorem should be stated as an exact finite container
certificate. For every affine syndrome line, after a canonical assignment of
slopes to primitive, quotient, or envelope-descendant containers, prove

```text
|Bad_sigma(ell)|
  <= P_prim + P_occ + P_quot + P_env
  <= floor(q_line / 2^128).
```

The primitive calibrated bound should have the shape

```text
P_prim + P_occ
  <= C_occ * binom(n,k+sigma) / q_line^{sigma-1}
     + P(n,sigma),
```

with explicit finite constants, not just asymptotic `n^{o(1)}`.

For list decoding, the finite scalar target is:

```text
max_s sum_{e=0}^{r-sigma} nu_e^circ(s)
  <= floor(q / 2^128),
```

plus the matching lower/failure at the previous integer reserve. Under the
projection inequality, this determines the interleaved threshold.

## What Remains Open

The current route is **not** one lemma from a full solve. It appears to require
at least:

1. a line-intrinsic split-rational quotient classifier;
2. a fixed-defect quotient/action-rank cover theorem;
3. a hereditary envelope/container system with bounded branching;
4. a primitive finite occupancy/discrepancy theorem for affine syndrome lines;
5. a scalar full-support point-secant kernel container theorem for list
   decoding;
6. explicit constants small enough for the `2^-128` finite target;
7. field-transfer closure for any generated-field versus line-field mismatch.

## Next Prompts

The strongest next theorem-worker prompts should no longer ask for the old
pure inverse theorem. They should attack:

```text
W-MCA-PROJECTIVE-SPLIT-RATIONAL-ACTION-RANK-INVERSE
W-MCA-QAR-FIXED-DEFECT-COVER
W-MCA-FINITE-CANONICAL-HEREDITARY-AFFINE-SECANT-CONTAINER
W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION
W-LIST-FINITE-FULL-SUPPORT-POINT-SECANT-KERNEL-CONTAINER
```

The highest priority is the split-rational quotient issue, because if that
ledger is wrong then the primitive theorem is not yet well-defined.

