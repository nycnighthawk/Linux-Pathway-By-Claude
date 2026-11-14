# Lab: a router advertisement configuration, and the address a host builds from it

Two small jobs: write the `radvd` configuration for a router, then write the calculator that predicts the SLAAC address of a host.

## Starting state

`setup` writes `radvd.conf` (a comment only) and a stub `eui64.sh` in your working directory (`$LAB_DIR`).

## Your task

1. `radvd.conf` for the router interface `eth1`: send advertisements, with the managed (M) flag off and the other-config (O) flag on, and a `MaxRtrAdvInterval` of at most 600 seconds. Advertise the prefix `2001:db8:42:7::/64` with `AdvOnLink on` and `AdvAutonomous on`, and the DNS server `2001:db8:42:7::53` in an `RDNSS` block.
2. `eui64.sh MAC PREFIX`: print the address a host with that MAC builds under the 64-bit prefix (given as its first four groups, for example `2001:db8:42:7`). The rule: split the MAC into halves, insert `ff:fe` in the middle and flip the second-lowest bit of the first byte (the universal/local bit). For `52:54:00:12:34:56` the result is `2001:db8:42:7:5054:ff:fe12:3456`. The output may be written in compressed or uncompressed form.

## Grade it

`bin/lpc course lab LNX-202 slaac-radvd` runs the whole cycle. To grade your files run `check` with `LAB_DIR` set to the directory that holds them. The grader runs `radvd -c` (a syntax check, no router needed), checks the settings and runs your script on four MAC addresses.

## Notes

- `radvd -c -C radvd.conf` checks the file; on a real router radvd also needs `net.ipv6.conf.all.forwarding=1`.
- Modern hosts often use stable-privacy or temporary addresses instead of the EUI-64 form; the calculator shows the original method.
- Bash can do the arithmetic with `$(( 0x52 ^ 0x02 ))`, and `printf '%x'` prints hex without leading zeros.
- The lab needs the packages `radvd` and `python3`.
- Reading material: [the lesson](lesson:LNX-202-T03). Afterwards, try [the quiz](quiz:LNX-202-T03).
