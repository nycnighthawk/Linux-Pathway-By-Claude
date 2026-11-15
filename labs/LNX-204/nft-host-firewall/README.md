# Lab: a default-drop host firewall

Turn an IPv4-only, accept-everything ruleset into a dual-stack default-drop policy that exposes SSH to one management
network and the web ports to everyone, rate-limits what it should and logs what it drops. The file is validated with
`nft -c` (check only), so nothing is applied to the machine running the lab.

## Starting state

`setup` writes `host.nft` (table `ip filter`, `policy accept`) and a blank `answers.txt`.

## Your task

Write `host.nft` with a single `inet` table containing: a set `mgmt4` (type `ipv4_addr`, flags `interval`) holding
`10.20.0.0/24`; an input chain with `policy drop`; rules, in order, for loopback, `ct state invalid drop`, established
and related, rate-limited ICMP echo, ICMPv6 including neighbour discovery and packet-too-big, SSH from `@mgmt4` only,
`tcp dport { 80, 443 }`, and a rate-limited `log` at the end. Validate with `nft -c -f host.nft` and fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-204/nft-host-firewall/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-204/nft-host-firewall/check
```

## Notes

- Needs the `nftables` package and a kernel with nf_tables; `nft -c` talks to the kernel parser, so it needs root.
- Never apply a new ruleset remotely without a revert timer. See [the lesson](lesson:LNX-204-T06) and [the quiz](quiz:LNX-204-T06).
