---
{"title": "HTTP Migration Example", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress-to-gateway/http-migration/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# HTTP Migration Example[](#http-migration-example "Link to this heading")

This example shows you how to migrate an existing Ingress configuration to the equivalent Gateway API resource.

The Cilium [Ingress HTTP Example](../../http/#gs-ingress-http) serves as the starting Ingress configuration. The same approach applies to other controllers, though each Ingress controller configuration varies.

The example Ingress configuration routes traffic to backend services from the `bookinfo`{.docutils .literal .notranslate} demo microservices app from the Istio project.

## Review Ingress Configuration[](#review-ingress-configuration "Link to this heading")

You can find the example Ingress definition in `basic-ingress.yaml`{.docutils .literal .notranslate}.

``` {#codecell0}
# Basic ingress for istio bookinfo demo application, which can be found in below
# https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: basic-ingress
  namespace: default
spec:
  ingressClassName: cilium
  rules:
  - http:
      paths:
      - backend:
          service:
            name: details
            port:
              number: 9080
        path: /details
        pathType: Prefix
      - backend:
          service:
            name: productpage
            port:
              number: 9080
        path: /
        pathType: Prefix
```

Copy First Line Copy All

This example listens for traffic on port 80, routes requests for the path `/details`{.docutils .literal .notranslate} to the `details`{.docutils .literal .notranslate} service, and `/`{.docutils .literal .notranslate} to the `productpage`{.docutils .literal .notranslate} service.

## Create Equivalent Gateway Configuration[](#create-equivalent-gateway-configuration "Link to this heading")

To create the equivalent Gateway configuration, consider the following:

-   Entry Point

The entry point is a combination of an IP address and port through which external clients access the data plane.

Every Ingress resource has two implicit entry points -- one for HTTP and the other for HTTPS traffic. An Ingress controller provides the entry points. Typically, entry points are either shared by all Ingress resources, or every Ingress resource has dedicated entry points.

``` {#codecell1}
apiVersion: networking.k8s.io/v1
kind: Ingress
spec:
  ingressClassName: cilium
```

Copy First Line Copy All

In the Gateway API, entry points must be explicitly defined in a Gateway resource. For example, for the data plane to handle HTTP traffic on port 80, you must define a listener for that traffic. Typically, a Gateway implementation provides a dedicated data plane for each Gateway resource.

``` {#codecell2}
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: cilium-gateway
spec:
  gatewayClassName: cilium
  listeners:
  - name: http
    port: 80
    protocol: HTTP
```

Copy First Line Copy All

-   Routing Rules

When using Ingress or Gateway API, routing rules must be defined to attach applications to those entry points.

The path-based routing rules are configured in the Ingress resource.

In the Ingress resource, each hostname has separate routing rules:

``` {#codecell3}
apiVersion: networking.k8s.io/v1
kind: Ingress
[...]
rules:
- http:
    paths:
    - backend:
        service:
          name: details
          port:
            number: 9080
      path: /details
      pathType: Prefix
    - backend:
        service:
          name: productpage
          port:
            number: 9080
      path: /
      pathType: Prefix
```

Copy First Line Copy All

The routing rules are configured in the HTTPRoute.

``` {#codecell4}
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
spec:
  parentRefs:
  - name: cilium-gateway
rules:
- matches:
  - path:
      type: PathPrefix
      value: /
  backendRefs:
  - name: productpage
    port: 9080
- matches:
  - path:
      type: PathPrefix
      value: /details
  backendRefs:
  - name: details
    port: 9080
```

Copy First Line Copy All

-   Selecting Data Plane to Attach to:

Both Ingress and Gateway API resources must be explicitly attached to a Dataplane.

An Ingress resource must specify a class that selects which Ingress controller to use.

``` {#codecell5}
apiVersion: networking.k8s.io/v1
kind: Ingress
spec:
  ingressClassName: cilium
```

Copy First Line Copy All

A Gateway resource must also specify a class: in this example, it is always the `cilium`{.docutils .literal .notranslate} class. An HTTPRoute must specify which Gateway (or Gateways) to attach to via a `parentRef`{.docutils .literal .notranslate}.

``` {#codecell6}
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: cilium-gateway
  namespace: default
spec:
  gatewayClassName: cilium
[...]
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
spec:
  parentRefs:
  - name: cilium-gateway
```

Copy First Line Copy All

## Review Equivalent Gateway Configuration[](#review-equivalent-gateway-configuration "Link to this heading")

You can find the equivalent final Gateway and HTTPRoute definition in `http-migration.yaml`{.docutils .literal .notranslate}.

``` {#codecell7}
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: cilium-gateway
  namespace: default
spec:
  gatewayClassName: cilium
  listeners:
  - name: http
    port: 80
    protocol: HTTP
---
apiVersion: gateway.networking.k8s.io/v1beta1
kind: HTTPRoute
metadata:
  name: all-hosts
  namespace: default
spec:
  parentRefs:
  - name: cilium-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: productpage
      port: 9080
  - matches:
    - path:
        type: PathPrefix
        value: /details
    backendRefs:
    - name: details
      port: 9080
```

Copy First Line Copy All

The preceding example creates a Gateway named `cilium-gateway`{.docutils .literal .notranslate} that listens on port 80 for HTTP traffic. Two routes are defined, one for `/details`{.docutils .literal .notranslate} to the `details`{.docutils .literal .notranslate} service, and one for `/`{.docutils .literal .notranslate} to the `productpage`{.docutils .literal .notranslate} service.

Deploy the resources and verify that the HTTP requests are routed successfully to the services. For more information, consult the Gateway API [HTTP Example](../../gateway-api/http/#gs-gateway-http).
