# V-CYCLE118 two-ended agreement-263 replay checker

Run:

```bash
./run_checker.sh
```

Expected JSON decision:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

The checker imports the hash-bound Cycle84 occupancy and does not rerun the 52-billion enumeration. See `CHECKER_SPEC.md` for the exact finite checks and `SYMBOLIC_LEMMAS.md` for the universal algebraic implications.
