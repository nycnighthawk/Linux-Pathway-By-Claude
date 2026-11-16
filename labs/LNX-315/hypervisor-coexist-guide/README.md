# Lab (guide): diagnose a hypervisor conflict and plan coexistence

No special hardware needed: `setup` writes `host-state.txt`, a captured session from a workstation where VirtualBox and KVM clash, and `goals.txt`.

## Your task

1. Read the captured commands and errors. Fill `report.txt`: which component already holds VMX operation, what the log says about Secure Boot, which kernel module option lets both stacks be installed together, its value, whether it permits guests of both at once, which approach gives simultaneous guests, whether one disk image may be opened in both stacks, and how you would check the plan before production.
2. Write `kvm-lazy.conf`, the modprobe.d file that applies the fix.

## Success criteria

The check reads your report and the one-line conf file. Facts about the KVM backend are recent; say in `verify_before_production` how you would confirm them.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/hypervisor-coexist-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/hypervisor-coexist-guide/check
```

Reading: [the lesson](lesson:LNX-315-T07); then [the quiz](quiz:LNX-315-T07).
