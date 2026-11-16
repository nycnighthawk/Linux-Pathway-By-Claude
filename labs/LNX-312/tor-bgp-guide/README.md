# Guide: bring up a BGP session to a top-of-rack switch

Environment H (hardware): you need a switch that speaks BGP, or a second Linux machine running FRR that plays the switch. The check validates the shape
of your report, not the truth of the values.

## Starting state

`setup` writes `report.txt` with empty fields.

## Your task

1. Configure the node side (FRR or the Cilium BGP resources) to announce the node's Pod CIDR, with graceful restart and BFD.
2. Configure the switch side with an inbound prefix list and a maximum-prefix limit.
3. Read the neighbour summary on both ends and fill `report.txt`:
   - `switch_os`: frr, sonic, eos, cumulus, nxos, junos or other
   - `local_as`, `peer_as`: AS numbers (integers)
   - `session_state`: established, active, idle or connect
   - `prefixes_received`: integer, the routes the switch has from the node
   - `bfd`: up, down or none
   - `graceful_restart`: yes or no
   - `ecmp_paths`: integer, next hops the switch holds for a service address
   - `prefix_filter`: yes or no (does the switch reject a prefix the node must not announce? prove it by announcing one)
4. In `notes.txt`, write at least three lines: the command you used for each reading and what the output showed.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/tor-bgp-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/tor-bgp-guide/check
```

Reading: [the lesson](lesson:LNX-312-T13), then [the quiz](quiz:LNX-312-T13).
