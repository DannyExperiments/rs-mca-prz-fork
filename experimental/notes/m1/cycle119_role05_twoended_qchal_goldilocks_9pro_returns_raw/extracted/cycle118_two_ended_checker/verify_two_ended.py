#!/usr/bin/env python3
"""Fail-closed verifier for the Cycle118 two-ended agreement-263 transfer.

The checker imports the hash-bound Cycle84 occupancy exactly as the Cycle116
checker did; it does not rerun the 52-billion shell census.  It then verifies
all finite field, slot, constant-term, partition, degree, evaluator, product,
line, noncontainment-prerequisite, and strict-distance clauses.

Exit codes:
  0  CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
  1  CERTIFICATE_REJECTED
  2  MALFORMED_INPUT
  3  MISSING_TWO_ENDED_CERTIFICATE
  4  MISSING_BASE_INPUT
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


def verify_sha256_manifest(manifest_path: Path) -> int:
    """Verify every GNU-style entry in a manifest, relative to its directory."""
    count = 0
    try:
        lines = manifest_path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        raise Malformed(f"cannot read manifest {manifest_path}: {exc}") from exc
    for lineno, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line:
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError as exc:
            raise Malformed(f"malformed manifest line {lineno}: {raw!r}") from exc
        rel = rel.lstrip("*").removeprefix("./")
        target = manifest_path.parent / rel
        require(target.is_file(), "BASE_MANIFEST_FILE_MISSING", rel)
        actual = sha256_file(target)
        require(actual == expected, "BASE_MANIFEST_HASH", f"{rel}: expected {expected}, got {actual}")
        count += 1
    require(count > 0, "BASE_MANIFEST_EMPTY", str(manifest_path))
    return count


def k_dot(xs: Sequence[KElement], ys: Sequence[KElement], K: QuadraticExtension) -> KElement:
    require(len(xs) == len(ys), "INTERNAL_VECTOR_LENGTH", f"{len(xs)} != {len(ys)}")
    out = K.zero
    for x, y in zip(xs, ys):
        out = K.add(out, K.mul(x, y))
    return out


def solve_square_K(matrix: Sequence[Sequence[KElement]], rhs: Sequence[KElement], K: QuadraticExtension) -> list[KElement]:
    """Deterministic Gaussian elimination over K; intended only for 7x7."""
    n = len(rhs)
    require(len(matrix) == n and all(len(row) == n for row in matrix),
            "EVALUATOR_MATRIX_SHAPE", "matrix is not square")
    aug = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col] != K.zero), None)
        require(pivot is not None, "EVALUATOR_MATRIX_SINGULAR", f"no pivot in column {col}")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        inv = K.inv(aug[col][col])
        aug[col] = [K.mul(inv, x) for x in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor == K.zero:
                continue
            aug[r] = [K.sub(aug[r][c], K.mul(factor, aug[col][c])) for c in range(n + 1)]
    return [aug[i][n] for i in range(n)]


def polynomial_from_roots_K(roots: Sequence[KElement], K: QuadraticExtension) -> list[KElement]:
    coeffs: list[KElement] = [K.one]
    for root in roots:
        coeffs = poly_mul_linear(coeffs, root, K.zero, K.add, K.neg, K.mul)
    return coeffs


def shifted_polynomial_K(coeffs: Sequence[KElement], shift: int, length: int, K: QuadraticExtension) -> list[KElement]:
    require(shift >= 0 and len(coeffs) + shift <= length,
            "POLYNOMIAL_SHIFT", f"shift {shift}, length {length}, degree {len(coeffs)-1}")
    out = [K.zero for _ in range(length)]
    for i, c in enumerate(coeffs):
        out[i + shift] = c
    return out


def synthetic_divide_root_K(coeffs: Sequence[KElement], root: KElement, K: QuadraticExtension) -> list[KElement]:
    """Return Q for monic P=(X-root)Q; coefficients are low-to-high."""
    degree = len(coeffs) - 1
    require(degree >= 1, "SYNTHETIC_DIVISION", "constant polynomial")
    q = [K.zero for _ in range(degree)]
    q[degree - 1] = coeffs[degree]
    for d in range(degree - 1, 0, -1):
        q[d - 1] = K.add(coeffs[d], K.mul(root, q[d]))
    remainder = K.add(coeffs[0], K.mul(root, q[0]))
    require(remainder == K.zero, "SYNTHETIC_DIVISION_REMAINDER", "root is not a root")
    return q


def syndrome_word_K(word: Sequence[KElement], domain: Sequence[KElement], K: QuadraticExtension) -> list[KElement]:
    """Weighted Vandermonde syndrome for H=<theta>, r=256."""
    require(len(word) == len(domain) == 512, "SYNDROME_DOMAIN_LENGTH", "expected length 512")
    derivative_scalar = K.emb(K.F.emb(512 % K.F.p))
    out = [K.zero for _ in range(256)]
    for value, x in zip(word, domain):
        if value == K.zero:
            continue
        ldprime = K.mul(derivative_scalar, K.pow(x, 511))
        weighted = K.div(value, ldprime)
        power = K.one
        for m in range(256):
            out[m] = K.add(out[m], K.mul(power, weighted))
            power = K.mul(power, x)
    return out


def right_inverse_on_even_domain(y: Sequence[KElement], domain: Sequence[KElement], K: QuadraticExtension) -> list[KElement]:
    """Explicit parity-check preimage using the 256-point even subgroup.

    For x in D0=<eta>, t_x=(1/256) sum_m y_m x^{-m}; in characteristic
    17, 256=1, but the inverse is computed rather than assumed.  The word is
    L_H'(x)t_x on D0 and zero on the odd coset.
    """
    require(len(y) == 256 and len(domain) == 512, "RIGHT_INVERSE_SHAPE", "bad dimensions")
    inv256 = K.inv(K.emb(K.F.emb(256 % K.F.p)))
    derivative_scalar = K.emb(K.F.emb(512 % K.F.p))
    out = [K.zero for _ in range(512)]
    for idx in range(0, 512, 2):
        x = domain[idx]
        xinv = K.inv(x)
        power = K.one
        total = K.zero
        for coeff in y:
            total = K.add(total, K.mul(coeff, power))
            power = K.mul(power, xinv)
        total = K.mul(inv256, total)
        ldprime = K.mul(derivative_scalar, K.pow(x, 511))
        out[idx] = K.mul(ldprime, total)
    return out


def supported_error_from_moments(
    y: Sequence[KElement],
    roots: Sequence[KElement],
    locator: Sequence[KElement],
    domain: Sequence[KElement],
    K: QuadraticExtension,
) -> list[KElement]:
    """Construct the unique J-supported error with the prescribed syndrome.

    The first |J| moments are inverted by Lagrange coefficients, then all 256
    moments are checked by the caller.  This is a 249-point replay, not a shell
    enumeration.
    """
    j = len(roots)
    require(len(locator) == j + 1 and len(y) == 256, "ERROR_CONSTRUCTION_SHAPE", "bad dimensions")
    index = {x: i for i, x in enumerate(domain)}
    require(len(index) == 512 and all(a in index for a in roots),
            "ERROR_CONSTRUCTION_ROOTS", "root outside domain")
    derivative_scalar = K.emb(K.F.emb(512 % K.F.p))
    out = [K.zero for _ in domain]
    for a in roots:
        quotient = synthetic_divide_root_K(locator, a, K)
        pprime = poly_eval(quotient, a, K.zero, K.add, K.mul)
        require(pprime != K.zero, "ERROR_CONSTRUCTION_DERIVATIVE", "repeated locator root")
        inv_pprime = K.inv(pprime)
        t = K.zero
        for m in range(j):
            t = K.add(t, K.mul(K.mul(quotient[m], inv_pprime), y[m]))
        ldprime = K.mul(derivative_scalar, K.pow(a, 511))
        out[index[a]] = K.mul(ldprime, t)
    return out


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
    require(master.get("color_filter") == "colorL + colorR == 4 mod 16",
            "MASTER_COLOR_FILTER", str(master.get("color_filter")))
    require(master.get("theorem") == "For the explicit Cycle84 seven-slot product/color model at beta=X+2, m_max(beta)=2.",
            "MASTER_THEOREM_BINDING", str(master.get("theorem")))
    model = master.get("model", {})
    require(model.get("beta") == [2, 1], "MASTER_MODEL_BETA", str(model.get("beta")))
    require(model.get("eta") == [0,0,0,0,0,0,0,0,0,6], "MASTER_MODEL_ETA", str(model.get("eta")))
    require(model.get("field_poly") == [3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            "MASTER_MODEL_FIELD", str(model.get("field_poly")))
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


def main_verify(anchor_path: Path, fixed_path: Path, two_ended_path: Path) -> dict[str, Any]:
    anchor = load_json(anchor_path)
    fixed = load_json(fixed_path)
    two_ended = load_json(two_ended_path)
    require(fixed.get("schema") == "cycle116.fixed_jet_and_smooth_lift.v1", "FIXED_JET_SCHEMA", "unexpected fixed-jet schema")
    require(two_ended.get("schema") == "cycle118.two_ended_agreement_263.v1",
            "TWO_ENDED_SCHEMA", "unexpected two-ended schema")

    binding = two_ended.get("claim_binding")
    if not isinstance(binding, dict):
        raise Malformed("claim_binding must be an object")
    role_path = (two_ended_path.parent / binding["role05_response_path"]).resolve()
    manifest_path = (two_ended_path.parent / binding["cycle116_manifest_path"]).resolve()
    require(role_path.is_file(), "ROLE05_CLAIM_MISSING", str(role_path))
    require(sha256_file(role_path) == binding["role05_response_sha256"],
            "ROLE05_CLAIM_HASH", "Role05 response hash mismatch")
    require(manifest_path.is_file(), "BASE_MANIFEST_MISSING", str(manifest_path))
    require(sha256_file(manifest_path) == binding["cycle116_manifest_sha256"],
            "BASE_MANIFEST_BINDING", "Cycle116 manifest hash mismatch")
    base_manifest_files = verify_sha256_manifest(manifest_path)

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
    slot_constant_checks = 0
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
                expected_constant = F.emb(pow(3, (t + state_colors[(i,a)]) % 16, p))
                require(coeffs[0] == expected_constant,
                        "SLOT_CONSTANT_IDENTITY",
                        f"L_{{{t},{i},{a}}}(0) != 3^(t+color)")
                slot_constant_checks += 1
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

    # Universal Cycle84 constant identity on the color shell.
    slot_index_sum = sum(int(t) for t in packet["slot_indices"])
    shell_constant_exponent = (slot_index_sum + shell_target) % 16
    require(slot_constant_checks == 336, "SLOT_CONSTANT_COUNT", str(slot_constant_checks))
    require(slot_index_sum == 28 and shell_target == 4,
            "SHELL_CONSTANT_PARAMETERS", f"sum(t)={slot_index_sum}, target={shell_target}")
    require(pow(3, slot_index_sum + shell_target, p) == 1 and shell_constant_exponent == 0,
            "SHELL_CONSTANT_IDENTITY", "Q_T(0) is not forced to 1")
    native_locator_constant = F.emb(-1)

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
    require(P_ref[0] == native_locator_constant,
            "REFERENCE_NATIVE_CONSTANT", "reference P_T(0) != -1")
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

    # Cycle118 two-ended partition and exact parameter ledger.
    partition = two_ended.get("partition")
    params = two_ended.get("parameters")
    finite_cfg = two_ended.get("finite")
    ledger_cfg = two_ended.get("field_ledger")
    if not all(isinstance(x, dict) for x in (partition, params, finite_cfg, ledger_cfg)):
        raise Malformed("two-ended partition/parameters/finite/field_ledger must be objects")
    expected_params = {
        "n": 512,
        "native_j": 113,
        "R_size": 136,
        "j": 249,
        "sigma": 7,
        "r": 256,
        "k": 256,
        "agreement": 263,
        "strict_radius_numerator": 125,
        "strict_radius_denominator": 256,
        "strict_distance_integer_cutoff": 250,
    }
    require({k: int(v) for k, v in params.items()} == expected_params,
            "TWO_ENDED_PARAMETER_CERTIFICATE", f"unexpected parameters: {params}")
    require({k: int(v) for k, v in finite_cfg.items()} == {
                "packet_supports": 52_747_567_104,
                "distinct_products": 52_747_567_092,
            }, "TWO_ENDED_FINITE_CERTIFICATE", f"unexpected finite values: {finite_cfg}")
    require(ledger_cfg == {
                "q_gen": "17^32", "q_code": "17^32", "q_line": "17^32", "q_chal": None,
            }, "TWO_ENDED_FIELD_LEDGER", f"unexpected ledger: {ledger_cfg}")
    require(two_ended.get("terminal") == "CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED",
            "TWO_ENDED_TERMINAL", str(two_ended.get("terminal")))

    a0, a1 = [int(x) for x in partition["A_odd_coset_exponent_range_inclusive"]]
    r0, r1 = [int(x) for x in partition["R_odd_coset_exponent_range_inclusive"]]
    require((a0, a1, r0, r1) == (0, 119, 120, 255),
            "TWO_ENDED_PARTITION_RANGES", f"got {(a0,a1,r0,r1)}")
    A_star = [K.mul(theta, K.emb(F.pow(eta, i))) for i in range(a0, a1 + 1)]
    R_star = [K.mul(theta, K.emb(F.pow(eta, i))) for i in range(r0, r1 + 1)]
    require(len(A_star) == 120 and len(R_star) == 136,
            "TWO_ENDED_PARTITION_SIZES", f"A={len(A_star)}, R={len(R_star)}")
    require(set(A_star).isdisjoint(R_star) and set(A_star + R_star) == set(odd_coset),
            "TWO_ENDED_PARTITION", "A* and R* do not partition theta<eta>")

    betaK = K.emb(beta)
    require(betaK not in set(H), "BETA_OUTSIDE_SMOOTH_DOMAIN", "beta lies in H")

    # Fixed padding polynomial and its two endpoint values.
    P_R = polynomial_from_roots_K(R_star, K)
    require(len(P_R) == 137 and P_R[136] == K.one,
            "P_R_DEGREE", "P_R* is not monic degree 136")
    P_R_zero = P_R[0]
    P_R_beta = poly_eval(P_R, betaK, K.zero, K.add, K.mul)
    require(P_R_zero != K.zero, "P_R_ZERO_NONZERO", "P_R*(0)=0")
    require(P_R_beta != K.zero, "P_R_BETA_NONZERO", "P_R*(beta)=0")

    # Augmented reference co-support and exact agreement support.
    J_plus = [K.emb(x) for x in J_ref] + R_star
    require(len(J_plus) == 249 and len(set(J_plus)) == 249,
            "TWO_ENDED_COSUPPORT", "J_ref union R* is not a 249-set")
    J_plus_set = set(J_plus)
    S_plus = [x for x in H if x not in J_plus_set]
    require(len(S_plus) == 263, "TWO_ENDED_SUPPORT", "agreement support size is not 263")
    J_ref_set = set(J_ref)
    require(set(S_plus) == ({K.emb(x) for x in D_native if x not in J_ref_set} | set(A_star)),
            "TWO_ENDED_SUPPORT", "support is not (D0\\J_T) union A*")

    P_plus = polynomial_from_roots_K(J_plus, K)
    require(len(P_plus) == 250 and P_plus[249] == K.one,
            "P_PLUS_DEGREE", "P_T* is not monic degree 249")
    common_constant = K.mul(P_R_zero, K.emb(native_locator_constant))
    require(P_plus[0] == common_constant and common_constant != K.zero,
            "TWO_ENDED_COMMON_CONSTANT", "P_T*(0) is not the certified common nonzero constant")

    # Universal degree and parameter arithmetic.  The native local checks prove
    # deg(P_T-P_T')<=107; fixed multiplication adds exactly at most 136.
    j = expected_params["j"]
    sigma = expected_params["sigma"]
    r_dim = expected_params["r"]
    require(136 + 107 == 243 == j - sigma + 1,
            "TWO_ENDED_COMMON_TOP_SIX", "degree bound is not 243=j-sigma+1")
    require(expected_params["native_j"] + expected_params["R_size"] == j,
            "TWO_ENDED_PARAMETER_IDENTITY", "113+136 != 249")
    require(j + sigma == r_dim == 256,
            "TWO_ENDED_PARAMETER_IDENTITY", "j+sigma != r")
    require(expected_params["k"] == expected_params["n"] - r_dim == 256,
            "TWO_ENDED_PARAMETER_IDENTITY", "k != n-r")
    require(expected_params["agreement"] == expected_params["n"] - j == 263,
            "TWO_ENDED_PARAMETER_IDENTITY", "agreement != n-j")

    # Product scalar and preservation of the exact Cycle84 occupancy.
    P_plus_beta = poly_eval(P_plus, betaK, K.zero, K.add, K.mul)
    fixed_scalar = K.mul(P_R_beta, K.emb(kappa))
    require(fixed_scalar != K.zero, "TWO_ENDED_FIXED_SCALAR_NONZERO", "fixed scalar is zero")
    require(P_plus_beta == K.mul(P_R_beta, K.emb(P_ref_beta)),
            "TWO_ENDED_PRODUCT_FACTOR", "P_T*(beta) != P_R*(beta)P_T(beta)")
    require(P_plus_beta == K.mul(fixed_scalar, K.emb(phi_ref)),
            "TWO_ENDED_REFERENCE_PRODUCT_SCALAR", "P_T*(beta) != fixed_scalar*Phi(T)")
    N = finite["distinct_products"]
    require(N == int(finite_cfg["distinct_products"]) == 52_747_567_092,
            "TWO_ENDED_DISTINCT_EVALUATIONS", f"N={N}")

    # Explicit seven-coordinate evaluator.  For Q=P_T*A, |A|<7, the selected
    # coordinates are degree 0 and degrees 250..255.  The high rows use only
    # P_T* coefficients 249..244, and the low row uses only P_T*(0).
    selected_degrees = [0] + list(range(j + 1, j + sigma))
    require(selected_degrees == [0, 250, 251, 252, 253, 254, 255],
            "EVALUATOR_SELECTED_DEGREES", str(selected_degrees))
    evaluator_matrix: list[list[KElement]] = []
    dependency_indices: list[list[int]] = []
    for degree in selected_degrees:
        row: list[KElement] = []
        deps: list[int] = []
        for m in range(sigma):
            idx = degree - m
            if 0 <= idx <= j:
                row.append(P_plus[idx])
                deps.append(idx)
            else:
                row.append(K.zero)
        evaluator_matrix.append(row)
        dependency_indices.append(deps)
    require(dependency_indices[0] == [0],
            "EVALUATOR_LOW_ENDPOINT_DEPENDENCY", str(dependency_indices[0]))
    require(all(set(deps).issubset(set(range(244, 250))) for deps in dependency_indices[1:]),
            "EVALUATOR_HIGH_ENDPOINT_DEPENDENCY", str(dependency_indices[1:]))
    require(evaluator_matrix[0][0] == common_constant and
            all(evaluator_matrix[0][m] == K.zero for m in range(1, sigma)),
            "EVALUATOR_LOW_ENDPOINT_ROW", "constant row is not c*a0")
    for sidx in range(1, sigma):
        require(evaluator_matrix[sidx][sidx] == K.one,
                "EVALUATOR_TRIANGULAR_DIAGONAL", f"row {sidx}")
        require(all(evaluator_matrix[sidx][m] == K.zero for m in range(sidx)),
                "EVALUATOR_TRIANGULAR_SHAPE", f"row {sidx}")

    beta_powers = [K.one]
    for _ in range(1, sigma):
        beta_powers.append(K.mul(beta_powers[-1], betaK))
    transpose = [[evaluator_matrix[row][col] for row in range(sigma)] for col in range(sigma)]
    evaluator_weights = solve_square_K(transpose, beta_powers, K)
    for col in range(sigma):
        lhs = K.zero
        for row in range(sigma):
            lhs = K.add(lhs, K.mul(evaluator_matrix[row][col], evaluator_weights[row]))
        require(lhs == beta_powers[col], "EVALUATOR_LINEAR_SYSTEM", f"column {col}")

    y0 = [K.zero for _ in range(r_dim)]
    for degree, weight in zip(selected_degrees, evaluator_weights):
        y0[degree] = weight
    y1 = [K.one]
    for _ in range(1, r_dim):
        y1.append(K.mul(y1[-1], betaK))

    evaluator_basis_checks = 0
    annihilator_basis_checks = 0
    z_ref = K.neg(K.inv(P_plus_beta))
    y_ref = [K.add(a, K.mul(z_ref, b)) for a, b in zip(y0, y1)]
    for m in range(sigma):
        q = shifted_polynomial_K(P_plus, m, r_dim, K)
        require(k_dot(q, y0, K) == beta_powers[m],
                "EVALUATOR_BASIS", f"ell(P_T* X^{m}) != beta^{m}")
        require(k_dot(q, y1, K) == K.mul(P_plus_beta, beta_powers[m]),
                "EVALUATION_VECTOR_BASIS", f"<P_T*X^{m},y1> mismatch")
        evaluator_basis_checks += 1
        require(k_dot(q, y_ref, K) == K.zero,
                "REFERENCE_ANNIHILATOR_BASIS", f"basis {m} not annihilated")
        annihilator_basis_checks += 1

    # Deterministic common-line construction in syndrome coordinates.  The
    # even subgroup D0 has exactly r=256 distinct points, so its weighted
    # Vandermonde block is invertible.  Hence the displayed inverse-DFT formula
    # deterministically defines words f and g with Hf=y0 and Hg=y1; no shell
    # enumeration is involved.
    require(len(D_even) == r_dim and len(set(D_even)) == r_dim,
            "COMMON_LINE_RIGHT_INVERSE_DOMAIN", "D0 is not a 256-point right-inverse block")
    require(256 % p == 1 and 512 % p == 2,
            "COMMON_LINE_DERIVATIVE_SCALARS", "unexpected characteristic scalars")
    require(all((m - sidx) % 256 != 0 for m in range(256) for sidx in range(256) if m != sidx),
            "COMMON_LINE_DFT_ORTHOGONALITY", "distinct exponents collide modulo 256")
    dft_root_sums = [F.zero for _ in range(256)]
    for x in D_native:
        power = F.one
        for d in range(256):
            dft_root_sums[d] = F.add(dft_root_sums[d], power)
            power = F.mul(power, x)
    require(dft_root_sums[0] == F.emb(256) and all(v == F.zero for v in dft_root_sums[1:]),
            "COMMON_LINE_DFT_ROOT_SUMS", "order-256 root sums failed")
    require(any(x != K.zero for x in y1),
            "COMMON_LINE_DIRECTION_NONZERO_SYNDROME", "y1 is zero")

    # For the reference tuple, the seven annihilator checks above prove
    # y_ref in W_J because W_J^perp=P_J* K[X]_{<7}.  The 249 columns at J are
    # independent, so there is a unique J-supported error e_ref with syndrome
    # y_ref, and c_ref=f+z_ref*g-e_ref lies in ker H.
    require(len(J_plus_set) == 249 and 249 <= r_dim,
            "REFERENCE_ERROR_EXISTENCE", "J columns are not an independent 249-set")
    reference_distance_upper_bound = len(J_plus_set)
    require(reference_distance_upper_bound == 249,
            "REFERENCE_DISTANCE", str(reference_distance_upper_bound))

    # Universal support-wise noncontainment prerequisite: for every 249-set J,
    # the 249 weighted Vandermonde columns at J together with v(beta) are
    # independent because beta is outside H and 250<=r=256.
    require(betaK not in J_plus_set and len(J_plus_set) + 1 == 250 <= r_dim,
            "TWO_ENDED_NONCONTAINMENT_VANDERMONDE",
            "250 distinct Vandermonde columns in dimension 256 not certified")
    # Strict radius and security arithmetic.
    require(249 < expected_params["strict_distance_integer_cutoff"] == 250,
            "STRICT_DISTANCE", "249 is not strictly below 250")
    require(expected_params["strict_radius_numerator"] * expected_params["n"] ==
            expected_params["strict_distance_integer_cutoff"] * expected_params["strict_radius_denominator"],
            "STRICT_RADIUS_ARITHMETIC", "(125/256)*512 != 250")
    q_line = 17**32
    threshold = q_line // (2**128)
    require(q_line == K.q, "Q_LINE", "quadratic field size mismatch")
    require(threshold == int(expected_cfg["floor_17_pow_32_over_2_pow_128"]) == 6,
            "INTEGER_THRESHOLD", f"floor(q/2^128)={threshold}")
    require(N > threshold and (2**128) * N > q_line,
            "STRICT_2_POW_128_COMPARISON", "N/q_line is not strictly >2^-128")

    # The old master JSON displays generator X+1, while the executable slot-log
    # receipt uses beta=X+2.  All algebra is bound to the executable receipt.
    master_generator = master.get("model", {}).get("generator")
    metadata_notice = {
        "master_display_generator": master_generator,
        "executable_slot_log_generator": list(field_cfg["slot_log_generator_coefficients_low_to_high"]),
        "status": "NONFATAL_METADATA_MISMATCH" if master_generator != list(field_cfg["slot_log_generator_coefficients_low_to_high"]) else "CONSISTENT",
    }

    return {
        "decision": "CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED",
        "label": "PROOF",
        "scope": {
            "theorem": "finite attached-packet/source-scoped support-wise LD_sw",
            "ordinary_list_decoding_lower_bound": False,
            "protocol_soundness_failure": False,
            "asymptotic_theorem": False,
            "official_proximity_prize_counterpacket": False,
        },
        "imports": {
            "base_manifest_files_verified": base_manifest_files,
            "cycle84_sha256": import_hashes,
            "cycle84_values_consumed_not_recensused": True,
            "role05_response_sha256": binding["role05_response_sha256"],
            "metadata_notice": metadata_notice,
        },
        "finite_checks": {
            "cycle84_packet_supports": finite["packet_supports"],
            "cycle84_distinct_occupancy": N,
            "slot_states_checked": 336,
            "slot_constant_identities_checked": slot_constant_checks,
            "block_product_scalar_identities_checked": 336,
            "A_star_size": len(A_star),
            "R_star_size": len(R_star),
            "P_R_zero_nonzero": True,
            "P_R_beta_nonzero": True,
            "reference_evaluator_basis_checks": evaluator_basis_checks,
            "reference_annihilator_basis_checks": annihilator_basis_checks,
            "reference_distance_upper_bound": reference_distance_upper_bound,
            "dft_root_sum_checks": 256,
        },
        "symbolic_lemmas": {
            "cycle84_shell_constant": "L_{t,i,a}(0)=3^(t+color); sum(t)+shell_color=28+4=32, so P_T(0)=-1",
            "native_common_jet": "P_T=X^113-X^112+degree<=107",
            "padded_common_top_six": "deg(P_R*(P_T-P_T'))<=136+107=243=249-7+1",
            "two_ended_evaluator": "coordinates [X^0] and [X^250]..[X^255] recover a_0..a_6; determinant=P_T*(0)!=0",
            "product_scalar": "P_T*(beta)=P_R*(beta)*4*(beta-1)*Phi(T)",
            "distinct_evaluations": N,
            "parity_check_kernel": "ker H=RS[K,H,256]",
            "noncontainment": "J union {beta} gives 250 distinct Vandermonde columns in dimension 256",
        },
        "two_ended_data": {
            "selected_degrees": selected_degrees,
            "evaluator_matrix_sha256": canonical_sha256([[K.elem_json(x) for x in row] for row in evaluator_matrix]),
            "evaluator_weights_sha256": canonical_sha256([K.elem_json(x) for x in evaluator_weights]),
            "evaluator_determinant": "P_T*(0)",
            "common_constant_sha256": canonical_sha256(K.elem_json(common_constant)),
            "P_R_polynomial_sha256": canonical_sha256([K.elem_json(x) for x in P_R]),
            "P_R_zero_sha256": canonical_sha256(K.elem_json(P_R_zero)),
            "P_R_beta_sha256": canonical_sha256(K.elem_json(P_R_beta)),
            "fixed_scalar_sha256": canonical_sha256(K.elem_json(fixed_scalar)),
            "reference_P_T_star_sha256": canonical_sha256([K.elem_json(x) for x in P_plus]),
        },
        "one_common_affine_line_receipt": {
            "construction": "choose the unique D0-supported f,g with Hf=y0 and Hg=(1,beta,...,beta^255); z_T=-1/P_T*(beta)",
            "deterministic_right_inverse": "for x in D0, w_y(x)=L_H'(x)*(1/256)*sum_{m=0}^{255} y_m*x^{-m}; zero on theta*D0",
            "all_explaining_errors": "for every shell tuple T, e_T is the unique J_T*-supported word with He_T=y0+z_T*y1; c_T=f+z_T*g-e_T",
            "reference_tuple": ref_state_indices,
            "z_ref_sha256": canonical_sha256(K.elem_json(z_ref)),
            "y0_sha256": canonical_sha256([K.elem_json(x) for x in y0]),
            "y1_sha256": canonical_sha256([K.elem_json(x) for x in y1]),
            "reference_target_syndrome_sha256": canonical_sha256([K.elem_json(x) for x in y_ref]),
            "reference_cosupport_sha256": hash_points_K(J_plus, K),
            "reference_agreement_support_sha256": hash_points_K(S_plus, K),
            "agreement_support_size": len(S_plus),
            "distance_upper_bound": 249,
        },
        "row": {
            "code": "RS[F_17^32,H,256]",
            "n": 512,
            "k": 256,
            "j": 249,
            "sigma": 7,
            "agreement": 263,
            "LD_sw_lower_bound": N,
            "exact_source_radius": "249/512",
            "strict_external_radius": "distance < (125/256)*512 = 250",
            "epsilon_mca_lower_bound": f"{N}/17^32",
            "strictly_greater_than_2^-128": True,
        },
        "field_parameter_ledger": {
            "q_gen": q_line,
            "q_code": q_line,
            "q_line": q_line,
            "q_chal": None,
            "challenge_space": None,
            "challenge_distribution": None,
            "challenge_to_line_parameter_map": None,
            "mca_denominator": "q_line",
            "bad_slope_numerator": N,
            "floor_q_line_over_2^128": threshold,
            "strict_integer_test": f"2^128*{N} > 17^32",
        },
    }



def emit(obj: dict[str, Any]) -> None:
    print(json.dumps(obj, indent=2, sort_keys=True))


def parse_args() -> argparse.Namespace:
    root = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser()
    ap.add_argument("--anchor", type=Path,
                    default=root / "base_cycle116" / "inputs" / "cycle84_anchor.json")
    ap.add_argument("--fixed-jet", type=Path,
                    default=root / "base_cycle116" / "inputs" / "fixed_jet_certificate.json")
    ap.add_argument("--two-ended", type=Path,
                    default=root / "inputs" / "two_ended_certificate.json")
    return ap.parse_args()


def entrypoint() -> int:
    args = parse_args()
    if not args.anchor.is_file() or not args.fixed_jet.is_file():
        emit({"decision": "MISSING_BASE_INPUT", "anchor": str(args.anchor), "fixed_jet": str(args.fixed_jet)})
        return 4
    if not args.two_ended.is_file():
        emit({"decision": "MISSING_TWO_ENDED_CERTIFICATE", "path": str(args.two_ended)})
        return 3
    try:
        result = main_verify(args.anchor.resolve(), args.fixed_jet.resolve(), args.two_ended.resolve())
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
