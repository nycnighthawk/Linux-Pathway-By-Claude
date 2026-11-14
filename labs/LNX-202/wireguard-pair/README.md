# Lab: a WireGuard site-to-site tunnel, written as two configuration files

Two gateways, A (LAN 192.168.10.0/24, public address 198.51.100.1) and B (LAN 192.168.20.0/24, public address 203.0.113.2), will be joined by a tunnel on 10.77.0.0/24. You write the keys and both files; nothing is brought up, so the lab needs no kernel module and is safe anywhere.

## Starting state

`setup` removes old files and writes a `notes.txt` in your working directory (`$LAB_DIR`).

## Your task

1. Generate two key pairs: `wg genkey` into `a.key` and `b.key` with mode 600 (use `umask 077`).
2. Write `a.conf`: Address 10.77.0.1/24, ListenPort 51820, MTU 1420, A's private key, and one peer: B's public key (`wg pubkey < b.key`), `AllowedIPs` of exactly B's tunnel address `10.77.0.2/32` and B's LAN `192.168.20.0/24`, `Endpoint` 203.0.113.2:51821 and `PersistentKeepalive` 25.
3. Write `b.conf` the same way for B: Address 10.77.0.2/24, ListenPort 51821, MTU 1420 and one peer, A: `AllowedIPs` 10.77.0.1/32 and 192.168.10.0/24, `Endpoint` 198.51.100.1:51820, `PersistentKeepalive` 25.
4. Both files must be mode 600.

## Grade it

`bin/lpc course lab LNX-202 wireguard-pair` runs the whole cycle. To grade your files run `check` with `LAB_DIR` set to the directory that holds them. The grader derives the public keys from your key files, compares them with the peers' entries, checks addresses, ports and `AllowedIPs`, and runs `wg-quick strip` on each file.

## Notes

- Cryptokey routing: `AllowedIPs` decides both where packets for a destination go and which inner source addresses a peer may use.
- Only public keys are exchanged between the sites. A private key never leaves its host.
- On real hosts you would bring the tunnel up with `wg-quick up ./a.conf` (the name of the file becomes the interface name) and check it with `wg show`.
- The lab needs the packages `wireguard-tools` and `python3`.
- Reading material: [the lesson](lesson:LNX-202-T07). Afterwards, try [the quiz](quiz:LNX-202-T07).
