# Lab: write a kubeadm configuration for a three-node HA control plane

Write `kubeadm.yaml` in your working directory (`$LAB_DIR`) for a cluster whose control plane survives the loss of one machine.

## Starting state

`setup` writes `plan.txt` with the design inputs (endpoint name, subnets, version, node names) and a skeleton `kubeadm.yaml` that is incomplete.

## Your task

1. `ClusterConfiguration` uses `controlPlaneEndpoint` equal to the endpoint in `plan.txt`.
2. `networking.podSubnet` and `serviceSubnet` match `plan.txt` and do not overlap.
3. `kubernetesVersion` matches `plan.txt`.
4. A `KubeletConfiguration` document sets `cgroupDriver: systemd`.
5. `apiServer.certSANs` lists the endpoint host name and each node name from `plan.txt`.
6. Add `etcd.local` with the data directory `/var/lib/etcd` (stacked topology).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/kubeadm-ha-config/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/kubeadm-ha-config/check
```

Needs Python 3 with PyYAML. Reading: [the lesson](lesson:LNX-311-T02); then [the quiz](quiz:LNX-311-T02).
