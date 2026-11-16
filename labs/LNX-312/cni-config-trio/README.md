# Lab: the same overlay, three configurations

You will write the configuration that puts each of the three plugins into a VXLAN-based design for the same cluster.
Nothing is installed; the check parses your files.

## The scenario

The cluster Pod range is `10.244.0.0/16`. Nodes are on two subnets, and you want tunnels for everything with VXLAN.
Setup creates three skeleton files in `$LAB_DIR`:

1. `flannel-net-conf.json`: set `Network` to the Pod range, the backend `Type` to `vxlan`, `VNI` to `1` and `Port` to `8472`.
2. `calico-ippool.yaml`: an `IPPool` named `default-pool` with `cidr` the Pod range, `blockSize` 26, `vxlanMode` `Always`, `ipipMode` `Never`, `natOutgoing` true.
3. `cilium-values.yaml`: Helm values selecting tunnel routing with the vxlan protocol, and full kube-proxy replacement
   (`routingMode: tunnel`, `tunnelProtocol: vxlan`, `kubeProxyReplacement: true`).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/cni-config-trio/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/cni-config-trio/check
```

The check needs `python3` with `PyYAML`. Key names follow the upstream docs for Flannel, Calico and Cilium at the time of writing; verify against your installed version (to verify: Cilium value names change between releases).

Reading: [the lesson](lesson:LNX-312-T03), then [the quiz](quiz:LNX-312-T03).
