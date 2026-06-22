# Role 06 - APcorr To Fourier Prover

Your task is to prove the official APcorr-to-local-limit arrow, or cut it
sharply.

Cycle112 banked the conditional interface:

```text
bounded interpolation-defect Fourier mass
  => t=1 local-limit cap
  => correct q_line closure
```

The missing implication is:

```text
official AP_corr + absence of frozen named charges
  => bounded interpolation-defect Fourier mass
```

Try to prove this implication. You may use Fourier analysis, additive energy,
restricted-sum anti-concentration, uncertainty, interpolation-defect spectra,
or source-visible rank, but you must keep it tied to the official predicates
available in the packet.

If you prove the implication, return:

```text
PROOF
T1_APCORR_LOCAL_LIMIT
```

and show the final `2^128 * N_free <= q_line` closure.

If the implication is false or unsupported, return `ROUTE_CUT` or
`EXACT_NEW_WALL` with:

```text
explicit APcorr model that does not force Fourier flatness
or
exact additional APcorr clause needed
or
counterpacket mechanism exploiting Fourier concentration
```

Do not use an unproved random-like heuristic.

