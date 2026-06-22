# Role 06: q-Ledger And Status Auditor

Use the common prompt. No Internet.

Your job is to audit all field sizes, denominators, and status claims.

Compute exactly:

```text
17^16
17^32
floor(17^16/2^128)
floor(17^32/2^128)
52,747,567,092 / 17^32
```

Then classify:

```text
q_gen
q_code
q_line
q_chal
```

for the native and smooth lifted rows.

Decide whether the statement

```text
epsilon_mca(C,125/256) > 2^-128
```

is mathematically correct, and whether it is protocol/prize meaningful.

Deliverable: a field-ledger table and exact warning language preventing the standalone certificate from overstating the result.
