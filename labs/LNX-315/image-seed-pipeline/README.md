# Lab: a small image pipeline with a cloud-init seed

You build the three pieces of a first-boot pipeline: a validated cloud-init seed, a pinned base image and a cheap copy-on-write test disk. No VM is booted; `qemu-img` stands in for the hypervisor tools.

## Your task

`setup` creates `base.qcow2` (a small stand-in image) and writes `requirements.txt`. Create `user-data`, `meta-data` and `build.sh` that follow it: a key-only `ops` user, no passwords, the guest agent, a recorded sha256 of the base, a qcow2 overlay `test1.qcow2` that uses `base.qcow2` as backing file, and a `seed/` directory with the seed files.

## Success criteria

The check parses the YAML, runs `build.sh` in your lab directory and inspects the overlay with `qemu-img info`. It also confirms the base was not modified.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/image-seed-pipeline/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/image-seed-pipeline/check
```

Needs `qemu-img` (package `qemu-utils`), `python3` and PyYAML. Reading: [the lesson](lesson:LNX-315-T08); then [the quiz](quiz:LNX-315-T08).
