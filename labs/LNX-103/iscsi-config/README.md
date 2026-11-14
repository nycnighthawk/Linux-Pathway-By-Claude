# Lab: a targetcli script and an initiator configuration for one LUN

You will write the configuration for a small iSCSI SAN: the commands that publish a logical volume as a LUN on the
target, and the files the initiator needs. Nothing is started; the files are graded as text.

## Starting state

`setup` writes a blank `answers.txt` and removes earlier results under your working directory (`$LAB_DIR`).

## Your task

1. `target.cli`: one `targetcli` command per line, in a valid order, that
   - creates a block backstore `lun1` on `/dev/vg0/lun1`;
   - creates the target `iqn.2025-06.lab.example:san.lun1`;
   - maps the backstore as a LUN of that target's `tpg1`;
   - allows the initiator `iqn.2025-06.lab.example:compute1` (an ACL);
   - adds a portal `192.0.2.10` on port `3260`;
   - ends with `saveconfig`.
   Use the path style of the lesson (`backstores/block create ...`, `iscsi/ create ...`).
2. `initiatorname.iscsi`: one line, `InitiatorName=iqn.2025-06.lab.example:compute1`.
3. `iscsid.conf` (mode `0600`): log in automatically (`node.startup = automatic`), fail over quickly with
   `node.session.timeo.replacement_timeout = 5`, and use CHAP with user `lab` and any non-empty password.
4. `fstab`: one line mounting the file system with UUID `0c1d4a02-5b1e-4a77-9a6d-2f1b3c4d5e6f` at `/srv/san`, type
   `xfs`, options `defaults,_netdev,nofail`, dump 0, pass 0.
5. Fill in `answers.txt`: the TCP port iSCSI uses, the user-space daemon of the Open-iSCSI initiator, and the prefix
   that begins an iSCSI qualified name.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-103/iscsi-config/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-103/iscsi-config/check
```

## Notes

- A LUN cannot be mapped before its backstore and target exist; `saveconfig` writes `/etc/target/saveconfig.json`.
- `_netdev` orders the mount after the network, and `nofail` keeps a missing SAN from blocking the boot.
- Reading material: [the lesson](lesson:LNX-103-T08). Afterwards, try [the quiz](quiz:LNX-103-T08).
