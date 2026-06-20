# ROLE 02 - Block-Collapse Lemma

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-MODEL-GJ-BLOCK-COLLAPSE-LEMMA
```

## Objective

Prove the block-collapse part of `L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE`.

For

```text
Delta=[0]+sigma[infinity],
H cyclic,
K<=H, |K|=M>=sigma,
```

define

```text
beta_K(cK)=prod_{u in K} alpha_Delta(cu).
```

Prove exactly:

1. `beta_K(cK)` has no jet coordinates in degrees `1,...,sigma-1`.
2. It depends only on the toric block color `c^M`.
3. The statement is invariant under the choice of auxiliary form `L_*`.
4. The statement is invariant under scalar normalization of the coset.
5. The statement survives extension fields and nonsplit descriptions of `K`
   when the coset is realized over the base field.

## Success Criteria

Output `BANKABLE_LEMMA` with a complete finite proof and all edge cases.

## Failure Criteria

Output `COUNTERPACKET` if the collapse fails for some finite `F,H,K,sigma`.

