#!/usr/bin/env python3
"""Render THEOREM_NOTE.md to a simple PDF draft using reportlab.

This avoids requiring pandoc or a TeX installation on the local machine. The
Markdown remains the canonical source; the PDF is only a readable draft for
human review.
"""

from __future__ import annotations

import re
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
)
from reportlab.lib.units import inch


HERE = Path(__file__).resolve().parent
SRC = HERE / "THEOREM_NOTE.md"
OUT = HERE / "THEOREM_NOTE.pdf"


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def main() -> None:
    styles = getSampleStyleSheet()
    title = styles["Title"]
    h1 = styles["Heading1"]
    h2 = styles["Heading2"]
    body = styles["BodyText"]
    body.leading = 13
    pre = styles["Code"]
    pre.fontName = "Courier"
    pre.fontSize = 8
    pre.leading = 10

    story = []
    in_code = False
    code_lines: list[str] = []

    def flush_code() -> None:
        nonlocal code_lines
        if code_lines:
            story.append(Preformatted("\n".join(code_lines), pre))
            story.append(Spacer(1, 0.08 * inch))
            code_lines = []

    for raw_line in SRC.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line:
            story.append(Spacer(1, 0.06 * inch))
            continue
        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:]), title))
            story.append(Spacer(1, 0.12 * inch))
        elif line.startswith("## "):
            story.append(Paragraph(escape(line[3:]), h1))
        elif line.startswith("### "):
            story.append(Paragraph(escape(line[4:]), h2))
        elif line == "---":
            story.append(PageBreak())
        else:
            # Minimal inline-code rendering: keep content readable, not fancy.
            text = escape(line)
            text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
            story.append(Paragraph(text, body))

    if in_code:
        flush_code()

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=LETTER,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.6 * inch,
        bottomMargin=0.6 * inch,
        title="Cycle120 ABF-Facing RS-MCA Counterexample Note",
    )
    doc.build(story)
    print(OUT)


if __name__ == "__main__":
    main()

