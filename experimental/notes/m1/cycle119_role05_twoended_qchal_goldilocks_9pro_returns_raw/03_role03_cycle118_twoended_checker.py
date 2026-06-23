#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, json, sys
from pathlib import Path
from typing import Any

SUCCESS = "CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED"

class Reject(Exception):
    def __init__(self, clause: str, detail: str):
        super().__init__(f"{clause}: {detail}")
        self.clause = clause
        self.detail = detail

def req(c: bool, clause: str, detail: str) -> None:
    if not c:
        raise Reject(clause, detail)

def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("c116_verify", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def poly_mul(a, b, K):
    out = [K.zero for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] = K.add(out[i+j], K.mul(x,y))
    return out

def poly_from_roots(roots, K):
    c=[K.one]
    for r in roots:
        c = MOD.poly_mul_linear(c, r, K.zero, K.add, K.neg, K.mul)
    return c

def ksum(xs, K):
    s=K.zero
    for x in xs: s=K.add(s,x)
    return s

def solve(A, b, K):
    # Exact Gaussian elimination. A square, rows copied.
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for col in range(n):
        piv=next((r for r in range(col,n) if M[r][col] != K.zero), None)
        req(piv is not None, "EVALUATOR_MATRIX_SINGULAR", f"column {col}")
        M[col],M[piv]=M[piv],M[col]
        inv=K.inv(M[col][col])
        M[col]=[K.mul(inv,x) for x in M[col]]
        for r in range(n):
            if r==col: continue
            fac=M[r][col]
            if fac != K.zero:
                M[r]=[K.sub(M[r][c],K.mul(fac,M[col][c])) for c in range(n+1)]
    return [M[i][n] for i in range(n)]

def dot(a,b,K):
    return ksum((K.mul(x,y) for x,y in zip(a,b)),K)

def main(root: Path) -> dict[str,Any]:
    verifier_dir=root/"context/base_cycle118_context/cycle116_verifier/cycle116_role08_verifier"
    verify_py=verifier_dir/"verify_transfer.py"
    global MOD
    MOD=load_module(verify_py)
    anchor=verifier_dir/"inputs/cycle84_anchor.json"
    fixedp=verifier_dir/"inputs/fixed_jet_certificate.json"
    base=MOD.main_verify(anchor, fixedp)
    req(base.get("decision")=="CYCLE116_TRANSFER_CERTIFICATE_VERIFIED", "BASE_REPLAY", str(base.get("decision")))
    fixed=json.loads(fixedp.read_text())
    fc=fixed["field"]
    F=MOD.PrimeFieldExtension(int(fc["p"]),tuple(fc["modulus_coefficients_low_to_high"]))
    eta=F.trim(fc["eta_coefficients_low_to_high"])
    beta=F.trim(fc["beta_coefficients_low_to_high"])
    K=MOD.QuadraticExtension(F,eta)
    theta=K.theta; betaK=K.emb(beta)
    D0=[F.pow(eta,i) for i in range(256)]
    H0=[F.pow(eta,8*i) for i in range(32)]
    H=[K.pow(theta,i) for i in range(512)]
    req(len(set(H))==512 and betaK not in set(H),"FIELD_DOMAIN","bad H or beta in H")

    packet=fixed["packet"]
    E={int(i):tuple(es) for i,es in packet["base_exponent_sets"].items()}
    colors={}
    lifts={}
    all_block_top=True
    all_block_constant=True
    for i in (1,2,3):
        for a in range(16):
            B=tuple(sorted((a+e)%16 for e in E[i]))
            col=sum(B)%16
            colors[i,a]=col
            targets={F.emb(pow(3,b,17)) for b in B}
            roots=tuple(y for y in H0 if F.mul(y,y) in targets)
            req(len(roots)==16,"BLOCK_LIFT",f"{i},{a}")
            lifts[i,a]=roots
            for t in range(1,8):
                roots_t=[K.emb(F.mul(F.pow(eta,t),y)) for y in roots]
                L=poly_from_roots(roots_t,K)
                all_block_top &= len(L)==17 and all(L[d]==K.zero for d in range(11,16))
                expected=K.emb(F.emb(pow(3,(t+col)%16,17)))
                all_block_constant &= L[0]==expected
    req(all_block_top,"BLOCK_TOP_SIX","a block is not X^16+O(X^10)")
    req(all_block_constant,"BLOCK_CONSTANT","L_tia(0)!=3^(t+color)")
    req(int(packet["color_shell_target"])==4,"SHELL_TARGET","not 4")
    req(pow(3,28+4,17)==1,"SHELL_CONSTANT","3^(28+4)!=1")

    refidx=[int(x) for x in packet["reference_tuple_zero_based_state_indices"]]
    refstates=[(x//16+1,x%16) for x in refidx]
    req(sum(colors[s] for s in refstates)%16==4,"REFERENCE_SHELL","reference not in shell")
    Jnative=[K.one]
    for t,(i,a) in enumerate(refstates,1):
        Jnative += [K.emb(F.mul(F.pow(eta,t),y)) for y in lifts[i,a]]
    req(len(Jnative)==113 and len(set(Jnative))==113,"NATIVE_SUPPORT","bad size")
    Pnative=poly_from_roots(Jnative,K)
    req(Pnative[0]==K.neg(K.one),"NATIVE_CONSTANT","P_T(0)!=-1")
    req(Pnative[113]==K.one and Pnative[112]==K.neg(K.one),"NATIVE_TOP","leading pair")
    req(all(Pnative[d]==K.zero for d in range(108,112)),"NATIVE_TOP","degrees108..111")

    Astar=[K.mul(theta,K.emb(F.pow(eta,i))) for i in range(0,120)]
    Rstar=[K.mul(theta,K.emb(F.pow(eta,i))) for i in range(120,256)]
    odd={K.pow(theta,2*i+1) for i in range(256)}
    req(len(Astar)==120 and len(Rstar)==136,"AR_SIZE","bad 120/136")
    req(set(Astar).isdisjoint(Rstar) and set(Astar+Rstar)==odd,"AR_PARTITION","not odd-coset partition")
    PR=poly_from_roots(Rstar,K)
    Pstar=poly_mul(PR,Pnative,K)
    req(len(PR)==137 and len(Pstar)==250,"PADDED_DEGREE","bad degrees")
    c=K.neg(PR[0])
    req(Pstar[0]==c and c!=K.zero,"PADDED_CONSTANT","not common nonzero c")
    PRb=MOD.poly_eval(PR,betaK,K.zero,K.add,K.mul)
    req(PRb!=K.zero,"PADDED_BETA","P_R(beta)=0")

    j=249; sigma=7; r=256; n=512; k=256
    req(136+107==243==j-sigma+1,"TOP_SIX_BOUND","degree bound")
    req(n-j==263 and n-j-sigma==k,"PARAMETERS","parameter mismatch")
    selected=[0]+list(range(j+1,j+sigma)) # 0,250,...,255
    common_indices={0,*range(j-(sigma-2),j+1)} # 0,244,...,249
    # Check selected coordinates of P*X^m never inspect the variable coefficient X^243.
    for d in selected:
        for m in range(sigma):
            idx=d-m
            if 0<=idx<=j:
                req(idx in common_indices,"HIDDEN_SEVENTH_JET",f"selected d={d},m={m} reads P[{idx}]")

    # M[:,m] = selected coefficients of P* X^m. It is common to every family member.
    M=[]
    for d in selected:
        row=[]
        for m in range(sigma):
            idx=d-m
            row.append(Pstar[idx] if 0<=idx<len(Pstar) else K.zero)
        M.append(row)
    # Solve M^T lambda = (1,beta,...,beta^6).
    MT=[[M[c][rr] for c in range(sigma)] for rr in range(sigma)]
    b=[K.pow(betaK,m) for m in range(sigma)]
    lam=solve(MT,b,K)
    for m in range(sigma):
        col=[M[row][m] for row in range(sigma)]
        req(dot(lam,col,K)==b[m],"EVALUATOR_BASIS",f"m={m}")

    # Explicit determinant shape checks: q0=c*a0 and high block unit upper triangular.
    req(M[0][0]==c and all(M[0][m]==K.zero for m in range(1,sigma)),"EVALUATOR_CONSTANT_ROW","bad")
    for t in range(1,sigma):
        req(M[t][t]==K.one,"EVALUATOR_DIAGONAL",f"t={t}")
        for m in range(t):
            req(M[t][m]==K.zero,"EVALUATOR_TRIANGULAR",f"row={t},col={m}")

    # Evaluation scalar and exact imported occupancy.
    Pnb=MOD.poly_eval(Pnative,betaK,K.zero,K.add,K.mul)
    Psb=MOD.poly_eval(Pstar,betaK,K.zero,K.add,K.mul)
    req(Psb==K.mul(PRb,Pnb) and Psb!=K.zero,"PRODUCT_SCALAR","bad padded eval")
    N=int(base["field_parameter_ledger"]["bad_slope_numerator"])
    req(N==52_747_567_092,"NUMERATOR","wrong N")
    req(j+1<=r and betaK not in set(H),"NONCONTAINMENT","Vandermonde prerequisites")
    q=17**32
    req((2**128)*N>q,"THRESHOLD","N/q not >2^-128")
    req(j<250 and n-j==263,"STRICT_BALL","not distance <=249")

    return {
      "decision":SUCCESS,
      "base_terminal":base["decision"],
      "two_ended_selector_degrees":selected,
      "hidden_seventh_top_coefficient_used":False,
      "common_constant_nonzero":True,
      "A_star_size":120,"R_star_size":136,
      "n":n,"k":k,"j":j,"sigma":sigma,"agreement":263,
      "strict_hamming_distance_upper_bound":249,
      "distinct_slopes":N,
      "q_gen":q,"q_code":q,"q_line":q,"q_chal":None,
      "strictly_greater_than_2^-128":True
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("root",type=Path)
    args=ap.parse_args()
    try:
        print(json.dumps(main(args.root.resolve()),indent=2,sort_keys=True))
    except Reject as e:
        print(json.dumps({"decision":"CYCLE118_TWO_ENDED_TRANSFER_REJECTED","failure_clause":e.clause,"detail":e.detail},indent=2,sort_keys=True))
        raise SystemExit(1)
