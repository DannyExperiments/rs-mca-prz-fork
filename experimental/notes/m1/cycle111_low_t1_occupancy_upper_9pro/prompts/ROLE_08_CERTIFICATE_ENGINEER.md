# Role 08: Certificate Engineer / Finite Stress Harness

Design the exact checker or proof-carrying harness for the Cycle111 wall.

Focus points:

1. Specify an exact finite replay that tests the `t=1` support/product
   formulation and detects structured counterpackets.
2. Terminal labels must be conservative:
   `SOURCE_ROUTE_PROOF`, `FINITE_MODEL_PASS`, `COUNTERPACKET`,
   `ROUTE_CUT`, `RESOURCE_EXHAUSTED_NO_CLAIM`.
3. Include source-validity receipts: AP_corr, charge absence/payment,
   field ledger, corrected reserve, distinct slope count, and numerator bound.
4. If a checker can only provide finite/model evidence, state the exact theorem
   needed to lift it.
5. If possible, provide pseudocode or executable skeleton precise enough for
   Codex to implement.

Ambition bar: create a checker spec that can distinguish proof, finite stress,
and false counterpacket without interpretation.

