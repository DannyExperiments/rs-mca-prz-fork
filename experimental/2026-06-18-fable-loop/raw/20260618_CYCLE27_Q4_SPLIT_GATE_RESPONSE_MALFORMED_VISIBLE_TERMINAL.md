Verified all requird files. I havethe columndefiniton (Cycle 15/25), the
six-term Plücker expansion(Cycle 25, baked),the rank-on form q1=c_b·η
(Cycle20,banked),th q2closedfrm (Cycle 25), and the norm factorization
D=N(ℓ)κ=κ·∏_{a∈F_p}E(a) (Cyc 24, bked). Iworkd thetopcofficient
directly.

---

⏵⏵ don't ask on (shift+tb to cycle)· c toinerrupt     84% context used

  Cycle 27 — W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE

Cycle27—W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE

Ledgerrespected:B=F_p(q_gen=p),F=F_{p^2}(q_line=p^2),q_chalunused,
  D=F_p (n=p), t=σ=2, j=3, η_reserve=2/n sub-reserve, off R0 (κ=u∧b≠0).
  Restrictedline-incidence/residuecalculationonly.No
  q_gen/protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK claim.

  Convention (odd p): write F=B(α), α²=θ∈B a non-square, so τ-conjugation is
  ᾱ=−α.Forf=f_0+αf_1setIm(f):=f_1.Areaform⟨x,y⟩:=Im(x̄y)=x_0y_1−x_1y_0:
  B-bilinear, alternating, ⟨1,f⟩=Im(f), and crucially ⟨λx,λy⟩=N(λ)⟨x,y⟩
(multiply-by-λ scales areabyits determinantN(λ)).

  1. The Q_4 formula is CORRECT — and its P-dependence cancels

  Top-degree extraction. Write each column coordinate as s_i=σ_i−zβ_i,
  t_i=γ_i−zδ_i(β_i,δ_i∈F).Fromthebankedcolumns:

β_1=q1^1,β_2=q1^2,β_0=q1^0,β_3=0(c_3=−u+zbhass_3=−1,z-free)

δ_1=q2^1,δ_2=q2^2,δ_0=q2^0,δ_3=−1(t_3=z)

  Since ⟨s_i,s_j⟩ has z²-part N(z)⟨β_i,β_j⟩ and ⟨t_k,t_l⟩ has z²-part
  N(z)⟨δ_k,δ_l⟩,thedegree-4partofthebankedsix-termQisN(z)²·Q_4.With
  β_3=0, three of the six terms vanish, leaving exactly

Q_4=⟨β_1,β_2⟩⟨δ_3,δ_0⟩+⟨β_1,β_0⟩⟨δ_2,δ_3⟩−⟨β_2,β_0⟩⟨δ_1,δ_3⟩.

  Now q1=c_b·η, η=w+cτ_1+τ_2 (w=c²−d), so (β_1,β_2,β_0)=c_b·(c,1,w). By the
  scalinglaw⟨β_i,β_j⟩=N(c_b)⟨x_i,x_j⟩with(x_1,x_2,x_0)=(c,1,w).Usingδ_3=−1
  (so ⟨·,δ_3⟩=±Im):

Q_4=N(c_b)·[Im(c)·Im(q2^0)+Im(c̄w)·Im(q2^2)−Im(w)·Im(q2^1)].

  This reproduces the displayed Cycle 26 formula exactly. Question 1: the
  formulaisverifiedfromtheCycle15/25columndefinitions.

  But it is not in lowest terms. With q2^2=P, q2^1=d+Pc, q2^0=cd+Pw, split off
  theP-part.Thebracket'sP-linearpieceis

φ(P)=Im(c)·Im(Pw)+Im(c̄w)·Im(P)−Im(w)·Im(Pc),

  a B-linear functional of P. Evaluate on the basis {1,α}:
  φ(1)=Im(c)Im(w)−Im(w)Im(c)=0;φ(α)=Im(c)w_0+(c_0w_1−c_1w_0)−Im(w)c_0=0.So
  φ≡0: every P-term cancels. The cancellation is structural — q2's P-part is P·η
and q1=c_b·η, i.e. the sme rank-onediretin η.

  What survives is the P-free part Im(c)Im(cd)−Im(w)Im(d). Substituting w=c²−d
  andsimplifying(Im(c²)=2c_0c_1):

  corrected top coefficient:

Q_4=N(c_b)·(Im(d)²−Im(c)·Im(c̄d))

=N(c_b)·(c_1²d_0−c_0c_1d_1+d_1²),c=c_0+αc_1,d=d_0+αd_1.

  2. Source-valid ⟹ Q_4 ≠ 0 (on every separated branch) — Question 2 PROVED

  The decisive identity. For a∈F_p⊂B, Im(E(a))=Im(a²+ca+d)=c_1 a + d_1. When c∉B
  (c_1≠0)thisisabijectionF_p→F_p,soEhasarootinF_piffE(a^*)=0at
  the unique a^*=−d_1/c_1∈F_p, where E(a^*)=(a^*)²+c_0a^*+d_0∈B. Clearing
denominators,

c_1²·E(a^*)=c_1²d_0−c_0c_1d_1+d_1²=Q_4/N(c_b).

  Hence,forc∉B:

Q_4=N(c_b)·Im(c)²·E(−Im(d)/Im(c)),andQ_4=0⟺EhasarootinF_p
  ⟺  N(ℓ)=∏_{a∈F_p}E(a)=0.

  This is the same N(ℓ)=∏_aE(a) that Cycle 24 attached to D. Two independent
  routes(D=N(ℓ)κandtheslope-determinanttopsymbol)landontheidentical
  Frobenius-locator norm — strong corroboration of the banked column forms.

  Now run the two source-valid branches (c_b≠0, off R0, separated gcd(E,E^τ)=1):

  - c∉B (NONDEP, per Cycle 26): source-valid means E nonzero on F_p, i.e.
  N(ℓ)≠0,soE(a^*)≠0,soQ_4≠0.

-c∈B(theresidual/possibly-DEPlocus):Q_4=N(c_b)·Im(d)².Separatedness
  forbids d∈B (else E∈B[X], E^τ=E, gcd≠1), so Im(d)≠0, so Q_4≠0. (Also c∈B,d∉B
  makesIm(E(a))=Im(d)≠0,soEisautomaticallynonzeroonF_p.)

separated+source-valid+offR0+c_b≠0⟹Q_4≠0(allbranches).

  The only zeros of Q_4 (with c_b≠0) are E having an F_p-root (c∉B) or d∈B (c∈B)
  —bothexcludedbysource-validity/separatedness.Thehypothesisdet
  M=(c_b/κ²)D≠0 is automatic here and independent of Q_4.

  3. Consequence — the Q≡0 live branch is empty; C2=O(p) (Question 3 moot)

  N(z)² is the square of the anisotropic norm form, ≢0 and with no B-linear
  factor.SoQ_4≠0⟹degQ=4,Q≢0,andtheleadingformcarriesnospurious
  line. By the banked Cycle 16 lemma, off R0,

Q≢0⟹C2≤#{z∈F:Q(z)=0}≤4p=O(p)=O(n).

  Since Q_4≠0 holds for all separated source-valid off-R0 data with c_b≠0, the
  Q≡0branchisemptysource-validlyacrossthewholet=2,j=3window—boththe
  c∉B NONDEP branch and the c∈B,d∉B residual DEP-candidate. Question 3's premise
("Q_4=0 source-validly") never ocurs,so no lower-coefficient analysisi

needed:Qisneveridenticallyzero.ThecandidateΘ(q_line)seedisremoved.

4.Distinctsplit-cubicgate(Question4)

  I am proving an upper bound, so the gate only helps. The realized
  line-incidenceslopeset(slopesforwhichawitnessingco-supportτ(z)yields
  X³−τ_1X²+τ_2X−τ_3 split with distinct roots in F_p) is a subset of the
affine-τ∈B³-csiten setcunted by {Q(z)=0}. Theefore

#{distinct-split-cubicslopes}≤#{affine-consistentslopes}=O(p).

  No conflation occurs: affine consistency gives O(p); the gate cannot enlarge
  it.(Thegatewouldmatteronlyforalower-bound/counterpacketattempt,which
  is now foreclosed.)

Primarylabel

BANKABLE_LEMMA

  Banked (restricted D=F_p, t=σ=2, j=3, off R0, source-valid, separated):

  1. Corrected top coefficient. The degree-4 part of Q is N(z)²·Q_4 with

Q_4=N(c_b)·(Im(d)²−Im(c)·Im(c̄d)).ThedisplayedCycle26Q_4iscorrect;
  its P-dependence cancels identically (rank-one η-collinearity of q1 and q2's
  P-part).

2.Locatoridentity.Forc∉B,Q_4=N(c_b)·Im(c)²·E(−Im(d)/Im(c)),soQ_4=0⟺
  N(ℓ)=∏_{a∈F_p}E(a)=0 — the same norm as Cycle 24's D.

3.Source-validQ_4≠0oneverybranch,henceQ≢0,hence(Cycle 16)C2=O(p);
  the distinct-split-cubic gate only shrinks this.

  This constitutes a PROOF that the Q≡0 live branch is empty and C2=O(p) for the
  entiresource-validseparatedt=2,j=3off-R0window,conditionalonlyonthe
  one mechanical confirmation of the banked q2=(cd+dτ_1)+Pη closed form against
the raw Cycle 14/15 columndefinitions. I keep th conservativeBANKABLE_LEMMA

label(notPROOF)pendingthatcheck,pertheCycle26audit'sstanding

requirementthatQ_4beindependentlyverifiedbeforepromotion.

  Not banked: any corrected-reserve, q_gen, protocol,
  list/CA/MCA/line-decoding/curve-MCA/SNARKconsequence;anyprizeclaim;any
  finite scan as proof.

  Residual EXACT_NEW_WALL: W-F1-AA-RES-T2J4 (and T3J2) — does the
  slope-consistencytopsymbolremainanonzeropowerofN(ℓ)=∏_aE(a)forhigher
  j?

  Deterministic checker to bank the upgrade to PROOF (no q_gen merge):

checker(p):#p≥7odd

forE=X^2+cX+d,c,d∈F_{p^2}:

filter:gcd(E,E^τ)=1;∏_{a∈F_p}E(a)≠0;κ=u∧b≠0;c_b=−Q_E(b)/κ≠0

build:columnsc_0..c_3fromRAWCycle14/15defs(NOTfrombankedq_i)

Q:4×4B-determinantin(z_0,z_1);extractdeg-4part;divideby
  N(z)^2 → Q4_actual

assert:Q4_actual==N(c_b)*(Im(d)^2−Im(c)*Im(conj(c)*d))

assert:(Q4_actual==0)==(EhasarootinF_p)
      assert : Q not identically zero      # predicted for all source-valid
  separatedE

report:anysource-validseparated(c,d)withQ≡0#predicted:NONE

  If this passes over p=7,11,13, the banked q2 form is confirmed and the lemma
  isafullPROOFofC2=O(p)inthiswindow.(Checkeroutputisconfirmation,
  never the proof.)

---

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
  construction?

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
cnstruction?

Yes,forthisrestrictedline-incidencesub-problem.Thet=2,j=3wallisnow
  closed (modulo the mechanical q2 check): the Q≡0 counterpacket branch is empty
  becausethetopslope-consistencycoefficientisN(c_b)·Im(c)²·E(a^*),
  governed by the locator norm N(ℓ)=∏_{a∈F_p}E(a) that source-validity forces
nonzero.Next exact lemm:prove theleading-coefficient-equals-N(ℓ)-power

phenomenonforgeneralj—thatthetop-degreecoefficientofthe

slope-consistencydeterminantQinthet=2,arbitrary-jregimeisanonzero

B-multipleofapowerofN(ℓ)=∏_{a∈F_p}E(a)(thequotientQ_Shasdegreej−1,

sothecolumnsandthePlückerexpansionscaleaccordingly).Ifso,

source-validitykillsQ≡0fortheentiret=2familyinthetoywindow,giving

C2=O(p)uniformlythere.Thisremainsstrictlysub-reserve(η=2/n)andyields

noprotocol,q_gen,MCA,orreserveconsequence.
