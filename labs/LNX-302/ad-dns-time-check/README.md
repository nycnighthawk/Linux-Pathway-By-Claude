# Lab: fix a member's resolver and time configuration

A Linux server in `acme.example` lost its domain membership after a domain controller reboot. You will read what its resolver and clock configuration look like, repair them, and write the two chrony configurations used in the domain: one for a member and one for a Samba DC that serves signed time to Windows clients.

## Starting state

`setup` writes `resolv.conf` (a DC and the office router as nameservers), `lookup.txt` (the record queries the member ran, including the failing one), stub `chrony-member.conf` and `chrony-dc.conf`, and `answers.txt`.

## Your task

1. `resolv.conf`: search domain `acme.example`; nameservers are the two DCs only (`10.0.0.10` and `10.0.0.11`); the router must not appear.
2. `chrony-member.conf`: `server dc1.acme.example iburst` and `server dc2.acme.example iburst`, plus a `makestep` line. A member serves no time, so it must not contain `allow`.
3. `chrony-dc.conf`: one upstream `server ... iburst`, `bindcmdaddress 10.0.0.10`, `allow 10.0.0.0/16`, `makestep`, and `ntpsigndsocket /var/lib/samba/ntp_signd`.
4. `answers.txt`: `failing_query` (the record name that returned NXDOMAIN), `why_nxdomain` (`router-answered` or `record-missing`), `max_kerberos_skew_minutes` and `tool_to_recreate_dc_records`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-302/ad-dns-time-check/setup
# ...do the task...
LAB_DIR=$PWD /path/to/repo/labs/LNX-302/ad-dns-time-check/check
```

## Notes

- On a real host: `host -t SRV _ldap._tcp.dc._msdcs.acme.example`, `resolvectl status`, `chronyc tracking`, `chronyc sources -v`.
- Reading material: [the lesson](lesson:LNX-302-T05). Afterwards, try [the quiz](quiz:LNX-302-T05).
