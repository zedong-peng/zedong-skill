#!/usr/bin/env python3
"""Build a self-contained HTML presentation from a JSON deck and local figures."""

import argparse
import base64
import html
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


TEMPLATE = Path(__file__).resolve().parents[1] / "assets" / "deck.html"
IMAGE_TYPES = {
    ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif",
}
LAYOUT_COUNTS = {"single": 1, "columns": 2, "strip-and-columns": 3}


def escape(value):
    return html.escape(str(value), quote=True)


def required_text(obj, key):
    value = obj.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} must be a nonempty string")
    return value.strip()


def chapters_for(slides):
    chapters = []
    seen = set()
    for number, slide in enumerate(slides, 2):
        name = required_text(slide, "chapter")
        if chapters and chapters[-1]["name"] == name:
            chapters[-1]["last"] = number
        else:
            if name in seen:
                raise ValueError(f"Keep the slides of chapter {name!r} together")
            seen.add(name)
            chapters.append({"name": name, "first": number, "last": number})
    return chapters


def chapter_progress(number, chapters):
    items = []
    for index, chapter in enumerate(chapters, 1):
        first, last, name = chapter["first"], chapter["last"], chapter["name"]
        active = first <= number <= last
        state = "current" if active else ("complete" if number > last else "upcoming")
        fill = max(0, min(1, (number - first + 1) / (last - first + 1))) * 100
        compact = " compact" if len(name) > 9 else ""
        current = ' aria-current="step"' if active else ""
        items.append(
            f'<li class="chapter {state}"><button type="button" '
            f'data-slide-target="{first}" title="{escape(name)}" '
            f'aria-label="{index:02}: {escape(name)}; go to slide {first}"{current}>'
            f'<span class="chapter-meter" aria-hidden="true"><span style="width:{fill:.2f}%"></span></span>'
            f'<span class="chapter-name{compact}"><span class="chapter-number">{index:02}</span>'
            f'<span class="chapter-label">{escape(name)}</span></span></button></li>'
        )
    return '<nav class="chapter-progress" aria-label="Chapter progress"><ol>' + "".join(items) + "</ol></nav>"


def check_svg_resources(data):
    """External images and styles would break a forwarded, offline SVG."""
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise ValueError(f"Invalid SVG: {error}") from error
    if root.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError("Expected an SVG document")
    styles = []
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag == "style":
            styles.append("".join(element.itertext()))
        for key, value in element.attrib.items():
            key = key.rsplit("}", 1)[-1]
            value = value.strip()
            if key in ("href", "src") and tag != "a":
                if value and not value.startswith(("#", "data:")):
                    raise ValueError("Embed the SVG's referenced images before building the deck")
            if key == "style" or "url(" in value.lower():
                styles.append(value)
    for style in styles:
        if "@import" in style.lower():
            raise ValueError("Inline imported SVG styles before building the deck")
        for target in re.findall(r"url\(\s*([^)]*?)\s*\)", style, re.I):
            target = target.strip(" \t\r\n\"'")
            if target and not target.startswith(("#", "data:")):
                raise ValueError("Embed external SVG style resources before building the deck")


def pdf_svg(path, figure):
    try:
        import fitz
    except ImportError as error:
        raise ValueError("PDF figures require PyMuPDF: python3 -m pip install pymupdf") from error
    number = figure.get("page", 1)
    if type(number) is not int or number < 1:
        raise ValueError("PDF page must be an integer, starting at 1")
    with fitz.open(path) as document:
        if number > len(document):
            raise ValueError(f"PDF page {number} exceeds the document's {len(document)} pages")
        page = document[number - 1]
        if "crop" not in figure:
            return page.get_svg_image(text_as_path=True).encode()
        crop = figure["crop"]
        if not isinstance(crop, list) or len(crop) != 4:
            raise ValueError("crop must be [x0, y0, x1, y1] in PDF points")
        rect = fitz.Rect(crop)
        if rect.is_empty or rect.is_infinite or not page.rect.contains(rect):
            raise ValueError("crop must be a nonempty rectangle inside the selected PDF page")
        with fitz.open() as cropped:
            target = cropped.new_page(width=rect.width, height=rect.height)
            target.show_pdf_page(target.rect, document, number - 1, clip=rect)
            return target.get_svg_image(text_as_path=True).encode()


def figure_html(figure, base, extra=""):
    path = base / required_text(figure, "path")
    alt = required_text(figure, "alt")
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        data, media_type = pdf_svg(path, figure), "image/svg+xml"
    elif suffix in IMAGE_TYPES:
        if "page" in figure or "crop" in figure:
            raise ValueError("page and crop are only supported for PDF figures")
        data, media_type = path.read_bytes(), IMAGE_TYPES[suffix]
    else:
        raise ValueError("Use PDF, SVG, PNG, JPEG, WebP or GIF figures")
    if media_type == "image/svg+xml":
        check_svg_resources(data)
    uri = f"data:{media_type};base64," + base64.b64encode(data).decode()
    return (
        f'<button class="figure {extra}" type="button" '
        f'aria-label="Enlarge figure: {escape(alt)}" data-source="{escape(path.name)}">'
        f'<img src="{uri}" alt="{escape(alt)}" draggable="false"></button>'
    )


def slide_content(slide, base):
    figures = slide.get("figures", [])
    if not isinstance(figures, list) or not all(isinstance(f, dict) for f in figures):
        raise ValueError("figures must be a list of objects")
    if figures:
        if "text" in slide:
            raise ValueError("Use either figures or text on a slide")
        layout = slide.get("layout", "single")
        if layout not in LAYOUT_COUNTS or len(figures) != LAYOUT_COUNTS[layout]:
            raise ValueError("Layouts require: single = 1 figure, columns = 2, strip-and-columns = 3")
        if layout == "single":
            return figure_html(figures[0], base)
        if layout == "columns":
            return '<div class="columns">' + "".join(figure_html(f, base) for f in figures) + "</div>"
        return (
            '<div class="strip-layout">' + figure_html(figures[0], base, "strip-figure")
            + '<div class="columns">' + "".join(figure_html(f, base) for f in figures[1:]) + "</div></div>"
        )
    paragraphs = slide.get("text")
    if not isinstance(paragraphs, list) or not paragraphs or not all(isinstance(p, str) for p in paragraphs):
        raise ValueError("A slide needs figures or a nonempty text list")
    return '<div class="text-content">' + "".join(f"<p>{escape(p)}</p>" for p in paragraphs) + "</div>"


def build(spec, base):
    title = required_text(spec, "title")
    slides = spec.get("slides")
    if not isinstance(slides, list) or not slides or not all(isinstance(s, dict) for s in slides):
        raise ValueError("slides must be a nonempty list of objects")
    chapters = chapters_for(slides)
    title_lines = spec.get("title_lines", [title])
    if not isinstance(title_lines, list) or not title_lines or not all(isinstance(t, str) for t in title_lines):
        raise ValueError("title_lines must be a nonempty list of strings")
    author, affiliation, date = (spec.get(k, "") for k in ("author", "affiliation", "date"))
    author_html = f'<p class="author">{escape(author)}</p>' if author else ""
    affiliation_html = f"<p>{escape(affiliation)}</p>" if affiliation else ""
    date_html = f"<p>{escape(date)}</p>" if date else ""
    cover = (
        f'<section class="slide title-slide" id="slide-01" aria-label="Slide 1: {escape(title)}" '
        f'aria-roledescription="slide" data-title="{escape(title)}" data-section="Cover">'
        '<div class="slide-body"><div class="cover-content"><h1>'
        + "<br>".join(escape(line) for line in title_lines) + '</h1><div class="title-bottom"><div>'
        + author_html + affiliation_html + "</div>" + date_html + "</div></div></div></section>"
    )
    output_slides = [cover]
    for number, slide in enumerate(slides, 2):
        name, slide_title = required_text(slide, "chapter"), required_text(slide, "title")
        chapter_index = next(i for i, c in enumerate(chapters, 1) if c["name"] == name)
        note = slide.get("note", "")
        caption = f'<div class="source-row"><p>{escape(note)}</p></div>' if note else ""
        output_slides.append(
            f'<section class="slide" id="slide-{number:02}" '
            f'aria-label="Slide {number}: {escape(slide_title)}" aria-roledescription="slide" '
            f'data-title="{escape(slide_title)}" data-section="{chapter_index:02} / {escape(name)}" hidden inert>'
            '<div class="slide-body">' + slide_content(slide, base) + '</div><footer class="slide-footer">'
            + caption + chapter_progress(number, chapters) + "</footer></section>"
        )
    replacements = {
        "__TITLE__": escape(title), "__AUTHOR__": escape(author),
        "__DESCRIPTION__": escape(spec.get("description", title)),
        "__SLIDE_COUNT__": str(len(output_slides)), "__SLIDES__": "\n".join(output_slides),
        "__CHAPTER_COLUMNS__": " ".join(f'minmax(0,{c["last"] - c["first"] + 1}fr)' for c in chapters),
    }
    # One pass keeps placeholder-like strings in user content literal.
    return re.sub(r"__[A-Z_]+__", lambda m: replacements[m.group()], TEMPLATE.read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path, help="JSON deck; figure paths are relative to this file")
    parser.add_argument("-o", "--output", type=Path, required=True, help="Output .html file")
    args = parser.parse_args()
    try:
        if args.output.suffix.lower() not in (".html", ".htm"):
            raise ValueError("Use an .html or .htm output path")
        spec = json.loads(args.deck.read_text(encoding="utf-8"))
        if not isinstance(spec, dict):
            raise ValueError("The deck JSON must be an object")
        document = build(spec, args.deck.resolve().parent)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(document, encoding="utf-8")
    except (OSError, ValueError, TypeError) as error:
        parser.error(str(error))
    print(f"Built {args.output.name}: {len(spec['slides']) + 1} slides, {args.output.stat().st_size:,} bytes; fully offline")


if __name__ == "__main__":
    main()
