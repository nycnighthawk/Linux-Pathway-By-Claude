# Lab: a hardened service and its timer

Replace a cron job with a systemd timer. You write the two unit files; nothing is installed or started, so the lab is safe to run anywhere.

## Starting state

`setup` writes `backup.service` and `backup.timer`, each with only a `[Unit]` description, in your working directory (`$LAB_DIR`).

## Your task

`backup.service` needs a `[Service]` section that:

- is `Type=oneshot`;
- runs an absolute, existing program with `ExecStart=` (for example `/usr/bin/logger -t backup nightly-run`);
- runs as an unprivileged account with `User=` (for example `daemon`; `nobody` makes verify complain);
- sets `ProtectSystem=strict` and `NoNewPrivileges=yes`.

`backup.timer` needs:

- a `[Timer]` section with a valid `OnCalendar=` (nightly, for example `*-*-* 02:30:00`), `Persistent=true` and a `RandomizedDelaySec=`;
- an `[Install]` section with `WantedBy=timers.target`.

The timer needs no `Unit=` line because `backup.timer` activates `backup.service` by name.

## Grade it

`bin/lpc course lab LNX-203 timer-unit` runs the whole cycle. To grade your files run `check` with `LAB_DIR` set to the directory that holds them. The grader runs `systemd-analyze calendar` on your expression and `systemd-analyze verify` on both files, which must be silent.

## Notes

- `systemd-analyze calendar 'EXPR'` prints the normalized form and the next elapse time.
- `systemd-analyze verify` reports unknown directives and missing programs.
- Reading material: [the lesson](lesson:LNX-203-T07). Afterwards, try [the quiz](quiz:LNX-203-T07).
