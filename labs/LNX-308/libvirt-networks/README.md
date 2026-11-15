# Lab: write a NAT network, a VLAN access port and a macvtap interface

Three ways of attaching guests to a network, written as the XML libvirt consumes. You complete one network definition and two interface snippets that would go into a domain.

## Starting state

`setup` writes `lab-net.xml`, `trunk-iface.xml` and `macvtap-iface.xml` into your working directory (`$LAB_DIR`), each with a TODO comment.

## Your task

| File | Requirement |
|---|---|
| `lab-net.xml` | network `labnet`, NAT forwarding, bridge `virbr10`, gateway `192.168.150.1/24`, DHCP range `.100` to `.200`, and a reservation of `192.168.150.10` for host `db1` with MAC `52:54:00:aa:bb:01` |
| `trunk-iface.xml` | an interface of type `bridge` on host bridge `br0`, access VLAN 20 (a single tag, not a trunk), model `virtio` |
| `macvtap-iface.xml` | an interface of type `direct` on `eth0` in `bridge` mode, model `virtio` |

The reservation must lie outside the dynamic range. When `virt-xml-validate` is installed the network file is also checked against libvirt's schema. Nothing is defined on a host, so no hypervisor is needed.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/libvirt-networks/setup
# ...edit the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/libvirt-networks/check
```

## Notes

- On a real host: `virsh net-define lab-net.xml`, `virsh net-start labnet`, `virsh net-dhcp-leases labnet`. A macvtap guest cannot reach its own host through `eth0`; think about why.
- Reading material: [the lesson](lesson:LNX-308-T03). Afterwards, try [the quiz](quiz:LNX-308-T03).
