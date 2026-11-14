# Lab: configure FRR for OSPF and an eBGP peer

Write the configuration of router `r1`. It has `eth1` on 10.0.12.0/24 towards router `r2` (OSPF) and reaches an external BGP peer at 192.0.2.2.

## Starting state

`setup` writes `frr.conf` in your working directory (`$LAB_DIR`) with the hostname and three TODO comments.

## Your task

1. OSPF: `router ospf` with router-id 10.255.0.1, `passive-interface default` with `no passive-interface eth1`, and a `network 10.0.12.0/24 area 0` statement.
2. Under `interface eth1`: `ip ospf network point-to-point`, hello interval 2 and dead interval 8.
3. BGP: `router bgp 65001` with router-id 10.255.0.1, the neighbour 192.0.2.2 in AS 65002, activated inside `address-family ipv4 unicast`, which also advertises 198.51.100.0/24 with a `network` statement.
4. Make the eBGP session usable: either `no bgp ebgp-requires-policy` or an inbound and outbound route map on the neighbour.

## Grade it

`bin/lpc course lab LNX-202 frr-config` runs the whole cycle. To grade your file run `check` with `LAB_DIR` set to the directory that holds `frr.conf`. The grader asks `vtysh -C -f frr.conf` to parse the file without any daemon running, then checks each rule above.

## Notes

- A real router would also need the daemons enabled in `/etc/frr/daemons`, forwarding on, and the firewall open for OSPF (protocol 89) and TCP 179.
- `vtysh -C -f FILE` is the offline syntax check; on a live router use `show running-config` and `write memory`.
- The lab needs the package `frr`.
- Reading material: [the lesson](lesson:LNX-202-T09). Afterwards, try [the quiz](quiz:LNX-202-T09).
