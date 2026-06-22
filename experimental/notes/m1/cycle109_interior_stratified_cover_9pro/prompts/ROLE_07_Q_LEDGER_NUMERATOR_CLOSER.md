# Role 07: q-Ledger Numerator Closer

Close the field and numerator ledger.

Assume the branch-level source cover is available only if you state its exact
hypotheses. Determine the precise numerical theorem needed to conclude

`N_off / q_line <= 2^-128`.

You must separate:

- `q_gen`: generated-field entropy/reserve;
- `q_code`: code alphabet/scalar-extension source field;
- `q_line`: actual MCA slope field and denominator;
- `q_chal`: protocol challenge field, usable only through a protocol-transfer
  theorem.

Produce either:

- a conditional `BANKABLE_LEMMA` with exact caps and final inequality;
- a `ROUTE_CUT` showing a common field-transfer shortcut is invalid;
- or a `PROOF` if you can combine the branch caps and close the official
  numerator.

Do not use asymptotic `n^O(1)` alone unless you also show it is below
`floor(q_line/2^128)` for the intended parameter regime.

