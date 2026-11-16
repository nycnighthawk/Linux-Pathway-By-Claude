# Lab: harden a service unit

`setup` writes a service unit that runs as root with no sandboxing, and a socket unit that listens on every address. Edit them so the daemon runs unprivileged, with a read-only system, no home access, private temporary files and devices, protected kernel interfaces, no capabilities, only the address families it needs, a system-call filter and native architecture only, no writable executable memory, a declared state directory and `Type=notify`.

On a machine with systemd, finish with `systemd-analyze security pingd.service` and read the exposure score; directive support differs between versions (to verify).

## Run it

`bin/lpc course lab LNX-403 unit-hardening`, or edit the files in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-403-T04).
