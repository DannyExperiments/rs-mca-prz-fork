# Role 07: q-Ledger / Field Transfer Closer

Audit and close the denominator transfer required by Cycle111.

Focus points:

1. Separate `q_gen`, `q_line`, `q_code`, and `q_chal`.
2. State exactly which field each numerator term lives over.
3. Prove or refute the transfer from generated-field entropy to `K_line` slope
   occupancy needed for `2^128 * N_off <= q_line`.
4. Track floors, constants, stratum sums, and max-vs-sum accounting.
5. If the target theorem is true only with `q_line^(sigma-1)` rather than
   `q_gen^(sigma-1)`, state the exact corrected theorem and whether it still
   closes the official ledger.

Ambition bar: produce a ledger theorem that can be pasted into the canonical
tracker without ambiguity.

