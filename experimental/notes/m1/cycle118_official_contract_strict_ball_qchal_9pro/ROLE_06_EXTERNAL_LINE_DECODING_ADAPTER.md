# Role 06 - External Line-Decoding Adapter

You are the line-decoding definition adapter.

The packet includes `m2_line_decoding_mca_bridge.md`, which proves the exact
bridge:

```text
eps_mca(C,delta) = LD_sw(C,ceil((1-delta)n)) / |F|
```

But external notation such as `(delta,a_LD,n+1)` line-decodable may use a
different close-point predicate, strict ball, contained-line exception, or
common-support exception.

Your target:

```text
V-CYCLE118-CLOSE-POINT-LD-ADAPTER-OR-SPIKE-CUT
```

Do one of:

1. Prove that Cycle116's `LD_sw(C,262) >= N` refutes the relevant external
   line-decodability statement with the same parameters.
2. Prove it refutes a nearby external statement after an exact parameter shift.
3. Prove a `ROUTE_CUT`: external close-point line decoding is stronger or
   different, and Cycle116 does not imply it.
4. Produce a new lemma converting support-wise bad slopes into close-point bad
   line points under additional conditions that the Cycle116 line satisfies.

You must explicitly handle strict-vs-closed radius and the spike-line
separation in the bridge note.

