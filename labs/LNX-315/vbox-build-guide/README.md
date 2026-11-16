# Lab (guide): build a headless VirtualBox machine with VBoxManage only

This is a manual guide with a shape check, so it works without VirtualBox installed. If you have VirtualBox, run your script for real and compare the result with `VBoxManage showvminfo node1 --machinereadable`.

## Your task

1. Read `requirements.txt` (written by `setup`).
2. Write `build.sh`: one `VBoxManage` command per line that creates and registers the machine, sets CPU, memory, firmware and network adapters, creates the disk, attaches the disk and ISO, adds the port forward, takes the `base` snapshot and starts the machine headless.
3. Fill `report.txt`, including how the host finds the guest's address and how you would see early boot with no window and no Extension Pack.

## Success criteria

The check reads your script and report for the required options. It never runs VirtualBox.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vbox-build-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vbox-build-guide/check
```

Reading: [the lesson](lesson:LNX-315-T06); then [the quiz](quiz:LNX-315-T06).
