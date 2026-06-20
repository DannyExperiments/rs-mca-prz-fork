# ROLE 03: MITM DUPLICATE DETECTOR SPEC

Your role is checker-spec writer.

Design the exact lowest-resource checker for the threshold:

```text
max_v m(v) <= 12.
```

The checker should not build a full histogram if avoidable. It should abort and
emit a counterpacket as soon as any `v` reaches 13 compatible representations.

Cycle83 proposed:

- Bloom duplicate detector plus exact recount, about 66GB RAM;
- deterministic shard/reduce, about 0.5-0.85TB scratch;
- recompute sharding, slow but lower disk.

Your job:

1. produce a concrete executable design;
2. define the field encoding;
3. define exact record format;
4. define deterministic shard key;
5. prove no false negatives;
6. specify certificate output for both PASS and FAIL;
7. estimate RAM/disk/time.

If possible, improve substantially on the Cycle83 resource estimates.

