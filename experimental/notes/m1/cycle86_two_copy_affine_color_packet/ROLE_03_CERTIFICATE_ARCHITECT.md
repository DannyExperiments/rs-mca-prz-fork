# ROLE 03: Certificate Architect

You are a fresh finite-checker and certificate architect.

Assume the two-copy theorem might be true. Design the smallest deterministic
certificate/checker that would make it public-reviewable.

Your output must specify:

1. field model for `F_17^48` and embeddings of `F_17^16`;
2. domain representation and digest;
3. code parameters and official profile fields;
4. how the support map `Psi(T1,T2)` is represented without listing `N^2`
   supports;
5. how to certify the slope formula;
6. how to certify distinctness/injectivity or max multiplicity <= 8;
7. how to certify transversality/noncontainment;
8. exact JSON schema for PASS and FAIL;
9. deterministic verifier pseudocode or self-contained code outline.

If the theorem is not yet formal enough for a checker, return `EXACT_NEW_WALL`
with the exact missing mathematical datum the checker would need.
