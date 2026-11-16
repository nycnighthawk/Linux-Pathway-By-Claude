# Lab: configure a kube-proxy-free cluster

You will write the two configuration files that create a kubeadm cluster without kube-proxy and install Cilium
with the eBPF replacement and Hubble. The check parses the files; nothing is installed.

## Files (created by `setup` in `$LAB_DIR`)

1. `kubeadm-init.yaml`: a kubeadm `InitConfiguration` document. Skip the `addon/kube-proxy` phase (`skipPhases`).
2. `cilium-values.yaml`: Helm values with
   - `kubeProxyReplacement: true`, `k8sServiceHost: 10.0.0.10`, `k8sServicePort: 6443`
   - `routingMode: native`, `ipv4NativeRoutingCIDR: 10.244.0.0/16`, `autoDirectNodeRoutes: true`
   - `loadBalancer.mode: dsr`, `loadBalancer.algorithm: maglev`
   - `bpf.masquerade: true`
   - `hubble.relay.enabled: true`, `hubble.ui.enabled: true`

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/kpr-values/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/kpr-values/check
```

Needs `python3` and `PyYAML`. Value names follow the upstream chart at the time of writing (to verify against your chart version).
Reading: [the lesson](lesson:LNX-312-T05), then [the quiz](quiz:LNX-312-T05).
