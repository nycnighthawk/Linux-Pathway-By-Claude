---
{"title": "GatewayClass Parameters Support", "url": "https://docs.cilium.io/en/stable/network/servicemesh/gateway-api/parameterized-gatewayclass/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# GatewayClass Parameters Support[](#gatewayclass-parameters-support "Link to this heading")

The default behavior of Gateway API can be modified by providing parameters to the GatewayClass. The parameters are defined in the GatewayClass and can be referenced in the Gateway object. The GatewayClass parameters are defined in the `CiliumGatewayClassConfig`{.docutils .literal .notranslate} CRD.

The demo application is from the `bookinfo`{.docutils .literal .notranslate} demo microservices app from the Istio project.

## Deploy the Demo App[](#deploy-the-demo-app "Link to this heading")

``` {#codecell0}
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
```

Copy Line

This is just deploying the demo app, it's not adding any Istio components. You can confirm that with Cilium Service Mesh there is no Envoy sidecar created alongside each of the demo app microservices.

``` {#codecell1}
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-5498c86cf5-kjzkj       1/1     Running   0          2m39s
productpage-v1-65b75f6885-ff59g   1/1     Running   0          2m39s
ratings-v1-b477cf6cf-kv7bh        1/1     Running   0          2m39s
reviews-v1-79d546878f-r5bjz       1/1     Running   0          2m39s
reviews-v2-548c57f459-pld2f       1/1     Running   0          2m39s
reviews-v3-6dd79655b9-nhrnh       1/1     Running   0          2m39s
```

Copy First Line Copy Commands Copy All

Note

With the sidecar implementation the output would show 2/2 READY. One for the microservice and one for the Envoy sidecar.

## Deploy the Cilium Gateway with customized parameters[](#deploy-the-cilium-gateway-with-customized-parameters "Link to this heading")

In this example, we will deploy a Cilium Gateway with `NodePort`{.docutils .literal .notranslate} service instead of the default `LoadBalancer`{.docutils .literal .notranslate} type.

``` {#codecell2}
---
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nodeport-gateway-class
spec:
  controllerName: io.cilium/gateway-controller
  description: The default Cilium GatewayClass
  parametersRef:
    group: cilium.io
    kind: CiliumGatewayClassConfig
    name: nodeport-gateway-config
    namespace: default
---
apiVersion: cilium.io/v2alpha1
kind: CiliumGatewayClassConfig
metadata:
  name: nodeport-gateway-config
  namespace: default
spec:
  service:
    type: NodePort
---
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: nodeport-gateway
spec:
  gatewayClassName: nodeport-gateway-class
  listeners:
  - protocol: HTTP
    port: 80
    name: web-gw
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-app-1
spec:
  parentRefs:
  - name: nodeport-gateway
    namespace: default
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /details
    backendRefs:
    - name: details
      port: 9080
```

Copy First Line Copy All

Apply the configuration:

``` {#codecell3 .literal-block}
$ kubectl apply -f https://raw.githubusercontent.com/cilium/cilium/1.20.4/examples/kubernetes/gateway/gateway-with-parameters.yaml
```

Copy Line

Once the Gateway is deployed, you can access the service using via NodePort service.

``` {#codecell4}
$ kubectl  services cilium-gateway-nodeport-gateway
NAME                              TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
cilium-gateway-nodeport-gateway   NodePort   10.96.45.118   <none>        80:30493/TCP   11s

# Sending some traffic to nodeport service, after ssh to one of the kubernetes node
root@kind-worker:/# curl http://localhost:30493/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}root@kind-worker:/#
```

Copy First Line Copy Commands Copy All

## Disable gRPC-web translation[](#disable-grpc-web-translation "Link to this heading")

Cilium Gateway API enables Envoy's gRPC-web to gRPC request translation by default. To pass gRPC-web requests through unchanged for all Gateways using a parameterized GatewayClass, set `httpOptions.grpcWebTranslation.enabled`{.docutils .literal .notranslate} to `false`{.docutils .literal .notranslate} in the `CiliumGatewayClassConfig`{.docutils .literal .notranslate}:

``` {#codecell5}
apiVersion: cilium.io/v2alpha1
kind: CiliumGatewayClassConfig
metadata:
  name: grpc-web
  namespace: default
spec:
  httpOptions:
    grpcWebTranslation:
      enabled: false
```

Copy First Line Copy All

## Server header transformations[](#server-header-transformations "Link to this heading")

Cilium Gateway API allows for controlling server response headers. Using Envoy's `ServerHeaderTransformation`{.docutils .literal .notranslate}, header server manipulations can be:

-   `OVERWRITE`{.docutils .literal .notranslate} (default)

-   `APPEND_IF_ABSENT`{.docutils .literal .notranslate}

-   `PASS_THROUGH`{.docutils .literal .notranslate}

Here is an example `CiliumGatewayClassConfig`{.docutils .literal .notranslate} with `ServerHeaderTransformation`{.docutils .literal .notranslate} set to `PASS_THROUGH`{.docutils .literal .notranslate}:

``` {#codecell6}
apiVersion: cilium.io/v2alpha1
kind: CiliumGatewayClassConfig
metadata:
  name: test-gateway-config
  namespace: default
spec:
  envoy:
    serverHeaderTransformation: PASS_THROUGH
```

Copy First Line Copy All

## Reference[](#reference "Link to this heading")

The full list of supported parameters can be found in the `CiliumGatewayClassConfig`{.docutils .literal .notranslate} CRD.

Warning

The `CiliumGatewayClassConfig`{.docutils .literal .notranslate} CRD is an alpha API, and per the standard Kubernetes object versioning, is subject to breaking changes. If you use it, please read the release notes carefully in case there are breaking changes. Please also consider reporting both your usage of the CRD and any issues either on Github or in Slack.

``` {#codecell7}
---
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.20.1
  name: ciliumgatewayclassconfigs.cilium.io
spec:
  group: cilium.io
  names:
    categories:
    - cilium
    kind: CiliumGatewayClassConfig
    listKind: CiliumGatewayClassConfigList
    plural: ciliumgatewayclassconfigs
    shortNames:
    - cgcc
    singular: ciliumgatewayclassconfig
  scope: Namespaced
  versions:
  - additionalPrinterColumns:
    - jsonPath: .status.conditions[?(@.type=="Accepted")].status
      name: Accepted
      type: string
    - jsonPath: .metadata.creationTimestamp
      name: Age
      type: date
    - jsonPath: .spec.description
      name: Description
      priority: 1
      type: string
    name: v2alpha1
    schema:
      openAPIV3Schema:
        description: |-
          CiliumGatewayClassConfig is a Kubernetes third-party resource which
          is used to configure Gateways owned by GatewayClass.
        properties:
          apiVersion:
            description: |-
              APIVersion defines the versioned schema of this representation of an object.
              Servers should convert recognized schemas to the latest internal value, and
              may reject unrecognized values.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            type: string
          kind:
            description: |-
              Kind is a string value representing the REST resource this object represents.
              Servers may infer this from the endpoint the client submits requests to.
              Cannot be updated.
              In CamelCase.
              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            type: string
          metadata:
            type: object
          spec:
            description: Spec is a human-readable of a GatewayClass configuration.
            properties:
              description:
                description: Description helps describe a GatewayClass configuration
                  with more details.
                maxLength: 64
                type: string
              envoy:
                description: |-
                  Envoy specifies proxy configuration options.
                  These settings control Envoy-specific behavior that is not part of the Gateway API standard.
                properties:
                  serverHeaderTransformation:
                    default: OVERWRITE
                    description: |-
                      ServerHeaderTransformation controls the HTTP "Server" response header.
                      Defaults to OVERWRITE.
                    enum:
                    - OVERWRITE
                    - APPEND_IF_ABSENT
                    - PASS_THROUGH
                    type: string
                type: object
              httpOptions:
                description: HTTPOptions specifies HTTP connection manager options.
                properties:
                  grpcWebTranslation:
                    description: GRPCWebTranslation controls Envoy's gRPC-web to gRPC
                      request translation.
                    properties:
                      enabled:
                        default: true
                        description: Enabled controls Envoy's gRPC-web to gRPC request
                          translation.
                        type: boolean
                    type: object
                type: object
              service:
                description: |-
                  Service specifies the configuration for the generated Service.
                  Note that not all fields from upstream Service.Spec are supported
                properties:
                  allocateLoadBalancerNodePorts:
                    description: Sets the Service.Spec.AllocateLoadBalancerNodePorts
                      in generated Service objects to the given value.
                    type: boolean
                  externalTrafficPolicy:
                    default: Cluster
                    description: Sets the Service.Spec.ExternalTrafficPolicy in generated
                      Service objects to the given value.
                    type: string
                  ipFamilies:
                    description: Sets the Service.Spec.IPFamilies in generated Service
                      objects to the given value.
                    items:
                      description: |-
                        IPFamily represents the IP Family (IPv4 or IPv6). This type is used
                        to express the family of an IP expressed by a type (e.g. service.spec.ipFamilies).
                      type: string
                    type: array
                    x-kubernetes-list-type: atomic
                  ipFamilyPolicy:
                    description: Sets the Service.Spec.IPFamilyPolicy in generated
                      Service objects to the given value.
                    type: string
                  loadBalancerClass:
                    description: Sets the Service.Spec.LoadBalancerClass in generated
                      Service objects to the given value.
                    type: string
                  loadBalancerSourceRanges:
                    description: Sets the Service.Spec.LoadBalancerSourceRanges in
                      generated Service objects to the given value.
                    items:
                      type: string
                    type: array
                    x-kubernetes-list-type: atomic
                  loadBalancerSourceRangesPolicy:
                    default: Allow
                    description: |-
                      LoadBalancerSourceRangesPolicy defines the policy for the LoadBalancerSourceRanges if the incoming traffic
                      is allowed or denied.
                    enum:
                    - Allow
                    - Deny
                    type: string
                  trafficDistribution:
                    description: Sets the Service.Spec.TrafficDistribution in generated
                      Service objects to the given value.
                    type: string
                  type:
                    default: LoadBalancer
                    description: |-
                      Sets the Service.Spec.Type in generated Service objects to the given value.
                      Only LoadBalancer and NodePort are supported.
                    enum:
                    - LoadBalancer
                    - NodePort
                    type: string
                type: object
              telemetry:
                description: |-
                  Telemetry specifies observability options for Gateways using this
                  GatewayClass configuration.
                properties:
                  accessLogs:
                    description: |-
                      AccessLogs configures Envoy access logging for generated Gateway
                      listeners.
                    items:
                      description: |-
                        AccessLogs defines an Envoy access log configuration, including its output
                        format and the generated proxy components that should emit it.
                        Access logs are currently written to Envoy stdout.
                      properties:
                        format:
                          description: Format specifies the access log output format.
                          enum:
                          - JSON
                          - Text
                          type: string
                        json:
                          additionalProperties:
                            type: string
                          default:
                            authority: '%REQUEST_HEADER(:AUTHORITY)%'
                            bytes_received: '%BYTES_RECEIVED%'
                            bytes_sent: '%BYTES_SENT%'
                            duration: '%DURATION%'
                            method: '%REQUEST_HEADER(:METHOD)%'
                            path: '%REQUEST_HEADER(X-ENVOY-ORIGINAL-PATH?:PATH)%'
                            protocol: '%PROTOCOL%'
                            request_id: '%REQUEST_HEADER(X-REQUEST-ID)%'
                            response_code: '%RESPONSE_CODE%'
                            response_flags: '%RESPONSE_FLAGS%'
                            start_time: '%START_TIME%'
                            upstream_host: '%UPSTREAM_HOST%'
                            upstream_service_time: '%RESPONSE_HEADER(X-ENVOY-UPSTREAM-SERVICE-TIME)%'
                            user_agent: '%REQUEST_HEADER(USER-AGENT)%'
                            x_forwarded_for: '%REQUEST_HEADER(X-FORWARDED-FOR)%'
                          description: |-
                            JSON maps access log field names to Envoy command operators.
                            It is used when Format is "JSON".
                            For available format specifiers, see the Envoy documentation:
                            - https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage
                            Note: Always refer to the documentation matching the specific Envoy version you are running.
                            The following Cilium-specific formatters are also supported:
                            - %CILIUM_GATEWAY_NAME% -- replaced with the Gateway resource name.
                            - %CILIUM_GATEWAY_NAMESPACE% -- replaced with the Gateway resource namespace.
                          maxProperties: 64
                          minProperties: 1
                          type: object
                        targets:
                          default:
                          - HTTP
                          description: |-
                            Targets specifies the generated Envoy proxy components where access logs
                            are emitted. If omitted, access logs are emitted for HTTP traffic only.
                            HTTP targets Envoy HTTP connection managers. TCP targets Envoy TCP proxies,
                            including TLS passthrough.
                          items:
                            description: AccessLogsTarget specifies where access logs
                              are emitted.
                            enum:
                            - HTTP
                            - TCP
                            type: string
                          minItems: 1
                          type: array
                          x-kubernetes-list-type: set
                        text:
                          default: '[%START_TIME%] "%REQUEST_HEADER(:METHOD)% %REQUEST_HEADER(X-ENVOY-ORIGINAL-PATH?:PATH)%
                            %PROTOCOL%" %RESPONSE_CODE% %RESPONSE_FLAGS% %BYTES_RECEIVED%
                            %BYTES_SENT% %DURATION% %RESPONSE_HEADER(X-ENVOY-UPSTREAM-SERVICE-TIME)%
                            "%REQUEST_HEADER(X-FORWARDED-FOR)%" "%REQUEST_HEADER(USER-AGENT)%"
                            "%REQUEST_HEADER(X-REQUEST-ID)%" "%REQUEST_HEADER(:AUTHORITY)%"
                            "%UPSTREAM_HOST%"'
                          description: |-
                            Text specifies the Envoy access log format string.
                            It is used when Format is "Text".
                            For available format specifiers, see the Envoy documentation:
                            - https://www.envoyproxy.io/docs/envoy/latest/configuration/observability/access_log/usage
                            Note: Always refer to the documentation matching the specific Envoy version you are running.
                            The following Cilium-specific formatters are also supported:
                            - %CILIUM_GATEWAY_NAME% -- replaced with the Gateway resource name.
                            - %CILIUM_GATEWAY_NAMESPACE% -- replaced with the Gateway resource namespace.
                          maxLength: 4096
                          minLength: 1
                          type: string
                      required:
                      - format
                      type: object
                    maxItems: 8
                    minItems: 1
                    type: array
                type: object
            type: object
          status:
            description: Status is the status of the policy.
            properties:
              conditions:
                description: Current service state
                items:
                  description: Condition contains details for one aspect of the current
                    state of this API Resource.
                  properties:
                    lastTransitionTime:
                      description: |-
                        lastTransitionTime is the last time the condition transitioned from one status to another.
                        This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
                      format: date-time
                      type: string
                    message:
                      description: |-
                        message is a human readable message indicating details about the transition.
                        This may be an empty string.
                      maxLength: 32768
                      type: string
                    observedGeneration:
                      description: |-
                        observedGeneration represents the .metadata.generation that the condition was set based upon.
                        For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
                        with respect to the current state of the instance.
                      format: int64
                      minimum: 0
                      type: integer
                    reason:
                      description: |-
                        reason contains a programmatic identifier indicating the reason for the condition's last transition.
                        Producers of specific condition types may define expected values and meanings for this field,
                        and whether the values are considered a guaranteed API.
                        The value should be a CamelCase string.
                        This field may not be empty.
                      maxLength: 1024
                      minLength: 1
                      pattern: ^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$
                      type: string
                    status:
                      description: status of the condition, one of True, False, Unknown.
                      enum:
                      - "True"
                      - "False"
                      - Unknown
                      type: string
                    type:
                      description: type of condition in CamelCase or in foo.example.com/CamelCase.
                      maxLength: 316
                      pattern: ^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$
                      type: string
                  required:
                  - lastTransitionTime
                  - message
                  - reason
                  - status
                  - type
                  type: object
                type: array
                x-kubernetes-list-map-keys:
                - type
                x-kubernetes-list-type: map
            type: object
        required:
        - metadata
        type: object
    served: true
    storage: true
    subresources:
      status: {}
```

Copy First Line Copy All
