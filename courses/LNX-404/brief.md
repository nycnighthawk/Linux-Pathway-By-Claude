# LNX-404 Capstone brief: Upstream-Quality Kernel Work

## Scenario

A hardware vendor wants a Linux driver for a new device and wants it in the mainline kernel, not in a private fork. You are asked to develop it against an emulated device, make it pass the project's checks on two architectures, prove you can find and fix regressions, get a real change through public review, run it on a physical board and shake it with a fuzzer. You deliver a branch of patches and an evidence folder.

## What you deliver

One repository and one evidence folder, with one stage per milestone. Do the milestones in order; each builds on the one before.

| # | Milestone | Environment | Graded by |
|---|---|---|---|
| 1 | Driver for a QEMU device with KUnit tests | nested VM | lab `edu-driver-model` in CI, plus your driver and tests |
| 2 | Series passes checkpatch; boots on x86_64 and arm64 | nested VM | lab `series-verdict` in CI, plus your series |
| 3 | Bisect and fix a planted regression | nested VM | lab `bisect-sim` in CI, plus your bisect log |
| 4 | Submit to a real subsystem list and address review | people and time | lab `list-review-evidence` structure, plus archive links |
| 5 | Run on a real development board | hardware | lab `dev-board-evidence` structure, plus your boot log |
| 6 | Multi-day syzkaller campaign | shared hardware | lab `syzkaller-evidence` structure, plus the manager configuration and reports |

Each milestone page lists the lessons from earlier courses it relies on. Read those first; this course adds integration, not new theory.

## Marking rubric (100 points)

| Area | Points | Full marks |
|---|---:|---|
| Driver and tests | 20 | Clear split between register access and logic, KUnit cases for errors and timeouts, the driver loads against the real emulated device |
| Series quality | 20 | Each commit builds on both architectures, checkpatch clean, cover letter explains testing, boot test on both |
| Bisect and fix | 15 | Reproducible test script, culprit found by bisection, minimal fix with a regression test and a Fixes tag |
| Public review | 15 | Right maintainers and list, versioned revisions, every comment answered, links recorded |
| Real board | 10 | Serial log, safe wiring, differences from the emulator explained |
| Fuzzing campaign | 10 | Sanitizer and coverage enabled, at least two days, crashes triaged against known reports |
| Repository quality | 10 | Small commits, signed off, a README that lets a stranger reproduce each stage |

Pass is 70. Anything that cannot be shown (for example a stage you could not run) must be said plainly with the reason; unconfirmed claims are marked "(to verify)" and are not marked down for that.

## Score levels

Each rubric area is marked at one of four levels, so two markers reach the same number.

| Level | Share of the area's points | What it looks like |
|---|---:|---|
| Full | 100% | Everything in the Full marks column, with evidence a stranger can check |
| Most | 70% | It works, but one element of Full marks is missing or its evidence is thin |
| Some | 40% | A design or partial build exists, but the working evidence is missing |
| None | 0% | Not attempted, or the evidence does not support the claim |

A substitute from the fallback table below is marked the same way, but cannot score above Most for that area.

## Resources and time budget

These are planning estimates, not limits. Record your actual figures in the README.

| Item | Estimate |
|---|---|
| Lab host | 16 GB RAM, 8 cores and about 100 GB of disk for kernel trees and two build directories (x86_64 and arm64) |
| Time | about 100 hours: milestone 1 about 25, 2 about 15, 3 about 15, 4 about 15 plus weeks of waiting, 5 about 15, 6 about 15 of work over at least two days of running |
| Board | any low-cost arm64 board with a 3.3 V serial console, about 50 to 100 US dollars |
| Fuzzing | a host that can run several VMs for two days; a spare desktop is enough |

## If you cannot run a milestone

| Milestone | Substitute | Area affected |
|---|---|---|
| 4 Public review | If no reply arrives in time, submit the archive link and your v2 prepared from a mock review by a peer; a real reply still earns more | Public review |
| 5 Real board | Boot on QEMU `virt` with a board-like device tree and explain three things real hardware would change | Real board |
| 6 Multi-day campaign | Run at least twelve hours on your own machine with the same configuration and triage what you find | Fuzzing campaign |

## Rules

- Original work. You may follow vendor and project documentation but write your own code and prose.
- Never commit passwords, private keys, tokens or cloud access keys.
- The grader labs are sanity checks. Passing them is necessary, not sufficient: the repository and evidence are what is marked.
- Every patch carries a Signed-off-by line and follows the project's rules on the developer certificate.
- Security-relevant fuzzing findings are reported privately first; do not publish a reproducer for a live vulnerability.
