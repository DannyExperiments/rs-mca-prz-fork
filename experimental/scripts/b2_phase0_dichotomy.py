#!/usr/bin/env python3
"""
b2 Phase 0 — structural classification of t-null blocks (the rigidity go/no-go).

Dichotomy (u2c U2-C'): every t-null block B<=mu_n is a union of mu_M-cosets with
M >= t.  Test it by the SYMMETRY SCALE M_sym(B) = largest power-of-2 M|n such that
B is a union of mu_M-cosets (invariant under mult by mu_M).  In exponent space
(B={zeta^k : k in K}, index=exponent), mu_M-closure <=> K invariant under +n/M.

  structured (b1) : M_sym >= M0, M0 = least 2-power > t   (coset-union theorem)
  boundary        : M_sym = t exactly (the Frobenius-gap "extras")
  DICHOTOMY holds <=> every t-null block has M_sym >= t.

Two regimes: small-t (16,2 full) vs near-balance/giant-ish (32,4 via meet-in-middle).
"""
from itertools import combinations
from collections import defaultdict, Counter

def _isprime(m):
    if m<2: return False
    i=2
    while i*i<=m:
        if m%i==0: return False
        i+=1
    return True

def primitive_root(q):
    assert _isprime(q), f"q must be prime: {q}"
    order=q-1; f=set(); m=order; d=2
    while d*d<=m:
        while m%d==0: f.add(d); m//=d
        d+=1
    if m>1: f.add(m)
    for g in range(2,q):
        if all(pow(g,order//p,q)!=1 for p in f): return g
    raise RuntimeError

def mu_n(n,q):
    assert (q-1)%n==0, f"need n|q-1 (so mu_n <= F_q): n={n} q={q}"
    g=primitive_root(q); zeta=pow(g,(q-1)//n,q)
    xs=[pow(zeta,k,q) for k in range(n)]               # index k = exponent
    assert len(set(xs))==n, "zeta must be a primitive n-th root"
    return xs

def M_sym(K, n):
    Kset=set(K); M=n
    while M>=2:
        d=n//M
        if all(((k+d)%n) in Kset for k in Kset):
            return M
        M//=2
    return 1

def powersum_vec(K, xs, t, q):
    v=[0]*t
    for k in K:
        xr=xs[k]
        for r in range(t):
            v[r]=(v[r]+xr)%q
            xr=(xr*xs[k])%q
    return tuple(v)

def all_tnull_full(n,t,q):
    xs=mu_n(n,q); out=[]
    for size in range(n+1):
        for K in combinations(range(n),size):
            if powersum_vec(K,xs,t,q)==tuple([0]*t):
                out.append(frozenset(K))
    return out, xs

def all_tnull_mitm(n,t,q):
    xs=mu_n(n,q); half=n//2
    left=defaultdict(list)
    for mask in range(1<<half):
        K=[i for i in range(half) if (mask>>i)&1]
        left[powersum_vec(K,xs,t,q)].append(K)
    out=[]
    for mask in range(1<<half):
        K=[half+i for i in range(half) if (mask>>i)&1]
        need=tuple((-x)%q for x in powersum_vec(K,xs,t,q))
        if need in left:
            for LK in left[need]:
                out.append(frozenset(LK+K))
    return out, xs

def report(name, n, t, q, blocks):
    M0=1
    while M0<=t: M0*=2
    M0=min(M0,n)
    msyms=[M_sym(K,n) for K in blocks]
    hist=dict(sorted(Counter(msyms).items()))
    structured=[K for K,m in zip(blocks,msyms) if m>=M0]
    extras    =[K for K,m in zip(blocks,msyms) if m< M0]
    minM=min(msyms) if msyms else None
    dich = (minM is not None and minM>=t)
    print(f"=== {name}: n={n} t={t} q={q}  (M0={M0}, boundary M=t={t}) ===")
    print(f"  total t-null blocks : {len(blocks)}")
    print(f"  M_sym histogram     : {hist}")
    print(f"  structured (M_sym>=M0={M0}) : {len(structured)}")
    print(f"  EXTRAS   (M_sym< M0={M0})   : {len(extras)}     n^3={n**3}  within cushion? {len(extras)<=n**3}")
    print(f"  min M_sym = {minM}   -->  DICHOTOMY (all M_sym>=t={t})?  {'HOLDS' if dich else 'FAILS'}")
    if not dich:
        bad=[K for K,m in zip(blocks,msyms) if m<t and 0<len(K)<n]
        print(f"  dichotomy-violating blocks (M_sym<t): {len(bad)}; e.g. {sorted(next(iter(bad))) if bad else None}")
    print()
    return dict(n=n,t=t,extras=len(extras),minM=minM,dich=dich,hist=hist,cushion=n**3)

print("Phase 0: symmetry-scale classification of t-null blocks\n")
b16,_ = all_tnull_full(16,2,17)
r1=report("SMALL-t (full enum)", 16,2,17, b16)

b32,_ = all_tnull_mitm(32,4,97)
r2=report("NEAR-BALANCE / giant-ish (MITM)", 32,4,97, b32)

print("SUMMARY")
for r in (r1,r2):
    print(f"  n={r['n']:>2} t={r['t']}: extras={r['extras']:>6}  minM_sym={r['minM']}  "
          f"dichotomy={'HOLDS' if r['dich'] else 'FAILS'}  cushion n^3={r['cushion']}")

# --- balance-threshold sweep (reuses the Codex-green functions above) ---
# Hypothesis: dichotomy FAILS iff cost t*log2(q) < entropy ~ log2 C(n,n/2) (below balance).
from math import comb, log2
print("\nBALANCE SWEEP  n=32 q=97  (entropy ~ %.1f bits):" % log2(comb(32,16)))
print(f"  {'t':>2} {'cost=t*log2 q':>13} {'total':>7} {'extras':>7} {'minM':>5} {'dichotomy':>10} {'regime':>13}")
for t in [2,3,4,5,6]:
    blocks,_ = all_tnull_mitm(32, t, 97)
    M0=1
    while M0<=t: M0*=2
    M0=min(M0,32)
    msyms=[M_sym(K,32) for K in blocks]
    extras=sum(1 for m in msyms if m<M0)
    minM=min(msyms) if msyms else None
    dich = (minM is not None and minM>=t)
    cost=t*log2(97); ent=log2(comb(32,16))
    print(f"  {t:>2} {cost:>13.1f} {len(blocks):>7} {extras:>7} {str(minM):>5} "
          f"{('HOLDS' if dich else 'FAILS'):>10} {('below bal.' if cost<ent else 'above bal.'):>13}")
