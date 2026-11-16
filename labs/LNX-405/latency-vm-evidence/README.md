# Guide lab: A pinned, hugepage-backed VM that meets a latency target

Tune a virtual machine and its host for low and steady latency, measure the worst case over a long run with load, and compare with a target you set before you started. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `host_cpu_model` | `lscpu`, model name |
| `numa_nodes` | `lscpu`, NUMA node count |
| `isolated_cores` | number of host cores isolated with isolcpus or cpusets |
| `vcpus` | virtual CPUs of the VM |
| `vcpus_pinned` | yes if each vCPU is pinned to its own host core |
| `same_numa_node` | yes if vCPUs, memory and the device threads are on one NUMA node |
| `hugepage_size_kib` | size of the pages backing guest memory |
| `target_max_us` | the worst-case latency target you wrote down first, in microseconds |
| `baseline_max_us` | worst case with default settings |
| `tuned_max_us` | worst case after tuning (cyclictest or similar) |
| `test_minutes` | length of each measurement under load |
| `load_running` | yes if a CPU and I/O load ran in the host during the test |
| `smi_checked` | yes if you checked for firmware interrupts that steal time |

## Success criteria

- The target was written before the first measurement.
- You changed one setting at a time and kept a table of results.
- You ran the tuned test with load, not on an idle host.
- You say plainly whether the target was met and what limited it.

## Grade it

`bin/lpc course lab LNX-405 latency-vm-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-405-T03).
