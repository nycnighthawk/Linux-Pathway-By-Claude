# Lab: a Kconfig fragment for a guest kernel

`setup` writes `Kconfig.mini`, a small Kconfig with the same rules as the kernel's (`bool`, prompts, `depends on`, `select`, `default`). The check resolves your fragment the way `merge_config.sh` plus `make olddefconfig` would: a requested symbol whose dependencies are not met is dropped, a promptless symbol cannot be set directly, and `select` forces symbols on.

## Your task

Write `guest.config` for a minimal virtual machine guest. After resolution the result must have:

- `VIRTIO_BLK`, `VIRTIO_NET` and `SERIAL_8250_CONSOLE` enabled,
- `DEBUG_INFO`, `KASAN`, `KVM` and `VHOST_NET` disabled,
- and **every line of your fragment must survive resolution** (no silently dropped requests).

Use the kernel format: `CONFIG_X=y` and `# CONFIG_X is not set`. Read `Kconfig.mini` to find the parents each symbol needs.

## Success criteria

The check prints the resolved state and compares it with the rules above. It never builds a kernel. Needs `python3`.

## Grade it

```bash
mkdir -p ~/lab && cd ~/lab && LAB_DIR=$PWD /path/to/repo/labs/LNX-330/kconfig-fragment/setup
LAB_DIR=$PWD /path/to/repo/labs/LNX-330/kconfig-fragment/check
```

Reading: [the lesson](lesson:LNX-330-T02); then [the quiz](quiz:LNX-330-T02).
