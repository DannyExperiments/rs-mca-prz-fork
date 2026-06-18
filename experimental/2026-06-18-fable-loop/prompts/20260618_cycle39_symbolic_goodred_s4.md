# Cycle 39 Prompt: Symbolic Good-Reduction S4 Gate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA / Proximity Prize Fable loop as a skeptical
mathematical co-director. Work only from mounted repository/context files. Do
not use web access. Keep these ledgers separate:

- `q_gen`
- `q_line`
- `q_chal`
- `B`
- `F`

Do not promote any statement to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, prize, or `COUNTERPACKET` status
unless the exact source hypotheses are proved.

## Current Target

Attack exactly:

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
```

Cycle 38 repaired the Cycle 37 checker type error and Codex locally verified
that the patched checker passes at `p=31` for the explicit family. This is only
finite-place `EXPERIMENTAL / AUDIT` evidence. The missing theorem is a
symbolic good-reduction or monodromy bridge.

## Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`
- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `ROUTE_BOARD_CURRENT.md`

Use `.tex` files only if you need exact source definitions or hypotheses.

## Explicit Family

Work in the restricted branch:

```text
p = 3 mod 4
B = F_p
F = F_{p^2} = B(alpha)
alpha^2 = -1
D = F_p
q_gen = p
q_line = p^2
t = sigma = 2
j = n-a = r-t = 4
E = X^2 + alpha X + 1
b = X
u = [W]_E = 1 + X
W_{n-1..n-4} = 1, alpha, 1+alpha, 1
```

The Cycle 38 patched checker at `p=31` reports:

```text
hist = {"1111": 1, "112": 5, "13": 11, "22": 6, "4": 6, "nonsquarefree": 2}
witness_4cycle = [0,0]
witness_13 = [4,4]
resolvent_irred_at = [4,4]
disc_nonsquare_at = [0,0]
PASS_S4_finite_place = true
```

Treat this as finite evidence only unless you prove the bridge.

## Required Output

Choose the strongest route you can justify. Acceptable outcomes:

1. **PROOF / BANKABLE_LEMMA:** a symbolic or good-reduction proof that the
   explicit family has the needed geometric/arithmetic `S_4` behavior on a
   growing-prime set.
2. **EXACT_NEW_WALL:** a sharper obstruction below symbolic good reduction,
   with the next exact lemma stated.
3. **ROUTE_CUT:** a proof that this `A^2_B`, `t=2,j=4` route cannot yield the
   desired source-valid counterpacket seed.
4. **EXPERIMENTAL / AUDIT:** a stronger checker/certificate, preferably with
   symbolic discriminant/resolvent data and good-prime exclusions.

If you can write deliverables, write only under `output_files/`.

Preferred deliverables:

- `output_files/cycle39_symbolic_goodred_result.md`
- `output_files/cycle39_symbolic_goodred_checker.py`
- `output_files/cycle39_symbolic_certificate.json`
- `output_files/cycle39_next_prompt.md`

Use these labels literally:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `EXPERIMENTAL`

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
