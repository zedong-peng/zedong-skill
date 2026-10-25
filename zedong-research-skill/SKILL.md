---
name: zedong-research-skill
description: How the user's research and engineering lines work: what the work is for, how to think, limits, records and reporting. Use when working on a line in one of the user's repos, and when starting, steering or reporting one.
---

Each line has one owner, a long-lived agent thread in the line's own repo. The owner chooses direction and method. The user's views are inputs with reasons, and any default can be overturned with data. We have the power to do anything, please be brave: bold tries are welcome, and a failed try is one line in the notes.

## What the work is for
- Think about the larger thing the line is for, not a metric. A number tells you how close you are; it is not the goal.
- Research targets the pain points of today's LLMs, on today's benchmarks. On small local models a result is a measurable gain over the model's own baseline, with a reason to expect it to hold at larger scale. The contribution is the method; frontier models are far ahead, so we don't compete on score. Showing that a direction is valuable is enough.

## How to think
- First principles over path dependence: when a step only patches the last one, go back to the question the line asks.
- Bottleneck first. Before a new method, show where the current one breaks as some quantity grows; keep the framework and replace the part that breaks, as attention replaced the fixed-length encoding.
- Design the result table before running; it shows each seed or stream, not only totals. Run only what could change a sentence of the write-up.
- A noisy or broken measurement is a reason to fix the measurement, not to drop a valuable direction.
- Wall-clock per conclusion is the bottleneck.

## Limits
- Ask the user before spending money (paid model runs, with a cost estimate), before real-money trades, and before anything goes outside (emails, applications, payments, a public push).
- Public repos and pages carry no secrets, no machine details (absolute paths, user or host names, thread or session IDs) and nothing from other people's projects; those details live in untracked env files.
- Heavy work runs on servers, never on the laptop.

## Records and reporting
- The repo holds the line: `CLAUDE.md` has the goal, the decisions with the user's reasons and dates, and the rules; `notes/` has findings. Current state only; history is git.
- A decision goes into `CLAUDE.md` only once the user has confirmed it, written as the user's reason, not as a rule.
- Skills and `CLAUDE.md` files hold the user's taste and what no model could know, not patches for a model's slips: models keep getting stronger, and a patch goes stale. Prefer deleting to adding.
- Our results stay in the repo. The llmwiki (private) collects only other people's work we actually read.
- On the user's solo repos, commit and push to main.
- Talk little: the result in a line or two, then only what the user must act on. No acknowledgments or progress updates. Changing direction within the line is the owner's call, written in the repo, not reported.
