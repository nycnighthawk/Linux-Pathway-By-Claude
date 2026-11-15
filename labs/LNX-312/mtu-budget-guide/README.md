# Guide: build an MTU budget and measure the layers

Environment S: this is a guided exercise with a check that verifies the arithmetic exactly and the shape of your measurements.

## Starting state

`setup` writes `budget.txt` with empty fields.

## Your task

1. Compute the Pod MTU (IPv4 outer headers throughout) for each case and write it in `budget.txt`:
   `ipip_1500`, `vxlan_1500`, `wireguard_1500`, `vxlan_in_wireguard_1500`, `vxlan_9000`.
2. `max_ping_payload_vxlan_1500`: the largest `ping -M do -s` payload that passes on a path with the VXLAN Pod MTU.
3. On a real or virtual pair of nodes, run a throughput tester in four ways (node to node, Pod to Pod same node, Pod to Pod across nodes, Pod to Service)
   and record `gbps_node`, `gbps_pod_same`, `gbps_pod_cross`, `gbps_service` as numbers. If you have no cluster, run the same four shapes with
   network namespaces on one host and say so in `notes.txt`.
4. `bottleneck`: one of `link`, `cpu`, `offload`, `mtu`, with a sentence in `notes.txt` naming the evidence.

Success criteria: the five computed values and the ping payload are exactly right; the four rates are positive numbers with
`gbps_node` (the ceiling for traffic that crosses the wire) at least as large as `gbps_pod_cross` and `gbps_service`; `bottleneck` is one of the allowed words; `notes.txt` has at least three lines.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/mtu-budget-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/mtu-budget-guide/check
```

Reading: [the lesson](lesson:LNX-312-T12), then [the quiz](quiz:LNX-312-T12).
