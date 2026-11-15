# Lab: a daemon that speaks the systemd protocols

You will write a small daemon that uses socket activation, reports readiness with `sd_notify` messages, and logs to the
journal through stderr priorities, plus the two unit files that run it. The grader plays the part of the service manager, so
the lab runs with or without a live systemd.

## Starting state

`setup` writes `PROTOCOL.txt` (the three protocols and the behaviour required) and a blank `answers.txt`.

## Your task

1. Write `daemon.py` following `PROTOCOL.txt`. Use only the Python standard library: open the inherited socket with
   `socket.socket(fileno=3)`, and send datagrams to `NOTIFY_SOCKET` with a Unix datagram socket.
2. Write `lab.socket` (`ListenStream=/run/lab.sock`, `Accept=no`, an `[Install]` section) and `lab.service`
   (`Type=notify`, `NotifyAccess=main`, an `ExecStart` that runs `daemon.py`).
3. Try it without systemd: `systemd-socket-activate -l /tmp/lab.sock python3 daemon.py` and `printf 'ping\n' | nc -U /tmp/lab.sock`
   (if those tools are installed).
4. Fill in `answers.txt`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-220/sd-notify-activation/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-220/sd-notify-activation/check
```

## Notes

- The lab needs `python3`. On a VM with systemd you can also install the units and read the log with
  `journalctl -u lab.service`.
- Reading material: [the lesson](lesson:LNX-220-T08). Afterwards, try [the quiz](quiz:LNX-220-T08).
