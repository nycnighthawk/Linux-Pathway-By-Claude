# Lab: override a vendor unit with a drop-in and enable it

A package ships `labapp.service` in `/usr/lib/systemd/system`. You must change three settings without editing that
file, so that a package update does not undo your change. Everything happens in a scratch root, which `systemctl` and
`systemd-analyze` read through `--root=DIR`.

## Starting state

`setup` creates `root/usr/lib/systemd/system/labapp.service` (restart policy `no`, a 90 second stop timeout) and a
few copies of the standard targets, plus an empty `root/etc/systemd/system`.

## Your task

1. Create a drop-in `root/etc/systemd/system/labapp.service.d/override.conf` with a `[Service]` section that sets
   `Restart=on-failure`, `TimeoutStopSec=10` and `Environment=LAB_MODE=prod`.
2. Confirm that systemd sees the merged result: `systemd-analyze --root="$PWD/root" cat-config systemd/system/labapp.service`.
3. Enable the unit for `multi-user.target` inside the scratch root with `systemctl --root="$PWD/root" enable labapp.service`.
4. Leave the vendor unit unchanged.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/unit-override/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/unit-override/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
real machine, try `systemctl edit labapp.service` and `systemctl cat labapp.service` and compare them with your files.

## Notes

- `systemctl edit` creates the same `override.conf` file; `systemctl edit --full` copies the whole unit instead.
- To reset a list setting such as `ExecStart=`, a drop-in must first assign it empty.
- Reading material: [the lesson](lesson:LNX-102-T03). Afterwards, try [the quiz](quiz:LNX-102-T03).
