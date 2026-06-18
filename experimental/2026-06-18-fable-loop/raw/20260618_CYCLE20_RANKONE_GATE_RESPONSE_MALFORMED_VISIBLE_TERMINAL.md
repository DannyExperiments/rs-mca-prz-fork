Ihave al thesurce identities need. Codeexecution was denied (theDE
tool is blockedand thismatches Cycle 19's own no-code constraint), so this
isan analytic audiworkeddirectly frm the Cycle 12/14 multiplicationable
inA=F[X]/E — r-deriving eachcandidatefrom firtprinciples rather than
pattern-matching.

---
Primary lbe

BANKABLE_LEMMA

  All five Cycle 19 closed forms are correct exactly off R0, with no hidden
  genericitybeyondkappa=uwedgeb!=0.Noformulaisfalse,sothisisnota
  ROUTE_CUT. I also isolate the sharper collapse condition (the EXACT_NEW_WALL
refinement) below, bu heheadlin isthat the fomlasarenowproven,not

candidate.

  Ledger (kept separate)

  B=F_p, q_gen=p; F=F_{p^2}=B+alpha B, q_line=p^2; q_chal unused. D=F_p, n=p.
  t=sigma=2,j=3,a=n-3,k=n-5.eta_reserve=2/nsub-reserve.Workoff
  R0={kappa=[W]_E wedge [Bnum]_E=0}. Line-incidence/residue calculation only.

  The multiplication engine (source-checked)

  Write x=(x^{(0)},x^{(1)}) for x=x^{(0)}+x^{(1)}xi, xi^2=-c xi-d. Then

(xy)^{(0)}=x0y0-dx1y1,(xy)^{(1)}=x0y1+x1y0-cx1y1,

xwedgey=x0y1-x1y0,

Q_E(x)=x0^2-cx0x1+dx1^2=N(x)(normform),

P_E(x,y)=x0y0-cx0y1+dx1y1,P_E(x,x)=Q_E(x).

  Two structural facts I use repeatedly (both proven by 2x2 expansion):

(R1)P_E(x,y)-P_E(y,x)=-c(xwedgey).

(R2master)(lambda_0x)wedgey=lambda_0^{(0)}(xwedgey)-
  lambda_0^{(1)} P_E(y,x).

  From Cycle 12 (D=F_p): lambda_0=xi^3-tau_1 xi^2+tau_2 xi reduces to

lambda_0^{(0)}=cd+dtau_1,

lambda_0^{(1)}=(c^2-d)+ctau_1+tau_2=:eta,[matchescandidate]

  and Q:=[Q_S]_E has Q^{(0)}=W_{n-3}-d W_{n-1}-W_{n-2}tau_1+W_{n-1}tau_2,
  Q^{(1)}=(W_{n-2}-cW_{n-1})-W_{n-1}tau_1.FromCycle14,offR0,A0=u
  lambda_0-ell Q, B0=lambda_0 b, and in the F-basis {u,b}:

p1=(A0wedgeb)/kappa,p2=(uwedgeA0)/kappa,q1=(B0wedgeb)/kappa,q2=(u
  wedge B0)/kappa.

  Verification of the four closed forms (each exact)

  q1. By (R2) with x=b,y=b (so x wedge y=0, P_E(b,b)=Q_E(b)):

(lambda_0b)wedgeb=-etaQ_E(b).Hence

q1=-(Q_E(b)/kappa)eta.[CANDIDATECONFIRMED]

  q2. u wedge(lambda_0 b) = -[(lambda_0 b) wedge u] = -[lambda_0^{(0)}(b wedge
  u)-etaP_E(u,b)]=lambda_0^{(0)}kappa+etaP_E(u,b).Hence

q2=lambda_0^{(0)}+(P_E(u,b)/kappa)eta.[CONFIRMED]

  p1. (u lambda_0) wedge b = lambda_0^{(0)}kappa - eta P_E(b,u) by (R2). Using
  (R1),P_E(b,u)=P_E(u,b)+ckappa,soP_E(b,u)/kappa=c+P_E(u,b)/kappa.WithA0=u
  lambda_0-ell Q:

p1=lambda_0^{(0)}-(c+P_E(u,b)/kappa)eta-(1/kappa)((ellQ)wedgeb).
  [CONFIRMED]

  p2. u wedge(u lambda_0) = -[(lambda_0 u) wedge u] = eta Q_E(u) (since u wedge
  u=0,P_E(u,u)=Q_E(u)).Hence

p2=(1/kappa)(Q_E(u)eta-(uwedgeellQ)).[CONFIRMED]

  The two Q-dependent pieces also reduce exactly as claimed (project onto
  Q^{(0)}1+Q^{(1)}xiandapply(R2)withlambda_0->xi):

(ellQ)wedgeb=(ellwedgeb)Q^{(0)}-P_E(b,ell)Q^{(1)},

uwedge(ellQ)=(uwedgeell)Q^{(0)}+P_E(u,ell)Q^{(1)}.

  Lemma 1 (rank-one) — PROVEN

  q1=-(Q_E(b)/kappa) eta is a fixed F-scalar times the single affine form eta.
  Sotheleadingcoefficientoftheslopequadraticq1z^2-(p1-q2)z-p2=0is
  rank-one in (tau_1,tau_2), vanishing exactly on the F-line eta=0. Also
lambda_0^{(0)}=cd+d tau_1 cancels fromq1,p1-q2, p2 andsurvivesonlyinthe

tracep1+q2=2lambda_0^{(0)}-ceta-(1/kappa)((ellQ)wedgeb).Bothclaimshold

unconditionallyoffR0.

  Lemma 2 (quadric normal form) — PROVEN

  The discriminant identity is algebraic (always true):

delta_z:=(p1-q2)^2+4q1p2=(p1+q2)^2-4detP,detP:=p1q2-p2
  q1.

  Delta=tau_3^2-(p1+q2)tau_3+det P, so Delta1==0 is exactly {p1+q2 in
  B[tau_1,tau_2]}and{detPinB[tau_1,tau_2]};onthatlocus
  delta_z=(p1+q2)^2-4 det P in B[tau_1,tau_2]. With c_b=-Q_E(b)/kappa and A=(ell
Q)wedgeb, thequadratic formula gives (using p1-q2=-c

eta-2(P_E(u,b)/kappa)eta-A/kappa):

z=const_F+w^±,w^±=(±sqrt(delta_z)-A/kappa)/(2c_beta),

const_F=(-c-2P_E(u,b)/kappa)/(2c_b)[tau-independent].

  The eta in q1 cancels the eta-proportional part of p1-q2, leaving a fixed
  F-translation;sincetranslationisabijection,C2=#{z}=#{w^±}.Confirmed
  (requires b a unit, Q_E(b)!=0, so c_b!=0).

  The scalar gate D — definition and role PROVEN (collapse role still open)

  Express the three slope-coefficient forms in the frame {eta, Q^{(0)},
  Q^{(1)}}.Thecoefficientmatrixis

M=[c_b00](q1)

[*-(ellwedgeb)/kappaP_E(b,ell)/kappa](p1-q2)

[*-(uwedgeell)/kappa-P_E(u,ell)/kappa](p2)

  Expanding along the first row:

detM=(c_b/kappa^2)*[(ellwedgeb)P_E(u,ell)+P_E(b,ell)(uwedgeell)]
  = (c_b/kappa^2) * D.

  So with c_b!=0, kappa!=0:

D=0<=>{q1,p1-q2,p2}areF-linearlydependentintheframe
  {eta,Q^{(0)},Q^{(1)}}

(theP^2(F)coefficientimageliesinafixedline).

  D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell) depends only on (E,u,b,ell)
  andisnotidenticallyzero:u=ellgivesD=(ellwedgeb)Q_E(ell),nonzero
  whenever ell is a unit independent of b. So D=0 is a proper closed gate. This
confirmsthecandidate gte is wel-defined and coeclyplacedasthe

P^2(F)-leveldegenerationobstruction.

  What this does not settle: D=0 is the F-linear (P^2) degeneration, which is
  necessaryforC2=O(p),buteta,Q^{(0)},Q^{(1)}arethreeaffineformsinonly
  two B-variables, so the genuine collapse is a finer B-level condition. This is
the residualwall.

  What is banked vs not

  Bank (proven, exact, off R0, restricted D=F_p, t=sigma=2, j=3 window): the
  fourclosedformsp1,p2,q1,q2;Lemma1(rank-oneq1,lambda_0^{(0)}
  cancellation); Lemma 2 (discriminant identity, Delta1==0 ⟺ {p1+q2,det P}∈B,
descet of delta_z to B[tau_1,tau_2], normal form w^±);thegateidentitydet

M=(c_b/kappa^2)DwithD≢0.

  Do not bank: collapse or non-collapse; any C2 bound on Delta1==0; any
  Theta(q_line)counterpacket;theclaimD=0<=>C2=O(p)(onlytheP^2-level
  equivalence is proven); anything at/above corrected reserve; any q_gen,
protcol, list/line/curve-decoding, CA, orMCA consequence.

  Sharpened wall (EXACT_NEW_WALL refinement)

W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE(sharpened)

  OntheDelta1==0locus{p1+q2inB[tau1,tau2],detPinB[tau1,tau2]},with

q1=c_beta(rankone),delta_zinB[tau1,tau2],and

w^±=(±sqrt(delta_z)-A/kappa)/(2c_beta),A=(ellQ)wedgeb:

provedim_BIm(w)=1(equivalentlydwwedgedeta==0onthelocus)=>
  C2=O(p),

ORbuildsource-validgrowing-pdatawithdim_BIm(w)=2=>
  C2=Theta(p^2)=Theta(q_line).

  The gate D=0 is the P^2(F)-level necessary condition; the open question is
  whethertheDelta1==0resonanceconditionson(p1+q2,detP)forcethefiner
  B-level dependence dw wedge d eta==0. This corrects Cycle 18's "collapse
plausible": thenormal form shows collapeisa non-genericdegenerationthat

mustbeforced,sinceA=(ellQ)wedgebisarank-twoF-affineformwhileeta

isrank-one.TheCycle15p=7,C2<=6dataareconsistentwiththegatefiring

butaresingle-primeEXPERIMENTALanddecidenothing.

  Which prior wall survives: none is cut. Cycles 12–18 all check out against the
  multiplicationidentities;Cycle16'sQ!=0=>C2<=4psafesidestands,and
  the live residual is exactly the Delta1==0 / Q==0 branch, now equipped with
the proven normal form andgate.

Forbidden-upgradecompliance

  No Proximity-Prize solve/disproof; no conj:B; eta=2/n stays sub-reserve (even
  aTheta(q_line)herewouldnotrefutecorrectedMCA);q_genandq_linekept
  separate; no protocol denominator saving; no list/line/curve decoding, CA,
MCA; finite scans cted only as EXPERIMENTAL;malfomedterminaltextnotused

asmath.

  ---

  Do you see a route to a full solve? If yes, what is the next exact lemma or
  construction?

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
cnstruction?

Notafullsolvefromhere—thisisasub-reserveeta=2/ntoywindow,soeven
  a positive collapse result closes only restricted t=2,j=3 local F1, not the
  Prize.Butthereisaconcrete,code-freeroutetoclosingthiswindow.The
  next exact lemma is the B-rank-one descent on the Delta1==0 locus:

NEXTEXACTLEMMA(finitesymbolic,nogrowingprime):

OnDelta1==0,thetwoB-descentconditionsare

(i)Im_alpha(p1+q2)≡0inB[tau1,tau2],

(ii)Im_alpha(detP)≡0inB[tau1,tau2].

Computedwwedgedetaasapolynomialin(tau1,tau2)modulotheideal
  (i),(ii).

Provedwwedgedeta≡0onV(i,ii)(=>C2=O(p),windowclosed),

orfindonesource-valid(E,Bnum,W)onV(i,ii)withdwwedgedeta≢0

(theprecisecounterpacketseed;onlythenrunp=11,13,17,19,23filteredto
  Delta1==0,
  watchingC2/p^2).

  Equivalently: factor Res_{tau_3}(Delta0,Delta1) and test whether the gate D
  togetherwithconditions(i),(ii)forcestheresultanttocarrythe
  eta-rank-one structure. This is a finite Gröbner/resultant computation in
B[tau_1,tu_2] — it needs a working CAS but no asymptoics,anditwould

eitherbankC2=O(p)forthefullt=2,j=3windoworexposethefirst

source-validTheta(q_line)seed.Thatisthesingledecisivenext

construction.
