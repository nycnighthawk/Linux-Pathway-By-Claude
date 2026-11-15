# Lab: forward logs reliably and rotate them safely

You will write an rsyslog forwarding rule that survives a collector outage and authenticates the collector, and a logrotate stanza that does not leave a service writing into a renamed file. The grader reads the files; it does not need a network or root.

## Starting state

`setup` creates stub files `10-forward.conf` and `logrotate-myapp.conf` and an `answers.txt`.

## Your task

1. In `10-forward.conf` write one `action(type="omfwd" ...)` that sends to `logs.example.org` port `6514` over TCP with the `gtls` stream driver in mode 1, authenticates the server by name (`x509/name` with permitted peers) and uses a disk-assisted queue with a file name, `saveOnShutdown` on and unlimited retries (`action.resumeRetryCount="-1"`).
2. In `logrotate-myapp.conf` write a stanza for `/var/log/myapp/*.log` that rotates daily or weekly, keeps at least 7, compresses, tolerates missing files and either reloads the service in `postrotate` or uses `copytruncate`.
3. Fill in `answers.txt`: the lossy transport, the command for the previous boot's kernel messages, and a phrase describing what you see when rotation happens without a reload.

If `rsyslogd` is installed the grader also runs `rsyslogd -N1` on your file as a hint.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-307/rsyslog-forward/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-307/rsyslog-forward/check
```

## Notes

- On a real pair of hosts, test with `logger -p local0.info test`, stop the collector, send more, restart it and confirm every message arrives.
- Reading material: [the lesson](lesson:LNX-307-T04). Afterwards, try [the quiz](quiz:LNX-307-T04).
