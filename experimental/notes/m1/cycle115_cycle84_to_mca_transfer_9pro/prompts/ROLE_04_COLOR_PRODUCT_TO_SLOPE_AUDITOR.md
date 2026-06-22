# Role 04: Color/Product-To-Slope Preservation Auditor

Use the common prompt. No Internet.

Your role is to audit the algebraic bridge from Cycle84 product fibers to slope values.

Cycle84 proves a color-filtered product map has `m_max(beta)=2` and `52,747,567,092` occupied product values. A transfer theorem needs an exact map from those product values to bad slopes, line parameters, or residue-line colors.

Audit and prove or refute:

1. Product equality in Cycle84 is equivalent to equality of the RS/MCA slope parameter after the chosen normalization.
2. The color condition `c_L+c_R=4 mod 16` is exactly the required support/witness/filter condition in the RS object.
3. The slope map is injective or has a precisely bounded fiber loss.
4. Reciprocal-affine normalization, scalar factors, GRS scaling, and color normalization do not collapse the numerator below the claimed threshold.
5. The twelve double fibers and absence of triples do not introduce hidden same-slope collisions in the target theorem.

You may use the Cycle85 transfer audit and the Cycle84 standalone certificate. Do not trust them blindly: restate the algebra in your own theorem form.

Output the exact slope map and its fiber bound. If it is not source-valid, state exactly which normalization or quotient makes it fail.
