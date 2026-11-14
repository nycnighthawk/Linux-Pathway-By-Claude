# Lab: a chrony policy and a time zone

Time must be right on every machine, and the settings that make it so are a few lines in `chrony.conf` plus one
symlink. You will bring a starting configuration up to a written policy and set the time zone the way
`timedatectl set-timezone` does, in a scratch root.

## Starting state

`setup` creates `chrony.conf` (one pool line and a drift file) and `root/` with `etc/` and a link to the host's zone
database in `root/usr/share/zoneinfo`.

## Your task

1. Edit `chrony.conf` so it keeps its pool line (with `iburst`) and its drift file, and also: steps the clock when the
   offset is over 1 second during the first 3 updates, keeps the hardware clock in step, serves time to
   `192.168.10.0/24`, and logs tracking data.
2. Validate it with `chronyd -p -f chrony.conf`, which parses the file and prints the result.
3. Make `root/etc/localtime` a symbolic link to the Europe/Berlin zone file under `root/usr/share/zoneinfo`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/time-sync/setup
# ...edit chrony.conf, make the link...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/time-sync/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
real machine, compare with `timedatectl`, `chronyc tracking` and `chronyc sources -v`.

## Notes

- The lab needs the packages `chrony` and `tzdata`.
- Reading material: [the lesson](lesson:LNX-102-T07). Afterwards, try [the quiz](quiz:LNX-102-T07).
