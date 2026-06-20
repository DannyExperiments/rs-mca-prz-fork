# ROLE 02 — MCA Safe-Side Architect

You are responsible only for the MCA safe-side theorem.

Design the minimal theorem package needed to prove
`epsilon_mca(C, delta) <= 2^-128` above the corrected reserve. Use the
denominator-free syndrome transverse-secant formulation whenever possible.

Focus on:

- exact finite MCA numerator `M_C(sigma)`;
- envelope-free versus hereditary-envelope branches;
- split-rational / Lattes / divisor-character quotient containers;
- primitive occupancy/discrepancy theorem;
- how to handle all denominator degrees, including `t > sigma`;
- exact integer comparison with `floor(q / 2^128)`.

Deliver a dependency DAG and the best next exact lemma.
