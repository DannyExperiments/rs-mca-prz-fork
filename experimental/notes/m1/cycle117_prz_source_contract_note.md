# Note To PRZ: Cycle117 Source-Contract Audit

Przemek,

Codex here. I audited the Cycle117 9-Pro source-contract round and replayed the
generated checker package locally.

The concise result is:

```text
Cycle116's finite row is accepted by the attached manuscript/source semantics:

C = RS[F_17^32,H,256], H=<theta>, |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128

q_gen = q_code = q_line = 17^32
q_chal = null
```

The source/manuscript layer also retains the events: endpoint deletion is absent,
periodic/quotient/tangent machinery is not a raw deletion or charge, contained
line is paid by the Cycle116 noncontainment proof, same-slope collision is
already paid by the Cycle84 occupancy, and no attached `AP_corr` or charge
registry removes the numerator.

But I do not think this is yet an official Proximity Prize counterpacket. The
first missing object is an authority-pinned contract/adoption clause saying that
the official predicate admits this exact extension-field row, samples the line
parameter over `F_17^32` or defines another `q_chal`, and exhaustively specifies
endpoint / periodic / quotient / tangent / retained-event / charge rules.

Role 08 produced a useful fail-closed checker. Its default terminal vector is:

```text
attached manuscript row    SOURCE_ACCEPTED_CYCLE116_ROW
attached manuscript q_chal QCHAL_UNDEFINED_FINITE_MCA_ONLY
attached manuscript events EVENT_RETAINED
official/prize contract    SOURCE_CONTRACT_MISSING_NO_CLAIM
```

Local checker replay and nonmutating self-tests pass. So the banked status is:

```text
BANKABLE_LEMMA / ROUTE_CUT / AUDIT
```

My proposed next exact target is:

```text
V-CYCLE118-AUTHORITY-PINNED-OFFICIAL-ROW-EVENT-CONTRACT
```

If that contract accepts the attached manuscript semantics, Cycle116 composes
directly into the official/source counterpacket. If it rejects the extension
field or changes the retained-event map, we should not guess; the next math
target is then the accepted-field compiler, driven by the first named rejected
clause.
