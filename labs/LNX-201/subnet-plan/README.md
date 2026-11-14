# Lab: plan the address space of a small site

You are given the IPv4 block `10.40.0.0/22` and the IPv6 block `2001:db8:10::/48` and must cut them into subnets.

## Starting state

`setup` writes `plan.txt` in your working directory (`$LAB_DIR`) with a `?` for every value.

## Your task

1. Allocate four IPv4 subnets inside `10.40.0.0/22`, with the **smallest prefix that fits** and no overlap:
   `users` (300 hosts), `servers` (100 hosts), `mgmt` (20 hosts) and `link` (a point-to-point link; a /30 or a /31).
   Write each as a network address in CIDR form, with the host bits zero (for example `10.40.0.0/23`).
2. Compute and write: `users_broadcast`, `servers_netmask` (dotted form) and `mgmt_last_host` (the highest usable address).
3. Give `users`, `servers` and `mgmt` one distinct IPv6 /64 each from `2001:db8:10::/48`.

You may use `python3 -c 'import ipaddress; ...'`, or do the binary arithmetic by hand and then confirm it.

## Grade it

`bin/lpc course lab LNX-201 subnet-plan` runs the grader on a fresh copy; to grade your own file run `check` with
`LAB_DIR` pointing at the directory that holds `plan.txt`.

## Notes

- A subnet with prefix length p has 2^(32-p) addresses; usable hosts are two fewer (network and broadcast), except /31.
- Aligning on the block size is what makes a network address valid: a /25 starts at a multiple of 128 in the last octet.
- Reading material: [the lesson](lesson:LNX-201-T01). Afterwards, try [the quiz](quiz:LNX-201-T01).
