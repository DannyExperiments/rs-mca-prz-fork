#!/usr/bin/env python3
"""Fail-closed verifier for the finite Cycle84 -> RS MCA/LD_sw transfer inputs.

This checker consumes only the extracted Cycle116 packet.  It verifies the
finite Cycle84 receipt, the 336-state support/locator compiler, the fixed
six-jet and locator-evaluation scalar inputs, the quadratic smooth-domain
field lift, and the exact q-ledger arithmetic.  The universal fixed-jet
locator theorem remains the short algebraic lemma stated in the proof note;
this script checks every concrete antecedent used by its two instantiations.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


def load_model(path: Path):
    spec = importlib.util.spec_from_file_location("cycle68_model", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "packet_root",
        nargs="?",
        default="/mnt/data/cycle116_packet/cycle116_standalone_c84_to_rs_mca_ld_certificate_9pro",
        help="extracted packet root",
    )
    args = ap.parse_args()
    root = Path(args.packet_root).resolve()
    cert = root / "context" / "cycle84_finite_certificate"
    if not cert.is_dir():
        raise SystemExit(f"missing certificate directory: {cert}")

    # Integrity and the accepted finite occupancy receipt.
    subprocess.run(
        ["sha256sum", "-c", "REVIEW_MANIFEST.sha256"],
        cwd=cert,
        check=True,
        stdout=subprocess.DEVNULL,
    )
    finite_raw = subprocess.check_output(
        [sys.executable, "verify_certificate.py"], cwd=cert, text=True
    )
    finite = json.loads(finite_raw)
    assert finite["decision"] == "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED"
    assert finite["exact_true_m_max"] == 2
    assert finite["exact_true_occupancy"] == 52_747_567_092
    assert finite["exact_true_ordered_offdiagonal_energy"] == 24
    assert finite["true_double_fibers"] == 12

    c = load_model(cert / "model" / "cycle68_slot_factorization_checker.py")
    f = c.find_field_poly()
    eta = c.find_eta(f)
    beta = c.find_beta(f)
    q0 = 17**16
    assert c.irred16(f)
    assert f == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
    assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
    assert beta == (2, 1)
    assert c.fpow(eta, 256, f) == c.ONE
    assert c.fpow(eta, 128, f) != c.ONE
    assert c.fpow(eta, 16, f) == c.emb(3)
    assert c.fpow(beta, 256, f) != c.ONE  # beta not in <eta>

    # Exact E_i root polynomials and the two missing high coefficients.
    for i, eset in c.E_SETS.items():
        p = c.ONE
        for e in sorted(eset):
            p = c.pmul(p, ((-pow(3, e, 17)) % 17, 1))
        assert p == c.P_COEFFS[i]
        assert len(p) == 9 and p[8] == 1 and p[7] == p[6] == 0

    # Field-polynomial helpers for locator polynomials in a new variable Y.
    FZERO = ()
    FONE = c.ONE

    def fneg(a):
        return c.psub(FZERO, a)

    def poly_mul(A, B):
        out = [FZERO] * (len(A) + len(B) - 1)
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                out[i + j] = c.padd(out[i + j], c.fmul(a, b, f))
        while out and out[-1] == FZERO:
            out.pop()
        return out

    def poly_eval(A, x):
        y = FZERO
        for a in reversed(A):
            y = c.padd(c.fmul(y, x, f), a)
        return y

    table = c.build_u(f, eta, beta)
    state_sets = {}
    block_checks = 0
    for t in range(1, 8):
        seen_at_t = set()
        for i in (1, 2, 3):
            for a in range(16):
                B = frozenset((a + e) % 16 for e in c.E_SETS[i])
                assert len(B) == 8
                # The 16 roots in eta^t<eta^8>, represented by eta-exponents.
                exps = frozenset(
                    eidx
                    for b in B
                    for eidx in ((t + 8 * b) % 256, (t + 8 * (b + 16)) % 256)
                )
                assert len(exps) == 16
                assert all(eidx % 8 == t for eidx in exps)
                assert exps not in seen_at_t
                seen_at_t.add(exps)
                state_sets[(t, i, a)] = exps

                # R_{t,i,a}(Y)=prod_b(Y^2-eta^{2t}3^b).
                R = [FONE]
                for b in sorted(B):
                    root = c.fmul(c.fpow(eta, 2 * t, f), c.emb(pow(3, b, 17)), f)
                    R = poly_mul(R, [fneg(root), FZERO, FONE])
                assert len(R) == 17 and R[16] == FONE
                assert all(R[d] == FZERO for d in range(11, 16))
                expected = c.fmul(c.emb(pow(3, t, 17)), table[(t, i, a)], f)
                assert poly_eval(R, beta) == expected
                assert expected != FZERO
                block_checks += 1
        assert len(seen_at_t) == 48

    # Distinct slot cosets and the fixed point give 113-point supports.
    assert block_checks == 336
    for t1 in range(1, 8):
        union1 = set().union(*(state_sets[(t1, i, a)] for i in (1, 2, 3) for a in range(16)))
        assert 0 not in union1
        for t2 in range(t1 + 1, 8):
            union2 = set().union(*(state_sets[(t2, i, a)] for i in (1, 2, 3) for a in range(16)))
            assert union1.isdisjoint(union2)

    # The concrete fixed jet and common scalar follow from the checked block data.
    # Each block is Y^16 + degree<=10, hence seven blocks are
    # Y^112 + degree<=106, and multiplication by (Y-1) gives
    # Y^113-Y^112+degree<=107.
    kappa = c.fmul(c.psub(beta, c.ONE), c.emb(pow(3, 28, 17)), f)
    assert pow(3, 28, 17) == 4
    assert kappa == c.fmul(c.emb(4), c.psub(beta, c.ONE), f)
    assert kappa != FZERO

    # eta is nonsquare and theta^2=eta produces F_{17^32} with ord(theta)=512.
    x = q0 - 1
    v2 = 0
    while x % 2 == 0:
        x //= 2
        v2 += 1
    assert v2 == 8
    assert c.fpow(eta, (q0 - 1) // 2, f) == c.emb(16)  # -1

    KZERO = (FZERO, FZERO)
    KONE = (FONE, FZERO)
    theta = (FZERO, FONE)

    def kadd(u, v):
        return (c.padd(u[0], v[0]), c.padd(u[1], v[1]))

    def kneg(u):
        return (fneg(u[0]), fneg(u[1]))

    def ksub(u, v):
        return kadd(u, kneg(v))

    def kmul(u, v):
        ac = c.fmul(u[0], v[0], f)
        bdeta = c.fmul(c.fmul(u[1], v[1], f), eta, f)
        adbc = c.padd(c.fmul(u[0], v[1], f), c.fmul(u[1], v[0], f))
        return (c.padd(ac, bdeta), adbc)

    def kpow(u, e):
        out, base = KONE, u
        while e:
            if e & 1:
                out = kmul(out, base)
            base = kmul(base, base)
            e >>= 1
        return out

    assert kmul(theta, theta) == (eta, FZERO)
    assert kpow(theta, 256) == (c.emb(16), FZERO)
    assert kpow(theta, 512) == KONE
    H = [kpow(theta, i) for i in range(512)]
    assert len(set(H)) == 512
    betaK = (beta, FZERO)
    assert betaK not in set(H)

    A = [kmul(theta, (c.fpow(eta, i, f), FZERO)) for i in range(119)]
    Rfix = [kmul(theta, (c.fpow(eta, i, f), FZERO)) for i in range(119, 256)]
    D0 = [(c.fpow(eta, i, f), FZERO) for i in range(256)]
    assert len(set(A)) == 119 and len(set(Rfix)) == 137 and len(set(D0)) == 256
    assert set(A).isdisjoint(Rfix) and set(A).isdisjoint(D0) and set(Rfix).isdisjoint(D0)
    assert set(A) | set(Rfix) | set(D0) == set(H)
    pRbeta = KONE
    for r in Rfix:
        pRbeta = kmul(pRbeta, ksub(betaK, r))
    assert pRbeta != KZERO

    # Final parameters and exact security comparison.
    n_native, j_native, sigma = 256, 113, 6
    k_native = n_native - j_native - sigma
    assert (k_native, n_native - j_native) == (137, 143)
    n_lift, j_lift = 512, 113 + len(Rfix)
    k_lift = n_lift - j_lift - sigma
    agreement = n_lift - j_lift
    assert (j_lift, k_lift, agreement) == (250, 256, 262)
    assert (n_lift - agreement, n_lift) == (250, 512)

    occ = finite["exact_true_occupancy"]
    q_line = 17**32
    assert q_line == 2_367_911_594_760_467_245_844_106_297_320_951_247_361
    threshold = q_line // 2**128
    assert threshold == 6
    assert occ > threshold
    assert occ * 2**128 > q_line

    result = {
        "decision": "C84_TO_SMOOTH_RS_MCA_LD_SW_ANTECEDENTS_VERIFIED",
        "finite": {
            "m_max": finite["exact_true_m_max"],
            "occupancy": occ,
            "ordered_offdiagonal_energy": finite["exact_true_ordered_offdiagonal_energy"],
            "double_fibers": finite["true_double_fibers"],
        },
        "native_row": {"n": 256, "k": 137, "j": 113, "sigma": 6, "agreement": 143},
        "smooth_row": {
            "field": "F_17^32",
            "domain_order": 512,
            "n": 512,
            "k": 256,
            "j": 250,
            "sigma": 6,
            "agreement": 262,
            "radius": "125/256",
        },
        "concrete_checks": {
            "block_states": block_checks,
            "block_locator_form": "Y^16 + degree<=10",
            "locator_jet": "Y^113-Y^112+degree<=107",
            "locator_scalar": "P_T(beta)=4(beta-1)Phi(T)",
            "eta_order": 256,
            "theta_order": 512,
            "fixed_cosupport_roots": len(Rfix),
            "agreement_padding_roots": len(A),
        },
        "q_ledger": {
            "q_gen": q_line,
            "q_code": q_line,
            "q_line": q_line,
            "q_chal": None,
            "floor_q_line_over_2^128": threshold,
            "occupancy_exceeds_threshold": True,
        },
        "scope": "finite support-wise MCA/LD_sw antecedents; no protocol or official-prize contract",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
