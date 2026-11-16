# Lab (guide): read NUMA and cache measurements and choose a placement

This is a guide for hardware you have. `setup` writes sample measurements from a two-socket server so the analysis can be graded anywhere. It never runs a benchmark.

## Part 1: analyse the sample data

`setup` writes:

- `chase.csv`: pointer-chase latency in ns for working sets from 8 KiB to 131072 KiB (128 MiB), measured on a pinned thread.
- `numa.txt`: latency and bandwidth for local and remote memory, from `numactl --cpunodebind=0 --membind=0|1`.
- `counters.csv`: ns per update for two threads updating adjacent counters, and for padded counters.
- `context.txt`: the application's wish (a latency-sensitive service whose NIC is attached to node 1).

Fill `report.txt` (key=value):

1. `l1_kib`, `l2_kib`, `l3_mib`: the largest working set in each plateau before the next jump (from the curve).
2. `remote_latency_ratio`: remote latency divided by local latency, one decimal.
3. `remote_bandwidth_loss_percent`: how much bandwidth is lost remotely, whole percent.
4. `false_sharing_slowdown`: slowdown factor from sharing a line, whole number.
5. `cause`: one phrase for why the adjacent counters are slow.
6. `command`: one command line that starts `./service` on the right node with local memory only.

## Part 2: do it on your machine (not graded)

Compile a pointer-chase and a padded-counter test, pin with `taskset`, and compare your results with `lscpu`. Report the topology next to every number. Reading the data: [the lesson](lesson:LNX-320-T13); then [the quiz](quiz:LNX-320-T13).

## Success criteria

The check reads `report.txt` and compares it with the data: cache sizes at the jumps, the ratio and loss from `numa.txt`, the false sharing factor, the cause and a command that binds both CPUs and memory to node 1.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-320/numa-cache-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-320/numa-cache-guide/check
```
