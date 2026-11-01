---
{"title": "Concepts", "url": "https://docs.cilium.io/en/stable/network/kubernetes/concepts/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Concepts[](#concepts "Link to this heading")

## Deployment[](#deployment "Link to this heading")

The configuration of a standard Cilium Kubernetes deployment consists of several Kubernetes resources:

-   A `DaemonSet`{.docutils .literal .notranslate} resource: describes the Cilium pod that is deployed to each Kubernetes node. This pod runs the cilium-agent and associated daemons. The configuration of this DaemonSet includes the image tag indicating the exact version of the Cilium docker container (e.g., v1.0.0) and command-line options passed to the cilium-agent.

-   A `ConfigMap`{.docutils .literal .notranslate} resource: describes common configuration values that are passed to the cilium-agent, such as the kvstore endpoint and credentials, enabling/disabling debug mode, etc.

-   `ServiceAccount`{.docutils .literal .notranslate}, `ClusterRole`{.docutils .literal .notranslate}, and `ClusterRoleBindings`{.docutils .literal .notranslate} resources: the identity and permissions used by cilium-agent to access the Kubernetes API server when Kubernetes RBAC is enabled.

-   A `Secret`{.docutils .literal .notranslate} resource: describes the credentials used to access the etcd kvstore, if required.

## Networking For Existing Pods[](#networking-for-existing-pods "Link to this heading")

In case pods were already running before the Cilium [DaemonSet](../../../glossary/#term-DaemonSet) was deployed, these pods will still be connected using the previous networking plugin according to the CNI configuration. A typical example for this is the `kube-dns`{.docutils .literal .notranslate} service which runs in the `kube-system`{.docutils .literal .notranslate} namespace by default.

A simple way to change networking for such existing pods is to rely on the fact that Kubernetes automatically restarts pods in a Deployment if they are deleted, so we can simply delete the original kube-dns pod and the replacement pod started immediately after will have networking managed by Cilium. In a production deployment, this step could be performed as a rolling update of kube-dns pods to avoid downtime of the DNS service.

``` {#codecell0}
$ kubectl --namespace kube-system delete pods -l k8s-app=kube-dns
pod "kube-dns-268032401-t57r2" deleted
```

Copy First Line Copy Commands Copy All

Running `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`pods`{.docutils .literal .notranslate} will show you that Kubernetes started a new set of `kube-dns`{.docutils .literal .notranslate} pods while at the same time terminating the old pods:

``` {#codecell1}
$ kubectl --namespace kube-system get pods
NAME                          READY     STATUS        RESTARTS   AGE
cilium-5074s                  1/1       Running       0          58m
kube-addon-manager-minikube   1/1       Running       0          59m
kube-dns-268032401-j0vml      3/3       Running       0          9s
kube-dns-268032401-t57r2      3/3       Terminating   0          57m
```

Copy First Line Copy Commands Copy All

## Default Ingress Allow from Local Host[](#default-ingress-allow-from-local-host "Link to this heading")

Kubernetes has functionality to indicate to users the current health of their applications via [Liveness Probes and Readiness Probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/). In order for `kubelet`{.docutils .literal .notranslate} to run these health checks for each pod, by default, Cilium will always allow all ingress traffic from the local host to each pod.
