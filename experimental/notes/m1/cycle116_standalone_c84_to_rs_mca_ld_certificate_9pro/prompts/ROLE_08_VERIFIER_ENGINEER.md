# Role 08: Verifier Engineer

Use the common prompt. No Internet.

Design the tiny deterministic verifier for the standalone certificate.

Do not re-run the full Cycle84 census. Consume the standalone Cycle84 certificate values as inputs, but verify every small algebra/ledger claim needed for the transfer:

```text
field F0 = F_17[X]/(X^16+X^8+3)
irreducibility
eta order 256
eta nonsquare
theta^2=eta gives F_17^32
theta order 512
floor(17^32/2^128)=6
N=52,747,567,092 > 6
fixed-jet/product-scalar identities if data are present
otherwise emit MISSING_FIXED_JET_CERTIFICATE
```

Deliverable:

- exact checker input files;
- exact terminal decisions;
- pseudocode or Python skeleton;
- fail-closed behavior;
- SHA/checksum manifest recommendations.
