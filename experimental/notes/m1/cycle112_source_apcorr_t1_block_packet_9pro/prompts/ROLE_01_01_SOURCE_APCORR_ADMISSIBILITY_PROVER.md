# Role 01: Source AP_corr Admissibility Prover

Try to prove that the Cycle111 block/prefix/affine-involution packets are not
admissible under the official source predicate, or prove that they are
admissible. Your answer must make `AP_corr` noncircular and source-checkable.

Focus points:

1. Extract the strongest frozen or implied source AP_corr definition from the
   packet and tracker.
2. Test the Cycle111 counterpacket mechanisms against it.
3. If AP_corr accepts them, emit `SOURCE_VALID_LOW_T1_COUNTERPACKET` with exact
   receipts still needed.
4. If AP_corr rejects them, state the exact rejecting predicate and prove it is
   official-source justified.
5. Do not use vague aperiodicity language. Give the exact predicate.
