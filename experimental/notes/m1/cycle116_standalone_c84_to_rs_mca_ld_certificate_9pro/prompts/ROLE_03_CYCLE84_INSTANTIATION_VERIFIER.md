# Role 03: Cycle84 Instantiation Verifier

Use the common prompt. No Internet.

Your job is to verify the Cycle84-specific identities needed by the transfer.

Audit:

```text
D0 = <eta>, |D0|=256
Cycle84 co-support size j=113
P_T(X)=X^113-X^112+O(X^107)
P_T(beta)=kappa*Phi(T), kappa != 0
```

and therefore:

```text
#{P_T(beta): T in color shell} = Occ(beta) = 52,747,567,092.
```

Use the standalone certificate, Cycle85 audit, and source/checker files. State which identities are directly verified in the packet and which require a new tiny checker.

Deliverable: a checklist and/or verifier specification that would make the Cycle84-to-locator bridge reviewer-clean.
