#!/usr/bin/env python3
"""Cycle 75 MITM half-rung checker.

This script checks product-injectivity for the exact halves proposed by the
Cycle 75 meet-in-the-middle route:

  left slots  = (1, 2, 3)
  right slots = (4, 5, 6, 7)

The default is deliberately bounded and runs only the left half, which has
48^3 entries. The right half has 48^4 entries and is available behind an
explicit flag; it is intended as a reference path, not a heartbeat default.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
CYCLE68_PATH = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"
S_COLOR = {1: 15, 2: 9, 3: 12}


def load_cycle68():
    spec = importlib.util.spec_from_file_location("cycle68_checker", CYCLE68_PATH)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def pack(v):
    key = 0
    coeffs = tuple(v) + (0,) * (16 - len(v))
    for c in reversed(coeffs):
        key = key * 17 + c
    return key


def check_slots(c68, f, table, slots):
    seen = {}
    for keys in itertools.product(range(48), repeat=len(slots)):
        prod = c68.ONE
        color = 0
        for t, key in zip(slots, keys):
            i = key // 16 + 1
            a = key % 16
            prod = c68.fmul(prod, table[(t, i, a)], f)
            color = (color + S_COLOR[i] + 8 * (a % 2)) % 16
        packed = pack(prod)
        if packed in seen:
            return {
                "product_injective": False,
                "slots": list(slots),
                "keys_a": list(seen[packed]["keys"]),
                "keys_b": list(keys),
                "value": list(prod),
                "color_a": seen[packed]["color"],
                "color_b": color,
            }
        seen[packed] = {"keys": keys, "color": color}
    return {
        "product_injective": True,
        "slots": list(slots),
        "tuple_count": 48 ** len(slots),
        "distinct_products": len(seen),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--right4",
        action="store_true",
        help="also run the 48^4 right half; this is intentionally not default",
    )
    args = parser.parse_args()

    c68 = load_cycle68()
    f = c68.find_field_poly()
    eta = c68.find_eta(f)
    beta = c68.find_beta(f)
    table = c68.build_u(f, eta, beta)

    result = {
        "model": {
            "field_poly": list(f),
            "eta": list(eta),
            "beta": list(beta),
        },
        "key": "packed_product_only",
        "domain_filter_note": "colors recorded for P0 filtering, not used as equality keys",
        "left_123": check_slots(c68, f, table, (1, 2, 3)),
        "right_4567": "not_run",
    }
    if args.right4:
        result["right_4567"] = check_slots(c68, f, table, (4, 5, 6, 7))

    if result["left_123"]["product_injective"] and (
        result["right_4567"] == "not_run"
        or result["right_4567"]["product_injective"]
    ):
        result["decision"] = "MITM_HALF_RUNG_PASS_FOR_RUN_HALVES"
    else:
        result["decision"] = "MITM_HALF_RUNG_COLLISION_FOUND"

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
