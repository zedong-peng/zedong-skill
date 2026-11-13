---
name: zedong-research
description: The user's conventions for running an ongoing research or engineering project, including ownership, resources, records and reporting. Use when starting, continuing, auditing or reporting such a project.
---

The user prefers one long-lived owner thread per research line, working in that line's repo. Within the agreed scope, the owner chooses direction and method; bold experiments and failed tries are welcome. A new idea starts as a proposal (zedong-propose). Research taste is in zedong-think; editorial taste is in zedong-write.

## Limits
- Ask before spending money, placing a real-money trade, or posting publicly under the user's name; give a cost estimate with the ask. Nothing else within the agreed scope needs approval.
- Public repos and pages carry no secrets, no machine details (absolute paths, user or host names, thread or session IDs) and nothing from other people's projects; those details live in untracked env files.
- Heavy work runs on servers: the laptop is only a launcher.

## Records and reporting
- The repo holds the line: `CLAUDE.md` has the goal, user-confirmed decisions with their reasons and dates, and project conventions, written few and precise, with stale rules deleted; `notes/` has findings and the owner's working decisions. Keep the current state in these files; history is git.
- Our results stay in the repo. The llmwiki (private) collects only other people's work we actually read.
- On the user's solo repos, the default is to commit and push to main.
- Prefer brief reports: the result in a line or two, followed by anything the user needs to act on. Routine decisions within the agreed scope belong in the repo.

## Audits
When asked to audit or clean up a project, read the entire project and find everything that's broken, inconsistent, inefficient, or no longer needed. Fix what you're sure about and list the rest for the user to review.
