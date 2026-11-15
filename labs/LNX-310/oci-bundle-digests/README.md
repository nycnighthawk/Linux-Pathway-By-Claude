# Lab: repair an OCI runtime bundle and an image layout

An OCI runtime bundle (`rootfs/` plus `config.json`) and an OCI image layout (`layout/`) are given with deliberate mistakes. Nothing here needs a container runtime: the grader reads the files and recomputes the digests, like `runc spec` plus `skopeo copy oci:` would let you do by hand.

## Starting state

`setup` writes `bundle/rootfs/`, `bundle/config.json`, `layout/` (`oci-layout`, `index.json`, `blobs/sha256/*`) and `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. Edit `bundle/config.json` so that the container: runs `/bin/app --serve` as UID and GID 10001; sets `noNewPrivileges`; has a read-only root filesystem; keeps only `CAP_NET_BIND_SERVICE` in the bounding, permitted and effective sets; has a memory limit of 256 MiB and a PIDs limit of 100; lists the namespaces `pid`, `mount`, `network`, `ipc`, `uts`, `cgroup` and `user`; masks `/proc/kcore`; and has a seccomp default action that returns an error.
2. In `layout/`, `index.json` points to the manifest with a wrong digest and size. Correct it (the manifest blob is in `blobs/sha256/`; its name is its digest). Do not modify blobs.
3. Fill in `answers.txt`: `layer_digest` (digest of the layer blob as stored, `sha256:...`), `diff_id` (digest of the uncompressed layer tar) and `layer_media_type`.

Hints: `sha256sum`, `gunzip -c blob | sha256sum`, `wc -c`, `jq`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/oci-bundle-digests/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/oci-bundle-digests/check
```

## Notes

- Reading: [the lesson](lesson:LNX-310-T02). Afterwards try [the quiz](quiz:LNX-310-T02).
