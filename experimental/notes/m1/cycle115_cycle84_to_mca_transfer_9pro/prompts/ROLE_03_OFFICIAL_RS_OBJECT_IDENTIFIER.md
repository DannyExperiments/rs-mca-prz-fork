# Role 03: Official RS Object Identifier

Use the common prompt. No Internet.

Your role is to identify the exact Reed--Solomon or generalized Reed--Solomon object, if any, that Cycle84 transfers to.

Do not focus on the finite computation. Focus on definitions and parameters.

For every plausible transfer row, fill the ledger:

```text
field F =
evaluation domain D =
is D a smooth multiplicative subgroup/coset? =
code type RS or GRS =
n =
k =
rate rho =
agreement size a or support size |S| =
radius delta =
line family f + z g =
bad-slope numerator =
q_gen =
q_code =
q_line =
q_chal =
target floor(q_line / 2^128) =
whether numerator > target =
first unsupported official-definition condition =
```

Analyze both:

- one-copy Cycle85-style row over `F_17^16`;
- two-copy / extension Cycle88-89-style row over `F_17^48`.

Use `readme.md`, `RS_disproof_v3.tex`, `slackMCA_v3.tex`, `snarks_v4.tex`, and the Cycle85/88/89 audits. Pay special attention to whether a row is merely finite/paper-facing or is actually within the smooth multiplicative RS family that the prize discussion cares about.

End with an exact classification:

```text
OFFICIAL_ROW_IDENTIFIED
FINITE_RS_ROW_ONLY
GRS_ONLY_NOT_RS
ARBITRARY_DOMAIN_ONLY
PRIZE_FAMILY_EMBEDDING_MISSING
Q_LEDGER_FAIL
SOURCE_DEFINITION_FAIL
```

Then justify it.
