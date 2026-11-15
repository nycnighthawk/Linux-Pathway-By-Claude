# Lab: diagnose five captured failures

`cases/` in your working directory (`$LAB_DIR`) holds five captured outputs from a broken cluster. For each, name the cause and the first command you would run.

## Starting state

`setup` writes `cases/1.txt` to `cases/5.txt` and an empty `diagnosis.txt`.

## Your task

Write `diagnosis.txt` with one line per case in the form `N: cause-code | first-command`, using exactly one cause code from this list:

`oom-killed`, `selector-mismatch`, `cgroup-driver-mismatch`, `cert-expired`, `image-not-found`, `scheduling-taint`, `dns-loop`, `disk-pressure`

The first command must start with `kubectl`, `crictl`, `journalctl`, `systemctl` or `kubeadm`, and must be a plausible next step (the check looks for the tool that fits the layer).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-311/triage-cases/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-311/triage-cases/check
```

Reading: [the lesson](lesson:LNX-311-T10); then [the quiz](quiz:LNX-311-T10).
