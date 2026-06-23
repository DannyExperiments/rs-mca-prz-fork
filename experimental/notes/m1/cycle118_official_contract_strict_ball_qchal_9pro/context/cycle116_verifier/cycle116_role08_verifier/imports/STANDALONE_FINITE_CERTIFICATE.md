# Cycle84 Standalone Finite Certificate

Status: finite-model `PROOF`.

Scope: this proves an exact finite theorem for one explicit color-filtered
seven-slot product model. It is not, by itself, an RS-MCA/list-decoding/prize
theorem. The missing paper-facing bridge is a separate transfer theorem from
this finite model to the official RS parameters.

## 1. Theorem

Let

```text
F = F_17[X] / (X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2.
```

Use the Cycle68/Cycle84 seven-slot table with 48 states in each slot,
indexed by `(i,a)` with `i in {1,2,3}` and `a in Z/16Z`. Let `u_t(i,a)` be
the slot value in `F^*`, and let `color(i,a)` be the Cycle68 mod-16 color.

For a seven-tuple

```text
T = ((i_1,a_1), ..., (i_7,a_7))
```

define

```text
Phi(T) = product_{t=1}^7 u_t(i_t,a_t) in F^*.
```

Restrict to the color shell

```text
P_0 = { T : sum_t color(i_t,a_t) == 4 mod 16 }.
```

For each product value `v in F^*`, let

```text
m(v) = #{ T in P_0 : Phi(T) = v }.
```

Then the exact finite result is:

```text
m_max(beta) = max_v m(v) = 2.
```

More precisely, the product-fiber spectrum is:

```text
|P_0|                         = 52,747,567,104
#{v : m(v) = 1}               = 52,747,567,080
#{v : m(v) = 2}               = 12
#{v : m(v) >= 3}              = 0
#{v : m(v) > 0}               = 52,747,567,092
ordered off-diagonal energy D = 24
```

Thus the finite occupancy is:

```text
Occ(beta) = 52,747,567,092
          = 2^32 + 48,452,599,796.
```

## 2. What This Certificate Is Not

This certificate does not assert:

```text
1. a prize-level theorem;
2. an official RS-MCA/list-decoding transfer;
3. that Cycle84 is the final paper-facing object;
4. that the public replay verifies every earlier research transcript.
```

It only asserts the finite color-filtered product theorem above.

The exact transfer theorem still needed for paper-facing relevance has the
following shape:

```text
If the official RS-MCA/list-decoding reduction maps the relevant bad
configuration injectively or multiplicity-monotonically into this exact
Cycle84 color-filtered product model, preserving the color shell and product
fibers as specified, then m_max(beta)=2 gives the corresponding official
MCA/list-decoding occupancy bound.
```

That transfer theorem is not proved in this finite certificate.

## 3. Finite Field and Log Reduction

The multiplicative group has order

```text
N = 17^16 - 1
  = 48,661,191,875,666,868,480
  = 2^8 * 3^2 * 5 * 29 * 18913 * 41761 * 184417.
```

The verifier reconstructs the field and checks:

```text
X^16 + X^8 + 3 is irreducible over F_17;
gamma = X + 1 is primitive in F^*;
all 336 slot values u_t(i,a) are nonzero;
all 336 discrete-log identities are correct.
```

For every slot state, the certificate contains an exponent

```text
lambda_t(i,a) in Z/NZ
```

such that

```text
u_t(i,a) = gamma^lambda_t(i,a).
```

Therefore product equality is exactly equality of seven-term log sums modulo
`N`:

```text
Phi(T) = Phi(T')
iff
sum_t lambda_t(T_t) == sum_t lambda_t(T'_t) mod N.
```

This reduces the exhaustive product census to exact integer arithmetic.

## 4. Direct Full-Census Certificate

The direct checker uses the split

```text
left slots  = {1,2,3}
right slots = {4,5,6,7}.
```

It forms:

```text
48^3 = 110,592 left records
48^4 = 5,308,416 right records.
```

Right records are bucketed by color. For a left record of color `c`, only
right records of color `4-c mod 16` are compatible.

The checker partitions the full log interval `[0,N)` into 1536 disjoint
half-open shards. For every compatible left/right pair, it inserts the exact
full product log in the correct shard. The table key is the exact shard offset,
not a probabilistic hash key. The hash mixer only chooses the initial probe
position; equality is always tested on the complete key. Hence machine-hash
collisions cannot change multiplicities.

The recorded direct full-census output is:

```json
{
  "decision": "MMAX_CERTIFIED_LE_12",
  "compatible_pairs": 52747567104,
  "distinct_products": 52747567092,
  "D_offdiagonal_ordered": 24,
  "m_max": 2,
  "hit_value_log": null,
  "shards": {
    "total": 1536,
    "start": 0,
    "requested": 1536,
    "completed": 1536,
    "threads": 4
  }
}
```

The source and recorded output are:

```text
src/cycle84_exact_mmax_checker.cpp
output/fresh_full_certificate.json
```

The source SHA-256 is:

```text
1ed541cb5b60629d6864082a006b672ad5b6c9f100dcd6e41d537ef0809b6189
```

## 5. Histogram Rigidity Check

Let

```text
P = |P_0| = 52,747,567,104,
U = #{v : m(v)>0} = 52,747,567,092,
D = sum_v m(v)(m(v)-1) = 24.
```

For any finite fiber histogram:

```text
P - U = sum_{m(v)>0} (m(v)-1),
D     = sum_v m(v)(m(v)-1).
```

Therefore:

```text
D - 2(P-U)
  = sum_{m(v)>0} (m(v)-1)(m(v)-2).
```

Here:

```text
D - 2(P-U) = 24 - 2*12 = 0.
```

Every summand on the right is a nonnegative integer. Hence no occupied fiber
has multiplicity at least 3. Since the checker also gives `P-U=12`, exactly
12 fibers have multiplicity 2 and all other occupied fibers have multiplicity
1.

Thus:

```text
m_max(beta) <= 2.
```

The explicit double witness below proves equality.

## 6. Explicit Double Fiber

The following two tuples both lie in the color shell and have the same product:

```text
((1,4),(2,10),(3,14),(1,12),(3,0),(2,6),(3,8))
((2,0),(2,11),(1,7),(1,1),(3,9),(2,8),(1,14))
```

Their common product logarithm is:

```text
814,364,899,710,808,391.
```

Their common field product, written as coefficients in the basis
`1,X,...,X^15`, is:

```text
(3,16,6,13,15,10,10,11,8,5,12,9,13,6,4,3).
```

Direct field multiplication verifies the equality. Therefore:

```text
m_max(beta) >= 2.
```

Combined with the exhaustive upper bound, this proves:

```text
m_max(beta) = 2.
```

## 7. Public Replay Receipt

A public GitHub Actions run recompiled and reran the compact projected-census
and kernel-lift verifier:

```text
repository: DannyExperiments/rs-mca-prz-fork
branch: cycle58-5p5-audit
workflow: Cycle84 certificate replay
run id: 27889140962
run URL: https://github.com/DannyExperiments/rs-mca-prz-fork/actions/runs/27889140962
status: completed
conclusion: success
completed: 2026-06-21T01:09:37Z
```

The light job verified hashes and the compact certificate. The full job
recompiled and reran:

```text
src/tau_fold_full_optimized.cpp
src/tau_duplicate_lift.cpp
```

The logged terminal decisions were:

```text
TAU_FOLDED_PROJECTED_MMAX_LE_12
KERNEL_3_DUPLICATE_LIFT_COMPLETE
```

The public replay independently recorded:

```text
exact_true_m_max                  = 2
exact_true_occupancy              = 52,747,567,092
exact_true_ordered_offdiagonal_D  = 24
projected_max_multiplicity        = 2
projected_ordered_energy          = 120
true_collision_tau_orbits         = 6
true_double_fibers                = 12
slot_value_log_checks             = 336
```

## 8. Local Review Commands

From this directory:

```bash
python3 verify_certificate.py
```

Expected output:

```json
{
  "decision": "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED",
  "exact_true_m_max": 2,
  "exact_true_occupancy": 52747567092,
  "exact_true_ordered_offdiagonal_energy": 24,
  "projected_max_multiplicity": 2,
  "projected_ordered_offdiagonal_energy": 120,
  "slot_value_log_checks": 336,
  "true_collision_tau_orbits": 6,
  "true_double_fibers": 12
}
```

To rerun the compact public-replay path locally:

```bash
g++ -O3 -march=native -fopenmp -D_GLIBCXX_PARALLEL \
  src/tau_fold_full_optimized.cpp \
  -o /tmp/tau_fold_full_optimized

threads="$(nproc 2>/dev/null || sysctl -n hw.ncpu)"
OMP_NUM_THREADS="$threads" /tmp/tau_fold_full_optimized 16384 "$threads"

g++ -O3 -march=native src/tau_duplicate_lift.cpp -o /tmp/tau_duplicate_lift
/tmp/tau_duplicate_lift
```

To rerun the direct full-shard checker:

```bash
g++ -O3 -std=c++17 -pthread \
  src/cycle84_exact_mmax_checker.cpp \
  -o /tmp/cycle84_exact_mmax_checker

/tmp/cycle84_exact_mmax_checker \
  0 1536 1536 4 \
  /tmp/fresh_full_certificate.json
```

The direct full-shard run is the slower route. The recorded run took about
969 seconds with four threads.

## 9. Files in This Certificate

Core finite note:

```text
STANDALONE_FINITE_CERTIFICATE.md
```

Light verifier:

```text
verify_certificate.py
model/cycle68_slot_factorization_checker.py
data/slot_logs.json
data/cycle84_log_tau_certificate.json
data/cycle84_true_collision_pairs.json
```

Projected public-replay sources:

```text
src/logsM.hpp
src/logsN.hpp
src/tau_fold_full_optimized.cpp
src/tau_duplicate_lift.cpp
```

Direct full-census source:

```text
src/cycle84_exact_mmax_checker.cpp
```

Recorded outputs:

```text
output/tau_opt.out
output/tau_lift.out
output/fresh_full_certificate.json
cycle84_exact_mmax2_certificate.json
cycle84_master_proof_certificate.json
```

## 10. Reviewer Summary

The finite theorem is closed:

```text
For the explicit Cycle84 model at beta=X+2, m_max(beta)=2.
```

The paper-facing theorem is not closed by this file. The next mathematical
question is the transfer theorem:

```text
What exact RS-MCA/list-decoding reduction maps the official RS bad event into
this Cycle84 color-filtered product model with multiplicity no larger than
the finite model multiplicity?
```

Until that transfer theorem is supplied, this certificate should be cited only
as a standalone finite computation/theorem.
