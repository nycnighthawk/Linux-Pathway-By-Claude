# Lab: a default-drop input policy with nftables

A server namespace (**lab-srv**, 10.2.0.1) runs two TCP services, on ports 8080 and 9090. A client namespace
(**lab-cli**, 10.2.0.2) can reach both. Your job is to write a default-drop input policy that leaves only 8080 open.

## Starting state

`setup` builds the two namespaces joined by a virtual Ethernet pair, starts the services (inside lab-srv, listening
on all addresses), and writes `policy.nft` with an empty `input` chain. It needs root or `sudo` and does not touch
the host's own firewall: nftables rules are per network namespace.

## Your task

Complete `policy.nft` and load it into the server namespace:

```
ip netns exec lab-srv nft -c -f policy.nft     # dry run
ip netns exec lab-srv nft -f policy.nft        # load
```

The input chain must be a base chain with `policy drop` that accepts: the loopback interface, packets of established
and related connections, ICMP and ICMPv6, and TCP port 8080. Port 9090 must stay closed.

Test from the client: `ip netns exec lab-cli ping -c1 10.2.0.1`, and a TCP connection with `nc -zv -w2 10.2.0.1 8080`.

## Grade it

`bin/lpc course lab LNX-201 nft-input-policy` runs the whole cycle. To grade your own work run `check` after loading
the file. Clean up with `ip netns del lab-srv; ip netns del lab-cli` and `kill $(cat .srv.pid)`.

## Notes

- Rule order matters: put the established-connection rule first, so only new connections walk the whole list.
- Without the ICMPv6 rule an IPv6 host would lose neighbour discovery; the lab includes it as a habit.
- The lab needs the packages `nftables`, `iproute2` and `python3`.
- Reading material: [the lesson](lesson:LNX-201-T06). Afterwards, try [the quiz](quiz:LNX-201-T06).
