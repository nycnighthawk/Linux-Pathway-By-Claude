# Lab: configure DRBD and its Pacemaker resources (active/passive)

Write the DRBD resource file and the `pcs` script for a two-node pair that replicates `/dev/vg0/data` and mounts an xfs file system from `/dev/drbd1` at `/srv/www` on whichever node is primary. The grader checks both files statically (and runs `drbdadm dump` if `drbdadm` happens to be installed); no cluster is needed.

## Environment

Nodes `node1` (`192.168.122.11`) and `node2` (`192.168.122.12`). `setup` writes a near-empty `wwwdata.res` and `drbd-pcs.sh`.

## Your task

1. `wwwdata.res`: resource `wwwdata`, `device minor 1`, internal metadata; `net` with `protocol C`, `fencing resource-and-stonith` and `verify-alg`; `handlers` with the `crm-fence-peer` and `crm-unfence-peer` scripts; an `on` section per node (`disk "/dev/vg0/data"`, `node-id` 0 and 1); a `connection` with each host's address and port 7789. This pair is active/passive, so do **not** allow two primaries.
2. `drbd-pcs.sh`: queue the changes in a file (`pcs cluster cib <file>`, `pcs -f <file> ...`): an `ocf:linbit:drbd` resource with separate monitors for `role=Promoted` and `role=Unpromoted`, made promotable with `promoted-max=1` and `clone-max=2`; a `Filesystem` resource (xfs); colocate the file system with the promoted role and start it only after promotion; push the file with `pcs cluster cib-push` at the end.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-309/drbd-config/setup
# ...edit wwwdata.res and drbd-pcs.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-309/drbd-config/check
```

## Notes

- DRBD 9 syntax is used; DRBD 8 differs (to verify). Never use `allow-two-primaries` without a cluster file system and working fencing.
- Reading material: [the lesson](lesson:LNX-309-T02). Afterwards, try [the quiz](quiz:LNX-309-T02).
