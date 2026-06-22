# Role 08 - Reviewer Checker Engineer

You are the verifier and reviewer-package engineer.

Your task is to design the exact checker/package that would let PRZ or a review
agent verify the source/admissibility status without reading raw transcripts.

Required deliverables:

1. Specify a fail-closed checker or checklist with terminal decisions:

```text
SOURCE_ACCEPTED_CYCLE116_ROW
SOURCE_REJECTED_CYCLE116_ROW
SOURCE_CONTRACT_MISSING_NO_CLAIM
QCHAL_UNDEFINED_FINITE_MCA_ONLY
EVENT_RETAINED
EVENT_CHARGED_OR_EXCLUDED
```

2. State the minimal input files and hashes needed.

3. Include exact clauses the checker cannot machine-verify and must leave as
   symbolic/source-text lemmas.

4. Fix the two known Cycle116 package issues:
   - canonical `A/R` naming;
   - primitive-log gauge mismatch (`X+1` prose vs `beta=X+2` executable logs).

5. Avoid mutable self-test receipts. The Role 08 Cycle116 package had a useful
   checker but its self-test mutates a tamper receipt if run in place. Propose a
   nonmutating harness.

6. If possible, provide pseudocode or a Python skeleton for the source-contract
   checker. Do not require external packages.

Use `PROOF` only if you can make the source/admissibility decision. Otherwise
return a `BANKABLE_LEMMA` checker spec or `EXACT_NEW_WALL`.
