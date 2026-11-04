---
{"title": "Monitoring & Metrics", "url": "https://docs.cilium.io/en/stable/observability/metrics/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Monitoring & Metrics[](#monitoring-metrics "Link to this heading")

Cilium and Hubble can both be configured to serve [Prometheus](https://prometheus.io) metrics. Prometheus is a pluggable metrics collection and storage system and can act as a data source for [Grafana](https://grafana.com/), a metrics visualization frontend. Unlike some metrics collectors like statsd, Prometheus requires the collectors to pull metrics from each source.

Cilium and Hubble metrics can be enabled independently of each other.

## Cilium Metrics[](#cilium-metrics "Link to this heading")

Cilium metrics provide insights into the state of Cilium itself, namely of the `cilium-agent`{.docutils .literal .notranslate}, `cilium-envoy`{.docutils .literal .notranslate}, and `cilium-operator`{.docutils .literal .notranslate} processes. To run Cilium with Prometheus metrics enabled, deploy it with the `prometheus.enabled=true`{.docutils .literal .notranslate} Helm value set.

Cilium metrics are exported under the `cilium_`{.docutils .literal .notranslate} Prometheus namespace. Envoy metrics are exported under the `envoy_`{.docutils .literal .notranslate} Prometheus namespace, of which the Cilium-defined metrics are exported under the `envoy_cilium_`{.docutils .literal .notranslate} namespace. When running and collecting in Kubernetes they will be tagged with a pod name and namespace.

### Installation[](#installation "Link to this heading")

You can enable metrics for `cilium-agent`{.docutils .literal .notranslate} (including Envoy) with the Helm value `prometheus.enabled=true`{.docutils .literal .notranslate}. `cilium-operator`{.docutils .literal .notranslate} metrics are enabled by default, if you want to disable them, set Helm value `operator.prometheus.enabled=false`{.docutils .literal .notranslate}.

``` {#codecell0 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true
```

Copy First Line Copy All

``` {#codecell1 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true
```

Copy First Line Copy All

### Cilium Metrics Scraping[](#cilium-metrics-scraping "Link to this heading")

#### Prometheus Port Configuration[](#prometheus-port-configuration "Link to this heading")

The ports can be configured via `prometheus.port`{.docutils .literal .notranslate}, `envoy.prometheus.port`{.docutils .literal .notranslate}, or `operator.prometheus.port`{.docutils .literal .notranslate} respectively.

When metrics are enabled and ServiceMonitor is not enabled (`hubble.metrics.serviceMonitor.enabled:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate}), all Cilium components will have the following annotations. These annotations can be used to signal Prometheus whether to scrape metrics.

If ServiceMonitor is enabled (`hubble.metrics.serviceMonitor.enabled:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`true`{.docutils .literal .notranslate}), these annotations are omitted and Prometheus discovers metrics via the ServiceMonitor resource.

``` {#codecell2}
prometheus.io/scrape: true
prometheus.io/port: 9962
```

Copy First Line Copy All

To collect Envoy metrics the Cilium chart will create a Kubernetes headless service named `cilium-agent`{.docutils .literal .notranslate} with the `prometheus.io/scrape:'true'`{.docutils .literal .notranslate} annotation set:

``` {#codecell3}
prometheus.io/scrape: true
prometheus.io/port: 9964
```

Copy First Line Copy All

This additional headless service in addition to the other Cilium components is needed as each component can only have one Prometheus scrape and port annotation.

Prometheus will pick up the Cilium and Envoy metrics automatically if the following option is set in the `scrape_configs`{.docutils .literal .notranslate} section:

``` {#codecell4}
scrape_configs:
- job_name: 'kubernetes-pods'
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: ${1}:${2}
      target_label: __address__
```

Copy First Line Copy All

#### Prometheus Operator ServiceMonitor[](#prometheus-operator-servicemonitor "Link to this heading")

You can automatically create a [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) `ServiceMonitor`{.docutils .literal .notranslate} by setting `prometheus.serviceMonitor.enabled=true`{.docutils .literal .notranslate}, or `envoy.prometheus.serviceMonitor.enabled=true`{.docutils .literal .notranslate}, or `operator.prometheus.serviceMonitor.enabled=true`{.docutils .literal .notranslate} respectively.

## Hubble Metrics[](#hubble-metrics "Link to this heading")

While Cilium metrics allow you to monitor the state of Cilium itself, Hubble metrics on the other hand allow you to monitor the network behavior of your Cilium-managed Kubernetes pods with respect to connectivity and security.

Some of the metrics can also be configured with additional options. See the [Hubble exported metrics](#hubble-exported-metrics) section for the full list of available metrics and their options.

### Static or dynamic exporter[](#static-or-dynamic-exporter "Link to this heading")

Hubble Metrics can either be configured with a static or dynamic exporter.

The dynamic metrics exporter allows you to change defined metrics as needed without requiring an agent restart.

### Installation with a static metrics exporter[](#installation-with-a-static-metrics-exporter "Link to this heading")

To deploy Cilium with Hubble Metrics static exporter enabled, you need to enable Hubble with `hubble.enabled=true`{.docutils .literal .notranslate} and provide a set of Hubble metrics you want to enable via `hubble.metrics.enabled`{.docutils .literal .notranslate}.

``` {#codecell5 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled="{dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip\,source_namespace\,source_workload\,destination_ip\,destination_namespace\,destination_workload\,traffic_direction}"
```

Copy First Line Copy All

``` {#codecell6 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled="{dns,drop,tcp,flow,port-distribution,icmp,httpV2:exemplars=true;labelsContext=source_ip\,source_namespace\,source_workload\,destination_ip\,destination_namespace\,destination_workload\,traffic_direction}"
```

Copy First Line Copy All

### Installation with a dynamic metrics exporter[](#installation-with-a-dynamic-metrics-exporter "Link to this heading")

To deploy Cilium with Hubble dynamic metrics enabled, you need to enable Hubble with `hubble.enabled=true`{.docutils .literal .notranslate} and `hubble.metrics.dynamic.enabled=true`{.docutils .literal .notranslate}.

In this example, a `ConfigMap`{.docutils .literal .notranslate} with a set of metrics will be applied before enabling the exporter, but the desired set of metrics (together with the `ConfigMap`{.docutils .literal .notranslate}) can be created during installation.

See the [Helm Reference](../../helm-reference/#helm-reference) (keys with `hubble.metrics.dynamic.*`{.docutils .literal .notranslate})

``` {#codecell7}
apiVersion: v1
kind: ConfigMap
metadata:
  name: cilium-dynamic-metrics-config
  namespace: kube-system
data:
  dynamic-metrics.yaml: |
    metrics:
      - name: dns
      - contextOptions:
        - name: sourceContext
          values:
          - workload-name
          - reserved-identity
        - name: destinationContext
          values:
          - workload-name
          - reserved-identity
        name: flow
      - name: drop
      - name: tcp
      - contextOptions:
        - name: sourceContext
          values:
          - workload-name
          - reserved-identity
        name: icmp
      - contextOptions:
        - name: exemplars
          values:
          - true
        - name: labelsContext
          values:
          - source_ip
          - source_namespace
          - source_workload
          - destination_ip
          - destination_namespace
          - destination_workload
          - traffic_direction
        - name: sourceContext
          values:
          - workload-name
          - reserved-identity
        - name: destinationContext
          values:
          - workload-name
          - reserved-identity
        name: httpV2
      - contextOptions:
        - name: sourceContext
          values:
          - app
          - workload-name
          - pod
          - reserved-identity
        - name: destinationContext
          values:
          - app
          - workload-name
          - pod
          - dns
          - reserved-identity
        - name: labelsContext
          values:
          - source_namespace
          - destination_namespace
        excludeFilters:
        - destination_pod:
          - default/
        name: policy
```

Copy First Line Copy All

Deploy the [ConfigMap](../../glossary/#term-ConfigMap):

``` {#codecell8}
kubectl apply -f dynamic-metrics.yaml
```

Copy Line

``` {#codecell9 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled=[] \
   --set hubble.metrics.dynamic.enabled=true \
   --set hubble.metrics.dynamic.config.configMapName=cilium-dynamic-metrics-config \
   --set hubble.metrics.dynamic.config.createConfigMap=false
```

Copy First Line Copy All

``` {#codecell10 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set prometheus.enabled=true \
   --set operator.prometheus.enabled=true \
   --set hubble.enabled=true \
   --set hubble.metrics.enableOpenMetrics=true \
   --set hubble.metrics.enabled=[] \
   --set hubble.metrics.dynamic.enabled=true \
   --set hubble.metrics.dynamic.config.configMapName=cilium-dynamic-metrics-config \
   --set hubble.metrics.dynamic.config.createConfigMap=false
```

Copy First Line Copy All

### Hubble Metrics Scraping[](#hubble-metrics-scraping "Link to this heading")

#### Prometheus Port Configuration[](#id2 "Link to this heading")

The port of the Hubble metrics can be configured with the `hubble.metrics.port`{.docutils .literal .notranslate} Helm value.

For details on enabling Hubble metrics with TLS see the [Hubble Metrics TLS and Authentication](../hubble/configuration/tls/#hubble-configure-metrics-tls) section of the documentation.

Note

L7 metrics such as HTTP, are only emitted for pods that enable [Layer 7 Protocol Visibility](../visibility/#proxy-visibility).

When deployed with a non-empty `hubble.metrics.enabled`{.docutils .literal .notranslate} Helm value, the Cilium chart will create a Kubernetes headless service named `hubble-metrics`{.docutils .literal .notranslate} with the `prometheus.io/scrape:'true'`{.docutils .literal .notranslate} annotation set:

``` {#codecell11}
prometheus.io/scrape: true
prometheus.io/port: 9965
```

Copy First Line Copy All

Set the following options in the `scrape_configs`{.docutils .literal .notranslate} section of Prometheus to have it scrape all Hubble metrics from the endpoints automatically:

``` {#codecell12}
scrape_configs:
  - job_name: 'kubernetes-endpoints'
    scrape_interval: 30s
    kubernetes_sd_configs:
      - role: endpoints
    relabel_configs:
      - source_labels: [__meta_kubernetes_service_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__address__, __meta_kubernetes_service_annotation_prometheus_io_port]
        action: replace
        target_label: __address__
        regex: (.+)(?::\d+);(\d+)
        replacement: $1:$2
```

Copy First Line Copy All

#### Prometheus Operator ServiceMonitor[](#id3 "Link to this heading")

You can automatically create a [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) `ServiceMonitor`{.docutils .literal .notranslate} by setting `hubble.metrics.serviceMonitor.enabled=true`{.docutils .literal .notranslate}.

### OpenMetrics[](#openmetrics "Link to this heading")

Additionally, you can opt-in to [OpenMetrics](https://openmetrics.io) by setting `hubble.metrics.enableOpenMetrics=true`{.docutils .literal .notranslate}. Enabling OpenMetrics configures the Hubble metrics endpoint to support exporting metrics in OpenMetrics format when explicitly requested by clients.

Using OpenMetrics supports additional functionality such as Exemplars, which enables associating metrics with traces by embedding trace IDs into the exported metrics.

Prometheus needs to be configured to take advantage of OpenMetrics and will only scrape exemplars when the [exemplars storage feature is enabled](https://prometheus.io/docs/prometheus/latest/feature_flags/#exemplars-storage).

OpenMetrics imposes a few additional requirements on metrics names and labels, so this functionality is currently opt-in, though we believe all of the Hubble metrics conform to the OpenMetrics requirements.

## Cluster Mesh API Server Metrics[](#cluster-mesh-api-server-metrics "Link to this heading")

Cluster Mesh API Server metrics provide insights into the state of the `clustermesh-apiserver`{.docutils .literal .notranslate} process, the `kvstoremesh`{.docutils .literal .notranslate} process (if enabled), and the sidecar etcd instance. Cluster Mesh API Server metrics are exported under the `cilium_clustermesh_apiserver_`{.docutils .literal .notranslate} Prometheus namespace. KVStoreMesh metrics are exported under the `cilium_kvstoremesh_`{.docutils .literal .notranslate} Prometheus namespace. Etcd metrics are exported under the `etcd_`{.docutils .literal .notranslate} Prometheus namespace.

### Installation[](#id5 "Link to this heading")

You can enable the metrics for different Cluster Mesh API Server components by setting the following values:

-   clustermesh-apiserver: `clustermesh.apiserver.metrics.enabled=true`{.docutils .literal .notranslate}

-   kvstoremesh: `clustermesh.apiserver.metrics.kvstoremesh.enabled=true`{.docutils .literal .notranslate}

-   sidecar etcd instance: `clustermesh.apiserver.metrics.etcd.enabled=true`{.docutils .literal .notranslate}

``` {#codecell13 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set clustermesh.useAPIServer=true \
   --set clustermesh.apiserver.metrics.enabled=true \
   --set clustermesh.apiserver.metrics.kvstoremesh.enabled=true \
   --set clustermesh.apiserver.metrics.etcd.enabled=true
```

Copy First Line Copy All

``` {#codecell14 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set clustermesh.useAPIServer=true \
   --set clustermesh.apiserver.metrics.enabled=true \
   --set clustermesh.apiserver.metrics.kvstoremesh.enabled=true \
   --set clustermesh.apiserver.metrics.etcd.enabled=true
```

Copy First Line Copy All

You can figure the ports by way of `clustermesh.apiserver.metrics.port`{.docutils .literal .notranslate}, `clustermesh.apiserver.metrics.kvstoremesh.port`{.docutils .literal .notranslate} and `clustermesh.apiserver.metrics.etcd.port`{.docutils .literal .notranslate} respectively.

You can automatically create a [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) `ServiceMonitor`{.docutils .literal .notranslate} by setting `clustermesh.apiserver.metrics.serviceMonitor.enabled=true`{.docutils .literal .notranslate}.

## Example Prometheus & Grafana Deployment[](#example-prometheus-grafana-deployment "Link to this heading")

If you don't have an existing Prometheus and Grafana stack running, you can deploy a stack with:

``` {#codecell15 .literal-block}
kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/addons/prometheus/monitoring-example.yaml
```

Copy Line

It will run Prometheus and Grafana in the `cilium-monitoring`{.docutils .literal .notranslate} namespace. If you have either enabled Cilium or Hubble metrics, they will automatically be scraped by Prometheus. You can then expose Grafana to access it via your browser.

``` {#codecell16}
kubectl -n cilium-monitoring port-forward service/grafana --address 0.0.0.0 --address :: 3000:3000
```

Copy Line

Open your browser and access [http://localhost:3000/](http://localhost:3000/)

## Metrics Reference[](#metrics-reference "Link to this heading")

### cilium-agent[](#cilium-agent "Link to this heading")

#### Configuration[](#configuration "Link to this heading")

To expose any metrics, invoke `cilium-agent`{.docutils .literal .notranslate} with the `--prometheus-serve-addr`{.docutils .literal .notranslate} option. This option takes a `IP:Port`{.docutils .literal .notranslate} pair but passing an empty IP (e.g. `:9962`{.docutils .literal .notranslate}) will bind the server to all available interfaces (there is usually only one in a container).

To customize metrics, use `+/-`{.docutils .literal .notranslate} prefix to enable/disable specific metrics. For large clusters, consider disabling high-cardinality metrics like `cilium_node_health_connectivity_status`{.docutils .literal .notranslate} and `cilium_node_health_connectivity_latency_seconds`{.docutils .literal .notranslate}.

Use the `prometheus.metrics`{.docutils .literal .notranslate} value:

``` {#codecell17 .literal-block}
helm install cilium cilium/cilium 1.20.4 \
    --namespace kube-system \
    --set prometheus.enabled=true \
    --set prometheus.metrics="{-cilium_node_health_connectivity_status,-cilium_node_health_connectivity_latency_seconds}"
```

Copy First Line Copy All

Use the `--metrics`{.docutils .literal .notranslate} flag:

``` {#codecell18}
cilium-agent --prometheus-serve-addr=:9962 \
    --metrics="-cilium_node_health_connectivity_status -cilium_node_health_connectivity_latency_seconds"
```

Copy First Line Copy All

##### Feature Metrics[](#feature-metrics "Link to this heading")

Cilium Feature Metrics are exported under the `cilium_feature`{.docutils .literal .notranslate} Prometheus namespace.

The following tables categorize feature metrics into four groups:

-   **Advanced Connectivity and Load Balancing** ([adv_connect_and_lb](#cilium-feature-adv-connect-and-lb))

    This category includes features related to advanced networking and load balancing capabilities, such as Bandwidth Manager, BGP, Envoy Proxy, and Cluster Mesh.

-   **Control Plane** ([controlplane](#cilium-feature-controlplane))

    These metrics track control plane configurations, including identity allocation modes and IP address management (IPAM).

-   **Datapath** ([datapath](#cilium-feature-datapath))

    Metrics in this group monitor datapath configurations, such as Internet protocol modes, chaining modes, and network modes.

-   **Network Policies** ([network_policies](#cilium-feature-network-policies))

    This group encompasses metrics related to policy enforcement, including Cilium Network Policies, Host Firewall, DNS policies, and Mutual Auth.

For example, to check if the Bandwidth Manager is enabled on a Cilium agent, observe the metric `cilium_feature_adv_connect_and_lb_bandwidth_manager_enabled`{.docutils .literal .notranslate}. All metrics follow the format `cilium_feature`{.docutils .literal .notranslate} + group name + metric name. A value of `0`{.docutils .literal .notranslate} indicates that the feature is disabled, while `1`{.docutils .literal .notranslate} indicates it is enabled.

Note

For metrics of type "counter", the agent has processed the associated object (e.g., a network policy) but might not be actively enforcing it. These metrics serve to observe if the object has been received and processed, but not necessarily enforced by the agent.

##### `adv_connect_and_lb`{.docutils .literal .notranslate}[](#adv-connect-and-lb "Link to this heading")

  Name                                                                Labels                                                      Possible Label Values                                                Description                                         Type
  ------------------------------------------------------------------- ----------------------------------------------------------- -------------------------------------------------------------------- --------------------------------------------------- -------
  `bandwidth_manager_enabled`{.docutils .literal .notranslate}        *None*                                                      *None*                                                               Bandwidth Manager enabled on the agent              gauge
  `bgp_enabled`{.docutils .literal .notranslate}                      *None*                                                      *None*                                                               BGP enabled on the agent                            gauge
  `big_tcp_enabled`{.docutils .literal .notranslate}                  `address_family`{.docutils .literal .notranslate}           `"ipv4-ipv6-dual-stack"`{.docutils .literal .notranslate}            Big TCP enabled on the agent                        gauge
                                                                                                                                  `"ipv4-only"`{.docutils .literal .notranslate}                                                                           
                                                                                                                                  `"ipv6-only"`{.docutils .literal .notranslate}                                                                           
  `cilium_envoy_config_enabled`{.docutils .literal .notranslate}      *None*                                                      *None*                                                               Cilium Envoy Config enabled on the agent            gauge
  `cilium_node_config_enabled`{.docutils .literal .notranslate}       *None*                                                      *None*                                                               Cilium Node Config enabled on the agent             gauge
  `clustermesh_enabled`{.docutils .literal .notranslate}              `max_connected_clusters`{.docutils .literal .notranslate}   `"255"`{.docutils .literal .notranslate}                             Mode of the active Cluster Mesh connections/peers   gauge
                                                                                                                                  `"511"`{.docutils .literal .notranslate}                                                                                 
  `clustermesh_enabled`{.docutils .literal .notranslate}              `mode`{.docutils .literal .notranslate}                     `"clustermesh-apiserver"`{.docutils .literal .notranslate}                                                               
                                                                                                                                  `"clustermesh-apiserver_or_etcd"`{.docutils .literal .notranslate}                                                       
                                                                                                                                  `"etcd"`{.docutils .literal .notranslate}                                                                                
                                                                                                                                  `"kvstoremesh"`{.docutils .literal .notranslate}                                                                         
  `egress_gateway_enabled`{.docutils .literal .notranslate}           *None*                                                      *None*                                                               Egress Gateway enabled on the agent                 gauge
  `envoy_proxy_enabled`{.docutils .literal .notranslate}              `mode`{.docutils .literal .notranslate}                     `"embedded"`{.docutils .literal .notranslate}                        Envoy Proxy mode enabled on the agent               gauge
                                                                                                                                  `"standalone"`{.docutils .literal .notranslate}                                                                          
  `kube_proxy_replacement_enabled`{.docutils .literal .notranslate}   *None*                                                      *None*                                                               KubeProxyReplacement enabled on the agent           gauge
  `l2_lb_enabled`{.docutils .literal .notranslate}                    *None*                                                      *None*                                                               L2 LB announcement enabled on the agent             gauge
  `l2_pod_announcement_enabled`{.docutils .literal .notranslate}      *None*                                                      *None*                                                               L2 pod announcement enabled on the agent            gauge
  `node_port_configuration`{.docutils .literal .notranslate}          `acceleration`{.docutils .literal .notranslate}             `"best-effort"`{.docutils .literal .notranslate}                     Node Port configuration enabled on the agent        gauge
                                                                                                                                  `"disabled"`{.docutils .literal .notranslate}                                                                            
                                                                                                                                  `"native"`{.docutils .literal .notranslate}                                                                              
                                                                                                                                  `"testing-only"`{.docutils .literal .notranslate}                                                                        
  `node_port_configuration`{.docutils .literal .notranslate}          `algorithm`{.docutils .literal .notranslate}                `"maglev"`{.docutils .literal .notranslate}                                                                              
                                                                                                                                  `"random"`{.docutils .literal .notranslate}                                                                              
  `node_port_configuration`{.docutils .literal .notranslate}          `mode`{.docutils .literal .notranslate}                     `"dsr"`{.docutils .literal .notranslate}                                                                                 
                                                                                                                                  `"hybrid"`{.docutils .literal .notranslate}                                                                              
                                                                                                                                  `"snat"`{.docutils .literal .notranslate}                                                                                
  `sctp_enabled`{.docutils .literal .notranslate}                     *None*                                                      *None*                                                               SCTP enabled on the agent                           gauge
  `transparent_encryption`{.docutils .literal .notranslate}           `mode`{.docutils .literal .notranslate}                     `"ipsec"`{.docutils .literal .notranslate}                           Encryption mode enabled on the agent                gauge
                                                                                                                                  `"wireguard"`{.docutils .literal .notranslate}                                                                           
  `transparent_encryption`{.docutils .literal .notranslate}           `node2node_enabled`{.docutils .literal .notranslate}        `"false"`{.docutils .literal .notranslate}                                                                               
                                                                                                                                  `"true"`{.docutils .literal .notranslate}                                                                                
  `transparent_encryption`{.docutils .literal .notranslate}           `strict_mode_enabled`{.docutils .literal .notranslate}      `"false"`{.docutils .literal .notranslate}                                                                               
                                                                                                                                  `"true"`{.docutils .literal .notranslate}                                                                                
  `vtep_enabled`{.docutils .literal .notranslate}                     *None*                                                      *None*                                                               VTEP enabled on the agent                           gauge

##### `controlplane`{.docutils .literal .notranslate}[](#controlplane "Link to this heading")

  Name                                                                Labels                                    Possible Label Values                                          Description                                     Type
  ------------------------------------------------------------------- ----------------------------------------- -------------------------------------------------------------- ----------------------------------------------- -------
  `cilium_endpoint_slices_enabled`{.docutils .literal .notranslate}   *None*                                    *None*                                                         Cilium Endpoint Slices enabled on the agent     gauge
  `identity_allocation`{.docutils .literal .notranslate}              `mode`{.docutils .literal .notranslate}   `"crd"`{.docutils .literal .notranslate}                       Identity Allocation mode enabled on the agent   gauge
                                                                                                                `"doublewrite-readcrd"`{.docutils .literal .notranslate}                                                       
                                                                                                                `"doublewrite-readkvstore"`{.docutils .literal .notranslate}                                                   
                                                                                                                `"kvstore"`{.docutils .literal .notranslate}                                                                   
  `ipam`{.docutils .literal .notranslate}                             `mode`{.docutils .literal .notranslate}   `"alibabacloud"`{.docutils .literal .notranslate}              IPAM mode enabled on the agent                  gauge
                                                                                                                `"azure"`{.docutils .literal .notranslate}                                                                     
                                                                                                                `"cluster-pool"`{.docutils .literal .notranslate}                                                              
                                                                                                                `"crd"`{.docutils .literal .notranslate}                                                                       
                                                                                                                `"delegated-plugin"`{.docutils .literal .notranslate}                                                          
                                                                                                                `"eni"`{.docutils .literal .notranslate}                                                                       
                                                                                                                `"kubernetes"`{.docutils .literal .notranslate}                                                                
                                                                                                                `"multi-pool"`{.docutils .literal .notranslate}                                                                

##### `datapath`{.docutils .literal .notranslate}[](#datapath "Link to this heading")

  Name                                                         Labels                                                Possible Label Values                                       Description                                 Type
  ------------------------------------------------------------ ----------------------------------------------------- ----------------------------------------------------------- ------------------------------------------- -------
  `chaining_enabled`{.docutils .literal .notranslate}          `mode`{.docutils .literal .notranslate}               `"aws-cni"`{.docutils .literal .notranslate}                Chaining mode enabled on the agent          gauge
                                                                                                                     `"calico"`{.docutils .literal .notranslate}                                                             
                                                                                                                     `"flannel"`{.docutils .literal .notranslate}                                                            
                                                                                                                     `"generic-veth"`{.docutils .literal .notranslate}                                                       
                                                                                                                     `"none"`{.docutils .literal .notranslate}                                                               
                                                                                                                     `"portmap"`{.docutils .literal .notranslate}                                                            
  `config`{.docutils .literal .notranslate}                    `configured_mode`{.docutils .literal .notranslate}    `"auto"`{.docutils .literal .notranslate}                   Datapath config mode enabled on the agent   gauge
                                                                                                                     `"netkit"`{.docutils .literal .notranslate}                                                             
                                                                                                                     `"netkit-l2"`{.docutils .literal .notranslate}                                                          
                                                                                                                     `"veth"`{.docutils .literal .notranslate}                                                               
  `config`{.docutils .literal .notranslate}                    `operational_mode`{.docutils .literal .notranslate}   `"netkit"`{.docutils .literal .notranslate}                                                             
                                                                                                                     `"netkit-l2"`{.docutils .literal .notranslate}                                                          
                                                                                                                     `"veth"`{.docutils .literal .notranslate}                                                               
  `endpoint_routes_enabled`{.docutils .literal .notranslate}   *None*                                                *None*                                                      Endpoint Routes enabled in the datapath     gauge
  `internet_protocol`{.docutils .literal .notranslate}         `address_family`{.docutils .literal .notranslate}     `"ipv4-ipv6-dual-stack"`{.docutils .literal .notranslate}   IP mode enabled on the agent                gauge
                                                                                                                     `"ipv4-only"`{.docutils .literal .notranslate}                                                          
                                                                                                                     `"ipv6-only"`{.docutils .literal .notranslate}                                                          
  `network`{.docutils .literal .notranslate}                   `mode`{.docutils .literal .notranslate}               `"direct-routing"`{.docutils .literal .notranslate}         Network mode enabled on the agent           gauge
                                                                                                                     `"overlay-geneve"`{.docutils .literal .notranslate}                                                     
                                                                                                                     `"overlay-vxlan"`{.docutils .literal .notranslate}                                                      

##### `network_policies`{.docutils .literal .notranslate}[](#network-policies "Link to this heading")

  Name                                                                           Labels                                      Possible Label Values                         Description                                                                            Type
  ------------------------------------------------------------------------------ ------------------------------------------- --------------------------------------------- -------------------------------------------------------------------------------------- ---------
  `cidr_policies`{.docutils .literal .notranslate}                               `mode`{.docutils .literal .notranslate}     `"nodes"`{.docutils .literal .notranslate}    Mode to apply CIDR Policies to Nodes                                                   gauge
  `cilium_clusterwide_envoy_config_total`{.docutils .literal .notranslate}       `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Cilium Clusterwide Envoy Config have been ingested since the agent started             counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `cilium_clusterwide_network_policies_total`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Cilium Clusterwide Network Policies have been ingested since the agent started         counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `cilium_envoy_config_total`{.docutils .literal .notranslate}                   `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Cilium Envoy Config have been ingested since the agent started                         counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `cilium_network_policies_total`{.docutils .literal .notranslate}               `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Cilium Network Policies have been ingested since the agent started                     counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `deny_policies_total`{.docutils .literal .notranslate}                         `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Deny Policies have been ingested since the agent started                               counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `dns_policies_total`{.docutils .literal .notranslate}                          `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      DNS Policies have been ingested since the agent started                                counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `fqdn_policies_total`{.docutils .literal .notranslate}                         `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      ToFQDNs Policies have been ingested since the agent started                            counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `host_firewall_enabled`{.docutils .literal .notranslate}                       *None*                                      *None*                                        Host firewall enabled on the agent                                                     gauge
  `host_network_policies_total`{.docutils .literal .notranslate}                 `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Host Network Policies have been ingested since the agent started                       counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `http_header_matches_policies_total`{.docutils .literal .notranslate}          `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      HTTP HeaderMatches Policies have been ingested since the agent started                 counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `http_policies_total`{.docutils .literal .notranslate}                         `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      HTTP/GRPC Policies have been ingested since the agent started                          counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `ingress_cidr_group_policies_total`{.docutils .literal .notranslate}           `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Ingress CIDR Group Policies have been ingested since the agent started                 counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `internal_traffic_policy_services_total`{.docutils .literal .notranslate}      `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      K8s Services with Internal Traffic Policy have been ingested since the agent started   counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `l3_policies_total`{.docutils .literal .notranslate}                           `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Layer 3 and Layer 4 policies have been ingested since the agent started                counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `local_redirect_policies_total`{.docutils .literal .notranslate}               `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Local Redirect Policies have been ingested since the agent started                     counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `local_redirect_policy_enabled`{.docutils .literal .notranslate}               *None*                                      *None*                                        Local Redirect Policy enabled on the agent                                             gauge
  `mutual_auth_enabled`{.docutils .literal .notranslate}                         *None*                                      *None*                                        Mutual Auth enabled on the agent                                                       gauge
  `mutual_auth_policies_total`{.docutils .literal .notranslate}                  `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Mutual Auth Policies have been ingested since the agent started                        counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `non_defaultdeny_policies_enabled`{.docutils .literal .notranslate}            *None*                                      *None*                                        Non DefaultDeny Policies is enabled in the agent                                       gauge
  `non_defaultdeny_policies_total`{.docutils .literal .notranslate}              `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      Non DefaultDeny Policies have been ingested since the agent started                    counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `sni_allow_list_policies_total`{.docutils .literal .notranslate}               `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      SNI Allow List Policies have been ingested since the agent started                     counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          
  `tls_inspection_policies_total`{.docutils .literal .notranslate}               `action`{.docutils .literal .notranslate}   `"add"`{.docutils .literal .notranslate}      TLS Inspection Policies have been ingested since the agent started                     counter
                                                                                                                             `"delete"`{.docutils .literal .notranslate}                                                                                          

#### Exported Metrics[](#exported-metrics "Link to this heading")

##### Endpoint[](#endpoint "Link to this heading")

  Name                                                                          Labels                                                                                                                            Default   Description
  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------- --------- ----------------------------------------------------------------------------------------------
  `endpoint`{.docutils .literal .notranslate}                                                                                                                                                                     Enabled   Number of endpoints managed by this agent
  `endpoint_component_status`{.docutils .literal .notranslate}                  `type`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}                                                Enabled   Number of endpoints tagged by different endpoint components type and their status
  `endpoint_restoration_endpoints`{.docutils .literal .notranslate}             `phase`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}                                              Enabled   Number of restored endpoints labeled by phase and outcome
  `endpoint_restoration_duration_seconds`{.docutils .literal .notranslate}      `phase`{.docutils .literal .notranslate}                                                                                          Enabled   Duration of restoration phases in seconds
  `endpoint_regenerations_total`{.docutils .literal .notranslate}               `reason`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `error`{.docutils .literal .notranslate}   Enabled   Count of all endpoint regenerations that have completed, tagged by reason, outcome and error
  `endpoint_regeneration_time_stats_seconds`{.docutils .literal .notranslate}   `scope`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}                                               Enabled   Endpoint regeneration time stats
  `endpoint_state`{.docutils .literal .notranslate}                             `endpoint_state`{.docutils .literal .notranslate}                                                                                 Enabled   Count of all endpoints

##### Services[](#services "Link to this heading")

  Name                                                              Labels                                      Default   Description
  ----------------------------------------------------------------- ------------------------------------------- --------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `services_events_total`{.docutils .literal .notranslate}          `action`{.docutils .literal .notranslate}   Enabled   Number of services events labeled by action type
  `service_implementation_delay`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}   Enabled   Duration in seconds to propagate the data plane programming of a service, its network and endpoints from the time the service or the service pod was changed excluding the event queue latency

##### Cluster health[](#cluster-health "Link to this heading")

  Name                                                              Labels   Default   Description
  ----------------------------------------------------------------- -------- --------- ---------------------------------------------------
  `unreachable_nodes`{.docutils .literal .notranslate}                       Enabled   Number of nodes that cannot be reached
  `unreachable_health_endpoints`{.docutils .literal .notranslate}            Enabled   Number of health endpoints that cannot be reached

##### Node Connectivity[](#node-connectivity "Link to this heading")

  Name                                                                          Labels                                                                                                                                  Default   Description
  ----------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- --------- ------------------------------------------------------------------------------------------------------------------------------------------
  `node_health_connectivity_status`{.docutils .literal .notranslate}            `type`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}                                                      Enabled   Number of endpoints with last observed status of both ICMP and HTTP connectivity between the current Cilium agent and other Cilium nodes
  `node_health_connectivity_latency_seconds`{.docutils .literal .notranslate}   `type`{.docutils .literal .notranslate}, `address_type`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}   Enabled   Histogram of the last observed latency between the current Cilium agent and other Cilium nodes in seconds

##### Clustermesh[](#clustermesh "Link to this heading")

  Name                                                                              Labels                                              Default   Description
  --------------------------------------------------------------------------------- --------------------------------------------------- --------- ---------------------------------------------------------------------
  `clustermesh_remote_cluster_services`{.docutils .literal .notranslate}            `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of services per remote cluster
  `clustermesh_remote_cluster_endpoint_slices`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of endpoint slices per remote cluster
  `clustermesh_remote_cluster_endpoints`{.docutils .literal .notranslate}           `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of endpoints per remote cluster
  `clustermesh_remote_cluster_nodes`{.docutils .literal .notranslate}               `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of nodes per remote cluster
  `clustermesh_remote_clusters`{.docutils .literal .notranslate}                                                                        Enabled   The total number of remote clusters meshed with the local cluster
  `clustermesh_remote_cluster_failures`{.docutils .literal .notranslate}            `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of failures related to the remote cluster
  `clustermesh_remote_cluster_last_failure_ts`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   Enabled   The timestamp of the last failure of the remote cluster
  `clustermesh_remote_cluster_readiness_status`{.docutils .literal .notranslate}    `target_cluster`{.docutils .literal .notranslate}   Enabled   The readiness status of the remote cluster
  `clustermesh_remote_cluster_cache_revocations`{.docutils .literal .notranslate}   `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of cache revocations related to the remote cluster

##### Datapath[](#id6 "Link to this heading")

  Name                                                                           Labels                                                                                                                              Default   Description
  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------- --------- --------------------------------------------------------------------------------------------------------------
  `datapath_conntrack_dump_resets_total`{.docutils .literal .notranslate}        `area`{.docutils .literal .notranslate}, `name`{.docutils .literal .notranslate}, `family`{.docutils .literal .notranslate}         Enabled   Number of conntrack dump resets. Happens when a BPF entry gets removed while dumping the map is in progress.
  `datapath_conntrack_gc_runs_total`{.docutils .literal .notranslate}            `family`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}   Enabled   Number of times that the conntrack garbage collector process was run
  `datapath_conntrack_gc_key_fallbacks_total`{.docutils .literal .notranslate}   `family`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}                                              Enabled   Number of times a key fallback was needed when iterating over the BPF map
  `datapath_conntrack_gc_entries`{.docutils .literal .notranslate}               `family`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}   Enabled   The number of alive and deleted conntrack entries at the end of a garbage collector run
  `datapath_conntrack_gc_duration_seconds`{.docutils .literal .notranslate}      `family`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}   Enabled   Duration in seconds of the garbage collector process

##### IPsec[](#ipsec "Link to this heading")

  Name                                                     Labels                                                                              Default   Description
  -------------------------------------------------------- ----------------------------------------------------------------------------------- --------- -----------------------------
  `ipsec_xfrm_error`{.docutils .literal .notranslate}      `error`{.docutils .literal .notranslate}, `type`{.docutils .literal .notranslate}   Enabled   Total number of xfrm errors
  `ipsec_keys`{.docutils .literal .notranslate}                                                                                                Enabled   Number of keys in use
  `ipsec_xfrm_states`{.docutils .literal .notranslate}     `direction`{.docutils .literal .notranslate}                                        Enabled   Number of XFRM states
  `ipsec_xfrm_policies`{.docutils .literal .notranslate}   `direction`{.docutils .literal .notranslate}                                        Enabled   Number of XFRM policies

##### eBPF[](#ebpf "Link to this heading")

  Name                                                                    Labels                                                                                                                                  Default    Description
  ----------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------- ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `bpf_syscall_duration_seconds`{.docutils .literal .notranslate}         `operation`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}                                                Disabled   Duration of eBPF system call performed
  `bpf_map_ops_total`{.docutils .literal .notranslate}                    `map_name`{.docutils .literal .notranslate}, `operation`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}   Enabled    Number of eBPF map operations performed.
  `bpf_map_pressure`{.docutils .literal .notranslate}                     `map_name`{.docutils .literal .notranslate}                                                                                             Enabled    Map pressure is defined as a ratio of the required map size compared to its configured size. Values \< 1.0 indicate the map's utilization, while values \>= 1.0 indicate that the map is full. Policy map pressure metrics are emitted only when map utilization exceeds the threshold set by `policyMapPressureMetricsThreshold`{.docutils .literal .notranslate} helm value, which defaults to 0.1 (10% full).
  `bpf_map_capacity`{.docutils .literal .notranslate}                     `map_group`{.docutils .literal .notranslate}                                                                                            Enabled    Maximum size of eBPF maps by group of maps (type of map that have the same max capacity size). Map types with size of 65536 are not emitted, missing map types can be assumed to be 65536.
  `bpf_maps_virtual_memory_max_bytes`{.docutils .literal .notranslate}                                                                                                                                            Enabled    Max memory used by eBPF maps installed in the system
  `bpf_progs_virtual_memory_max_bytes`{.docutils .literal .notranslate}                                                                                                                                           Enabled    Max memory used by eBPF programs installed in the system
  `bpf_ratelimit_dropped_total`{.docutils .literal .notranslate}          `usage`{.docutils .literal .notranslate}                                                                                                Enabled    Total drops resulting from BPF ratelimiter, tagged by source of drop

Both `bpf_maps_virtual_memory_max_bytes`{.docutils .literal .notranslate} and `bpf_progs_virtual_memory_max_bytes`{.docutils .literal .notranslate} are currently reporting the system-wide memory usage of eBPF that is directly and not directly managed by Cilium. This might change in the future and only report the eBPF memory usage directly managed by Cilium.

##### Drops/Forwards (L3/L4)[](#drops-forwards-l3-l4 "Link to this heading")

  Name                                                         Labels                                                                                    Default   Description
  ------------------------------------------------------------ ----------------------------------------------------------------------------------------- --------- ---------------------------------------------------------------------------------------
  `drop_count_total`{.docutils .literal .notranslate}          `reason`{.docutils .literal .notranslate}, `direction`{.docutils .literal .notranslate}   Enabled   Total dropped packets
  `drop_bytes_total`{.docutils .literal .notranslate}          `reason`{.docutils .literal .notranslate}, `direction`{.docutils .literal .notranslate}   Enabled   Total dropped bytes
  `forward_count_total`{.docutils .literal .notranslate}       `direction`{.docutils .literal .notranslate}                                              Enabled   Total forwarded packets
  `forward_bytes_total`{.docutils .literal .notranslate}       `direction`{.docutils .literal .notranslate}                                              Enabled   Total forwarded bytes
  `mtu_error_message_total`{.docutils .literal .notranslate}   `direction`{.docutils .literal .notranslate}                                              Enabled   Total number of icmp fragmentation-needed or ICMPv6 packet-too-big messages processed
  `fragmented_count_total`{.docutils .literal .notranslate}    `direction`{.docutils .literal .notranslate}                                              Enabled   Total number of fragmented packets processed

##### Policy[](#policy "Link to this heading")

  Name                                                                    Labels                                                                                                                                Default   Description
  ----------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------- --------- -------------------------------------------------------------------------------------------------------------------------
  `policy`{.docutils .literal .notranslate}                                                                                                                                                                     Enabled   Number of policies currently loaded
  `policy_max_revision`{.docutils .literal .notranslate}                                                                                                                                                        Enabled   Highest policy revision number in the agent
  `policy_change_total`{.docutils .literal .notranslate}                  `source`{.docutils .literal .notranslate}, `operation`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}   Enabled   Number of policy changes by source, operation and outcome
  `policy_endpoint_enforcement_status`{.docutils .literal .notranslate}   `enforcement`{.docutils .literal .notranslate}                                                                                        Enabled   Number of endpoints labeled by policy enforcement status
  `policy_implementation_delay`{.docutils .literal .notranslate}          `source`{.docutils .literal .notranslate}                                                                                             Enabled   Time in seconds between a policy change and it being fully deployed into the datapath, labeled by the policy's source
  `policy_selector_match_count_max`{.docutils .literal .notranslate}      `class`{.docutils .literal .notranslate}                                                                                              Enabled   The maximum number of identities selected by a network policy selector
  `policy_incremental_update_duration`{.docutils .literal .notranslate}   `scope`{.docutils .literal .notranslate}                                                                                              Enabled   The time taken for newly learned identities to be added to the policy system, including BPF policy maps and L7 proxies.
  `policy_missing_proxy_redirects`{.docutils .literal .notranslate}                                                                                                                                             Enabled   Total number of proxy redirects missing in endpoint policies

##### Policy L7 (HTTP/FQDN)[](#policy-l7-http-fqdn "Link to this heading")

  Name                                                                     Labels                                                                                                                               Default    Description
  ------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------ ---------- -----------------------------------------------------------------
  `proxy_redirects`{.docutils .literal .notranslate}                       `protocol_l7`{.docutils .literal .notranslate}                                                                                       Enabled    Number of redirects installed for endpoints
  `proxy_upstream_reply_seconds`{.docutils .literal .notranslate}          `error`{.docutils .literal .notranslate}, `protocol_l7`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}   Enabled    Seconds waited for upstream server to reply to a request
  `proxy_datapath_update_timeout_total`{.docutils .literal .notranslate}                                                                                                                                        Disabled   Number of total datapath update timeouts due to FQDN IP updates
  `policy_l7_total`{.docutils .literal .notranslate}                       `rule`{.docutils .literal .notranslate}, `proxy_type`{.docutils .literal .notranslate}                                               Enabled    Number of total L7 requests/responses

##### Identity[](#identity "Link to this heading")

  Name                                                                        Labels                                                                              Default    Description
  --------------------------------------------------------------------------- ----------------------------------------------------------------------------------- ---------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `identity`{.docutils .literal .notranslate}                                 `type`{.docutils .literal .notranslate}                                             Enabled    Number of identities currently allocated
  `identity_label_sources`{.docutils .literal .notranslate}                   `source`{.docutils .literal .notranslate}                                           Enabled    Number of identities which contain at least one label from the given label source
  `ipcache_errors_total`{.docutils .literal .notranslate}                     `type`{.docutils .literal .notranslate}, `error`{.docutils .literal .notranslate}   Enabled    Number of errors interacting with the ipcache
  `ipcache_events_total`{.docutils .literal .notranslate}                     `type`{.docutils .literal .notranslate}                                             Disabled   Number of events interacting with the ipcache
  `identity_updater_timer_duration`{.docutils .literal .notranslate}          `name`{.docutils .literal .notranslate}                                             Enabled    Seconds required to execute periodic policy processes. `name="id-alloc-update-policy-maps"`{.docutils .literal .notranslate} is the time taken to apply incremental updates to the BPF policy maps.
  `identity_updater_timer_trigger_latency`{.docutils .literal .notranslate}   `name`{.docutils .literal .notranslate}                                             Enabled    Seconds spent waiting for a previous process to finish before starting the next round. `name="id-alloc-update-policy-maps"`{.docutils .literal .notranslate} is the time waiting before applying incremental updates to the BPF policy maps.
  `identity_updater_timer_trigger_folds`{.docutils .literal .notranslate}     `name`{.docutils .literal .notranslate}                                             Enabled    Number of timer triggers that were coalesced in to one execution. `name="id-alloc-update-policy-maps"`{.docutils .literal .notranslate} applies the incremental updates to the BPF policy maps.

##### Events external to Cilium[](#events-external-to-cilium "Link to this heading")

  Name                                                       Labels                                                                                                                           Default    Description
  ---------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------- ---------- -----------------------------------------------------------------------------------------------------------------------------------------
  `event_ts`{.docutils .literal .notranslate}                `source`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}   Enabled    Last timestamp when Cilium received an event from a control plane source, per resource and per action
  `k8s_event_lag_seconds`{.docutils .literal .notranslate}   `source`{.docutils .literal .notranslate}                                                                                        Disabled   Lag for Kubernetes events - computed value between receiving a CNI ADD event from kubelet and a Pod event received from kube-api-server

##### Controllers[](#controllers "Link to this heading")

  Name                                                                   Labels                                                                                     Default   Description
  ---------------------------------------------------------------------- ------------------------------------------------------------------------------------------ --------- -------------------------------------------------------------------------------------
  `controllers_runs_total`{.docutils .literal .notranslate}              `status`{.docutils .literal .notranslate}                                                  Enabled   Number of times that a controller process was run
  `controllers_runs_duration_seconds`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}                                                  Enabled   Duration in seconds of the controller process
  `controllers_group_runs_total`{.docutils .literal .notranslate}        `status`{.docutils .literal .notranslate}, `group_name`{.docutils .literal .notranslate}   Enabled   Number of times that a controller process was run, labeled by controller group name
  `controllers_failing`{.docutils .literal .notranslate}                                                                                                            Enabled   Number of failing controllers

The `controllers_group_runs_total`{.docutils .literal .notranslate} metric reports the success and failure count of each controller within the system, labeled by controller group name and completion status. Due to the large number of controllers, enabling this metric is on a per-controller basis. This is configured using an allow-list which is passed as the `controller-group-metrics`{.docutils .literal .notranslate} configuration flag, or the `prometheus.controllerGroupMetrics`{.docutils .literal .notranslate} helm value. The current recommended default set of group names can be found in the values file of the Cilium Helm chart. The special names "all" and "none" are supported.

##### SubProcess[](#subprocess "Link to this heading")

  Name                                                        Labels                                         Default   Description
  ----------------------------------------------------------- ---------------------------------------------- --------- ------------------------------------------------------
  `subprocess_start_total`{.docutils .literal .notranslate}   `subsystem`{.docutils .literal .notranslate}   Enabled   Number of times that Cilium has started a subprocess

##### Kubernetes[](#kubernetes "Link to this heading")

  Name                                                                        Labels                                                                                                                                                                    Default   Description
  --------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- ----------------------------------------------------------------
  `kubernetes_resource_sync_duration`{.docutils .literal .notranslate}        `scope`{.docutils .literal .notranslate}                                                                                                                                  Enabled   Duration in seconds of a specific Kubernetes resource sync
  `kubernetes_events_received_total`{.docutils .literal .notranslate}         `scope`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}, `valid`{.docutils .literal .notranslate}, `equal`{.docutils .literal .notranslate}   Enabled   Number of Kubernetes events received
  `kubernetes_events_total`{.docutils .literal .notranslate}                  `scope`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}                                            Enabled   Number of Kubernetes events processed
  `k8s_terminating_endpoints_events_total`{.docutils .literal .notranslate}                                                                                                                                                                             Enabled   Number of terminating endpoint events received from Kubernetes

##### Kubernetes Rest Client[](#kubernetes-rest-client "Link to this heading")

  Name                                                                          Labels                                                                                                                               Default   Description
  ----------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------ --------- ------------------------------------------------------------------------------------
  `k8s_client_api_latency_time_seconds`{.docutils .literal .notranslate}        `path`{.docutils .literal .notranslate}, `method`{.docutils .literal .notranslate}                                                   Enabled   Duration of processed API calls labeled by path and method
  `k8s_client_rate_limiter_duration_seconds`{.docutils .literal .notranslate}                                                                                                                                        Enabled   Kubernetes client rate limiter latency in seconds.
  `k8s_client_api_calls_total`{.docutils .literal .notranslate}                 `host`{.docutils .literal .notranslate}, `method`{.docutils .literal .notranslate}, `return_code`{.docutils .literal .notranslate}   Enabled   Number of API calls made to kube-apiserver labeled by host, method and return code

##### Kubernetes workqueue[](#kubernetes-workqueue "Link to this heading")

  Name                                                                                 Labels                                    Default   Description
  ------------------------------------------------------------------------------------ ----------------------------------------- --------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `k8s_workqueue_depth`{.docutils .literal .notranslate}                               `name`{.docutils .literal .notranslate}   Enabled   Current depth of workqueue
  `k8s_workqueue_adds_total`{.docutils .literal .notranslate}                          `name`{.docutils .literal .notranslate}   Enabled   Total number of adds handled by workqueue
  `k8s_workqueue_queue_duration_seconds`{.docutils .literal .notranslate}              `name`{.docutils .literal .notranslate}   Enabled   Duration in seconds an item stays in workqueue prior to request
  `k8s_workqueue_work_duration_seconds`{.docutils .literal .notranslate}               `name`{.docutils .literal .notranslate}   Enabled   Duration in seconds to process an item from workqueue
  `k8s_workqueue_unfinished_work_seconds`{.docutils .literal .notranslate}             `name`{.docutils .literal .notranslate}   Enabled   Duration in seconds of work in progress that hasn't been observed by work_duration. Large values indicate stuck threads. You can deduce the number of stuck threads by observing the rate at which this value increases.
  `k8s_workqueue_longest_running_processor_seconds`{.docutils .literal .notranslate}   `name`{.docutils .literal .notranslate}   Enabled   Duration in seconds of the longest running processor for workqueue
  `k8s_workqueue_retries_total`{.docutils .literal .notranslate}                       `name`{.docutils .literal .notranslate}   Enabled   Total number of retries handled by workqueue

##### IPAM[](#ipam "Link to this heading")

  Name                                                   Labels                                                                                 Default   Description
  ------------------------------------------------------ -------------------------------------------------------------------------------------- --------- ---------------------------------------------------------------------------
  `ipam_capacity`{.docutils .literal .notranslate}       `family`{.docutils .literal .notranslate}, `cidr`{.docutils .literal .notranslate}     Enabled   Total number of IPs in the IPAM pool labeled by family
  `ipam_events_total`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}, `family`{.docutils .literal .notranslate}   Enabled   Number of IPAM events received labeled by action and datapath family type
  `ip_addresses`{.docutils .literal .notranslate}        `family`{.docutils .literal .notranslate}                                              Enabled   Number of allocated IP addresses

##### KVstore[](#kvstore "Link to this heading")

  Name                                                                     Labels                                                                                                                                                                     Default   Description
  ------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- -----------------------------------------------------------------------
  `kvstore_operations_duration_seconds`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}, `kind`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}   Enabled   Duration of kvstore operation
  `kvstore_events_queue_seconds`{.docutils .literal .notranslate}          `action`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}                                                                                        Enabled   Seconds waited before a received event was queued
  `kvstore_quorum_errors_total`{.docutils .literal .notranslate}           `error`{.docutils .literal .notranslate}                                                                                                                                   Enabled   Number of quorum errors
  `kvstore_sync_errors_total`{.docutils .literal .notranslate}             `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Enabled   Number of times synchronization to the kvstore failed
  `kvstore_sync_queue_size`{.docutils .literal .notranslate}               `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Enabled   Number of elements queued for synchronization in the kvstore
  `kvstore_initial_sync_completed`{.docutils .literal .notranslate}        `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}                                     Enabled   Whether the initial synchronization from/to the kvstore has completed

##### Agent[](#agent "Link to this heading")

  Name                                                          Labels                                                                                                                               Default   Description
  ------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------ --------- ------------------------------------------------------------------------------------------------------------------------
  `api_process_time_seconds`{.docutils .literal .notranslate}   `path`{.docutils .literal .notranslate}, `method`{.docutils .literal .notranslate}, `return_code`{.docutils .literal .notranslate}   Enabled   Processing time of all the API calls made to the cilium-agent, labeled by API method, API path and returned HTTP code.

##### FQDN[](#fqdn "Link to this heading")

  Name                                                               Labels                                        Default    Description
  ------------------------------------------------------------------ --------------------------------------------- ---------- --------------------------------------------------------------------------------------------------------------------------------------------
  `fqdn_gc_deletions_total`{.docutils .literal .notranslate}                                                       Enabled    Number of FQDNs that have been cleaned on FQDN garbage collector job
  `fqdn_active_names`{.docutils .literal .notranslate}               `endpoint`{.docutils .literal .notranslate}   Disabled   Number of domains inside the DNS cache that have not expired (by TTL), per endpoint
  `fqdn_active_ips`{.docutils .literal .notranslate}                 `endpoint`{.docutils .literal .notranslate}   Disabled   Number of IPs inside the DNS cache associated with a domain that has not expired (by TTL), per endpoint
  `fqdn_alive_zombie_connections`{.docutils .literal .notranslate}   `endpoint`{.docutils .literal .notranslate}   Disabled   Number of IPs associated with domains that have expired (by TTL) yet still associated with an active connection (aka zombie), per endpoint
  `fqdn_selectors`{.docutils .literal .notranslate}                                                                Enabled    Number of registered ToFQDN selectors

##### Hive[](#hive "Link to this heading")

  Name                                                        Labels   Default    Description
  ----------------------------------------------------------- -------- ---------- --------------------------------------------------------------------------------------------------------------------------------
  `hive_start_duration`{.docutils .literal .notranslate}               Enabled    Duration of the hive.Start method
  `hive_stop_duration`{.docutils .literal .notranslate}                Disabled   Duration of the hive.Stop method. Not reported when metrics are handled by a hive (common in cilium-agent and cilium-operator)
  `hive_populate_duration`{.docutils .literal .notranslate}            Enabled    Duration of the hive.Populate method

##### Jobs[](#jobs "Link to this heading")

  Name                                                                              Labels                                                                                      Default   Description
  --------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------- --------- --------------------------------------------
  `hive_jobs_runs_total`{.docutils .literal .notranslate}                           `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Total number of jobs runs
  `hive_jobs_runs_failed`{.docutils .literal .notranslate}                          `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Number of jobs runs that returned an error
  `hive_jobs_oneshot_last_run_duration_seconds`{.docutils .literal .notranslate}    `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Duration of last one shot job run
  `hive_jobs_observer_last_run_duration_seconds`{.docutils .literal .notranslate}   `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Duration of last observer job run
  `hive_jobs_observer_run_duration_seconds`{.docutils .literal .notranslate}        `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Histogram of observer job run duration
  `hive_jobs_timer_last_run_duration_seconds`{.docutils .literal .notranslate}      `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Duration of last timer job run
  `hive_jobs_timer_run_duration_seconds`{.docutils .literal .notranslate}           `module_id`{.docutils .literal .notranslate}, `job_name`{.docutils .literal .notranslate}   Enabled   Histogram of timer job run duration

##### API Rate Limiting[](#api-rate-limiting "Link to this heading")

  Name                                                                           Labels                                                                                                                                    Default    Description
  ------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------------------------------------------------------
  `api_limiter_adjustment_factor`{.docutils .literal .notranslate}               `api_call`{.docutils .literal .notranslate}                                                                                               Enabled    Most recent adjustment factor for automatic adjustment
  `api_limiter_processed_requests_total`{.docutils .literal .notranslate}        `api_call`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `return_code`{.docutils .literal .notranslate}   Enabled    Total number of API requests processed
  `api_limiter_processing_duration_seconds`{.docutils .literal .notranslate}     `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Enabled    Mean and estimated processing duration in seconds
  `api_limiter_rate_limit`{.docutils .literal .notranslate}                      `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Enabled    Current rate limiting configuration (limit and burst)
  `api_limiter_requests_in_flight`{.docutils .literal .notranslate}              `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Enabled    Current and maximum allowed number of requests in flight
  `api_limiter_wait_duration_seconds`{.docutils .literal .notranslate}           `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Enabled    Mean, min, and max wait duration
  `api_limiter_wait_history_duration_seconds`{.docutils .literal .notranslate}   `api_call`{.docutils .literal .notranslate}                                                                                               Disabled   Histogram of wait duration per API call processed

##### BGP Control Plane[](#bgp-control-plane "Link to this heading")

  Name                                                                                  Labels                                                                                                                                                                                                                                                                          Default   Description
  ------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- --------------------------------------------------------------------
  `bgp_control_plane_session_state`{.docutils .literal .notranslate}                    `instance_name`{.docutils .literal .notranslate}, `local_asn`{.docutils .literal .notranslate}, `neighbor`{.docutils .literal .notranslate}, `neighbor_asn`{.docutils .literal .notranslate}                                                                                    Enabled   Current state of the BGP session with the peer, Up = 1 or Down = 0
  `bgp_control_plane_advertised_routes`{.docutils .literal .notranslate}                `instance_name`{.docutils .literal .notranslate}, `local_asn`{.docutils .literal .notranslate}, `neighbor`{.docutils .literal .notranslate}, `neighbor_asn`{.docutils .literal .notranslate}, `afi`{.docutils .literal .notranslate}, `safi`{.docutils .literal .notranslate}   Enabled   Number of routes advertised to the peer
  `bgp_control_plane_received_routes`{.docutils .literal .notranslate}                  `instance_name`{.docutils .literal .notranslate}, `local_asn`{.docutils .literal .notranslate}, `neighbor`{.docutils .literal .notranslate}, `neighbor_asn`{.docutils .literal .notranslate}, `afi`{.docutils .literal .notranslate}, `safi`{.docutils .literal .notranslate}   Enabled   Number of routes received from the peer
  `bgp_control_plane_reconcile_errors_total`{.docutils .literal .notranslate}           `instance_name`{.docutils .literal .notranslate}                                                                                                                                                                                                                                Enabled   Number of reconciliation runs that returned an error
  `bgp_control_plane_reconcile_run_duration_seconds`{.docutils .literal .notranslate}   `instance_name`{.docutils .literal .notranslate}                                                                                                                                                                                                                                Enabled   Histogram of reconciliation run duration

All metrics are enabled only when the BGP Control Plane is enabled.

### cilium-operator[](#cilium-operator "Link to this heading")

#### Configuration[](#id7 "Link to this heading")

`cilium-operator`{.docutils .literal .notranslate} can be configured to serve metrics by running with the option `--enable-metrics`{.docutils .literal .notranslate}. By default, the operator will expose metrics on port 9963, the port can be changed with the option `--operator-prometheus-serve-addr`{.docutils .literal .notranslate}.

##### Feature Metrics[](#id8 "Link to this heading")

Cilium Operator Feature Metrics are exported under the `cilium_operator_feature`{.docutils .literal .notranslate} Prometheus namespace.

The following tables categorize feature metrics into the following groups:

-   **Advanced Connectivity and Load Balancing** ([adv_connect_and_lb](#cilium-operator-feature-adv-connect-and-lb))

    This category includes features related to advanced networking and load balancing capabilities, such as Gateway API, Ingress Controller, LB IPAM, Node IPAM and L7 Aware Traffic Management.

For example, to check if the Gateway API is enabled on a Cilium operator, observe the metric `cilium_operator_feature_adv_connect_and_lb_gateway_api_enabled`{.docutils .literal .notranslate}. All metrics follows the format `cilium_operator_feature`{.docutils .literal .notranslate} + group name + metric name. A value of `0`{.docutils .literal .notranslate} indicates that the feature is disabled, while `1`{.docutils .literal .notranslate} indicates it is enabled.

Note

For metrics of type "counter," the operator has processed the associated object (e.g., a network policy) but might not be actively enforcing it. These metrics serve to observe if the object has been received and processed, but not necessarily enforced by the operator.

##### `adv_connect_and_lb`{.docutils .literal .notranslate}[](#cilium-operator-feature-adv-connect-and-lb "Link to this heading")

  Name                                                                     Labels   Possible Label Values   Description                                           Type
  ------------------------------------------------------------------------ -------- ----------------------- ----------------------------------------------------- -------
  `gateway_api_enabled`{.docutils .literal .notranslate}                   *None*   *None*                  GatewayAPI enabled on the operator                    gauge
  `ingress_controller_enabled`{.docutils .literal .notranslate}            *None*   *None*                  IngressController enabled on the operator             gauge
  `l7_aware_traffic_management_enabled`{.docutils .literal .notranslate}   *None*   *None*                  L7 Aware Traffic Management enabled on the operator   gauge
  `lb_ipam_enabled`{.docutils .literal .notranslate}                       *None*   *None*                  LB IPAM enabled on the operator                       gauge
  `node_ipam_enabled`{.docutils .literal .notranslate}                     *None*   *None*                  Node IPAM enabled on the operator                     gauge

#### Exported Metrics[](#id10 "Link to this heading")

Most metrics are exported under the `cilium_operator_`{.docutils .literal .notranslate} Prometheus namespace. Some metrics are instead exported under the `cilium_`{.docutils .literal .notranslate} namespace (shared with the agent); these are called out in the relevant sections below.

##### BGP Control Plane Operator[](#bgp-control-plane-operator "Link to this heading")

  Name                                                                                  Labels                                                                                               Default   Description
  ------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------- --------- -----------------------------------------------------------
  `bgp_control_plane_reconcile_errors_total`{.docutils .literal .notranslate}           `resource_kind`{.docutils .literal .notranslate}, `resource_name`{.docutils .literal .notranslate}   Enabled   Number of errors returned per BGP resource reconciliation
  `bgp_control_plane_reconcile_run_duration_seconds`{.docutils .literal .notranslate}                                                                                                        Enabled   Histogram of reconciliation run duration

All metrics are enabled only when the BGP Control Plane is enabled.

##### IPAM[](#ipam-metrics "Link to this heading")

Note

IPAM metrics are all `Enabled`{.docutils .literal .notranslate} only if using the AWS, Alibabacloud or Azure IPAM plugins.

  Name                                                                      Labels                                                                                                                             Default   Description
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- --------- ---------------------------------------------------------------------------------------------
  `ipam_ip_allocation_ops`{.docutils .literal .notranslate}                 `subnet_id`{.docutils .literal .notranslate}                                                                                       Enabled   Number of IP allocation operations.
  `ipam_ip_release_ops`{.docutils .literal .notranslate}                    `subnet_id`{.docutils .literal .notranslate}                                                                                       Enabled   Number of IP release operations.
  `ipam_interface_creation_ops`{.docutils .literal .notranslate}            `subnet_id`{.docutils .literal .notranslate}                                                                                       Enabled   Number of interfaces creation operations.
  `ipam_release_duration_seconds`{.docutils .literal .notranslate}          `type`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `subnet_id`{.docutils .literal .notranslate}   Enabled   Release ip or interface latency in seconds
  `ipam_allocation_duration_seconds`{.docutils .literal .notranslate}       `type`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `subnet_id`{.docutils .literal .notranslate}   Enabled   Allocation ip or interface latency in seconds
  `ipam_nodes`{.docutils .literal .notranslate}                             `category`{.docutils .literal .notranslate}                                                                                        Enabled   Number of nodes by category { total \| in-deficit \| at-capacity }
  `ipam_resync_total`{.docutils .literal .notranslate}                                                                                                                                                         Enabled   Number of synchronization operations with external IPAM API
  `ipam_api_duration_seconds`{.docutils .literal .notranslate}              `operation`{.docutils .literal .notranslate}, `response_code`{.docutils .literal .notranslate}                                     Enabled   Duration of interactions with external IPAM API.
  `ipam_api_rate_limit_duration_seconds`{.docutils .literal .notranslate}   `operation`{.docutils .literal .notranslate}                                                                                       Enabled   Duration of rate limiting while accessing external IPAM API
  `ipam_available_ips`{.docutils .literal .notranslate}                     `target_node`{.docutils .literal .notranslate}                                                                                     Enabled   Number of available IPs on a node (taking into account plugin specific NIC/Address limits).
  `ipam_used_ips`{.docutils .literal .notranslate}                          `target_node`{.docutils .literal .notranslate}                                                                                     Enabled   Number of currently used IPs on a node.
  `ipam_needed_ips`{.docutils .literal .notranslate}                        `target_node`{.docutils .literal .notranslate}                                                                                     Enabled   Number of IPs needed to satisfy allocation on a node.

##### LB-IPAM[](#lb-ipam "Link to this heading")

Note

These metrics are exported under the `cilium_`{.docutils .literal .notranslate} namespace (for example `cilium_lbipam_conflicting_pools`{.docutils .literal .notranslate}), not `cilium_operator_`{.docutils .literal .notranslate}.

  Name                                                             Labels                                    Default   Description
  ---------------------------------------------------------------- ----------------------------------------- --------- ----------------------------------------------------
  `lbipam_conflicting_pools`{.docutils .literal .notranslate}                                                Enabled   Number of conflicting pools
  `lbipam_ips_available`{.docutils .literal .notranslate}          `pool`{.docutils .literal .notranslate}   Enabled   Number of available IPs per pool
  `lbipam_ips_used`{.docutils .literal .notranslate}               `pool`{.docutils .literal .notranslate}   Enabled   Number of used IPs per pool
  `lbipam_services_matching`{.docutils .literal .notranslate}                                                Enabled   Number of matching services
  `lbipam_services_unsatisfied`{.docutils .literal .notranslate}                                             Enabled   Number of services which did not get requested IPs

##### Controllers[](#id12 "Link to this heading")

  Name                                                              Labels                                                                                     Default   Description
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------ --------- -------------------------------------------------------------------------------------
  `controllers_group_runs_total`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}, `group_name`{.docutils .literal .notranslate}   Enabled   Number of times that a controller process was run, labeled by controller group name

The `controllers_group_runs_total`{.docutils .literal .notranslate} metric reports the success and failure count of each controller within the system, labeled by controller group name and completion status. Due to the large number of controllers, enabling this metric is on a per-controller basis. This is configured using an allow-list which is passed as the `controller-group-metrics`{.docutils .literal .notranslate} configuration flag, or the `prometheus.controllerGroupMetrics`{.docutils .literal .notranslate} helm value. The current recommended default set of group names can be found in the values file of the Cilium Helm chart. The special names "all" and "none" are supported.

##### CiliumEndpointSlices (CES)[](#ciliumendpointslices-ces "Link to this heading")

  Name                                                               Labels                                                                                        Description
  ------------------------------------------------------------------ --------------------------------------------------------------------------------------------- -----------------------------------------------
  `number_of_ceps_per_ces`{.docutils .literal .notranslate}                                                                                                        The number of CEPs batched in a CES
  `number_of_cep_changes_per_ces`{.docutils .literal .notranslate}   `opcode`{.docutils .literal .notranslate}                                                     The number of changed CEPs in each CES update
  `ces_sync_total`{.docutils .literal .notranslate}                  `outcome`{.docutils .literal .notranslate}, `failure_type`{.docutils .literal .notranslate}   The number of completed CES syncs by outcome
  `ces_queueing_delay_seconds`{.docutils .literal .notranslate}      `queue`{.docutils .literal .notranslate}                                                      CiliumEndpointSlice queueing delay in seconds

Note that the CES controller has multiple internal queues for handling CES updates. Detailed metrics which are emitted by these queues can be found in the [Internal WorkQueues](#internal-workqueues-metrics) section below.

##### Unmanaged Pods[](#unmanaged-pods "Link to this heading")

  Name                                                Labels   Default   Description
  --------------------------------------------------- -------- --------- ----------------------------------------------------------------------
  `unmanaged_pods`{.docutils .literal .notranslate}            Enabled   The total number of pods observed to be unmanaged by Cilium operator

##### "Double Write" Identity Allocation Mode[](#double-write-identity-allocation-mode "Link to this heading")

When the "[Double Write](../../operations/upgrade/#double-write-migration)" identity allocation mode is enabled, the following metrics are available:

  Name                                                                     Labels   Default   Description
  ------------------------------------------------------------------------ -------- --------- --------------------------------------------------------------
  `doublewrite_crd_identities`{.docutils .literal .notranslate}                     Enabled   The total number of CRD identities
  `doublewrite_kvstore_identities`{.docutils .literal .notranslate}                 Enabled   The total number of identities in the KVStore
  `doublewrite_crd_only_identities`{.docutils .literal .notranslate}                Enabled   The number of CRD identities not present in the KVStore
  `doublewrite_kvstore_only_identities`{.docutils .literal .notranslate}            Enabled   The number of identities in the KVStore not present as a CRD

##### Identity Garbage Collection[](#identity-garbage-collection "Link to this heading")

Identity garbage collection runs in the operator. These metrics are only reported when using the CRD identity allocation mode.

  Name                                                     Labels                                                                                         Default   Description
  -------------------------------------------------------- ---------------------------------------------------------------------------------------------- --------- ------------------------------------------------------------------------------
  `identity_gc_entries`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}, `identity_type`{.docutils .literal .notranslate}    Enabled   Number of alive and deleted identities at the end of a garbage collector run
  `identity_gc_runs`{.docutils .literal .notranslate}      `outcome`{.docutils .literal .notranslate}, `identity_type`{.docutils .literal .notranslate}   Enabled   Number of times identity garbage collector has run
  `identity_gc_latency`{.docutils .literal .notranslate}   `outcome`{.docutils .literal .notranslate}, `identity_type`{.docutils .literal .notranslate}   Enabled   Duration of the last successful identity GC run

##### Identity Management Mode[](#identity-management-metrics "Link to this heading")

  Name                                                                       Labels                                                                                    Description
  -------------------------------------------------------------------------- ----------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------
  `cid_controller_work_queue_event_count`{.docutils .literal .notranslate}   `resource`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}   Counts processed events by CID controller work queues
  `cid_controller_work_queue_latency`{.docutils .literal .notranslate}       `resource`{.docutils .literal .notranslate}, `phase`{.docutils .literal .notranslate}     Duration of CID controller work queues enqueuing and processing latencies in seconds

##### Internal WorkQueues[](#internal-workqueues "Link to this heading")

The Operator uses internal queues to manage the processing of various tasks. Currently, only the Cilium Node Synchronizer queues and Cilium EndpointSlice Controller queues are reporting the metrics listed below.

  Name                                                                             Labels                                          Default   Description
  -------------------------------------------------------------------------------- ----------------------------------------------- --------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `workqueue_depth`{.docutils .literal .notranslate}                               `queue_name`{.docutils .literal .notranslate}   Enabled   Current depth of workqueue
  `workqueue_adds_total`{.docutils .literal .notranslate}                          `queue_name`{.docutils .literal .notranslate}   Enabled   Total number of adds handled by workqueue
  `workqueue_queue_duration_seconds`{.docutils .literal .notranslate}              `queue_name`{.docutils .literal .notranslate}   Enabled   Duration in seconds an item stays in workqueue prior to request
  `workqueue_work_duration_seconds`{.docutils .literal .notranslate}               `queue_name`{.docutils .literal .notranslate}   Enabled   Duration in seconds to process an item from workqueue
  `workqueue_unfinished_work_seconds`{.docutils .literal .notranslate}             `queue_name`{.docutils .literal .notranslate}   Enabled   Duration in seconds of work in progress that hasn't been observed by work_duration. Large values indicate stuck threads. You can deduce the number of stuck threads by observing the rate at which this value increases.
  `workqueue_longest_running_processor_seconds`{.docutils .literal .notranslate}   `queue_name`{.docutils .literal .notranslate}   Enabled   Duration in seconds of the longest running processor for workqueue
  `workqueue_retries_total`{.docutils .literal .notranslate}                       `queue_name`{.docutils .literal .notranslate}   Enabled   Total number of retries handled by workqueue

##### MCS-API[](#mcs-api "Link to this heading")

  Name                                                                       Labels                                                                                                                                                                                                                               Default   Description
  -------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ----------------------------------------------------------
  `mcsapi_serviceexport_info`{.docutils .literal .notranslate}               `serviceexport`{.docutils .literal .notranslate}, `namespace`{.docutils .literal .notranslate}                                                                                                                                       Enabled   Information about ServiceExport in the local cluster
  `mcsapi_serviceexport_status_condition`{.docutils .literal .notranslate}   `serviceexport`{.docutils .literal .notranslate}, `namespace`{.docutils .literal .notranslate}, `condition`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `reason`{.docutils .literal .notranslate}   Enabled   Status Condition of ServiceExport in the local cluster
  `mcsapi_serviceimport_info`{.docutils .literal .notranslate}               `serviceimport`{.docutils .literal .notranslate}, `namespace`{.docutils .literal .notranslate}                                                                                                                                       Enabled   Information about ServiceImport in the local cluster
  `mcsapi_serviceimport_status_condition`{.docutils .literal .notranslate}   `serviceimport`{.docutils .literal .notranslate}, `namespace`{.docutils .literal .notranslate}, `condition`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `reason`{.docutils .literal .notranslate}   Enabled   Status Condition of ServiceImport in the local cluster
  `mcsapi_serviceimport_status_clusters`{.docutils .literal .notranslate}    `serviceimport`{.docutils .literal .notranslate}, `namespace`{.docutils .literal .notranslate}                                                                                                                                       Enabled   The number of clusters currently backing a ServiceImport

##### Clustermesh[](#id13 "Link to this heading")

Note

`clustermesh_remote_clusters`{.docutils .literal .notranslate}, `clustermesh_remote_cluster_failures`{.docutils .literal .notranslate}, `clustermesh_remote_cluster_last_failure_ts`{.docutils .literal .notranslate}, `clustermesh_remote_cluster_readiness_status`{.docutils .literal .notranslate} and `clustermesh_remote_cluster_cache_revocations`{.docutils .literal .notranslate} are exported under the `cilium_`{.docutils .literal .notranslate} namespace (for example `cilium_clustermesh_remote_clusters`{.docutils .literal .notranslate}), not `cilium_operator_`{.docutils .literal .notranslate}. The remaining metrics in this section (`clustermesh_remote_cluster_services`{.docutils .literal .notranslate}, `clustermesh_remote_cluster_endpoint_slices`{.docutils .literal .notranslate} and `clustermesh_remote_cluster_service_exports`{.docutils .literal .notranslate}) are exported under `cilium_operator_`{.docutils .literal .notranslate}.

  Name                                                                              Labels                                              Default   Description
  --------------------------------------------------------------------------------- --------------------------------------------------- --------- ---------------------------------------------------------------------
  `clustermesh_remote_clusters`{.docutils .literal .notranslate}                                                                        Enabled   The total number of remote clusters meshed with the local cluster
  `clustermesh_remote_cluster_failures`{.docutils .literal .notranslate}            `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of failures related to the remote cluster
  `clustermesh_remote_cluster_last_failure_ts`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   Enabled   The timestamp of the last failure of the remote cluster
  `clustermesh_remote_cluster_readiness_status`{.docutils .literal .notranslate}    `target_cluster`{.docutils .literal .notranslate}   Enabled   The readiness status of the remote cluster
  `clustermesh_remote_cluster_cache_revocations`{.docutils .literal .notranslate}   `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of cache revocations related to the remote cluster
  `clustermesh_remote_cluster_services`{.docutils .literal .notranslate}            `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of services per remote cluster
  `clustermesh_remote_cluster_endpoint_slices`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of endpoint slices per remote cluster
  `clustermesh_remote_cluster_service_exports`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   Enabled   The total number of MCS-API service exports per remote cluster

### Hubble[](#hubble "Link to this heading")

#### Configuration[](#id14 "Link to this heading")

Hubble metrics are served by a Hubble instance running inside `cilium-agent`{.docutils .literal .notranslate}. The command-line options to configure them are `--enable-hubble`{.docutils .literal .notranslate}, `--hubble-metrics-server`{.docutils .literal .notranslate}, and `--hubble-metrics`{.docutils .literal .notranslate}. `--hubble-metrics-server`{.docutils .literal .notranslate} takes an `IP:Port`{.docutils .literal .notranslate} pair, but passing an empty IP (e.g. `:9965`{.docutils .literal .notranslate}) will bind the server to all available interfaces. `--hubble-metrics`{.docutils .literal .notranslate} takes a space-separated list of metrics. It's also possible to configure Hubble metrics to listen with TLS and optionally use mTLS for authentication. For details see [Hubble Metrics TLS and Authentication](../hubble/configuration/tls/#hubble-configure-metrics-tls).

Some metrics can take additional semicolon-separated options per metric, e.g. `--hubble-metrics="dns:query;ignoreAAAA`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`http:destinationContext=workload-name"`{.docutils .literal .notranslate} will enable the `dns`{.docutils .literal .notranslate} metric with the `query`{.docutils .literal .notranslate} and `ignoreAAAA`{.docutils .literal .notranslate} options, and the `http`{.docutils .literal .notranslate} metric with the `destinationContext=workload-name`{.docutils .literal .notranslate} option.

#### Context Options[](#context-options "Link to this heading")

Hubble metrics support configuration via context options. Supported context options for all metrics:

-   `sourceContext`{.docutils .literal .notranslate} - Configures the `source`{.docutils .literal .notranslate} label on metrics for both egress and ingress traffic.

-   `sourceEgressContext`{.docutils .literal .notranslate} - Configures the `source`{.docutils .literal .notranslate} label on metrics for egress traffic (takes precedence over `sourceContext`{.docutils .literal .notranslate}).

-   `sourceIngressContext`{.docutils .literal .notranslate} - Configures the `source`{.docutils .literal .notranslate} label on metrics for ingress traffic (takes precedence over `sourceContext`{.docutils .literal .notranslate}).

-   `destinationContext`{.docutils .literal .notranslate} - Configures the `destination`{.docutils .literal .notranslate} label on metrics for both egress and ingress traffic.

-   `destinationEgressContext`{.docutils .literal .notranslate} - Configures the `destination`{.docutils .literal .notranslate} label on metrics for egress traffic (takes precedence over `destinationContext`{.docutils .literal .notranslate}).

-   `destinationIngressContext`{.docutils .literal .notranslate} - Configures the `destination`{.docutils .literal .notranslate} label on metrics for ingress traffic (takes precedence over `destinationContext`{.docutils .literal .notranslate}).

-   `labelsContext`{.docutils .literal .notranslate} - Configures a list of labels to be enabled on metrics.

There are also some context options that are specific to certain metrics. See the documentation for the individual metrics to see what options are available for each.

See below for details on each of the different context options.

Most Hubble metrics can be configured to add the source and/or destination context as a label using the `sourceContext`{.docutils .literal .notranslate} and `destinationContext`{.docutils .literal .notranslate} options. The possible values are:

  Option Value                                           Description
  ------------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `identity`{.docutils .literal .notranslate}            All Cilium security identity labels
  `namespace`{.docutils .literal .notranslate}           Kubernetes namespace name
  `pod`{.docutils .literal .notranslate}                 Kubernetes pod name and namespace name in the form of `namespace/pod`{.docutils .literal .notranslate}.
  `pod-name`{.docutils .literal .notranslate}            Kubernetes pod name.
  `dns`{.docutils .literal .notranslate}                 All known DNS names of the source or destination (comma-separated)
  `ip`{.docutils .literal .notranslate}                  The IPv4 or IPv6 address
  `reserved-identity`{.docutils .literal .notranslate}   Reserved identity label.
  `workload`{.docutils .literal .notranslate}            Kubernetes pod's workload name and namespace in the form of `namespace/workload-name`{.docutils .literal .notranslate}.
  `workload-name`{.docutils .literal .notranslate}       Kubernetes pod's workload name (workloads are: Deployment, Statefulset, Daemonset, ReplicationController, CronJob, Job, DeploymentConfig (OpenShift), etc).
  `app`{.docutils .literal .notranslate}                 Kubernetes pod's app name, derived from pod labels (`app.kubernetes.io/name`{.docutils .literal .notranslate}, `k8s-app`{.docutils .literal .notranslate}, or `app`{.docutils .literal .notranslate}).

When specifying the source and/or destination context, multiple contexts can be specified by separating them via the `|`{.docutils .literal .notranslate} symbol. When multiple are specified, then the first non-empty value is added to the metric as a label. For example, a metric configuration of `flow:destinationContext=dns|ip`{.docutils .literal .notranslate} will first try to use the DNS name of the target for the label. If no DNS name is known for the target, it will fall back and use the IP address of the target instead.

Note

There are 3 cases in which the identity label list contains multiple reserved labels:

1.  `reserved:kube-apiserver`{.docutils .literal .notranslate} and `reserved:host`{.docutils .literal .notranslate}

2.  `reserved:kube-apiserver`{.docutils .literal .notranslate} and `reserved:remote-node`{.docutils .literal .notranslate}

3.  `reserved:kube-apiserver`{.docutils .literal .notranslate} and `reserved:world`{.docutils .literal .notranslate}

In all of these 3 cases, `reserved-identity`{.docutils .literal .notranslate} context returns `reserved:kube-apiserver`{.docutils .literal .notranslate}.

Hubble metrics can also be configured with a `labelsContext`{.docutils .literal .notranslate} which allows providing a list of labels that should be added to the metric. Unlike `sourceContext`{.docutils .literal .notranslate} and `destinationContext`{.docutils .literal .notranslate}, instead of different values being put into the same metric label, the `labelsContext`{.docutils .literal .notranslate} puts them into different label values.

  Option Value                                                   Description
  -------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `source_ip`{.docutils .literal .notranslate}                   The source IP of the flow.
  `source_namespace`{.docutils .literal .notranslate}            The namespace of the pod if the flow source is from a Kubernetes pod.
  `source_pod`{.docutils .literal .notranslate}                  The pod name if the flow source is from a Kubernetes pod.
  `source_workload`{.docutils .literal .notranslate}             The name of the source pod's workload (Deployment, Statefulset, Daemonset, ReplicationController, CronJob, Job, DeploymentConfig (OpenShift)).
  `source_workload_kind`{.docutils .literal .notranslate}        The kind of the source pod's workload, for example, Deployment, Statefulset, Daemonset, ReplicationController, CronJob, Job, DeploymentConfig (OpenShift).
  `source_app`{.docutils .literal .notranslate}                  The app name of the source pod, derived from pod labels (`app.kubernetes.io/name`{.docutils .literal .notranslate}, `k8s-app`{.docutils .literal .notranslate}, or `app`{.docutils .literal .notranslate}).
  `destination_ip`{.docutils .literal .notranslate}              The destination IP of the flow.
  `destination_namespace`{.docutils .literal .notranslate}       The namespace of the pod if the flow destination is from a Kubernetes pod.
  `destination_pod`{.docutils .literal .notranslate}             The pod name if the flow destination is from a Kubernetes pod.
  `destination_workload`{.docutils .literal .notranslate}        The name of the destination pod's workload (Deployment, Statefulset, Daemonset, ReplicationController, CronJob, Job, DeploymentConfig (OpenShift)).
  `destination_workload_kind`{.docutils .literal .notranslate}   The kind of the destination pod's workload, for example, Deployment, Statefulset, Daemonset, ReplicationController, CronJob, Job, DeploymentConfig (OpenShift).
  `destination_app`{.docutils .literal .notranslate}             The app name of the source pod, derived from pod labels (`app.kubernetes.io/name`{.docutils .literal .notranslate}, `k8s-app`{.docutils .literal .notranslate}, or `app`{.docutils .literal .notranslate}).
  `traffic_direction`{.docutils .literal .notranslate}           Identifies the traffic direction of the flow. Possible values are `ingress`{.docutils .literal .notranslate}, `egress`{.docutils .literal .notranslate} and `unknown`{.docutils .literal .notranslate}.

When specifying the flow context, multiple values can be specified by separating them via the `,`{.docutils .literal .notranslate} symbol. All labels listed are included in the metric, even if empty. For example, a metric configuration of `http:labelsContext=source_namespace,source_pod`{.docutils .literal .notranslate} will add the `source_namespace`{.docutils .literal .notranslate} and `source_pod`{.docutils .literal .notranslate} labels to all Hubble HTTP metrics.

Note

To limit metrics cardinality hubble will remove data series bound to specific pod after one minute from pod deletion. Metric is considered to be bound to a specific pod when at least one of the following conditions is met:

-   `sourceContext`{.docutils .literal .notranslate} is set to `pod`{.docutils .literal .notranslate} and metric series has `source`{.docutils .literal .notranslate} label matching `<pod_namespace>/<pod_name>`{.docutils .literal .notranslate}

-   `destinationContext`{.docutils .literal .notranslate} is set to `pod`{.docutils .literal .notranslate} and metric series has `destination`{.docutils .literal .notranslate} label matching `<pod_namespace>/<pod_name>`{.docutils .literal .notranslate}

-   `labelsContext`{.docutils .literal .notranslate} contains both `source_namespace`{.docutils .literal .notranslate} and `source_pod`{.docutils .literal .notranslate} and metric series labels match namespace and name of deleted pod

-   `labelsContext`{.docutils .literal .notranslate} contains both `destination_namespace`{.docutils .literal .notranslate} and `destination_pod`{.docutils .literal .notranslate} and metric series labels match namespace and name of deleted pod

#### Exported Metrics[](#hubble-exported-metrics "Link to this heading")

Hubble metrics are exported under the `hubble_`{.docutils .literal .notranslate} Prometheus namespace.

##### lost events[](#lost-events "Link to this heading")

This metric, unlike other ones, is not directly tied to network flows. It's enabled if any of the other metrics is enabled.

  Name                                                   Labels                                      Default   Description
  ------------------------------------------------------ ------------------------------------------- --------- -----------------------
  `lost_events_total`{.docutils .literal .notranslate}   `source`{.docutils .literal .notranslate}   Enabled   Number of lost events

###### Labels[](#labels "Link to this heading")

-   

    `source`{.docutils .literal .notranslate} identifies the source of lost events, one of:

    :   -   `perf_event_ring_buffer`{.docutils .literal .notranslate}

        -   `observer_events_queue`{.docutils .literal .notranslate}

        -   `hubble_ring_buffer`{.docutils .literal .notranslate}

##### `dns`{.docutils .literal .notranslate}[](#dns "Link to this heading")

  Name                                                          Labels                                                                                                                                 Default    Description
  ------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------------------------------
  `dns_queries_total`{.docutils .literal .notranslate}          `rcode`{.docutils .literal .notranslate}, `qtypes`{.docutils .literal .notranslate}, `ips_returned`{.docutils .literal .notranslate}   Disabled   Number of DNS queries observed
  `dns_responses_total`{.docutils .literal .notranslate}        `rcode`{.docutils .literal .notranslate}, `qtypes`{.docutils .literal .notranslate}, `ips_returned`{.docutils .literal .notranslate}   Disabled   Number of DNS responses observed
  `dns_response_types_total`{.docutils .literal .notranslate}   `type`{.docutils .literal .notranslate}, `qtypes`{.docutils .literal .notranslate}                                                     Disabled   Number of DNS response types

###### Options[](#options "Link to this heading")

  Option Key                                      Option Value   Description
  ----------------------------------------------- -------------- ------------------------------------
  `query`{.docutils .literal .notranslate}        N/A            Include the query as label "query"
  `ignoreAAAA`{.docutils .literal .notranslate}   N/A            Ignore any AAAA requests/responses

This metric supports [Context Options](#hubble-context-options).

##### `drop`{.docutils .literal .notranslate}[](#drop "Link to this heading")

  Name                                            Labels                                                                                   Default    Description
  ----------------------------------------------- ---------------------------------------------------------------------------------------- ---------- -----------------
  `drop_total`{.docutils .literal .notranslate}   `reason`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}   Disabled   Number of drops

###### Options[](#id16 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `flow`{.docutils .literal .notranslate}[](#flow "Link to this heading")

  Name                                                       Labels                                                                                                                                                                         Default    Description
  ---------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- ---------------------------------
  `flows_processed_total`{.docutils .literal .notranslate}   `protocol`{.docutils .literal .notranslate}, `type`{.docutils .literal .notranslate}, `subtype`{.docutils .literal .notranslate}, `verdict`{.docutils .literal .notranslate}   Disabled   Total number of flows processed

###### Options[](#id17 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `flows-to-world`{.docutils .literal .notranslate}[](#flows-to-world "Link to this heading")

This metric counts all non-reply flows containing the `reserved:world`{.docutils .literal .notranslate} label in their destination identity. By default, dropped flows are counted if and only if the drop reason is `Policy`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`denied`{.docutils .literal .notranslate}. Set `any-drop`{.docutils .literal .notranslate} option to count all dropped flows.

  Name                                                      Labels                                                                                    Default    Description
  --------------------------------------------------------- ----------------------------------------------------------------------------------------- ---------- -----------------------------------------------------------------------------
  `flows_to_world_total`{.docutils .literal .notranslate}   `protocol`{.docutils .literal .notranslate}, `verdict`{.docutils .literal .notranslate}   Disabled   Total number of flows to `reserved:world`{.docutils .literal .notranslate}.

###### Options[](#id18 "Link to this heading")

  Option Key                                    Option Value   Description
  --------------------------------------------- -------------- --------------------------------------------------------------------------------
  `any-drop`{.docutils .literal .notranslate}   N/A            Count any dropped flows regardless of the drop reason.
  `port`{.docutils .literal .notranslate}       N/A            Include the destination port as label `port`{.docutils .literal .notranslate}.
  `syn-only`{.docutils .literal .notranslate}   N/A            Only count non-reply SYNs for TCP flows.

This metric supports [Context Options](#hubble-context-options).

##### `http`{.docutils .literal .notranslate}[](#http "Link to this heading")

Deprecated, use `httpV2`{.docutils .literal .notranslate} instead. These metrics can not be enabled at the same time as `httpV2`{.docutils .literal .notranslate}.

  Name                                                               Labels                                                                                                                                                                           Default    Description
  ------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- -----------------------------------------------
  `http_requests_total`{.docutils .literal .notranslate}             `method`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `reporter`{.docutils .literal .notranslate}                                              Disabled   Count of HTTP requests
  `http_responses_total`{.docutils .literal .notranslate}            `method`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `reporter`{.docutils .literal .notranslate}   Disabled   Count of HTTP responses
  `http_request_duration_seconds`{.docutils .literal .notranslate}   `method`{.docutils .literal .notranslate}, `reporter`{.docutils .literal .notranslate}                                                                                           Disabled   Histogram of HTTP request duration in seconds

###### Labels[](#id19 "Link to this heading")

-   `method`{.docutils .literal .notranslate} is the HTTP method of the request/response.

-   `protocol`{.docutils .literal .notranslate} is the HTTP protocol of the request, (For example: `HTTP/1.1`{.docutils .literal .notranslate}, `HTTP/2`{.docutils .literal .notranslate}).

-   `status`{.docutils .literal .notranslate} is the HTTP status code of the response.

-   `reporter`{.docutils .literal .notranslate} identifies the origin of the request/response. It is set to `client`{.docutils .literal .notranslate} if it originated from the client, `server`{.docutils .literal .notranslate} if it originated from the server, or `unknown`{.docutils .literal .notranslate} if its origin is unknown.

###### Options[](#id20 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `httpV2`{.docutils .literal .notranslate}[](#httpv2 "Link to this heading")

`httpV2`{.docutils .literal .notranslate} is an updated version of the existing `http`{.docutils .literal .notranslate} metrics. These metrics can not be enabled at the same time as `http`{.docutils .literal .notranslate}.

The main difference is that `http_requests_total`{.docutils .literal .notranslate} and `http_responses_total`{.docutils .literal .notranslate} have been consolidated, and use the response flow data.

Additionally, the `http_request_duration_seconds`{.docutils .literal .notranslate} metric source/destination related labels now are from the perspective of the request. In the `http`{.docutils .literal .notranslate} metrics, the source/destination were swapped, because the metric uses the response flow data, where the source/destination are swapped, but in `httpV2`{.docutils .literal .notranslate} we correctly account for this.

  Name                                                               Labels                                                                                                                                                                           Default    Description
  ------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- -----------------------------------------------
  `http_requests_total`{.docutils .literal .notranslate}             `method`{.docutils .literal .notranslate}, `protocol`{.docutils .literal .notranslate}, `status`{.docutils .literal .notranslate}, `reporter`{.docutils .literal .notranslate}   Disabled   Count of HTTP requests
  `http_request_duration_seconds`{.docutils .literal .notranslate}   `method`{.docutils .literal .notranslate}, `reporter`{.docutils .literal .notranslate}                                                                                           Disabled   Histogram of HTTP request duration in seconds

###### Labels[](#id21 "Link to this heading")

-   `method`{.docutils .literal .notranslate} is the HTTP method of the request/response.

-   `protocol`{.docutils .literal .notranslate} is the HTTP protocol of the request, (For example: `HTTP/1.1`{.docutils .literal .notranslate}, `HTTP/2`{.docutils .literal .notranslate}).

-   `status`{.docutils .literal .notranslate} is the HTTP status code of the response.

-   `reporter`{.docutils .literal .notranslate} identifies the origin of the request/response. It is set to `client`{.docutils .literal .notranslate} if it originated from the client, `server`{.docutils .literal .notranslate} if it originated from the server, or `unknown`{.docutils .literal .notranslate} if its origin is unknown.

###### Options[](#id22 "Link to this heading")

  Option Key                                     Option Value                              Description
  ---------------------------------------------- ----------------------------------------- ----------------------------------------------------------------------------------------------------------
  `exemplars`{.docutils .literal .notranslate}   `true`{.docutils .literal .notranslate}   Include extracted trace IDs in HTTP metrics. Requires [OpenMetrics to be enabled](#hubble-open-metrics).

This metric supports [Context Options](#hubble-context-options).

##### `icmp`{.docutils .literal .notranslate}[](#icmp "Link to this heading")

  Name                                            Labels                                                                               Default    Description
  ----------------------------------------------- ------------------------------------------------------------------------------------ ---------- -------------------------
  `icmp_total`{.docutils .literal .notranslate}   `family`{.docutils .literal .notranslate}, `type`{.docutils .literal .notranslate}   Disabled   Number of ICMP messages

###### Options[](#id23 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `port-distribution`{.docutils .literal .notranslate}[](#port-distribution "Link to this heading")

  Name                                                         Labels                                                                                 Default    Description
  ------------------------------------------------------------ -------------------------------------------------------------------------------------- ---------- ----------------------------------------------------
  `port_distribution_total`{.docutils .literal .notranslate}   `protocol`{.docutils .literal .notranslate}, `port`{.docutils .literal .notranslate}   Disabled   Numbers of packets distributed by destination port

###### Options[](#id24 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `tcp`{.docutils .literal .notranslate}[](#tcp "Link to this heading")

  Name                                                 Labels                                                                               Default    Description
  ---------------------------------------------------- ------------------------------------------------------------------------------------ ---------- ----------------------
  `tcp_flags_total`{.docutils .literal .notranslate}   `flag`{.docutils .literal .notranslate}, `family`{.docutils .literal .notranslate}   Disabled   TCP flag occurrences

###### Options[](#id25 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### `sctp`{.docutils .literal .notranslate}[](#sctp "Link to this heading")

  Name                                                        Labels                                                                                     Default    Description
  ----------------------------------------------------------- ------------------------------------------------------------------------------------------ ---------- -----------------------------
  `sctp_chunk_types_total`{.docutils .literal .notranslate}   `chunk_type`{.docutils .literal .notranslate}, `family`{.docutils .literal .notranslate}   Disabled   SCTP chunk type occurrences

###### Options[](#id26 "Link to this heading")

This metric supports [Context Options](#hubble-context-options).

##### dynamic_exporter_exporters_total[](#dynamic-exporter-exporters-total "Link to this heading")

This is dynamic hubble exporter metric.

  Name                                                                  Labels                                      Default   Description
  --------------------------------------------------------------------- ------------------------------------------- --------- ---------------------------------------
  `dynamic_exporter_exporters_total`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}   Enabled   Number of configured hubble exporters

###### Labels[](#id27 "Link to this heading")

-   

    `status`{.docutils .literal .notranslate} identifies status of exporters, can be one of:

    :   -   `active`{.docutils .literal .notranslate}

        -   `inactive`{.docutils .literal .notranslate}

##### dynamic_exporter_up[](#dynamic-exporter-up "Link to this heading")

This is dynamic hubble exporter metric.

  Name                                                     Labels                                    Default   Description
  -------------------------------------------------------- ----------------------------------------- --------- -----------------------------------------------
  `dynamic_exporter_up`{.docutils .literal .notranslate}   `name`{.docutils .literal .notranslate}   Enabled   Status of exporter (1 - active, 0 - inactive)

###### Labels[](#id28 "Link to this heading")

-   `name`{.docutils .literal .notranslate} identifies exporter name

##### dynamic_exporter_reconfigurations_total[](#dynamic-exporter-reconfigurations-total "Link to this heading")

This is dynamic hubble exporter metric.

  Name                                                                         Labels                                  Default   Description
  ---------------------------------------------------------------------------- --------------------------------------- --------- ----------------------------------------------
  `dynamic_exporter_reconfigurations_total`{.docutils .literal .notranslate}   `op`{.docutils .literal .notranslate}   Enabled   Number of dynamic exporters reconfigurations

###### Labels[](#id29 "Link to this heading")

-   

    `op`{.docutils .literal .notranslate} identifies reconfiguration operation type, can be one of:

    :   -   `add`{.docutils .literal .notranslate}

        -   `update`{.docutils .literal .notranslate}

        -   `remove`{.docutils .literal .notranslate}

##### dynamic_exporter_config_hash[](#dynamic-exporter-config-hash "Link to this heading")

This is dynamic hubble exporter metric.

  Name                                                              Labels   Default   Description
  ----------------------------------------------------------------- -------- --------- -----------------------------
  `dynamic_exporter_config_hash`{.docutils .literal .notranslate}            Enabled   Hash of last applied config

##### dynamic_exporter_config_last_applied[](#dynamic-exporter-config-last-applied "Link to this heading")

This is dynamic hubble exporter metric.

  Name                                                                      Labels   Default   Description
  ------------------------------------------------------------------------- -------- --------- ----------------------------------
  `dynamic_exporter_config_last_applied`{.docutils .literal .notranslate}            Enabled   Timestamp of last applied config

### clustermesh-apiserver[](#clustermesh-apiserver "Link to this heading")

#### Configuration[](#id30 "Link to this heading")

To expose any metrics, invoke `clustermesh-apiserver`{.docutils .literal .notranslate} with the `--prometheus-serve-addr`{.docutils .literal .notranslate} option. This option takes a `IP:Port`{.docutils .literal .notranslate} pair but passing an empty IP (e.g. `:9962`{.docutils .literal .notranslate}) will bind the server to all available interfaces (there is usually only one in a container).

#### Exported Metrics[](#id31 "Link to this heading")

All metrics are exported under the `cilium_clustermesh_apiserver_`{.docutils .literal .notranslate} Prometheus namespace.

##### Bootstrap[](#bootstrap "Link to this heading")

  Name                                                   Description
  ------------------------------------------------------ -------------------------------------------
  `bootstrap_seconds`{.docutils .literal .notranslate}   Duration in seconds to complete bootstrap

##### KVstore[](#id32 "Link to this heading")

  Name                                                                     Labels                                                                                                                                                                     Description
  ------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------
  `kvstore_operations_duration_seconds`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}, `kind`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}   Duration of kvstore operation
  `kvstore_events_queue_seconds`{.docutils .literal .notranslate}          `action`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}                                                                                        Seconds waited before a received event was queued
  `kvstore_quorum_errors_total`{.docutils .literal .notranslate}           `error`{.docutils .literal .notranslate}                                                                                                                                   Number of quorum errors
  `kvstore_sync_errors_total`{.docutils .literal .notranslate}             `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Number of times synchronization to the kvstore failed
  `kvstore_sync_queue_size`{.docutils .literal .notranslate}               `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Number of elements queued for synchronization in the kvstore
  `kvstore_initial_sync_completed`{.docutils .literal .notranslate}        `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}                                     Whether the initial synchronization from/to the kvstore has completed

##### API Rate Limiting[](#id33 "Link to this heading")

  Name                                                                         Labels                                                                                                                                    Description
  ---------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------
  `api_limiter_processed_requests_total`{.docutils .literal .notranslate}      `api_call`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `return_code`{.docutils .literal .notranslate}   Total number of API requests processed
  `api_limiter_processing_duration_seconds`{.docutils .literal .notranslate}   `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Mean and estimated processing duration in seconds
  `api_limiter_rate_limit`{.docutils .literal .notranslate}                    `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Current rate limiting configuration (limit and burst)
  `api_limiter_requests_in_flight`{.docutils .literal .notranslate}            `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Current and maximum allowed number of requests in flight
  `api_limiter_wait_duration_seconds`{.docutils .literal .notranslate}         `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Mean, min, and max wait duration

##### Controllers[](#id34 "Link to this heading")

  Name                                                              Labels                                                                                     Default   Description
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------ --------- -------------------------------------------------------------------------------------
  `controllers_group_runs_total`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}, `group_name`{.docutils .literal .notranslate}   Enabled   Number of times that a controller process was run, labeled by controller group name

The `controllers_group_runs_total`{.docutils .literal .notranslate} metric reports the success and failure count of each controller within the system, labeled by controller group name and completion status. Enabling this metric is on a per-controller basis. This is configured using an allow-list which is passed as the `controller-group-metrics`{.docutils .literal .notranslate} configuration flag. The current default set for `clustermesh-apiserver`{.docutils .literal .notranslate} found in the Cilium Helm chart is the special name "all", which enables the metric for all controller groups. The special name "none" is also supported.

### kvstoremesh[](#kvstoremesh "Link to this heading")

#### Configuration[](#id35 "Link to this heading")

To expose any metrics, invoke `kvstoremesh`{.docutils .literal .notranslate} with the `--prometheus-serve-addr`{.docutils .literal .notranslate} option. This option takes a `IP:Port`{.docutils .literal .notranslate} pair but passing an empty IP (e.g. `:9964`{.docutils .literal .notranslate}) binds the server to all available interfaces (there is usually only one interface in a container).

#### Exported Metrics[](#id36 "Link to this heading")

All metrics are exported under the `cilium_kvstoremesh_`{.docutils .literal .notranslate} Prometheus namespace.

##### Bootstrap[](#id37 "Link to this heading")

  Name                                                   Description
  ------------------------------------------------------ -------------------------------------------
  `bootstrap_seconds`{.docutils .literal .notranslate}   Duration in seconds to complete bootstrap

##### KVStoremesh[](#id38 "Link to this heading")

  Name                                                               Labels                                    Description
  ------------------------------------------------------------------ ----------------------------------------- ----------------------------
  `leader_election_master_status`{.docutils .literal .notranslate}   `name`{.docutils .literal .notranslate}   The leader election status

##### Clustermesh[](#id39 "Link to this heading")

Note that these metrics are not prefixed by `clustermesh_`{.docutils .literal .notranslate}.

  Name                                                                  Labels                                              Description
  --------------------------------------------------------------------- --------------------------------------------------- ---------------------------------------------------------------------
  `remote_clusters`{.docutils .literal .notranslate}                                                                        The total number of remote clusters meshed with the local cluster
  `remote_cluster_failures`{.docutils .literal .notranslate}            `target_cluster`{.docutils .literal .notranslate}   The total number of failures related to the remote cluster
  `remote_cluster_last_failure_ts`{.docutils .literal .notranslate}     `target_cluster`{.docutils .literal .notranslate}   The timestamp of the last failure of the remote cluster
  `remote_cluster_readiness_status`{.docutils .literal .notranslate}    `target_cluster`{.docutils .literal .notranslate}   The readiness status of the remote cluster
  `remote_cluster_cache_revocations`{.docutils .literal .notranslate}   `target_cluster`{.docutils .literal .notranslate}   The total number of cache revocations related to the remote cluster

##### KVstore[](#id40 "Link to this heading")

  Name                                                                     Labels                                                                                                                                                                     Description
  ------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------
  `kvstore_operations_duration_seconds`{.docutils .literal .notranslate}   `action`{.docutils .literal .notranslate}, `kind`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}   Duration of kvstore operation
  `kvstore_events_queue_seconds`{.docutils .literal .notranslate}          `action`{.docutils .literal .notranslate}, `scope`{.docutils .literal .notranslate}                                                                                        Seconds waited before a received event was queued
  `kvstore_quorum_errors_total`{.docutils .literal .notranslate}           `error`{.docutils .literal .notranslate}                                                                                                                                   Number of quorum errors
  `kvstore_sync_errors_total`{.docutils .literal .notranslate}             `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Number of times synchronization to the kvstore failed
  `kvstore_sync_queue_size`{.docutils .literal .notranslate}               `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}                                                                                Number of elements queued for synchronization in the kvstore
  `kvstore_initial_sync_completed`{.docutils .literal .notranslate}        `scope`{.docutils .literal .notranslate}, `source_cluster`{.docutils .literal .notranslate}, `action`{.docutils .literal .notranslate}                                     Whether the initial synchronization from/to the kvstore has completed

##### API Rate Limiting[](#id41 "Link to this heading")

  Name                                                                         Labels                                                                                                                                    Description
  ---------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------
  `api_limiter_processed_requests_total`{.docutils .literal .notranslate}      `api_call`{.docutils .literal .notranslate}, `outcome`{.docutils .literal .notranslate}, `return_code`{.docutils .literal .notranslate}   Total number of API requests processed
  `api_limiter_processing_duration_seconds`{.docutils .literal .notranslate}   `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Mean and estimated processing duration in seconds
  `api_limiter_rate_limit`{.docutils .literal .notranslate}                    `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Current rate limiting configuration (limit and burst)
  `api_limiter_requests_in_flight`{.docutils .literal .notranslate}            `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Current and maximum allowed number of requests in flight
  `api_limiter_wait_duration_seconds`{.docutils .literal .notranslate}         `api_call`{.docutils .literal .notranslate}, `value`{.docutils .literal .notranslate}                                                     Mean, min, and max wait duration

##### Controllers[](#id42 "Link to this heading")

  Name                                                              Labels                                                                                     Default   Description
  ----------------------------------------------------------------- ------------------------------------------------------------------------------------------ --------- -------------------------------------------------------------------------------------
  `controllers_group_runs_total`{.docutils .literal .notranslate}   `status`{.docutils .literal .notranslate}, `group_name`{.docutils .literal .notranslate}   Enabled   Number of times that a controller process was run, labeled by controller group name

The `controllers_group_runs_total`{.docutils .literal .notranslate} metric reports the success and failure count of each controller within the system, labeled by controller group name and completion status. Enabling this metric is on a per-controller basis. This is configured using an allow-list which is passed as the `controller-group-metrics`{.docutils .literal .notranslate} configuration flag. The current default set for `kvstoremesh`{.docutils .literal .notranslate} found in the Cilium Helm chart is the special name "all", which enables the metric for all controller groups. The special name "none" is also supported.

##### NAT[](#nat "Link to this heading")

  Name                                                             Labels                                      Default   Description
  ---------------------------------------------------------------- ------------------------------------------- --------- ---------------------------------------------------------------------------------------------------------------------
  `nat_endpoint_max_connection`{.docutils .literal .notranslate}   `family`{.docutils .literal .notranslate}   Enabled   Saturation of the most saturated distinct NAT mapped connection, in terms of egress-IP and remote endpoint address.

These metrics are for monitoring Cilium's NAT mapping functionality. NAT is used by features such as Egress Gateway and BPF masquerading.

The NAT map holds mappings for masqueraded connections. Connection held in the NAT table that are masqueraded with the same egress-IP and are going to the same remote endpoints IP and port all require a unique source port for the mapping. This means that any Node masquerading connections to a distinct external endpoint is limited by the possible ephemeral source ports.

Given a Node forwarding one or more such egress-IP and remote endpoint tuples, the `nat_endpoint_max_connection`{.docutils .literal .notranslate} metric is the most saturated such connection in terms of a percent of possible source ports available. This metric is especially useful when using the egress gateway feature where it's possible to overload a Node if many connections are all going to the same endpoint. In general, this metric should normally be fairly low. A high number here may indicate that a Node is reaching its limit for connections to one or more external endpoints.

##### Local Redirect Policy (control plane)[](#local-redirect-policy-control-plane "Link to this heading")

  Name                                                             Labels   Default   Description
  ---------------------------------------------------------------- -------- --------- -----------------------------------------------------------
  `controller_duration_seconds`{.docutils .literal .notranslate}            Enabled   Histogram of processing times for local redirect policies
