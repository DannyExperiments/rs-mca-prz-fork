# Role 03: Charge Ledger Formalizer

Assume the Cycle111 packets are dangerous. Build the exact charge ledger needed
to pay them.

Focus on endpoint, field confinement, affine-color, tangent, contained/delete-one,
periodic/quotient, same-slope, retained-normalization, hidden-action-rank, and
restricted-sum/local-limit charges.

Output either a `T1_BLOCK_PACKET_CHARGED` theorem with exact cap `A0` and
`2^128*A0 <= allocated q_line reserve`, or a route cut explaining why no existing
charge can pay the packets.
