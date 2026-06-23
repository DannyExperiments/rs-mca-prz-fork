#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, json, subprocess, sys
from pathlib import Path

ROOT = Path('/mnt/data/cycle119_packet/cycle119_role05_twoended_qchal_goldilocks_9pro/context/base_cycle118_context/cycle116_verifier/cycle116_role08_verifier')
MODPATH = ROOT / 'verify_transfer.py'

def loadmod():
    spec=importlib.util.spec_from_file_location('v116', MODPATH)
    assert spec and spec.loader
    m=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=m
    spec.loader.exec_module(m)
    return m

m=loadmod()

# Replay the banked Cycle116 finite/field certificate first.
p=subprocess.run([str(ROOT/'run_verifier.sh')], cwd=ROOT, capture_output=True, text=True, check=True)
base=json.loads(p.stdout)
assert base['decision']=='CYCLE116_TRANSFER_CERTIFICATE_VERIFIED'
assert base['field_parameter_ledger']['bad_slope_numerator']==52_747_567_092

fixed=json.loads((ROOT/'inputs/fixed_jet_certificate.json').read_text())
F=m.PrimeFieldExtension(int(fixed['field']['p']), tuple(fixed['field']['modulus_coefficients_low_to_high']))
eta=F.trim(fixed['field']['eta_coefficients_low_to_high'])
beta=F.trim(fixed['field']['beta_coefficients_low_to_high'])
K=m.QuadraticExtension(F,eta)
theta=K.theta
betaK=K.emb(beta)

# Helpers.
def pmul(coeffs1, coeffs2, zero, add, mul):
    out=[zero for _ in range(len(coeffs1)+len(coeffs2)-1)]
    for i,a in enumerate(coeffs1):
        for j,b in enumerate(coeffs2):
            out[i+j]=add(out[i+j],mul(a,b))
    while out and out[-1]==zero: out.pop()
    return out

def peval(coeffs,x,zero,add,mul):
    y=zero
    for c in reversed(coeffs): y=add(mul(y,x),c)
    return y

def shift_poly(coeffs,s,zero):
    return [zero]*s+list(coeffs)

packet=fixed['packet']
Esets={int(i):tuple(es) for i,es in packet['base_exponent_sets'].items()}
colors={}
blocks={}
block_constant_checks=0
for i in (1,2,3):
    for a in range(16):
        B=tuple(sorted((a+e)%16 for e in Esets[i]))
        color=sum(B)%16
        colors[(i,a)]=color
        for t in range(1,8):
            coeff=[F.one]
            eta2t=F.pow(eta,2*t)
            for b in B:
                root=F.mul(eta2t,F.emb(pow(3,b,17)))
                # X^2-root
                factor=[F.neg(root),F.zero,F.one]
                coeff=pmul(coeff,factor,F.zero,F.add,F.mul)
            assert len(coeff)==17 and coeff[16]==F.one
            assert all(coeff[d]==F.zero for d in range(11,16))
            expected=F.emb(pow(3,t+color,17))
            assert coeff[0]==expected
            blocks[(t,i,a)]=coeff
            block_constant_checks+=1
assert block_constant_checks==336
assert pow(3,16,17)==1 and all(pow(3,d,17)!=1 for d in (1,2,4,8))
assert (sum(range(1,8))+int(packet['color_shell_target']))%16==0
# Hence every color-shell Q_T has Q_T(0)=1 and P_T=(X-1)Q_T has P_T(0)=-1.

# Reconstruct the certified reference native locator.
refidx=list(packet['reference_tuple_zero_based_state_indices'])
refstates=[(x//16+1,x%16) for x in refidx]
assert sum(colors[s] for s in refstates)%16==int(packet['color_shell_target'])
Q=[F.one]
for t,(i,a) in enumerate(refstates,1):
    Q=pmul(Q,blocks[(t,i,a)],F.zero,F.add,F.mul)
P=pmul([F.emb(-1),F.one],Q,F.zero,F.add,F.mul) # X-1
assert len(P)==114 and P[113]==F.one and P[112]==F.emb(-1)
assert all(P[d]==F.zero for d in range(108,112))
assert P[0]==F.emb(-1)
assert peval(P,beta,F.zero,F.add,F.mul)!=F.zero

# New 120/136 odd-coset partition.
H=[K.pow(theta,i) for i in range(512)]
D0=H[0::2]
odd=H[1::2]
A=[K.mul(theta,K.emb(F.pow(eta,i))) for i in range(0,120)]
R=[K.mul(theta,K.emb(F.pow(eta,i))) for i in range(120,256)]
assert len(set(H))==512 and len(A)==120 and len(R)==136
assert set(A).isdisjoint(R) and set(A+R)==set(odd)
assert set(D0).isdisjoint(A+R)
assert betaK not in set(H)

# Fixed padding locator P_R and padded reference locator P*=P_R P_T.
PR=[K.one]
for root in R:
    PR=m.poly_mul_linear(PR,root,K.zero,K.add,K.neg,K.mul)
assert len(PR)==137 and PR[136]==K.one and PR[0]!=K.zero
PRbeta=peval(PR,betaK,K.zero,K.add,K.mul)
assert PRbeta!=K.zero
PK=[K.emb(c) for c in P]
Pstar=pmul(PR,PK,K.zero,K.add,K.mul)
assert len(Pstar)==250 and Pstar[249]==K.one
assert Pstar[0]==K.mul(PR[0],K.emb(F.emb(-1))) and Pstar[0]!=K.zero
assert peval(Pstar,betaK,K.zero,K.add,K.mul)==K.mul(PRbeta,K.emb(peval(P,beta,F.zero,F.add,F.mul)))

# Exact common-data ledger: native differences <=107; padding degree 136.
j,sigma,r,n,k=249,7,256,512,256
assert 136+107==243==j-sigma+1
assert j+sigma==r and n-r==k and n-j==263

# Construct the two-ended evaluator from coefficient 0 and degrees 250..255.
c=Pstar[0]
def ell(Qcoeff):
    q=list(Qcoeff)+[K.zero]*max(0,r-len(Qcoeff))
    aa=[K.zero]*sigma
    aa[0]=K.mul(q[0],K.inv(c))
    # q_{j+m} = sum_{t=m}^{sigma-1} a_t p_{j+m-t}; p_j=1.
    for mm in range(sigma-1,0,-1):
        val=q[j+mm]
        for t in range(mm+1,sigma):
            val=K.sub(val,K.mul(aa[t],Pstar[j+mm-t]))
        aa[mm]=val
    out=K.zero
    bp=K.one
    for a in aa:
        out=K.add(out,K.mul(a,bp))
        bp=K.mul(bp,betaK)
    return out
for mm in range(sigma):
    assert ell(shift_poly(Pstar,mm,K.zero))==K.pow(betaK,mm)

N=52_747_567_092
q=17**32
assert q==K.q and q//2**128==6 and N*2**128>q
assert j+1==250<=r

print(json.dumps({
  'decision':'CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED',
  'base_receipt':base['decision'],
  'block_constant_checks':block_constant_checks,
  'shell_constant':'P_T(0)=-1 for every color-shell tuple',
  'partition':{'A_size':len(A),'R_size':len(R),'agreement':n-j},
  'two_ended_evaluator':{
      'selected_coefficients':[0,250,251,252,253,254,255],
      'basis_checks':sigma,
      'common_top_coefficients':sigma-1,
      'common_constant_nonzero':True,
  },
  'degree_ledger':{'native_difference_max':107,'padding_degree':136,'padded_difference_max':243,'required_max':243},
  'parameters':{'n':n,'j':j,'sigma':sigma,'r':r,'k':k,'agreement':n-j,'distance_at_most':j},
  'noncontainment':{'vandermonde_columns':j+1,'ambient_dimension':r,'beta_outside_domain':True},
  'field_ledger':{'q_gen':q,'q_code':q,'q_line':q,'q_chal':None},
  'numerator':N,
  'floor_q_over_2^128':q//2**128,
  'strictly_above_2^-128':True,
  'scope':'finite/source-scoped LD_sw theorem; no official contract claim'
},indent=2,sort_keys=True))
