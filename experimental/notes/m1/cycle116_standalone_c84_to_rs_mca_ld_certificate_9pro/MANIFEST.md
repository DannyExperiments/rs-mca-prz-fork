# Cycle116 Standalone Cycle84-To-RS-MCA/LD Certificate Packet

Purpose: produce or falsify a standalone reviewer-facing certificate for the
Cycle84-to-RS-MCA transfer theorem.

This packet is not asking for another broad search. It asks for a compact proof
artifact:

```text
V-CYCLE116-STANDALONE-C84-TO-RS-MCA-LD-TRANSFER-CERTIFICATE
```

Core target:

```text
Cycle84 finite certificate
  m_max(beta)=2, Occ(beta)=52,747,567,092
      =>
RS support-wise MCA / LD_sw lower bound
      =>
smooth lifted row
  RS[F_17^32,H,256], |H|=512,
  LD_sw(C,262) >= 52,747,567,092,
  epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128.
```

Important: this would be a finite/paper-facing RS-MCA theorem, not by itself an
official Proximity Prize solve.

Included context:

- `TARGET_CERTIFICATE_BLUEPRINT.md`
- standalone Cycle84 finite certificate directory;
- Cycle115 audited returns and raw pasted role answers;
- Cycle85 transfer audit;
- M2 line-decoding bridge note;
- canonical tracker;
- relevant source TeX/markdown files.

Expected outputs:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Preferred next artifact after this round:

```text
STANDALONE_C84_TO_RS_MCA_LD_TRANSFER_CERTIFICATE.md
verify_c84_to_rs_mca_ld_transfer.py
```
