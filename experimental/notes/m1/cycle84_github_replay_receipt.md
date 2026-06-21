# Cycle 84 GitHub Replay Receipt

## Verdict

```text
PROOF / BANKABLE_LEMMA / PUBLIC_REPLAY
```

Confidence: high for the finite Cycle84 model certificate. This is a public
GitHub Actions replay of the exact certificate chain and the full projected
census plus kernel-3 lift. It is not a prize-level theorem by itself.

Run:

```text
repository: DannyExperiments/rs-mca-prz-fork
branch: cycle58-5p5-audit
workflow: Cycle84 certificate replay
run id: 27889140962
run URL: https://github.com/DannyExperiments/rs-mca-prz-fork/actions/runs/27889140962
head commit: 3914f4d08b6ca5b919c84fe2598e4e74685caec4
status: completed
conclusion: success
completed: 2026-06-21T01:09:37Z
```

## Jobs

```text
Light certificate chain
status: completed
conclusion: success
job URL: https://github.com/DannyExperiments/rs-mca-prz-fork/actions/runs/27889140962/job/82529457638
started: 2026-06-21T01:01:49Z
completed: 2026-06-21T01:01:58Z
```

The light job verified raw artifact hashes and the lightweight certificate. Its
logged certificate output included:

```json
{
  "decision": "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED",
  "exact_true_m_max": 2,
  "exact_true_occupancy": 52747567092,
  "exact_true_ordered_offdiagonal_energy": 24,
  "projected_max_multiplicity": 2,
  "projected_ordered_offdiagonal_energy": 120,
  "true_collision_tau_orbits": 6,
  "true_double_fibers": 12
}
```

```text
Full projected census and kernel lift
status: completed
conclusion: success
job URL: https://github.com/DannyExperiments/rs-mca-prz-fork/actions/runs/27889140962/job/82529457653
started: 2026-06-21T01:01:49Z
completed: 2026-06-21T01:09:37Z
```

The full job recompiled and reran the optimized projected census and kernel-3
duplicate lift on GitHub's Ubuntu runner. Its logged decisions included:

```text
TAU_FOLDED_PROJECTED_MMAX_LE_12
KERNEL_3_DUPLICATE_LIFT_COMPLETE
```

The kernel lift replay again logged:

```json
{
  "exact_true_m_max": 2,
  "exact_true_occupancy": 52747567092
}
```

and ended with:

```text
Projected census replay verified
Kernel lift replay verified
```

## Consequence

This public replay upgrades the Cycle84 finite-wall status from
"worker-provided full census plus local lightweight verifier" to
"public GitHub full replay receipt."

The banked finite result is:

```text
compatible pairs        = 52,747,567,104
distinct products       = 52,747,567,092
singleton fibers        = 52,747,567,080
double fibers           = 12
fibers of size >= 3     = 0
ordered off-diagonal D  = 24
m_max(beta)             = 2
Occ(beta)               = 52,747,567,092
```

The next exact target remains:

```text
L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER
```

Namely, splice the finite spectrum through the banked Cycle65-68
locator-evaluation reduction and record the official frontier-ledger entry

```text
Occ(beta)=52,747,567,092 > 2^32.
```
