---
{"title": "Running Prometheus & Grafana", "url": "https://docs.cilium.io/en/stable/observability/grafana/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Running Prometheus & Grafana[](#running-prometheus-grafana "Link to this heading")

## Install Prometheus & Grafana[](#install-prometheus-grafana "Link to this heading")

This is an example deployment that includes Prometheus and Grafana in a single deployment.

Video

> You can see Cilium, Prometheus and Grafana in action together in the KubeCon + CloudNativeCon talk [Effortless Open Source Observability with Cilium, Prometheus and Grafana](https://www.youtube.com/watch?v=l3zY7wHUkBA).

The default installation contains:

-   **Grafana**: A visualization dashboard with Cilium Dashboard pre-loaded.

-   **Prometheus**: a time series database and monitoring system.

> ``` {#codecell0 .literal-block}
> $ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/addons/prometheus/monitoring-example.yaml
> namespace/cilium-monitoring created
> serviceaccount/prometheus-k8s created
> configmap/grafana-config created
> configmap/grafana-cilium-dashboard created
> configmap/grafana-cilium-operator-dashboard created
> configmap/grafana-hubble-dashboard created
> configmap/prometheus created
> clusterrole.rbac.authorization.k8s.io/prometheus unchanged
> clusterrolebinding.rbac.authorization.k8s.io/prometheus unchanged
> service/grafana created
> service/prometheus created
> deployment.apps/grafana created
> deployment.apps/prometheus created
> ```
>
> Copy First Line Copy All

This example deployment of Prometheus and Grafana will automatically scrape the Cilium and Hubble metrics. See the [Monitoring & Metrics](../metrics/#metrics) configuration guide on how to configure a custom Prometheus instance.

## Deploy Cilium and Hubble with metrics enabled[](#deploy-cilium-and-hubble-with-metrics-enabled "Link to this heading")

*Cilium*, *Hubble*, and *Cilium Operator* do not expose metrics by default. Enabling metrics for these services will open ports `9962`{.docutils .literal .notranslate}, `9965`{.docutils .literal .notranslate}, and `9963`{.docutils .literal .notranslate} respectively on all nodes of your cluster where these components are running.

The metrics for Cilium, Hubble, and Cilium Operator can all be enabled independently of each other with the following Helm values:

> -   `prometheus.enabled=true`{.docutils .literal .notranslate}: Enables metrics for `cilium-agent`{.docutils .literal .notranslate}.
>
> -   `operator.prometheus.enabled=true`{.docutils .literal .notranslate}: Enables metrics for `cilium-operator`{.docutils .literal .notranslate}.
>
> -   `hubble.metrics.enabled`{.docutils .literal .notranslate}: Enables the provided list of Hubble metrics. For Hubble metrics to work, Hubble itself needs to be enabled with `hubble.enabled=true`{.docutils .literal .notranslate}. See [Hubble exported metrics](../metrics/#hubble-exported-metrics) for the list of available Hubble metrics.

Refer to [Monitoring & Metrics](../metrics/#metrics) for more details about the individual metrics.

Setup Helm repository:

``` {#codecell1}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

Deploy Cilium via Helm as follows to enable all metrics:

``` {#codecell2 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled="{dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip\,source_namespace\,source_workload\,destination_ip\,destination_namespace\,destination_workload\,traffic_direction}"
```

Copy First Line Copy All

``` {#codecell3 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled="{dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip\,source_namespace\,source_workload\,destination_ip\,destination_namespace\,destination_workload\,traffic_direction}"
```

Copy First Line Copy All

### Configure Operator Prometheus TLS[](#configure-operator-prometheus-tls "Link to this heading")

To enable TLS on Operator Prometheus, you must first create a secret containing keys `tls.crt`{.docutils .literal .notranslate} and `tls.key`{.docutils .literal .notranslate}. Then, add the following flags to your Helm command to enable TLS:

``` {#codecell4}
--set operator.prometheus.tls.enabled=true                      # Enable TLS on Operator Prometheus
--set operator.prometheus.tls.server.existingSecret=secret-name # TLS secret name
```

Copy First Line Copy All

If you also want to enable mTLS, add key `ca.crt`{.docutils .literal .notranslate} to above secret. Then, add the following Helm flag to your list of options:

``` {#codecell5}
--set operator.prometheus.tls.server.mtls.enabled=true # Use ca.crt of secret to verify client certificates
```

Copy Line

Note

You can combine the above Helm options with any of the other installation guides.

## How to access Grafana[](#how-to-access-grafana "Link to this heading")

Expose the port on your local machine

``` {#codecell6}
kubectl -n cilium-monitoring port-forward service/grafana --address 0.0.0.0 --address :: 3000:3000
```

Copy Line

Access it via your browser: [http://localhost:3000](http://localhost:3000)

## How to access Prometheus[](#how-to-access-prometheus "Link to this heading")

Expose the port on your local machine

``` {#codecell7}
kubectl -n cilium-monitoring port-forward service/prometheus --address 0.0.0.0 --address :: 9090:9090
```

Copy Line

Access it via your browser: [http://localhost:9090](http://localhost:9090)

## Examples[](#examples "Link to this heading")

### Generic[](#generic "Link to this heading")

### Network[](#network "Link to this heading")

### Policy[](#policy "Link to this heading")

### Endpoints[](#endpoints "Link to this heading")

### Controllers[](#controllers "Link to this heading")

### Kubernetes[](#kubernetes "Link to this heading")

### Hubble General Processing[](#hubble-general-processing "Link to this heading")

### Hubble Networking[](#hubble-networking "Link to this heading")

Note

The `port-distribution`{.docutils .literal .notranslate} metric is disabled by default. Refer to [Monitoring & Metrics](../metrics/#metrics) for more details about the individual metrics.

### Hubble DNS[](#hubble-dns "Link to this heading")

### Hubble HTTP[](#hubble-http "Link to this heading")

### Hubble Network Policy[](#hubble-network-policy "Link to this heading")
