# Provenance

## Current Git State At Packet Creation

```text
branch: cycle58-5p5-audit
latest relevant commits:
2965689 Verify Cycle120 ABF admissibility gates
8511e98 Audit Cycle120 official source gates
0bb1df6 Audit final Cycle119 hostile returns
7f8b37c Assemble Cycle119 submission prep packet
e62898d Harden Cycle119 cold packet
```

## ABF Source Audit

Direct ABF admissibility audit:

```text
experimental/notes/m1/cycle119_official_source_audit/
  V_CYCLE120_ABF_DIRECT_ADMISSIBILITY_AUDIT.md
```

Local PDF:

```text
experimental/notes/m1/cycle119_official_source_audit/abf_pdf_extract/ABF26_680_iacr.pdf
sha256:
e543ec6a4f3312b4383000e72e5aa23862e79cc9770ce21db2c48db679581de3
```

Extracted text:

```text
ABF26_680_iacr_pdfplumber.txt
sha256:
eac4031f15a8ab430541e7d31af82f1dc10c2686ee31ed9d8c14ef10c78ec344

ABF26_680_iacr_pypdf.txt
sha256:
1f0db1f08b6b00955039eb9376eac866ba2362e5a4ac97d30a95575e4073b255
```

Rendered check pages:

```text
page 5: grand MCA challenge
page 9: Reed-Solomon and smooth-domain definitions
page 17: Definition 4.3, MCA error
```

## Cycle116 Finite Theorem

Cycle116 banked theorem:

```text
C = RS[F_17^32,H,256], |H|=512
LD_sw(C,262) >= 52,747,567,092
epsilon_mca(C,125/256) >= 52,747,567,092 / 17^32 > 2^-128
```

Relevant tracker key:

```text
A1-C116
```

## Cycle119 Strict Strengthening

Cycle119 banked theorem:

```text
LD_sw(RS[F_17^32,H,256],263) >= 52,747,567,092
```

Relevant tracker key:

```text
A1-C119
```

Local replay terminal:

```text
CYCLE118_TWO_ENDED_AGREEMENT_263_TRANSFER_VERIFIED
```

## Proximity Prize Website Snapshot

Local snapshot:

```text
experimental/notes/m1/cycle119_official_source_audit/proximityprize_20260624.html
```

The live site was also checked on 2026-06-24. The submission FAQ states that a
submission needs a PDF, a public academic repository timestamp, human
verification/editing for AI-aided work, and peer-reviewed acceptance for final
prize consideration.

## Cycle120 Packet Bundle

Packet directory:

```text
experimental/notes/m1/cycle120_abf_counterexample_packet/
```

Packet zip:

```text
experimental/notes/m1/cycle120_abf_counterexample_packet.zip
```

Packet zip SHA-256 file:

```text
experimental/notes/m1/cycle120_abf_counterexample_packet.zip.sha256
```
