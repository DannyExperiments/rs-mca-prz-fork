Ihave everything I need. Both file-writing ad code-execution are disabedin
this harness(Writ denied, MCP xecute denied, no Bash tool), soper the
promp's fallback I'll provide the fullscript text plus thecompanion
certifcate/adit content inine. I have not executethe scaner, so I report
noscan numbes asresults —the dliverable is the checker itself
(classcation AUDIT);rnning it yields EXPERIMENTALdata.

  The scanner reuses the mounted stack (cycle11 → cycle12_t2_j3 →
  cycle12_base_component_rank→cycle15_forced_ra)andaddsonlytheCycle14/15
  column layer and the direct Q-determinant test. It does not use the Cycle 16
trace/Gram criterion (keptAUDIT); it tts Q≡0 by directevaluationof

det₄ₓ₄[c1|c2|c3|c0]overallofB²,whichissoundbecauseeachmatrixentry

isB-affinein(z₀,z₁)sodegQ≤4<p.

  Deliverable 1 — output_files/rank_det_split_scanner.py

#!/usr/bin/envpython3

"""Cycle17scannerforW-F1-AA-RES-T2J3-RANK-DET-SPLIT.

  Status: AUDIT (checker implementation / spec). Any number this script prints
  is

EXPERIMENTALfinite-sampleevidence,neveratheorem.

  Cycle 16 banked the safe side: off R0, if the Cycle 15 determinant consistency

polynomialQ(z_0,z_1)isNOTidenticallyzero,everylandingslopeliesonthe

nonzerodegree-<=4planecurve{Q=0},soC2<=4p=O(p)=O(n).Theresidual

livewallistheQ==0branchwiththedistinctD-splitcubiccondition
  retained.

Thisscannerisolatesthatbranchandcountstheslopeimageofdistinct

D-splitco-supportsTsubsetF_p,|T|=3.

  Ledger (never merged):

B=F_p,q_gen=pF=F_{p^2},q_line=p^2q_chal
  unused.

D=F_p,n=p.t=sigma=2,j=n-a=3,a=n-3,k=n-5.

eta=2/n(sub-reserve).WorkoffR0={wedge([W]_E,[Bnum]_E)=0}.

  Reuse, not reinvention. Imports the audited finite-field stack:

20260618_cycle11_t2_j2_line_incidence_verify.py(B,F=F_{p^2},polys,
  residues)

20260618_cycle12_t2_j3_line_incidence_scan.py(Q_Sclosedform,e_i)

20260618_cycle12_base_component_rank_scan.py(Delta,coeff-linerank,
  solver)

20260618_cycle15_forced_ra_slope_scan.py(forced-RaWnullspace)

  Q test (NO trace/Gram shortcut). The Cycle 16 trace / conjugate-skew Gram

criterionisAUDIT-onlyandisNOTusedhere.WebuildthefourB-linear
  columns

c1,c2,c3,c0inA=F[X]/E~=B^4,formthe4x4determinantQ(z_0,z_1)overB,
  and

evaluateatevery(z_0,z_1)inB^2.EachentryisB-affinein(z_0,z_1),so

degQ<=4<pforp>=7;vanishingatallp^2pointsisthereforeasound

identically-zerotest,andabivariatefitrecoversdegQforthecertificate.

  Self-checks (any failure => status HARNESS_OR_SOURCE_GAP):

*Delta(reused)==wedge(iota,mu)ofthecolumnpipeline.

*iota,muaffinein(tau1,tau2)withtau3-coefficientexactly-[W]_E,-b.

*everybrute-forcelandingslopezsatisfiesQ(z)=0AND

tau1c1(z)+tau2c2(z)+tau3c3(z)+c0(z)=0inA.

*whenQisNOTidenticallyzero,C2<=4p(Cycle16bound)holds.

  Counterpacket trigger (family level only): Q==0 AND C2/p^2 bounded below
  across

agrowing-pfamily.AsingleprimeisEXPERIMENTALonly.

"""

  from__future__importannotations

import argparse

importimportlib.util

importjson
  import os

importsys

fromitertoolsimportcombinations

frompathlibimportPath
  import random

  #--------------------------------------------------------------------------

#Locateandloadthemountedfinite-field/modelstack.

#--------------------------------------------------------------------------

def_find_local_checks(explicit):

candidates=[]
      if explicit:

candidates.append(Path(explicit))

env=os.environ.get("RS_MCA_LOCAL_CHECKS")

ifenv:

candidates.append(Path(env))

here=Path(__file__).resolve()

rel=Path("current_loop_20260618")/"2026-06-18-fable-loop"/
  "local_checks"

forparentin[here.parent]+list(here.parents):

candidates.append(parent/"input_project"/rel)

candidates.append(parent/rel)

needed="20260618_cycle15_forced_ra_slope_scan.py"

forcandincandidates:
          try:

if(cand/needed).is_file():

returncand.resolve()

exceptOSError:
              continue

raiseSystemExit(
          f"Could not locate local_checks dir containing {needed}. "

"Pass--local-checks-dirorsetRS_MCA_LOCAL_CHECKS."
      )

  def_load(name,path):

spec=importlib.util.spec_from_file_location(name,path)

mod=importlib.util.module_from_spec(spec)

sys.modules[name]=mod

spec.loader.exec_module(mod)
      return mod

  defload_stack(local_checks):

"""Loadcycle15(whichtransitivelyloadscycle12_rank/cycle12/cycle11)
  and

reusetheSAMEmoduleinstancessothereisexactlyonesharedfield
  state."""

c15=_load("cycle15_forced_ra",

local_checks/"20260618_cycle15_forced_ra_slope_scan.py")

returnc15,c15.c12r,c15.c12,c15.c11

  #--------------------------------------------------------------------------

#DeterminantoverF_p(B)forthe4x4consistencymatrix.

#--------------------------------------------------------------------------

defdet_mod_p(matrix,p):
      n = len(matrix)

a=[[v%pforvinrow]forrowinmatrix]

det=1

forcolinrange(n):
          piv = None
   forrinrange(col,n):

ifa[r][col]%p:
                  piv = r
   break
          if piv is None:

return0

ifpiv!=col:

a[col],a[piv]=a[piv],a[col]

det=(-det)%p

inv=pow(a[col][col],p-2,p)

det=(det*a[col][col])%p

forrinrange(col+1,n):

f=(a[r][col]*inv)%p

iff:

a[r]=[(a[r][k]-f*a[col][k])%pforkinrange(n)]
      return det % p

  #--------------------------------------------------------------------------

#Cycle-17layer,boundtoone(c11,c12,c12r)instance.

#--------------------------------------------------------------------------
  class SplitScanner:

def__init__(self,c11,c12,c12r):

self.c11,self.c12,self.c12r=c11,c12,c12r

      # A = F[X]/E, element = (R0, R1) with R_i in F.

defa_scale(self,e,s):

c=self.c11

return(c.fmul(s,e[0]),c.fmul(s,e[1]))

      def a_add(self, u, v):

c=self.c11

return(c.fadd(u[0],v[0]),c.fadd(u[1],v[1]))

      def a_sub(self, u, v):

c=self.c11

return(c.fsub(u[0],v[0]),c.fsub(u[1],v[1]))

      def a_is_zero(self, e):

returne[0]==self.c11.zeroande[1]==self.c11.zero

      def a_to_b4(self, e):

(r0re,r0im),(r1re,r1im)=e[0],e[1]

p=self.c11.P

return[r0re%p,r0im%p,r1re%p,r1im%p]

      def expand_in_WB(self, elt, Wres, Bres):

"""Solveelt=p1*[W]_E+p2*boverF(uniqueoffR0)."""
          c = self.c11

a,b_=Wres[0],Bres[0]

cc,d=Wres[1],Bres[1]

det=c.fsub(c.fmul(a,d),c.fmul(b_,cc))#=wedge([W]_E,b)

ifdet==c.zero:

returnNone

di=c.finv(det)

p1=c.fmul(c.fsub(c.fmul(d,elt[0]),c.fmul(b_,elt[1])),di)

p2=c.fmul(c.fsub(c.fmul(a,elt[1]),c.fmul(cc,elt[0])),di)

returnp1,p2

      def iota_mu(self, Wres, LDres, Bres, E, W, D1, D2, n, t1, t2, t3):

"""iota=[W]_E[L_T]_E-[L_D]_E[Q_S]_E;mu=[Bnum]_E[L_T]_E.

Identicaltothereuseddelta_for_taupre-wedgefactors."""

c,c12=self.c11,self.c12

LT=c.trim([c.fneg(t3),t2,c.fneg(t1),c.one])

Q=c12.q_formula_j3(W,n,D1,D2,t1,t2)

LTres=c.residue2(LT,E)

Qres=c.residue2(Q,E)

iota=c.rsub(c.rmul(Wres,LTres,E),c.rmul(LDres,Qres,E))

mu=c.rmul(Bres,LTres,E)

returniota,mu

      def affine_pq(self, Wres, LDres, Bres, E, W, D1, D2, n):

"""Coeffsofp1,p2,q1,q2(affineintau1,tau2)forA0=p1[W]+p2b,

B0=q1[W]+q2b.VerifiesCycle14affinestructure+tau3
  coefficients."""

c=self.c11

          def A0B0(t1, t2):

returnself.iota_mu(Wres,LDres,Bres,E,W,D1,D2,n,t1,t2,
  c.zero)

          b0, b1 = c.b(0), c.b(1)

A00,B00=A0B0(b0,b0)

A10,B10=A0B0(b1,b0)

A01,B01=A0B0(b0,b1)

pA00=self.expand_in_WB(A00,Wres,Bres)

pA10=self.expand_in_WB(A10,Wres,Bres)

pA01=self.expand_in_WB(A01,Wres,Bres)

qB00=self.expand_in_WB(B00,Wres,Bres)

qB10=self.expand_in_WB(B10,Wres,Bres)

qB01=self.expand_in_WB(B01,Wres,Bres)

ifNonein(pA00,pA10,pA01,qB00,qB10,qB01):

returnNone#onR0

          p1c, p2c = pA00

q1c,q2c=qB00
          coeffs = {

"p1":(p1c,c.fsub(pA10[0],p1c),c.fsub(pA01[0],p1c)),

"p2":(p2c,c.fsub(pA10[1],p2c),c.fsub(pA01[1],p2c)),

"q1":(q1c,c.fsub(qB10[0],q1c),c.fsub(qB01[0],q1c)),

"q2":(q2c,c.fsub(qB10[1],q2c),c.fsub(qB01[1],q2c)),

}

          def lin(co, x, y):

returnc.fadd(c.fadd(co[0],c.fmul(co[1],x)),c.fmul(co[2],y))

          rng = random.Random(0xA0B0)
   for_inrange(6):

t1,t2,t3=(c.b(rng.randrange(c.P))for_inrange(3))

iota,mu=self.iota_mu(Wres,LDres,Bres,E,W,D1,D2,n,t1,
  t2, t3)
   A0,B0=A0B0(t1,t2)

A0r=self.a_add(self.a_scale(Wres,lin(coeffs["p1"],t1,t2)),

self.a_scale(Bres,lin(coeffs["p2"],t1,t2)))

B0r=self.a_add(self.a_scale(Wres,lin(coeffs["q1"],t1,t2)),

self.a_scale(Bres,lin(coeffs["q2"],t1,t2)))
              if A0r != A0 or B0r != B0:

raiseAssertionError("Cycle14affineA0/B0expansionfailed")

ifiota!=self.a_sub(A0,self.a_scale(Wres,t3)):

raiseAssertionError("iotatau3-coefficient!=-[W]_E")

ifmu!=self.a_sub(B0,self.a_scale(Bres,t3)):
                  raise AssertionError("mu tau3-coefficient != -b")

returncoeffs

      def columns_at(self, coeffs, z, Wres, Bres):

"""(c1,c2,c3,c0)asA-elementsatslopez=(z0,z1)inF(Cycle15)."""
          c = self.c11

          def col(idx):

u=c.fsub(coeffs["p1"][idx],c.fmul(z,coeffs["q1"][idx]))

v=c.fsub(coeffs["p2"][idx],c.fmul(z,coeffs["q2"][idx]))

return(c.fadd(c.fmul(u,Wres[0]),c.fmul(v,Bres[0])),

c.fadd(c.fmul(u,Wres[1]),c.fmul(v,Bres[1])))

   c1,c2,c0=col(1),col(2),col(0)

neg=c.fneg(c.one)

c3=(c.fadd(c.fmul(neg,Wres[0]),c.fmul(z,Bres[0])),

c.fadd(c.fmul(neg,Wres[1]),c.fmul(z,Bres[1])))

returnc1,c2,c3,c0

      def Q_at(self, coeffs, z, Wres, Bres):

c1,c2,c3,c0=self.columns_at(coeffs,z,Wres,Bres)

cols=[self.a_to_b4(c1),self.a_to_b4(c2),

self.a_to_b4(c3),self.a_to_b4(c0)]

mat=[[cols[j][i]forjinrange(4)]foriinrange(4)]

returndet_mod_p(mat,self.c11.P)

      def Q_grid(self, coeffs, Wres, Bres):

p=self.c11.P

return{(z0,z1):self.Q_at(coeffs,(z0,z1),Wres,Bres)

forz0inrange(p)forz1inrange(p)}

      def fit_degQ(self, grid, p):

"""FitQasatotal-degree-<=4bivariatepoly;returnitsdegree

(-1ifidenticallyzero)usingthereusedsolver."""

monos=[(i,d-i)fordinrange(5)foriinrange(d+1)]

rows,rhs=[],[]

for(z0,z1),valingrid.items():

rows.append([(pow(z0,i,p)*pow(z1,j,p))%pfor(i,j)in
  monos])

rhs.append(val%p)

try:

sol=self.c12r.solve_mod_p(rows,rhs,p)

exceptAssertionError:
              return None

deg=-1

for(i,j),cfinzip(monos,sol):

ifcf%p:

deg=max(deg,i+j)
          return deg

      def case_landings(self, p, nr, E, bnum, W, coeffs, Q_is_zero):

c,c12,c12r=self.c11,self.c12,self.c12r

D=[c.b(x)forxinrange(p)]

n=len(D)

LD=c.locator(D)

D1,D2=c12.sum_points(D),c12.elem2(D)

Wres=c.residue2(W,E)
          LDres = c.residue2(LD, E)
   Bres=c.residue2(bnum,E)

       slopes = {}

split_landings=0
          examined = 0

foridxsincombinations(range(n),3):#each=adistinctD-split
  cubic

examined+=1

T=[D[i]foriinidxs]

t1,t2,t3=c12.sum_points(T),c12.elem2(T),c12.elem3(T)

delta=c12r.delta_for_tau(Wres,LDres,Bres,E,W,D1,D2,n,t1,
  t2, t3)

iota,mu=self.iota_mu(Wres,LDres,Bres,E,W,D1,D2,n,t1,
  t2, t3)

ifc.wedge(iota,mu)!=delta:

raiseAssertionError("Delta!=wedge(iota,mu):pipeline
  mismatch")

ifdelta!=c.zero:

continue

split_landings+=1

LT=c.locator(T)

Ls,rem=c.pdivmod(LD,LT)

ifrem!=[c.zero]:

raiseAssertionError("L_TdidnotdivideL_D")

_,Is=c.pdivmod(W,Ls)

z=c.line_scalar(c.residue2(Is,E),Bres)

ifzisNone:

raiseAssertionError("Delta=0butdirectslopetestfailed")

c1,c2,c3,c0=self.columns_at(coeffs,z,Wres,Bres)

lhs=self.a_add(self.a_add(self.a_scale(c1,t1),self.a_scale(c2,
  t2)),

self.a_add(self.a_scale(c3,t3),c0))

ifnotself.a_is_zero(lhs):

raiseAssertionError("tau(T)doesnotsolveL_z(tau)=0")

ifself.Q_at(coeffs,z,Wres,Bres)%p!=0:

raiseAssertionError("landingslopehasQ(z)!=0")

slopes[z]=slopes.get(z,0)+1

          if not Q_is_zero and len(slopes) > 4 * p:

raiseAssertionError("Q!=0butC2>4pviolatesCycle16")

returnslopes,split_landings,examined

  #--------------------------------------------------------------------------

#Helpers.
  # --------------------------------------------------------------------------
  defsmallest_nonresidue(p):

fornrinrange(2,p):

ifpow(nr,(p-1)//2,p)==p-1:
              return nr

raiseValueError(f"nonon-residuemod{p}")

  defhistogram_summary(fiber_sizes):
      h = {}

forsinfiber_sizes:

h[s]=h.get(s,0)+1

return{str(k):h[k]forkinsorted(h)}

  def_fmt_poly(c11,poly):

return[[v%c11.Pforvincoeff]forcoeffinc11.trim(poly)]

  #--------------------------------------------------------------------------
  # Certificate builder.
# --------------------------------------------------------------------------

defbuild_certificate(stack,scanner,p,nr,seed,E,bnum,W,

stratum,direction,kernel_dim):
      c15, c12r, c12, c11 = stack

D=[c11.b(x)forxinrange(p)]
      n = len(D)

LD=c11.locator(D)

D1,D2=c12.sum_points(D),c12.elem2(D)

Wres=c11.residue2(W,E)

LDres=c11.residue2(LD,E)

Bres=c11.residue2(bnum,E)

triples=n*(n-1)*(n-2)//6

   off_R0=(c11.wedge(Wres,Bres)!=c11.zero)

coeff_rank=c12r.coefficient_line_rank(c15.coeff_pairs_for_W(W,E,bnum,
  D), p)

      base = {

"p":p,"q_gen":p,"q_line":p*p,"seed":seed,

"E":_fmt_poly(c11,E),"Bnum":_fmt_poly(c11,bnum),

"stratum":stratum+(""ifdirectionisNoneelse
  f"|dir={direction}"),

"off_R0":off_R0,"coeff_line_rank":coeff_rank,

"direction":direction,"kernel_dim":kernel_dim,

"split_triples_examined":triples,

}

   ifnotoff_R0:

#R0=global/tangentendpoint;theCycle14/15reductionisstated

#offR0.MarkapplicabilityandexcludefromtheQ==0family
  (C2=None).

base.update({

"stratum":base["stratum"]+"|on_R0",

"Q_identically_zero":None,"degQ_or_test":"skipped_on_R0",

"split_landings":None,"C2":None,"max_slope_fiber":None,

"fiber_histogram_summary":{},"note":"on_R0_outside_wall",

"status":"PASS_QNONZERO_OP",
          })
   returnbase

   try:

coeffs=scanner.affine_pq(Wres,LDres,Bres,E,W,D1,D2,n)

ifcoeffsisNone:

raiseAssertionError("affine_pqreturnedNoneoffR0")

grid=scanner.Q_grid(coeffs,Wres,Bres)

Q_zero=all(v%p==0forvingrid.values())

degQ=scanner.fit_degQ(grid,p)

slopes,split_landings,_=scanner.case_landings(

p,nr,E,bnum,W,coeffs,Q_zero)

c2=len(slopes)

base.update({
              "Q_identically_zero": Q_zero,

"degQ_or_test":"Q_grid_all_zero"ifQ_zeroelsef"degQ={degQ}",
              "split_landings": split_landings, "C2": c2,

"max_slope_fiber":max(slopes.values())ifslopeselse0,
              "fiber_histogram_summary":
  histogram_summary(list(slopes.values())),

"status":"OPEN_QZERO_SMALL_SAMPLE"ifQ_zeroelse
  "PASS_QNONZERO_OP",
   })

exceptAssertionErrorasexc:
          base.update({

"Q_identically_zero":None,"degQ_or_test":"ERROR",

"split_landings":None,"C2":None,"max_slope_fiber":None,
              "fiber_histogram_summary": {}, "error": str(exc),

"status":"HARNESS_OR_SOURCE_GAP",
          })

returnbase

  #--------------------------------------------------------------------------
  # Case runners.

#--------------------------------------------------------------------------

defrun_forced_ra_case(stack,scanner,p,nr,seed,samples_per_direction):
      c15, c12r, c12, c11 = stack
   c11.set_field(p,nr)

rng=random.Random(seed)

E=c11.random_separated_quadratic(rng)

bnum=c11.random_bnum(rng)

ifc11.residue2(bnum,E)==(c11.zero,c11.zero):
          raise AssertionError("zero bnum residue")

directions=[(1,s)forsinrange(p)]+[(0,1)]
      certs = []
   fordirectionindirections:

basis=c15.forced_line_nullspace(p,nr,E,bnum,direction)
          if not basis:

continue
          for _ in range(samples_per_direction):

W=c15.vec_to_W(c15.random_from_basis(basis,p,rng))

ifW==[c11.zero]:
                  continue

certs.append(build_certificate(

stack,scanner,p,nr,seed,E,bnum,W,

stratum="Ra_forced",direction=direction,
  kernel_dim=len(basis)))
   returncerts

  defrun_random_case(stack,scanner,p,nr,seed):

c15,c12r,c12,c11=stack

c11.set_field(p,nr)

rng=random.Random(seed^0x5151)

D=[c11.b(x)forxinrange(p)]

n=len(D)

E=c11.random_separated_quadratic(rng)

bnum=c11.random_bnum(rng)

w0=[c11.b(rng.randrange(p))for_inD]

w1=[c11.b(rng.randrange(p))for_inD]

w=[c11.fadd(w0[i],c11.fmul(c11.alpha,w1[i]))foriinrange(n)]

W=c11.interp(D,w)

return[build_certificate(stack,scanner,p,nr,seed,E,bnum,W,
                                stratum="generic_random", direction=None,
   kernel_dim=None)]

  #--------------------------------------------------------------------------

#Familyaggregation+counterpackettrigger.

#--------------------------------------------------------------------------

deffamily_summary(certs,c2_over_p2_floor):

qzero=[cforcincerts

ifc.get("Q_identically_zero")isTrueandc.get("C2")isnot
  None]

primes_qzero=sorted({c["p"]forcinqzero})

ratios={}
      for c in qzero:

ratios.setdefault(c["p"],[]).append(c["C2"]/(c["p"]**2))

per_prime_max={p:max(rs)forp,rsinratios.items()}

growing=len(primes_qzero)>=3

bounded_below=growingandall(per_prime_max[p]>=c2_over_p2_floor

forpinprimes_qzero)

any_gap=any(c.get("status")=="HARNESS_OR_SOURCE_GAP"or"error"inc

forcincerts)
      return {

"primes_scanned":sorted({c["p"]forcincerts}),

"cases_total":len(certs),

"cases_off_R0":sum(1forcincertsifc.get("off_R0")),

"cases_Q_identically_zero":len(qzero),
          "primes_with_Q_zero": primes_qzero,

"max_C2_over_p2_per_prime":{str(p):round(v,5)

forp,vinper_prime_max.items()},

"max_C2_observed":max((c["C2"]forcincerts

ifc.get("C2")isnotNone),default=None),

"counterpacket_trigger_met":bool(bounded_below),
          "harness_or_source_gap_seen": bool(any_gap),
   }

  defoverall_status(summary):

ifsummary["harness_or_source_gap_seen"]:

return"HARNESS_OR_SOURCE_GAP"
      if summary["counterpacket_trigger_met"]:

return"COUNTERPACKET_C2_GROWTH_CANDIDATE"

ifsummary["cases_Q_identically_zero"]>0:

return"OPEN_QZERO_SMALL_SAMPLE"

return"PASS_QNONZERO_OP"

  # --------------------------------------------------------------------------
# CLI.

#--------------------------------------------------------------------------
  def main(argv=None):

ap=argparse.ArgumentParser(description="Cycle17Q==0split-distinct
  scanner")

ap.add_argument("--local-checks-dir",default=None)
      ap.add_argument("--primes", default="7,11,13")

ap.add_argument("--seeds",type=int,default=4)

ap.add_argument("--samples-per-direction",type=int,default=2)

ap.add_argument("--mode",choices=["forced_ra","random","both"],

default="forced_ra")

ap.add_argument("--c2-floor",type=float,default=0.10)

ap.add_argument("--json-out",default=None)

ap.add_argument("--max-print",type=int,default=40)

args=ap.parse_args(argv)

      stack = load_stack(_find_local_checks(args.local_checks_dir))

c15,c12r,c12,c11=stack

scanner=SplitScanner(c11,c12,c12r)

      primes = [int(x) for x in args.primes.split(",") if x.strip()]

forpinprimes:
          if p < 7:

raiseSystemExit("pmustbe>=7(needdegQ<=4<pfortheQ
  test)")

      certs = []

forpinprimes:

nr=smallest_nonresidue(p)

forseedinrange(args.seeds):

ifargs.modein("forced_ra","both"):

certs.extend(run_forced_ra_case(

stack,scanner,p,nr,seed,args.samples_per_direction))

ifargs.modein("random","both"):

certs.extend(run_random_case(stack,scanner,p,nr,seed))

      summary = family_summary(certs, args.c2_floor)

status=overall_status(summary)

summary["overall_status"]=status

      for cert in certs[:args.max_print]:

print("p={p}seed={seed}stratum={stratum}off_R0={off_R0}"

"coeff_rank={coeff_line_rank}Qzero={Q_identically_zero}"

"{degQ_or_test}split_landings={split_landings}C2={C2}"

"max_fiber={max_slope_fiber}status={status}".format(**cert))

      print("-" * 72)

print("FAMILYSUMMARY:",json.dumps(summary,sort_keys=True))

print("OVERALLSTATUS:",status)

print("NOTE:finite-sampleEXPERIMENTALevidence;sub-reserveeta=2/n;"

"noconj:B/q_gen/protocolclaim.")

      if args.json_out:

Path(args.json_out).write_text(json.dumps({

"scanner":"W-F1-AA-RES-T2J3-RANK-DET-SPLIT",

"ledger":{"B":"F_p","F":"F_{p^2}","q_chal":"unused",

"D":"F_p","t":2,"sigma":2,"j":3,"eta":"2/n"},

"params":{"primes":primes,"seeds":args.seeds,

"samples_per_direction":args.samples_per_direction,

"mode":args.mode,"c2_floor":args.c2_floor},

"summary":summary,"certificates":certs,

},indent=2,sort_keys=True))

print("wrote",args.json_out)

      return 2 if status == "HARNESS_OR_SOURCE_GAP" else 0

  if__name__=="__main__":

raiseSystemExit(main())

  Reproduce command (offline, where execution is allowed):

python3output_files/rank_det_split_scanner.py\

--primes7,11,13,17--seeds6--samples-per-direction3\

--modeforced_ra--json-outoutput_files/RESULTS.json

  Deliverable 2 — output_files/RESULT.md (content)

#Cycle17Result:W-F1-AA-RES-T2J3-RANK-DET-SPLITQ==0Scanner

  Primary classification: AUDIT (checker implementation + spec).

RunningthescannerproducesEXPERIMENTALfinite-sampledataonly.

  ## What this delivers

-rank_det_split_scanner.py:extendsthereusedstack(cycle11->
  cycle12_t2_j3

->cycle12_base_component_rank->cycle15_forced_ra)withtheCycle14/15

columnlayerc1,c2,c3,c0inA=F[X]/E~=B^4andaDIRECTtestof

Q(z_0,z_1)=det_4x4[c1|c2|c3|c0]byevaluationoverallofB^2.

-IsolatestheQ==0branchand,onit,countsdistinctslopesfromdistinct

D-splitcubicsTsubsetF_p,|T|=3,emittingper-casecertificates.

  ## Why the Q test is sound (not the trace/Gram criterion)

EachmatrixentryisB-affinein(z_0,z_1),sodegQ<=4.Forp>=7,

degQ<p,soQvanishingatallp^2points<=>Qidenticallyzero.TheCycle
  16

trace/conjugate-skewGramcriterionisNOTused;itremainsAUDIT.

  ## Built-in identity checks (fail-loud, => HARNESS_OR_SOURCE_GAP)

1.Delta(reused)==wedge(iota,mu)fromthecolumnpipeline.

2.iota,muaffinein(tau1,tau2);tau3-coefficientexactly-[W]_E,-b(Cycle
  14).

3.eachbrute-forcelandingslopezsatisfiesQ(z)=0and

tau1c1+tau2c2+tau3c3+c0=0inA.

4.Q!=0=>C2<=4p(Cycle16bankedsafe-sidebound),checkedeverycase.

  ## Certificate fields (per case)

p,q_gen,q_line,seed,E,Bnum,stratum,off_R0,coeff_line_rank,

Q_identically_zero,degQ_or_test,split_triples_examined,split_landings,C2,

max_slope_fiber,fiber_histogram_summary,direction,kernel_dim,status.

  ## Statuses

PASS_QNONZERO_OP|OPEN_QZERO_SMALL_SAMPLE|

COUNTERPACKET_C2_GROWTH_CANDIDATE|HARNESS_OR_SOURCE_GAP.

  ## Counterpacket trigger (family level only)

Q==0ANDminoveragrowingset(>=3)ofprimesofmax(C2/p^2)>=c2_floor.

AsingleprimeisEXPERIMENTALonlyandcannevertripthetrigger.

  ## Ledger

B=F_p(q_gen=p);F=F_{p^2}(q_line=p^2);q_chalunused;D=F_p,n=p;

t=sigma=2,j=3,a=n-3,k=n-5;eta=2/nsub-reserve;offR0.

  ##Notclaimed

Noproofofconj:B;nocorrected-reservecounterpacket(eta=2/nis

sub-reserve);noq_gencollapse;noprotocol/MCA/CA/list-/line-decoding/SNARK

consequence;nothingfromterminal/adtranscripttext.

  ## Execution note

Thisdeliverablewasproducedinaharnesswithfile-writeandcode-execution

disabled,soNOscannumbersarereportedasresultshere.PriorCycle15

forced-Rasmoke(p=7)recordedC2<=6,consistentwithnocounterpacket,andis

EXPERIMENTALonly.

  Deliverable 3 — output_files/NEXT_PROMPT.md (content)

#NextPrompt(Cycle18candidate)

  Run rank_det_split_scanner.py on a growing-p ladder (p=7,11,13,17,19,23) in an

environmentwhereexecutionisenabled.Then:

  1. If status stays OPEN_QZERO_SMALL_SAMPLE with max(C2/p^2) -> 0 as p grows:

pursueBANKABLE_LEMMA"split-distinctcollapseonQ==0",i.e.provethaton

theQ==0branchthedistinct-D-split-cubiclocusforcesC2=O(p).Candidate

invariant:relatesplitlandingstothelineell_zfiberin
  (tau1,tau2,tau3).

2.IfCOUNTERPACKET_C2_GROWTH_CANDIDATEfires(C2/p^2boundedbelowover>=3

primes):promotetoasymbolicfamily;rememberitissub-reserve(eta=2/n)

andisNOTacorrected-reserverefutation.

3.Independentlyre-derivetheCycle16trace/GramcriterionforQ==0andadd
  it

asaSECONDQ-testpath;keepAUDITuntilitagreeswiththedirect

det-evaluationtestacrossthewholeladder.

4.Alsoexercise--moderandomtoconfirmgenericanchorsareQ!=0

(PASS_QNONZERO_OP)andthattheCycle16C2<=4passertionnevertrips.

  Secondary: W-F1-AA-RES-T3J2 (deg E=t=3, j=2, codimension-two bad line).

  Classification

  The deliverable is a checker implementation plus spec; I could not execute it
  inthisharness,soIreportnofiniteoutcomesasresults.Thescanner
  targets the literal wall W-F1-AA-RES-T2J3-RANK-DET-SPLIT, reuses the mounted
stack, estsQ≡0 directly (nt via theAUDIT-only tace/Gramcriterion),

retainsthedistinct-split-cubiccondition,embedsfail-loudcross-checksof

thebankedCycle13/14/16identities,anddecidesthecounterpackettrigger

onlyatthegrowing-pfamilylevel.Noconj:B,corrected-reserve,q_gen,or

protocolclaimsaremade;eta=2/nremainssub-reserve.

  AUDIT
