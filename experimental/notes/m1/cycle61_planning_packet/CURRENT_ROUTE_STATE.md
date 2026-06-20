# Current Route State For Cycle 61 Planners

This file is a compact orientation note for the Cycle 61 planning round.

## Problem Being Solved

The project is trying to solve two Proximity Prize challenges for
Reed-Solomon codes over smooth evaluation domains at rates
`1/2, 1/4, 1/8, 1/16`.

1. **Grand MCA challenge:** determine the largest radius `delta_C^*` such
   that the worst-case support-wise MCA error is at most `2^-128`.

2. **Grand list decoding challenge:** determine the largest radius
   `delta_C^*` such that the worst-case interleaved RS list size is at most
   `2^-128 |F|`.

The official problem is finite and code-specific. A rate-only asymptotic
formula is not enough unless the finite ledgers and quotient/envelope floors
are also handled.

## What Is Banked

### MCA lower/failure side

The lower/failure branch is the strongest part of the project. The
random-anchor/Bessel-style construction gives many, and often all, bad slopes
below the corrected entropy reserve. This is theorem-grade in the restricted
branches already audited.

### Exact MCA reformulation

The best global language is the syndrome transverse-secant formulation:

```text
bad slopes = affine syndrome line intersections with j-column spans,
             excluding contained/transverse failures
```

This denominator-free view covers all residue-denominator degrees at once and
is preferred over trying to solve only the balanced `t = sigma` residue cloud.

### Interleaved list reduction

At the official target scale, the interleaved list problem reduces to the
scalar full-support list problem by linear projection, assuming same-field
conditions. The scalar theorem is still open.

### Cycle 58-60 route repair

Cycle 58:

- Pure `n^{1+o(1)}` upper target is too strong or wrong.
- Correct safe-side bound needs an occupancy/main term plus finite template
  floors.

Cycle 59:

- Quotient ledger expanded from monomial `X -> X^M` action rank to
  projective/split-rational quotients.
- Pure Kronecker/minimal-basis section extraction and high-denominator
  compression shortcuts were cut.

Cycle 60:

- Genus-one Lattes/isogeny quotient packets must be added if arithmetic
  verifies.
- Point-fiber quotients are not enough; divisor-norm/configuration characters
  can appear in the jet-residue branch.
- Fixed-partition QAR packing, fixed-core petal bounds, hereditary MDS-3-core
  extraction, `t=1` apolar normal form, and scalar full-support circuit
  reductions are useful bankable route objects.

## What Is Not Solved

The MCA safe-side theorem is still open. The project does not yet have:

1. a support-theoretic split-rational/Lattes cover theorem on one envelope-free
   affine syndrome line;
2. a finite hereditary-envelope branching theorem;
3. a primitive occupancy/discrepancy theorem after quotient/envelope removal;
4. a complete divisor-norm/configuration-character JR ledger;
5. a `t=1` apolar primitive split-numerator inverse theorem;
6. a scalar list low-arity full-support circuit cover theorem;
7. finite integer certificates fitting below `floor(q / 2^128)`.

## Current Best Wall Names

```text
W-SRQ-GENUS-0/1-MONODROMY-CONTAINER
W-MCA-LATTES-SPLIT-RATIONAL-QAR-COVER
W-SRQ-HIGH-GENUS-FROBENIUS-DISCREPANCY-CONTAINER
W-MCA-SUPPORT-THEORETIC-SPLIT-RATIONAL-COVER
W-MCA-FINITE-CRITICAL-SEED-H2-DEFECT-CHARGE
W-JR-CORANK-ONE-DIVISOR-NORM-CHARACTER-TRICHOTOMY
W-JR-T1-PRIMITIVE-APOLAR-SPLIT-NUMERATOR-INVERSE
W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER
```

## Where To Go Next

The planning round should decide whether the best next move is:

1. **verification-first:** independently check the Lattes finite packets and
   then build the genus-0/1 quotient registry;
2. **container-first:** prove the support-theoretic split-rational cover
   theorem, treating Lattes as one class of block systems;
3. **primitive-first:** attack the `t=1` apolar primitive theorem and
   divisor-norm character trichotomy;
4. **list-first:** solve the scalar full-support low-arity circuit cover;
5. **finite-ledger-first:** build exact certificate scripts and only then
   decide which theorem constants are actually needed.

The planner should be blunt about which of these has the highest expected
value and which are likely distractions.
