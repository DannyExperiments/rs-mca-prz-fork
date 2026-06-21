# ROLE 08 - Certificate Engineer

Your job is to design the exact reproducibility bundle for the next local or
GitHub replay.

Required tasks:

1. Specify source files and language choices for the separator checker.
2. Specify finite-field arithmetic representation.
3. Specify input artifacts and hashes from Cycle84/Cycle85.
4. Specify output certificate JSON schema.
5. Specify independent verifier logic.
6. Specify memory-bounded sharding if the full P0 scan is too large.
7. Specify how to emit a FAIL certificate if `mu_proj(y) > 8`.
8. Specify how to emit a PASS certificate if `mu_proj(y) <= 8`.
9. Explain exactly how a reviewer reproduces the result.

The best answer is close to executable code or complete pseudocode. Avoid
handwavy "write a checker" language.

