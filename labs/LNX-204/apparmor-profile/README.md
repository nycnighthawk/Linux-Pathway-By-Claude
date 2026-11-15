# Lab: tighten a learned AppArmor profile

A learning run left a profile in complain mode that allows every file, every capability and all networking. You will
turn it into an enforcing allow-list and check that the parser accepts it. The profile is parsed, not loaded into the
kernel, so any container or VM can run the lab.

## Starting state

`setup` writes `report.profile` for `/usr/local/bin/report` and a blank `answers.txt`.

## Your task

1. Remove `flags=(complain)`.
2. Replace the broad rules by exactly these: capability `net_bind_service`; `network inet stream`; read
   `/etc/report/**`; write `/var/log/report.log`; read, write and lock `/var/lib/report/**`; map and read its own
   binary (`mr`); and explicit denies for `/home/**` (`rwx`) and `/etc/shadow` (`rwx`). Keep the base abstraction.
3. Check it: `apparmor_parser -Q -K report.profile` (parse only, no kernel load).
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/apparmor-profile/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/apparmor-profile/check
```

## Notes

- The lab needs the `apparmor` package (parser and abstractions). The "Cache read/write disabled" warning is harmless.
- On a host with AppArmor enabled, load it with `apparmor_parser -r` and watch `journalctl -k | grep DENIED`.
- See [the lesson](lesson:LNX-204-T05) and [the quiz](quiz:LNX-204-T05).
