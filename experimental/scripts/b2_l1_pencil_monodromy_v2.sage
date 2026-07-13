#!/usr/bin/env sage
# -*- mode: python -*-
r"""
b2_l1_pencil_monodromy_v2.sage -- Step 3 (shared b2/L1 core): monodromy of the pencil
psi: X -> X^ell/Gamma(X), CORRECTING pencil_monodromy.sage.

Fixes:
  (1) BASE POINT: Gamma is constant-free (Gamma(0)=0) so X | Gamma and X | (X^ell - t Gamma):
      X=0 is a t-independent root.  The nontrivial degree-(ell-1) cover is
          Q(X) = X^{ell-1} - t*gamma(X),   gamma = Gamma/X  (deg ell-2).
      Monodromy G = Gal(Q / F_p(t)) <= S_{ell-1}.  (The old script factored the degree-ell
      poly, whose ever-present X=0 linear factor blocked any ell-cycle -> false "intransitive".)
  (2) TRANSITIVITY tested SYMBOLICALLY (bivariate irreducibility of Q over F_p), not by
      Frobenius statistics -- sidestepping the decorrelation trap (FF global stats blind to
      local monodromy).  Frobenius sampling is used ONLY to detect group ELEMENTS (transpositions).

GO/NO-GO: if EXTREMAL Gamma (E_3=ell-2) have SPECIAL/small G while RANDOM Gamma give S_{ell-1},
monodromy detects the structure (monodromy route alive).  If both give S_{ell-1}, monodromy is
BLIND to E_3 -> the shared BGK additive-combinatorics inverse theorem is the only route.
"""
import random

def gamma_and_E3(gm, p, ell):
    F = GF(p); g = F.multiplicative_generator(); n = (p-1)//ell
    zeta = g**n; H = [zeta**j for j in range(ell)]
    Rx = PolynomialRing(F, 'X'); X = Rx.gen()
    Gam = sum(F(gm[r-1])*X**r for r in range(1, ell))     # Gamma = sum_{r=1}^{ell-1} gm[r-1] X^r
    E3 = 0
    for i in range(n):
        b = g**i; tab = {}
        for h in H:
            v = Gam(b*h); tab[v] = tab.get(v, 0) + 1
        mu = max(tab.values())
        if mu >= 3: E3 += mu - 2
    # gamma = Gamma / X : coefficients gm[0..ell-2] shifted down one degree
    gam = sum(F(gm[s])*X**s for s in range(ell-1))         # deg <= ell-2
    return Gam, gam, E3

def transitive_symbolic(gam_coeffs, p, ell):
    # transitive monodromy  <=>  Q = X^{ell-1} - t*gamma(X) irreducible over F_p(t)
    K = FunctionField(GF(p), 't'); t = K.gen()
    Rx = PolynomialRing(K, 'X'); X = Rx.gen()
    gam = sum(K(int(gam_coeffs[s]))*X**s for s in range(len(gam_coeffs)))
    Q = X**(ell-1) - t*gam
    return Q.is_irreducible()

def frobenius_cycle_types(gam, p, ell):
    F = GF(p); Rx = PolynomialRing(F, 'X'); X = Rx.gen()
    types = {}; ntransp = 0; nodd = 0; nsq = 0
    for t0 in range(1, p):
        Q = X**(ell-1) - F(t0)*gam
        if Q.degree() < ell-1: continue
        fac = Q.factor()
        if any(e > 1 for _, e in fac): continue            # branch point (non-squarefree)
        nsq += 1
        degs = tuple(sorted((fp.degree() for fp, _ in fac), reverse=True))
        types[degs] = types.get(degs, 0) + 1
        if sorted(degs) == sorted([2] + [1]*(ell-3)): ntransp += 1     # a transposition on ell-1 points
        # parity: permutation is odd iff #even-length cycles is odd
        if sum(1 for d in degs if d % 2 == 0) % 2 == 1: nodd += 1
    return types, ntransp, nodd, nsq

def gap_surviving_groups(observed_type_keys, d):
    # RIGOROUS group ID: keep every transitive group of degree d whose element cycle-type SET
    # contains all observed Frobenius cycle types. If only S_d survives, G = S_d (certificate-grade).
    obs = set(tuple(int(x) for x in ct) for ct in observed_type_keys)
    survivors = []
    for G in TransitiveGroups(d):
        realized = set(tuple(int(x) for x in g.cycle_type())
                       for g in G.conjugacy_classes_representatives())
        if obs <= realized:
            survivors.append(int(G.order()))
    return sorted(survivors)

def analyze(tag, gm, p, ell, rigorous=False):
    Gam, gam, E3 = gamma_and_E3(gm, p, ell)
    gam_coeffs = [gm[s] for s in range(ell-1)]
    tr = transitive_symbolic(gam_coeffs, p, ell)
    types, ntransp, nodd, nsq = frobenius_cycle_types(gam, p, ell)
    d = ell - 1
    # Robust discriminators (Chebotarev): for the FULL symmetric group S_d,
    #   P(d-cycle) = 1/d exactly, and P(odd permutation) = 1/2.
    frac_dcyc = types.get((d,), 0) / max(nsq, 1)     # observed fraction of (ell-1)-cycles
    frac_odd  = nodd / max(nsq, 1)
    has_transp = ntransp > 0
    # Is the profile consistent with S_d?  (d-cycle freq ~ 1/d AND odd freq ~ 1/2)
    consistent_Sd = tr and abs(frac_dcyc - 1.0/d) < 0.5/d and abs(frac_odd - 0.5) < 0.12
    verdict = ("consistent with S_%d (transitive; P[d-cyc]~1/d, P[odd]~1/2%s)"
               % (d, "; transposition seen" if has_transp else "")) if consistent_Sd \
              else ("transitive but NOT clearly S_%d (P[d-cyc]=%.3f vs 1/d=%.3f, P[odd]=%.2f) -- possible proper subgroup"
                    % (d, frac_dcyc, 1.0/d, frac_odd)) if tr \
              else "INTRANSITIVE (psi decomposes)"
    print("  %-22s E_3=%2d  d=%2d  transitive=%s  P[d-cyc]=%.3f (1/d=%.3f)  P[odd]=%.2f  transp=%d"
          % (tag, E3, d, tr, frac_dcyc, 1.0/d, frac_odd, ntransp))
    print("        verdict: %s" % verdict)
    if rigorous:
        surv = gap_surviving_groups(types.keys(), d)
        import math as _m
        fact = _m.factorial(d)
        print("        GAP transitive-subgroup filter: survivors (by order) = %s  [d! = %d => %s]"
              % (surv, fact, "S_%d ONLY" % d if surv == [fact] else "NOT uniquely S_%d" % d))
    return E3, consistent_Sd, frac_dcyc

def main():
    SAT = [("EXTREMAL ell=11 p=331", 331, 11, [97,29,97,239,171,92,143,155,270,1]),
           ("EXTREMAL ell=13 p=313", 313, 13, [254,289,29,276,242,219,201,261,79,232,133,1])]
    print("Step 3: pencil monodromy G = Gal(X^{ell-1} - t*gamma / F_p(t)) <= S_{ell-1}")
    print(" (base point X=0 removed; transitivity symbolic; group ID via Chebotarev discriminators)\n")
    print(" -- EXTREMAL (E_3=ell-2) --")
    ext = {}
    for (tag, p, ell, gm) in SAT:
        E3, cS, fdc = analyze(tag, gm, p, ell, rigorous=True); ext[ell] = (cS, fdc)
    print(" -- RANDOM Gamma (contrast) --")
    for (p, ell) in [(331,11),(313,13)]:
        rng = random.Random(int(7*p+ell))
        for k in range(2):
            gm = [rng.randrange(p) for _ in range(ell-1)]
            if not any(gm): continue
            analyze("random ell=%d p=%d #%d" % (ell,p,k), gm, p, ell)
    print("\n VERDICT LOGIC: extremal G smaller than random (S_{ell-1}) => monodromy DETECTS E_3 (route alive);")
    print(" both consistent with S_{ell-1} => monodromy BLIND to E_3 => shared BGK inverse-theorem is the only route.")
    print(" extremal 'consistent with S_{ell-1}': %s"
          % {ell: v[0] for ell, v in ext.items()})
    return 0

import sys; sys.exit(main())
