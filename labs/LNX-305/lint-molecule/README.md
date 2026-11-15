# Lab: lint a role and test it with Molecule

You will bring a small role up to the `safety` lint profile, make it safe to run twice, and write a Molecule scenario
that converges it, checks idempotence and verifies the result. The grader also damages the output to prove that your
verification really fails when it should. No containers are needed: the scenario uses Molecule's default driver with
`ansible_connection: local`.

## Starting state

`setup` writes `.ansible-lint` (profile `safety`), the role `roles/webcfg/` (tasks, defaults, a template, metadata), a
ready `molecule/default/molecule.yml` with the test sequence syntax, converge, idempotence and verify, and a blank
`answers.txt`. The role works the first time but it breaks several rules and it changes something on every run.

## Your task

1. Run `ansible-lint roles/webcfg` and read each finding. Fix them all: fully qualified module names, task names,
   explicit file modes, no unprefixed role variables, no `yes`, and no `command` or `shell` where a module does the job
   without reporting a change every time.
2. Write `roles/webcfg/molecule/default/converge.yml` (apply the role to `all`, with `webcfg_dir` set to
   `/tmp/webcfg-lab`) and `verify.yml` (read `web.conf` and assert on the port and the worker count).
3. From `roles/webcfg`, run `molecule test`. The idempotence step must report no changes.
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/lint-molecule/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/lint-molecule/check
```

## Notes

- If `molecule` or `ansible-lint` are not on your `PATH`, the grader builds a virtual environment `.venv` in your working
  directory and installs both with pip (this needs network access once).
- The lab needs the packages `ansible-core`, `python3-venv` and `python3-pip`.
- Reading material: [the lesson](lesson:LNX-305-T06). Afterwards, try [the quiz](quiz:LNX-305-T06).
