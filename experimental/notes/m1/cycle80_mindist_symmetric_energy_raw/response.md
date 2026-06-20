I'll start by reading the file index and key project files to understand the current state.Let me read the key project files and the most relevant scripts for this cycle.Let me read the core model definition and the most relevant scripts. I'll read several in parallel.This gives me the exact model. Now let me read the cycle77 subset injectivity check and the cycle79 involution verifier.I now understand the exact model. Let me read the cycle77 certificate, the cycle79 involution verifier, and the common-ratio audit to see precisely what is banked.Now let me read the cycle79 involution verifier and the common-ratio bound audit.Now let me read the common-ratio bound audit and raw response to understand the structure deeply.I now have the exact model. Key structural facts I've extracted: `eta^16 = 3` in F_17 (so the slot factors are `xi - eta^{2t}·3^b`), and pairs are already proven injective. Let me verify the environment can run Python and reconstruct the model.I have the full model. Before finalizing, let me confirm whether I can execute anything in this environment.## Environment status

I confirmed the harness is effectively read-only for me: the only working tool is `Read`. `bash_tool` returns "No such tool available," and I have no file‑writing tool wired in, so I cannot execute Python or write into `output_files`. Per discipline, all code below is marked **UNRUN**, and I deliver the artifacts inline for the director to save and run.

I read the model (`cycle68_slot_factorization_checker.py`), the pair-injectivity checker and certificate (`cycle77_*`), the involution verifier (`cycle79_involution_verifier.py`), and the Cycle 79 audit. Everything below is grounded in those.

## What is exactly true about the model (theorem-grade, from banked C1)

The Cycle 68 `C1` check (Codex-run) certifies the closed form

```
u_t(S) = 3^{-t} · ∏_{b∈S} ( ξ − η^{2t+16b} ),   ξ = β²,   S a legal 8-subset of Z/16.
```

Set `θ = η²`. Since `find_eta` forces `η¹⁶ = 3` (the embedded scalar) and `v₂(17¹⁶−1)=8`, `η` has order 256 and **`θ` is a primitive 128-th root of unity**. Writing the exponent as `m = t + 8b (mod 128)`:

```
u_t(S) = 3^{-t} · ∏_{m∈ι_t(S)} (ξ − θ^m),   ι_t(S) = { t + 8b mod 128 : b∈S }.
```

So slot `t` occupies the residue class `m ≡ t (mod 8)` of `Z/128`; the seven used slots are 7 of the 8 classes (class `0` ≡ unused `t=8`, the "scalar" coset `θ^{8b}=3^b`). The full-column product is `∏_{b}(ξ−θ^{t+8b}) = ξ¹⁶ − 9^t = β³² − 9^t = M_t`, matching `C4`, and complement ⇒ `u_t(S)u_t(S^c)=3^{-2t}M_t`, matching L‑CYCLE79.

This normal form is the right coordinate system: the `3^{-t}` factors **cancel in any fixed-slot product**, so all injectivity questions reduce to the raw products `Q_t(S)=∏_{m∈ι_t(S)}(ξ−θ^m)`.

## The exact three-slot rung, reduced (theorem-grade)

**Lemma A (weight-3 structure).** Any three-slot product collision differs in all three slots.
*Proof.* If a genuine collision agreed in one slot, cancel that nonzero factor; the remaining equality is a two-slot product collision, contradicting the banked pair-injectivity (Cycle 77 certificate). ∎

**Lemma B (ratio reformulation).** For a slot triple `(t1,t2,t3)`, define the achievable single-slot ratio set `R_t = { Q_t(S)/Q_t(S') : S≠S' }` (note `1∉R_t` by banked single-slot injectivity, and `R_t = R_t^{-1}`). Then

```
3-slot map is injective on triple (t1,t2,t3)
   ⇔  no r_k∈R_{t_k} with r1·r2·r3 = 1
   ⇔  (R_{t1} · R_{t2}) ∩ R_{t3} = ∅.
```

Moreover the obstruction is automatically nontrivial: `r1r2=1` is impossible (that is exactly pair-injectivity), so any solution forces `r3≠1`. ∎

So min-distance `≥4` for the product-fiber code is **equivalent to** the statement that no product of one ratio from each of two slots lands in a third slot's ratio set. This is the exact object the coherent-ratio route needs, and it makes the check cheap and certain.

## Verdict on the primary target

I cannot, by hand, certify injectivity or exhibit a collision for this specific `F_{17¹⁶}`: with `θ` and `ξ` living in the same large field there is no a‑priori independence to exploit, and I have no execution to run the finite check. I will not claim proof from unrun code.

Two honest statements I *can* make:

- **Heuristic (not a proof):** the 35 triples map `35·48³ ≈ 3.9·10⁶` products into `F^*` of size `~1.9·10¹⁹`; the birthday expectation of any collision is `~10⁻⁹`. Injectivity (min distance `≥4`) is the expected outcome, consistent with pairs and the L/R splits all being injective.
- **The rung is decidable by a small, certain, exhaustive check.** Below is an optimized checker that reuses the banked model construction verbatim (so it inherits Cycle 68's verified arithmetic) and decides the question with equality key = packed field product only, no heuristic.

## Deliverable 1 — `CHECKER.py` (UNRUN, exact, certain)

Reuses `cycle68` for model build and the Cycle 77 inline `X¹⁶ = −X⁸−3` reduction. Default decides all 35 triples; `--include-four` upgrades toward min-distance `≥5` for the energy route.

```python
#!/usr/bin/env python3
"""Cycle 80 three-slot product-injectivity decider (UNRUN here; run locally).

Equality key = packed field product ONLY. Color is recorded, never keyed.
Reuses cycle68 model build (verified C1..C6) and the cycle77 inline reduction.

Decision:
  all 35 triples product-injective  -> fiber_min_distance_lower_bound = 4
  any collision                     -> explicit three-slot collision packet
Place next to cycle68_slot_factorization_checker.py.
"""
from __future__ import annotations
import argparse, importlib.util, itertools, json
from pathlib import Path

P, NDEG = 17, 16
SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"

def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec); assert spec.loader is not None
    spec.loader.exec_module(mod); return mod

def dense(v):
    out = [0]*NDEG
    for i, x in enumerate(v[:NDEG]): out[i] = x % P
    return tuple(out)

def fmul_fast(a, b):                      # exact F_17[X]/(X^16+X^8+3) product
    tmp = [0]*31
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y: tmp[i+j] = (tmp[i+j] + x*y) % P
    for d in range(30, 15, -1):
        c = tmp[d] % P
        if c:
            tmp[d-8]  = (tmp[d-8]  - c)   % P
            tmp[d-16] = (tmp[d-16] - 3*c) % P
    return tuple(tmp[:16])

def pack(v):
    key = 0
    for c in reversed(v): key = key*P + c
    return key

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=3, choices=(3, 4))
    args = ap.parse_args()
    size = args.size

    c68 = load_cycle68()
    f   = c68.find_field_poly(); eta = c68.find_eta(f); beta = c68.find_beta(f)
    raw = c68.build_u(f, eta, beta)
    ONE = (1,) + (0,)*(NDEG-1)
    slot = {}                              # slot[t] = list of 48 dense values
    keyofk = {}                            # (i,a) per packed-index for witnesses
    for t in range(1, 8):
        vals = []
        for k in range(48):
            i, a = k//16 + 1, k % 16
            vals.append(dense(raw[(t, i, a)]))
            keyofk[k] = (i, a)
        slot[t] = vals
    color = {k: (c68.S_COLOR[k//16+1] + 8*((k % 16) % 2)) % 16 for k in range(48)}

    results, all_ok, collision = [], True, None
    for trip in itertools.combinations(range(1, 8), size):
        seen = {}
        # precompute first-two-slot products (injective: 2304 distinct), then extend
        head = trip[:-1]; last = trip[-1]
        pre = {}
        for ks in itertools.product(range(48), repeat=len(head)):
            pr = ONE
            for t, k in zip(head, ks): pr = fmul_fast(pr, slot[t][k])
            pre[ks] = pr
        hit = None
        for ks, prh in pre.items():
            for kl in range(48):
                key = pack(fmul_fast(prh, slot[last][kl]))
                full = ks + (kl,)
                if key in seen:
                    hit = (seen[key], full, key); break
                seen[key] = full
            if hit: break
        if hit:
            a_keys, b_keys, kval = hit
            collision = {
                "slots": list(trip),
                "assignment_A": [{"slot": t, "k": k, "ia": list(keyofk[k]),
                                  "color": color[k]} for t, k in zip(trip, a_keys)],
                "assignment_B": [{"slot": t, "k": k, "ia": list(keyofk[k]),
                                  "color": color[k]} for t, k in zip(trip, b_keys)],
                "packed_product": kval,
                "colorsum_A": sum(color[k] for k in a_keys) % 16,
                "colorsum_B": sum(color[k] for k in b_keys) % 16,
            }
            results.append({"slots": list(trip), "product_injective": False})
            all_ok = False; break
        results.append({"slots": list(trip), "product_injective": True,
                        "tuple_count": 48**size, "distinct_products": len(seen)})

    out = {
        "model": {"field_poly": list(f), "eta": list(eta), "beta": list(beta)},
        "key": "packed_product_only", "subset_size": size,
        "triples_checked": len(results),
        "all_checked_product_injective": all_ok, "results": results,
    }
    if all_ok:
        out["fiber_min_distance_lower_bound"] = size + 1
        out["decision"] = f"ALL_{size}_SUBSETS_PRODUCT_INJECTIVE"
    else:
        out["collision_packet"] = collision
        out["decision"] = "THREE_SLOT_PRODUCT_COLLISION_FOUND"
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
```

Cost: per triple it builds the 2304 head-products once, then `2304·48 ≈ 1.1·10⁵` extension multiplies; `×35 ≈ 3.9·10⁶` field multiplies total. Seconds in PyPy/numpy/C, a few minutes in CPython. The earlier "too slow for a heartbeat" was an unstructured `itertools.product(...,repeat=3)` over 110k full triple-products per triple with no head reuse; this is the same certainty at a fraction of the constant.

**Certificate format** (`RESULTS.json`): exactly the printed JSON. On the injective branch the bankable fields are `all_checked_product_injective: true`, `fiber_min_distance_lower_bound: 4`, `decision: ALL_3_SUBSETS_PRODUCT_INJECTIVE`. On the collision branch, `collision_packet` is the explicit packet acceptable output #2 requires: slot triple, both `(i,a)` assignments, matching `packed_product`, and both color sums (color reported, not keyed) — which feeds Lemma B's coherent ratio `r_k = Q_{t_k}(S_k)/Q_{t_k}(S_k')`.

## Secondary target — tau-symmetric setup and the exact next finite check

With the L/R split (`Φ = ℓρ`, both product-injective per Cycles 75/76), Cycle 78 gives `m(v) = #{ℓ∈L_img : v/ℓ∈R_img, colorL(ℓ)+colorR(v/ℓ)≡4}`. The additive-log symmetry `W_t(k)+W_t(τk)=c_t` integrates to the banked `Φ(τT)=K/Φ(T)`, `τ(P_0)=P_0`, hence `m(v)=m(K/v)`: the value space folds into `⌈·⌉/2` orbits `{v, K/v}`, with self-paired fibers (`v²=K`) of even size. This halves the census target but does not by itself yield 12.

The honest status of `m_max≤12`: it equals `max_v |L_img ∩ v·R_img^{-1}|` under the color‑4 filter — a multiplicative incidence bound between an explicit `48³` set and an explicit `48⁴` set. A soft code bound from min-distance `≥4` (even `≥5`) is far too weak (Singleton gives only `≤48⁴`); the constant 12 must come from the specific arithmetic. So the realistic staged plan, smallest exact rung first:

1. Run `CHECKER.py --size 3` → bank `L-CYCLE80-MINDIST≥4` or a collision packet. (This prompt's wall.)
2. Run `--size 4` → if injective, min-distance `≥5`, i.e. any two tuples in a fiber agree in `≤2` slots, so every projection of a fiber to 3 coordinates is injective. This is the strongest soft constraint available and the right input to the energy argument.
3. The exact finite check that actually decides ≤12 is the **L/R coincidence census**: hash `L_img` (110,592 keys), stream `R_img` (5,308,416), and accumulate, per realized value, the color‑4 fiber size, exploiting `m(v)=m(K/v)` to traverse one representative per τ-orbit. Max accumulated count `= m_max(β)`. This is a compiled-scale MITM, not `48⁷`; it is the same "REDUCTION_VERIFIED__FULL_MMAX_REQUIRES_COMPILED_RUN" boundary the project already recorded, now sharpened by τ-folding and (pending) min-distance `≥5`.

## Answer to the meta-question

Yes — there is a clean route to fully closing **this prompt's rung**, and it is bounded, certain, and heuristic-free: the reductions above (Lemmas A–B) turn the 35-triple question into the cheap MITM in `CHECKER.py`. The **next exact lemma/construction** is therefore:

> Run the size-3 checker. Either it returns `ALL_3_SUBSETS_PRODUCT_INJECTIVE` ⇒ bank **L-CYCLE79/80-MINDIST-EXACT: product-fiber minimum distance ≥ 4** (no weight-3 codeword, equivalently `(R_{t1}·R_{t2})∩R_{t3}=∅` for all 35 triples); or it returns a `collision_packet` ⇒ the explicit three-slot counter-packet with its coherent ratio `(r1,r2,r3)`, `r1r2r3=1`.

For the prize target `m_max(β)≤12`, the route is not soft-combinatorial; it is the τ-folded L/R coincidence census in step 3, which I have specified exactly but which needs a compiled run. I did not run any of this (read-only environment), so the primary target is **reduced and staged to a decidable bounded check**, not closed, and the secondary target's exact next check is identified.