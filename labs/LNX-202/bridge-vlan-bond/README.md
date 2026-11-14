# Lab: split a bridge into VLANs, and describe an LACP bond

Part 1 is live: three namespaces hang on one flat bridge and you isolate them with VLAN filtering. Part 2 is a pair of systemd-networkd files for an 802.3ad bond (nothing is applied, so no bonding module is needed).

## Starting state

`setup` creates the bridge `lab-br0` with the ports `lab-pa`, `lab-pb` and `lab-pc`, and namespaces `lab-a`, `lab-b` and `lab-c` (addresses 10.20.10.1, .2 and .3 on one subnet). Everything can reach everything. It needs root or sudo.

## Your task

1. Turn on VLAN filtering on `lab-br0`.
2. Make `lab-pa` and `lab-pb` access ports in VLAN 10 (`bridge vlan add dev PORT vid 10 pvid untagged`) and `lab-pc` an access port in VLAN 20. Remove the default VLAN 1 from the ports.
3. Check: `a` and `b` can ping each other; `a` and `c` cannot.
4. Write `bond0.netdev`: a bond named `bond0` in mode `802.3ad` with `TransmitHashPolicy=layer3+4`, `LACPTransmitRate=fast` and `MIIMonitorSec=100ms`.
5. Write `ports.network`: it matches the links `enp7s0` and `enp8s0` and enslaves them with `Bond=bond0`.

## Grade it

`bin/lpc course lab LNX-202 bridge-vlan-bond` runs the whole cycle. To grade your work run `check` with `LAB_DIR` set to the directory that holds your files. The grader reads the bridge state, pings between the namespaces and parses the two files.

## Notes

- `bridge vlan show` lists VLANs per port; `bridge -c vlan show dev PORT` gives one port in a compact form.
- `ip netns exec lab-a ping -c1 10.20.10.2` runs a command inside a namespace.
- Tear down with `ip link del lab-br0` and `ip netns del lab-a` (and b, c).
- The lab runs on the V environment (needs root, network namespaces and bridge support) and needs the package `iproute2`.
- Reading material: [the lesson](lesson:LNX-202-T01). Afterwards, try [the quiz](quiz:LNX-202-T01).
