---
{"title": "Endpoint CRD", "url": "https://docs.cilium.io/en/stable/network/kubernetes/ciliumendpoint/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Endpoint CRD[](#endpoint-crd "Link to this heading")

When managing pods in Kubernetes, Cilium will create a Custom Resource Definition (CRD) of Kind `CiliumEndpoint`{.docutils .literal .notranslate}. One `CiliumEndpoint`{.docutils .literal .notranslate} is created for each pod managed by Cilium, with the same name and in the same namespace. The `CiliumEndpoint`{.docutils .literal .notranslate} objects contain the same information as the json output of `cilium-dbg`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`endpoint`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`get`{.docutils .literal .notranslate} under the `.status`{.docutils .literal .notranslate} field, but can be fetched for all pods in the cluster. Adding the `-o`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`json`{.docutils .literal .notranslate} will export more information about each endpoint. This includes the endpoint's labels, security identity and the policy in effect on it.

For example:

``` {#codecell0}
$ kubectl get ciliumendpoints --all-namespaces
NAMESPACE     NAME                     AGE
default       app1-55d7944bdd-l7c8j    1h
default       app1-55d7944bdd-sn9xj    1h
default       app2                     1h
default       app3                     1h
kube-system   cilium-health-minikube   1h
kube-system   microscope               1h
```

Copy First Line Copy Commands Copy All

Note

Each cilium-agent pod will create a CiliumEndpoint to represent its own inter-agent health-check endpoint. These are not pods in Kubernetes and are in the `kube-system`{.docutils .literal .notranslate} namespace. They are named as `cilium-health-<node-name>`{.docutils .literal .notranslate}
