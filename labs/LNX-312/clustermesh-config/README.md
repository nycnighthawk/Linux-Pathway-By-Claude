# Lab: configuration for a two-cluster kind mesh

Write five files in `$LAB_DIR`. Nothing is created; the check parses them.

1. `kind-a.yaml` and `kind-b.yaml` (`kind.x-k8s.io/v1alpha4` `Cluster`): `networking.disableDefaultCNI: true`, and non-overlapping subnets:
   a uses `podSubnet: 10.1.0.0/16`, `serviceSubnet: 10.96.0.0/12`; b uses `podSubnet: 10.2.0.0/16`, `serviceSubnet: 10.97.0.0/12`.
2. `values-a.yaml` and `values-b.yaml` (Cilium Helm values): `cluster.name` `mesh-a` / `mesh-b`, `cluster.id` 1 / 2, `routingMode: tunnel`,
   `clustermesh.useAPIServer: true`, and `clustermesh.apiserver.service.type: NodePort`.
3. `rebel-base.yaml`: a Service `rebel-base` in `default` with `service.cilium.io/global: "true"` and `service.cilium.io/affinity: "local"`.

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-312/clustermesh-config/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-312/clustermesh-config/check
```

Needs `python3` and `PyYAML`. Value names follow the upstream chart (to verify for your chart version).
Reading: [the lesson](lesson:LNX-312-T11), then [the quiz](quiz:LNX-312-T11).
