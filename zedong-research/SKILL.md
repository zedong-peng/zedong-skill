---
name: zedong-research
description: The user's conventions for running an ongoing research or engineering project, including ownership, resources, records and reporting. Use when starting, continuing or reporting such a project.
---

The user prefers one long-lived owner thread per research line, working in that line's repo. Within the agreed scope, the owner chooses direction and method; bold experiments and failed tries are welcome. Research taste is in zedong-think; editorial taste is in zedong-write.

## Limits
- Spending, real-money trades and external actions need user authorization. For paid runs outside an approved budget, give a cost estimate before asking. Existing authorization applies; the solo-repo publishing default is below.
- Public repos and pages carry no secrets, no machine details (absolute paths, user or host names, thread or session IDs) and nothing from other people's projects; those details live in untracked env files.
- Heavy work runs on servers, never on the laptop.

## Records and reporting
- The repo holds the line: `CLAUDE.md` has the goal, user-confirmed decisions with their reasons and dates, and project conventions; `notes/` has findings and the owner's working decisions. Keep the current state in these files; history is git.
- Our results stay in the repo. The llmwiki (private) collects only other people's work we actually read.
- On the user's solo repos, the default is to commit and push to main.
- Prefer brief reports: the result in a line or two, followed by anything the user needs to act on. Routine decisions within the agreed scope belong in the repo.
