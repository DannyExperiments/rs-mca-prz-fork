Code excuon and file writing are denied in this harness (the same
constaint Cycles 19–22reorded), so I worked thealgebraby hand from the
banked Cycle 12/14/20/21/22 multiplcationtable nd the sourcescripts
(cycle11/cycl12 dfine wedge,P_E, he residue pipeline, and L_D = X^p -X
for D = F_p).The result is decisive and does not ned a scn.

---
Primary label

PROOF

  The stratum is empty. Question B is therefore vacuous. This closes the c in B,
  dnotinBportionoftheD=0branchintherestrictedt=2,j=3window.

Direct answer

  Question A: No — the stratum is empty. On c in B, d notin B (separated E), off
  R0,thegateDisforcednonzero.Concretely

D=-mu^2*sigma^2*kappa,sigma^2=c^2/4-d,muinF^*,

  and all three factors are nonzero, so D != 0 everywhere on {c in B, d notin B,
  offR0}.TheextraconditionsDelta1==0,c_b!=0,W_{n-1}!=0nevergeta
  chance to act.

  Question B: vacuous (no points), hence no Omega(p^2) and no O(p) to report on
  thisstratum.

  Proof that D != 0 on {c in B, d notin B, off R0}

  Work in A = F[X]/E, E = X^2 + cX + d, basis {1, xi}, xi = [X]_E, xi^2 = -c xi
  -d.Thesourcescriptsfix

xwedgey=x0y1-x1y0andP_E(x,y)=x0y0-cx0y1+dx1y1;bothare
  confirmed by the banked Cycle 21 expansions

(ellQ)wedgeb=(ellwedgeb)Q0-P_E(b,ell)Q1anduwedge(ellQ)=(u
  wedge ell)Q0 + P_E(u,ell)Q1 (I re-checked (ell·xi) wedge b = -P_E(b,ell) and u
  wedge(ell·xi)=P_E(u,ell)directly).

Step 1 —thelocator residue ell when c inB.

ForD=F_p,L_D=X^p-X,soell=[X^p-X]_E=xi^p-xi.Put

  sigma:=xi+c/2inA,sigma^2=xi^2+cxi+c^2/4=(-d)+c^2/4=
  c^2/4 - d  in F.

  The p-power map is a ring endomorphism of A, semilinear over the Frobenius of
  F.BecausecinBwehave(c/2)^p=c/2,so

sigma^p=(xi+c/2)^p=xi^p+c/2.

  But sigma^2 = c^2/4 - d in F, hence sigma^{p-1} = (sigma^2)^{(p-1)/2} in F;
  writemu:=sigma^{p-1}-1inF,sosigma^p=(mu+1)sigma.Then

ell=xi^p-xi=(sigma^p-c/2)-(sigma-c/2)=sigma^p-sigma=mu*
  sigma.

  So ell = mu * sigma with mu in F, sigma = (c/2, 1) in coordinates.

  mu != 0: if mu = 0 then ell = 0, i.e. X^p == X (mod E), i.e. both roots of E
  lieinF_p,forcingEinB[X]anddinB—contradictingdnotinB.Hencemu
  != 0.

  Step 2 — the four forms collapse onto sigma.

Sinceell=musigma,bilinearitygivesg1=mu(sigmawedgeb),g2=mu
  P_E(b,sigma), h1 = mu (u wedge sigma), h2 = mu P_E(u,sigma). Therefore

D=g1h2+g2h1=mu^2[(sigmawedgeb)P_E(u,sigma)+P_E(b,sigma)(uwedge
  sigma) ].

  Step 3 — evaluate the bracket. With sigma = (c/2, 1), b = (b0,b1), u =
  (u0,u1):

sigmawedgeb=(c/2)b1-b0,P_E(u,sigma)=-cu0/2+du1,

P_E(b,sigma)=-cb0/2+db1,uwedgesigma=u0-cu1/2.

  Multiplying and summing, the b1u1 and b0u0 terms cancel and the cross terms
  combineto

(sigma wedgeb)P_E(u,sigma) +P_E(b,sigma)(u wedg sigma)

=(c^2/4-d)(b0u1-b1u0)

=-sigma^2*kappa,

  using b0 u1 - b1 u0 = -(u0 b1 - u1 b0) = -kappa. Hence

  D = -mu^2 * sigma^2 * kappa.

  Step 4 — nonvanishing.

  - kappa != 0 (off R0, given);

-mu!=0(Step1,sincednotinB);

-sigma^2=c^2/4-d!=0,becausec^2/4inBwhilednotinB,soc^2/4-d
  notin B, in particular != 0.

-kappa!=0(offR0,given);
mu !=0 (Step 1, since d notinB);
sigma^2= c^2/4 - d !=0, because c^2/4inBwhilednotinB,soc^2/4-d
notn B, inparticular != 0.

ThereforeD!=0.TheconditionscinB,dnotinB(separated),offR0,andD
  = 0 are mutually inconsistent: the stratum is empty. ∎

  (Equivalently: D = 0 off R0 forces mu sigma^2 = 0. sigma^2 = 0 is discriminant
  ramificationdisc=c^2-4d=0;mu=0isEinB[X]non-separation.Both
  are excluded by the stratum hypotheses, so the alignment gate cannot vanish
there all.)

  Why this is consistent with — and sharper than — Cycle 22

  Cycle 22's (DECOUPLE) identity Im_alpha(J_A) = 2 Im_alpha(d) + Im_alpha(c) f_2
  provedalignmentimpossibleonthisstratumconditionalonthestratumbeing
  nonempty. The present computation removes the conditional in the strongest
possibleway: on c n B, dntin B (off R0) the knel gateDisidentically

nonzero,sothelocusD=0itconditionedondoesnotexist.ThebankedCycle

21fact"D!=0blockssimultaneousbranchcollapse"thensaysdirectlythat

simultaneousslope-collapseisimpossiblehere—noneedtoinspectJ_Aat

all.

  So Cycle 22's Im_alpha(J_A) = 2 Im_alpha(d) and the present D = -mu^2 sigma^2
  kappaaretwoconsistentwitnessestothesamestructuralfact:thecinB
  separated stratum lives strictly off the D=0 kernel.

  Sharpened live wall (where a Theta(q_line) seed could still hide)

  D = 0 off R0 is now pinned to the complementary geometry:

W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C:

D=0,offR0,Eseparated==>cnotinB(equivalentlyIm_alpha(c)!=
  0).

  This is the only surviving lane. There Cycle 22's (DECOUPLE) does not force
  impossibility;alignmentinsteadneedsthesingleextrascalarf_2=-2
  Im_alpha(d)/Im_alpha(c) plus Re(J_A)=0. The relocated question is whether {c
notin B,Delta1==0, D=0, off R0} is nonmpty and, if so,itssplitcount.

  A byproduct I verified by hand and bank as a tool for that lane (no scan
  needed):onanyDelta1==0point(p1+q2,detPinB[tau]),

delta_z := (p1+q2)^2 - 4 deP in B[tau_1,tau_2]   (degree2),

tau_3=((p1+q2)-/+sqrt(delta_z))/2,z=(p1-tau_3)/(c_beta)=
  ((p1-q2) +/- sqrt(delta_z))/(2 c_b eta),

  so on Delta1==0 the landing condition is exactly delta_z(tau_1,tau_2) in
  QR(F_p),andA/kappaisafunctionofetaaloneiffJ_A=0(alignment).Hence
  on any nonempty alignment-failing Delta1==0 point the slope does not collapse
toeta, giving the lower ound C2 = Omega(p) per ta-fibre;theOmega(p^2)vs

O(p)splitthenreducestoasinglefinitecross-fibreslope-collisioncount.

ThisisthepreciseresidualobjectforthecnotinBlane—butitisnot

invokedforthepresentstratum,whichissimplyempty.

  Inline checker specification (Write denied; copy to output_files/CHECKER.py)

  Identity-confirmation only, not the proof:

Forpin{7,11,13,17,19},NRanonresidue,F=F_{p^2},A=F[X]/(X^2+cX+d):

formany(cinB,dwithIm(d)!=0,u,bwithkappa=u∧b!=0):

ell=residueofX^p-XmodE#expectell==mu*(c/2,1)forscalar
  mu

g1=ell∧b;g2=P_E(b,ell);h1=u∧ell;h2=P_E(u,ell);D=g1*h2+g2*h1

assertD==-mu^2*(c^2/4-d)*kappa#closedform

assertD!=0#emptinesswitness

Report:zerocounterexamplesexpectedoverallsampled(cinB,dnotinB).

  Ledger discipline: q_gen=p and q_line=p^2 kept separate; eta=2/n stays
  sub-reserve;noprotocol/list/line/CA/MCA/curve-MCA/SNARKconsequence;no
  internet; no scan cited as proof (the proof is the closed form in Steps 1–4).

  Banked vs not

  Bank (proven, exact, restricted D=F_p, t=sigma=2, j=3, off R0): ell =
  [X^p-X]_E=mu*(xi+c/2)forcinB;theclosedformD=-mu^2sigma^2kappa
  with sigma^2 = c^2/4 - d; the corollary {c in B, d notin B, D=0, off R0} is
empty, henceQuestion A negative andth inB pat oftheD=0branchclosed;

andtheDelta1==0landingcriteriondelta_zinQR(F_p)withtheexplicit

tau_3,zformulasandthecollapse-iff-J_A=0dictionary.

  Do not bank: nonemptiness or split count in the c notin B lane; any C2 bound
  there;anyTheta(q_line)counterpacket;anythingat/abovecorrectedreserve;
  any q_gen, protocol, list/line/curve-decoding, CA, MCA, or SNARK consequence.

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
  construction?

  Not a Prize solve — this is the sub-reserve eta=2/n toy window, so closing it
  closesonlytherestrictedt=2,j=3local-F1wall.Butthereisnowasharp
  route. This cycle closes the c in B half of the D=0 branch outright (empty).
The nexexact step is hemirror computation the onlysurvivinglane:

NEXTEXACTLEMMA(cnotinBlane;finite,CAS-checkable,noasymptotics):

Computeell=[X^p-X]_EforcnotinB.Now(c/2)^p!=c/2,sotheStep-1

collapseell=mu*(xi+c/2)fails;insteadxi^pisthesecondrootofE^tau
  in A

andellisagenuine2-dimensionalA-element.Re-deriveDinclosedform:

D=(ellwedgeb)P_E(u,ell)+P_E(b,ell)(uwedgeell)

asabilinearformin(u,b)withcoefficientsinFdeterminedby(c,d)and
  the

Frobeniusimagexi^p.DecidewhetherD=0(offR0)issolvablejointlywith

Delta1==0andIm(c)!=0(thef_2=-2Im(d)/Im(c)gate).

Then,onanysolution,applythebanked'delta_zinQR(F_p)'landing
  criterion and

settlethecross-fibreslope-collisioncount:Omega(p^2)=>first
  source-valid

Theta(q_line)seed;O(p)=>thewholeD=0branchclosesandC2=O(p)inthis
  window.

  The decisive reduction this cycle delivers: the D=0 branch is no longer a
  two-parameter(c,d)surfacetosearch—itisforcedentirelyintocnotinB,
  and the gate there is one explicit bilinear-form vanishing plus one finite
collision count.
