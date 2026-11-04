---
{"title": "IP Address Management (IPAM)", "url": "https://docs.cilium.io/en/stable/network/concepts/ipam/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# IP Address Management (IPAM)[](#ip-address-management-ipam "Link to this heading")

IP Address Management (IPAM) is responsible for the allocation and management of IP addresses used by network endpoints (container and others) managed by Cilium. Various IPAM modes are supported to meet the needs of different users:

  Feature                      Kubernetes Host Scope   Cluster Scope (default)   Multi-Pool   CRD-backed   AWS ENI          Azure IPAM         GKE
  ---------------------------- ----------------------- ------------------------- ------------ ------------ ---------------- ------------------ ----------------
  Tunnel routing               ✅                      ✅                        ✅           ❌           ❌               ❌                 ❌
  Direct routing               ✅                      ✅                        ✅           ✅           ✅               ✅                 ✅
  CIDR Configuration           Kubernetes              Cilium                    Cilium       External     External (AWS)   External (Azure)   External (GCP)
  Multiple CIDRs per cluster   ❌                      ✅                        ✅           N/A          N/A              N/A                N/A
  Multiple CIDRs per node      ❌                      ❌                        ✅           N/A          N/A              N/A                N/A
  Dynamic CIDR/IP allocation   ❌                      ❌                        ✅           ✅           ✅               ✅                 ❌

Don't change the IPAM mode of an existing cluster except when following a documented migration procedure. Changing the IPAM mode in a live environment may cause persistent disruption of connectivity for existing workloads. The safest path to change IPAM mode is to install a fresh Kubernetes cluster with the new IPAM configuration.

The only currently available online migration path is from cluster-pool IPAM to multi-pool IPAM. To migrate, see [Migrating from Cluster Scope to Multi-Pool](cluster-pool-to-multi-pool/#ipam-cluster-pool-to-multi-pool-migration).

-   [Cluster Scope (Default)](cluster-pool/)
-   [Kubernetes Host Scope](kubernetes/)
-   [Multi-Pool](multi-pool/)
-   [Migrating from Cluster Scope to Multi-Pool](cluster-pool-to-multi-pool/)
-   [Azure IPAM](azure/)
-   [Azure Delegated IPAM](azure-delegated-ipam/)
-   [AWS ENI](eni/)
-   [Google Kubernetes Engine](gke/)
-   [CRD-Backed](crd/)
-   [Technical Deep Dive](deep_dive/)
