# Guide lab: a repeatable benchmark with an honest report

Two things cannot be provided by a shared runner: a quiet machine you control and a device you may exercise at will. This is a guided exercise with success criteria. Use a scratch file or an empty scratch device (never a device with data) and a tool of your choice (`fio`, `iperf3` between two hosts, `sysbench`). The grader only checks that your report is complete, well formed and internally consistent; the evidence is in your measurements.

## Starting state

`setup` writes `bench-report.txt` in your working directory (`$LAB_DIR`) with question marks.

## Your task

| Key | What to put |
|---|---|
| `question` | the decision the benchmark supports, in a sentence |
| `tool`, `workload` | the tool and the pattern, block size or payload, and concurrency |
| `cache_bypassed` | `yes` if you used direct I/O or a set larger than RAM, `not-applicable` for CPU or network tests |
| `cpu_governor` | the governor during the runs (`cpupower frequency-info`) |
| `runs`, `min`, `median`, `max`, `unit` | at least three runs of the same configuration, with their spread |
| `limiting_resource` | what you saw saturated in `mpstat`, `iostat -x` or `sar` while the test ran |
| `changed_one_variable` | what you changed between two sets of runs |

## Success criteria

- You wrote the question and the pass/fail threshold before you ran anything.
- You recorded kernel version, CPU model, device model, filesystem, mount options and tool version in your own notes.
- You ran a warm-up, repeated the test at least three times and noticed the spread.
- You watched at least one observation tool during a run and can name the limiting resource.
- You changed exactly one variable and measured again.
- You can state one reason your number might not transfer to production.

## Grade it

`bin/lpc course lab LNX-307 benchmark-report` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `bench-report.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-307-T09). Afterwards, try [the quiz](quiz:LNX-307-T09).
