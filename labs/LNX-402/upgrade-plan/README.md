# Lab: a safe order for a Kubernetes minor upgrade

`setup` writes `upgrade.py` with a `plan` function that raises `NotImplementedError`. Implement it so it returns the ordered steps in the docstring and refuses unsupported jumps. The order encodes the rules: snapshot etcd before anything, upgrade the first control-plane node with `apply`, the others with `upgrade-node`, and workers one at a time with a drain and an uncordon.

The order of kubelet upgrades and the exact commands depend on the version and the installer (to verify against the current kubeadm documentation).

## Run it

`bin/lpc course lab LNX-402 upgrade-plan`, or edit `upgrade.py` in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-402-T03).
