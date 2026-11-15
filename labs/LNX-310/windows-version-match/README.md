# Lab: decide isolation modes from host and image versions

Windows containers only start when the host and the image versions fit together, and the isolation mode decides which combinations fit. You will turn the compatibility rules from the lesson into a decision table and repair a Windows Dockerfile. This lab is graded on a Windows runner (environment W); the scripts are Python so that they run the same on any platform, and no container engine is required.

## Starting state

`setup` creates `pairs.json` (host and image combinations), `plan.json` (empty), `Dockerfile` (a Linux-minded Windows build) and `answers.txt`. `$LAB_DIR` is your working directory.

## Your task

1. `plan.json`: a JSON object that maps each key `"<host>|<image>"` from `pairs.json` to `"process"` (process isolation works), `"hyperv"` (only Hyper-V isolation works) or `"impossible"` (neither works). Rules: a host runs images of its own release with process isolation and older Windows Server releases with Hyper-V isolation; it never runs a newer release; a Windows 11 24H2 host also runs Server 2025 and Server 2022 images with process isolation.
2. `Dockerfile`: use `mcr.microsoft.com/windows/servercore:ltsc2022` (an explicit long-term-servicing tag, never `latest`), set `SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop';"]`, end with `USER ContainerUser`, and use the exec form for `ENTRYPOINT`.
3. `answers.txt`: `k8s_isolation` (which mode Kubernetes supports on Windows nodes: `process` or `hyperv`) and `latest_tag` (`yes` or `no`: does Microsoft publish `latest` for the Windows base images?).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD python3 /path/to/repo/labs/LNX-310/windows-version-match/setup
# ...do the task...
LAB_DIR=$PWD python3 /path/to/repo/labs/LNX-310/windows-version-match/check
```

## Notes

- Needs only Python 3. Reading: [the lesson](lesson:LNX-310-T11). Afterwards try [the quiz](quiz:LNX-310-T11).
