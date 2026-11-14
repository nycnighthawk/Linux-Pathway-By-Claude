# Lab: default target, enabled and masked units, and boot-loader defaults

Boot behaviour is a set of small files: a symlink for the default target, symlinks that enable units, a symlink to
`/dev/null` that masks one, and a defaults file that the boot-loader tools turn into a configuration. You will change
all of them in a scratch root, so no real boot setting is touched.

## Starting state

`setup` creates `root/` with copies of the standard targets, a default target of `graphical.target`, two units
(`labweb.service`, `labbluetooth.service`), `root/etc/default/grub` and `answers.txt` with four question marks.

## Your task

1. Make `multi-user.target` the default target, using `systemctl --root="$PWD/root" set-default`.
2. Enable `labweb.service` and mask `labbluetooth.service`.
3. In `root/etc/default/grub` set `GRUB_TIMEOUT=5`; change `GRUB_CMDLINE_LINUX` so it no longer contains `quiet`, adds
   `console=ttyS0,115200n8` and keeps `rhgb`.
4. Fill in `answers.txt`: the kernel arguments that boot rescue and emergency mode, whether rescue mode asks for the
   root password, and the command that regenerates `grub.cfg` on RHEL-family systems (write it without spaces).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/boot-targets/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/boot-targets/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
disposable virtual machine, boot once with `systemd.unit=rescue.target` added at the boot menu and return to the normal
target with `systemctl default`.

## Notes

- `systemctl --root=DIR` edits symlinks only; it never talks to a running manager.
- Reading material: [the lesson](lesson:LNX-102-T04). Afterwards, try [the quiz](quiz:LNX-102-T04).
