# Lab: repair a simulated host with four planted faults

A web application is down after a reboot. The "host" is a directory tree under `host/` so that you can practise safely and the grader can check the outcome without root. Treat it like a real incident: find each cause from the evidence, fix it, and record what you found.

## Starting state

`setup` builds `host/` with a unit file, an application directory, a configuration file, `host/proc/listeners.txt` (a stand-in for `ss -ltnp`), an fstab and a log directory, and writes `answers.txt`.

## Your task

1. Read the unit file and the application directory. The unit cannot start: repair the cause so the `ExecStart` target exists and is executable.
2. Read the configuration and the listener list. The configured port is taken by another process: pick a free port of 1024 or more and note who owned it.
3. Read the fstab. One entry can drop a host to emergency mode if its device is missing: make it harmless.
4. The application log is never rotated: write `host/etc/logrotate.d/webapp`.
5. Fill in `answers.txt` (the systemd result code for the failed start, the port owner, the hazardous device, a phrase about the log problem).

Change one thing at a time and keep a copy of anything you edit (`cp -a file file.orig`).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/breakfix-host/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/breakfix-host/check
```

## Notes

- The grader checks outcomes (files, modes, free port), not the exact fix you chose.
- Reading material: [the lesson](lesson:LNX-307-T07). Afterwards, try [the quiz](quiz:LNX-307-T07).
