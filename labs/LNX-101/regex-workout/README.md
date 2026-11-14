# Lab: write patterns that match exactly the right lines

Five small patterns, each tested against lines that must match and lines that must not. Two dialects are involved:
four extended expressions (the form you pass to `grep -E`) and one basic expression (plain `grep`). One of the five
needs a backreference.

## Starting state

`setup` creates five files in your working directory (`$LAB_DIR`), each holding only comments. Replace the comment
text by one pattern on the first line that is not a comment (comments start with `#`).

| File | Dialect | What the pattern must accept |
|---|---|---|
| `ipv4.ere` | extended | a whole line that is a dotted-quad IPv4 address: four numbers from 0 to 255 without leading zeros |
| `date.ere` | extended | a whole line in the form `YYYY-MM-DD` with month 01 to 12 and day 01 to 31 |
| `hex.ere` | extended | a whole line that is `0x` followed by one to eight hexadecimal digits, upper or lower case |
| `repeated.ere` | extended | any line that contains the same word twice in a row, separated by one space |
| `digits.bre` | basic | a whole line of two or more digits followed by a semicolon, using a bounded repetition |

## Your task

Write the five patterns. The grader runs `grep` against hidden lists of good and bad lines and prints the ones you got
wrong. Anchor the patterns where the table says "whole line". Remember that in the basic dialect the braces of a
bounded repetition need backslashes, and that the extended dialect lets you group and refer back.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-101/regex-workout/setup
# ...fill in the five files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-101/regex-workout/check
```

In CI the harness runs `setup`, proves `check` fails, copies `solution/` over the work directory, and proves `check` passes.
Afterwards, try your `ipv4.ere` with `grep -P` and the nested-repetition pattern from the lesson on a long line to feel
the difference between engines.

## Notes

- Date validation here checks the shape and the month and day ranges only, not leap years. Real validation belongs in code.
- Reading material: [the lesson](lesson:LNX-101-T06). Afterwards, try [the quiz](quiz:LNX-101-T06).
