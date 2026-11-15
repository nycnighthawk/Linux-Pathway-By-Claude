# Lab: triage a stalled domain controller and write the SYSVOL job

You will read recorded output from a two-DC Samba domain, name what has stopped replicating and why, and write the shell script that keeps SYSVOL in step from the right source. Nothing needs a real domain controller.

## Starting state

`setup` writes `showrepl.txt` (output of `samba-tool drs showrepl` on `dc2`), `fsmo.txt` (output of `samba-tool fsmo show`), a stub `sysvol-sync.sh` and `answers.txt`.

## Your task

1. `answers.txt`: `failing_partition` (the naming context with the failure, as printed), `error_number` (the Windows error number), `root_cause` (one of `dns`, `firewall`, `credentials`, `database`), `repair_command` (the Samba tool that recreates a DC's missing DNS records) and `pdc_holder` (the DC holding the PDC emulator role).
2. `sysvol-sync.sh`: a bash script run on `dc2` that pulls SYSVOL from the PDC emulator holder into `/var/lib/samba/sysvol/` with `rsync`, keeping extended attributes and ACLs (`-X` and `-A`), deleting files that no longer exist at the source after the transfer (`--delete-after`), and then running `samba-tool ntacl sysvolreset`. The source host must be the PDC emulator holder you found, not a hard-coded guess. It must be valid bash (`bash -n`).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/dc-replication-triage/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/dc-replication-triage/check
```

## Notes

- Check order for replication faults: DNS, then Kerberos and time, then firewall, then the database.
- Reading material: [the lesson](lesson:LNX-302-T03). Afterwards, try [the quiz](quiz:LNX-302-T03).
