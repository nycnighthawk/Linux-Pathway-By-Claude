---
{"title": "Access Logs", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/access-logs/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Access Logs[](#access-logs "Link to this heading")

This example builds on the previous [HTTP Example](../http/#gs-gateway-http) and configures [Envoy access logs](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage) for Gateways managed by Cilium Gateway API.

Access logging is managed via the `spec.telemetry.accessLogs`{.docutils .literal .notranslate} field within a `CiliumGatewayClassConfig`{.docutils .literal .notranslate} resource. Since this configuration is referenced by `GatewayClass`{.docutils .literal .notranslate} resource via `spec.parametersRef`{.docutils .literal .notranslate}, any settings you define here will automatically apply to all Gateways using that specific Gateway Class.

Cilium configures Envoy to write access logs to stdout.

## Configuration Options[](#configuration-options "Link to this heading")

When configuring access logs, the `format`{.docutils .literal .notranslate} field is required. You can customize the log output using the following parameters:

-   `format`{.docutils .literal .notranslate} (Required): Defines the log output type. Supported values are `Text`{.docutils .literal .notranslate} or `JSON`{.docutils .literal .notranslate}.

-   `text`{.docutils .literal .notranslate} (Optional): A custom Envoy text format string. If you select `format:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`Text`{.docutils .literal .notranslate} but leave this field empty, Cilium falls back to the [default Envoy text format](https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage#default-format-string).

-   `json`{.docutils .literal .notranslate} (Optional): A key-value map linking your custom JSON field names to Envoy format operators. If you select `format:`{.docutils .literal .notranslate}` `{.docutils .literal .notranslate}`JSON`{.docutils .literal .notranslate} but leave this field empty, Cilium applies a pre-configured JSON template that mirrors the information from the default Envoy text format.

    Note

    This default JSON mapping is provided by Cilium, not by Envoy's built-in defaults.

-   `targets`{.docutils .literal .notranslate} (Optional): Specifies the traffic type to log. Supported values are `HTTP`{.docutils .literal .notranslate} and `TCP`{.docutils .literal .notranslate} (which includes TLS passthrough). If omitted, Cilium defaults to logging `HTTP`{.docutils .literal .notranslate} traffic only.

## Custom Cilium formatters[](#custom-cilium-formatters "Link to this heading")

In addition to standard Envoy operators, Cilium provides two Gateway-specific formatters to help you identify the source of the traffic:

-   `%CILIUM_GATEWAY_NAMESPACE%`{.docutils .literal .notranslate} resolves to the namespace of the Gateway.

-   `%CILIUM_GATEWAY_NAME%`{.docutils .literal .notranslate} resolves to the name of the Gateway.

For a complete list of all other available format operators, please refer to the official Envoy access log substitution [formatter documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/advanced/substitution_formatter).

## Deploy a Gateway with access logs[](#deploy-a-gateway-with-access-logs "Link to this heading")

Create a `CiliumGatewayClassConfig`{.docutils .literal .notranslate} that enables JSON access logs for HTTP traffic:

``` {#codecell0}
apiVersion: cilium.io/v2alpha1
kind: CiliumGatewayClassConfig
metadata:
  name: cilium
  namespace: default
spec:
  telemetry:
    accessLogs:
    - format: JSON
      json:
        gateway: "%CILIUM_GATEWAY_NAMESPACE%/%CILIUM_GATEWAY_NAME%"
        start_time: "%START_TIME%"
        method: "%REQUEST_HEADER(:METHOD)%"
        path: "%REQUEST_HEADER(X-ENVOY-ORIGINAL-PATH?:PATH)%"
        protocol: "%PROTOCOL%"
        response_code: "%RESPONSE_CODE%"
        response_flags: "%RESPONSE_FLAGS%"
        bytes_received: "%BYTES_RECEIVED%"
        bytes_sent: "%BYTES_SENT%"
        duration: "%DURATION%"
        authority: "%REQUEST_HEADER(:AUTHORITY)%"
        upstream_host: "%UPSTREAM_HOST%"
```

Copy First Line Copy All

Update the `GatewayClass`{.docutils .literal .notranslate} to reference the `CiliumGatewayClassConfig`{.docutils .literal .notranslate} resource:

``` {#codecell1}
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: cilium
spec:
  controllerName: io.cilium/gateway-controller
  parametersRef:
    group: cilium.io
    kind: CiliumGatewayClassConfig
    name: cilium
    namespace: default
```

Copy First Line Copy All

Verify that the GatewayClass configuration is accepted:

``` {#codecell2}
$ kubectl get ciliumgatewayclassconfig cilium
NAME     ACCEPTED   AGE
cilium   True       33s
```

Copy First Line Copy Commands Copy All

Send a request through the Gateway:

``` {#codecell3}
$ GATEWAY=$(kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}')
$ curl --fail -s http://"$GATEWAY"/details/1 | jq
```

Copy First Line Copy Commands Copy All

## Verify access logs[](#verify-access-logs "Link to this heading")

Check the Envoy stdout logs for an access log entry that contains the Gateway namespace and name.

``` {#codecell4}
$ kubectl -n kube-system logs -l app.kubernetes.io/name=cilium-envoy,app.kubernetes.io/part-of=cilium | grep default/my-gateway
{"authority":"172.18.255.193","bytes_received":0,"bytes_sent":178,"duration":8,"gateway":"default/my-gateway","method":"GET","path":"/details/1","protocol":"HTTP/1.1","response_code":200,"response_flags":"-","start_time":"2026-07-06T10:10:13.622Z","upstream_host":"10.244.0.221:9080"}
```

Copy First Line Copy Commands Copy All

## Log HTTP and TCP traffic[](#log-http-and-tcp-traffic "Link to this heading")

To emit access logs for both HTTP and TCP proxy traffic, set both targets:

``` {#codecell5}
spec:
  telemetry:
    accessLogs:
    - format: Text
      text: '[%START_TIME%] %CILIUM_GATEWAY_NAMESPACE%/%CILIUM_GATEWAY_NAME% "%REQUEST_HEADER(:METHOD)% %REQUEST_HEADER(X-ENVOY-ORIGINAL-PATH?:PATH)% %PROTOCOL%" %RESPONSE_CODE% %DURATION%'
      targets:
      - HTTP
      - TCP
```

Copy First Line Copy All

Multiple access log entries may use the same target. Envoy emits one log entry for each matching configuration, so duplicate configurations will produce duplicate log lines.
