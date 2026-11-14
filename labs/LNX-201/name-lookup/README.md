# Lab: make a name resolve, in the right order, with the right server

Name resolution on Linux is a chain: the name service switch decides *which* sources are asked and in what order
(`files`, `dns`, ...), `/etc/hosts` is the local source, and `systemd-resolved` decides *which DNS server* answers
which domain. This lab changes private copies of the files and tests them without touching the real ones.

## Starting state

`setup` writes three files in your working directory (`$LAB_DIR`): `hosts`, `nsswitch.conf` (the `hosts:` line asks
only DNS) and `resolved-lab.conf` (an empty `[Resolve]` drop-in).

## Your task

1. In `hosts`, give `10.20.30.40` the names `intranet.lab.test` and `intranet`.
2. In `nsswitch.conf`, make the `hosts:` line consult `files` first and keep `dns` after it.
3. In `resolved-lab.conf`, set `DNS=192.0.2.53` and `Domains=~lab.test`: the tilde makes it a routing-only domain, so
   only names under `lab.test` go to that server.

## Grade it

`bin/lpc course lab LNX-201 name-lookup` runs the whole cycle. The grader mounts your `hosts`, `nsswitch.conf` and a
throw-away `resolv.conf` over the real ones in a private mount namespace (it needs root, or `sudo`) and runs
`getent hosts intranet` and `getent hosts intranet.lab.test`; the real files are never modified.

## Notes

- `getent hosts` follows the system's lookup order like applications do; `dig` does not (it asks DNS only).
- The drop-in would be installed as `/etc/systemd/resolved.conf.d/lab.conf` followed by `systemctl restart systemd-resolved`.
- Reading material: [the lesson](lesson:LNX-201-T04). Afterwards, try [the quiz](quiz:LNX-201-T04).
