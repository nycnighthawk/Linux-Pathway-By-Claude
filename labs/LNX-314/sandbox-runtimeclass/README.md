# Lab: a gVisor RuntimeClass, a sandboxed Pod and a policy that requires it

Everything is graded offline from the files (no runsc is needed). `setup` writes stubs and a `build-job` Pod in namespace `builds`.

## Your task

1. `runtimeclass.yaml`: `node.k8s.io/v1` RuntimeClass `gvisor`, handler `runsc`, overhead `podFixed` cpu `250m` and memory `120Mi`, scheduling to nodes labelled `sandbox=gvisor` with a toleration for the taint `sandbox=gvisor:NoSchedule`.
2. `pod.yaml`: make `build-job` use the class.
3. `containerd-snippet.toml`: the containerd CRI runtime entry for handler `runsc` with `runtime_type = "io.containerd.runsc.v1"`.
4. `require-sandbox.yaml`: a ValidatingAdmissionPolicy that rejects Pod creation unless `runtimeClassName` is `gvisor`, and a binding (Deny) for the `builds` namespace.
5. `answer.txt`: the Pod's effective requests for scheduling (container requests plus overhead): `effective_cpu_m=<n>` and `effective_memory_mi=<n>`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/sandbox-runtimeclass/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/sandbox-runtimeclass/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T08); then [the quiz](quiz:LNX-314-T08).
