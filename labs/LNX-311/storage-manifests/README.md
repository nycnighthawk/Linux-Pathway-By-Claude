# Lab: storage manifests for a database

`storage.yaml` in your working directory (`$LAB_DIR`) holds a StorageClass, a StatefulSet and a VolumeSnapshotClass, all with unsafe settings. Make them production-sensible.

## Starting state

`setup` writes `storage.yaml` with `reclaimPolicy: Delete`, `volumeBindingMode: Immediate`, no expansion and a StatefulSet without claim templates.

## Your task

1. StorageClass `db-fast` (provisioner `csi.example.com`): `reclaimPolicy: Retain`, `volumeBindingMode: WaitForFirstConsumer`, `allowVolumeExpansion: true`.
2. StatefulSet `db`: three replicas, `volumeClaimTemplates` with one claim `data`, `ReadWriteOnce`, `20Gi`, class `db-fast`, mounted at `/var/lib/db`.
3. VolumeSnapshotClass `db-snap` for the same driver with `deletionPolicy: Retain`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/storage-manifests/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/storage-manifests/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T06); then [the quiz](quiz:LNX-311-T06).
