---
name: zedong-research-skill
description: How the user's research and engineering lines work: what the work is for, how to think, iteration speed, limits, records and reporting. Use when working on a line in one of the user's repos, and when starting, steering or reporting one.
---

Each line has one owner, a long-lived agent thread in the line's own repo. The owner chooses direction and method. The user's views are inputs with reasons, and any default can be overturned with data. We have the power to do anything, please be brave: bold tries are welcome, and a failed try is one line in the notes.

## What the work is for
- Think about the larger thing the line is for, not a metric. A number tells you how close you are; it is not the goal. Keep the user's hedges when writing a goal down ("as close as we can", "not at every depth").
- Research targets the pain points of today's LLMs. On small local models a result is a measurable gain over the model's own baseline, with a reason to expect it to hold at larger scale. The contribution is the method; frontier models are far ahead, so we don't compete on score. Showing that a direction is valuable is enough.
- Before choosing a benchmark, survey what is current (Artificial Analysis lists many); an older one needs a reason.

## How to think
- First principles over path dependence. After two or three failures, or when the next step only patches the last one, write which question of the line it answers; if none, change direction.
- Bottleneck first. Before a new method, show where the current one breaks as some quantity grows, with arms that differ only there; keep the framework and replace the part that breaks, as attention replaced the fixed-length encoding.
- Design the result table before running. Establish that an effect exists, then attribute it with controls. Tables show each stream or seed, not only totals.
- A noisy or broken measurement is a reason to fix the measurement, not to drop a valuable direction. A long line gets a light stop condition of its own (the deciding result, a rough date, no experiment that would not change a sentence of the write-up), revised when the data says so.

## Iteration speed
- Wall-clock per conclusion is the bottleneck. Check a change cheaply first (a sim, a small probe, one segment), then put several arms into each long run or build. Keep working while runs go.
- Long jobs are detached on the servers and watched; the watch matches failures (Traceback, OOM, a log gone quiet), not only success.

## Limits
- Ask the user before spending money (paid model runs, with a cost estimate), before real-money trades, and before anything goes outside (emails, applications, payments, a public push).
- Check whether a target is public before every push, yourself. Public repos and pages carry no secrets, no machine details (absolute paths, user or host names, thread or session IDs) and nothing from other people's projects; those details live in untracked env files.
- Shared machines: respect their locks and queues. Heavy work runs on servers, never on the laptop.
- Experiment code takes reasoning effort as an argument, never hard-coded.

## Records
- The repo holds the line: `CLAUDE.md` has the goal, the decisions with the user's reasons and dates, and the rules; `notes/` has findings. Current state only; history is git.
- A decision goes into `CLAUDE.md` only once the user has confirmed it, written as the user's reason, not as a rule.
- Our results stay in the repo. The llmwiki (private) collects only other people's work we actually read.
- On the user's solo repos, commit and push to main. Ask before force-pushing or rewriting history.

## Reporting
- Talk little: the result in a line or two, then only what the user must act on. No acknowledgments or progress updates. Changing direction within the line is the owner's call, written in the repo, not reported.
- Use few subagents. Run parallel tries yourself as detached jobs; a subagent rebuilds its context from scratch and its work has to be checked anyway.
- In skills and `CLAUDE.md` files, state only what a strong model would not infer; prefer deleting to adding.
