# Lab: write a safe etcd backup script

Write `etcd-backup.sh` in your working directory (`$LAB_DIR`). The check runs your script against fake `etcdctl` and `etcdutl` programs, so no cluster is needed.

## Starting state

`setup` creates `fakebin/etcdctl` and `fakebin/etcdutl` (they log their arguments), `backups/` with an old backup file (10 days old) and a recent one, and a stub `etcd-backup.sh`.

## Your task

The script must, using the `BACKUP_DIR` environment variable (default `./backups`):

1. Run `etcdctl snapshot save` to `BACKUP_DIR/etcd-YYYY-MM-DD.db` with `--endpoints=https://127.0.0.1:2379` and `--cacert`, `--cert`, `--key` pointing into `/etc/kubernetes/pki/etcd/`.
2. Verify the file with `etcdutl snapshot status`.
3. Leave the file readable only by its owner (mode 600).
4. Delete backups in `BACKUP_DIR` older than 7 days and keep newer ones.
5. Exit non-zero, and not delete anything, when the snapshot command fails.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/etcd-backup-script/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/etcd-backup-script/check
```

Reading: [the lesson](lesson:LNX-311-T04); then [the quiz](quiz:LNX-311-T04).
