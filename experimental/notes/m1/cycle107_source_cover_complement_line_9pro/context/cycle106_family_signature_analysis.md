# Cycle106 Family Signature Analysis

Status: AUDIT / EXPERIMENTAL_SIGNATURE_SUMMARY / EXACT_NEW_WALL.

This note records a second-layer finite signature audit for the Cycle106
k-free incidence stress families. It is finite toy evidence only: it is not a
Cycle106 theorem, not a source-valid `COUNTERPACKET`, and not prize-level
evidence.

## Artifacts

- Miner: `experimental/scripts/cycle106_family_signature_miner.py`
- Compact summary: `experimental/notes/m1/cycle106_family_signature_summary.json`
- Baseline full summary source: `experimental/notes/m1/cycle106_kfree_incidence_stress_extended_sigma2.jsonl`
- Family sample packets:
  `experimental/notes/m1/cycle106_kfree_incidence_stress_dominant_cluster.jsonl`
  and
  `experimental/notes/m1/cycle106_kfree_incidence_stress_distributed_dense_tail.jsonl`

Replay command:

```bash
python3 experimental/scripts/cycle106_family_signature_miner.py \
  --summary-jsonl experimental/notes/m1/cycle106_kfree_incidence_stress_extended_sigma2.jsonl \
  --json experimental/notes/m1/cycle106_family_signature_summary.json
```

The recomputed family totals match the summary rows in the extended JSONL.

## D8: Distributed Dense-Tail Family

Full count: `9,684` distributed dense-tail stress survivors.

By case:

| Case | Count |
|---|---:|
| `(43,14,2)` | 9,352 |
| `(37,12,2)` | 312 |
| `(31,10,2)` | 20 |

No distributed dense-tail survivors occur in `(23,11,2)` or `(41,10,2)`.
In this finite grid, the family appears exactly in the quotient-order-three
cases `(p-1)/n=3`; the tested quotient-order-two and quotient-order-four cases
do not contribute.

Occupancy aggregate:

| `H`-coset occupancy shape | Count |
|---|---:|
| `[1,1,1]` | 6,956 |
| `[2,1,1]` | 2,352 |
| `[2,2,1]` | 252 |
| `[3,2,1]` | 56 |
| `[2,2,2]` | 28 |
| `[8,3,1]` | 14 |
| `[9,2,1]` | 14 |
| `[7,2,1]` | 12 |

Active-count aggregate:

| Active count | Count |
|---|---:|
| 3 | 6,956 |
| 4 | 2,352 |
| 5 | 252 |
| 6 | 84 |
| 12 | 28 |
| 10 | 12 |

Main read: the dangerous distributed residual is mostly not a high-activity
cloud. It is a quotient-transversal phenomenon: three nonzero `H`-cosets, dense
coefficient tail, usually one active theta in each quotient coset, concentrated
near middle layers. For `(43,14,2)`, the largest layer counts are at `s=7`
with `3,276`, `s=8` with `2,394`, and `s=6` with `2,226`.

There is no obvious single coefficient-tail scalar relation explaining the
family. All `9,684` rows have `tail_weight_3`; only `260` have
`sigma2_tail_palindrome`, `838` have `inverse_pair_present`, and `278` have
`negation_pair_present`. Top repeated active triples in `(43,14,2)` recur
`29` times each, which is enough structure to mine, but not yet a theorem-level
parametrization.

Before the quotient-index probe below, this suggested narrowing D8 from
"distributed residual" to the temporary label:

`D8A-CYCLE106-QUOTIENT-THREE-DENSE-TAIL-TRANSVERSAL`

The probe below corrects this label further. The current live label is the
large/middle-layer version stated at the end of the probe section.

## Quotient-Index Probe

After the signature summary, a small quotient-index probe tested additional
cases:

```bash
python3 experimental/scripts/cycle106_family_signature_miner.py \
  --case 13,4,2 --case 19,6,2 --case 17,4,2 --case 37,9,2 \
  --case 31,6,2 --case 41,8,2 --case 43,7,2 \
  --json experimental/notes/m1/cycle106_quotient_index_signature_probe.json

python3 experimental/scripts/cycle106_kfree_incidence_stress.py \
  --case 13,4,2 --case 19,6,2 --case 17,4,2 --case 37,9,2 \
  --case 31,6,2 --case 41,8,2 --case 43,7,2 \
  --candidate-min-active 3 --stress-survivor-min-active 3 \
  --max-candidate-rows-per-case 0 \
  --jsonl experimental/notes/m1/cycle106_quotient_index_stress_probe.jsonl
```

Probe cases by quotient index `(p-1)/n`:

| Quotient index | Cases |
|---:|---|
| 3 | `(13,4,2)`, `(19,6,2)` |
| 4 | `(17,4,2)`, `(37,9,2)` |
| 5 | `(31,6,2)`, `(41,8,2)` |
| 6 | `(43,7,2)` |

Result: the family miner found zero dominant-cluster and zero
distributed-dense-tail rows in all seven cases. The stress checker also found
zero gated candidates and zero stress survivors in all seven cases. The only
rough active rows in this probe had active count `2`, in `(37,9,2)` and
`(43,7,2)`.

This corrected the first interpretation of D8A. The original distributed dense-tail
family is not explained by quotient index `3` alone: the smaller quotient-index
three cases `(13,4,2)` and `(19,6,2)` do not produce stress survivors. The
temporary reading after this probe was:

`D8A-CYCLE106-LARGE-MIDDLE-LAYER-Q3-DENSE-TAIL-TRANSVERSAL`

The fixed-field `p=61` probe below refutes the q=3-specific part of this label.

## Fixed-Field p=61 Quotient-Index Probe

A larger matched comparison fixed `p=61` and varied the subgroup size:

```bash
python3 experimental/scripts/cycle106_kfree_incidence_stress.py \
  --case 61,20,2 --case 61,15,2 --case 61,12,2 --case 61,10,2 \
  --candidate-min-active 3 --stress-survivor-min-active 3 \
  --max-candidate-rows-per-case 0 \
  --jsonl experimental/notes/m1/cycle106_p61_quotient_index_stress_probe.jsonl

python3 experimental/scripts/cycle106_family_signature_miner.py \
  --case 61,20,2 --case 61,15,2 --case 61,12,2 --case 61,10,2 \
  --summary-jsonl experimental/notes/m1/cycle106_p61_quotient_index_stress_probe.jsonl \
  --json experimental/notes/m1/cycle106_p61_family_signature_summary.json
```

The stress checker was optimized before this run so each `g(theta)` value is
computed once per `Uhat`, not once per `(Uhat,s,theta)`. The optimized script
preserves the same finite gate and compiled cleanly.

Stress-survivor and family totals:

| Case | Quotient index `(p-1)/n` | Stress survivors | Dominant cluster | Distributed dense-tail |
|---|---:|---:|---:|---:|
| `(61,20,2)` | 3 | 41,350 | 30,240 | 8,080 |
| `(61,15,2)` | 4 | 148,545 | 77,730 | 59,160 |
| `(61,12,2)` | 5 | 2,076 | 1,608 | 456 |
| `(61,10,2)` | 6 | 0 | 0 | 0 |

This refutes the q=3-specific D8A label. The largest p=61
distributed-dense-tail family occurs at quotient index `4`, not `3`.

The p=61 distributed dense-tail signatures still match the broader structural
pattern:

| Aggregate occupancy shape | Count |
|---|---:|
| `[1,1,1]` | 41,508 |
| `[2,1,1]` | 18,251 |
| `[2,2,1]` | 2,415 |
| `[1,1,1,1]` | 2,040 |
| `[2,1,1,1]` | 1,350 |

The p=61 dominant-cluster signatures also reinforce D3A:

| Aggregate occupancy shape | Count |
|---|---:|
| `[2,1]` | 75,835 |
| `[3,1]` | 8,425 |
| `[5,1]` | 5,715 |
| `[7,1]` | 2,421 |
| `[8,1]` | 2,409 |

Current D8 label:

`D8B-CYCLE106-DENSITY-ADMITTED-DENSE-TAIL-TRANSVERSAL`

The best finite reading is no longer quotient-index-specific. The dangerous
family is a density-gated dense-tail transversal across three or more
`H`-cosets, with the bulk in small active counts and one-per-coset or
two-plus-single occupancy. Quotient index affects severity, but it is not the
primary invariant.

## p=61 Density-Gate Sensitivity

The fixed-field p=61 result above still used the permissive toy density gate
from the stress checker. A post-processor recomputed family counts under
stricter layer-density gates without re-enumerating vectors:

```bash
python3 experimental/scripts/cycle106_density_sensitivity_from_signatures.py \
  --signature-json experimental/notes/m1/cycle106_p61_family_signature_summary.json \
  --stress-jsonl experimental/notes/m1/cycle106_p61_quotient_index_stress_probe.jsonl \
  --json experimental/notes/m1/cycle106_p61_density_sensitivity_summary.json \
  --density-den 20 --density-den 50 --density-den 100 --density-den 200 --density-den 500
```

Distributed dense-tail sensitivity:

| Density gate | Total | q=3 `(61,20,2)` | q=4 `(61,15,2)` | q=5 `(61,12,2)` |
|---|---:|---:|---:|---:|
| `1/20` | 67,696 | 8,080 | 59,160 | 456 |
| `1/50` | 5,831 | 20 | 5,355 | 456 |
| `1/100` | 866 | 20 | 390 | 456 |
| `1/200` | 456 | 0 | 0 | 456 |
| `1/500` | 0 | 0 | 0 | 0 |

Dominant-cluster sensitivity:

| Density gate | Total | q=3 `(61,20,2)` | q=4 `(61,15,2)` | q=5 `(61,12,2)` |
|---|---:|---:|---:|---:|
| `1/20` | 109,578 | 30,240 | 77,730 | 1,608 |
| `1/50` | 11,658 | 660 | 9,390 | 1,608 |
| `1/100` | 3,273 | 660 | 1,005 | 1,608 |
| `1/200` | 1,623 | 0 | 15 | 1,608 |
| `1/500` | 48 | 0 | 0 | 48 |

This is a real re-evaluation cut. The raw D8B mass is highly sensitive to the
toy density threshold: distributed dense-tail drops from `67,696` at `1/20` to
`5,831` at `1/50`, `866` at `1/100`, `456` at `1/200`, and zero at `1/500`.
Most of the q=4 bulk is therefore probably a permissive-density artifact unless
the actual corrected reserve admits those same layers.

The surviving strict-density residual is much smaller and concentrated in
`(61,12,2)`, quotient index `5`. That suggests a sharper follow-up target:

`D8C-CYCLE106-STRICT-DENSITY-RESIDUAL-TRANSVERSAL`

This is still finite toy bookkeeping only. It does not refute M1-C106, does not
produce a source-valid `COUNTERPACKET`, and does not prove that the q=5
residual exists under the true aperiodicity and reserve hypotheses.

## D3: Dominant-Cluster Family

Full count: `31,798` dominant-cluster stress survivors.

By case:

| Case | Count |
|---|---:|
| `(43,14,2)` | 29,162 |
| `(37,12,2)` | 2,094 |
| `(23,11,2)` | 462 |
| `(41,10,2)` | 80 |

The dominant family is overwhelmingly a two-`H`-coset phenomenon:
`31,086` of `31,798` rows have `H_coset_cover_2`, while only `712` have
`H_coset_cover_3`. It is also overwhelmingly "cluster plus one":
`30,234` rows are tagged `cluster_plus_one`, while `1,564` are
`cluster_plus_two`.

Occupancy aggregate:

| `H`-coset occupancy shape | Count |
|---|---:|
| `[2,1]` | 22,889 |
| `[3,1]` | 2,223 |
| `[7,1]` | 1,306 |
| `[6,1]` | 1,164 |
| `[8,1]` | 1,101 |
| `[9,1]` | 580 |
| `[5,1]` | 468 |
| `[3,2]` | 448 |

The coefficient-sparse explanation is false as a dominant account. Only
`2,100` of `31,798` rows are `coefficient_sparse`; `29,698` have dense
tail weight `3`. The right D3 target is not "kill sparse coefficients", but
"charge one-heavy-coset plus one/two outliers".

D3 should therefore be narrowed to:

`D3A-CYCLE106-DOMINANT-H-COSET-OUTLIER-CHARGE`

Prove that active profiles with occupancy `[m,1]` or `[m,1,1]` are quotient or
near-coset artifacts under the true aperiodicity hypotheses, or produce a
source-valid dominant-cluster stress family.

## Re-Evaluation Result

The old broad split remains correct:

- dominant-cluster survivors: `31,798`
- distributed dense-tail survivors: `9,684`

The new information is the sharper structure:

- D3 is mostly two-coset, cluster-plus-one/outlier charge.
- D8 is mostly density-admitted, dense-tail, three-or-more-coset transversal.
- Neither family can be dismissed as coefficient sparsity.
- Neither family is a `COUNTERPACKET` without source-valid aperiodicity and
  theorem-level parameter transfer.

Next computational check: add a small quotient-index sweep beyond the current
five cases, especially additional quotient-order-three cases and at least one
larger quotient-order-four/five case, to distinguish a genuine quotient-index
mechanism from a low-dimensional accident.

The first small quotient-index sweep was negative for all target families. The
fixed-field p=61 sweep then cut the q=3-specific interpretation: q=4 produced
the largest distributed dense-tail count. The next sweep should vary the
density gate and quotient index together, or try to prove a charge theorem for
dense-tail transversals independent of quotient index.
