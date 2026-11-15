# Lab: repair a draft libvirt domain definition

A colleague wrote a quick domain XML for a web guest. It would start, but slowly, with emulated hardware, an unpinned machine type and a console open to the network. Turn it into a definition you would be willing to keep in version control.

## Starting state

`setup` writes `web1.xml` into your working directory (`$LAB_DIR`).

## Your task

Edit `web1.xml` so that it describes this guest:

| Item | Requirement |
|---|---|
| acceleration | `type='kvm'` |
| memory, CPUs | 2 GiB, 2 vCPUs |
| machine type | a versioned q35 type, for example `pc-q35-9.2` |
| CPU | `<cpu mode='host-model'/>` |
| disk | qcow2 file `/var/lib/libvirt/images/web1.qcow2`, driver named `qemu` with `type='qcow2'`, target `vda` on the `virtio` bus |
| network | one interface of type `network` on the `default` network, model `virtio` |
| console | a pty console so `virsh console` works |
| graphics | removed or bound to `127.0.0.1` only |

The grader parses the XML and, when `virt-xml-validate` is installed, checks it against the libvirt domain schema. It does not define the guest; no hypervisor is needed.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-308/domain-xml/setup
# ...edit web1.xml...
LAB_DIR=$PWD /path/to/repo/labs/LNX-308/domain-xml/check
```

## Notes

- On a real host you would finish with `virsh define web1.xml` and `virsh start web1`; try it with `virsh -c qemu:///session` if you have libvirt installed.
- Reading material: [the lesson](lesson:LNX-308-T01). Afterwards, try [the quiz](quiz:LNX-308-T01).
