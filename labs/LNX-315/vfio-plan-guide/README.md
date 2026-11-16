# Lab (hardware planning guide): read an IOMMU group listing and plan a passthrough

Passthrough needs real hardware, so this lab works on a captured listing. `setup` writes `iommu-groups.txt` (what you would collect from `/sys/kernel/iommu_groups` and `lspci -nns`) and `cmdline-now.txt`. If you have a machine with VT-d or AMD-Vi, repeat the steps on it: list the groups with a small shell loop, find your target and write the same report.

## Your task

The VM must get the RTX GPU (both of its functions). A colleague also wants the free NIC port 1.

1. Fill `report.txt`: the GPU's group and whether it is viable, the NIC port 1's group and whether it can be assigned alone (and why), the kernel command line additions for an Intel host, the `vendor:device` ids to bind to `vfio-pci` at boot (comma separated), and the guest firmware and machine type that suit a modern GPU.
2. Write `hostdev.xml` with the two libvirt `hostdev` elements (type `pci`, `managed='yes'`) for the GPU functions.

## Success criteria

The check parses your report and XML. In your own words (`nic_port1_reason`), explain the rule that decides viability: all endpoint devices of a group go to one owner.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vfio-plan-guide/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-315/vfio-plan-guide/check
```

Needs `python3`. Reading: [the lesson](lesson:LNX-315-T01); then [the quiz](quiz:LNX-315-T01).
