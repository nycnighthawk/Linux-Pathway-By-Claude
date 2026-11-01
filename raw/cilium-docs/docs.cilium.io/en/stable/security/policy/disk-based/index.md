---
{"title": "Disk based Cilium Network Policies", "url": "https://docs.cilium.io/en/stable/security/policy/disk-based/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Disk based Cilium Network Policies[](#disk-based-cilium-network-policies "Link to this heading")

This functionality enables users to place network policy YAML files directly into the node's filesystem, bypassing the need for definition via k8s CRD. By setting the config field `static-cnp-path`{.docutils .literal .notranslate}, users specify the directory from which policies will be loaded. The Cilium agent then processes all policy YAML files present in this directory, transforming them into rules that are incorporated into the policy engine. Additionally, the Cilium agent monitors this directory for any new policy YAML files as well as any updates or deletions, making corresponding updates to the policy engine's rules. It is important to note that this feature only supports CiliumNetworkPolicy and CiliumClusterwideNetworkPolicy.

The directory that the Cilium agent needs to monitor should be mounted from the host using volume mounts. For users deploying via Helm, this can be enabled via `extraArgs`{.docutils .literal .notranslate} and `extraHostPathMounts`{.docutils .literal .notranslate} as follows:

``` {#codecell0}
extraArgs:
- --static-cnp-path=/policies
extraHostPathMounts:
- name: static-policies
  mountPath: /policies
  hostPath: /policies
  hostPathType: Directory
```

Copy First Line Copy All

To determine whether a policy was established via Kubernetes CRD or directly from a directory, execute the command `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} and examine the source attribute within the policy. In output, you could notice policies that have been sourced from a directory will have the `source`{.docutils .literal .notranslate} field set as `directory`{.docutils .literal .notranslate}. Additionally, `cilium`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`<endpoint_id>`{.docutils .literal .notranslate} also have fields to show the source of policy associated with that endpoint.

## Previous limitations and known issues[](#previous-limitations-and-known-issues "Link to this heading")

For Cilium versions prior to 1.14 deny-policies for peers outside the cluster sometimes did not work because of [GitHub issue 15198](https://github.com/cilium/cilium/issues/15198). Make sure that you are using version 1.14 or later if you are relying on deny policies to manage external traffic to your cluster.
