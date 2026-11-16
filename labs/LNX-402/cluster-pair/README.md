# Lab: two clusters that can be joined later, and one safe gateway

`setup` writes two kubeadm cluster configurations and a Gateway manifest. They have defects that would hurt later: overlapping pod and service ranges, the same cluster name and endpoint, mismatched minor versions, no kube-proxy skip although Cilium replaces it, and a gateway that anyone can attach routes to. Fix the three files until `check` passes. (The `skipPhases` key is the one this grader looks for; the exact kubeadm field layout depends on the configuration version, to verify.)

## Run it

`bin/lpc course lab LNX-402 cluster-pair`, or edit the files in your work directory and run `check` with `LAB_DIR` set to it.

## Notes

Reading material: [the milestone](lesson:LNX-402-T01).
