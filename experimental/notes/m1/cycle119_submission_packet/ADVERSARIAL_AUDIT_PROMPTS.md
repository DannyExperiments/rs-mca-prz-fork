# Adversarial Audit Prompts

Use these prompts for hostile expert/model review. Do not ask for encouragement. Ask for fatal lines.

## Prompt 1: Kill The Two-Ended Theorem

```text
You are auditing a claimed two-ended locator-to-LD_sw theorem.

The theorem assumes monic degree-j locators P_J with:
  deg(P_J-P_J') <= j-sigma+1
  P_J(0)=c != 0

It claims that the selected product coefficients
  [X^0](P_J A), [X^{j+1}](P_J A), ..., [X^{j+sigma-1}](P_J A)
recover A in F[X]_<sigma by one J-independent linear map, giving one
functional ell with ell(P_J A)=A(beta).

Then the weighted Vandermonde parity-check argument constructs one line f+zg
with z_J=-1/P_J(beta), support S_J=D\J, explaining codewords, and uniform
noncontainment.

Your task:
  Find the exact fatal line, if any.
  Check especially:
    the coefficient recovery;
    the W_J^perp identification;
    the syndrome-line construction;
    surjectivity and right inverse;
    Vandermonde noncontainment;
    hidden use of a missing top coefficient.

If the theorem is correct, return PROOF with the shortest rigorous verification.
If it fails, return ROUTE_CUT with the first false statement.
```

## Prompt 2: Kill The Cycle84 Instantiation

```text
You are auditing the Cycle84 instantiation of the two-ended theorem.

Claimed facts:
  K=F_17^32
  H=<theta>, |H|=512
  native |J_T|=113
  P_T=X^113-X^112+O(X^107)
  P_T(beta)=4(beta-1)Phi(T)
  #{Phi(T)}=52,747,567,092

Augmentation:
  A*={theta eta^i: 0<=i<=119}, |A*|=120
  R*={theta eta^i: 120<=i<=255}, |R*|=136
  J_T*=J_T union R*
  P_T*=P_R*P_T
  j=249, sigma=7

Claim:
  deg(P_T*-P_T'*) <=243=j-sigma+1
  P_T*(0) is common nonzero
  P_T*(beta)=fixed_nonzero_scalar*Phi(T)
  hence LD_sw(RS[K,H,256],263)>=52,747,567,092.

Your task:
  Find any arithmetic, degree, scalar, support-size, field, or collision error.
  Pay special attention to P_T(0)=-1, P_R*(0)!=0, beta notin H,
  and whether multiplication by P_R* introduces collisions.

Return PROOF if clean, or ROUTE_CUT with the first fatal clause.
```

## Prompt 3: Kill Official Prize Admissibility

```text
You are auditing whether the finite theorem implies an official Proximity Prize
negative result.

Finite theorem:
  C=RS[F_17^32,H,256], |H|=512
  LD_sw(C,263)>=52,747,567,092
  distance <=249 < 250=(125/256)*512
  source epsilon_mca >= 52,747,567,092/17^32 > 2^-128

Your task:
  Compare this theorem line by line to the official ABF/Proximity Prize grand
  MCA challenge.

Check:
  1. Are extension fields F_17^32 admitted?
  2. Is H=<theta> a permitted smooth domain?
  3. Is support-wise same-support noncontainment the official epsilon_mca?
  4. Is gamma sampled uniformly from F_17^32?
  5. Are endpoint, quotient, periodic, charge, duplicate, or event-retention
     filters absent?
  6. Is n=512/rate=1/2 within the target envelope?

Return:
  OFFICIAL_ACCEPT if the implication is valid;
  OFFICIAL_REJECT with the first rejected clause;
  OFFICIAL_UNKNOWN with the missing source clause.
```
