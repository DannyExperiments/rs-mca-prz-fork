#!/usr/bin/env python3
"""Deterministic finite checks for the Cycle116 Cycle84 -> smooth [512,256] lift.

This script verifies the finite-field, Cycle84 structural bridge, padding-domain,
and integer-ledger clauses.  The generic fixed-jet syndrome theorem and the
L_A-divisibility lift are mathematical lemmas proved in the accompanying note.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
C84 = ROOT / 'context' / 'cycle84_finite_certificate'
MODEL = C84 / 'model' / 'cycle68_slot_factorization_checker.py'

spec = importlib.util.spec_from_file_location('cycle68', MODEL)
c = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(c)

ZERO = ()
ONE = c.ONE
P = 17


def fadd(a, b):
    return c.padd(a, b)


def fneg(a):
    return c.psub(ZERO, a)


def fmul(a, b, modulus):
    return c.fmul(a, b, modulus)


def poly_from_roots(roots, modulus):
    """Monic polynomial over F0, low-degree coefficients first."""
    out = [ONE]
    for root in roots:
        nxt = [ZERO] * (len(out) + 1)
        for i, coeff in enumerate(out):
            nxt[i] = fadd(nxt[i], fneg(fmul(coeff, root, modulus)))
            nxt[i + 1] = fadd(nxt[i + 1], coeff)
        out = nxt
    return out


def prime_poly_from_roots(roots):
    out = [1]
    for root in roots:
        nxt = [0] * (len(out) + 1)
        for i, coeff in enumerate(out):
            nxt[i] = (nxt[i] - root * coeff) % P
            nxt[i + 1] = (nxt[i + 1] + coeff) % P
        out = nxt
    return tuple(out)


# Re-run the accepted Cycle84 light verifier and parse its exact receipt.
receipt = json.loads(subprocess.run(
    [sys.executable, str(C84 / 'verify_certificate.py')],
    check=True,
    capture_output=True,
    text=True,
).stdout)
assert receipt['decision'] == 'CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED'
assert receipt['exact_true_m_max'] == 2
assert receipt['exact_true_occupancy'] == 52_747_567_092
assert receipt['exact_true_ordered_offdiagonal_energy'] == 24
assert receipt['true_double_fibers'] == 12

# Base field and native domain facts.
f = c.find_field_poly()
eta = c.find_eta(f)
beta = c.find_beta(f)
q0 = P**16
minus_one = c.emb(-1)
assert f == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
assert c.irred16(f)
assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
assert beta == (2, 1)
assert c.fpow(eta, 256, f) == ONE
assert c.fpow(eta, 128, f) == minus_one
assert c.fpow(eta, (q0 - 1) // 2, f) == minus_one  # nonsquare
assert c.fpow(beta, 256, f) != ONE                  # beta not in D0
assert c.fpow(eta, 16, f) == c.emb(3)

D0 = [c.fpow(eta, i, f) for i in range(256)]
assert len(set(D0)) == 256
H32 = [c.fpow(eta, 8 * i, f) for i in range(32)]
assert len(set(H32)) == 32
cosets = [set(c.fmul(c.fpow(eta, t, f), y, f) for y in H32) for t in range(8)]
assert all(len(s) == 32 for s in cosets)
assert len(set().union(*cosets)) == 256
assert all(cosets[i].isdisjoint(cosets[j]) for i in range(8) for j in range(i))

# Recompute the three base locator polynomials and their two missing top terms.
for i in (1, 2, 3):
    roots = [pow(3, e, P) for e in c.E_SETS[i]]
    coeffs = prime_poly_from_roots(roots)
    assert coeffs == c.P_COEFFS[i]
    assert len(coeffs) == 9 and coeffs[8] == 1
    assert coeffs[7] == coeffs[6] == 0

# Verify all 336 slot states: cardinality, distinctness, common jet, color,
# and the exact evaluation scalar block(beta)=3^t u_t(i,a).
table = c.build_u(f, eta, beta)
all_Y = set()
slot_checks = 0
for t in range(1, 8):
    eta_t = c.fpow(eta, t, f)
    for i in (1, 2, 3):
        for a in range(16):
            B = {(a + e) % 16 for e in c.E_SETS[i]}
            assert len(B) == 8
            color = (c.S_COLOR[i] + 8 * (a & 1)) % 16
            assert sum(B) % 16 == color
            target = {c.emb(pow(3, b, P)) for b in B}
            Y = tuple(y for y in H32 if c.fpow(y, 2, f) in target)
            assert len(Y) == 16 and len(set(Y)) == 16
            all_Y.add(frozenset(Y))
            roots = [c.fmul(eta_t, y, f) for y in Y]
            assert set(roots).issubset(cosets[t])
            loc = poly_from_roots(roots, f)
            assert len(loc) == 17 and loc[16] == ONE
            assert all(loc[d] == ZERO for d in range(11, 16))  # X^16 + O(X^10)
            block_at_beta = ONE
            block_root_product = ONE
            for root in roots:
                block_at_beta = c.fmul(block_at_beta, c.psub(beta, root), f)
                block_root_product = c.fmul(block_root_product, root, f)
            assert block_at_beta == c.fmul(c.emb(pow(3, t, P)), table[(t, i, a)], f)
            assert block_root_product == c.emb(pow(3, (t + sum(B)) % 16, P))
            slot_checks += 1
assert slot_checks == 336
assert len(all_Y) == 48

# The per-slot checks imply, for every seven-tuple, the exact universal identities:
# P_T=X^113-X^112+O(X^107) and P_T(beta)=(beta-1)3^28 Phi(T).
kappa = c.fmul(c.psub(beta, ONE), c.emb(pow(3, 28, P)), f)
assert kappa == (4, 4)
assert kappa != ZERO
assert pow(3, 28, P) == 4

# Quadratic extension K=F0(theta), theta^2=eta.
def kadd(x, y):
    return (fadd(x[0], y[0]), fadd(x[1], y[1]))


def kmul(x, y):
    a, b = x
    d, e = y
    return (
        fadd(c.fmul(a, d, f), c.fmul(c.fmul(b, e, f), eta, f)),
        fadd(c.fmul(a, e, f), c.fmul(b, d, f)),
    )


def kpow(x, n):
    out = (ONE, ZERO)
    base = x
    while n:
        if n & 1:
            out = kmul(out, base)
        base = kmul(base, base)
        n >>= 1
    return out


theta = (ZERO, ONE)
k_one = (ONE, ZERO)
k_minus_one = (minus_one, ZERO)
assert kmul(theta, theta) == (eta, ZERO)
assert kpow(theta, 512) == k_one
assert kpow(theta, 256) == k_minus_one
H = [kpow(theta, i) for i in range(512)]
assert len(set(H)) == 512
D_even = {(x, ZERO) for x in D0}
assert set(H[0::2]) == D_even
odd_coset = set(H[1::2])
assert D_even.isdisjoint(odd_coset)
assert len(odd_coset) == 256
A = {kpow(theta, 2 * i + 1) for i in range(119)}
R = {kpow(theta, 2 * i + 1) for i in range(119, 256)}
assert len(A) == 119 and len(R) == 137
assert A.isdisjoint(R) and A.isdisjoint(D_even) and R.isdisjoint(D_even)
assert D_even | A | R == set(H)

# Generated-field degrees and the exact MCA denominator ledger.
def multiplicative_order_mod(a, m):
    x = 1
    for d in range(1, 10_000):
        x = (x * a) % m
        if x == 1:
            return d
    raise AssertionError('order search failed')

assert multiplicative_order_mod(17, 256) == 16
assert multiplicative_order_mod(17, 512) == 32
q = P**32
Nbad = 52_747_567_092
assert q // 2**128 == 6
assert Nbad > 6
assert Nbad * 2**128 > q
assert 143 + 119 == 262
assert 137 + 119 == 256
assert 1 - 262 / 512 == 125 / 256

print(json.dumps({
    'decision': 'CYCLE116_BRIDGE_AND_SMOOTH_LIFT_FINITE_CLAUSES_VERIFIED',
    'cycle84': {
        'm_max': 2,
        'occupancy': Nbad,
        'ordered_offdiagonal_energy': 24,
        'double_fibers': 12,
    },
    'native': {
        'field_size': q0,
        'eta_order': 256,
        'eta_nonsquare': True,
        'beta_outside_D0': True,
        'slot_structural_checks': slot_checks,
        'fixed_jet': 'X^113-X^112+O(X^107)',
        'kappa_coefficients': list(kappa),
    },
    'lift': {
        'field_size': q,
        'theta_order': 512,
        'H_size': 512,
        'A_size': 119,
        'R_size': 137,
        'dimension': 256,
        'agreement': 262,
        'delta': '125/256',
    },
    'ledger': {
        'floor_17pow32_over_2pow128': q // 2**128,
        'bad_numerator': Nbad,
        'strictly_above_2powminus128': True,
        'q_gen': q,
        'q_code': q,
        'q_line': q,
        'q_chal': 'not used by the finite MCA theorem',
    },
}, indent=2, sort_keys=True))
