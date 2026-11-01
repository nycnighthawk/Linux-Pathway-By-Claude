---
{"title": "Restricting privileged Cilium pod access", "url": "https://docs.cilium.io/en/stable/security/restrict-pod-access/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Restricting privileged Cilium pod access[](#restricting-privileged-cilium-pod-access "Link to this heading")

This page shows you how to restrict privileged access to Cilium pods by limiting access from the Kubernetes API, specifically from [kubernetes exec pod](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/).

If you haven't read the [Introduction to Cilium & Hubble](../../overview/intro/#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on [Cilium Slack](https://slack.cilium.io). With Cilium contributors across the globe, there is almost always someone available to help.

## Setup Cilium[](#setup-cilium "Link to this heading")

If you have not set up Cilium yet, follow the guide [Cilium Quick Installation](../../gettingstarted/k8s-install-default/#k8s-install-standard) for instructions on how to quickly bootstrap a Kubernetes cluster and install Cilium. If in doubt, pick the minikube route, you will be good to go in less than 5 minutes.

### Background[](#background "Link to this heading")

The Cilium agent needs some specific Linux capabilities to perform essential system and network operations.

Cilium relies on Kubernetes and containers to set up the environment and mount the corresponding volumes. Cilium doesn't perform any extra operations that could result in an unsafe volume mount.

Cilium needs kernel interfaces to properly configure the environment. Some kernel interfaces are part of the `/proc`{.docutils .literal .notranslate} filesystem, which includes host and machine configurations that can't be virtualized or namespaced.

If `pod`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate} operations aren't restricted, then remote [exec into pods](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/) and containers defeats Linux namespace restrictions.

The Linux kernel restricts joining other namespaces by default. To enter the Cilium container, the `CAP_SYS_ADMIN`{.docutils .literal .notranslate} capability is required in both the current user namespace and in the Cilium user namespace (the initial namespace). If both namespaces have the `CAP_SYS_ADMIN`{.docutils .literal .notranslate} capability, then this is already a privileged access.

To prevent privileged access to Cilium pods, restrict access to the Kubernetes API and arbitrary `pod`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate} operations.

### Restrict authorization for `kubernetes`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pod`{.docutils .literal .notranslate}[](#restrict-authorization-for-kubernetes-exec-pod "Link to this heading")

To restrict access to Cilium pods through `kubernetes`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`exec`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pod`{.docutils .literal .notranslate}:

1.  Configure [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in Kubernetes.

2.  Limit [access to the proxy subresource of Nodes](https://kubernetes.io/docs/concepts/security/rbac-good-practices/#access-to-proxy-subresource-of-nodes).

### References[](#references "Link to this heading")

For more information about namespace security, visit:

-   [https://man7.org/linux/man-pages/man7/user_namespaces.7.html](https://man7.org/linux/man-pages/man7/user_namespaces.7.html)

-   [https://man7.org/linux/man-pages/man1/nsenter.1.html](https://man7.org/linux/man-pages/man1/nsenter.1.html)

-   [https://man7.org/linux/man-pages/man2/setns.2.html](https://man7.org/linux/man-pages/man2/setns.2.html)
