# Cycle84 Finite Certificate

This directory is the reviewer-facing finite certificate for the Cycle84
color-filtered seven-slot product model.

Start with:

```text
STANDALONE_FINITE_CERTIFICATE.md
```

The directory intentionally excludes raw Packy/Fable transcripts and large
cycle-provenance archives. It contains only the finite theorem statement,
checker sources, compact data tables, and recorded outputs needed to inspect or
rerun the finite certificate.

Quick verification:

```bash
python3 verify_certificate.py
```

Public replay receipt:

```text
https://github.com/DannyExperiments/rs-mca-prz-fork/actions/runs/27889140962
```

Scope:

```text
This proves the explicit finite Cycle84 model theorem m_max(beta)=2.
It does not by itself prove an RS-MCA/list-decoding/prize theorem.
```
