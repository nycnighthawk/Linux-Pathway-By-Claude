---
{"title": "Fragment Handling", "url": "https://docs.cilium.io/en/stable/network/concepts/fragmentation/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Fragment Handling[](#fragment-handling "Link to this heading")

By default, Cilium configures the eBPF datapath to perform IP fragment tracking to allow protocols that do not support segmentation (such as UDP) to transparently transmit large messages over the network. This feature may be configured using the following options:

-   `--enable-ipv4-fragment-tracking`{.docutils .literal .notranslate}: Enable or disable IPv4 fragment tracking. Enabled by default.

-   `--enable-ipv6-fragment-tracking`{.docutils .literal .notranslate}: Enable or disable IPv6 fragment tracking. Enabled by default.

-   `--bpf-fragments-map-max`{.docutils .literal .notranslate}: Control the maximum number of active concurrent connections using IP fragmentation. For the defaults, see [eBPF Maps](../../ebpf/maps/#bpf-map-limitations).

To check whether fragmentation occurred, check the value of the following metrics:

-   `cilium_bpf_map_pressure{map_name="cilium_ipv4_frag_datagrams"}`{.docutils .literal .notranslate}

-   `cilium_bpf_map_pressure{map_name="cilium_ipv6_frag_datagrams"}`{.docutils .literal .notranslate}

If they're non-zero, it means that fragmented packets were processed.

As well, it's possible check how many MTU error messages (i.e. ICMP `fragmentation_needed`{.docutils .literal .notranslate} or ICMPv6 `packet_too_big`{.docutils .literal .notranslate}) have been processed by Cilium's datapath by checking the following metrics:

-   `mtu_error_message_total`{.docutils .literal .notranslate}

These packets are the basis for path MTU discovery and indicate that packets along a network path are exceeding max MTU size of the network.

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.
