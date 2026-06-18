Ihave compted the invstigation. File-writing, code-excution (Jupyter),
and shll are alldnied in this harnes, soI cannot bank afreshly-run
certificate or write to output_files/. I delivr everything inline, wichis
sufficient because the obstruction turned out to be a single mistypedline
that I can repair and audit statically against alreay-validate machinery.

---

⏵⏵ don't ask on (shift+tb to cycle)· c toinerrupt    100% context used

  Cycle 38 Homerun Result — W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT

Cycle38HomerunResult—W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT

Classification:AUDIT(checkerrepair,provablestatically)+BANKABLE_LEMMA
  (source-validity gates, explicit constants) + EXACT_NEW_WALL (symbolic
  certificate+good-reduction)+EXPERIMENTAL(theonefinitefactstill
  needing a run). No PROOF, no COUNTERPACKET, no S_4 banked.

  1. Root-cause diagnosis (exact, single line)

  The Cycle 37 checker fails at line 133 of …_unrun_model_checker.py:

w1,w2,w3,w4=(OF,ZF),(ZF,OF),(OF,OF),(OF,ZF)#W_{n-1..n-4},fixedfree
  data

  OF=(1,0), ZF=(0,0), ALPHA=(0,1) are F-elements (pairs of ints). But w1..w4 are
  consumedonlyinsideqresviafmul/fsub,whichrequireF-elements.The
  literals above are residue-pairs (pairs of F-elements, i.e. elements of
A=F[X]/E). So fmul(w1,t1) computes ((OF,ZF)[0]*… )%P = tuple % int →

TypeError:unsupportedoperandtype(s)for%:'tuple'and'int'

  The author conflated two type layers and also conflated the residue variable X
  withthefieldgeneratoralpha.TheCycle37JSONitselfstatestheintent:
  W_{n-1..n-4} = 1, alpha, 1+alpha, 1. As F-elements that is OF, ALPHA,
OF+ALPHA, OF. Nothing elseinthe filei mistyped (, b_res, ell ar

correctlyresidue-pairs;lamcorrectlyliftstau_ito(x,0)).

  2. The repair (minimal, 1 line) + static-equivalence audit

  Replace line 133 with:

w1,w2,w3,w4=OF,ALPHA,fadd(OF,ALPHA),OF#W_{n-1..n-4}=1,alpha,1+alpha,1
  (F-elements)

  Everything else in the Cycle 37 file is left unchanged. I audited the
  correcteddata-flowline-for-lineagainstthevalidatedCycle32reference
  (20260618_cycle32_t2_j4_monodromy_histogram.py, whose histograms already match
direct support enumerationoff Deta=0):

  ┌┬┬┐
  │Cycle38function│Cycle32reference│structuralmatchafterfix│
  ├┼┼┤
└───────────────────┴────────────────────┴────────────────────────────┘

─┬─┬───┐
 │     Cycle 32 refrence      │ structural match │
│                    │                             │      after fix    │
├─┼─┼───┤
│qres(tau)(q3=w1;│q_residue_from_tau(q3=Wn1;│identical;w_i=Wn_i│
  │ q2=w2−w1·t1; …)    │  q2=Wn2−Wn1·tau1; …)        │  now both           │
  │││F-elements✓│
  └┴┴┘

Cycle 38 function: qres(tau) (q3=w1; q2=w2−w1·t1; …)
Cycle 32 reerence:q_residue_from_tau (q3=Wn1;q2=Wn2−Wn1·au1;…)
structuralmatchafterfix:identical;w_i=Wn_inow bothF-elments✓
──
Cycl 38 function: lam(tau) (XI[4]−t1·XI[3]+t2·XI[2]−t3·XI[1]+t4)
Cycle 32 reference:lambda_from_tau
structuralmatchafterfix:identical✓

  Cycle 38 function: eqres ((u−z·b)·lam − ell·qres)
  Cycle32reference:equation_residue
  structural match after fix: identical ✓

  Cycle 38 function: build (finite-difference columns)
  Cycle32reference:solve_tau_for_z
  structural match after fix: identical ✓

  Hand-lemma making build correct: eqres(z,·) is affine-linear in tau (lam is
  linearintau_1..tau_4;qresisaffine-linear;(u−zb)andellaretau-free).
  Hence eqres(z,e_i)−eqres(z,0) is exactly column i of M(z), and M(z)tau=−C_0(z)
isrecoveredcorrectly.

  The only difference from Cycle 32 is that Cycle 32 derives (u, W_{n-1..n-4},
  b)fromonerandominterpolatedW,whereasCycle38fixesthemasexplicit
  source-valid free data. So the repaired checker is correct relative to
validated machinery; whether it passes(types"4" and "13"appear off Delta)

istheoneremainingempiricalfact.

  Optional hardening to make any run self-validating (prepend to __main__):

assertP%4==3andall((x*x)%P!=(P-1)forxinrange(P))#-1
  nonresidue

#affine-linearityself-check(guaranteesbuild()extractsMcorrectly):
  import random; rng = random.Random(1)

for_inrange(20):

z=(rng.randrange(P),rng.randrange(P));a=[rng.randrange(P)for_in
  range(4)]; bb=[rng.randrange(P) for _ in range(4)]

f0=eqres(z,[0,0,0,0]);fa=eqres(z,a);fb=eqres(z,bb);
  fab=eqres(z,[(a[i]+bb[i])%P for i in range(4)])

assertrsub(fab,f0)==rsub(rsub(fa,f0),rsub(f0,fb))#f(a+b)-f0==
  (fa-f0)+(fb-f0)

  3. Source-validity gates — hand-verified with explicit constants
  (BANKABLE_LEMMA/AUDIT)

  For p ≡ 3 mod 4, alpha^2=-1, E=X^2+alpha X+1, b=[Bnum]_E=X, free data
  u=[W]_E=1+X,(W_{n-1},…,W_{n-4})=(1,alpha,1+alpha,1):

  1. No F_p root. E(a)=(a^2+1)+alpha·a; the alpha-part is a, zero only at a=0,
  andE(0)=1≠0.✓

2.E/E^tauseparated.E−E^tau=2alphaX;acommonrootforcesX=0,butE(0)=1.
  ✓

3.c∉Bbranchactive.c=alpha∉F_p⇒c_b≠0.✓

4.kappa=u_0.kappa=wedge_F(u,[b]_E);[b]_E=(0,1)so
  wedge((u_0,u_1),(0,1))=u_0. With u=1+X, kappa=1≠0. ✓

5.Topsymbolnonzero.c=alpha,d=1⇒Im(c)=1,Im(d)=0,
  Im(conj(c)d)=Im(−alpha)=−1, so Q_4=N(c_b)·(0−1·(−1))=N(c_b)≠0. Hence
  TopSym(Delta)=−N(kappa)N(z)^2Q_4isanonzeropolynomial,Deltaisnot
  identically zero, and the singular locus Delta=0 contributes ≤4p=O(p) slopes
(Cycle 33 L-T2J4-A2B-SINGULAR-OP). ✓

  New gate (closes a source-validity gap Cycle 37 left implicit). The checker
  setsu=[W]_Eand(W_{n-1..n-4})independently.Thisisgenuinelysource-valid:
  interpolation F^n→\{deg≤n-1\} is a bijection, and W↦([W]_E, \text{top-4
coeffs})i an F-linear map F^n→F^2×F^4 tha is sujecivefor n≥6 (the

residuefunctionalrestrictedtoX^0,…,X^{n-5}alreadyhitsallofF[X]/E

sinceitcontains1,X).Forp0=31,n=31≫6,andanyw∈F^nsplitsasw_0+alpha

w_1withbaseanchorsw_0,w_1∈B^n.Sotheexplicitfreedataisrealizedbya

genuinesource-validbase-anchorword.✓

4.Whatremainsunverifiableinthisharness

  Only one fact: that the off-Delta squarefree specializations of L_tau on some
  linez_1=mz_0+eatp0=31includebothtype"4"(4-cycle)andtype"13"
  (3-cycle). The corrected Cycle 35/36 criterion is enforced (transitivity comes
from the4-cycle, not the forbidden "irreducible resolvent+ nonsquare dic"

shortcut;theeventype"13"simultaneouslykillsthesignconstant-field

obstruction,sinceG_geom∈\{A_4,S_4\}andanevendegree-oneFrobeniusis

impossibleifG_geom=A_4).TheCycle32randominstanceatp=29already

exhibited"4","13","1111"inS_4proportions,sogenericoccurrenceis

well-evidenced—butthespecificfreedatacouldinprinciplebenon-generic

(aforcedsquaredisc_numwouldpushintoA_4andsuppress"4").Thatriskis

exactlywhytherun,withtheself-checksabove,isthecheaphigh-information

nextaction.PerCycle37disciplineIdonotassertarunoccurredanddo

notbankthecertificate.

  5. Route assessment and exact next steps

  The chain is intact and now unblocked: Cycle 33 (singular O(p)) + Cycle 34
  (off-curvebirationalontotheCycle30quadric,rank-2,surface-sized)+
  Cycle 35 (finite-place S_4 ⇒ Theta(p^2/24) split density in the local branch)
+ Cycle 36 (explicit family, reductionto onegood prime)+ Cycle 38 (working

checker).TheremainingmathematicsisgeometricS_4ofL_tau/\bar

F_p(z_0,z_1),uniformlyinp.

  Sharpened EXACT_NEW_WALL (replaces the finite-scan dependence):

W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED

(a)Computedisc_num(z_0,z_1)andresolventR(y)symbolicallyfrom

tau_i=detM_i/DeltaforE=X^2+alphaX+1,b=X,u=1+X,W=(1,alpha,1+alpha,1).

(b)Provedisc_numhasnonconstantsquarefreepartandR(y)isabsolutely

irreducibleover\barF_p(z_0,z_1),plusoneexplicit"4"slicefor
  transitivity.

(c)ProveL-T2J4-A2B-GOODRED:(a),(b)aregood-reduction-openinthep=3mod4

family,soonegoodprimepromotesG_geom=S_4toallbutfinitelymanyp,

withtheexcluded-primesetrecorded;thenauniform-complexityLang-Weil

countyieldsC2=p^2/24+O(p^{3/2})=Theta(q_line)inthislocal
  branch.

  Obstruction ranking for the promotion, by risk: (i) a hidden forced square
  factorindisc_numpeculiartothissymmetricE,bchoice(wouldbea
  ROUTE_CUT); (ii) constant-field drift across the family (cut conditional on
geometric S_4, mut be re-checked uniformly);(iii) niform contrl of the

Lang-Weilerrorsoitdoesnotswampthep^2/24mainterm.

---

  Do you see a route to a full solve? If yes, what is the next exact lemma or
  construction?

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
cnstruction?

Nottoafullprize-levelsolve,andtherouteboard'sledgerseparations
  forbid promoting any of this past a restricted local t=2,j=4 sub-reserve
  object(nomergeofq_gen=pwithq_line=p^2;no
  MCA/CA/list/line/curve-MCA/protocol/SNARK status). But there is a concrete
two-steproute to the nextreal milestone (he uniform/growing-prime

Theta(q_line)counterpacketseed):

  1. Single-prime confirmation (one run away): apply the one-line repair of §2
  andruncycle38_checker.pyatp0=31;aPASS(types"4"+"13"offDelta)banks
  G_geom=G_arith=S_4 for that instance via Cycle 35's certificate.

2.Nextexactlemma—L-T2J4-A2B-GOODRED:provethesymbolic
  disc_num/resolvent conditions of §5(a,b) and that they are good-reduction-open
  inthep≡3mod4family,promotingonegoodprimetoalmostallprimes,then
  attach a uniform-complexity Lang-Weil count. That converts the conditional
see ino a geuine resriced localThta(q_le) counterpacket seed —still

strictlysub-reserve,neveracorrected-reserveorprizestatement.
