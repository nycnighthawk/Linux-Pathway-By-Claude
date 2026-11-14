# Guide lab: a throughput report between two hosts

A real link, two real hosts and a quiet network cannot be provided by a shared runner, so this is a guided exercise with success criteria. Use two machines (or two virtual machines on a host-only network if that is all you have; say so in your notes). The grader only checks that your report is complete, well formed and internally consistent; the evidence is in your measurements.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with seven question marks.

## Your task

| Key | How to find it |
|---|---|
| `nic_speed_mbps` | `ethtool IFACE | grep Speed` on both ends, in Mb/s (the lower one) |
| `mtu` | `ip link show IFACE` on both ends (they must match) |
| `single_stream_mbps` | `iperf3 -c SERVER -t 30`, the sender's summary in Mb/s |
| `parallel_streams` | the N you used with `iperf3 -P N` (2 or more) |
| `parallel_mbps` | the `[SUM]` line of that run, in Mb/s |
| `retransmissions` | the Retr total of the parallel run |
| `bottleneck` | `link`, `cpu`, `irq`, `buffer`, `path`, `mtu` or `none`, from watching `mpstat -P ALL 1`, `ethtool -S` and `ip -s link` during the test |

## Success criteria

- You ran each test for at least 30 seconds and repeated the single-stream test three times, noticing the spread.
- You recorded NIC model, driver, kernel version, MTU and offload settings in your own notes.
- You watched CPU per core on both ends during a test and can say whether one core was saturated.
- You can compute the packet rate for the line rate at 64-byte and 1518-byte frames.
- You changed exactly one thing (stream count, MTU, ring size or buffer) and measured again.

## Grade it

`bin/lpc course lab LNX-202 throughput-report` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment S: shared test hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-202-T10). Afterwards, try [the quiz](quiz:LNX-202-T10).
