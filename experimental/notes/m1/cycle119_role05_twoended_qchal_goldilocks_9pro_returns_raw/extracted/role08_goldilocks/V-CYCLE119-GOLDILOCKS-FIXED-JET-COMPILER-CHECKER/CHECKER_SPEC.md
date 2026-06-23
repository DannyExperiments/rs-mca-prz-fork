# V-CYCLE119-GOLDILOCKS-FIXED-JET-COMPILER-CHECKER

The checker has two layers.

1. **Main theorem layer (existential beta).** It verifies the Proth primality
   certificate, the order-512 domain, the 8-to-1 map `H -> H^8`, the fixed-jet
   parameters `(j,sigma,k)=(248,8,256)`, the exact collision average, and
   `L(q)=73,674,899,375,228,060`. The proof that these antecedents imply the
   existence of a beta and a common affine line is in `STANDALONE_CERTIFICATE.md`.
   No explicit beta realizing `L(q)` is claimed.

2. **Constructive fallback layer (beta=0).** It directly builds 64 translated
   31-subsets, checks 64 distinct slopes, constructs every degree-<256
   explaining polynomial, checks all 264 agreement coordinates, and records
   the root-count noncontainment certificate. This explicit packet alone has
   density `64/q > 2^-128`.

Successful terminal:

```text
CYCLE119_GOLDILOCKS_FIXED_JET_COMPILER_VERIFIED_EXISTENTIAL_BETA
```

Additional terminals:

```text
GOLDILOCKS_PRIME_PROTH_VERIFIED
ORDER_512_DOMAIN_VERIFIED
MU8_FIBER_FIXED_JET_FAMILY_VERIFIED
AVERAGE_SPECIALIZATION_NUMERATOR=73674899375228060
AGREEMENT_264_VERIFIED
STRICT_BALL_263_SURVIVES
EXPLICIT_BETA_ZERO_64_SLOPE_PACKET_VERIFIED
q_gen=q_code=q_line=18446744069414584321
q_chal=null
OFFICIAL_CONTRACT_PENDING
```

The checker is not an authority-pinned official row/event/challenge receipt.
