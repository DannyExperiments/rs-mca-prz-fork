# Role 06: Periodic / Quotient / Collision Charge Ledger

Your job is to prevent numerator overcount.

Audit whether the Cycle107 gates correctly handle:

```text
quotient structure
periodic/coset-swap structure
contained incidences
same-slope collisions
affine color normalization
```

You must decide exactly when these structures:

1. are forbidden by `AP_corr(Uhat)`,
2. survive but are charged separately,
3. reduce the claimed numerator,
4. create a source-valid counterpacket mechanism.

Also audit the field ledger:

```text
q_gen
q_line
q_code
q_chal
2^-128 target
```

If they are irrelevant to this single-field upper-side wall, say so explicitly
and name the first official-transfer stage where they become relevant.

Required output:

```text
charge rule =
numerator preserved? yes/no/conditional =
first place q-ledger enters =
exact missing lemma or counterexample =
```

Return `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, or `PLAN`.
