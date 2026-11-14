# Lab: read a packet capture and name the failure

Someone captured a client's traffic for you. Read it with `tcpdump -r` and say what went wrong at each step.

## Starting state

`setup` writes `lab.pcap` (seven packets from client 192.0.2.10) and `answers.txt` with a `?` for each value.
Nothing is captured live and no privileges are needed: the file is read offline.

## Your task

Run `tcpdump -nn -r lab.pcap` (add `-tt` for timestamps, or a filter such as `'tcp[tcpflags] & tcp-rst != 0'`) and fill in:

| Key | Meaning |
|---|---|
| `refused_port` | the destination port whose SYN was answered with a reset (flags `[R.]`) |
| `silent_port` | the destination port whose SYN was never answered |
| `syn_count_silent` | how many SYNs the client sent to that port |
| `dns_server` | the address the client sent its DNS query to |
| `dns_name` | the name that was looked up |
| `dns_status` | the status in the reply (tcpdump prints `NXDomain`; write `NXDOMAIN`) |

## Grade it

`bin/lpc course lab LNX-201 read-the-capture` runs the whole cycle. To grade your own file run `check` with `LAB_DIR`
set to the directory that holds `answers.txt` and `lab.pcap`.

## Notes

- A reset answers a SYN when nothing listens (or a reject rule fires); silence points to a drop rule or a lost path.
- The repeated SYNs with growing gaps are TCP retransmissions.
- The lab needs the packages `tcpdump` and `python3`.
- Reading material: [the lesson](lesson:LNX-201-T08). Afterwards, try [the quiz](quiz:LNX-201-T08).
