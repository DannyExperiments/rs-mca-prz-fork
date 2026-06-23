# Role 02: Two-Ended Checker Engineer

Design the deterministic replay checker for Role05.

Target terminal:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

Read:

```text
context/cycle118_returns/05_role05_response.md
context/base_cycle118_context/cycle116_verifier/18_verify_cycle116_transfer_hypotheses.py
context/base_cycle118_context/cycle116_verifier/19_cycle116_checker_receipt.json
```

Your checker/spec must verify, fail-closed:

```text
Cycle84 imported occupancy N = 52,747,567,092
P_T(0) = -1 for every Cycle84 tuple, by symbolic slot identities
A* and R* partition the odd coset with |A*|=120, |R*|=136
P_R*(0) != 0
deg(P_R*(P_T-P_T')) <= 243
P_T*(beta) = nonzero_fixed_scalar * Phi(T)
distinct evaluations = 52,747,567,092
n=512, k=256, j=249, sigma=7, agreement=263
two-ended evaluator lemma hypotheses
noncontainment prerequisites
strict distance <250
```

Do not rerun a 52-billion enumeration unless unnecessary; import the hash-bound Cycle84 occupancy exactly as Cycle116 did. The output should make clear which parts are symbolic lemmas and which parts are finite checks.

If the checker cannot be made fail-closed from the attached data, return `ROUTE_CUT` and name the missing datum.
