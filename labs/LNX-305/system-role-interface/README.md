# Lab: drive a system-role style role from data

RHEL System Roles all share one habit: you do not edit them, you describe the result you want in variables. In this
lab you use a small vendored role, `hostsfile`, written with the same conventions (a prefixed public interface, internal
variables with a double underscore, a per-platform vars file, an argument spec, a list of dictionaries with `state`). It
manages a hosts-style file in your working directory, so no system file is touched and no package is needed.

## Starting state

`setup` writes `ansible.cfg` (roles are found in `./roles`), a `localhost` inventory, the role under `roles/hostsfile/`,
the file `out/hosts` with `localhost` and an obsolete `old.example.org` entry, and a blank `answers.txt`. A checksum of
the role is kept in `.roles.sha`; the grader fails if you change the role.

## Your task

1. Read `roles/hostsfile/defaults/main.yml`, `meta/argument_specs.yml` and `tasks/main.yml`.
2. Write `group_vars/all.yml` that sets `hostsfile_path` to `out/hosts` inside the playbook directory and describes three
   entries: `10.0.0.5` named `db.example.org` and `db`, `10.0.0.6` named `cache.example.org`, and `10.0.0.9` removed.
3. Write `site.yml` that applies the role to `localhost` (set `gather_facts: false`; the role collects what it needs).
4. Run `ansible-playbook site.yml --check --diff`, then without `--check`, then again. The last run must change nothing.
5. Fill in `answers.txt` about the conventions of the real vendor roles.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-305/system-role-interface/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-305/system-role-interface/check
```

## Notes

- Afterwards, on a disposable RHEL, Rocky or Fedora host, try a real role: install `rhel-system-roles` and call
  `redhat.rhel_system_roles.timesync` with `timesync_ntp_servers`. The conventions are the ones you just used.
- The lab needs the package `ansible-core` and PyYAML.
- Reading material: [the lesson](lesson:LNX-305-T05). Afterwards, try [the quiz](quiz:LNX-305-T05).
