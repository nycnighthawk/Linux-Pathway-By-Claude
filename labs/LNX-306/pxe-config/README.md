# Lab: configure network boot for BIOS and UEFI clients

`setup` writes an incomplete `dnsmasq.conf`, an empty `boot.ipxe` and an empty `default.ipxe`. Complete them so that BIOS and UEFI machines get the right loader, iPXE clients are sent to a script, a machine scheduled for a build gets an installer, and every other machine falls through to its disk. Nothing is started; the check reads the files (and runs `dnsmasq --test` if it is installed).

## Starting state

`dnsmasq.conf` has a DHCP range and nothing else.

## Your task

1. `dnsmasq.conf`: bind to the provisioning interface with `interface=eth1` and `bind-interfaces`; enable TFTP with `enable-tftp` and a `tftp-root`; match client architecture 0 as tag `bios`, 7 and 9 as tag `efi64` (`dhcp-match=set:...,option:client-arch,N`); match option 175 as tag `ipxe`; give BIOS clients `undionly.kpxe` and EFI clients `ipxe.efi`, both only when `tag:!ipxe`; give `tag:ipxe` clients a `dhcp-boot=` URL starting `http://`.
2. `boot.ipxe`: first line `#!ipxe`; `dhcp`; a `kernel` line with `inst.repo=http://` pointing into a path containing `/snapshots/`, `inst.ks=http://` ending `${mac}.cfg`, and `ip=dhcp`; an `initrd` line over `http://`; `boot`.
3. `default.ipxe`: first line `#!ipxe` and a line `exit` (the answer for machines not in build mode).

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-306/pxe-config/setup
# ...edit the three files...
LAB_DIR=$PWD /path/to/repo/labs/LNX-306/pxe-config/check
```

## Notes

- Needs `python3`. If `dnsmasq` is installed the check also runs `dnsmasq --test -C dnsmasq.conf` (it only parses; nothing is started).
- Reading material: [the lesson](lesson:LNX-306-T02). Afterwards, try [the quiz](quiz:LNX-306-T02).
