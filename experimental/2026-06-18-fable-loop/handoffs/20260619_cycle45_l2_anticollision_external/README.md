# Cycle 45 External Packet: L2 Anticollision Wall

Status: EXTERNAL_MODEL_PACKET / AUDIT.

Purpose: run six fresh external 5.5 Pro-style instances against the exact wall
created by Cycle 44:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION
```

This packet is not a claim. It is a prompt bundle for independent proof,
falsifier, source-audit, checker, homerun, and obstruction-reduction attempts.

Use no internet. Keep the ledgers separate:

```text
q_gen = p
B = F_p
F = F_{p^2}
q_line = p^2
q_chal = unused
D = F_p
deg E = t = sigma
A = F[X]/E
j = |T| = n-a
```

Core banked Cycle 44 identity:

```text
rho(T) = [I_{D\T}]_E = -ell * Lambda(T)^(-1) * N(T),
N(T)=sum_{d in D} w(d)L_T(d)(xi-d)^(-1).
```

Core target:

```text
M_2 = sum_z nu(z)^2 <= #Land + (1+o(1)) #Land^2/q_line.
```

Core falsifier:

```text
max_z nu(z) >= #Land/p^(1+epsilon)
```

for a source-valid growing family.

Read order:

1. `PROMPT_COMMON.md`
2. `ROLE_PROMPTS.md`
3. `MANIFEST.md`
4. Attachments listed in `MANIFEST.md`.
