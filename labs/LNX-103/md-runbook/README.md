# Lab: read a degraded RAID 5 and write the repair runbook

Kernels on shared runners often have no `md` driver, so you cannot build an array here. This lab trains the part that
matters in an incident: reading the evidence of a degraded array and writing a precise configuration and runbook.

## Starting state

`setup` writes two files under your working directory (`$LAB_DIR`): `mdstat.txt`, a copy of `/proc/mdstat` from a
server, and `detail.txt`, the output of `mdadm --detail /dev/md0` from the same server. It also writes a blank
`answers.txt`.

## Your task

1. Write `mdadm.conf` so the array assembles at boot: a `DEVICE partitions` line, `MAILADDR root`, and one `ARRAY`
   line for `/dev/md0` with `metadata=1.2`, the `name=` and the `UUID=` taken from `detail.txt`.
2. Write `runbook.txt`: one command per line, in the order you would run them, to replace the failed member with the
   new partition `/dev/sdd1`. Include marking the failed member failed, removing it, copying the partition table of a
   healthy disk (`/dev/sda`) onto `/dev/sdd` with `sfdisk -d`, adding the new partition, and a command that watches the
   rebuild. Lines starting with `#` are comments.
3. Fill in `answers.txt`: the RAID level of the array, the failed device, how many member failures this level survives,
   and the status string that `/proc/mdstat` shows for the array (the part in square brackets that marks the missing
   member with an underscore).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/md-runbook/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/md-runbook/check
```

## Notes

- Nothing here touches a real disk. The runbook is graded as text.
- The `mdadm --detail --scan` output format is the best source for the `ARRAY` line.
- Reading material: [the lesson](lesson:LNX-103-T05). Afterwards, try [the quiz](quiz:LNX-103-T05).
