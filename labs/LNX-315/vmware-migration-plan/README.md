# Lab: plan a VMware migration wave and convert a disk

A real migration needs vCenter and a converter host. This lab trains the two parts you can check anywhere: classifying an inventory into actions, and the disk-format step with `qemu-img` (what `virt-v2v` does for the disk, before it also fixes drivers and boot configuration).

## Your task

1. `setup` writes `inventory.csv`, `requirements.txt` and a small `guest.vmdk`. Apply the rules in `requirements.txt` to every machine in `report.txt`.
2. List the machines whose snapshots must be collapsed first and the machine that needs a BitLocker recovery key.
3. Write `convert.sh` that converts `guest.vmdk` to `guest.qcow2`.

## Success criteria

The check recomputes the expected action for each machine, runs your script and compares the two images with `qemu-img compare`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vmware-migration-plan/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vmware-migration-plan/check
```

Needs `qemu-img` (package `qemu-utils`) and `python3`. Reading: [the lesson](lesson:LNX-315-T10); then [the quiz](quiz:LNX-315-T10).
