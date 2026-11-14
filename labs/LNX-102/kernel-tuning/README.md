# Lab: kernel parameters and modules, runtime versus persistent

Kernel settings have two lives. `sysctl -w` and `modprobe` change the running kernel and are gone after a reboot; files
under `/etc/sysctl.d`, `/etc/modules-load.d` and `/etc/modprobe.d` are read at every boot. You will write the persistent
side in a scratch root and name the runtime commands.

## Starting state

`setup` creates `root/etc/sysctl.d`, `root/etc/modules-load.d`, `root/etc/modprobe.d` (all empty) and `answers.txt`.

## Your task

1. `root/etc/sysctl.d/99-lab.conf`: `net.ipv4.ip_forward = 1`, `vm.swappiness = 10`, `kernel.dmesg_restrict = 1`.
   Each name must be a real parameter of the running kernel (`sysctl -N name` tells you).
2. `root/etc/modules-load.d/lab.conf`: load `br_netfilter` at boot.
3. `root/etc/modprobe.d/lab.conf`: blacklist `floppy`; make `usb-storage` unloadable with an `install` line that runs
   `/bin/false`; set the options `mode=802.3ad miimon=100` for the `bonding` module.
4. Fill in `answers.txt`: the runtime-only sysctl command, the directory for your own persistent sysctl files, the
   command that lists loaded modules and the command that prints a module's details.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-102/kernel-tuning/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-102/kernel-tuning/check
```

In CI the harness runs `setup`, proves `check` fails, runs `solution/apply`, and proves `check` passes. Afterwards, on a
disposable machine, apply a file with `sysctl --system`, change a value with `sysctl -w`, reboot, and compare.

## Notes

- Files are read in lexical order across `/etc`, `/run` and `/usr/lib`; a later file wins, hence the `99-` prefix.
- Reading material: [the lesson](lesson:LNX-102-T08). Afterwards, try [the quiz](quiz:LNX-102-T08).
