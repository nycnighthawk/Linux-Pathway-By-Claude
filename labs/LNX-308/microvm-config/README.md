# Lab: configure a Firecracker microVM and check nested virtualisation

Two small jobs around KVM: write the JSON configuration of a microVM, and fill in the facts you must know to enable and verify nested virtualisation. No guest is started; the grader reads the files.

## Starting state

`setup` writes `vm.json` (a faulty microVM configuration) and `nested.txt` (an unanswered sheet) into your working directory (`$LAB_DIR`).

## Your task

Fix `vm.json` so that the microVM has one writable root drive named `rootfs` on `/srv/fc/rootfs.ext4`, 2 vCPUs with SMT off, 256 MiB, a serial console, a boot command line that makes a crashed guest exit (`reboot=k panic=1`), and one network interface `eth0` on host tap `tap0` with a valid unicast MAC address.

Fill in `nested.txt`: the sysfs file that shows whether Intel nesting is on, the CPU flag names on Intel and AMD, the device node a VMM opens, the libvirt CPU mode that exposes the flag to a nested hypervisor, and a short reason why a named CPU model does not.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/microvm-config/setup
# ...edit vm.json and nested.txt...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/microvm-config/check
```

## Notes

- To try it for real you need `/dev/kvm`, a Firecracker binary, a kernel and a root file system: `firecracker --api-sock /tmp/fc.sock --config-file vm.json`.
- Reading material: [the lesson](lesson:LNX-308-T07). Afterwards, try [the quiz](quiz:LNX-308-T07).
