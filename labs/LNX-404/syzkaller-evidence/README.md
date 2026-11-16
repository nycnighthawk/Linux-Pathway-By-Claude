# Guide lab: A multi-day syzkaller campaign

Run syzkaller against a kernel build for several days on hardware you can leave running, and triage what it finds. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `kernel_release` | the kernel under test (`uname -r` inside the VM) |
| `kasan_enabled` | yes if the kernel has KASAN |
| `kcov_enabled` | yes if the kernel has KCOV for coverage |
| `vm_count` | fuzzing virtual machines running in parallel |
| `run_hours` | hours the manager ran |
| `enabled_syscalls_scope` | what you enabled |
| `coverage_blocks_final` | coverage figure at the end from the manager page |
| `coverage_blocks_day1` | coverage figure after about 24 hours |
| `crash_reports` | distinct crash titles |
| `already_known` | of those, matched an existing report |
| `with_reproducer` | crashes with a reproducer |
| `reported_upstream` | new bugs you reported or fixed |

## Success criteria

- The kernel has coverage and a sanitizer, or the campaign is not graded.
- You checked every crash title against the public dashboard before reporting it.
- You kept the manager configuration and the first and last coverage figures.
- Security-relevant findings were reported privately first.

## Grade it

`bin/lpc course lab LNX-404 syzkaller-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-404-T06).
