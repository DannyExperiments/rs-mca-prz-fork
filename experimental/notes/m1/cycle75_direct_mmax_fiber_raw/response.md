The index is huge. Let me read the specific files the prompt directs me to, starting with the cycle74/73 m1 notes.The index is very large. Let me grep for the specific files I need.I now have the key paths. Let me read the core cycle74/73 files and the cycle75 prompt directly.Now let me read the cycle75 prompt, the cycle73 checker and certificate, and the cycle68 checker.Let me find the actual checker scripts and certificate.Now let me read the cycle68 checker, cycle73 checker, cycle71 checker, and the cycle67 audit and the banked lemmas/walls.Now let me read the cycle73 and cycle71 checkers plus the banked lemmas, cuts, and walls.Let me read the banked lemmas, cuts/false routes, and active walls files.Let me find these files in the index.The top-level project files are at input_project/ directly. Let me read those plus the cycle66 occupancy script and cycle66 response to understand the model fully.Let me read the banked lemmas and cuts/false routes files.I have deep context now. Let me read the cuts file and the cycle66 occupancy self-check to nail down P_0 structure.PLAN (with one bankable design lemma `L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS` and two route-corrections)

Environment note: in this harness I have a read-only file tool and no code execution or file-write capability. So, like the Cycle 72–74 workers, I do not and cannot claim an executed pass. All code below is marked UNRUN and must not be treated as evidence. What is new and load-bearing here is (a) an exact, memory-bounded census design that removes the materialization problem cycle 74 worried about, (b) a corrected energy estimate that rehabilitates the original gate on the *right* domain, and (c) a route-cut showing the product ladder alone cannot finish.

## 1. Executive verdict and confidence

`m_max(beta) <= 12` is almost certainly true with enormous margin (high confidence as a prediction, zero as a certificate). The decisive new point is that Cycle 74's alarm number `7082` was computed on the wrong domain. The honest situation:

- The random-map heuristic on the *actual constrained* domain `P_0` gives ordered off-diagonal collision energy `D_constrained ~= |P_0|^2 / N = (5.2748e10)^2 / 4.8661e19 ~= 57.2`, comfortably below `155`, predicting `m_max ~= 2` (not `12`).
- Cycle 74's `~=7082` is `(48^7)^2/N`, i.e. the *unconstrained* `48^7` domain. Since `P_0` is a subset, `D_constrained <= D_unconstrained`, so the unconstrained figure only yields the weak rigorous-style bound `m_max(m_max-1) <= 7082 => m_max <= 84`. It does not refute `m_max <= 12`; it was never the right quantity.

So the target holds heuristically with slack `~12 vs ~2`. No rigorous moment shortcut closes it (see §4), so the finish line is a direct, lossless, memory-bounded max-fiber census, which is compiled-feasible.

## 2. Exact direct-`m_max` route

### 2.1 The domain `P_0`, made fully explicit

From `cycle68_slot_factorization_checker.py` and `cycle66_occupancy_selfcheck.py`, each slot `t in {1..7}` has 48 keys `k in {0..47}`, with `i=k//16+1`, `a=k%16`, slot value `u_t(k) in F^*` (48 distinct per slot, C5), and color

```text
color(k) = (S_COLOR[i] + 8*(a mod 2)) mod 16,  S_COLOR={1:15,2:9,3:12}.
```

The six attainable colors are exactly `{1,4,7,9,12,15}`, each realized by 8 keys (one `i`, one parity, 8 values of `a`). `P_0` is the single linear color constraint

```text
P_0 = { (k_1,...,k_7) : sum_t color(k_t) ≡ 4 (mod 16) },
|P_0| = 25152 * 8^7 = 52,747,567,104 = 393*2^27.
```

The target object is the product map `F(T) = prod_t u_t(k_t) in F^*` (this is `rho_beta` up to the global nonzero constant `(beta-1)3^12`, banked Cycle 66), and

```text
m_max = max_{v in F^*} #{ T in P_0 : F(T) = v }.
```

### 2.2 The three key types, kept strictly separate

- Product-equality key: the packed field element `F(T)` (16 base-17 digits). This is the only thing that certifies a collision.
- Lossless shard: a multiplicative class function of the product. The norm `N_{F/F_17}` (Cycle 73) is the order-16 instance; the *subfield-norm tower* gives arbitrarily fine lossless shards (§2.3).
- Color: a domain filter selecting `P_0`. It never certifies product equality.

### 2.3 Subfield-norm tower: free, lossless, arbitrarily-fine sharding

The norm to any subfield is multiplicative, so it is a function of the product alone (equal products always share it) and factors over slots. The tower of fixed fields of `Frob^e` gives

```text
N_{F/F_{17^2}}  : image order 17^2-1 = 288,
N_{F/F_{17^4}}  : image order 17^4-1 = 83,520,
N_{F/F_{17^8}}  : image order 17^8-1 = 6,975,757,440.
```

`N_{F/F_{17^8}}(v) = v * Frob^8(v) = v^{1+17^8}`. Precompute the 336 per-slot subfield norms `nu_t(k) = N_{F/F_{17^8}}(u_t(k)) in F_{17^8}^*` once; then for any tuple the shard index `prod_t nu_t(k_t)` is an `F_{17^8}` multiply-accumulate over 7 slots. This shards `P_0` into `~6.98e9` lossless buckets of average size `|P_0|/(17^8-1) ~= 7.56`. A genuine 13-fold product collision is wholly contained in one bucket, so it is never split. This is the sound, finer replacement for the order-16 norm bucket of Cycle 73/74 (and avoids any discrete-log assumption on `N`).

### 2.4 Memory-bounded meet-in-the-middle census

Split slots `L = {1,2,3}` (`48^3 = 110,592` left tuples) and `R = {4,5,6,7}` (`48^4 = 5,308,416` right tuples). For each tuple store `(packed product, color, subfield-norm shard)`. Stream `P_0` as color-matched pairs (`color_L + color_R ≡ 4`), route each combined tuple to its `F_{17^8}` shard, and within a shard accumulate `count[packed F(T)]`, tracking the global max and capturing any value that reaches 13 together with its preimages.

Roles: color selects which `(l,r)` pairs are in `P_0` (filter); the `F_{17^8}` norm routes losslessly (shard); `packed F(T)` is the dedup key (equality). Memory is `O(48^4)` for the right index plus one shard at a time (`~tens of tuples`) — it never holds `5e10` points. This is exactly the "without materializing all `>5e10` domain points" requirement, in the memory sense.

Honest complexity: time is `Theta(|P_0|) ~= 5.27e10` field products (the sum of all fiber sizes is `|P_0|`). With packed arithmetic, precomputed slot tables, and integer-keyed hashing this is a compiled multi-hour-to-overnight single-machine job, embarrassingly parallel across the `~7e9` shards. It is *not* sub-`|P_0|` (see §4 for why no exact sublinear-time route is known).

### 2.5 Ladder as accelerator, not finisher

If the 3-slot left map is product-injective (k=3 ladder) and the 4-slot right map is product-injective (k=4), then within any fiber each left value determines its left tuple and each right value its right tuple, so `fiber(v) = #{ a in LeftVals : v/a in RightVals, colors match }`. This cuts constants and confirms collisions are highly displaced, but it cannot finish: a k=5 pass forces colliding tuples to differ in `>= 6` of 7 slots (Cycle 71 full displacement), and the Singleton bound for a length-7, alphabet-48, min-distance-6 code gives only `m_max <= 48^2 = 2304`. So the ladder alone does not bound `m_max <= 12`.

## 3. Certificate schema and UNRUN reference checker

```json
{
  "key_semantics": {
    "equality_key": "packed_field_product",
    "lossless_shard": "N_{F/F_17^8}_of_product",
    "domain_filter": "color_sum_eq_4_mod_16"
  },
  "model": {"field_poly":"X^16+X^8+3","eta":"6X^9","beta":"X+2"},
  "P0": 52747567104,
  "selfchecks": {
    "prime_field_slot_identity_all_336": true,
    "subfield_norm_is_homomorphism": true,
    "color_sum_constraint_count_eq_P0": true
  },
  "ladder": [{"k":3,"left_injective":"UNRUN"},{"k":4,"right_injective":"UNRUN"}],
  "m_max": "UNRUN",
  "thirteen_fold_packet": null,
  "decision": "UNRUN_NO_PASS_CLAIMED"
}
```

```python
#!/usr/bin/env python3
"""Cycle 75 MITM subfield-norm-sharded max-fiber census. UNRUN reference.
Equality key = packed product; shard = N_{F/F_17^8}(product) (lossless);
color = domain filter for P_0. Pure Python is adequate only for the cheap
k=3/k=4 ladder; the full P_0 census needs the compiled, sharded port."""
from __future__ import annotations
import importlib.util, itertools, json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
C68 = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"
COLOR0 = 4  # sum_t color(k_t) ≡ 4 (mod 16) defines P_0

def load():
    spec = importlib.util.spec_from_file_location("c68", C68)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def pack(v):
    key = 0
    for c in reversed(tuple(v) + (0,)*(16-len(v))): key = key*17 + c
    return key
```

```python
def build(c68):
    f = c68.find_field_poly(); eta = c68.find_eta(f); beta = c68.find_beta(f)
    table = c68.build_u(f, eta, beta)
    S = c68.S_COLOR
    def color(k):
        i, a = k//16+1, k%16
        return (S[i] + 8*(a % 2)) % 16
    uval = lambda t,k: table[(t, k//16+1, k%16)]
    # subfield norm to F_17^8: v -> v * Frob^8(v) = v^(1+17^8); lossless shard
    sub = lambda v: c68.fmul(v, c68.fpow(v, c68.P**8, f), f)
    nu  = {(t,k): sub(uval(t,k)) for t in range(1,8) for k in range(48)}
    return f, color, uval, nu

def half(slots, color, uval, f, c68):
    out = []
    for keys in itertools.product(range(48), repeat=len(slots)):
        prod = c68.ONE; col = 0
        for t,k in zip(slots, keys):
            prod = c68.fmul(prod, uval(t,k), f); col = (col + color(k)) % 16
        out.append((keys, prod, col))
    return out  # left: 110592 entries; right: 5,308,416 entries
```

```python
def census(kmax_only=True):
    c68 = load(); f, color, uval, nu = build(c68)
    # CHEAP, runnable: k=3 (left) and k=4 (right) product injectivity rungs.
    left  = half((1,2,3),       color, uval, f, c68)
    right = half((4,5,6,7),     color, uval, f, c68)
    k3 = len({pack(p) for _,p,_ in left})  == 48**3
    k4 = len({pack(p) for _,p,_ in right}) == 48**4
    if kmax_only:
        return {"ladder":[{"k":3,"left_injective":k3},
                          {"k":4,"right_injective":k4}],
                "m_max":"UNRUN","decision":"LADDER_ONLY"}
    # FULL census (Theta(|P_0|)): compiled+sharded only. Sketch, UNRUN:
    #   index right by (color, packed product); stream color-matched left*right
    #   pairs, route by F_17^8 shard of product, count[packed product], capture
    #   first value reaching 13 with preimages. Never materialize all of P_0.
    raise SystemExit("full census requires compiled sharded run (UNRUN)")
```

This keeps the Cycle 71 product-only dedup discipline (packed product, never `(color,product)`), uses color strictly as the `P_0` filter, and uses the subfield norm strictly as a lossless shard.

## 4. What remains open

- No executed certificate: the `k=3`/`k=4` rungs (cheap: `110,592` and `5,308,416` products) and the full `P_0` census are all UNRUN here.
- No exact sublinear-time route. The census is `Theta(|P_0|)`. The reason a moment shortcut fails: `D_constrained ~= 57` is spread over `~28` independent double-collisions, so `D <= 155` is heuristically true but proving it is itself a collision count of the same `Theta(|P_0|)` order; and bounding `m_max <= 12` directly would need the 13th-order energy `E_13 = sum_v m_v...(m_v-12) = 0`, which is strictly harder than the census. Mode-of-sumset over `Z/N` has no known exact sub-`|A||B|` algorithm and `N ~= 4.9e19` forbids FFT binning. So `Theta(|P_0|)` time stands.
- Whether the constrained energy `D_constrained` is provably `<= 155` (which would give `m_max <= 12` with the Cycle 69 gate) is open; only the heuristic `~=57` is available.

## 5. Next exact lemma/construction

Bank the design as

```text
L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS:
  Splitting 7 = 3+4, using packed product as equality key, color-sum ≡ 4 (mod 16)
  as the P_0 filter, and N_{F/F_17^8} (order 17^8-1) as a lossless multiplicative
  shard computed from 336 precomputed per-slot subfield norms, the max-fiber
  census of F on P_0 runs in O(48^4) memory and Theta(|P_0|) time, never
  materializing all 5.27e10 points, and emits either m_max or an explicit
  13-fold packet (slots, 13 distinct key-tuples, shared product, shard).
```

and bank the corrective route-cuts

```text
W-CYCLE75-CONSTRAINED-ENERGY-IS-THE-RIGHT-SCALE:
  D_constrained ~= |P_0|^2/N ~= 57 (<155), not 7082; the 7082 figure is the
  unconstrained 48^7 over-count and yields only m_max <= 84.
W-CYCLE75-LADDER-CANNOT-FINISH:
  product injectivity through k=5 bounds collision support (differ in >=6 slots)
  but, by the Singleton bound (length 7, alphabet 48, distance 6), bounds m_max
  only by 48^2 = 2304, not 12.
```

Concrete next executable steps, in order: (1) run the cheap `k=3` left and `k=4` right injectivity rungs (seconds-to-minutes, would be the first real banked rung beyond `k=2`); (2) run the compiled, `F_17^8`-sharded MITM census of §2.4 to obtain `m_max` exactly (compiled overnight job), capturing a 13-packet if one exists; (3) optionally, certify `D_constrained <= 155` directly during the same pass as an independent cross-check against the Cycle 69 gate.

Do you see a route to a full solve? Yes. The next exact construction is `L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS`: a meet-in-the-middle (3+4) max-fiber census of the seven-slot product map on `P_0`, sharded losslessly by the `F_17^8` subfield norm and filtered by the color constraint, run in compiled code. It certifies `m_max <= 12` exactly in bounded memory; the heuristic constrained energy `~=57` says it will pass with margin `~12 vs ~2`. The k=3/k=4 ladder rungs are worth banking first as cheap supporting checks, but they cannot finish on their own.