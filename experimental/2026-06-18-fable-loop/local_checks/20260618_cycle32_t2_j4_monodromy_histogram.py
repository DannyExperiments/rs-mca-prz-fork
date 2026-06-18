#!/usr/bin/env python3
"""Cycle 32 finite histogram for the t=2, j=4 quartic map.

This is EXPERIMENTAL evidence only.  It implements the Cycle 29/30 affine
system

    (u - z b) * [L_tau]_E - ell * [Q_tau]_E = 0 in A = F[X]/E

over B=F_p, F=F_{p^2}, D=F_p, t=sigma=2, j=4.  For every z in F it solves
the resulting 4x4 B-linear system for tau=(tau_1,...,tau_4), forms

    L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,

and records the factorization type over B.  As a sanity check it also compares
the number of totally split distinct slopes with the older direct support
enumeration from Cycle 30.
"""

from collections import Counter
from itertools import combinations
import importlib.util
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
PREV = ROOT / "20260618_cycle11_t2_j2_line_incidence_verify.py"
spec = importlib.util.spec_from_file_location("cycle11", PREV)
c11 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c11)


def f_to_b2(x):
    return [x[0] % c11.P, x[1] % c11.P]


def residue_to_b4(r):
    return f_to_b2(r[0]) + f_to_b2(r[1])


def modinv_int(a, p):
    return pow(a % p, p - 2, p)


def solve_linear_mod(mat, rhs, p):
    """Solve mat*x=rhs over F_p; return None unless there is a unique solution."""
    n = len(rhs)
    aug = [[x % p for x in row] + [rhs[i] % p] for i, row in enumerate(mat)]
    pivots = []
    row = 0
    for col in range(n):
        pivot = None
        for r in range(row, n):
            if aug[r][col] % p:
                pivot = r
                break
        if pivot is None:
            continue
        aug[row], aug[pivot] = aug[pivot], aug[row]
        inv = modinv_int(aug[row][col], p)
        aug[row] = [(v * inv) % p for v in aug[row]]
        for r in range(n):
            if r != row and aug[r][col] % p:
                factor = aug[r][col] % p
                aug[r] = [(aug[r][c] - factor * aug[row][c]) % p for c in range(n + 1)]
        pivots.append(col)
        row += 1
    if len(pivots) != n:
        return None
    return [aug[i][-1] % p for i in range(n)]


def poly_trim(poly, p):
    out = [x % p for x in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_eval(poly, x, p):
    out = 0
    for c in reversed(poly):
        out = (out * x + c) % p
    return out


def poly_div_linear(poly, root, p):
    """Divide by X-root, assuming divisibility."""
    coeffs = list(reversed(poly_trim(poly, p)))
    out = [coeffs[0]]
    for c in coeffs[1:-1]:
        out.append((c + root * out[-1]) % p)
    rem = (coeffs[-1] + root * out[-1]) % p
    if rem:
        raise AssertionError("linear division remainder is nonzero")
    return poly_trim(list(reversed(out)), p)


def poly_divmod_int(a, b, p):
    a = poly_trim(a, p)
    b = poly_trim(b, p)
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    r = a[:]
    inv_lc = modinv_int(b[-1], p)
    while len(r) >= len(b) and r != [0]:
        shift = len(r) - len(b)
        coef = r[-1] * inv_lc % p
        q[shift] = coef
        for i, bi in enumerate(b):
            r[i + shift] = (r[i + shift] - coef * bi) % p
        r = poly_trim(r, p)
    return poly_trim(q, p), r


def poly_gcd_int(a, b, p):
    a = poly_trim(a, p)
    b = poly_trim(b, p)
    while b != [0]:
        _, r = poly_divmod_int(a, b, p)
        a, b = b, r
    inv = modinv_int(a[-1], p)
    return [(x * inv) % p for x in a]


def factor_type_quartic(tau, p):
    """Return a string such as 1111, 211, 22, 31, 4, or nonsquarefree."""
    t1, t2, t3, t4 = [x % p for x in tau]
    poly = [t4, (-t3) % p, t2, (-t1) % p, 1]
    deriv = [(i * poly[i]) % p for i in range(1, len(poly))]
    if len(poly_gcd_int(poly, deriv, p)) > 1:
        return "nonsquarefree"

    degrees = []
    rem = poly[:]
    changed = True
    while changed:
        changed = False
        for r in range(p):
            if len(rem) > 1 and poly_eval(rem, r, p) == 0:
                degrees.append(1)
                rem = poly_div_linear(rem, r, p)
                changed = True
                break

    d = len(poly_trim(rem, p)) - 1
    if d == 0:
        pass
    elif d == 2:
        degrees.append(2)
    elif d == 3:
        degrees.append(3)
    elif d == 4:
        found_quad = False
        for a in range(p):
            for b in range(p):
                q = [b, a, 1]
                _, rr = poly_divmod_int(rem, q, p)
                if rr == [0]:
                    degrees.extend([2, 2])
                    found_quad = True
                    break
            if found_quad:
                break
        if not found_quad:
            degrees.append(4)
    else:
        raise AssertionError(f"unexpected remaining degree {d}")
    return "".join(str(x) for x in sorted(degrees))


def build_trial_data(p, nr, seed):
    c11.set_field(p, nr)
    rng = random.Random(seed)
    D = [c11.b(x) for x in range(p)]
    n = len(D)
    t = 2
    j = 4
    a = n - j
    k = a - t
    if k < 0:
        raise ValueError("p too small")

    E = c11.random_separated_quadratic(rng)
    bnum = c11.random_bnum(rng)
    bnum_res = c11.residue2(bnum, E)
    w0 = [c11.b(rng.randrange(p)) for _ in D]
    w1 = [c11.b(rng.randrange(p)) for _ in D]
    w = [c11.fadd(w0[i], c11.fmul(c11.alpha, w1[i])) for i in range(n)]
    W = c11.interp(D, w)
    LD = c11.locator(D)
    return D, E, bnum, bnum_res, W, LD, {"p": p, "nr": nr, "seed": seed, "n": n, "k": k, "a": a, "t": t, "sigma": 2, "j": j}


def direct_split_slopes(D, E, bnum_res, W, LD):
    slopes = set()
    landings = 0
    for idxs in combinations(range(len(D)), 4):
        T = [D[i] for i in idxs]
        LT = c11.locator(T)
        Ls, rem_l = c11.pdivmod(LD, LT)
        if rem_l != [c11.zero]:
            raise AssertionError("L_T did not divide L_D")
        _, Is = c11.pdivmod(W, Ls)
        z = c11.line_scalar(c11.residue2(Is, E), bnum_res)
        if z is not None:
            slopes.add(z)
            landings += 1
    return slopes, landings


def xtimes_power_residues(E, max_power=4):
    powers = []
    xpoly = [c11.zero, c11.one]
    cur = [c11.one]
    for _ in range(max_power + 1):
        powers.append(c11.residue2(cur, E))
        cur = c11.pmul(cur, xpoly)
    return powers


def q_residue_from_tau(W, E, tau):
    n = len(W) - 1
    tau1, tau2, tau3, _tau4 = [c11.b(x) for x in tau]
    Wn1 = c11.coeff(W, n)
    Wn2 = c11.coeff(W, n - 1)
    Wn3 = c11.coeff(W, n - 2)
    Wn4 = c11.coeff(W, n - 3)
    q3 = Wn1
    q2 = c11.fsub(Wn2, c11.fmul(Wn1, tau1))
    q1 = c11.fadd(c11.fsub(Wn3, c11.fmul(Wn2, tau1)), c11.fmul(Wn1, tau2))
    q0 = c11.fsub(c11.fadd(c11.fsub(Wn4, c11.fmul(Wn3, tau1)), c11.fmul(Wn2, tau2)), c11.fmul(Wn1, tau3))
    return c11.residue2([q0, q1, q2, q3], E)


def lambda_from_tau(E, tau):
    tau1, tau2, tau3, tau4 = [c11.b(x) for x in tau]
    xi = xtimes_power_residues(E, 4)
    out = xi[4]
    out = c11.rsub(out, (c11.fmul(tau1, xi[3][0]), c11.fmul(tau1, xi[3][1])))
    out = (c11.fadd(out[0], c11.fmul(tau2, xi[2][0])), c11.fadd(out[1], c11.fmul(tau2, xi[2][1])))
    out = c11.rsub(out, (c11.fmul(tau3, xi[1][0]), c11.fmul(tau3, xi[1][1])))
    out = (c11.fadd(out[0], tau4), out[1])
    return out


def equation_residue(z, tau, E, W, LD, bnum_res):
    u = c11.residue2(W, E)
    ell = c11.residue2(LD, E)
    z_b = (c11.fmul(z, bnum_res[0]), c11.fmul(z, bnum_res[1]))
    left_scalar = c11.rsub(u, z_b)
    lam = lambda_from_tau(E, tau)
    qres = q_residue_from_tau(W, E, tau)
    return c11.rsub(c11.rmul(left_scalar, lam, E), c11.rmul(ell, qres, E))


def solve_tau_for_z(z, E, W, LD, bnum_res):
    zero_tau = [0, 0, 0, 0]
    const = residue_to_b4(equation_residue(z, zero_tau, E, W, LD, bnum_res))
    cols = []
    for i in range(4):
        tau = [0, 0, 0, 0]
        tau[i] = 1
        val = residue_to_b4(equation_residue(z, tau, E, W, LD, bnum_res))
        cols.append([(val[r] - const[r]) % c11.P for r in range(4)])
    mat = [[cols[c][r] for c in range(4)] for r in range(4)]
    rhs = [(-x) % c11.P for x in const]
    return solve_linear_mod(mat, rhs, c11.P)


def run_case(p, nr, seed):
    D, E, bnum, bnum_res, W, LD, meta = build_trial_data(p, nr, seed)
    direct_slopes, landings = direct_split_slopes(D, E, bnum_res, W, LD)
    hist = Counter()
    singular = 0
    solved = 0
    split_slopes = set()
    for z0 in range(p):
        for z1 in range(p):
            z = (z0, z1)
            tau = solve_tau_for_z(z, E, W, LD, bnum_res)
            if tau is None:
                singular += 1
                continue
            solved += 1
            ftype = factor_type_quartic(tau, p)
            hist[ftype] += 1
            if ftype == "1111":
                split_slopes.add(z)
    meta.update({
        "q_gen": p,
        "q_line": p * p,
        "singular_z": singular,
        "solved_z": solved,
        "direct_C2": len(direct_slopes),
        "hist_C2": hist["1111"],
        "singular_split_C2": len(direct_slopes - split_slopes),
        "direct_landings": landings,
        "hist": dict(sorted(hist.items())),
        "split_sets_match": direct_slopes == split_slopes,
    })
    return meta


def main():
    print("cycle32_t2_j4_monodromy_histogram: EXPERIMENTAL / AUDIT")
    cases = [(7, 3, 0), (11, 2, 0), (13, 2, 0), (17, 3, 0)]
    for p, nr, seed in cases:
        r = run_case(p, nr, seed)
        print(
            "p={p} seed={seed} q_gen={q_gen} q_line={q_line} "
            "solved_z={solved_z} singular_z={singular_z} "
            "hist={hist} direct_C2={direct_C2} hist_C2={hist_C2} "
            "singular_split_C2={singular_split_C2} match={split_sets_match} "
            "landings={direct_landings}".format(**r)
        )


if __name__ == "__main__":
    main()
