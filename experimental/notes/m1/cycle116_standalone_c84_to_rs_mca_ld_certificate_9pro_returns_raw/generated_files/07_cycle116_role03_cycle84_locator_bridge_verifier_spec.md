# Cycle116 Role03 Cycle84-to-Locator Verifier Specification

## Scope

This verifier imports the accepted Cycle84 finite occupancy certificate and checks the algebraic bridge from the 336 slot records to the 113-point co-support locators, together with one explicit smooth `[512,256]` fixed-root lift. It does not rerun the 52.7-billion-incidence census and does not certify ordinary list decoding, protocol soundness, asymptotics, or official prize admissibility.

## Required clauses

1. Verify `X^16+X^8+3` is irreducible over `F_17`.
2. Verify `eta=6X^9` has order `256`, `eta^16=3`, and `beta=X+2` is outside `<eta>`.
3. Reconstruct the three formal degree-eight templates from the packet sets `E_i`; check their `Z^7` and `Z^6` coefficients vanish.
4. For every one of the 48 states `(i,a)`, construct the 16-point lift in `<eta^8>` and check distinctness.
5. For every one of the 336 triples `(t,i,a)`, construct the 16-point block locator, check coefficients in degrees `15,...,11` vanish, and check
   `R_{t,i,a}(beta)=3^t u_t(i,a)` against `data/slot_logs.json`.
6. Check the eight cosets `eta^t<eta^8>`, `0<=t<8`, partition `<eta>`. Deduce every tuple co-support has size `113` and the tuple-to-co-support map is injective.
7. Check the global six-jet
   `P_T=X^113-X^112+O(X^107)`
   and the exact scalar
   `P_T(beta)=kappa Phi(T)`, `kappa=4(X+1)!=0`.
8. Import and cross-check the finite certificate values
   `Occ=52,747,567,092`, `m_max=2`, `D=24`, 12 double fibers, no fibers of size at least 3.
9. Verify `eta` is nonsquare, construct `K=F_0(theta)` with `theta^2=eta`, verify `ord(theta)=512`, and set `H=<theta>`.
10. Use the explicit fixed set `R={theta^(2m+1):0<=m<137}`; verify disjointness, `|R|=137`, `P_R(beta)!=0`, lifted co-support size `250`, agreement `262`, and fixed six-jet preservation.
11. Verify `ord_512(17)=32`, hence `q_gen=q_code=q_line=17^32`; leave `q_chal` unset.
12. Verify `floor(17^32/2^128)=6` and `52,747,567,092>6` by exact integer arithmetic.

## Replay

```bash
python3 cycle116_role03_cycle84_locator_bridge_checker.py \
  /path/to/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro \
  > cycle116_role03_cycle84_locator_bridge_checker_output.json
```

Run without Python `-O`. Expected decision:

```text
CYCLE116_ROLE03_C84_LOCATOR_BRIDGE_VERIFIED
```

## Artifact hashes

```text
b22259612abd406de891adc2b98e4138999060db7853da3fe886fb97a76354aa  cycle116_role03_cycle84_locator_bridge_checker.py
48b898cfa5c82d92296e62d97004cc47904d389fde78657da8601fc17ea5fb13  cycle116_role03_cycle84_locator_bridge_checker_output.json
```
