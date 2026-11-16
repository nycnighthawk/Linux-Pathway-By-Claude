# Lab: Pod Security Admission labels, a restricted Pod and a ValidatingAdmissionPolicy

Three small files, all graded offline (the check implements a subset of the restricted-level rules and tests the shape of the policy objects):

1. `pod.yaml`: the Pod `agent` asks for host networking, a hostPath volume, privileged mode and extra capabilities. Change it so it passes the **restricted** level while keeping the image and the scratch volume (replace the hostPath with an `emptyDir`, run as non-root, drop all capabilities except `NET_BIND_SERVICE`, forbid privilege escalation, set the seccomp profile).
2. `namespaces.yaml`: label `prod` to enforce `restricted` pinned to a `v1.x` version, with warn and audit `restricted`. Label `staging` to enforce `baseline`, with warn and audit `restricted`.
3. `vap.yaml`: a stable-API `ValidatingAdmissionPolicy` (failurePolicy `Fail`) that rejects Pod creation when any container image does not start with `registry.example/`, plus a `ValidatingAdmissionPolicyBinding` with action `Deny` that selects namespaces by label.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-314/psa-and-vap/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-314/psa-and-vap/check
```

Needs `python3` and PyYAML. Reading: [the lesson](lesson:LNX-314-T04); then [the quiz](quiz:LNX-314-T04).
