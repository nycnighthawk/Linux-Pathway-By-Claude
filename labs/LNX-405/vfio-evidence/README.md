# Guide lab: VFIO passthrough of a real device

Give a physical PCI device that you can spare to a virtual machine through VFIO, on a host where the IOMMU is enabled. This is a guided exercise with success criteria. The grader only checks that your evidence file is complete, well formed and internally consistent; the real evidence is in your own notes, logs and screenshots.

## Starting state

`setup` writes `evidence.txt` in your working directory (`$LAB_DIR`) with a question mark for every key.

## Your task

| Key | How to find it |
|---|---|
| `iommu_enabled` | yes if `dmesg | grep -i -e DMAR -e IOMMU` shows it active |
| `device_class` | kind of device |
| `pci_address` | `lspci -nn`, the domain:bus:device.function |
| `iommu_group` | the number in /sys/kernel/iommu_groups/N |
| `group_members` | number of devices in that group |
| `all_members_assigned` | yes if every device in the group went to the same guest or is a bridge |
| `acs_override_used` | yes if you used a kernel patch or parameter that weakens group isolation; you want no |
| `bound_driver_after` | the driver shown by `lspci -k` after binding |
| `guest_sees_device` | yes if the guest lists the device with `lspci` |
| `guest_driver_works` | yes if the guest's own driver loaded and the device did real work |
| `reset_works` | yes if the device survived a guest reboot without a host reboot |
| `host_recovered` | yes if you returned the device to the host driver afterwards |

## Success criteria

- The device is not the one your host boots from or uses for its console.
- You read the IOMMU group before changing any binding.
- You can undo every change, and you did.
- You recorded the firmware and kernel settings that mattered.

## Grade it

`bin/lpc course lab LNX-405 vfio-evidence` checks the starting state and the structure of the sample answer; to grade your own file run `check` with `LAB_DIR` set to the directory that holds `evidence.txt`.

## Notes

- This lab is not run by CI (environment H: real hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-405-T04).
