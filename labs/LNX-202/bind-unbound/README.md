# Lab: an authoritative BIND zone, a restricted policy and an Unbound resolver

Build a small DNS setup on the loopback interface: BIND answers for `lab.example` and nothing else, Unbound answers a local zone and forwards `lab.example` to BIND.

## Starting state

`setup` writes `named.conf`, an empty `lab.example.db` and `unbound.conf` in your working directory (`$LAB_DIR`). BIND listens on 127.0.0.1 port 5300 and Unbound on 127.0.0.1 port 5301, so nothing needs privileged ports.

## Your task

1. In `named.conf` turn recursion off and deny zone transfers (`allow-transfer { none; }`).
2. Add a primary zone `lab.example` that reads `lab.example.db`.
3. Write `lab.example.db` with: an SOA record (any serial in date form), `NS ns1`, `MX 10 mail`, `ns1` = 192.0.2.53, `www` = 192.0.2.80, `mail` = 192.0.2.25 and `app` as a CNAME to `www`.
4. In `unbound.conf` refuse all clients except loopback (`access-control: 0.0.0.0/0 refuse` and `127.0.0.0/8 allow`), hide the identity and version, and define a static local zone `lab.test.` with `router.lab.test.` at 192.0.2.1.
5. Add a `forward-zone` that sends `lab.example.` to `127.0.0.1@5300`. Because the forwarded zone is unsigned, mark it with `domain-insecure` if validation is on in your build. Unbound refuses to query loopback addresses unless `do-not-query-localhost: no` is set.

## Grade it

`bin/lpc course lab LNX-202 bind-unbound` runs the whole cycle. To grade your files run `check` with `LAB_DIR` set to the directory that holds them. The grader runs the check tools, starts both servers in the background, queries them with `dig` and stops them.

## Notes

- Check before you start a server: `named-checkconf named.conf`, `named-checkzone lab.example lab.example.db`, `unbound-checkconf unbound.conf`.
- Query by hand: `dig -p 5300 @127.0.0.1 www.lab.example`, and `dig -p 5301 @127.0.0.1 router.lab.test`.
- A name in a zone file that does not end in a dot is relative to the zone name.
- The lab needs the packages `bind9`, `bind9-utils`, `bind9-dnsutils` and `unbound`.
- Reading material: [the lesson](lesson:LNX-202-T04). Afterwards, try [the quiz](quiz:LNX-202-T04).
