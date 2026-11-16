# LNX-403 Capstone brief: Ship a Linux Service

## Scenario

A small team needs a network service that is safe to expose, easy to install on four kinds of systems and boring to operate. You are asked to write it, test it hard, package it, lock it down, tune it and then run it in public for a month, answering real users. You deliver a repository, its CI, its packages and a record of what happened after release.

## What you deliver

One repository and one evidence folder, with one stage per milestone. Do the milestones in order; each builds on the one before.

| # | Milestone | Environment | Graded by |
|---|---|---|---|
| 1 | Epoll daemon with sd_notify and socket activation | container | lab `activated-daemon` in CI, plus your daemon |
| 2 | Fuzzing and sanitizers in CI | container | lab `fuzz-ci` in CI, plus your CI runs |
| 3 | Packages: RPM, DEB, Flatpak, OCI | container | lab `package-consistency` in CI, plus built packages |
| 4 | Hardened systemd unit | nested VM | lab `unit-hardening` in CI, plus your unit and its analysis |
| 5 | Profiling and flame graphs | shared test hardware | lab `flamegraph-evidence` structure, plus your graph and notes |
| 6 | Releases and user issues over time | time and people | lab `release-history-evidence` structure, plus your repository history |

Each milestone page lists the lessons from earlier courses it relies on. Read those first; this course adds integration, not new theory.

## Marking rubric (100 points)

| Area | Points | Full marks |
|---|---:|---|
| Service design | 20 | Socket activation, one epoll loop, readiness and stopping messages, clean shutdown, no busy loops |
| Testing in CI | 20 | Unit tests under sanitizers, a replayed corpus and crash files, a time-boxed fuzz job that fails on a crash |
| Packaging | 15 | Four formats built in CI from one version, signed, with a non-root image and no network access in package scripts |
| Hardening | 15 | Unit settings justified one by one, an exposure score before and after, a test that exercises the normal path |
| Profiling | 10 | Repeatable load, a flame graph with resolved stacks, one change, a gain beyond the noise |
| Release and users | 10 | Signed releases, an honest changelog, replies to every report, a published security policy |
| Repository quality | 10 | Small reviewed commits, a README that lets a stranger build and run it, licences stated |

Pass is 70. Anything that cannot be shown (for example a stage you could not run) must be said plainly with the reason; unconfirmed claims are marked "(to verify)" and are not marked down for that.

## Rules

- Original work. You may follow vendor and project documentation but write your own code and prose.
- Never commit passwords, private keys, tokens or cloud access keys.
- The grader labs are sanity checks. Passing them is necessary, not sufficient: the repository and evidence are what is marked.
- Choose C or Rust for the service; the graders are language-neutral models of the same logic.
- A release must not contain secrets or build paths of your machine.
