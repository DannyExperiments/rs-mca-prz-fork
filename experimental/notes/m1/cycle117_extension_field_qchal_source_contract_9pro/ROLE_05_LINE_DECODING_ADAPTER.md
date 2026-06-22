# Role 05 - Line-Decoding / LD_sw Adapter

You are the line-decoding adapter prover.

Cycle116 proves an `LD_sw` / support-wise MCA lower bound. PRZ's question also
mentions MCA/list/line-decoding. Your task is to prove the exact adapter, or cut
it.

Required deliverables:

1. Define `LD_sw(C,a)` in a way exactly compatible with the source
   support-wise MCA definition.

2. Prove:

```text
epsilon_mca(C,delta)
  = or >= LD_sw(C,ceil((1-delta)n)) / |F|
```

under the attached source definitions. Be precise about ceiling/floor and
agreement size. For Cycle116:

```text
n=512
delta=125/256
ceil((1-delta)n)=262
```

3. Search the attached source files for any formal
`(delta,a_LD,n+1)-line-decodable` definition. If present, prove:

```text
(delta,a_LD,n+1)-line-decodable
  => LD_sw(C,ceil((1-delta)n)) <= a_LD
```

or the exact correct variant.

4. If that definition is absent, return `ROUTE_CUT` with the exact missing
definition and a clean proposed adapter theorem.

5. Do not claim ordinary list decoding unless you prove a fixed received word
with many close codewords.

This role should be proof-heavy. The best answer is a reusable adapter theorem
for the reviewer packet.
