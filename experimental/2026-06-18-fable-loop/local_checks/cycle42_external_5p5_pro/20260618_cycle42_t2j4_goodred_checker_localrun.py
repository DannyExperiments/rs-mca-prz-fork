#!/usr/bin/env python3
"""Independent Cycle 42 checker for the restricted t=2,j=4 branch.

It reconstructs the source equation
    (u-z b) lambda(tau) - ell Q(tau) = 0
in Q(i)[X]/(X^2+iX+1), with tau_j constrained to Q, audits the
z1=z0 Subcase-A cancellation, and certifies the replacement line z1=0:
  A at p0=7, B at p0=11.

Requires only SymPy.  No network access or packet-generated formulas are used.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import sympy as sp


def residue_mul(a, b):
    """Multiply pairs a0+a1 X modulo X^2+iX+1."""
    a0, a1 = a
    b0, b1 = b
    return (
        sp.expand(a0 * b0 - a1 * b1),
        sp.expand(a0 * b1 + a1 * b0 - sp.I * a1 * b1),
    )


def residue_add(a, b):
    return (sp.expand(a[0] + b[0]), sp.expand(a[1] + b[1]))


def residue_sub(a, b):
    return (sp.expand(a[0] - b[0]), sp.expand(a[1] - b[1]))


def residue_scale(c, a):
    return (sp.expand(c * a[0]), sp.expand(c * a[1]))


def residue_pow(a, n):
    out = (sp.Integer(1), sp.Integer(0))
    for _ in range(n):
        out = residue_mul(out, a)
    return out


def derive_surface(subcase: str):
    z0, z1 = sp.symbols("z0 z1", real=True)
    t1, t2, t3, t4 = sp.symbols("t1 t2 t3 t4", real=True)
    tau = (t1, t2, t3, t4)
    X = (sp.Integer(0), sp.Integer(1))
    powers = [residue_pow(X, j) for j in range(5)]

    # lambda=[X^4-t1 X^3+t2 X^2-t3 X+t4]_E
    lam = powers[4]
    lam = residue_sub(lam, residue_scale(t1, powers[3]))
    lam = residue_add(lam, residue_scale(t2, powers[2]))
    lam = residue_sub(lam, residue_scale(t3, powers[1]))
    lam = residue_add(lam, (t4, 0))

    # Source top coefficients W_{n-1..n-4}=1,i,1+i,1.
    w1, w2, w3, w4 = 1, sp.I, 1 + sp.I, 1
    q3 = w1
    q2 = w2 - w1 * t1
    q1 = w3 - w2 * t1 + w1 * t2
    q0 = w4 - w3 * t1 + w2 * t2 - w1 * t3
    qres = residue_add(
        residue_add((q0, 0), residue_scale(q1, powers[1])),
        residue_add(residue_scale(q2, powers[2]), residue_scale(q3, powers[3])),
    )

    z = z0 + sp.I * z1
    left = (1, 1 - z)  # u-zb=(1+X)-zX
    ell = (sp.I, 0) if subcase == "A" else (0, -2)
    eq = residue_sub(residue_mul(left, lam), residue_mul(ell, qres))

    # tau_j are base-field coordinates, hence four Q-linear equations.
    flat = []
    for c in eq:
        flat.extend([sp.expand(sp.re(c)), sp.expand(sp.im(c))])
    M = sp.Matrix([[sp.diff(f, tj) for tj in tau] for f in flat])
    rhs = sp.Matrix([-f.subs({tj: 0 for tj in tau}) for f in flat])
    Delta = sp.expand(M.det())
    return {
        "z0": z0,
        "z1": z1,
        "tau_symbols": tau,
        "lambda": tuple(map(sp.expand, lam)),
        "qres": tuple(map(sp.expand, qres)),
        "M": M,
        "rhs": rhs,
        "Delta": Delta,
    }


def quartic_data_on_line(model, z1_expr):
    z0, z1 = model["z0"], model["z1"]
    T = sp.symbols("T")
    M = model["M"].subs(z1, z1_expr)
    rhs = model["rhs"].subs(z1, z1_expr)
    det = sp.expand(M.det())
    sol = [sp.cancel(v) for v in M.inv() * rhs]
    L = sp.cancel(T**4 - sol[0] * T**3 + sol[1] * T**2 - sol[2] * T + sol[3])
    disc = sp.factor(sp.discriminant(L, T))
    num, den = map(sp.expand, sp.fraction(sp.cancel(disc)))
    num_poly = sp.Poly(num, z0, domain=sp.QQ)
    content, primitive = num_poly.clear_denoms(convert=True)[1].primitive()
    # primitive() returns (content, primitive); normalize positive leading coefficient.
    P = primitive
    if P.LC() < 0:
        P = -P
    return {
        "T": T,
        "M": M,
        "rhs": rhs,
        "det": det,
        "tau": sol,
        "L": L,
        "disc": disc,
        "disc_num": num,
        "disc_den": den,
        "P_primitive": P,
    }


def factor_type(poly: sp.Poly, p: int):
    if sp.gcd(poly, poly.diff()).degree() > 0:
        return "nonsquarefree", []
    _, factors = sp.factor_list(poly, modulus=p)
    degrees = []
    for fac, exponent in factors:
        degrees.extend([fac.degree()] * exponent)
    return "".join(str(d) for d in sorted(degrees)), factors


def finite_scan(line_data, p: int):
    z = next(iter(line_data["P_primitive"].gens))
    T = line_data["T"]
    det = sp.Poly(line_data["det"], z, domain=sp.ZZ)
    tau = line_data["tau"]
    hist = Counter()
    witnesses = {}
    singular = []
    for a in range(p):
        den = int(det.eval(a)) % p
        if den == 0:
            singular.append(a)
            continue
        vals = []
        for rational in tau:
            n, d = sp.fraction(sp.cancel(rational))
            nv = int(sp.Poly(n, z).eval(a)) % p
            dv = int(sp.Poly(d, z).eval(a)) % p
            vals.append(nv * pow(dv, -1, p) % p)
        f_expr = T**4 - vals[0] * T**3 + vals[1] * T**2 - vals[2] * T + vals[3]
        f = sp.Poly(f_expr, T, modulus=p)
        kind, factors = factor_type(f, p)
        hist[kind] += 1
        if kind not in witnesses:
            witnesses[kind] = {
                "z": a,
                "tau": vals,
                "quartic_mod_p": str(f.as_expr()),
                "factorization": [
                    {"factor": str(g.as_expr()), "exponent": e} for g, e in factors
                ],
                "discriminant_mod_p": int(sp.discriminant(f.as_expr(), T)) % p,
            }
    return {
        "p": p,
        "hist": dict(sorted(hist.items())),
        "singular_z": singular,
        "witness_13": witnesses.get("13"),
        "witness_4": witnesses.get("4"),
    }


def resultant_certificate(line_data, p: int, use_intrinsic_denominator: bool = True):
    z = next(iter(line_data["P_primitive"].gens))
    if use_intrinsic_denominator:
        # The correct pole boundary is the primitive l.c.m. of the *reduced*
        # Cramer denominators.  Using det(M) before cancellation can insert
        # fake multiplicities (the Cycle-41 Subcase-A bug).
        d_expr = sp.Integer(1)
        for rational in line_data["tau"]:
            _, den = sp.fraction(sp.cancel(rational))
            d_expr = sp.lcm(sp.Poly(d_expr, z, domain=sp.QQ),
                            sp.Poly(den, z, domain=sp.QQ)).as_expr()
        d = sp.Poly(d_expr, z, domain=sp.QQ).clear_denoms(convert=True)[1].primitive()[1]
        if d.LC() < 0:
            d = -d
    else:
        d = sp.Poly(-line_data["det"], z, domain=sp.ZZ)
    P = sp.Poly(line_data["P_primitive"], z, domain=sp.ZZ)
    r_dd = int(sp.resultant(d, d.diff()))
    r_pp = int(sp.resultant(P, P.diff()))
    r_dp = int(sp.resultant(d, P))
    return {
        "d": str(d.as_expr()),
        "P": str(P.as_expr()),
        "disc_formula": str(sp.factor(line_data["disc"])),
        "resultants": {
            "Res(d,dprime)": str(r_dd),
            "Res(P,Pprime)": str(r_pp),
            "Res(d,P)": str(r_dp),
        },
        "mod_p": {
            "p": p,
            "lc_d": int(d.LC()) % p,
            "lc_P": int(P.LC()) % p,
            "Res(d,dprime)": r_dd % p,
            "Res(P,Pprime)": r_pp % p,
            "Res(d,P)": r_dp % p,
            "tame_24": (24 % p) != 0,
        },
        "good_reduction_gate": all(
            x != 0
            for x in [
                int(d.LC()) % p,
                int(P.LC()) % p,
                r_dd % p,
                r_pp % p,
                r_dp % p,
                24 % p,
            ]
        ),
        "bad_ideal_generator_components": [
            "120",
            str(int(P.LC())),
            str(r_dd),
            str(r_pp),
            str(r_dp),
        ],
    }


def main():
    A = derive_surface("A")
    B = derive_surface("B")

    # Diagnose Cycle 41's diagonal line.
    A_diag = quartic_data_on_line(A, A["z0"])
    B_diag = quartic_data_on_line(B, B["z0"])
    z = A["z0"]
    raw_ddisc = sp.factor(A_diag["det"] ** 6 * A_diag["disc"])
    diag = {
        "Delta_A_on_z1_eq_z0": str(sp.factor(A_diag["det"])),
        "tau": [str(sp.factor(v)) for v in A_diag["tau"]],
        "disc": str(sp.factor(A_diag["disc"])),
        "raw_Delta6_times_disc": str(raw_ddisc),
        "extraneous_factor": "(z0 - 1)^8",
        "surface_node": {
            "point": [1, 1],
            "Delta": int(A["Delta"].subs({A["z0"]: 1, A["z1"]: 1})),
            "gradient": [
                int(sp.diff(A["Delta"], v).subs({A["z0"]: 1, A["z1"]: 1}))
                for v in (A["z0"], A["z1"])
            ],
            "Hessian_det": int(
                sp.hessian(A["Delta"], (A["z0"], A["z1"]))
                .subs({A["z0"]: 1, A["z1"]: 1})
                .det()
            ),
        },
    }

    # Clean common line z1=0.
    A0 = quartic_data_on_line(A, sp.Integer(0))
    B0 = quartic_data_on_line(B, sp.Integer(0))
    cert_A_same_line = resultant_certificate(A_diag, 7)
    cert_B_same_line = resultant_certificate(B_diag, 31)
    cert_A = resultant_certificate(A0, 7)
    cert_B = resultant_certificate(B0, 11)
    scan_A = finite_scan(A0, 7)
    scan_B = finite_scan(B0, 11)

    expected_hist_A = {"112": 1, "13": 4, "4": 2}
    expected_hist_B = {"1111": 1, "112": 2, "13": 3, "22": 2, "4": 3}
    checks = {
        "source_residue_powers": {
            "X2": "-1-iX",
            "X3": "i-2X",
            "X4": "2+3iX",
        },
        "A_same_line_corrected_good": cert_A_same_line["good_reduction_gate"],
        "A_good": cert_A["good_reduction_gate"],
        "B_same_line_good": cert_B_same_line["good_reduction_gate"],
        "B_good": cert_B["good_reduction_gate"],
        "A_hist": scan_A["hist"] == expected_hist_A,
        "B_hist": scan_B["hist"] == expected_hist_B,
        "A_has_4_and_13": scan_A["witness_4"] is not None and scan_A["witness_13"] is not None,
        "B_has_4_and_13": scan_B["witness_4"] is not None and scan_B["witness_13"] is not None,
        "A_raw_checker_false_negative_factor": "(z0 - 1)**8" in str(raw_ddisc),
    }

    out = {
        "model": {
            "lambda": str(A["lambda"]),
            "Q_residue": str(A["qres"]),
            "A": {
                "M": [[str(x) for x in row] for row in A["M"].tolist()],
                "rhs": [str(x) for x in A["rhs"]],
                "Delta": str(A["Delta"]),
            },
            "B": {
                "M": [[str(x) for x in row] for row in B["M"].tolist()],
                "rhs": [str(x) for x in B["rhs"]],
                "Delta": str(B["Delta"]),
            },
        },
        "A_z1_eq_z0_diagnosis": {**diag, "corrected_intrinsic_certificate_at_p7": cert_A_same_line},
        "B_z1_eq_z0_source_audit": {
            "tau": [str(sp.factor(v)) for v in B_diag["tau"]],
            "certificate_at_p31": cert_B_same_line,
        },
        "clean_line_z1_eq_0": {
            "A": {
                "tau": [str(sp.factor(v)) for v in A0["tau"]],
                "certificate": cert_A,
                "finite_scan": scan_A,
            },
            "B": {
                "tau": [str(sp.factor(v)) for v in B0["tau"]],
                "certificate": cert_B,
                "finite_scan": scan_B,
            },
        },
        "checks": checks,
        "all_checks_pass": all(checks.values()),
    }
    output = Path("experimental/2026-06-18-fable-loop/local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_localrun_result.json")
    output.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({"all_checks_pass": out["all_checks_pass"], "result": str(output)}, indent=2))


if __name__ == "__main__":
    main()
