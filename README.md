# zedong-skill

Zedong Peng's Claude Code skills, one per thing the user does, and two for the media they share:

- `zedong-think`: thinking through research and engineering: what the work is for, the question, the experiment.
- `zedong-research`: running a research or engineering line: ownership, limits, records and reports.
- `zedong-write`: editorial taste for technical writing.
- `zedong-daily`: what the morning briefing covers: mail worth answering, then training and major news.
- `zedong-mail`: sorting mail across the three inboxes: what each kind is, what to do, when to draft a reply (in Chinese).
- `zedong-ci`: diagnosing a GitHub Actions workflow that keeps failing.
- `zedong-t3-threads`: reading and summarizing T3 Code threads, read-only.
- `zedong-quant-note`: recording a strategy, paper or experiment in the quant research repo, judged before it is written down.
- `zedong-html-fig`: drawing a figure in HTML, at print size, for a paper, page or talk.
- `zedong-html-slides`: giving a talk as an offline, figure-led HTML deck.

They hold taste, not patches: models keep getting stronger, and a rule that corrects today's model soon goes stale.

To install, clone the repo and run `./install.sh`. It links each skill into `~/.claude/skills`, or into the directory given as its argument, so a change here takes effect in the next session.
