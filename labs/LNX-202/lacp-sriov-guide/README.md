# Guide lab: LACP against a vendor switch, and SR-IOV virtual functions

Switch ports, port-channels and SR-IOV capable NICs cannot be tested on a shared runner, so this is a guided exercise with success criteria. Use a server with two bonded ports and a managed switch, or a server with an SR-IOV NIC; if you have neither, record `none` where the key says so and work through the criteria on paper with a lab at work or a vendor manual. The grader only checks that your report is complete and well formed; the evidence is on the equipment.

## Starting state

`setup` writes `report.txt` in your working directory (`$LAB_DIR`) with seven question marks.

## Your task

| Key | How to find it |
|---|---|
| `bond_mode` | the Bonding Mode line of `/proc/net/bonding/bond0`, as the mode name (`802.3ad`), or `none` |
| `aggregator_ids` | how many different Aggregator ID values the ports show (1 means one bundle), or `none` |
| `partner_mac` | the partner's system MAC in the 802.3ad section of the same file, or `none` |
| `lacp_rate` | `slow` or `fast` from the same file, or `none` |
| `sriov_totalvfs` | `cat /sys/class/net/IFACE/device/sriov_totalvfs`, or `none` |
| `vfs_enabled` | the number you wrote to `sriov_numvfs`, or `none` |
| `vf_spoofchk` | `on` or `off` for `vf 0` in `ip link show IFACE`, or `none` |

## Success criteria

- For a bond: you can explain what the switch needs (a port-channel in active or passive LACP mode, matching speed and VLANs) and what you saw when the two sides disagreed.
- You pulled one cable and watched the traffic move, and you know that one TCP stream still uses one port.
- For SR-IOV: IOMMU and SR-IOV are enabled in firmware and kernel, you created at least one VF, set its MAC and VLAN from the PF, and can say what traffic a VF bypasses (host bridge and firewall).
- Every key holds a value you read yourself.

## Grade it

`bin/lpc course lab LNX-202 lacp-sriov-guide` checks the starting state and the structure of the sample answer; to grade your own report run `check` with `LAB_DIR` set to the directory that holds `report.txt`.

## Notes

- This lab is not run by CI (environment H: hardware); the grader exists so the structure stays correct.
- Reading material: [the lesson](lesson:LNX-202-T11). Afterwards, try [the quiz](quiz:LNX-202-T11).
