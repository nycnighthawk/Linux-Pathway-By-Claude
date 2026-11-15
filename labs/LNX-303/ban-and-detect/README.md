# Lab: ban brute force and detect a probe

`access.log` is a web server log: three failed logins from one address, a normal visitor, an administrator on the bastion `10.0.0.5` who mistyped once, a failed GET, a failed POST with a query string over HTTP/2.0, and an IPv6 client. Write a fail2ban filter and jail that stop password guessing without banning the others, and a Suricata rule for a configuration-file probe.

## Starting state

`setup` writes `access.log` into `$LAB_DIR`.

## Your task

1. `filter.conf`: a `[Definition]` with a `failregex` that matches failed `POST /login` requests (status 401, with or without a query string, any HTTP version, IPv4 and IPv6 clients) and nothing else. Use `<HOST>` for the address.
2. `jail.local`: a `[login-abuse]` jail that is enabled, uses the filter, reads the access log, bans after 5 to 10 failures within a window of 1 minute to 1 hour for at least 10 minutes through `nftables`, and never bans the bastion `10.0.0.5`.
3. `local.rules`: one Suricata rule that alerts on HTTP requests whose URI contains `/admin/config.php`, case-insensitively, towards `$HOME_NET`, with a local sid.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-303/ban-and-detect/setup
# ...write the files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-303/ban-and-detect/check
```

## Notes

- With fail2ban installed, `fail2ban-regex access.log filter.conf` is the real tool for the first task; the grader replays the log in Python so that it needs no package. `suricata -T` validates a rule file on a host that has Suricata.
- Reading material: [the lesson](lesson:LNX-303-T06). Afterwards, try [the quiz](quiz:LNX-303-T06).
