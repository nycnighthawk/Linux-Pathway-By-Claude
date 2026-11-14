# Lab: HAProxy with health checks, and a keepalived VRRP pair

Configure the primary load balancer: HAProxy spreads requests over two backends and drops a dead one, and keepalived floats a virtual address and gives up the address when HAProxy dies.

## Starting state

`setup` writes `haproxy.cfg` (global and defaults only) and an empty `keepalived.conf` in your working directory (`$LAB_DIR`).

## Your task

HAProxy (`haproxy.cfg`):

1. A `frontend web` bound to `127.0.0.1:8080` with `default_backend app`.
2. A `backend app` with `balance roundrobin`, `option httpchk GET /health` and two servers, `127.0.0.1:8081` and `127.0.0.1:8082`, each with `check inter 1s fall 2 rise 2`.

keepalived (`keepalived.conf`), written for interface `eth0` (the grader substitutes the real name):

3. `global_defs` with `enable_script_security` and `script_user root`.
4. A `vrrp_script` that runs `/usr/bin/pgrep haproxy` every 2 seconds with a negative `weight` and `fall`/`rise` of 2.
5. A `vrrp_instance` with `state BACKUP`, `virtual_router_id 51`, a `priority` above 100, `advert_int 1`, PASS authentication, the virtual address `192.0.2.80/24` and the script in `track_script`.

## Grade it

`bin/lpc course lab LNX-202 haproxy-keepalived` runs the whole cycle. To grade your files run `check` with `LAB_DIR` set to the directory that holds them. The grader starts two small web servers on ports 8081 and 8082 and HAProxy in the foreground, sends requests, stops the first backend and checks that traffic moves to the second within five seconds. For keepalived it only tests the configuration (`keepalived -t`); a real failover needs two machines.

## Notes

- `haproxy -c -f haproxy.cfg` and `keepalived -t -f keepalived.conf` check files without starting anything.
- Without `enable_script_security` keepalived refuses to run scripts and the configuration test fails.
- The lab needs the packages `haproxy`, `keepalived`, `python3` and `curl`.
- Reading material: [the lesson](lesson:LNX-202-T06). Afterwards, try [the quiz](quiz:LNX-202-T06).
