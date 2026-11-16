# Lab (tuning guide): write the pinning and NUMA XML for a database guest

`setup` writes `host-topology.txt` (a trimmed `lscpu -e` plus notes from `numactl` and sysfs) and `requirements.txt`. On a real host, collect the same facts with `lscpu -e`, `numactl --hardware` and `cat /sys/class/block/*/device/numa_node`, and read the NUMA-node fact about the disk before you choose cores.

## Your task

Write `db01.xml`: a libvirt `<domain>` (or the fragments `vcpu`, `iothreads`, `cputune`, `numatune`, `memoryBacking`, `cpu`, `devices/disk`) that meets `requirements.txt`. Watch two details: SMT siblings are `cpu+16` on this machine (copying pinning from a host with different numbering is the classic mistake), and the guest topology must match the pinning.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/pinning-xml-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/pinning-xml-guide/check
```

Needs `python3`. If you have libvirt, also run `virt-xml-validate db01.xml domain` on your file. Reading: [the lesson](lesson:LNX-315-T03); then [the quiz](quiz:LNX-315-T03).
