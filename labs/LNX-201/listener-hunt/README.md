# Lab: find the mystery listener with ss and ip

A process is listening on a TCP port on the loopback address and nobody wrote down which one. Find it with `ss`.

## Starting state

`setup` starts a small background program listening on `127.0.0.1` at a random port, records its process id in
`.listener.pid` (a hidden file; do not read it for the answer), and writes `answers.txt` with a `?` for each value.

## Your task

Fill in `answers.txt`:

| Key | How to find it |
|---|---|
| `port` | `ss -ltnp` (TCP, listening, numeric, with processes) |
| `pid` | the `pid=` field in the same line |
| `command` | the quoted program name in that line (for example `python3`) |
| `bind_address` | the local address part of the socket (the part before the port) |
| `lo_mtu` | `ip link show lo` |
| `lo_state` | `ip -br link show lo` (the state column, for example `UNKNOWN` or `UP`) |

## Grade it

`bin/lpc course lab LNX-201 listener-hunt` runs the whole cycle. To grade your own file run `check` with `LAB_DIR`
set to the directory that holds `answers.txt`. Stop the listener afterwards with `kill $(cat .listener.pid)`.

## Notes

- `ss -ltnp` needs `-p` and enough privilege to see other users' processes; run it as root if the process column is empty.
- The lab needs the packages `iproute2` and `python3`.
- Reading material: [the lesson](lesson:LNX-201-T02). Afterwards, try [the quiz](quiz:LNX-201-T02).
