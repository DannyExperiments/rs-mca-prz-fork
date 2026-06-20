# ROLE 09 - Referee And Route Board Formalizer

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
REFEREE-CYCLE63-BLOCK-TRADE-ROUTE-BOARD
```

## Objective

Act as the round referee. Do not solve from scratch. Formalize the route board
that should result if the block-trade repair works, fails, or partially works.

Use the Cycle 62 audit as the starting truth:

```text
Banked-positive: Roles 01/02 algebraic spine.
Cut: one-atom Q_per local-limit theorem.
Repair target: L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE.
Residual target: W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS.
MCA backup correction: Delta+[beta] color.
```

## Required Output

Give:

1. Dependency DAG after Cycle 62.
2. Exact theorem package needed for scalar list.
3. Exact theorem package needed for MCA transfer.
4. What counts as a successful Cycle 63 result.
5. What result kills the scalar-apolar route.
6. What result means switch to finite-checker implementation first.
7. What result should be sent to PRZ for review.
8. Next two-round plan after Cycle 63.

## Success Criteria

Output `PLAN` or `AUDIT` with a crisp route board and no vague taxonomy.

## Failure Criteria

Output `ROUTE_CUT` if you conclude the block-trade repair cannot plausibly
lead to a full scalar/list theorem.

