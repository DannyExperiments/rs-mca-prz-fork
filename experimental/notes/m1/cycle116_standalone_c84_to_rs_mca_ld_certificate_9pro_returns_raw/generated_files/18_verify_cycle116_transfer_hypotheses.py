#!/usr/bin/env python3
"""Deterministic algebraic-hypothesis verifier for the Cycle116 transfer.

This checker consumes only the supplied Cycle116 packet.  It verifies the
finite Cycle84 receipt through its existing verifier, and independently checks
all finite-field, block-locator, fixed-jet, product-scalar, and smooth-lift
hypotheses used by the generic mathematical transfer lemma.

It does not attempt to machine-prove the generic fixed-jet theorem itself; that
is a short symbolic linear-algebra lemma that must accompany this receipt.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Tuple


def verify_sha256_manifest(base: Path, manifest: Path) -> int:
    """Fail closed on a GNU-style SHA-256 manifest; return checked-file count."""
    checked = 0
    for lineno, raw in enumerate(manifest.read_text().splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError as exc:
            raise AssertionError(f"malformed manifest line {lineno}: {raw!r}") from exc
        rel = rel.lstrip("*").removeprefix("./")
        target = base / rel
        assert target.is_file(), f"missing manifest target: {target}"
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        assert actual == expected, f"SHA-256 mismatch for {rel}: {actual} != {expected}"
        checked += 1
    assert checked > 0
    return checked


def load_model(root: Path):
    path = root / "context" / "cycle84_finite_certificate" / "model" / "cycle68_slot_factorization_checker.py"
    spec = importlib.util.spec_from_file_location("cycle68_model", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load model: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def v2(n: int) -> int:
    if n <= 0:
        raise ValueError("v2 expects a positive integer")
    ans = 0
    while n % 2 == 0:
        ans += 1
        n //= 2
    return ans


def ff_zero() -> tuple[int, ...]:
    return ()


def poly_trim_ff(p: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    while p and not p[-1]:
        p.pop()
    return p


def poly_mul_ff(c, a: list[tuple[int, ...]], b: list[tuple[int, ...]], modulus) -> list[tuple[int, ...]]:
    if not a or not b:
        return []
    out = [ff_zero() for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = c.padd(out[i + j], c.fmul(x, y, modulus))
    return poly_trim_ff(out)


def poly_eval_ff(c, p: list[tuple[int, ...]], x: tuple[int, ...], modulus) -> tuple[int, ...]:
    out = ff_zero()
    for coeff in reversed(p):
        out = c.padd(c.fmul(out, x, modulus), coeff)
    return out


def poly_over_fp_from_roots(roots: Iterable[int], p: int) -> tuple[int, ...]:
    out = [1]
    for root in roots:
        nxt = [0] * (len(out) + 1)
        for i, coeff in enumerate(out):
            nxt[i] = (nxt[i] - coeff * root) % p
            nxt[i + 1] = (nxt[i + 1] + coeff) % p
        out = nxt
    return tuple(out)


def k_add(c, x, y):
    return (c.padd(x[0], y[0]), c.padd(x[1], y[1]))


def k_mul(c, modulus, eta, x, y):
    # (a+b theta)(c+d theta)=(ac+bd eta)+(ad+bc)theta, theta^2=eta.
    a, b = x
    d, e = y
    const = c.padd(c.fmul(a, d, modulus), c.fmul(c.fmul(b, e, modulus), eta, modulus))
    theta = c.padd(c.fmul(a, e, modulus), c.fmul(b, d, modulus))
    return (const, theta)


def k_pow(c, modulus, eta, x, exponent: int):
    one = (c.ONE, ff_zero())
    out = one
    base = x
    e = exponent
    while e:
        if e & 1:
            out = k_mul(c, modulus, eta, out, base)
        base = k_mul(c, modulus, eta, base, base)
        e >>= 1
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--packet-root",
        type=Path,
        default=Path("/mnt/data/cycle116_packet/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro"),
        help="directory containing TARGET_CERTIFICATE_BLUEPRINT.md and context/",
    )
    args = parser.parse_args()
    root = args.packet_root.resolve()
    cert_root = root / "context" / "cycle84_finite_certificate"

    # Bind the run to the review-facing packet root before importing Python files.
    # REVIEW_MANIFEST intentionally excludes mutable __pycache__ artifacts.
    review_manifest_count = verify_sha256_manifest(
        cert_root, cert_root / "REVIEW_MANIFEST.sha256"
    )

    c = load_model(root)

    # Existing finite receipt.
    proc = subprocess.run(
        [sys.executable, str(cert_root / "verify_certificate.py")],
        cwd=cert_root,
        check=True,
        capture_output=True,
        text=True,
    )
    finite = json.loads(proc.stdout)
    assert finite["decision"] == "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED"
    assert finite["exact_true_m_max"] == 2
    assert finite["exact_true_occupancy"] == 52_747_567_092
    assert finite["exact_true_ordered_offdiagonal_energy"] == 24
    assert finite["true_double_fibers"] == 12

    # Base field and named elements.
    p = 17
    q0 = p**16
    modulus = c.find_field_poly()
    eta = c.find_eta(modulus)
    beta = c.find_beta(modulus)
    assert modulus == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
    assert beta == (2, 1)
    assert c.irred16(modulus)
    assert c.fpow(eta, 16, modulus) == c.emb(3)
    assert c.fpow(eta, 256, modulus) == c.ONE
    assert c.fpow(eta, 128, modulus) == c.emb(-1)
    assert c.fpow(beta, 256, modulus) != c.ONE
    assert v2(q0 - 1) == 8
    assert c.fpow(eta, (q0 - 1) // 2, modulus) == c.emb(-1)  # nonsquare

    # eta generates F_{17^16} over F_17: no proper subfield can contain an order-256 element.
    for d in (1, 2, 4, 8):
        assert c.fpow(eta, p**d - 1, modulus) != c.ONE

    # The three eight-root polynomials, including the two zero top subleading coefficients.
    for i, eset in c.E_SETS.items():
        got = poly_over_fp_from_roots((pow(3, e, p) for e in eset), p)
        assert got == c.P_COEFFS[i]
        assert got[7] == 0 and got[6] == 0

    table = c.build_u(modulus, eta, beta)
    eta_pows = [c.fpow(eta, j, modulus) for j in range(256)]
    seen_bsets: set[frozenset[int]] = set()
    all_block_gap_checks = 0
    all_block_value_checks = 0

    for t in range(1, 8):
        for i in (1, 2, 3):
            for a in range(16):
                bset = frozenset((a + e) % 16 for e in c.E_SETS[i])
                if t == 1:
                    seen_bsets.add(bset)
                    expected_color = (c.S_COLOR[i] + 8 * (a & 1)) % 16
                    assert sum(bset) % 16 == expected_color

                # R_{t,i,a}(X)=prod_b (X^2-eta^(2t)3^b).
                block: list[tuple[int, ...]] = [c.ONE]
                eta2t = eta_pows[2 * t]
                for b in sorted(bset):
                    root = c.fmul(eta2t, c.emb(pow(3, b, p)), modulus)
                    factor = [c.psub(ff_zero(), root), ff_zero(), c.ONE]
                    block = poly_mul_ff(c, block, factor, modulus)
                assert len(block) == 17 and block[16] == c.ONE
                assert all(not block[d] for d in range(11, 16))
                all_block_gap_checks += 1

                # Exact factor linking the finite packet slot value to locator evaluation.
                lhs = poly_eval_ff(c, block, beta, modulus)
                rhs = c.fmul(c.emb(pow(3, t, p)), table[(t, i, a)], modulus)
                assert lhs == rhs
                all_block_value_checks += 1

    assert len(seen_bsets) == 48
    assert all_block_gap_checks == all_block_value_checks == 336

    # Degree-support proof of the common six-jet.
    possible_degrees = {0}
    for _ in range(7):
        possible_degrees = {a + b for a in possible_degrees for b in ({16} | set(range(0, 11)))}
    assert 112 in possible_degrees
    assert not any(d in possible_degrees for d in range(107, 112))
    # Multiplication by X-1 leaves degrees 113,112 fixed and all other terms <=107.

    kappa = c.fmul(c.emb(4), c.psub(beta, c.ONE), modulus)
    assert kappa
    assert pow(3, 28, p) == 4

    # Quadratic smooth lift K=F0(theta), theta^2=eta.
    theta = (ff_zero(), c.ONE)
    k_one = (c.ONE, ff_zero())
    k_minus_one = (c.emb(-1), ff_zero())
    assert k_pow(c, modulus, eta, theta, 2) == (eta, ff_zero())
    assert k_pow(c, modulus, eta, theta, 256) == k_minus_one
    assert k_pow(c, modulus, eta, theta, 512) == k_one
    H = [k_pow(c, modulus, eta, theta, i) for i in range(512)]
    assert len(set(H)) == 512

    D0 = {k_pow(c, modulus, eta, theta, 2 * i) for i in range(256)}
    odd = {k_pow(c, modulus, eta, theta, 2 * i + 1) for i in range(256)}
    assert D0.isdisjoint(odd)
    assert D0 | odd == set(H)
    A = {k_pow(c, modulus, eta, theta, 2 * i + 1) for i in range(119)}
    R = {k_pow(c, modulus, eta, theta, 2 * i + 1) for i in range(119, 256)}
    assert len(A) == 119 and len(R) == 137 and A.isdisjoint(R)
    assert D0.isdisjoint(A | R) and D0 | A | R == set(H)

    # Parameter and security arithmetic.
    N = 52_747_567_092
    q = 17**32
    assert 137 + 119 == 256
    assert 143 + 119 == 262
    assert 512 - 262 == 250
    assert (250, 512) == (125 * 2, 256 * 2)
    assert q // 2**128 == 6
    assert N > q // 2**128
    assert N * 2**128 > q

    # Detect and quarantine the stale mixed primitive-log metadata instead of
    # silently accepting an unbased numerical logarithm.  Both gauges are
    # primitive and exponentiate to the same explicit double-fiber product.
    prose = (cert_root / "STANDALONE_FINITE_CERTIFICATE.md").read_text()
    master = json.loads((cert_root / "cycle84_master_proof_certificate.json").read_text())
    slot_logs = json.loads((cert_root / "data" / "slot_logs.json").read_text())
    mixed_log_gauge_detected = (
        "gamma = X + 1" in prose
        and master["model"]["generator"] == [1, 1]
        and slot_logs["generator"] == [2, 1]
    )
    assert mixed_log_gauge_detected
    gamma_x_plus_1 = (1, 1)
    gamma_x_plus_2 = beta
    factors = (2, 3, 5, 29, 18_913, 41_761, 184_417)
    for gamma in (gamma_x_plus_1, gamma_x_plus_2):
        assert c.fpow(gamma, q0 - 1, modulus) == c.ONE
        assert all(c.fpow(gamma, (q0 - 1) // ell, modulus) != c.ONE for ell in factors)
    witness_product = tuple(master["explicit_double_witness"]["product_field_coefficients"])
    log_x_plus_1 = int(master["explicit_double_witness"]["product_log"])
    # The compact/full-census table is in the X+2 gauge.
    records = {(r["t"], r["i"], r["a"]): int(r["log"]) for r in slot_logs["records"]}
    witness_tuple = ((1, 4), (2, 10), (3, 14), (1, 12), (3, 0), (2, 6), (3, 8))
    log_x_plus_2 = sum(records[(t, i, a)] for t, (i, a) in enumerate(witness_tuple, 1)) % (q0 - 1)
    assert c.fpow(gamma_x_plus_1, log_x_plus_1, modulus) == witness_product
    assert c.fpow(gamma_x_plus_2, log_x_plus_2, modulus) == witness_product

    result = {
        "decision": "CYCLE116_TRANSFER_HYPOTHESES_VERIFIED",
        "packet_binding": {
            "review_manifest": "REVIEW_MANIFEST.sha256",
            "files_verified": review_manifest_count,
        },
        "finite_receipt": {
            "m_max": finite["exact_true_m_max"],
            "occupancy": finite["exact_true_occupancy"],
            "ordered_offdiagonal_energy": finite["exact_true_ordered_offdiagonal_energy"],
            "double_fibers": finite["true_double_fibers"],
        },
        "base_field": {
            "q0": q0,
            "eta_order": 256,
            "eta_16": 3,
            "eta_nonsquare": True,
            "beta_outside_D0": True,
            "generated_degree_by_eta": 16,
        },
        "cycle84_bridge": {
            "block_gap_checks": all_block_gap_checks,
            "block_value_checks": all_block_value_checks,
            "distinct_state_sets": len(seen_bsets),
            "fixed_locator_jet": "X^113-X^112+degree<=107",
            "locator_value_scalar": "P_T(beta)=4(beta-1)Phi(T)",
        },
        "smooth_lift": {
            "field_size": q,
            "theta_order": 512,
            "domain_size": len(H),
            "A_size": len(A),
            "R_size": len(R),
            "code_dimension": 256,
            "agreement": 262,
            "radius": "125/256",
        },
        "security_arithmetic": {
            "floor_q_over_2^128": q // 2**128,
            "numerator": N,
            "strictly_above_2^-128": True,
        },
        "audit_warning": {
            "mixed_primitive_log_gauge_detected": True,
            "x_plus_1_product_log": log_x_plus_1,
            "x_plus_2_product_log": log_x_plus_2,
            "same_field_product_verified": True,
            "required_action": "Correct or explicitly separate the X+1 and X+2 log gauges; do not use a numerical product log without naming its base.",
        },
        "scope": "Verifies algebraic hypotheses only; the generic fixed-jet and padding implications are supplied by the accompanying proof, not by enumeration.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
