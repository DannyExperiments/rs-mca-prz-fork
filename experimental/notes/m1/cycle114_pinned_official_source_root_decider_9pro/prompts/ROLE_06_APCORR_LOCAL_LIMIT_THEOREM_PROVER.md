# Role 06 - APcorr Local-Limit Theorem Prover

Your task is to prove or sharply cut the only proof route that would avoid
explicitly replaying every final color:

```text
official AP_corr + absence of frozen named charges
  => bounded interpolation-defect Fourier mass
  => t=1 local-limit cap
  => 2^128 * N_free <= q_line
```

Use only official predicates actually present in the packet. You may use
Fourier analysis, additive energy, restricted-sum anti-concentration,
uncertainty, interpolation defect spectra, source-visible rank, or inverse
theorems, but every hypothesis must be an official source-visible clause.

If you prove the implication, return:

```text
PROOF
T1_APCORR_LOCAL_LIMIT
```

If the implication is false or unsupported, return `ROUTE_CUT` or
`EXACT_NEW_WALL` with one of:

```text
explicit APcorr model that does not force Fourier flatness
exact additional APcorr clause needed
source-valid counterpacket mechanism exploiting Fourier concentration
```

Do not use random-like heuristics or informal "aperiodicity" claims.

