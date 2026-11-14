# Guide lab: survey your storage hardware and write a multipath configuration

Hardware RAID controllers, Fibre Channel adapters and multipath arrays cannot be simulated on a shared runner, so this is
a guided exercise with success criteria. Do it on any Linux machine: a laptop or virtual machine will show you the
empty case (no FC adapters, one path per disk), which is still a valid answer. The grader only checks that your report
and configuration are complete and well formed; the evidence is on the machine.

## Starting state

`setup` writes `report.txt` (six question marks) in your working directory (`$LAB_DIR`).

## Your task

Part 1: find each value on the machine and write it in `report.txt`.

| Key | How to find it |
|---|---|
| `multipath_tools_installed` | `yes` if `command -v multipath` finds the tool, otherwise `no` |
| `fc_hosts` | number of entries in `/sys/class/fc_host/` (0 when there is no Fibre Channel adapter) |
| `scsi_hosts` | number of entries in `/sys/class/scsi_host/` |
| `block_devices` | number of whole disks in `lsblk -d -n` |
| `storage_driver` | the kernel module that drives your main disk (`lsblk -o NAME,TRAN`, `lsmod`): for example `virtio_scsi`, `nvme`, `ahci`, `megaraid_sas`; write `none` if you cannot tell |
| `paths_per_lun` | how many `sdX` devices lead to your main disk: `1` unless `multipath -ll` shows more |

Part 2: write `multipath.conf` for an imaginary server. It needs a `defaults` section with
`user_friendly_names yes` and `find_multipaths yes`, a `blacklist` section with a `wwid` line for the local boot disk
(any quoted value), and a `multipaths` section with one `multipath` block that gives the WWID
`360000000000000000e00000000010001` the alias `oradata`.

## Success criteria

- Every key in `report.txt` holds a value you read from the machine.
- `multipath.conf` has the sections above, with balanced braces.
- You can explain, in one sentence, why you must use `/dev/mapper/oradata` and not the underlying `sdX` devices.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/multipath-report/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/multipath-report/check
```

## Notes

- Reading material: [the lesson](lesson:LNX-103-T11). Afterwards, try [the quiz](quiz:LNX-103-T11).
