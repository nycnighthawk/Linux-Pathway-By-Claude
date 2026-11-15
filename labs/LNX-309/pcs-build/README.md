# Lab: script a two-node Pacemaker cluster with fencing

You will write the `pcs` commands that build a safe two-node web cluster. The grader reads your script and checks it statically; it does not run it, so you do not need a cluster. If you have two virtual machines you can run the script for real and compare.

## Environment

Nodes `node1` and `node2` (libvirt domains `vm-node1` and `vm-node2`) on a hypervisor at `192.168.122.1`. `setup` creates `build-cluster.sh` with TODO comments.

## Your task

Edit `build-cluster.sh`, one `pcs` command per line (a trailing `\` continues a line):

1. Authenticate both nodes (`pcs host auth`), create a cluster from `node1` and `node2` with `pcs cluster setup <name> ...`, start it and enable it at boot (`--all`).
2. Create a `fence_virsh` stonith device pointing at the hypervisor with `pcmk_host_map="node1:vm-node1;node2:vm-node2"`. Fencing stays enabled; do not use `--force`.
3. Create the address `ocf:heartbeat:IPaddr2` with `ip=192.168.122.50` and `cidr_netmask=24`, and the web server `ocf:heartbeat:apache` with an `op monitor interval=...`.
4. Colocate the web server with the address (`INFINITY`), start the address first, and prefer `node2` with a finite score below INFINITY.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-309/pcs-build/setup
# ...edit build-cluster.sh...
LAB_DIR=$PWD /path/to/repo/labs/LNX-309/pcs-build/check
```

## Notes

- Option names of `fence_virsh` vary by release: check `pcs stonith describe fence_virsh` (to verify).
- Reading material: [the lesson](lesson:LNX-309-T01). Afterwards, try [the quiz](quiz:LNX-309-T01).
