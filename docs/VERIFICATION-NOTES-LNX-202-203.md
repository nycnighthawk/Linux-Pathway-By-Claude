# Verification notes: LNX-202, LNX-203 and the Btrfs claim in LNX-103

Facts re-checked on 2026-11-15 against upstream documentation. Each row lists what changed and where it connects to other syntheses.

| Synthesis | Finding | Source checked |
|---|---|---|
| LNX-103-T02 | Btrfs RAID 5/6 is still rated unstable; no write journal; metadata should use RAID1/RAID1C3; RAID stripe tree is experimental with a non-final on-disk format (last change 6.12) and no RAID56 support | btrfs.readthedocs.io (Status, btrfs(5)) |
| LNX-202-T06 | RFC 5798 (VRRPv3) covers IPv4 and IPv6 and replaces RFC 3768; `http-check send` replaces the one-line `option httpchk GET`; `bind ... transparent` is an alternative to `ip_nonlocal_bind`; `vrrp_strict` conflicts with unicast peers; `authentication` is legacy VRRPv2 | docs.haproxy.org 3.0, keepalived docs, RFC 5798 |
| LNX-202-T10 | `-P` does not use more cores before iperf 3.16; UDP default rate is 1 Mbit/s; the old reference iperf.fr documents iperf2, replaced by software.es.net; pktgen control files and parameters added | software.es.net iperf3 news and man page, docs.kernel.org pktgen |
| LNX-202-T11 | `lacp_rate` is the rate requested of the partner, not a match to the switch; layer3+4 is not fully 802.3ad compliant; `lacp_active`, `lacp_strict`, `min_links`, `ad_select`; `sriov_numvfs` must pass through 0; `sriov_drivers_autoprobe`; exact `[SR-IOV]` keys | docs.kernel.org bonding and pci-iov-howto, systemd.link(5), systemd.network(5) |
| LNX-203-T03 | The rotate example deleted its own copy and counted wrongly (fixed with a `logs` subdirectory); `run -1` needs `bats_require_minimum_version 1.5.0`; added `run !`, `bats_pipe` (1.10), `bats::on_failure` (1.12), `--abort` and `--negative-filter` (1.13), 1.14 `run` honouring `set -e` and the empty-suite error | bats-core docs and changelog |

## Connections between syntheses

- LNX-202-T10 (measurement) feeds LNX-202-T11: test a bond with several flows, because the hash policy decides the port.
- LNX-202-T06 and T11 share the multicast-blocked failure: `unicast_peer` in keepalived, and LACP partner discovery on virtual switches.
- LNX-103-T02 (Btrfs profiles) and LNX-103-T05 (md RAID write hole) describe the same write-hole problem.
- LNX-203-T03 (bats) is the test harness for the labs in LNX-203-T01 and T07.
