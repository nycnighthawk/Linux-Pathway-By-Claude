# Lab: a blameless post-incident review that checks out

`setup` writes `review.txt`, a plain-text review with mistakes: durations that do not match the times, a timeline out of order, an action without an owner, a cause that is not covered by any action, a vague action, and wording that blames a person. Fix the file until `check` passes.

The grader checks structure and arithmetic only. A review can pass and still be shallow; the point of the exercise is to write causes that name conditions in the system and actions that can be verified.

## Run it

`bin/lpc course lab LNX-401 incident-review`, or edit `review.txt` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-401-T06).
