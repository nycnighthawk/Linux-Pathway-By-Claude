# Lab: route between two networks through a router

Three network namespaces play three hosts in a line: **lab-a** (10.1.1.2/24) - **lab-r** (10.1.1.1 and 10.1.2.1, a router
with forwarding on) - **lab-b** (10.1.2.2/24). Each host knows only its own network, so a and b cannot reach each other.

## Starting state

`setup` builds the namespaces and virtual Ethernet pairs with `ip netns` and `ip link add ... type veth`. It needs
root, or `sudo` (the CI runner has it). It changes nothing outside the namespaces except creating them.

## Your task

Use `ip -n <namespace> route ...` to give lab-a a route to 10.1.2.0/24 via 10.1.1.1 and lab-b a route to 10.1.1.0/24
via 10.1.2.1. Use these specific routes, not default routes. Then ping across: `ip netns exec lab-a ping -c1 10.1.2.2`.

Useful reading of the state: `ip -n lab-a route`, `ip -n lab-a route get 10.1.2.2`, `ip -n lab-r addr`.

## Grade it

`bin/lpc course lab LNX-201 route-through-router` runs the whole cycle. To grade your own work run `check`
(the namespaces must exist). Remove them afterwards with `ip netns del lab-a`, `lab-r` and `lab-b`.

## Notes

- A packet only crosses the router if the router forwards (`net.ipv4.ip_forward`, already set in lab-r) **and** the return path is routed, which is why both routes are needed.
- Without the return route the ping reaches lab-b but the reply is lost.
- The lab needs the package `iproute2` and a kernel with network namespaces and veth.
- Reading material: [the lesson](lesson:LNX-201-T05). Afterwards, try [the quiz](quiz:LNX-201-T05).
