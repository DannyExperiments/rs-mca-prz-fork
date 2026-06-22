#!/usr/bin/env python3
"""Deterministic verifier for the Cycle84 exact m_max=2 certificate.

This verifies the finite-field/log/tau chain, the emitted projected-census
certificate, the kernel-3 lift, and all 30 lifted pairs directly in F_{17^16}.
It does not rerun the 26.37-billion-entry census; use src/tau_fold_full_optimized.cpp
for that reproducible exact run.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODEL = ROOT / "model" / "cycle68_slot_factorization_checker.py"
spec = importlib.util.spec_from_file_location("cycle68", MODEL)
c = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(c)

P0 = 52_747_567_104
N = 17**16 - 1
FACTORS = {2: 8, 3: 2, 5: 1, 29: 1, 18913: 1, 41761: 1, 184417: 1}
M = N // 3
KAPPA = 15_337_197_211_725_320_908
S0 = 7_668_598_605_862_660_454
S1 = 15_778_797_251_807_138_534

slot_path = ROOT / "data" / "slot_logs.json"
D = json.loads(slot_path.read_text())
assert D["N"] == N
assert {int(k): v for k, v in D["factors"].items()} == FACTORS
assert D["generator"] == [2, 1]
assert len(D["records"]) == 336

f = c.find_field_poly()
eta = c.find_eta(f)
beta = c.find_beta(f)
table = c.build_u(f, eta, beta)
assert f == (3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
assert eta == (0, 0, 0, 0, 0, 0, 0, 0, 0, 6)
assert beta == (2, 1)
assert all(c.fpow(beta, N // p, f) != c.ONE for p in FACTORS)

logs = [[None] * 48 for _ in range(7)]
logsN = [[None] * 48 for _ in range(7)]
colors = [[None] * 48 for _ in range(7)]
seen = set()
for r in D["records"]:
    t, i, a = r["t"], r["i"], r["a"]
    key = (t, i, a)
    assert key not in seen
    seen.add(key)
    k = (i - 1) * 16 + a
    x = int(r["log"])
    assert 0 <= x < N
    assert c.fpow(beta, x, f) == table[key]
    col = (c.S_COLOR[i] + 8 * (a & 1)) % 16
    assert r["color"] == col
    logs[t - 1][k] = x % M
    logsN[t - 1][k] = x
    colors[t - 1][k] = col
assert len(seen) == 336

def tauk(k: int) -> int:
    i, a = k // 16 + 1, k % 16
    if i == 1:
        return 16 + (a + 6) % 16
    if i == 2:
        return (a + 10) % 16
    return 32 + (a + 8) % 16

slot_constants = []
for t in range(7):
    vals = set()
    for k in range(48):
        assert tauk(tauk(k)) == k and tauk(k) != k
        assert (colors[t][k] + colors[t][tauk(k)]) % 16 == 8
        vals.add((logs[t][k] + logs[t][tauk(k)]) % M)
    assert len(vals) == 1
    slot_constants.append(vals.pop())
assert sum(slot_constants) % M == KAPPA
assert (2 * S0 - KAPPA) % M == 0
assert (2 * S1 - KAPPA) % M == 0
H = [k for k in range(48) if k < tauk(k)]
assert len(H) == 24

# Verify C++ headers exactly reproduce the certified JSON tables.
hm = (ROOT / "src" / "logsM.hpp").read_text()
block = hm.split("static constexpr uint64_t LOGS[7][48]={", 1)[1].split("};", 1)[0]
header_logs = [int(x) for x in re.findall(r"(\d+)ULL", block)]
cblock = hm.split("static constexpr uint8_t COLORS[7][48]={", 1)[1].split("};", 1)[0]
header_colors = [int(x) for x in re.findall(r"\d+", cblock)]
assert header_logs == sum(logs, [])
assert header_colors == sum(colors, [])
assert int(re.search(r"MOD=(\d+)ULL", hm).group(1)) == M

hn = (ROOT / "src" / "logsN.hpp").read_text()
hib = hn.split("static constexpr uint64_t LOGN_HI[7][48]={", 1)[1].split("};", 1)[0]
lob = hn.split("static constexpr uint64_t LOGN_LO[7][48]={", 1)[1].split("};", 1)[0]
his = [int(x) for x in re.findall(r"(\d+)ULL", hib)]
los = [int(x) for x in re.findall(r"(\d+)ULL", lob)]
reconstructed = [(hi << 64) | lo for hi, lo in zip(his, los)]
assert reconstructed == sum(logsN, [])

scan = json.loads((ROOT / "output" / "tau_opt.out").read_text())
assert scan["decision"] == "TAU_FOLDED_PROJECTED_MMAX_LE_12"
assert scan["projection_modulus"] == M and scan["kernel_order"] == 3
assert scan["kappa"] == KAPPA and scan["fixed_roots"] == [S0, S1]
assert scan["fixed_selected_counts"] == [0, 0]
assert scan["tau_half_domain_expected"] == scan["tau_half_domain_counted"] == P0 // 2
assert scan["folded_ordered_energy"] == 60
assert scan["projected_ordered_energy"] == 120
assert scan["max_canonical_projected_multiplicity"] == 2
assert scan["full_projected_max_including_fixed"] == 2
assert len(scan["duplicate_canonical_bins"]) == 30
assert len({x["key"] for x in scan["duplicate_canonical_bins"]}) == 30
assert all(x["count"] == 2 for x in scan["duplicate_canonical_bins"])
assert sum(x["count"] * (x["count"] - 1) for x in scan["duplicate_canonical_bins"]) == 60
scan_keys = [x["key"] for x in scan["duplicate_canonical_bins"]]

lift = json.loads((ROOT / "output" / "tau_lift.out").read_text())
assert lift["decision"] == "KERNEL_3_DUPLICATE_LIFT_COMPLETE"
assert lift["projection_modulus"] == M
assert lift["projection_duplicate_orbits_checked"] == 30
assert lift["candidate_base_targets"] == 138_240
assert lift["oriented_five_slot_tuples_scanned"] == 127_401_984
assert lift["selected_witnesses_recovered"] == 60
assert [x["canonical_key"] for x in lift["lifts"]] == scan_keys

def color_sum(T):
    return sum(colors[t][k] for t, k in enumerate(T)) % 16

def projected_sum(T):
    return sum(logs[t][k] for t, k in enumerate(T)) % M

def full_log_sum(T):
    return sum(logsN[t][k] for t, k in enumerate(T)) % N

def field_product(T):
    z = c.ONE
    for t, k in enumerate(T, 1):
        z = c.fmul(z, table[(t, k // 16 + 1, k % 16)], f)
    return z

def tau(T):
    return [tauk(k) for k in T]

true_orbits = 0
true_tuples = []
for rec in lift["lifts"]:
    r = rec["canonical_key"]
    W = rec["witnesses"]
    assert len(W) == 2
    products = []
    normalized_logs = []
    for w in W:
        T = w["selected_tuple"]
        U = w["normalized_tuple"]
        assert len(T) == len(U) == 7
        assert all(0 <= k < 48 for k in T + U)
        assert color_sum(T) == color_sum(U) == 4
        side = w["selected_side"]
        assert side in (0, 1)
        assert U == (T if side == 0 else tau(T))
        assert min((projected_sum(T) - S0) % M, (S0 - projected_sum(T)) % M) == r
        assert projected_sum(U) == (S0 + r) % M
        flog = full_log_sum(U)
        assert int(w["normalized_full_log"]) == flog
        normalized_logs.append(flog)
        products.append(field_product(U))
    assert W[0]["normalized_tuple"] != W[1]["normalized_tuple"]
    diff = (normalized_logs[0] - normalized_logs[1]) % N
    assert diff % M == 0
    q = diff // M
    assert q == rec["kernel_difference"] and q in (0, 1, 2)
    is_collision = products[0] == products[1]
    assert is_collision == rec["true_collision"] == (q == 0)
    if is_collision:
        true_orbits += 1
        A, B = W[0]["normalized_tuple"], W[1]["normalized_tuple"]
        true_tuples.extend([tuple(A), tuple(B), tuple(tau(A)), tuple(tau(B))])

assert true_orbits == 6
assert len(true_tuples) == len(set(true_tuples)) == 24
true_double_fibers = 2 * true_orbits
true_D = 2 * true_double_fibers
m_max = 2 if true_orbits else 1
occupancy = P0 - true_double_fibers
assert lift["true_collision_tau_orbits"] == true_orbits
assert lift["true_double_fibers"] == true_double_fibers == 12
assert lift["exact_true_ordered_offdiagonal_energy"] == true_D == 24
assert lift["exact_true_m_max"] == m_max == 2
assert lift["exact_true_occupancy"] == occupancy == 52_747_567_092

result = {
    "decision": "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED",
    "slot_value_log_checks": 336,
    "projected_max_multiplicity": 2,
    "projected_ordered_offdiagonal_energy": 120,
    "true_collision_tau_orbits": true_orbits,
    "true_double_fibers": true_double_fibers,
    "exact_true_ordered_offdiagonal_energy": true_D,
    "exact_true_m_max": m_max,
    "exact_true_occupancy": occupancy,
    "slot_logs_sha256": hashlib.sha256(slot_path.read_bytes()).hexdigest(),
}
print(json.dumps(result, indent=2, sort_keys=True))
