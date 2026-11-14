# Lab: the same schedule as a cron line and as a systemd timer

Run `jobs/backup.sh` at 02:30 on weekdays, once with cron and once with a systemd timer. The point is to see both
syntaxes side by side and to notice what the timer adds: a separate service unit, a calendar parser you can query, and
catch-up runs after downtime.

## Starting state

`setup` creates `jobs/backup.sh` and empty directories `jobs/` and `units/` in your working directory (`$LAB_DIR`).

## Your task

1. Write `jobs/backup.cron` in the **system** crontab format (it has a user field): 02:30, Monday to Friday, as root,
   running the full path of `jobs/backup.sh`.
2. Write `units/backup.service` (`Type=oneshot`, `ExecStart` with the full path) and `units/backup.timer` (`OnCalendar`
   for Monday to Friday at 02:30, `Persistent=true`, `WantedBy=timers.target`).
3. Check the calendar with `systemd-analyze calendar` and the units with `systemd-analyze verify`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/schedule-jobs/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/schedule-jobs/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards,
look at `systemctl list-timers` on a real system and find which jobs were already scheduled by your packages.

## Notes

- A user crontab (`crontab -e`) has five time fields then the command; the system files `/etc/crontab` and
  `/etc/cron.d/*` add a sixth field for the user.
- Reading material: [the lesson](lesson:LNX-102-T06). Afterwards, try [the quiz](quiz:LNX-102-T06).
