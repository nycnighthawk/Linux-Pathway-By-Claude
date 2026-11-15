# Lab: tune a database guest with virtio, huge pages and pinning

You are given an untuned guest definition and a description of the host. Apply the functional tuning steps, in the right places, without breaking the placement rules the host sets.

## Starting state

`setup` writes `db1.xml` (4 vCPUs, 8 GiB, SATA disk, e1000 NIC), `host.txt` and `answers.txt` into your working directory (`$LAB_DIR`).

`host.txt` says: two NUMA nodes, node 0 owns CPUs 0 to 7, CPUs 0-1 are for housekeeping and CPUs 2-7 are isolated for guests, and huge pages are 2 MiB.

## Your task

1. Pin each vCPU to its own single CPU inside the isolated set, and put the emulator thread and the iothread on the housekeeping CPUs.
2. Define one `iothread` and give the disk driver `cache='none' io='native' discard='unmap' iothread='1'`.
3. Back the guest with 2 MiB huge pages from node 0 and bind its memory strictly to node 0.
4. Use `host-passthrough` with a topology of 1 socket, 2 cores, 2 threads.
5. Move the disk to `virtio` as `vda` and the NIC to virtio with `vhost` and 4 queues.
6. Remove the memory balloon (`model='none'`).
7. Record in `answers.txt` how many 2 MiB pages the host must reserve for this guest.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/tuned-domain/setup
# ...edit db1.xml and answers.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/tuned-domain/check
```

## Notes

- On a real host you would reserve the pool with `sysctl vm.nr_hugepages=...`, check `grep Huge /proc/meminfo` and verify pinning with `virsh vcpuinfo db1`.
- Reading material: [the lesson](lesson:LNX-308-T04). Afterwards, try [the quiz](quiz:LNX-308-T04).
