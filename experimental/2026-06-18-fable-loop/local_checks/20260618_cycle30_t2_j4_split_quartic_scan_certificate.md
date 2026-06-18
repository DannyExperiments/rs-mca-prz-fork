# Cycle 30 T2J4 Split-Quartic Scan Certificate

Status: EXPERIMENTAL.

Script:

- `local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`

Command:

```bash
python3 experimental/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py
```

Result:

```text
cycle30_t2_j4_split_quartic_scan: EXPERIMENTAL
summary p=7 trials=20 off_R0_trials=19 min_C2=0 avg_C2=0.55 max_C2=2 avg_C2_over_p=0.079 avg_C2_over_p2=0.0112 off_R0_avg_C2=0.53
summary p=11 trials=20 off_R0_trials=20 min_C2=1 avg_C2=2.40 max_C2=4 avg_C2_over_p=0.218 avg_C2_over_p2=0.0198 off_R0_avg_C2=2.40
summary p=13 trials=16 off_R0_trials=16 min_C2=3 avg_C2=4.31 max_C2=10 avg_C2_over_p=0.332 avg_C2_over_p2=0.0255 off_R0_avg_C2=4.31
summary p=17 trials=10 off_R0_trials=10 min_C2=4 avg_C2=8.20 max_C2=12 avg_C2_over_p=0.482 avg_C2_over_p2=0.0284 off_R0_avg_C2=8.20
```

Additional bounded spot checks:

```text
extra summary p=19 trials=8 min=6 avg=11.75 max=17 avg/p=0.618 avg/p2=0.0325
extra summary p=23 trials=6 min=11 avg=17.00 max=25 avg/p=0.739 avg/p2=0.0321
extra summary p=29 trials=4 min=28 avg=31.25 max=35 avg/p=1.078 avg/p2=0.0372
```

Interpretation:

- The scan is direct experimental evidence only.
- The data lean toward `O(p)`-scale growth, not the naive positive-density
  `Theta(p^2)` heuristic from Cycle 30's generic two-quadric discussion.
- This suggests the next proof target should search for a hidden split-quadric
  collapse or rational-root/factorization mechanism.

Rejected overclaims:

- This is not a proof of `O(p)`.
- This is not evidence for a corrected-reserve theorem or full MCA statement.
- This does not check `c_b != 0` separately; it reports `off_R0` and direct
  slope counts in the same finite-field toy ledger.
