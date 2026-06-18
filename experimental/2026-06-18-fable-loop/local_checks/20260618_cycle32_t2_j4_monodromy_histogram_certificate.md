# Cycle 32 T2J4 Monodromy Histogram Certificate

Status: EXPERIMENTAL / AUDIT.

Command:

```bash
python3 experimental/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py
python3 - <<'PY' ... larger p spot-checks ... PY
```

Output:

```text
cycle32_t2_j4_monodromy_histogram: EXPERIMENTAL / AUDIT
p=7 seed=0 q_gen=7 q_line=49 solved_z=38 singular_z=11 hist={'112': 7, '13': 13, '22': 2, '4': 10, 'nonsquarefree': 6} direct_C2=1 hist_C2=0 singular_split_C2=1 match=False landings=1
p=11 seed=0 q_gen=11 q_line=121 solved_z=110 singular_z=11 hist={'1111': 3, '112': 24, '13': 30, '22': 10, '4': 30, 'nonsquarefree': 13} direct_C2=3 hist_C2=3 singular_split_C2=0 match=True landings=3
p=13 seed=0 q_gen=13 q_line=169 solved_z=156 singular_z=13 hist={'1111': 3, '112': 30, '13': 58, '22': 17, '4': 38, 'nonsquarefree': 10} direct_C2=3 hist_C2=3 singular_split_C2=0 match=True landings=3
p=17 seed=0 q_gen=17 q_line=289 solved_z=269 singular_z=20 hist={'1111': 8, '112': 43, '13': 100, '22': 28, '4': 74, 'nonsquarefree': 16} direct_C2=8 hist_C2=8 singular_split_C2=0 match=True landings=8
case p=19
 seed=0 solved=335 singular=26 hist={'1111': 13, '112': 74, '13': 98, '22': 42, '4': 90, 'nonsquarefree': 18} direct_C2=14 hist_C2=13 singular_split_C2=1 match=False landings=14
 seed=1 solved=343 singular=18 hist={'1111': 14, '112': 77, '13': 121, '22': 35, '4': 82, 'nonsquarefree': 14} direct_C2=16 hist_C2=14 singular_split_C2=2 match=False landings=16
 seed=2 solved=339 singular=22 hist={'1111': 12, '112': 69, '13': 116, '22': 40, '4': 85, 'nonsquarefree': 17} direct_C2=13 hist_C2=12 singular_split_C2=1 match=False landings=13
 summary p=19 trials=3 avg_hist_C2=13.00 avg_over_p=0.684 avg_over_p2=0.0360
case p=23
 seed=0 solved=511 singular=18 hist={'1111': 11, '112': 121, '13': 168, '22': 60, '4': 129, 'nonsquarefree': 22} direct_C2=12 hist_C2=11 singular_split_C2=1 match=False landings=31
 seed=1 solved=511 singular=18 hist={'1111': 9, '112': 109, '13': 181, '22': 63, '4': 128, 'nonsquarefree': 21} direct_C2=9 hist_C2=9 singular_split_C2=0 match=True landings=9
 summary p=23 trials=2 avg_hist_C2=10.00 avg_over_p=0.435 avg_over_p2=0.0189
case p=29
 seed=0 solved=808 singular=33 hist={'1111': 33, '112': 193, '13': 259, '22': 101, '4': 197, 'nonsquarefree': 25} direct_C2=34 hist_C2=33 singular_split_C2=1 match=False landings=34
 summary p=29 trials=1 avg_hist_C2=33.00 avg_over_p=1.138 avg_over_p2=0.0392
```

Audit note:

The Cramer-system histogram agrees with direct support enumeration away from the singular determinant curve. Discrepancies are recorded as singular_split_C2 and remain experimental boundary contributions. The factorization distribution is compatible with a two-dimensional B-parameter family, but this is not a proof of S4 monodromy or a Theta(q_line) counterpacket.
