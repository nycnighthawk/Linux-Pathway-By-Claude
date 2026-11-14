# Lab: a static address with netplan, rendered safely, and the same profile for NetworkManager

You will write a static interface configuration in netplan and check what systemd-networkd would receive, then produce the
equivalent NetworkManager keyfile, all without touching the host's network: both tools can render into files.

## Starting state

`setup` creates a fake root directory `root/` containing `root/etc/netplan/10-lab.yaml`, a skeleton that still asks DHCP
for `eth0` (mode 0600). Nothing outside the lab directory is read or changed.

## Your task

1. Edit `root/etc/netplan/10-lab.yaml` so `eth0` has the static address `192.0.2.10/24`, a default route via `192.0.2.1`,
   the nameserver `192.0.2.53` and the search domain `lab.test`, and no DHCP.
2. Render it: `netplan generate --root-dir "$PWD/root"`, then read `root/run/systemd/network/*.network`.
3. Create the same profile for NetworkManager without a running daemon:

   ```
   nmcli --offline connection add type ethernet con-name lab ifname eth0 ipv4.method manual \
       ipv4.addresses 192.0.2.10/24 ipv4.gateway 192.0.2.1 ipv4.dns 192.0.2.53 > lab.nmconnection
   ```

## Grade it

`bin/lpc course lab LNX-201 netplan-static` runs the whole cycle. To grade your own work run `check` with `LAB_DIR` set
to the directory that holds `root/` and `lab.nmconnection`. The grader runs `netplan generate` itself.

## Notes

- `netplan generate` only renders; `netplan apply` would also change the running system, and `netplan try` would roll back after a timeout.
- The rendered `.network` file is what `networkctl` would show as the configuration of the link.
- The lab needs the packages `netplan.io` and `network-manager` (for `nmcli --offline`).
- Reading material: [the lesson](lesson:LNX-201-T03). Afterwards, try [the quiz](quiz:LNX-201-T03).
