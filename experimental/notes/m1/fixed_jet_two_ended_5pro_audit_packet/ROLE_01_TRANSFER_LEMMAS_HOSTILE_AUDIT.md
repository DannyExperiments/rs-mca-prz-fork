# Role 01 - Transfer Lemmas Hostile Audit

Audit only Sections 1-3 of:

```text
fixed_jet_and_two_ended_transfer_note.md
```

Your job is to decide whether the two transfer lemmas are valid as ordinary
mathematics.

Do not evaluate the 84-state computation. Do not evaluate the ABF consequence.

## Claims To Audit

1. Fixed-jet locator transfer:

```text
deg(P_J - P_J') <= j - sigma
=> LD_sw(RS[F,D,n-j-sigma], n-j) >= #{P_J(beta)}.
```

2. Two-ended locator transfer:

```text
deg(P_J - P_J') <= j - sigma + 1
and P_J(0)=c != 0
=> LD_sw(RS[F,D,n-j-sigma], n-j) >= #{P_J(beta)}.
```

## Required Checks

- Does the fixed-jet proof correctly derive the common high truncation of
  `L_J = V_D/P_J`?
- Is `deg c_J < k` correct?
- Does the root-count noncontainment proof really rule out simultaneous
  explanation?
- Is the two-ended functional `ell` actually independent of `J`?
- Does the two-ended proof avoid using the missing coefficient in degree
  `j-sigma+1`?
- Is the weighted Vandermonde parity check exactly the RS parity check?
- Is `W_J^perp = P_J F[X]_<sigma` correct?
- Does the Vandermonde independence argument prove support-wise
  noncontainment?

Find the first false line if one exists.
