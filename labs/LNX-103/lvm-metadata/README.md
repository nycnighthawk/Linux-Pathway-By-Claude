# Lab: a volume group from loop devices, and a thin-pool policy

You will build the PV and VG layer of LVM on three **loop devices** backed by files, using a private LVM configuration so
the host's own volume groups are never touched. (Creating logical volumes needs the kernel's device-mapper, which
shared runners do not always have, so this lab covers the metadata layers and the policy files.)

## Starting state

`setup` creates three 200 MiB image files, attaches them to loop devices (listed in `loops.txt`, one per line), and
writes a private `lvm/lvm.conf` that only accepts those loop devices. Run every LVM command with
`export LVM_SYSTEM_DIR="$LAB_DIR/lvm"`.

## Your task

1. Make the three loop devices physical volumes (`pvcreate`).
2. Create a volume group `labvg` with extent size 8 MiB from the first two devices (`vgcreate -s 8M`), then add the third
   device with `vgextend`.
3. Save the volume group metadata as text: `vgcfgbackup -f labvg.cfg labvg`.
4. Write `thin.conf`, an LVM configuration fragment with an `activation` section that grows a thin pool by 20% when it
   is 80% full (`thin_pool_autoextend_threshold` and `thin_pool_autoextend_percent`). Check it with `lvmconfig`.
5. Fill in `answers.txt`: the `lvextend` option that also resizes the file system, whether a thin snapshot request may
   carry a size option (`yes` or `no`), and the `lvs` column name that shows how full a thin pool's data is
   (`data_percent`-style name).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/lvm-metadata/setup
export LVM_SYSTEM_DIR=$PWD/lvm
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/lvm-metadata/check
```

## Notes

- Run as root. `setup` detaches loop devices that an earlier run left behind. Detach yours afterwards with
  `losetup -d` on each line of `loops.txt`.
- The lab needs the package `lvm2`.
- Reading material: [the lesson](lesson:LNX-103-T03). Afterwards, try [the quiz](quiz:LNX-103-T03).
