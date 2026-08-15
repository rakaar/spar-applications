#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
NAVY = colors.HexColor("#172A46")
BLUE = colors.HexColor("#2463A6")
INK = colors.HexColor("#1F2933")
MUTED = colors.HexColor("#667085")
PALE = colors.HexColor("#EAF1F8")


def register_fonts() -> None:
    pdfmetrics.registerFont(TTFont("DejaVuSans", str(FONT_DIR / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSans-Bold", str(FONT_DIR / "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSans-Oblique", str(FONT_DIR / "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSerif", str(FONT_DIR / "DejaVuSerif.ttf")))
    pdfmetrics.registerFont(TTFont("DejaVuSerif-Italic", str(FONT_DIR / "DejaVuSerif-Italic.ttf")))


def normalize(text: str) -> str:
    replacements = {
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u000b": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def inline_markup(text: str) -> str:
    text = normalize(text)
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"@@MARKUP{len(placeholders) - 1}@@"

    def link_repl(match: re.Match[str]) -> str:
        label = html.escape(match.group(1), quote=False)
        url = html.escape(match.group(2), quote=True)
        return stash(f'<link href="{url}" color="#2463A6"><u>{label}</u></link>')

    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", link_repl, text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", lambda m: stash(f'<font name="DejaVuSans">{m.group(1)}</font>'), text)
    text = re.sub(r"\*\*([^*]+)\*\*", lambda m: stash(f"<b>{m.group(1)}</b>"), text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", lambda m: stash(f"<i>{m.group(1)}</i>"), text)
    for index, value in enumerate(placeholders):
        text = text.replace(f"@@MARKUP{index}@@", value)
    return text


def make_styles():
    sample = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=sample["Title"],
            fontName="DejaVuSans-Bold",
            fontSize=24,
            leading=30,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=14,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=sample["Heading2"],
            fontName="DejaVuSans-Bold",
            fontSize=14,
            leading=18,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=sample["Heading3"],
            fontName="DejaVuSans-Bold",
            fontSize=11.5,
            leading=15,
            textColor=BLUE,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=sample["BodyText"],
            fontName="DejaVuSans",
            fontSize=9.6,
            leading=14.2,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=7,
        ),
        "question": ParagraphStyle(
            "Question",
            parent=sample["BodyText"],
            fontName="DejaVuSerif-Italic",
            fontSize=9.4,
            leading=14.2,
            textColor=NAVY,
            backColor=PALE,
            borderColor=colors.HexColor("#B9CEE3"),
            borderWidth=0.6,
            borderPadding=8,
            leftIndent=4,
            rightIndent=4,
            spaceBefore=3,
            spaceAfter=11,
        ),
        "reference": ParagraphStyle(
            "Reference",
            parent=sample["BodyText"],
            fontName="DejaVuSans",
            fontSize=8.6,
            leading=12.5,
            textColor=INK,
            leftIndent=9,
            firstLineIndent=-9,
            spaceAfter=6,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=sample["BodyText"],
            fontName="DejaVuSans",
            fontSize=8.8,
            leading=13,
            textColor=MUTED,
            spaceAfter=7,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=sample["BodyText"],
            fontName="DejaVuSans",
            fontSize=9.4,
            leading=13.8,
            textColor=INK,
        ),
    }


def draw_page(canvas, doc) -> None:
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(colors.HexColor("#D9E2EC"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 16 * mm, width - 18 * mm, 16 * mm)
    canvas.setFont("DejaVuSans", 7.7)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 10.5 * mm, "SPAR Applications - Private Working Draft")
    canvas.drawRightString(width - 18 * mm, 10.5 * mm, f"Page {doc.page}")
    if doc.page > 1:
        canvas.setFont("DejaVuSans", 7.5)
        canvas.drawString(18 * mm, height - 13 * mm, doc.project_title[:92])
    canvas.restoreState()


def parse_markdown(path: Path, styles):
    lines = path.read_text(encoding="utf-8").splitlines()
    story = []
    index = 0
    in_references = False
    first_heading = True

    while index < len(lines):
        raw = lines[index].rstrip()
        stripped = raw.strip()
        if not stripped:
            index += 1
            continue
        if stripped.startswith("# "):
            if not first_heading:
                story.append(Spacer(1, 6))
            story.append(Paragraph(inline_markup(stripped[2:]), styles["title"]))
            story.append(HRFlowable(width="100%", thickness=1.1, color=BLUE, spaceAfter=10))
            first_heading = False
            index += 1
            continue
        if stripped.startswith("## "):
            heading = stripped[3:]
            in_references = heading.strip().lower() == "references"
            story.append(Paragraph(inline_markup(heading), styles["h2"]))
            index += 1
            continue
        if stripped.startswith("### "):
            story.append(Paragraph(inline_markup(stripped[4:]), styles["h3"]))
            index += 1
            continue
        if stripped.startswith("- "):
            bullets = []
            while index < len(lines) and lines[index].strip().startswith("- "):
                item = lines[index].strip()[2:]
                bullets.append(ListItem(Paragraph(inline_markup(item), styles["bullet"]), leftIndent=10))
                index += 1
            story.append(ListFlowable(bullets, bulletType="bullet", start="circle", leftIndent=17, bulletFontName="DejaVuSans", bulletFontSize=6, spaceAfter=8))
            continue

        parts = [stripped]
        index += 1
        while index < len(lines):
            nxt = lines[index].strip()
            if not nxt or nxt.startswith(("# ", "## ", "### ", "- ")):
                break
            parts.append(nxt)
            index += 1
        paragraph = " ".join(parts)

        if paragraph.startswith("*") and paragraph.endswith("*") and not paragraph.startswith("**"):
            question = paragraph[1:-1]
            story.append(Paragraph(inline_markup(question), styles["question"]))
        elif in_references and re.match(r"^\[\d+\]", paragraph):
            story.append(Paragraph(inline_markup(paragraph), styles["reference"]))
        elif paragraph.lower().startswith(("project page:", "track represented")):
            story.append(Paragraph(inline_markup(paragraph), styles["meta"]))
        else:
            story.append(Paragraph(inline_markup(paragraph), styles["body"]))
    return story


def build_one(markdown_path: Path) -> Path:
    styles = make_styles()
    title = markdown_path.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ").strip()
    output_path = markdown_path.with_suffix(".pdf")
    doc = BaseDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=19 * mm,
        bottomMargin=21 * mm,
        title=title,
        author="Raghavendra Kaushik Archak",
        subject="SPAR Fall 2026 application response",
    )
    doc.project_title = title
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")
    doc.addPageTemplates([PageTemplate(id="application", frames=[frame], onPage=draw_page)])
    doc.build(parse_markdown(markdown_path, styles))
    return output_path


def main() -> None:
    register_fonts()
    markdown_files = sorted(path for path in ROOT.glob("*/application.md"))
    if not markdown_files:
        raise SystemExit("No application.md files found")
    for markdown_path in markdown_files:
        output = build_one(markdown_path)
        print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
