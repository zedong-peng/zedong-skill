---
name: html-slides
description: Create or edit standalone HTML slide decks from reports and figures, with embedded assets and chapter navigation. Use for browser presentations; preserve a requested Beamer or PowerPoint format.
---

# HTML slides

A talk the user can forward as one HTML file and open offline. Start from [the template](assets/deck.html); it includes figure zoom, an overview, chapter jumps, keyboard and touch navigation, fullscreen, and printing.

## Presentation taste

- A clean cover: title, author, affiliation and date. Warm ivory background, Georgia title, system fonts elsewhere. No downloaded fonts by default.
- Let original figures carry the content. Body slides have no large headings by default; titles live in the overview. A short source note is enough. Add text when it earns its space.
- Preserve source figures' labels, colours and proportions. Prefer complete figures and tables when legible; use a panel crop when it warrants its own explanation.
- Short chapter names, no page counters. Chapter widths track their page counts, excluding the cover. Detailed architecture and supporting material can live in an appendix when they interrupt the main argument.
- Fullscreen hides the toolbar, keeps the chapter footer and expands the slide viewport.

These are defaults for a new talk; explicit choices and an existing deck's design take precedence.

## Template and builder

Read [the deck format](references/deck-format.md) to prepare the JSON and choose layouts. From this skill's directory:

```sh
python3 scripts/build_slides.py path/to/deck.json -o path/to/slides.html
```

The builder embeds local figures and derives chapter boundaries, proportional widths, progress and destinations from slide order. PDF figures need PyMuPDF and become SVG with outlined text. Only the output HTML needs forwarding; keep the working sources for edits unless cleanup is requested.

Adapt the template when a layout needs it. When editing an existing standalone deck, preserve embedded figures and update every chapter footer after structural changes. Check the resulting layout and navigation in a browser; the deck-format reference includes the checks relevant to this template.

The [saved Anthropic brand guide](references/brand-guidelines.md) is an optional visual reference. Palette changes do not imply font changes; the default remains Georgia and system fonts.
