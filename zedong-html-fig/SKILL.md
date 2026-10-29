---
name: zedong-html-fig
description: How the user's figures are drawn: one HTML file each, at the size it is shown, printed to PDF for LaTeX. Use when drawing a figure for a paper, page or talk.
---

A figure is one HTML file, drawn at the size it is shown and in the body font of the document it goes into, so its text matches the page. A page or deck embeds the HTML. For LaTeX it is printed to PDF and included at natural size, with no `width=`.

For a NeurIPS paper the column is 5.5in and the font Times:

```css
@page { size: 5.5in 4in; margin: 0 }  /* height generous; the crop trims it */
html, body { margin: 0 }
body { width: 5.5in; font-family: "Times New Roman", Times, serif;
       print-color-adjust: exact; -webkit-print-color-adjust: exact }
```

```sh
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless \
  --no-pdf-header-footer --print-to-pdf=fig.pdf "file://$PWD/fig.html"
pdfcrop --margins 2 fig.pdf fig.pdf
```

On Linux the browser is `google-chrome` or `chromium`.
