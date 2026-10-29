---
name: zedong-write
description: The user's writing: what to say, how to say it, and how a paper is built. Use when drafting, revising or publishing a technical page, blog post or paper for the user, or deciding what a talk says.
---

The standard is one word: Anthropic. Work should read like Anthropic's blog and research reports: concise and clear, sure of its technical ground, and showing research taste in what it claims and how it backs the claim. The reader is a smart outsider with little time; the writer does the interpretive work so the reader doesn't have to.

## What to say

Less is more. A write-up is not better for being complete: each part earns the reader's attention, or it goes.

- Spend words on what is new and hard. What the reader would assume, or grasps at once, gets a clause or nothing.
- What a figure can show accurately, a figure shows: easy to read, not simplistic. The text supports it.
- Detail that backs a claim but is not the claim goes to the appendix.
- Don't argue that a part is worth it. The result shows it, or the part goes.
- What the approach entails is stated, not apologized for. A choice made for the setting is a decision for that setting, not a limitation or a roadmap.

  BAD

  > Limitations: the design supports only batch size 1. Batched prefill and multiple sequences are left to future work.

  GOOD

  > We target single-stream decoding at batch 1, and spend the chip's limited resources there.

## How to say it

- Technical write-ups for peers are in English.
- When revising, settle each section's role first, then restructure; don't polish sentence by sentence.
- Define each term at first use, or rename it. One word, one meaning.
- One metric per quantity. Say whether each number is measured, derived or nominal.
- Derive in the order things are decided, with every unit step shown.
- Few percentages and ratios; scores are the exception, given as percentages.
- One color means one thing across all figures.

## Papers

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

## Talks

A talk has its own skill, zedong-talk, for offline HTML decks. Ask the user whether to use it.
