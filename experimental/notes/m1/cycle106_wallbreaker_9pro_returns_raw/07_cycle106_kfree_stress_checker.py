#!/usr/bin/env python3
"""Bounded exact stress checker for the Cycle106 k-free incidence wall.

Mathematical model (d = sigma+1, r=d+1):

    theta active with witness S, |S|=s
    iff U(X) == (1-theta X) prod_{x in S}(1-xX) mod X^r.

Using T=H\\S and prod_H(1-xX)=1-X^n == 1 mod X^r,

    U(X) == (1-theta X) / prod_{x in T}(1-xX) mod X^r.

The exact all-U mode hashes the smaller of the S and T layers, so it enumerates
p*binom(n,min(s,n-s)) incidence records rather than p^(sigma+1) U-prefixes.
The local-exchange mode fixes one active pair and enumerates only supports at
bounded exchange distance, with theta read directly from the first coefficient.

This program deliberately does NOT pretend to implement the project/source
"above corrected reserve aperiodicity" predicate, because that predicate and
its reserve inequality are absent from the supplied compact Cycle106 packet.
It computes an explicit model obstruction filter AP_block and therefore emits
ROUTE_CUT_FINITE_MODEL_TOO_WEAK unless a future source-valid adapter is added.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Set, Tuple


STATUS_PASS = "PASS_NO_SUPERPOLY_PATTERN_IN_WINDOW"
STATUS_CANDIDATE = "COUNTERPACKET_CANDIDATE"
STATUS_ROUTE_CUT = "ROUTE_CUT_FINITE_MODEL_TOO_WEAK"


# ---------- finite-field and truncated-series utilities ----------

def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for q in small:
        if n % q == 0:
            return n == q
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for unsigned 64-bit integers.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_factors(n: int) -> List[int]:
    out: List[int] = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q = 3 if q == 2 else q + 2
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    phi = p - 1
    factors = prime_factors(phi)
    for g in range(2, p):
        if all(pow(g, phi // q, p) != 1 for q in factors):
            return g
    raise RuntimeError("failed to find a primitive root")


def subgroup(p: int, n: int) -> Tuple[int, List[int]]:
    if not is_prime_64(p):
        raise ValueError(f"p={p} is not prime")
    if (p - 1) % n:
        raise ValueError("require n | (p-1)")
    g = primitive_root(p)
    omega = pow(g, (p - 1) // n, p)
    H = [pow(omega, e, p) for e in range(n)]
    if len(set(H)) != n or pow(omega, n, p) != 1:
        raise AssertionError("subgroup construction failed")
    return omega, H


def mul_trunc(a: Sequence[int], b: Sequence[int], p: int, r: int) -> Tuple[int, ...]:
    out = [0] * r
    for i, ai in enumerate(a[:r]):
        if ai == 0:
            continue
        for j, bj in enumerate(b[: r - i]):
            if bj:
                out[i + j] = (out[i + j] + ai * bj) % p
    return tuple(out)


def inv_series(a: Sequence[int], p: int, r: int) -> Tuple[int, ...]:
    if not a or a[0] % p == 0:
        raise ValueError("series is not a unit")
    b = [0] * r
    b[0] = pow(a[0] % p, -1, p)
    for k in range(1, r):
        total = 0
        for i in range(1, min(k + 1, len(a))):
            total = (total + a[i] * b[k - i]) % p
        b[k] = (-b[0] * total) % p
    return tuple(b)


def locator_jet_from_exponents(E: Sequence[int], H: Sequence[int], p: int, r: int) -> Tuple[int, ...]:
    out: Tuple[int, ...] = (1,) + (0,) * (r - 1)
    for e in E:
        out = mul_trunc(out, (1, (-H[e]) % p), p, r)
    return out


def u_key_direct(theta: int, S: Sequence[int], H: Sequence[int], p: int, r: int) -> Tuple[int, ...]:
    gS = locator_jet_from_exponents(S, H, p, r)
    return mul_trunc((1, (-theta) % p), gS, p, r)


def u_key_complement(theta: int, T: Sequence[int], H: Sequence[int], p: int, r: int) -> Tuple[int, ...]:
    hT = locator_jet_from_exponents(T, H, p, r)
    return mul_trunc((1, (-theta) % p), inv_series(hT, p, r), p, r)


def exponents_to_values(E: Sequence[int], H: Sequence[int]) -> List[int]:
    return [H[e] for e in E]


def bit_values(mask: int) -> List[int]:
    out: List[int] = []
    while mask:
        lsb = mask & -mask
        out.append(lsb.bit_length() - 1)
        mask ^= lsb
    return out


# ---------- exact all-U pair-fiber scan ----------

@dataclass(frozen=True)
class ScanPlan:
    side: str
    layer_size: int
    subset_count: int
    pair_count: int


def choose_scan_plan(p: int, n: int, s: int, side: str) -> ScanPlan:
    if side == "auto":
        side = "direct" if s <= n - s else "complement"
    if side not in ("direct", "complement"):
        raise ValueError("side must be auto, direct, or complement")
    layer_size = s if side == "direct" else n - s
    subset_count = math.comb(n, layer_size)
    return ScanPlan(side, layer_size, subset_count, p * subset_count)


def scan_all_u(
    p: int,
    n: int,
    sigma: int,
    s: int,
    H: Sequence[int],
    side: str,
    max_pairs: int,
) -> Tuple[ScanPlan, Dict[Tuple[int, ...], int]]:
    r = sigma + 2
    plan = choose_scan_plan(p, n, s, side)
    if plan.pair_count > max_pairs:
        raise RuntimeError(
            f"bounded-window refusal: p*C(n,{plan.layer_size})={plan.pair_count} "
            f"exceeds max_pairs={max_pairs}"
        )
    masks: Dict[Tuple[int, ...], int] = {}
    all_exponents = tuple(range(n))
    for E in itertools.combinations(all_exponents, plan.layer_size):
        if plan.side == "direct":
            jet = locator_jet_from_exponents(E, H, p, r)
            for theta in range(p):
                key = mul_trunc((1, (-theta) % p), jet, p, r)
                masks[key] = masks.get(key, 0) | (1 << theta)
        else:
            invjet = inv_series(locator_jet_from_exponents(E, H, p, r), p, r)
            for theta in range(p):
                key = mul_trunc((1, (-theta) % p), invjet, p, r)
                masks[key] = masks.get(key, 0) | (1 << theta)
    return plan, masks


def collect_witnesses(
    wanted: Set[Tuple[int, ...]],
    p: int,
    n: int,
    sigma: int,
    s: int,
    H: Sequence[int],
    plan: ScanPlan,
) -> Dict[Tuple[int, ...], Dict[int, List[Tuple[int, ...]]]]:
    r = sigma + 2
    out: Dict[Tuple[int, ...], Dict[int, List[Tuple[int, ...]]]] = {
        key: defaultdict(list) for key in wanted
    }
    universe = set(range(n))
    for E in itertools.combinations(range(n), plan.layer_size):
        if plan.side == "direct":
            S = tuple(E)
            base = locator_jet_from_exponents(E, H, p, r)
        else:
            Tset = set(E)
            S = tuple(sorted(universe - Tset))
            base = inv_series(locator_jet_from_exponents(E, H, p, r), p, r)
        for theta in range(p):
            key = mul_trunc((1, (-theta) % p), base, p, r)
            if key in wanted:
                out[key][theta].append(S)
    return out


# ---------- bounded local-exchange scan around one active pair ----------

def parse_int_tuple(text: str) -> Tuple[int, ...]:
    if text.strip() == "":
        return tuple()
    return tuple(int(piece.strip()) for piece in text.split(",") if piece.strip())


def scan_local_exchanges(
    p: int,
    n: int,
    sigma: int,
    s: int,
    H: Sequence[int],
    theta0: int,
    S0: Tuple[int, ...],
    qmax: int,
    max_exchange_records: int,
) -> Tuple[Tuple[int, ...], Dict[int, List[Tuple[int, ...]]], int]:
    if len(S0) != s or len(set(S0)) != s or any(e < 0 or e >= n for e in S0):
        raise ValueError("base-support must be s distinct exponents in [0,n)")
    r = sigma + 2
    U = u_key_direct(theta0 % p, S0, H, p, r)
    base = set(S0)
    outside = set(range(n)) - base
    qcap = min(qmax, s, n - s)
    record_count = sum(math.comb(s, q) * math.comb(n - s, q) for q in range(qcap + 1))
    if record_count > max_exchange_records:
        raise RuntimeError(
            f"bounded-window refusal: exchange records={record_count} exceeds "
            f"max_exchange_records={max_exchange_records}"
        )
    witnesses: DefaultDict[int, List[Tuple[int, ...]]] = defaultdict(list)
    seen: Set[Tuple[int, Tuple[int, ...]]] = set()
    for q in range(qcap + 1):
        for B in itertools.combinations(sorted(base), q):
            sumB = sum(H[e] for e in B) % p
            Bset = set(B)
            for A in itertools.combinations(sorted(outside), q):
                # First-coefficient readout from
                # (1-theta0 X)g_B == (1-phi X)g_A mod X^r.
                phi = (theta0 + sumB - sum(H[e] for e in A)) % p
                S = tuple(sorted((base - Bset) | set(A)))
                if u_key_direct(phi, S, H, p, r) != U:
                    continue
                pair = (phi, S)
                if pair not in seen:
                    seen.add(pair)
                    witnesses[phi].append(S)
    return U, dict(witnesses), record_count


# ---------- obstruction diagnostics and exact collision verification ----------

def proper_nontrivial_subgroup_orders(n: int) -> List[int]:
    return [q for q in range(2, n) if n % q == 0]


def support_stabilizer_shifts(S: Sequence[int], n: int) -> List[int]:
    Sset = set(S)
    return [a for a in range(1, n) if {(e + a) % n for e in Sset} == Sset]


def difference_is_constant_on_K_cosets(S: Sequence[int], T: Sequence[int], n: int, q: int) -> bool:
    """K has order q; its exponent step is n/q. Constancy means K-invariance."""
    if q <= 1 or q >= n or n % q:
        raise ValueError("q must be a proper nontrivial divisor of n")
    step = n // q
    Sset, Tset = set(S), set(T)
    for residue in range(step):
        values = {
            (1 if e in Sset else 0) - (1 if e in Tset else 0)
            for e in range(residue, n, step)
        }
        if len(values) > 1:
            return False
    return True


def jet_stabilizer_shifts(U: Sequence[int], H: Sequence[int], p: int) -> List[int]:
    n = len(H)
    out = []
    for a in range(1, n):
        zeta = H[a]
        if all((u * pow(zeta, j, p) - u) % p == 0 for j, u in enumerate(U)):
            out.append(a)
    return out


def verify_witness_family(
    U: Tuple[int, ...],
    witnesses: Mapping[int, Sequence[Tuple[int, ...]]],
    p: int,
    n: int,
    sigma: int,
    s: int,
    H: Sequence[int],
) -> Dict[str, object]:
    r = sigma + 2
    verification_failures: List[object] = []
    support_stabilizers: List[object] = []
    coset_swap_hits: List[object] = []
    close_collision_failures: List[object] = []
    coset_swap_readout_failures: List[object] = []
    all_supports: List[Tuple[int, Tuple[int, ...]]] = []

    for theta, supports in witnesses.items():
        for S in supports:
            all_supports.append((theta, S))
            if len(S) != s or u_key_direct(theta, S, H, p, r) != U:
                verification_failures.append({"theta": theta, "support": list(S)})
            shifts = support_stabilizer_shifts(S, n)
            if shifts:
                support_stabilizers.append({"theta": theta, "support": list(S), "shifts": shifts})

    subgroup_orders = proper_nontrivial_subgroup_orders(n)
    for i, (theta, S) in enumerate(all_supports):
        for phi, T in all_supports[:i]:
            if S != T:
                for q in subgroup_orders:
                    if difference_is_constant_on_K_cosets(S, T, n, q):
                        hit = {
                            "theta": theta,
                            "phi": phi,
                            "support": list(S),
                            "other_support": list(T),
                            "subgroup_order": q,
                        }
                        coset_swap_hits.append(hit)
                        # Exact numerator fact: after cancelling the common part,
                        # both locator ratios are rational functions of X^q.  Their
                        # linear coefficients vanish, so a common-U collision must
                        # have theta=phi.  A distinct-theta hit would falsify either
                        # the witness equations or this implementation.
                        if theta != phi:
                            coset_swap_readout_failures.append(hit)
            if theta == phi:
                continue
            A = set(S) - set(T)
            B = set(T) - set(S)
            if len(A) != len(B):
                close_collision_failures.append({"reason": "unequal exchange sizes"})
                continue
            exchange = len(A)
            if exchange <= sigma:
                expected = (
                    exchange == 1
                    and theta in H
                    and phi in H
                    and A == {H.index(phi)}
                    and B == {H.index(theta)}
                )
                if not expected:
                    close_collision_failures.append(
                        {
                            "theta": theta,
                            "phi": phi,
                            "support": list(S),
                            "other_support": list(T),
                            "exchange": exchange,
                            "A": sorted(A),
                            "B": sorted(B),
                        }
                    )

    jet_stabilizers = jet_stabilizer_shifts(U, H, p)
    ap_block = not (
        verification_failures
        or support_stabilizers
        or coset_swap_hits
        or jet_stabilizers
    )
    return {
        "all_witness_equations_verified": not verification_failures,
        "verification_failures": verification_failures,
        "close_collision_lemma_verified": not close_collision_failures,
        "close_collision_failures": close_collision_failures,
        "model_aperiodicity_AP_block": ap_block,
        "model_aperiodicity_definition": (
            "trivial U-jet multiplicative stabilizer; every witness support has trivial H-stabilizer; "
            "no difference of distinct witness supports is constant on cosets of a proper nontrivial subgroup"
        ),
        "jet_stabilizer_shifts": jet_stabilizers,
        "support_stabilizer_hits": support_stabilizers,
        "whole_coset_swap_hits": coset_swap_hits,
        "whole_coset_swaps_force_same_theta_verified": not coset_swap_readout_failures,
        "whole_coset_swap_distinct_theta_failures": coset_swap_readout_failures,
        "proper_nontrivial_subgroup_orders_tested": subgroup_orders,
    }


def family_record(
    U: Tuple[int, ...],
    witnesses: Mapping[int, Sequence[Tuple[int, ...]]],
    p: int,
    n: int,
    sigma: int,
    s: int,
    omega: int,
    H: Sequence[int],
) -> Dict[str, object]:
    Hset = set(H)
    theta_values = sorted(witnesses)
    external = [theta for theta in theta_values if theta not in Hset]
    internal = [theta for theta in theta_values if theta in Hset]
    witness_json = {
        str(theta): [
            {
                "support_exponents": list(S),
                "support_values": exponents_to_values(S, H),
            }
            for S in witnesses[theta]
        ]
        for theta in theta_values
    }
    diagnostics = verify_witness_family(U, witnesses, p, n, sigma, s, H)
    canonical = json.dumps(
        {"U": U, "theta_values": theta_values, "witnesses": witness_json},
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    return {
        "Uhat_coefficients_low_to_high": list(U),
        "theta_values": theta_values,
        "external_theta_values": external,
        "internal_theta_values": internal,
        "distinct_theta_count": len(theta_values),
        "distinct_external_theta_count": len(external),
        "witnesses": witness_json,
        "diagnostics": diagnostics,
        "certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def summarize_masks(
    masks: Mapping[Tuple[int, ...], int], p: int, H: Sequence[int]
) -> Tuple[int, int, List[Tuple[Tuple[int, ...], int, int]]]:
    Hmask = 0
    for x in H:
        Hmask |= 1 << x
    allmask = (1 << p) - 1
    external_mask = allmask ^ Hmask
    scored: List[Tuple[Tuple[int, ...], int, int]] = []
    max_total = 0
    max_external = 0
    for key, mask in masks.items():
        total = mask.bit_count()
        external = (mask & external_mask).bit_count()
        max_total = max(max_total, total)
        max_external = max(max_external, external)
        scored.append((key, external, total))
    scored.sort(key=lambda item: (item[1], item[2], item[0]), reverse=True)
    return max_total, max_external, scored


def validate_parameters(p: int, n: int, sigma: int, s: int) -> Tuple[int, int]:
    if n < 1:
        raise ValueError("require n >= 1")
    if sigma < 0:
        raise ValueError("require sigma >= 0")
    r = sigma + 2
    d = sigma + 1
    if r > n:
        raise ValueError("require sigma+2 <= n for the banked complement truncation")
    if not (0 <= s <= n):
        raise ValueError("require 0 <= s <= n")
    # The bandwidth model has s=sigma+k with k>=1.
    if s < sigma + 1:
        raise ValueError("require s >= sigma+1 (equivalently bandwidth k=s-sigma >= 1)")
    return d, r


def main() -> None:
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--mode", choices=("all-u", "local-exchange"), default="all-u")
    parser.add_argument("--p", type=int, required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--sigma", type=int, required=True)
    parser.add_argument("--s", type=int, required=True)
    parser.add_argument("--side", choices=("auto", "direct", "complement"), default="auto")
    parser.add_argument("--max-pairs", type=int, default=2_000_000)
    parser.add_argument("--alarm-external", type=int, default=8)
    parser.add_argument("--top", type=int, default=1)
    parser.add_argument("--base-theta", type=int)
    parser.add_argument("--base-support", help="comma-separated subgroup exponents")
    parser.add_argument("--qmax", type=int)
    parser.add_argument("--max-exchange-records", type=int, default=2_000_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    d, r = validate_parameters(args.p, args.n, args.sigma, args.s)
    omega, H = subgroup(args.p, args.n)
    k = args.s - args.sigma

    source_gate = {
        "available": False,
        "reason": (
            "The supplied compact Cycle106 packet names above-reserve aperiodicity but contains neither "
            "the formal AP_src(Uhat) predicate nor the corrected-reserve inequality. AP_block is only a "
            "model obstruction filter and cannot be promoted to source-valid aperiodicity."
        ),
    }

    base_result: Dict[str, object] = {
        "schema": "cycle106-kfree-stress-v2",
        "parameters": {
            "p": args.p,
            "n": args.n,
            "sigma": args.sigma,
            "d": d,
            "r": r,
            "s": args.s,
            "k": k,
            "subgroup_generator_omega": omega,
            "subgroup_values_by_exponent": H,
            "alarm_external_distinct_theta": args.alarm_external,
        },
        "source_aperiodicity_and_reserve_gate": source_gate,
        "counting_convention": "distinct theta values; witness multiplicity is never substituted for numerator support",
    }

    prospective: str
    families: List[Dict[str, object]] = []

    if args.mode == "all-u":
        plan, masks = scan_all_u(
            args.p, args.n, args.sigma, args.s, H, args.side, args.max_pairs
        )
        max_total, max_external, scored = summarize_masks(masks, args.p, H)
        wanted_keys: Set[Tuple[int, ...]] = set()
        for key, external, total in scored[: max(0, args.top)]:
            wanted_keys.add(key)
        # Always retain representatives attaining both extrema.  These may differ:
        # the total maximum is often the unavoidable internal delete-one packet,
        # whereas the external maximum is the actual aperiodic-incidence stress target.
        if scored:
            wanted_keys.add(max(scored, key=lambda item: item[2])[0])
            wanted_keys.add(max(scored, key=lambda item: item[1])[0])
        alarm_key = next((key for key, ext, _ in scored if ext >= args.alarm_external), None)
        if alarm_key is not None:
            wanted_keys.add(alarm_key)
        witness_map = collect_witnesses(
            wanted_keys, args.p, args.n, args.sigma, args.s, H, plan
        ) if wanted_keys else {}
        for key in sorted(wanted_keys):
            families.append(
                family_record(key, witness_map[key], args.p, args.n, args.sigma, args.s, omega, H)
            )
        prospective = STATUS_CANDIDATE if max_external >= args.alarm_external else STATUS_PASS
        base_result["scan"] = {
            "mode": "all-u-pair-fiber",
            "side": plan.side,
            "enumerated_layer_size": plan.layer_size,
            "subset_count": plan.subset_count,
            "pair_record_count": plan.pair_count,
            "distinct_relevant_Uhat_prefixes": len(masks),
            "maximum_distinct_theta_count": max_total,
            "maximum_distinct_external_theta_count": max_external,
            "exhaustive_within_declared_finite_window": True,
        }
    else:
        if args.base_theta is None or args.base_support is None or args.qmax is None:
            raise SystemExit("local-exchange mode requires --base-theta, --base-support, and --qmax")
        S0 = parse_int_tuple(args.base_support)
        U, witnesses, record_count = scan_local_exchanges(
            args.p,
            args.n,
            args.sigma,
            args.s,
            H,
            args.base_theta % args.p,
            S0,
            args.qmax,
            args.max_exchange_records,
        )
        rec = family_record(U, witnesses, args.p, args.n, args.sigma, args.s, omega, H)
        families.append(rec)
        max_external = int(rec["distinct_external_theta_count"])
        prospective = STATUS_CANDIDATE if max_external >= args.alarm_external else STATUS_PASS
        qcap = min(args.qmax, args.s, args.n - args.s)
        base_result["scan"] = {
            "mode": "bounded-local-exchange",
            "base_theta": args.base_theta % args.p,
            "base_support_exponents": list(S0),
            "qmax": qcap,
            "exchange_record_count": record_count,
            "exhaustive_for_fixed_Uhat": qcap == min(args.s, args.n - args.s),
            "scope": (
                "all active supports at exchange distance <=qmax from the supplied active base; "
                "when qmax=min(s,n-s), this is exhaustive for that fixed Uhat"
            ),
        }

    # No source-valid gate is available in this packet. The exact finite/model
    # finding is retained as prospective_decision, but the emitted certificate
    # status is necessarily the route cut required by source hygiene.
    base_result["prospective_decision_if_source_gate_were_verified"] = prospective
    base_result["decision"] = STATUS_ROUTE_CUT
    base_result["families"] = families
    base_result["finite_interpretation"] = {
        "a_hit_proves": (
            "an exact finite Uhat prefix with the listed distinct theta values and verified subset witnesses; "
            "it may falsify a proposed finite obstruction classification"
        ),
        "a_hit_does_not_prove": (
            "source-valid aperiodicity, the corrected-reserve hypothesis, superpolynomial asymptotic growth, "
            "or an official Proximity Prize counterpacket without an inflation theorem"
        ),
        "a_pass_proves": (
            "absence of any alarm-reaching pair fiber in the declared exhaustive finite window, or absence "
            "within the declared local exchange radius"
        ),
        "a_pass_does_not_prove": (
            "an unspecified n^{O(1)} asymptotic bound; a fixed finite field always has the vacuous cap p"
        ),
    }

    text = json.dumps(base_result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError) as exc:
        print(json.dumps({"decision": STATUS_ROUTE_CUT, "error": str(exc)}, indent=2), file=sys.stderr)
        raise SystemExit(2)
