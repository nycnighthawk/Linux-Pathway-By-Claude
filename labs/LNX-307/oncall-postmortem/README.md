# Guide lab: write a blameless postmortem

Being on call cannot be simulated by a runner, and the judgement in a good postmortem cannot be graded by a script. This is a guided exercise: you receive the facts of one incident and write the review. The grader checks shape and consistency, so that a reviewer can spend their time on the substance.

## Starting state

`setup` writes `incident.txt` (timestamps and facts) and a template `postmortem.md`.

## Your task

Rewrite `postmortem.md` with these headings: Summary, Impact, Timeline, Root cause, Contributing factors, What went well, What went badly, Action items.

- The timeline has at least five entries, each starting with a UTC time like `02:10Z`, in ascending order, including 02:05Z, 02:10Z and 02:21Z.
- Add a line `minutes_to_mitigate=N` with the minutes from the page to recovery.
- The root cause names the configuration cause from the notes, without naming a person.
- Write at least three action items in the form `- action | owner: team | due: YYYY-MM-DD | class: prevent` using at least two classes from prevent, detect and mitigate.

## Success criteria

- A reader who was not there can follow what happened and why it was not caught earlier.
- Every action has an owner and a date and says which defence it improves.
- You describe how the system and process allowed the error, not who is at fault.
- You noted what you would collect before a mitigating restart.

## Grade it

`bin/lpc course lab LNX-307 oncall-postmortem` checks the starting state and the structure of the sample answer; to grade your own run `check` with `LAB_DIR` set to the directory that holds `postmortem.md` and `incident.txt`.

## Notes

- This lab is not run by CI (environment O: human judgement); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-307-T10). Afterwards, try [the quiz](quiz:LNX-307-T10).
