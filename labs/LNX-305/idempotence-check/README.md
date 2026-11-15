# Lab: make a playbook safe to repeat and safe to preview

You will repair a playbook that works on the first run and then changes something every time, and make `--check`
and `--diff` give honest previews. Everything happens in `out/` inside your working directory.

## Starting state

`setup` writes `ansible.cfg`, an inventory with `localhost`, `site.yml` (five working tasks and one debug task),
`templates/motd.j2` and a blank `answers.txt`. Three tasks are not idempotent: an appended setting, a template with a
timestamp, and a command that rebuilds a directory every time. One more task reads a value that a dry run never creates.

## Your task

1. Run `ansible-playbook site.yml` twice and look at which tasks print `changed` on the second run.
2. Make the setting line appear exactly once (`setting=1`) with a module that compares before it writes, and that also replaces a different value such as `setting=2` if someone edits the file.
3. Make the message of the day identical on every run (use `ansible_managed` instead of the time).
4. Make the data directory command run only when `out/data/PG_VERSION` does not exist.
5. Make `--check` work on a fresh machine: the task that reads the data version must run in check mode too and must not
   report a change.
6. Verify with `--check --diff` on a fresh directory, on a converged one, and after editing `out/app.conf` by hand.
7. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/idempotence-check/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/idempotence-check/check
```

## Notes

- The grader runs `--check` on a fresh directory, a real run, a second run, `--check` on the converged state, then edits
  `out/app.conf` and expects a predicted change that the dry run does not apply.
- The lab needs the package `ansible-core`.
- Reading material: [the lesson](lesson:LNX-305-T07). Afterwards, try [the quiz](quiz:LNX-305-T07).
