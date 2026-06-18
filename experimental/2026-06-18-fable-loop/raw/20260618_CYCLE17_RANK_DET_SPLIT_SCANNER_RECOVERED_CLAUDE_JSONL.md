I have everything I need. Both file-writing and code-execution are disabled in this harness (Write denied, MCP execute denied, no Bash tool), so per the prompt's fallback I'll provide the full script text plus the companion certificate/audit content inline. I have not executed the scanner, so I report no scan numbers as results — the deliverable is the checker itself (classification AUDIT); running it yields EXPERIMENTAL data.

The scanner reuses the mounted stack (`cycle11 → cycle12_t2_j3 → cycle12_base_component_rank → cycle15_forced_ra`) and adds only the Cycle 14/15 column layer and the direct `Q`-determinant test. It does not use the Cycle 16 trace/Gram criterion (kept AUDIT); it tests `Q≡0` by direct evaluation of `det₄ₓ₄[c1|c2|c3|c0]` over all of `B²`, which is sound because each matrix entry is `B`-affine in `(z₀,z₁)` so `deg Q ≤ 4 < p`.

## Deliverable 1 — `output_files/rank_det_split_scanner.py`

```python
#!/usr/bin/env python3
"""Cycle 17 scanner for W-F1-AA-RES-T2J3-RANK-DET-SPLIT.

Status: AUDIT (checker implementation / spec). Any number this script prints is
EXPERIMENTAL finite-sample evidence, never a theorem.

Cycle 16 banked the safe side: off R0, if the Cycle 15 determinant consistency
polynomial Q(z_0,z_1) is NOT identically zero, every landing slope lies on the
nonzero degree-<=4 plane curve {Q=0}, so C2 <= 4p = O(p) = O(n). The residual
live wall is the Q==0 branch with the distinct D-split cubic condition retained.
This scanner isolates that branch and counts the slope image of distinct
D-split co-supports T subset F_p, |T|=3.

Ledger (never merged):
    B = F_p,     q_gen  = p        F = F_{p^2}, q_line = p^2     q_chal unused.
    D = F_p, n = p.  t = sigma = 2,  j = n-a = 3,  a = n-3, k = n-5.
    eta = 2/n (sub-reserve).   Work off R0 = { wedge([W]_E,[Bnum]_E) = 0 }.

Reuse, not reinvention. Imports the audited finite-field stack:
    20260618_cycle11_t2_j2_line_incidence_verify.py   (B, F=F_{p^2}, polys, residues)
    20260618_cycle12_t2_j3_line_incidence_scan.py     (Q_S closed form, e_i)
    20260618_cycle12_base_component_rank_scan.py      (Delta, coeff-line rank, solver)
    20260618_cycle15_forced_ra_slope_scan.py          (forced-Ra W nullspace)

Q test (NO trace/Gram shortcut). The Cycle 16 trace / conjugate-skew Gram
criterion is AUDIT-only and is NOT used here. We build the four B-linear columns
c1,c2,c3,c0 in A = F[X]/E ~= B^4, form the 4x4 determinant Q(z_0,z_1) over B, and
evaluate at every (z_0,z_1) in B^2. Each entry is B-affine in (z_0,z_1), so
deg Q <= 4 < p for p >= 7; vanishing at all p^2 points is therefore a sound
identically-zero test, and a bivariate fit recovers deg Q for the certificate.

Self-checks (any failure => status HARNESS_OR_SOURCE_GAP):
  * Delta (reused) == wedge(iota, mu) of the column pipeline.
  * iota, mu affine in (tau1,tau2) with tau3-coefficient exactly -[W]_E, -b.
  * every brute-force landing slope z satisfies Q(z)=0 AND
    tau1 c1(z)+tau2 c2(z)+tau3 c3(z)+c0(z) = 0 in A.
  * when Q is NOT identically zero, C2 <= 4p (Cycle 16 bound) holds.

Counterpacket trigger (family level only): Q==0 AND C2/p^2 bounded below across
a growing-p family. A single prime is EXPERIMENTAL only.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from itertools import combinations
from pathlib import Path
import random

# --------------------------------------------------------------------------
# Locate and load the mounted finite-field / model stack.
# --------------------------------------------------------------------------
def _find_local_checks(explicit):
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    env = os.environ.get("RS_MCA_LOCAL_CHECKS")
    if env:
        candidates.append(Path(env))
    here = Path(__file__).resolve()
    rel = Path("current_loop_20260618") / "2026-06-18-fable-loop" / "local_checks"
    for parent in [here.parent] + list(here.parents):
        candidates.append(parent / "input_project" / rel)
        candidates.append(parent / rel)
    needed = "20260618_cycle15_forced_ra_slope_scan.py"
    for cand in candidates:
        try:
            if (cand / needed).is_file():
                return cand.resolve()
        except OSError:
            continue
    raise SystemExit(
        f"Could not locate local_checks dir containing {needed}. "
        "Pass --local-checks-dir or set RS_MCA_LOCAL_CHECKS."
    )

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

def load_stack(local_checks):
    """Load cycle15 (which transitively loads cycle12_rank/cycle12/cycle11) and
    reuse the SAME module instances so there is exactly one shared field state."""
    c15 = _load("cycle15_forced_ra",
                local_checks / "20260618_cycle15_forced_ra_slope_scan.py")
    return c15, c15.c12r, c15.c12, c15.c11

# --------------------------------------------------------------------------
# Determinant over F_p (B) for the 4x4 consistency matrix.
# --------------------------------------------------------------------------
def det_mod_p(matrix, p):
    n = len(matrix)
    a = [[v % p for v in row] for row in matrix]
    det = 1
    for col in range(n):
        piv = None
        for r in range(col, n):
            if a[r][col] % p:
                piv = r
                break
        if piv is None:
            return 0
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            det = (-det) % p
        inv = pow(a[col][col], p - 2, p)
        det = (det * a[col][col]) % p
        for r in range(col + 1, n):
            f = (a[r][col] * inv) % p
            if f:
                a[r] = [(a[r][k] - f * a[col][k]) % p for k in range(n)]
    return det % p

# --------------------------------------------------------------------------
# Cycle-17 layer, bound to one (c11,c12,c12r) instance.
# --------------------------------------------------------------------------
class SplitScanner:
    def __init__(self, c11, c12, c12r):
        self.c11, self.c12, self.c12r = c11, c12, c12r

    # A = F[X]/E, element = (R0, R1) with R_i in F.
    def a_scale(self, e, s):
        c = self.c11
        return (c.fmul(s, e[0]), c.fmul(s, e[1]))

    def a_add(self, u, v):
        c = self.c11
        return (c.fadd(u[0], v[0]), c.fadd(u[1], v[1]))

    def a_sub(self, u, v):
        c = self.c11
        return (c.fsub(u[0], v[0]), c.fsub(u[1], v[1]))

    def a_is_zero(self, e):
        return e[0] == self.c11.zero and e[1] == self.c11.zero

    def a_to_b4(self, e):
        (r0re, r0im), (r1re, r1im) = e[0], e[1]
        p = self.c11.P
        return [r0re % p, r0im % p, r1re % p, r1im % p]

    def expand_in_WB(self, elt, Wres, Bres):
        """Solve elt = p1*[W]_E + p2*b over F (unique off R0)."""
        c = self.c11
        a, b_ = Wres[0], Bres[0]
        cc, d = Wres[1], Bres[1]
        det = c.fsub(c.fmul(a, d), c.fmul(b_, cc))   # = wedge([W]_E, b)
        if det == c.zero:
            return None
        di = c.finv(det)
        p1 = c.fmul(c.fsub(c.fmul(d, elt[0]), c.fmul(b_, elt[1])), di)
        p2 = c.fmul(c.fsub(c.fmul(a, elt[1]), c.fmul(cc, elt[0])), di)
        return p1, p2

    def iota_mu(self, Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, t3):
        """iota = [W]_E[L_T]_E - [L_D]_E[Q_S]_E ; mu = [Bnum]_E[L_T]_E.
        Identical to the reused delta_for_tau pre-wedge factors."""
        c, c12 = self.c11, self.c12
        LT = c.trim([c.fneg(t3), t2, c.fneg(t1), c.one])
        Q = c12.q_formula_j3(W, n, D1, D2, t1, t2)
        LTres = c.residue2(LT, E)
        Qres = c.residue2(Q, E)
        iota = c.rsub(c.rmul(Wres, LTres, E), c.rmul(LDres, Qres, E))
        mu = c.rmul(Bres, LTres, E)
        return iota, mu

    def affine_pq(self, Wres, LDres, Bres, E, W, D1, D2, n):
        """Coeffs of p1,p2,q1,q2 (affine in tau1,tau2) for A0=p1[W]+p2 b,
        B0=q1[W]+q2 b. Verifies Cycle 14 affine structure + tau3 coefficients."""
        c = self.c11

        def A0B0(t1, t2):
            return self.iota_mu(Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, c.zero)

        b0, b1 = c.b(0), c.b(1)
        A00, B00 = A0B0(b0, b0)
        A10, B10 = A0B0(b1, b0)
        A01, B01 = A0B0(b0, b1)
        pA00 = self.expand_in_WB(A00, Wres, Bres)
        pA10 = self.expand_in_WB(A10, Wres, Bres)
        pA01 = self.expand_in_WB(A01, Wres, Bres)
        qB00 = self.expand_in_WB(B00, Wres, Bres)
        qB10 = self.expand_in_WB(B10, Wres, Bres)
        qB01 = self.expand_in_WB(B01, Wres, Bres)
        if None in (pA00, pA10, pA01, qB00, qB10, qB01):
            return None  # on R0

        p1c, p2c = pA00
        q1c, q2c = qB00
        coeffs = {
            "p1": (p1c, c.fsub(pA10[0], p1c), c.fsub(pA01[0], p1c)),
            "p2": (p2c, c.fsub(pA10[1], p2c), c.fsub(pA01[1], p2c)),
            "q1": (q1c, c.fsub(qB10[0], q1c), c.fsub(qB01[0], q1c)),
            "q2": (q2c, c.fsub(qB10[1], q2c), c.fsub(qB01[1], q2c)),
        }

        def lin(co, x, y):
            return c.fadd(c.fadd(co[0], c.fmul(co[1], x)), c.fmul(co[2], y))

        rng = random.Random(0xA0B0)
        for _ in range(6):
            t1, t2, t3 = (c.b(rng.randrange(c.P)) for _ in range(3))
            iota, mu = self.iota_mu(Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, t3)
            A0, B0 = A0B0(t1, t2)
            A0r = self.a_add(self.a_scale(Wres, lin(coeffs["p1"], t1, t2)),
                             self.a_scale(Bres, lin(coeffs["p2"], t1, t2)))
            B0r = self.a_add(self.a_scale(Wres, lin(coeffs["q1"], t1, t2)),
                             self.a_scale(Bres, lin(coeffs["q2"], t1, t2)))
            if A0r != A0 or B0r != B0:
                raise AssertionError("Cycle14 affine A0/B0 expansion failed")
            if iota != self.a_sub(A0, self.a_scale(Wres, t3)):
                raise AssertionError("iota tau3-coefficient != -[W]_E")
            if mu != self.a_sub(B0, self.a_scale(Bres, t3)):
                raise AssertionError("mu tau3-coefficient != -b")
        return coeffs

    def columns_at(self, coeffs, z, Wres, Bres):
        """(c1,c2,c3,c0) as A-elements at slope z=(z0,z1) in F (Cycle 15)."""
        c = self.c11

        def col(idx):
            u = c.fsub(coeffs["p1"][idx], c.fmul(z, coeffs["q1"][idx]))
            v = c.fsub(coeffs["p2"][idx], c.fmul(z, coeffs["q2"][idx]))
            return (c.fadd(c.fmul(u, Wres[0]), c.fmul(v, Bres[0])),
                    c.fadd(c.fmul(u, Wres[1]), c.fmul(v, Bres[1])))

        c1, c2, c0 = col(1), col(2), col(0)
        neg = c.fneg(c.one)
        c3 = (c.fadd(c.fmul(neg, Wres[0]), c.fmul(z, Bres[0])),
              c.fadd(c.fmul(neg, Wres[1]), c.fmul(z, Bres[1])))
        return c1, c2, c3, c0

    def Q_at(self, coeffs, z, Wres, Bres):
        c1, c2, c3, c0 = self.columns_at(coeffs, z, Wres, Bres)
        cols = [self.a_to_b4(c1), self.a_to_b4(c2),
                self.a_to_b4(c3), self.a_to_b4(c0)]
        mat = [[cols[j][i] for j in range(4)] for i in range(4)]
        return det_mod_p(mat, self.c11.P)

    def Q_grid(self, coeffs, Wres, Bres):
        p = self.c11.P
        return {(z0, z1): self.Q_at(coeffs, (z0, z1), Wres, Bres)
                for z0 in range(p) for z1 in range(p)}

    def fit_degQ(self, grid, p):
        """Fit Q as a total-degree-<=4 bivariate poly; return its degree
        (-1 if identically zero) using the reused solver."""
        monos = [(i, d - i) for d in range(5) for i in range(d + 1)]
        rows, rhs = [], []
        for (z0, z1), val in grid.items():
            rows.append([(pow(z0, i, p) * pow(z1, j, p)) % p for (i, j) in monos])
            rhs.append(val % p)
        try:
            sol = self.c12r.solve_mod_p(rows, rhs, p)
        except AssertionError:
            return None
        deg = -1
        for (i, j), cf in zip(monos, sol):
            if cf % p:
                deg = max(deg, i + j)
        return deg

    def case_landings(self, p, nr, E, bnum, W, coeffs, Q_is_zero):
        c, c12, c12r = self.c11, self.c12, self.c12r
        D = [c.b(x) for x in range(p)]
        n = len(D)
        LD = c.locator(D)
        D1, D2 = c12.sum_points(D), c12.elem2(D)
        Wres = c.residue2(W, E)
        LDres = c.residue2(LD, E)
        Bres = c.residue2(bnum, E)

        slopes = {}
        split_landings = 0
        examined = 0
        for idxs in combinations(range(n), 3):   # each = a distinct D-split cubic
            examined += 1
            T = [D[i] for i in idxs]
            t1, t2, t3 = c12.sum_points(T), c12.elem2(T), c12.elem3(T)
            delta = c12r.delta_for_tau(Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, t3)
            iota, mu = self.iota_mu(Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, t3)
            if c.wedge(iota, mu) != delta:
                raise AssertionError("Delta != wedge(iota,mu): pipeline mismatch")
            if delta != c.zero:
                continue
            split_landings += 1
            LT = c.locator(T)
            Ls, rem = c.pdivmod(LD, LT)
            if rem != [c.zero]:
                raise AssertionError("L_T did not divide L_D")
            _, Is = c.pdivmod(W, Ls)
            z = c.line_scalar(c.residue2(Is, E), Bres)
            if z is None:
                raise AssertionError("Delta=0 but direct slope test failed")
            c1, c2, c3, c0 = self.columns_at(coeffs, z, Wres, Bres)
            lhs = self.a_add(self.a_add(self.a_scale(c1, t1), self.a_scale(c2, t2)),
                             self.a_add(self.a_scale(c3, t3), c0))
            if not self.a_is_zero(lhs):
                raise AssertionError("tau(T) does not solve L_z(tau)=0")
            if self.Q_at(coeffs, z, Wres, Bres) % p != 0:
                raise AssertionError("landing slope has Q(z)!=0")
            slopes[z] = slopes.get(z, 0) + 1

        if not Q_is_zero and len(slopes) > 4 * p:
            raise AssertionError("Q!=0 but C2 > 4p violates Cycle 16")
        return slopes, split_landings, examined

# --------------------------------------------------------------------------
# Helpers.
# --------------------------------------------------------------------------
def smallest_nonresidue(p):
    for nr in range(2, p):
        if pow(nr, (p - 1) // 2, p) == p - 1:
            return nr
    raise ValueError(f"no non-residue mod {p}")

def histogram_summary(fiber_sizes):
    h = {}
    for s in fiber_sizes:
        h[s] = h.get(s, 0) + 1
    return {str(k): h[k] for k in sorted(h)}

def _fmt_poly(c11, poly):
    return [[v % c11.P for v in coeff] for coeff in c11.trim(poly)]

# --------------------------------------------------------------------------
# Certificate builder.
# --------------------------------------------------------------------------
def build_certificate(stack, scanner, p, nr, seed, E, bnum, W,
                      stratum, direction, kernel_dim):
    c15, c12r, c12, c11 = stack
    D = [c11.b(x) for x in range(p)]
    n = len(D)
    LD = c11.locator(D)
    D1, D2 = c12.sum_points(D), c12.elem2(D)
    Wres = c11.residue2(W, E)
    LDres = c11.residue2(LD, E)
    Bres = c11.residue2(bnum, E)
    triples = n * (n - 1) * (n - 2) // 6

    off_R0 = (c11.wedge(Wres, Bres) != c11.zero)
    coeff_rank = c12r.coefficient_line_rank(c15.coeff_pairs_for_W(W, E, bnum, D), p)

    base = {
        "p": p, "q_gen": p, "q_line": p * p, "seed": seed,
        "E": _fmt_poly(c11, E), "Bnum": _fmt_poly(c11, bnum),
        "stratum": stratum + ("" if direction is None else f"|dir={direction}"),
        "off_R0": off_R0, "coeff_line_rank": coeff_rank,
        "direction": direction, "kernel_dim": kernel_dim,
        "split_triples_examined": triples,
    }

    if not off_R0:
        # R0 = global/tangent endpoint; the Cycle 14/15 reduction is stated
        # off R0. Mark applicability and exclude from the Q==0 family (C2=None).
        base.update({
            "stratum": base["stratum"] + "|on_R0",
            "Q_identically_zero": None, "degQ_or_test": "skipped_on_R0",
            "split_landings": None, "C2": None, "max_slope_fiber": None,
            "fiber_histogram_summary": {}, "note": "on_R0_outside_wall",
            "status": "PASS_QNONZERO_OP",
        })
        return base

    try:
        coeffs = scanner.affine_pq(Wres, LDres, Bres, E, W, D1, D2, n)
        if coeffs is None:
            raise AssertionError("affine_pq returned None off R0")
        grid = scanner.Q_grid(coeffs, Wres, Bres)
        Q_zero = all(v % p == 0 for v in grid.values())
        degQ = scanner.fit_degQ(grid, p)
        slopes, split_landings, _ = scanner.case_landings(
            p, nr, E, bnum, W, coeffs, Q_zero)
        c2 = len(slopes)
        base.update({
            "Q_identically_zero": Q_zero,
            "degQ_or_test": "Q_grid_all_zero" if Q_zero else f"degQ={degQ}",
            "split_landings": split_landings, "C2": c2,
            "max_slope_fiber": max(slopes.values()) if slopes else 0,
            "fiber_histogram_summary": histogram_summary(list(slopes.values())),
            "status": "OPEN_QZERO_SMALL_SAMPLE" if Q_zero else "PASS_QNONZERO_OP",
        })
    except AssertionError as exc:
        base.update({
            "Q_identically_zero": None, "degQ_or_test": "ERROR",
            "split_landings": None, "C2": None, "max_slope_fiber": None,
            "fiber_histogram_summary": {}, "error": str(exc),
            "status": "HARNESS_OR_SOURCE_GAP",
        })
    return base

# --------------------------------------------------------------------------
# Case runners.
# --------------------------------------------------------------------------
def run_forced_ra_case(stack, scanner, p, nr, seed, samples_per_direction):
    c15, c12r, c12, c11 = stack
    c11.set_field(p, nr)
    rng = random.Random(seed)
    E = c11.random_separated_quadratic(rng)
    bnum = c11.random_bnum(rng)
    if c11.residue2(bnum, E) == (c11.zero, c11.zero):
        raise AssertionError("zero bnum residue")
    directions = [(1, s) for s in range(p)] + [(0, 1)]
    certs = []
    for direction in directions:
        basis = c15.forced_line_nullspace(p, nr, E, bnum, direction)
        if not basis:
            continue
        for _ in range(samples_per_direction):
            W = c15.vec_to_W(c15.random_from_basis(basis, p, rng))
            if W == [c11.zero]:
                continue
            certs.append(build_certificate(
                stack, scanner, p, nr, seed, E, bnum, W,
                stratum="Ra_forced", direction=direction, kernel_dim=len(basis)))
    return certs

def run_random_case(stack, scanner, p, nr, seed):
    c15, c12r, c12, c11 = stack
    c11.set_field(p, nr)
    rng = random.Random(seed ^ 0x5151)
    D = [c11.b(x) for x in range(p)]
    n = len(D)
    E = c11.random_separated_quadratic(rng)
    bnum = c11.random_bnum(rng)
    w0 = [c11.b(rng.randrange(p)) for _ in D]
    w1 = [c11.b(rng.randrange(p)) for _ in D]
    w = [c11.fadd(w0[i], c11.fmul(c11.alpha, w1[i])) for i in range(n)]
    W = c11.interp(D, w)
    return [build_certificate(stack, scanner, p, nr, seed, E, bnum, W,
                              stratum="generic_random", direction=None,
                              kernel_dim=None)]

# --------------------------------------------------------------------------
# Family aggregation + counterpacket trigger.
# --------------------------------------------------------------------------
def family_summary(certs, c2_over_p2_floor):
    qzero = [c for c in certs
             if c.get("Q_identically_zero") is True and c.get("C2") is not None]
    primes_qzero = sorted({c["p"] for c in qzero})
    ratios = {}
    for c in qzero:
        ratios.setdefault(c["p"], []).append(c["C2"] / (c["p"] ** 2))
    per_prime_max = {p: max(rs) for p, rs in ratios.items()}
    growing = len(primes_qzero) >= 3
    bounded_below = growing and all(per_prime_max[p] >= c2_over_p2_floor
                                    for p in primes_qzero)
    any_gap = any(c.get("status") == "HARNESS_OR_SOURCE_GAP" or "error" in c
                  for c in certs)
    return {
        "primes_scanned": sorted({c["p"] for c in certs}),
        "cases_total": len(certs),
        "cases_off_R0": sum(1 for c in certs if c.get("off_R0")),
        "cases_Q_identically_zero": len(qzero),
        "primes_with_Q_zero": primes_qzero,
        "max_C2_over_p2_per_prime": {str(p): round(v, 5)
                                     for p, v in per_prime_max.items()},
        "max_C2_observed": max((c["C2"] for c in certs
                                if c.get("C2") is not None), default=None),
        "counterpacket_trigger_met": bool(bounded_below),
        "harness_or_source_gap_seen": bool(any_gap),
    }

def overall_status(summary):
    if summary["harness_or_source_gap_seen"]:
        return "HARNESS_OR_SOURCE_GAP"
    if summary["counterpacket_trigger_met"]:
        return "COUNTERPACKET_C2_GROWTH_CANDIDATE"
    if summary["cases_Q_identically_zero"] > 0:
        return "OPEN_QZERO_SMALL_SAMPLE"
    return "PASS_QNONZERO_OP"

# --------------------------------------------------------------------------
# CLI.
# --------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description="Cycle 17 Q==0 split-distinct scanner")
    ap.add_argument("--local-checks-dir", default=None)
    ap.add_argument("--primes", default="7,11,13")
    ap.add_argument("--seeds", type=int, default=4)
    ap.add_argument("--samples-per-direction", type=int, default=2)
    ap.add_argument("--mode", choices=["forced_ra", "random", "both"],
                    default="forced_ra")
    ap.add_argument("--c2-floor", type=float, default=0.10)
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--max-print", type=int, default=40)
    args = ap.parse_args(argv)

    stack = load_stack(_find_local_checks(args.local_checks_dir))
    c15, c12r, c12, c11 = stack
    scanner = SplitScanner(c11, c12, c12r)

    primes = [int(x) for x in args.primes.split(",") if x.strip()]
    for p in primes:
        if p < 7:
            raise SystemExit("p must be >= 7 (need deg Q <= 4 < p for the Q test)")

    certs = []
    for p in primes:
        nr = smallest_nonresidue(p)
        for seed in range(args.seeds):
            if args.mode in ("forced_ra", "both"):
                certs.extend(run_forced_ra_case(
                    stack, scanner, p, nr, seed, args.samples_per_direction))
            if args.mode in ("random", "both"):
                certs.extend(run_random_case(stack, scanner, p, nr, seed))

    summary = family_summary(certs, args.c2_floor)
    status = overall_status(summary)
    summary["overall_status"] = status

    for cert in certs[:args.max_print]:
        print("p={p} seed={seed} stratum={stratum} off_R0={off_R0} "
              "coeff_rank={coeff_line_rank} Qzero={Q_identically_zero} "
              "{degQ_or_test} split_landings={split_landings} C2={C2} "
              "max_fiber={max_slope_fiber} status={status}".format(**cert))

    print("-" * 72)
    print("FAMILY SUMMARY:", json.dumps(summary, sort_keys=True))
    print("OVERALL STATUS:", status)
    print("NOTE: finite-sample EXPERIMENTAL evidence; sub-reserve eta=2/n; "
          "no conj:B / q_gen / protocol claim.")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps({
            "scanner": "W-F1-AA-RES-T2J3-RANK-DET-SPLIT",
            "ledger": {"B": "F_p", "F": "F_{p^2}", "q_chal": "unused",
                       "D": "F_p", "t": 2, "sigma": 2, "j": 3, "eta": "2/n"},
            "params": {"primes": primes, "seeds": args.seeds,
                       "samples_per_direction": args.samples_per_direction,
                       "mode": args.mode, "c2_floor": args.c2_floor},
            "summary": summary, "certificates": certs,
        }, indent=2, sort_keys=True))
        print("wrote", args.json_out)

    return 2 if status == "HARNESS_OR_SOURCE_GAP" else 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Reproduce command (offline, where execution is allowed):

```bash
python3 output_files/rank_det_split_scanner.py \
  --primes 7,11,13,17 --seeds 6 --samples-per-direction 3 \
  --mode forced_ra --json-out output_files/RESULTS.json
```

## Deliverable 2 — `output_files/RESULT.md` (content)

```text
# Cycle 17 Result: W-F1-AA-RES-T2J3-RANK-DET-SPLIT Q==0 Scanner

Primary classification: AUDIT (checker implementation + spec).
Running the scanner produces EXPERIMENTAL finite-sample data only.

## What this delivers
- rank_det_split_scanner.py: extends the reused stack (cycle11 -> cycle12_t2_j3
  -> cycle12_base_component_rank -> cycle15_forced_ra) with the Cycle 14/15
  column layer c1,c2,c3,c0 in A=F[X]/E ~= B^4 and a DIRECT test of
  Q(z_0,z_1)=det_4x4[c1|c2|c3|c0] by evaluation over all of B^2.
- Isolates the Q==0 branch and, on it, counts distinct slopes from distinct
  D-split cubics T subset F_p, |T|=3, emitting per-case certificates.

## Why the Q test is sound (not the trace/Gram criterion)
Each matrix entry is B-affine in (z_0,z_1), so deg Q <= 4. For p >= 7,
deg Q < p, so Q vanishing at all p^2 points <=> Q identically zero. The Cycle 16
trace / conjugate-skew Gram criterion is NOT used; it remains AUDIT.

## Built-in identity checks (fail-loud, => HARNESS_OR_SOURCE_GAP)
1. Delta (reused) == wedge(iota, mu) from the column pipeline.
2. iota, mu affine in (tau1,tau2); tau3-coefficient exactly -[W]_E, -b (Cycle 14).
3. each brute-force landing slope z satisfies Q(z)=0 and
   tau1 c1+tau2 c2+tau3 c3+c0 = 0 in A.
4. Q!=0 => C2 <= 4p (Cycle 16 banked safe-side bound), checked every case.

## Certificate fields (per case)
p, q_gen, q_line, seed, E, Bnum, stratum, off_R0, coeff_line_rank,
Q_identically_zero, degQ_or_test, split_triples_examined, split_landings, C2,
max_slope_fiber, fiber_histogram_summary, direction, kernel_dim, status.

## Statuses
PASS_QNONZERO_OP | OPEN_QZERO_SMALL_SAMPLE |
COUNTERPACKET_C2_GROWTH_CANDIDATE | HARNESS_OR_SOURCE_GAP.

## Counterpacket trigger (family level only)
Q==0 AND min over a growing set (>=3) of primes of max(C2/p^2) >= c2_floor.
A single prime is EXPERIMENTAL only and can never trip the trigger.

## Ledger
B=F_p (q_gen=p); F=F_{p^2} (q_line=p^2); q_chal unused; D=F_p, n=p;
t=sigma=2, j=3, a=n-3, k=n-5; eta=2/n sub-reserve; off R0.

## Not claimed
No proof of conj:B; no corrected-reserve counterpacket (eta=2/n is
sub-reserve); no q_gen collapse; no protocol/MCA/CA/list-/line-decoding/SNARK
consequence; nothing from terminal/ad transcript text.

## Execution note
This deliverable was produced in a harness with file-write and code-execution
disabled, so NO scan numbers are reported as results here. Prior Cycle 15
forced-Ra smoke (p=7) recorded C2<=6, consistent with no counterpacket, and is
EXPERIMENTAL only.
```

## Deliverable 3 — `output_files/NEXT_PROMPT.md` (content)

```text
# Next Prompt (Cycle 18 candidate)

Run rank_det_split_scanner.py on a growing-p ladder (p=7,11,13,17,19,23) in an
environment where execution is enabled. Then:

1. If status stays OPEN_QZERO_SMALL_SAMPLE with max(C2/p^2) -> 0 as p grows:
   pursue BANKABLE_LEMMA "split-distinct collapse on Q==0", i.e. prove that on
   the Q==0 branch the distinct-D-split-cubic locus forces C2=O(p). Candidate
   invariant: relate split landings to the line ell_z fiber in (tau1,tau2,tau3).
2. If COUNTERPACKET_C2_GROWTH_CANDIDATE fires (C2/p^2 bounded below over >=3
   primes): promote to a symbolic family; remember it is sub-reserve (eta=2/n)
   and is NOT a corrected-reserve refutation.
3. Independently re-derive the Cycle 16 trace/Gram criterion for Q==0 and add it
   as a SECOND Q-test path; keep AUDIT until it agrees with the direct
   det-evaluation test across the whole ladder.
4. Also exercise --mode random to confirm generic anchors are Q!=0
   (PASS_QNONZERO_OP) and that the Cycle 16 C2<=4p assertion never trips.

Secondary: W-F1-AA-RES-T3J2 (deg E=t=3, j=2, codimension-two bad line).
```

## Classification

The deliverable is a checker implementation plus spec; I could not execute it in this harness, so I report no finite outcomes as results. The scanner targets the literal wall `W-F1-AA-RES-T2J3-RANK-DET-SPLIT`, reuses the mounted stack, tests `Q≡0` directly (not via the AUDIT-only trace/Gram criterion), retains the distinct-split-cubic condition, embeds fail-loud cross-checks of the banked Cycle 13/14/16 identities, and decides the counterpacket trigger only at the growing-`p` family level. No `conj:B`, corrected-reserve, `q_gen`, or protocol claims are made; `eta=2/n` remains sub-reserve.

```text
AUDIT
```
