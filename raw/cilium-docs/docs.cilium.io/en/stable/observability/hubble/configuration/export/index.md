---
{"title": "Configuring Hubble exporter", "url": "https://docs.cilium.io/en/stable/observability/hubble/configuration/export/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Configuring Hubble exporter[](#configuring-hubble-exporter "Link to this heading")

**Hubble Exporter** is a feature of `cilium-agent`{.docutils .literal .notranslate} that lets you write Hubble flows to a file for later consumption as logs. Hubble Exporter supports file rotation, size limits, filters, and field masks.

## Prerequisites[](#prerequisites "Link to this heading")

Setup Helm repository:

``` {#codecell0}
helm repo add cilium https://helm.cilium.io/
```

Copy Line

Cilium charts are also available via OCI registries (Quay.io and Docker Hub). No setup required - you can install directly using `oci://`{.docutils .literal .notranslate} URLs.

See the [OCI Registry section](../../../../installation/k8s-install-helm/#k8s-install-helm) for more information, including chart signing verification and digest-based installations.

## Basic Configuration[](#basic-configuration "Link to this heading")

### Setup[](#setup "Link to this heading")

**Hubble Exporter** is enabled with Config Map property. It is disabled until you set a file path value for `hubble-export-file-path`{.docutils .literal .notranslate}.

You can use helm to install cilium with hubble exporter enabled:

``` {#codecell1 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.filePath=/var/run/cilium/hubble/events.log
```

Copy First Line Copy All

``` {#codecell2 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.filePath=/var/run/cilium/hubble/events.log
```

Copy First Line Copy All

Wait for `cilium`{.docutils .literal .notranslate} pod to become ready:

``` {#codecell3}
kubectl -n kube-system rollout status ds/cilium
```

Copy Line

Verify that flow logs are stored in target files:

``` {#codecell4}
kubectl -n kube-system exec ds/cilium -- tail -f /var/run/cilium/hubble/events.log
```

Copy Line

Once you have configured the Hubble Exporter, you can configure your logging solution to consume logs from your Hubble export file path.

To get Hubble flows directly exported to the logs instead of written to a rotated file, `stdout`{.docutils .literal .notranslate} can be defined as `hubble-export-file-path`{.docutils .literal .notranslate}.

To disable the static configuration, you must remove the `hubble-export-file-path`{.docutils .literal .notranslate} key in the `cilium-config`{.docutils .literal .notranslate} ConfigMap and manually clean up the log files created in the specified location in the container. The below command will restart the Cilium pods. If you edit the ConfigMap manually, you will need to restart the Cilium pods.

``` {#codecell5}
cilium config delete hubble-export-file-path
```

Copy Line

### Configuration options[](#configuration-options "Link to this heading")

Helm chart configuration options include:

-   `hubble.export.static.filePath`{.docutils .literal .notranslate}: file path of target log file. (default /var/run/cilium/hubble/events.log)

-   `hubble.export.static.fileMaxSizeMb`{.docutils .literal .notranslate}: size in MB at which to rotate the Hubble export file. (default 10)

-   `hubble.export.static.fileMaxBackups`{.docutils .literal .notranslate}: number of rotated Hubble export files to keep. (default 5)

-   `hubble.export.static.fileCompress`{.docutils .literal .notranslate}: enable compression of rotated files. (default false)

## Performance tuning[](#performance-tuning "Link to this heading")

Configuration options impacting performance of **Hubble exporter** include:

-   `hubble.export.static.allowList`{.docutils .literal .notranslate}: specify an allowlist as JSON encoded FlowFilters to Hubble exporter.

-   `hubble.export.static.denyList`{.docutils .literal .notranslate}: specify a denylist as JSON encoded FlowFilters to Hubble exporter.

-   `hubble.export.static.fieldMask`{.docutils .literal .notranslate}: specify a list of fields to use for field masking in Hubble exporter.

### Filters[](#filters "Link to this heading")

You can use `hubble`{.docutils .literal .notranslate} CLI to generated required filters (see [Specifying Raw Flow Filters](https://github.com/cilium/hubble#specifying-raw-flow-filters) for more examples).

For example, to filter flows with verdict `DENIED`{.docutils .literal .notranslate} or `ERROR`{.docutils .literal .notranslate}, run:

``` {#codecell6}
$ hubble observe --verdict DROPPED --verdict ERROR --print-raw-filters
allowlist:
- '{"verdict":["DROPPED","ERROR"]}'
```

Copy First Line Copy Commands Copy All

Then paste the output to `hubble-export-allowlist`{.docutils .literal .notranslate} in `cilium-config`{.docutils .literal .notranslate} Config Map:

``` {#codecell7}
kubectl -n kube-system patch cm cilium-config --patch-file=/dev/stdin <<-EOF
data:
  hubble-export-allowlist: '{"verdict":["DROPPED","ERROR"]}'
EOF
```

Copy First Line Copy All

Or use helm chart to update your cilium installation setting value flag `hubble.export.static.allowList`{.docutils .literal .notranslate}.

``` {#codecell8 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.allowList[0]='{"verdict":["DROPPED","ERROR"]}'
```

Copy First Line Copy All

``` {#codecell9 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.allowList[0]='{"verdict":["DROPPED","ERROR"]}'
```

Copy First Line Copy All

You can do the same to selectively filter data. For example, to filter all flows in the `kube-system`{.docutils .literal .notranslate} namespace, run:

``` {#codecell10}
$ hubble observe --not --namespace kube-system --print-raw-filters
denylist:
- '{"source_pod":["kube-system/"]}'
- '{"destination_pod":["kube-system/"]}'
```

Copy First Line Copy Commands Copy All

Then paste the output to `hubble-export-denylist`{.docutils .literal .notranslate} in `cilium-config`{.docutils .literal .notranslate} Config Map:

``` {#codecell11}
kubectl -n kube-system patch cm cilium-config --patch-file=/dev/stdin <<-EOF
data:
  hubble-export-denylist: '{"source_pod":["kube-system/"]},{"destination_pod":["kube-system/"]}'
EOF
```

Copy First Line Copy All

Or use helm chart to update your cilium installation setting value flag `hubble.export.static.denyList`{.docutils .literal .notranslate}.

``` {#codecell12 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.denyList[0]='{"source_pod":["kube-system/"]}' \
   --set hubble.export.static.denyList[1]='{"destination_pod":["kube-system/"]}'
```

Copy First Line Copy All

``` {#codecell13 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.static.enabled=true \
   --set hubble.export.static.denyList[0]='{"source_pod":["kube-system/"]}' \
   --set hubble.export.static.denyList[1]='{"destination_pod":["kube-system/"]}'
```

Copy First Line Copy All

### Field mask[](#field-mask "Link to this heading")

Field mask can't be generated with `hubble`{.docutils .literal .notranslate}. Field mask is a list of field names from the [flow proto](https://github.com/cilium/cilium/blob/main/api/v1/flow/flow.proto) definition.

Examples include:

> -   To keep all information except pod labels:
>
>     ``` {#codecell14}
>     hubble-export-fieldmask: time source.identity source.namespace source.pod_name destination.identity destination.namespace destination.pod_name source_service destination_service l4 IP ethernet l7 Type node_name is_reply event_type verdict Summary
>     ```
>
>     Copy Line
>
> -   To keep only timestamp, verdict, ports, IP addresses, node name, pod name, and namespace:
>
>     ``` {#codecell15}
>     hubble-export-fieldmask: time source.namespace source.pod_name destination.namespace destination.pod_name l4 IP node_name is_reply verdict
>     ```
>
>     Copy Line

The following is a complete example of configuring Hubble Exporter.

> -   Configuration:
>
>     ``` {#codecell16 .literal-block}
>     helm upgrade cilium cilium/cilium --version 1.20.4 \
>        --namespace kube-system \
>        --set hubble.enabled=true \
>        --set hubble.export.static.enabled=true \
>        --set hubble.export.static.filePath=/var/run/cilium/hubble/events.log \
>        --set hubble.export.static.allowList[0]='{"verdict":["DROPPED","ERROR"]}' \
>        --set hubble.export.static.denyList[0]='{"source_pod":["kube-system/"]}' \
>        --set hubble.export.static.denyList[1]='{"destination_pod":["kube-system/"]}' \
>        --set "hubble.export.static.fieldMask={time,source.namespace,source.pod_name,destination.namespace,destination.pod_name,l4,IP,node_name,is_reply,verdict,drop_reason_desc}"
>     ```
>
>     Copy First Line Copy All
>
>     ``` {#codecell17 .literal-block}
>     helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
>        --namespace kube-system \
>        --set hubble.enabled=true \
>        --set hubble.export.static.enabled=true \
>        --set hubble.export.static.filePath=/var/run/cilium/hubble/events.log \
>        --set hubble.export.static.allowList[0]='{"verdict":["DROPPED","ERROR"]}' \
>        --set hubble.export.static.denyList[0]='{"source_pod":["kube-system/"]}' \
>        --set hubble.export.static.denyList[1]='{"destination_pod":["kube-system/"]}' \
>        --set "hubble.export.static.fieldMask={time,source.namespace,source.pod_name,destination.namespace,destination.pod_name,l4,IP,node_name,is_reply,verdict,drop_reason_desc}"
>     ```
>
>     Copy First Line Copy All
>
> -   Command:
>
>     ``` {#codecell18}
>     kubectl -n kube-system exec ds/cilium -- tail -f /var/run/cilium/hubble/events.log
>     ```
>
>     Copy Line
>
> -   Output:
>
>     ``` {#codecell19}
>     {"flow":{"time":"2023-08-21T12:12:13.517394084Z","verdict":"DROPPED","IP":{"source":"fe80::64d8:8aff:fe72:fc14","destination":"ff02::2","ipVersion":"IPv6"},"l4":{"ICMPv6":{"type":133}},"source":{},"destination":{},"node_name":"kind-kind/kind-worker","drop_reason_desc":"INVALID_SOURCE_IP"},"node_name":"kind-kind/kind-worker","time":"2023-08-21T12:12:13.517394084Z"}
>     {"flow":{"time":"2023-08-21T12:12:18.510175415Z","verdict":"DROPPED","IP":{"source":"10.244.1.60","destination":"10.244.1.5","ipVersion":"IPv4"},"l4":{"TCP":{"source_port":44916,"destination_port":80,"flags":{"SYN":true}}},"source":{"namespace":"default","pod_name":"xwing"},"destination":{"namespace":"default","pod_name":"deathstar-7848d6c4d5-th9v2"},"node_name":"kind-kind/kind-worker","drop_reason_desc":"POLICY_DENIED"},"node_name":"kind-kind/kind-worker","time":"2023-08-21T12:12:18.510175415Z"}
>     ```
>
>     Copy First Line Copy All

## Dynamic exporter configuration[](#dynamic-exporter-configuration "Link to this heading")

Standard hubble exporter configuration accepts only one set of filters and requires cilium pod restart to change config. Dynamic flow logs allow configuring multiple filters at the same time and saving output in separate files. Additionally it does not require cilium pod restarts to apply changed configuration.

**Dynamic Hubble Exporter** is enabled with Config Map property. It is disabled until you set a file path value for `hubble-flowlogs-config-path`{.docutils .literal .notranslate}.

Install cilium with dynamic exporter enabled:

``` {#codecell20 .literal-block}
helm install cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.dynamic.enabled=true
```

Copy First Line Copy All

``` {#codecell21 .literal-block}
helm install cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.dynamic.enabled=true
```

Copy First Line Copy All

Wait for `cilium`{.docutils .literal .notranslate} pod to become ready:

``` {#codecell22}
kubectl -n kube-system rollout status ds/cilium
```

Copy Line

You can change flow log settings without a need for pod to be restarted (changes should be reflected within 60s because of configmap propagation delay):

``` {#codecell23 .literal-block}
helm upgrade cilium cilium/cilium --version 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.dynamic.enabled=true \
   --set hubble.export.dynamic.config.content[0].name=system \
   --set hubble.export.dynamic.config.content[0].filePath=/var/run/cilium/hubble/events-system.log \
   --set hubble.export.dynamic.config.content[0].includeFilters[0].source_pod[0]='kube_system/' \
   --set hubble.export.dynamic.config.content[0].includeFilters[1].destination_pod[0]='kube_system/'
```

Copy First Line Copy All

``` {#codecell24 .literal-block}
helm upgrade cilium oci://quay.io/cilium/charts/cilium 1.20.4 \
   --namespace kube-system \
   --set hubble.enabled=true \
   --set hubble.export.dynamic.enabled=true \
   --set hubble.export.dynamic.config.content[0].name=system \
   --set hubble.export.dynamic.config.content[0].filePath=/var/run/cilium/hubble/events-system.log \
   --set hubble.export.dynamic.config.content[0].includeFilters[0].source_pod[0]='kube_system/' \
   --set hubble.export.dynamic.config.content[0].includeFilters[1].destination_pod[0]='kube_system/'
```

Copy First Line Copy All

Dynamic flow logs can be configured with `end`{.docutils .literal .notranslate} property which means that it will automatically stop logging after specified date time. It supports the same field masking and filtering as static hubble exporter.

File rotation is configured per flow log entry. Each entry accepts its own `fileMaxSizeMb`{.docutils .literal .notranslate}, `fileMaxBackups`{.docutils .literal .notranslate} and `fileCompress`{.docutils .literal .notranslate} settings. If an entry omits these settings, the defaults are used (`fileMaxSizeMb:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`10`{.docutils .literal .notranslate}, `fileMaxBackups:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`5`{.docutils .literal .notranslate}, `fileCompress:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`false`{.docutils .literal .notranslate}).

Sample dynamic flow logs configs:

``` {#codecell25}
hubble:
  export:
    dynamic:
      enabled: true
      config:
        enabled: true
        content:
        - name: "test001"
          filePath: "/var/run/cilium/hubble/test001.log"
          fieldMask: []
          includeFilters: []
          excludeFilters: []
          end: "2023-10-09T23:59:59-07:00"
        - name: "test002"
          filePath: "/var/run/cilium/hubble/test002.log"
          fieldMask: ["source.namespace", "source.pod_name", "destination.namespace", "destination.pod_name", "verdict"]
          fileMaxSizeMb: 100
          fileMaxBackups: 2
          fileCompress: true
          includeFilters:
          - source_pod: ["default/"]
            event_type:
            - type: 1
          - destination_pod: ["frontend/webserver-975996d4c-7hhgt"]
          excludeFilters: []
          end: "2023-10-09T23:59:59-07:00"
        - name: "test003"
          filePath: "/var/run/cilium/hubble/test003.log"
          fieldMask: ["source", "destination","verdict"]
          includeFilters: []
          excludeFilters:
          - destination_pod: ["ingress/"]
```

Copy First Line Copy All
