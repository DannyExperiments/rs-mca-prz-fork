# ROLE 03 - Canonical Maximal `(K,D)` Assignment

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-MODEL-GJ-MAXIMAL-KD-ASSIGNMENT
```

## Objective

Define or disprove a canonical, shear-invariant maximal `(K,D)` assignment for
support profiles of the form:

```text
D union union_{cK in S} cK.
```

Here `K<=H` is a subgroup with `|K|>=sigma`, and `D` is a defect set outside
the selected full `K`-blocks.

The assignment must prevent double-counting when the same support admits
several block-plus-defect descriptions.

## Required Properties

Try to define `(K,D)` so that:

- `K` is maximal among subgroup scales explaining the block collapse;
- `D` is minimal/canonical after choosing `K`;
- the assignment is invariant under generator shear in the apolar CI;
- equivalent descriptions map to the same charge class;
- non-equivalent descriptions have bounded overlap or a common refinement
  that is assigned instead.

## Success Criteria

Output `BANKABLE_LEMMA` if you construct and prove a canonical assignment with
finite overlap control.

## Failure Criteria

Output `COUNTERPACKET` if a family of supports has many inequivalent maximal
`(K,D)` descriptions with no canonical choice or bounded overlap.

