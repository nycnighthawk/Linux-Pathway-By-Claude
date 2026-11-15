# Lab: a keepalived and HAProxy front end

Write the configuration for a pair of load balancers. LB-A (`192.168.10.11`) and LB-B (`192.168.10.12`) share the address `192.168.10.100/24` on `eth0` and balance two application servers, `192.168.10.21:8080` and `192.168.10.22:8080`. The grader checks the files statically and, if `keepalived` and `haproxy` are installed, also runs `keepalived -t` and `haproxy -c`. Nothing is started.

## Your task

1. `keepalived-a.conf` and `keepalived-b.conf`: a `vrrp_instance` on `eth0` with the same `virtual_router_id`, different priorities, unicast source and peer addresses (the other node), the virtual address `192.168.10.100/24`, and a `vrrp_script` (with `interval`) listed in `track_script`, and `global_defs { enable_script_security script_user root }` (keepalived refuses to run scripts otherwise). Do not use `auth_type PASS`.
2. `haproxy.cfg`: `defaults` with `mode http`, the three timeouts and `option forwardfor`; a `frontend` bound to `192.168.10.100:80` with a `default_backend`; a `backend` with `balance roundrobin` or `leastconn`, `option httpchk GET /healthz` and both servers with `check inter 2s fall 3 rise 2`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-309/keepalived-haproxy/setup
# ...write the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-309/keepalived-haproxy/check
```

## Notes

- To run it for real, set `net.ipv4.ip_nonlocal_bind=1` on both nodes, allow VRRP (protocol 112) between them, and stop HAProxy on the master to watch the address move.
- Reading material: [the lesson](lesson:LNX-309-T03). Afterwards, try [the quiz](quiz:LNX-309-T03).
