# Lab (hardware planning guide): size an SR-IOV deployment and write its host configuration

`setup` writes `device-info.txt` with the facts of one adapter. On a real SR-IOV NIC, repeat with its numbers (`cat /sys/class/net/IFACE/device/sriov_totalvfs`, `ip -d link show IFACE`).

## Your task

1. `report.txt`: how many VFs to enable for the workload, the maximum number of VFs that still leaves 8 queue pairs each (shared queue budget), and the queue pairs per VF you configure.
2. `vf-setup.sh`: write 0 and then the VF count to `sriov_numvfs`, then apply the policy for VF 0 with one `ip link set` on the PF: MAC, VLAN, rate cap, spoof checking, trust, link state.
3. `pool-network.xml`: a libvirt network (`forward mode='hostdev' managed='yes'`) that offers the PF's VFs as a pool.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/sriov-plan-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/sriov-plan-guide/check
```

The check reads the files (nothing is run against a real NIC). Reading: [the lesson](lesson:LNX-315-T02); then [the quiz](quiz:LNX-315-T02).
