#!/usr/bin/env python3
"""Cycle 80 three-slot product-injectivity decider.

Equality key is packed field product only. Color is recorded in collision
packets, never used as an equality key.

Default mode checks all 35 three-slot product maps in the Cycle 68 finite
model. A passing certificate gives product-fiber minimum distance at least 4.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path


P = 17
NDEG = 16
SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"


def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def dense(v):
    out = [0] * NDEG
    for i, x in enumerate(v[:NDEG]):
        out[i] = x % P
    return tuple(out)


def fmul_fast(a, b):
    tmp = [0] * 31
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    tmp[i + j] = (tmp[i + j] + x * y) % P
    for d in range(30, 15, -1):
        c = tmp[d] % P
        if c:
            tmp[d - 8] = (tmp[d - 8] - c) % P
            tmp[d - 16] = (tmp[d - 16] - 3 * c) % P
    return tuple(tmp[:16])


def pack(v):
    key = 0
    for c in reversed(v):
        key = key * P + c
    return key


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=3, choices=(3, 4))
    args = parser.parse_args()
    size = args.size

    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    raw = c68.build_u(f, eta, beta)
    one = (1,) + (0,) * (NDEG - 1)

    slot = {}
    key_of_k = {}
    for t in range(1, 8):
        vals = []
        for k in range(48):
            i, a = k // 16 + 1, k % 16
            vals.append(dense(raw[(t, i, a)]))
            key_of_k[k] = (i, a)
        slot[t] = vals

    color = {
        k: (c68.S_COLOR[k // 16 + 1] + 8 * ((k % 16) % 2)) % 16
        for k in range(48)
    }

    results = []
    all_ok = True
    collision = None
    for slots in itertools.combinations(range(1, 8), size):
        seen = {}
        head, last = slots[:-1], slots[-1]
        pre = {}
        for keys in itertools.product(range(48), repeat=len(head)):
            prod = one
            for t, k in zip(head, keys):
                prod = fmul_fast(prod, slot[t][k])
            pre[keys] = prod

        hit = None
        for keys, prod_head in pre.items():
            for k_last in range(48):
                key = pack(fmul_fast(prod_head, slot[last][k_last]))
                full = keys + (k_last,)
                if key in seen:
                    hit = (seen[key], full, key)
                    break
                seen[key] = full
            if hit:
                break

        if hit:
            keys_a, keys_b, packed = hit
            collision = {
                "slots": list(slots),
                "assignment_A": [
                    {
                        "slot": t,
                        "k": k,
                        "ia": list(key_of_k[k]),
                        "color": color[k],
                    }
                    for t, k in zip(slots, keys_a)
                ],
                "assignment_B": [
                    {
                        "slot": t,
                        "k": k,
                        "ia": list(key_of_k[k]),
                        "color": color[k],
                    }
                    for t, k in zip(slots, keys_b)
                ],
                "packed_product": packed,
                "colorsum_A": sum(color[k] for k in keys_a) % 16,
                "colorsum_B": sum(color[k] for k in keys_b) % 16,
            }
            results.append({"slots": list(slots), "product_injective": False})
            all_ok = False
            break

        results.append(
            {
                "slots": list(slots),
                "product_injective": True,
                "tuple_count": 48**size,
                "distinct_products": len(seen),
            }
        )

    out = {
        "model": {"field_poly": list(f), "eta": list(eta), "beta": list(beta)},
        "key": "packed_product_only",
        "subset_size": size,
        "subsets_checked": len(results),
        "all_checked_product_injective": all_ok,
        "results": results,
    }
    if all_ok:
        out["fiber_min_distance_lower_bound"] = size + 1
        out["decision"] = f"ALL_{size}_SUBSETS_PRODUCT_INJECTIVE"
    else:
        out["collision_packet"] = collision
        out["decision"] = "PRODUCT_COLLISION_FOUND"
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
