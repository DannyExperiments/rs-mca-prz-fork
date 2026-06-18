I have what I need. Note: code execution is disabled inthis harness(the
executeCodpermission ws denied and there is no shell ool), so I cnnot run
the finitecheckermyself.TheauditsflagthesameconstraintforCycles
24–29.IwillthereforedelivertheexactreductionIderivedbyhandfromthe
  source-valid c11/c12 conventions, the dimension/density analysis, and a
  runnablecheckerspec—andIwillmarkclearlywhatisprovenversus
  heuristic.

---

EXACT_NEW_WALL

EXACT_NEW_WALL

W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATEdoesnotcloseasO(p).Ireduceittoan
  explicit two-quadric / split-locus incidence problem, show the affine layer
  alonegivesonlythetrivialO(p^2)bound,andshowthehonestexpectationis
  Theta(p^2)=Theta(q_line) (a counterpacket seed), gated on one geometric fact I
cannt certify witou running the checker.

Fieldandparameterledger

  - B = F_p, q_gen = p. F = F_{p^2} = B(alpha), alpha^2 = NR nonsquare. q_line =
  |F|=p^2.q_chalunused,keptseparate.

-D=F_p,n=p.t=sigma=2,j=n-a=r-t=4;eta=2/n,sub-reserve.

-A=F[X]/E,E=X^2+cX+dsource-valid(nonzeroonF_p),separated
  (gcd(E,E^tau)=1); xi_m=[X^m]_E, u=[W]_E, b=[Bnum]_E, ell=[X^p-X]_E, kappa = u
  wedge_Fb!=0(offR0),c_b!=0.

-wedge_F(x,y)=x_0y_1-x_1y_0isthealternatingF-areaformonA~=F^2
  in basis {1,xi}.

  Residue-line / bad-slope incidence calculation only. Not
  list-decoding/CA/MCA/line-decoding/curve-MCA/protocol/SNARK/Proximity-Prize,
  no q_gen/q_line merge.

1.Exactalgebraicsplitcondition(item1)

  From the banked c11/c12 incidence test, a co-support 4-subset T = D\S (always
  adistinct4-subsetofF_pbyconstruction)realizesabadslopeiff,withW=
  L_S Q_S + I_S, L_S = L_D/L_T, L_D = X^p-X:

[I_S]_E=z*bforsomezinF,

  i.e. [I_S]_E and b are F-collinear in the 2-dimensional F-space A. Multiplying
  bytheunitlambda=[L_T]_E(aunitbecauseEhasnoF_p-root,soEis
  coprime to every X-x, x in T) and using [I_S]_E * lambda = iota gives the
clean source-correct gae

Phi(T):=iotawedge_Fmu=0,

iota=u*lambda-ell*[Q_S]_E,mu=b*lambda,lambda=[L_T]_E.

  ThisisthesingleF-valuedequationbehindline_scalar.Twostructuralfacts:

  - The "splits into 4 distinct roots in F_p" requirement is the
  parametrization,notthegate.Writingtau=(tau_1,...,tau_4)=e(T)(elementary
  symmetrics), P_z(X)=X^4-tau_1X^3+tau_2X^2-tau_3X+tau_4 = L_T, which splits
into 4 distinctF_p-roos automatically because T subsetF_pisadistinct

4-set.Equivalently,intheslope→taudirection(offthecurve),P_zsplits

distinctiffP_z|X^p-X.TherealcutisPhi=0.

-lambda,[Q_S]_Eareaffineintau(Q_Sdependsontau_1,tau_2,tau_3only;
  lambda on all four), so Phi is a quadratic form in tau — one F-quadric = two
  B-quadrics.

  Closed form (the useful one). Since (u lambda) wedge_F (b lambda) =
  N_{A/F}(lambda)*(uwedge_Fb)=kappa*N_{A/F}(lambda):

Phi(tau)=kappa*N_{A/F}(lambda)-(ell*[Q_S]_E)wedge_F(b*lambda).

  Splitting lambda = lambda' + tau_4, lambda' = xi_4 - tau_1 xi_3 + tau_2 xi_2 -
  tau_3xi_1(independentoftau_4),and[Q_S]_Eindependentoftau_4:

Phi = kappa*tau_4^2

+tau_4*(kappa*Tr_{A/F}(lambda')-(ell[Q_S]_E)wedge_Fb)

+(kappa*N_{A/F}(lambda')-(ell[Q_S]_E)wedge_F(blambda')).

  The leading kappa*tau_4^2 term is the affine-layer shadow of the Cycle 29 top
  symbolTopSym(det_BM)=-N(kappa)N(z)^2Q_4:samelocator-controlled,
  source-valid-nonzero leading coefficient (kappa != 0).

  2-3. The slope count is not O(p); it is a split-locus incidence (items 2,3,5)

  Let V = { tau in A^4(B) : Phi(tau)=0 }, the intersection of the two B-quadrics
  (theB-componentsofthesingleF-quadricPhi).Threeexactsteps:

  (a) Off-curve bijection. By Cycle 29, off the noninvertibility curve det_B
  M(z)=0(<=4pslopes,keptseparateperitem5)themapz->tau(z)isa
  well-defined rational map, and M(z)tau + C_0(z)=0 is affine in z, so tau
determines z. Hence z <-> T is a bijectionbetween ealizedoff-curveslopes

andbaddistinct4-subsets.Therefore

C2=#{distinct4-subsetsTsubsetF_p:Phi(e(T))=0}+O(p).

  (b) Dimension. Phi=0 is two B-equations in four B-variables. Eliminating the
  singleB-unknowntau_4betweenthetwoB-components(thetau_4^2coefficient
  is kappa != 0, so the resultant is nondegenerate) yields one B-equation in
(tau_1,au_2,tau_3). Thus V is a 2-dimenional variety ofboundeddegree(<=

afew).Theaffine/consistencylayerthatgaveC2<=4patj=3(codim-1

obstructionQ)isgone:atj=4thesystemissquare,thedeterminantisthe

uniquenessdeterminant,andPhi=0iscodim-2ina4-space,i.e.dimension2,

not1.

  (c) Count = split-distinct quartics on V. As T ranges over C(p,4) ~ p^4/24
  distinct4-subsets,e(T)rangesbijectivelyoveralltotally-split-distinct
  monic quartic coefficient tuples. So

C2=#{totally-split-distinctquarticswhosetauliesonV}+O(p).

  |V(F_p)| ~ p^2 (Lang-Weil, if V geometrically irreducible of dim 2). Being
  totallysplitwithdistinctF_p-rootsistheFrobenius/Chebotarevcondition
  "factorization type (1,1,1,1)", which holds for a 1/24 proportion of quartics
when theuniversal quaricX^4 - tau_1X^3+ tau_2 X^2 -tau_3X+tau_4

restrictedtoF_p(V)hasGaloisgroupS_4.Underthatgenericity,

C2~|V(F_p)|/24~p^2/24=Theta(p^2)=Theta(q_line).

  So the O(p) bound is implausible at j=4, and the natural value saturates
  q_line.Thisispreciselythesub-reservecounterpacketseedCycle28/29
  flagged. It is not yet a counterpacket: it needs (i) a growing-prime family of
source-valid(E, Bnum, W) forwhich V is geometrically irreducibleof

dimension2,and(ii)theS_4GaloisconditiononF_p(V)(orweaker:positive

lowerdensityofsplittype),neitherofwhichIcertifyhere.

  The only way C2=O(p) survives is if V is non-generic for splitting: e.g. the
  universalquarticfactorsoverF_p(V)(arootrationalonV),concentrating
  the split locus on a curve. There is no structural reason in Phi = kappa
N(lambda) - (ell[Q_S]) wedge (b lambda) tofrce such factorization,butI

cannotexcludeitbyhand.

  4. Smallest exact next wall + finite-checker spec

  Next wall:

W-F1-AA-RES-T2J4-SPLIT-QUADRIC-IRREDUCIBILITY

  Decide, for source-valid separated off-R0 (E,Bnum,W):

  1. Is V = {Phi=0} geometrically irreducible of dimension 2? (Eliminate tau_4;
  testtheresulting(tau_1,tau_2,tau_3)-surface.)

2.IstheGaloisgroupoftheuniversalquarticoverF_p(V)equaltoS_4
  (density 1/24 split)? — or does the quartic acquire an F_p(V)-rational root
  (splitlocuscollapsestoacurve,restoringO(p))?

1.IsV={Phi=0}geometricallyirreducibleofdimension2?(Eliminatetau_4;
test the resulting (tau_1,tu_2,tau_3)-surface.)
2. Is the Galois roup of he universal quartic overF_p(V)equaltoS_4
(deniy 1/24 split)? — or does th quartic acquir an F_p(V)-rtional root
split locus colapses t a curve, restorng O(p))?

Eitheranswersettlesthegate:S_4/positive-density=>C2=Theta(q_line)
  counterpacket; rational-root collapse => C2 = O(p) and the t=2 law extends to
  j=4.

  Finite-checker spec (directly runnable on the banked module; I could not
  executeithere).Usingc11from
  20260618_cycle11_t2_j2_line_incidence_verify.py:

forpin{5,7,11,13(,17,19)},severalseeds:

c11.set_field(p,NR);D=[c11.b(x)forxinrange(p)];LD=c11.locator(D)

E=c11.random_separated_quadratic(rng);bnum=c11.random_bnum(rng)
    Bres=c11.residue2(bnum,E)

W=c11.interp(D,randomF-valuedvector)

slopes=set()

forTincombinations(D,4):#distinct4-subsets
        LT=c11.locator(T);  Ls,rem=c11.pdivmod(LD,LT)   # rem must be 0

_,Is=c11.pdivmod(W,Ls)

z=c11.line_scalar(c11.residue2(Is,E),Bres)#bad-slopetest

ifzisnotNone:slopes.add(z)

reportC2=len(slopes),C2/p,C2/p^2,off_R0=(kappa!=0)

DECISION:C2/pboundedaspgrows=>O(p)(lawextends);

C2/p^2boundedbelow=>Theta(q_line)counterpacketseed
  confirmed.

  (Also emit, per T, the symbolic check Phi(e(T))==0  <=>  z is not None to
  validatethequadricPhi=kappaN(lambda)-(ell[Q_S])wedge(blambda)
  against the direct division test, exactly as c11/c12 validate their det
against line_scalar.)

Bankablesub-lemma(insidethiswall)

  In the restricted D=F_p, t=sigma=2, j=4, off-R0, source-valid separated c_b!=0
  window:thesplit-quarticgateequalsthevanishingofthesingle
  source-valid F-quadric

Phi(tau)=iotawedge_Fmu=kappaN_{A/F}(lambda)-(ell[Q_S]_E)wedge_F(b
  lambda),

  tau=e(T) for a distinct 4-subset T. Its zero locus V is the intersection of
  twoB-quadricswithleadingcoefficientkappa!=0,hencedimV=2.
  Consequently, via the off-curve z<->T bijection,

C2=#{totally-split-distinctquarticsonV}+O(p),

  so the affine/consistency layer cannot bound C2 below O(p^2): the j<=3
  mechanismprovablyterminatesatj=4.

Dependency list

  - Cycle 11/12: c11/c12 source conventions, Q_S closed form, line_scalar
  bad-slopetest,e(T)-parametrization.

-Cycle16/25:det_BMisthez-freeinvariant;Q(z)fiberseparation;the
  codim-1-obstruction-at-j=3 contrast.

-Cycle24:N(ell)=prod_{a}E(a),source-validnonvanishingofthelocator
  factor.

-Cycle28:Q_4=N(c_b)(Im(d)^2-Im(c)Im(cbard)),source-validnonzero—the
  leading-tau_4^2 coefficient kappa here is the same locator-controlled top
  symbol.

-Cycle29:squaresystem,uniqueoff-curvepre-imagetau(z),topsymbol
  -N(kappa)N(z)^2 Q_4, off-curve z->tau well-defined.

  Hidden assumptions

  - Q_S closed form uses p large enough that W_{n-1..n-4} are genuine top
  coefficients(Cycle11/12hypothesis).

-N_{A/F}(lambda),Tr_{A/F}(lambda')usemultiplication-determinant/traceof
  lambda acting F-linearly on A.

-TheTheta(p^2)valueassumesVgeometricallyirreducibleofdim2andS_4
  (or positive-density) splitting on F_p(V); unproven (this is the wall). The
  O(p)alternativerequiresanF_p(V)-rationalrootoftheuniversalquartic;
  not excluded by hand.

-Nofinitecheckerwasrun(kernelexecutiondisabledinthisharness).The
  spec above converts the wall to a decidable experiment for p=5,7,11,13.

  Rejected overclaims

  - NOT a proof of C2=O(p) for j=4; the j<=3 consistency mechanism provably
  stopshere.

-NOTacounterpacket:nogrowing-primefamily,noprovenirreducibility/S_4,
  no executed scan. Theta(q_line) is the expected, not proven, value.

-NOTaclaimthatPhiforcessplittingdensity1/24;thatisconditionalon
  the next wall.

-Sub-reserve(eta=2/n),local.Nocorrected-reserve,q_gen/q_linemerge,
  q_chal, list/CA/MCA/line-decoding/curve-MCA/protocol/SNARK, or Proximity-Prize
  consequence.

-det_BM(z)=0curvekeptseparate:O(p)slopes,absorbedintothe+O(p)term;
  it neither proves nor refutes the gate.

  Do I see a route to a full solve?

  Yes, but it is a single decidable step, not a closed proof from the desk. The
  split-quarticgateisnowexactly#(Vcapsplit-distinctquartics)withVan
  explicit dim-2 two-quadric variety. The next exact lemma/construction is
W-F1-AA-RES-T2J4-SPLIT-QUADRIC-IRREDUCIBILITY: either provetheuniversal

quarticoverF_p(V)hasanF_p(V)-rationalroot(=>C2=O(p),t=2lawextends

toj=4),orproveVisgeometricallyirreducibleofdim2with

S_4/positive-densitysplitting(=>C2=Theta(q_line)counterpacketseed).The

finitecheckerforpin{5,7,11,13}discriminatesbetweenthetwoinonerun

bytestingwhetherC2/porC2/p^2stabilizes.
