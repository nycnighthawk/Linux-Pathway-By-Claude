# Lab: a container by hand, from recorded kernel state

You cannot rely on privileges in a grading sandbox, so this lab works on a fake cgroup v2 tree (plain files) and on recorded `/proc` output. The shell logic you write is the same you would run against `/sys/fs/cgroup`.

## Starting state

`setup` creates in `$LAB_DIR`: `cgroot/` (an empty stand-in for `/sys/fs/cgroup`), `ns_host.txt` and `ns_container.txt` (the output of `readlink /proc/<pid>/ns/*` for a host shell and a container process), `status.txt` (the capability and mapping lines of a container process), `limits.sh` (a stub) and `answers.txt`.

## Your task

1. Write `limits.sh`. It must use `$CGROOT` as the cgroup mount, enable the `memory`, `pids` and `cpu` controllers for children (`cgroup.subtree_control`), create the group `demo`, set `memory.max` to 100 MiB, `pids.max` to 64 and `cpu.max` to one fifth of a core with a 100 ms period, and write a process ID into `demo/cgroup.procs`. It must be safe to run twice.
2. Fill in `answers.txt` from the recorded files: `shared_namespaces` (comma separated, alphabetical, the namespace types whose inode is identical for host and container), `has_sys_admin` and `has_net_bind_service` (`yes` or `no`, decoded from `CapEff`), and `host_uid_of_container_root` (from the `uid_map` line).

Hints: `capsh --decode=<hex>` decodes masks (capability numbers: `CAP_NET_BIND_SERVICE` is 10, `CAP_SYS_ADMIN` is 21); a bit is set when `(mask >> n) & 1`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/ns-cgroup-by-hand/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/ns-cgroup-by-hand/check
```

## Notes

- No extra packages are needed. Reading: [the lesson](lesson:LNX-310-T01). Afterwards try [the quiz](quiz:LNX-310-T01).
- Real run: replace `CGROOT` with `/sys/fs/cgroup` as root and read `memory.events` after allocating more than the limit.
