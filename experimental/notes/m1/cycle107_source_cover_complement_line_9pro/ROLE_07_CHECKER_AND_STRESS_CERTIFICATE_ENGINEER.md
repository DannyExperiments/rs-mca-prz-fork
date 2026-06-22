# Role 07: Checker And Stress Certificate Engineer

Your job is to produce an executable route.

Use the provided scripts and certificates as starting points:

```text
context/scripts/03_cycle106_complement_line_eliminant_check.py
context/scripts/07_cycle106_kfree_stress_checker.py
context/scripts/cycle106_kfree_incidence_stress.py
context/scripts/cycle106_family_signature_miner.py
context/scripts/cycle106_density_sensitivity_from_signatures.py
context/certificates/
```

Do not install dependencies. Prefer standard-library Python or self-contained
C++/Python.

Build one of:

1. A Gate A checker that validates source-cover normalization into `AP_corr`.
2. A Gate B checker that emits/validates `R_{m,D}(Uhat) != 0`.
3. A counterpacket verifier for a source-valid family.
4. A finite stress generator that explicitly reports why its output is not
   source-valid.

Required terminal decisions:

```text
SOURCE_COVER_VERIFIED
COMPLEMENT_LINE_ESCAPE_CERTIFIED
SOURCE_VALID_COUNTERPACKET_FOUND
FINITE_STRESS_ONLY_NO_CLAIM
RESOURCE_EXHAUSTED_NO_CLAIM
```

If you provide code, include exact invocation and expected output fields.

Return `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `EXACT_NEW_WALL`, `AUDIT`,
or `PLAN`.
