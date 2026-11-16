# Lab: MetalLB resources and the FRR router side

Write two files in `$LAB_DIR`.

1. `metallb.yaml` (multi-document), namespace `metallb-system`, API group `metallb.io`:
   - `IPAddressPool` `lab-pool`, address range `192.0.2.240-192.0.2.250` (auto-assign on).
   - `BGPPeer` `tor-a` (`v1beta2`): `myASN` 65010, `peerASN` 65000, `peerAddress` 10.0.0.1, `bfdProfile` `fast`.
   - `BFDProfile` `fast` with `receiveInterval` 300 and `transmitInterval` 300.
   - `BGPAdvertisement` `lab-adv`: `ipAddressPools: [lab-pool]`, `aggregationLength` 32.
2. `frr.conf` for the switch: `router bgp 65000`, a peer group `NODES` with `remote-as 65010`, `bgp listen range 10.0.0.0/24 peer-group NODES`,
   BFD on the peer group, in `address-family ipv4 unicast` activate `NODES`, `maximum-paths 8`, and an inbound `prefix-list METALLB`
   permitting `192.0.2.240/28 le 32` applied to the group.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/metallb-frr/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/metallb-frr/check
```

Needs `python3` and `PyYAML`. Reading: [the lesson](lesson:LNX-312-T10), then [the quiz](quiz:LNX-312-T10).
