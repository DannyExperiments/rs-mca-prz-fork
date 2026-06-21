# ROLE 04: Two-Copy Counterpacket Hunter

You are a fresh red-team instance.

Try to kill:

```text
L-CYCLE86-TWO-BLOCK-ADDITIVE-COLOR-COMPOSITION
```

Find a precise reason the proposed two-copy construction cannot yield one
official RS/GRS MCA line.

Attack points:

1. Does the construction secretly produce `t=2` or two independent lines?
2. Does the combined support fail to be a degree-`j` complement locator for
   one RS code?
3. Does affine color addition fail under the Role05 `Delta^+` quotient?
4. Does quotient/periodic structure identify many supposed slopes?
5. Does transversality fail after padding or domain translation?
6. Is the field `F_17^48` being used as line field but not generated field or
   code field correctly?
7. Do the proposed parameter packages violate rate, reserve, or support-size
   equations?

Return `COUNTERPACKET` if you find a concrete false statement. Return
`ROUTE_CUT` if the route is structurally impossible. Return `BANKABLE_LEMMA`
only if your red-team audit fails and you can state exactly what survived.
