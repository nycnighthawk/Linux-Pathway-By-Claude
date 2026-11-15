# Lab: build a container network by hand

Write `build-net.sh` in your working directory (`$LAB_DIR`) that builds the network from the lesson. The check runs it as root (with `sudo` if needed), probes the result and tears everything down.

## Starting state

`setup` removes leftovers from earlier runs and writes a stub `build-net.sh`. It needs `iproute2` and `nftables`, root rights and network namespace support.

## Your task

The script must (and must be safe to run twice):

1. Create bridge `lab0` with the address `10.10.0.1/24`, up.
2. Create namespaces `c1` and `c2`, each joined by a veth pair to `lab0`, with the namespace end named `eth0` and the addresses `10.10.0.2/24` and `10.10.0.3/24`, loopback up, default route via `10.10.0.1`.
3. Enable IPv4 forwarding.
4. In an nftables table `ip lab`: a postrouting masquerade rule for `10.10.0.0/24` leaving through anything but `lab0`, and a prerouting DNAT rule sending TCP port 8080 to `10.10.0.2:80`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/netns-bridge-nat/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/netns-bridge-nat/check
```

Reading: [the lesson](lesson:LNX-312-T01); then [the quiz](quiz:LNX-312-T01).
