#!/usr/bin/env python3
"""Fail-closed verifier for V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE.

This verifier deliberately does not rerun the Cycle84 full census. It hash-binds
and checks the accepted finite outputs, then verifies all small field, fixed-jet,
product-scalar, smooth-lift, line-construction, and integer-ledger claims.

Exit codes:
  0  CYCLE116_TRANSFER_CERTIFICATE_VERIFIED
  1  CERTIFICATE_REJECTED
  2  MALFORMED_INPUT
  3  MISSING_FIXED_JET_CERTIFICATE
  4  MISSING_CYCLE84_ANCHOR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence


class Rejected(Exception):
    def __init__(self, clause: str, detail: str):
        super().__init__(f"{clause}: {detail}")
        self.clause = clause
        self.detail = detail


class Malformed(Exception):
    pass


def require(condition: bool, clause: str, detail: str) -> None:
    if not condition:
        raise Rejected(clause, detail)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise Malformed(f"cannot read JSON {path}: {exc}") from exc


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_sha256(obj: Any) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def is_prime_small(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


@dataclass(frozen=True)
class PrimeFieldExtension:
    p: int
    modulus: tuple[int, ...]

    def __post_init__(self) -> None:
        if self.p <= 2 or not is_prime_small(self.p):
            raise Malformed("base characteristic must be an odd prime")
        if len(self.modulus) < 2 or self.modulus[-1] % self.p != 1:
            raise Malformed("modulus must be monic")

    @property
    def degree(self) -> int:
        return len(self.modulus) - 1

    @property
    def q(self) -> int:
        return self.p ** self.degree

    def trim(self, a: Sequence[int]) -> tuple[int, ...]:
        b = [int(x) % self.p for x in a]
        while b and b[-1] == 0:
            b.pop()
        return tuple(b)

    @property
    def zero(self) -> tuple[int, ...]:
        return ()

    @property
    def one(self) -> tuple[int, ...]:
        return (1,)

    def emb(self, c: int) -> tuple[int, ...]:
        c %= self.p
        return (c,) if c else ()

    def add(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        n = max(len(a), len(b))
        r = [0] * n
        for i in range(n):
            r[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % self.p
        return self.trim(r)

    def neg(self, a: Sequence[int]) -> tuple[int, ...]:
        return self.trim([(-x) % self.p for x in a])

    def sub(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        return self.add(a, self.neg(b))

    def poly_mul_raw(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        if not a or not b:
            return ()
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x % self.p:
                for j, y in enumerate(b):
                    r[i + j] = (r[i + j] + x * y) % self.p
        return self.trim(r)

    def poly_divmod_raw(self, a: Sequence[int], b: Sequence[int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
        aa = list(self.trim(a))
        bb = list(self.trim(b))
        if not bb:
            raise ZeroDivisionError("polynomial division by zero")
        q = [0] * max(1, len(aa) - len(bb) + 1)
        inv_lead = pow(bb[-1], self.p - 2, self.p)
        while aa and len(aa) >= len(bb):
            d = len(aa) - len(bb)
            c = aa[-1] * inv_lead % self.p
            q[d] = c
            for i, y in enumerate(bb):
                aa[d + i] = (aa[d + i] - c * y) % self.p
            aa = list(self.trim(aa))
        return self.trim(q), self.trim(aa)

    def poly_mod_raw(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        return self.poly_divmod_raw(a, b)[1]

    def poly_gcd_raw(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        aa, bb = self.trim(a), self.trim(b)
        while bb:
            aa, bb = bb, self.poly_mod_raw(aa, bb)
        if aa:
            inv = pow(aa[-1], self.p - 2, self.p)
            aa = self.trim([(inv * x) % self.p for x in aa])
        return aa

    def mul(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        return self.poly_mod_raw(self.poly_mul_raw(a, b), self.modulus)

    def pow(self, a: Sequence[int], e: int) -> tuple[int, ...]:
        if e < 0:
            return self.pow(self.inv(a), -e)
        result = self.one
        base = self.poly_mod_raw(a, self.modulus)
        while e:
            if e & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            e >>= 1
        return result

    def inv(self, a: Sequence[int]) -> tuple[int, ...]:
        aa = self.trim(a)
        if not aa:
            raise ZeroDivisionError("field inverse of zero")
        return self.pow(aa, self.q - 2)

    def div(self, a: Sequence[int], b: Sequence[int]) -> tuple[int, ...]:
        return self.mul(a, self.inv(b))

    def irreducible_rabin(self) -> bool:
        # For n=16, the only prime divisor of n is 2. Rabin's criterion is:
        # X^(p^16)=X mod f and gcd(X^(p^8)-X,f)=1.
        n = self.degree
        if n != 16:
            raise Malformed("this checker version is pinned to degree 16")
        x = (0, 1)
        xp = x
        gcd8 = None
        for i in range(1, n + 1):
            xp = self.pow(xp, self.p)
            if i == 8:
                gcd8 = self.poly_gcd_raw(self.sub(xp, x), self.modulus)
        return gcd8 == self.one and self.sub(xp, x) == self.zero

    def elem_json(self, a: Sequence[int]) -> list[int]:
        aa = self.trim(a)
        return [aa[i] if i < len(aa) else 0 for i in range(self.degree)]


FElement = tuple[int, ...]
KElement = tuple[FElement, FElement]


@dataclass(frozen=True)
class QuadraticExtension:
    F: PrimeFieldExtension
    eta: FElement

    @property
    def zero(self) -> KElement:
        return (self.F.zero, self.F.zero)

    @property
    def one(self) -> KElement:
        return (self.F.one, self.F.zero)

    @property
    def theta(self) -> KElement:
        return (self.F.zero, self.F.one)

    @property
    def q(self) -> int:
        return self.F.q * self.F.q

    def emb(self, a: FElement) -> KElement:
        return (self.F.trim(a), self.F.zero)

    def add(self, x: KElement, y: KElement) -> KElement:
        return (self.F.add(x[0], y[0]), self.F.add(x[1], y[1]))

    def neg(self, x: KElement) -> KElement:
        return (self.F.neg(x[0]), self.F.neg(x[1]))

    def sub(self, x: KElement, y: KElement) -> KElement:
        return self.add(x, self.neg(y))

    def mul(self, x: KElement, y: KElement) -> KElement:
        a, b = x
        c, d = y
        ac = self.F.mul(a, c)
        bd_eta = self.F.mul(self.F.mul(b, d), self.eta)
        ad_bc = self.F.add(self.F.mul(a, d), self.F.mul(b, c))
        return (self.F.add(ac, bd_eta), ad_bc)

    def pow(self, x: KElement, e: int) -> KElement:
        if e < 0:
            return self.pow(self.inv(x), -e)
        result = self.one
        base = x
        while e:
            if e & 1:
                result = self.mul(result, base)
            base = self.mul(base, base)
            e >>= 1
        return result

    def inv(self, x: KElement) -> KElement:
        a, b = x
        if not a and not b:
            raise ZeroDivisionError("quadratic-field inverse of zero")
        # (a+b theta)^-1 = (a-b theta)/(a^2-b^2 eta)
        norm = self.F.sub(self.F.mul(a, a), self.F.mul(self.F.mul(b, b), self.eta))
        norm_inv = self.F.inv(norm)
        return (self.F.mul(a, norm_inv), self.F.neg(self.F.mul(b, norm_inv)))

    def div(self, x: KElement, y: KElement) -> KElement:
        return self.mul(x, self.inv(y))

    def elem_json(self, x: KElement) -> list[list[int]]:
        return [self.F.elem_json(x[0]), self.F.elem_json(x[1])]


# Generic polynomial helpers over an arbitrary field-like operation set.
def poly_mul_linear(
    coeffs: Sequence[Any],
    root: Any,
    zero: Any,
    add: Callable[[Any, Any], Any],
    neg: Callable[[Any], Any],
    mul: Callable[[Any, Any], Any],
) -> list[Any]:
    out = [zero for _ in range(len(coeffs) + 1)]
    minus_root = neg(root)
    for i, c in enumerate(coeffs):
        out[i] = add(out[i], mul(c, minus_root))
        out[i + 1] = add(out[i + 1], c)
    return out


def poly_eval(
    coeffs: Sequence[Any],
    x: Any,
    zero: Any,
    add: Callable[[Any, Any], Any],
    mul: Callable[[Any, Any], Any],
) -> Any:
    result = zero
    for c in reversed(coeffs):
        result = add(mul(result, x), c)
    return result


def prime_poly_from_roots(roots: Iterable[int], p: int) -> list[int]:
    coeffs = [1]
    for root in roots:
        out = [0] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            out[i] = (out[i] - c * root) % p
            out[i + 1] = (out[i + 1] + c) % p
        coeffs = out
    return coeffs


def eval_prime_coeff_poly_in_F(coeffs: Sequence[int], x: FElement, F: PrimeFieldExtension) -> FElement:
    result = F.zero
    for c in reversed(coeffs):
        result = F.add(F.mul(result, x), F.emb(c))
    return result


def hash_field_word_K(word: Sequence[KElement], K: QuadraticExtension) -> str:
    return canonical_sha256([K.elem_json(x) for x in word])


def hash_points_K(points: Iterable[KElement], K: QuadraticExtension) -> str:
    encoded = [K.elem_json(x) for x in points]
    encoded.sort()
    return canonical_sha256(encoded)


def verify_imports(anchor_path: Path, anchor: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, str]]:
    require(anchor.get("schema") == "cycle116.cycle84_anchor.v1", "ANCHOR_SCHEMA", "unexpected anchor schema")
    imported = anchor.get("imported_files")
    if not isinstance(imported, dict):
        raise Malformed("anchor imported_files must be an object")
    loaded: dict[str, Any] = {}
    hashes: dict[str, str] = {}
    for name in ("master", "slot_logs", "light_receipt", "standalone_note"):
        rec = imported.get(name)
        if not isinstance(rec, dict) or "path" not in rec or "sha256" not in rec:
            raise Malformed(f"missing imported file descriptor {name}")
        path = (anchor_path.parent / rec["path"]).resolve()
        require(path.is_file(), "IMPORTED_FILE_MISSING", f"{name}: {path}")
        actual = sha256_file(path)
        require(actual == rec["sha256"], "IMPORTED_FILE_HASH", f"{name}: expected {rec['sha256']} got {actual}")
        hashes[name] = actual
        if name == "standalone_note":
            loaded[name] = path.read_text(encoding="utf-8")
        else:
            loaded[name] = load_json(path)
    return loaded["master"], loaded["slot_logs"], loaded["light_receipt"], hashes


def verify_cycle84_anchor(anchor: dict[str, Any], master: dict[str, Any], light: dict[str, Any]) -> dict[str, int]:
    vals = anchor.get("accepted_finite_values")
    if not isinstance(vals, dict):
        raise Malformed("accepted_finite_values missing")
    expected = {
        "packet_supports": 52_747_567_104,
        "distinct_products": 52_747_567_092,
        "ordered_offdiagonal_energy": 24,
        "m_max": 2,
        "singleton_fibers": 52_747_567_080,
        "double_fibers": 12,
        "fibers_ge_3": 0,
    }
    require(vals == expected, "ANCHOR_VALUES", f"accepted values differ from pinned values: {vals}")
    require(master.get("decision") == "CYCLE84_FINITE_WALL_PROVED", "MASTER_DECISION", str(master.get("decision")))
    require(master.get("compatible_pairs") == expected["packet_supports"], "MASTER_PACKET_SUPPORTS", "compatible_pairs mismatch")
    require(master.get("distinct_products") == expected["distinct_products"], "MASTER_OCCUPANCY", "distinct_products mismatch")
    require(master.get("D_offdiagonal_ordered") == expected["ordered_offdiagonal_energy"], "MASTER_ENERGY", "energy mismatch")
    require(master.get("m_max") == expected["m_max"], "MASTER_MMAX", "m_max mismatch")
    hist = master.get("fiber_histogram", {})
    require(hist.get("multiplicity_1") == expected["singleton_fibers"], "MASTER_HISTOGRAM", "singleton count mismatch")
    require(hist.get("multiplicity_2") == expected["double_fibers"], "MASTER_HISTOGRAM", "double count mismatch")
    require(hist.get("multiplicity_ge_3") == 0, "MASTER_HISTOGRAM", "multiplicity >=3 is nonzero")
    require(light.get("decision") == "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED", "LIGHT_RECEIPT", str(light.get("decision")))
    require(light.get("exact_true_occupancy") == expected["distinct_products"], "LIGHT_OCCUPANCY", "light receipt mismatch")
    require(light.get("exact_true_m_max") == 2, "LIGHT_MMAX", "light receipt mismatch")
    require(light.get("exact_true_ordered_offdiagonal_energy") == 24, "LIGHT_ENERGY", "light receipt mismatch")
    require(light.get("true_double_fibers") == 12, "LIGHT_DOUBLES", "light receipt mismatch")
    P = expected["packet_supports"]
    U = expected["distinct_products"]
    D = expected["ordered_offdiagonal_energy"]
    require(P - U == 12, "HISTOGRAM_RIGIDITY", "P-U != 12")
    require(D - 2 * (P - U) == 0, "HISTOGRAM_RIGIDITY", "D-2(P-U) != 0")
    require(expected["singleton_fibers"] + expected["double_fibers"] == U, "HISTOGRAM_RIGIDITY", "occupied-fiber counts do not sum to U")
    require(expected["singleton_fibers"] + 2 * expected["double_fibers"] == P, "HISTOGRAM_RIGIDITY", "fiber weighted sum does not equal P")
    return expected


def main_verify(anchor_path: Path, fixed_path: Path) -> dict[str, Any]:
    anchor = load_json(anchor_path)
    fixed = load_json(fixed_path)
    require(fixed.get("schema") == "cycle116.fixed_jet_and_smooth_lift.v1", "FIXED_JET_SCHEMA", "unexpected fixed-jet schema")

    master, slot_logs, light, import_hashes = verify_imports(anchor_path, anchor)
    finite = verify_cycle84_anchor(anchor, master, light)

    field_cfg = fixed["field"]
    p = int(field_cfg["p"])
    modulus = tuple(int(x) for x in field_cfg["modulus_coefficients_low_to_high"])
    F = PrimeFieldExtension(p, modulus)
    require(F.degree == int(field_cfg["degree"]) == 16, "FIELD_DEGREE", "degree mismatch")
    require(F.irreducible_rabin(), "FIELD_IRREDUCIBILITY", "X^16+X^8+3 is reducible")

    eta = F.trim(field_cfg["eta_coefficients_low_to_high"])
    beta = F.trim(field_cfg["beta_coefficients_low_to_high"])
    log_generator = F.trim(field_cfg["slot_log_generator_coefficients_low_to_high"])
    require(modulus == (3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1), "FIELD_MODULUS", "modulus is not the pinned polynomial")
    require(eta == (0,0,0,0,0,0,0,0,0,6), "ETA_VALUE", "eta is not 6 X^9")
    require(beta == (2,1), "BETA_VALUE", "beta is not X+2")
    require(log_generator == beta, "LOG_GENERATOR", "slot log generator must be beta=X+2")

    factorization = {int(k): int(v) for k, v in field_cfg["multiplicative_group_factorization"].items()}
    require(all(is_prime_small(q) and e >= 1 for q, e in factorization.items()), "GROUP_FACTORIZATION", "non-prime factor or nonpositive exponent")
    group_order = F.q - 1
    product = math.prod(q ** e for q, e in factorization.items())
    require(product == group_order, "GROUP_FACTORIZATION", "factorization does not multiply to 17^16-1")
    for q in factorization:
        require(F.pow(log_generator, group_order // q) != F.one, "LOG_GENERATOR_PRIMITIVITY", f"generator fails prime divisor {q}")
    require(F.pow(log_generator, group_order) == F.one, "LOG_GENERATOR_PRIMITIVITY", "generator^(q-1) != 1")

    expected_cfg = fixed["expected"]
    require(F.pow(eta, 16) == F.emb(expected_cfg["eta_power_16_prime_field_value"]), "ETA_POWER_16", "eta^16 != 3")
    require(F.pow(eta, 256) == F.one and F.pow(eta, 128) != F.one, "ETA_ORDER", "eta does not have exact order 256")
    minus_one = F.emb(-1)
    euler_eta = F.pow(eta, group_order // 2)
    require(euler_eta == minus_one, "ETA_NONSQUARE", "Euler criterion does not give -1")
    require(F.pow(beta, 256) != F.one, "BETA_OUTSIDE_NATIVE_DOMAIN", "beta lies in <eta>")

    packet = fixed["packet"]
    E_sets = {int(i): tuple(int(e) for e in es) for i, es in packet["base_exponent_sets"].items()}
    expected_base = {int(i): [int(c) for c in cs] for i, cs in packet["expected_base_locator_coefficients_low_to_high"].items()}
    color_offsets = {int(i): int(c) for i, c in packet["color_offsets"].items()}
    require(set(E_sets) == {1,2,3}, "PACKET_BASE_SETS", "expected indices 1,2,3")
    base_polys: dict[int, list[int]] = {}
    for i in (1,2,3):
        require(len(E_sets[i]) == 8 and len(set(E_sets[i])) == 8, "PACKET_BASE_SETS", f"E_{i} is not an 8-set")
        roots = [pow(3, e % 16, p) for e in E_sets[i]]
        coeffs = prime_poly_from_roots(roots, p)
        require(coeffs == expected_base[i], "BASE_LOCATOR_COEFFICIENTS", f"base polynomial {i} mismatch: {coeffs}")
        require(len(coeffs) == 9 and coeffs[8] == 1 and coeffs[7] == 0 and coeffs[6] == 0,
                "BASE_LOCATOR_TOP_JET", f"base polynomial {i} lacks zero Z^7,Z^6 coefficients")
        base_polys[i] = coeffs

    # Native order-256 domain and its order-32 subgroup.
    D_native = [F.pow(eta, m) for m in range(256)]
    D_native_set = set(D_native)
    require(len(D_native_set) == 256, "NATIVE_DOMAIN", "<eta> has fewer than 256 points")
    H0 = [F.pow(eta, 8*m) for m in range(32)]
    require(len(set(H0)) == 32, "HALF_SUBGROUP", "<eta^8> has fewer than 32 points")
    square_fibers: dict[FElement, int] = {}
    for y in H0:
        y2 = F.mul(y, y)
        square_fibers[y2] = square_fibers.get(y2, 0) + 1
    expected_squares = {F.emb(pow(3, b, p)) for b in range(16)}
    require(set(square_fibers) == expected_squares and set(square_fibers.values()) == {2},
            "HALF_SUBGROUP_SQUARE_MAP", "square map is not 2-to-1 onto <3>")

    # Parse and index the 336 certified slot logs.
    require(slot_logs.get("N") == group_order, "SLOT_LOG_ORDER", "slot log modulus mismatch")
    require(slot_logs.get("generator") == list(field_cfg["slot_log_generator_coefficients_low_to_high"]),
            "SLOT_LOG_GENERATOR", "slot_logs.json is not based at beta=X+2")
    log_factorization = {int(k): int(v) for k, v in slot_logs.get("factors", {}).items()}
    require(log_factorization == factorization, "SLOT_LOG_FACTORIZATION", "slot log factorization mismatch")
    records = slot_logs.get("records")
    require(isinstance(records, list) and len(records) == int(expected_cfg["slot_state_count"]) == 336,
            "SLOT_LOG_COUNT", "expected 336 records")
    record_by_key: dict[tuple[int,int,int], dict[str, Any]] = {}
    for rec in records:
        key = (int(rec["t"]), int(rec["i"]), int(rec["a"]))
        require(key not in record_by_key, "SLOT_LOG_DUPLICATE_KEY", str(key))
        record_by_key[key] = rec
    mods = [int(x) for x in slot_logs.get("mods", [])]

    lift_sets: dict[tuple[int,int], tuple[FElement, ...]] = {}
    bsets_seen: set[tuple[int, ...]] = set()
    state_colors: dict[tuple[int,int], int] = {}
    for i in (1,2,3):
        for a in range(16):
            bset = tuple(sorted((a + e) % 16 for e in E_sets[i]))
            require(bset not in bsets_seen, "PACKET_STATE_DISTINCTNESS", f"duplicate shifted exponent set {i},{a}")
            bsets_seen.add(bset)
            color = sum(bset) % 16
            expected_color = (color_offsets[i] + 8*(a & 1)) % 16
            require(color == expected_color, "PACKET_COLOR", f"state {(i,a)} color mismatch")
            state_colors[(i,a)] = color
            targets = {F.emb(pow(3, b, p)) for b in bset}
            roots = tuple(y for y in H0 if F.mul(y, y) in targets)
            require(len(roots) == 16 and len(set(roots)) == 16, "PACKET_LIFT_SIZE", f"state {(i,a)} does not lift to 16 roots")
            lift_sets[(i,a)] = roots
    require(len(bsets_seen) == 48, "PACKET_STATE_DISTINCTNESS", "not all 48 states are distinct")

    slot_values: dict[tuple[int,int,int], FElement] = {}
    block_roots: dict[tuple[int,int,int], tuple[FElement, ...]] = {}
    block_locator_hashes: list[str] = []
    beta2 = F.mul(beta, beta)
    eta_inv = F.inv(eta)
    for t in packet["slot_indices"]:
        t = int(t)
        require(1 <= t <= 7, "SLOT_INDEX", f"bad slot {t}")
        eta_t = F.pow(eta, t)
        eta_minus_2t = F.pow(eta_inv, 2*t)
        for i in (1,2,3):
            for a in range(16):
                roots = tuple(F.mul(eta_t, y) for y in lift_sets[(i,a)])
                require(len(set(roots)) == 16 and all(x in D_native_set for x in roots),
                        "SLOT_BLOCK_ROOTS", f"slot {(t,i,a)} invalid")
                block_roots[(t,i,a)] = roots
                coeffs: list[FElement] = [F.one]
                for root in roots:
                    coeffs = poly_mul_linear(coeffs, root, F.zero, F.add, F.neg, F.mul)
                require(len(coeffs) == 17 and coeffs[16] == F.one,
                        "SLOT_BLOCK_LOCATOR", f"slot {(t,i,a)} not monic degree 16")
                require(all(coeffs[d] == F.zero for d in range(11,16)),
                        "SLOT_BLOCK_FIXED_JET", f"slot {(t,i,a)} is not X^16+O(X^10)")
                block_eval = poly_eval(coeffs, beta, F.zero, F.add, F.mul)
                arg = F.mul(F.mul(beta2, F.emb(pow(3, (-a) % 16, p))), eta_minus_2t)
                u = eval_prime_coeff_poly_in_F(base_polys[i], arg, F)
                if a & 1:
                    u = F.neg(u)
                require(u != F.zero, "SLOT_VALUE_NONZERO", f"slot {(t,i,a)} vanishes")
                require(block_eval == F.mul(F.emb(pow(3, t, p)), u),
                        "SLOT_PRODUCT_SCALAR", f"slot {(t,i,a)} lacks factor 3^{t}")
                rec = record_by_key.get((t,i,a))
                require(rec is not None, "SLOT_LOG_MISSING_KEY", str((t,i,a)))
                logv = int(rec["log"])
                require(0 <= logv < group_order, "SLOT_LOG_RANGE", str((t,i,a)))
                require(F.pow(log_generator, logv) == u,
                        "SLOT_LOG_FIELD_IDENTITY", f"slot {(t,i,a)} log does not reconstruct u")
                require(int(rec["color"]) == state_colors[(i,a)],
                        "SLOT_LOG_COLOR", f"slot {(t,i,a)} color mismatch")
                if mods:
                    require([logv % m for m in mods] == [int(x) for x in rec.get("res", [])],
                            "SLOT_LOG_RESIDUES", f"slot {(t,i,a)} residue mismatch")
                slot_values[(t,i,a)] = u
                block_locator_hashes.append(canonical_sha256([F.elem_json(c) for c in coeffs]))

    # Pairwise disjoint cosets for the seven moving blocks, and exclusion of 1.
    cosets = []
    for t in range(1,8):
        coset = {F.mul(F.pow(eta,t), y) for y in H0}
        require(len(coset) == 32, "SLOT_COSET", f"coset {t} has wrong size")
        cosets.append(coset)
    require(all(F.one not in c for c in cosets), "SLOT_COSET_DISJOINTNESS", "a moving coset contains 1")
    for i in range(7):
        for j in range(i+1,7):
            require(cosets[i].isdisjoint(cosets[j]), "SLOT_COSET_DISJOINTNESS", f"cosets {i+1},{j+1} intersect")

    # Exact color-shell size by a 16-state dynamic program, not a 48^7 enumeration.
    colors_one_slot = [state_colors[(i,a)] for i in (1,2,3) for a in range(16)]
    dp = [0]*16
    dp[0] = 1
    for _ in range(7):
        ndp = [0]*16
        for s, count in enumerate(dp):
            for c in colors_one_slot:
                ndp[(s+c) % 16] += count
        dp = ndp
    shell_target = int(packet["color_shell_target"])
    P0 = dp[shell_target]
    require(P0 == int(expected_cfg["packet_supports"]) == finite["packet_supports"],
            "COLOR_SHELL_SIZE", f"computed {P0}")

    # Concrete reference locator plus the local-to-global generic identities.
    ref_state_indices = [int(x) for x in packet["reference_tuple_zero_based_state_indices"]]
    require(len(ref_state_indices) == 7 and all(0 <= x < 48 for x in ref_state_indices),
            "REFERENCE_TUPLE", "reference tuple must have seven state indices")
    ref_states = [(x//16 + 1, x % 16) for x in ref_state_indices]
    ref_color = sum(state_colors[s] for s in ref_states) % 16
    require(ref_color == shell_target, "REFERENCE_TUPLE_COLOR", f"reference color is {ref_color}")
    J_ref: list[FElement] = [F.one]
    phi_ref = F.one
    for t, (i,a) in enumerate(ref_states, 1):
        J_ref.extend(block_roots[(t,i,a)])
        phi_ref = F.mul(phi_ref, slot_values[(t,i,a)])
    require(len(J_ref) == 113 and len(set(J_ref)) == 113,
            "REFERENCE_LOCATOR_ROOTS", "reference support is not a 113-set")
    P_ref: list[FElement] = [F.one]
    for root in J_ref:
        P_ref = poly_mul_linear(P_ref, root, F.zero, F.add, F.neg, F.mul)
    require(len(P_ref) == 114 and P_ref[113] == F.one and P_ref[112] == F.emb(-1),
            "REFERENCE_FIXED_JET", "leading terms are not X^113-X^112")
    require(all(P_ref[d] == F.zero for d in range(108,112)),
            "REFERENCE_FIXED_JET", "coefficient in degree 108..111 is nonzero")
    P_ref_beta = poly_eval(P_ref, beta, F.zero, F.add, F.mul)
    three28 = pow(3, 28, p)
    require(three28 == int(expected_cfg["three_power_28_prime_field_value"]),
            "THREE_POWER_28", f"3^28 mod 17 is {three28}")
    kappa = F.mul(F.sub(beta, F.one), F.emb(three28))
    require(kappa != F.zero, "PRODUCT_SCALAR_NONZERO", "kappa is zero")
    require(P_ref_beta == F.mul(kappa, phi_ref),
            "REFERENCE_PRODUCT_SCALAR", "P_ref(beta) != kappa Phi(ref)")

    native = fixed["native"]
    require(int(native["k"]) == int(native["n"]) - int(native["j"]) - int(native["sigma"]),
            "NATIVE_PARAMETER_IDENTITY", "k != n-j-sigma")
    require(int(native["agreement"]) == int(native["n"]) - int(native["j"]) == int(native["k"]) + int(native["sigma"]),
            "NATIVE_PARAMETER_IDENTITY", "agreement mismatch")
    require((int(native["delta_numerator"]), int(native["delta_denominator"])) == (113,256),
            "NATIVE_DELTA", "native delta mismatch")

    # Smooth quadratic extension and order-512 domain.
    K = QuadraticExtension(F, eta)
    theta = K.theta
    require(K.mul(theta, theta) == K.emb(eta), "THETA_RELATION", "theta^2 != eta")
    require(K.pow(theta, 256) == K.emb(minus_one), "THETA_ORDER", "theta^256 != -1")
    require(K.pow(theta, 512) == K.one, "THETA_ORDER", "theta^512 != 1")
    H = [K.pow(theta, i) for i in range(512)]
    require(len(set(H)) == 512, "SMOOTH_DOMAIN_ORDER", "<theta> has fewer than 512 points")
    D_even = [K.emb(F.pow(eta, i)) for i in range(256)]
    require(H[0::2] == D_even, "SMOOTH_DOMAIN_DECOMPOSITION", "even powers are not <eta>")
    odd_coset = H[1::2]
    require(len(set(odd_coset)) == 256 and set(D_even).isdisjoint(odd_coset),
            "SMOOTH_DOMAIN_DECOMPOSITION", "H is not D disjoint union theta D")

    # Generated-field receipt: theta lies in no proper subfield F_{17^d}, d|32.
    for d in (1,2,4,8,16):
        require(K.pow(theta, 17**d) != theta, "Q_GEN_SUBFIELD_TEST", f"theta lies in F_17^{d}")
    require(K.pow(theta, 17**32) == theta, "Q_GEN_FROBENIUS", "theta is not fixed by 17^32 Frobenius")

    lift = fixed["smooth_lift"]
    a0,a1 = [int(x) for x in lift["A_odd_coset_exponent_range_inclusive"]]
    r0,r1 = [int(x) for x in lift["R_odd_coset_exponent_range_inclusive"]]
    require((a0,a1,r0,r1) == (0,118,119,255), "LIFT_PARTITION", "unexpected A/R ranges")
    A = [K.mul(theta, K.emb(F.pow(eta,i))) for i in range(a0,a1+1)]
    R = [K.mul(theta, K.emb(F.pow(eta,i))) for i in range(r0,r1+1)]
    require(len(A) == 119 and len(R) == 137, "LIFT_PARTITION", "A/R sizes are not 119/137")
    require(set(A).isdisjoint(R) and set(A+R) == set(odd_coset),
            "LIFT_PARTITION", "A and R do not partition theta<eta>")
    betaK = K.emb(beta)
    require(betaK not in set(H), "BETA_OUTSIDE_SMOOTH_DOMAIN", "beta lies in H")

    P_R_beta = K.one
    for root in R:
        P_R_beta = K.mul(P_R_beta, K.sub(betaK, root))
    require(P_R_beta != K.zero, "FIXED_ROOT_SCALAR_NONZERO", "P_R(beta)=0")
    kappa_plus = K.mul(P_R_beta, K.emb(kappa))
    require(kappa_plus != K.zero, "LIFTED_PRODUCT_SCALAR_NONZERO", "lifted scalar is zero")

    # Augmented reference co-support and exact smooth parameters.
    J_plus = [K.emb(x) for x in J_ref] + R
    require(len(J_plus) == 250 and len(set(J_plus)) == 250,
            "LIFTED_COSUPPORT", "J_ref union R is not a 250-set")
    S_plus = [x for x in H if x not in set(J_plus)]
    require(len(S_plus) == 262, "LIFTED_SUPPORT", "smooth witness support size is not 262")
    J_ref_set = set(J_ref)
    require(set(S_plus) == ({K.emb(x) for x in D_native if x not in J_ref_set} | set(A)),
            "LIFTED_SUPPORT", "smooth support is not (D\\J) union A")
    require(137 + 107 == 244 == int(lift["j"]) - int(lift["sigma"]),
            "LIFTED_FIXED_JET_DEGREE", "deg P_R + 107 != j-sigma")
    require(int(lift["k"]) == int(lift["n"]) - int(lift["j"]) - int(lift["sigma"]) == 256,
            "LIFTED_PARAMETER_IDENTITY", "k != n-j-sigma")
    require(int(lift["agreement"]) == int(lift["n"]) - int(lift["j"]) == int(lift["k"]) + int(lift["sigma"]) == 262,
            "LIFTED_PARAMETER_IDENTITY", "agreement mismatch")
    require((int(lift["delta_numerator"]), int(lift["delta_denominator"])) == (125,256),
            "LIFTED_DELTA", "delta mismatch")
    require(512 * (256-125) == 262 * 256, "LIFTED_DELTA", "(1-delta)n != 262")

    # Construct one concrete final affine line via the fixed-jet theorem's formula.
    # Domain locator is X^512-1; derivative at x in H is 512*x^511.
    LH_beta = K.sub(K.pow(betaK, 512), K.one)
    require(LH_beta != K.zero, "LINE_CONSTRUCTION", "L_H(beta)=0")
    P_plus_beta = K.mul(P_R_beta, K.emb(P_ref_beta))
    require(P_plus_beta == K.mul(kappa_plus, K.emb(phi_ref)),
            "LIFTED_REFERENCE_PRODUCT_SCALAR", "P_plus(beta) != kappa_plus Phi(ref)")
    z0 = K.inv(P_plus_beta)
    J_plus_set = set(J_plus)
    e0: list[KElement] = []
    g_word: list[KElement] = []
    derivative_scalar = K.emb(F.emb(512 % p))
    for x in H:
        gx = K.div(LH_beta, K.sub(betaK, x))
        g_word.append(gx)
        if x in J_plus_set:
            pprime = K.one
            for y in J_plus:
                if y != x:
                    pprime = K.mul(pprime, K.sub(x, y))
            ldprime = K.mul(derivative_scalar, K.pow(x, 511))
            denom = K.mul(K.sub(betaK, x), pprime)
            e0.append(K.div(ldprime, denom))
        else:
            e0.append(K.zero)
    f_word = [K.sub(e, K.mul(z0, g)) for e, g in zip(e0, g_word)]
    require(all(K.add(f_word[i], K.mul(z0, g_word[i])) == K.zero for i,x in enumerate(H) if x not in J_plus_set),
            "LINE_REFERENCE_AGREEMENT", "reference line point does not agree with zero codeword on S_plus")
    require(all(e0[i] != K.zero for i,x in enumerate(H) if x in J_plus_set),
            "LINE_ERROR_SUPPORT", "reference error has a zero inside J_plus")
    # Noncontainment template: J_plus union {beta} has 251 distinct points and 251 <= r=256,
    # so the corresponding length-256 Vandermonde columns are independent.
    require(betaK not in J_plus_set and len(J_plus_set) + 1 == 251 <= 256,
            "LINE_NONCONTAINMENT_VANDERMONDE", "Vandermonde independence prerequisites fail")

    q_line = 17**32
    threshold = q_line // (2**128)
    N = finite["distinct_products"]
    require(q_line == K.q, "Q_LINE", "quadratic field size mismatch")
    require(threshold == int(expected_cfg["floor_17_pow_32_over_2_pow_128"]) == 6,
            "INTEGER_THRESHOLD", f"floor(q/2^128)={threshold}")
    require(N > threshold and (2**128)*N > q_line,
            "STRICT_2_POW_128_COMPARISON", "N/q_line is not strictly >2^-128")

    # This notice is deliberate: the old master JSON displays generator X+1,
    # while the executable slot-log receipt uses beta=X+2. The checker binds to
    # the executable receipt. This metadata mismatch is non-fatal but surfaced.
    master_generator = master.get("model", {}).get("generator")
    metadata_notice = {
        "master_display_generator": master_generator,
        "executable_slot_log_generator": list(field_cfg["slot_log_generator_coefficients_low_to_high"]),
        "status": "NONFATAL_METADATA_MISMATCH" if master_generator != list(field_cfg["slot_log_generator_coefficients_low_to_high"]) else "CONSISTENT"
    }

    return {
        "decision": "CYCLE116_TRANSFER_CERTIFICATE_VERIFIED",
        "label": "PROOF",
        "imports": {
            "sha256": import_hashes,
            "cycle84_values_consumed_not_recensused": True,
            "metadata_notice": metadata_notice
        },
        "field": {
            "F0": "F_17[X]/(X^16+X^8+3)",
            "irreducible": True,
            "q0": F.q,
            "eta_order": 256,
            "eta_nonsquare": True,
            "eta_power_16": 3,
            "beta_outside_D": True,
            "slot_log_generator_is_beta_and_primitive": True
        },
        "fixed_jet": {
            "slot_states_checked": 336,
            "all_slot_locators": "X^16+O(X^10)",
            "family_locator": "P_T(X)=X^113-X^112+O(X^107)",
            "product_scalar": "P_T(beta)=kappa*Phi(T)",
            "kappa_coefficients_low_to_high": F.elem_json(kappa),
            "kappa_nonzero": True,
            "reference_locator_sha256": canonical_sha256([F.elem_json(c) for c in P_ref]),
            "block_locator_multiset_sha256": canonical_sha256(sorted(block_locator_hashes))
        },
        "native_row": {
            "code": "RS[F_17^16,<eta>,137]",
            "n": 256,
            "k": 137,
            "agreement": 143,
            "delta": "113/256",
            "LD_sw_lower_bound": N,
            "epsilon_mca_lower_bound": f"{N}/17^16"
        },
        "smooth_lift": {
            "K": "F_17^32=F0(theta), theta^2=eta",
            "theta_order": 512,
            "H_order": 512,
            "H_generates_K": True,
            "A_size": 119,
            "R_size": 137,
            "code": "RS[F_17^32,H,256]",
            "n": 512,
            "k": 256,
            "agreement": 262,
            "delta": "125/256",
            "LD_sw_lower_bound": N,
            "epsilon_mca_lower_bound": f"{N}/17^32",
            "strictly_greater_than_2^-128": True,
            "fixed_root_scalar_sha256": canonical_sha256(K.elem_json(P_R_beta))
        },
        "one_affine_line_receipt": {
            "construction": "f=e_J0-z0*g, g(x)=L_H(beta)/(beta-x)",
            "reference_tuple": ref_state_indices,
            "z0_sha256": canonical_sha256(K.elem_json(z0)),
            "f_word_sha256": hash_field_word_K(f_word, K),
            "g_word_sha256": hash_field_word_K(g_word, K),
            "reference_cosupport_sha256": hash_points_K(J_plus, K),
            "reference_support_sha256": hash_points_K(S_plus, K),
            "support_size": len(S_plus),
            "noncontainment_clause": "251 distinct Vandermonde columns in dimension 256"
        },
        "field_parameter_ledger": {
            "q_gen": q_line,
            "q_code": q_line,
            "q_line": q_line,
            "q_chal": None,
            "mca_denominator": "q_line",
            "floor_q_line_over_2^128": threshold,
            "bad_slope_numerator": N,
            "strict_integer_test": f"2^128*{N} > 17^32"
        },
        "scope": {
            "ordinary_list_decoding_lower_bound": False,
            "protocol_soundness_failure": False,
            "asymptotic_theorem": False,
            "official_proximity_prize_counterpacket": False,
            "accepted_deployed_prime_field_theorem": False
        }
    }


def emit(obj: dict[str, Any]) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--anchor", required=True, type=Path)
    ap.add_argument("--fixed-jet", required=True, type=Path)
    return ap.parse_args()


def entrypoint() -> int:
    args = parse_args()
    if not args.anchor.is_file():
        emit({"decision": "MISSING_CYCLE84_ANCHOR", "path": str(args.anchor)})
        return 4
    if not args.fixed_jet.is_file():
        emit({"decision": "MISSING_FIXED_JET_CERTIFICATE", "path": str(args.fixed_jet)})
        return 3
    try:
        result = main_verify(args.anchor.resolve(), args.fixed_jet.resolve())
    except Rejected as exc:
        emit({"decision": "CERTIFICATE_REJECTED", "failure_clause": exc.clause, "detail": exc.detail})
        return 1
    except (Malformed, KeyError, TypeError, ValueError, ZeroDivisionError) as exc:
        emit({"decision": "MALFORMED_INPUT", "detail": str(exc)})
        return 2
    emit(result)
    return 0


if __name__ == "__main__":
    sys.exit(entrypoint())
