---
{"title": "Iptables Usage", "url": "https://docs.cilium.io/en/stable/network/ebpf/iptables/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Iptables Usage[](#iptables-usage "Link to this heading")

Depending on the Linux kernel version being used, the eBPF datapath can implement a varying feature set fully in eBPF. If certain required capabilities are not available, the functionality is provided using a legacy iptables implementation. See [Requirements for IPsec](../../../operations/system_requirements/#features-kernel-matrix) for more details.

## kube-proxy Interoperability[](#kube-proxy-interoperability "Link to this heading")

The following diagram shows the integration of iptables rules as installed by kube-proxy and the iptables rules as installed by Cilium.
