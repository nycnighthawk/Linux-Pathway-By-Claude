# Lab: answer questions from a packet capture with tshark

A capture file holds three TCP conversations and one DNS exchange between a client (10.0.0.5), a web server (10.0.0.10) and a resolver (10.0.0.53). Use `tshark` to turn it into numbers.

## Starting state

`setup` writes `capture.pcap` (generated deterministically, no privileges needed) and an `answers.txt` with six question marks in your working directory (`$LAB_DIR`).

## Your task

Fill in `answers.txt`:

| Key | Question |
|---|---|
| `tcp_streams` | how many TCP conversations are in the capture |
| `http_requests` | how many HTTP requests were sent |
| `retransmissions` | how many packets tshark marks as TCP retransmissions |
| `refused_port` | the server port that answered with a reset |
| `dns_name` | the name asked about in the DNS response |
| `dns_rcode` | the numeric response code of the DNS answer |

## Grade it

`bin/lpc course lab LNX-202 tshark-analysis` runs the whole cycle. To grade your answers run `check` with `LAB_DIR` set to the directory that holds them. The grader recounts each value from the capture with its own tshark commands.

## Notes

- `tshark -r capture.pcap` prints a summary line per packet; add `-Y FILTER` to select packets and `-T fields -e FIELD` to print chosen fields.
- `tshark -r capture.pcap -q -z conv,tcp` prints the conversation table.
- The expert fields `tcp.analysis.retransmission` and the flags `tcp.flags.reset` answer two of the questions directly.
- Display filters are applied after decoding; they are not the same language as the capture filters of tcpdump.
- The lab needs the packages `tshark` and `python3`.
- Reading material: [the lesson](lesson:LNX-202-T08). Afterwards, try [the quiz](quiz:LNX-202-T08).
