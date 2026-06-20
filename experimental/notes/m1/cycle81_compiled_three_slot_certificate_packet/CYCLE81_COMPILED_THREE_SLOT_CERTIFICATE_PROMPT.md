# RS-MCA Cycle 81: Compiled Three-Slot Certificate Or Collision Packet

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Current Finite Model

We are in the M1 scalar-apolar finite model:

```text
F = F_17[X] / (X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

There are seven slots and 48 values per slot:

```text
Phi(T)=prod_{t=1}^7 u_t(k_t),  T=(k_1,...,k_7).
```

Constrained domain:

```text
P_0 = {T : sum_t color(k_t)=4 mod 16}.
```

Prize-local finite target:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

## Banked Facts

Cycle 75:

```text
slots {1,2,3}: 48^3 tuples, product map injective.
```

Cycle 76:

```text
slots {4,5,6,7}: 48^4 tuples, product map injective.
```

Cycle 77:

All singleton and pair slot-product maps are injective.

Cycle 78:

```text
m(v)=#{ l in L_img : v l^{-1} in R_img
        and colorL(l)+colorR(v l^{-1})=4 mod 16 }.
```

Cycle 79:

Complement involution:

```text
Phi(tau(T)) = K / Phi(T),  tau(P_0)=P_0,  m(v)=m(K/v).
```

Cycle 80:

Any three-slot collision must differ in all three slots, and for a triple
`(t1,t2,t3)` the product map is injective iff:

```text
(R_t1 R_t2) cap R_t3 = empty,
R_t = {u_t(k)/u_t(k') : k != k'}.
```

Codex preserved the pure-Python exact checker:

```text
current_repo_snapshot/experimental/scripts/cycle80_three_slot_injectivity_checker.py
```

but its first CPython run was too slow for a heartbeat-local bound and was
interrupted before producing a certificate.

## This Prompt's Exact Wall

Attack:

```text
V-CYCLE81-COMPILED-THREE-SLOT-CERTIFICATE
L-CYCLE80-MINDIST-CERTIFICATE
W-CYCLE80-COMPILED-MITM-MMAX-CENSUS
```

## Task

Primary target:

```text
Produce a theorem-grade executable certificate for all 35 three-slot product
maps, or produce an explicit three-slot product collision packet.
```

Preferred output:

1. A compact C, Rust, or optimized Python implementation that decides the
   all-triples question quickly using exact arithmetic in
   `F_17[X]/(X^16+X^8+3)`.
2. The precise certificate schema, with fields:
   `decision`, `subsets_checked`, `all_checked_product_injective`,
   `fiber_min_distance_lower_bound` on pass; or explicit
   `collision_packet` on fail.
3. If you can prove all-triples injectivity algebraically without code, give
   the proof. Do not handwave with birthday heuristics.

Secondary target:

```text
If the all-triples certificate is easy, specify the compiled MITM census that
decides m_max(beta)<=12 using the Cycle 78 L/R split and Cycle 79 tau-folding.
```

## Required Discipline

- Equality key is packed field product only.
- Color is a domain filter or collision annotation, not an equality key.
- Do not claim proof from unrun code.
- If your environment is read-only, say so and mark code `UNRUN`.
- Avoid broad planning. The immediate target is an executable certificate or
  explicit collision for the 35 three-slot maps.

## Useful Mounted Files

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle80_three_slot_injectivity_checker.py
current_repo_snapshot/experimental/notes/m1/m1_cycle80_mindist_symmetric_energy_audit.md
current_repo_snapshot/experimental/notes/m1/cycle80_mindist_symmetric_energy_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
```
