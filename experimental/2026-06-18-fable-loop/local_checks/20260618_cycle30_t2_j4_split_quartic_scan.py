#!/usr/bin/env python3
"""Finite scan for the Cycle 30 t=2, j=4 split-quartic gate.

This is experimental evidence only. It counts distinct bad slopes by direct
division/line-scalar testing for the restricted toy ledger:

  B=F_p, F=F_{p^2}, D=F_p, t=sigma=2, j=n-a=4.

The purpose is to distinguish the two Cycle 30 possibilities:

  * C2/p remains bounded, suggesting an O(p) split-gate law;
  * C2/p^2 stays visibly positive, suggesting a Theta(q_line) seed.
"""

from itertools import combinations
import importlib.util
from pathlib import Path
import random


ROOT = Path(__file__).resolve().parent
PREV = ROOT / "20260618_cycle11_t2_j2_line_incidence_verify.py"
spec = importlib.util.spec_from_file_location("cycle11", PREV)
c11 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c11)


def run_trial(p, nr, seed):
    c11.set_field(p, nr)
    rng = random.Random(seed)
    D = [c11.b(x) for x in range(p)]
    n = len(D)
    t = 2
    j = 4
    a = n - j
    k = a - t
    if k < 0:
        raise ValueError("p too small for t=2,j=4 balanced ledger")

    E = c11.random_separated_quadratic(rng)
    bnum = c11.random_bnum(rng)
    bnum_res = c11.residue2(bnum, E)

    w0 = [c11.b(rng.randrange(p)) for _ in D]
    w1 = [c11.b(rng.randrange(p)) for _ in D]
    w = [c11.fadd(w0[i], c11.fmul(c11.alpha, w1[i])) for i in range(n)]
    W = c11.interp(D, w)
    LD = c11.locator(D)

    Wres = c11.residue2(W, E)
    kappa = c11.wedge(Wres, bnum_res)

    slopes = set()
    landings = 0
    supports = 0
    for idxs in combinations(range(n), 4):
        T = [D[i] for i in idxs]
        LT = c11.locator(T)
        Ls, rem_l = c11.pdivmod(LD, LT)
        if rem_l != [c11.zero]:
            raise AssertionError("L_T did not divide L_D")
        _, Is = c11.pdivmod(W, Ls)
        supports += 1

        direct = c11.residue2(Is, E)
        z = c11.line_scalar(direct, bnum_res)
        if z is not None:
            slopes.add(z)
            landings += 1

    c2 = len(slopes)
    return {
        "p": p,
        "q_gen": p,
        "q_line": p * p,
        "seed": seed,
        "n": n,
        "k": k,
        "a": a,
        "t": t,
        "sigma": 2,
        "j": j,
        "off_R0": kappa != c11.zero,
        "supports": supports,
        "landings": landings,
        "C2": c2,
        "C2_over_p": c2 / p,
        "C2_over_p2": c2 / (p * p),
    }


def main():
    cases = [(7, 3, 20), (11, 2, 20), (13, 2, 16), (17, 3, 10)]
    print("cycle30_t2_j4_split_quartic_scan: EXPERIMENTAL")
    for p, nr, trials in cases:
        vals = []
        vals_off = []
        for seed in range(trials):
            r = run_trial(p, nr, seed)
            vals.append(r["C2"])
            if r["off_R0"]:
                vals_off.append(r["C2"])
            print(
                "p={p} seed={seed} q_gen={q_gen} q_line={q_line} "
                "n={n} k={k} a={a} t={t} sigma={sigma} j={j} "
                "off_R0={off_R0} C2={C2} C2/p={C2_over_p:.3f} "
                "C2/p^2={C2_over_p2:.4f} landings={landings}/{supports}".format(**r)
            )
        if vals:
            avg = sum(vals) / len(vals)
            off_avg = sum(vals_off) / len(vals_off) if vals_off else 0.0
            print(
                f"summary p={p} trials={len(vals)} off_R0_trials={len(vals_off)} "
                f"min_C2={min(vals)} avg_C2={avg:.2f} max_C2={max(vals)} "
                f"avg_C2_over_p={avg/p:.3f} avg_C2_over_p2={avg/(p*p):.4f} "
                f"off_R0_avg_C2={off_avg:.2f}"
            )


if __name__ == "__main__":
    main()
