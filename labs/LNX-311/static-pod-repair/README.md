# Lab: repair a broken kube-scheduler static pod

A control-plane node's `kube-scheduler` pod will not stay healthy. The manifest lives in `manifests/kube-scheduler.yaml` in your working directory (`$LAB_DIR`). Fix it the way you would on a real node, where the kubelet watches `/etc/kubernetes/manifests`.

## Starting state

`setup` writes a manifest with four defects.

## Your task

1. The pod must use the host network (`hostNetwork: true`), as control-plane static pods do.
2. It must run with `priorityClassName: system-node-critical` so the node never evicts it first.
3. Its `--kubeconfig` and `--authentication-kubeconfig` flags must both point to `/etc/kubernetes/scheduler.conf`, and the matching `hostPath` volume must mount that same file read-only.
4. The liveness probe must hit `/livez` on the secure port named by `--secure-port=10259`, over HTTPS.

Do not change the image or remove other flags.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/static-pod-repair/setup
# edit manifests/kube-scheduler.yaml
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/static-pod-repair/check
```

## Notes

Needs Python 3 with PyYAML. Compare with a real `kubeadm` manifest on a lab node. Reading material: [the lesson](lesson:LNX-311-T01); then [the quiz](quiz:LNX-311-T01).
