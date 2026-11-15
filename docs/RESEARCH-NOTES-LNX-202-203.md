# Research notes: LNX-202 and LNX-203 second pass

Date: 2026-11-15. Follows `docs/VERIFICATION-NOTES-LNX-202-203.md` (PR 26), which fixed the flagged claims. This pass reads each synthesis against upstream source code, reference manuals and its own test runs, and adds what the first pass left out. Every row says what changed, how it was checked and where it connects to other syntheses.

How facts were checked, in order of strength: (1) run on this host (bash 5.2.21, mawk 1.3.4, jq 1.7, PyYAML 6.0.3, Python 3.13, git 2.43, systemd 255, pytest); (2) upstream source or reference text read directly (kernel `Documentation/`, `iproute2` man pages, systemd man sources, radvd, wg-quick, Kea, BIND, Unbound, FRR, HAProxy, keepalived, ShellCheck, bats-core, jq, Git and bash release files); (3) general knowledge, marked below as "unverified here". The `ip` command was not installed on this host, so the namespace and VRF command sequences were not executed; `bats` was not run because installing it would have meant running a downloaded program, so its examples were checked against its manual instead.

## Corrections found in the existing text

| Where | What was wrong | Evidence |
|---|---|---|
| LNX-202-T03 (and its lesson and quiz) | Said radvd refuses to run when IPv6 forwarding is off. The daemon logs a warning and continues. The failure is a gateway that cannot forward, not a missing daemon. | radvd.c, `check_ip6_forwarding()` branch logs "continuing anyway" |
| LNX-202-T02 | Said enslaving an interface sets up the l3mdev rule. One rule serves all VRFs and is created when the first VRF device is created. | docs.kernel.org vrf.rst |
| LNX-202-T01 | `lacp_rate` described as the rate this host sends LACPDUs. It is the rate this host asks the partner to use (PR 26 corrected this in T11 only). Also the claim that a bond port must be down before it joins was too strong. | docs.kernel.org bonding.rst |
| LNX-202-T04 | Described the default DNSSEC policy as a key-signing and zone-signing pair. The built-in `default` policy is one combined signing key, ECDSAP256SHA256, unlimited lifetime, NSEC. | BIND 9 ARM, `dnssec-policy` |
| LNX-202-T05 | Described T1 and T2 as always half and seven eighths while the example set 900 and 1800. The server sends no T1/T2 unless `renew-timer`/`rebind-timer` or `calculate-tee-times` is set. Also described `kea-ctrl-agent` as the management interface. The agent was removed in Kea 3.1.8; daemons serve HTTP control themselves since 2.7.2. Hook libraries: most are open source since 3.0.0. | Kea ARM (dhcp4-srv, ctrl-channel, hooks), Kea ChangeLog |
| LNX-202-T06 | Said HAProxy has no state sync. Stick tables replicate through `peers`; connections do not. Script weight and `nopreempt` details were missing. | HAProxy 3.2 manual, keepalived.conf.5 |
| LNX-202-T07 | WireGuard MTU line (1420, or 1400 over IPv6 or PPPoE) did not match what wg-quick does: path MTU minus 80. Libreswan example used the superseded `ikev2=yes`. | wg-quick `linux.bash`, `set_mtu_up`; ipsec.conf(5) |
| LNX-203-T03 | The rotation example parsed `ls`, contradicting the rule in LNX-203-T02. Replaced with a NUL-safe `find`/`sort -z`/`tail -z` version and run against names with spaces and a leading dash. | run on this host |
| LNX-203-T07 (and lesson) | Said `ExecStart=` must be an absolute path. A bare name from a fixed search list is accepted. | systemd.service(5) |
| LNX-203-T04 | Said jq loses precision for large integers in "older versions". From 1.7 an unchanged literal is preserved, arithmetic converts to a double. Function-version claim replaced with what the changelog and the host show. | jq NEWS.md; run on jq 1.7 |

## Additions by synthesis

| Synthesis | Added | Source |
|---|---|---|
| LNX-202-T01 | `encap2+3`, `encap3+4`, `vlan+srcmac`; 802.3ad compliance of hash policies; `stp_mode`, `mst_enabled`; `vlan_protocol 802.1ad`; the whole stack as systemd-networkd files; `min_links`, `ad_select` | kernel bonding.rst; ip-link man page; systemd.netdev and systemd.network |
| LNX-202-T02 | Three-namespace router lab with the per-namespace forwarding trap; `udp_l3mdev_accept`, `raw_l3mdev_accept`; wg-quick's `not fwmark` plus `suppress_prefixlength 0` rules; `fib_multipath_hash_policy` values; networkd `[RoutingPolicyRule]` and `[VRF]`; kernel selftests as examples | vrf.rst, ip-sysctl.rst, wg-quick, networkd manuals, `tools/testing/selftests/net` |
| LNX-202-T03 | `addr_gen_mode` values, `accept_ra_pinfo`; the kernel does not process RDNSS; networkd `[IPv6SendRA]`/`[IPv6Prefix]` and dnsmasq `ra-only`/`slaac`/`ra-stateless` as radvd alternatives | ip-sysctl.rst, systemd.network, dnsmasq manual |
| LNX-202-T04 | CSK default and `checkds`; pinned policy example with `nsec3param`; `recursion` default is yes; Unbound `qname-minimisation`, `aggressive-nsec`, `edns-buffer-size` 1232, `serve-expired`, `control-enable` defaults; DS mismatch after a provider change | BIND ARM, unbound.conf, RFC 9276 |
| LNX-202-T05 | `calculate-tee-times`, `t1-percent`, `t2-percent`; reservation flags and defaults; `host-reservation-identifiers`; PXE class from the manual's architecture test; relay subnets; control channel migration; hook licensing | Kea ARM |
| LNX-202-T06 | keepalived advert timeout formula, `nopreempt` initial state, `preempt_delay`, `vrrp_track_process` exact match, script user and `enable_script_security`; HAProxy stick-table rate limiter, `peers`, ACME in 3.2, `ip` vs `ipv4` table type | keepalived.conf.5, HAProxy 3.2 manual |
| LNX-202-T07 | MTU arithmetic; wg-quick full-tunnel rule set, `Table = off`, `syncconf`, preshared keys; XFRM interfaces (`ip link add ... type xfrm`), Libreswan `ipsec-interface`, strongSwan `if_id_in/out` and a `swanctl.conf` | wg-quick, ip-link man page, ipsec.conf(5), strongSwan swanctl.conf reference |
| LNX-202-T08 | `-Q`, `--immediate-mode`, `--time-stamp-precision`, `-d`, `-z`; dumpcap ring options; `tshark -z expert`; nftables trace for packets that never reach the capture point | tcpdump(1); RHEL nftables debugging chapter |
| LNX-202-T09 | RFC 8212 behaviour of `ebgp-requires-policy`; `frr defaults` profiles; OSPF timer, priority and cost defaults; `ip ospf area` vs `network`; leaf BGP example with ECMP; kernel protocol numbers; soft reconfiguration; `import-check` failing example; topotests | FRR user guide and source, rt_protos |
| LNX-202-T10 | Goodput arithmetic (9.41 and 9.90 Gb/s), bandwidth-delay product, `ss -ti`, pktgen sample scripts and the burst option, RPS/RFS sysfs files | kernel scaling and pktgen docs and sample scripts |
| LNX-202-T11 | Vendor vocabulary for LACP; MLAG evidence in `/proc/net/bonding`; VF rate, trust, link-state options; VF live migration constraints; `switchdev` mode and representors | RHEL virtualisation guide chunk, ip-link man page |
| LNX-203-T01 | `ERR` trap and `set -E`; EXIT on TERM; `local x=$(...)`; `inherit_errexit`; `lastpipe`; release table (4.2, 4.4, 5.0, 5.1, 5.2); `wait -n -p` pattern | bash NEWS (5.2 tarball); all behaviours run on bash 5.2 |
| LNX-203-T02 | `.shellcheckrc`, optional checks, `source-path=SCRIPTDIR`; 0.11.0 changes; pre-commit hook; SC2337 for `grep -q` under pipefail; three runnable strict-mode proofs | ShellCheck manual and changelog; run on bash 5.2 |
| LNX-203-T03 | Tags, `bats_test_function`, comment syntax, `bats_load_library`, `skip`, the file descriptor 3 hang, `run -0` equivalence | bats-core writing-tests manual |
| LNX-203-T04 | Which awk (mawk vs gawk) on Debian and what breaks; jq version changes; YAML 1.1 hazards measured with PyYAML and Python `yq`; CSV field-count demo | run on mawk 1.3.4, jq 1.7, PyYAML 6.0.3 |
| LNX-203-T05 | Inline script metadata (PEP 723) with `uv run` or `pipx run`; `subprocess` exception behaviour; pytest tests for the rotation script including the `caplog` versus `basicConfig` trap | packaging specification; pytest run |
| LNX-203-T06 | `zdiff3`, `autoSetupRemote`, `rerere`, `--update-refs` (tried on a stacked pair), SSH signing, `range-diff`; Git 3.0 plan; CI sketch | Git configuration and rebase manuals, BreakingChanges |
| LNX-203-T07 | Offline exposure scores for the example unit (9.4, 5.4, 1.4) and threshold scale; `Type=exec`; credentials; `FixedRandomDelay`; `systemd-analyze calendar` | systemd 255 on this host; systemd manuals |

## Connections between syntheses

Existing links (from the first pass): T10 feeds T11; T06 and T11 share the multicast problem; LNX-103-T02 and T05 share the write hole; bats (LNX-203-T03) tests the labs of T01 and T07. New links added in this pass:

- **Flow hashing is one idea in five places.** Bond transmit hash (LNX-202-T01), ECMP `fib_multipath_hash_policy` (LNX-202-T02 and T09), `encap` hash modes for tunnels (T01 and T07), the iperf stream count (T10) and vendor LACP hashing (T11). A single TCP flow never exceeds one path in any of them.
- **Policy routing carries tunnels.** wg-quick's rule pair (LNX-202-T07) is the `ip rule` mechanism of LNX-202-T02; an XFRM interface lets FRR (T09) run BGP across IPsec (T07).
- **MTU is the common failure.** OSPF ExStart (T09), WireGuard overhead (T07), bond/bridge/VLAN children (T01), offload artefacts in captures (T08) and jumbo-frame goodput (T10).
- **Capture and counters answer "where did it stop".** tcpdump on both sides, nft trace and `ip route get` (T08, T02); `ss -ti` and per-queue CPU (T10).
- **systemd-networkd expresses the same objects** as the `ip` commands in T01, T02 and T03 (bond, bridge VLAN, VRF, policy rules, router advertisements), which is the persistence answer for each.
- **The shell slices form one chain.** ShellCheck (LNX-203-T02) flags the `grep -q` pipefail case that T02's text describes and T01's `local` masking (SC2155); bats (T03) is where the proofs of strict-mode behaviour should live; T06's CI sketch runs both; T07's `systemd-analyze` checks fit the same bats suite; T05 gives the Python counterpart (pytest, `caplog`).
- **Rotation example in three languages.** The same log-rotation task appears in bash (T03, NUL-safe), Python (T05, `pathlib`) and as a bats or pytest test.
- **Version drift is a recurring risk.** Kea control agent (T05), BIND default policy (T04), ShellCheck defaults (T02), jq functions (T04), bash features (T01), HAProxy table types (T06), Git 3.0 (T06), FRR defaults profile (T09). Each synthesis now names the release where behaviour changed.

## Not verified here (training knowledge)

- Vendor CLI spellings for port channels in T11 (marked in the text).
- Kernel STP being the classic 802.1D protocol only, with RSTP/MSTP from a userspace daemon (the man page confirms the MST primitives and the missing implementation, not the statement about the kernel's STP).
- The skb drop-reason tracing mention in LNX-202-T08.
- gawk counting characters in a UTF-8 locale (LNX-203-T04); only mawk was measured.
- The Libreswan, strongSwan and Kea examples were checked against option references but not run.

## Follow-ups worth a later pass

- Run the LNX-202-T02 lab and the LNX-203 bats examples in a container that has `iproute2` and `bats` (the labs under labs/LNX-202 and labs/LNX-203 hold the lab definitions).
- LNX-202-T09: add the `show bgp summary` output with the policy marker once captured from a real session.
- `labs/LNX-202/haproxy-keepalived/README.md` says keepalived refuses to run scripts and the configuration test fails without `enable_script_security`. The manual says the option stops scripts that run as root from a path a non-root user can write to. keepalived was not installed here, so the stated refusal is unconfirmed and was left unchanged.
- Sections not deepened this pass: history paragraphs, which were accurate when checked.
