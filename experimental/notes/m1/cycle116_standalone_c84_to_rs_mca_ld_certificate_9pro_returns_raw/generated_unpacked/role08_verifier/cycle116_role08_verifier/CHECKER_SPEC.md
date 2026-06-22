# Cycle116 Role08 Deterministic Verifier Specification

## Terminal decisions

| Decision | Exit | Meaning |
|---|---:|---|
| `CYCLE116_TRANSFER_CERTIFICATE_VERIFIED` | 0 | Every imported hash, finite anchor, field check, fixed-jet identity, scalar identity, smooth-lift clause, line receipt, and integer ledger check passed. |
| `CERTIFICATE_REJECTED` | 1 | A well-formed certificate failed a named mathematical or ledger clause. The JSON output includes `failure_clause` and `detail`. |
| `MALFORMED_INPUT` | 2 | JSON, schema, field representation, or required value is malformed. |
| `MISSING_FIXED_JET_CERTIFICATE` | 3 | The fixed-jet/product-scalar input is absent. This is the mandated fail-closed terminal. |
| `MISSING_CYCLE84_ANCHOR` | 4 | The imported finite anchor is absent. |

The checker never converts an absent or malformed clause into a warning or a partial pass.

## Exact inputs

1. `inputs/cycle84_anchor.json`
   - pins the accepted Cycle84 finite values;
   - names and SHA-256-binds the imported master certificate, 336 slot-log table, light receipt, and standalone finite note;
   - does not request a full Cycle84 census rerun.

2. `inputs/fixed_jet_certificate.json`
   - pins `F0`, `eta`, `beta`, the multiplicative-group factorization, the three exponent sets, their locator coefficients, the color shell, one reference tuple, and the native/lifted parameter ledgers;
   - supplies all data required to avoid `MISSING_FIXED_JET_CERTIFICATE`.

3. `imports/*`
   - exact packet files named by the anchor and checked byte-for-byte by SHA-256.

## Deterministic pseudocode

```text
read anchor
if absent: MISSING_CYCLE84_ANCHOR
read fixed-jet input
if absent: MISSING_FIXED_JET_CERTIFICATE

for each imported Cycle84 file:
    verify SHA-256
parse master and light receipts
verify P=52,747,567,104, U=52,747,567,092, D=24, m_max=2
verify histogram rigidity and 12 double fibers

construct F0 = F_17[X]/(X^16+X^8+3)
Rabin-test irreducibility
verify beta=X+2 is the slot-log primitive generator
verify eta=6X^9 has order 256, eta^16=3, and eta is nonsquare
verify beta^256 != 1

for i=1,2,3:
    recompute prod_{e in E_i}(Z-3^e)
    verify the supplied coefficients and zero Z^7,Z^6 coefficients

construct <eta^8> and every one of the 48 lifted 16-point blocks
for all 7*48=336 slot states:
    construct the block locator
    verify X^16+O(X^10)
    verify L_{t,i,a}(beta)=3^t u_t(i,a)
    verify beta^(certified log)=u_t(i,a)
    verify color and CRT residues

DP-count the seven-slot color shell and verify P
construct one reference J_T and verify
    P_T(X)=X^113-X^112+O(X^107)
    P_T(beta)=((beta-1)3^28) Phi(T), scalar nonzero

construct K=F0(theta), theta^2=eta
verify theta^256=-1, theta^512=1, |<theta>|=512
verify theta fails every proper-subfield Frobenius test
partition theta<eta> as A (119 points) disjoint union R (137 points)
verify augmented co-support size 250 and support size 262
verify deg(P_R(P_T-P_T')) <= 244 = 250-6
verify P_R(beta) is nonzero

construct one concrete final line:
    g(x)=L_H(beta)/(beta-x)
    f=e_J0-z0 g
hash f, g, z0, support and co-support
verify reference agreement and Vandermonde noncontainment prerequisites

set q_gen=q_code=q_line=17^32 and q_chal=UNSET
verify floor(q_line/2^128)=6
verify 52,747,567,092>6 and 2^128*N>q_line
emit CYCLE116_TRANSFER_CERTIFICATE_VERIFIED
```

## Fail-closed tests included

- `receipts/missing_fixed_jet.json`: absent fixed-jet input returns exit 3.
- `receipts/tamper_rejected.json`: changing the threshold from 6 to 7 returns exit 1 at `INTEGER_THRESHOLD`.
- `receipts/success.json`: full successful terminal receipt.

## Manifest policy

Use one root `MANIFEST.sha256` over every file except the manifest itself. For a review archive, also retain:

- the original packet-level `SHA256SUMS.txt`;
- canonical JSON (UTF-8, sorted keys for generated receipts);
- interpreter version and command line in the review log;
- no mutable URLs or network fetches;
- an explicit statement that Cycle84 census values are imported, not recomputed;
- a separate authority-signed official-source/challenge receipt before any official Proximity Prize claim.
