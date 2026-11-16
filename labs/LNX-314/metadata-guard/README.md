# Lab: keep pods away from the metadata endpoint

A node runs pods in their own network namespace. A fake cloud metadata service answers on `169.254.169.254` and an internal service answers on `10.30.0.2`. Both live in a namespace behind the node, so pod traffic reaches them through the **forward** path.

## Starting state

`setup` writes `netenv` (builds and removes the test network), a stub `block.nft` and a weak `kubelet.yaml`. Needs `iproute2`, `nftables`, `curl`, `python3`, PyYAML, and root rights (the check uses `sudo` if needed).

## Your task

1. Edit `block.nft` so that `sudo nft -f block.nft` creates table `ip nodeguard` with a chain of type `filter` on the `forward` hook (policy accept) that drops traffic from the pod interface `v-pod-h` to `169.254.169.254`. The pod must still reach `10.30.0.2`, and the node itself must still reach the metadata address.
2. Edit `kubelet.yaml` to the safe node settings: anonymous authentication off, webhook authentication on with a client CA file, authorization mode `Webhook`, read-only port off, `protectKernelDefaults` true, certificate rotation on.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/metadata-guard/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/metadata-guard/check
```

Reading: [the lesson](lesson:LNX-314-T01); then [the quiz](quiz:LNX-314-T01).
