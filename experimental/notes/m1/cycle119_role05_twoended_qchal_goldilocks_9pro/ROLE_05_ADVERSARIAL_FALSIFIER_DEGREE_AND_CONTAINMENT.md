# Role 05: Adversarial Falsifier - Degree And Containment

Try to kill Role05. Be aggressive and precise.

Read `context/cycle118_returns/05_role05_response.md`.

Attack these possible failure points:

```text
1. Naive degree issue: deg c_T <137 and |A*|=120 seems to risk degree <257, not <256.
2. Two-ended lemma may construct syndrome closeness but not actual support-wise noncontainment.
3. The claimed line may depend on J after all.
4. y1 may lie in W_J in edge cases, destroying noncontainment.
5. Common constant P_T(0) may not be enough to replace the missing top coefficient.
6. Distinct P_T(beta) values may not imply distinct z_J after augmentation by R*.
7. Strict radius/agreement convention might be off by one.
```

If Role05 survives your attacks, say so and return the strongest repaired theorem/checker target. If it fails, give the shortest counterexample or symbolic obstruction you can.

Do not hedge. Return `PROOF` only if the theorem survives all attacks; otherwise return `ROUTE_CUT` or `COUNTERPACKET`.
