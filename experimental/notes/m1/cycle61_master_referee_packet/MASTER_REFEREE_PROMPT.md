# MASTER REFEREE PROMPT — Cycle 61

You are the final Master Planner / Referee for the RS-MCA / Proximity Prize
project.

Do **not** brainstorm from scratch. You are adjudicating:

1. the repository context;
2. the Cycle 58-60 audits and raw returns;
3. the nine Cycle 61 planning answers;
4. the Codex synthesis of those nine plans.

Your job is to choose the route, cut distractions, state the exact next theorem
or verification target, and output a concrete two-round execution plan.

Use MAX reasoning. No Internet. Be blunt. Do not oversell. If the current
route is not convergent, say so and repair it.

## Context Read Order

Read in this order:

1. `rs-mca/experimental/notes/m1/m1_cycle61_planning_synthesis.md`
2. `rs-mca/experimental/notes/m1/cycle61_planning_raw/`
3. `rs-mca/experimental/notes/m1/m1_cycle60_find_the_theorem_audit.md`
4. `rs-mca/experimental/notes/m1/m1_cycle59_5p6_route_repair_audit.md`
5. `rs-mca/experimental/notes/m1/m1_cycle58_5p5_upper_audit.md`
6. `rs-mca/experimental/notes/m1/cycle61_planning_packet/CURRENT_ROUTE_STATE.md`
7. Main source files only as needed:
   - `rs-mca/tex/slackMCA_v3.tex`
   - `rs-mca/tex/RS_disproof_v3.tex`
   - `rs-mca/tex/cs25_cap_v4.tex`
   - `rs-mca/tex/snarks_v4.tex`

## Decision You Must Make

You must choose among at least these candidate priorities:

```text
A. verify Lattes / split-rational registry first;
B. prove support-theoretic split-rational overlap cover first;
C. attack primitive t=1 apolar / generalized-Jacobian base case first;
D. attack scalar list apolar/circuit theorem first;
E. build finite checker and threshold ledger first.
```

You may propose a hybrid, but you must name one **primary** route and one
**backup** route. Do not say "all of the above."

## Required Output

Your answer must have these sections.

### 1. Executive Decision

- One primary route.
- One backup route.
- Confidence levels.
- Whether this is a route to a full solve, a route to route-repair, or a
  kill-test phase.

### 2. Why Other Routes Are Deprioritized

For each candidate A-E, state whether it is primary, backup, parallel support,
or deprioritized. Give the reason.

### 3. Dependency DAG

Give a dependency graph with each node marked:

```text
BANKED
LIKELY
UNKNOWN
FALSE / CUT
VERIFY_FIRST
```

Separate the MCA challenge and the scalar/list challenge.

### 4. Round 1 Execution Plan

Allocate exactly 9 theorem-worker instances.

For each instance, give:

- role name;
- exact wall/lemma;
- prompt objective;
- success criteria;
- failure criteria;
- whether output should be PROOF, COUNTERPACKET, BANKABLE_LEMMA, ROUTE_CUT,
  EXACT_NEW_WALL, AUDIT, or PLAN.

### 5. Round 2 Conditional Plan

Give conditional allocations:

- if Round 1 verifies the chosen route;
- if Round 1 kills the chosen route;
- if Round 1 produces another exception family;
- if Round 1 is inconclusive.

### 6. Human / PRZ Review Priorities

List the exact claims PRZ should inspect first. Do not include broad reading
assignments. Prioritize things that change route decisions.

### 7. Scripts / Checkers To Write

Name the scripts and their exact input/output contracts. Include which claims
they verify or falsify.

### 8. Stop Conditions

State what result means:

- abandon the current route;
- rewrite the primitive theorem;
- stop expanding the quotient taxonomy;
- switch from MCA to scalar list first;
- switch from theorem proving to finite checker first.

### 9. Final Next Lemma

State the exact next lemma or construction. It must be narrow enough to be
assigned to a theorem-worker instance immediately.

## Important Constraints

- Treat Cycle 61 planning answers as `AUDIT / PLAN / CONDITIONAL`, not proofs.
- Do not promote Lattes or divisor-norm packets without verification.
- Do not use `n^{1+o(1)}` as a finite prize certificate.
- Do not hide behind undefined words like "primitive" or "generic."
- Do not propose another broad all-genus/all-`t` theorem unless you also give
  a restricted first lemma and kill test.
- Remember that the final official answer is finite and code-specific, not a
  table of four rate-only constants.
