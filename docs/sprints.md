# Sprint Log — CRE Status Agent

## Sprint 1 (Oct 27 – Nov 10, 2026)

**Goal:** My script reads the Monday CSV, cleans it and shows progress for each of the 4 phases.

### Notes
- Oct 27: I opened the Monday export in TextEdit and found the data wasn't clean: the headers repeat for each phase, and there are title, summary and empty rows mixed in. Good news: names with commas are wrapped in quotes, so Python's csv module can handle them. Cleaning this is my first code challenge.

### Review
- Result: Goal met. The script reads 18 tasks and shows the progress for each phase.
- Done: CSA-8, CSA-9, CSA-10, CSA-11, CSA-13
- Not done (and why): CSA-12 (stretch) — not started. I had 3 days off, so I focused on the sprint goal first.
- Demo: When I run read_monday.py, it cleans the data: it skips the title, the phase rows, the repeated headers, and the empty rows. No status warnings were displayed, so the data passed validation. During the demo I found a format bug (50 % instead of 50%), and I fixed it with an f-string.

### Retro
- What worked: Predicting the output before running the code, breaking the code on purpose to learn how to read a traceback, checking the data before cleaning it, and adding a warning instead of fixing bad data silently.
- What didn't work: My estimates. CSA-9 part 1 took twice its timebox, and CSA-8 and CSA-10 had no timebox at all. Small mistakes also slipped through (unsaved files, indentation, wrong working directory).
- What I'll change in Sprint 2: (1) Set a timebox for every ticket and log the actual time; if I go 30 minutes over, I stop and split the ticket. (2) Use a quick checklist before running code: Cmd+S, cd into the project, check the file name.


## Sprint 2 (Nov 6 – Nov 20, 2026)

**Goal:** The agent reads the Monday CSV, flags overdue and upcoming tasks, uses the Claude API to draft a weekly executive status for the COO, returns it as validated JSON, and the repo has a case-study README.

### Review
- Result: Goal met, 9 days before the sprint ends. The agent works end to end: CSV → overdue and upcoming tasks → Claude API → validated JSON → case-study README.
- Done: CSA-12, CSA-14, CSA-15, CSA-16, CSA-17, CSA-22
- Not done (and why): Nothing from the sprint backlog. The rest of CSA-18 and CSA-20 (stretch) were not started. I decided not to add more work to this sprint and moved them to Sprint 3.
- Demo: When I run status_agent.py, it reads the 18 tasks, finds the overdue and upcoming ones, and sends them to Claude with their dependencies. Claude drafts a weekly status for the COO (summary, risks, next steps), and the script validates the keys and types before printing the JSON. I also tested the setup from a clean clone: without the .env file, the agent shows a clear "missing API key" message instead of crashing.

### Retro
- What worked: My estimates. I planned 11–12 hours and the sprint took about 11. Three tickets finished under their timebox (CSA-15, CSA-17, CSA-22) and two only 5 minutes over (CSA-12, CSA-14). QA against the CSV also worked: I found 3 hallucinations (invented dependencies on the PSA, "Financing has not started", and suggestions to assign owners that already exist) and fixed them with grounding rules, re-tests and a regression check.
- What didn't work: CSA-16 went 35 minutes over its timebox (3h35 vs. 3 h). I split it into a part 2, as planned, but the ticket was too big: the refactor could have been its own ticket. A new type of small bug also showed up twice: leaving a placeholder instead of the real value (the API key in CSA-15 and KeyError '___' in CSA-16).
- Did my Sprint 1 action items work? (1) Timebox + actual time: yes, on all 6 tickets. (2) Pre-run checklist: partly. I had fewer unsaved-file and wrong-folder mistakes, but the checklist didn't catch placeholders.
- Known minor issues: "1 days late" (should be "1 day late"); the "Check the error above" message is misleading when there was no API error; the output varies between runs and sometimes adds a speculative or repeated risk.
- What I'll change in Sprint 3: (1) Add a placeholder check to my pre-run checklist (Cmd+F for ___). (2) Split any ticket estimated over 2 hours before I start it. (3) Start every ticket with the pain it solves.