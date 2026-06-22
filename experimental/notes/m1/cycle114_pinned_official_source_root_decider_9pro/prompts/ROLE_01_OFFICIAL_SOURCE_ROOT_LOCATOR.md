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

