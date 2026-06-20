# ROLE 01 - Role 04 Counterpacket Formalizer

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-MODEL-GJ-BLOCK-TRADE-COUNTERPACKET-FORMALIZATION
```

## Objective

Formalize the Role 04 counterpacket as a clean theorem in repository language.

You must independently check the exact same-field construction:

```text
q = 21*2^128 + 1,
n = 256,
k = 128,
sigma = 4,
j = 124,
deg A = 5,
deg B = 124,
packet size = 7,045,058,086,196,679,
target floor(q/2^128)=21.
```

State precisely why it:

- lies in the minimal scalar stratum;
- satisfies the full-coordinate criterion;
- has no lower `H`-supported representation;
- has trivial support stabilizers;
- lies in one generalized-Jacobian fiber;
- is not charged by the one-atom `Q_per` from Role 03;
- is explained by a block-plus-defect profile.

## Success Criteria

Output `COUNTERPACKET` if the construction is valid and the route cut is real.
Output `ROUTE_CUT` if it invalidates more than the stated `Q_per` theorem.
Output `AUDIT` if it is valid but needs a narrower interpretation.

## Failure Criteria

Output `ROUTE_CUT` against the counterpacket if any exact finite claim fails:
primality, domain, packet cardinality, full-coordinate status, target
comparison, or `Q_per` comparison.

