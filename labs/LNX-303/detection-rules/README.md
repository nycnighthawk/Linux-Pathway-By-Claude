# Lab: audit rules and a Falco rule that catch a webshell

`draft.rules` has two audit rules written in a hurry. Replace it with a rule set you could ship, and add a Falco rule for the classic webshell behaviour.

## Starting state

`setup` writes `draft.rules` into `$LAB_DIR`. Nothing is loaded into a kernel.

## Your task

1. `audit.rules`: start with `-D`, set a backlog of 8192 or more, watch `/etc/passwd`, `/etc/shadow` and `/etc/sudoers` for writes and attribute changes with keys, audit `execve` for both `b64` and `b32` for real login sessions only (`auid>=1000`, not `unset`), audit kernel module loading (`init_module`, `finit_module`, `delete_module`) for both architectures, and end with the rule that makes the configuration immutable.
2. `local-falco.yaml`: a Falco rule that fires when a web server process (httpd, nginx, apache2) spawns a shell. Use lists or a macro if you like. Give it a description, a condition on process execution, an output that includes the command line, a priority above notice and a MITRE tag.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/detection-rules/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/detection-rules/check
```

## Notes

- On a test machine, `augenrules --check` and `auditctl -R audit.rules` load audit rules, and `falco --validate local-falco.yaml` checks a rule file. Neither is needed for the grader.
- Reading material: [the lesson](lesson:LNX-303-T05). Afterwards, try [the quiz](quiz:LNX-303-T05).
