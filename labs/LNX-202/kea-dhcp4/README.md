# Lab: a Kea DHCPv4 subnet with a pool, options and a reservation

Write the configuration of a small DHCPv4 server and let Kea itself test the syntax.

## Starting state

`setup` writes `kea-dhcp4.conf` in your working directory (`$LAB_DIR`) with the global settings and an empty `subnet4` list. Kea accepts `//` and `#` comments in this file.

## Your task

Add one subnet for `192.0.2.0/24` with an `id` of 1 and:

1. A pool of at least 50 addresses inside the subnet, written as `FIRST - LAST`.
2. The options `routers` = 192.0.2.1, `domain-name-servers` = 192.0.2.53 and `domain-name` = lab.example.
3. A reservation that gives the client with hardware address `52:54:00:aa:bb:01` the address 192.0.2.20 and the hostname `printer1`. The address must be outside the pool.
4. A `valid-lifetime` between 600 and 7200 seconds with `renew-timer` and `rebind-timer` below it (renew smaller than rebind).

## Grade it

`bin/lpc course lab LNX-202 kea-dhcp4` runs the whole cycle. To grade your file run `check` with `LAB_DIR` set to the directory that holds it. The grader runs `kea-dhcp4 -t` and then checks the design rules above with a small script.

## Notes

- `kea-dhcp4 -t FILE` checks syntax and semantics without starting the server.
- The timers are in seconds; clients renew at T1 and rebind at T2.
- A missing comma between two objects is the most common error.
- The lab needs the packages `kea-dhcp4-server` and `python3`.
- Reading material: [the lesson](lesson:LNX-202-T05). Afterwards, try [the quiz](quiz:LNX-202-T05).
