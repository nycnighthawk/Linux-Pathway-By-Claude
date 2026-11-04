---
{"title": "Identity Management Mode", "url": "https://docs.cilium.io/en/stable/network/kubernetes/identity-management-mode/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Identity Management Mode[](#identitymanagementmode "Link to this heading")

Cilium supports Cilium Identity (CID) management by either the Cilium Agents (default) or the Cilium Operator.

When the Operator manages identities, identity creation is centralized. This provides benefits such as reduced CID duplication, which can occur when multiple Agents simultaneously create identities for the same set of labels. Given that there is a limitation on the maximum number of identities in a cluster and eBPF Policy Map size (see [eBPF Maps](../../ebpf/maps/#bpf-map-limitations)), when the operator manages identities, we can improve the reliability of network policies and cluster scalability.

Note

Labels relevant to identity management may be configured in the Cilium ConfigMap (see: [Limiting Identity-Relevant Labels](../../../operations/performance/scalability/identity-relevant-labels/#identity-relevant-labels)). If the Cilium Operator is managing identities, both the Operator and Agents must be restarted to pick up the new label pattern setting.

## Enable Identity Management by the Cilium Operator (Beta)[](#enable-identity-management-by-the-cilium-operator-beta "Link to this heading")

Note

This is a beta feature. Please provide feedback and file a GitHub issue if you experience any problems.

The Cilium Agents manage CIDs by default. This section describes the steps necessary for enabling CID management by the Cilium Operator.

### Enable Operator Managing Identities on a New Cluster[](#enable-operator-managing-identities-on-a-new-cluster "Link to this heading")

To enable the Cilium Operator to manage identities on a new cluster, set the `identityManagementMode`{.docutils .literal .notranslate} value to `operator`{.docutils .literal .notranslate} in your Helm chart or set the `identity-management-mode`{.docutils .literal .notranslate} flag to `operator`{.docutils .literal .notranslate} in the `cilium-config`{.docutils .literal .notranslate} configmap.

### How to Migrate from Cilium Agent to Cilium Operator Managing Identities[](#how-to-migrate-from-cilium-agent-to-cilium-operator-managing-identities "Link to this heading")

In order to minimize disruptions to connections or workload management, the following procedure should be followed. Note that in order to prevent disruptions to the cluster, there is an intermediate state where both the Cilium Agents and the Operator manage identities. As long as the Cilium Agents are creating identities, the CID duplication issue may occur. The transitional state is intended to only be used temporarily for the purpose of migrating identity management modes.

1.  Allow the Operator to also manage identities by setting the `identityManagementMode`{.docutils .literal .notranslate} value to `both`{.docutils .literal .notranslate} in your Helm chart or by setting the `identity-management-mode`{.docutils .literal .notranslate} flag to `both`{.docutils .literal .notranslate} in the `cilium-config`{.docutils .literal .notranslate} configmap. Restart the Operator.

2.  Once the operator is running, upgrade the Cilium Agents by setting the `identityManagementMode`{.docutils .literal .notranslate} value to `operator`{.docutils .literal .notranslate} or by setting the `identity-management-mode`{.docutils .literal .notranslate} flag to `operator`{.docutils .literal .notranslate} and restarting the Cilium Agent DaemonSet.

### How to Downgrade from Cilium Operator to Cilium Agent Managing Identities[](#how-to-downgrade-from-cilium-operator-to-cilium-agent-managing-identities "Link to this heading")

For a safe downgrade, the following procedure should be followed.

1.  First, downgrade the Cilium Agents by setting the `identityManagementMode`{.docutils .literal .notranslate} value to `both`{.docutils .literal .notranslate} in your Helm chart or by setting the `identity-management-mode`{.docutils .literal .notranslate} flag to `both`{.docutils .literal .notranslate} in the `cilium-config`{.docutils .literal .notranslate} configmap. Restart the Cilium Agent DaemonSet.

2.  Once the Cilium Agents are running, downgrade the Operator by setting the `identityManagementMode`{.docutils .literal .notranslate} value to `agent`{.docutils .literal .notranslate} and restarting the Operator.

## Metrics[](#metrics "Link to this heading")

Metrics for identity management by the operator are documented in the [Identity Management Mode](../../../observability/metrics/#identity-management-metrics) section of the metric documentation.
