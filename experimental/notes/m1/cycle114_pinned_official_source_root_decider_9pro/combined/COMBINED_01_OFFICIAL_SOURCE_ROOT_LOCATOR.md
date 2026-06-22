# Common Prompt - Cycle114 Pinned Official Source Root Decider

NO INTERNET. Do not browse, search, cite online sources, or use external tools.
Use only the attached packet and your own reasoning. Use maximum reasoning.

You are one of nine independent theorem workers on the RS-MCA / Proximity Prize
M1 upper-side route. Try to fully solve the assigned problem. If you cannot
fully solve it, progress as far as possible and isolate the exact next theorem,
checker, or counterpacket mechanism. Be ambitious, but do not overclaim.

Read `CURRENT_CYCLE114_STATE.md`, `MANIFEST.md`, the canonical tracker, the
Cycle111-113 audits, the Cycle112-113 raw response summaries, and the attached
source files in `context/source_docs/` before answering. The source docs include
the repo README/agents files and the TeX manuscripts. If the official source
predicate is absent from those files, say so exactly. Do not invent it.

The active wall is:

```text
V-CYCLE114-PINNED-OFFICIAL-SOURCE-ROOT-P190-OR-C284-DECIDER
```

Cycle113's conservative terminal was:

```text
SOURCE_RECEIPT_MISSING_NO_CLAIM
```

The stress packets to replay are:

```text
p = q_line = q_gen = q_code = 130 * 2^128 + 1
floor(q_line / 2^128) = 130

P190 displayed colors = 190
P190 after one endpoint = 189
P190 full natural t=1 zero-sum supports = 26980
P190 full natural raw colors = 26245

C284 displayed colors = 284
C284 after one endpoint = 283
```

If more than 130 official final free events remain, the final ledger fails:

```text
2^128 * N_free > q_line
```

If at most 130 official final free events remain, the answer must explain the
exact source rejection, exact final-color compression, or exact charge ledger
that reduced the count. Labels are not receipts.

Return under one of these labels only:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Preferred terminal decisions, if you can justify one:

```text
SOURCE_REJECTED:
  name the first official source/APcorr/final-normalization clause that fails,
  with exact calculation and file/theorem/definition reference.

COLOR_COMPRESSED_OR_CHARGED:
  give the exact final retained color map or official charge set, the number
  of colors removed/merged, the cap, and the integer q_line allocation.

SOURCE_VALID_LOW_T1_COUNTERPACKET:
  prove official source adapter and AP_corr acceptance, all charges absent or
  exactly paid, and final retained colors > floor(q_line / 2^128).

T1_APCORR_LOCAL_LIMIT:
  prove official AP_corr plus absence of frozen named charges implies bounded
  interpolation-defect Fourier mass, hence the t=1 local-limit and q_line
  closure.

SOURCE_RECEIPT_MISSING_NO_CLAIM:
  if the packet lacks a necessary official source/APcorr/final-color/charge
  receipt, name exactly which receipt is missing and what would decide it.

RESOURCE_EXHAUSTED_NO_CLAIM:
  if you can specify a valid replay but cannot complete it in this answer.
```

Do not answer with broad language like "probably charged", "periodic", "seems
aperiodic", "source-like", "morally APcorr", or "should compress." A charge is
valid only if it names:

```text
official predicate
exact final retained color subset or quotient map
exact cap
exact q_line allocation
no double counting with free colors or other charges
```

Correct q-ledger discipline:

```text
q_line = sole final color/security denominator
q_gen  = entropy denominator only after a source theorem proves the entropy loss
q_code = code field size / metadata; not a denominator
q_chal = unused absent a protocol transfer theorem
target = 2^128 * N_free <= q_line
```

Explicitly answer whether you see a route to a full solution. If yes, give the
first theorem/checker that would convert your answer into `PROOF` or
`COUNTERPACKET`. If no, give the exact route cut and the first failure line.

Verification bar:

1. State the exact implication proved.
2. State the exact implication not proved.
3. Identify the first line in the reduction chain where the theorem could fail.
4. Use `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target correctly.
5. Check whether quotient/periodic structure, contained incidences,
   same-slope collisions, endpoint effects, affine color normalization, final
   retained normalization, or support/source exclusions reduce the numerator.
6. If you propose a checker, specify its exact inputs, outputs, terminal
   decisions, and no-false-positive/no-false-negative proof.



---

# Self-Audit Addendum

Before finalizing, do a self-audit.

Explicitly answer:

1. What exact implication did I prove, and what exact implication did I not
   prove?
2. Is the result official-prize-relevant, or only a finite/model/source-route
   research certificate?
3. What is the first line in the reduction chain where the theorem could fail?
4. Are `q_gen`, `q_line`, `q_code`, `q_chal`, and the `2^-128` target being used
   correctly?
5. Could quotient/periodic structure, contained incidences, same-slope
   collisions, endpoint effects, affine color normalization, retained-tag
   normalization, or final source exclusions reduce the claimed numerator?
6. If my answer is a `PLAN`, what exact theorem/checker/counterpacket would
   convert it into `PROOF` or `COUNTERPACKET`?

Do not hide behind broad language. Give the exact next lemma, exact missing
hypothesis, exact official source clause, or exact counterexample mechanism.



---

# Role 01 - Official Source Root Locator

Your task is to find the strongest official source root actually present in the
packet. This is a legalistic theorem-source job, not a model-building job.

Search the attached source docs and audits for authoritative definitions or
theorems for:

```text
source adapter
official AP_corr
endpoint convention
final retained K_line color/event map
retained-tag normalization
charge registry
field transfer / q_gen-to-q_line transfer
integer q_line ledger
```

For every object, give the file name and theorem/definition/section label if it
exists. If it does not exist, mark it `MISSING`.

Then decide whether the available source root is sufficient to replay P190 or
C284. Return exactly one of:

```text
SOURCE_REJECTED
COLOR_COMPRESSED_OR_CHARGED
SOURCE_VALID_LOW_T1_COUNTERPACKET
T1_APCORR_LOCAL_LIMIT
SOURCE_RECEIPT_MISSING_NO_CLAIM
```

If the answer is `SOURCE_RECEIPT_MISSING_NO_CLAIM`, name the first missing
official object and the minimal receipt that would decide Cycle114. Do not infer
an official predicate from prior Pro prose.

