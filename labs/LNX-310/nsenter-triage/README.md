# Lab: triage a restarting container from recorded evidence

A service named `api` is restarted every half minute and nobody knows why. Recorded `docker inspect`, `docker events` and cgroup output are supplied. You read them, state the cause, and write the commands that would capture the network traffic of the container from the host without installing anything in the image.

## Starting state

`setup` writes `inspect.json`, `events.txt`, `memory.events` (the cgroup counters of the container), `answers.txt` and `debug.sh` (a stub).

## Your task

1. `answers.txt`:
   - `exit_signal`: the signal name behind the exit code in `inspect.json` (for example `SIGTERM`).
   - `oom_killed`: `yes` or `no`, from `OOMKilled` and `memory.events`.
   - `restart_interval_seconds`: the number of seconds between two `die` events in `events.txt`.
   - `entrypoint_form`: `shell` or `exec`, from `Config.Entrypoint`.
   - `root_cause`: `oom`, `stop_timeout`, `crash` or `bad_command`.
   - `fix`: `exec_form`, `raise_memory_limit` or `fix_shebang`.
2. `debug.sh`: commands, run on the host as root, that (a) read the container's PID from `docker inspect` or use the PID recorded in `inspect.json`, (b) use `nsenter` with only the network namespace (`-n`) to run `tcpdump` on port 8443, writing to `/tmp/api.pcap`, and (c) do not join the mount namespace (`-m` or `-a`), so the host's tcpdump stays available.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-310/nsenter-triage/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-310/nsenter-triage/check
```

## Notes

- Reading: [the lesson](lesson:LNX-310-T09). Afterwards try [the quiz](quiz:LNX-310-T09).
- Exit codes above 128 are 128 plus the signal number.
