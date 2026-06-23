# V-CYCLE116 Standalone C84-to-RS-MCA/LD Transfer Verifier

Run:

```bash
./run_verifier.sh
```

Expected terminal:

```text
"decision": "CYCLE116_TRANSFER_CERTIFICATE_VERIFIED"
```

This package verifies the small algebraic and ledger layer of the standalone transfer. It deliberately imports, rather than reruns, the Cycle84 full census. It checks:

- irreducibility of `X^16+X^8+3` over `F_17`;
- exact orders and nonsquareness of `eta`;
- all 336 fixed-jet/product-scalar slot identities and their binding to the certified slot logs;
- `P_T(X)=X^113-X^112+O(X^107)` and `P_T(beta)=kappa Phi(T)`, `kappa!=0`;
- the quadratic smooth lift, order-512 subgroup, generated-field receipt, `A/R` partition, agreement 262, and noncontainment prerequisites;
- one concrete final affine-line receipt, represented by SHA-256 hashes of `f`, `g`, `z0`, the reference support, and co-support;
- the exact `q_gen/q_code/q_line/q_chal` ledger and the strict `2^-128` comparison.

The output is a finite standard Reed--Solomon support-wise MCA / `LD_sw` certificate. It is not an ordinary list-decoding lower bound, protocol soundness failure, asymptotic theorem, accepted prime-field result, or official Proximity Prize counterpacket.

## Metadata notice

The imported Cycle84 master JSON displays generator `X+1`, whereas the executable slot-log receipt and light verifier use `beta=X+2` as the primitive log generator. The verifier surfaces this as `NONFATAL_METADATA_MISMATCH` and binds all algebra to the executable slot-log generator. The finite product theorem and transfer are unaffected, but a publication bundle should correct the displayed generator metadata.

See `CHECKER_SPEC.md` for exact inputs, pseudocode, exit codes, and manifest policy.
