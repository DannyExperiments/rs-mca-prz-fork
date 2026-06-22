#!/usr/bin/env python3
"""Cycle109 proof-carrying finite stress checker.

This reference kernel implements:
  * finite-field arithmetic for GF(p^e) from an irreducible modulus;
  * exact official RS-MCA bad-slope enumeration at support size s=k+sigma;
  * same-slope support deduplication;
  * field-ledger checks (q_gen, q_code, q_line, q_chal discipline);
  * tagged chart coverage, same-field/injective normalization checks;
  * exact finite-field rank-escape checks for one-dimensional Gate-B charts;
  * the Cycle109 terminal-label state machine.

It intentionally does NOT manufacture source branch proofs. Non-builtin branch,
AP_corr, denominator-minimality, uniform chart-count, and family-promotion facts
must arrive as receipts from a separately trusted proof kernel. In strict mode,
unverified receipts prevent STRATIFIED_COVER_CERTIFIED and
SOURCE_VALID_COUNTERPACKET.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple


REQUIRED_TERMINALS = {
    "STRATIFIED_COVER_CERTIFIED",
    "UNPAID_LOW_RESIDUAL",
    "UNPAID_BALANCED_COVER",
    "UNPAID_HIGH_PLANE",
    "AP_DESCENT_FAILURE",
    "FIELD_LEDGER_MISMATCH",
    "SOURCE_VALID_COUNTERPACKET",
    "MODEL_ONLY_STRESS_FAMILY",
}

PAID_BRANCHES = {
    "ENDPOINT",
    "QUOTIENT_PERIODIC",
    "CONTAINED_DELETE_ONE",
    "TANGENT",
    "FIELD_CONFINEMENT",
    "AFFINE_COLOR",
    "HIDDEN_ACTION_RANK",
    "INTERNAL_NORMALIZATION",
}
RESIDUAL_BRANCHES = {"LOW", "BALANCED", "HIGH"}
PRIMARY_BRANCHES = PAID_BRANCHES | RESIDUAL_BRANCHES


class CheckError(Exception):
    pass


def sha256_json(value: Any) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _is_probable_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for n < 2^64; strong probable-prime beyond that.
    bases = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
    for a in bases:
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


def _prime_divisors(n: int) -> List[int]:
    out: List[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def _trim_poly(a: List[int]) -> List[int]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def _poly_add(a: Sequence[int], b: Sequence[int], p: int) -> List[int]:
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        c[i] = ((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) % p
    return _trim_poly(c)


def _poly_sub(a: Sequence[int], b: Sequence[int], p: int) -> List[int]:
    n = max(len(a), len(b))
    c = [0] * n
    for i in range(n):
        c[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % p
    return _trim_poly(c)


def _poly_mul(a: Sequence[int], b: Sequence[int], p: int) -> List[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % p
    return _trim_poly(c)


def _poly_divmod(a: Sequence[int], b: Sequence[int], p: int) -> Tuple[List[int], List[int]]:
    aa = _trim_poly(list(a))
    bb = _trim_poly(list(b))
    if bb == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    if len(aa) < len(bb):
        return [0], aa
    q = [0] * (len(aa) - len(bb) + 1)
    inv = pow(bb[-1], p - 2, p)
    while aa != [0] and len(aa) >= len(bb):
        shift = len(aa) - len(bb)
        coeff = aa[-1] * inv % p
        q[shift] = coeff
        for j in range(len(bb)):
            aa[shift + j] = (aa[shift + j] - coeff * bb[j]) % p
        _trim_poly(aa)
    return _trim_poly(q), _trim_poly(aa)


def _poly_mod(a: Sequence[int], modulus: Sequence[int], p: int) -> List[int]:
    return _poly_divmod(a, modulus, p)[1]


def _poly_gcd(a: Sequence[int], b: Sequence[int], p: int) -> List[int]:
    aa, bb = _trim_poly(list(a)), _trim_poly(list(b))
    while bb != [0]:
        aa, bb = bb, _poly_mod(aa, bb, p)
    if aa == [0]:
        return [0]
    inv = pow(aa[-1], p - 2, p)
    return [(x * inv) % p for x in aa]


def _poly_pow_mod(base: Sequence[int], exponent: int, modulus: Sequence[int], p: int) -> List[int]:
    result = [1]
    b = _poly_mod(base, modulus, p)
    e = exponent
    while e:
        if e & 1:
            result = _poly_mod(_poly_mul(result, b, p), modulus, p)
        b = _poly_mod(_poly_mul(b, b, p), modulus, p)
        e >>= 1
    return result


def _is_irreducible(modulus: Sequence[int], p: int) -> bool:
    f = _trim_poly([x % p for x in modulus])
    e = len(f) - 1
    if e <= 0 or f[-1] != 1:
        return False
    if e == 1:
        return True
    x = [0, 1]
    # Rabin irreducibility criterion.
    xp = x
    frob: Dict[int, List[int]] = {0: x}
    for i in range(1, e + 1):
        xp = _poly_pow_mod(xp, p, f, p)
        frob[i] = xp
    if _poly_sub(frob[e], x, p) != [0]:
        return False
    for ell in _prime_divisors(e):
        h = _poly_sub(frob[e // ell], x, p)
        if len(_poly_gcd(f, h, p)) > 1:
            return False
    return True


@dataclass(frozen=True)
class FiniteField:
    p: int
    modulus: Tuple[int, ...]  # low-to-high, monic

    @property
    def degree(self) -> int:
        return len(self.modulus) - 1

    @property
    def order(self) -> int:
        return self.p ** self.degree

    @staticmethod
    def from_spec(spec: Mapping[str, Any], verify_irreducible: bool = True) -> "FiniteField":
        p = int(spec["p"])
        if p >= (1 << 64):
            raise CheckError("reference kernel requires p < 2^64; larger characteristics need an external primality-proof wrapper")
        if not _is_probable_prime(p):
            raise CheckError(f"field characteristic is not prime: {p}")
        modulus = tuple(int(x) % p for x in spec.get("line_modulus", [0, 1]))
        if len(modulus) < 2 or modulus[-1] != 1:
            raise CheckError("line_modulus must be monic, low-to-high")
        if verify_irreducible and not _is_irreducible(modulus, p):
            raise CheckError("line_modulus is not irreducible")
        return FiniteField(p, modulus)

    def coeffs(self, a: int) -> List[int]:
        if a < 0 or a >= self.order:
            raise CheckError(f"field element {a} outside canonical range [0,{self.order})")
        out = []
        x = a
        for _ in range(self.degree):
            out.append(x % self.p)
            x //= self.p
        return out

    def encode(self, coeffs: Sequence[int]) -> int:
        if len(coeffs) > self.degree:
            raise CheckError("too many coefficients for field element")
        acc, place = 0, 1
        for c in coeffs:
            acc += (c % self.p) * place
            place *= self.p
        return acc

    def add(self, a: int, b: int) -> int:
        ac, bc = self.coeffs(a), self.coeffs(b)
        return self.encode([(x + y) % self.p for x, y in zip(ac, bc)])

    def neg(self, a: int) -> int:
        return self.encode([(-x) % self.p for x in self.coeffs(a)])

    def sub(self, a: int, b: int) -> int:
        return self.add(a, self.neg(b))

    def mul(self, a: int, b: int) -> int:
        ac, bc = self.coeffs(a), self.coeffs(b)
        conv = [0] * (2 * self.degree - 1)
        for i, x in enumerate(ac):
            for j, y in enumerate(bc):
                conv[i + j] = (conv[i + j] + x * y) % self.p
        f = list(self.modulus)
        for d in range(len(conv) - 1, self.degree - 1, -1):
            coeff = conv[d] % self.p
            if coeff:
                shift = d - self.degree
                for j in range(self.degree):
                    conv[shift + j] = (conv[shift + j] - coeff * f[j]) % self.p
        return self.encode(conv[: self.degree])

    def pow(self, a: int, e: int) -> int:
        if e < 0:
            return self.pow(self.inv(a), -e)
        result, b = 1, a
        while e:
            if e & 1:
                result = self.mul(result, b)
            b = self.mul(b, b)
            e >>= 1
        return result

    def inv(self, a: int) -> int:
        if a == 0:
            raise ZeroDivisionError("zero has no inverse")
        return self.pow(a, self.order - 2)

    def div(self, a: int, b: int) -> int:
        return self.mul(a, self.inv(b))

    def eq0(self, a: int) -> bool:
        return a == 0

    def in_subfield_degree(self, a: int, d: int) -> bool:
        if self.degree % d != 0:
            return False
        return self.pow(a, self.p ** d) == a

    def minimal_subfield_degree(self, elements: Sequence[int]) -> int:
        for d in sorted(x for x in range(1, self.degree + 1) if self.degree % x == 0):
            if all(self.in_subfield_degree(a, d) for a in elements):
                return d
        return self.degree


def matrix_rank(matrix: Sequence[Sequence[int]], F: FiniteField) -> int:
    if not matrix:
        return 0
    A = [list(row) for row in matrix]
    nrows, ncols = len(A), len(A[0])
    if any(len(row) != ncols for row in A):
        raise CheckError("ragged matrix")
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = F.inv(A[r][c])
        A[r] = [F.mul(x, inv) for x in A[r]]
        for i in range(nrows):
            if i == r or A[i][c] == 0:
                continue
            factor = A[i][c]
            A[i] = [F.sub(A[i][j], F.mul(factor, A[r][j])) for j in range(ncols)]
        r += 1
        if r == nrows:
            break
    return r


def nullspace(matrix: Sequence[Sequence[int]], F: FiniteField) -> List[List[int]]:
    """Right nullspace basis of matrix."""
    if not matrix:
        return []
    A = [list(row) for row in matrix]
    nrows, ncols = len(A), len(A[0])
    pivots: List[int] = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        inv = F.inv(A[r][c])
        A[r] = [F.mul(x, inv) for x in A[r]]
        for i in range(nrows):
            if i == r or A[i][c] == 0:
                continue
            factor = A[i][c]
            A[i] = [F.sub(A[i][j], F.mul(factor, A[r][j])) for j in range(ncols)]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis: List[List[int]] = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivots):
            v[pc] = F.neg(A[i][fc])
        basis.append(v)
    return basis


def dot(a: Sequence[int], b: Sequence[int], F: FiniteField) -> int:
    if len(a) != len(b):
        raise CheckError("dot-product length mismatch")
    out = 0
    for x, y in zip(a, b):
        out = F.add(out, F.mul(x, y))
    return out


def vandermonde(xs: Sequence[int], k: int, F: FiniteField) -> List[List[int]]:
    V: List[List[int]] = []
    for x in xs:
        row = []
        power = 1
        for _ in range(k):
            row.append(power)
            power = F.mul(power, x)
        V.append(row)
    return V


def official_bad_slopes(instance: Mapping[str, Any], F: FiniteField) -> Dict[str, Any]:
    D = [int(x) for x in instance["D"]]
    f = [int(x) for x in instance["f"]]
    g = [int(x) for x in instance["g"]]
    k = int(instance["k"])
    sigma = int(instance["sigma"])
    n = len(D)
    s = k + sigma
    if not (0 <= k < s <= n):
        raise CheckError(f"need 0 <= k < k+sigma <= n; got n={n}, k={k}, sigma={sigma}")
    if len(f) != n or len(g) != n:
        raise CheckError("D, f, and g must have equal length")
    if len(set(D)) != n:
        raise CheckError("evaluation domain has duplicates")
    for x in D + f + g:
        F.coeffs(x)  # range check

    supports_by_slope: Dict[int, List[List[int]]] = {}
    support_rows: List[Dict[str, Any]] = []
    for idx_tuple in itertools.combinations(range(n), s):
        xs = [D[i] for i in idx_tuple]
        V = vandermonde(xs, k, F)
        # left nullspace of V = right nullspace of V^T
        VT = [[V[i][j] for i in range(s)] for j in range(k)]
        H = [[1 if i == j else 0 for j in range(s)] for i in range(s)] if k == 0 else nullspace(VT, F)
        fs = [f[i] for i in idx_tuple]
        gs = [g[i] for i in idx_tuple]
        a = [dot(h, fs, F) for h in H]
        b = [dot(h, gs, F) for h in H]
        nz = next((j for j, value in enumerate(b) if value != 0), None)
        if nz is None:
            # If a=0 too, both are explained: condition (ii) fails. If a!=0,
            # no z can solve a+zb=0.
            continue
        z = F.neg(F.div(a[nz], b[nz]))
        if all(F.add(a[j], F.mul(z, b[j])) == 0 for j in range(len(H))):
            support = list(idx_tuple)
            supports_by_slope.setdefault(z, []).append(support)
            support_rows.append({"slope": z, "support": support})

    slopes = sorted(supports_by_slope)
    collisions = sum(max(0, len(v) - 1) for v in supports_by_slope.values())
    return {
        "n": n,
        "k": k,
        "sigma": sigma,
        "s": s,
        "q_line": F.order,
        "distinct_bad_slopes": slopes,
        "N_off_exact": len(slopes),
        "supports_by_slope": {str(z): v for z, v in sorted(supports_by_slope.items())},
        "support_witness_count": len(support_rows),
        "same_slope_support_collision_count": collisions,
        "truth_hash": sha256_json({"slopes": slopes, "supports": support_rows}),
    }


def _receipt_verified(receipt: Optional[Mapping[str, Any]], strict: bool) -> bool:
    if not receipt:
        return False
    if receipt.get("verifier") == "builtin":
        return bool(receipt.get("verified", False))
    if strict:
        # Strict mode will not trust a boolean assertion from an external proof
        # system. A production wrapper must actually invoke the named kernel.
        return False
    return bool(receipt.get("verified", False))


def _parse_slope_key(x: Any) -> int:
    if isinstance(x, int):
        return x
    return int(str(x), 10)


def _chart_rank_escape(chart: Mapping[str, Any], F: FiniteField) -> Tuple[bool, Dict[str, Any]]:
    gate = chart.get("gate_b", {})
    if not gate:
        return False, {"reason": "missing gate_b"}
    A = gate.get("evaluation_matrix")
    R = gate.get("restriction_matrix")
    if A is None or R is None:
        return False, {"reason": "missing evaluation/restriction matrix"}
    A2 = [[int(x) for x in row] for row in A]
    R2 = [[int(x) for x in row] for row in R]
    if A2 and R2 and len(A2[0]) != len(R2[0]):
        return False, {"reason": "matrix column mismatch"}
    rank_A = matrix_rank(A2, F)
    rank_stacked = matrix_rank(A2 + R2, F)
    claimed_A = gate.get("rank_A")
    claimed_stacked = gate.get("rank_stacked")
    if claimed_A is not None and int(claimed_A) != rank_A:
        return False, {"reason": "rank_A mismatch", "computed": rank_A}
    if claimed_stacked is not None and int(claimed_stacked) != rank_stacked:
        return False, {"reason": "rank_stacked mismatch", "computed": rank_stacked}
    return rank_stacked > rank_A, {"rank_A": rank_A, "rank_stacked": rank_stacked}


def _field_ledger_check(cert: Mapping[str, Any], F: FiniteField, truth: Optional[Mapping[str, Any]]) -> Tuple[bool, List[str], Dict[str, Any]]:
    ledger = cert.get("field_ledger", {})
    errors: List[str] = []
    q_line = int(ledger.get("q_line", F.order))
    if q_line != F.order:
        errors.append(f"q_line={q_line} but line field order is {F.order}")
    if ledger.get("security_denominator", "q_line") != "q_line":
        errors.append("security denominator must be q_line")
    target_bits = int(ledger.get("target_bits", 128))
    if target_bits != 128:
        errors.append("Cycle109 target_bits must be 128")

    code_degree = int(ledger.get("code_degree", F.degree))
    if F.degree % code_degree != 0:
        errors.append("code_degree must divide line-field degree")
    claimed_q_code = int(ledger.get("q_code", F.p ** code_degree))
    if claimed_q_code != F.p ** code_degree:
        errors.append("q_code does not match p^code_degree")

    D: List[int] = []
    f: List[int] = []
    g: List[int] = []
    if "instance" in cert:
        inst = cert["instance"]
        D = [int(x) for x in inst.get("D", [])]
        f = [int(x) for x in inst.get("f", [])]
        g = [int(x) for x in inst.get("g", [])]
        if any(not F.in_subfield_degree(x, code_degree) for x in D):
            errors.append("domain is not contained in K_code")
    gen_degree = F.minimal_subfield_degree(D) if D else int(ledger.get("gen_degree", code_degree))
    claimed_gen_degree = int(ledger.get("gen_degree", gen_degree))
    claimed_q_gen = int(ledger.get("q_gen", F.p ** claimed_gen_degree))
    if claimed_gen_degree != gen_degree:
        errors.append(f"claimed gen_degree={claimed_gen_degree}, computed={gen_degree}")
    if claimed_q_gen != F.p ** claimed_gen_degree:
        errors.append("q_gen does not match p^gen_degree")

    # q_chal is metadata only unless a transfer theorem is supplied and verified.
    q_chal = ledger.get("q_chal")
    if q_chal is not None and ledger.get("uses_q_chal", False):
        transfer = ledger.get("protocol_transfer_receipt")
        if not _receipt_verified(transfer, strict=True):
            errors.append("q_chal used without a verified protocol-transfer receipt")

    if truth is not None and int(truth.get("q_line", F.order)) != F.order:
        errors.append("truth q_line mismatch")

    return not errors, errors, {
        "p": F.p,
        "line_degree": F.degree,
        "q_gen": F.p ** gen_degree,
        "q_code": F.p ** code_degree,
        "q_line": F.order,
        "q_chal": q_chal,
        "security_floor": F.order // (1 << 128),
        "target_bits": target_bits,
        "line_data_is_code_valued": bool(f or g) and all(F.in_subfield_degree(x, code_degree) for x in f + g),
    }


def audit_certificate(cert: Mapping[str, Any], strict: bool = True) -> Dict[str, Any]:
    if cert.get("schema_version") != "cycle109-cert-v1":
        raise CheckError("unsupported schema_version")
    F = FiniteField.from_spec(cert["field_ledger"], verify_irreducible=not cert.get("skip_irreducibility_check", False))

    truth: Optional[Dict[str, Any]] = None
    if cert.get("instance") and cert.get("scope", {}).get("truth_mode") == "EXHAUSTIVE_SOURCE":
        truth = official_bad_slopes(cert["instance"], F)

    field_ok, field_errors, ledger_report = _field_ledger_check(cert, F, truth)
    report: Dict[str, Any] = {
        "schema_version": cert["schema_version"],
        "terminal_label": None,
        "scope": cert.get("scope", {}),
        "field_ledger": ledger_report,
        "field_errors": field_errors,
        "truth": truth,
        "violations": [],
        "warnings": [],
    }
    if not field_ok:
        report["terminal_label"] = "FIELD_LEDGER_MISMATCH"
        return report

    source_completeness_ok = True
    if truth is None:
        claimed = [_parse_slope_key(x) for x in cert.get("claimed_bad_slopes", [])]
        truth_slopes = set(claimed)
        source_completeness_ok = _receipt_verified(cert.get("source_completeness_receipt"), strict)
        if not source_completeness_ok:
            report["warnings"].append("bad-slope completeness is supplied but not proof-kernel verified")
    else:
        truth_slopes = set(int(x) for x in truth["distinct_bad_slopes"])

    denom = cert.get("denominator", {})
    denominator_minimality_ok = _receipt_verified(denom.get("minimality_receipt"), strict)
    if not denominator_minimality_ok:
        report["warnings"].append("intrinsic denominator minimality is not proof-kernel verified")

    classifications_raw = cert.get("classifications", {})
    classifications: Dict[int, Mapping[str, Any]] = {
        _parse_slope_key(k): v for k, v in classifications_raw.items()
    }
    classified_slopes = set(classifications)
    missing = sorted(truth_slopes - classified_slopes)
    extra = sorted(classified_slopes - truth_slopes)
    if missing:
        report["violations"].append({"kind": "UNCLASSIFIED_BAD_SLOPES", "slopes": missing})
    if extra:
        report["violations"].append({"kind": "CLASSIFIED_NONBAD_SLOPES", "slopes": extra})

    branch_slopes: Dict[str, List[int]] = {b: [] for b in sorted(PRIMARY_BRANCHES)}
    semantic_receipt_failures: List[Dict[str, Any]] = []
    for z, row in classifications.items():
        branch = str(row.get("primary_branch", ""))
        if branch not in PRIMARY_BRANCHES:
            report["violations"].append({"kind": "UNKNOWN_PRIMARY_BRANCH", "slope": z, "branch": branch})
            continue
        branch_slopes[branch].append(z)
        receipt = row.get("branch_receipt")
        # LOW/BALANCED/HIGH stratum is additionally checked against intrinsic_t.
        if branch in RESIDUAL_BRANCHES:
            t = int(row.get("intrinsic_t", cert.get("denominator", {}).get("intrinsic_t", -1)))
            sigma = int(cert.get("instance", {}).get("sigma", cert.get("parameters", {}).get("sigma", -1)))
            expected = "LOW" if 1 <= t < sigma else "BALANCED" if t == sigma else "HIGH" if t > sigma else None
            if expected != branch:
                semantic_receipt_failures.append({"slope": z, "reason": "intrinsic-degree stratum mismatch", "t": t, "sigma": sigma, "expected": expected, "got": branch})
            if not denominator_minimality_ok:
                semantic_receipt_failures.append({"slope": z, "reason": "intrinsic denominator minimality unverified", "t": t})
        elif not _receipt_verified(receipt, strict):
            semantic_receipt_failures.append({"slope": z, "reason": "paid-branch receipt unverified", "branch": branch})

    if semantic_receipt_failures:
        report["violations"].append({"kind": "UNVERIFIED_BRANCH_RECEIPTS", "items": semantic_receipt_failures})

    charts = {str(c["chart_id"]): c for c in cert.get("charts", [])}
    chart_assignments: Dict[str, List[int]] = {cid: [] for cid in charts}
    for z, row in classifications.items():
        branch = row.get("primary_branch")
        if branch in RESIDUAL_BRANCHES:
            cid = row.get("chart_id")
            if cid is None or str(cid) not in charts:
                report["violations"].append({"kind": f"UNPAID_{branch}_SLOPE", "slope": z})
            else:
                chart_assignments[str(cid)].append(z)

    chart_results: Dict[str, Any] = {}
    ap_failures: List[Dict[str, Any]] = []
    unpaid_low: List[Any] = []
    unpaid_balanced: List[Any] = []
    unpaid_high: List[Any] = []
    chart_cap_sum = 0
    for cid, chart in charts.items():
        assigned = sorted(chart_assignments.get(cid, []))
        branch = str(chart.get("branch", ""))
        result: Dict[str, Any] = {"branch": branch, "assigned_slopes": assigned, "violations": []}
        if branch not in RESIDUAL_BRANCHES:
            result["violations"].append("chart branch must be LOW/BALANCED/HIGH")
        tag = chart.get("tag")
        required_tag_keys = {"source_object_id", "support_selector_id", "normalization_id", "field_embedding_id"}
        if not isinstance(tag, Mapping) or not required_tag_keys.issubset(tag):
            result["violations"].append("incomplete retained chart tag")

        norm = chart.get("normalization", {})
        if norm.get("source_field") != "K_line" or norm.get("target_field") != "K_line":
            result["violations"].append("normalization is not same-field K_line -> K_line")
        values_raw = norm.get("values", {})
        values = {_parse_slope_key(k): int(v) for k, v in values_raw.items()}
        if set(values) != set(assigned):
            result["violations"].append("normalization domain does not equal assigned slope set")
        if len(set(values.values())) != len(values):
            result["violations"].append("normalization is not injective")
        for v in values.values():
            try:
                F.coeffs(v)
            except CheckError as exc:
                result["violations"].append(str(exc))

        gate_ok, gate_detail = _chart_rank_escape(chart, F)
        result["gate_b"] = gate_detail
        result["gate_b"]["rank_escape"] = gate_ok

        ap = chart.get("ap_corr", {})
        ap_verified = _receipt_verified(ap.get("source_receipt"), strict)
        charged_failure = bool(chart.get("failure_charge_id"))
        if not ap_verified:
            ap_failures.append({"chart": cid, "reason": "source AP_corr receipt unverified"})
        if ap_verified and not gate_ok and not charged_failure:
            ap_failures.append({"chart": cid, "reason": "AP_corr verified but Gate B rank escape failed without charge"})

        cap = chart.get("cap", {})
        cap_kind = cap.get("kind")
        cap_value = int(cap.get("value", -1))
        cap_valid = False
        if cap_kind == "FINITE_EXACT_IMAGE":
            cap_valid = cap_value >= len(set(values.values())) and cap_value >= len(assigned)
        elif cap_kind == "UNIVARIATE_SEPARATOR":
            parameter_dimension = int(chart.get("gate_b", {}).get("parameter_dimension", -1))
            degree_bound = int(cap.get("degree_bound", -1))
            cap_valid = gate_ok and parameter_dimension == 1 and cap_value == degree_bound and len(assigned) <= cap_value
        elif cap_kind == "CURVE_BEZOUT":
            separator_degree = int(cap.get("separator_degree", -1))
            curve_degree = int(cap.get("curve_degree", -1))
            no_common_component = _receipt_verified(cap.get("no_common_component_receipt"), strict)
            cap_valid = gate_ok and no_common_component and cap_value == separator_degree * curve_degree and len(assigned) <= cap_value
        elif cap_kind == "TWO_SEPARATOR_BEZOUT":
            d1 = int(cap.get("degree_1", -1))
            d2 = int(cap.get("degree_2", -1))
            zero_dimensional = _receipt_verified(cap.get("zero_dimensional_receipt"), strict)
            cap_valid = zero_dimensional and cap_value == d1 * d2 and len(assigned) <= cap_value
        elif cap_kind == "SYMBOLIC_BOUND":
            cap_valid = _receipt_verified(cap.get("bound_receipt"), strict) and len(assigned) <= cap_value
        if not cap_valid:
            result["violations"].append("missing or invalid distinct-slope cap")
        else:
            chart_cap_sum += cap_value
        result["cap_valid"] = cap_valid
        result["cap_value"] = cap_value

        if result["violations"]:
            if branch == "LOW":
                unpaid_low.append({"chart": cid, "violations": result["violations"]})
            elif branch == "BALANCED":
                unpaid_balanced.append({"chart": cid, "violations": result["violations"]})
            elif branch == "HIGH":
                unpaid_high.append({"chart": cid, "violations": result["violations"]})
        chart_results[cid] = result

    # Any residual slope with no chart is an unpaid branch defect.
    for violation in report["violations"]:
        if violation.get("kind") == "UNPAID_LOW_SLOPE":
            unpaid_low.append(violation)
        elif violation.get("kind") == "UNPAID_BALANCED_SLOPE":
            unpaid_balanced.append(violation)
        elif violation.get("kind") == "UNPAID_HIGH_SLOPE":
            unpaid_high.append(violation)

    # Chart-count condition. Finite numerical inequality is checked directly;
    # uniformity in k,sigma,t needs a theorem receipt in strict mode.
    chart_bound = cert.get("chart_bound", {})
    C = int(chart_bound.get("C", -1))
    n = int(cert.get("instance", {}).get("D") and len(cert["instance"]["D"]) or cert.get("parameters", {}).get("n", 0))
    chart_count_numeric_ok = C >= 0 and n > 0 and len(charts) <= n ** C
    chart_uniform_ok = _receipt_verified(chart_bound.get("uniformity_receipt"), strict)
    if not chart_count_numeric_ok:
        report["violations"].append({"kind": "CHART_COUNT_EXCEEDS_BOUND", "chart_count": len(charts), "n": n, "C": C})
    if not chart_uniform_ok:
        report["warnings"].append("uniform chart exponent independent of k,sigma,t is not proof-kernel verified")

    # Paid caps are checked on distinct assigned slopes only.
    paid_caps_raw = cert.get("paid_caps", {})
    paid_cap_sum = 0
    paid_cap_results: Dict[str, Any] = {}
    for branch in sorted(PAID_BRANCHES):
        assigned = sorted(branch_slopes.get(branch, []))
        cap_row = paid_caps_raw.get(branch)
        if not assigned and cap_row is None:
            paid_cap_results[branch] = {"assigned": 0, "cap": 0, "valid": True}
            continue
        if cap_row is None:
            valid = False
            cap_value = -1
        else:
            cap_value = int(cap_row.get("value", -1))
            valid = cap_value >= len(assigned) and _receipt_verified(cap_row.get("receipt"), strict)
            if branch == "ENDPOINT":
                valid = valid and cap_value <= 1
            if branch == "FIELD_CONFINEMENT" and cap_row.get("builtin_subfield_degree") is not None:
                d = int(cap_row["builtin_subfield_degree"])
                inst = cert.get("instance", {})
                vals = [int(x) for x in inst.get("D", []) + inst.get("f", []) + inst.get("g", [])]
                builtin_ok = F.degree % d == 0 and all(F.in_subfield_degree(x, d) for x in vals)
                valid = valid and builtin_ok and cap_value == F.p ** d
        paid_cap_results[branch] = {"assigned": len(assigned), "cap": cap_value, "valid": valid}
        if valid:
            paid_cap_sum += cap_value
        elif assigned:
            report["violations"].append({"kind": "UNPAID_BRANCH_CAP", "branch": branch, "assigned": assigned})

    N_off_exact = len(truth_slopes) if truth is not None else None
    N_cap = paid_cap_sum + chart_cap_sum
    security_floor = F.order // (1 << 128)
    security_ok = N_cap <= security_floor
    exact_security_ok = N_off_exact is not None and N_off_exact <= security_floor

    report.update({
        "branch_distinct_slope_counts": {k: len(set(v)) for k, v in branch_slopes.items()},
        "same_slope_support_collision_count": truth.get("same_slope_support_collision_count") if truth else None,
        "charts": chart_results,
        "chart_count": len(charts),
        "chart_bound": {"C": C, "numeric_ok": chart_count_numeric_ok, "uniformity_verified": chart_uniform_ok},
        "paid_caps": paid_cap_results,
        "N_off_exact": N_off_exact,
        "N_cap": N_cap,
        "security_floor": security_floor,
        "security_bound_verified": security_ok,
        "exact_finite_security_verified": exact_security_ok,
        "ap_failures": ap_failures,
        "source_completeness_verified": source_completeness_ok,
        "denominator_minimality_verified": denominator_minimality_ok,
    })

    # Terminal precedence is deliberate and deterministic.
    if unpaid_low:
        report["terminal_label"] = "UNPAID_LOW_RESIDUAL"
        report["first_failure"] = unpaid_low[0]
        return report
    if unpaid_balanced:
        report["terminal_label"] = "UNPAID_BALANCED_COVER"
        report["first_failure"] = unpaid_balanced[0]
        return report
    if unpaid_high:
        report["terminal_label"] = "UNPAID_HIGH_PLANE"
        report["first_failure"] = unpaid_high[0]
        return report
    if ap_failures:
        report["terminal_label"] = "AP_DESCENT_FAILURE"
        report["first_failure"] = ap_failures[0]
        return report

    family = cert.get("family_promotion", {})
    counter_claimed = bool(family.get("claims_counterpacket", False))
    if counter_claimed:
        promotion_requirements = [
            family.get("official_source_family_receipt"),
            family.get("unbounded_parameter_receipt"),
            family.get("corrected_reserve_receipt"),
            family.get("all_charges_paid_or_absent_receipt"),
            family.get("growth_or_systematic_failure_receipt"),
        ]
        promoted = all(_receipt_verified(x, strict) for x in promotion_requirements)
        report["family_promotion_verified"] = promoted
        report["terminal_label"] = "SOURCE_VALID_COUNTERPACKET" if promoted else "MODEL_ONLY_STRESS_FAMILY"
        return report

    all_semantic_ok = source_completeness_ok and not missing and not extra and not semantic_receipt_failures
    all_paid_ok = all(v["valid"] for v in paid_cap_results.values())
    all_chart_ok = all(not v["violations"] for v in chart_results.values())
    if all_semantic_ok and all_paid_ok and all_chart_ok and chart_count_numeric_ok and chart_uniform_ok and security_ok:
        report["terminal_label"] = "STRATIFIED_COVER_CERTIFIED"
    else:
        report["terminal_label"] = "MODEL_ONLY_STRESS_FAMILY"
        if not security_ok:
            report["violations"].append({"kind": "NUMERATOR_TARGET_FAILED", "N_cap": N_cap, "floor": security_floor})
    return report


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_enum = sub.add_parser("enumerate", help="exactly enumerate official bad slopes for one finite source instance")
    p_enum.add_argument("input", type=Path)
    p_enum.add_argument("--output", type=Path)
    p_enum.add_argument("--skip-irreducibility-check", action="store_true")

    p_audit = sub.add_parser("audit", help="audit a Cycle109 proof-carrying certificate")
    p_audit.add_argument("input", type=Path)
    p_audit.add_argument("--output", type=Path)
    p_audit.add_argument("--non-strict", action="store_true", help="trust externally asserted receipt booleans (research only)")

    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text())
        if args.command == "enumerate":
            F = FiniteField.from_spec(data["field_ledger"], verify_irreducible=not args.skip_irreducibility_check)
            result = official_bad_slopes(data["instance"], F)
        else:
            result = audit_certificate(data, strict=not args.non_strict)
    except (CheckError, KeyError, ValueError, ZeroDivisionError) as exc:
        result = {"terminal_label": "INVALID_CERTIFICATE", "error": str(exc)}

    text = json.dumps(result, indent=2, sort_keys=True)
    if getattr(args, "output", None):
        args.output.write_text(text + "\n")
    else:
        print(text)
    return 0 if result.get("terminal_label") != "INVALID_CERTIFICATE" else 2


if __name__ == "__main__":
    raise SystemExit(main())
