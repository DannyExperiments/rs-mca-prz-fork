# ROLE 05 - Near-Split Collision-Class Mass

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS
```

## Objective

Attack the residual wall named by Role 03.

Work in the hard regime not covered by:

1. the norm-rigid theorem; and
2. the cyclotomic-rank-safe theorem.

Prove or kill a finite bound for the union of finite-characteristic collision
classes after block-trade charges have been removed.

## Target Shape

Prove a finite inequality of the form:

```text
N_Delta(b)
<= block_trade_charge(b)
 + C_sigma * binom(n,j)/|G_eff|
 + explicit_collision_residual(n,p,sigma).
```

If that shape is wrong, replace it with the correct finite statement.

## Success Criteria

Output `PROOF` or `BANKABLE_LEMMA` if you prove a finite mass bound strong
enough to be usable by the frontier checker.

## Failure Criteria

Output `COUNTERPACKET` if you find a finite base gadget whose
product-conditioned fiber has normalized entropy high enough to inflate into a
parameterized counterpacket.

