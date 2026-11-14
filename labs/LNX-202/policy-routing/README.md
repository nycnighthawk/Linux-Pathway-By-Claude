# Lab: source-based routing on a dual-homed host

A host has two uplinks. Its default route points to ISP 1, so traffic that uses the address given by ISP 2 leaves through the wrong provider and its replies never return. Fix it with a second routing table and rules.

## Starting state

`setup` creates three namespaces: `lab-host` (eth1 = 192.0.2.7/24 towards ISP 1 at 192.0.2.1, eth2 = 198.51.100.7/24 towards ISP 2 at 198.51.100.1), `lab-isp1` and `lab-isp2`. Both providers answer for the test address `203.0.113.9`, but each knows only its own subnet. The host's main table has one default route via 192.0.2.1. Setup needs root or sudo.

## Your task

Work inside the host (`ip -n lab-host ...`):

1. Create routing table **100** with a default route via 198.51.100.1 on eth2 and the connected route for 198.51.100.0/24 (source 198.51.100.7).
2. Add the rule `from 198.51.100.7 lookup 100`.
3. Add a second rule so that packets with firewall mark 2 also use table 100.
4. Leave the main table alone.

## Grade it

`bin/lpc course lab LNX-202 policy-routing` runs the whole cycle. To grade your work run `check` with `LAB_DIR` set to the directory that holds your notes. The grader asks the kernel with `ip route get` (with and without `from` and `mark`) and sends real pings with each source address.

## Notes

- `ip route get 203.0.113.9 from 198.51.100.7` shows which route a packet would use, and is the first debugging tool.
- Numeric tables work without editing `/etc/iproute2/rt_tables`.
- Rules are checked in priority order, lowest number first; the main table sits at 32766.
- Tear down with `ip netns del lab-host` (and lab-isp1, lab-isp2).
- The lab runs on the V environment (root and network namespaces) and needs the package `iproute2` and `iputils-ping`.
- Reading material: [the lesson](lesson:LNX-202-T02). Afterwards, try [the quiz](quiz:LNX-202-T02).
