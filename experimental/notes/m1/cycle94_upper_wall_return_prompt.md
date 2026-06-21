# Cycle 94 Prompt: Return To The Upper Residue-Cloud Wall

You are working on RS-MCA / Proximity Prize research.

No Internet. Take all the time to reason you need. Use MAX reasoning.

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. Do you see a route to a full solve? If yes, what is the next
exact lemma or construction?

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not prove?
2. Is the result official-prize-relevant, or only a finite/model/research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are q_gen, q_line, q_code, q_chal, and the 2^-128 target being used correctly?
5. Could quotient/periodic structure, contained incidences, same-slope collisions, or affine color normalization reduce the claimed numerator?
6. If my answer is a PLAN, what exact theorem/checker/counterpacket would convert it into PROOF or COUNTERPACKET?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, or exact counterexample mechanism.

## Current State

Cycle91-93 resolved the lower/failure extension-field detour:

```text
Cycle91: BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL / HARNESS_PARTIAL
Cycle92: AUDIT / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
Cycle93: AUDIT / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL
```

Banked lower-side lemma:

```text
L-CYCLE93-GENERATED-EXTENSION-CYCLOTOMIC-FLOOR
```

For generated extension fields `F_{p^d}` with an order-`N=2^s` subgroup
`H <= F_q^*`, `d=ord_N(p)`, the monomial line `x^{k+1}+z x^k` gives:

```text
|bad slopes| >= sum_{w <= min(k+1,d), w == k+1 mod 2} binom(d,w) 2^w.
```

For `(p,N,d,rho)=(5,256,64,1/16)`, this gives:

```text
epsilon_mca >= 2^-81.31 > 2^-128.
```

But Cycle93 cuts the above-corrected-reserve interpretation:

```text
entropy/tau_star scale cleared,
full quotient-profile corrected reserve not cleared.
```

Thus the lower/failure branch is banked but not the main frontier.

## Target

Return to the main positive/upper wall:

```text
W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
```

The target is not to produce another lower-side quotient-floor row. The target
is to prove, kill, or sharply reduce the upper-side statement:

```text
Lambda^{NC}_{t,delta}(L,k)
  <= n^{1+o(1)} + explicit quotient-profile term
```

uniformly over denominator degree, arbitrary anchors, and all support-wise
line-MCA residue data, above the corrected reserve and after quotient-profile
exceptions are charged.

## Required Tasks

1. Read the normal-form and corrected-reserve source files.
2. State the exact finite upper theorem that would solve the official safe
   side, with all quantifiers and exception terms.
3. Identify the smallest currently unproved sublemma.
4. Decide whether the right next wall is:

```text
W-OFFICIAL-MCA-MATCHING-UPPER-ARBITRARY-ANCHOR-RESIDUE-CLOUD
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
W-LIST-FULL-SUPPORT-INTERSECTION-LOCAL-LIMIT
W-MCA-HIGH-DENOMINATOR-THICK-RESIDUE-COMPRESSION
```

5. Prove a nontrivial restricted case if possible. Prefer a theorem-grade
   finite statement over a broad plan.
6. If no proof is possible, output a dependency DAG and a single exact lemma
   for Cycle95.

## Source Files To Read

Use the mounted project source. Read:

```text
readme.md
agents.md
tex/slackMCA_v3.tex
tex/RS_disproof_v3.tex
experimental/notes/m1/m1_cycle89_official_mca_row_audit.md
experimental/notes/m1/m1_cycle92_extension_field_admissibility_audit.md
experimental/notes/m1/m1_cycle93_corrected_reserve_section7_audit.md
```

## Required Output Format

Start with one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. Exact theorem/counterpacket/route cut.
3. Proof or obstruction.
4. Verification requirements.
5. Next exact lemma or construction.

Do not spend the answer producing a new lower-side quotient-floor construction
unless it is a source-valid counterpacket to the corrected upper theorem.
