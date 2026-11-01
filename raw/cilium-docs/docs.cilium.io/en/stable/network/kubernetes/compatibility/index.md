---
{"title": "Kubernetes Compatibility", "url": "https://docs.cilium.io/en/stable/network/kubernetes/compatibility/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Kubernetes Compatibility[](#kubernetes-compatibility "Link to this heading")

Cilium is compatible with multiple Kubernetes API Groups. Some are deprecated or beta, and may only be available in specific versions of Kubernetes.

All Kubernetes versions listed are e2e tested and guaranteed to be compatible with Cilium. Older and newer Kubernetes versions, while not listed, will depend on the forward / backward compatibility offered by Kubernetes.

+------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| k8s Version            | k8s NetworkPolicy API                                                                                                               | CiliumNetworkPolicy                                                                                                                |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 1.33, 1.34, 1.35, 1.36 | -   [networking.k8s.io/v1](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#networkpolicy-v1-networking-k8s-io) | `cilium.io/v2`{.docutils .literal .notranslate} has a [CustomResourceDefinition](../../../glossary/#term-CustomResourceDefinition) |
+------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

As a general rule, Cilium aims to run e2e tests using the latest build from the development branch against currently supported Kubernetes versions defined in [Kubernetes Patch Releases](https://kubernetes.io/releases/patch-releases/) page.

Once a release branch gets created from the development branch, Cilium typically does not change the Kubernetes versions it uses to run e2e tests for the entire maintenance period of that particular release.

Additionally, Cilium runs e2e tests against various cloud providers' managed Kubernetes offerings using multiple Kubernetes versions. See the following links for the current test matrix for each cloud provider:

-   [AKS](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/azure/k8s-versions.yaml)

-   [EKS](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/eks/k8s-versions.yaml)

-   [GKE](https://raw.githubusercontent.com/cilium/cilium/1.20.4/.github/actions/gke/k8s-versions.yaml)

## Cilium CRD schema validation[](#cilium-crd-schema-validation "Link to this heading")

Cilium uses a CRD for its Network Policies in Kubernetes. This CRD might have changes in its schema validation, which allows it to verify the correctness of a Cilium Clusterwide Network Policy (CCNP) or a Cilium Network Policy (CNP).

The CRD itself has an annotation, `io.cilium.k8s.crd.schema.version`{.docutils .literal .notranslate}, with the schema definition version. By default, Cilium automatically updates the CRD, and its validation, with a newer one.

The following table lists all Cilium versions and their expected schema validation version:

  ---------------- -----------------------------
  Cilium Version   CNP and CCNP Schema Version
  v1.18.0-pre.0    1.31.2
  v1.18.0-pre.1    1.31.7
  v1.18.0-pre.2    1.31.9
  v1.18.0-pre.3    1.31.10
  v1.18.0-rc.0     1.31.11
  v1.18.0-rc.1     1.31.11
  v1.18.0          1.31.11
  v1.18.1          1.31.11
  v1.18.2          1.31.11
  v1.18.3          1.31.11
  v1.18.4          1.31.11
  v1.18.5          1.31.11
  v1.18.6          1.31.11
  v1.18.7          1.31.11
  v1.18.8          1.31.11
  v1.18.9          1.31.11
  v1.18.10         1.31.11
  v1.18.11         1.31.11
  v1.18.12         1.31.12
  v1.18.13         1.31.12
  v1.18.14         1.31.12
  v1.18.15         1.31.12
  v1.18            1.31.12
  v1.19.0-pre.0    1.32.1
  v1.19.0-pre.1    1.32.2
  v1.19.0-pre.2    1.32.3
  v1.19.0-pre.3    1.32.4
  v1.19.0-pre.4    1.32.5
  v1.19.0-rc.0     1.32.6
  v1.19.0-rc.1     1.32.6
  v1.19.0          1.32.6
  v1.19.1          1.32.6
  v1.19.2          1.32.6
  v1.19.3          1.32.6
  v1.19.4          1.32.6
  v1.19.5          1.32.6
  v1.19.6          1.32.7
  v1.19.7          1.32.7
  v1.19.8          1.32.7
  v1.19.9          1.32.7
  v1.19            1.32.7
  v1.20.0-pre.0    1.33.1
  v1.20.0-pre.1    1.33.2
  v1.20.0-pre.2    1.33.3
  v1.20.0-pre.3    1.33.8
  v1.20.0-pre.4    1.33.9
  v1.20.0-rc.0     1.33.9
  v1.20.0-rc.1     1.33.10
  v1.20.0          1.33.11
  v1.20.1          1.33.11
  v1.20.2          1.33.12
  v1.20.3          1.33.13
  v1.20            1.33.13
  latest / main    1.34.5
  ---------------- -----------------------------
