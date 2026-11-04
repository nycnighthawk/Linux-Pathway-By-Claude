---
{"title": "L7 Path Translation", "url": "https://docs.cilium.io/en/stable/network/servicemesh/envoy-custom-listener/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# L7 Path Translation[](#l7-path-translation "Link to this heading")

This example replicates the Prometheus metrics listener which is already available via the command line option `--proxy-prometheus-port`{.docutils .literal .notranslate}. So the point of this example is not to add new functionality, but to show how a feature that previously required Cilium Agent code changes can be implemented with the new Cilium Envoy Config CRD.

## Apply Example CRD[](#apply-example-crd "Link to this heading")

This example adds a new Envoy listener `envoy-prometheus-metrics-listener`{.docutils .literal .notranslate} on the standard Prometheus port (e.g. `9090`{.docutils .literal .notranslate}) to each Cilium node, translating the default Prometheus metrics path `/metrics`{.docutils .literal .notranslate} to Envoy's Prometheus metrics path `/stats/prometheus`{.docutils .literal .notranslate}.

Apply this Cilium Envoy Config CRD:

``` {#codecell0 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/envoy-prometheus-metrics-listener.yaml
```

Copy Line

This version of the `CiliumClusterwideEnvoyConfig`{.docutils .literal .notranslate} CRD is Cluster-scoped, (i.e., not namespaced), so the name needs to be unique in the cluster, unless you want to replace a CRD with a new one.

Note

Note that these Envoy resources are not validated by K8s at all, so any errors in the Envoy resources will only be seen by the Cilium Agent observing these CRDs. This means that `kubectl`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`apply`{.docutils .literal .notranslate} will report success, while parsing and/or installing the resources for the node-local Envoy instance may have failed. Currently the only way of verifying this is by observing Cilium Agent logs for errors and warnings. Additionally, Cilium Agent will print warning logs for any conflicting Envoy resources in the cluster.

Note

Note that Cilium Ingress Controller will configure required Envoy resource under the hood. Please check Cilium Agent logs if you are creating Envoy resources explicitly to make sure there is no conflict.

``` {#codecell1}
$ kubectl logs -n kube-system ds/cilium | grep -E "level=(error|warning)"
```

Copy Line

## Test the Listener Port[](#test-the-listener-port "Link to this heading")

Test that the new port is responding to the metrics requests:

``` {#codecell2}
$ curl http://<node-IP>:9090/metrics
```

Copy Line

Where `<node-IP>`{.docutils .literal .notranslate} is the IP address of one of your k8s cluster nodes.

## Clean-up[](#clean-up "Link to this heading")

Remove the prometheus listener with:

``` {#codecell3 .literal-block}
$ kubectl delete -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/servicemesh/envoy/envoy-prometheus-metrics-listener.yaml
```

Copy Line
