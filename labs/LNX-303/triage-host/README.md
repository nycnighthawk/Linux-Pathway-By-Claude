# Lab: triage a compromised host

`evidence/` holds what a first responder collected from `web01`: the SSH log, a user crontab, an `authorized_keys` file, `/etc/ld.so.preload`, `lsof +L1` output and `ss` output. Treat it as read-only evidence.

## Starting state

`setup` writes the `evidence/` directory into `$LAB_DIR`.

## Your task

1. Write `findings.json` with these keys: `account` (the compromised account), `source_ip`, `first_access` (ISO time of the first successful attacker login), `persistence` (a list of the three file paths an attacker used to survive reboots), `c2` (the remote `ip:port` the deleted binary talks to), `deleted_binary_pid`, and `steps`: your response order, chosen from `isolate-network`, `capture-memory`, `copy-proc-exe`, `image-disk`, `hash-evidence`, `rebuild`. Follow the order of volatility, and do not reboot or reinstall before the evidence is saved.
2. Write `evidence-hashes.txt` with a SHA-256 for each file in `evidence/` (`sha256sum` format).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/triage-host/setup
# ...read the evidence, write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/triage-host/check
```

## Notes

- Do not edit anything under `evidence/`: the hashes must still match.
- Reading material: [the lesson](lesson:LNX-303-T10). Afterwards, try [the quiz](quiz:LNX-303-T10).
