# Deck format

The builder takes UTF-8 JSON and writes one HTML file. Python's standard library is sufficient for image inputs. PDF inputs additionally require `pymupdf`.

```json
{
  "title": "A figure-led technical talk",
  "title_lines": ["A figure-led", "technical talk"],
  "author": "Speaker",
  "affiliation": "Research group",
  "date": "Presentation date",
  "slides": [
    {
      "chapter": "Intro",
      "title": "The system boundary",
      "note": "Report Figure 1. The interface between the host and device.",
      "figures": [
        {"path": "figures/system.pdf", "page": 1, "alt": "The system's inputs, compute units and outputs."}
      ]
    },
    {
      "chapter": "Results",
      "title": "Measured throughput",
      "note": "Report Table 1, including its original caption.",
      "figures": [
        {"path": "figures/results.svg", "alt": "Throughput measured across the evaluated configurations."}
      ]
    }
  ]
}
```

Replace the example figure paths with actual local assets. Paths resolve from the JSON file's directory, independent of where the command runs. The builder never includes their absolute paths in the output.

## Cover and slides

`title` and a nonempty `slides` list are required. The cover is added automatically and does not belong to a chapter. `title_lines` controls its line breaks; otherwise `title` appears as one heading. `author`, `affiliation`, `date` and the HTML metadata `description` are optional. Text is escaped, so literal `<`, `&` and quotes do not become markup.

Each content slide needs a `chapter` and `title`. The title appears in the overview, browser tab and accessibility label, not as a large visible heading. `note` is an optional, plain-text source caption.

Each slide contains either `figures` or `text`. A `text` value is a list of short paragraphs. Prefer figures for mechanisms and original exported tables for dense results.

## Figure layouts

| `layout` | Figures | Placement |
| --- | --- | --- |
| `single` (default) | 1 | One figure, fitted proportionally to the available area |
| `columns` | 2 | Two figures side by side |
| `strip-and-columns` | 3 | A narrow strip above two figures, in input order |

A figure requires `path` and meaningful `alt` text. Supported formats are PDF, SVG, PNG, JPEG, WebP and GIF. SVG images and styles must already have their dependent resources embedded; external resource references are rejected.

For PDF figures, `page` is **1-based** and defaults to 1. Optional `crop: [x0, y0, x1, y1]` selects a rectangle in PDF page coordinates, in points. The rectangle must lie inside the selected page. Cropping and PDF-to-SVG conversion retain vector geometry; text becomes outlines to avoid missing fonts on the recipient's machine. Existing raster layers remain raster.

## Chapters and navigation

Chapters follow their first appearance in `slides`; repeated names must remain contiguous. Their page counts determine the footer's segment widths, and the builder recalculates progress and destinations on every run. A one-slide chapter therefore has a shorter segment than a four-slide chapter. Long labels use compact type and may truncate when space is insufficient; shorten them and inspect the result.

Slide IDs include the cover: `#slide-01`, `#slide-02`, and so on. Deep links use these IDs. The appendix is simply a chapter named `Appendix`, normally placed after the main talk. No chapter names, slide counts, dates or authors are fixed in the template.

The output has no visible page counters. The overview and screen-reader announcements retain page indices for navigation. Fullscreen hides the control toolbar; F toggles it, and keyboard and touch navigation continue working.

## Checking a generated deck

Open the HTML directly and inspect the cover, changed layouts, dense figures, and chapter boundaries. Confirm labels and source notes fit and images load without network requests. Chapter widths, current progress and overview destinations should match the manifest.

For template or interaction changes, exercise figure zoom, fullscreen entry and exit, keyboard navigation, and a narrow viewport. Print with backgrounds enabled and browser headers and footers disabled; expect one slide per page. Keep verification artifacts outside the deliverable folder unless requested.
