#!/usr/bin/env python3
"""Independent Cycle 42 checker for the restricted t=2,j=4 residue-line branch.

No packet checker code is imported.  The script reconstructs the characteristic-zero
restriction-of-scalars equations from
  E=X^2+iX+1, b=X, u=1+X, W_top=(1,i,1+i,1),
for ell=i (A) and ell=-2X (B), computes Cramer quartics, diagnoses the
A diagonal slice, and certifies clean lines A:z1=0 at p=7 and B:z1=z0 at p=19.

Requires sympy.  It writes a machine-readable JSON certificate next to this file
when invoked with --output PATH; otherwise prints JSON to stdout.
"""
from __future__ import annotations

import argparse
import json
import warnings
from dataclasses import dataclass
from typing import Dict, List, Tuple

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning
warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)

z0,z1,s,x,y,h = sp.symbols('z0 z1 s x y h')
t1,t2,t3,t4 = sp.symbols('t1 t2 t3 t4')
T=(t1,t2,t3,t4)

# Gaussian expression as (real,imag), both in Q[z0,z1,tau].
def ga(a=0,b=0): return (sp.expand(a),sp.expand(b))
def gadd(a,b): return (sp.expand(a[0]+b[0]),sp.expand(a[1]+b[1]))
def gsub(a,b): return (sp.expand(a[0]-b[0]),sp.expand(a[1]-b[1]))
def gmul(a,b): return (sp.expand(a[0]*b[0]-a[1]*b[1]),sp.expand(a[0]*b[1]+a[1]*b[0]))
def gscale(a,c): return (sp.expand(c*a[0]),sp.expand(c*a[1]))
I=ga(0,1); ONE=ga(1,0); ZERO=ga(0,0)

# A=Q(i)[X]/(X^2+iX+1), residue pair (c0,c1).
def radd(a,b): return (gadd(a[0],b[0]),gadd(a[1],b[1]))
def rsub(a,b): return (gsub(a[0],b[0]),gsub(a[1],b[1]))
def rmul(a,b):
    a0,a1=a; b0,b1=b
    # X^2=-1-iX
    return (gsub(gmul(a0,b0),gmul(a1,b1)),
            gsub(gadd(gmul(a0,b1),gmul(a1,b0)),gmul(I,gmul(a1,b1))))
def rscalar(c,a): return (gmul(c,a[0]),gmul(c,a[1]))

XRES=(ZERO,ONE)
XP=[(ONE,ZERO)]
for _ in range(4): XP.append(rmul(XP[-1],XRES))
assert XP[2] == (ga(-1), ga(0,-1))
assert XP[3] == (I,ga(-2))
assert XP[4] == (ga(2),ga(0,3))

# tau_j are Q-scalars: this is restriction of scalars from Q(i), source-correct
# because finite-field tau_j lie in B=F_p.
def qscalar(q): return ga(q,0)

def lam() -> Tuple[Tuple[sp.Expr,sp.Expr],Tuple[sp.Expr,sp.Expr]]:
    out=XP[4]
    out=rsub(out,rscalar(qscalar(t1),XP[3]))
    out=radd(out,rscalar(qscalar(t2),XP[2]))
    out=rsub(out,rscalar(qscalar(t3),XP[1]))
    out=radd(out,(qscalar(t4),ZERO))
    return out

def qres():
    w1,w2,w3,w4=ONE,I,gadd(ONE,I),ONE
    q3=w1
    q2=gsub(w2,gmul(w1,qscalar(t1)))
    q1=gadd(gsub(w3,gmul(w2,qscalar(t1))),gmul(w1,qscalar(t2)))
    q0=gsub(gadd(gsub(w4,gmul(w3,qscalar(t1))),gmul(w2,qscalar(t2))),gmul(w1,qscalar(t3)))
    out=(q0,ZERO)
    out=radd(out,rscalar(q1,XP[1]))
    out=radd(out,rscalar(q2,XP[2]))
    out=radd(out,rscalar(q3,XP[3]))
    return out

LAM=lam(); QRES=qres()
assert LAM == (ga(2-t2+t4,-t1), ga(2*t1-t3,3-t2))
assert QRES == (ga(1-t3,-t1+t2), ga(t2,1))

Z=ga(z0,z1)
U=(ONE,ONE)
BRES=(ZERO,ONE)
LEFT=rsub(U,rscalar(Z,BRES))

@dataclass
class Model:
    name: str
    M: sp.Matrix
    c: sp.Matrix
    Delta: sp.Expr
    N: List[sp.Expr]
    P: sp.Expr


def build_model(name: str) -> Model:
    ell=(I,ZERO) if name=='A' else (ZERO,ga(-2))
    eq=rsub(rmul(LEFT,LAM),rmul(ell,QRES))
    equations=[sp.expand(eq[0][0]),sp.expand(eq[0][1]),sp.expand(eq[1][0]),sp.expand(eq[1][1])]
    M=sp.Matrix([[sp.diff(e,t) for t in T] for e in equations])
    c=sp.Matrix([sp.expand(e.subs({t1:0,t2:0,t3:0,t4:0})) for e in equations])
    Delta=sp.expand(M.det())
    rhs=-c
    N=[]
    for j in range(4):
        Mj=M.copy(); Mj[:,j]=rhs
        N.append(sp.factor(Mj.det()))
    P=sp.expand(Delta*x**4-N[0]*x**3+N[1]*x**2-N[2]*x+N[3])
    return Model(name,M,c,Delta,N,P)

MODELS={k:build_model(k) for k in ('A','B')}

EXPECTED={
'A':{
'M':[[2*z0-3,z1,1-z0,1],[2*z1-1,1-z0,1-z1,0],[2-3*z1,2*z0-2,z1-1,1-z0],[3*z0-3,2*z1-2,1-z0,-z1]],
'c':[2-3*z1,3*z0-4,6-5*z0,3-5*z1]},
'B':{
'M':[[2*z0-2,z1-3,1-z0,1],[2*z1-1,1-z0,-z1,0],[2-3*z1,2*z0-2,z1-3,1-z0],[3*z0-5,2*z1-1,1-z0,-z1]],
'c':[2-3*z1,3*z0-5,9-5*z0,3-5*z1]}}
for k,m in MODELS.items():
    assert m.M == sp.Matrix(EXPECTED[k]['M'])
    assert m.c == sp.Matrix(EXPECTED[k]['c'])


def line_data(model:Model, sub:Dict[sp.Symbol,sp.Expr]):
    D=sp.factor(model.Delta.subs(sub))
    N=[sp.factor(n.subs(sub)) for n in model.N]
    P=sp.expand(D*x**4-N[0]*x**3+N[1]*x**2-N[2]*x+N[3])
    g=sp.Poly(D,s,domain=sp.QQ)
    for n in N: g=sp.gcd(g,sp.Poly(n,s,domain=sp.QQ))
    gcd_coeff=sp.factor(g.as_expr())
    Pprim=sp.cancel(P/gcd_coeff)
    disc=sp.factor(sp.discriminant(sp.Poly(P,x),x))
    discprim=sp.factor(sp.discriminant(sp.Poly(Pprim,x),x))
    return D,N,P,gcd_coeff,sp.expand(Pprim),disc,discprim

A_diag=line_data(MODELS['A'],{z0:s,z1:s})
A_horiz=line_data(MODELS['A'],{z0:s,z1:0})
B_diag=line_data(MODELS['B'],{z0:s,z1:s})

# Local A diagonal geometry at s=1, infinity chart y=Y/X, after primitive saturation.
# Pprim^h/X^4 is obtained by x=1/y and multiplication by y^4.
Aprim=A_diag[4]
local=sp.expand((Aprim.subs({s:1+h,x:1/y})*y**4))
local=sp.Poly(local,h,y).as_expr()
assert sp.expand(local.subs(h,0)) == 3*y**3
assert sp.diff(local,h).subs({h:0,y:0}) == 3


def mod_resultant(f,g,p): return int(sp.resultant(f,g,s))%p

def ftype(coeffs:List[int],p:int)->str:
    poly=sp.Poly(sum((coeffs[j]%p)*x**(4-j) for j in range(5)),x,modulus=p)
    if poly.degree()!=4 or sp.gcd(poly,poly.diff()).degree()>0: return 'nonsquarefree'
    _,facs=sp.factor_list(poly,modulus=p)
    degs=[]
    for f,e in facs: degs.extend([f.degree()]*e)
    return ''.join(str(d) for d in sorted(degs))

def histogram(D,N,p):
    hist={}; witnesses={}
    singular=[]
    for sv in range(p):
        dv=int(D.subs(s,sv))%p
        if dv==0:
            singular.append(sv); continue
        nv=[int(n.subs(s,sv))%p for n in N]
        typ=ftype([dv,-nv[0],nv[1],-nv[2],nv[3]],p)
        hist[typ]=hist.get(typ,0)+1
        witnesses.setdefault(typ,{'s':sv,'tau':[(v*pow(dv,-1,p))%p for v in nv]})
    return hist,singular,witnesses


def cert_line(label,data,p):
    D,N,P,g,Pprim,disc,discprim=data
    # clean lines have g=1 and discprim=disc. Remove scalar content from discriminant.
    cont,H=sp.Poly(discprim,s,domain=sp.ZZ).primitive()
    H=H.as_expr()
    out={
      'line':label,'p0':p,'Delta':str(D),'N':[str(n) for n in N],
      'coefficient_gcd':str(g),'discriminant_content':int(cont),
      'H_coeff_desc':[int(c) for c in sp.Poly(H,s).all_coeffs()],
      'degrees':{'Delta':int(sp.degree(D,s)),'H':int(sp.degree(H,s))},
      'mod_p':{
        'lead_Delta':int(sp.LC(sp.Poly(D,s)))%p,
        'lead_H':int(sp.LC(sp.Poly(H,s)))%p,
        'Res_Delta_DeltaPrime':mod_resultant(D,sp.diff(D,s),p),
        'Res_H_HPrime':mod_resultant(H,sp.diff(H,s),p),
        'Res_Delta_H':mod_resultant(D,H,p),
      },
      'exact_resultants':{
        'Res_Delta_DeltaPrime':str(int(sp.resultant(D,sp.diff(D,s),s))),
        'Res_H_HPrime':str(int(sp.resultant(H,sp.diff(H,s),s))),
        'Res_Delta_H':str(int(sp.resultant(D,H,s))),
      }
    }
    hist,sing,wit=histogram(D,N,p)
    out['finite_histogram']=hist; out['singular_Cramer_s']=sing; out['witnesses']=wit
    out['PASS_simple_gate']=all(out['mod_p'][k]!=0 for k in out['mod_p']) and p not in (2,3)
    out['PASS_S4_types']='4' in hist and '13' in hist
    return out,H

A_cert,HA=cert_line('A: z1=0',A_horiz,7)
B_cert,HB=cert_line('B: z1=z0',B_diag,19)
assert A_cert['PASS_simple_gate'] and A_cert['PASS_S4_types']
assert B_cert['PASS_simple_gate'] and B_cert['PASS_S4_types']

# Generalized certificate for the original A diagonal line.
D,N,P,g,Pprim,disc,discprim=A_diag
cont,Hdiag=sp.Poly(discprim,s,domain=sp.ZZ).primitive(); Hdiag=Hdiag.as_expr()
# disc(Pprim)=(s-1)^2*H16
H16=sp.cancel(Hdiag/(s-1)**2)
assert sp.rem(sp.Poly(Hdiag,s),sp.Poly((s-1)**2,s))==0
diag_hist,diag_sing,diag_wit=histogram(D,N,7)
A_diag_general={
  'coefficient_gcd':str(g),
  'disc_primitive_factorization':str(sp.factor(discprim)),
  'H16_coeff_desc':[int(c) for c in sp.Poly(H16,s).all_coeffs()],
  'local_infinity_chart':str(sp.collect(local,h)),
  'd_local_dh_at_origin':int(sp.diff(local,h).subs({h:0,y:0})),
  'p7':{
    'lead_H16':int(sp.LC(sp.Poly(H16,s)))%7,
    'H16_at_1':int(H16.subs(s,1))%7,
    'Res_H16_H16Prime':mod_resultant(H16,sp.diff(H16,s),7),
  },
  'finite_histogram_p7':diag_hist,
  'singular_Cramer_s_p7':diag_sing,
  'witnesses_p7':diag_wit,
  'PASS_generalized_good_reduction_p7': all(v != 0 for v in [int(sp.LC(sp.Poly(H16,s)))%7,int(H16.subs(s,1))%7,mod_resultant(H16,sp.diff(H16,s),7),int(sp.diff(local,h).subs({h:0,y:0}))%7]),
  'interpretation':'smooth total curve; tame ramification index 3 at s=1 for p != 3'
}

out={
 'ledger':{'q_gen':'p','B':'F_p','F':'F_{p^2}=B(alpha)','q_line':'p^2','q_chal':'unused'},
 'restriction_of_scalars_note':'z0,z1,tau_j are Q/B coordinates; the source algebra is over Q(i), but the four scalar equations and integral quartic are Q-defined.',
 'powers_mod_E':{'X2':'-1-iX','X3':'i-2X','X4':'2+3iX'},
 'models':{},
 'A_diagonal_obstruction':A_diag_general,
 'certificates':{'A_horizontal_p7':A_cert,'B_diagonal_p19':B_cert},
 'bad_prime_ideals':{
   'intrinsic_A':'prime ideals of Z[i] dividing (30 * lc(H_A) * Res(H_A,H_A\'))',
   'intrinsic_B':'prime ideals of Z[i] dividing (30 * lc(H_B) * Res(H_B,H_B\'))',
   'conservative_Cycle41_add':'also include lc(Delta), Res(Delta,Delta\'), Res(Delta,H)'
 },
 'density_statement':'For relevant inert primes outside the finite bad set, the ordered-root S4 cover is geometrically irreducible of dimension 2, hence N_split=p^2/24+O(p^(3/2)).'
}
for k,m in MODELS.items():
 out['models'][k]={
  'M':[[str(sp.factor(v)) for v in row] for row in m.M.tolist()],
  'c':[str(sp.factor(v)) for v in list(m.c)],
  'Delta':str(sp.factor(m.Delta)),
  'N':[str(sp.factor(v)) for v in m.N]
 }

ap=argparse.ArgumentParser(); ap.add_argument('--output')
args=ap.parse_args()
text=json.dumps(out,indent=2)
if args.output:
    with open(args.output,'w') as f: f.write(text+'\n')
else: print(text)
