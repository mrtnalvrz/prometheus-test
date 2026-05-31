"""
Convert Droidscouts episode PDFs to Markdown using screenplay formatting rules.
Usage: py scripts/pdf_to_markdown.py
"""

import re
import pathlib
from collections import defaultdict

try:
    import pdfplumber
except ImportError:
    raise SystemExit("Run: py -m pip install pdfplumber")

REPO = pathlib.Path(__file__).parent.parent
SCRIPTS_DIR = REPO / "create" / "scripts"

EPISODES = [
    ("DS S1E1.pdf", "ch01-script.md", 1),
    ("DS S1E2.pdf", "ch02-script.md", 2),
    ("DS S1E3.pdf", "ch03-script.md", 3),
    ("DS S1E4.pdf", "ch04-script.md", 4),
]

# X-position thresholds (derived from layout analysis)
X_ACTION    = 160   # x0 < threshold  → action / slugline
X_DIALOGUE  = 220   # threshold range → dialogue / parenthetical
X_CHARACTER = 290   # threshold range → character name
X_RIGHT     = 380   # x0 > threshold  → transition or page number


def fix_text(text: str) -> str:
    """Normalize encoding artifacts from PDF extraction."""
    # Replace Unicode replacement chars (curly apostrophes / quotes in PDF)
    text = text.replace("�", "'")
    # Tidy up stray whitespace around punctuation
    text = re.sub(r"\s+,", ",", text)
    return text.strip()


def dedup_doubled(text: str) -> str:
    """Fix doubled characters from PDF rendering artifacts (e.g. NNAARR → NAR)."""
    if len(text) < 4:
        return text
    result = []
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            result.append(text[i])
            i += 2
        else:
            return text  # not uniformly doubled; leave as-is
    if i < len(text):
        result.append(text[i])
    # Only accept if the result is shorter and non-empty
    deduped = "".join(result)
    return deduped if len(deduped) < len(text) else text


def classify(x0: float, text: str):
    """Return (kind, text) for a line based on x-position and content."""
    if not text:
        return "blank", text

    # Page numbers — right-aligned digits like "22.." or "3."
    if x0 > X_RIGHT and re.fullmatch(r"\d+\.+", text):
        return "page_num", text

    # Transitions — right of center, specific keywords
    transition_pattern = re.compile(
        r"^(FADE|CUT TO|MATCH CUT|SMASH CUT|DISSOLVE|WIPE|TITLE|END OF|DROID SCOUTS)",
        re.I,
    )
    if x0 > 350 and transition_pattern.match(text):
        return "transition", text

    # Sluglines — left margin, starts with INT. or EXT.
    if x0 < X_ACTION and re.match(r"^(INT\.|EXT\.)", text):
        return "slugline", text

    # Character names — centered (~252), all-caps or mostly caps
    if X_DIALOGUE < x0 < X_CHARACTER:
        clean = re.sub(r"\(CONT[^)]*\)", "", text).strip()
        if clean and (clean.isupper() or re.fullmatch(r"[A-Z0-9\s\.\-]+", clean)):
            return "character", clean
        if text.startswith("(") and text.endswith(")"):
            return "cont_marker", text  # e.g. (CONT'D) orphan
        return "character", text  # fall through for mixed-case character names

    # CONT'D orphan on its own line (e.g. x0 ~314-342)
    if x0 > X_DIALOGUE and text.startswith("("):
        return "cont_marker", text

    # Parenthetical at dialogue indent — starts with (
    if X_ACTION <= x0 <= X_DIALOGUE and text.startswith("("):
        return "parenthetical", text

    # Dialogue — indented relative to action
    if X_ACTION <= x0 <= X_DIALOGUE:
        return "dialogue", text

    # Action lines — left margin
    if x0 < X_ACTION:
        return "action", text

    return "action", text  # fallback


def extract_elements(pdf_path: pathlib.Path):
    """Extract (kind, text) elements from all pages of the PDF."""
    elements = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words(x_tolerance=3, y_tolerance=3)
            if not words:
                continue

            line_dict = defaultdict(list)
            for w in words:
                line_dict[round(w["top"])].append(w)

            for y in sorted(line_dict.keys()):
                ws = line_dict[y]
                x0 = min(w["x0"] for w in ws)
                raw = " ".join(w["text"] for w in ws)
                # Fix each word for doubled chars, then join
                fixed_words = [dedup_doubled(fix_text(w["text"])) for w in ws]
                text = " ".join(fixed_words)
                text = fix_text(text)
                kind, text = classify(x0, text)
                elements.append((kind, text))

    return elements


def render_markdown(elements, episode_num: int) -> str:
    lines = [
        "# DROIDSCOUTS",
        f"## Season 1, Chapter {episode_num:02d}",
        "",
        "---",
        "",
    ]

    prev_kind = None

    for kind, text in elements:
        if kind in ("blank", "page_num", "cont_marker"):
            continue

        if kind == "slugline":
            _gap(lines)
            lines.append(f"**{text}**")
            lines.append("")

        elif kind == "transition":
            _gap(lines)
            padding = " " * max(0, 62 - len(text))
            lines.append(f"{padding}{text}")
            lines.append("")

        elif kind == "character":
            _gap(lines)
            lines.append(f"**{text}**")

        elif kind == "parenthetical":
            # Keep parens, render italic
            lines.append(f"*{text}*")

        elif kind == "dialogue":
            lines.append(text)

        elif kind == "action":
            if prev_kind == "dialogue":
                _gap(lines)
            lines.append(text)

        prev_kind = kind

    return "\n".join(lines) + "\n"


def _gap(lines):
    """Ensure there is a blank line before the next element."""
    if lines and lines[-1] != "":
        lines.append("")


def convert_all():
    for pdf_name, md_name, num in EPISODES:
        pdf_path = SCRIPTS_DIR / pdf_name
        md_path = SCRIPTS_DIR / md_name
        if not pdf_path.exists():
            print(f"SKIP (not found): {pdf_path}")
            continue
        print(f"Converting {pdf_name} ...", end=" ", flush=True)
        elements = extract_elements(pdf_path)
        md = render_markdown(elements, num)
        md_path.write_text(md, encoding="utf-8")
        print(f"-> {md_name} ({len(elements)} elements, {md_path.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    convert_all()
