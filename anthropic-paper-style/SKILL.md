---
name: anthropic-paper-style
description: How the user's papers are built, after Anthropic's research papers: structure, template and figures. Use when planning, drafting or restructuring a paper for the user, with zedong-writing-style for the prose.
---

- Introduction, then one short section of setup or method, then one section per finding, each titled with its claim or question. No "Experiments" section. Related Work comes after the findings, then limitations, discussion and conclusion. Detail goes to the appendix.
- On arXiv: NeurIPS's style in preprint mode, `\usepackage[preprint]{neurips_2026}`, one column, Times. A version for a venue uses that venue's template.
- Figures are drawn in HTML, one file each, printed to PDF and included in the LaTeX at natural size, with no `width=`. Each is drawn at print size in the body font, so its text matches the page; the NeurIPS column is 5.5in:

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
