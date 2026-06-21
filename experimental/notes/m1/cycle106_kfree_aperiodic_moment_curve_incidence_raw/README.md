# Cycle106 Raw Artifact Preservation

This directory preserves the failed Cycle106 Fable artifact-stream attempt:

```text
2026-06-21T16-05-57-059Z-cycle106-kfree-aperiodic-moment-curve-incidence-55832618
```

The run targeted:

```text
W-CYCLE106-KFREE-APERIODIC-MOMENT-CURVE-INCIDENCE
```

The run is not a mathematical answer. It ended with:

```text
CLAUDE_CAPTURE_WARNING_FATAL
Claude CLI stream-json ended without a final result event
Timed out after 5400000ms
```

The manifest records the local staging blocker:

```text
projectSource.included = false
fileIndex.included = false
reason = ENOSPC while copying a large raw Cycle66 JSONL into input_project
```

The copied artifacts are kept only for provenance and harness diagnosis. Do not
bank mathematical content from `response.md`; it contains only failed setup and
tool-access chatter.

