# Cycle 38 Homerun S4 Repair Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible-terminal scrape is preserved only as harness
provenance and is not used as mathematics. The readable Claude structured JSONL
recovery was source-audited conservatively, and Codex ran one bounded local
checker repair.

Source artifacts:

- `raw/20260618_CYCLE38_HOMERUN_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE38_HOMERUN_RAW.json`
- `raw/20260618_CYCLE38_HOMERUN_RUN_RESULT.json`
- `raw/20260618_CYCLE38_HOMERUN_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE38_HOMERUN_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE38_HOMERUN_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_result.txt`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_stderr.txt`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`, with `alpha^2=-1`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Candidate family: primes `p = 3 mod 4`,
  `E=X^2+alpha X+1`, `b=X`.

This remains a restricted residue-line / finite-place monodromy calculation.
It is not a corrected-reserve theorem, MCA claim, list-decoding claim, CA
claim, line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## What Cycle 38 Found

Cycle 38 identified the exact type error in the Cycle 37 inline checker. In
`local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`,
the line

```python
w1,w2,w3,w4=(OF,ZF),(ZF,OF),(OF,OF),(OF,ZF)
```

sets the four top free coefficients to residue-pairs of `F`-elements. Later
`qres` consumes these as `F`-elements using `fmul` and `fsub`, causing the
local crash

```text
TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
```

This is a checker implementation error, not a source-validity failure of the
explicit family.

## Banked Checker Repair

Cycle 38 proposes, and Codex locally verified, the one-line repair

```python
w1,w2,w3,w4=OF,ALPHA,fadd(OF,ALPHA),OF
```

This means

```text
W_{n-1..n-4} = 1, alpha, 1+alpha, 1
```

as actual `F`-elements. The repaired free data remains consistent with the
previous source gates:

- `E(a)=(a^2+1)+alpha*a`, so `E` has no root on `D=F_p`.
- `E-E^tau=2 alpha X`, so a common root would force `X=0`, but `E(0)=1`.
- `c=alpha notin B` and `c_b != 0`.
- `u=1+X`, so `kappa=u_0=1`.
- The Cycle 28/29 top symbol remains nonzero: `Q_4=N(c_b) != 0`.
- The Cycle 33 singular determinant curve bound still isolates the
  `Delta=0` bad locus.

Codex copied the Cycle 37 checker to
`local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`,
patched only this line, and ran it with no dependency installation.

Execution receipt:

```text
command=python3 experimental/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py
returncode=0
```

The checker output at `p=31` is:

```json
{
  "p": 31,
  "q_gen": 31,
  "q_line": 961,
  "NR": -1,
  "family": "E=X^2+alphaX+1,b=X,nr=-1",
  "free_data": {
    "u": "1+X (kappa=u0=1)",
    "W_{n-1..n-4}": "(1),(alpha),(1+alpha),(1)"
  },
  "line": {
    "m": 1,
    "e": 0
  },
  "singular_on_line": 0,
  "hist": {
    "1111": 1,
    "112": 5,
    "13": 11,
    "22": 6,
    "4": 6,
    "nonsquarefree": 2
  },
  "witness_4cycle": [
    0,
    0
  ],
  "witness_13": [
    4,
    4
  ],
  "resolvent_irred_at": [
    4,
    4
  ],
  "disc_nonsquare_at": [
    0,
    0
  ],
  "PASS_S4_finite_place": true
}
```

This is finite-place evidence for arithmetic `S_4` behavior in the explicit
restricted family. The factorization types `"4"` and `"13"` supply the
expected transitivity and 3-cycle witnesses in this finite scan, and the
reported nonsquare discriminant/resolvent checks are compatible with the
Cycle 35 monodromy certificate criterion.

## Source-Validity Gate

Cycle 38 also records the source-validity point that the remaining free data is
not just formal checker input. For `n>=6`, the map

```text
W -> ([W]_E, W_{n-1}, W_{n-2}, W_{n-3}, W_{n-4})
```

from degree `< n` polynomials to `A x F^4` is `F`-linear and surjective. Thus
the chosen residue `u=[W]_E=1+X` and top free coefficients
`1, alpha, 1+alpha, 1` can be realized simultaneously by a source-valid base
anchor word.

This gate is bankable as a finite-dimensional linear-algebra audit. It does
not by itself prove a uniform growing-prime monodromy theorem.

## New Exact Wall

The live wall has sharpened from a crashed single-prime checker to symbolic
good reduction and uniform monodromy:

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
```

The next theorem-sized target is:

1. compute or certify the symbolic discriminant and cubic resolvent for
   `tau_i=det(M_i)/Delta` in the explicit family;
2. prove nonconstant squarefree discriminant part, resolvent absolute
   irreducibility, and a transitive type `"4"` specialization away from
   `Delta=0`;
3. prove that the finite `p=31` certificate is a good-reduction witness for a
   growing-prime family or identify the exact obstruction;
4. only then discuss any restricted `Theta(q_line)` counterpacket seed.

## What Is Not Banked

Do not bank:

- a full solution or disproof of the Proximity Prize;
- a proof of corrected-reserve RS-MCA;
- a `COUNTERPACKET`;
- a uniform growing-prime `Theta(q_line)` theorem;
- a proof of geometric `S_4` over `B(z_0,z_1)`;
- an MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, or SNARK
  statement;
- any merge of `q_gen=p` with `q_line=p^2`;
- malformed visible-terminal text as theorem content.

## Next Prompt Direction

Ask the next worker to attack exactly

```text
W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED
```

and require one of:

- a source-valid symbolic/good-reduction proof upgrading the repaired
  single-prime certificate;
- a precise obstruction showing why the finite `p=31` S4 evidence cannot
  globalize;
- a stronger finite checker/certificate with explicit symbolic ingredients;
- a sharper exact wall below symbolic good reduction.
