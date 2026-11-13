# Lab: a ClusterIP Service as an nftables verdict map

In this lab you write the node-local data plane for one Service, the way kube-proxy's nftables mode does, but by
hand. No Kubernetes cluster is needed: the lab only loads and inspects an nftables rule file.

## The scenario

A Service named `web` has the virtual IP `10.96.0.10` and listens on TCP port `80`. Two Pods back it:

| Pod | IP | Container port |
|---|---|---|
| web-0 | `10.244.1.5` | `8080` |
| web-1 | `10.244.2.7` | `8080` |

## Starting state

`setup` creates `service.nft` in your working directory (`$LAB_DIR`). It contains the table, an empty
verdict map named `services`, an empty `svc-web` chain, and two base chains, `prerouting` and `output`, with TODO
markers where your rules go.

## Your task

Edit `service.nft` so that all of these hold:

1. `services` maps the key `10.96.0.10 . tcp . 80` to the verdict `goto svc-web`.
2. `svc-web` rewrites the destination for TCP traffic to one of the two Pods, picked at random with equal
   probability, using `numgen` and a map whose values pair a Pod IP with port `8080`.
3. Both base chains look every packet up in the map by destination address, protocol and port, using `vmap @services`.
   The `prerouting` chain covers traffic from other hosts and Pods. The `output` chain covers traffic that starts on the
   node itself, which the first chain never sees.
4. `nft -c -f service.nft` accepts the file (a dry run: nothing is loaded into the kernel).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/nft-service-map/setup
# ...edit service.nft...
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/nft-service-map/check
```

In CI the harness runs `setup`, proves `check` fails, applies `solution/`, and proves `check` passes.
Try to finish before you open the solution. After it passes, think about what would change if a third Pod joined
(`mod 3`, one more map entry) and why that edit touches one chain instead of the whole table.

## Notes

- The check needs the `nft` command (package `nftables`) and permission to run the dry run, which in a container
  means the `NET_ADMIN` capability. The CI job provides both.
- Reading material: [the lesson](lesson:LNX-312-T04). Afterwards, try [the quiz](quiz:LNX-312-T04).
