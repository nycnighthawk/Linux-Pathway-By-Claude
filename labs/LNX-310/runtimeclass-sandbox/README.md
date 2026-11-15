# Lab: wire a sandbox RuntimeClass and check KVM readiness

A cluster operator wants untrusted plug-in pods to run under gVisor. You write the containerd handler, the RuntimeClass and a pod that uses it, and you interpret a recorded readiness check for a VM-based alternative (Kata), which needs KVM. This lab is graded in a VM runner (environment V) because real KVM probing is the point on a real host; the grading itself uses the files you write and the recorded output.

## Starting state

`setup` writes `kvm_check.txt` (recorded output of three readiness commands on a cloud VM), `answers.txt`, an empty `k8s/` directory and `containerd-snippet.toml` (a stub).

## Your task

1. `k8s/runtimeclass.yaml`: a `RuntimeClass` (`node.k8s.io/v1`) named `gvisor` with `handler: runsc`, `overhead.podFixed` giving both `memory` and `cpu`, and `scheduling.nodeSelector` with at least one label.
2. `k8s/pod.yaml`: a Pod using `runtimeClassName: gvisor`, a pinned image (a version tag, not `latest`), `securityContext.runAsNonRoot: true` and container `resources.requests` for `memory` and `cpu`.
3. `containerd-snippet.toml`: the CRI runtime entry that defines the handler `runsc` with `runtime_type = "io.containerd.runsc.v1"`, under `plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runsc` (containerd 1.x layout) or `plugins."io.containerd.cri.v1.runtime".containerd.runtimes.runsc` (2.x layout).
4. `answers.txt`: from `kvm_check.txt`, `kvm_ready` (`yes` or `no`), `likely_cause` (`nested_virtualisation`, `no_cpu_support` or `missing_package`), and `gvisor_usable` (`yes` or `no`: does gVisor's default `systrap` platform need `/dev/kvm`?).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/runtimeclass-sandbox/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/runtimeclass-sandbox/check
```

## Notes

- Needs `python3-yaml` and Python 3.11 or later. Reading: [the lesson](lesson:LNX-310-T10). Afterwards try [the quiz](quiz:LNX-310-T10).
- On a real node run the three commands in `kvm_check.txt` yourself; a Kata pod needs `/dev/kvm`.
