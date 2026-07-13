#!/usr/bin/env python3
"""
b2: character-sum count of t-null blocks (the analytic handle) cross-checked
against the brute-force enumeration, and used to scope the n^3 bound's regime.

Exact first-moment identity (additive-character orthogonality over F_q):
  N_t(n,q) := #{ B subset mu_n : sum_{x in B} x^r = 0 in F_q, r=1..t }
           = q^{-t} * sum_{c in F_q^t} prod_{x in mu_n} ( 1 + e_q( sum_r c_r x^r ) )
  where e_q(u) = exp(2 pi i u / q).  The c=0 term gives 2^n; the rest is the
  "error" the giant-regime bound must control.  N_t counts ALL blocks (incl. empty
  and the structured coset-unions); extras = N_t - (structured count).

  The identity above is the theoretical handle for the giant regime.  `char_count`
  below EVALUATES the same N_t by an EXACT integer DP over power-sum vectors in
  F_q^t (state space <= q^t) -- the complex-float evaluation of the character sum
  lost precision on large rows (e.g. (64,1,193) was off by 448), so it is not used.
"""
from itertools import combinations

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
    xs=[pow(zeta,k,q) for k in range(n)]
    assert len(set(xs))==n, "zeta must be a primitive n-th root"
    return xs

def char_count(n,t,q):
    """Exact N_t = #{B<=mu_n : sum_{x in B} x^r = 0 (F_q), r=1..t}, via an EXACT
    integer DP over power-sum vectors in F_q^t (state <= q^t).  Same quantity as the
    additive-character identity in the module docstring, evaluated with exact ints."""
    from collections import defaultdict
    xs=mu_n(n,q)
    dp={(0,)*t:1}
    for x in xs:
        pv=[]; xr=x
        for r in range(t):
            pv.append(xr); xr=(xr*x)%q
        pv=tuple(pv)
        ndp=defaultdict(int)
        for v,c in dp.items():
            ndp[v]+=c                                        # exclude x
            nv=tuple((v[i]+pv[i])%q for i in range(t))       # include x
            ndp[nv]+=c
        dp=ndp
    return dp.get((0,)*t,0)

def enum_count(n,t,q):
    xs=mu_n(n,q)
    def tnull(K):
        return all(sum(pow(xs[k],r,q) for k in K)%q==0 for r in range(1,t+1))
    c=0
    for size in range(n+1):
        for K in combinations(range(n),size):
            if tnull(K): c+=1
    return c

print("cross-check: character-sum count  vs  brute enumeration  (must match)")
print(f"{'n':>3}{'t':>3}{'q':>5} | {'char N_t':>9} {'enum':>7} {'match':>6} | {'2^n/q^t':>10} {'n^3':>8}")
print("-"*70)
for (n,t,q) in [(8,1,17),(8,2,17),(16,1,17),(16,2,17),(16,3,17),(16,4,17),(16,2,97)]:
    Nc=char_count(n,t,q); Ne=enum_count(n,t,q)
    fm=2**n/q**t
    print(f"{n:>3}{t:>3}{q:>5} | {Nc:>9} {Ne:>7} {str(Nc==Ne):>6} | {fm:>10.1f} {n**3:>8}")

print()
print("scoping the bound's regime (char-sum only; no enumeration needed):")
print(f"{'n':>3}{'t':>3}{'q':>6} | {'char N_t':>12} {'2^n/q^t':>14} {'n^3':>10} {'N_t vs n^3':>12}")
print("-"*72)
for (n,t,q) in [(16,1,17),(32,1,97),(32,2,97),(64,1,193)]:
    Nc=char_count(n,t,q); fm=2**n/q**t
    verdict = "<= n^3" if Nc<=n**3 else ">> n^3 (small-t, NOT a prize row)"
    print(f"{n:>3}{t:>3}{q:>6} | {Nc:>12} {fm:>14.1f} {n**3:>10} {verdict:>12}")
